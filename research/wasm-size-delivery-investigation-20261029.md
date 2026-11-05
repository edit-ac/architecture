# Wasm and package size investigation — 29 October 2026

The largest opportunities are removing unused highlighting data, removing document
restoration from the Markdown companion, fixing the effective production LTO
configuration, and reducing code retained across the browser/extension boundary.
Shipping test fixtures separately is also a substantial npm packaging opportunity.
Compiler flags and compression alone have no evidence of closing the current gaps.

This is an investigation and implementation proposal, not a new qualification
receipt. No production source, compiler setting, artifact, current roadmap,
runner, optimization allowance or acceptance cap was changed. The accompanying
[delivery roadmap](../runner-queues/wasm-size-delivery-20261029/README.md) is proposed,
unqueued work. It does not invoke or replace the excluded Deep Review tasks.

## Evidence and freshness

The latest authenticated production repair is the 29 October checkpoint in
`.roadmap-runner/wex-production-repair-20261028/`. Its
`current-matrix-facts.json`, `current-matrix-paths.json`,
`WEX-9.1-current-audit.json`, `WEX-9.1-final-artifacts.json` and
`final-owner-matrix.json` are the compact evidence references. Paths beginning
`core/` or `.roadmap-runner/` in this report are relative to the workspace root.
Generated evidence stays ignored; this authored analysis belongs in Git.

This investigation matched all five recorded Wasm artifact hashes to the current
files, including the separate fixture artifact. All 139 core-configuration and
171 expanded-configuration package input hashes matched current `dist` files;
none were missing or changed. This validates reuse of those delivered inventories,
not equivalence of every dirty source file to its build. The checkout is extensively
dirty: source changes must be bound again before future implementation. Core HEAD
was `5dfb328`; architecture HEAD was `3bf1134`. No rebuild or optimizer candidate
was executed here. Codanna was unavailable; bounded source and symbol searches
were used.

## Current budgets and measured costs

All numbers below are bytes, using the existing canonical gzip-9 accounting.
Required lazy resources count in the union. The default Task and core configuration
are distinct measured consumers; do not replace the former with the smaller one.

| Consumer / metric | Recorded size | Hard cap | Reduction needed |
| --- | ---: | ---: | ---: |
| Default Task total | 848,176 | 524,288 | 323,888 (38.2%) |
| Default Task JS | 88,936 | 32,768 | 56,168 (63.2%) |
| Core configuration total | 846,297 | 524,288 | 322,009 (38.0%) |
| Core configuration JS | 84,521 | 32,768 | 51,753 (61.2%) |
| Expanded document total | 2,865,598 | 1,048,576 | 1,817,022 (63.4%) |
| Expanded document JS | 232,510 | 131,072 | 101,438 (43.6%) |

Expanded Wasm alone costs 2,630,334 gzip bytes: highlighting 1,285,730, the
canonical engine 759,022, and Markdown 585,582. Expanded JS costs 232,510 and
CSS 2,754. The optional comparison Wasm is a separate 83,549-byte resource in
its own measured profile; it is not in this frozen expanded selection.

Even hypothetically deleting the entire highlighting Wasm would leave 1,579,868
gzip bytes, still 531,292 above the expanded total cap, with functionality missing.
The standalone engine Wasm already exceeds the entire core cap by 234,734 bytes
before JS/CSS. These arithmetic checks rule out a single small packaging fix as
the route to qualification. The current Math renderer chunk is 76,861 gzip bytes;
even deleting it entirely would leave expanded JS above its cap.

The expanded initial graph is 846,869 gzip bytes and its deferred portion is
2,018,729. Lazy loading helps first use but cannot close the required-union gap.
Core configuration Brotli is 634,244 bytes versus 846,297 gzip; that is a different
transfer representation, not a pass against the gzip contract.

The repaired build reduced the recorded expanded result from about 3,016,743 to
2,865,598 gzip bytes (151,145 fewer), while JS rose from 229,112 to 232,510. This
is a recorded inventory change, not a matched experiment attributing all savings
to one flag. The repair explicitly lacks a comparable historical compiler baseline.
It already aligned highlighting with the production profile, removed diagnostic
sections, bound grammar/notices and checked HTTP representations. Repeating these
completed repairs is not a new opportunity. The current repair reports 16 admitted
graphs/decoded representations, 6 HTTP helper cases and 30 browser scenarios.
Those passes coexist with failed size caps and incomplete performance qualification.

## Ranked implementation opportunities

### 1. Compile the admitted highlighting grammar closure

`core/crates/editac-highlighting/src/lib.rs`, `Backend::new`, calls
`two_face::syntax::extra_newlines()`. `highlight_cancellable` admits only Rust,
TypeScript and JSON. Filtering the language name at runtime does not remove the
embedded full grammar set. The final highlighting module contains 1,353,676 raw
data-section bytes and 802,906 raw code-section bytes. Earlier authenticated
grammar evidence identifies a 959,011-byte full bundle; do not equate that blob
or a section with removable gzip bytes.

