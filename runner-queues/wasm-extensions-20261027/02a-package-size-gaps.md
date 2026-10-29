# Close the measured extension package size gaps

Status: IN_PROGRESS

User authority: add the investigated package-size gaps to the upcoming roadmaps,
2026-10-28. This source schedules implementation; it does not restart the stopped
runner, resolve WEX-2.7, grant another optimization batch or relax a hard cap.
Progress: `.roadmap-runner/wasm-extensions-20261027/02a-package-size-gaps.progress.md`.
Entry: source 02's required functionality and focused checks accepted, with the
WEX-2.6 packed-consumer inventory and WEX-2.7 allowance disposition authenticated.

The WEX-2.6 reference is 3,016,740 total / 229,109 JS gzip bytes; its limits remain
1,048,576 / 131,072. Its three Wasm resources are highlighting 1,435,671, kernel
759,022 and Markdown 590,184 gzip bytes. Core without extensions is 846,301 total
/ 84,525 JS against 524,288 / 32,768. These are recorded failures, not savings
targets silently assigned to individual components. Removing all highlighting
Wasm would still leave 1,581,069 total gzip bytes. Do not promise one fix closes
the aggregate gap or sum overlapping component estimates.

Reuse `core/docs/extensions/configuration-v1.md`, the WEX-2.6 measurements under
the source 02 progress evidence directory, and `architecture/decisions/highlighting-backend.md`.
Verify current artifact/source identities before using those observations. The
2026-10-28 read-only investigation matched all three current Wasm hashes to the
receipt; it ran no build, test or optimization experiment.

## Execution and acceptance constraints

Keep one canonical kernel and document format, all supported languages/math and
editor behavior, immutable source, UTF-16 offsets, history, recovery, permissions
and unknown-data preservation. No runtime per preset or second writable replica.
Material API/wire/ABI changes require a concrete proposal and explicit adoption
before implementation. A roadmap checkbox is not adoption of that proposal.

Resolve the WEX ledger's `not_started` state versus the exhausted-allowance
handoff before any size candidate. Record the authoritative disposition with its
source, elapsed time and hypotheses; do not assume the favorable record or reset
the ledger. All size-motivated comparative builds, grammar/backend/renderer
variants and measured source candidates share the existing 45-minute/two-hypothesis
allowance with WEX-2.7 and source 03. Per-parent session scopes below are not extra
experiment allocations. When allowance is unavailable, retain the unfinished
implementation and exact changed-input/authority requirement; do not disguise
experimental tuning as unbudgeted functional work or tick it as implemented.
Document review and contract design may proceed independently of candidate work.

Count every distinct required lazy JS, worker, glue, Wasm, CSS and asset resource
once using canonical gzip level 9. Report raw and Brotli separately. Runtime
filtering, delayed fetching, Brotli/Zopfli substitution, reduced language support
or a renamed workload cannot satisfy the unchanged gzip gates. No paid inference,
credentials, native/OS qualification, publication, deployment or new runner.

Use existing narrow fixtures during delivery; all additional broad test authoring
and coverage gaps belong to WEX-4.1/4.2, with timing/resource observations owned
by WEX-5.2/5.3. Keep generated output ignored and task-owned. Record exact selected
cases, nonzero pass/fail/skip counts, source/artifact pins and failures in progress;
preserve unrelated working/index bytes and clean task-owned servers/output.

## Tasks

### Task WEX-6.1 — Align the highlighting production build

- [x] WEX-6.1 Deliver the highlighting artifact through the existing browser production pipeline.

