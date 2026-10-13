import { identityKey, ownIdentity, openStorageDatabase, verifyEntries, JournalIntegrityError,
  type JournalIdentity, type JournalEntry } from "./journal.js";

/** Host-negotiated application protocol, not a Yjs sync event or state vector. */
export const durableReceiptProtocol = "editac-durable-receipt-v1";
export interface DurableReceipt {
  protocol: typeof durableReceiptProtocol;
  state: "durable";
  identity: JournalIdentity;
  writerId: number;
  sequence: number;
  checksum: string;
  updateId: string;
}
export interface ReceiptResult {
  state: "remoteCommitted" | "ignored";
  updateId: string;
  reason?: "capability-unavailable" | "unknown-update" | "identity-mismatch";
}

function ownReceipt(input: DurableReceipt): DurableReceipt {
  const identity = ownIdentity(input?.identity);
  if (input.protocol !== durableReceiptProtocol || input.state !== "durable"
    || !Number.isSafeInteger(input.writerId) || input.writerId <= 0
    || !Number.isSafeInteger(input.sequence) || input.sequence <= 0
    || typeof input.updateId !== "string" || !input.updateId
    || typeof input.checksum !== "string" || !/^[a-f0-9]{64}$/.test(input.checksum)) {
    throw new JournalIntegrityError("Invalid durable application receipt");
  }
  return { protocol: input.protocol, state: input.state, identity, writerId: input.writerId,
    sequence: input.sequence, checksum: input.checksum, updateId: input.updateId };
}
function matches(receipt: DurableReceipt, entry: JournalEntry): boolean {
  return receipt.updateId === entry.updateId && receipt.checksum === entry.checksum
    && receipt.writerId === entry.writerId && receipt.sequence === entry.sequence
    && identityKey(receipt.identity) === identityKey(entry.identity);
}

/** Internal adapter. Receipts prune pending membership, never the journal's recovery tail.
 * The host passes only receipts from its negotiated durable application transport.
 * Existing v1/v2 journals are pending by default; upgrading does not infer acknowledgments.
 */
export class UpdateOutbox {
  private constructor(private readonly database: IDBDatabase, readonly receiptProtocol: typeof durableReceiptProtocol | null) {}
  static async open(factory: IDBFactory, name = "editac-local-storage",
    receiptProtocol: typeof durableReceiptProtocol | null = null): Promise<UpdateOutbox> {
    if (receiptProtocol !== null && receiptProtocol !== durableReceiptProtocol) throw new JournalIntegrityError("Unsupported receipt capability");
    return new UpdateOutbox(await openStorageDatabase(factory, name), receiptProtocol);
  }
  close(): void { this.database.close(); }

  /** One snapshot of committed bytes and durable receipt markers, independent of checkpoints. */
  async pending(identity: JournalIdentity): Promise<JournalEntry[]> {
    const expected = ownIdentity(identity);
    const raw = await new Promise<{ entries: JournalEntry[]; receipts: Map<string, DurableReceipt> }>((resolve, reject) => {
      const tx = this.database.transaction(["updates", "receipts"], "readonly");
      let entries: JournalEntry[] = [];
      const receipts = new Map<string, DurableReceipt>();
      tx.oncomplete = () => resolve({ entries, receipts });
      tx.onabort = () => reject(tx.error ?? new DOMException("Outbox read aborted", "AbortError"));
      const request = tx.objectStore("updates").index("documentEpochSchema").getAll([expected.documentId, expected.epoch, expected.schema]);
      request.onsuccess = () => {
        entries = request.result as JournalEntry[];
        for (const entry of entries) {
          const receipt = tx.objectStore("receipts").get(entry.updateId);
          receipt.onsuccess = () => { if (receipt.result !== undefined) receipts.set(entry.updateId, receipt.result as DurableReceipt); };
        }
      };
    });
    const entries = await verifyEntries(raw.entries, expected);
    return entries.filter(entry => {
      const marker = raw.receipts.get(entry.updateId);
      if (!marker) return true;
      const receipt = ownReceipt(marker);
      if (!matches(receipt, entry)) throw new JournalIntegrityError("Stored receipt identity mismatch");
      return false;
    });
  }

  /** Remote acknowledgment becomes visible only after the local receipt transaction completes. */
  async accept(input: DurableReceipt): Promise<ReceiptResult> {
    const receipt = ownReceipt(input);
    if (this.receiptProtocol === null) return { state: "ignored", updateId: receipt.updateId, reason: "capability-unavailable" };
    let tx: IDBTransaction;
    try { tx = this.database.transaction(["updates", "receipts"], "readwrite", { durability: "strict" }); }
    catch (error) {
      if (!(error instanceof TypeError) && !(error instanceof DOMException && error.name === "NotSupportedError")) throw error;
      tx = this.database.transaction(["updates", "receipts"], "readwrite");
    }
    return new Promise((resolve, reject) => {
      let failure: unknown;
      let result: ReceiptResult = { state: "ignored", updateId: receipt.updateId, reason: "unknown-update" };
      tx.oncomplete = () => resolve(result);
      tx.onabort = () => reject(failure ?? tx.error ?? new DOMException("Receipt transaction aborted", "AbortError"));
      tx.onerror = () => { failure ??= tx.error; };
      const abort = (error: unknown) => { failure = error; try { tx.abort(); } catch { reject(error); } };
      try {
        const request = tx.objectStore("updates").get([receipt.identity.documentId, receipt.identity.epoch,
          receipt.identity.schema, receipt.writerId, receipt.sequence]);
        request.onerror = () => { failure = request.error; };
        request.onsuccess = () => {
          try {
            const entry = request.result as JournalEntry | undefined;
            if (entry === undefined) return;
            if (!matches(receipt, entry)) { result.reason = "identity-mismatch"; return; }
            const write = tx.objectStore("receipts").put(receipt, receipt.updateId);
            write.onerror = () => { failure = write.error; };
            result = { state: "remoteCommitted", updateId: receipt.updateId };
          } catch (error) { abort(error); }
        };
      } catch (error) { abort(error); }
    });
  }
}
