# Bind evidence and prepare boundary decisions

Status: COMPLETE

Goal: Bind evidence and prepare boundary decisions with preserved behavior and measured delivery accounting.

Entry conditions: Read-only planning may proceed now. Source/code edits require the active single-main worker to finish and release the checkout. Read only the investigation sections named by the current task. No new compilation, runtime experiment or optimization allowance is required for this file.

Canonical ownership: WEX-9.1 evidence reuse; WEX-6.3 boundary proposal; new npm distribution proposal. This file does not redo the completed build audit.

Progress: `.roadmap-runner/wasm-size-delivery-20261029/01-baseline-and-decisions.progress.md`.

## Execution contract

Paths beginning `../core` are relative to the architecture repository; `.roadmap-runner/` progress paths are relative to the workspace root. Run core commands from `core/`, using its pinned installed toolchain. Read the current task and its named symbols only: normally at most 8 files or 600 relevant lines; expand for a named dependency, or request a controller split. Do one parent per iteration, serially on existing main after the active worker releases ownership. Do not create another checkout/controller or alter active queue/history.

This proposed source does not authorize execution, renew the exhausted size-tuning allowance, adopt an API change, or start a runner. Before size-motivated candidates, require a recorded explicit scope/time/hypothesis decision and the shared ledger. Session estimates below are scheduling estimates, not additional experiment time. Stop at the shared deadline or hypothesis limit. No unchanged retry, repeated completed contract, paid inference, secrets, native qualification, publication or deployment. Preserve all current features, one canonical kernel/format, safety, Unicode, recovery, history, original failures, and unrelated dirty/staged bytes.

Use current narrow tests during functionality. New suites, comprehensive cases and cross-file coverage belong only to source 06. Existing scripts sometimes pack/build or start browsers in setup: inspect the named test setup, freeze exact selectors, isolate outputs, and count that cost before running. No zero-match or skipped check proves acceptance. Reuse compatible evidence. Record executed/passed/failed/skipped counts and changed-input reasons for reruns. Candidate rejection does not complete an implementation task promising a reduction.

Each task writes only verified source checkboxes/Status and a separate progress handoff. Progress includes deliverable paths, exact source/artifact pins, selector/setup, results, measured byte deltas, authority consumed, remaining gaps and next action. Missing authority or adoption blocks only its dependent work; controller schedules eligible independent files before a blocked branch. This draft is not safe to enqueue wholesale without resolving its entry conditions.

## Tasks

### Task WSD-1.1 — Bind the retained baseline and candidate protocol

- [x] WSD-1.1 Bind the retained baseline and candidate protocol.

Purpose: Prevent stale receipts, repeated tuning and false budget passes.
Deliverable: Bind the retained baseline and candidate protocol, with the concrete result and checks in this task's acceptance.
Context: research/wasm-size-delivery-investigation-20261029.md, Evidence and Current budgets; ../.roadmap-runner/wex-production-repair-20261028/{current-matrix-facts,WEX-9.1-current-audit,final-owner-matrix}.json; specs/verification.md, bundle budgets and shared optimization allowance.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: none.
Independent work: Any ready task whose own inputs and authority are valid.
Session scope: 20 minutes; static evidence only.
Acceptance: A compact progress record identifies current source/artifact hashes, default Task/core/expanded inventories, four canonical hard gates, current tuning authority and missing regression inputs. Distinguish current dist from dirty source. Record zero available candidate time unless a later explicit decision changes it. List completed checks eligible for reuse and each changed-input reason that would invalidate them. Do not recreate WEX-7.1/WEX-8.1.

Implementation:

- [x] WSD-1.1-I1 Authenticate the existing 5 Wasm hashes and relevant package input hashes; inspect changed files only. Retain old failure identities and consumer names.
- [x] WSD-1.1-I2 For the first proposed candidate, define exact changed input, frozen flags, affected consumers, required semantic checks, cold/compile/first-use and input/memory regression limits from the existing verification contract. Missing telemetry is an entry blocker for candidate adoption; do not invent permissive limits. Record one shared time/hypothesis ledger and remaining authority.

