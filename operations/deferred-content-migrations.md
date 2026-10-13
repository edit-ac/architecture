# Deferred editor content migrations

Status: DEFERRED

## User decision and activation gate

On 2026-10-13 the user instructed: “lets not spend too much time on migrations right now, defer those until the entire app is completed and qualified correctly”.

Content conversion, collaborative migration/cutover and editor migration guides are outside all current runner batches. The original tasks below are preserved with their IDs, acceptance, validation and workspace context; they are not active roadmap tasks and must not be marked complete merely because deferred. Any partial implementation, tests, source snapshots and failed evidence remain in place. No migration implementation, migration-specific synthetic scenarios/qualification runs or migration guide work should continue now.

Activate only after all current application delivery roadmaps 01–42 are complete at their then-current source revisions and their required product/platform/release qualification has real passing evidence: nonzero executed counts, no unresolved mandatory failures/skips, and actual device evidence wherever required. An assumed-complete development baseline does not substitute for this full qualification gate; roadmap 05 FMT-1.15 and other existing device/history/footprint constraints must be resolved if mandatory for that qualification. Full app completion includes the web SDK, native and CLI clients, extensions and documentation. Do not interpret initial web release alone as full completion.

After the gate is reviewed, restore these tasks to a separate explicitly scoped migration roadmap with preserved IDs or a recorded ID mapping and valid dependencies. Current hourly monitoring must not activate them or expand into later tracks automatically.

Routine data preservation and internal schema/version compatibility required for current correctness remain in scope; this deferral concerns user-content/editor migration features and their adoption guides.

## Preserved core converter task

Original workspace: `core`. Original source: `roadmaps/08-sdk-integration.md`. Dependencies below are historical and must be reconciled against completed app evidence before future activation.

### Task SDK-1.5 — Implement scoped Tiptap JSON migration

- [ ] SDK-1.5 Implement scoped Tiptap JSON migration.

Purpose: Deliver implement scoped Tiptap JSON migration as one reviewable boundary.
Context: `crates/editac-core/src/import/tiptap.rs`; `crates/editac-core/tests/migration.rs`; `../architecture/specs/packages-release.md`.
Dependencies: SDK-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Supported fixture content survives; unknown nodes preserve bounded source with diagnostics; old Yjs sessions cannot merge silently into the new schema.

Implementation:

- [ ] SDK-1.5-I1 Map only supported node/mark JSON to prepared semantic content with a versioned converter and diagnostics. Start a new explicit epoch/session for migrated collaborative data.

Validation:

- [ ] SDK-1.5-V1 cargo test -p editac-core --test migration --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SDK-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SDK-1.5`.
Blocked behavior: Leave `SDK-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.


## Preserved editor migration documentation tasks

Original workspace: `docs`. Original source: `roadmaps/29-public-docs-demo.md`. Dependencies below are historical; current docs delivery does not depend on these deferred tasks.

### Task DOC-1.15 — Create the migration overview and shared example contract

- [ ] DOC-1.15 Create the migration overview and shared example contract.

Purpose: Create the migration overview and shared example contract as one reviewable documentation boundary.
Context: `content/docs/migrate/_index.md`; `navigation.json`; `examples/migrations/manifest.json`; `tests/migration-contract.test.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.3.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: The source-editor inventory, safe migration sequence, fidelity/status labels and shared fixture format are discoverable without claiming an available converter. Overview explicitly covers collaborative cutover, assets, IDs/permissions, batch recovery and rollback.

Implementation:

- [ ] DOC-1.15-I1 Create the migration section and versioned source/schema/converter fixture manifest; specify native source export, independent expected target semantics, rendered output and source-located diagnostics. Provide shared equivalent Tiptap/Quill bold-paragraph fixtures, unsupported/custom-content cases and corpus coverage; no fabricated target API or converter-generated oracle. Link planned editor pages only once their owning task creates them.

Validation:

- [ ] DOC-1.15-V1 Create and run `node --test tests/migration-contract.test.mjs` for manifest/version/status rules and independent semantic expectations; run `npm run check`, `zola check --skip-external-links` and `zola build`. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.15` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.15` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.16 — Write the Tiptap migration guide

- [ ] DOC-1.16 Write the Tiptap migration guide.

Purpose: Write the Tiptap migration guide as one reviewable documentation boundary.
Context: `content/docs/migrate/tiptap.md`; `examples/migrations/tiptap/`; `examples/migrations/manifest.json`; `tests/migration-tiptap.test.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.15.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: The Tiptap route records source/target versions, mapping and fidelity, fixtures, diagnostics and recovery under the shared contract. Source-only/planned examples are clearly distinct from qualified conversion.

