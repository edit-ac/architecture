# Codex-managed editor visual QA

Status: PLANNED — preparation and execution have not started; this plan is not queued.

Requested 2026-10-23: a broad Codex session must click through rendered editor
fixtures, type and edit, exercise imports, compare imported documents with their
originals, and look for regressions and unexpected changes. Cover browsers near
internal alpha and native applications on actual simulator/emulator runtimes after
native feature delivery. This is an authored execution plan, not passing evidence.

## Timing and ownership

Prepare the corpus, gallery and runbook before the alpha candidate freezes. Run
the browser campaign against the integrated candidate when its declared web
features and focused correctness/data-safety checks are ready. Native preparation
follows native implementation; native execution remains with
[roadmap43](../roadmaps/43-physical-device-verification.md) and the corresponding
final native testing owners in the
[current readiness queue](../runner-queues/emulator-web-readiness-20261022/README.md).
Native availability does not hold the web alpha review. Native visual QA feeds the
later beta handoff; it does not require physical hardware.

The coordinator maps these tasks to existing RGS/PHY/QWB/native owners and original
case IDs before execution. This plan adds the human-style visual inspection method;
it does not replace existing semantic tests, duplicate qualification ownership, or
change a running controller's source. No runner, scheduler, emulator or server is
started by writing this plan. Use one existing root-workspace controller, with no
parallel agents or worktrees.

Entry context, read only as needed:

- [Delivery sequencing](web-feature-first-20261018.md),
  [current document format](../decisions/006-single-format-before-publication.md)
  and [durability](../specs/document-durability.md).
- [Editing regression suite](../specs/editing-regression-suite.md),
  [format contract](../specs/formats.md) and
  [existing regression roadmap](../roadmaps/42-editing-regression-suite.md).
- Local product: `core/examples/task-editor/ALPHA.md`, `README.md`, `FEATURES.md`
  and `product.mjs`; existing fixtures: `core/tests/browser/`,
  `core/tests/browser/fixture-server.mjs`, `core/tests/editing/` and
  `core/tests/formats/consumers/`.
- Native entry points: `core/tests/native/ios-control.sh`,
  `core/tests/native/android-control.sh` and `core/native/`.
  Inspect actual supported commands and capabilities before using them; their
  existence alone does not establish a visible editor or UI automation support.

## Inspection contract

Use real visible editor controls for clicks, drags, typing, selection, menus,
file picking, import confirmation, navigation and save/reopen. Prefer the Codex
in-app browser for the managed walkthrough. Use the existing Playwright harness
for repeatable browser-engine coverage and diagnostics. Native interaction must
operate the rendered application through a supported simulator/emulator UI driver;
desktop mobile viewports, injected callbacks and headless engine tests do not
establish native behavior. Keep state inspection as an independent assertion,
never as a substitute for the action being tested.

Freeze the exact source/package/build, current format, fixture hash, fonts,
locale, time zone, scale, viewport, theme and browser/OS/runtime for each result.
Wait for fonts, images and layout readiness; freeze nondeterministic content and
animations in fixture configuration. Capture meaningful checkpoints after opening,
editing, importing, undoing and reopening. Never hide selection, error messages or
other content under test with screenshot masks. A stuck loader or missing font is
a finding, not a reason to capture a blank passing frame.

Compare two independent things:

1. **Import fidelity:** render the original through its source application or an
   independent trusted reader. Compare it side by side with the imported editor at
   compatible widths and scale, with a declared construct-by-construct oracle.
   Separate supported fidelity, documented transformations and unsupported content.
   Flow-based editing can rewrap differently; lost text, marks, tables or images
   cannot be explained away as reflow. PDF is currently export-only; reject PDF
   import honestly, and inspect exported PDFs independently.
2. **Regression:** compare candidate checkpoints with a reviewed, applicable prior
   baseline using overlays/diffs and Codex visual inspection. Compare matching
   environments. Investigate antialiasing separately from geometry, clipping,
   ordering, missing content and control changes. First-time baseline capture
   requires review against the oracle; candidate output cannot approve itself.

Semantic content, selection/history and save/reopen assertions accompany visual
checks. Screenshots alone cannot prove text completeness, atomicity or durability;
semantic equality alone cannot prove an unclipped, usable editor.

## Coverage and result rules