Purpose: Close a concrete build-path inconsistency before interpreting further highlighting savings.
Deliverable: One reproducible highlighting build using the admitted browser profile and staged optimizer/feature validation, with its package consumers wired to that artifact.
Context: `core/scripts/{build-highlight-worker,build-wasm,optimize-wasm}.mjs`; `core/scripts/probe-highlighting.sh`; `core/Cargo.toml`; `core/crates/editac-highlighting`; `core/tests/highlight-production-wasm-probe.test.mjs`; current RCH/WCU receipts. The current builder uses ordinary release and skips the shared optimizer; the inspected Wasm retains a 291,880-byte raw name section, not that many proven gzip savings.
Dependencies: none.
Independent work: WEX-6.3 can design the Markdown boundary while candidate allowance is unresolved.
Session scope: One build/consumer boundary, 20–30 minutes, with comparative work inside the shared remaining allowance.
Acceptance: Use the existing size-focused browser settings and pinned safe optimizer where compatible; preserve native release policy, imports/exports, permitted Wasm features and production behavior. Stage output before replacement and honor the existing no-growth/identity guards. Remove diagnostic names from shipping output without losing separate diagnostic capability. Measure actual aggregate and JS/resource changes; retain rejected candidates and any startup or semantic regression. A smaller binary alone is not acceptance.

Implementation:

- [x] WEX-6.1-I1 Reconcile allowance, pin the current production artifact, and route the highlight build and production probe to the shared profile/staging/optimizer contract. Preserve target-directory handling and qualification-versus-production bindings; do not introduce a second optimizer.

Validation:

- [x] WEX-6.1-V1 Run the existing production highlighting probe and affected package/artifact identity selector, then inspect final sections and complete gzip resource union. Budget: 5 minutes inside remaining candidate allowance when comparing settings; reuse unchanged native/worker cases. Record executed/passed/failed/skipped counts and actual gzip delta, never raw name bytes as gzip savings.

Evidence: Exact profile/flags/toolchain, artifact hashes, size/section observations, selected cases and retained/rejected disposition.
Handoff: Remaining build/probe step, allowance and changed-input blocker; no implicit pipeline fallback or unchanged retry.
Blocked behavior: Missing allowance or a failed semantic/feature assertion stops this candidate; preserve the current artifact and record the exact changed-input or authority condition before retry.

### Task WEX-6.2 — Ship only the admitted highlighting grammar closure

- [ ] WEX-6.2 Replace the complete embedded grammar bundle with a validated build-time subset.

Purpose: Remove unused grammar data while retaining Rust, TypeScript and JSON behavior.
Deliverable: Reproducible source-controlled subset recipe and identity/license inputs, with generated grammar assets excluded from Git and loaded by the existing backend.
Context: `core/crates/editac-highlighting/src/lib.rs` Backend::new; `examples/grammar_inventory.rs`; `core/fixtures/highlighting/backend.json`; `core/licenses/highlighting`; `architecture/decisions/highlighting-backend.md`; pinned two-face 0.5.2+bat-0.26.1 and Syntect 5.3.0 builder/linking documentation. The full embedded blob is 959,011 raw / 869,430 gzip bytes; that is an attribution lead, not all removable bytes.
Dependencies: WEX-6.1.
Independent work: Dependency/license analysis can proceed before a candidate build; no backend replacement is implied.
Session scope: One grammar build/load seam, 30–45 minutes; candidate comparisons consume the remaining shared allowance.
Acceptance: Retain the transitive context/reference closure needed by all three supported languages, newline behavior, source-preserving fallback, scope/UTF-16 parity and all retained notices. Generate from authenticated pinned inputs; include plain-text fallback as needed. The shipped binary must omit the complete unused bundle, not load then filter it. Record actual grammar and full Wasm/worker/aggregate gzip costs. If the closure is still too large, propose a browser-specific backend as separate follow-up with parity/portability costs; do not silently switch implementations or reduce support.

Implementation:

- [ ] WEX-6.2-I1 Build and link the minimal required grammar closure, replace the production full-bundle loading edge, and update admitted subset identities and notices. Keep the same highlighting port, scheduler and failure behavior; do not rely on runtime filtering or guessed grammar independence.

Validation:

- [ ] WEX-6.2-V1 Reuse existing three-language native/Wasm parity, source/fallback and inventory selectors; select only affected cases plus a minimal cross-grammar regression if the current corpus misses a retained reference. Budget: 6 minutes within the shared allowance for comparative execution. Verify the full bundle is absent and generated output is reproducible; defer comprehensive syntax corpus expansion to WEX-4.1.

Evidence: Retained grammar/dependency/license closure, recipe/input pins, selected parity counts and nonoverlapping measured costs.
Handoff: Exact unresolved grammar reference or parity failure; preserve the original full-bundle failure and pending broader coverage.
Blocked behavior: An unresolved grammar dependency, changed language behavior or exhausted allowance leaves the task unchecked; do not ship a smaller incomplete grammar set.

### Task WEX-6.3 — Propose a data-only Markdown source boundary

- [ ] WEX-6.3 Define and obtain adoption of a concrete Markdown table-source boundary proposal.

Purpose: Determine how to remove document-restoration machinery from the optional codec without duplicating semantic authority.
Deliverable: A bounded proposal in `architecture/specs/extension-dx.md` with matching acceptance, retained-dependency evidence and an explicit adopted or pending decision.
Context: `core/crates/editac-markdown-wasm/src/lib.rs` SnapshotInput::restore and table_source_value; `core/crates/editac-markdown/src/{reconcile,table_format}.rs`; `core/crates/editac-core/src/interchange.rs`; current table-source bridge and Markdown public package. Inspect actual symbols before changing the proposal.
Dependencies: none.
Independent work: This source/contract review does not require running a tuning candidate or another backend.
Session scope: One contract proposal, 15–30 minutes, read-only attribution until adoption.
Acceptance: Describe current versus proposed payloads, immutable opening/current projections, stale-source and identity checks, kernel validation/commit ownership, bounded inputs, source recovery and error behavior. Attribute which restore/Yrs/validation paths the codec actually retains; a Cargo dependency alone is not proof. Prefer an inert data boundary with restoration and commit in the existing kernel. Quantify possible duplication and check whether moving work increases core cost. Do not change a public/wire/ABI contract or claim gzip savings before the proposal is explicitly adopted. Pending adoption leaves this implementation gate unchecked with the exact decision needed.

Implementation:

- [ ] WEX-6.3-I1 Trace retained table-source entry points, write the smallest concrete boundary proposal and update the affected task acceptance together after explicit adoption. Preserve one current format and every original stale-plan, recovery and atomicity assertion.

Validation:

- [ ] WEX-6.3-V1 Review the proposal against the named call sites and existing table-source assertions, listing exact preserved checks, removed roots and missing proof. Budget: 3 minutes; no build or new broad suite. Record the adoption reference; absence is not approval.

Evidence: Retained-root map, old/new contract, semantic obligations, adoption state and exact implementation owner WEX-6.4.
Handoff: The concrete unresolved design/adoption question; independent highlighting/JS work remains available.
Blocked behavior: Missing explicit adoption blocks WEX-6.4 only; keep the proposal reviewable, preserve current behavior and continue other eligible source tasks without repeated requests.

### Task WEX-6.4 — Remove codec-owned document restoration

- [ ] WEX-6.4 Implement the adopted Markdown boundary and remove its redundant retained machinery.

Purpose: Make the optional Markdown artifact pay for codec work without restoring documents for table-source operations.
Deliverable: Kernel/codec/public-adapter implementation of the adopted data contract, with old production entry paths removed where superseded.
Context: WEX-6.3 adopted proposal and retained roots; current Markdown Wasm, source reconciliation, table-source bridge and public web adapters; existing Markdown/table-source fixtures.
Dependencies: WEX-6.3.
Independent work: none across the adoption gate; no speculative API rewrite.
Session scope: One coherent codec/kernel boundary, 30–45 minutes including narrow checks; controller-split a larger implementation before starting it.
Acceptance: Preserve current Markdown fidelity, table recovery, stale/foreign target rejection, input bounds, deterministic errors, one history owner and atomic commit. The codec accepts inert bounded data, not another live document authority. Verify the removed restoration roots are absent from its emitted artifact and report both core and codec changes plus the complete expanded union. Merely moving bytes between artifacts, duplicating validation or removing required behavior is not a size win. Follow the adopted proposal if it establishes a safer equivalent boundary; do not redesign it in the worker.