Implementation:

- [ ] DOC-1.16-I1 Document JSON from the pinned source exporter; supported node/mark/attribute mappings, custom extensions/mentions and HTML fallback. Require SDK-1.5 immutable converter evidence before executable target snippets; explain new collaborative epoch/session rather than reuse of Tiptap Yjs bytes. Apply the shared overview sequence: export, map, preview/review, commit, asset/metadata handling, interrupted/idempotent batch migration and rollback. Include baseline and unsupported/custom-content examples; pin redistributable fixtures and primary-source export references. Register the page and cross-link applicable format/comparison pages when available.

Validation:

- [ ] DOC-1.16-V1 Create and run `node --test tests/migration-tiptap.test.mjs` for pinned source export and documented fixture/mapping/diagnostic contracts; for available immutable converters execute the corresponding packaged target consumer and compare independently authored expected semantics/diagnostics. Missing target runs stay unqualified with separate counts. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.16` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.16` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.17 — Write the ProseMirror migration guide

- [ ] DOC-1.17 Write the ProseMirror migration guide.

Purpose: Write the ProseMirror migration guide as one reviewable documentation boundary.
Context: `content/docs/migrate/prosemirror.md`; `examples/migrations/prosemirror/`; `examples/migrations/manifest.json`; `tests/migration-prosemirror.test.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.15.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: The ProseMirror route records source/target versions, mapping and fidelity, fixtures, diagnostics and recovery under the shared contract. Source-only/planned examples are clearly distinct from qualified conversion.

Implementation:

- [ ] DOC-1.17-I1 Document JSON together with the exact source schema; custom node/mark names, attributes, nested lists and tables. Tiptap adapter evidence is not general ProseMirror-schema compatibility; plugins, decorations, steps/history and collaborative state need explicit independent handling. Apply the shared overview sequence: export, map, preview/review, commit, asset/metadata handling, interrupted/idempotent batch migration and rollback. Include baseline and unsupported/custom-content examples; pin redistributable fixtures and primary-source export references. Register the page and cross-link applicable format/comparison pages when available.

Validation:

- [ ] DOC-1.17-V1 Create and run `node --test tests/migration-prosemirror.test.mjs` for pinned source export and documented fixture/mapping/diagnostic contracts; for available immutable converters execute the corresponding packaged target consumer and compare independently authored expected semantics/diagnostics. Missing target runs stay unqualified with separate counts. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.17` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.17` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.18 — Write the Lexical migration guide

- [ ] DOC-1.18 Write the Lexical migration guide.

Purpose: Write the Lexical migration guide as one reviewable documentation boundary.
Context: `content/docs/migrate/lexical.md`; `examples/migrations/lexical/`; `examples/migrations/manifest.json`; `tests/migration-lexical.test.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.15.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: The Lexical route records source/target versions, mapping and fidelity, fixtures, diagnostics and recovery under the shared contract. Source-only/planned examples are clearly distinct from qualified conversion.

Implementation:

- [ ] DOC-1.18-I1 Serialized editor-state JSON with exact node versions/configuration; formatting, nested nodes, custom/decorator nodes and embeds. Separate source content from plugins, selection/history and collaborative state; document HTML fallback losses. Apply the shared overview sequence: export, map, preview/review, commit, asset/metadata handling, interrupted/idempotent batch migration and rollback. Include baseline and unsupported/custom-content examples; pin redistributable fixtures and primary-source export references. Register the page and cross-link applicable format/comparison pages when available.

Validation:

- [ ] DOC-1.18-V1 Create and run `node --test tests/migration-lexical.test.mjs` for pinned source export and documented fixture/mapping/diagnostic contracts; for available immutable converters execute the corresponding packaged target consumer and compare independently authored expected semantics/diagnostics. Missing target runs stay unqualified with separate counts. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.18` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.18` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.19 — Write the Slate and Plate migration guide

- [ ] DOC-1.19 Write the Slate and Plate migration guide.