| Area | Required journeys and observations |
| --- | --- |
| Editor content | Empty/plain documents; headings, marks, nested lists, links/references, tables, code, math, images/attachments and enabled rich blocks; long documents, long words, Unicode/emoji, RTL and mixed directions. Include optional-extension-off and readonly profiles. |
| Editing | Place/move caret; forward/backward and cross-block selection; type, Enter, Backspace/Delete; cut/copy/paste; keyboard shortcuts; toolbar/menu actions; drag/reorder; find/replace; undo/redo; focus transfer; scrolling and zoom. Check toolbar state and caret visibility. |
| Import/export | Text/Markdown, RTF, CSV/TSV, DOCX, ODT and EPUB according to declared profiles; empty/large files, supported images/tables, malformed input, wrong extension, unsupported constructs and disabled codec. Exercise picker, preview, cancel, confirm, loss diagnostics, stale target and readonly changes, undo/redo, export and reopen. Test rejection without partial mutation. |
| Product lifecycle | Task/comment isolation, React/routes and Back navigation, multiple editors, save errors, offline/reload, recovery and same-format reopen. Use the configured collaboration fixture to inspect peer edits, presence, selections and reconnect behavior; retain local-history semantics. |
| Layout/accessibility | Desktop/narrow/mobile web, supported light/dark themes and zoom, keyboard-only access, visible focus, dialogs/popovers, overflow, contrast and accessible names. Inspect native keyboard/insets, rotation, safe areas, touch selection handles and OS file/clipboard surfaces. |
| Exploratory use | Bounded charters combining actions: import → edit table → undo → save/reopen; paste Unicode into lists; resize while selecting; navigate/reload after a failed save; open menus near viewport edges. Record actions even when nothing fails. |

Build the matrix from the actual alpha feature ledger, not a claim that every
listed feature exists in the default sample. Add a visible fixture for a declared
SDK capability missing from the sample; classify unimplemented required behavior
as a defect. Original-media imports need an authorized local asset host; use
prepared local assets and report any missing integration explicitly.

Browser coverage: Chromium, Firefox and WebKit on pinned versions; complete the
core editing/import journey on all three. Use a primary desktop profile for the
full corpus, then risk-based narrow/touch/theme/zoom variants. WebKit testing does
not by itself establish Safari or iOS OS-input behavior. At matrix freeze, name
the exact supported browser claims and any required real-browser follow-up.

Native coverage: iPhone and iPad simulators, Android phone and tablet emulators;
include an oldest-supported and a current OS runtime per claimed platform where
required by the existing platform matrix. Use native macOS hosts and Windows/Linux
hosts or VMs for declared desktop-native claims. Share document expectations, but
keep platform-specific controls, fonts, input and layout expectations. Start with
one runtime per family, then execute the remaining required variants. No full
Cartesian product is necessary: every selected variant has a risk and an owner.

Every case/profile receives PASS, FAIL, BLOCKED, NOT_RUN or an explicitly justified
NOT_APPLICABLE. Required blocked/skipped cases prevent a complete result for that
profile. Report executed/passed/failed/blocked/not-run counts and distinguish
scripted observations from exploratory findings. A session's completion is not a
claim of whole-platform qualification.

## Preparation tasks

### VQA-1 — Freeze the manifest and alpha entry conditions

- [ ] VQA-1 Define the fixture, journey, environment and ownership matrix.

Purpose: Make breadth and completion measurable.
Context/paths: Feature ledger, existing case catalogs and final testing owners above;
planned authored manifest under `architecture/tests/visual-qa/`.
Dependencies: none. Independent work: VQA-2 source collection.
Scope: 30–45 minutes; inventory decisions only.
Acceptance: Every required feature/journey has stable case IDs, platform variants,
priority, expected observations and one test owner; web/native entry gates are
separate and name their concrete missing prerequisites.

Implementation:

- [ ] VQA-1-I1 Map existing cases and gaps; select representative documents and risk-based profiles. Define checkpoint names, per-session case limits and expected duration.
- [ ] VQA-1-I2 Freeze web entry on a runnable candidate with focused data-safety checks; native entry additionally requires the actual native UI, accepted runtime and existing final-testing handoff.

Validation:

- [ ] VQA-1-V1 Review links, unique IDs, owner coverage and dependencies against the feature ledger; budget 5 minutes, no application suite.