Generate the three languages' complete referenced context closure plus required
fallback from pinned grammar sources at build time. Keep the same Syntect port,
newline semantics, scopes, UTF-16 offsets, limits and source-preserving fallback.
Remove the full `two-face` runtime loading edge; using it only in a build tool can
keep it out of delivered code. Commit the recipe and authenticated source inputs,
not generated binary packs. Retain all applicable notices.

This has high confidence as a data-removal mechanism; its savings and ability to
meet the 98,304-byte highlighting allocation are unknown. Regex/parser code and
transitive grammars remain. If the resulting closure is still too large, a different
backend requires its own explicit design and parity decision; a smaller language
set is not an acceptable substitute. Syntect documents linked syntax sets and
[uncompressed SyntaxSet containers](https://docs.rs/syntect/5.3.0/syntect/dumps/index.html):
their individual syntax payloads are already compressed. Double compression or
runtime filtering is not the primary fix.

### 2. Remove Markdown's document-restoration dependency

`core/crates/editac-markdown-wasm/src/lib.rs` implements
`SnapshotInput::restore` and `table_source_value`. It restores both opening and
current `Document` snapshots, captures a `SourceBaseline`, and calls native table
format/recovery logic. These read-only replicas are not second writable owners,
but the exported path retains document/restore/validation machinery in a companion
intended for codecs. `editac-markdown` also directly depends on `yrs` and core.

Keep identity, checkpoint, stale-source, target and atomic commit validation in the
existing kernel. Supply a bounded immutable table/source projection to pure codec
functions, and let the kernel validate/prepare the resulting replacement. Share
inert types/functions only where needed; a crate split without removing reachable
`Document` calls saves nothing. Preserve unknown fields, recovery, Unicode and all
current malformed/duplicate-field rejection behavior.

The Markdown module is 1,814,436 raw / 585,582 gzip bytes, including 1,547,083 raw
code bytes. This is a high-value structural target, not a promise to remove the
whole module. Measure the kernel plus codec union because moving restoration to
an already authoritative kernel may still add adapters. The material ABI proposal
remains unadopted under WEX-6.3; design/adoption must precede implementation.

### 3. Make production LTO effective before further flag tuning

`core/Cargo.toml` already declares `opt-level="z"`, `lto=true`, one codegen unit,
symbol stripping and aborting panics. All four producer crates request both
`cdylib` and `rlib`; current authenticated rustc commands have no explicit LTO
argument. The observed omission matches the documented
[mixed-crate-type issue](https://github.com/rust-lang/rust/issues/51009).

The first compiler candidate should use Cargo's `rustc --lib --crate-type cdylib`
selection for shipping producers, keeping the existing browser profile, target,
features, staging and optimizer. This is a hypothesis until the pinned compiler
actually receives LTO and a matched build passes. Preserve the rlib/native/test
policy in manifests. If selection still omits LTO, stop and report that evidence;
do not start a flag sweep or silently change the architecture.

Current post-link work already performs duplicate-function elimination, unused
element removal, vacuuming, instruction optimization and debug stripping. `-Oz`,
`-Os`, convergence, similar-function merging and alternative inlining remain
conditional candidates, not automatic additional tasks. Choose at most the next
attributed hypothesis within explicit available tuning authority. Keep import,
export, feature, raw-size and gzip-size guards plus semantic/runtime checks.

### 4. Share browser code across the prebundle boundary

`core/scripts/build-extension-runtime.mjs` bundles optional presenters separately
and externalizes core plus `presenter-sequence`. Its own comment explains why
simply re-exporting the ordinary modules previously hoisted optional code eagerly.
The expanded consumer then bundles those emitted chunks together with ordinary
`dist` imports. Comparing both retained metafiles shows these source families
emitted on both sides:

| Logical helper | Prebundle raw contribution | Direct consumer raw contribution |
| --- | ---: | ---: |
| `commands/conversions` | 5,991 | 3,434 |
| `commands/catalog` | 4,450 | 3,652 |
| `input/composition-keys` | 2,759 | 1,511 |
| `clipboard/fragment` | 2,711 | 16,876 |
| `ui/elements` | 1,877 | 1,161 |
| `ui/theme` | 1,656 | 1,391 |

These establish duplicate source retention, not identical emitted functions or
additive gzip savings. Externalize a small audited set of shared helpers to one
canonical module identity, beginning with catalog/composition helpers. Validate
that optional tables/presenters stay lazy and that stateful owners remain unique.
Broaden only for a measured retained duplication, rather than externalizing every
relative import and undoing the existing boundary.

The core graph's largest emitted inputs are keyboard (23,994 raw bytes), text
input (23,005), DOM selection (17,006), clipboard (16,887), the engine wrapper
(16,023) and DOM renderer (12,385). These are required behavior, not optional code
to delete. JS needs real consolidation of repeated dispatch/validation bodies and
feature-specific retained branches, backed by selection, IME, clipboard, keyboard
and accessibility checks. Splitting files, minifying again or changing a barrel
alone does not establish removal. Pick one demonstrated repeated family per task.

### 5. Target measured Rust duplication, not the allocator or Unicode

The current core module is predominantly code: 2,314,222 of 2,564,696 raw bytes;
its data section is 235,287 bytes. Historical WEX-1.1 diagnostic attribution found
large serialization families and preparation bodies. It also explicitly states
that diagnostic code was not byte-identical to production, and overlapping family
counts cannot be summed or treated as compressed savings.

Rebind that attribution to the post-LTO artifact before selecting a refactor.
Start with `interchange::parse<T>`, `Command::translate`, bridge preparation and
typed-to-JSON conversion roots. Share substantial repeated bodies through concrete
internal data, keeping generic conversion wrappers small. Do not replace Serde
wholesale, add a second live wire protocol or loosen field validation. The Wasm
engine already shares `output`/`error_value`; counting that change again is wrong.

URL/IDNA code is rooted by link and asset safety checks. Historical data matches
found ICU tables, but current exact retained attribution still needs rebinding.
Do not substitute a hand-written URL parser, ASCII-only checks, host-dependent
browser parsing, or remove grapheme correctness for an assumed saving. The older
allocator family was only about 7.5 KiB of diagnostic code; an allocator change is
low priority and would introduce memory/performance risk. The historical normal
core graph had no regex family; highlighting's regex costs must not be assigned
to the kernel.

### 6. Reduce npm archives independently of browser delivery

The retained `@edit-ac/core` tarball is 1,733,053 bytes compressed and 6,499,669
unpacked. Six fixture files total 2,714,508 unpacked bytes, including the
2,671,326-byte fixture Wasm. `package.json` exports the fixture and includes all
of `dist`, so deleting it would break a declared entry point.

Propose a dedicated development/test-support package or an explicitly adopted
development-only distribution, migrate fixture consumers, then narrow the shipping
allowlist. Retain declarations, comparison assets, licenses and all supported
production exports. An actual paired `npm pack` is needed to establish compressed
savings; tar compression is not additive. This can remove about 2.71 MB of known
fixture files from the core package without claiming any browser-cap improvement.

`@edit-ac/web` is 1,925,946 packed / 5,011,357 unpacked bytes; Markdown is 617,891
packed / 2,437,988 unpacked. The web archive includes both source-module outputs
and prebundled extension chunks; inventory their necessity before dropping either.
Core and Markdown notices are sizable (623,911 and 576,860 raw bytes), but notices
are obligations, not disposable metadata. The generator already selects a
normal/build dependency closure. Any notice deduplication needs verified coverage
and offers no browser saving unless those notices are actually requested.

## Secondary techniques and boundaries

The Math renderer currently calls a KaTeX default object with `output: 'mathml'`.
Try its existing named `renderToString` export only as an authorized, isolated
candidate. The largest Math chunk is 76,861 gzip bytes, but registrations and HTML
builders may remain reachable; do not promise a full MathML-only build from an
import spelling change. Preserve trust restrictions, annotations, macro bounds,
escaping and error behavior. A fork/replacement requires a separate decision.

Keep HTTP gzip/Brotli precompression, immutable content addressing and shared
resource caching: they are already implemented and checked. Report startup and
site union separately. Zopfli/Brotli quality changes, worker deferral, streaming
instantiation and cache hits can improve transfer/latency without reducing the
canonical gzip code union. Custom compressed-Wasm loaders must include their own
decoder and CSP/MIME/streaming costs; they are not justified ahead of removing
unneeded code and data. Dynamic linking/component splitting cannot freely share
Rust-owned handles across memories and can duplicate the runtime. Keep one
canonical semantic kernel, with immutable optional-service inputs.

The active handoff reports zero authorized candidate seconds. This request
authorizes the investigation and roadmap, not renewed tuning, API adoption or
runner dispatch. The proposed sequence separates these gates, uses the existing
WEX owners, preserves every original failure, and leaves unmet caps unresolved.

## Verification performed for this investigation

Read-only checks: 5/5 recorded Wasm hashes matched; 139/139 core and 171/171
expanded package input hashes matched; three retained package archives inspected;
both consumer and extension-prebundle graphs cross-checked against current source.
No compiler candidates, runtime tests, paid inference, native checks or browser
sessions were run. Historical runtime passes are attributed to their original
repair, not to this investigation. New savings remain unmeasured.