Purpose: Write the Slate and Plate migration guide as one reviewable documentation boundary.
Context: `content/docs/migrate/slate-plate.md`; `examples/migrations/slate-plate/`; `examples/migrations/manifest.json`; `tests/migration-slate-plate.test.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.15.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: The Slate and Plate route records source/target versions, mapping and fidelity, fixtures, diagnostics and recovery under the shared contract. Source-only/planned examples are clearly distinct from qualified conversion.

Implementation:

- [ ] DOC-1.19-I1 Application-defined node JSON with exact Slate/Plate versions and application/plugin schema; text leaves/marks, inline/void elements and custom properties. Show distinct Slate and Plate fixtures where schemas differ; do not assume a universal Slate schema. Apply the shared overview sequence: export, map, preview/review, commit, asset/metadata handling, interrupted/idempotent batch migration and rollback. Include baseline and unsupported/custom-content examples; pin redistributable fixtures and primary-source export references. Register the page and cross-link applicable format/comparison pages when available.

Validation:

- [ ] DOC-1.19-V1 Create and run `node --test tests/migration-slate-plate.test.mjs` for pinned source export and documented fixture/mapping/diagnostic contracts; for available immutable converters execute the corresponding packaged target consumer and compare independently authored expected semantics/diagnostics. Missing target runs stay unqualified with separate counts. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.19` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.19` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.20 — Write the Quill migration guide

- [ ] DOC-1.20 Write the Quill migration guide.

Purpose: Write the Quill migration guide as one reviewable documentation boundary.
Context: `content/docs/migrate/quill.md`; `examples/migrations/quill/`; `examples/migrations/manifest.json`; `tests/migration-quill.test.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.15.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: The Quill route records source/target versions, mapping and fidelity, fixtures, diagnostics and recovery under the shared contract. Source-only/planned examples are clearly distinct from qualified conversion.

Implementation:

- [ ] DOC-1.20-I1 Full-document Delta from an authoritative snapshot, not an isolated change Delta; newline-owned block attributes, terminal newline, inline formatting, embeds and custom blots. Preserve UTF-16/range semantics and demonstrate the shared bold-paragraph fixture. Apply the shared overview sequence: export, map, preview/review, commit, asset/metadata handling, interrupted/idempotent batch migration and rollback. Include baseline and unsupported/custom-content examples; pin redistributable fixtures and primary-source export references. Register the page and cross-link applicable format/comparison pages when available.

Validation:

- [ ] DOC-1.20-V1 Create and run `node --test tests/migration-quill.test.mjs` for pinned source export and documented fixture/mapping/diagnostic contracts; for available immutable converters execute the corresponding packaged target consumer and compare independently authored expected semantics/diagnostics. Missing target runs stay unqualified with separate counts. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.20` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.20` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.21 — Write the Draft.js migration guide

- [ ] DOC-1.21 Write the Draft.js migration guide.

Purpose: Write the Draft.js migration guide as one reviewable documentation boundary.
Context: `content/docs/migrate/draftjs.md`; `examples/migrations/draftjs/`; `examples/migrations/manifest.json`; `tests/migration-draftjs.test.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.15.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: The Draft.js route records source/target versions, mapping and fidelity, fixtures, diagnostics and recovery under the shared contract. Source-only/planned examples are clearly distinct from qualified conversion.

Implementation:

- [ ] DOC-1.21-I1 Raw content state with block data, inline-style ranges, entity ranges and entity map; links, entity mutability and atomic blocks. Preserve Unicode range interpretation and report unmapped entities or styles without flattening away recovery data. Apply the shared overview sequence: export, map, preview/review, commit, asset/metadata handling, interrupted/idempotent batch migration and rollback. Include baseline and unsupported/custom-content examples; pin redistributable fixtures and primary-source export references. Register the page and cross-link applicable format/comparison pages when available.

Validation:

- [ ] DOC-1.21-V1 Create and run `node --test tests/migration-draftjs.test.mjs` for pinned source export and documented fixture/mapping/diagnostic contracts; for available immutable converters execute the corresponding packaged target consumer and compare independently authored expected semantics/diagnostics. Missing target runs stay unqualified with separate counts. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.21` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.21` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.22 — Write the Editor.js migration guide

- [ ] DOC-1.22 Write the Editor.js migration guide.

Purpose: Write the Editor.js migration guide as one reviewable documentation boundary.
Context: `content/docs/migrate/editorjs.md`; `examples/migrations/editorjs/`; `examples/migrations/manifest.json`; `tests/migration-editorjs.test.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.15.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: The Editor.js route records source/target versions, mapping and fidelity, fixtures, diagnostics and recovery under the shared contract. Source-only/planned examples are clearly distinct from qualified conversion.