Evidence: Ignored progress records matrix revision and unresolved prerequisites.
Handoff/blocker: Next unmapped case and owner; missing runtime blocks only its profile.

### VQA-2 — Curate original documents and independent expectations

- [ ] VQA-2 Prepare the versioned input corpus and reference-render recipe.

Purpose: Detect plausible-looking but incorrect imports.
Context/paths: VQA-1 matrix, existing deterministic format fixtures;
planned input fixtures in the existing core fixture tree and authored expectations.
Dependencies: none; reconcile IDs to VQA-1 before acceptance.
Independent work: Gallery scaffolding can consume an initial small corpus.
Scope: One 30–45-minute corpus slice per supported format family; split before execution.
Acceptance: Each input has provenance/license, hash, format/profile, independent
expected text/structure/marks/assets and source-renderer details. Include simple,
complex and malformed/lossy examples; originals remain immutable.

Implementation:

- [ ] VQA-2-I1 Reuse legally usable authored fixtures; add only missing representative documents and explicit expected transformations/unsupported outcomes.
- [ ] VQA-2-I2 Specify how to reproduce source views and identify anchors/regions for side-by-side comparison. Record fonts and layout limitations; do not use the editor's own import/export as its oracle.

Validation:

- [ ] VQA-2-V1 Inspect one original and its independent structural/reference recipe per new format slice; verify hashes and coverage mapping. Budget 5–10 minutes per slice.

Evidence: Source inputs/expectations in Git; generated reference captures outside Git.
Handoff/blocker: Exact missing renderer/font/license or expectation, with acquisition owner.

### VQA-3 — Expose a navigable browser fixture gallery

- [ ] VQA-3 Make the declared editor fixtures easy for Codex to open and exercise.

Purpose: Enable visible walkthroughs of both focused fixtures and the installed product.
Context/paths: Existing browser fixture server, task-editor launcher and fixtures;
planned gallery code in the existing browser test tree.
Dependencies: VQA-1. Independent work: Complete VQA-2 alongside the gallery.
Scope: One gallery/launcher boundary, 30–45 minutes; split missing product flows by owner.
Acceptance: Stable case URLs show case ID, instructions and expected checkpoints;
reset creates disposable state without touching real documents; imports use real
UI controls. Feature combinations expose the actual production SDK/renderers.

Implementation:

- [ ] VQA-3-I1 Reuse existing servers and installed product launchers; add navigation, case filtering, deterministic reset and file-input access where missing.
- [ ] VQA-3-I2 Include original/reference access and diagnostics without changing editor behavior. Record launcher/PID/port/log ownership and graceful teardown.

Validation:

- [ ] VQA-3-V1 Open one representative fixture, type through the visible UI, reset, and verify state isolation and shutdown. Budget 5 minutes; no broad suite.

Evidence: Ignored progress with URL recipe, pins, interaction and process result.
Handoff/blocker: Missing public flow goes to its feature owner; do not bypass it by state injection.

### VQA-4 — Prepare native fixture access and UI controls

- [ ] VQA-4 Define and wire native fixture launch, reset and observation.

Purpose: Reuse the corpus on actual native editors.
Context/paths: VQA-1/VQA-2, native example apps and existing iOS/Android controls.
Dependencies: VQA-1, VQA-2; native implementation entry described above.
Independent work: Browser tasks do not depend on this task.
Scope: One platform's launch/control boundary per 30–45-minute slice.
Acceptance: Exact build/install/launch/reset/screenshot/UI-input/file-import commands
are documented for that platform with runtime IDs and teardown; unsupported driver
capabilities have a concrete fallback. No engine-only probe is labeled native UI QA.

Implementation:

- [ ] VQA-4-I1 Reuse packaged native fixture apps and shared fixture IDs; add only missing fixture selection/import entry points at their owning adapters.
- [ ] VQA-4-I2 Define real touch/keyboard, accessibility and OS file/clipboard interactions using available platform tooling; pin the simulator/emulator and disposable app storage.

Validation:

- [ ] VQA-4-V1 Validate command availability and build/fixture wiring using existing narrow checks, budget 5 minutes. Runtime UI proof is owned by VQA-8 at the final native gate.

