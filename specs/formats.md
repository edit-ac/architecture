# Import, export and Markdown contract

Status: development contract; parser conformance and schema qualification are implementation gates.
Scope: semantic interchange and clipboard behavior for the initial web editor.
The Rust implementation must remain reusable by future native adapters.

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
Do not split input into independent paragraph parses: references and block structure cross paragraph boundaries.
Maintain source ranges for diagnostics when the parser exposes them.
Unsupported constructs must retain recoverable source and report an actionable diagnostic.
Unknown atoms/marks retain namespaced type/version and validated data even without a renderer.
No Markdown export may silently erase unknown content to make a round-trip assertion pass.
Validate target schema and resource limits before committing any prepared import.

## Clipboard precedence

1. A valid supported edit-ac fragment with declared schema/version.
2. Explicit Markdown clipboard flavor or the user's paste-as-Markdown action.
3. Sanitized rich HTML admitted through the semantic importer.
4. Plain text processed under the host's declared Markdown-paste policy.

Malformed internal fragments fall back to the next safe available flavor with diagnostics.
An unsupported fragment version is not reinterpreted as a current internal structure.
The task-editor preset formats plain-text Markdown by default.
A minimal host chooses and documents its plain-text policy during configuration.
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

## Export and representability

Markdown export is deterministic semantic serialization, not recovery of the author's original spelling.
Specify escaping, fence length, list indentation, line endings and trailing newline once in fixtures.
Keep text/marks/nesting meaning and code whitespace stable through supported semantic round trips.
Underline has no standard CommonMark syntax; choose a declared safe HTML extension or explicit diagnostic/fallback.
For unsupported atoms, preserve an agreed text/source fallback and return diagnostics alongside output.
Do not claim a fallback exports an editable table, native math rendering or full-fidelity unknown content.
Versioned JSON export preserves semantic types/data without pretending to be collaborative history.
HTML export emits only the declared safe semantic vocabulary with escaped text/attributes.
Export requires an explicit request and never runs on each keystroke or save notification.

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