Implementation:

- [ ] DOC-1.22-I1 Saved block JSON with exact editor/tool versions and tool keys; block IDs, per-tool data, inline HTML and custom tools. Use declared safe HTML handling for inline data and distinguish unknown tool payloads from supported semantic blocks. Apply the shared overview sequence: export, map, preview/review, commit, asset/metadata handling, interrupted/idempotent batch migration and rollback. Include baseline and unsupported/custom-content examples; pin redistributable fixtures and primary-source export references. Register the page and cross-link applicable format/comparison pages when available.

Validation:

- [ ] DOC-1.22-V1 Create and run `node --test tests/migration-editorjs.test.mjs` for pinned source export and documented fixture/mapping/diagnostic contracts; for available immutable converters execute the corresponding packaged target consumer and compare independently authored expected semantics/diagnostics. Missing target runs stay unqualified with separate counts. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.22` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.22` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.23 — Write the BlockNote migration guide

- [ ] DOC-1.23 Write the BlockNote migration guide.

Purpose: Write the BlockNote migration guide as one reviewable documentation boundary.
Context: `content/docs/migrate/blocknote.md`; `examples/migrations/blocknote/`; `examples/migrations/manifest.json`; `tests/migration-blocknote.test.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.15.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: The BlockNote route records source/target versions, mapping and fidelity, fixtures, diagnostics and recovery under the shared contract. Source-only/planned examples are clearly distinct from qualified conversion.

Implementation:

- [ ] DOC-1.23-I1 Native block JSON with exact block/inline/style schemas; nested children, block properties, tables, media and custom blocks. Explain HTML/Markdown fallback losses and avoid claiming native BlockNote JSON is interchangeable with Tiptap JSON. Apply the shared overview sequence: export, map, preview/review, commit, asset/metadata handling, interrupted/idempotent batch migration and rollback. Include baseline and unsupported/custom-content examples; pin redistributable fixtures and primary-source export references. Register the page and cross-link applicable format/comparison pages when available.

Validation:

- [ ] DOC-1.23-V1 Create and run `node --test tests/migration-blocknote.test.mjs` for pinned source export and documented fixture/mapping/diagnostic contracts; for available immutable converters execute the corresponding packaged target consumer and compare independently authored expected semantics/diagnostics. Missing target runs stay unqualified with separate counts. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.23` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.23` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.24 — Write the CKEditor 4 migration guide

- [ ] DOC-1.24 Write the CKEditor 4 migration guide.

Purpose: Write the CKEditor 4 migration guide as one reviewable documentation boundary.
Context: `content/docs/migrate/ckeditor4.md`; `examples/migrations/ckeditor4/`; `examples/migrations/manifest.json`; `tests/migration-ckeditor4.test.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.15.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: The CKEditor 4 route records source/target versions, mapping and fidelity, fixtures, diagnostics and recovery under the shared contract. Source-only/planned examples are clearly distinct from qualified conversion.

Implementation:

- [ ] DOC-1.24-I1 Pinned CKEditor 4 exported HTML with plugin/configuration metadata; styles, tables, images, widgets and application-managed attachments. Declare sanitation and unsupported markup behavior; migrate comments/history/application metadata separately rather than implying HTML contains them. Apply the shared overview sequence: export, map, preview/review, commit, asset/metadata handling, interrupted/idempotent batch migration and rollback. Include baseline and unsupported/custom-content examples; pin redistributable fixtures and primary-source export references. Register the page and cross-link applicable format/comparison pages when available.

Validation:

- [ ] DOC-1.24-V1 Create and run `node --test tests/migration-ckeditor4.test.mjs` for pinned source export and documented fixture/mapping/diagnostic contracts; for available immutable converters execute the corresponding packaged target consumer and compare independently authored expected semantics/diagnostics. Missing target runs stay unqualified with separate counts. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.24` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.24` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.25 — Write the CKEditor 5 migration guide

- [ ] DOC-1.25 Write the CKEditor 5 migration guide.

