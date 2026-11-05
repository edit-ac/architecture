# Deliver optional extensions over one core

Status: COMPLETE

Progress: `.roadmap-runner/wasm-extensions-20261027/02-optional-extensions.progress.md`.
Entry: source 01 WEX-1.1–1.4 receipts identify current attribution, frozen
interfaces/budgets and validated minimal Rust/browser graphs. Read selected
receipts from its separate progress file; an old or failed receipt is not entry.

Planning only until adoption by the one guarded root-main controller. One ready
parent per session; preserve dirty/index work, current format and native deferrals.
Reuse existing SDK-1.11–1.13/EXT-1.14–1.20 ports and implemented requirements; do not
create a second registry, document, history owner or per-preset kernel. Use the
same canonical browser kernel for every configuration. Kernel admission and
atomic commits remain authoritative; companions exchange bounded data/proposed
commands, never cross-module Rust pointers. Stored disabled/unknown feature data
must survive honest fallback and round trips without executing it. Schema
registration remains frozen before attachment; hot schema changes are not implied.
Baseline Task caps remain 524,288 total/32,768 JS gzip bytes; expanded ceiling and
inventory follow the WEX-1.2 contract and user-confirmed 2026-10-28 ceiling of
1,048,576 total gzip bytes (1 MiB). Required lazy/glue/CSS/assets count. No paid inference, secrets,
publication or deployment. Existing narrow deterministic checks only during
delivery; remaining test development and broad coverage belong to sources 03a/04.

Workers change only verified checkboxes/Status. Progress records input pins,
selected commands, exit/counts, reused receipts, exact interruption and next
action. Failures/skips stay unchecked with task/input/error fingerprint, owner,
attempted repair and concrete changed-input resume condition. No unchanged retry.
Stop owned temporary processes; remove only inactive session-generated outputs.

## Tasks

### Task WEX-2.1 — Complete configurable extension and preset composition

- [x] WEX-2.1 Expose typed, inspectable composition using the existing registry.

Purpose: Let apps select features as in Tiptap without low-level worker/codec assembly.
Deliverable: Residual public factory/configuration/preset wiring and deterministic capability admission.
Context: `architecture/specs/extension-dx.md` Composition, Core boundaries, One import and Loading sections; `core/packages/core/src/extensions/{registry,profiles}.ts`; `core/packages/web/src/extensions/{configuration,contract,resource}.ts`; WEX-1.2 owner map and EXT-1.14/SDK-1.11 receipts.
Dependencies: none.
Independent work: WEX-2.2–2.5 can use the already frozen interfaces.
Session scope: One public composition/preset seam, 30–45 minutes; reuse delivered factories.
Acceptance: Explicit extension list supports fresh immutable configuration and configurable convenience presets with inspectable expansion/disabled members. Dependencies, versions, capability and binding conflicts fail before document mutation with actionable errors. App labels/import order cannot grant capabilities. No Tiptap runtime/schema dependency, duplicate dispatcher or advertised unimplemented API.

Implementation:

- [x] WEX-2.1-I1 Close residual composition gaps over existing ports; keep lightweight imports inert and extension heavy implementations separate. Preserve supported existing callers; remove only obsolete unpublished aliases according to current-format policy, without broad API cleanup.

Validation:

- [x] WEX-2.1-V1 Run affected existing contract/configuration selectors and one preset expansion/disabled-member consumer. Inspect actual dispatcher-supported groups before use. Budget: 5 minutes; record nonzero counts and reuse unchanged proof.

Evidence: Public imports, preset expansion, conflict results and retained graph in progress.
Handoff: Unresolved public option/contract and precise consumer failure.
Blocked behavior: Record missing owner/interface; independent feature seams remain eligible.

Controller recovery, 2026-10-28: Code implementation and production admission are
owned by the preceding focused recovery sources. WEX-2.2 consumes their exact
RCH-1.1–1.5 and WCU-1.1 receipts plus existing EXT-1.14/WEX-2.1 contract proof.
Do not repeat already-passing generic loading checks without changed inputs.
Complete only the remaining Code-dependent integration/asset proof; the parent
and I1 remain unchecked until their original acceptance is satisfied.

### Task WEX-2.2 — Complete independent codec and presenter loading

- [x] WEX-2.2 Keep existing Markdown/highlighting/math implementations outside minimal loading.

