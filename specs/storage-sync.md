# Storage and synchronization contract

The engine emits immutable update bytes and document/epoch/schema/origin metadata. Browser and native CLI storage/transport adapters consume these independently. Baseline versions and wire layout are frozen by the foundation protocol task, using the [engine contract](engine.md). The [CLI contract](cli.md) defines filesystem durability, Markdown working buffers and hosted target resolution; browser-specific storage mechanisms are not native filesystem guarantees.

## Local durability

Journal key: document ID, epoch, writer ID and monotonic per-writer sequence. Store immutable update bytes, checksum, schema version and pending receipt identity. Generate distinct live CRDT client IDs and writer IDs for simultaneous tabs. Restoring document bytes never restores a shared active client identity.

`localCommitted(updateId)` means the transaction containing that update completed. Queueing, creating a request and scheduling a timer are insufficient. Request strict durability where supported and report actual capability. The guarantee covers tested process crashes; browser eviction, user deletion and arbitrary hardware/power failures remain outside it. No unload-handler dependency.

A checkpoint consists of CRDT state, coverage metadata and hash. Publish checkpoint/coverage atomically. Keep the previous valid point and a recoverable tail until replacement is safely published. A checkpoint may cover unacknowledged local updates, but the outbox must still retain their identities and retransmittable bytes. JSON export is never used as a checkpoint that silently changes CRDT identity.

`flush({target:'local'})` captures the pending set and resolves once all those updates complete storage; later updates need not extend the barrier. A failed transaction rejects the barrier, clears saved status and exposes a recoverable error. Keep in-memory state/export available. Destroy policy explicitly flushes or reports unsaved state; destruction must not imply saving.

Use deterministic failure injection before/after each write/transaction/publication boundary, plus actual browser process termination after acknowledgment. Test two tab writers, duplicate/reordered replay, corrupt latest checkpoint, quota/permission rejection, schema mismatch and missing document identity. Preserve failures in evidence.

## Network

Transport is optional and attaches to the existing engine. It must not reinitialize the document, import a second snapshot or replace selection/history on connection. Use transaction origins to avoid echo. Define bounded receive/send queues, frame sizes, retry/backoff and reconnection behavior. Defer unauthorized uploads but retain recoverable local edits.

Profile four independently versioned contracts: v1 update bytes, baseline sync messages, awareness messages, and edit.ac document schema. The pinned JS fixture operates on the same schema. A Yrs handle is not a JS `Y.Doc`; use a direct wire adapter or an explicitly tested provider adapter. Yjs compatibility does not imply Tiptap/ProseMirror schema compatibility.

Awareness is ephemeral, expiring and throttled. It cannot advance document durability. Relative peer selections resolve against current state and fail safely when targets disappear. Presence remains optional and is never journaled as document state.

## Durable receipts

`remoteCommitted(updateId)` requires an explicit negotiated application receipt, emitted after the service's durable storage commit. A synced event, state vector or socket delivery does not meet this contract. Receipt identity includes document, epoch, writer/sequence and content identity; wrong identity cannot prune the outbox. Receipt capability absence means remote durability is unknown.

The local reference service is integration infrastructure: loopback by default, prepared auth fixtures, transactional storage, duplicate handling and restart recovery. Do not deploy it as a production service by implication. Host/service is responsible for authentication, authorization, rate limits and retention. Revocation leaves local work exportable and does not erase it.

Remote schema/epoch mismatch returns an explicit incompatibility state. Migrations use a declared new epoch and session transition; old offline updates cannot be silently applied after a rewrite. Checkpoint compaction retains reconnect identity according to the pinned protocol.

Sources: [IndexedDB durability](https://w3c.github.io/IndexedDB/), [Yjs updates](https://docs.yjs.dev/api/document-updates), [Yrs sync protocol](https://docs.rs/yrs/0.28.0/yrs/sync/protocol/trait.Protocol.html).

## Additional clients and protected profiles

[Client contracts](client-contracts.md) extend these ports to native/CLI sessions and explicit cross-tab/process delivery; sharing storage alone is not live synchronization. [Security profiles](security-encryption.md) can wrap local storage and transport while preserving acknowledgment identity. Ciphertext receipts certify stored bytes, not plaintext schema validation or endpoint authorization. Agent requests add durable request/result deduplication in the host/session boundary.
