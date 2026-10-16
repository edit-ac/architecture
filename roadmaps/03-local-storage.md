# Recover browser documents safely

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Deliver only the outcomes below. Read `../architecture/specs/storage-sync.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Upstream entry gates: `02-engine.md` complete at current source revision with passing artifact evidence.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus validation; if a boundary is too large, stop with a precise proposed split for the controller. Pick a task only when every named dependency is implemented and validated. Other ready tasks are permitted independent work; a roadmap entry gate remains mandatory for its dependents. Do not launch this roadmap while its upstream gate is unavailable.

Create named checks before invoking them. Record nonzero executed/passed/failed/skipped counts; missing tests and zero-match Rust filters fail acceptance. Run the narrow check, then relevant integration checks. Use prepared fixtures and transports only. No model API tests, live dogfood, background runner startup or publication outside an explicit release task.

## Epic LOC-1 — Recover browser documents safely

### Task LOC-1.1 — Verify the engine persistence boundary

- [ ] LOC-1.1 Verify the engine persistence boundary.

Purpose: Deliver verify the engine persistence boundary as one reviewable boundary.
Context: `crates/editac-core/src/patches.rs`; `../architecture/specs/schema-v1.md`; `../architecture/specs/storage-sync.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Storage tests can obtain real update bytes and restore a document without a browser or sync service.

Implementation:

- [ ] LOC-1.1-I1 Check current engine evidence, update/epoch metadata and replay interface. Add the storage contract test harness using prepared update fixtures.

Validation:

- [ ] LOC-1.1-V1 cargo test -p editac-core --test patches --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `LOC-1.1` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `LOC-1.1`.
Blocked behavior: Leave `LOC-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task LOC-1.2 — Implement browser update journal

- [ ] LOC-1.2 Implement browser update journal.

Purpose: Deliver implement browser update journal as one reviewable boundary.
Context: `packages/web/src/storage/journal.ts`; `tests/journal.test.mjs`; `../architecture/specs/storage-sync.md`.
Dependencies: LOC-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Journal entries are idempotent; localCommitted occurs only after transaction complete, never on enqueue; quota/abort errors propagate.

Implementation:

- [ ] LOC-1.2-I1 Use IndexedDB transactions for immutable updates with writer/sequence/document/epoch/schema keys. Introduce a deterministic fake storage boundary for injected failures.

Validation:

- [ ] LOC-1.2-V1 npm run build; node --test tests/journal.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `LOC-1.2` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `LOC-1.2`.
Blocked behavior: Leave `LOC-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task LOC-1.3 — Implement checkpoint publication and restore

- [ ] LOC-1.3 Implement checkpoint publication and restore.

Purpose: Deliver implement checkpoint publication and restore as one reviewable boundary.
Context: `packages/web/src/storage/checkpoint.ts`; `tests/checkpoint.test.mjs`; `../architecture/specs/storage-sync.md`.
Dependencies: LOC-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Crashes before/after each publication boundary recover the last locally committed content; corrupt latest checkpoint falls back without silent loss.

Implementation:

- [ ] LOC-1.3-I1 Store checkpoint bytes and coverage atomically; retain previous valid checkpoint and necessary tail. Validate checksum/version before selecting recovery state.

Validation:

- [ ] LOC-1.3-V1 npm run build; node --test tests/checkpoint.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `LOC-1.3` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `LOC-1.3`.
Blocked behavior: Leave `LOC-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task LOC-1.4 — Implement outbox retention and receipt matching

- [ ] LOC-1.4 Implement outbox retention and receipt matching.

Purpose: Deliver implement outbox retention and receipt matching as one reviewable boundary.
Context: `packages/web/src/storage/outbox.ts`; `tests/outbox.test.mjs`; `../architecture/specs/storage-sync.md`.
Dependencies: LOC-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: A sync event, wrong receipt or checkpoint alone cannot drop unsynced updates; duplicate durable receipts are harmless.

Implementation:

- [ ] LOC-1.4-I1 Track local update identities awaiting durable remote receipt independently of checkpoint coverage. Require same document/epoch/update identity before pruning eligible entries.

Validation:

- [ ] LOC-1.4-V1 npm run build; node --test tests/outbox.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `LOC-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `LOC-1.4`.
Blocked behavior: Leave `LOC-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task LOC-1.5 — Implement multi-tab storage isolation

- [ ] LOC-1.5 Implement multi-tab storage isolation.

Purpose: Deliver implement multi-tab storage isolation as one reviewable boundary.
Context: `packages/web/src/storage/writer.ts`; `tests/writers.test.mjs`; `../architecture/specs/storage-sync.md`.
Dependencies: LOC-1.4.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Two writers cannot overwrite journal entries; simultaneous checkpoint attempts retain all committed updates and outbox content.

Implementation:

- [ ] LOC-1.5-I1 Give simultaneous tabs distinct live replica/writer IDs; make checkpoint replacement concurrency-safe and replay idempotent. Avoid shared mutable client IDs from persisted documents.

Validation:

- [ ] LOC-1.5-V1 npm run build; node --test tests/writers.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `LOC-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `LOC-1.5`.
Blocked behavior: Leave `LOC-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task LOC-1.6 — Expose local flush and recovery state

- [ ] LOC-1.6 Expose local flush and recovery state.

Purpose: Deliver expose local flush and recovery state as one reviewable boundary.
Context: `packages/web/src/storage/index.ts`; `tests/storage-lifecycle.test.mjs`; `../architecture/specs/storage-sync.md`. [Wordcraft-derived cases](../tests/wordcraft-regression-cases.md).
Dependencies: LOC-1.5.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Flush resolves for its captured update set after completion; errors reject it and saved UI is cleared; recovery retains in-memory edits. WCF-01: Repeated permanent recovery rejection suppresses unchanged expensive work, transient errors back off, and recovery preserves the last valid checkpoint/tail/outbox with explicit retry conditions and measured attempt/write counts.

Implementation:

- [ ] LOC-1.6-I1 Expose pending/localCommitted/error plus flush(local) barrier, strict-durability capability reporting and recovery export. Reject new edits only according to an explicit host policy after storage failure.

Validation:

- [ ] LOC-1.6-V1 npm run build; node --test tests/storage-lifecycle.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required). Execute the named WCF-01 variants through this owner's real boundary; record case/fixture revisions and work/effect counts. Planning validation is not runtime evidence.

Evidence: Progress entry `LOC-1.6` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `LOC-1.6`.
Blocked behavior: Leave `LOC-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task LOC-1.7 — Prove process-crash recovery in browsers

- [ ] LOC-1.7 Prove process-crash recovery in browsers.

Purpose: Deliver prove process-crash recovery in browsers as one reviewable boundary.
Context: `tests/browser/recovery.spec.ts`; `fixtures/crash-boundaries/`; `../architecture/specs/storage-sync.md`.
Dependencies: LOC-1.6.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Every tested acknowledged update survives supported process termination; pre-ack data loss is reported as outside the guarantee; no unload dependency.

Implementation:

- [ ] LOC-1.7-I1 Add pinned Playwright and a task-owned fixture server with teardown if absent; persist real engine updates, close the page/process after acknowledgment, reopen and compare.

Validation:

- [ ] LOC-1.7-V1 npm run test:browser -- recovery. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `LOC-1.7` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `LOC-1.7`.
Blocked behavior: Leave `LOC-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.
