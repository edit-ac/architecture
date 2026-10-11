# Build the continuous browser editing surface

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Deliver only the outcomes below. Read `../architecture/specs/web.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Upstream entry gates: `02-engine.md` complete at current source revision with passing artifact evidence, `03-local-storage.md` complete at current source revision with passing artifact evidence.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus validation; if a boundary is too large, stop with a precise proposed split for the controller. Pick a task only when every named dependency is implemented and validated. Other ready tasks are permitted independent work; a roadmap entry gate remains mandatory for its dependents. Do not launch this roadmap while its upstream gate is unavailable.

Create named checks before invoking them. Record nonzero executed/passed/failed/skipped counts; missing tests and zero-match Rust filters fail acceptance. Run the narrow check, then relevant integration checks. Use prepared fixtures and transports only. No model API tests, live dogfood, background runner startup or publication outside an explicit release task.

## Epic WEB-1 — Build the continuous browser editing surface

### Task WEB-1.1 — Verify engine, storage and WASM entry contracts

- [ ] WEB-1.1 Verify engine, storage and WASM entry contracts.

Purpose: Deliver verify engine, storage and WASM entry contracts as one reviewable boundary.
Context: `packages/core/`; `packages/web/`; `../architecture/specs/web.md`; `../architecture/specs/web.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Real engine and persistence attach before ready; missing prerequisites leave this track blocked with exact evidence gaps.

Implementation:

- [ ] WEB-1.1-I1 Confirm engine patches/anchors, local flush, WASM init and storage recovery evidence; make the browser fixture load the real packed core.

Validation:

- [ ] WEB-1.1-V1 npm run build:wasm; npm run test:browser -- recovery. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.1` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.1`.
Blocked behavior: Leave `WEB-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.2 — Render and map a single contenteditable root

- [ ] WEB-1.2 Render and map a single contenteditable root.

Purpose: Deliver render and map a single contenteditable root as one reviewable boundary.
Context: `packages/web/src/dom/render.ts`; `tests/browser/render.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Text/heading/marks/lists render; a one-character edit does not replace unrelated nodes; read-only rendering uses safe text/attributes.

Implementation:

- [ ] WEB-1.2-I1 Render semantic blocks/marks in one contenteditable root, with stable node-to-DOM mapping and explicit noneditable atoms. Patch only changed spans.

Validation:

- [ ] WEB-1.2-V1 npm run test:browser -- render. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.2` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.2`.
Blocked behavior: Leave `WEB-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.3 — Map DOM selections to relative anchors

- [ ] WEB-1.3 Map DOM selections to relative anchors.

Purpose: Deliver map DOM selections to relative anchors as one reviewable boundary.
Context: `packages/web/src/dom/selection.ts`; `tests/browser/selection.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Cross-block, emoji, empty-block and deleted-node selections have stable tested behavior without stale absolute targets.

Implementation:

- [ ] WEB-1.3-I1 Translate forward/backward multi-block selections, caret affinity and UTF-16 positions to engine anchors. Restore selection after local/remote patches.

Validation:

- [ ] WEB-1.3-V1 npm run test:browser -- selection. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.3` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.3`.
Blocked behavior: Leave `WEB-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.4 — Reconcile ordinary input exactly once

- [ ] WEB-1.4 Reconcile ordinary input exactly once.

Purpose: Deliver reconcile ordinary input exactly once as one reviewable boundary.
Context: `packages/web/src/input/text.ts`; `tests/browser/input.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Typing/deleting never double-applies, model and DOM agree after each input, and unrelated DOM remains intact.

Implementation:

- [ ] WEB-1.4-I1 Handle cancelable beforeinput commands and native browser input reconciliation for ordinary insert/delete. Suppress observer echoes and emit one prepared semantic operation.

Validation:

- [ ] WEB-1.4-V1 npm run test:browser -- input. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.4`.
Blocked behavior: Leave `WEB-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.5 — Support noncancelable input fallback

- [ ] WEB-1.5 Support noncancelable input fallback.

Purpose: Deliver support noncancelable input fallback as one reviewable boundary.
Context: `packages/web/src/input/reconcile.ts`; `tests/browser/reconcile.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.4.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Prepared spellcheck/autocorrect/paste-like mutation fixtures reconcile once or surface an explicit unsupported recovery state; no whole-document HTML diff.

Implementation:

- [ ] WEB-1.5-I1 Handle input events without usable beforeinput and a bounded MutationObserver fallback. Limit reconciliation to known affected blocks and guard renderer-authored mutations.

Validation:

- [ ] WEB-1.5-V1 npm run test:browser -- reconcile. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.5`.
Blocked behavior: Leave `WEB-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.6 — Preserve local composition ownership

- [ ] WEB-1.6 Preserve local composition ownership.

Purpose: Deliver preserve local composition ownership as one reviewable boundary.
Context: `packages/web/src/input/composition.ts`; `tests/browser/composition.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.5.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Multi-event composition generates one intended edit with no intermediate renderer replacement; cancel/blur paths do not duplicate or discard committed input.

Implementation:

