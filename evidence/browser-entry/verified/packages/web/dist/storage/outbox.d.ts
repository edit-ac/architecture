import { type JournalIdentity, type JournalEntry } from "./journal.js";
/** Host-negotiated application protocol, not a Yjs sync event or state vector. */
export declare const durableReceiptProtocol = "editac-durable-receipt-v1";
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
/** Internal adapter. Receipts prune pending membership, never the journal's recovery tail.
 * The host passes only receipts from its negotiated durable application transport.
 * Existing v1/v2 journals are pending by default; upgrading does not infer acknowledgments.
 */
export declare class UpdateOutbox {
    private readonly database;
    readonly receiptProtocol: typeof durableReceiptProtocol | null;
    private constructor();
    static open(factory: IDBFactory, name?: string, receiptProtocol?: typeof durableReceiptProtocol | null): Promise<UpdateOutbox>;
    close(): void;
    /** One snapshot of committed bytes and durable receipt markers, independent of checkpoints. */
    pending(identity: JournalIdentity): Promise<JournalEntry[]>;
    /** Remote acknowledgment becomes visible only after the local receipt transaction completes. */
    accept(input: DurableReceipt): Promise<ReceiptResult>;
}
