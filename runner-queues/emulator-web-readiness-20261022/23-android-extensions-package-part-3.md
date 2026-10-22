# android extension wiring and native package delivery

Status: IN_PROGRESS

## Goal and entry conditions

Exact implemented android SDK/public shared extension, format and link interfaces are authenticated in prior rows; no whole-track qualification label is required. All paths below are relative to the single root workspace unless explicitly stated. Read only the prerequisite summary rows named by the active parent in `.roadmap-runner/emulator-web-readiness-20261022/readiness.json`; the first entry creates them. No old whole-roadmap COMPLETE label is an entry gate.

## Execution contract

User authority, 2026-10-22: one serial Roadmap Runner in `/Users/bpstr/Github/edit-ac`, directly on the current main branches (the user's master), with no worktree, parallel lane, subagent or second controller. Other controllers stay stopped. Work across `core`, `cli`, `architecture` and `docs` from this workspace; canonical native commands are run from `core`, terminal commands from `cli`. Never require a physical device. iOS simulators, Android emulators and actual desktop OS hosts/VMs must prove the claimed target behavior. A desktop mobile viewport, host-only JNA test or successful cross-compilation cannot stand in for target execution.

Run one bounded parent per worker. Source files are controller-owned and immutable; only separate progress files carry live checkmarks. Authenticate existing applicable implementation and passing proof before coding or rerunning. Older BLOCKED labels and removed generated output are not current dependencies. A feature projection does not close its originating aggregate qualification parent: final testing owns the original runtime/performance predicates. Preserve original IDs and failure dispositions in the runtime matrix.

Functional tasks use only existing affected checks (normally 1–5 minutes) and necessary defect regressions. Test development, full suites and exhaustive matrices are owned by the final testing entries after functional delivery. Full suites are mandatory, as requested; reuse exact applicable current-source runs, enumerate complete discovery and repair failures without silently reducing coverage. A missing command/dispatcher, zero cases, required skip, cancelled run or unsupported required cell is not a pass. If a required full command cannot fit a worker, record its real cost and checkpoint and request a controller split before running it; never report partial coverage as full.

All automated inference/provider behavior uses deterministic prepared fixtures and mocked transports. Read `/Users/bpstr/Github/assign/architecture/operations/paid-inference-testing-policy.md` before AI test changes. No paid inference, ambient credentials, `.secrets`, subscription proxies, live fixture recording, paid services, cloud provisioning, publication, push, deployment or external integration. Optional encrypted/cloud and physical-only claims remain explicitly outside this readiness profile; do not remove tests from the existing full suites on that basis.

Keep authored code/configuration/specs/deterministic fixtures in Git; keep runtime matrices, logs, reports, benchmarks, screenshots and binaries ignored and task-owned. Record concise command/exit and executed/passed/failed/skipped counts plus exact input/runtime pins in progress. Delete inactive reproducible bulk output after debugging, retaining concise failure dispositions. Track and tear down owned browsers/servers; check data-volume space after builds. Commit only validated owned paths on the existing main branches at two-parent and source boundaries, using plain-English subjects and the coordination lock. Preserve unrelated work; never stash/reset or stage another task's files.

For a blocker, first select an independent ready parent in THIS source. If none is ready, leave requirements unchecked, record task/source/error/missing-prerequisite fingerprint, owner, attempted repair and exact changed-input resume condition, then end with Status: BLOCKED. The event guard stops the controller after that completed worker; no unchanged retry or automatic restart. An unavailable physical device never blocks this queue. An unavailable required virtual platform remains unproven. Do not read the whole queue or all referenced specs: read this file, bounded progress and only the current parent's named source section/prerequisite row.

## Epic ANDROID_EXTENSIONS_PACKAGE — android extension wiring and native package delivery

### Task RAN-2.1 — Build the distributable native SDK artifact

- [ ] RAN-2.1 Build the distributable native SDK artifact.

Purpose: package.
Context: `architecture/roadmaps/17-android-sdk.md`, ONLY Task AND-2.1; canonical affected context: `native/android/packaging/`. Read core-relative paths from `core/`. Prior inputs: AND-1.13, AND-1.14, AND-1.15, AND-1.17, AND-1.18
Dependencies: none.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of AND-2.1: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QAN-1.5, not waived. Original acceptance: The package contains supported binaries, API/version metadata, resources and notices, with immutable hashes and no publication.

Implementation:

- [ ] RAN-2.1-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Build an Android library artifact with declared native ABI libraries and dependency metadata. Pin runtime/generator compatibility, check contents via the pinned Gradle wrapper and adb, and record OS/CPU support. Signing/publication are separate release actions. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RAN-2.1-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QAN-1.5: `bash native/android/scripts/check.sh package`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task RAN-2.2 — Verify a clean native consumer

- [ ] RAN-2.2 Verify a clean native consumer.

Purpose: consumer.
Context: `architecture/roadmaps/17-android-sdk.md`, ONLY Task AND-2.2; canonical affected context: `native/android/consumer/`. Read core-relative paths from `core/`. Prior inputs: none beyond the source entry summary
Dependencies: RAN-2.1.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of AND-2.2: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QAN-1.5, not waived. Original acceptance: A clean consumer needs no sibling checkout and runs actual local/rich/offline/mocked-collaboration and change-review smoke cases.

Implementation:

- [ ] RAN-2.2-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Build a native sample against the immutable packed SDK; test install/open/edit/review/dispose and reject missing resources. Keep every mandatory feature discoverable. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RAN-2.2-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QAN-1.5: `bash native/android/scripts/check.sh consumer`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.
