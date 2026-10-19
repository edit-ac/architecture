# Local document import and export extensions

Status: planned capability contract. Format names below are targets, not claims
that the current scaffold imports or exports them.

Conversion is explicit and local. Optional Rust format adapters produce a bounded
prepared semantic batch or an output artifact from a fixed document revision.
They consume the [base formats](formats.md), [shared client](client-contracts.md),
[extension library](extension-library.md) and [rich-content/attachment](rich-content-extensions.md)
contracts. They never become another writable document or a replacement for CRDT
checkpoints, history, encryption policy or host authorization.

## Direction and fidelity profiles

Every capability record includes format/version, direction, enabled feature set,
tested target, input limits, fidelity tier, diagnostics and required optional
dependencies. `import` and `export` are independent claims. A recognizer or text
extractor must not advertise full document editing or round-trip fidelity.

| Profile | Import | Export | Qualified fidelity boundary |
|---|---|---|---|
| Existing baseline | Markdown, safe HTML, UTF-8 text, versioned semantic JSON | Same named formats | Existing semantic/source rules; snapshots do not retain collaborative history |
| DOCX | Supported paragraphs/runs/styles, lists, bounded tables and admitted media | Supported editor semantics and embedded admitted assets | Semantic subset; no Word pagination, arbitrary style/theme or package-byte round-trip promise |
| PDF publication | Rejected: export-only | Paginated PDF with selectable/shaped text, admitted assets, links and semantic tags where qualified | Visual publication artifact; generated output is not the original authoring source |
| ODT | Supported text/marks/lists/tables/assets | Same declared semantic subset | Unsupported styles, fields, layouts and encrypted packages are explicit |
| RTF | Bounded supported text/format/table subset | Same declared semantic subset | Code-page/control-word policy; no OLE, embedded application or arbitrary layout fidelity |
| EPUB | Ordered supported chapters and sanitized content/assets | Reflowable publication with navigation/metadata | No scripts, remote-resource fetch, fixed-layout or DRM fidelity claim |
| CSV/TSV | One bounded table using an explicit dialect | One chosen table using an explicit dialect | Cell text only; no workbook, formula evaluation, rich marks or type-inference claim |

Legacy binary DOC/PPT/XLS, presentation/workbook fidelity, arbitrary Office
macros, PDF forms/signatures, fixed-layout EPUB and unrestricted converter support
are outside the initial qualified profile. A future isolated local converter may
add individually tested capabilities. No generic “all formats” promise or silent
cloud fallback is permitted. Unsupported content yields an actionable report and
retains the original input under host retention policy; discarding it requires an
explicit lossy action.

## Adapter and execution boundary

Keep the minimum engine/WASM bundle unchanged. A lightweight capability registry
and prepared-batch contract may be shared; ZIP/XML codecs, layout engines, PDF
libraries and fonts load only through optional worker/native
conversion subsystems. Format feature flags, browser assets and native dependencies
are independently measurable. The app advertises unavailable adapters honestly;
opening a private file never uploads it or downloads document-selected code/fonts.

A conversion request fixes input identity/hash, direction/profile, resource
budget, output representation and relative insertion target or export revision.
Preparation cannot mutate the live replica. On import, revalidate target/capability
and commit through the shared session API once; cancellation, stale anchors,
rejected diagnostics and failed asset preparation leave the live document intact.
Export works from the captured revision and labels it; later edits cannot produce
a mixed-revision artifact. Re-import creates an explicit new session or prepared
insertion, never silently overwrites live CRDT identity/history.

Use the attachment service for staged embedded assets, hashes, authorization,
encryption and cleanup. A failed import removes only its uncommitted temporary
assets. Remote relationships, images, templates, fonts and hyperlinks remain
unfetched unless a separate explicit host-authorized operation allows access.
Password-protected inputs return a typed locked/unsupported result; any supported
unlock uses an explicitly provided secret held outside logs, URIs and documents.