Evidence: Ignored platform progress and exact available/missing control inventory.
Handoff/blocker: Missing native app/runtime/driver, owner and exact unblock condition.

## Final testing and managed campaigns

### VQA-5 — Add repeatable visual regression checks

- [ ] VQA-5 Implement the capture/comparison workflow and focused replay tests.

Purpose: Preserve useful findings after the exploratory session.
Context/paths: VQA-1–VQA-3, existing browser harness and editing drivers;
planned visual-QA selectors/scripts in the current test tree.
Dependencies: VQA-1, VQA-2, VQA-3; relevant web functionality implemented.
Independent work: Native development remains independent.
Scope: One capture/diff boundary, 30–45 minutes; split additional coverage slices.
Acceptance: Repeatable named checkpoints compare against reviewed external baselines;
semantic assertions remain independent; failure produces a bounded actionable diff.

Implementation:

- [ ] VQA-5-I1 Add focused browser journeys, deterministic capture readiness, region/geometry checks and diff reports. Set tolerances from unchanged repeated captures; required content regions cannot be masked or tuned to pass a defect.
- [ ] VQA-5-I2 Keep authored inputs, expectations and scripts in Git. Store generated screenshot baselines/reports outside source repositories with hashes and review metadata; disable automatic golden acceptance.

Validation:

- [ ] VQA-5-V1 Demonstrate one unchanged capture passes and deliberate missing-content/layout changes fail; verify missing baselines fail explicitly. Budget 10 minutes.

Evidence: Counts, selectors, baseline identifiers and detector result in ignored progress.
Handoff/blocker: Exact unstable region, environment discrepancy or missing approved baseline.

### VQA-6 — Execute the Codex browser editing walkthrough

- [ ] VQA-6 Inspect every assigned web case through rendered UI.

Purpose: Find editing, appearance and product-flow defects beyond scripted assertions.
Context/paths: Frozen manifest, gallery, installed alpha product and VQA-5 tooling.
Dependencies: VQA-5; web alpha entry conditions satisfied.
Independent work: VQA-7 can use separate disposable documents; no parallel runner implied.
Scope: 30–45-minute sessions by case/profile group; never one unbounded whole-corpus turn.
Acceptance: Every assigned case has actual interactions and visual observations;
core journeys run in all three engines; exploratory charters cover unexpected changes.

Implementation:

- [ ] VQA-6-I1 Run the manifest's editing/lifecycle/layout journeys and checkpoint comparisons; inspect console/runtime errors and independent semantic/save outcomes.
- [ ] VQA-6-I2 Spend a bounded charter on combined actions and awkward content/layouts; record repro steps and nearest fixture for each finding.

Validation:

- [ ] VQA-6-V1 Reconcile assigned case/profile outcomes and executed/passed/failed/blocked/not-run counts. Capture expected/actual and environment for every failure; do not infer PASS from absence of an exception.

Evidence: Ignored session progress; only active-failure captures retained locally.
Handoff/blocker: Last completed case/checkpoint, next case and exact candidate pins.

### VQA-7 — Execute import fidelity and recovery comparisons

- [ ] VQA-7 Compare imported documents to original source views.

Purpose: Catch content loss, misleading previews and visual conversion regressions.
Context/paths: Original corpus/oracles, format profile contract, actual file controls.
Dependencies: VQA-5; import feature and authorized local asset-host prerequisites for selected cases.
Independent work: Plain/text-only cases proceed beside unavailable media support.
Scope: One format family/profile per 30–45-minute session; split complex documents by region.
Acceptance: Each format's assigned cases include visual fidelity and semantic
comparison plus preview/cancel/commit/undo/reopen; unsupported/lossy outcomes are
visible, expected and nonmutating until approved through the actual UI.

Implementation:

- [ ] VQA-7-I1 Inspect original and imported content side by side; compare whole-document structure and representative detailed regions, including every supported construct in that fixture.
- [ ] VQA-7-I2 Exercise failure/loss/stale-target/readonly paths, retained original bytes, undo/redo and same-format save/reopen. Inspect supported exports independently; classify PDF import as unsupported.

Validation:

- [ ] VQA-7-V1 Record per-construct fidelity results, content/asset assertions and UI checkpoints. Explain every observed difference as a defect or a specific documented transformation; no blanket visual-similarity pass.

