# Extension and ecosystem architecture review

Reviewed 2026-10-11. The user requested richer first-party extensions, document formats, public documentation/demo and cloud-store readiness. Their later clarification is authoritative: **PDF export only; no PDF import or OCR**.

## Outcome and task coverage

All requested features have contracts and bounded delivery tasks. Existing slash/reference/reorder/image/table work in07/21 is retained; follow-ups add missing behavior and qualification rather than parallel implementations. [Requirements](../requirements.md) provide the complete mapping. [Decision003](../decisions/003-extension-ecosystem.md) records the architecture adjustment.

The plan now has **37 roadmaps, 443 parent tasks and 1,329 checkboxes**. This adds 13 roadmap sources and 151 tasks, including two additions to the optional encrypted profile. Every parent has purpose, context, local dependencies, session scope, acceptance, implementation, validation, evidence, handoff and blocked behavior. Platform wiring is split into31–35 and terminal36 so one missing OS does not block unrelated client development.

## Corrections and improvements

- Optional `editac-highlighting` owns runtime/grammar/cache dependencies. The semantic engine keeps only small data contracts. Incremental output is checked against full recomputation, while typing/persistence never wait on highlighting.
- Tables distinguish semantic editing, cached layout and explicit Markdown source formatting. Identity, source preservation, undo, concurrent edits and invalidation costs are tested separately. Merged-cell/spreadsheet/layout-engine claims remain outside the bounded table profile.
- Assets use staged upload/finalize/cancel/retry and independent asset/document receipts. Safe embed presentation never grants arbitrary script or network authority. Slash/reorder include cancellation, touch and a non-drag pointer alternative.
- URL metadata auto mode applies under explicit host policy to local paste/refresh. Internal resolution uses principal-scoped caches, permission rechecks and no generic external-fetch fallback; private titles do not silently become shared CRDT labels.
- Conversion is local-only, optional and direction-specific: Markdown/HTML/text/semantic JSON plus DOCX, ODT, RTF, EPUB and CSV/TSV subsets, with PDF export only. Loss diagnostics and original-source recovery are mandatory. Heavy layout/font/media components stay outside minimum editor loading.
- Cloud readiness requires a real durable reference service and reusable adapter conformance. Actual production-provider claims additionally need configured-provider deployment/restore evidence. One deployable reference host is sufficient; no microservice or vendor requirement was introduced.
- A shared capability/version schema drives existing native profiles, package checks, public tables, demo controls and host negotiation. Declared feature support never grants authorization. Layer, optional-loading, compatibility, dependency/notice and redacted-diagnostic checks make the architecture enforceable.
- Resolved a semantic release cycle: EQL-1.9 publishes tested immutable prerelease artifacts; advanced DOC examples/demo consume them; EQL-1.7 verifies DOC-1.14 deployment evidence; EQL-1.8 promotes those same artifacts without rebuilding. Roadmap37 does not require29 at entry.
- Optional encrypted profile24 now qualifies the new assets, conversion, private link metadata and ciphertext cloud behavior before its final independent review.

## Public repository and milestones

Created the public Apache-2.0 [edit-ac/docs](https://github.com/edit-ac/docs) repository with 13 Markdown pages, checked navigation, integration guides, release/capability labels and dependency-free CI. Its source commit is `5672833fd6488bd430f4dc11a4c8917fac2dc76b`. [Docs CI passed](https://github.com/edit-ac/docs/actions/runs/38146145813). The static website and real editor demo remain explicit tasks in29; no placeholder demo is presented as functional. [Bootstrap evidence](public-docs-bootstrap.json) records that distinction.

Synchronized 14 GitHub milestones: eight created and six existing native/security milestones updated. [Milestone records](extension-ecosystem-milestones.json) link authoritative roadmap sources instead of duplicating 443 tasks as issues.

## Validation and preservation

`npm run check` passed with the installed Roadmap Runner 0.8.0: 37 files, 443 parents, 1,329 checkboxes, zero errors. See [validator output](extension-ecosystem-validation.json). The docs workspace is now a valid manifest target; a temporary negative fixture confirmed that an unknown workspace is rejected and was removed after the check. Documentation checks passed 13 pages and 10 navigation entries with no errors. The first staged whitespace check found extra trailing blank lines in nine new sources; they were removed before commit. The initial check output is retained in `extension-ecosystem-whitespace-initial.log`.

All 292 prior parent IDs remain. Foundation source SHA-256 stays `38b5b9d96921dc419471bdce3a85537df40e7bc3255ebbdc4a20c0ace71d0897`; [preservation evidence](extension-ecosystem-preservation.json) records it. This review neither changed the active foundation source nor started/stopped/messaged its runner. Its concurrent evidence directories remain outside this commit.

Validation establishes task-contract and documentation consistency, not runtime editor capability. No new editor implementation, package release, cloud provisioning, live model call, paid inference test or temporary browser/server was part of this planning follow-up. Performance and native/format/security support remain subject to their named implementation and real-platform gates.

## Primary-source research

- [Rich extensions and secure link patterns](rich-extension-research.md): Tree-sitter/Shiki, table precedent, accessibility and link/metadata boundaries.
- [Document converter evidence](document-conversion-research.md): Rust DOCX, PDF generation/layout candidates, format containers, isolation and direction-specific limits. Earlier PDF-import exploration is explicitly superseded.
- [Public delivery and cloud-store evidence](public-cloud-research.md): documentation/deployment boundaries, object storage, conditional writes and reference versus provider qualification.