- [ ] WEB-1.6-I1 Track composition lifecycle, baseline anchors and final commit boundary. Keep the active composing subtree browser-owned and group one completed composition intentionally in history.

Validation:

- [ ] WEB-1.6-V1 npm run test:browser -- composition. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.6` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.6`.
Blocked behavior: Leave `WEB-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.7 — Reconcile remote edits during composition

- [ ] WEB-1.7 Reconcile remote edits during composition.

Purpose: Deliver reconcile remote edits during composition as one reviewable boundary.
Context: `packages/web/src/input/composition.ts`; `tests/browser/composition-remote.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.6.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Remote insert and remote delete of the target do not silently overwrite local composition or redirect text; stale targets produce an explicit result.

Implementation:

- [ ] WEB-1.7-I1 Buffer/defer patches touching composition while applying independent remote changes. Define target-deleted behavior that preserves captured composition text for recovery.

Validation:

- [ ] WEB-1.7-V1 npm run test:browser -- composition-remote. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.7` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.7`.
Blocked behavior: Leave `WEB-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.8 — Bridge structural keyboard commands and undo

- [ ] WEB-1.8 Bridge structural keyboard commands and undo.

Purpose: Deliver bridge structural keyboard commands and undo as one reviewable boundary.
Context: `packages/web/src/input/keyboard.ts`; `tests/browser/keyboard.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.7.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Cross-block splits/joins and list indentation preserve selection; keyboard/menu undo use only the semantic history and remote edits stay excluded.

Implementation:

- [ ] WEB-1.8-I1 Handle Enter/Backspace/Tab/list navigation and platform historyUndo/historyRedo using engine commands; retain native navigation where correct. Add toolbar command applicability.

Validation:

- [ ] WEB-1.8-V1 npm run test:browser -- keyboard. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.8` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.8`.
Blocked behavior: Leave `WEB-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.9 — Implement internal-fragment and literal clipboard

- [ ] WEB-1.9 Implement internal-fragment and literal clipboard.

Purpose: Deliver implement internal-fragment and literal clipboard as one reviewable boundary.
Context: `packages/web/src/clipboard/fragment.ts`; `tests/browser/clipboard.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.8.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Copy/cut across blocks round-trips supported semantics; malformed payloads never execute markup or cause partial edits; literal paste remains literal.

Implementation:

- [ ] WEB-1.9-I1 Version internal fragment payloads, validate bounds/schema, add copy/cut and literal paste, and keep paste into code literal. Fall back safely from invalid fragments.

Validation:

- [ ] WEB-1.9-V1 npm run test:browser -- clipboard. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.9` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.9`.
Blocked behavior: Leave `WEB-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.10 — Implement visible and ready lifecycle

- [ ] WEB-1.10 Implement visible and ready lifecycle.

Purpose: Deliver implement visible and ready lifecycle as one reviewable boundary.
Context: `packages/web/src/lifecycle.ts`; `tests/browser/lifecycle.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.9.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Stale preview cannot become editable and overwrite recovery; network is unnecessary for local activation; initialization failure leaves an accessible recovery view.

Implementation:

- [ ] WEB-1.10-I1 Adopt revision/schema-tagged previews only when matching recovered state; otherwise replace them before enabling input. Expose visible, ready, localCommitted and failed/recovery states.

Validation:

- [ ] WEB-1.10-V1 npm run test:browser -- lifecycle. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.10` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.10`.
Blocked behavior: Leave `WEB-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.11 — Dispose editor resources predictably

- [ ] WEB-1.11 Dispose editor resources predictably.

Purpose: Deliver dispose editor resources predictably as one reviewable boundary.
Context: `packages/web/src/editor.ts`; `tests/browser/dispose.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.10.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Repeated create/edit/destroy reaches a stable resource plateau; pending operations cannot mutate a destroyed editor; unsaved flush failures are observable.

Implementation:

- [ ] WEB-1.11-I1 Destroy observers/listeners/timers/subscriptions and WASM handles; abort pending async preparation. Define flush-before-destroy policy and idempotence.

Validation:

- [ ] WEB-1.11-V1 npm run test:browser -- dispose. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.11` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.11`.
Blocked behavior: Leave `WEB-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.12 — Add accessibility checks and device test protocol

- [ ] WEB-1.12 Add accessibility checks and device test protocol.

Purpose: Deliver add accessibility checks and device test protocol as one reviewable boundary.
Context: `tests/manual/browser-input.md`; `tests/browser/accessibility.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.11.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Automated mechanics pass and the manual protocol lists steps/expected outcomes and required devices. Device availability does not block this implementation track; actual support evidence belongs to REL-1.6.

Implementation:

- [ ] WEB-1.12-I1 Add automated semantics/keyboard tests and a runnable manual protocol for real IME, RTL, screen readers, autocorrect and mobile selection. Label actual device runs as final qualification work.

Validation:

- [ ] WEB-1.12-V1 npm run test:browser -- accessibility; review tests/manual/browser-input.md for complete cases. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.12` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.12`.
Blocked behavior: Leave `WEB-1.12` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.
