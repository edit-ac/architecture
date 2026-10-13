import { checksum, identityKey, ownIdentity, openStorageDatabase, verifyEntries, JournalIntegrityError } from "./journal.js";
export class CheckpointConflictError extends Error {
    constructor() { super("Concurrent checkpoint publication; retry from current storage"); this.name = "CheckpointConflictError"; }
}
const publicationVersion = (p) => JSON.stringify([p.revision, p.latest?.manifestHash, p.previous?.manifestHash]);
const scope = (identity) => [identity.documentId, identity.epoch, identity.schema];
const key = (identity) => JSON.stringify(scope(identity));
function ownCheckpoint(input) {
    const identity = ownIdentity(input.identity);
    if (input.initialized !== true || !Number.isSafeInteger(input.writerId) || input.writerId <= 0
        || !(input.bytes instanceof Uint8Array) || !input.bytes.length)
        throw new JournalIntegrityError("Invalid CRDT checkpoint");
    return { identity, initialized: true, writerId: input.writerId, bytes: new Uint8Array(input.bytes) };
}
async function manifest(record) {
    return checksum(new TextEncoder().encode(JSON.stringify([record.version, identityKey(record.checkpoint.identity),
        record.checkpoint.initialized, record.checkpoint.writerId, record.checksum, record.coverage])));
}
async function validate(record, expected) {
    if (record.version !== 1 || !Array.isArray(record.coverage) || record.coverage.some(id => typeof id !== "string")
        || new Set(record.coverage).size !== record.coverage.length)
        throw new JournalIntegrityError("Unsupported checkpoint version/coverage");
    const checkpoint = ownCheckpoint(record.checkpoint);
    if (identityKey(checkpoint.identity) !== identityKey(expected))
        throw new JournalIntegrityError("Checkpoint identity mismatch");
    if (await checksum(checkpoint.bytes) !== record.checksum || await manifest(record) !== record.manifestHash)
        throw new JournalIntegrityError("Corrupt checkpoint bytes or coverage");
    return { ...record, checkpoint, coverage: [...record.coverage] };
}
/** Internal browser adapter. Retains all journal/outbox bytes; compaction requires later receipt policy. */
export class CheckpointStorage {
    database;
    constructor(database) {
        this.database = database;
    }
    static async open(factory, name = "editac-local-storage") {
        return new CheckpointStorage(await openStorageDatabase(factory, name));
    }
    close() { this.database.close(); }
    readRaw(identity) {
        return new Promise((resolve, reject) => {
            const tx = this.database.transaction(["checkpoints", "updates"], "readonly");
            let publication = {}, entries = [];
            tx.oncomplete = () => resolve({ publication, entries });
            tx.onabort = () => reject(tx.error ?? new DOMException("Checkpoint read aborted", "AbortError"));
            const point = tx.objectStore("checkpoints").get(key(identity));
            point.onsuccess = () => { publication = point.result ?? {}; };
            const tail = tx.objectStore("updates").index("documentEpochSchema").getAll(scope(identity));
            tail.onsuccess = () => { entries = tail.result; };
        });
    }
    /** The host captures coverage from the same engine state as bytes. Publication acknowledges only completion. */
    async publish(input, coveredUpdateIds) {
        const checkpoint = ownCheckpoint(input);
        const coverage = [...coveredUpdateIds];
        if (coverage.some(id => typeof id !== "string") || new Set(coverage).size !== coverage.length)
            throw new JournalIntegrityError("Invalid checkpoint coverage");
        const raw = await this.readRaw(checkpoint.identity);
        const entries = await verifyEntries(raw.entries, checkpoint.identity);
        const ids = new Set(entries.map(e => e.updateId));
        if (coverage.some(id => !ids.has(id)))
            throw new JournalIntegrityError("Checkpoint covers an uncommitted or foreign update");
        // Validate retained fallback before starting the write transaction (no async work inside IDB transaction).
        let previous;
        for (const candidate of [raw.publication.latest, raw.publication.previous]) {
            if (!candidate)
                continue;
            try {
                previous = await validate(candidate, checkpoint.identity);
                break;
            }
            catch { /* keep searching */ }
        }
        const base = { version: 1, checkpoint, coverage, checksum: await checksum(checkpoint.bytes) };
        const latest = { ...base, manifestHash: await manifest(base) };
        let tx;
        try {
            tx = this.database.transaction("checkpoints", "readwrite", { durability: "strict" });
        }
        catch (error) {
            if (!(error instanceof TypeError) && !(error instanceof DOMException && error.name === "NotSupportedError"))
                throw error;
            tx = this.database.transaction("checkpoints", "readwrite");
        }
        return new Promise((resolve, reject) => {
            tx.oncomplete = () => resolve({ state: "checkpointCommitted", durability: tx.durability ?? "unknown" });
            tx.onabort = () => reject(tx.error ?? new DOMException("Checkpoint publication aborted", "AbortError"));
            let failure;
            tx.onabort = () => reject(failure ?? tx.error ?? new DOMException("Checkpoint publication aborted", "AbortError"));
            const abort = (error) => { failure = error; tx.abort(); };
            try {
                const store = tx.objectStore("checkpoints");
                const current = store.get(key(checkpoint.identity));
                current.onsuccess = () => {
                    try {
                        // IndexedDB serializes overlapping readwrite transactions. Never replace
                        // a publication whose fallback was validated from a stale read snapshot.
                        if (publicationVersion(current.result ?? {}) !== publicationVersion(raw.publication))
                            throw new CheckpointConflictError();
                        store.put({ latest, previous, revision: globalThis.crypto.randomUUID() }, key(checkpoint.identity));
                    }
                    catch (error) {
                        abort(error);
                    }
                };
            }
            catch (error) {
                abort(error);
            }
        });
    }
    /** Rust callback validates semantic checkpoint bytes and replays the retained tail before exposing a document. */
    async restore(expectedInput, restore) {
        const expected = ownIdentity(expectedInput);
        const raw = await this.readRaw(expected);
        const entries = await verifyEntries(raw.entries, expected);
        const rejected = [];
        for (const source of ["latest", "previous"]) {
            const candidate = raw.publication[source];
            if (!candidate)
                continue;
            try {
                const valid = await validate(candidate, expected);
                // Retain and replay even covered updates: CRDT replay is idempotent, and this avoids trusting coverage to omit bytes.
                const recovery = { checkpoint: valid.checkpoint, tail: entries, source, rejected: [...rejected] };
                return { value: restore(recovery), recovery };
            }
            catch (error) {
                rejected.push(`${source}: ${error instanceof Error ? error.message : String(error)}`);
            }
        }
        throw new JournalIntegrityError(`No valid recovery checkpoint: ${rejected.join("; ") || "missing checkpoint"}`);
    }
}
