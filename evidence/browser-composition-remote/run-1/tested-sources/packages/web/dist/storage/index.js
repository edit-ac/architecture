import { UpdateJournal } from "./journal.js";
import { StorageWriter } from "./writer.js";
/** Internal host adapter. Takes ownership of writer/journal; hosts edit through commit().
 * Rust remains the only semantic replica. There are no unload handlers or timers.
 */
export class LocalStorageLifecycle {
    writer;
    journal;
    policy;
    updates = new Set();
    subscription;
    latest = null;
    failure = null;
    capability = "unknown";
    observedUnknownDurability = false;
    closing = false;
    destroyed = false;
    constructor(writer, journal, policy = { afterStorageFailure: "continue" }) {
        this.writer = writer;
        this.journal = journal;
        this.policy = policy;
        // Capture policy by value so host mutation cannot silently change it.
        this.policy = { ...policy };
        this.subscription = writer.engine.subscribe({ type: "updates" }, patch => {
            if (!patch.update)
                return;
            const update = { identity: { ...patch.identity }, writerId: patch.writerId,
                sequence: patch.sequence, origin: patch.origin, bytes: new Uint8Array(patch.update.bytes) };
            const record = { update, completion: Promise.resolve().then(() => this.journal.append(update)), failed: false };
            this.updates.add(record);
            record.completion = record.completion.then(commit => {
                this.updates.delete(record);
                this.latest = { ...commit };
                if (commit.durability === "unknown") {
                    this.observedUnknownDurability = true;
                    if (this.capability !== "unavailable")
                        this.capability = "unknown";
                }
                else if (commit.durability !== "strict")
                    this.capability = "unavailable";
                else if (this.capability === "unknown" && !this.observedUnknownDurability)
                    this.capability = "supported";
                return commit;
            }, error => {
                record.failed = true;
                this.failure = error;
                throw error;
            });
            // Edits are synchronous; storage errors are exposed by state/flush, not unhandled rejections.
            void record.completion.catch(() => { });
        });
    }
    get state() {
        const failed = [...this.updates].some(record => record.failed);
        return { phase: failed ? "error" : this.updates.size ? "pending" : "localCommitted",
            pending: [...this.updates].filter(record => !record.failed).length,
            localCommitted: this.latest ? { ...this.latest } : null, error: this.failure,
            saved: this.latest !== null && this.updates.size === 0,
            strictDurability: this.capability };
    }
    /** Policy is checked before preparing or mutating the Rust document. */
    commit(request) {
        this.requireLive();
        if (this.closing)
            throw new Error("Storage lifecycle is closing");
        if (this.policy.afterStorageFailure === "reject" && [...this.updates].some(record => record.failed)) {
            throw new Error("Host policy rejects edits after storage failure", { cause: this.failure });
        }
        const plan = this.writer.engine.prepare(request);
        try {
            return this.writer.engine.commit(plan);
        }
        finally {
            this.writer.engine.releasePlan(plan);
        }
    }
    /** Captures synchronously. Later updates cannot extend this barrier. Failed updates remain included. */
    flush(options) {
        this.requireLive();
        if (options.target !== "local")
            return Promise.reject(new Error("Unsupported flush target"));
        return Promise.all([...this.updates].map(record => record.completion)).then(() => { });
    }
    recoveryExport() {
        this.requireLive();
        return { checkpoint: this.writer.engine.checkpoint(), unsavedUpdates: [...this.updates].map(({ update }) => ({ ...update, identity: { ...update.identity }, bytes: new Uint8Array(update.bytes) })) };
    }
    /** Flush failure keeps the live replica available. Report mode exports before releasing it. */
    async destroy(options) {
        this.requireLive();
        if (this.closing)
            throw new Error("Storage lifecycle is already closing");
        if (options.policy !== "flush" && options.policy !== "report")
            throw new Error("Explicit destroy policy required");
        this.closing = true;
        try {
            if (options.policy === "flush")
                await this.flush({ target: "local" });
            const recovery = this.recoveryExport();
            const unsaved = this.updates.size !== 0;
            this.subscription.dispose();
            this.writer.dispose();
            this.journal.close();
            this.destroyed = true;
            return { unsaved, recovery };
        }
        finally {
            this.closing = false;
        }
    }
    requireLive() { if (this.destroyed)
        throw new Error("Storage lifecycle destroyed"); }
}