Browser workers and isolated native jobs have bounded input/output bytes, active
jobs, wall time, memory where enforceable, decoded pixels, pages/nodes and nesting.
Cancellation disposes the worker/job and staged buffers. Native converters receive
only approved input/assets and output destinations, with no arbitrary filesystem
or network access. A missing required isolation/resource capability is a typed
unavailable profile, not permission to run unrestricted. Platform-specific wiring
and native/TUI integration belong to roadmaps 31–36; final ecosystem qualification belongs to roadmap 37.

## Hostile containers and documents

DOCX/ODT/EPUB ingestion validates signatures, package part names, relationships
and declared types before mapping content. Bound entry count, per-entry and total
**actual decompressed** bytes, compression ratio, XML depth/attributes/text and
decoded media dimensions; archive headers alone do not establish safe size.
Reject traversal, absolute/duplicate/conflicting paths, unexpected encryption and
symlink extraction. Prefer bounded in-memory part access; do not extract arbitrary
archive paths. Reject DTD/external-entity resolution, malformed encodings and
unapproved nested packages. Never execute macros, OLE objects, active content or
HTML import fragments from a document. Unsupported features have diagnostics.

PDF is export-only by user decision. Every PDF import request returns a clear
`FORMAT_EXPORT_ONLY` result before any converter, page renderer or semantic
mutation; filename, MIME and bounded content-signature checks must not route a
PDF renamed as another format into an importer. Do not add PDF text extraction,
tagged-PDF import or scanned-document recognition as a fallback. Generic file
attachment behavior, if supported by the host, remains separate from editable
content import.

PDF export jobs receive captured semantic content and authorized local assets,
not a source PDF. Bound layout time, pages, fonts, decoded images and output
allocation. Escape text and use trusted layouts rather than evaluating
user-supplied templates/scripts. Font/resource lookup is allowlisted; no
arbitrary filesystem or external fetch is permitted. Signatures/authenticity of
an imported authoring document are not transferred to a newly generated PDF.

CSV/TSV ingestion specifies delimiter, quote/escape, encoding, line endings and
ragged-row policy; it never executes formulas. Export discloses text/type loss and
offers an explicit spreadsheet-safe policy for formula-like cells without silently
changing the exact-data profile. EPUB content is sanitized through the existing
semantic HTML importer, not rendered as an active hidden webpage.

## Candidate and licensing gates

No candidate is approved or pinned by this document. Before adding a dependency,
verify the exact release, official API, target/toolchain support, license and
transitive/native/font/data notices, feature flags, known security advisories,
offline operation and representative compile/resource results. Record rejected
candidates. Never replace a bounded Rust adapter with a hosted conversion service.

