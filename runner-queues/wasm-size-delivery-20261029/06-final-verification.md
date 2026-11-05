# Close coverage and reconcile unchanged hard gates

Status: IN_PROGRESS

Goal: Close coverage and reconcile unchanged hard gates with preserved behavior and measured delivery accounting.

Entry conditions: All adopted functional changes are implemented and individually validated. Record deferred/rejected candidates honestly; pending required work is not a completed optimization or cap pass. Consume the compact per-file progress evidence, not every historical log. This is the only owner for new comprehensive test development and cross-file validation.

Canonical ownership: Feeds existing WEX-4.1/4.2/4.3 and WEX-5.2/5.3, FIT/QPF gates; no duplicate final qualification track.

Progress: `.roadmap-runner/wasm-size-delivery-20261029/06-final-verification.progress.md`.

## Execution contract

Paths beginning `../core` are relative to the architecture repository; `.roadmap-runner/` progress paths are relative to the workspace root. Run core commands from `core/`, using its pinned installed toolchain. Read the current task and its named symbols only: normally at most 8 files or 600 relevant lines; expand for a named dependency, or request a controller split. Do one parent per iteration, serially on existing main after the active worker releases ownership. Do not create another checkout/controller or alter active queue/history.

This proposed source does not authorize execution, renew the exhausted size-tuning allowance, adopt an API change, or start a runner. Before size-motivated candidates, require a recorded explicit scope/time/hypothesis decision and the shared ledger. Session estimates below are scheduling estimates, not additional experiment time. Stop at the shared deadline or hypothesis limit. No unchanged retry, repeated completed contract, paid inference, secrets, native qualification, publication or deployment. Preserve all current features, one canonical kernel/format, safety, Unicode, recovery, history, original failures, and unrelated dirty/staged bytes.

Use current narrow tests during functionality. New suites, comprehensive cases and cross-file coverage belong only to source 06. Existing scripts sometimes pack/build or start browsers in setup: inspect the named test setup, freeze exact selectors, isolate outputs, and count that cost before running. No zero-match or skipped check proves acceptance. Reuse compatible evidence. Record executed/passed/failed/skipped counts and changed-input reasons for reruns. Candidate rejection does not complete an implementation task promising a reduction.

Each task writes only verified source checkboxes/Status and a separate progress handoff. Progress includes deliverable paths, exact source/artifact pins, selector/setup, results, measured byte deltas, authority consumed, remaining gaps and next action. Missing authority or adoption blocks only its dependent work; controller schedules eligible independent files before a blocked branch. This draft is not safe to enqueue wholesale without resolving its entry conditions.

## Tasks

### Task WSD-6.1 — Fill remaining semantic and regression coverage

- [ ] WSD-6.1 Fill remaining semantic and regression coverage.

Purpose: Prove preservation across the changed boundaries once.
Deliverable: Fill remaining semantic and regression coverage, with the concrete result and checks in this task's acceptance.
Context: Progress acceptance matrices from sources 02–05; existing highlighting corpus, Markdown table-source cases, wasm-error-contract, input/selection and optional resource lifecycle tests; specs/verification.md.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: none.
Independent work: Any ready task whose own inputs and authority are valid.
Session scope: 30–45 minutes per bounded uncovered group; controller splits before dispatch if the gap matrix needs more.
Acceptance: Every changed invariant has one test owner and matching current-artifact proof. Cover grammar cross-references/multiline UTF-16/fallback, Markdown unknown data/stale/foreign/atomic recovery, malformed/duplicate fields, and changed input/IME/a11y paths. Cold/compile/first-use/input/memory regression cells required by the selected candidates are complete. Reuse unchanged passing coverage; preserve original failure assertions and unrelated native deferrals.

Implementation:

- [ ] WSD-6.1-I1 Build one coverage-gap matrix from retained checks. Author only missing deterministic cases; use prepared fixtures and no provider/credential work.
- [ ] WSD-6.1-I2 Bind exact current artifacts to any new test/runtime observations. Do not run broad suites solely because a roadmap boundary or commit changed.

Validation:

- [ ] WSD-6.1-V1 Execute only the uncovered or invalidated cases and contract-required observations, recording selectors, executed/passed/failed/skipped counts and failure inputs. Budget at most 10 minutes execution within this session; split concrete excess before running. Missing telemetry remains unresolved.

Evidence: This file's separate progress record, task `WSD-6.1`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.

### Task WSD-6.2 — Verify packed delivery, caching and provenance

- [ ] WSD-6.2 Verify packed delivery, caching and provenance.

Purpose: Ensure smaller source actually reaches clean consumers safely.
Deliverable: Verify packed delivery, caching and provenance, with the concrete result and checks in this task's acceptance.
Context: Current package exports/build receipts; tests/{packed-consumers,extension-exports,browser-size-http,http-assets}.test.mjs; scripts/{prepare-browser-size,browser-size-contract,http-assets}.mjs; current grammar notice identities.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: none.
Independent work: Any ready task whose own inputs and authority are valid.
Session scope: 30–40 minutes; one changed-artifact clean-consumer and delivery pass.
Acceptance: Clean packed consumers resolve real files/declarations without workspace aliases; production archives omit fixture payload per the adopted map. All enabled companions/workers/grammars/notices are present once, with correct immutable identities. HTTP gzip/Brotli decode to exact admitted bytes, wrong/corrupt assets fail before mutation, and loader singleton/retry/destroy behavior holds. No new publication or native qualification.

Implementation:

- [ ] WSD-6.2-I1 Reuse the current package and HTTP harnesses. Extend missing pack/export/duplicate-owner guards only where functional changes require them.
- [ ] WSD-6.2-I2 Select representative Task and expanded consumers and changed optional resources; bind package, graph and decoded byte identities. Preserve output and server ownership until checks finish.

Validation:

- [ ] WSD-6.2-V1 Run the affected packed/declaration/SSR cases and the changed HTTP/loader matrix once; reuse unaffected browser cells. Budget 8 minutes. Stop all owned servers/browsers in finally/teardown and record cleanup plus exact notices coverage.

Evidence: This file's separate progress record, task `WSD-6.2`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.

### Task WSD-6.3 — Measure final unions and preserve honest cap status

- [ ] WSD-6.3 Measure final unions and preserve honest cap status.

Purpose: Determine whether the actual package and delivered-code goals were met.
Deliverable: Measure final unions and preserve honest cap status, with the concrete result and checks in this task's acceptance.
Context: WSD-6.1/6.2 proof; scripts/check-browser-size.mjs and browser-size-contract.mjs; specs/verification.md; source 01 frozen baseline and original WEX failures.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: WSD-6.1, WSD-6.2.
Independent work: Any ready task whose own inputs and authority are valid.
Session scope: 20–30 minutes; one final accounting/admission pass.
Acceptance: Report paired npm packed/unpacked, raw/gzip/Brotli per resource, default Task/core/expanded JS+total, initial/deferred/site unions and standalone/incremental optional costs. Preserve limits 524288/32768 and 1048576/131072 and planning allocations. Pass only when every required hard gate and current functional/delivery requirement passes. Remaining gap means PROBLEM with exact bytes, owner and changed-input prerequisite; never COMPLETE-by-deferral or an automatic tuning restart.

Implementation:

- [ ] WSD-6.3-I1 Prepare the complete required inventory once using EDITAC_BROWSER_SIZE_OUTPUT in an ignored task-owned directory and node scripts/check-browser-size.mjs --inventory; bind the frozen expanded configuration as well. Capture expected nonzero budget exits and full small diagnostics instead of masking them.
- [ ] WSD-6.3-I2 Reconcile actual deltas and current test receipts to canonical WEX/FIT/QPF owners; do not mark original historical failures passed. Keep adopted/rejected/deferred candidates distinct, and retain no imaginary estimated savings.

Validation:

- [ ] WSD-6.3-V1 Check duplicate/missing resource controls and all four hard gates with the canonical checker; record nonzero counts, exact failures and size differences. Budget 7 minutes including the one matrix preparation; reuse identical receipts. Verify no task-owned listeners/processes remain and check disk space; remove only this run’s inactive reproducible outputs.

Evidence: This file's separate progress record, task `WSD-6.3`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.
