# Reduce package payload and fix the production link

Status: IN_PROGRESS

Goal: Reduce package payload and fix the production link with preserved behavior and measured delivery accounting.

Entry conditions: WSD-1.1 baseline/protocol is bound. WSD-2.1 additionally requires the adopted WSD-1.2 export/layout proposal. WSD-2.2/2.3 require explicit available tuning authority and the candidate regression inputs from WSD-1.1; the historical allowance is not renewed. Current worker must release shared source/dist before edits or builds. These branches are independent.

Canonical ownership: New npm distribution work; existing WEX-3.1/3.2 compiler selection/adoption and WEX-9.1 effective flags.

Progress: `.roadmap-runner/wasm-size-delivery-20261029/02-package-and-production-link.progress.md`.

## Execution contract

Paths beginning `../core` are relative to the architecture repository; `.roadmap-runner/` progress paths are relative to the workspace root. Run core commands from `core/`, using its pinned installed toolchain. Read the current task and its named symbols only: normally at most 8 files or 600 relevant lines; expand for a named dependency, or request a controller split. Do one parent per iteration, serially on existing main after the active worker releases ownership. Do not create another checkout/controller or alter active queue/history.

This proposed source does not authorize execution, renew the exhausted size-tuning allowance, adopt an API change, or start a runner. Before size-motivated candidates, require a recorded explicit scope/time/hypothesis decision and the shared ledger. Session estimates below are scheduling estimates, not additional experiment time. Stop at the shared deadline or hypothesis limit. No unchanged retry, repeated completed contract, paid inference, secrets, native qualification, publication or deployment. Preserve all current features, one canonical kernel/format, safety, Unicode, recovery, history, original failures, and unrelated dirty/staged bytes.

Use current narrow tests during functionality. New suites, comprehensive cases and cross-file coverage belong only to source 06. Existing scripts sometimes pack/build or start browsers in setup: inspect the named test setup, freeze exact selectors, isolate outputs, and count that cost before running. No zero-match or skipped check proves acceptance. Reuse compatible evidence. Record executed/passed/failed/skipped counts and changed-input reasons for reruns. Candidate rejection does not complete an implementation task promising a reduction.

Each task writes only verified source checkboxes/Status and a separate progress handoff. Progress includes deliverable paths, exact source/artifact pins, selector/setup, results, measured byte deltas, authority consumed, remaining gaps and next action. Missing authority or adoption blocks only its dependent work; controller schedules eligible independent files before a blocked branch. This draft is not safe to enqueue wholesale without resolving its entry conditions.

## Tasks

### Task WSD-2.1 — Apply the adopted fixture distribution split

- [ ] WSD-2.1 Apply the adopted fixture distribution split.

Purpose: Stop production npm consumers downloading the fixture implementation.
Deliverable: Apply the adopted fixture distribution split, with the concrete result and checks in this task's acceptance.
Context: WSD-1.2 adopted layout/export map and consumer list; ../core/packages/core/package.json; ../core/packages/core/src/fixture.ts; affected package build and pack scripts; ../core/tests/wasm-load.test.mjs.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: none.
Independent work: Any ready task whose own inputs and authority are valid.
Session scope: 30–45 minutes; one atomic packaging/migration unit. If the adopted map exceeds 8 implementation files, controller splits it before dispatch.
Acceptance: Production core archives contain no fixture Wasm, fixture glue or removed fixture exports; the adopted test-support distribution still executes real fixture behavior. Every production export, declaration and notice resolves from a packed install. Shared source has one owner. Report actual tgz and unpacked differences separately; no browser-cap saving is claimed from fixture removal.

Implementation:

- [ ] WSD-2.1-I1 Apply exactly the adopted package/build/export map and migrate its listed fixture consumers in the same task. Keep generated packages and staged manifests ignored.
- [ ] WSD-2.1-I2 Use explicit package allowlists; preserve comparison/production Wasm and declaration assets. Remove stale generated fixture files only from the production staging directory, never from live tests or unrelated dist.

Validation:

- [ ] WSD-2.1-V1 Run the existing wasm-load packed fixture/production selection and SSR export cases with nonzero matching counts; inspect production and test-support tar entries and installed declarations. Budget 5 minutes, reused current Wasm where unchanged. Store exact commands and paired tgz sizes; no full browser suite.

Evidence: This file's separate progress record, task `WSD-2.1`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.

### Task WSD-2.2 — Test one effective-LTO core producer

- [ ] WSD-2.2 Test one effective-LTO core producer.

Purpose: Correct the observed mixed-crate-type LTO omission before other compiler tuning.
Deliverable: Test one effective-LTO core producer, with the concrete result and checks in this task's acceptance.
Context: ../core/scripts/{build-wasm,wasm-build-receipt,optimize-wasm}.mjs; ../core/Cargo.toml; ../core/crates/editac-wasm/Cargo.toml; WSD-1.1 selected candidate protocol.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: none.
Independent work: WSD-2.1 can proceed when its adoption gate is satisfied, even if LTO is unavailable.
Session scope: 20–30 minutes including one matched candidate; charged to explicitly available shared tuning time.
Acceptance: Shipping core requests only cdylib through Cargo selection and the actual root rustc invocation includes the intended LTO. Fixture/native/rlib policy is preserved. Receipt/staging, allowed features and public import/export boundary remain valid. Adopt only with measured raw/gzip union improvement, passing affected semantics and bound runtime observations; otherwise retain baseline and leave implementation/adoption unchecked with a specific disposition.

Implementation:

- [ ] WSD-2.2-I1 Change only the shipping build invocation to cargo rustc --lib --crate-type cdylib under the unchanged browser profile and locked offline toolchain. Do not append contradictory crate types after -- or mutate every library manifest.
- [ ] WSD-2.2-I2 Capture actual rustc flags; stop if LTO is still missing. Compare one retained/candidate core artifact using the existing optimizer/receipt and exact current consumers. No s/z or optimizer sweep in this task.

Validation:

- [ ] WSD-2.2-V1 Run node --test tests/wasm-error-contract.test.mjs and the affected production cases of tests/wasm-glue-sharing.test.mjs from core, plus the current ABI/feature audit; budget 4 minutes excluding the already scoped build. Reuse unchanged results, inspect no-growth checks and run only protocol-required runtime observations. Record counts, byte deltas and candidate time.

Evidence: This file's separate progress record, task `WSD-2.2`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.

### Task WSD-2.3 — Apply the accepted shipping link to companions

- [ ] WSD-2.3 Apply the accepted shipping link to companions.

Purpose: Keep all shipping producers on the same proven link policy.
Deliverable: Apply the accepted shipping link to companions, with the concrete result and checks in this task's acceptance.
Context: ../core/scripts/{build-wasm,build-highlight-worker,wasm-build-receipt}.mjs; three companion Cargo manifests; WSD-2.2 retained settings and receipts.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: WSD-2.2.
Independent work: Source 03 source/license analysis remains independent; companion adoption waits for its own passing checks.
Session scope: 25–35 minutes; one producer family, part of the same recorded LTO hypothesis, not a new allowance.
Acceptance: Markdown, highlighting and comparison shipping builds each show effective LTO, preserve their exports/features/notices and use the existing staged optimizer. All actual companion deltas and combined unions are recorded; failures are not hidden by another artifact shrinking. No new native qualification is claimed.

Implementation:

- [ ] WSD-2.3-I1 Reuse the accepted Cargo invocation for the existing Markdown/comparison modes and highlighting producer. Preserve probe/fixture behavior and explicit output directories.
- [ ] WSD-2.3-I2 Build each affected shipping companion once and bind the exact artifacts to production receipts; stop the family on an ABI, semantic or bound runtime regression.

Validation:

- [ ] WSD-2.3-V1 Select existing Markdown stateless roundtrip/export checks, highlighting production parity/fallback checks and comparison contract checks using their documented current receipt setup. Budget 6 minutes plus scoped builds; name exact selectors before running. Reuse core proof and do not repeat all 16 consumer preparations.

Evidence: This file's separate progress record, task `WSD-2.3`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.
