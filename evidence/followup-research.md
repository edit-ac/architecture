# Follow-up research: local-first editing, agents, diffs and encryption

Reviewed 11 October 2026. Primary documentation only; no providers called, packages installed or project files changed. Existing Yrs architecture remains the default. Other projects below supply implementation patterns, not a recommendation to replace the engine. Facts and edit-ac design proposals are separated.

## Verified examples and reusable patterns

### Yjs: persistence and networking are independent

**Fact.** y-indexeddb persists shared data locally and restores it on later sessions. Its `synced` event means the database connection and initial content loading completed, including when the database is empty. It is not a remote disk-commit acknowledgment. [y-indexeddb documentation](https://docs.yjs.dev/ecosystem/database-provider/y-indexeddb)

**Design implication.** Keep independent states for local recovery, local durable commit, transport connectivity, peer synchronization and durable hosted acknowledgment. Start editing from recovered local state without a network dependency. An empty-but-existing document is distinct from an uninitialized document. For Yrs, implement the same storage pattern through its own update interface; do not insert a second writable `Y.Doc` solely to use the JavaScript provider.

### Automerge Repo: adapter separation and document handles

**Fact.** Automerge Repo separates storage adapters from network adapters. Official examples use IndexedDB for persistence, BroadcastChannel for cross-tab communication and WebSocket for remote peers. Previously loaded documents remain editable offline. A document URL identifies content, while the repository resolves locally available data and peers. [Local storage tutorial](https://automerge.org/docs/tutorial/local-sync/), [network tutorial](https://automerge.org/docs/tutorial/network-sync/), [repository concepts](https://automerge.org/docs/reference/concepts/)

**Fact.** Sharing IndexedDB between repositories does not itself make them live-update; the storage documentation explicitly recommends a local network channel for that. Automerge also supplies a filesystem storage adapter. [Storage reference](https://automerge.org/docs/reference/repositories/storage/)

**Design implication.** Give edit-ac document handles pluggable local store and optional transport ports. Treat a local filesystem store, IndexedDB store and later native database as implementations of a common recovery contract. Cross-tab delivery, cross-process local delivery and remote delivery are separate channels. Distinct independently editing replicas still need distinct identities. Define a source resolver separately from document state: local path, cached hosted document and authenticated hosted authority must converge on an explicit document/session identity.

### Loro: history and review are explicit APIs

**Fact.** Loro models versions using frontiers/version vectors. Its `diff(from, to)` produces typed container differences, and the API documents a review-style workflow using `diff` and `applyDiff`. Historical checkout detaches the document into read-only state until reattached. [Version model](https://loro.dev/docs/tutorial/version), [diff API](https://www.loro.dev/docs/api/js), [historical checkout](https://loro.dev/docs/tutorial/time_travel)

**Design implication.** Separate live editing, read-only current view, historical view, proposed change preview and restore-as-new-edit. A history viewer must not rewind the live collaborative replica. Restoring an old revision is a new authorized semantic operation with current-state checks. Define availability after pruning; a missing old revision is an explicit result. No claim that Yrs automatically supplies Loro's history API is justified by these examples.

## Exact diffs are separate from CRDT synchronization

**Fact.** Yjs updates are binary, commutative, associative and idempotent. `diffUpdate` computes update data missing from a peer state vector. That is synchronization data, not a human-readable source patch. [Yjs document updates](https://docs.yjs.dev/api/document-updates)

**Fact.** Yjs snapshots include both a state vector and deletion state. Yjs can garbage-collect deleted content; disabling GC is documented as necessary when relying on restoring old content from the live document. A state vector alone therefore must not be treated as an exact whole-document revision token. [Yjs internals](https://github.com/yjs/yjs/blob/main/INTERNALS.md), [Y.Doc GC option](https://docs.yjs.dev/api/y.doc)

**Fact.** Git diff compares snapshots/files and supports multiple diff algorithms. “Exactly like Git” is incomplete without defining inputs, algorithm and options. [Git diff manual](https://git-scm.com/docs/git-diff)

**Proposed contract.** Preserve immutable before/after source bytes, their cryptographic hashes, encoding/line-ending policy, serializer/profile version and document/session/revision IDs. Produce a deterministic unified text patch against those exact bytes, plus a separate semantic node/mark/move view. Patch application must reproduce the expected output hash; rejection leaves the document/file unchanged. Handle final-newline changes and mixed Unicode explicitly. Golden tests can compare a pinned `git diff --no-index` invocation, treating exit code 1 as differences rather than command failure.

**Pitfall.** Rich-text Markdown serialization normalizes syntax. An exact diff of saved bytes is still possible, but it does not imply preserving the original Markdown spelling. Keep the actual local-file baseline, preview serialization-induced changes, and avoid rewriting unrelated content where a tested source mapping allows it. If byte-preserving Markdown authoring is required, a concrete-syntax/source-mapping contract is additional work; the current semantic parser cannot promise it. CRDT checkpoints, selective undo and persistent revision history are three different retention features.

## MCP editing: transport conventions do not provide mutation safety

**Fact.** MCP exposes resources identified by URIs, permits custom URI schemes and supports optional resource-change subscriptions. Subscriptions notify that a resource changed; they do not define edit-ac's CRDT delivery protocol. [MCP resources, revision 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/resources)

**Fact.** MCP tools define inputs/outputs, but behavior annotations are hints and cannot enforce idempotency, authorization or read-only behavior. [MCP tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools), [official annotation guidance](https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/)

**Reference pattern.** HTTP conditional requests use validators to avoid lost updates; strong comparison is appropriate when exact representation equality matters. [RFC 9110, conditional requests](https://www.rfc-editor.org/rfc/rfc9110.html#section-13)

**Proposed edit-ac contract.** The host application supplies authentication and document permissions; a reusable adapter maps its MCP tools onto the same prepared-command engine used by web/TUI/native views. Read returns source plus revision, source hash, schema/profile and current capabilities. Write requires an expected revision/source hash, bounded patch or anchored edit set, and an idempotency request ID. Validate under the same serialized mutation boundary that commits the edit. A stale precondition returns a conflict with current revision metadata and no mutation; do not silently perform a whole-document replacement or reinterpret old integer offsets.

Persist request identity, request payload hash and the resulting receipt with the committed operation. An identical retry returns its original result; reusing the ID with different input rejects. Scope deduplication to authenticated actor/document/session and define retention. A transport timeout is an unknown result until the client reads the receipt/retries safely. CRDT update idempotence does not make repeating a high-level “insert text” command idempotent.

Successful agent edits carry an authenticated origin and flow through normal history, local persistence, renderer patches and sync so open editors see them in realtime. Tool output identifies what committed locally and what is remotely acknowledged. Resource notifications support agents refreshing context; the editor's existing update channel remains responsible for low-latency collaboration. Untrusted document prose is content, not authority for further tool actions. Read-only permissions must be enforced at the write boundary, independent of UI state or MCP hints.

## Local files, hosted sources and a TUI

**Proposed source contract.** `ac://authority/document-id` is an application resolver address, not proof of authorization, a bearer credential or an automatic network request. Validate/normalize URIs, resolve only configured authorities and keep credentials outside URLs. Opening a hosted source offline uses a matching cached document or returns unavailable; it must not invent an empty authoritative document. Local-file adapters restrict paths according to the host and preserve original bytes plus a baseline hash.

File saves use conditional baseline checks and an atomic replacement strategy appropriate to the platform. Detect external modification; offer an explicit merge/reload/recovery path rather than overwriting it. Watching a file and importing every serialization event can create echo loops; distinguish self-writes using file identity/content hashes and serialize admission. A local Markdown file is an interchange projection, not automatically the entire CRDT journal. Define where collaborative state/history lives and how moved/copied files affect document identity.

TUI editing is a platform adapter with terminal input, selections, rendering, history and lifecycle responsibilities. It should invoke shared commands and persistence/sync ports, not run a separate CRDT or repeatedly replace the whole document through Markdown. Terminal source editing and structured rich-text editing need distinct advertised capabilities; attachments/tables require preserved fallbacks and diagnostics.

## Optional encryption: proven pattern and design constraints

**Fact.** Automerge Repo Keyhive separates relay, read, edit and admin access. Relays can synchronize ciphertext without reading it. Its API guide shows why encrypted-document creation must be explicit: its legacy `repo.create` path bypasses protection while `repo.create2` uses the configured protected identity path. This is evidence for fail-closed creation tests, not a drop-in encryption layer for Yrs. [Official Keyhive integration guide](https://automerge.org/docs/keyhive/ark-api-guide/)

**Design implications, requiring a later security design gate.** Distinguish encrypted local storage from end-to-end encrypted collaboration. E2EE requires identity/key provisioning, key recovery, authenticated update envelopes, key epochs, rotation, encrypted attachments/history, replay handling and metadata disclosure rules. Choose and review a maintained protocol/cryptographic implementation; do not invent cryptography or claim “optional encryption” by wrapping only one transport connection in TLS.

A ciphertext-only host cannot simultaneously parse Markdown, produce plaintext diffs or run plaintext MCP edits without a decryption-capable authorized endpoint. Place those operations in the trusted local host/client, or explicitly grant the hosted agent service the needed access. Treat that choice as part of the trust model. Enforce read/edit rights independently; possessing read capability must not automatically authorize a write. Offline revocation cannot erase plaintext/keys a former reader already copied; define future-key access and pending-write behavior explicitly.

Encrypted mode must never silently downgrade on creation, restore, export, unsupported peer or missing key. Locked documents expose a locked/recovery state. Preserve ciphertext and pending local work on authorization/key failures. An opaque server can enforce envelope limits and store/acknowledge ciphertext, but cannot promise plaintext semantic validation. Server-side search/indexing/previews and agent edits need explicit capability tradeoffs. Add deterministic wrong-key, rotation, replay, recovery, revoked-writer and no-downgrade fixtures before publishing an encryption claim.

## Roadmap gates suggested by the evidence

1. Local-first source identity, recovery and cache-miss semantics before hosted CLI/TUI attachment.
2. Immutable revision snapshots and exact-byte diff/conditional-patch fixtures before “exact git-like diff” claims.
3. Shared agent edit contract and crash-safe idempotency receipts before MCP mutation exposure.
4. Host-authorized URI resolution and external-file conflict tests before remote/local source writes.
5. Separate read-only/history, TUI, iOS, Android and desktop adapter qualification tracks using common fixtures.
6. An optional encryption threat-model/protocol decision before encrypted storage/sync implementation; plaintext release behavior remains explicit.

All suggested gates are edit-ac design choices inferred from the sources, not features supplied automatically by MCP or Yrs.
