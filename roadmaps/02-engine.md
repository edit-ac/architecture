# Implement the semantic document kernel

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Deliver only the outcomes below. Read `../architecture/specs/engine.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Upstream entry gates: `01-foundation.md` complete at current source revision with passing artifact evidence.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus validation; if a boundary is too large, stop with a precise proposed split for the controller. Pick a task only when every named dependency is implemented and validated. Other ready tasks are permitted independent work; a roadmap entry gate remains mandatory for its dependents. Do not launch this roadmap while its upstream gate is unavailable.

Create named checks before invoking them. Record nonzero executed/passed/failed/skipped counts; missing tests and zero-match Rust filters fail acceptance. Run the narrow check, then relevant integration checks. Use prepared fixtures and transports only. No model API tests, live dogfood, background runner startup or publication outside an explicit release task.

## Epic ENG-1 — Implement the semantic document kernel

### Task ENG-1.1 — Verify the foundation entry gate

- [ ] ENG-1.1 Verify the foundation entry gate.

Purpose: Deliver verify the foundation entry gate as one reviewable boundary.
Context: `../architecture/evidence/foundation.md`; `../architecture/specs/schema-v1.md`; `../architecture/specs/engine.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Foundation evidence is complete and the chosen schema is available; missing evidence blocks this track without changing its acceptance.

Implementation:

- [ ] ENG-1.1-I1 Check upstream completion against the current source revision and rerun the pinned interop fixture. Record schema/profile hashes in this progress file.

Validation:

- [ ] ENG-1.1-V1 cargo test -p editac-core --test interop --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.1` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.1`.
Blocked behavior: Leave `ENG-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.2 — Implement document identity and initialization

- [ ] ENG-1.2 Implement document identity and initialization.

Purpose: Deliver implement document identity and initialization as one reviewable boundary.
Context: `crates/editac-core/src/document.rs`; `crates/editac-core/tests/initialization.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Opening existing data never imports defaults twice; duplicate/reordered initialization updates converge; wrong epochs return a typed error.

Implementation:

- [ ] ENG-1.2-I1 Implement new-document and restore as distinct operations; enforce document/epoch/schema identity, unique live clients and explicit initialized state. Reuse the frozen schema.

Validation:

- [ ] ENG-1.2-V1 cargo test -p editac-core --test initialization --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.2` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.2`.
Blocked behavior: Leave `ENG-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.3 — Implement read projection and incremental indexes

- [ ] ENG-1.3 Implement read projection and incremental indexes.

Purpose: Deliver implement read projection and incremental indexes as one reviewable boundary.
Context: `crates/editac-core/src/projection.rs`; `crates/editac-core/tests/projection.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Snapshots match fixed fixtures; a single text edit reports only affected nodes and does not rebuild a second mutable document.

Implementation:

- [ ] ENG-1.3-I1 Project stable nodes, attributed text and deterministic placement from Yrs. Build only necessary node/range indexes and update them from touched transaction ranges.

Validation:

- [ ] ENG-1.3-V1 cargo test -p editac-core --test projection --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.3` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.3`.
Blocked behavior: Leave `ENG-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.4 — Implement relative anchors and UTF-16 conversion

- [ ] ENG-1.4 Implement relative anchors and UTF-16 conversion.

Purpose: Deliver implement relative anchors and UTF-16 conversion as one reviewable boundary.
Context: `crates/editac-core/src/anchors.rs`; `crates/editac-core/tests/anchors.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Emoji, ZWJ, combining text, RTL and deleted targets have fixed results; malformed offsets fail before mutation.

Implementation:

- [ ] ENG-1.4-I1 Define anchor resolution/deletion results and biased selection endpoints. Validate UTF-16 boundaries with grapheme-aware editing helpers; preserve anchors across remote insert/delete.

Validation:

- [ ] ENG-1.4-V1 cargo test -p editac-core --test anchors --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.4`.
Blocked behavior: Leave `ENG-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.5 — Implement prepared text edits

- [ ] ENG-1.5 Implement prepared text edits.

