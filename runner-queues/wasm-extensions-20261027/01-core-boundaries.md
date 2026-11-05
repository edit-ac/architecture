# Establish the small core boundary

Status: COMPLETE

Leptos research input: `architecture/research/wasm-code-size-methods-20261027.md`,
Leptos binary-size guide addendum. WEX-1.1 additionally attributes retained regex/
Unicode tables and serializer families, without assuming those dependencies are
present or repeating upstream size estimates. WEX-1.2 compares standalone optional
companions with a function-split build graph at compatible async leaf boundaries:
actual toolchain, memory/table/import ownership, glue/loader bytes, readiness and
failure behavior. Keep one semantic owner/canonical kernel and synchronous input/
composition/selection/atomic commit. Default to existing ports unless evidence
supports a concrete alternate design; propose any material ABI/runtime change
before implementation and update authoritative spec/acceptance together. This
assessment adds no framework dependency, split implementation or candidate run.

Progress: `.roadmap-runner/wasm-extensions-20261027/01-core-boundaries.progress.md`
from the workspace root. Entry: all 17 RAQ parents in
`architecture/runner-queues/rust-architecture-quality-20261026/` are implemented
and validated, including current RAQ-4.1–4.4 receipts; consume their four separate
progress files by selected receipt. Missing/currently invalid proof blocks entry.

Planning only until safe controller adoption. One serial root-main worker, one
ready parent per session. Preserve unrelated dirty/index bytes, current format,
original assertions, existing Task 524,288-total/32,768-JS gzip caps and native
deferrals. User-confirmed expanded reference-app cap, 2026-10-28: 1,048,576 total
gzip bytes (1 MiB). WEX-1.2 freezes its capability inventory before gate changes. Count
required lazy code, glue, CSS/assets and site unions. No paid inference, secrets,
publication or deployment. Use existing deterministic checks and ignored bounded
outputs. Permanent test development and broad coverage belong to sources 03a/04.
Workers edit only verified checkboxes and Status; record source/input pins,
commands, exit/counts, retained failures and next action in progress. Failed or
skipped checks leave the parent unchecked. Stop unchanged retry loops; record
task/input/error fingerprint, owner, attempted repair and exact resume condition.
Stop owned temporary processes and clean only inactive session outputs.

## Tasks

### Task WEX-1.1 — Attribute the post-RAQ production graph

- [x] WEX-1.1 Produce a current core/extension attribution decision.

Purpose: Choose physical boundaries using current artifacts rather than old sizes.
Deliverable: Compact contribution and ownership map in progress; authored decisions in the existing extension DX record.
Context: `core/scripts/{prepare-browser-size,browser-size-contract,build-wasm,optimize-wasm}.mjs`; core/session/Wasm Cargo manifests; `architecture/specs/extension-dx.md` sections Core and extension boundaries and Size reduction and compression; RAQ dependency receipts.
Research input: `architecture/research/wasm-code-size-methods-20261027.md`, Existing local controls, Methods and applicability, and Tool reliability and diagnostics; read only those sections for attribution.
Dependencies: none. Independent work: none before attribution; this is a true boundary prerequisite.
Session scope: One unchanged post-RAQ inventory, 30–45 minutes; no optimizer candidates.
Acceptance: Current raw/gzip/Brotli resource contributions distinguish JS, glue, Wasm, CSS/assets, initial/deferred and shared code. Compile edges are distinguished from retained bytes. Attribute Wasm code/data/custom-section cost and rooted exports, without summing overlapping retained subgraphs or equating raw contribution with compressed savings. Identify formatting/serialization, generic-instantiation, allocator and glue candidates only where current evidence implicates them. Baseline capability inventory, existing optionality and rejected prior experiments are identified. Old 852810/95661-byte observations remain historical, not current measurements.

Implementation:

- [x] WEX-1.1-I1 Reuse the current packed-consumer producer and source-bound receipts; inspect retained exports/imports and map the largest actual owners. Use an already available compatible Twiggy only as an optional diagnostic, since its upstream is archived; otherwise use maintained wasm-tools section/export inspection and targeted IR where needed, recording attribution gaps. Keep symbol-rich/IR diagnostics bounded and separate from production-size evidence. Do not create another size harness, install a profiler as a permanent dependency or rebuild valid unchanged artifacts without cause.

Validation:

- [x] WEX-1.1-V1 Run the existing producer for one current baseline (inspect its actual arguments first), or verify matching retained input pins; reconcile totals and required-resource inventory. Budget: 10 minutes within session. Record actual overrun/failure; the deliverable is accurate attribution, not a fabricated passing budget.

Evidence: Progress stores inventory path, exact source/build/settings, byte totals and selected owners; generated inventories stay ignored.
Handoff: Missing artifact/build input, unresolved retained owner and exact next inspection.
Blocked behavior: Missing RAQ proof or broken producer records a blocker; repair the owning prerequisite before further WEX work.

### Task WEX-1.2 — Freeze boundaries, public contracts and configuration budgets

- [x] WEX-1.2 Define one core and explicit extension-enabled app contracts.

Purpose: Preserve guarantees while adopting Tiptap-style organization and a bounded expanded app.
Deliverable: Updated existing `extension-dx.md`, `extension-library.md`, `web.md` and verification budget sections; targeted existing roadmap acceptance amendments where needed.
Context: WEX-1.1 map; `architecture/specs/{document-durability,extension-dx,extension-library,web,verification}.md`; SDK-1.11–1.13, EXT-1.14–1.20, FIT-1.10/1.11 acceptance; this folder's README Target product and accounting.
Dependencies: WEX-1.1. Independent work: none before shared contracts are frozen.
Session scope: One contract/ownership amendment, 30–45 minutes; no implementation.
Acceptance: Kernel versus optional content/behavior/presenter boundaries, readiness, capabilities, deterministic conflicts and cleanup are explicit. Apply the user-confirmed 2026-10-28 expanded-app ceiling of 1 MiB (1,048,576 bytes) total canonical gzip across JS/glue/Wasm/CSS/required assets, including required lazy code. Retain baseline 512 KiB total/32 KiB JS and promised Task inventory; name the expanded reference configuration and its total ceiling, JS allocation and extension contributions. No default-task relabeling, schema-per-preset, runtime per preset, silent ABI redesign or duplicate ownership. Map already passing requirements and residual work to existing canonical owners and WEX tasks.

Implementation:

- [x] WEX-1.2-I1 Reconcile existing implementation/receipts and freeze the minimal semantic/adapter inventory plus named expanded inventory. Define stable data/command companion interfaces and explicit unsupported behavior before code changes; amend authoritative spec and owning acceptance together. Propose any materially different design before implementing it.

Validation:

- [x] WEX-1.2-V1 Review inventory and arithmetic against the current producer and user budget decision; verify every residual claim has one delivery and final-check owner with no dependency cycle. Budget: 5 minutes; no product suite for prose.

Evidence: Progress maps decisions, exact budget units/configurations, source sections, canonical owners, reused receipts and remaining blockers.

Small-editor contract amendment: freeze empty, 128-byte/one-paragraph and 1-KiB/
four-paragraph configurations, core/rich-text/durable capability classes, actual
edit-readiness and first-use endpoints, current absolute latency/resource targets,
relative Tiptap objectives and uncertainty/noise policy before WEX-2.7 candidates
or WEX-5 comparison runs. Match competent vanilla Tiptap/basic and StarterKit
profiles; keep React integration and persistence differences explicit. Reuse the
existing comparator and REL-1.2–1.4 owners. Establish one shared 45-minute/two-
hypothesis optimization ledger covering WEX-2.7 plus source 03, without a reset at
the source boundary. Read only the small-editor/protocol sections of
`architecture/research/small-editor-and-loading-methods-20261027.md` for this decision.
Handoff: Exact unresolved interface or capability-inventory decision, affected consumers and owner; budget units are already confirmed.
Blocked behavior: Missing capability-inventory or contract proof blocks gate implementation, not independent boundary design. The expanded ceiling and core limits are already user-confirmed; preserve existing runtime gates until the planned implementation is ready.