- `docx-rs` is a Rust/WASM read/write candidate with MIT licensing and explicitly
  non-exhaustive OOXML support. Its default image previews decode/re-encode images;
  disable them when original admitted bytes suffice. These are library features,
  not proof of edit.ac fidelity. [Official repository](https://github.com/bokuweb/docx-rs)
- PDF export needs a layout engine or a deliberately limited layout policy.
  `krilla` is MIT/Apache-2.0 and offers PDF graphics/text/tagging primitives but
  explicitly excludes document layout, tables and pagination. Typst is an
  Apache-2.0 typesetting candidate; its PDF exporter supports tagging and declared
  conformance modes. Preserve semantic input and validate actual outputs rather
  than inferring PDF/UA compliance from the library choice.
  [krilla](https://github.com/LaurenzV/krilla), [Typst licensing](https://github.com/typst/typst/blob/main/Cargo.toml),
  [Typst PDF export](https://typst.app/docs/reference/pdf/)

## Qualification and truthful output

Hand-authored fixtures cover semantic content, unknown features, Unicode/shaping,
styles/tables/assets, malformed inputs, container bombs, cancellation and recovery.
Import acceptance compares supported semantic projections and complete diagnostics;
export acceptance uses independent readers and rendered-page inspection where
layout matters. ZIP/PDF byte identity is not a semantic round-trip oracle. PDF validation concerns generated artifacts only; it does not add a PDF import feature.

Measure complete cold/warm conversion: optional asset transfer/loading, inflate,
parse, mapping, font/image work, prepared-batch commit, peak memory and output size.
Keep imports off the edit hot path; never run export on each keystroke. Report
measured limits per target and preserve failed/skipped cases. Native adapter wiring,
real viewer/OS checks and release support claims remain gated by the platform tracks 31–36 and final qualification in roadmap 37.
Local prepared fixtures and mocked host transports suffice for automated checks;
private user documents, live credentials and paid models are not test fixtures.

### Logical export names and browser downloads

The prepared export artifact retains the requested logical filename exactly,
including its Unicode code units. The browser adapter passes that exact name to
`File`, the save picker and the download anchor; it must not strip accents,
normalize the logical name or change converter bytes. Browser download metadata
is a separate boundary: `suggestedFilename()` may use a canonically equivalent
Unicode spelling (NFC/NFD), as observed in WebKit. Compare canonical NFC forms
only at that boundary, while checking the logical artifact and anchor name
independently and exactly. Compatibility normalization, accent removal, case
folding, extension changes and arbitrary substitutions are not equivalent.
ASCII suggested names remain exact. Downloaded bytes remain exact for all names.
These checks establish a browser download request and received bytes, not a
claim about the final OS destination or actual device delivery. The baseline
`MWX-C22-download` and installed-worker `MFA-1.1-worker-export-*` cases share this
contract; neither browser spelling nor a successful request changes export
revision, retained artifact or save/share completion semantics.

## Failure and fidelity qualification refinements

[WCF-03/WCF-05–WCF-07/WCF-09–WCF-14](../tests/wordcraft-regression-cases.md) strengthen existing CNV owners. Cumulative budgets include nested parser work and repeated resource references. Check remaining allowance before decode/allocation; deduplicate expensive failed attempts within the immutable input/resource/profile job. Changed eligible jobs must not inherit stale failures. Duplicate or normalized-alias parts and corrupt required entries cannot become last-entry-wins or log-only omissions. Validate adapter span arithmetic and Unicode boundaries before preparing edits.

Output limits never silently truncate a supposedly complete artifact. Unsupported direction/structure and loss are visible through the existing capability/diagnostic contract with original-input retention. Host Save-before-New/Open waits for a correlated output completion; cancellation/write/close failure preserves recoverable state, and revision N completion cannot mark N+1 clean. Export completion remains distinct from journal durability. Platform wiring owners reuse these prepared host cases at their existing integration boundaries.

Build minimal original ZIP/XML fixtures for supported semantics and unsupported wrappers/defaults/list/relationship cases. Compare semantic projections and complete diagnostics through independent package inspection; do not extend the profile to TOC editing, arbitrary opaque-package preservation or legacy DOC. Pin font files/hashes and allowlisted fallback environments. Generated PDF checks independently assess logical text/reading order and visual placement, including Arabic lam-alef/zero-advance glyphs, clipping and multipage breaks; perturbations must fail the relevant oracle. Keep external validation tooling outside runtime dependencies and preserve the export-only PDF policy. No imported Wordcraft code, assets or new converter dependency is approved by these scenarios.

## Format references

[ECMA-376 OOXML](https://ecma-international.org/publications-and-standards/standards/ecma-376/)
defines the DOCX package vocabulary; [ZIP path-safety API](https://docs.rs/zip/latest/zip/read/struct.ZipFile.html#method.enclosed_name)
documents why archive names cannot be written directly. PDF output tagging and
accessibility must be checked against generated content and its declared
semantics, as explained by the [Typst accessibility guide](https://typst.app/docs/guides/accessibility/).
This is an export quality requirement, not a PDF reader/import contract.

Secondary adapters name their supported subsets against
[OpenDocument 1.3 packages](https://docs.oasis-open.org/office/OpenDocument/v1.3/OpenDocument-v1.3-part2-packages.html),
[EPUB 3.3](https://www.w3.org/TR/epub-33/) and
[CSV RFC 4180](https://www.rfc-editor.org/info/rfc4180/).
TSV and RTF dialect/encoding behavior must be explicitly pinned by their adapter
selection tasks; a filename extension is not a complete format contract.
