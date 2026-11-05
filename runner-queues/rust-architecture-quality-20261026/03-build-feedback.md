# Reduce unnecessary Rust build and test work

Status: COMPLETE

## Goal and execution contract

Own F04 and P01 from `architecture/research/rust-architecture-quality-20261026.md`.
Progress: `.roadmap-runner/rust-architecture-quality-20261026/03-build-feedback.progress.md`.
Entry: existing test selectors and current source/feature configuration. RAQ-3.1
and RAQ-3.2 do not depend on earlier-file functionality. RAQ-3.3 consumes adopted
RAQ-1.1/RAQ-1.3/RAQ-1.5 interface receipts where they affect its measured graph;
measure the current accepted graph, not unfinished work in another checkout.

This source is planning-only until safe controller adoption. Preserve the guarded
serial lane, dirty work, existing tests/fixtures and current semantic contracts.
Reorganizing existing assertions is delivery work; new coverage belongs only to
source 04. No paid inference, secrets, runtime qualification, publication or
automatic fixture recording. No source snapshots, timings or generated reports in
Git. Use ignored task-owned targets and concise progress receipts; never clean or
signal another task's cache/process. Track started processes and remove this
session's inactive reproducible artifacts, checking disk before and after builds.

One ready parent per session. Record exact selectors, inputs, counts, elapsed
budgets and reuse decisions in progress; change only checkboxes/Status here.
Missing/zero-match/skipped checks do not pass. Fingerprint blockers with owner,
attempt and changed-input resume condition; do not rerun unchanged failures.
RAQ-3.3 is subject to the one-45-minute-batch/two-hypothesis limit and cannot hold
independent feature delivery. Production size/latency caps remain unchanged.

## Final qualification allocation, 2026-10-28

The user authorized unblocking and resuming after the 12 independent Rust
functional parents were accepted. The controller allocates one separate final
build-feedback batch to RAQ-3.3 only, under its existing acceptance. It ends at
45 minutes of total wall time or two materially different measured hypotheses,
whichever comes first. The single clock includes measurement, interpretation,
focused validation and cleanup; stop new measurements by minute 40. Continuations
and retries share that clock and hypothesis count; another session never renews
this allocation. Consume the start/deadline and hypothesis ledger at
`.roadmap-runner/raq-final-resume-20261028/allocation.json` before any experiment.
Record every attempted hypothesis there before measuring it. If interrupted,
resume only within the remaining allocation and with a concrete changed input.

QPF/browser optimization remains stopped. No production size/latency cap, original
failure, native deferral or prerequisite is waived. A conclusive measured
non-adoption may satisfy RAQ-3.3's existing decision acceptance; an inconclusive
or unexecuted measurement remains open. Final source 04 still requires all 13
original functional parents accepted. No further allocation is authorized.

## Tasks

### Task RAQ-3.1 — Give existing integration scenarios one target owner

- [x] RAQ-3.1 Remove duplicate suite compilation without losing assertions.

Purpose: Avoid compiling and running the same tests through standalone and aggregate targets.
Deliverable: An explicit ownership map and one Cargo-discovered owner per duplicated scenario.
Context: F04; `core/crates/editac-core/tests/{structure_conflicts,delete_edit_probe,hierarchy_probe,split_join_probe,table_shape,table_structure}.rs`, their support modules, Cargo test targets and exact selectors used by owned scripts/roadmaps.
Dependencies: none.
Independent work: RAQ-3.2 is logically independent; RAQ-3.3 may measure an accepted current graph if topology delivery is blocked.
Session scope: Four observed duplicate inclusions and their callers, 30–45 minutes including focused checks.
Acceptance: Every original scenario remains present under one discoverable owner, including the at-least-21 duplicated functions. No root-level support file is accidentally another test target. Retained selectors work, or their owned callers are migrated coherently with explicit coverage mapping. No active runner source or external worker input is rewritten.

Implementation:

- [x] RAQ-3.1-I1 Inventory discovered targets and path-included modules; choose canonical owners by existing contracts. Map old selectors to retained ones before moving/removing duplicate inclusions.
- [x] RAQ-3.1-I2 Reorganize only duplicated suites/support and update affected owned callers at a safe checkpoint. Preserve assertion bodies, fixture bytes and historical case meaning.

Validation:

- [x] RAQ-3.1-V1 Compare pre/post Cargo target and static test-function ownership maps; list tests only for affected targets and run one existing case from each changed family. Budget: 5 minutes; report before/after unique and duplicate counts, not merely a lower executed total.

Evidence: Progress contains complete selector mapping, retained assertion counts, removed duplicate owners and nonzero focused results.
Handoff: Selector still consumed by a protected active source, its owner and safe adoption condition. Do not silently remove that acceptance or leave a duplicate marked fixed.
Blocked behavior: If a selector is owned by an active runner, await its safe checkpoint with an exact migration mapping; RAQ-3.2 remains eligible.

### Task RAQ-3.2 — Compile shared fixture oracles through dev-only support

