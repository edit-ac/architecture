# Build the editing regression suite and architecture guards

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Read [suite contract](../specs/editing-regression-suite.md), [new regression cases](../tests/editor-regression-cases.md), the active recipe/guard in [suite.json](../tests/editing-suite/suite.json), and task-local paths. Paths below are core-relative unless explicitly prefixed. The current architecture validator checks planning consistency; this roadmap implements and runs real drivers/assertions.

Upstream entry gate: `08-sdk-integration.md` complete at reviewed current source/implementation revisions with passing packed-engine/browser evidence. Earlier engine/input/format tests remain with their owners. Track 38 requires this common suite infrastructure; tracks 40/41 inherit it without adding runtime dependencies. This track's completion proves its own recipes/guards, not every future catalog/device cell.

The [baseline typing/rendering gate](../specs/web.md#baseline-typing-and-rendering-guarantees) runs independently before this infrastructure exists. Bind its permanent renderer/keyboard/example regressions into future coverage reports while retaining the baseline command, independent expectations and visible-space assertions. A planned recipe never substitutes for those executed tests.

## Execution rules

The controller owns this source. Keep checkmarks, exact counts and handoff in separate progress. Implement one parent per iteration, normally 15–45 minutes plus checks; propose a controller split if a boundary outgrows it. Local Dependencies contain only IDs in this file. Create named scripts/suites first; zero matching tests and missing commands fail. Use deterministic fixtures/mock external transports, real engine/adapters, fixed clocks and independently authored expected outcomes. No paid inference, secrets loading, live provider recording or automatic golden updates. Preserve failing traces and distinguish validation-only, semantic, synthetic replay, real-browser and actual-device evidence. Track/clean up owned test resources and preserve others' processes and work.

## Epic RGS-1 — Prove editing invariants at their owning boundaries

### Task RGS-1.1 — Bind the shared regression fixture and driver contract

- [ ] RGS-1.1 Bind the shared regression fixture and driver contract.

Purpose: Bind the shared regression fixture and driver contract as one bounded fixture/behavior boundary.
Context: `tests/editing/fixture-loader.ts`; `tests/editing/driver.ts`; `tests/editing/fixture-loader.test.mjs`; [suite contract](../specs/editing-regression-suite.md); [suite manifest](../tests/editing-suite/suite.json); [new cases](../tests/editor-regression-cases.md). [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: none.
Session scope: One named group and directly required adapter/test glue; preserve unrelated active engine work and schema contracts.
Acceptance: The architecture suite manifest/recipes load against declared capabilities with stable logical-to-engine ID mapping and independent snapshots. Case links do not imply complete variant coverage or executed results; missing engine/profile support is explicit. Index the additional catalog and its platform/profile variants without assigning passed status to metadata. Existing recipe drivers admit the selected replacement checkpoints.

Implementation:

- [ ] RGS-1.1-I1 Create the shared real-engine driver ports, typed action/result/snapshot adapter, deterministic clock and group dispatcher. Consume architecture JSON without copying a second authoritative fixture catalog; map required capabilities and retain invalid-input actions while rejecting invalid expected states.

Validation:

- [ ] RGS-1.1-V1 node --test tests/editing/fixture-loader.test.mjs. Use actual packed engine handles and deliberate wrong expected snapshots/IDs/ranges. Mark corpus binding separately from runtime behavior; reject auto-generated goldens and unknown groups. Record exact command/exit, nonzero executed/passed/failed/skipped counts and immutable source/fixture/profile hashes.

Evidence: Separate progress entry `RGS-1.1` identifies actual driver/engine revisions, every executed recipe/guard/case variant and retained raw artifacts under `../architecture/evidence/editing-regression-suite/`.
Handoff: Record the last completed substep, changed symbols/paths, minimal failing trace or missing capability and next bounded action.
Blocked behavior: Leave `RGS-1.1` unchecked with owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task RGS-1.2 — Qualify atomic command and selection recipes

- [ ] RGS-1.2 Qualify atomic command and selection recipes.

Purpose: Qualify atomic command and selection recipes as one bounded fixture/behavior boundary.
Context: `crates/editac-core/tests/editing_regressions.rs`; `tests/editing/semantic-adapter.ts`; `tests/editing/semantic.test.mjs`; [suite contract](../specs/editing-regression-suite.md); [suite manifest](../tests/editing-suite/suite.json); [new cases](../tests/editor-regression-cases.md).
Dependencies: RGS-1.1.
Session scope: One named group and directly required adapter/test glue; preserve unrelated active engine work and schema contracts.
Acceptance: SEQ-01–SEQ-07, SEQ-11 and SEQ-12 pass their representative checkpoints; REG-05/06/07/13 variants have complete owning assertions. Guards G02/G03/G04/G06 cover compound atomicity, resulting selection, pending marks and independent UTF-16/grapheme behavior. SEQ-13/SEQ-14 add independent backward-selection Enter/hard-break, sentinel and undo/redo checkpoints; unsupported primitives remain blocked.

Implementation:

- [ ] RGS-1.2-I1 Reuse qualified prepared operations. If current plain-text, format or structure APIs cannot express one atomic action with its selection policy, stop with the upstream engine gap; do not sequentially commit or weaken the recipe. Add schema-crossing suffix preservation, separated pre fragments, block-attribute/pending-mark and invalid-final-operation variants.

Validation:

- [ ] RGS-1.2-V1 npm run test:editing -- --group semantic. Run matching native Rust and WASM vectors with nonzero test counts. Assert document/marks/identity, pending null versus empty, direction/affinity, revisions/state vectors and zero effects on rejection; corrupted expectations must fail. Record exact command/exit, nonzero executed/passed/failed/skipped counts and immutable source/fixture/profile hashes.

Evidence: Separate progress entry `RGS-1.2` identifies actual driver/engine revisions, every executed recipe/guard/case variant and retained raw artifacts under `../architecture/evidence/editing-regression-suite/`.
Handoff: Record the last completed substep, changed symbols/paths, minimal failing trace or missing capability and next bounded action.
Blocked behavior: Leave `RGS-1.2` unchecked with owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task RGS-1.3 — Qualify history boundaries and rebased selection

- [ ] RGS-1.3 Qualify history boundaries and rebased selection.

Purpose: Qualify history boundaries and rebased selection as one bounded fixture/behavior boundary.
Context: `crates/editac-core/tests/editing_history.rs`; `tests/editing/history.test.mjs`; [suite contract](../specs/editing-regression-suite.md); [suite manifest](../tests/editing-suite/suite.json); [new cases](../tests/editor-regression-cases.md).
Dependencies: RGS-1.2.
Session scope: One named group and directly required adapter/test glue; preserve unrelated active engine work and schema contracts.
Acceptance: SEQ-03/SEQ-08 and REG-01–REG-04 pass. Guard G07 proves single-character paste/cut isolation, transaction-entry selection, remote preservation and inverse/reapplied mapping under a fixed clock; missing history origin support blocks acceptance. Include REG-01's heading-before-list history-selection variant and `npm run test:browser -- history-selection` (permanent failing regression in `tests/browser/history-selection.spec.ts`). `evidence/baseline-typing/baseline-1/` preserves the 2026-10-12 failure where paragraph removal clears selection. Baseline content-history success does not complete this selection criterion.

Implementation:

- [ ] RGS-1.3-I1 Use the qualified engine history origin/grouping policy and a deterministic clock. Implement temporary-selection-before-first-operation, typing/paste/typing, cut, local/remote and pending-local-rebase sequences with checkpoints for every undo and redo.

Validation:

- [ ] RGS-1.3-V1 npm run test:editing -- --group history. Compare exact document and selection after every boundary. Deliberately merge a paste group or corrupt a mapped bookmark to prove assertions detect the regression; record fixed scheduler/clock policy and exact actor traces. Record exact command/exit, nonzero executed/passed/failed/skipped counts and immutable source/fixture/profile hashes.

Evidence: Separate progress entry `RGS-1.3` identifies actual driver/engine revisions, every executed recipe/guard/case variant and retained raw artifacts under `../architecture/evidence/editing-regression-suite/`.
Handoff: Record the last completed substep, changed symbols/paths, minimal failing trace or missing capability and next bounded action.
Blocked behavior: Leave `RGS-1.3` unchecked with owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task RGS-1.4 — Build deterministic browser input and settling probes

- [ ] RGS-1.4 Build deterministic browser input and settling probes.

Purpose: Build deterministic browser input and settling probes as one bounded fixture/behavior boundary.
Context: `tests/editing/browser-driver.ts`; `tests/browser/editing-input.spec.ts`; `packages/web/src/input/`; [suite contract](../specs/editing-regression-suite.md); [suite manifest](../tests/editing-suite/suite.json); [new cases](../tests/editor-regression-cases.md).
Dependencies: RGS-1.1, RGS-1.2.
Session scope: One named group and directly required adapter/test glue; preserve unrelated active engine work and schema contracts.
Acceptance: SEQ-10, REG-14 and REG-16 pass mechanically through the real adapter. G01/G05/G09 distinguish observed notifications from actual intents, composition commit keys from deliberate commands and renderer echoes from genuine input.

Implementation:

- [ ] RGS-1.4-I1 Verify and reuse the input/composition ADR and protocol qualification delivered by WEB-1.13, including its correlation identity, terminal disposition and evidence limits. Qualify the shared recipe driver against the completed production input/composition adapter. Drive prepared missing/noncancelable/observer-first/duplicate sequences, use real DOM mutations and actual handlers, and expose bounded generation-aware quiescence without fixed sleeps. Missing or stale ADR evidence remains a prerequisite gap; this task does not replace the pre-WEB-1.4 qualification.

Validation:

- [ ] RGS-1.4-V1 npm run test:editing -- --group input. Assert content, caret, commit/update/history/journal counters where attached; follow duplicate-notification traces with an identical deliberate edit. WebDriver native-interaction and actual OS evidence remain separately named, not inferred from synthetic replay. Record exact command/exit, nonzero executed/passed/failed/skipped counts and immutable source/fixture/profile hashes.

Evidence: Separate progress entry `RGS-1.4` identifies actual driver/engine revisions, every executed recipe/guard/case variant and retained raw artifacts under `../architecture/evidence/editing-regression-suite/`.
Handoff: Record the last completed substep, changed symbols/paths, minimal failing trace or missing capability and next bounded action.
Blocked behavior: Leave `RGS-1.4` unchecked with owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task RGS-1.5 — Add bounded property and interleaving tests

- [ ] RGS-1.5 Add bounded property and interleaving tests.

Purpose: Add bounded property and interleaving tests as one bounded fixture/behavior boundary.
Context: `crates/editac-core/tests/editing_properties.rs`; `tests/editing/generators/`; `fixtures/editing-failures/`; [suite contract](../specs/editing-regression-suite.md); [suite manifest](../tests/editing-suite/suite.json); [new cases](../tests/editor-regression-cases.md).
Dependencies: RGS-1.2, RGS-1.3.
Session scope: One named group and directly required adapter/test glue; preserve unrelated active engine work and schema contracts.
Acceptance: REG-08 and G10 pass fixed-point, resource-bound and schema-preservation checks. Seeded valid-command, normalization and replica-interleaving properties preserve independent content/selection invariants; failures shrink reproducibly.

Implementation:

- [ ] RGS-1.5-I1 Create small schema-aware generators and reducers, reusing existing fixtures and engine operations. Pin Unicode vectors/versions, seeds and scheduling. Cover atomic rejection, normalization idempotence, supported round trips, duplicate/reordered updates and valid anchored selection; retain unknown data under declared profiles.

Validation:

- [ ] RGS-1.5-V1 npm run test:editing -- --group properties. Run bounded deterministic seeds and injected counterexamples. Record actual sample/case counts, maximal lengths, failures/skips and minimized traces; a passing random sample never replaces fixed regressions or real-device evidence. Record exact command/exit, nonzero executed/passed/failed/skipped counts and immutable source/fixture/profile hashes.

Evidence: Separate progress entry `RGS-1.5` identifies actual driver/engine revisions, every executed recipe/guard/case variant and retained raw artifacts under `../architecture/evidence/editing-regression-suite/`.
Handoff: Record the last completed substep, changed symbols/paths, minimal failing trace or missing capability and next bounded action.
Blocked behavior: Leave `RGS-1.5` unchecked with owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task RGS-1.6 — Probe callback failure and asynchronous lifetime safety

- [ ] RGS-1.6 Probe callback failure and asynchronous lifetime safety.

Purpose: Probe callback failure and asynchronous lifetime safety as one bounded fixture/behavior boundary.
Context: `tests/editing/failure-injection.test.mjs`; `tests/browser/editing-lifetime.spec.ts`; `packages/web/src/commands/`; [suite contract](../specs/editing-regression-suite.md); [suite manifest](../tests/editing-suite/suite.json); [new cases](../tests/editor-regression-cases.md).
Dependencies: RGS-1.3, RGS-1.4.
Session scope: One named group and directly required adapter/test glue; preserve unrelated active engine work and schema contracts.
Acceptance: SEQ-09, REG-12 and REG-15 pass. G08/G11 require post-transaction callbacks, explicit deferred/rejected reentrancy, recoverable stale targets and inert callbacks after disposal. Existing commits survive subscriber exceptions.

Implementation:

- [ ] RGS-1.6-I1 Inject final prepare failures, subscriber exceptions/commands/unsubscribe/destroy, canceled providers and target/session deletion with prepared transports. Observe real port boundaries rather than fabricate commit counters. Specify callback scheduling and cancellation ownership before implementation.

Validation:

- [ ] RGS-1.6-V1 npm run test:editing -- --group failures. Compare pre/post state vectors, semantic state, history, publication and persistence counts; drain bounded queues and verify no detached DOM write/refocus/resource leak. Keep independent remote/OS effects attributed separately. Record exact command/exit, nonzero executed/passed/failed/skipped counts and immutable source/fixture/profile hashes.

Evidence: Separate progress entry `RGS-1.6` identifies actual driver/engine revisions, every executed recipe/guard/case variant and retained raw artifacts under `../architecture/evidence/editing-regression-suite/`.
Handoff: Record the last completed substep, changed symbols/paths, minimal failing trace or missing capability and next bounded action.
Blocked behavior: Leave `RGS-1.6` unchecked with owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task RGS-1.7 — Qualify presenter and nested event ownership regressions

- [ ] RGS-1.7 Qualify presenter and nested event ownership regressions.

Purpose: Qualify presenter and nested event ownership regressions as one bounded fixture/behavior boundary.
Context: `tests/browser/editing-presenters.spec.ts`; `packages/web/src/dom/`; `packages/web/src/modules/`; [suite contract](../specs/editing-regression-suite.md); [suite manifest](../tests/editing-suite/suite.json); [new cases](../tests/editor-regression-cases.md).
Dependencies: RGS-1.4, RGS-1.6.
Session scope: One named group and directly required adapter/test glue; preserve unrelated active engine work and schema contracts.
Acceptance: REG-09/10/11/17 and G12/G13 pass: tag/view changes retain identity, nested controls own input/clipboard, drop commits once, and widget insertion anchors differ from explicit node selection. Use prepared registry fixtures to falsify event/command precedence for official profile contracts; actual FPX combinations remain with EXT/RCH/platform feature owners and do not create a downstream entry dependency.

Implementation:

- [ ] RGS-1.7-I1 Create minimal real custom-view fixtures for tag replacement, delayed mount, before/after-widget insertion and retained outer selection during inner-input paste/secondary insertion. Add base cases before composition/remote/drag variants; reuse module commands and shared dispatcher.

Validation:

- [ ] RGS-1.7-V1 npm run test:editing -- --group presenters. Observe actual DOM selection/focus, next typed sentinel, semantic identity, effect counts and teardown. Run supported WebDriver actions separately from injected notifications and record platform cases requiring native input evidence. Record exact command/exit, nonzero executed/passed/failed/skipped counts and immutable source/fixture/profile hashes.

Evidence: Separate progress entry `RGS-1.7` identifies actual driver/engine revisions, every executed recipe/guard/case variant and retained raw artifacts under `../architecture/evidence/editing-regression-suite/`.
Handoff: Record the last completed substep, changed symbols/paths, minimal failing trace or missing capability and next bounded action.
Blocked behavior: Leave `RGS-1.7` unchecked with owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task RGS-1.8 — Publish honest suite coverage and CI gates

- [ ] RGS-1.8 Publish honest suite coverage and CI gates.

Purpose: Publish honest suite coverage and CI gates as one bounded fixture/behavior boundary.
Context: `scripts/check-editing-coverage.mjs`; `tests/editing/coverage.test.mjs`; `.github/workflows/`; `../architecture/evidence/editing-regression-suite/`; [suite contract](../specs/editing-regression-suite.md); [suite manifest](../tests/editing-suite/suite.json); [new cases](../tests/editor-regression-cases.md).
Dependencies: RGS-1.2, RGS-1.3, RGS-1.4, RGS-1.5, RGS-1.6, RGS-1.7.
Session scope: One named group and directly required adapter/test glue; preserve unrelated active engine work and schema contracts.
Acceptance: All common-driver recipes, new REG cases and fourteen guard negative controls have nonzero actual evidence at matching revisions. Remaining original catalog rows retain planned/unexecuted status until their owners implement them; metadata validation cannot mark them passed. G14 rejects missing/stale/fabricated evidence. Report additional desktop/native/preset/performance cases by owning task and layer; infrastructure completion never substitutes for real gesture/device/performance qualification.

Implementation:

- [ ] RGS-1.8-I1 Create the binding/receipt format, per-layer runner reports and bounded CI groups. Reuse dispatchers in INT/MWB/MWX instead of duplicating fixtures. Report all catalog IDs, variant completeness, implementation/profile/fixture revisions and actual assertion/device counts; wire later release gates to mandatory coverage.

Validation:

- [ ] RGS-1.8-V1 npm run test:editing -- --group all; node scripts/check-editing-coverage.mjs --profile infrastructure. Prove receipt rejection with wrong expected state, missing case, zero assertions, skipped mandatory checks and stale/incorrect platform revisions. Infrastructure completion does not claim all catalog/device support; hand the shared harness to tracks 38/40/41 and keep their qualification gates. Record exact command/exit, nonzero executed/passed/failed/skipped counts and immutable source/fixture/profile hashes.

Evidence: Separate progress entry `RGS-1.8` identifies actual driver/engine revisions, every executed recipe/guard/case variant and retained raw artifacts under `../architecture/evidence/editing-regression-suite/`.
Handoff: Record the last completed substep, changed symbols/paths, minimal failing trace or missing capability and next bounded action.
Blocked behavior: Leave `RGS-1.8` unchecked with owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

