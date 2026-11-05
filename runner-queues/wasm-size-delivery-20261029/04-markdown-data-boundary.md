# Remove document restoration from the Markdown companion

Status: IN_PROGRESS

Goal: Remove document restoration from the Markdown companion with preserved behavior and measured delivery accounting.

Entry conditions: WSD-1.3 exact request/result schema is explicitly adopted and its preservation matrix is available; pending adoption blocks this file only. WSD-1.1 baseline/candidate authority is valid. Use current core/Markdown producer receipts, independent of whether highlighting is complete. Do not load historical Deep Review tasks.

Canonical ownership: Decomposition of WEX-6.3/6.4; core remains the only mutable semantic authority.

Progress: `.roadmap-runner/wasm-size-delivery-20261029/04-markdown-data-boundary.progress.md`.

## Execution contract

Paths beginning `../core` are relative to the architecture repository; `.roadmap-runner/` progress paths are relative to the workspace root. Run core commands from `core/`, using its pinned installed toolchain. Read the current task and its named symbols only: normally at most 8 files or 600 relevant lines; expand for a named dependency, or request a controller split. Do one parent per iteration, serially on existing main after the active worker releases ownership. Do not create another checkout/controller or alter active queue/history.

This proposed source does not authorize execution, renew the exhausted size-tuning allowance, adopt an API change, or start a runner. Before size-motivated candidates, require a recorded explicit scope/time/hypothesis decision and the shared ledger. Session estimates below are scheduling estimates, not additional experiment time. Stop at the shared deadline or hypothesis limit. No unchanged retry, repeated completed contract, paid inference, secrets, native qualification, publication or deployment. Preserve all current features, one canonical kernel/format, safety, Unicode, recovery, history, original failures, and unrelated dirty/staged bytes.

Use current narrow tests during functionality. New suites, comprehensive cases and cross-file coverage belong only to source 06. Existing scripts sometimes pack/build or start browsers in setup: inspect the named test setup, freeze exact selectors, isolate outputs, and count that cost before running. No zero-match or skipped check proves acceptance. Reuse compatible evidence. Record executed/passed/failed/skipped counts and changed-input reasons for reruns. Candidate rejection does not complete an implementation task promising a reduction.

Each task writes only verified source checkboxes/Status and a separate progress handoff. Progress includes deliverable paths, exact source/artifact pins, selector/setup, results, measured byte deltas, authority consumed, remaining gaps and next action. Missing authority or adoption blocks only its dependent work; controller schedules eligible independent files before a blocked branch. This draft is not safe to enqueue wholesale without resolving its entry conditions.

## Tasks

### Task WSD-4.1 — Extract pure table-source formatting over inert inputs

- [ ] WSD-4.1 Extract pure table-source formatting over inert inputs.

Purpose: Make codec work independent of Document without a second implementation.
Deliverable: Extract pure table-source formatting over inert inputs, with the concrete result and checks in this task's acceptance.
Context: Adopted WSD-1.3 schema; ../core/crates/editac-markdown/src/{reconcile,table_format}.rs; exact inert type owner selected by the proposal.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: none.
Independent work: Any ready task whose own inputs and authority are valid.
Session scope: 25–35 minutes; one pure function/type seam.
Acceptance: One canonical formatting/recovery implementation accepts bounded inert table/source values. Existing native callers adapt to it with identical results; no public ABI changes yet and no duplicate formatter. Input limits and error fidelity are preserved. A new types crate is allowed only if the adopted dependency map requires it.

Implementation:

- [ ] WSD-4.1-I1 Extract pure formatting/recovery from Document access and route the existing implementation through it. Keep projections and type ownership exactly as adopted.
- [ ] WSD-4.1-I2 Remove generic wrappers only where extraction makes them redundant; do not replace the entire Markdown parser or change supported grammar.

Validation:

- [ ] WSD-4.1-V1 Run existing cargo test -p editac-markdown --locked --offline with the exact table_format/reconcile test filters discovered from these modules; budget 3 minutes. Record matched cases; zero matches are a failure, not a pass.

Evidence: This file's separate progress record, task `WSD-4.1`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.

### Task WSD-4.2 — Prepare authoritative inert projections in the kernel

- [ ] WSD-4.2 Prepare authoritative inert projections in the kernel.

