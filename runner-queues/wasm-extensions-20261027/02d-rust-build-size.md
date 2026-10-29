# Reduce Rust build and post-link size

Status: IN_PROGRESS

User authority: add the compiler-size research to a new roadmap and queue it in
the runner, 2026-10-28. Progress:
`.roadmap-runner/wasm-extensions-20261027/02d-rust-build-size.progress.md`.
Entry: accepted original source02 correctness and current canonical artifacts;
consume source02a's exact accepted/deferred dispositions without claiming its
unfinished reductions complete. The user skipped WEX-7.1 and its dependent
WEX-8.1; neither is an entry gate. WEX-9.1/9.2 read-only artifact/option audits
can proceed on the retained canonical artifact. WEX-3.1/3.2 keep their own
actual inventory/protocol prerequisites and existing zero tuning authorization.
The original WEX-2.7 malformed-request failure and its validated repair remain
preserved; no unchanged defect retry or new optimization allocation is granted.

This controller split moves **unstarted WEX-3.1 and WEX-3.2** here without changing
their IDs or existing implementation/validation obligations. Their old source
03/progress pair remains in place for WEX-3.3 HTTP delivery. Neither progress file
existed at this split. WEX-9.1 and WEX-9.2 add the compiler/linker audit and advanced
method disposition. Do not repeat earlier grammar, Markdown, browser/MathML or
generic-body implementation: WEX-6 and WEX-8 remain those owners. No checkmark is
transferred or newly granted by this split.