Purpose: Write the CKEditor 5 migration guide as one reviewable documentation boundary.
Context: `content/docs/migrate/ckeditor5.md`; `examples/migrations/ckeditor5/`; `examples/migrations/manifest.json`; `tests/migration-ckeditor5.test.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.15.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: The CKEditor 5 route records source/target versions, mapping and fidelity, fixtures, diagnostics and recovery under the shared contract. Source-only/planned examples are clearly distinct from qualified conversion.

Implementation:

- [ ] DOC-1.25-I1 Pinned CKEditor 5 data processor/export configuration, commonly HTML; tables, images, custom widgets and multi-root content. Separate content export from comments, suggestions and revision history; show declared processor/plugin differences and conversion diagnostics. Apply the shared overview sequence: export, map, preview/review, commit, asset/metadata handling, interrupted/idempotent batch migration and rollback. Include baseline and unsupported/custom-content examples; pin redistributable fixtures and primary-source export references. Register the page and cross-link applicable format/comparison pages when available.

Validation:

- [ ] DOC-1.25-V1 Create and run `node --test tests/migration-ckeditor5.test.mjs` for pinned source export and documented fixture/mapping/diagnostic contracts; for available immutable converters execute the corresponding packaged target consumer and compare independently authored expected semantics/diagnostics. Missing target runs stay unqualified with separate counts. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.25` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.25` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.26 — Write the TinyMCE migration guide

- [ ] DOC-1.26 Write the TinyMCE migration guide.

Purpose: Write the TinyMCE migration guide as one reviewable documentation boundary.
Context: `content/docs/migrate/tinymce.md`; `examples/migrations/tinymce/`; `examples/migrations/manifest.json`; `tests/migration-tinymce.test.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.15.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: The TinyMCE route records source/target versions, mapping and fidelity, fixtures, diagnostics and recovery under the shared contract. Source-only/planned examples are clearly distinct from qualified conversion.

Implementation:

- [ ] DOC-1.26-I1 Pinned TinyMCE exported HTML with enabled plugins/configuration; inline/block styles, tables, media and custom plugin markup. Show sanitation, media asset remapping and HTML fidelity limits; treat plugin behavior and application metadata separately. Apply the shared overview sequence: export, map, preview/review, commit, asset/metadata handling, interrupted/idempotent batch migration and rollback. Include baseline and unsupported/custom-content examples; pin redistributable fixtures and primary-source export references. Register the page and cross-link applicable format/comparison pages when available.

Validation:

- [ ] DOC-1.26-V1 Create and run `node --test tests/migration-tinymce.test.mjs` for pinned source export and documented fixture/mapping/diagnostic contracts; for available immutable converters execute the corresponding packaged target consumer and compare independently authored expected semantics/diagnostics. Missing target runs stay unqualified with separate counts. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.26` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.26` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.27 — Write the shared HTML, Markdown and plain-text routes migration guide

- [ ] DOC-1.27 Write the shared HTML, Markdown and plain-text routes migration guide.

Purpose: Write the shared HTML, Markdown and plain-text routes migration guide as one reviewable documentation boundary.
Context: `content/docs/migrate/other-editors.md`; `examples/migrations/other-editors/`; `examples/migrations/manifest.json`; `tests/migration-other-editors.test.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.15.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: The shared HTML, Markdown and plain-text routes route records source/target versions, mapping and fidelity, fixtures, diagnostics and recovery under the shared contract. Source-only/planned examples are clearly distinct from qualified conversion.

Implementation:

- [ ] DOC-1.27-I1 Separate HTML, Markdown dialect and plain-text fixtures, with entry points for Froala, Summernote, CodeMirror and Monaco. Verify exact source exporters/configuration against primary docs; distinguish rich HTML editors from code/text buffers, document fallback losses and identify when a custom adapter is necessary. Apply the shared overview sequence: export, map, preview/review, commit, asset/metadata handling, interrupted/idempotent batch migration and rollback. Include baseline and unsupported/custom-content examples; pin redistributable fixtures and primary-source export references. Register the page and cross-link applicable format/comparison pages when available.

Validation:

- [ ] DOC-1.27-V1 Create and run `node --test tests/migration-other-editors.test.mjs` for pinned source export and documented fixture/mapping/diagnostic contracts; for available immutable converters execute the corresponding packaged target consumer and compare independently authored expected semantics/diagnostics. Missing target runs stay unqualified with separate counts. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.27` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.27` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

