# Build bounded optional editor modules

Status: IN_PROGRESS

Qualification amendment (user decision, 2026-10-14): Physical devices, named target-platform simulators/emulators and desktop OS VMs/test hosts are accepted for platform and release qualification under the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms). Missing physical hardware does not block completion. Execute required behavior against the implemented target-platform runtime; document and test virtual equivalents for unavailable hardware-only input/accessibility cases. Record physical versus virtual provenance and measure performance in the tested environment. This supersedes earlier physical-only or manual-only clauses below; it does not complete unchecked tasks or waive implementation, correctness, security or artifact gates.

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Deliver only the outcomes below. Read `../architecture/specs/modules-native.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Upstream entry gates: `05-markdown-content.md` complete at current source revision with passing artifact evidence, `06-synchronization.md` complete at current source revision with passing artifact evidence.

Controller handoff (2026-10-13): The user instructed "Assume roadmap 5 as completed" in the roadmap 06 continuation and queued this track after roadmap 06. For this continuation, accept roadmap 05 as the upstream baseline by user instruction; retain its outstanding FMT-1.15 physical or virtual platform qualification and do not claim that evidence exists. Roadmap 06 must still complete at its current source revision before this runner starts. Queue receipt: `../../evidence/roadmap-07-runner/queue.json`.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus validation; if a boundary is too large, stop with a precise proposed split for the controller. Pick a task only when every named dependency is implemented and validated. Other ready tasks are permitted independent work; a roadmap entry gate remains mandatory for its dependents. Do not launch this roadmap while its upstream gate is unavailable.

Create named checks before invoking them. Record nonzero executed/passed/failed/skipped counts; missing tests and zero-match Rust filters fail acceptance. Run the narrow check, then relevant integration checks. Use prepared fixtures and transports only. No model API tests, live dogfood, background runner startup or publication outside an explicit release task.

## Epic MOD-1 — Build bounded optional editor modules

### Task MOD-1.1 — Verify portable extension entry gate

- [ ] MOD-1.1 Verify portable extension entry gate.

Purpose: Deliver verify portable extension entry gate as one reviewable boundary.
Context: `crates/editac-core/`; `packages/web/`; `../architecture/specs/schema-v1.md`; `../architecture/specs/modules-native.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: The same descriptors are understood by Rust and web without executable callbacks stored in documents.

Implementation:

- [ ] MOD-1.1-I1 Confirm schema descriptors, patches, move policy, fallback import and browser command surfaces. Create extension conformance fixtures.

Validation:

- [ ] MOD-1.1-V1 cargo test -p editac-core --test patches --test moves --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `MOD-1.1` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `MOD-1.1`.
Blocked behavior: Leave `MOD-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task MOD-1.2 — Implement declarative mark and atom registration

- [ ] MOD-1.2 Implement declarative mark and atom registration.

Purpose: Deliver implement declarative mark and atom registration as one reviewable boundary.
Context: `crates/editac-core/src/modules/registry.rs`; `tests/module-contract.test.mjs`; `../architecture/specs/modules-native.md`.
Dependencies: MOD-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Duplicate/incompatible definitions reject cleanly; unknown/absent renderers retain original attributes/content and show safe fallback.

Implementation:

- [ ] MOD-1.2-I1 Validate namespace/version/attributes/content shape and fallback descriptors before mount; add a custom mark and inline atom fixture without core-specific branches.

Validation:

- [ ] MOD-1.2-V1 npm run build; node --test tests/module-contract.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `MOD-1.2` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `MOD-1.2`.
Blocked behavior: Leave `MOD-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task MOD-1.3 — Implement scoped module subscriptions

- [ ] MOD-1.3 Implement scoped module subscriptions.

Purpose: Deliver implement scoped module subscriptions as one reviewable boundary.
Context: `packages/web/src/modules/runtime.ts`; `tests/module-runtime.test.mjs`; `../architecture/specs/modules-native.md`.
Dependencies: MOD-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Unrelated updates do not invoke modules; errors are isolated; selection changes do not recreate unchanged atom views.

Implementation:

- [ ] MOD-1.3-I1 Subscribe by kind/range/selection and provide lifecycle disposal plus stable renderer updates. Avoid running every module for every keystroke.

Validation:

