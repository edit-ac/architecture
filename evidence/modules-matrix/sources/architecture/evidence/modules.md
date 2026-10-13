# Optional module capabilities and production footprint

This is MOD-1.9 evidence for source revision `621cbff280187a584cd0ceb5b9ac66d176b916c16f99ba34a48e6fd74c08c294`. The packages remain private scaffolds. This record does not publish a package or qualify a release.

The browser results use packed production WASM/Yrs, DOM/input/selection, IndexedDB recovery and prepared peers or host transports. Chromium, Firefox and WebKit mechanical checks pass for the cases linked below. Native controls in these browser fixtures are DOM controls; they do not establish UIKit, Android or desktop native editor support. Physical-device, OS clipboard, IME and assistive technology qualification remains with the owning interaction/device roadmaps. Roadmap 05 is the user-instructed baseline with FMT-1.15 actual-device qualification unclaimed; roadmap 06 is the recorded completed upstream baseline.

## Capability matrix

“Qualified” below means the bounded fixture behavior, not catalog-scale support. “Unqualified” advertises no support for that operation. Every qualified cell maps to passing cases in [the machine-readable capability ledger](modules-matrix/capabilities.json); its hashed three-engine receipts are checked by `tests/module-bundles.test.mjs`.

| Module | Browser read/render | Browser edit | Browser copy | Markdown/export | Disabled presenter |
|---|---|---|---|---|---|
| Slash | Qualified named menu and literal query | Qualified local eligible trigger, registered engine command, keyboard/pointer choice, one history group; remote/paste/replacement exclusion and IME priority | No persisted slash content or separate copy operation | No persisted slash content or separate codec | No presenter/trigger when factory omitted; underlying document editing continues |
| References | Qualified inert host ID and label fallback; opening makes no resolver call | Qualified explicit anchored block insertion, canceled/stale response guard, keyboard choice and one history group; inline reference editing unqualified | Qualified prepared plain-label copy and internal fragment identity round-trip; OS clipboard unqualified | Label-only fallback and identity-loss diagnostic are the contract; this matrix does not qualify reference Markdown conversion | Qualified checkpoint/recovery preserves unknown identity and label without resolution |
| Reorder | Qualified named controls and feedback | Qualified keyboard/button semantic move, concurrent identity/content preservation, nested invalid-target rejection, undo/redo and selection retention | No separate move-specific copy operation | No separate reorder codec; general document-order export unqualified here | Qualified reordered data recovery with controls absent |
| Images | Qualified alt/title/source plus host-policy asset URL; absent, unsafe or failed policy stays inert | Image authoring, resizing and upload UI unqualified; uploads/auth remain host services | Qualified prepared literal source copy and keyboard selection; OS clipboard unqualified | Image Markdown conversion unqualified by this matrix | Qualified original metadata/source recovery without asset load |
| Tables | Qualified bounded rectangular table, simple cells and preserved marks | Qualified native cell controls, atomic Rust `tableCell`, exact-descriptor stale guard, composition, undo and empty cells; merged/rich/nested cells excluded | Qualified prepared cell-range plain-text copy and keyboard/Tab selection; OS clipboard unqualified | Qualified current-row Markdown update and identical export after disabled/re-enabled recovery; no merged-cell claim | Qualified exact edited tuple/fallback recovery |
| Math example | Qualified bounded LaTeX inline/display source atom; lazy pinned KaTeX 0.19.0 MathML preview, trust disabled, invalid/error source fallback | No dedicated math authoring UI; portable helper/atom preservation and peer-update handling qualified | Math-specific clipboard behavior unqualified | Math Markdown conversion unqualified by this matrix | Qualified explicit “LaTeX source” fallback and source recovery with absent/disabled renderer |

Passing proofs include slash `keyboard-history`/`provenance`, references `stale-query`/`clipboard-fallback`/`recovery-fallback`, reorder `concurrent-before`/`concurrent-after`/`invalid-descendant`/`keyboard-parity`, images `render`/`no-policy`/`image-copy`, tables `edit`/`keyboard-copy`/`disabled-recovery`, and math `renderer-safety`/`load-error`/`peer-source`. The ledger resolves each case to all three engines. Repaired clipboard and math-peer cases use their final focused receipts; failed earlier receipts remain preserved and are not counted as passing proof.

This gate reuses those original browser receipts at their recorded build revisions and verifies that their presenter source bytes still match. Its new checks execute packed bundle inspection and receipt integrity; they do not rerun browser integration or requalify the entire current release. The owning receipts retain the exact engine, adapter, fixture and packed-build provenance for each observation.

