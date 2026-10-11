# Exact source and semantic change review

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core`; paths below are core-relative unless prefixed `../architecture/`. Follow `../architecture/specs/change-diffs.md` and the active task context. This is planned follow-up delivery, not implemented capability.

Required upstream tracks: `12-client-contracts.md` complete at reviewed source/implementation revisions with passing evidence. Check these gates before launching; source dependencies below are local to this file.

## Execution rules

The controller owns this source. Write progress/checkmarks/evidence in the configured separate progress file. Each iteration implements at most one parent with its implementation and validation substeps. Aim for 15–45 minutes plus checks; if the boundary cannot fit, propose a stable controller-approved split before implementation. Use named fixtures/checks, creating planned test commands before running them. Missing checks, zero matches, failures and skips are not passing acceptance.

Use deterministic fixtures and mocked transports only; no paid model/provider calls, .secrets loading or production document writes. Other ready local tasks are permitted independent work. Unavailable device/toolchain/review evidence blocks its qualified claim, not unrelated platform work. Do not launch another runner or publish before an explicit release task.

## Epic DIF-1 — Exact source and semantic change review

### Task DIF-1.1 — Freeze revision representation and retention fixtures

- [ ] DIF-1.1 Freeze revision representation and retention fixtures.

Purpose: Freeze revision representation and retention fixtures as one bounded reusable delivery boundary.
Context: `crates/editac-diff/`; `fixtures/diff/`; `../architecture/evidence/diff-contract.md`; `../architecture/specs/change-diffs.md`; `../architecture/specs/verification.md`.
Dependencies: none.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Cases distinguish formatting-only edits, structural moves, deletion-only changes, CRLF/final newline and unavailable old revisions; no CRDT byte delta is labeled a source diff.

Implementation:

- [ ] DIF-1.1-I1 Define exact-source versus projected-Markdown versus semantic representations, hashes/encoding/profile, bounded history availability and deterministic golden inputs. Create the test harness.

Validation:

- [ ] DIF-1.1-V1 cargo test -p editac-diff --test representation --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `DIF-1.1` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DIF-1.1`.
Blocked behavior: Leave `DIF-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task DIF-1.2 — Implement bounded immutable revision storage

- [ ] DIF-1.2 Implement bounded immutable revision storage.

Purpose: Implement bounded immutable revision storage as one bounded reusable delivery boundary.
Context: `crates/editac-session/src/history_store.rs`; `crates/editac-session/tests/history_store.rs`; `../architecture/specs/change-diffs.md`; `../architecture/specs/verification.md`.
Dependencies: DIF-1.1.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Pruning/missing keys/wrong schema return explicit unavailable results; historical reads never mutate live state; no full serialization is added to every keystroke.

Implementation:

- [ ] DIF-1.2-I1 Store named immutable snapshots or reconstructable checkpoints/tails with capability metadata and retention policy; materialize on request outside ordinary typing.

Validation:

- [ ] DIF-1.2-V1 cargo test -p editac-session --test history_store --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `DIF-1.2` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DIF-1.2`.
Blocked behavior: Leave `DIF-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task DIF-1.3 — Implement exact unified source patches

- [ ] DIF-1.3 Implement exact unified source patches.

Purpose: Implement exact unified source patches as one bounded reusable delivery boundary.
Context: `crates/editac-diff/src/text.rs`; `crates/editac-diff/tests/text_patch.rs`; `../architecture/specs/change-diffs.md`; `../architecture/specs/verification.md`.
Dependencies: DIF-1.1.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Applying a valid patch reproduces exact expected bytes/hash; wrong baseline, malformed ranges and overlapping hunks fail atomically; repeated-line cases are deterministic.

Implementation:

- [ ] DIF-1.3-I1 Pin line/word diff options and before/after hashes; encode/decode bounded unified hunks against exact UTF-8 bytes, including newline metadata.

Validation:

- [ ] DIF-1.3-V1 cargo test -p editac-diff --test text_patch --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `DIF-1.3` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DIF-1.3`.
Blocked behavior: Leave `DIF-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task DIF-1.4 — Implement semantic structural and mark diffs

- [ ] DIF-1.4 Implement semantic structural and mark diffs.

Purpose: Implement semantic structural and mark diffs as one bounded reusable delivery boundary.
Context: `crates/editac-diff/src/semantic.rs`; `crates/editac-diff/tests/semantic.rs`; `../architecture/specs/change-diffs.md`; `../architecture/specs/verification.md`.
Dependencies: DIF-1.2.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: A moved block is visible as a move without erasing content changes; link-target/mark-only and opaque attribute changes are not hidden by Markdown normalization.

Implementation:

- [ ] DIF-1.4-I1 Compare immutable projections by stable IDs and text/mark/attribute/placement changes; expose formatting, references, tables and unknown module differences separately.

Validation:

- [ ] DIF-1.4-V1 cargo test -p editac-diff --test semantic --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `DIF-1.4` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DIF-1.4`.
Blocked behavior: Leave `DIF-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task DIF-1.5 — Prepare revision-checked hunk application

- [ ] DIF-1.5 Prepare revision-checked hunk application.

Purpose: Prepare revision-checked hunk application as one bounded reusable delivery boundary.
Context: `crates/editac-session/src/review_apply.rs`; `crates/editac-session/tests/review_apply.rs`; `../architecture/specs/change-diffs.md`; `../architecture/specs/verification.md`.
Dependencies: DIF-1.3, DIF-1.4.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Stale proposals and invalid partial syntax reject with base/current/proposed recovery; accepted changes update existing identities instead of reimporting the document.

Implementation:

- [ ] DIF-1.5-I1 Translate accepted full/partial proposals via source reconciliation or semantic commands, revalidate the live revision and preserve history/origin policy.

Validation:

- [ ] DIF-1.5-V1 cargo test -p editac-session --test review_apply --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `DIF-1.5` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DIF-1.5`.
Blocked behavior: Leave `DIF-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task DIF-1.6 — Build accessible web change views

- [ ] DIF-1.6 Build accessible web change views.

Purpose: Build accessible web change views as one bounded reusable delivery boundary.
Context: `packages/web/src/review/`; `tests/browser/review.spec.ts`; `../architecture/specs/change-diffs.md`; `../architecture/specs/verification.md`.
Dependencies: DIF-1.3, DIF-1.4.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Content and formatting differences are distinguishable; readonly/history views expose no mutation controls; large views remain bounded and labels explain representation.

Implementation:

- [ ] DIF-1.6-I1 Render inline/unified/side-by-side views from the portable change model with keyboard/screen-reader labels, whitespace controls and stable selection.

Validation:

- [ ] DIF-1.6-V1 npm run test:browser -- review. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `DIF-1.6` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DIF-1.6`.
Blocked behavior: Leave `DIF-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task DIF-1.7 — Implement historical inspection and restore as edit

- [ ] DIF-1.7 Implement historical inspection and restore as edit.

Purpose: Implement historical inspection and restore as edit as one bounded reusable delivery boundary.
Context: `packages/web/src/review/history.ts`; `tests/browser/history-review.spec.ts`; `../architecture/specs/change-diffs.md`; `../architecture/specs/verification.md`.
Dependencies: DIF-1.5, DIF-1.6.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Inspecting an old revision never rewinds the live replica; restoration while another peer edits either revalidates safely or conflicts visibly.

Implementation:

- [ ] DIF-1.7-I1 Display immutable available revisions and provenance; preview restoration as a new current-state-checked semantic edit. Retain unknown attribution labels and unavailable-history results.

Validation:

- [ ] DIF-1.7-V1 npm run test:browser -- history-review. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `DIF-1.7` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DIF-1.7`.
Blocked behavior: Leave `DIF-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task DIF-1.8 — Qualify Git-like fidelity and cross-client model

- [ ] DIF-1.8 Qualify Git-like fidelity and cross-client model.

Purpose: Qualify Git-like fidelity and cross-client model as one bounded reusable delivery boundary.
Context: `crates/editac-diff/tests/git_goldens.rs`; `tests/browser/review-concurrent.spec.ts`; `../architecture/evidence/change-diffs.md`; `../architecture/specs/change-diffs.md`; `../architecture/specs/verification.md`.
Dependencies: DIF-1.7.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Exact hashes round-trip, exit1 from Git differences is handled correctly, no author claim exceeds evidence and recorded large-diff budgets are honest.

Implementation:

- [ ] DIF-1.8-I1 Run pinned git diff --no-index golden comparisons and semantic cases with a prepared concurrent peer; export a versioned change model for terminal/native presenters.

Validation:

- [ ] DIF-1.8-V1 cargo test -p editac-diff --locked; npm run test:browser -- review-concurrent. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `DIF-1.8` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DIF-1.8`.
Blocked behavior: Leave `DIF-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.
