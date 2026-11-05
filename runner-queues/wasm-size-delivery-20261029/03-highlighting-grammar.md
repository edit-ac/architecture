# Generate only required highlighting grammar data

Status: IN_PROGRESS

Goal: Generate only required highlighting grammar data with preserved behavior and measured delivery accounting.

Entry conditions: Reuse repaired WEX-6.1 producer and current grammar/notices identities. WSD-3.1 is static and independent of LTO. WSD-3.2/3.3 require available authority for grammar candidate work plus WSD-1.1 baseline; compare against the current admitted producer (whether LTO was adopted or deferred). Do not treat source 02 completion as a semantic prerequisite.

Canonical ownership: Decomposition of existing WEX-6.2; existing RCH highlighting semantics remain authoritative.

Progress: `.roadmap-runner/wasm-size-delivery-20261029/03-highlighting-grammar.progress.md`.

## Execution contract

Paths beginning `../core` are relative to the architecture repository; `.roadmap-runner/` progress paths are relative to the workspace root. Run core commands from `core/`, using its pinned installed toolchain. Read the current task and its named symbols only: normally at most 8 files or 600 relevant lines; expand for a named dependency, or request a controller split. Do one parent per iteration, serially on existing main after the active worker releases ownership. Do not create another checkout/controller or alter active queue/history.

This proposed source does not authorize execution, renew the exhausted size-tuning allowance, adopt an API change, or start a runner. Before size-motivated candidates, require a recorded explicit scope/time/hypothesis decision and the shared ledger. Session estimates below are scheduling estimates, not additional experiment time. Stop at the shared deadline or hypothesis limit. No unchanged retry, repeated completed contract, paid inference, secrets, native qualification, publication or deployment. Preserve all current features, one canonical kernel/format, safety, Unicode, recovery, history, original failures, and unrelated dirty/staged bytes.

Use current narrow tests during functionality. New suites, comprehensive cases and cross-file coverage belong only to source 06. Existing scripts sometimes pack/build or start browsers in setup: inspect the named test setup, freeze exact selectors, isolate outputs, and count that cost before running. No zero-match or skipped check proves acceptance. Reuse compatible evidence. Record executed/passed/failed/skipped counts and changed-input reasons for reruns. Candidate rejection does not complete an implementation task promising a reduction.

Each task writes only verified source checkboxes/Status and a separate progress handoff. Progress includes deliverable paths, exact source/artifact pins, selector/setup, results, measured byte deltas, authority consumed, remaining gaps and next action. Missing authority or adoption blocks only its dependent work; controller schedules eligible independent files before a blocked branch. This draft is not safe to enqueue wholesale without resolving its entry conditions.

## Tasks

### Task WSD-3.1 — Pin the transitive grammar source closure

- [ ] WSD-3.1 Pin the transitive grammar source closure.

Purpose: Avoid shipping an incomplete three-language subset.
Deliverable: Pin the transitive grammar source closure, with the concrete result and checks in this task's acceptance.
Context: ../core/crates/editac-highlighting/{src/lib.rs,examples/grammar_inventory.rs}; ../core/fixtures/highlighting/backend.json; ../core/licenses/highlighting/; decisions/highlighting-backend.md; pinned Syntect 5.3.0/two-face 0.5.2 source.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: none.
Independent work: Any ready task whose own inputs and authority are valid.
Session scope: 20–30 minutes; source/dependency/license analysis only.
Acceptance: A deterministic recipe names Rust, TypeScript, JSON, required Plain Text and every referenced syntax/context source, pinned revisions/hashes, newline semantics and notice mapping. Missing source or unresolved references have a precise owner and unblock input. No runtime-loaded full bundle is presented as a subset.

Implementation:

- [ ] WSD-3.1-I1 Inspect linked and source grammar references, including embedded-language and prototype includes. Identify authenticated source availability; acquire no unpinned replacement.
- [ ] WSD-3.1-I2 Write the recipe/input manifest and required license map as authored source. Document closure traversal and how an unresolved reference fails generation.

Validation:

- [ ] WSD-3.1-V1 Compare the closure with existing grammar identities and scope/fallback requirements; 3 minutes. Record missing references explicitly. No candidate binary or performance probe.

