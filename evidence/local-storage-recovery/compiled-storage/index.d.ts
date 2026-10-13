import type { Checkpoint, PrepareRequest } from "@edit-ac/core";
import type { JournalUpdate, LocalCommit } from "./journal.js";
import { UpdateJournal } from "./journal.js";
import { StorageWriter } from "./writer.js";
export interface StorageState {
    phase: "pending" | "localCommitted" | "error";
    pending: number;
    localCommitted: LocalCommit | null;
    error: unknown;
    saved: boolean;
    /** Conservative, observed transaction capability; unknown before the first commit. */
    strictDurability: "unknown" | "supported" | "unavailable";
}
export interface RecoveryExport {
    checkpoint: Checkpoint;
    unsavedUpdates: JournalUpdate[];
}
/** Internal host adapter. Takes ownership of writer/journal; hosts edit through commit().
 * Rust remains the only semantic replica. There are no unload handlers or timers.
 */
export declare class LocalStorageLifecycle {
    private readonly writer;
    private readonly journal;
    private readonly policy;
    private readonly updates;
    private readonly subscription;
    private latest;
    private failure;
    private capability;
    private observedUnknownDurability;
    private closing;
    private destroyed;
    constructor(writer: StorageWriter, journal: UpdateJournal, policy?: {
        afterStorageFailure: "continue" | "reject";
    });
    get state(): StorageState;
    /** Policy is checked before preparing or mutating the Rust document. */
    commit(request: PrepareRequest): {
        revision: number;
    };
    /** Captures synchronously. Later updates cannot extend this barrier. Failed updates remain included. */
    flush(options: {
        target: "local";
    }): Promise<void>;
    recoveryExport(): RecoveryExport;
    /** Flush failure keeps the live replica available. Report mode exports before releasing it. */
    destroy(options: {
        policy: "flush" | "report";
    }): Promise<{
        unsaved: boolean;
        recovery: RecoveryExport;
    }>;
    private requireLive;
}