Purpose: Turn existing optional modules into verifiably independent installations.
Deliverable: Residual package exports/asset manifest wiring for already implemented codec/presenter modules.
Context: `core/packages/markdown`, `core/crates/editac-markdown-wasm`, `core/packages/web/src/extensions/{markdown-resource,highlighting,code,assets}.ts`, code/math module loaders and package exports; existing SDK-1.12/EXT loading receipts.
Dependencies: none.
Independent work: WEX-2.1 and semantic/service seams are independent.
Session scope: One common package/asset seam across existing modules, 30–45 minutes; no new parser, grammar or renderer implementation. Split remaining unrelated package defects before exceeding scope.
Acceptance: Disabled modules contribute no implementation JS/Wasm/grammars/fonts/dictionaries or startup requests; enabled modules load through current managed readiness and preserve source on missing/failing assets. Shared immutable code loads once while state, options, cancellation and disposal remain per editor. Baseline safe clipboard remains available.

Implementation:

- [x] WEX-2.2-I1 Repair only current retained-import/asset leaks; use the existing standalone Markdown codec pattern and resource gateway. Pin companion/core compatibility before activation and reject incompatible artifacts without document writes.

Dependency-loading acceptance: use the existing resource/registry dependency DAG,
not another loader. Missing/cyclic/incompatible dependencies fail before mutation;
shared immutable in-flight work deduplicates, independent ready dependencies avoid
unnecessary serial waterfalls, and cancellation/failure/retry remain per editor.
WEX-2.2's existing focused loading checks cover the changed seam; comprehensive
first-use/readiness cases belong to WEX-5.2. Source review:
`architecture/research/small-editor-and-loading-methods-20261027.md`, Blazyload.

Validation:

- [x] WEX-2.2-V1 Select existing loading/Markdown/glue-sharing tests for changed owners and compare one disabled/enabled packed graph. Budget: 5 minutes; reuse matching unchanged module proof and explicitly name uncovered modules.

Evidence: Resource identities, absent/present graph comparison, readiness/fallback and sharing results.
Handoff: Exact missing module capability, asset or package boundary.
Blocked behavior: A module failure blocks only its own integration; record unavailable capability honestly and continue independent work.

### Task WEX-2.3 — Isolate comparison and nonbaseline export work

- [x] WEX-2.3 Move separable comparison/export implementation out of the required kernel graph.

Purpose: Reduce retained Wasm/export glue where work consumes immutable bounded content.
Deliverable: One companion package/interface for residual comparison or nonbaseline export work, selected by WEX-1.1 attribution.
Context: `core/crates/editac-bridge/src/comparison.rs`, `core/crates/editac-wasm/src/engine.rs`, `editac-diff`, `editac-html`; `core/packages/core/src/engine.ts`, `core/packages/web/src/review/history.ts`; WEX-1.2 boundary decision, extension-dx.md section Semantic comparison companion admission — 2026-10-28, and existing format/semantic-comparison tests.
Dependencies: none.
Independent work: other optional families do not depend on this extraction.
Session scope: One measured leaf boundary, 30–45 minutes. If comparison and export need distinct interfaces, extract the chosen first leaf and obtain a controller split for the remaining required leaf before closure.
Acceptance: Chosen heavy leaf is absent from the minimal emitted graph, with enabled output equivalent on existing fixtures. Preserve baseline HTML clipboard, generic transfer, validation and required serialization. Companion failures do not mutate the document; exported Engine allocations stay with their originating kernel. Do not add a replica or duplicate the admission algorithm to avoid an interface issue.

Implementation:

- [x] WEX-2.3-I1 Use existing admitted immutable transfer/snapshot inputs and bounded outputs; wire the managed companion through the frozen capability interface and remove only its proven unnecessary root exports/imports. Keep any inseparable invariant in kernel and record measured remaining cost.

Validation:

- [x] WEX-2.3-V1 Run affected existing comparison/export fixtures plus one minimal packed graph exclusion check. Budget: 6 minutes. Compare semantic output and original failure behavior, not just export signatures or compressed sizes.

Controller-adopted boundary, 2026-10-28: implement the normative managed-preload,
synchronous comparison contract in architecture/specs/extension-dx.md. The kernel
alone admits existing captures through prepare_semantic_comparison; the optional
stateless companion owns the existing diff algorithm over detached admitted data.
Preserve public synchronous comparison, explicit unavailable/readiness, exact
current limits/errors, per-editor attachment and baseline HTML clipboard/export.
This adopts proposal option (a); no further architecture decision is a prerequisite
for this chosen leaf. WEX-2.6 owns expanded-consumer preload/action wiring. A real
new invariant discovered during implementation still requires a precise handoff.

Evidence: Before/after retained owners and bytes, interface identity and exact fixture results.
Handoff: Remaining leaf, inseparable invariant or compatibility failure and the proposed bounded split.
Blocked behavior: Material ABI redesign requires a proposal before implementation; continue other independent families without marking this complete.