Purpose: Keep identity, stale-source and target validation at the existing owner.
Deliverable: Prepare authoritative inert projections in the kernel, with the concrete result and checks in this task's acceptance.
Context: WSD-4.1 types; ../core/crates/editac-bridge/src/bridge.rs: prepare_table_source; ../core/crates/editac-core document/projection helpers named in the adopted schema.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: WSD-4.1.
Independent work: Any ready task whose own inputs and authority are valid.
Session scope: 25–35 minutes; private kernel adapter only.
Acceptance: Private kernel code produces the adopted opening/current projection and validates identity, baseline equality, resource limits and target before preparing a change. No second replica is introduced for the codec. Existing exported path remains coherent until the atomic switch in WSD-4.3; no alternative production wire format is added.

Implementation:

- [ ] WSD-4.2-I1 Implement the private projection/validation adapter using existing document/plan ownership and limits.
- [ ] WSD-4.2-I2 Route existing native preparation through shared validation where appropriate without weakening errors or adding an alias API.

Validation:

- [ ] WSD-4.2-V1 Select successful, stale and foreign-target table_source_cases in editac-bridge with cargo test -p editac-bridge --locked --offline and exact discovered filters; budget 3 minutes. Confirm rejection before mutation and unchanged history count.

Evidence: This file's separate progress record, task `WSD-4.2`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.

### Task WSD-4.3 — Switch the codec and public adapter atomically

- [ ] WSD-4.3 Switch the codec and public adapter atomically.

Purpose: Remove the exported path that restores snapshots in the codec.
Deliverable: Switch the codec and public adapter atomically, with the concrete result and checks in this task's acceptance.
Context: Adopted schema and WSD-4.1/4.2; ../core/crates/editac-markdown-wasm/src/lib.rs; ../core/crates/editac-wasm/src/engine.rs; ../core/packages/{core/src/engine.ts,markdown/src/index.ts}; affected declarations.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: WSD-4.2.
Independent work: Any ready task whose own inputs and authority are valid.
Session scope: 35–45 minutes; one atomic ABI/adaptor cutover. Controller splits if the adopted map cannot fit before dispatch.
Acceptance: Capture/recover/prepare use only the adopted inert contract. Remove SnapshotInput::restore and superseded exported checkpoint decoding, with one current production interface. Preserve current recovery text, unknown attributes, Unicode, stale rejection, bounded errors, permissions and one history group. No speculative compatibility alias or silent stored-data conversion.

Implementation:

- [ ] WSD-4.3-I1 Switch kernel export, Wasm codec entry and TS adapter/declarations in one coherent change. Stop passing baseline/current checkpoint bytes into the companion.
- [ ] WSD-4.3-I2 Delete superseded production entry/types only after all listed consumers use the adopted contract; retain original regression assertions and source history.

Validation:

- [ ] WSD-4.3-V1 Run focused existing Markdown roundtrip and table-source success/recovery/stale/atomic cases and installed declaration checks from tests/markdown-codec.test.mjs plus the adopted matrix selectors. Budget 6 minutes. Read setup first; use task-owned EDITAC_MARKDOWN_OUTPUT and current artifacts. Add a single regression early only for an uncovered concrete cutover defect.

Evidence: This file's separate progress record, task `WSD-4.3`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.

### Task WSD-4.4 — Remove the codec dependency roots and measure the union

- [ ] WSD-4.4 Remove the codec dependency roots and measure the union.

Purpose: Verify that extraction removes delivered code rather than moving bytes.
Deliverable: Remove the codec dependency roots and measure the union, with the concrete result and checks in this task's acceptance.
Context: ../core/crates/editac-markdown{,-wasm}/Cargo.toml and affected pure type owner; current normal-target tree; current core and Markdown artifacts; WSD-4.3 consumer proof.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: WSD-4.3.
Independent work: Any ready task whose own inputs and authority are valid.
Session scope: 20–30 minutes; one dependency/artifact closure.
Acceptance: No codec export reaches Document::restore, live Yrs ownership or checkpoint admission. Remove normal-target dependencies only when actually unused; a remaining inert core edge is not itself a failure if emitted restore roots are absent. Bind removed roots to emitted artifacts and report core+codec+glue and complete required union deltas. Preserve notices for every retained dependency.

Implementation:

- [ ] WSD-4.4-I1 Inspect the selected normal feature graph and emitted roots; remove unused dependency edges/features and update notices with the existing generator.
- [ ] WSD-4.4-I2 Build the affected shipping artifacts once under admitted controls. Attribute both added core and removed companion cost; do not add separate estimated gzip savings.

Validation:

- [ ] WSD-4.4-V1 Reuse WSD-4.3 semantics when exact inputs permit; run the packed stateless exports/declarations selector after rebuilding, plus artifact-root and feature audits. Budget 3 minutes plus scoped build; record changed-input reasons for any rerun.

Evidence: This file's separate progress record, task `WSD-4.4`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.
