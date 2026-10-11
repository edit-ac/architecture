# Exchange updates and durable receipts

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Deliver only the outcomes below. Read `../architecture/specs/storage-sync.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Upstream entry gates: `02-engine.md` complete at current source revision with passing artifact evidence, `03-local-storage.md` complete at current source revision with passing artifact evidence.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus validation; if a boundary is too large, stop with a precise proposed split for the controller. Pick a task only when every named dependency is implemented and validated. Other ready tasks are permitted independent work; a roadmap entry gate remains mandatory for its dependents. Do not launch this roadmap while its upstream gate is unavailable.

Create named checks before invoking them. Record nonzero executed/passed/failed/skipped counts; missing tests and zero-match Rust filters fail acceptance. Run the narrow check, then relevant integration checks. Use prepared fixtures and transports only. No model API tests, live dogfood, background runner startup or publication outside an explicit release task.

## Epic SYN-1 — Exchange updates and durable receipts

### Task SYN-1.1 — Verify storage and protocol entry gates

- [ ] SYN-1.1 Verify storage and protocol entry gates.

Purpose: Deliver verify storage and protocol entry gates as one reviewable boundary.
Context: `../architecture/specs/protocol-v1.md`; `packages/web/src/storage/`; `../architecture/specs/storage-sync.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Protocol version and receipt schema are explicit; transport tests run without credentials or network.

Implementation:

- [ ] SYN-1.1-I1 Check fixed update/protocol profile and outbox evidence; establish prepared socket transport fixtures without a production endpoint.

Validation:

- [ ] SYN-1.1-V1 node --test tests/outbox.test.mjs tests/interop.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SYN-1.1` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SYN-1.1`.
Blocked behavior: Leave `SYN-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task SYN-1.2 — Implement direct Yjs sync message adapter

- [ ] SYN-1.2 Implement direct Yjs sync message adapter.

Purpose: Deliver implement direct Yjs sync message adapter as one reviewable boundary.
Context: `packages/web/src/sync/protocol.ts`; `tests/sync-protocol.test.mjs`; `../architecture/specs/storage-sync.md`.
Dependencies: SYN-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: JS fixture and Rust document exchange all baseline messages, reject malformed/oversized frames and converge after duplicates.

Implementation:

- [ ] SYN-1.2-I1 Implement state-vector/step/update exchange with bounded decoding and Yrs WASM calls. Use y-protocols fixtures as oracle without pretending the handle is a Y.Doc.

Validation:

- [ ] SYN-1.2-V1 npm run build; node --test tests/sync-protocol.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SYN-1.2` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SYN-1.2`.
Blocked behavior: Leave `SYN-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task SYN-1.3 — Implement reconnect and backpressure

- [ ] SYN-1.3 Implement reconnect and backpressure.

Purpose: Deliver implement reconnect and backpressure as one reviewable boundary.
Context: `packages/web/src/sync/session.ts`; `tests/reconnect.test.mjs`; `../architecture/specs/storage-sync.md`.
Dependencies: SYN-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Disconnect/shuffle/duplicate/backpressure fixtures converge without echo loops or dropped local updates; detach remains editable offline.

Implementation:

- [ ] SYN-1.3-I1 Attach/detach transport without recreating state; replay outbox after authorized reconnect with bounded queue/retry policy. Separate local, remote and replay origins.

Validation:

- [ ] SYN-1.3-V1 npm run build; node --test tests/reconnect.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SYN-1.3` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SYN-1.3`.
Blocked behavior: Leave `SYN-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task SYN-1.4 — Implement optional awareness

- [ ] SYN-1.4 Implement optional awareness.

Purpose: Deliver implement optional awareness as one reviewable boundary.
Context: `packages/web/src/sync/awareness.ts`; `tests/awareness.test.mjs`; `../architecture/specs/storage-sync.md`.
Dependencies: SYN-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Stale peers expire, invalid cursors fail safely, bursts are bounded and no awareness traffic changes the journal.

Implementation:

- [ ] SYN-1.4-I1 Bridge tested awareness encoding, expiry and throttling; represent remote selections with anchors. Keep presence out of durable update storage.

Validation:

- [ ] SYN-1.4-V1 npm run build; node --test tests/awareness.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SYN-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SYN-1.4`.
Blocked behavior: Leave `SYN-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task SYN-1.5 — Build a local reference durable relay

- [ ] SYN-1.5 Build a local reference durable relay.

Purpose: Deliver build a local reference durable relay as one reviewable boundary.
Context: `examples/sync-server/`; `tests/server-receipts.test.mjs`; `../architecture/specs/storage-sync.md`.
Dependencies: SYN-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Receipt is emitted only after storage commit; process restart replays stored updates; duplicate updates are idempotent; no production auth claim.

Implementation:

- [ ] SYN-1.5-I1 Create a clearly test-only reference service with per-document/epoch update identity, transactional storage and explicit receipt extension. Bind loopback by default and use prepared authorization fixtures.

Validation:

- [ ] SYN-1.5-V1 node --test tests/server-receipts.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SYN-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SYN-1.5`.
Blocked behavior: Leave `SYN-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task SYN-1.6 — Handle authorization and durable acknowledgments

- [ ] SYN-1.6 Handle authorization and durable acknowledgments.

Purpose: Deliver handle authorization and durable acknowledgments as one reviewable boundary.
Context: `packages/web/src/sync/receipts.ts`; `tests/receipts.test.mjs`; `../architecture/specs/storage-sync.md`.
Dependencies: SYN-1.5.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Ordinary synced handshake never claims durable state; revocation retains local edits; wrong-document/epoch receipts cannot prune.

Implementation:

- [ ] SYN-1.6-I1 Negotiate optional receipt capability and match identities before outbox pruning. Expose remoteCommitted only for durable receipt; model denied/revoked auth with recovery export.

Validation:

- [ ] SYN-1.6-V1 npm run build; node --test tests/receipts.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SYN-1.6` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SYN-1.6`.
Blocked behavior: Leave `SYN-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task SYN-1.7 — Prove offline two-browser recovery flow

- [ ] SYN-1.7 Prove offline two-browser recovery flow.

Purpose: Deliver prove offline two-browser recovery flow as one reviewable boundary.
Context: `tests/browser/offline-collaboration.spec.ts`; `../architecture/evidence/collaboration.md`; `../architecture/specs/storage-sync.md`.
Dependencies: SYN-1.4, SYN-1.6.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Semantic convergence and local crash recovery both pass; receipt behavior is separate from protocol interop and servers cleanly stop after tests.

Implementation:

- [ ] SYN-1.7-I1 Use headless real-engine browser fixtures (no editor UI dependency), plus JS/Rust peer, with disconnect/restart/reconnect and overlapping prepared commands. Capture local service commit fault boundaries and tear down the service.

Validation:

- [ ] SYN-1.7-V1 npm run test:browser -- offline-collaboration. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SYN-1.7` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SYN-1.7`.
Blocked behavior: Leave `SYN-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.
