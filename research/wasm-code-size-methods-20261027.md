# Rust/Wasm production size methods

Date: 2026-10-27. Status: researched planning input; no optimizer experiments,
new tool installations, production builds, size savings or qualification claimed.
Updated: 2026-10-28 with the compiler/linker/post-link survey below, using primary
documentation and the installed Rust/Binaryen help. No candidate was executed.
Delivery: [WEX follow-up](../runner-queues/wasm-extensions-20261027/README.md), after
all Rust architecture jobs, then physical core/extension separation. Existing
SDK/EXT/FIT/QPF owners remain canonical. No runner/queue or runtime budget changed.

The [additional loading and small-editor review](small-editor-and-loading-methods-20261027.md)
extends the candidate applicability screen with wasm-squeeze, Blazor loading
patterns and Component Model examples. WEX-2.7's measured fixed-cost work and
source 03 share the same candidate ledger; WEX-5 final comparisons add no tuning
allowance. No algorithm or performance benefit is inferred from those references.

## Reading the supplied guide in context

The [Rust/Wasm size guide](https://rustwasm.github.io/book/reference/code-size.html)
recommends profiling retained code, size-oriented builds, post-link optimization,
and scrutiny of formatting, allocation and generic code. It distinguishes transfer
size from interaction latency and recommends measuring compressed bytes. Adopt
that measurement approach, not automatic rewrites. Its page labels itself
unpublished documentation, and some examples and tool assumptions are historical.
This project uses its existing Cargo/wasm-bindgen build scripts, not a new
wasm-pack pipeline. Tool availability and runtime assumptions must be checked
against the pinned compiler, bindgen and Binaryen before execution.

## Existing local controls

Source inspection of `core/Cargo.toml` shows `[profile.browser]` already uses
`opt-level = "z"`, `lto = true`, `codegen-units = 1`, `strip = "symbols"` and
`panic = "abort"`. Workspace Rust lints forbid unsafe code. These settings are
implemented baseline controls, not new savings or additional experiments.

`core/scripts/optimize-wasm.mjs` pins Binaryen 132.0.0 and runs selected passes:
duplicate-function elimination, unused-module-element removal, vacuum,
instruction optimization and debug stripping. It declares the permitted Wasm
features and rejects changed import/export boundaries or increased raw/gzip size.
It is not presently an automatic `-Os`/`-Oz` default-pipeline comparison.
`browser-size-contract.mjs` fixes canonical gzip level 9 and Brotli quality 11,
counts required lazy resources and reports independent size metrics.
`share-wasm-glue.mjs` already shares generated bridge patterns; any new
transformation must preserve its pinned glue contract and existing assertions.
Recheck these inputs after RAQ/WEX architecture changes before candidate selection.

## Methods and applicability

| Method | Decision for edit.ac | Evidence and owner |
| --- | --- | --- |
| Wasm section and reachability attribution | Separate code, data, names/debug/custom sections and rooted exports. Identify shallow versus retained cost; do not sum overlapping retained subgraphs as independent savings. A raw-byte contributor is not an estimate of gzip savings. | WEX-1.1, WEX-3.1; [Twiggy source](https://github.com/AlexEne/twiggy), [wasm-tools](https://github.com/bytecodealliance/wasm-tools). |
| Generic code and monomorphization | Only when profiles implicate repeated instantiations, move a large non-generic body behind a small generic wrapper. `cargo llvm-lines` or targeted LLVM IR can locate repetition; IR volume is a lead, not emitted/retained or compressed-byte proof. Keep static dispatch on important hot paths unless measured otherwise. | WEX-3.1/3.2; [Rust Performance Book](https://nnethercote.github.io/perf-book/compile-times.html). |
| Cargo profile comparisons | A measured `s` versus current `z` candidate may be worthwhile; stronger nominal size settings do not guarantee a smaller result. Thin/fat LTO, codegen units and package overrides enter only a ranked hypothesis, not a combinatorial sweep. Check effective workspace settings and environment overrides. | WEX-3.1/3.2; [Cargo profiles](https://doc.rust-lang.org/cargo/reference/profiles.html). |
| Binaryen size pipelines | Compare current custom passes with a supported pinned `-Os` or `-Oz` pipeline only if prior failed evidence does not already reject the same inputs/settings. Verify features and semantics, not just export names. Preserve current raw/gzip staging guards. | WEX-3.1/3.2; [Binaryen 132 option source](https://github.com/WebAssembly/binaryen/blob/version_132/src/tools/optimization-options.h). |
| Formatting, serialization and cold errors | Inspect retained formatting/serializer families, repeated wrappers and panic paths before editing. Reuse the existing concise error serializer where helpful; retain typed errors, validation detail, privacy/redaction and explicit recovery content. Do not replace required JSON/wire serializers with an unbounded handwritten codec. | WEX-3.1/3.2; retained-artifact evidence plus RAQ safe-diagnostic contracts. |
| Inlining and outlining | Test only a measured repeated cold body or oversized generic wrapper. Shared non-generic helpers or selective outlining may reduce duplication; blanket `inline(never)`/trait-object rewrites can worsen call overhead, table retention and latency. | WEX-3.1/3.2; [Rust Performance Book](https://nnethercote.github.io/perf-book/compile-times.html), actual Wasm/call measurements. |
| JS/glue/tree shaking | Inspect real ESM consumer reachability, root barrels, side-effect declarations, duplicate chunks and generated glue. Annotate purity only where true; preserve CSS registration and worker entry effects. A small Wasm module does not solve a retained JS graph. | WEX-1.4, WEX-2.2 and WEX-3.2; [esbuild tree shaking](https://esbuild.github.io/api/#tree-shaking). |
| Reference-types glue | Audit actual generated bindings and pinned target settings before considering a change. Upstream documents reduced JS reference-management glue with `externref`; our optimizer already permits reference types. This may already be realized or inapplicable to the retained string/byte ABI. Never advertise it as an automatic new saving. | WEX-3.1; [wasm-bindgen reference types](https://wasm-bindgen.github.io/wasm-bindgen/reference/reference-types.html), current generated glue. |
| Static gzip with Zopfli | Zopfli can produce gzip-compatible output using more build CPU. Candidate scope is offline precompression, not runtime compression or a browser decoder. Report its actual transfer savings and build time against deterministic gzip-9, on the same complete resource union. | WEX-3.1–3.3; [Zopfli upstream](https://github.com/google/zopfli). |
| Brotli precompression | Brotli is a separate delivery representation. Quality 11 is already the inventory baseline; do not claim selecting it is a new gain. Compare any justified supported setting against that baseline, including compression CPU, local HTTP behavior and cache artifacts. | WEX-3.1–3.3; [Brotli upstream](https://github.com/google/brotli), existing HTTP contract. |
| Wasm feature validation | Validate final modules with an explicit permitted feature set, then instantiate them through generated glue. Compiler defaults change; dead code containing unsupported instructions may still make a module invalid. A successful host compiler or optimizer invocation does not qualify browsers. | WEX-3.2, WEX-4.2; [Rust target documentation](https://doc.rust-lang.org/rustc/platform-support/wasm32-unknown-unknown.html), [wasm-tools](https://github.com/bytecodealliance/wasm-tools). |

## Tool reliability and diagnostics

The old `rustwasm/twiggy` link redirects to
[AlexEne/twiggy](https://github.com/AlexEne/twiggy), which GitHub reports archived
on 2026-03-14. Do not adopt it as a required CI dependency. If an already available
compatible release parses the current module, use its retained-size/root-path
analysis as an optional diagnostic. Otherwise use maintained wasm-tools section,
module and feature inspection, actual generated exports, the existing packed
resource graph and targeted LLVM IR where attribution is still missing. Record
the loss of retained-call-graph detail; section sizes alone do not replace it.
Pin diagnostic versions and fail/record unsupported encodings honestly.

Source maps/names or diagnostic IR may help identify a measured owner. Generate
only a bounded task-owned diagnostic artifact when production stripping prevents
attribution. Keep the final production build/settings as the measurement source;
diagnostic byte sizes do not count as shipping results. Inspect a targeted
function/section rather than dumping a whole `.wat` or LLVM IR file into context.
Do not add a permanent profiler dependency or emit persistent debug artifacts.

## Rejected defaults and separately gated possibilities

- **No `wee_alloc` adoption.** [RustSec RUSTSEC-2022-0054](https://rustsec.org/advisories/RUSTSEC-2022-0054.html)
  marks it unmaintained and notes open memory-leak issues. The
  [Rust target docs](https://doc.rust-lang.org/rustc/platform-support/wasm32-unknown-unknown.html)
  identify dlmalloc as the default allocator. Keep the current allocator unless
  profiling demonstrates a material allocator contribution and a separately
  justified, maintained alternative passes allocation-heavy, long-session,
  fragmentation, peak-memory and disposal checks. No allocator package is selected
  or installed by this research.
- **No unchecked or lossy error shortcuts.** Preserve safe checks, typed admission
  failures and recovery. Do not replace a recoverable `Result` with a trap, remove
  bounds/resource checks, use unchecked unwrap/indexing or mark user-controlled
  paths unreachable for size. `panic = "abort"` is already the browser policy;
  it does not remove all panic formatting or make abort an acceptable validation
  error. Never enable undefined behavior or conflict with `unsafe_code = "forbid"`.
- **No blanket dynamic dispatch or allocation elimination.** A stateful CRDT editor
  needs owned data and durability. Keep changes within measured leaf boundaries;
  do not rewrite Yrs, history or persistence to chase a small theoretical saving.
- **Nightly `build-std`, custom targets and panic-runtime stripping are deferred.**
  They change toolchain/support obligations and are not assumed available in the
  current stable pinned workflow. The target docs explicitly distinguish default
  features, minimal targets and nightly standard-library rebuilds. No upgrade,
  unwinding change or new browser feature requirement is authorized here.
- **Custom transport codecs/dictionaries, Wasm splitting/rewriting ABIs and PGO**
  need a separate evidence-based proposal if standard methods leave a material
  gap. Count all decoders/dictionaries, caching and streaming consequences; never
  weaken the runtime baseline or cap to make a format appear cheaper. No such
  framework or production dependency is selected by this plan.

## Experiment protocol and metric integrity

The candidate menu is broader than the permitted experiment batch. Once the
architecture is complete, select at most two materially distinct hypotheses
within the existing 45-minute optimization allowance. Assessment/source inspection
is not authority to run every combination. Every actual candidate measurement,
including Zopfli or a source-level rewrite, consumes that same ledger. Do not reset
the allowance at a task, session or source boundary. Reuse unchanged failures;
unselected methods remain deferred with owner, reason and changed-input trigger.

Freeze identical feature inventories, source/toolchain/build identities and
numerical startup/compile/memory limits before comparing candidates. Keep raw,
canonical gzip-9, alternate gzip transport and Brotli bytes separate. The existing
hard cap is computed by canonical gzip-9: smaller Zopfli HTTP responses are useful
delivery evidence, not permission to replace that metric or mark its failure as
passing. A compression-metric change requires a separate explicit decision and
contract/gate update. Retain import/export, byte identity, compatible feature,
semantic fixture, cancellation and data-preservation assertions. Optimizer
acceptance also preserves the current no-raw/no-gzip-growth policy unless a
separately approved decision changes it. No source-level savings are established
by a function profile or an IR count alone.

WEX-4.2 owns the final configuration inventories, hidden-lazy/duplicate/missing
asset controls, side-effect retention controls, permitted-feature validation and
standard compressed HTTP negotiation/decompressed-identity checks. Reuse existing
unchanged tests and receipts; only missing controls belong in the final testing
phase. Final report states delivered bytes/headroom, startup/memory tradeoffs,
candidate rejection/defer reasons and any unmet core/expanded budget. User
confirmation, 2026-10-28: the expanded app ceiling is 1 MiB (1,048,576 bytes) total
gzip including JS/glue/Wasm/CSS/required assets and required lazy code; core limits
remain 512 KiB total/32 KiB JS gzip. This records budget authority, not a runtime
gate implementation or passing measurement.


## Leptos binary-size guide addendum — 2026-10-27

The [Leptos guide](https://book.leptos.dev/deployment/binary_size.html) reinforces
using release artifacts and a separate size-oriented Wasm profile. It additionally
suggests investigating regex/Unicode-table retention, subset serializers and
nightly panic-runtime changes. Its code-splitting section describes lazy functions
and routes, with function loading becoming async and independent route code/data
loading avoiding waterfalls. These are upstream capabilities and suggestions,
not measured edit.ac results; its size figures are not our expected savings.

**Binary splitting is an alternative worth assessing, not a Leptos dependency.**
WEX-1.2 compares the existing standalone companion approach with one build graph
split at optional leaf boundaries, using the guide and the upstream
[cargo-leptos implementation](https://github.com/leptos-rs/cargo-leptos) as design
references. Establish the actual tool/runtime requirements, memory/table/import
ownership, glue/loader cost and failure behavior before proposing adoption.
Multiple chunks need not mean multiple writable documents, but that property
must be demonstrated rather than assumed. Preserve one canonical kernel and
semantic owner, not a binary per preset. Never defer synchronous input,
composition, selection or atomic commits behind a first-load promise. Optional
codec/export/analysis preparation may use explicit async readiness when its
current contract permits it. A materially different split/ABI design requires a
concrete proposal and updated owning acceptance before implementation; the
current plan does not install Leptos or authorize that redesign automatically.
Actual size/startup experiments remain after physical architecture completion
and consume the same shared optimization ledger.

**Regex analysis starts from retained data and features.** WEX-1.1 distinguishes
Unicode tables, regex engines, parsers and unrelated data segments in actual
production artifacts, including host versus browser paths and feature unification.
WEX-3.1 may rank feature narrowing only when exact patterns, required Unicode
semantics and existing feature ownership permit it. Do not add a regex dependency
to test a theoretical saving. Do not disable Unicode, silently use ASCII-only
matching or substitute browser RegExp for Rust semantics on an authoritative
validation/matching boundary. Optional host/presenter-only parsing can use an
existing host port only with demonstrated equivalent public behavior; this is
not permission to move committed semantics out of Rust.

**Serializer alternatives require a bounded contract and a net-size case.**
Inventory retained serde/serde_json first; the current manifests already depend
on them for several engine and session boundaries. Adding a subset codec beside
required serde may retain both implementations. Consider an alternative only on
an independently removable optional leaf, with maintained/version-compatible
support and explicit proof for every required data type, unknown-field/opaque
preservation, bounds, error and number behavior. Do not change document, wire,
checkpoint or public error JSON to pursue size, build a second compatibility
reader or weaken deny-unknown/validation contracts. A serializer replacement is
not a default delivery requirement or an unmeasured promised gain.

**Nightly standard-library and panic flags remain deferred.** The guide's
build-std/panic_immediate_abort/cfg examples are not instructions to copy into the
workspace. Keep our pinned stable build and existing browser-only profile, which
already uses aborting panics; preserve native/server behavior. Any future proposal
must verify the exact compiler's supported flags, toolchain maintenance and
recovery semantics. Do not force a dependency cfg to suppress a real capability
mismatch. Current browser-profile settings are existing controls, not new savings.

**Chunk/cache identity needs negative controls if splitting is selected.** A
[reported upstream issue](https://github.com/leptos-rs/cargo-leptos/issues/658)
with cargo-leptos 0.3.6/Leptos 0.8.19 describes a loader filename retaining its hash
after referenced chunk hashes changed. This is an upstream report, not a verified
local defect or a claim about all current releases. It motivates WEX-4.2 checks
that references are finalized before loader/manifest identities are frozen,
changed chunks invalidate the referring graph correctly, and stale/missing/mixed
chunk versions fail without document mutation. WEX-5.2 reports first-use latency,
chunk/data concurrency and complete required unions; a smaller initial chunk alone
cannot establish a budget pass or faster actual readiness. Reuse current manifest,
HTTP and lifecycle ports rather than introduce another loader/harness.

Source review only: no Leptos tools, macros, regex features, serializers, nightly
flags, chunking or runtime budget settings were changed, and no benchmark ran.

## Compiler, linker and retained-code survey — 2026-10-28

Subsequent delivery owner: [Rust build-size roadmap](../runner-queues/wasm-extensions-20261027/02d-rust-build-size.md),
queued by the user's later explicit request. It preserves WEX-3.1/3.2 IDs and
adds WEX-9.1/9.2; no research result itself authorizes candidate execution.

The user requested further research into shrinking Rust while building/compiling
and other size-reduction methods. This extends research only; the existing seven
package-size parents, runner state, contracts, caps and optimization allowance
are unchanged. Actual builds/comparisons still require the reconciled shared
allowance. New upstream options are a candidate menu, not an experiment queue.

### Checked local baseline

The explicitly pinned compiler reports Rust 1.97.1 (8bab26f4f, 2026-07-14), LLVM
22.1.6; installed Binaryen reports version 132. The shell does not expose Rust
on PATH, so version/help inspection used its existing absolute toolchain path.
No toolchain was downloaded. `build-wasm.mjs` resolves the pinned Cargo and rustc,
requires wasm-bindgen 0.2.129, uses the browser profile, and stages post-link
optimization. `build-highlight-worker.mjs` still uses ordinary release and omits
that optimizer: WEX-6.1 owns the known inconsistency.

The browser profile already sets `opt-level = "z"`, fat LTO, one codegen unit,
symbol stripping and aborting panics. These are not additional gains. The
previously authenticated expanded artifact is 3,016,740 gzip bytes: highlighting
1,435,671, core 759,022 and Markdown 590,184 are Wasm; JS is 229,109 and CSS 2,754.
Wasm instruction optimization does not automatically eliminate the full embedded
highlighting grammar data or Markdown's reachable document-restoration paths.
The 65.2% required aggregate reduction has no compiler-only proof.

### Stable build and link methods

| Method | Mechanism and applicability | Owner / decision |
| --- | --- | --- |
| Effective profile consistency | Confirm the exact profile, compiler, Cargo feature graph and environment/config overrides for every shipped companion. Native release and test/probe artifacts are different inputs. | WEX-6.1 first; use existing staged production controls. |
| Compare `s` with `z` | `z` disables loop vectorization; neither option guarantees the smallest emitted or compressed result. Keep other inputs fixed. | WEX-3.1/3.2 candidate only if remaining allowance and prior results justify it. |
| LTO and codegen units | Cross-crate optimization can remove or combine code. Fat LTO/one unit already apply to the browser profile. Thin-LTO/profile overrides are alternatives to measure, not additive guaranteed savings. | Verify baseline; no factorial settings sweep. |
| Debug/name stripping | Inspect the final post-bindgen module, not just Cargo output. Debug data and names can be reintroduced by later tools. The highlighting name section previously measured 291,880 raw bytes; its gzip saving is unknown. | WEX-6.1; retain diagnostics separately and count only actual shipped bytes. |
| Dead-section elimination and export roots | Wasm LLD already defaults to garbage collection. Exported functions and their reachable code/data remain roots; marking code public or putting it in another crate alone does not establish its final retention. Avoid unnecessary export-all/link-dead-code settings and identify genuinely unused generated exports. | WEX-7.1/8.1; preserve public/ABI requirements and the single canonical kernel. |
| Feature/dependency narrowing | Remove unused normal-target functionality at its real dependency edge, checking feature unification and build versus runtime dependencies. Cargo features are additive; another edge can re-enable a default. | WEX-6/7; confirm the emitted graph, not only Cargo.toml. |
| Relocation padding | LLD offers `--compress-relocations` to reduce Wasm relocation padding. Post-link rewriting may already erase the opportunity; raw code size is not gzip evidence. Debug/source-map offsets must remain correct. | Low-priority inspection; do not add blindly to the pipeline. |

Primary references: [Cargo profiles](https://doc.rust-lang.org/cargo/reference/profiles.html),
[Cargo feature unification](https://doc.rust-lang.org/cargo/reference/features.html#feature-unification),
[Wasm LLD garbage collection and relocation options](https://lld.llvm.org/WebAssembly.html),
and [rustc codegen options](https://doc.rust-lang.org/stable/rustc/codegen-options/).
The installed compiler help also says `-C inline-threshold` has been removed.
Direct `-C llvm-args` tuning has no rustc CLI stability guarantee; old recipes
using that removed flag must not be copied into the pinned build.

### Post-link optimization beyond the current pass list

The current script runs duplicate-function elimination, unused-module removal,
vacuum, instruction optimization and debug stripping. Installed Binaryen 132
also exposes these mechanisms:

- `-Os` / `-Oz`: full default size-oriented pipelines, beyond the selected passes.
- `--merge-similar-functions`: parameterizes similar functions that differ in
  constants/call targets. This goes beyond the exact-duplicate pass already used.
- `--dae`, `--dce` and `--gufa`: argument elimination, unreachable-code removal
  and whole-module flow analysis. Some work can overlap default pipelines.
- `--converge`: repeats passes while binary size decreases. Its stopping metric
  is raw binary size, so keep a separate canonical-gzip and runtime regression
  check and a fixed wall-clock bound; convergence is not permission to exceed
  the experiment allowance.

Assess one supported pipeline or one attributed additional mechanism, not every
flag combination. Changes in function sharing/call shape can affect startup,
runtime and compression. Preserve explicit supported features and current staged
no-raw/no-gzip-growth guards. Do not enable closed-world assumptions without
proving the JS/Wasm boundary satisfies them, or use trap-ignoring/fast-math flags
that weaken required failure or numerical behavior. Import/export equality alone
does not establish semantic equivalence. WEX-3.1/3.2 own candidate selection;
WEX-4.1/4.2 retain semantic and artifact acceptance.

Primary pinned sources: [Binaryen 132 optimization options](https://github.com/WebAssembly/binaryen/blob/version_132/src/tools/optimization-options.h),
[similar-function merging](https://raw.githubusercontent.com/WebAssembly/binaryen/version_132/src/passes/MergeSimilarFunctions.cpp)
and [wasm-opt convergence](https://raw.githubusercontent.com/WebAssembly/binaryen/version_132/src/tools/wasm-opt.cpp).
Installed `wasm-opt --help` independently confirmed those options; no module was
passed to an optimizer during this research.

### Source and data changes that make compilation produce less code

1. **Share substantial non-generic bodies.** Keep a small generic conversion
   wrapper and move repeated work behind a concrete internal type where profiles
   demonstrate duplication. Avoid broad `dyn Trait` conversion: vtables, indirect
   calls, allocations and retention can offset savings. The
   [Rust Performance Book](https://nnethercote.github.io/perf-book/compile-times.html)
   describes this transformation; LLVM IR counts remain a lead rather than a
   shipping-byte result. WEX-7.1/8.1 inspect serializer/preparation families first.
2. **Review inlining and cold paths selectively.** A large repeated helper can
   justify `#[inline(never)]` or a shared cold helper; removing unnecessary
   `inline(always)` can allow better compiler decisions. These are hints and can
   hurt performance. Keep synchronous input paths measured and do not globally
   disable inlining. [Rust codegen attributes](https://doc.rust-lang.org/reference/attributes/codegen.html)
   document the behavior; WEX-7.1/8.1 own attribution and any source change.
3. **Remove unnecessary retained data and duplicate machinery.** Build the
   complete required three-language grammar closure instead of embedding every
   grammar, and keep Markdown codecs on an adopted inert-data boundary rather
   than restoring documents. Check costs across both core and companion;
   moving bytes is not removal. These are already WEX-6.2–6.4 work.
4. **Consolidate serialization/formatting without losing contracts.** Share
   repeated wire/error adapters where retained profiles support it. Required
   Serde, JSON validation, typed errors and recovery stay authoritative; adding a
   second serializer while Serde remains can increase total code. Removing user
   diagnostics or replacing errors with traps is not an acceptable compactness
   change. WEX-7.1/8.1 and the existing safe-diagnostic contracts own this work.
5. **Verify generated JS glue and renderer graphs.** Reference types can reduce
   manual JS reference-management glue, but the inspected legacy binding path
   previously changed ABI when metadata was preserved. The
   [wasm-bindgen guide](https://wasm-bindgen.github.io/wasm-bindgen/reference/reference-types.html)
   describes the mechanism, not a free local toggle. Any ABI proposal remains
   explicit; WEX-6.5 owns retained JS/MathML costs independently of Wasm size.

### Higher-cost or separately gated methods

| Method | What the research supports | Current disposition |
| --- | --- | --- |
| Rebuild standard libraries for size | The unstable `optimize_for_size` library feature selects smaller algorithms in core/alloc/std. It requires rebuilding std, rather than assuming the application profile changes every prebuilt library implementation. See the [Rust tracking issue](https://github.com/rust-lang/rust/issues/125612). | Potential later hypothesis for retained formatting/sort paths; nightly/toolchain and performance proposal required. Not enabled by this research or the current plan. |
| Immediate-abort panics | Current Cargo docs expose unstable `panic = "immediate-abort"`; Rust's current core source rejects the old `panic_immediate_abort` build-std feature recipe. Rebuilding core/std is still required. | Version-check before even proposing it. It removes panic handling/diagnostic machinery beyond ordinary abort; do not sacrifice required errors or recovery. Existing stable policy remains. |
| Trim panic locations | Unstable `-Z location-detail` can omit file/line/column data and permit shared panic paths. Already-built std may retain its own locations. | Separate diagnostics/toolchain trade-off; not a default, and not equivalent to debug-symbol stripping. |
| Profile-guided optimization | Training and recompilation can guide optimization using representative executions; it is primarily a performance tool, not a guaranteed size reduction. See [rustc PGO](https://doc.rust-lang.org/rustc/profile-guided-optimization.html). | Low priority; first establish target/runtime support and a deterministic representative corpus. No paid/provider traffic and no broad training sweep. |
| Alternative allocator or no_std | Could matter for a small independently removable leaf, but the editor still needs allocation and CRDT/durability behavior. Existing diagnostics did not identify allocator primitives as a dominant core contributor. | No whole-engine rewrite or wee_alloc adoption; require maintained support and retained-cost evidence before a proposal. |

Current unstable-panic sources: [Cargo immediate-abort](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#panic-immediate-abort),
[core's rejection of the old feature recipe](https://doc.rust-lang.org/stable/src/core/panicking.rs.html)
and [location-detail](https://doc.rust-lang.org/unstable-book/compiler-flags/location-detail.html).
Upstream/nightly availability does not mean our pinned stable toolchain supports
these options. No nightly flags, standard-library rebuild or loss of panic detail
was attempted.

### Distinguish package, build-cache and runtime sizes

Excluding examples, maps, diagnostics or duplicate source from a published
package can reduce its archive when they are actually included. It does not
reduce the measured browser resource union unless those files were required
downloads. Removing `.rlib` metadata/embedded bitcode mainly addresses build or
distribution artifacts; disabling bitcode also conflicts with LTO when that
bitcode is required. Source minification and fewer Rust lines do not establish
smaller machine code. Dynamic libraries, extra companions or lazy chunks can
shift bytes without reducing the complete dependency union. Native executable
packers are not a browser-Wasm solution and add runtime/support trade-offs.

Keep gzip-9 as the gate. Brotli/Zopfli precompression remains useful for actual
HTTP transfer, but cannot turn this gate green. The practical priority is
consistent production settings, removal of known retained data/implementation,
then an evidence-selected Binaryen or source-sharing candidate. `s` versus `z`,
std rebuilds and specialized panic handling remain alternatives ranked against
actual remaining cost and allowance; no method has a local savings percentage
until identical-feature production artifacts and affected semantics are checked.
