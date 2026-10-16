# Deliver local document import and export extensions

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core`; planned paths below are core-relative unless prefixed `../architecture/`. Read [document conversion](../specs/document-conversion.md), [base formats](../specs/formats.md), [rich content and attachments](../specs/rich-content-extensions.md) and the active task context. Source is controller-owned; workers write state/evidence only to their separate progress file.

Upstream entry gates: `05-markdown-content.md`, `12-client-contracts.md`, `21-extension-library.md` and `25-rich-content-extensions.md` complete at current source revisions with passing artifact evidence. Cross-file references are prerequisite context; local Dependencies lines below name only parents in this file. Do not launch while required upstream evidence is unavailable.

This track produces directional optional format adapters and reusable qualification fixtures. Roadmap 31 owns final browser/native adapter wiring, viewer/platform qualification and broader release. Local/private processing and original-input recovery are mandatory. PDF is export-only: reject PDF import clearly before conversion or live mutation. No PDF extraction, scanned-document recognition or reader dependency is part of this profile. Baseline source/CRDT semantics remain unchanged.

## Execution rules

Implement at most one parent task per iteration, including its implementation and validation. Each names one adapter boundary, target 15–45 minutes plus checks; if the chosen library cannot fit the promised boundary, report the exact missing dependency and propose a controller split before broad work. Other dependency-ready parents remain independent. A skipped, blocked, failed or zero-case result does not complete a parent.

Task CNV-1.1 creates `tests/formats/run.mjs` and the real profile suite. Each later task creates its named scenario and underlying actual Rust/worker/consumer tests before invoking it. The dispatcher records exact locked build/test commands from the versioned capability manifest; missing/unknown suites, absent binaries and zero tests fail instead of reporting synthetic success. Candidate-specific builds are selected only after the required official-doc/license/compatibility gate. Preserve failed/skipped counts and actual resource measurements.

Keep heavy codecs/renderers/fonts optional and outside the minimum editor WASM. Use local hand-authored fixtures and prepared host/transport responses for automated contract tests. No paid inference, live credentials, private user documents as fixtures, production writes, automatic dependency/font downloads at document open, runner startup or publication is part of this work.

## Epic CNV-1 — Qualify directional local conversion adapters


### Task CNV-1.1 — Freeze directional format profiles and test dispatch

- [ ] CNV-1.1 Freeze directional format profiles and test dispatch.

Purpose: Make supported directions and fidelity limits explicit before adding converters.
Context: `crates/editac-formats/`; `fixtures/formats/profiles.json`; `tests/formats/run.mjs`; `../architecture/evidence/document-conversion.md`; `../architecture/specs/document-conversion.md`. [Wordcraft-derived cases](../tests/wordcraft-regression-cases.md).
Dependencies: none.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: Existing Markdown/HTML/text/semantic-JSON behavior is reused; each new direction has a versioned profile, limits, diagnostic schema and target/dependency record. PDF import returns FORMAT_EXPORT_ONLY before any conversion or mutation, including misleading extensions/MIME. Legacy DOC/PPT/XLS and universal fidelity are excluded. The dispatcher invokes real named checks and rejects unknown, absent or zero-case suites. WCF-05: Import-only and exhausted-output profiles produce visible actionable outcomes on claimed host routes; no silent no-op save or successful truncated artifact. This adds no format direction.

Implementation:

- [ ] CNV-1.1-I1 Verify current upstream evidence and attachment staging APIs. Create a lightweight optional format capability/prepared-result crate and profile fixtures; keep converters absent from its default dependency graph. Add the manifest-driven dispatcher and a real profile/registry test including PDF export-only rejection, with exact underlying Rust/browser commands recorded per scenario.

Validation:

- [ ] CNV-1.1-V1 node tests/formats/run.mjs profiles. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable. Execute the named WCF-05 variants through this owner's real boundary; record case/fixture revisions and work/effect counts. Planning validation is not runtime evidence.

Evidence: Progress `CNV-1.1` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.1`.
Blocked behavior: Keep `CNV-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.2 — Implement bounded conversion jobs and asset staging

- [ ] CNV-1.2 Implement bounded conversion jobs and asset staging.

Purpose: Keep preparation local, cancellable and separate from live document mutation.
Context: `crates/editac-formats/src/job.rs`; `crates/editac-formats/tests/jobs.rs`; `fixtures/formats/jobs/`; `../architecture/specs/rich-content-extensions.md`; `../architecture/specs/document-conversion.md`. [Wordcraft-derived cases](../tests/wordcraft-regression-cases.md).
Dependencies: CNV-1.1.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: Input/profile/revision/target and resource budgets are fixed per job. Timeout/cancel/stale-target/asset failure leaves live state unchanged and releases only job-owned resources; fixed-revision export cannot mix later edits. Isolation-unavailable is explicit, with no cloud/network fallback. WCF-03: Host save transitions consume correlated completion/revision outcomes, not job initiation; cancel/write/close failure retains recoverable state and completion for revision N never marks N+1 saved. Reuse this fixture in existing platform wiring owners; conversion completion is not journal durability.

Implementation:

- [ ] CNV-1.2-I1 Expose worker/native-job ports with bounded buffers, deadline/cancellation and approved asset capabilities. Route prepared imports and export snapshots through the shared session API. Reuse attachment staging/cleanup; declare native/browser process isolation requirements for roadmaps31–36 rather than granting ambient filesystem/network access.

Validation:

- [ ] CNV-1.2-V1 node tests/formats/run.mjs jobs. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable. Execute the named WCF-03 variants through this owner's real boundary; record case/fixture revisions and work/effect counts. Planning validation is not runtime evidence.

Evidence: Progress `CNV-1.2` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.2`.
Blocked behavior: Keep `CNV-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.3 — Qualify DOCX and container codec candidates

- [ ] CNV-1.3 Qualify DOCX and container codec candidates.

Purpose: Pin only libraries whose documented behavior, licenses and target support fit the optional adapter.
Context: `crates/editac-formats/Cargo.toml`; `Cargo.lock`; `crates/editac-formats/tests/docx_probe.rs`; `../architecture/evidence/format-dependencies.md`; `../architecture/specs/document-conversion.md`.
Dependencies: CNV-1.1.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: The exact DOCX/ZIP/XML candidate versions/features, licenses/notices, compiler targets and supported parse/write subset are recorded from primary sources. Native and claimed WASM compile probes pass; rejected features/candidates stay visible. The minimum editor build does not gain converter assets.

Implementation:

- [ ] CNV-1.3-I1 Time-box a comparison to at most two viable DOCX/container stacks; include docx-rs as a candidate, not an automatic approval. Disable unnecessary image preview decoding, qualify read/write and original admitted-media access on tiny fixtures, and pin selected optional dependencies only after compatibility/license review.

Validation:

- [ ] CNV-1.3-V1 node tests/formats/run.mjs docx-dependencies. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable.

Evidence: Progress `CNV-1.3` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.3`.
Blocked behavior: Keep `CNV-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.4 — Enforce archive, XML and media ingress budgets

- [ ] CNV-1.4 Enforce archive, XML and media ingress budgets.

Purpose: Reject hostile document containers before semantic mapping or asset publication.
Context: `crates/editac-formats/src/container.rs`; `crates/editac-formats/tests/container_limits.rs`; `fixtures/formats/hostile/`; `../architecture/specs/document-conversion.md`. [Wordcraft-derived cases](../tests/wordcraft-regression-cases.md).
Dependencies: CNV-1.2, CNV-1.3.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: Traversal/absolute/duplicate/conflicting paths, symlinks, unsupported encryption, DTD/external entities, nested active packages and malformed encodings fail safely. Entry/depth/attribute, actual inflated bytes, ratio, decoded pixels and output-node limits are enforced during work, not only from archive headers. WCF-06/WCF-07: Aggregate work charges nested scans and repeated resource references, checks remaining allowance before decode/allocation, and deduplicates rejected resources within the immutable job. Exercise duplicate/normalized-alias/corrupt entries in both orders; log-only omission cannot substitute for structured failure/diagnostics.

Implementation:

- [ ] CNV-1.4-I1 Implement bounded part access and content-type/relationship validation over the selected codecs. Keep macros/OLE/altChunk/remote templates or media inert with explicit diagnostics. Add compressed-bomb and image-expansion fixtures plus cancelled/failed staging checks without extracting arbitrary filesystem paths.

Validation:

- [ ] CNV-1.4-V1 node tests/formats/run.mjs container-limits. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable. Execute the named WCF-06/WCF-07 variants through this owner's real boundary; record case/fixture revisions and work/effect counts. Planning validation is not runtime evidence.

Evidence: Progress `CNV-1.4` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.4`.
Blocked behavior: Keep `CNV-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.5 — Import DOCX text, marks and paragraph structure

- [ ] CNV-1.5 Import DOCX text, marks and paragraph structure.

Purpose: Map the qualified WordprocessingML text subset into prepared editor content.
Context: `crates/editac-formats/src/docx/import.rs`; `crates/editac-formats/tests/docx_import_text.rs`; `fixtures/formats/docx/text/`; `../architecture/specs/document-conversion.md`. [Wordcraft-derived cases](../tests/wordcraft-regression-cases.md).
Dependencies: CNV-1.4.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: Paragraphs, Unicode runs, supported direct/style-derived marks, headings, links, tabs and breaks map deterministically. Style/theme/field/revision constructs outside the profile produce complete diagnostics; import does not invent original-source spelling or Word layout fidelity. WCF-09: Validate adapter-produced Unicode span lengths, checked arithmetic and coordinate conversion before batch preparation; invalid boundaries cannot panic, normalize authored text or partially import.

Implementation:

- [ ] CNV-1.5-I1 Resolve supported paragraph/run styling and text order with bounded relationships. Map into shared semantic primitives; keep unsupported tracked changes/fields/content controls explicit rather than silently accepting an arbitrary branch. Preserve original input provenance and prepare without live mutation.

Validation:

- [ ] CNV-1.5-V1 node tests/formats/run.mjs docx-import-text. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable. Execute the named WCF-09 variants through this owner's real boundary; record case/fixture revisions and work/effect counts. Planning validation is not runtime evidence.

Evidence: Progress `CNV-1.5` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.5`.
Blocked behavior: Keep `CNV-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.6 — Import DOCX lists, tables and admitted assets

- [ ] CNV-1.6 Import DOCX lists, tables and admitted assets.

Purpose: Carry structured DOCX content through qualified modules and attachment services.
Context: `crates/editac-formats/src/docx/import.rs`; `crates/editac-formats/tests/docx_import_structure.rs`; `fixtures/formats/docx/structure/`; `../architecture/specs/document-conversion.md`.
Dependencies: CNV-1.5.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: Supported numbering/nesting, bounded rectangular tables and admitted embedded images preserve semantics and asset identity; unsupported merges/floating layout/headers/footnotes have named diagnostics. External assets never fetch implicitly and rejected assets cannot partially commit content.

Implementation:

- [ ] CNV-1.6-I1 Extend the import mapping only for profile-approved list/table/image semantics, using rich-content descriptors and staged original media bytes. Report transforms, alt text and unsupported objects; retain recoverable source when representation is lossy, then commit one validated insertion/new-session operation.

Validation:

- [ ] CNV-1.6-V1 node tests/formats/run.mjs docx-import-structure. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable.

Evidence: Progress `CNV-1.6` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.6`.
Blocked behavior: Keep `CNV-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.7 — Export the qualified semantic DOCX subset

- [ ] CNV-1.7 Export the qualified semantic DOCX subset.

Purpose: Produce portable Word documents from a captured editor revision.
Context: `crates/editac-formats/src/docx/export.rs`; `crates/editac-formats/tests/docx_export.rs`; `fixtures/formats/docx/export/`; `../architecture/specs/document-conversion.md`. [Wordcraft-derived cases](../tests/wordcraft-regression-cases.md).
Dependencies: CNV-1.6.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: A fixed-revision export encodes supported text/marks/lists/tables/links and embedded authorized assets; unknown features yield a representability report. Independent package parsing and declared viewer fixtures validate semantics; original layout, package-byte identity, macros and signatures are never claimed preserved. WCF-10/WCF-11: Minimal hand-authored packages distinguish preserved supported semantics from lost wrappers/defaults/numbering/metadata. Independent package and semantic inspection requires complete representability diagnostics even when plain text matches; no added TOC/content-control/opaque-part fidelity.

Implementation:

- [ ] CNV-1.7-I1 Implement deterministic semantic mapping to the selected writer with controlled metadata and package parts. Use allowed embedded attachment bytes, explicit page/style defaults and safe relationship targets. Refuse unapproved lossy export and avoid preview re-encoding when original bytes are supported.

Validation:

- [ ] CNV-1.7-V1 node tests/formats/run.mjs docx-export. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable. Execute the named WCF-10/WCF-11 variants through this owner's real boundary; record case/fixture revisions and work/effect counts. Planning validation is not runtime evidence.

Evidence: Progress `CNV-1.7` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.7`.
Blocked behavior: Keep `CNV-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.8 — Qualify PDF export engine, font assets and isolation

- [ ] CNV-1.8 Qualify PDF export engine, font assets and isolation.

Purpose: Choose optional PDF publication components with measured deployment costs.
Context: `crates/editac-formats/Cargo.toml`; `Cargo.lock`; `crates/editac-formats/tests/pdf_probe.rs`; `fixtures/formats/fonts/`; `../architecture/evidence/format-dependencies.md`; `../architecture/specs/document-conversion.md`. [Wordcraft-derived cases](../tests/wordcraft-regression-cases.md).
Dependencies: CNV-1.1, CNV-1.2.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: Exact export/layout versions, target builds, transitive/native notices and font embedding/redistribution permissions are recorded. Candidates demonstrate shaping, tagging and layout needs on tiny fixtures; heavyweight artifacts stay optional and claimed browser/native execution has enforceable isolation/resource limits. WCF-12: Pin test font files/hashes and fallback environment; missing fonts yield declared fallback/unavailability rather than an implicit host-font dependency or download. Font and target provenance accompany output evidence.

Implementation:

- [ ] CNV-1.8-I1 Compare at most two PDF export/layout candidates using official APIs. Distinguish low-level PDF primitives from document layout/pagination; do not add PDF reader/extraction dependencies. Pin the approved profile and test fonts; create bounded probes, trusted-template and allowlisted-resource configuration and process/worker capability checks before production mapping.

Validation:

- [ ] CNV-1.8-V1 node tests/formats/run.mjs pdf-dependencies. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable. Execute the named WCF-12 variants through this owner's real boundary; record case/fixture revisions and work/effect counts. Planning validation is not runtime evidence.

Evidence: Progress `CNV-1.8` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.8`.
Blocked behavior: Keep `CNV-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.9 — Export a paginated PDF publication profile

- [ ] CNV-1.9 Export a paginated PDF publication profile.

Purpose: Create readable publication artifacts without misrepresenting them as editable source.
Context: `crates/editac-formats/src/pdf/export.rs`; `crates/editac-formats/tests/pdf_export.rs`; `fixtures/formats/pdf/export/`; `../architecture/specs/document-conversion.md`. [Wordcraft-derived cases](../tests/wordcraft-regression-cases.md).
Dependencies: CNV-1.8.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: Declared text/marks/lists/tables/images paginate with correct Unicode shaping, selectable text, controlled fonts, links and semantic tags where supported. Independent text/render inspection checks clipping and reading order. PDF/UA or archival compliance is claimed only after its own output validation; no library-choice inference. WCF-13/WCF-14: Use independent logical-text/reading-order and visual/layout oracles for Arabic ligatures/zero-advance glyphs and multipage synthetic content. Perturbed text, missing lines/pages and clipping must fail the relevant oracle; raster similarity alone cannot qualify output. Validation tools inspect generated artifacts only.

Implementation:

- [ ] CNV-1.9-I1 Map captured semantic content into the selected existing layout engine or qualified bounded layout policy, not a new general typesetter. Escape literal content rather than evaluating document-controlled templates/scripts; provide only approved fonts/assets. Add page-break, long-word, RTL, image/table and unsupported-feature fixtures with explicit diagnostics.

Validation:

- [ ] CNV-1.9-V1 node tests/formats/run.mjs pdf-export. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable. Execute the named WCF-13/WCF-14 variants through this owner's real boundary; record case/fixture revisions and work/effect counts. Planning validation is not runtime evidence.

Evidence: Progress `CNV-1.9` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.9`.
Blocked behavior: Keep `CNV-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.10 — Import the semantic ODT subset

- [ ] CNV-1.10 Import the semantic ODT subset.

Purpose: Add OpenDocument text import through the existing guarded container pipeline.
Context: `crates/editac-formats/src/odt/import.rs`; `crates/editac-formats/tests/odt_import.rs`; `fixtures/formats/odt/`; `../architecture/evidence/format-dependencies.md`; `../architecture/specs/document-conversion.md`.
Dependencies: CNV-1.4.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: Supported ODT text/marks/lists/tables/embedded assets map with complete diagnostics; style/layout/field features outside the declared ODF profile and encrypted packages are explicit. No remote relationships or embedded active objects execute or fetch.

Implementation:

- [ ] CNV-1.10-I1 Verify official ODF profile and exact optional parser/XML dependencies/licenses before pinning. Reuse bounded package/manifest parsing and attachment staging; map only qualified schema constructs, preserve unsupported source and return one prepared batch without claiming suite-level fidelity.

Validation:

- [ ] CNV-1.10-V1 node tests/formats/run.mjs odt-import. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable.

Evidence: Progress `CNV-1.10` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.10`.
Blocked behavior: Keep `CNV-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.11 — Export the semantic ODT subset

- [ ] CNV-1.11 Export the semantic ODT subset.

Purpose: Provide an independently qualified OpenDocument export direction.
Context: `crates/editac-formats/src/odt/export.rs`; `crates/editac-formats/tests/odt_export.rs`; `fixtures/formats/odt/export/`; `../architecture/specs/document-conversion.md`.
Dependencies: CNV-1.10.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: The declared ODT package/manifest/content/style subset reopens in an independent reader with expected semantic content and admitted assets. Lossy features and metadata policy are reported; no source-package byte or arbitrary pagination guarantee is inferred from import support.

Implementation:

- [ ] CNV-1.11-I1 Generate the minimal standards-conforming qualified package with approved style/media defaults and explicit representability checks. Reuse exact pinned codec dependencies and fixed-revision export; test package structure and semantic mapping independently of the importer.

Validation:

- [ ] CNV-1.11-V1 node tests/formats/run.mjs odt-export. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable.

Evidence: Progress `CNV-1.11` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.11`.
Blocked behavior: Keep `CNV-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.12 — Import a bounded RTF subset

- [ ] CNV-1.12 Import a bounded RTF subset.

Purpose: Support rich-text exchange while treating control words and embedded objects as untrusted input.
Context: `crates/editac-formats/src/rtf/import.rs`; `crates/editac-formats/tests/rtf_import.rs`; `fixtures/formats/rtf/`; `../architecture/evidence/format-dependencies.md`; `../architecture/specs/document-conversion.md`.
Dependencies: CNV-1.2.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: The declared code-page/Unicode escape, text/mark/paragraph and bounded table subset maps deterministically; unknown destinations, excessive group depth, malformed lengths and OLE/active objects cannot execute or silently disappear. Unsupported content produces a recoverable report.

Implementation:

- [ ] CNV-1.12-I1 Qualify a maintained parser or a deliberately bounded documented grammar implementation against official RTF references before pinning dependencies. Reuse job limits and semantic mapping; handle Unicode fallback bytes and inert embedded payloads explicitly without using an active OS rich-text control as an unrestricted parser.

Validation:

- [ ] CNV-1.12-V1 node tests/formats/run.mjs rtf-import. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable.

Evidence: Progress `CNV-1.12` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.12`.
Blocked behavior: Keep `CNV-1.12` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.13 — Export the bounded RTF subset

