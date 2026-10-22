# android native rich content feature delivery

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

## Epic ANDROID_RICH_CONTENT — android native rich content feature delivery

### Task RAN-1.9 — Render native table structure

- [ ] RAN-1.9 Render native table structure.

Purpose: table-projection.
Context: `architecture/roadmaps/17-android-sdk.md`, ONLY Task AND-1.9; canonical affected context: `native/android/sdk/src/main/tables/`. Read core-relative paths from `core/`. Prior inputs: AND-1.8
Dependencies: none.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of AND-1.9: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QAN-1.2, not waived. Original acceptance: Native table/cell views retain identity under incremental updates; source or image fallback fails required parity.

Implementation:

- [ ] RAN-1.9-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Render the bounded shared table through native cell controls. Preserve cell identity and the engine model; defer command wiring to the next task. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RAN-1.9-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QAN-1.2: `bash native/android/scripts/check.sh table-projection`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task RAN-1.10 — Wire table cell editing and navigation

- [ ] RAN-1.10 Wire table cell editing and navigation.

Purpose: table-editing.
Context: `architecture/roadmaps/17-android-sdk.md`, ONLY Task AND-1.10; canonical affected context: `native/android/sdk/src/main/tables/`. Read core-relative paths from `core/`. Prior inputs: AND-1.7
Dependencies: RAN-1.9.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of AND-1.10: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QAN-1.2, not waived. Original acceptance: Cell edits/navigation, supported selections and row/column actions preserve identity through remote updates and undo.

Implementation:

- [ ] RAN-1.10-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Connect cell views to shared commands and logical focus transitions. Expose accessible action hooks and enforce the qualified table limits. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RAN-1.10-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QAN-1.2: `bash native/android/scripts/check.sh table-editing`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task RAN-1.11 — Bind native image and reference views

- [ ] RAN-1.11 Bind native image and reference views.

Purpose: attachments.
Context: `architecture/roadmaps/17-android-sdk.md`, ONLY Task AND-1.11; canonical affected context: `native/android/sdk/src/main/attachments/`. Read core-relative paths from `core/`. Prior inputs: AND-1.7, AND-1.8
Dependencies: none.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of AND-1.11: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QAN-1.2, not waived. Original acceptance: Images expose alt/error/edit states; references retain IDs/labels. Both reject stale or cancelled host resolutions.

Implementation:

- [ ] RAN-1.11-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Bind portable image/reference descriptors to native views and shared asset/resolver policy. Add activation, selection and replacement/removal controls. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RAN-1.11-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QAN-1.2: `bash native/android/scripts/check.sh attachments`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task RAN-1.12 — Expose portable renderer hooks and math capabilities

- [ ] RAN-1.12 Expose portable renderer hooks and math capabilities.

Purpose: extensions.
Context: `architecture/roadmaps/17-android-sdk.md`, ONLY Task AND-1.12; canonical affected context: `native/android/sdk/src/main/extensions/`. Read core-relative paths from `core/`. Prior inputs: AND-1.8
Dependencies: RAN-1.11.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of AND-1.12: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QAN-1.2, not waived. Original acceptance: Custom marks/atoms render, select, edit and dispose; unknown data survives. Math source editing never implies typesetting.

Implementation:

- [ ] RAN-1.12-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Expose roadmap-21 native hooks and its bounded math source editor. Record source/typeset capabilities separately; fallback cannot qualify mandatory content. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RAN-1.12-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QAN-1.2: `bash native/android/scripts/check.sh extensions`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task RAN-1.13 — Adapt native clipboard and drop formats

- [ ] RAN-1.13 Adapt native clipboard and drop formats.

Purpose: clipboard.
Context: `architecture/roadmaps/17-android-sdk.md`, ONLY Task AND-1.13; canonical affected context: `native/android/sdk/src/main/clipboard/`. [additional interaction cases](../tests/desktop-editing-cases.md). Read core-relative paths from `core/`. Prior inputs: AND-1.7
Dependencies: RAN-1.10, RAN-1.11, RAN-1.12.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of AND-1.13: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QAN-1.2, not waived. Original acceptance: Rich copy/cut/paste preserves supported structure; hostile data is diagnosed, while read-only/cancelled drops cannot mutate. NAT-10/NAT-11 adds multiple views, delayed providers, cross-app copy/move and source preservation under the shared transfer contract; qualify platform clipboard lifetime.

Implementation:

- [ ] RAN-1.13-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Connect native clipboard/drop formats to shared codecs, validation and asset policy. Preserve format precedence, plain text and one history operation; reuse sanitization. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RAN-1.13-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QAN-1.2: `bash native/android/scripts/check.sh clipboard`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.