Implementation:

- [ ] WEX-6.4-I1 Wire the adopted projections and authoritative validation through existing ports, remove superseded restoration/serialization roots from the codec, and update the canonical public consumer without aliases for unpublished old contracts.

Validation:

- [ ] WEX-6.4-V1 Select existing Markdown roundtrip and successful/stale/failed-atomic table-source cases for the changed boundary, plus the packed import/load check and emitted dependency inspection. Budget: 6 minutes, with size experiments charged to the shared allowance. Add only a minimal regression for an uncovered concrete defect; WEX-4.1 owns remaining preservation coverage.

Evidence: Adopted input/implementation pins, removed roots, core-plus-codec resource accounting and focused semantic counts.
Handoff: Exact incomplete interface or failed invariant, original bytes/fixtures preserved and no unchanged retry.
Blocked behavior: Failed stale-plan/recovery/atomicity behavior or an unadopted contract stops implementation admission; retain the original failure and a concrete owner/repair before resumption.

### Task WEX-6.5 — Reduce retained browser and MathML code

- [ ] WEX-6.5 Deliver a measured capability-preserving reduction in required browser JavaScript.

Purpose: Address the separate core and expanded JS caps rather than treating Wasm savings as sufficient.
Deliverable: A bounded improvement to the retained browser/MathML graph, with explicit residual JS gaps and source-bound public-consumer measurements.
Context: `core/packages/web/src/modules/math-renderer.ts`; `core/scripts/build-math-assets.mjs`; the WEX-2.6 esbuild metafiles and minified resource inventory; core/web engine, configuration and extension conversion adapters. Full KaTeX supplies MathML output in a 76,861-byte gzip chunk; fonts/CSS URLs are already absent. Core and expanded JS gaps are 51,757 and 98,037 bytes in that receipt.
Dependencies: none.
Independent work: Read-only retained-import analysis is independent of Markdown adoption and highlighting builds.
Session scope: One measured retained family, 20–40 minutes; do not combine unrelated speculative rewrites or renew the experiment allowance.
Acceptance: Distinguish required input/selection/clipboard/recovery code from removable adapters and renderer paths. Evaluate a supported smaller MathML build only with identical admitted math, trust, expansion/output bounds and accessibility; do not infer tree-shaking from the output option. Consider duplicated serializers/wrappers and optional family entry points only where the graph proves retention. Preserve keyboard/IME, selection, history and public imports. Report total JS and aggregate canonical gzip for unchanged core/expanded inventories. If no safe improvement fits the allowance, retain the failed caps and a precise deferred candidate; do not mark implementation complete on a measurement-only disposition.

Implementation:

- [ ] WEX-6.5-I1 Use the existing metafile attribution to select and implement one justified renderer or browser dependency change. Keep required presentation/security behavior and existing extension ownership; propose a material renderer contract change before adopting it.

Validation:

- [ ] WEX-6.5-V1 Run the affected existing math-bundle/math-safety selectors or the changed browser owner's focused input/selection/undo selectors, then rebuild the exact packed core/expanded consumer. Budget: 5 minutes within remaining candidate allowance for comparisons. Attribute emitted changes without treating raw metafile contributions as gzip savings; broader cases remain with WEX-4.1/4.2.

Evidence: Selected retained owner, candidate/allowance record, current resource union, actual JS/total gaps and semantic results.
Handoff: Remaining candidate, exact failing cap, reviewable source delta and changed-input resume condition.
Blocked behavior: No safe candidate or insufficient allowance leaves implementation unchecked with an explicit deferred owner; no removal of required math/input behavior or favorable workload relabeling.
