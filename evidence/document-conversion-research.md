# Document conversion review — current scope, 2026-10-11

**Controlling user correction: PDF EXPORT ONLY.** Earlier exploration of PDF text/tagged import and scanned/OCR providers is superseded and is not a development recommendation. The current plan rejects PDF import with `FORMAT_EXPORT_ONLY`; it contains no PDF reader, PDFium, OCR engine or language-pack dependency.

## Coverage and deliverables

Existing FMT-1.1–1.12 cover Markdown semantics/paste/source reconciliation and safe HTML import; existing specifications also define plain text and semantic JSON interchange. They do not previously deliver DOCX, PDF publication, ODT, RTF, EPUB or CSV/TSV adapters. Existing extension/attachment/session APIs should own shared commands, resource limits and staged assets rather than recreating them in converters.

Created only these project files:

- `specs/document-conversion.md`: directional support/fidelity matrix, local/private isolation, resource/security limits, candidate gates, source-linked facts and final platform handoff.
- `roadmaps/27-document-conversion.md`: 18 bounded parents CNV-1.1 through CNV-1.18; upstream 05, 12, 21 and 25-rich-content-extensions. Roadmap31 owns final native/browser wiring, viewer qualification and release.

Current directions: baseline Markdown/HTML/TXT/semantic JSON; DOCX import and export; PDF export only; explicit ODT, RTF, EPUB and CSV/TSV table import/export. Legacy binary DOC/PPT/XLS and universal Office/workbook/presentation fidelity remain outside the qualified profile. Lossy results require diagnostics and explicit acceptance; the original input remains recoverable under host retention policy.

## Primary-source facts informing the plan

- OOXML defines package parts/relationships, not a promise that a reader preserves all Word semantics. The `docx-rs` repository describes Rust/WASM reading and writing with non-exhaustive OOXML support under MIT; default image previews decode/re-encode, so preservation/performance-sensitive jobs should disable previews where original admitted media suffices. Exact release/target/fidelity qualification is still required. [ECMA-376](https://ecma-international.org/publications-and-standards/standards/ecma-376/), [docx-rs](https://github.com/bokuweb/docx-rs)
- PDF export requires actual layout decisions. MIT/Apache-2.0 `krilla` supplies PDF graphics/text/tagging but explicitly excludes text/table layout and pagination. Apache-2.0 Typst is a typesetting candidate; its PDF exporter supports semantic tagging and declared conformance modes. Neither choice alone proves correct edit.ac output or accessibility. [krilla](https://github.com/LaurenzV/krilla), [Typst license](https://github.com/typst/typst/blob/main/Cargo.toml), [PDF export](https://typst.app/docs/reference/pdf/), [accessibility](https://typst.app/docs/guides/accessibility/)
- Archive filenames can escape output directories; the ZIP API documents safe-path validation. Path checks are only one layer: the proposed adapter also bounds actual inflation, entry count, XML/media expansion, active relationships and staging. [ZIP path safety](https://docs.rs/zip/latest/zip/read/struct.ZipFile.html#method.enclosed_name)
- Secondary formats have distinct package/dialect contracts. EPUB can contain scripted/remote content, so the chosen import/export subset explicitly excludes execution and implicit fetch. CSV support is table text exchange, not a spreadsheet engine; TSV dialect and RTF encoding/control handling must be pinned separately. [ODF 1.3 packages](https://docs.oasis-open.org/office/OpenDocument/v1.3/OpenDocument-v1.3-part2-packages.html), [EPUB 3.3](https://www.w3.org/TR/epub-33/), [CSV RFC 4180](https://www.rfc-editor.org/info/rfc4180/)

## Task split and evidence

Four initial parents establish profiles/dispatcher, bounded jobs, dependency qualification and archive/XML/media protection. Three deliver DOCX content/structure import and export. Two select/qualify PDF export. Eight separately implement ODT, RTF, EPUB and CSV/TSV table directions. One final consumer/profile handoff records dependency/assets, exact support and measured costs.

Optional converter/font dependencies remain outside the minimum editor/WASM; work is local with no private-document upload or hosted fallback. Inputs cannot execute macros, entities, OLE objects, EPUB scripts or arbitrary filesystem/network requests. Exports use fixed revisions and imports prepare before one revalidated semantic commit. Output fidelity is checked with independent readers/rendered artifacts and complete diagnostics, rather than same-library round trips or ZIP/PDF byte equality.

The official local Roadmap Runner 0.8.0 `validateRoadmap()` accepted the new 18-parent source with zero errors. This verifies structural task/dependency compatibility only; no adapter implementation, package installation, document conversion, model inference or release qualification ran.