Evidence: This file's separate progress record, task `WSD-3.1`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.

### Task WSD-3.2 — Implement the offline grammar generator

- [ ] WSD-3.2 Implement the offline grammar generator.

Purpose: Produce a reproducible asset without embedding all grammars.
Deliverable: Implement the offline grammar generator, with the concrete result and checks in this task's acceptance.
Context: WSD-3.1 pinned recipe; ../core/crates/editac-highlighting build tooling; pinned Syntect SyntaxSetBuilder/dump APIs; ../core/.gitignore.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: WSD-3.1.
Independent work: Any ready task whose own inputs and authority are valid.
Session scope: 30 minutes; one offline build-tool boundary, no runtime switch yet.
Acceptance: The generator fails on missing or unlinked contexts, generates only the approved transitive closure with required fallback/newline behavior, and produces identical bytes for identical pinned inputs. Generated packs stay ignored. Runtime no longer needs two-face solely to construct that pack after WSD-3.3; generator dependencies are separate from normal target dependencies.

Implementation:

- [ ] WSD-3.2-I1 Add the smallest build-time generator to the adopted crate/build convention. Emit to an explicit ignored target-owned directory and use pinned offline inputs.
- [ ] WSD-3.2-I2 Generate a compact identity/notice manifest beside the output; do not commit binary packs or copy the full bundle and filter at runtime.

Validation:

- [ ] WSD-3.2-V1 Generate twice in separate task-owned outputs and compare hashes, language/reference inventories and absence of unlinked contexts. Budget 3 minutes within candidate authority. This is a build determinism check, not broad parser qualification.

Evidence: This file's separate progress record, task `WSD-3.2`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.

### Task WSD-3.3 — Load the subset in the production highlighter

- [ ] WSD-3.3 Load the subset in the production highlighter.

Purpose: Remove the full grammar loading edge from delivered Wasm.
Deliverable: Load the subset in the production highlighter, with the concrete result and checks in this task's acceptance.
Context: WSD-3.2 output contract; ../core/crates/editac-highlighting/{Cargo.toml,src/lib.rs}; ../core/scripts/build-highlight-worker.mjs; production highlighting probe and inventory tests.
Affected paths/symbols: Only the Context paths and the exact adopted/specified boundary; controller-split any material expansion before implementation.
Dependencies: WSD-3.2.
Independent work: Any ready task whose own inputs and authority are valid.
Session scope: 30–40 minutes including focused parity; one runtime/data edge.
Acceptance: Backend::new loads the generated closure; the normal target does not retain two_face::syntax::extra_newlines or its full data blob. Rust/TypeScript/JSON scopes, UTF-16 spans, multiline/newline behavior, source fallback and limits remain unchanged. Report full worker+Wasm+grammar union and the unresolved 98,304-byte allocation if exceeded.

Implementation:

- [ ] WSD-3.3-I1 Replace only the grammar construction edge and remove the unused normal dependency/features; preserve backend port, scheduler, source text and notices.
- [ ] WSD-3.3-I2 Bind generated identities to browser/packed inventories; do not rename the backend identity without updating its authoritative contract. Keep all required grammar assets in accounting.

Validation:

- [ ] WSD-3.3-V1 Use the production setup from scripts/probe-highlighting.sh to prepare an explicit EDITAC_HIGHLIGHT_EVIDENCE directory and matching production artifact; run tests/highlight-production-wasm-probe.test.mjs and affected inventory cases, reusing valid unchanged native parity inputs. Budget 6 minutes; do not launch the whole native/debug/release script. Check full-blob absence and actual combined gzip delta.

Evidence: This file's separate progress record, task `WSD-3.3`: exact changed files/input pins, commands/setup/selectors, counts, measured metrics, reuse decisions and unresolved requirements. Keep generated diagnostics in ignored task-owned output, never Git.
Handoff: Record the last completed substep, current symbol/interface, failing input or missing decision, next exact action and candidate time/hypotheses remaining. Preserve partial source; no blind stash/reset.
Blocked behavior: Leave this parent and failed/missing substeps unchecked. Record task + source/input revision + failure fingerprint, owner, attempted repair and exact resume condition. No unchanged rerun; continue only independent authorized work.