- [x] RAQ-3.2 Give repeated schema-v5 fixture support a reusable test crate.

Purpose: Avoid repeated front-end work for the same substantial fixture implementation.
Deliverable: One dev-only fixture-support crate and converted direct includes.
Context: F04; `core/fixtures/schema-v5/mapping.rs`, the 24 integration targets including it, `core/crates/editac-core/Cargo.toml`, root workspace membership and existing test support conventions.
Dependencies: none.
Independent work: RAQ-3.1 can progress without this crate; coordinate target moves through current source pins.
Session scope: Schema-v5 support only, 30–45 minutes including checks; older independent oracle conversions remain out of scope.
Acceptance: The shared mapping source is compiled in one test-support library for a given target/profile/features rather than separately in each migrated target. It is reachable only through development edges. Its logic stays independent of production admission/replay, and legacy fixture bytes remain intact. No test assertion is dropped or converted to testing the same production algorithm against itself.

Implementation:

- [x] RAQ-3.2-I1 Put the existing mapper behind a small test-only crate interface with only needed exports, retaining its original independent semantics and fixture ownership.
- [x] RAQ-3.2-I2 Replace direct includes with imports in current consumers; update Cargo dev edges and remove unused per-target copies. Preserve any test-local helpers that are genuinely specific.

Validation:

- [x] RAQ-3.2-V1 Inspect normal dependency trees for absence of fixture support, then compile/run two existing consumers with different mapped content (for example table and ownership/patch behavior). Budget: 4 minutes. Verify Cargo identifies the support implementation as one library unit; do not claim cross-target or cross-feature cache identity.

Evidence: Progress records migrated consumers, normal/dev graph separation and the selected fixture-equivalence receipts.
Handoff: Remaining include, visibility/type mismatch or oracle dependency; no production edge is allowed as a shortcut.
Blocked behavior: If support extraction couples the oracle to production or changes fixtures, preserve the independent oracle and record the offending edge; RAQ-3.1 remains eligible.

### Task RAQ-3.3 — Measure and retain only useful compile-feedback changes

- [x] RAQ-3.3 Complete one bounded compile-performance experiment batch.

Purpose: Improve the actual editor feedback loop with evidence and controlled tradeoffs.
Deliverable: An authored decision with reproducible selectors and any measured beneficial build configuration change.
Context: P01; `core/Cargo.toml`, `cli/Cargo.toml`, standalone formats roots, FFI crate types, existing build scripts, and `architecture/roadmaps/30-architecture-fitness.md` for deferred hard-cap ownership.
Dependencies: none.
Independent work: Functional delivery and RAQ-3.1/RAQ-3.2 remain eligible regardless of a tuning failure; do not repeat this batch to block them.
Session scope: At most 45 minutes total or two materially different measured hypotheses, whichever comes first, including measurement, interpretation and cleanup.
Acceptance: Report reproducible baseline and candidate results for the same source/feature/target/toolchain/job settings, separating cold, warm and incremental work. Retain a change only for a demonstrated useful improvement without breaking required debugging, test selection or build behavior. If no candidate wins, record deferral to existing final fitness; no speedup or qualification is claimed. Production browser settings and hard caps are preserved.

Implementation:

- [x] RAQ-3.3-I1 Define a bounded representative workflow: one library check, one affected integration-test build and, only if affordable, browser build. Pin inputs and account for concurrent load; use isolated task-owned copies/targets without touching another worker's source or cache.
- [x] RAQ-3.3-I2 Compare at most two justified hypotheses, prioritizing compatible per-lane cache reuse or lower development debug information. Record debugger/cache-contention tradeoffs. Revert an unsuccessful task-owned experiment, keep useful authored configuration only, and defer any FFI packaging redesign requiring a larger boundary change.

Validation:

- [x] RAQ-3.3-V1 Capture bounded Cargo timing/status results for baseline and candidate under identical inputs, plus the smallest affected functional check. Record elapsed time, output size and successful target/test counts. The total budget includes repeated measurements; stop for an inconclusive noisy result instead of presenting it as improvement.
- [x] RAQ-3.3-V2 Recheck data-volume space, verify no task-owned build process is active, and remove this batch's inactive outputs. Record exact removed paths and reclaimed/free space; preserve other work and failure diagnostics needed for a concrete repair.

Evidence: Progress stores workload, raw-result locations only while needed, concise comparison, decision, retained config and any explicit final-fitness deferral.
Handoff: Hypothesis, source/config pins, observed limit and exact deferred owner/resume condition. No new optimization batch follows without changed scope and controller authorization.
Blocked behavior: Stop at the budget or first unchanged failed hypothesis. Record measured non-adoption/deferment when conclusive, or a specific environment blocker when not; continue independent feature work without another optimization batch.

## Source handoff

Record final test ownership/selector mapping, dev-only fixture interface,
performance decision and compatible focused receipts in progress. RAQ-4.4 owns
remaining topology, lint and build-feedback verification; source closure does
not require another full test or timing run.