- [ ] CNV-1.13 Export the bounded RTF subset.

Purpose: Offer predictable RTF output without promising legacy application or layout equivalence.
Context: `crates/editac-formats/src/rtf/export.rs`; `crates/editac-formats/tests/rtf_export.rs`; `fixtures/formats/rtf/export/`; `../architecture/specs/document-conversion.md`.
Dependencies: CNV-1.12.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: Escaped Unicode/text/marks/paragraphs and the declared table subset reopen correctly through an independent reader. Unsupported images/atoms/styles follow explicit diagnostics; literal braces/backslashes and encoding fallbacks cannot inject control sequences.

Implementation:

- [ ] CNV-1.13-I1 Serialize only the qualified RTF vocabulary from a captured revision using explicit font/color/code-page defaults. Keep OLE/macros/active destinations absent, separate lossy policy from normal export and verify representability rather than assuming importer symmetry.

Validation:

- [ ] CNV-1.13-V1 node tests/formats/run.mjs rtf-export. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable.

Evidence: Progress `CNV-1.13` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.13`.
Blocked behavior: Keep `CNV-1.13` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.14 — Import safe reflowable EPUB content

- [ ] CNV-1.14 Import safe reflowable EPUB content.

Purpose: Turn supported publication chapters into editable content without executing the publication.
Context: `crates/editac-formats/src/epub/import.rs`; `crates/editac-formats/tests/epub_import.rs`; `fixtures/formats/epub/`; `../architecture/evidence/format-dependencies.md`; `../architecture/specs/document-conversion.md`.
Dependencies: CNV-1.4.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: Declared EPUB container/package/spine/navigation order and sanitized chapter text/assets import with provenance. Scripts/forms/remote resources/DRM/fixed-layout features remain inactive and explicitly unsupported; no hidden live web page is used to import HTML.

Implementation:

- [ ] CNV-1.14-I1 Verify the EPUB profile and selected optional container/XML/HTML codecs against primary docs before pinning. Reuse bounded archive and safe semantic HTML handling, chapter boundaries and authorized attachment staging; report unsupported navigation/layout/content instead of flattening it silently.

Validation:

- [ ] CNV-1.14-V1 node tests/formats/run.mjs epub-import. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable.

Evidence: Progress `CNV-1.14` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.14`.
Blocked behavior: Keep `CNV-1.14` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.15 — Export a reflowable EPUB publication