Purpose: Deliver implement prepared text edits as one reviewable boundary.
Context: `crates/editac-core/src/commands/text.rs`; `crates/editac-core/tests/text_commands.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.4.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Invalid preparation leaves updates/state unchanged; valid replacements commit once and produce the expected touched range.

Implementation:

- [ ] ENG-1.5-I1 Separate fallible preparation from commit. Implement insert/delete/replace and nonmutating applicability, with bounded byte/depth limits and explicit transaction origin.

Validation:

- [ ] ENG-1.5-V1 cargo test -p editac-core --test text_commands --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.5`.
Blocked behavior: Leave `ENG-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.6 — Implement marks and basic block attributes

- [ ] ENG-1.6 Implement marks and basic block attributes.

Purpose: Deliver implement marks and basic block attributes as one reviewable boundary.
Context: `crates/editac-core/src/commands/format.rs`; `crates/editac-core/tests/format_commands.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.5.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Toggle/apply/remove behavior across mixed selections is deterministic; code and URL policy follow formats spec; invalid attributes do not partially apply.

Implementation:

- [ ] ENG-1.6-I1 Add bold/italic/strike/underline/code/link marks and paragraph/heading attributes using one validated batch. Define invalid mark combinations and link attribute validation.

Validation:

- [ ] ENG-1.6-V1 cargo test -p editac-core --test format_commands --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.6` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.6`.
Blocked behavior: Leave `ENG-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.7 — Implement paragraph split and join

- [ ] ENG-1.7 Implement paragraph split and join.

Purpose: Deliver implement paragraph split and join as one reviewable boundary.
Context: `crates/editac-core/src/commands/structure.rs`; `crates/editac-core/tests/split_join.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.5.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Beginning/middle/end/empty splits and joins pass including remote insert races and deleted targets.

Implementation:

- [ ] ENG-1.7-I1 Implement split/join around stable text anchors and placement rules, preserving marks and concurrent edits according to schema-v1.

Validation:

- [ ] ENG-1.7-V1 cargo test -p editac-core --test split_join --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.7` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.7`.
Blocked behavior: Leave `ENG-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.8 — Implement list and quote structure

- [ ] ENG-1.8 Implement list and quote structure.

Purpose: Deliver implement list and quote structure as one reviewable boundary.
Context: `crates/editac-core/src/commands/lists.rs`; `crates/editac-core/tests/lists.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.7.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Nested enter/backspace/indent/outdent fixture transitions match semantic snapshots; illegal hierarchy is rejected before commit.

Implementation:

- [ ] ENG-1.8-I1 Add nested ordered/unordered/checklist and blockquote commands with indentation/outdent limits, list numbering and checked state. Use existing structure primitives.

Validation:

- [ ] ENG-1.8-V1 cargo test -p editac-core --test lists --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.8` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.8`.
Blocked behavior: Leave `ENG-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.9 — Implement code blocks and separators

- [ ] ENG-1.9 Implement code blocks and separators.

Purpose: Deliver implement code blocks and separators as one reviewable boundary.
Context: `crates/editac-core/src/commands/blocks.rs`; `crates/editac-core/tests/blocks.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.7.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Code whitespace and blank lines round-trip, literal editing avoids rich marks, separators do not trap a document without an editable position.

Implementation:

- [ ] ENG-1.9-I1 Add code language/text whitespace, hard breaks and separators with explicit insertion/navigation semantics and preserving unknown language labels.

Validation:

- [ ] ENG-1.9-V1 cargo test -p editac-core --test blocks --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.9` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.9`.
Blocked behavior: Leave `ENG-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.10 — Implement identity-preserving semantic move

- [ ] ENG-1.10 Implement identity-preserving semantic move.

Purpose: Deliver implement identity-preserving semantic move as one reviewable boundary.
Context: `crates/editac-core/src/commands/move.rs`; `crates/editac-core/tests/moves.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.8.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Move/move and move/edit converge without cloning/deleting text identity; nested moves and deleted destinations have explicit results.

Implementation:

- [ ] ENG-1.10-I1 Implement the selected placement operation, cycle rejection and selection anchoring using schema-v1. Reuse structural concurrency fixtures.

Validation:

- [ ] ENG-1.10-V1 cargo test -p editac-core --test moves --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.10` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.10`.
Blocked behavior: Leave `ENG-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.11 — Implement origin-aware undo groups

- [ ] ENG-1.11 Implement origin-aware undo groups.

Purpose: Deliver implement origin-aware undo groups as one reviewable boundary.
Context: `crates/editac-core/src/history.rs`; `crates/editac-core/tests/history.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.6, ENG-1.8, ENG-1.9, ENG-1.10.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Remote changes are excluded; one explicit operation produces one undo group even inside the capture timeout; undo after concurrent changes preserves others edits.

Implementation:

- [ ] ENG-1.11-I1 Use Yrs selective history with tracked local origins. Define typing/composition grouping and explicit reset boundaries around paste/format/move; cap history and clear redo correctly.

Validation:

- [ ] ENG-1.11-V1 cargo test -p editac-core --test history --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.11` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.11`.
Blocked behavior: Leave `ENG-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.12 — Expose batched patches and scoped subscriptions

- [ ] ENG-1.12 Expose batched patches and scoped subscriptions.

Purpose: Deliver expose batched patches and scoped subscriptions as one reviewable boundary.
Context: `crates/editac-core/src/patches.rs`; `crates/editac-core/tests/patches.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.11.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: No reentrant transaction panic; irrelevant listeners are not called; observer errors cannot corrupt committed state; unsubscribe removes callbacks.

Implementation:

- [ ] ENG-1.12-I1 Emit versioned changed-node/range, selection and update metadata once per commit. Defer observer callbacks until transactions/locks are released and make subscription disposal idempotent.

Validation:

- [ ] ENG-1.12-V1 cargo test -p editac-core --test patches --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.12` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.12`.
Blocked behavior: Leave `ENG-1.12` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.13 — Exercise seeded replica operation sequences

- [ ] ENG-1.13 Exercise seeded replica operation sequences.

Purpose: Deliver exercise seeded replica operation sequences as one reviewable boundary.
Context: `crates/editac-core/tests/replica_properties.rs`; `fixtures/replica-seeds/`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.12.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: All published seeds converge without losing acknowledged source content or violating schema; test count and bounded schedule coverage are recorded.

Implementation:

- [ ] ENG-1.13-I1 Run deterministic operation schedules for disconnect/reorder/duplicate, all structural commands and undo. Keep failing seeds and compare canonical semantic projections.

Validation:

- [ ] ENG-1.13-V1 cargo test -p editac-core --test replica_properties --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.13` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.13`.
Blocked behavior: Leave `ENG-1.13` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.14 — Bind semantic commands and snapshots to WASM

- [ ] ENG-1.14 Bind semantic commands and snapshots to WASM.

Purpose: Deliver bind semantic commands and snapshots to WASM as one reviewable boundary.
Context: `crates/editac-wasm/src/`; `packages/core/src/`; `tests/wasm-commands.test.mjs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.13.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Built WASM executes shared engine command fixtures and rejects malformed input without partial mutation; disposal is explicit and idempotent.

Implementation:

- [ ] ENG-1.14-I1 Promote the fixture bridge to opaque real engine handles with typed create/read/prepare/commit/anchor/history operations. Validate JS boundary types and propagate structured errors.

Validation:

- [ ] ENG-1.14-V1 npm run build:wasm; npm run build; node --test tests/wasm-commands.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.14` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.14`.
Blocked behavior: Leave `ENG-1.14` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.15 — Bind updates, restoration and patch events to WASM

- [ ] ENG-1.15 Bind updates, restoration and patch events to WASM.

Purpose: Deliver bind updates, restoration and patch events to WASM as one reviewable boundary.
Context: `crates/editac-wasm/src/`; `packages/core/src/`; `tests/wasm-updates.test.mjs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.14.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Browser storage and sync can use real update bytes; JS and Rust semantic snapshots agree after replay; disposed handles/subscriptions cannot be used.

Implementation:

- [ ] ENG-1.15-I1 Expose update/state-vector encoding, restore/apply, batched patch subscriptions and owned byte buffers with post-transaction callback scheduling.

Validation:

- [ ] ENG-1.15-V1 npm run build:wasm; npm run build; node --test tests/wasm-updates.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.15` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.15`.
Blocked behavior: Leave `ENG-1.15` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.
