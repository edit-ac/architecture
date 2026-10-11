# Portable local-first client and edit contracts

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core`; paths below are core-relative unless prefixed `../architecture/`. Follow `../architecture/specs/client-contracts.md` and the active task context. This is planned follow-up delivery, not implemented capability.

Required upstream tracks: `02-engine.md`, `03-local-storage.md`, `05-markdown-content.md`, `06-synchronization.md` complete at reviewed source/implementation revisions with passing evidence. Check these gates before launching; source dependencies below are local to this file.

## Execution rules

The controller owns this source. Write progress/checkmarks/evidence in the configured separate progress file. Each iteration implements at most one parent with its implementation and validation substeps. Aim for 15–45 minutes plus checks; if the boundary cannot fit, propose a stable controller-approved split before implementation. Use named fixtures/checks, creating planned test commands before running them. Missing checks, zero matches, failures and skips are not passing acceptance.

Use deterministic fixtures and mocked transports only; no paid model/provider calls, .secrets loading or production document writes. Other ready local tasks are permitted independent work. Unavailable device/toolchain/review evidence blocks its qualified claim, not unrelated platform work. Do not launch another runner or publish before an explicit release task.

## Epic CAP-1 — Portable local-first client and edit contracts

### Task CAP-1.1 — Audit shared-client compatibility

- [ ] CAP-1.1 Audit shared-client compatibility.

Purpose: Audit shared-client compatibility as one bounded reusable delivery boundary.
Context: `crates/editac-core/`; `crates/editac-markdown/`; `../architecture/evidence/client-compatibility.md`; `../architecture/specs/client-contracts.md`; `../architecture/specs/verification.md`.
Dependencies: none.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: All referenced gates including FMT-1.12 pass at recorded revisions; missing API/migration has a bounded controller-owned decision, not an invented compatibility promise.

Implementation:

- [ ] CAP-1.1-I1 Check real schema/patch/anchor/source-reconciliation/storage/sync evidence. Map required headless session ports and document any frozen-schema conflict before coding. Create the editac-session crate and contract-test harness only after the map is coherent.

Validation:

- [ ] CAP-1.1-V1 cargo test -p editac-core --locked; cargo test -p editac-markdown --test reconcile --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `CAP-1.1` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `CAP-1.1`.
Blocked behavior: Leave `CAP-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task CAP-1.2 — Freeze document locator and catalog grammar

- [ ] CAP-1.2 Freeze document locator and catalog grammar.

Purpose: Freeze document locator and catalog grammar as one bounded reusable delivery boundary.
Context: `crates/editac-session/src/locator.rs`; `crates/editac-session/tests/locator.rs`; `../architecture/specs/client-contracts.md`; `../architecture/specs/verification.md`.
Dependencies: CAP-1.1.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Ambiguous encodings, path traversal, unknown authorities and token-bearing URLs reject; offline cached lookup never fetches or creates an empty remote document.

Implementation:

- [ ] CAP-1.2-I1 Implement ac://document-id and ac://authority/document-id normalization with explicit IDs, epochs and local catalog mappings. Resolve only configured authorities; separate paths, URLs and credentials.

Validation:

- [ ] CAP-1.2-V1 cargo test -p editac-session --test locator --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `CAP-1.2` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `CAP-1.2`.
Blocked behavior: Leave `CAP-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task CAP-1.3 — Define reusable store and transport ports

- [ ] CAP-1.3 Define reusable store and transport ports.

Purpose: Define reusable store and transport ports as one bounded reusable delivery boundary.
Context: `crates/editac-session/src/ports.rs`; `crates/editac-session/tests/ports.rs`; `../architecture/specs/client-contracts.md`; `../architecture/specs/verification.md`.
Dependencies: CAP-1.1.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: The same prepared storage conformance cases run through memory and fault-injected adapters; browser libraries and database implementation details stay out of core.

Implementation:

- [ ] CAP-1.3-I1 Describe owned update buffers, journal/checkpoint/outbox records, capability/error states and serialized admission. Reuse prior browser guarantees; choose a bounded native transactional-store candidate in a recorded compatibility decision.

Validation:

- [ ] CAP-1.3-V1 cargo test -p editac-session --test ports --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `CAP-1.3` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `CAP-1.3`.
Blocked behavior: Leave `CAP-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task CAP-1.4 — Implement native local persistence adapter

- [ ] CAP-1.4 Implement native local persistence adapter.

Purpose: Implement native local persistence adapter as one bounded reusable delivery boundary.
Context: `crates/editac-session/src/store/`; `crates/editac-session/tests/native_store.rs`; `../architecture/specs/client-contracts.md`; `../architecture/specs/verification.md`.
Dependencies: CAP-1.3.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Acknowledged local edits recover across process termination/full-disk/commit boundaries; sidecar/store location and per-writer identity are explicit.

Implementation:

- [ ] CAP-1.4-I1 Implement the selected transactional store, checkpoint coverage and pending outbox with native crash/failure injection. Reuse CLI storage code if available rather than maintaining duplicate policies.

Validation:

- [ ] CAP-1.4-V1 cargo test -p editac-session --test native_store --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `CAP-1.4` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `CAP-1.4`.
Blocked behavior: Leave `CAP-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task CAP-1.5 — Implement local-first document handle lifecycle

- [ ] CAP-1.5 Implement local-first document handle lifecycle.

Purpose: Implement local-first document handle lifecycle as one bounded reusable delivery boundary.
Context: `crates/editac-session/src/session.rs`; `crates/editac-session/tests/lifecycle.rs`; `../architecture/specs/client-contracts.md`; `../architecture/specs/verification.md`.
Dependencies: CAP-1.2, CAP-1.4.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Local creation/edit/history works with network disabled; uncached hosted open reports unavailable; expired auth never discards pending work or claims remote commit.

Implementation:

- [ ] CAP-1.5-I1 Open local/cached/new documents before transport attachment; expose orthogonal readiness, commit, pending, conflict and auth states. Define cached-permission/expiry policy and recovery.

Validation:

- [ ] CAP-1.5-V1 cargo test -p editac-session --test lifecycle --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `CAP-1.5` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `CAP-1.5`.
Blocked behavior: Leave `CAP-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task CAP-1.6 — Bridge local cross-tab and cross-process delivery

- [ ] CAP-1.6 Bridge local cross-tab and cross-process delivery.

Purpose: Bridge local cross-tab and cross-process delivery as one bounded reusable delivery boundary.
Context: `packages/web/src/storage/local-channel.ts`; `crates/editac-session/src/local_channel.rs`; `tests/local-channel.test.mjs`; `../architecture/specs/client-contracts.md`; `../architecture/specs/verification.md`.
Dependencies: CAP-1.5.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Two offline tabs/processes see each others committed edits without a server, converge after reconnect and do not confuse shared storage with live delivery.

Implementation:

- [ ] CAP-1.6-I1 Exchange committed updates over explicit local channels with distinct replica IDs and echo suppression. Handle process/tab restarts and concurrent checkpoint writers.

Validation:

- [ ] CAP-1.6-V1 cargo test -p editac-session local_channel --locked; npm run build; node --test tests/local-channel.test.mjs. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `CAP-1.6` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `CAP-1.6`.
Blocked behavior: Leave `CAP-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task CAP-1.7 — Implement exact observed-revision validators

- [ ] CAP-1.7 Implement exact observed-revision validators.

Purpose: Implement exact observed-revision validators as one bounded reusable delivery boundary.
Context: `crates/editac-session/src/revision.rs`; `crates/editac-session/tests/revisions.rs`; `../architecture/specs/client-contracts.md`; `../architecture/specs/verification.md`.
Dependencies: CAP-1.5.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Deletion-only updates invalidate stale proposals; wrong document/epoch/profile rejects; concurrent unseen peer updates remain later CRDT events, not a claimed global transaction lock.

Implementation:

- [ ] CAP-1.7-I1 Add persisted document/epoch/profile-scoped observed-state tokens, covering deletion-only changes and restart. Compare them inside the serialized mutation boundary; define endpoint-local guarantees.

Validation:

- [ ] CAP-1.7-V1 cargo test -p editac-session --test revisions --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `CAP-1.7` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `CAP-1.7`.
Blocked behavior: Leave `CAP-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task CAP-1.8 — Expose shared prepared edit and permission service

- [ ] CAP-1.8 Expose shared prepared edit and permission service.

Purpose: Expose shared prepared edit and permission service as one bounded reusable delivery boundary.
Context: `crates/editac-session/src/edit_service.rs`; `crates/editac-session/tests/edit_service.rs`; `../architecture/specs/client-contracts.md`; `../architecture/specs/verification.md`.
Dependencies: CAP-1.7.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Local human, scripted and adapter calls share semantics; stale source/ambiguous anchors/readonly fail before mutation; unsafe whole-document replacement is unavailable.

Implementation:

- [ ] CAP-1.8-I1 Provide read/capabilities, source or anchored prepare, preview and apply over existing commands/reconciliation. Enforce readonly, module support, limits and current host authorization on every mutation path.

Validation:

- [ ] CAP-1.8-V1 cargo test -p editac-session --test edit_service --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `CAP-1.8` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `CAP-1.8`.
Blocked behavior: Leave `CAP-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task CAP-1.9 — Record operation provenance and origin policy

- [ ] CAP-1.9 Record operation provenance and origin policy.

Purpose: Record operation provenance and origin policy as one bounded reusable delivery boundary.
Context: `crates/editac-session/src/operations.rs`; `crates/editac-session/tests/origins.rs`; `../architecture/specs/client-contracts.md`; `../architecture/specs/verification.md`.
Dependencies: CAP-1.8.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Remote/agent work is not accidentally grouped as local typing undo; untrusted names/client IDs do not become authenticated audit authors; retention limits are explicit.

Implementation:

- [ ] CAP-1.9-I1 Record operation/request ID, authenticated host actor, origin and before/after tokens as bounded sideband metadata; separate human, agent, import and replay history groups.

Validation:

- [ ] CAP-1.9-V1 cargo test -p editac-session --test origins --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `CAP-1.9` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `CAP-1.9`.
Blocked behavior: Leave `CAP-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task CAP-1.10 — Qualify shared session and thin-core boundaries

- [ ] CAP-1.10 Qualify shared session and thin-core boundaries.

Purpose: Qualify shared session and thin-core boundaries as one bounded reusable delivery boundary.
Context: `crates/editac-session/tests/conformance.rs`; `../architecture/evidence/client-contracts.md`; `../architecture/specs/client-contracts.md`; `../architecture/specs/verification.md`.
Dependencies: CAP-1.6, CAP-1.9.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Offline/recovery/reconnect/readonly fixture outcomes agree; minimal core does not pull in terminal, OS UI, MCP, diff presenter or encryption dependencies.

Implementation:

- [ ] CAP-1.10-I1 Run identical prepared operations through browser and headless native sessions; inspect dependency/build features and update host contract docs.

Validation:

- [ ] CAP-1.10-V1 cargo test -p editac-session --locked; npm run build; node --test tests/local-channel.test.mjs. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `CAP-1.10` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `CAP-1.10`.
Blocked behavior: Leave `CAP-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.