Read the [compiler survey](../../research/wasm-code-size-methods-20261027.md#compiler-linker-and-retained-code-survey--2026-10-28)
and its versioned primary sources, selected WEX-6 accepted/deferred dispositions and original source02 receipts, and only the
current task's named source/spec sections. Reuse the completed research; repeat
documentation lookup only for a changed version or unresolved option. The survey
observed Rust 1.97.1 / LLVM 22.1.6, wasm-bindgen 0.2.129 and Binaryen 132, not a
production optimization result. Recheck actual versions before selecting flags.

## Shared controls and ownership

Canonical gzip remains level 9. Core/Task caps remain 524,288 total / 32,768 JS;
expanded-document-v1 remains 1,048,576 total / 131,072 JS, including distinct
required lazy code, worker, glue, Wasm, CSS and assets. Keep initial, deferred and
whole-site union observations separate; neither raw-byte savings nor improved
Brotli/Zopfli transfer can qualify a failed canonical gzip gate. The recorded
expanded 3,016,740 total / 229,109 JS and original core failures remain preserved.

One current document format, canonical browser kernel and Rust semantic authority
remain. Preserve all public capabilities, Unicode/IDNA, typed errors, bounded
validation, opaque data, privacy, stable anchors, history, persistence, recovery
and failure atomicity. Never replace checked failures with traps/unchecked paths,
strip required diagnostics, silently change ABI or compile a runtime per preset.
Material API/wire/ABI or toolchain changes need a concrete proposal and explicit
adoption before implementation. Keep native/device and stopped backend gates.

The current optimization ledger's authorizationGate records **zero remaining
authorized tuning** after the cumulative QPF stop. Its historical not_started
fields are not permission. This queue request creates no fresh allocation. WEX-9
read-only audit/proposal work and WEX-3.1 protocol work may proceed once entry
conditions hold; WEX-3.2 candidate execution requires a separately authorized
changed scope/decision and recorded available capacity. Preserve the original
45-minute/two-materially-different-hypothesis ceiling and every consumed attempt;
no reset across parent/source/run boundaries and no Cartesian setting sweep.
Source-level variants, standard-library/allocator experiments, alternate gzip
and post-link passes all count if actually measured. No unchanged rejected QPF,
RBO, WEX-6 or WEX-8 hypothesis becomes a new compiler candidate.

Use stable/pinned supported compiler and Wasm features by default. Nightly
build-std, optimize_for_size, immediate-abort, location-detail, new allocators,
PGO, custom targets, self-decompression, dictionaries or split/Component Model
ABIs are proposals only unless separately adopted. Do not copy force-cfg,
panic_immediate_abort recipes, -all, trap-ignoring or fast-math flags from guides.
Count any decoder/glue/dictionary and loss of streaming, cache or startup costs.

WEX-3.3 retains HTTP precompression/headers/cache/MIME/streaming delivery and may
use the unchanged canonical artifact when candidates are deferred. WEX-5 owns
remaining startup, first-use, input and memory observations. WEX-4.1/4.2 own new
broad regression/negative controls and final budget enforcement; WEX-4.3 owns
claim reconciliation. Delivery here uses existing focused checks, not duplicate
suites or a new benchmark harness. No credentials, paid inference, native OS
qualification, publication or deployment. No new root runner from a worker.

Workers change only verified checkboxes/Status. Separate progress records exact
source/feature/tool/artifact pins, commands, time, nonzero pass/fail/skip counts,
candidate disposition and remaining allowance. Keep generated output ignored and
task-owned; preserve source, data and unrelated index bytes; clean owned temporary
servers and inactive reproducible artifacts. Missing/failed/skipped acceptance
stays unchecked with a fingerprint, owner and concrete resume condition.

## Tasks

### Task WEX-9.1 — Audit the effective compiler and linker retention

- [x] WEX-9.1 Establish the current effective build controls and retained-code roots for every shipped Wasm companion.

Purpose: Select methods from actual post-delivery artifacts instead of repeating already-applied settings or measuring the wrong profile.
Deliverable: A compact effective-profile/export/feature/section map tied to the unchanged core and expanded inventories, with new opportunities and existing controls distinguished.
Context: `core/Cargo.toml`, `core/rust-toolchain.toml`, normal-target Cargo features and lockfile; `core/scripts/{build-wasm,build-highlight-worker,optimize-wasm,share-wasm-glue,browser-size-contract}.mjs`; current production-profile receipts and retained artifact identities; WEX-6 accepted/deferred dispositions; completed source01/02 retained-code attribution; the compiler survey's stable-build/link and package-size sections.
Dependencies: none.
Independent work: WEX-9.2 can classify already researched advanced methods while a nonessential diagnostic is unavailable; missing accepted entry functionality still blocks this source.
Session scope: One read-only audit, 15–25 minutes. Reuse current receipts and installed tool help; no production rebuild, broad metadata dump or diagnostic compiler experiment for unchanged inputs.
Acceptance: Verify actual profile/target/compiler/bindgen/optimizer options and relevant overrides, not only manifest intent. Separate normal runtime features from build/test dependencies and inspect additive feature unification. Distinguish code/data/names/custom sections, required exports and transitive roots, full-package archive contents and required browser downloads. Wasm LLD already garbage-collects unused sections; do not claim adding gc-sections is a new gain. Confirm whether export-all/link-dead-code, unnecessary rooted exports, duplicate dependencies or final diagnostic sections remain. Treat relocation-padding compression as a possible already-satisfied opportunity after post-link rewriting. Attribute observable facts; raw section/IR sizes and overlapping reachability are not additive gzip savings. Keep exports/callbacks required by the ABI and one canonical kernel.

Implementation:

- [x] WEX-9.1-I1 Authenticate existing final artifact identities and build receipts, inspect only missing effective settings/export/feature evidence, and map each remaining cost to WEX-6, WEX-8 or the compiler candidate owner. Record unavailable evidence and the minimal owning producer instead of starting a replacement build pipeline.

Validation:

- [x] WEX-9.1-V1 Cross-check the map against current source options, pinned tool help and existing final resource inventories; verify hashes and nonoverlapping required-resource counting. Budget: 3 minutes of static inspection. Do not report runtime passes or estimated savings as measurements.

Evidence: Current build/section/root map, artifact identities, applied versus missing controls, confidence and precise candidate owners.
Handoff: The missing setting/root or changed source that invalidates reuse, with its minimal producer; do not rerun the whole consumer without changed input.
Blocked behavior: Missing current artifact proof blocks a claim about that artifact; preserve known evidence and stop unchanged diagnostics. Absent tuning authority does not prohibit this read-only task.

### Task WEX-3.1 — Freeze the post-split baseline and candidate decision

- [ ] WEX-3.1 Select a bounded production optimization experiment.

Purpose: Investigate aggressive compression against the properly arranged architecture.
Deliverable: Compact comparison protocol and at most two distinct hypotheses in progress, with the chosen settings documented in the existing size decision record.
Context: `core/Cargo.toml` browser profile; `core/scripts/{build-wasm,optimize-wasm,share-wasm-glue,browser-size-contract}.mjs`; current pinned JS bundler/minifier and compression settings; WEX-1.1 rejected-experiment map; WEX-2.6 consumer artifacts; `architecture/specs/{extension-dx,verification}.md` size/performance sections.
Dependencies: WEX-9.1.
Independent work: HTTP wiring may be inspected, but candidates require this frozen protocol.
Session scope: One bounded attribution/research decision, 15–30 minutes; count actual candidate measurements against the source-wide allowance.
Acceptance: Pin baseline artifacts/toolchain/resources; rank measured remaining costs. Consider current `z` versus `s`, pinned Binaryen `-Os`/`-Oz` versus the existing custom pass list, measured generic-body sharing/cold outlining, formatting/serializer/panic-helper retention, glue/chunk/tree-shaking improvements and Zopfli gzip/Brotli static precompression. LTO, one codegen unit, stripping, aborting panics and Brotli quality 11 already exist; attribute any residual effect before choosing a candidate. Select at most two materially distinct hypotheses, not a Cartesian sweep; aggregate changes need attribution. Count custom decoder/dictionary/glue costs; reject unsupported browser features, CSP relaxation, lost streaming, missing assets, weakened validation or unsafe shortcuts. No wee_alloc adoption, blanket trait-object conversion or nightly/build-std change. Freeze byte, startup/compile/memory regression limits from the current verification contract before measurement. No promised savings percentage.

Compiler survey extension: consume WEX-9.1's effective profile/root map. Evaluate only ranked, supported candidates: current custom Binaryen passes versus one selected -Os/-Oz pipeline; similar-function merging beyond the existing exact-duplicate pass; dead-argument elimination/flow analysis where retained code warrants it; or s versus z. A bounded --converge invocation stops by raw size, so preserve independent canonical-gzip and runtime limits. Verify whether relocation padding is already removed before proposing --compress-relocations. Do not enable closed-world assumptions without boundary proof, combine independent changes without attribution, or repeat WEX-6/WEX-8 implementation. Check current authorizationGate rather than the historical not_started counters; proposing candidates does not grant execution.

Implementation:

- [ ] WEX-3.1-I1 Inspect pinned official tool documentation and earlier rejected candidates, then record each proposed setting, expected mechanism, measured resource owner, comparison controls, allowed runtime baseline and rollback condition. Use optional compatible Twiggy or maintained wasm-tools plus targeted LLVM IR/cargo-llvm-lines only when attribution needs it; profiler/IR counts are not compressed-byte savings. Reuse existing gzip/Brotli accounting, and record why unselected methods remain deferred. Do not add profiling/runtime dependencies merely because a guide names them.

Validation:

- [ ] WEX-3.1-V1 Check artifact hashes, complete resource union and comparable baseline settings; verify proposals differ materially from unchanged rejected ones and fit the shared time/hypothesis ledger. Budget: 3 minutes, no broad benchmark run.

Evidence: Protocol, candidate ledger, immutable baseline identities and official version-appropriate references in progress.
Handoff: Remaining allowance, candidate not yet measured and exact reproducible invocation.
Blocked behavior: Missing frozen interfaces/baseline/limits blocks experiments; repair the named prerequisite rather than guessing or changing metrics.

### Task WEX-3.2 — Implement the winning safe production settings

- [ ] WEX-3.2 Compare bounded candidates and retain only justified production changes.

Purpose: Reduce real shipped bytes without trading away correctness or browser startup.
Deliverable: Measured candidate dispositions and, where justified, reproducible pinned optimizer/minifier/precompression changes.
Context: WEX-3.1 protocol/remaining allowance; existing build staging/optimizer boundary checks, core and expanded inventories and affected semantic/load fixtures.
Dependencies: WEX-3.1.
Independent work: none; do not start another optimization batch.
Session scope: Remaining source-wide candidate allowance only; necessary winning-setting wiring/checks must stay bounded, otherwise hand off to the controller.
Acceptance: Compare identical feature inventories and toolchain with raw/canonical-gzip-9/alternate-gzip/Brotli, total JS/glue/assets, startup/compile, memory and build-compression CPU costs. No import/export-only correctness claim, checksum laundering, stripped required behavior, payload truncation or fixture runtime. Source-level generic/formatting/error-path changes retain current typed diagnostics, redaction, recovery and resource/bounds checks; no unchecked unwrap, artificial unreachable path or trap replaces an admitted error. Keep failed candidate evidence concise in progress. No improvement is a valid measured disposition, not proof that budgets passed. Retained settings reproduce, preserve original semantic/load fixtures and validate the explicit permitted Wasm feature set before instantiation through pinned generated glue.

Implementation:

- [ ] WEX-3.2-I1 Run only selected candidates within the shared ledger; wire a winner through existing staged production build gates. Revert rejected candidate source edits precisely without touching unrelated dirty work. Keep deterministic production assets reproducible and generated files outside Git.

Validation:

- [ ] WEX-3.2-V1 Run changed-owner Wasm load and semantic fixtures plus the exact bounded comparisons defined in WEX-3.1. Validate the final module against the explicit supported feature set using a pinned compatible validator; an optimizer success is not browser qualification. Record nonzero results, regression thresholds, bytes and retained/deferred dispositions. Budget: within the source-wide allowance; original budget failures remain visible and unchecked in final qualification.

Evidence: Candidate settings, comparisons, elapsed work, original failure observations and retained source changes.
Handoff: Exact remaining experiment/check, immutable input pins and remaining allowance; expiry is not permission to retry.
Blocked behavior: Unchanged failure or expired allowance stops candidate dispatch; WEX-3.3 can validate the retained canonical build independently of byte success.

### Task WEX-9.2 — Disposition advanced compiler and packaging methods

- [ ] WEX-9.2 Record explicit applicability and adoption gates for the remaining size methods.

Purpose: Keep higher-cost research actionable without silently changing toolchain, diagnostics, runtime support or size accounting.
Deliverable: A concise decision table in the existing research note/progress linking each method to current retained evidence, expected mechanism, risks, prerequisite decision and an implementation owner or deferral condition.
Context: WEX-9.1 current build/root map and existing source01/02 attribution; `architecture/research/wasm-code-size-methods-20261027.md` advanced-method and package/cache/runtime sections; current pinned Rust/Binaryen and browser feature contracts. Reuse its primary references; verify only changed or uncertain version details.
Dependencies: WEX-9.1.
Independent work: This read-only decision is independent of WEX-3.2 success and available tuning time; it does not authorize experiments.
Session scope: One bounded applicability decision, 15–25 minutes; no toolchain installation, new library, training run or benchmark.
Acceptance: Cover standard-library rebuilding with optimize_for_size; current unstable immediate-abort versus the obsolete panic_immediate_abort library-feature recipe; panic location-detail and diagnostic loss; targeted generic-body sharing/cold outlining as an unimplemented lead (review-dependent WEX-8 is skipped); PGO with proven target/runtime support and representative deterministic inputs; allocator/no_std leaf applicability; reference-types glue with the existing ABI gate; Brotli/Zopfli/custom decoder/splitting distinctions; and native/package/archive/cache changes versus the browser union. Installed rustc reports -C inline-threshold removed, and raw llvm-args lack the usual stability contract. Do not present these as stable defaults or guaranteed savings. Reject unsupported trap/float assumptions, lost diagnostics, unsafe/wee_alloc shortcuts, a second serializer beside still-required Serde, and shifts of bytes to another required resource. Each promising material change needs a concrete separate proposal before adoption; each deferred method has an evidence/authority condition, not an unchanged retry loop.

Implementation:

- [ ] WEX-9.2-I1 Map the researched advanced methods to current evidence and stable/native/browser obligations, update only changed conclusions in the existing note, and hand any justified future proposal to its exact owner. No automatic runtime, standard-library, allocator or ABI changes and no additional roadmap/controller launch.

Validation:

- [ ] WEX-9.2-V1 Check every disposition has a current source/version reference, honest retained-cost evidence or explicit gap, required decision and owning task. Budget: 3 minutes of source/document checks. Confirm no candidate, tool installation or paid/provider execution occurred and all canonical caps/diagnostic obligations remain unchanged.

Evidence: Versioned method/disposition table, remaining questions, exact proposal prerequisites and owner references.
Handoff: One unresolved applicability/version question with a concrete source to inspect; unselected methods remain deferred.
Blocked behavior: Missing support evidence leaves that method unadopted; do not block independent standard-method delivery solely because an optional nightly/native proposal is unavailable.