- [ ] MOD-1.3-V1 npm run build; node --test tests/module-runtime.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `MOD-1.3` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `MOD-1.3`.
Blocked behavior: Leave `MOD-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task MOD-1.4 — Implement slash command trigger and presenter

- [ ] MOD-1.4 Implement slash command trigger and presenter.

Purpose: Deliver implement slash command trigger and presenter as one reviewable boundary.
Context: `packages/web/src/modules/slash.ts`; `tests/browser/slash.spec.ts`; `../architecture/specs/modules-native.md`.
Dependencies: MOD-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Remote, pasted and unclassified replacement input never auto-open the menu. Follow specs/editor-interactions.md for eligible triggers, keyboard dispatch, query retention, composite focus and IME priority; committed commands use one history group. INT-1.9 owns complete regression coverage.

Implementation:

- [ ] MOD-1.4-I1 Add local bounded trigger matching and accessible keyboard/touch menu invoking registered commands; include focus restoration and cancellation.

Validation:

- [ ] MOD-1.4-V1 npm run test:browser -- slash. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `MOD-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `MOD-1.4`.
Blocked behavior: Leave `MOD-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task MOD-1.5 — Implement cancellable reference suggestions

- [ ] MOD-1.5 Implement cancellable reference suggestions.

Purpose: Deliver implement cancellable reference suggestions as one reviewable boundary.
Context: `packages/web/src/modules/references.ts`; `tests/browser/references.spec.ts`; `../architecture/specs/modules-native.md`.
Dependencies: MOD-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Out-of-order responses cannot insert stale results; opening a document makes no implicit resolver/network call; unknown targets preserve labels.

Implementation:

- [ ] MOD-1.5-I1 Store host-owned target identity and label fallback; add explicit host resolver with cancellation/stale-result guard and accessible menu.

Validation:

- [ ] MOD-1.5-V1 npm run test:browser -- references. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `MOD-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `MOD-1.5`.
Blocked behavior: Leave `MOD-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task MOD-1.6 — Expose reorder UI using semantic move

- [ ] MOD-1.6 Expose reorder UI using semantic move.

Purpose: Deliver expose reorder UI using semantic move as one reviewable boundary.
Context: `packages/web/src/modules/reorder.ts`; `tests/browser/reorder.spec.ts`; `../architecture/specs/modules-native.md`.
Dependencies: MOD-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Concurrent editing during reorder retains identity/content; invalid nested targets do not mutate; keyboard path provides equivalent move control.

Implementation:

- [ ] MOD-1.6-I1 Add keyboard move and optional drag handle using engine move operation and anchors; preserve selection and accessibility feedback.

Validation:

- [ ] MOD-1.6-V1 npm run test:browser -- reorder. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `MOD-1.6` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `MOD-1.6`.
Blocked behavior: Leave `MOD-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task MOD-1.7 — Render basic image and rectangular table modules

- [ ] MOD-1.7 Render basic image and rectangular table modules.

Purpose: Deliver render basic image and rectangular table modules as one reviewable boundary.
Context: `packages/web/src/modules/content.ts`; `tests/browser/content-modules.spec.ts`; `../architecture/specs/modules-native.md`.
Dependencies: MOD-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Keyboard selection/copy and cell editing work; disabled module round-trip retains data; uploads and merged cells remain excluded.

Implementation:

- [ ] MOD-1.7-I1 Render alt text, host-provided image URLs and bounded simple table cells, with native DOM navigation and preserved fallback when modules disabled.

Validation:

- [ ] MOD-1.7-V1 npm run test:browser -- content-modules. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `MOD-1.7` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `MOD-1.7`.
Blocked behavior: Leave `MOD-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task MOD-1.8 — Build a lazy safe math example

- [ ] MOD-1.8 Build a lazy safe math example.

Purpose: Deliver build a lazy safe math example as one reviewable boundary.
Context: `packages/web/src/modules/math.ts`; `tests/browser/math.spec.ts`; `../architecture/specs/modules-native.md`.
Dependencies: MOD-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: No external macro/URL execution, bounded error handling, lazy assets absent from minimal bundle; fallback is identified as source, not typeset native math.

Implementation:

- [ ] MOD-1.8-I1 Persist bounded LaTeX source as atom, lazy-load a verified pinned renderer with trust disabled, preserve invalid source and expose source fallback.

Validation:

- [ ] MOD-1.8-V1 npm run test:browser -- math. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `MOD-1.8` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `MOD-1.8`.
Blocked behavior: Leave `MOD-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task MOD-1.9 — Publish module capability and footprint matrix

- [ ] MOD-1.9 Publish module capability and footprint matrix.

Purpose: Deliver publish module capability and footprint matrix as one reviewable boundary.
Context: `../architecture/evidence/modules.md`; `tests/module-bundles.test.mjs`; `../architecture/specs/modules-native.md`.
Dependencies: MOD-1.4, MOD-1.5, MOD-1.6, MOD-1.7, MOD-1.8.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Each advertised capability has passing fixture evidence; native preparation/fallback is distinguished from full native editing.

Implementation:

- [ ] MOD-1.9-I1 Record supported editing/rendering/export per module and platform, and inspect production bundle manifests for disabled code/assets.

Validation:

- [ ] MOD-1.9-V1 npm run build; node --test tests/module-bundles.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `MOD-1.9` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `MOD-1.9`.
Blocked behavior: Leave `MOD-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.
