# macos native input feature delivery

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

## Epic MACOS_INPUT — macos native input feature delivery

### Task RMC-1.1 — Bootstrap the native SDK test host

- [ ] RMC-1.1 Bootstrap the native SDK test host.

Purpose: bootstrap.
Context: `architecture/roadmaps/18-desktop-native.md`, ONLY Task DSK-1.1; canonical affected context: `native/macos/` (project/test bootstrap only). Read core-relative paths from `core/`. Prior inputs: none beyond the source entry summary
Dependencies: none.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of DSK-1.1: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QMC-1.1, not waived. Original acceptance: Pinned tooling builds a native control and runs a real bootstrap test; missing tools name an exact unblock condition.

Implementation:

- [ ] RMC-1.1-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Pin Xcode, Swift, macOS SDK, deployment range and CPU slices. Create an AppKit SDK target, native test host and dispatcher with one real XCTest bootstrap case. Initialize capability.json as unqualified. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RMC-1.1-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QMC-1.1: `bash native/macos/scripts/check.sh bootstrap`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task RMC-1.2 — Qualify the native control candidate

- [ ] RMC-1.2 Qualify the native control candidate.

Purpose: toolkit.
Context: `architecture/roadmaps/18-desktop-native.md`, ONLY Task DSK-1.2; canonical affected context: `native/macos/probe/`. Read core-relative paths from `core/`. Prior inputs: none beyond the source entry summary
Dependencies: RMC-1.1.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of DSK-1.2: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QMC-1.1, not waived. Original acceptance: A native fixture proves composition and editable cell/atom feasibility; unsupported required routes block dependents.

Implementation:

- [ ] RMC-1.2-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Probe AppKit NSTextView and the selected native TextKit path; record selected input/selection hooks and table/atom limitations. Choose real native child controls when needed; this is feasibility, not parity. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RMC-1.2-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QMC-1.1: `bash native/macos/scripts/check.sh toolkit`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task RMC-1.3 — Bind session ownership and native disposal

- [ ] RMC-1.3 Bind session ownership and native disposal.

Purpose: session.
Context: `architecture/roadmaps/18-desktop-native.md`, ONLY Task DSK-1.3; canonical affected context: `native/macos/Sources/EditacMacOS/session/`. Read core-relative paths from `core/`. Prior inputs: none beyond the source entry summary
Dependencies: RMC-1.1.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of DSK-1.3: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QMC-1.1, not waived. Original acceptance: Open/dispose, failure and cancellation preserve ownership and callback order; disposed views receive no callbacks.

Implementation:

- [ ] RMC-1.3-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Bind the qualified Swift interface with an AppKit-owned session executor to the shared session. Use owned buffers, serialized calls and typed failures; reuse roadmap-12 ports. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RMC-1.3-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QMC-1.1: `bash native/macos/scripts/check.sh session`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task RMC-1.4 — Project patches and map native selection

- [ ] RMC-1.4 Project patches and map native selection.

Purpose: projection.
Context: `architecture/roadmaps/18-desktop-native.md`, ONLY Task DSK-1.4; canonical affected context: `native/macos/Sources/EditacMacOS/projection/`. [additional interaction cases](../tests/desktop-editing-cases.md). Read core-relative paths from `core/`. Prior inputs: none beyond the source entry summary
Dependencies: RMC-1.2, RMC-1.3.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of DSK-1.4: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QMC-1.1, not waived. Original acceptance: Incremental patches preserve stable identity and selection across Unicode, bidi text and attachment boundaries. The coordinate/range-mapping portion of NAT-05 covers selection direction and stale target rejection; full protocol sequences stay with the input owner.

Implementation:

- [ ] RMC-1.4-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Project shared snapshots/range patches; map AppKit NSRange UTF-16 ranges and attachment positions. Reuse conversion and anchor contracts; avoid a second semantic model. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RMC-1.4-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QMC-1.1: `bash native/macos/scripts/check.sh projection`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task RMC-1.5 — Route committed native text edits

- [ ] RMC-1.5 Route committed native text edits.

Purpose: edits.
Context: `architecture/roadmaps/18-desktop-native.md`, ONLY Task DSK-1.5; canonical affected context: `native/macos/Sources/EditacMacOS/input/`. Read core-relative paths from `core/`. Prior inputs: none beyond the source entry summary
Dependencies: RMC-1.4.
Independent work: Any local parent whose named inputs are available.
Session scope: One boundary, normally 15–45 minutes including focused validation.
Acceptance: Feature projection of DSK-1.5: authenticate applicable existing delivery or implement the original feature predicate below. Focused correctness, safety and usable public wiring are required now; comprehensive test development and all original runtime/platform/OS/AT/performance predicates are assigned to QMC-1.1, not waived. Original acceptance: Insert/delete/replacement each commits once; rejection leaves a consistent projection without recursive input.

Implementation:

- [ ] RMC-1.5-I1 Authenticate current ownership and existing accepted proof; change only the missing original boundary. Route NSTextView text-system edit notifications through prepared commands. Distinguish native-origin callbacks from applied patches and test rejected edits. Read prior input rows before use; whole-platform qualification is not an implementation prerequisite. Leave broad harness additions for final testing unless a concrete defect needs a minimal regression.

Validation:

- [ ] RMC-1.5-V1 Use an existing selector for this boundary or reuse exact applicable passing proof (normally 1–5 minutes). Prove nonzero relevant behavior; source checks alone cannot prove runtime behavior. Original final-validation contract, owned by QMC-1.1: `bash native/macos/scripts/check.sh edits`. Assert acceptance; require nonzero matching tests.

Evidence: Separate progress records exact source/profile/runtime pins, command/exit, meaningful executed/passed/failed/skipped counts, reused evidence and concise failure dispositions. Generated detail stays in ignored task scratch, not Git.
Handoff: Delivered interface/path, prerequisite row, remaining substep, exact failing selector and next bounded action.
Blocked behavior: Leave unchecked; try an independent ready parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.