### Task WEX-2.4 — Separate advanced table tooling from shared document invariants

- [x] WEX-2.4 Make advanced table orchestration an explicit extension capability.

Purpose: Keep expensive tooling optional without weakening table data and atomic edits.
Deliverable: One advanced table planner/presenter seam over existing kernel primitives and capability admission.
Context: `architecture/specs/{extension-dx,extension-library,document-durability}.md`; current table command catalog and table rectangle implementation located through Codanna (or bounded fallback); WEX-1.2 semantic boundary map and STB regression receipts.
Dependencies: none.
Independent work: comparison, codecs and host services do not depend on table tooling.
Session scope: One table tooling seam, 30–45 minutes; no new table feature or redesign of shared ownership algebra.
Acceptance: Disabled advanced tools cannot invoke unavailable table commands; existing table data, children, shape validation, copy/export fallback, reopen and sync retain their guarantees. Optional preparation proposes bounded commands; kernel revalidates authority/targets and commits one atomic history group. If table invariants are inseparable, retain them in core and isolate only measured tooling, recording that size limit honestly.

Implementation:

- [x] WEX-2.4-I1 Gate the existing advanced planner/presenter through admitted capabilities and ports; preserve generic primitive validation, required baseline commands and original crash/atomicity assertions. Do not move Rust-owned committed semantics into a JS document model.

Validation:

- [x] WEX-2.4-V1 Run existing absent-module catalog and one affected successful/failed-atomic table case, then inspect the changed graph. Budget: 6 minutes; choose exact current selectors and keep original failure assertions.

Evidence: Availability, preserved content/atomicity, focused counts and actual retained cost.
Handoff: Exact invariant/tooling boundary and failing selector; additional table work requires a bounded controller split.
Blocked behavior: Keep the parent unchecked if required exclusion or semantics cannot be achieved; independent families remain eligible.

### Task WEX-2.5 — Isolate optional host service orchestration

- [x] WEX-2.5 Make retained asset/resolver/assistance orchestration capability-selected.

Purpose: Avoid loading optional host workflows in plain local editors.
Deliverable: One residual common service-adapter seam using existing assets, resolver or assistance ports, selected by current retained-byte evidence.
Context: `core/packages/web/src/extensions/` host capability/resource owners; session assets/revision support; `architecture/specs/{extension-dx,ai-extensions,extension-library}.md`; WEX-1.1 map and current service receipts.
Dependencies: none.
Independent work: other extension families remain independent.
Session scope: One shared adapter seam, 30–45 minutes; no new AI/provider integration, upload, resolver or paid call. Controller splits unrelated remaining seams before closure.
Acceptance: Unconfigured services perform no host/provider work and contribute no heavy implementation assets. Enabled services retain permission checks, cancellation, stable anchors, bounds and per-editor teardown; late work cannot commit after detach/disposal. Generic asset data/recovery validation remains kernel-owned. Missing services preserve original content and actionable failure states.

Implementation:

- [x] WEX-2.5-I1 Close the measured retained-orchestration leak through existing capabilities/resources; reuse existing asset/AI/service interfaces and prepared transports. Keep dependencies/data fallback available without activating a service.

Validation:

- [x] WEX-2.5-V1 Select existing disabled-service and stale/cancelled-result cases with deterministic fixtures plus the affected graph check. Budget: 5 minutes; inspect the paid-inference policy before changing/running AI-named tests. No credential environment or provider recording.

Evidence: Selected service identity, absent/present implementation and request/work counts, cancellation results.
Handoff: Exact service seam and remaining required scoped work.
Blocked behavior: Missing host capability records a blocker for that seam; do not substitute live services or reinterpret missing proof.

### Task WEX-2.6 — Deliver core and expanded app consumers

- [x] WEX-2.6 Connect the chosen core/expanded inventories to public presets and examples.

Purpose: Make optionality usable and establish a stable architecture for compression.
Deliverable: Inspectable core/starter-style convenience configuration and expanded reference app, package exports and canonical example updates.
Context: WEX-2.1–2.5 receipts; WEX-1.2 inventories; existing `core/examples` composition consumers, `core/packages/{core,web}` public exports, SDK/EXT documentation owners.
Dependencies: WEX-2.1, WEX-2.2, WEX-2.3, WEX-2.4, WEX-2.5.
Independent work: documentation inventory may be prepared earlier; ready closure requires all family interfaces.
Session scope: One public consumer/example integration, 30–45 minutes; no public publishing.
Acceptance: A clean installed consumer can configure a useful core, individual extensions and the named expanded app through public imports. Presets disclose members and per-extension/combined cost; disabling members removes optional implementation assets. Documentation labels any remaining unqualified claim. All source 01/02 physical interfaces are complete and stable enough for compression; performance budget failures remain explicit.