### Task WEX-1.3 — Enforce the minimal Rust/Wasm compile boundary

- [x] WEX-1.3 Make the canonical browser kernel exclude optional host services.

Purpose: Keep unused source/native/service implementations out of the browser graph.
Deliverable: Additive Cargo feature/dependency wiring and canonical browser build selection over RAQ's existing extracted boundaries.
Context: `core/Cargo.toml`; `core/crates/{editac-core,editac-session,editac-wasm}/Cargo.toml`; `core/scripts/build-wasm.mjs`; WEX-1.2 interface map and RAQ-1.2/1.3 receipts.
Dependencies: WEX-1.2. Independent work: WEX-1.4 may proceed after the same contract.
Session scope: One browser versus host-service compile seam, 30–45 minutes; no binary per preset or dependency upgrade.
Acceptance: Minimal browser imports only required kernel/assets/revision contracts; service consumers explicitly opt in without feature-unification hiding absent dependencies. Already delivered RAQ work is reused, not reimplemented. Shared validation/commit/history stay in one kernel and required document data stays admissible. Build-time gating is not represented as hot-loadable code.

Implementation:

- [x] WEX-1.3-I1 Complete only residual manifest/module/build wiring from the frozen map; preserve explicit native/CLI/source-service callers and the one canonical browser artifact. Retain current browser toolchain and one format.

Validation:

- [x] WEX-1.3-V1 Run locked offline Cargo tree/check for the minimal Wasm target and one affected opted-in service consumer in separate feature graphs; run the existing focused Wasm load check if glue changed. Budget: 8 minutes; no workspace all-features substitute. Record emitted bytes when rebuilt without claiming the final budget gate.

Evidence: Selected Cargo graphs, build settings, affected callers, nonzero checks and byte delta in progress.
Handoff: Failing feature edge, consumer, command and prerequisite repair.
Blocked behavior: Record the owning missing dependency; WEX-1.4 remains independent when its inputs are unchanged.

### Task WEX-1.4 — Remove optional orchestration from the browser core graph

- [x] WEX-1.4 Isolate retained optional browser orchestration behind existing ports.

Purpose: Make disabling extensions reduce actual JS as well as network work.
Deliverable: Minimal facade/import boundary and host-selected optional orchestration using existing lifecycle/configuration ports.
Context: `core/packages/web/src/{editor,entry,surface}.ts`, `extensions/{configuration,assets}.ts`, sync attachment and `core/packages/{core,web}/package.json`; WEX-1.1 retained graph and WEX-1.2 core inventory.
Dependencies: WEX-1.2. Independent work: WEX-1.3 does not block this JS boundary.
Session scope: One retained orchestration seam (collaboration transport/presence first), 30–45 minutes; report any further seam for a controller split.
Acceptance: The local editor preserves persistence, recovery, input, selection and undo while disabled collaboration contributes no provider/subscription/timer/network activity or heavy retained implementation. Shared update primitives remain baseline. Existing explicit attachment contracts keep working; a new import cannot create an editor or enable siblings. Preserve baseline clipboard and formatting obligations.

Implementation:

- [x] WEX-1.4-I1 Move only measured optional orchestration through the existing attachment/resource gateway; keep per-instance permissions, cancellation and disposal. Avoid a second event bus, document, registry or loader.

Validation:

- [x] WEX-1.4-V1 Select affected existing configuration/loading cases and inspect one disabled versus enabled packed import graph; prove absent retained code as well as absent requests. Budget: 5 minutes. Freeze exact current selectors in progress and fail on zero matching cases.

Evidence: Graph difference, selected lifecycle counts and unchanged baseline obligations.
Handoff: Remaining retained owner or lifecycle failure and exact next bounded seam.
Blocked behavior: Record the concrete contract/owner gap; WEX-1.3 remains eligible.