- [ ] CNV-1.15 Export a reflowable EPUB publication.

Purpose: Package supported semantic content for reading systems with an explicit fidelity profile.
Context: `crates/editac-formats/src/epub/export.rs`; `crates/editac-formats/tests/epub_export.rs`; `fixtures/formats/epub/export/`; `../architecture/specs/document-conversion.md`.
Dependencies: CNV-1.14.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: The declared EPUB package, chapter spine, navigation, metadata and admitted local assets pass structure and independent-reader checks. Generated content has no scripts or unexpected remote resource dependencies; fixed-layout or exact pagination is not advertised.

Implementation:

- [ ] CNV-1.15-I1 Map captured headings/sections into deterministic chapter and navigation policy, emitting safe XHTML and package metadata. Preserve semantic accessibility labels where available, include authorized assets with correct types and surface unrepresentable module content before a lossy export.

Validation:

- [ ] CNV-1.15-V1 node tests/formats/run.mjs epub-export. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable.

Evidence: Progress `CNV-1.15` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.15`.
Blocked behavior: Keep `CNV-1.15` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.16 — Import CSV and TSV into bounded tables

- [ ] CNV-1.16 Import CSV and TSV into bounded tables.

Purpose: Support table data exchange without introducing spreadsheet semantics.
Context: `crates/editac-formats/src/table_text/import.rs`; `crates/editac-formats/tests/table_text_import.rs`; `fixtures/formats/table-text/`; `../architecture/evidence/format-dependencies.md`; `../architecture/specs/document-conversion.md`.
Dependencies: CNV-1.1, CNV-1.2.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: Explicit delimiter/quote/escape/encoding/newline/header/ragged-row policies produce one bounded table with exact cell text. Quotes/newlines/empty cells/Unicode round-trip the declared dialect; formula-like strings stay inert and rows/columns/cells obey resource limits.

Implementation:

- [ ] CNV-1.16-I1 Qualify a small maintained CSV codec and explicit TSV dialect before optional pinning. Require a selected dialect or reviewed bounded detection result; map only text cells through the rich-content table descriptor, never evaluate formulas or infer dates/numeric types silently.

Validation:

- [ ] CNV-1.16-V1 node tests/formats/run.mjs table-text-import. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable.

Evidence: Progress `CNV-1.16` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.16`.
Blocked behavior: Keep `CNV-1.16` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.17 — Export selected tables as CSV or TSV

