# android native input feature delivery

Status: IN_PROGRESS

## Goal and entry conditions

RRD current-source android rows and exact prior native API/patch/style inputs referenced by the current parent are available; missing runtime-only proof is owned by final testing. All paths below are relative to the single root workspace unless explicitly stated. Read only the prerequisite summary rows named by the active parent in `.roadmap-runner/emulator-web-readiness-20261022/readiness.json`; the first entry creates them. No old whole-roadmap COMPLETE label is an entry gate.

## Execution contract

User authority, 2026-10-22: one serial Roadmap Runner in `/Users/bpstr/Github/edit-ac`, directly on the current main branches (the user's master), with no worktree, parallel lane, subagent or second controller. Other controllers stay stopped. Work across `core`, `cli`, `architecture` and `docs` from this workspace; canonical native commands are run from `core`, terminal commands from `cli`. Never require a physical device. iOS simulators, Android emulators and actual desktop OS hosts/VMs must prove the claimed target behavior. A desktop mobile viewport, host-only JNA test or successful cross-compilation cannot stand in for target execution.

Run one bounded parent per worker. Source files are controller-owned and immutable; only separate progress files carry live checkmarks. Authenticate existing applicable implementation and passing proof before coding or rerunning. Older BLOCKED labels and removed generated output are not current dependencies. A feature projection does not close its originating aggregate qualification parent: final testing owns the original runtime/performance predicates. Preserve original IDs and failure dispositions in the runtime matrix.

Functional tasks use only existing affected checks (normally 1–5 minutes) and necessary defect regressions. Test development, full suites and exhaustive matrices are owned by the final testing entries after functional delivery. Full suites are mandatory, as requested; reuse exact applicable current-source runs, enumerate complete discovery and repair failures without silently reducing coverage. A missing command/dispatcher, zero cases, required skip, cancelled run or unsupported required cell is not a pass. If a required full command cannot fit a worker, record its real cost and checkpoint and request a controller split before running it; never report partial coverage as full.

All automated inference/provider behavior uses deterministic prepared fixtures and mocked transports. Read `/Users/bpstr/Github/assign/architecture/operations/paid-inference-testing-policy.md` before AI test changes. No paid inference, ambient credentials, `.secrets`, subscription proxies, live fixture recording, paid services, cloud provisioning, publication, push, deployment or external integration. Optional encrypted/cloud and physical-only claims remain explicitly outside this readiness profile; do not remove tests from the existing full suites on that basis.

Keep authored code/configuration/specs/deterministic fixtures in Git; keep runtime matrices, logs, reports, benchmarks, screenshots and binaries ignored and task-owned. Record concise command/exit and executed/passed/failed/skipped counts plus exact input/runtime pins in progress. Delete inactive reproducible bulk output after debugging, retaining concise failure dispositions. Track and tear down owned browsers/servers; check data-volume space after builds. Commit only validated owned paths on the existing main branches at two-parent and source boundaries, using plain-English subjects and the coordination lock. Preserve unrelated work; never stash/reset or stage another task's files.

For a blocker, first select an independent ready parent in THIS source. If none is ready, leave requirements unchecked, record task/source/error/missing-prerequisite fingerprint, owner, attempted repair and exact changed-input resume condition, then end with Status: BLOCKED. The event guard stops the controller after that completed worker; no unchanged retry or automatic restart. An unavailable physical device never blocks this queue. An unavailable required virtual platform remains unproven. Do not read the whole queue or all referenced specs: read this file, bounded progress and only the current parent's named source section/prerequisite row.

## Epic ANDROID_INPUT — android native input feature delivery

### Task RAN-1.6 — Integrate composition and OS replacements

- [ ] RAN-1.6 Integrate composition and OS replacements.

Purpose: composition.
Context: `architecture/roadmaps/17-android-sdk.md`, ONLY Task AND-1.6; canonical affected context: `native/android/sdk/src/main/input/`. [additional interaction cases](../tests/desktop-editing-cases.md). [Platform editing contract](../specs/platform-editing-services.md); [ENV acceptance variants](../tests/platform-editing-cases.md). Read core-relative paths from `core/`. Prior inputs: none beyond the source entry summary
Dependencies: none.
Prerequisite evidence: Earlier-file validated RAN-1.5 rows with current-source applicability; missing/failed/skipped proof does not unlock this parent.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of AND-1.6: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QAN-1.1, not waived. Original acceptance: Commit/cancel, OS replacement and remote overlap preserve text/selection; synthetic input does not qualify actual IMEs. Qualify NAT-01/NAT-02 through deterministic native protocol fixtures; supply actual OS/IME runbooks and preliminary observations for DEL-1.7, without claiming device qualification here. Android additionally binds NAT-06 handwriting preview/fallback where available. ENV-01–06/09/12 refine native control policy: default platform spelling respects user settings, off/custom are explicit, autocorrection remains independent and unsupported/coupled traits are reported. Reuse the selected control/provider; accepted corrections use captured targets once. No implicit checker dependency/service or automatic fallback is allowed.

Implementation:

- [ ] RAN-1.6-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Integrate InputConnection composing, batch-edit and selection state with the shared overlap policy. Handle supported autocorrect/dictation replacements without committing provisional input twice. Expose platform/off/custom spellcheck policy and independent autocorrection using the control adapter; preserve IME services and diagnose inseparable flags. Reuse configured host-checker ports where supported; never duplicate engine semantics. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RAN-1.6-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QAN-1.1: `bash native/android/scripts/check.sh composition`. Assert acceptance; require nonzero matching tests. Include prepared/control ENV preference/replacement variants and actual-control on/off/correction observations where available; supply exact settings/locale/toolkit and unqualified combinations to DEL-1.7. No synthetic-only platform claim.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task RAN-1.7 — Route commands, history and read-only state

- [ ] RAN-1.7 Route commands, history and read-only state.

Purpose: commands.
Context: `architecture/roadmaps/17-android-sdk.md`, ONLY Task AND-1.7; canonical affected context: `native/android/sdk/src/main/commands/`. [additional interaction cases](../tests/desktop-editing-cases.md). [Platform editing contract](../specs/platform-editing-services.md); [ENV acceptance variants](../tests/platform-editing-cases.md). Read core-relative paths from `core/`. Prior inputs: none beyond the source entry summary
Dependencies: RAN-1.6.
Prerequisite evidence: Earlier-file validated RAN-1.5 rows with current-source applicability; missing/failed/skipped proof does not unlock this parent.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of AND-1.7: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QAN-1.1, not waived. Original acceptance: Existing native actions honor shared history/capabilities and read-only state; later adapters must use this same mutation gate. NAT-07 command enablement/routing uses the appropriate first-party profile and injected transfer/service ports; unavailable optional services are explicit. Full NAT-10/NAT-11 transfer behavior remains with the clipboard owner, not an entry prerequisite here. ENV-07/08 route native undo/redo keys, Edit/context menus, accessibility actions and supported gestures to shared history exactly once, with current enablement and nested-responder/composition ownership. Native storage/projection changes cannot create a competing undo stack.

Implementation:

- [ ] RAN-1.7-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Route key/menu/touch actions, structural commands and undo/redo through the shared command catalog. Subscribe to enabled state; suppress independent native-history mutation. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RAN-1.7-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QAN-1.1: `bash native/android/scripts/check.sh commands`. Assert acceptance; require nonzero matching tests. Include ENV-07/08 empty/denied history, correction undo/redo, menu/key/gesture routing, duplicate delivery, remote edits and two-editor/nested-field ownership. Distinguish protocol checks from actual OS observations for DEL-1.7.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task RAN-1.8 — Map portable text styles and lists

- [ ] RAN-1.8 Map portable text styles and lists.

Purpose: styles.
Context: `architecture/roadmaps/17-android-sdk.md`, ONLY Task AND-1.8; canonical affected context: `native/android/sdk/src/main/styles/`. Read core-relative paths from `core/`. Prior inputs: none beyond the source entry summary
Dependencies: RAN-1.7.
Prerequisite evidence: Earlier-file validated RAN-1.4 rows with current-source applicability; missing/failed/skipped proof does not unlock this parent.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of AND-1.8: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QAN-1.1, not waived. Original acceptance: The shared mark/block/list corpus retains semantic equality, including links, mixed marks, nesting and checked items.

Implementation:

- [ ] RAN-1.8-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Map roadmap-21 descriptors to character/paragraph spans and native list projections in one registry. Existing engine commands own edits; use qualified fixtures for standard marks, headings/code/quotes and lists. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RAN-1.8-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QAN-1.1: `bash native/android/scripts/check.sh styles`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.
