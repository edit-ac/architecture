# macos native lifecycle feature delivery

Status: IN_PROGRESS

## Goal and entry conditions

RRD current-source macos rows and exact prior native API/patch/style inputs referenced by the current parent are available; missing runtime-only proof is owned by final testing. All paths below are relative to the single root workspace unless explicitly stated. Read only the prerequisite summary rows named by the active parent in `.roadmap-runner/emulator-web-readiness-20261022/readiness.json`; the first entry creates them. No old whole-roadmap COMPLETE label is an entry gate.

## Execution contract

User authority, 2026-10-22: one serial Roadmap Runner in `/Users/bpstr/Github/edit-ac`, directly on the current main branches (the user's master), with no worktree, parallel lane, subagent or second controller. Other controllers stay stopped. Work across `core`, `cli`, `architecture` and `docs` from this workspace; canonical native commands are run from `core`, terminal commands from `cli`. Never require a physical device. iOS simulators, Android emulators and actual desktop OS hosts/VMs must prove the claimed target behavior. A desktop mobile viewport, host-only JNA test or successful cross-compilation cannot stand in for target execution.

Run one bounded parent per worker. Source files are controller-owned and immutable; only separate progress files carry live checkmarks. Authenticate existing applicable implementation and passing proof before coding or rerunning. Older BLOCKED labels and removed generated output are not current dependencies. A feature projection does not close its originating aggregate qualification parent: final testing owns the original runtime/performance predicates. Preserve original IDs and failure dispositions in the runtime matrix.

Functional tasks use only existing affected checks (normally 1–5 minutes) and necessary defect regressions. Test development, full suites and exhaustive matrices are owned by the final testing entries after functional delivery. Full suites are mandatory, as requested; reuse exact applicable current-source runs, enumerate complete discovery and repair failures without silently reducing coverage. A missing command/dispatcher, zero cases, required skip, cancelled run or unsupported required cell is not a pass. If a required full command cannot fit a worker, record its real cost and checkpoint and request a controller split before running it; never report partial coverage as full.

All automated inference/provider behavior uses deterministic prepared fixtures and mocked transports. Read `/Users/bpstr/Github/assign/architecture/operations/paid-inference-testing-policy.md` before AI test changes. No paid inference, ambient credentials, `.secrets`, subscription proxies, live fixture recording, paid services, cloud provisioning, publication, push, deployment or external integration. Optional encrypted/cloud and physical-only claims remain explicitly outside this readiness profile; do not remove tests from the existing full suites on that basis.

Keep authored code/configuration/specs/deterministic fixtures in Git; keep runtime matrices, logs, reports, benchmarks, screenshots and binaries ignored and task-owned. Record concise command/exit and executed/passed/failed/skipped counts plus exact input/runtime pins in progress. Delete inactive reproducible bulk output after debugging, retaining concise failure dispositions. Track and tear down owned browsers/servers; check data-volume space after builds. Commit only validated owned paths on the existing main branches at two-parent and source boundaries, using plain-English subjects and the coordination lock. Preserve unrelated work; never stash/reset or stage another task's files.

For a blocker, first select an independent ready parent in THIS source. If none is ready, leave requirements unchecked, record task/source/error/missing-prerequisite fingerprint, owner, attempted repair and exact changed-input resume condition, then end with Status: BLOCKED. The event guard stops the controller after that completed worker; no unchanged retry or automatic restart. An unavailable physical device never blocks this queue. An unavailable required virtual platform remains unproven. Do not read the whole queue or all referenced specs: read this file, bounded progress and only the current parent's named source section/prerequisite row.

## Epic MACOS_LIFECYCLE — macos native lifecycle feature delivery

### Task RMC-1.14 — Connect durable sessions to app lifecycle

- [ ] RMC-1.14 Connect durable sessions to app lifecycle.

Purpose: durability.
Context: `architecture/roadmaps/18-desktop-native.md`, ONLY Task DSK-1.14; canonical affected context: `native/macos/Sources/EditacMacOS/storage/`. Read core-relative paths from `core/`. Prior inputs: DSK-1.3, DSK-1.7
Dependencies: none.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of DSK-1.14: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QMC-1.3, not waived. Original acceptance: Offline edit/restore needs no account; commit status follows durable receipts. Close/reopen and storage errors preserve recovery.

Implementation:

- [ ] RMC-1.14-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Bind qualified LocalStore and native lifecycle notifications to the shared session. Surface pending/committed/error states; reuse journal/checkpoint/outbox logic. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RMC-1.14-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QMC-1.3: `bash native/macos/scripts/check.sh durability`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task RMC-1.15 — Bind collaboration and reconnect state

- [ ] RMC-1.15 Bind collaboration and reconnect state.

Purpose: collaboration.
Context: `architecture/roadmaps/18-desktop-native.md`, ONLY Task DSK-1.15; canonical affected context: `native/macos/Sources/EditacMacOS/transport/`. Read core-relative paths from `core/`. Prior inputs: DSK-1.6
Dependencies: RMC-1.14.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of DSK-1.15: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QMC-1.3, not waived. Original acceptance: Two fixtures converge across reconnect; remote selection, revocation and document switching preserve receipt/input semantics.

Implementation:

- [ ] RMC-1.15-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Bind host-injected Transport/Authorization and presence to native UI state. Reuse qualified sync logic; exercise cancellation and remote composition overlap with mocks. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RMC-1.15-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QMC-1.3: `bash native/macos/scripts/check.sh collaboration`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task RMC-1.16 — Expose accessible text and editor actions

- [ ] RMC-1.16 Expose accessible text and editor actions.

Purpose: accessibility-text.
Context: `architecture/roadmaps/18-desktop-native.md`, ONLY Task DSK-1.16; canonical affected context: `native/macos/Sources/EditacMacOS/accessibility/`. [additional interaction cases](../tests/desktop-editing-cases.md). Read core-relative paths from `core/`. Prior inputs: DSK-1.6, DSK-1.7, DSK-1.8
Dependencies: none.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of DSK-1.16: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QMC-1.3, not waived. Original acceptance: Native accessibility exposes text, selection, command/read-only state and keyboard focus at declared scaling settings. NAT-13/NAT-14 checks current accessible text geometry and safe text-service lock/reentrancy behavior; record actual platform evidence.

Implementation:

- [ ] RMC-1.16-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Expose native text/actions for VoiceOver. Programmatically check labels and selection; preserve OS input. Actual screen-reader qualification belongs to roadmap 20. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RMC-1.16-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QMC-1.3: `bash native/macos/scripts/check.sh accessibility-text`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task RMC-1.17 — Expose accessible tables and attachments

- [ ] RMC-1.17 Expose accessible tables and attachments.

Purpose: accessibility-structure.
Context: `architecture/roadmaps/18-desktop-native.md`, ONLY Task DSK-1.17; canonical affected context: `native/macos/Sources/EditacMacOS/accessibility/`. Read core-relative paths from `core/`. Prior inputs: DSK-1.10, DSK-1.11, DSK-1.12
Dependencies: RMC-1.16.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of DSK-1.17: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QMC-1.3, not waived. Original acceptance: Tables/cells, alt text, reference labels and atom actions have accessible relationships and a pointer-free focus route.

Implementation:

- [ ] RMC-1.17-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Add native structure/actions for tables and attachments using shared labels and capabilities; test focus transitions and bounded announcements. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RMC-1.17-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QMC-1.3: `bash native/macos/scripts/check.sh accessibility-structure`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task RMC-1.18 — Present native change and revision views

- [ ] RMC-1.18 Present native change and revision views.

Purpose: change-review.
Context: `architecture/roadmaps/18-desktop-native.md`, ONLY Task DSK-1.18; canonical affected context: `native/macos/Sources/EditacMacOS/change-review/`. Read core-relative paths from `core/`. Prior inputs: DSK-1.10, DSK-1.11
Dependencies: RMC-1.16, RMC-1.17.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of DSK-1.18: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QMC-1.3, not waived. Original acceptance: Read-only unified/semantic changes retain profile labels and trusted/unknown attribution; stale revisions remain visible.

Implementation:

- [ ] RMC-1.18-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Render roadmap-13 changes in accessible native views with range navigation. Reuse its algorithm, revision and attribution contracts; never rewind the live replica. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RMC-1.18-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QMC-1.3: `bash native/macos/scripts/check.sh change-review`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.
