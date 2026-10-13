import { identityKey } from "./journal.js";
/** An engine replica plus an origin-wide lease. Persisted writer IDs are never reused. */
export class StorageWriter {
    engine;
    writerId;
    release;
    disposed = false;
    constructor(engine, writerId, release) {
        this.engine = engine;
        this.writerId = writerId;
        this.release = release;
    }
    /** Web Locks protects against rare random-ID collisions across separate WASM/tab realms. */
    static async restore(runtime, locks, expected, checkpoint, tail = []) {
        if (!locks?.request)
            throw new Error("Multi-tab writer isolation requires Web Locks");
        for (let attempt = 0; attempt < 128; attempt++) {
            const engine = runtime.restoreEngine(expected, checkpoint, tail);
            let writerId;
            try {
                writerId = engine.checkpoint().writerId;
            }
            catch (error) {
                engine.dispose();
                throw error;
            }
            let release;
            const held = new Promise(resolve => { release = resolve; });
            let decide;
            let fail;
            const acquired = new Promise((resolve, reject) => { decide = resolve; fail = reject; });
            let lease;
            try {
                lease = locks.request(`editac-writer:${identityKey(expected)}:${writerId}`, { ifAvailable: true }, async (lock) => {
                    decide(lock !== null);
                    if (lock)
                        await held;
                });
            }
            catch (error) {
                engine.dispose();
                throw error;
            }
            void lease.catch(fail);
            try {
                if (await acquired)
                    return new StorageWriter(engine, writerId, release);
            }
            catch (error) {
                engine.dispose();
                throw error;
            }
            engine.dispose();
        }
        throw new Error("No distinct live storage writer available");
    }
    dispose() {
        if (this.disposed)
            return;
        this.disposed = true;
        try {
            this.engine.dispose();
        }
        finally {
            this.release();
        }
    }
}
