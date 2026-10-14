# Import, export and Markdown contract

Status: development contract; parser conformance and schema qualification are implementation gates.
Scope: semantic interchange, browser clipboard behavior and the [CLI's Markdown editing representation](cli.md).
The Rust implementation must remain reusable by CLI and future native adapters.

## Optional Markdown capability

The user approved making Markdown a first-party optional extension on 2026-10-13. The grammar and fidelity requirements below remain mandatory when Markdown is enabled. The default browser Task preset does not include or automatically load the parser, Markdown paste processing, export/import helpers or typing shortcuts. A host explicitly registers the Markdown extension before using those operations; built-in rich-text editing, storage, collaboration and default internal-fragment/safe-HTML/plain clipboard handling remain available without it. CLI Markdown editing and Markdown-enabled native/browser consumers explicitly include the shared portable implementation. Existing roadmap-05 evidence qualifies the enabled feature, not its presence in every default bundle.

Missing Markdown operations expose a recoverable unsupported-capability result and preserve source data. With the extension absent, ordinary text including Markdown syntax is pasted literally and typing shortcuts cannot reinterpret it. An explicit Markdown clipboard/action without the capability preserves source and reports the unavailable codec rather than silently claiming formatted import; safe existing fallback flavors remain usable. Enabling the extension restores the qualified Markdown paste, shortcuts, import/export, stable-anchor, one-transaction history, diagnostics and preservation behavior. This profile change does not authorize a new document format, schema migration or second writable replica.

## Supported profile

The base grammar is CommonMark 0.31.2.
Name the extension profile `edit-ac-gfm-v1`; do not claim all GitHub behavior without evidence.
Its required extensions are task lists, strikethrough, basic rectangular tables and extended autolinks.
CommonMark links, images, fenced code and reference links belong to the declared base behavior.
The published GFM specification is version 0.29-gfm; record differences from the newer base grammar.
Pin official fixture versions and report pass/fail/unsupported outcomes per construct.
Document disabled syntax explicitly; optional math/reference syntax must not silently alter ordinary Markdown.
Raw HTML syntax is recognized as input but admitted only through the safe semantic import policy.
The parser does not define a plugin marketplace or execute document-supplied code.

## Parser qualification gate

Start with pulldown-cmark 0.13.4 as the candidate event parser.
Consume parse events into a prepared semantic batch; do not generate HTML just to parse it again.
Enable only the declared extension flags.
`ENABLE_GFM` is not a full-conformance switch: its documented feature is GitHub callout tags.
Qualify extended autolinks explicitly, including URL/email boundaries, punctuation and code exclusions.
The parser spike must compare actual fixture output to the complete required profile.
If a required feature fails, either add a bounded qualified extension or select another parser through an ADR.
Do not quietly rename missing syntax as supported or accept silent plain-text conversion.
Record whole-pipeline bytes, preparation time and memory, not parser throughput alone.
Parser selection blocks production Markdown import/export work, while fixture authoring can proceed independently.

## Semantic mapping

Map paragraphs, headings, marks, links, breaks, separators, lists, quotes and code to shared schema primitives.
Preserve code whitespace, list nesting/order, checked state, link destinations and alt text.
Map images/tables only through registered portable descriptors with explicit fallback behavior.
The v1 optional content descriptors use existing opaque block tuples, tagged
`module:editac.image` or `module:editac.table`, followed by version 1 and bounded
JSON data. This does not change profile roots or the v5 wire schema. Known
descriptors validate before staging; disabled/unknown descriptors retain source
and inert text. Images retain URL/alt/title/source without a network request.
Tables retain alignment, rectangular rows and rich simple-cell runs (32 columns,
128 rows, 1,024 runs, 1 MiB text/source). Inline image layout and nested cell
containers remain explicit unsupported source fallbacks. Registration governs
activation; rendering/upload services remain separately owned.

The separately admitted table v2 tuple keeps the same `module:editac.table` tag
and opaque v5 envelope, with version 2 and exact `alignments`, `rows`, `source`
keys. Rectangular rows contain cell records or null covered positions. Each cell
has `paragraphs`, positive integral `rowSpan`/`columnSpan`, and boolean `header`.
A paragraph has exact `style` and `runs` keys: styles are `["paragraph"]`,
`["heading", 1..6]`, or `["code", language]` using the existing language bounds;
runs use the qualified v1 table encoding and single-line text/mark/link policy.
Spans must tile the rectangle without overlap or out-of-bounds cells; covered
positions are explicitly null. Aggregate bounds stay 32 columns, 128 rows,
1,024 paragraphs/runs and 1 MiB text/source. Unknown keys/styles reject.
V1 is unchanged; no registration rewrite or automatic v1/v2 migration occurs.
V2 rich rendering/editing is optional and current v1 presenters fall back.
Portable structured copy/cut/paste retains the exact tuple atomically. Markdown
cannot express all v2 metadata: export reports `rich-table-source-fallback`,
returns inert source and retains the complete typed recovery fragment. Reimport
of that source alone is not a lossless v2 round trip.

Unknown/unavailable extension data uses the owning v1
`module:editac.inert-extension` carrier in the same opaque envelope. It stores
exact transfer `version`, `type`, `dataVersion`, `source`, `payload`; the wrapped
type/version is never interpreted or activated. The [extension library
contract](extension-library.md#ordinary-bounded-inert-extension-transfer) defines
JSON shape, 1 MiB/65,536-value/depth-16 bounds and unsafe-value/key rejection.
Fallback runs equal source and have no marks. Ordinary structured transfer,
whole-atom cut, history and checkpoint reopen retain the complete envelope without
codecs/presenters. Partial source editing rejects; literal paste deliberately
uses text only. Markdown export escapes active source syntax, reports
`inert-extension-source-fallback` and retains typed recovery; source-only reimport
cannot recover arbitrary payloads. No code/formula execution or resource fetch
is authorized by carrier admission.

Prepared paste adds an editable cut around edge atoms so preceding/following
destination text retains its original ownership and presentation. Those cuts,
descriptor installation and resulting caret belong to the same prepared update.
Do not split input into independent paragraph parses: references and block structure cross paragraph boundaries.
Maintain source ranges for diagnostics when the parser exposes them.
Unsupported constructs must retain recoverable source and report an actionable diagnostic.
Unknown atoms/marks retain namespaced type/version and validated data even without a renderer.
No Markdown export may silently erase unknown content to make a round-trip assertion pass.
Validate target schema and resource limits before committing any prepared import.

The portable import result retains the exact input source, byte ranges and
diagnostics alongside prepared fragments. Links reuse the core's public
`normalize_link_url` admission policy (absolute HTTP(S)/mailto; no credentials,
encoded controls or executable schemes). Grammar recognition alone does not
admit a URL. Unsupported link titles/destinations, raw HTML and disabled optional
content retain original source and report loss rather than executing or fetching.
Fragment limits remain 128 blocks, 1,024 runs, 16 container levels and 1 MiB of
source/text. Preparation returns no live document mutation.

## Clipboard precedence

1. A valid supported edit-ac fragment with declared schema/version.
2. Explicit Markdown clipboard flavor or the user's paste-as-Markdown action.
3. Sanitized rich HTML admitted through the semantic importer.
4. Plain text processed under the host's declared Markdown-paste policy.

Malformed internal fragments fall back to the next safe available flavor with diagnostics.
An unsupported fragment version is not reinterpreted as a current internal structure.
The task-editor preset pastes plain text literally by default. A host that explicitly registers the Markdown extension may configure its documented Markdown-paste policy; the extension-enabled Task configuration formats plain-text Markdown under that policy.
Every host chooses and documents its enabled codecs and plain-text policy during configuration.
Provide an accessible literal/plain-text paste command; do not rely on undocumented heuristics or AI.
Pasting into a code block or inline-code editing context is literal under the declared target policy.
Only user paste/import actions parse Markdown; remote structured updates are never reparsed.

## Transaction and asynchronous paste behavior

Capture clipboard data and selection once; sanitize/parse/validate outside live mutation.
For ordinary pastes, commit one prepared semantic operation before showing the formatted result.
Insert-raw-then-reformat is not the ordinary paste implementation.
Add explicit history boundaries so one undo removes the complete paste and one redo restores it.
For oversized preparation, retain source data, stable target anchors and a cancellation token.
Record the initiating document/session; results cannot cross into a replaced editor/document.
Revalidate current target and schema before commit; stale/deleted targets produce a recoverable result.
Cancellation creates no content/history/persistence update.
Asynchronous completion must preserve the user's subsequent selection unless policy explicitly follows insertion.
Measure preparation, transfer and main-thread application separately; a worker does not make application free.

Deferred paste is an explicit host action (`ClipboardInput.pasteDeferred`), with a cancelable status control and retained flavor data. It yields preparation scheduling without claiming worker offload. Each flavor is captured once, with per-flavor 1 MiB limits. Completion revalidates both endpoint owners and their parents, current anchors and schema; moved/deleted targets reject with retained source. Current user selection is restored after apply. Timings separate preparation and apply; no automatic size threshold is claimed before measurement.

## HTML and URL safety

Use an allowlisted HTML-to-semantics importer distinct from Markdown parsing.
Drop executable elements/attributes and report unsupported content using safe source/text fallbacks.
Never admit script, event-handler attributes, embedded browsing contexts or executable URL schemes.
Validate link/image URLs after decoding and normalization; escaping output is not URL validation.
Specify permitted URL schemes and relative-URL resolution in the importer configuration/schema.
Images do not upload or fetch automatically during parsing; loading policy belongs to the host renderer.
Do not insert source HTML directly into the live document or hidden active page as an import shortcut.
Bound bytes, nesting, attribute lengths, table dimensions and prepared node count before commit.
Test malformed encodings, nested tags, misleading MIME flavors and adversarial link/image values.
Untrusted internal fragments follow the same safety/resource checks as external formats.

The baseline HTML adapter admits absolute HTTP(S)/mailto destinations only; relative URLs, credentials and encoded controls become inert text with diagnostics. Styles are reduced to the named text marks; no CSS enters the live tree. Inert template parsing is capped at 1 MiB, 4,096 visits, depth 32, 128 blocks, 1,024 text runs and 4,096 characters per attribute. Dropped content retains exact source in bounded clipboard recovery. Optional resource elements require explicit codecs.

## Export and representability

Markdown export is deterministic semantic serialization, not recovery of the author's original spelling.
Specify escaping, fence length, list indentation, line endings and trailing newline once in fixtures.
Keep text/marks/nesting meaning and code whitespace stable through supported semantic round trips.
The deterministic serializer uses LF, a trailing newline, escaped punctuation,
bounded backtick delimiters and indentation derived from container markers.
It checks representability through the shared importer. Unrepresentable mark
boundaries or code whitespace return diagnostics and the original typed content
as recovery data; they must never be reported as lossless exports.
Underline has no standard CommonMark syntax; choose a declared safe HTML extension or explicit diagnostic/fallback.
For unsupported atoms, preserve an agreed text/source fallback and return diagnostics alongside output.
Do not claim a fallback exports an editable table, native math rendering or full-fidelity unknown content.
Versioned JSON export preserves semantic types/data without pretending to be collaborative history.
HTML export emits only the declared safe semantic vocabulary with escaped text/attributes.
Export requires an explicit request and never runs on each keystroke or save notification.

CLI source editing retains an exact source baseline and prepares semantic changes through the shared engine. Unchanged source must not be normalized or rewritten. Hosted document edits preserve unchanged semantic identities, anchors and unsupported data; replacing the document with a fresh Markdown import is not an editing/synchronization strategy. See the [CLI contract](cli.md) for source preservation, concurrent edit conflicts and literal-text mode. This does not change the deterministic semantic export contract or make Markdown a CRDT checkpoint.

## CRDT persistence and migration

Yjs/Yrs binary updates and checkpoints are the live collaborative persistence format.
JSON/Markdown/HTML snapshots are interchange content, not substitutes for CRDT identity/history.
Importing a snapshot into a fresh replica creates a new explicit session/epoch.
Do not merge stale offline updates from the old identity space into the new session.
Tiptap JSON migration covers a named supported node/mark set with fixture-by-fixture reporting.
Do not claim ProseMirror/Tiptap collaborative schema or plugin compatibility.
Migration preserves original input and emits diagnostics for every unsupported construct.
Existing documents are restored once; network delay must not cause repeated initialization/import.
A future container format is outside this release and must not block ordinary export/recovery.

## Required qualification fixtures

- CommonMark official examples plus the named extension corpus and documented deviations.
- Nested fences, code spans, escapes, reference links, nested lists and task states.
- Extended autolinks, tables, images, raw HTML and unknown module data.
- Unicode/RTL, empty documents, long single paragraphs and deeply nested content.
- Fragment/version corruption and each clipboard precedence/fallback branch.
- Paste/undo/redo with concurrent edits and target deletion during asynchronous preparation.
- Semantic parse/export/parse stability without requiring byte-for-byte source spelling.
- Sanitization/resource limits, rejected commands and canceled work leaving the core unchanged.
- Equivalent Rust and WASM fixture results; native bindings reuse the same corpus later.

Record failures, skips and diagnostics. Fixtures establish the supported profile; marketing names do not.

## Primary references

- [CommonMark 0.31.2](https://spec.commonmark.org/0.31.2/)
- [GFM 0.29-gfm](https://github.github.com/gfm/)
- [pulldown-cmark event parser](https://docs.rs/pulldown-cmark/latest/pulldown_cmark/)
- [pulldown-cmark option semantics](https://docs.rs/pulldown-cmark/0.13.4/pulldown_cmark/struct.Options.html)

## Optional broad-format services

[Document conversion](document-conversion.md) defines independent DOCX/ODT/RTF/EPUB/CSV/TSV import and export profiles alongside the baseline formats. PDF is **export-only** by explicit user decision; reject PDF imports, and do not add PDF-reader/OCR dependencies. Converters return bounded prepared edits or output artifacts with fidelity reports; they do not replace source reconciliation or CRDT storage.

## Interaction regression coverage

Use [editor interactions](editor-interactions.md) for literal-paste newline/whitespace policy, typing-rule eligibility and reversal, alternate formatting and clipboard command behavior. The [case catalog](../tests/editor-interaction-cases.md) separates pasted Markdown, literal text, imported HTML and local typing; INT-1.10/INT-1.11 own integrated regressions alongside the existing parser conformance fixtures. Markdown source soft breaks and CLI source preservation remain governed by this format contract, not by the browser's literal-paste presentation policy.

## Adapter integration ownership

WEB-1.9 provides atomic internal fragments, the bounded safe HTML adapter, literal/minimal-host text policy, optional reachable plain-paste control and platform plain-paste shortcuts. Full Rust CommonMark/GFM import and configurable formatted plain-text policy retain their parser qualification gates and FMT-1.13 integration owner. Registered codecs provide additional MIME/asset/extension support; RTF and image/file clipboard items require declared typed/resource-bounded adapters rather than pretending binary items are text. EXT-1.13 and RCH-1.23 own formatting-preserving table cells, captions and other extension payloads, with native and mobile presenter tasks and separate actual-device gates. The supported palette is the admitted model/codec capability set; unavailable formats retain inert source with diagnostics. Literal paste retains destination formatting but never imports source formatting or parses Markdown/HTML.

### Portable WASM Markdown adapters

`EngineHandle.importMarkdown(source, {images?, tables?})` prepares inert whole-document fragments, exact source, byte ranges and diagnostics without a document update. `exportMarkdown(blocks)` returns deterministic source, diagnostics and typed recovery. Both use the pinned portable Rust profile and are disposed with the engine. Unknown fields and resource excess are rejected at the bridge. Registered content tuples and separators share the fragment transfer boundary.

Normal task surfaces default plain text to Markdown; `preset: "minimal"` defaults to literal text. `plainTextPolicy` explicitly overrides the preset. Named Markdown flavors use the portable parser. Code blocks, inline code and explicit plain paste stay literal. Internal fragment, Markdown, HTML, custom codec, and plain text routing retains bounded diagnostics/source recovery and commits one prepared batch.

### Markdown extensions

Portable `extensions::Extension` defines stable names and ordered semantic import hooks over `PreparedContent`, with optional serializers. `extensions::import` always runs the qualified whole-document parser first. Extension outputs use the existing bounded fragment and registered content admission; errors leave the source available to the caller and never open a document transaction. Custom serializers are reparsed with the same hooks and compared semantically; unrepresentable output returns diagnostics and typed recovery.

`MarkdownOptions` exposes `images`, `tables`, `callouts` and ordered `extensions`. Each trusted host extension has a stable unique name and optional pure `prepare(content)` / `serialize(blocks)` callbacks. The WASM wrapper transports only data, validates callback output natively and uses the portable semantic comparator. No function is serialized across the bridge. A hook may recognize custom block syntax or transform existing semantics; its source remains exact, and changed whole-document mappings use explicit full-source ranges. Arbitrary unknown module tuples cannot bypass registration.

GitHub callouts (`NOTE`, `TIP`, `IMPORTANT`, `WARNING`, `CAUTION`) are optional v1 `module:editac.callout` descriptors with bounded kind, body Markdown and exact source. Their default view is inert fallback text, like optional images/tables; renderer extensions can present retained data. Disabled callouts remain normal quotes with a diagnostic; unknown kinds remain quotes. Nested/body structures are retained in source rather than silently claimed as editable rich module content. No upload, network load or HTML execution is implied.

### Bounded browser typing rules

The direct-key profile recognizes heading/list/checklist/quote prefixes followed by Space, fences followed by Enter or Space, and completed bold/italic/strike/code suffixes. Eligibility requires correlated trusted keydown and insertText, a collapsed caret at the current unmarked paragraph end, at most 2,048 UTF-16 units, and no composition/modifier/replacement/paste. Escape suppresses the next candidate; hosts can disable rules independently of paste parsing. Inline escapes remain literal. Conversion uses one prepared fragment and explicit history boundaries; immediate Backspace undoes that conversion to the preceding literal prefix. Undo then reverses preceding typing. No remote update triggers a rule.

### Host clipboard configuration

Both recovered `mountEditor` and borrowed-engine `mountEditorSurface` accept `preset`, `plainTextPolicy`, `contentCodecs` and `typingShortcuts`. Task defaults plain text to Markdown; minimal defaults to literal; an explicit policy overrides the preset. Named built-in MIME flavors cannot be replaced by custom codecs. Custom MIME names are unique, valid and capped at 16; validation precedes input-owner allocation. Unsupported RTF/TSV text retains source and an unavailable-codec diagnostic. Full-palette prepared event routing qualifies mechanics only; native mobile paste menus and actual OS clipboard shortcuts have a separate mandatory FMT-1.15 gate.

### Qualified portable source reconciliation

`reconcile::SourceBaseline` captures exact source, a bounded opening checkpoint and explicit ordered source-block/semantic-owner bindings. Bindings must be unique and ordered; shared parser ranges do not supply identity by themselves. Markdown uses the qualified whole-document parser; literal mode uses one literal block and never parses syntax. Exact source no-op and source-only spelling changes preserve the live replica and return the caller's exact source.

The first qualified edit profile preserves block cardinality and container topology. Text/mark/block-presentation/check-state edits on proven mappings are supported. Structural count/container changes return explicit unsupported/ambiguous conflicts, with the draft still caller-owned; they never fall back to whole-document replacement. Unknown/unsupported blocks may remain untouched but cannot be changed by this profile. Unicode text differences use scalar boundaries translated to UTF-16 anchors from the opening checkpoint. Current target ownership/relative order/style/mark context and expected deleted text are checked before staging. Disjoint remote text outside the edited range is preserved; overlap, deleted/moved targets and unsupported data changes reject.

Source deltas preserve existing glyph-source ownership; they do not create fresh clipboard fragments. All deltas stage on one isolated replica and commit through one `PreparedEditorEdit`. Commit retains the core's exact revision/checkpoint guard, so a change between prepare and commit rejects without mutation. The result keeps exact edited spelling; it is not a CRDT checkpoint or a source representation of unrelated remote changes. Hosts retain base/draft/current representations and refresh their source mapping after an accepted merge.

## Simulator/emulator development qualification

Controller decision, 2026-10-13: the user authorized "Lets unblock, emulator should do for now". A named iOS Simulator or Android Emulator running its platform browser is accepted for development clipboard qualification. This is a virtual-device result, not physical-device, real IME/accessibility or release support. Playwright mobile viewports, synthetic ClipboardEvent/InputEvent and prepared desktop event variants alone do not meet this emulator gate.

Roadmap 05 provides two qualification levels: its qualified portable FMT-1.1–FMT-1.14 behavior, including FMT-1.12, plus a passing virtual-device development receipt may unblock development tracks 08, 11, 12 and 21. FMT-1.15-V1 remains the mandatory physical-device release criterion; leave FMT-1.15 and roadmap 05 release completion open until it passes. Missing physical observations must not reblock those development tracks after the virtual gate passes. Other failed portable gates remain blockers. CAP-1.1 may execute the virtual gate as its next bounded development entry step rather than requiring a receipt before starting that step.

Use the procedure in tests/clipboard-emulator-development.md and record evidence under evidence/markdown/emulator-development/receipt.json. Require nonzero actually executed native clipboard cases, exact simulator/emulator/browser/OS versions, source/package hashes, semantic/history/storage observations, test counts, failures/skips and reproduction instructions. Missing or failed virtual cases cannot be marked passing. Retain previous physical-device BLOCKED receipts unchanged. Release/device owners later collect physical evidence against the then-current artifacts.