## Portable contract and platform limits

MOD-1.1–MOD-1.3 provide the shared data-only descriptor, namespace/version/shape validation, fallback, registry freeze, scoped subscriptions and stable renderer lifecycle. Their receipts are [entry](modules-entry/receipt.json), [registration](modules-registration/receipt.json) and [runtime](modules-runtime/receipt.json). Runtime's complete later registration regression is the current 15/15 browser proof; earlier repaired failures remain in their receipts. Declarative custom mark/inline atom fixtures work without a core-specific renderer branch. Unknown descriptors preserve bounded original attributes/content; executable callbacks are never document data. These are portable engine/browser contracts, not evidence of native UI integration.

| Platform | Read/fallback | Edit/copy/Markdown qualification |
|---|---|---|
| Browser engines | Above bounded mechanical fixture coverage | Only the qualified cells above; desktop WebKit is not physical Safari/mobile qualification |
| Rust / WASM semantic boundary | Data preservation, prepared validation and semantic operations in the owning module receipts | Engine command evidence only; no native text-control behavior inferred from Rust or native bridge tests |
| iOS / Android / macOS / Windows / Linux native hosts | Source/label/data fallback is the portable contract; no host view qualification claimed by this roadmap | No full native rendering, typesetting, editing, clipboard or accessibility parity claimed; native preparation and SDK roadmaps own execution evidence |

Images, tables and references retain opaque metadata with inert text fallback. Math fallback is labeled source rather than native typeset math. Storage recovery is qualified for the bounded browser fixtures; this evidence does not establish arbitrary future module compatibility.

## Production footprint method

The named check packs `@edit-ac/core` and `@edit-ac/web`, unpacks them into an isolated consumer, resolves the public package exports and bundles identical `mountEditor` baselines with pinned esbuild 0.25.12, minification, ESM splitting and browser platform. Profiles are minimal, explicit disabled, each presenter individually, and all enabled. Manifests inspect positive `bytesInOutput` contributions, since a parsed re-export with zero emitted bytes does not load optional code. The all-enabled graph supplies the positive control. Math renderer/KaTeX stay outside entry chunks behind a dynamic import; MathML mode emits no CSS or fonts.

The npm tarball contains optional code and the pinned renderer so hosts can opt in. “Absent” means absent from the shipped minimal consumer graph, not absent from the package archive. Shared descriptor/fallback/runtime plumbing can remain in baseline code. WASM is a separately loaded shared asset and is reported separately; JS totals alone are not the full editor payload. Counts use raw minified bytes and the sum of independently compressed output files with Node's default Brotli settings. They are transfer artifact measurements, not latency, memory or performance-budget qualification.

<!-- footprint:start -->
| Profile | Minified JS bytes (all chunks) | Brotli JS bytes (all chunks) | Incremental Brotli vs minimal |
|---|---:|---:|---:|
| minimal | 103,817 | 26,737 | +0 |
| disabled | 103,856 | 26,761 | +24 |
| slash | 114,748 | 29,154 | +2,417 |
| references | 111,791 | 28,436 | +1,699 |
| reorder | 109,798 | 28,038 | +1,301 |
| content | 111,014 | 28,500 | +1,763 |
| math | 374,700 | 91,643 | +64,906 |
| all | 406,783 | 98,188 | +71,451 |

Shared WASM: **3,708,331 raw / 628,006 Brotli bytes**; generated initialization glue: **25,241 raw / 3,352 Brotli bytes**. The glue and WASM are separately packed assets outside the adapter graph, not hidden in the JS total.

Math entry: **27,409 Brotli bytes**; its lazy renderer chunk: **64,234 Brotli bytes**. All-enabled entry: **33,954 Brotli bytes**, with the same lazy renderer chunk. Enabled totals include eventual lazy transfer; first-entry and total costs differ.

Minimal graph plus these common assets totals **658,095 Brotli bytes** before host application, document and other assets. This exceeds the provisional 400 KiB Task-preset JS+WASM+essential-CSS target in `specs/verification.md`; this gate neither qualifies that preset nor waives the target. Footprint/release owners must resolve that cost before a qualified payload claim.
<!-- footprint:end -->

Production manifests, hashes, packed file lists and compressed sizes are retained in [profiles](modules-matrix/bundles/profiles.json). The [delivery receipt](modules-matrix/receipt.json) records exact commands, counts, current source/build hashes and cleanup. No external resolver, model API, downloaded runtime plugin, paid inference or publication is part of this check.