- [ ] CNV-1.17 Export selected tables as CSV or TSV.

Purpose: Make exact table text and spreadsheet-safe output separate, reviewable choices.
Context: `crates/editac-formats/src/table_text/export.rs`; `crates/editac-formats/tests/table_text_export.rs`; `fixtures/formats/table-text/export/`; `../architecture/specs/document-conversion.md`.
Dependencies: CNV-1.16.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: One selected table exports deterministic dialect-compliant cells with declared loss of rich formatting. Exact-data output preserves text; an explicit spreadsheet-safe profile handles formula-like cells without silently altering the exact profile. Non-table document content is not silently dropped.

Implementation:

- [ ] CNV-1.17-I1 Serialize the captured selected-table projection with explicit quoting/newline/header policy and a representability report. Add a separately named spreadsheet-safe transform with visible diagnostics; reject ambiguous multi-table/whole-document requests until the user selects the export target.

Validation:

- [ ] CNV-1.17-V1 node tests/formats/run.mjs table-text-export. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable.

Evidence: Progress `CNV-1.17` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.17`.
Blocked behavior: Keep `CNV-1.17` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.


### Task CNV-1.18 — Qualify optional format consumers and hand off platform wiring

- [ ] CNV-1.18 Qualify optional format consumers and hand off platform wiring.

Purpose: Deliver reproducible format extensions and an honest capability matrix for platform integration.
Context: `tests/formats/consumers/`; `fixtures/formats/profiles.json`; `tests/formats/run.mjs`; `../architecture/evidence/document-conversion.md`; `../architecture/specs/document-conversion.md`.
Dependencies: CNV-1.7, CNV-1.9, CNV-1.11, CNV-1.13, CNV-1.15, CNV-1.17.
Session scope: One named direction/adapter boundary, 15–45 minutes plus focused checks; change only the named paths and required test/build glue.
Acceptance: Declared direction/profile fixtures pass on their claimed compiled targets; unsupported/lossy cases retain diagnostics and original-source recovery. Packed disabled-feature consumers omit heavy converters/fonts/assets, and measured cold/warm time/memory/size includes complete conversion costs. Native wiring/release claims remain owned by roadmaps31–36 and final qualification37.

Implementation:

- [ ] CNV-1.18-I1 Assemble public optional adapter entry points, exact dependency/asset notices, fixture hashes and per-direction support results. Exercise packed local consumers, cancellation/resource abuse and disabled-feature graphs; hand off concrete worker/native requirements and independent-viewer/manual evidence gaps to roadmaps31–36 and qualification37 without claiming they already pass.

Validation:

- [ ] CNV-1.18-V1 node tests/formats/run.mjs consumers. Assert every acceptance case; record exact underlying commands/exits, nonzero executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and measured limits where applicable.

Evidence: Progress `CNV-1.18` links changed paths, selected format/direction/profile, exact dependency and asset versions, test/resource results and preserved failures; durable summaries belong in `../architecture/evidence/document-conversion.md`.
Handoff: Last completed substep, relevant symbol/fixture, unsupported construct or exact failing case, remaining acceptance and next bounded action for `CNV-1.18`.
Blocked behavior: Keep `CNV-1.18` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, dependency/decision/host requirement, unblock condition and bounded retry trigger. Continue a different ready parent only in a later iteration; never downgrade fidelity, expose private content or invoke a remote converter to bypass the gate.
