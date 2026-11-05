# Small editors, loading boundaries and additional Wasm methods

Date: 2026-10-27. Status: source review and planned work only. No dependency
installation, benchmark, tool experiment, performance win or production change is
claimed. Extends [code-size research](wasm-code-size-methods-20261027.md) and the
[WEX plan](../runner-queues/wasm-extensions-20261027/README.md). Keep RAQ first,
physical extension boundaries next, optimizer/compressor experiments afterward.

## Findings from the supplied links

### Bit platform templates

The [template overview](https://bitplatform.dev/templates) describes a complete
Blazor application template, not a Rust/Wasm size experiment. Its linked
[upstream repository](https://github.com/bitfoundation/bitplatform) describes
prerendering combined with PWA behavior. Transferable lessons are application
shell separation, route-level assets and explicit cache/update identity. A fast
static shell or warm service-worker hit is not proof of uncached editor readiness
or smaller editor code. Do not provision/adopt the template, import its platform
stack or infer an edit.ac performance result from a demo.

### Reddit discussion

The [Blazor thread](https://www.reddit.com/r/Blazor/comments/1mbcwl9/how_to_squeeze_the_wasm_binaries_down_even_more/)
provides investigation leads, not controlled measurements. It discusses lazy
loading, dependencies, compression and runtime/compiler tradeoffs; comments also
mix installed storage, build output, transfer and readiness. Treat AOT, IL
linking, reflection/globalization settings and assembly runtime overhead as .NET
specific until separately supported by applicable primary documentation. Our Rust pipeline already emits compiled Wasm rather than .NET IL assemblies. Do not disable
Unicode/locale behavior or move committed semantics to JavaScript to imitate
Blazor flags. No Reddit percentage becomes a target, expected gain or local proof.

### Blazyload

[Blazyload's source README](https://github.com/RonSijm/RonSijm.Blazyload) describes
navigation-triggered assembly loading, dependent-assembly loading and service
registration. The useful analogue is an explicit extension dependency graph,
readiness before activation and controlled host capability binding. Use current
edit.ac resources/registry; do not add a second loader or copy a .NET DI framework.
Reject missing/cyclic/incompatible dependencies before document mutation; dedupe
in-flight immutable loads and initialize ready independent dependencies without
unnecessary serial waterfalls. Cancellation/retry/disposal and permissions remain
per editor even when a module is shared. Required first-input work cannot simply
move outside a reported timing window or disappear from the required byte union.

### wasm-squeeze

The [crate entry](https://crates.io/crates/wasm-squeeze) was not readable as package
metadata through the web text reader, so the review used its
[published crate documentation](https://docs.rs/crate/wasm-squeeze/0.1.0) and
[upstream README/algorithm](https://github.com/zetanumbers/wasm-squeeze).
It targets WASM-4 cartridges: it merges/compresses data segments with upkr, embeds
a decompressor and adds decompression to the Wasm start function. It is not a
general executable-code compressor; the project explicitly says RAM use is not
reduced. Its cartridge size results do not establish gzip/Brotli savings or
startup benefits for wasm-bindgen editor artifacts.

WEX-3.1 first assesses whether current data segments are material and whether the
tool supports our memory/imports, start function, generated glue, data offsets,
feature set and initialized memory semantics. Do not copy its example optimizer
`-all` setting or broaden browser features. Any actual candidate consumes the
same two-hypothesis/45-minute allowance and needs complete decoder overhead,
canonical gzip/actual transfer, instantiation/startup, peak memory and semantic
equivalence checks. If incompatible or not supported by attribution, defer with
the exact reason rather than install it or predict a saving.

### Component Model compression article

The [supplied article](https://medium.com/wasm/wasm-component-model-seamless-compression-c-rust-and-wasm-3b8d52ed8b31)
demonstrates compression functionality implemented across C++/Rust/Wasm using
Zstandard and component interfaces. That is distinct from compressing the
editor's executable distribution. WIT/capability boundaries are useful design
references, not evidence that Component Model packaging reduces browser cost.
The primary [Jco documentation](https://bytecodealliance.github.io/jco/introduction.html)
and [transpilation interface](https://github.com/bytecodealliance/jco/blob/main/docs/src/transpiling.md)
describe JavaScript bindings/core modules for components. Account for generated
bindings, modules, any WASI shims, decoding/copies and startup if this is ever
proposed. Do not port the browser kernel to components or add a Zstd decoder under
the current plan; a material ABI/runtime change needs a separate proposal.

## Why small editors need a separate performance track

An empty field or short comment can be dominated by module transfer, initialization,
CRDT admission, boundary crossings, serialization, subscriptions and DOM adoption.
This is an engineering hypothesis requiring attribution, not a measured diagnosis.
A larger-document throughput win would not establish a small-editor startup or
input-latency win. Keep a useful local editor and its existing durability/history
guarantees; a second writable JS model or a temporary contenteditable with lossy
handoff is not an acceptable shortcut.

Existing `core/benchmarks/comparison/` already pins Tiptap 3.32.0 and includes
edit-only and Yjs/persistence profiles, public-command checks and artifact union
accounting. Its current fixture corpus has Task (20 blocks/10,240 UTF-8 bytes) and
Long only. Its `tiptap-minimal` uses a configured StarterKit; that name is not
evidence of the smallest practical paragraph/text editor. Extend this harness,
not a new one. Preserve old fixture identities and failed results; add separately
versioned empty, one-paragraph 128-byte and four-paragraph 1-KiB fixtures, with
Unicode content and exact byte/UTF-16 counts. Use a supported current empty-doc
fixture, never reseed real documents. Retain Task/Long and their support boundaries.

Compare three explicit capability classes: basic text/undo; ordinary rich text;
local-durable and collaborative configurations where supported. Pin a truly basic
Tiptap extension list as well as the existing StarterKit profile; configure both
editors competently. The [official Tiptap performance guide](https://tiptap.dev/docs/guides/performance)
recommends isolated components and selected-state subscriptions for React.
Keep vanilla DOM comparisons separate from React host integration; use those
recommendations only in applicable host profiles. An edit-only competitor and a
durable edit.ac editor are useful product-cost observations, not capability parity.
Document unavoidable CRDT/recovery/authority differences rather than removing them.

Freeze workload, hardware/browser/network conditions, numerical absolute and
relative objectives, sample/order/warmup policy and uncertainty before candidate
changes or comparison runs. Retain existing verification targets (including core
ordinary-edit and input-to-visible limits); target competitive Tiptap results
without treating architecture, technology choice or a noisy near-tie as a win.
No result-dependent threshold, cherry-picked slow competitor or universal
"faster than Tiptap" claim is acceptable.

Measure uncached navigation/import through first visible content, actual accepted
first edit and committed visible result separately. Separate transfer,
decode/compile/instantiate, start-function decompression if selected, document
admission/restore and DOM work. Include first use of each command-lazy extension,
not just initial bytes. Distinguish no cache, HTTP cache and existing initialized
module/compiled-Wasm reuse; service-worker cache is a separate named condition.
No-editor host routes should request no editor artifacts where the host permits
that behavior. Shell rendering is read-only until real readiness; no lost or
untracked input is accepted during activation.

Measure real browser input to committed visible text plus command-to-layout
attribution, selection/formatting, undo, supported paste and optional first-use
stalls. Synthetic browser input is not an IME/native-device qualification claim.
Measure 1/10/50 mounted small editors and destroy/reopen cycles with retained and
peak memory, observer/timer/provider counts, unrelated-extension work and shared
resource unions. Freeze envelope and resource limits before runs. Required lazy
assets remain counted; caches, offscreen mounts and deferral do not erase costs.

Existing comparison summaries require at least 100 independent samples for p95
and 1,000 for p99; retain those fail-closed thresholds. Do not turn a quick smoke
into tail qualification. Run bounded cells with current applicable proof; split
long remaining matrices through the controller rather than rerun unchanged cells.
Record slower/inconclusive outcomes, quantified gaps and the responsible measured
cost. Candidate hot-path repairs stay within the same optimization allowance;
final measurement is not a new license for repeated tuning. Missing competitive
targets require explicit scope/architecture decisions and honest reporting, not
silent semantic downgrades or target relaxation.

## Delivery ownership

- WEX-1.2 freezes tiny-editor capability/latency objectives with existing REL/FIT
  owners; WEX-1.4 and WEX-2.2 incorporate host/dependency readiness boundaries.
- WEX-2.7 audits and, within the shared optimization allowance, repairs a measured
  small-edit fixed cost over current direct ports, subscriptions and patch paths.
- WEX-3.1 records wasm-squeeze/Component Model applicability before selecting any
  compressor experiment; WEX-3.2/3.3 own selected safe production changes.
- WEX-5.1–5.3 extend the existing comparator after functionality, collect the tiny
  editor startup/input/resource cells and report competitive gaps. WEX-4.3 binds
  that proof to REL-1.2–1.4/FIT/QPF, with no duplicate harness or public claims.

No absolute Tiptap advantage or edit.ac loss is asserted by this source review.
No paid inference, provider credentials, external provisioning or publication is
authorized. User confirmation, 2026-10-28: the expanded app ceiling is 1 MiB
(1,048,576 bytes) total gzip including JS/glue/Wasm/CSS/required assets and required
lazy code. Core limits remain 512 KiB total/32 KiB JS gzip; runtime gates await
the planned contract/inventory implementation, not another unit clarification.