Implementation:

- [x] WEX-2.6-I1 Update existing canonical examples and package export wiring to the completed interfaces, with one configuration per reference inventory; record remaining docs changes for final reconciliation. Reuse existing DOC recipes rather than duplicating tutorials.

Validation:

- [x] WEX-2.6-V1 Build/typecheck one affected clean packed consumer with core and expanded configurations; capture source-bound inventories and current budget failures as measurements. Budget: 8 minutes. Do not run broad combination suites yet or call failing budgets a readiness pass.

Evidence: Public imports, inventories, package identities, bounded checks and architecture handoff for source 03.
Handoff: Remaining family requirement/consumer failure, exact source pins and next action.
Blocked behavior: Failed family acceptance prevents compression entry; preserve unfinished work and request a bounded controller split when the seam exceeds this source.

### Task WEX-2.7 — Bound the fixed cost of small-editor work

- [x] WEX-2.7 Audit and address a measured small-editor hot-path cost.

Purpose: Make small fields competitive without dropping Rust-owned correctness or durability.
Deliverable: Attributed per-input work and one justified bounded repair, or an honest no-change/deferred disposition when evidence or allowance does not justify a change.
Context: WEX-2.6 physical architecture/public consumer receipts; WEX-1.2 frozen objectives/shared optimization ledger; `architecture/specs/verification.md` Extension dispatch and JS/Wasm performance; current core engine/direct ports, web input/text, DOM patch/selection and host subscriptions located through Codanna or bounded fallback; `architecture/research/small-editor-and-loading-methods-20261027.md` Why small editors need a separate performance track.
Dependencies: WEX-2.6.
Independent work: none before complete physical boundaries. Later final comparison collects broad evidence; it is not a delivery prerequisite.
Session scope: One fixed-cost attribution/repair seam, 30–45 minutes. Actual candidate changes/comparisons consume the same global 45-minute/two-hypothesis ledger as source 03; this task does not add a batch.
Acceptance: Attribute active input to committed visible patch without whole-document scans, snapshots/serialization or unrelated-extension dispatch unless required by a measured invariant. Inspect JS/Wasm call count, payload bytes, local validation, DOM changes and toolbar/subscriber work. Keep synchronous input/selection/undo correctness and one history owner. Use existing direct ports, region patches and selective subscriptions; no second writable JS model, per-character boundary loop, unsafe validation shortcut or batching across an input/composition correctness boundary. Retain any inseparable cost honestly. Core readiness is distinct from shell paint, and moving work into the first keystroke is not a speedup. Do not claim competitive results before WEX-5 measurements.

Implementation:

- [x] WEX-2.7-I1 Reuse current focused work counters/profile evidence; choose only a demonstrated fixed-cost owner. Repair one bounded seam within remaining shared allowance, preserving existing fixture semantics and public APIs. If no candidate is justified, record why and the exact final comparison owner rather than refactor speculatively. Pin updated consumer artifacts for source 03 if source changed.

Validation:

- [x] WEX-2.7-V1 Run existing affected direct/facade, text-route and input/selection/undo checks plus the smallest applicable work-count comparison, with prepared transports. Budget: 5 minutes within remaining candidate allowance where comparison is experimental. Existing 0/1/10/100 unrelated-extension controls must remain honest; do not write a second benchmark harness or call microbenchmarks user-visible latency proof.

Evidence: Shared elapsed/hypothesis ledger, source/build pins, call/payload/work counters, exact nonzero correctness checks, candidate decision and retained cost.
Handoff: Actual remaining allowance, unresolved measured owner and exact first comparison cell for WEX-5; retain failures and unfinished source.
Blocked behavior: Expired allowance or unchanged failed candidate stops tuning, not honest final measurement. A required semantic defect remains a blocker with owner/fingerprint and changed-input repair; no weaker behavior or new batch is substituted.

<!-- roadmap-runner:delivery:start -->
WEX-2.7 closed after the ENG-1.14 admission repair: refreshed17/17 input/selection/undo/work checks, compatible21/21 boundary and2/2 native proof. No-change cost disposition and exhausted tuning allowance retained. Original failures preserved; WEX-5 readiness/latency and hard-cap obligations remain. Evidence: `.roadmap-runner/wasm-extensions-20261027/02-optional-extensions.progress.md`.
<!-- roadmap-runner:delivery:end -->