Evidence: Ignored import progress with source hash, reference reader, region and repro.
Handoff/blocker: Exact format/construct and reader/asset-host prerequisite; untouched originals preserved.

### VQA-8 — Execute native simulator/emulator visual QA

- [ ] VQA-8 Exercise native editors on the accepted platform runtimes.

Purpose: Find native input, appearance and lifecycle defects using the same expectations.
Context/paths: VQA-4 controls, corpus, platform matrix and roadmap43/native final owners.
Dependencies: VQA-4; existing applicable native final-testing entry gate.
Independent work: Ready platform slices proceed beside unavailable profiles; web results stand separately.
Scope: One runtime/journey group per 30–45-minute session; split the matrix before execution.
Acceptance: Actual native UI actions, screenshots and independent content checks
cover editing, import, keyboard/selection, layout, clipboard and lifecycle; required
OS/IME/AT variants retain original case IDs and honest runtime provenance.

Implementation:

- [ ] VQA-8-I1 Run phone/tablet and native desktop slices through visible controls. Include soft-keyboard occlusion, rotation/resize, gestures, IME composition, OS clipboard/file picker, background/foreground and relaunch with saved state.
- [ ] VQA-8-I2 Compare native renders with platform-specific reviewed references and shared semantic expectations; record capability limitations without calling desktop viewport emulation native proof.

Validation:

- [ ] VQA-8-V1 Reconcile each executed slice with the owning PHY/native requirement and actual nonzero outcomes; missing/blocked required cases remain unproven. Verify task-owned apps/runtimes and launchers are shut down or explicitly retained by an active owner.

Evidence: Ignored runtime progress; preserve exact device/runtime/build/input/capture provenance.
Handoff/blocker: Last case and missing app/runtime/control, owner and changed-input retry condition.

### VQA-9 — Triage findings and close each candidate gate

- [ ] VQA-9 Resolve regressions and publish an internal readiness summary per milestone.

Purpose: Turn observations into a reviewable alpha or native/beta decision.
Context/paths: Campaign outcomes, original test owners, authored regression fixtures.
Dependencies: VQA-6 and VQA-7 for web alpha; VQA-8 additionally for native/beta.
Independent work: Web summary can close while native work remains explicitly pending.
Scope: One defect/fix/retest group or milestone summary per 30–45-minute session.
Acceptance: No unresolved required-profile data loss, corruption, silent import loss,
crash, blocked core editing/import/recovery journey or severe unreadable layout;
all required cases are accounted for. Smaller accepted limitations have an owner
and explicit disposition; none is silently passed or hidden in a baseline update.

Implementation:

- [ ] VQA-9-I1 Record severity, fixture, exact build/runtime, minimal steps, expected/actual, affected region and owning component. Repair defects in their existing feature owner and add the smallest deterministic regression case.
- [ ] VQA-9-I2 Rerun failed/affected cases and one relevant integrated journey. Invalidate only evidence affected by changed code/fixtures/fonts/runtime; require review for intentional baseline changes and retain the old baseline reference.

Validation:

- [ ] VQA-9-V1 Reconcile counts, open findings, accepted limitations, NOT_RUN/BLOCKED cases and evidence applicability. Issue separate web and native gate decisions; visual QA never implies other size/performance/security gates or publication approval.
- [ ] VQA-9-V2 Close task-owned browsers and temporary servers, verify listeners, inspect free disk space and remove inactive session-generated outputs. Keep active-failure diagnostics only as needed; report cleanup and any intentionally retained preview.

Evidence: Concise ignored internal summary with source/baseline/runtime pins, counts,
defect dispositions and remaining qualification gates. Release artifacts, if later
needed, belong outside source repositories. No generated evidence is committed.
Handoff/blocker: Unresolved severity/case, owner, repair hypothesis and exact rerun
selector. Do not repeat an unchanged blocked run without changed input.

## Execution safeguards

All test content and provider/network behavior are deterministic and local. Prepared
AI UI states may be inspected for presentation and mechanics; no live provider
calls, paid model/API tests, credential loading or automatic fixture recording are
part of this plan. Original documents are immutable; use disposable copies and
isolated per-case storage. No automatic migration, reseeding or source-format
relabeling. Current-format durability and unsupported-envelope rejection remain
mandatory. No publishing, deployment, service provisioning or remote release is
authorized by this QA plan.