Validation:

- [x] WSD-1.1-V1 Reconcile the arithmetic with the investigation table and manifest resource union; 3-minute static check. Record matched/mismatched/missing counts and source pins. No fresh all-profile pack or benchmark.

Evidence: This file's separate progress record, task `WSD-1.1`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.

### Task WSD-1.2 — Specify production versus fixture package contents

- [x] WSD-1.2 Specify production versus fixture package contents.

Purpose: Remove known test-support payload from normal npm installs without breaking declared imports.
Deliverable: Specify production versus fixture package contents, with the concrete result and checks in this task's acceptance.
Context: ../core/packages/core/{package.json,src/fixture.ts}; ../core/tests/{wasm-load,packed-consumers}.test.mjs; ../core/scripts/prepare-browser-size.mjs; investigation, npm archives.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: none.
Independent work: WSD-1.3 can proceed independently; neither proposal waits for LTO.
Session scope: 20–30 minutes; one distribution decision, no package rewrite.
Acceptance: A reviewable authored proposal names the exact production export/file allowlist, how fixture consumers continue to load actual fixture Wasm, build ownership, affected imports and license coverage. Recommend a separate dev/test-support distribution; use a concrete layout after tracing consumers. Record adopted or awaiting-adoption status. Proposal completion does not authorize breaking exports or claim compressed savings.

Implementation:

- [x] WSD-1.2-I1 Enumerate fixture-export users and all six shipped fixture files. Separate test URL names from actual @edit-ac/core/fixture users.
- [x] WSD-1.2-I2 Write a bounded proposal under architecture/decisions/ with an exact old/new export map, single owner for shared engine wrapper source, migration steps and rollback. Freeze the chosen layout for WSD-2.1; do not make that worker redesign packaging.

Validation:

- [x] WSD-1.2-V1 Cross-check every production export and every actual fixture consumer against the proposed map; 3 minutes, static only. Record the adoption reference or precise pending decision.

Evidence: This file's separate progress record, task `WSD-1.2`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.

### Task WSD-1.3 — Specify the inert Markdown table-source contract

- [x] WSD-1.3 Specify the inert Markdown table-source contract.

Purpose: Remove companion-owned document restoration while retaining kernel authority.
Deliverable: Specify the inert Markdown table-source contract, with the concrete result and checks in this task's acceptance.
Context: ../core/crates/editac-markdown-wasm/src/lib.rs: SnapshotInput::restore/table_source_value; ../core/crates/editac-markdown/src/{reconcile,table_format}.rs; ../core/crates/editac-bridge/src/bridge.rs: prepare_table_source; ../core/packages/{core/src/engine.ts,markdown/src/index.ts}; specs/extension-dx.md.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: none.
Independent work: WSD-1.2 and source 03 source/license analysis are independent.
Session scope: 30 minutes; one concrete contract proposal, at most 8 named source files.
Acceptance: The proposal gives exact request/result schemas and byte/count limits for capture/recover/prepare, opening/current identity checks, stale detection, unknown-data recovery, errors and atomic commit. The kernel owns all document validation/restore/mutation; the codec owns pure parsing/formatting. Include a call graph of removed restore roots and possible new core cost. Explicit adoption remains required before source 04; a proposal can be completed while its adoption is pending.

Implementation:

- [x] WSD-1.3-I1 Trace the current capture/recover/prepare path and list the existing assertions that must remain true. Specify immutable projections and kernel validation results, not raw Rust pointers or a second writable replica.
- [x] WSD-1.3-I2 Write the proposal in the existing extension-DX contract with matching WSD-4 acceptance; identify the authoritative types and exact pure helper extraction. Keep original WEX-6.3 adoption open until a recorded controller/user decision.

Validation:

- [x] WSD-1.3-V1 Cross-check stale/foreign identity, strict baseline equality, recovery, bounds and unknown-data behavior against current call sites; 4-minute static review. Record remaining questions and adoption state.

Evidence: This file's separate progress record, task `WSD-1.3`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.
