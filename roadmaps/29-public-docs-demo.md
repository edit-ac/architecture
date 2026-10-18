# Deliver public documentation and the real editor demo

Status: IN_PROGRESS

Delivery sequencing (superseding user decision, 2026-10-18): follow [web → features → alpha → native → docs → qualification → native tests → beta → integrations](../operations/web-feature-first-20261018.md). All device/target-runtime observations in this source belong to [roadmap43](43-physical-device-verification.md), including simulator/emulator/OS/IME/AT/clipboard device matrices. They do not gate feature development. Original predicate text below remains the later verification contract; its transfer owner and exact paragraphs are in the [device requirement register](../operations/device-requirements-20261018.json). Feature tasks retain focused correctness/data-safety checks; exhaustive performance/platform/release qualification is later. Windows/Linux implementation waits for web feature completeness; cloud28 retains its explicit deferral. Historical source/progress/checkmarks/failures are not rewritten or declared complete.

Qualification amendment (user decision, 2026-10-14): Physical devices, named target-platform simulators/emulators and desktop OS VMs/test hosts are accepted for platform and release qualification under the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms). Missing physical hardware does not block completion. Execute required behavior against the implemented target-platform runtime; document and test virtual equivalents for unavailable hardware-only input/accessibility cases. Record physical versus virtual provenance and measure performance in the tested environment. This supersedes earlier physical-only or manual-only clauses below; it does not complete unchecked tasks or waive implementation, correctness, security or artifact gates.

## Goal and entry conditions

Workspace: `docs`; paths below are workspace-relative unless prefixed `../architecture/` or another explicit sibling. Read `../architecture/specs/public-docs-demo.md` and only the active task's named context. Planned paths and commands are created by their owning task. This source describes delivery; it is not a capability claim or live progress.

Required upstream tracks: none for documentation bootstrap at reviewed immutable source/implementation revisions with passing evidence. Tasks name additional SDK/profile gates where required; documentation bootstrap does not wait for complete editor delivery. Local Dependencies fields refer only to this file.

Migration sequencing (2026-10-13): DOC-1.15–1.27 migration overview/guides and SDK-1.5 conversion are deferred until full application completion and qualification. Their original contracts and activation gate are preserved in `../operations/deferred-content-migrations.md`. Do not implement migration pages/fixtures now; current documentation, integration examples and evidence-backed comparisons proceed independently. Navigation may retain an explicitly deferred migration placeholder without conversion/support claims.

## Execution rules

The controller owns this source. Keep checkmarks, evidence and interruption handoff in the separate progress file. Run one parent per iteration, with its implementation and validation substeps. Read task-local context rather than the complete ecosystem. Create named checks before invoking them; unknown suites, zero matches and skipped platforms cannot pass. Use deterministic fixtures and prepared transports, no live model/provider calls or paid inference. Do not load `.secrets`. Missing toolchains or upstream evidence block only their dependent tasks. Do not launch another controller or publish outside a named release task.

## Epic DOC-1 — Deliver public documentation and the real editor demo

### Task DOC-1.1 — Verify the public documentation baseline

- [ ] DOC-1.1 Verify the public documentation baseline.

Purpose: Verify the public documentation baseline as one bounded integration or qualification boundary.
Context: `README.md`; `navigation.json`; `scripts/check-docs.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: none.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Public Apache-2.0 ownership, reading order and current capability labels are accurate; no placeholder editor API is advertised.

Implementation:

- [ ] DOC-1.1-I1 Review the created docs repository, retain useful guides, validate links and record the immutable source baseline; remove duplicate internal task content.

Validation:

- [ ] DOC-1.1-V1 `npm run check`; verify repository visibility/license with read-only GitHub metadata. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.1` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.2 — Select and build the static documentation site

- [ ] DOC-1.2 Select and build the static documentation site.

Purpose: Select and build the static documentation site as one bounded integration or qualification boundary.
Context: `site/`; `package.json`; `docs/reference/site-toolchain.md`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: A maintained generator is pinned with locks, license/maintenance evidence and a reproducible production build; no custom documentation framework or hidden cloud dependency.

Implementation:

- [ ] DOC-1.2-I1 Choose a supported static documentation generator from verified primary docs, record the bounded decision, integrate existing Markdown and add build/check scripts. Test production base path and asset URLs.

Validation:

- [ ] DOC-1.2-V1 `npm ci --ignore-scripts`; `npm run build`; `node --test tests/site-build.test.mjs` (create the build/asset fixtures). Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.2` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.3 — Complete reader navigation and guide templates

- [ ] DOC-1.3 Complete reader navigation and guide templates.

Purpose: Complete reader navigation and guide templates as one bounded integration or qualification boundary.
Context: `docs/`; `navigation.json`; `tests/navigation.test.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.2.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Getting started, Core concepts, Extensions, API reference, Guides, Examples, Compare and Troubleshooting are discoverable under the reader structure in public-docs-demo.md. Web/React/native/CLI paths and current versus planned support are visible on entry pages; existing canonical guides and redirects remain valid.

Implementation:

- [ ] DOC-1.3-I1 Map the Tiptap-informed reader structure in public-docs-demo.md to canonical Zola content sections, explicit weights, navigation and search; link existing guides rather than duplicating them. Record tested-version/prerequisite/example/failure/recovery template fields; reserve planned DOC-1.31–1.38 entries without broken links. Map the public information architecture to real pages; add consistent prerequisites, tested-version labels, failure/recovery sections and migration links without copying architecture roadmaps. Reserve discoverable Migrate to edit.ac and Compare editors entries for DOC-1.15/1.28/1.29, with links from the docs landing page, getting started, import/export and compatibility.

Validation:

- [ ] DOC-1.3-V1 `npm run check`; `node --test tests/navigation.test.mjs`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.3` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.4 — Generate versioned API and capability references

- [ ] DOC-1.4 Generate versioned API and capability references.

Purpose: Generate versioned API and capability references as one bounded integration or qualification boundary.
Context: `scripts/generate-reference.mjs`; `releases/`; `docs/reference/`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.3.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Generated signatures match named qualified artifacts; absent/unqualified APIs never receive install-ready examples. Capability tables derive from core profiles. Public lifecycle/document/commands/selection/events/storage/sync and extension entries link to qualified examples and core concepts, with parameters, outcomes, errors, platform limits and version history.

Implementation:

- [ ] DOC-1.4-I1 Consume immutable core public exports/binding metadata and roadmap30 profile schema; record external entry evidence from08 and30 before claiming executable API coverage. Generate only real exported public APIs/binding metadata; include per-entry example/source-manifest links and prerequisite profiles. Create generation drift checks.

Validation:

- [ ] DOC-1.4-V1 `node scripts/generate-reference.mjs --check`; `node --test tests/reference-profile.test.mjs`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.4` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.5 — Publish executable web, React and Astro quickstarts

- [ ] DOC-1.5 Publish executable web, React and Astro quickstarts.

Purpose: Publish executable web, React and Astro quickstarts as one bounded integration or qualification boundary.
Context: `examples/web/`; `examples/react/`; `examples/astro/`; `examples/releases.json`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.4.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Tutorials install real pinned registry artifacts, demonstrate lifecycle/read-only/save errors and dispose cleanly without workspace aliases. Browser, React and Astro consumers use the Project kickoff corpus and show create/mount, actual edit/readback, a formatting action, save/reopen, read-only and teardown. React demonstrates qualified SSR/client-boundary and mount/unmount behavior; Astro demonstrates qualified static/SSR rendering, browser initialization and ClientRouter navigation cleanup without React. Getting-started navigation makes both first-party integrations discoverable and explains their shared framework-independent SDK.

Implementation:

- [ ] DOC-1.5-I1 Require08 and10 release-consumer evidence, including SDK-1.7/1.4 Astro qualification, and the qualified package versions; create complete plain browser, React/SSR and Astro static/SSR consumers and derive snippets from tested files. Name required JS/WASM/CSS assets, loading failure handling, independently expected edit/readback/save states and lifecycle cleanup. Register sources, snippet ranges, exact versions, fixtures and capability status in examples/manifest.json; additional framework/native bindings remain clearly planned.

Shared-resource guidance: Consume SDK-1.9/1.10's qualified asset manifest and common dependency/chunk settings. Explain one runtime initialization per compatible module owner with independent document handles, optional-feature union versus instance enablement, stable URLs/cache headers across routes and fresh initialization after full navigation. SSR remains side-effect free. Do not promise unconditional cross-page cache hits; guides use exact supported host build settings.

Validation:

- [ ] DOC-1.5-V1 `npm run check:examples -- --suite web-react`; `npm run check:examples -- --suite astro`; create the dispatcher and reject unknown/empty suites. Validate all three consumers, including Astro static/SSR and navigation lifecycle, using deterministic content and prepared transports. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.5` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.6 — Write extension and resolver integration recipes

- [ ] DOC-1.6 Write extension and resolver integration recipes.

Purpose: Write extension and resolver integration recipes as one bounded integration or qualification boundary.
Context: `docs/guides/extensions.md`; `docs/guides/references.md`; `examples/extensions/`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.5.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Recipes show public and permission-scoped internal resolution, cancellation, custom references, assets and service policy with executable public APIs.

Implementation:

- [ ] DOC-1.6-I1 External task gate: require EQL-1.9 immutable candidate publication receipts plus25/26 evidence for enhanced features; build prepared-host examples from public extension entry points. Show a safe fixture link resolving to preview metadata, an internal-link permission denial, a cancelled asset upload and recovery; record before/action/after outcomes and source-manifest links. Clearly separate auto-paste metadata policy from permission or document-open fetch.

Validation:

- [ ] DOC-1.6-V1 `npm run check:examples -- --suite extensions-resolvers`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.6` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.7 — Write format and native integration guides

- [ ] DOC-1.7 Write format and native integration guides.

Purpose: Write format and native integration guides as one bounded integration or qualification boundary.
Context: `docs/guides/document-formats.md`; `docs/guides/native/`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.4.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Every supported direction/platform links its version and fidelity evidence; PDF is export-only and unsupported cases remain explicit.

Implementation:

- [ ] DOC-1.7-I1 Require27 and each claimed platform’s31–35 package-consumer evidence for runnable examples. Unavailable platforms retain explicitly conceptual guides and no executable-support claim; this documentation task does not require every native platform to qualify. Generate the support table and author short file-picker/preview/cancel/import/export recipes per qualified host. Include concrete pinned Swift/Kotlin/desktop/CLI consumers only for qualified bindings; compare source input, conversion report, resulting document, cancellation and restore rather than only listing API names.

Validation:

- [ ] DOC-1.7-V1 `npm run check:examples -- --suite formats-native`; native examples use recorded physical or virtual platform checks and tested hardware-only equivalents; missing required behavior remains a failure. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.7` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.8 — Document cloud hosting and host-app agents

- [ ] DOC-1.8 Document cloud hosting and host-app agents.

Purpose: Document cloud hosting and host-app agents as one bounded integration or qualification boundary.
Context: `docs/guides/cloud-hosting.md`; `docs/guides/agents.md`; `examples/host-services/`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.4.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: The reference service guide covers tenancy, auth, durable receipts, assets, backups and deployment limits; MCP examples use shared request semantics with prepared clients.

Implementation:

- [ ] DOC-1.8-I1 Require14 and28 evidence for runnable service instructions. Provide a local reference deployment and operational checklist without provisioning paid services or adding credentials. Add a prepared two-client save/reconnect/durable-receipt transcript and a fixed host-app MCP document proposal with acceptance, stale-target rejection and recovery; keep provider/model transports mocked.

Validation:

- [ ] DOC-1.8-V1 `npm run check:examples -- --suite host-services`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.8` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.9 — Build the real local-first public playground

- [ ] DOC-1.9 Build the real local-first public playground.

Purpose: Build the real local-first public playground as one bounded integration or qualification boundary.
Context: `playground/`; `tests/playground-local.spec.ts`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.5.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Actual package editor supports PM/document presets, local persistence/reset, read-only and undo/redo. No mock editor or live model dependency.

Implementation:

- [ ] DOC-1.9-I1 Use the qualified08/10 SDK artifacts, show the exact profile, create redistributable fixtures and error/recovery UI. Add a bounded browser check runner with documented cleanup.

Validation:

- [ ] DOC-1.9-V1 `npm run check:playground -- --suite local-editor`; verify real edits, reload/recovery, disposal and storage reset. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.9` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.10 — Add extension and conversion playground scenarios

- [ ] DOC-1.10 Add extension and conversion playground scenarios.

Purpose: Add extension and conversion playground scenarios as one bounded integration or qualification boundary.
Context: `playground/scenarios/`; `tests/playground-extensions.spec.ts`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.6, DOC-1.7, DOC-1.9.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Code/table/assets/references, source/semantic diffs and supported conversion directions use actual qualified services; PDF input reports export-only.

Implementation:

- [ ] DOC-1.10-I1 External task gate: require EQL-1.9 candidates; consume25/26/27/13 evidence; expose lazy feature toggles and size limits, cancellation and loss-report previews. Default URLs/media to approved fixtures and local imports.

Validation:

- [ ] DOC-1.10-V1 `npm run check:playground -- --suite extensions-formats`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.10` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.11 — Demonstrate real collaboration without a hidden backend

- [ ] DOC-1.11 Demonstrate real collaboration without a hidden backend.

Purpose: Demonstrate real collaboration without a hidden backend as one bounded integration or qualification boundary.
Context: `playground/scenarios/collaboration/`; `tests/playground-collaboration.spec.ts`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.9.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Two views/tabs converge through the actual qualified local channel; disconnect/reconnect and durability labels are real. No anonymous open proxy or shared private room.

Implementation:

- [ ] DOC-1.11-I1 Require12/06 evidence; add local multi-client interaction. Document an optional explicitly configured remote host mode gated by28; static public mode remains useful without remote provisioning.

Validation:

- [ ] DOC-1.11-V1 `npm run check:playground -- --suite collaboration`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.11` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.12 — Qualify docs and playground accessibility and loading

- [ ] DOC-1.12 Qualify docs and playground accessibility and loading.

Purpose: Qualify docs and playground accessibility and loading as one bounded integration or qualification boundary.
Context: `tests/site-accessibility.spec.ts`; `tests/site-assets.spec.ts`; `docs/reference/site-support.md`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.10, DOC-1.11.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Keyboard/touch/screen-reader paths, responsive tables/code, search, themes, lazy worker/WASM assets and production CSP work for the declared browser envelope.

Implementation:

- [ ] DOC-1.12-I1 Use actual production build; fix navigation, long-content and interaction failures. Include published concept/API/extension/example/migration/comparison sections, source links, code overflow, example reset controls and optional interactive embed teardown in the accessibility/search/mobile audit; later content releases reuse these checks. Record manual accessibility evidence, generator/search indexes, redistributable asset licenses and raw load samples.

Validation:

- [ ] DOC-1.12-V1 `npm run check:site`; `npm run check:playground -- --suite accessibility-assets`; execute declared manual screen-reader cases. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.12` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.12` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.13 — Publish and verify the public documentation and demo

- [ ] DOC-1.13 Publish and verify the public documentation and demo.

Purpose: Publish and verify the public documentation and demo as one bounded integration or qualification boundary.
Context: `.github/workflows/publish.yml`; `releases/site.json`; `scripts/check-deployment.mjs`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.8, DOC-1.12.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Actual public URLs load the named site/SDK build and permit real fixture edits; a retained previous artifact can be restored.

Implementation:

- [ ] DOC-1.13-I1 Require EQL-1.9 candidate identities for enhanced live content, label prerelease limits clearly, then configure organization-approved static publication with immutable builds and least privileges. Use the intended base path, verify deployment and record URL/artifact/revisions; no domain purchase or paid provider setup is required.

Validation:

- [ ] DOC-1.13-V1 `node scripts/check-deployment.mjs --release releases/site.json`; perform documented real-URL edit/export and previous-artifact rollback rehearsal. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.13` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.13` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.14 — Gate future documentation releases against SDK drift

- [ ] DOC-1.14 Gate future documentation releases against SDK drift.

Purpose: Gate future documentation releases against SDK drift as one bounded integration or qualification boundary.
Context: `scripts/check-release-links.mjs`; `.github/workflows/ci.yml`; `docs/reference/releases.md`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.13.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: SDK/profile references resolve to immutable releases and docs cannot silently advertise unqualified or removed capabilities. Published migration fixtures, feature cells and benchmark data retain source versions, review dates and immutable evidence; drift checks cover DOC-1.28–1.38 as those pages become available, including examples/manifest.json, derived snippet ranges and independently expected semantic outcomes.

Implementation:

- [ ] DOC-1.14-I1 Add release-note/migration/update procedure with owner and exact profile inputs; make snippet/reference drift fail CI. Keep internal architecture tasks out of public navigation. Include migration converter/source version drift, competitor feature evidence review and benchmark artifact/provenance checks; never refresh measured results from a newer unmeasured build. Gate every newly published concept/API/extension/example/recipe/troubleshooting page against its source manifest, exact qualified artifacts, navigation and applicable DOC-1.12 checks; planned pages retain maturity labels.

Validation:

- [ ] DOC-1.14-V1 `node scripts/check-release-links.mjs`; `npm run check`; `npm run check:examples -- --suite published-profile`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.14` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.14` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.28 — Create the versioned editor feature comparison

- [ ] DOC-1.28 Create the versioned editor feature comparison.

Purpose: Create the versioned editor feature comparison as one reviewable documentation boundary.
Context: `content/docs/compare/_index.md`; `content/docs/compare/features.md`; `comparisons/features.json`; `tests/comparison-features.test.mjs`; `navigation.json`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.3.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: The documented editor comparison set is compared by content/interchange, collaboration/offline/durability, integration, platforms/accessibility/mobile/IME, licensing/services and migration effort. Every cell carries a precise support label, version, evidence and review date; edit.ac maturity follows qualified profiles.

Implementation:

- [ ] DOC-1.28-I1 Create a primary-source-backed feature data schema and accessible comparison table; distinguish built-in, official extension, third-party, custom implementation, planned, unsupported and not verified. Explain workload tradeoffs without an overall winner; link existing migration guides and explicitly pending routes without broken links. Missing evidence cannot become an unsupported claim. Add Compare editors to navigation and relevant entry/format/compatibility pages.

Validation:

- [ ] DOC-1.28-V1 Create and run `node --test tests/comparison-features.test.mjs` for version/provenance/status and unknown-evidence rules; run `npm run check`, `zola check --skip-external-links` and `zola build`; inspect keyboard/mobile table use in a local preview, then close task tabs and stop the preview. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.28` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.28` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.29 — Document reproducible editor benchmark methodology

- [ ] DOC-1.29 Document reproducible editor benchmark methodology.

Purpose: Document reproducible editor benchmark methodology as one reviewable documentation boundary.
Context: `content/docs/compare/methodology.md`; `comparisons/benchmark-profile.schema.json`; `tests/comparison-methodology.test.mjs`; `../architecture/specs/verification.md`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.3.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: A reader can reproduce the declared REL-1.2/1.3/1.4 profiles. Minimal/full configurations, fixture sizes, cold/warm states, visible/edit-ready endpoints, sample sufficiency, input limitations and unavailable measurements are explicit; no numbers are invented.

Implementation:

- [ ] DOC-1.29-I1 Document optimized Tiptap/Lexical/edit.ac profiles and the limited plain-contenteditable reference from the existing core harness. Define version/build/feature/durability parity, hardware/OS/browser/network, seeds/hashes, warmup/order/counts, percentiles and raw artifact metadata; reuse Task/Long/Large/Aged definitions. Cover startup, input, HTML/Markdown paste, large edits, remote bursts, bytes/memory/teardown, save/restore and reconnect. Show Not yet measured/Inconclusive states and separate targets; do not execute or duplicate the harness in docs.

Validation:

- [ ] DOC-1.29-V1 Create and run `node --test tests/comparison-methodology.test.mjs` with prepared profile/results fixtures that reject missing provenance, insufficient samples represented as passes and target/result confusion; run `npm run check`, `zola check --skip-external-links` and `zola build`. No benchmark measurement or provider call is authorized by this documentation check. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.29` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.29` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.30 — Publish evidence-backed editor benchmark comparisons

- [ ] DOC-1.30 Publish evidence-backed editor benchmark comparisons.

Purpose: Publish evidence-backed editor benchmark comparisons as one reviewable documentation boundary.
Context: `content/docs/compare/benchmarks.md`; `comparisons/results/`; `scripts/check-comparison-evidence.mjs`; `tests/comparison-results.test.mjs`; `../architecture/specs/verification.md`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.28, DOC-1.29.
Session scope: One named guide or comparison surface, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary. Source documentation may proceed before target artifacts qualify; runnable target examples require the exact converter/SDK evidence.
Acceptance: Accessible tables/charts and sanitized downloadable samples reference exact immutable REL-1.2/1.3/1.4 builds/profiles, retaining regressions, failures/skips and supported envelopes. Unmeasured editors/metrics and insufficient evidence have explicit states; feature coverage is not benchmark coverage.

Implementation:

- [ ] DOC-1.30-I1 Consume reviewed core benchmark artifacts only; external gate for numeric publication is exact passing REL-1.2/1.3/1.4 provenance at immutable artifact revisions. Before evidence exists, create the page with Not yet measured entries, without claiming measured acceptance. Publish minimal/full results separately with raw data and reproduction commands; expose limitations and link methodology/features/migration. Integrate evidence/link drift checks with DOC-1.14 and the next named docs publication task; do not deploy or rerun benchmarks here.

Validation:

- [ ] DOC-1.30-V1 Create and run `node scripts/check-comparison-evidence.mjs` and `node --test tests/comparison-results.test.mjs` using prepared positive/negative report fixtures; reject mismatched builds/profiles, missing raw samples, fabricated measurements and hidden failures. Validate imported actual evidence separately before numeric acceptance. Run `npm run check`, `zola check --skip-external-links` and `zola build`; inspect charts/tables on desktop/mobile and close task tabs/preview. Record commands/exits, nonzero executed/passed/failed/skipped counts where checks have cases, source/artifact/profile revisions and preserved failures. Missing converter/device/measurement evidence remains unqualified.

Evidence: Separate progress entry `DOC-1.30` links changed paths, immutable inputs and focused check artifacts.
Handoff: Last completed substep, current page/fixture, exact failure or missing evidence, and next bounded action.
Blocked behavior: Leave `DOC-1.30` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.31 — Explain core concepts through one document fixture

- [ ] DOC-1.31 Explain core concepts through one document fixture.

Purpose: Explain core concepts through one document fixture as one bounded reader-facing documentation surface.
Context: `content/docs/concepts/`; `examples/concepts/`; `tests/docs-concepts.test.mjs`; `examples/manifest.json`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.3.
Session scope: One named section or example family, normally 15–45 minutes plus focused validation. Reuse owning-task consumers rather than implement editor features; propose a controller-reviewed split if needed. Conceptual source material may proceed before qualified artifacts; executable/support acceptance requires its exact profile evidence.
Acceptance: Document structure/schema, blocks and inline formatting, commands/selection/history, local-first persistence and collaboration are explained through one versioned Project kickoff fixture with independently expected states. Diagrams/transcripts distinguish conceptual semantics from public API/runtime evidence.

Implementation:

- [ ] DOC-1.31-I1 Create short linked concept pages and semantic tree/state diagrams. Trace selecting Friday, applying/removing bold, splitting/joining a paragraph, undo/redo, local save/reopen and a prepared remote insertion; show rejected/stale operations and localCommitted versus remoteCommitted outcomes. Reuse qualified engine/profile evidence where available without inventing API/schema shapes. Register original fixture IDs, expected outcomes, maturity and source-manifest links.

Validation:

- [ ] DOC-1.31-V1 Create/run `node --test tests/docs-concepts.test.mjs` for fixture identities, independent transcript expectations, status labels and concept/reference links; for any executable claim use the named immutable consumer. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Create named checks before use; record command exits, nonzero case counts, failures/skips, source/fixture/profile/artifact hashes and retained failure evidence. Planned material cannot pass runtime qualification.

Evidence: Separate progress entry `DOC-1.31` links canonical pages, source/example manifest and focused artifacts.
Handoff: Last completed page/fixture/check, exact unresolved dependency and next bounded action.
Blocked behavior: Leave `DOC-1.31` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.32 — Document commands and selection with before-and-after examples

- [ ] DOC-1.32 Document commands and selection with before-and-after examples.

Purpose: Document commands and selection with before-and-after examples as one bounded reader-facing documentation surface.
Context: `content/docs/reference/commands/`; `content/docs/reference/selection.md`; `examples/commands/`; `tests/docs-commands.test.mjs`; `examples/manifest.json`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.4, DOC-1.31.
Session scope: One named section or example family, normally 15–45 minutes plus focused validation. Reuse owning-task consumers rather than implement editor features; propose a controller-reviewed split if needed. Conceptual source material may proceed before qualified artifacts; executable/support acceptance requires its exact profile evidence.
Acceptance: Documented public commands include parameter/return/error contracts, selection requirements, capability/profile limits, history grouping and before/action/after outcomes; no unsupported chain/helper API is implied by the Tiptap reference.

Implementation:

- [ ] DOC-1.32-I1 Use generated real signatures to explain format toggles on Friday, heading/list changes where supported, paragraph split/join, undo/redo and rejected read-only/stale/protected operations. Pair API pages with complete consumers and independent semantic/selection snapshots; distinguish ordinary and collaboration-aware history. Show multi-command atomicity only when the public contract qualifies it.

Validation:

- [ ] DOC-1.32-V1 Create/run `node --test tests/docs-commands.test.mjs` against the exact packaged command/selection consumer; compare independent semantic/selection/history/error snapshots and verify generated signatures/snippet ranges. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Create named checks before use; record command exits, nonzero case counts, failures/skips, source/fixture/profile/artifact hashes and retained failure evidence. Planned material cannot pass runtime qualification.

Evidence: Separate progress entry `DOC-1.32` links canonical pages, source/example manifest and focused artifacts.
Handoff: Last completed page/fixture/check, exact unresolved dependency and next bounded action.
Blocked behavior: Leave `DOC-1.32` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.33 — Document lifecycle and events through a saving example

- [ ] DOC-1.33 Document lifecycle and events through a saving example.

Purpose: Document lifecycle and events through a saving example as one bounded reader-facing documentation surface.
Context: `content/docs/reference/lifecycle.md`; `content/docs/reference/events.md`; `examples/lifecycle/`; `tests/docs-lifecycle.test.mjs`; `examples/manifest.json`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.4, DOC-1.31.
Session scope: One named section or example family, normally 15–45 minutes plus focused validation. Reuse owning-task consumers rather than implement editor features; propose a controller-reviewed split if needed. Conceptual source material may proceed before qualified artifacts; executable/support acceptance requires its exact profile evidence.
Acceptance: A complete lifecycle/subscription example distinguishes ready, document changes, selection, errors, local commits and qualified remote receipts, with tested cleanup and no event-equals-durability claim.

Implementation:

- [ ] DOC-1.33-I1 Show mount/open, subscribe, edit Friday, refresh a save indicator from actual commit receipts, switch read-only, unsubscribe/dispose and remount. Include asset-load/save failure, cancellation and recovery with prepared local transports; document actual event ordering/reentrancy/lifetime from exported contracts. Explain React effect cleanup and SSR/client-boundary constraints through the existing consumer.

Validation:

- [ ] DOC-1.33-V1 Create/run `node --test tests/docs-lifecycle.test.mjs` with qualified artifact events and prepared storage/transport failures; verify independent event/commit timelines, unsubscribe/dispose and remount resource counts. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Create named checks before use; record command exits, nonzero case counts, failures/skips, source/fixture/profile/artifact hashes and retained failure evidence. Planned material cannot pass runtime qualification.

Evidence: Separate progress entry `DOC-1.33` links canonical pages, source/example manifest and focused artifacts.
Handoff: Last completed page/fixture/check, exact unresolved dependency and next bounded action.
Blocked behavior: Leave `DOC-1.33` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.34 — Build the extension catalog with configuration examples

- [ ] DOC-1.34 Build the extension catalog with configuration examples.

Purpose: Build the extension catalog with configuration examples as one bounded reader-facing documentation surface.
Context: `content/docs/extensions/`; `examples/extension-configurations/`; `tests/docs-extension-catalog.test.mjs`; `examples/manifest.json`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.4.
Session scope: One named section or example family, normally 15–45 minutes plus focused validation. Reuse owning-task consumers rather than implement editor features; propose a controller-reviewed split if needed. Conceptual source material may proceed before qualified artifacts; executable/support acceptance requires its exact profile evidence.
Acceptance: Catalog pages distinguish semantic blocks/nodes, inline marks and optional behavior/modules; each named extension/preset shows exact versions, options, dependencies/conflicts, costs, platform presenters and qualification limits. The 2026-10-17 [extension DX contract](../specs/extension-dx.md) adds one-import typed configuration, individual composition without use-case restrictions, managed lazy assets and optional generic default/document convenience presets. New facade examples require exact SDK-1.11, SDK-1.12, EXT-1.20 artifact evidence; historical low-level examples retain their version labels.

Implementation:

- [ ] DOC-1.34-I1 Generate or check catalog metadata against owning descriptors/profiles for headings/lists, code highlighting, tables, assets/links, menus/drag handles and supported first-party presets. Each page includes a small original input/action/output configuration example, shortcut/command links, serialization/import behavior, accessibility/cancellation and teardown. Separate portable semantic support from browser/native/terminal presenters; unavailable profiles retain planned labels. Reuse EXT-1.20's canonical source/version manifest for facade configuration and initial/deferred costs; beginners do not copy codec/registry/worker orchestration and application labels do not dictate extension sets.

Validation:

- [ ] DOC-1.34-V1 Create/run `node --test tests/docs-extension-catalog.test.mjs` for descriptor/profile/options/version drift and complete qualified configuration consumers; validate source links and independent expected outputs. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Create named checks before use; record command exits, nonzero case counts, failures/skips, source/fixture/profile/artifact hashes and retained failure evidence. Planned material cannot pass runtime qualification.

Evidence: Separate progress entry `DOC-1.34` links canonical pages, source/example manifest and focused artifacts.
Handoff: Last completed page/fixture/check, exact unresolved dependency and next bounded action.
Blocked behavior: Leave `DOC-1.34` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.35 — Teach custom extensions with block, mark and behavior examples

- [ ] DOC-1.35 Teach custom extensions with block, mark and behavior examples.

Purpose: Teach custom extensions with block, mark and behavior examples as one bounded reader-facing documentation surface.
Context: `content/docs/extensions/custom/`; `examples/custom-extensions/`; `tests/docs-custom-extensions.test.mjs`; `examples/manifest.json`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.34.
Session scope: One named section or example family, normally 15–45 minutes plus focused validation. Reuse owning-task consumers rather than implement editor features; propose a controller-reviewed split if needed. Conceptual source material may proceed before qualified artifacts; executable/support acceptance requires its exact profile evidence.
Acceptance: Original callout-block, highlight-mark and command/menu examples explain portable semantics, versioned descriptors, serialization and host presenters. Reuse qualified EXT-1.15, EXT-1.17, EXT-1.18, EXT-1.19, EXT-1.20 public authoring recipes for ASD-123 lookup-and-link, platform-first spellcheck with off/custom modes and separate autocorrection, custom parsing and safe URL insertion; not-found keeps literal text and stale async work cannot edit newer content. Show typed create/configure options and SDK-owned cleanup through public imports. Explain user-setting inheritance, unknown/unsupported platform capability and explicit custom-checker activation using the platform editing contract; do not imply bundled dictionaries or duplicate platform checking. Unsupported editing/rendering remains explicit; examples do not promise Tiptap runtime/plugin compatibility.

Implementation:

- [ ] DOC-1.35-I1 Reuse qualified public extension entry points and owning extension fixtures to build a callout containing Project kickoff content, highlight Friday and add a local command/menu action. Show configuration, validation, Markdown/semantic interchange, unknown-extension preservation, history, cancellation and disposal. Consume EXT-1.20's checked recipe source ranges for behavior/mark/atom authoring, task lookup, spelling, parsing and URL insertion; do not implement another matcher, resolver or editor. Keep advanced asset hosting separate from the one-import beginner path. Use qualified web presenters; native/terminal recipes consume their actual binding evidence or stay conceptual. Require EQL-1.9 immutable candidate identities for enhanced executable examples.

Validation:

- [ ] DOC-1.35-V1 Create/run `node --test tests/docs-custom-extensions.test.mjs` from the exact immutable extension consumer; compare independent validation/serialization/history/unknown-data expectations and cleanup. Do not rerun absent platform qualification. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Create named checks before use; record command exits, nonzero case counts, failures/skips, source/fixture/profile/artifact hashes and retained failure evidence. Planned material cannot pass runtime qualification.

Evidence: Separate progress entry `DOC-1.35` links canonical pages, source/example manifest and focused artifacts.
Handoff: Last completed page/fixture/check, exact unresolved dependency and next bounded action.
Blocked behavior: Leave `DOC-1.35` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.36 — Create an examples gallery backed by complete consumers

- [ ] DOC-1.36 Create an examples gallery backed by complete consumers.

Purpose: Create an examples gallery backed by complete consumers as one bounded reader-facing documentation surface.
Context: `content/docs/examples/`; `examples/gallery/`; `tests/docs-example-gallery.test.mjs`; `examples/manifest.json`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.5.
Session scope: One named section or example family, normally 15–45 minutes plus focused validation. Reuse owning-task consumers rather than implement editor features; propose a controller-reviewed split if needed. Conceptual source material may proceed before qualified artifacts; executable/support acceptance requires its exact profile evidence.
Acceptance: Gallery entries expose full source/downloads, immutable artifacts, capability labels, fixture inputs, expected outcomes and cleanup for ticket description, collaborative note and structured report. Optional interactive embeds use the actual editor and no hidden backend/model calls.

Implementation:

- [ ] DOC-1.36-I1 Curate existing task-owned consumers rather than duplicate them: browser/React basic editor, toolbar, ticket description, prepared local collaborative note and structured report with qualified code/table/asset profiles. Add filters for task/platform/feature/status, links to concepts/API/extension/migration pages and copyable checked snippets. Include loading, read-only, reset/export and dispose paths; reuse the real playground for optional live examples, and expose unavailable profiles without fake working demos.

Validation:

- [ ] DOC-1.36-V1 Create/run `node --test tests/docs-example-gallery.test.mjs` for manifest/source-range/download/profile link integrity and expected scenario outcomes; execute applicable packaged consumers only. Run `npm run check`, `zola check --skip-external-links` and `zola build`; inspect keyboard/mobile navigation and live reset/cleanup where available, then close test tabs and stop task previews. Create named checks before use; record command exits, nonzero case counts, failures/skips, source/fixture/profile/artifact hashes and retained failure evidence. Planned material cannot pass runtime qualification.

Evidence: Separate progress entry `DOC-1.36` links canonical pages, source/example manifest and focused artifacts.
Handoff: Last completed page/fixture/check, exact unresolved dependency and next bounded action.
Blocked behavior: Leave `DOC-1.36` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.37 — Publish task recipes using qualified example sources

- [ ] DOC-1.37 Publish task recipes using qualified example sources.

Purpose: Publish task recipes using qualified example sources as one bounded reader-facing documentation surface.
Context: `content/docs/guides/recipes/`; `examples/recipes/`; `tests/docs-recipes.test.mjs`; `examples/manifest.json`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.5, DOC-1.31.
Session scope: One named section or example family, normally 15–45 minutes plus focused validation. Reuse owning-task consumers rather than implement editor features; propose a controller-reviewed split if needed. Conceptual source material may proceed before qualified artifacts; executable/support acceptance requires its exact profile evidence.
Acceptance: Recipes explain a reader task through concrete input/action/output, errors and recovery, with source-manifest links rather than copied divergent snippets. Optional upstream features use their independent evidence gates.

Implementation:

- [ ] DOC-1.37-I1 Build the recipe index and checked walkthroughs from existing consumer sources: an accessible bold/heading/undo toolbar, Markdown paste with expected semantic output, a quota/save-failure recovery path and a prepared two-view reconnect scenario. Link DOC-1.6/1.7/1.8 sources for import preview/cancel, cancelled upload, internal-link denial and host operations when qualified; pending recipes remain labeled. Do not reimplement those features or conceal missing profile evidence.
- [ ] DOC-1.37-I2 Derive two recipes from SDK-1.10's SHR-01–SHR-08 consumers: task-description plus comment-body editors on one page, and task-description/document-body configurations across site routes. Show shared immutable engine/optional assets with isolated handles/history/storage/permissions, first versus incremental loading, loading failure/retry, disposal and client/full-navigation differences. Verify example asset URLs/chunk manifests and independent edit/save outcomes in DOC-1.37-V1; link exact profile/receipt revisions and disclose cache limits. Reuse the owning SDK examples; unqualified future document/code features remain planned.

Validation:

- [ ] DOC-1.37-V1 Create/run `node --test tests/docs-recipes.test.mjs` for source-range/fixture consistency and independent success/error/cancel outcomes in qualified consumers; missing advanced capability runs remain unqualified. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Create named checks before use; record command exits, nonzero case counts, failures/skips, source/fixture/profile/artifact hashes and retained failure evidence. Planned material cannot pass runtime qualification.

Evidence: Separate progress entry `DOC-1.37` links canonical pages, source/example manifest and focused artifacts.
Handoff: Last completed page/fixture/check, exact unresolved dependency and next bounded action.
Blocked behavior: Leave `DOC-1.37` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.38 — Add reproducible troubleshooting and recovery guides

- [ ] DOC-1.38 Add reproducible troubleshooting and recovery guides.

Purpose: Add reproducible troubleshooting and recovery guides as one bounded reader-facing documentation surface.
Context: `content/docs/troubleshooting/`; `examples/troubleshooting/`; `tests/docs-troubleshooting.test.mjs`; `examples/manifest.json`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.5, DOC-1.31.
Session scope: One named section or example family, normally 15–45 minutes plus focused validation. Reuse owning-task consumers rather than implement editor features; propose a controller-reviewed split if needed. Conceptual source material may proceed before qualified artifacts; executable/support acceptance requires its exact profile evidence.
Acceptance: Each troubleshooting page starts with an observable symptom, exact diagnostic and bounded deterministic reproduction, then preserves data through a tested recovery; unsupported versions/platforms and destructive recovery boundaries are explicit.

Implementation:

- [ ] DOC-1.38-I1 Reuse prepared failure fixtures for mismatched JS/WASM assets, unsupported schema/custom content, loading/SSR boundaries, quota/save failure, revoked permission and stale command targets. Show expected diagnostics and recovery through retry, preserved backup/export or compatible reopen; distinguish transport sync from durable save. Link compatibility, migration, versioned APIs and DOC-1.14 upgrade/rollback procedure; never recommend silently clearing documents or downgrading schemas.

Validation:

- [ ] DOC-1.38-V1 Create/run `node --test tests/docs-troubleshooting.test.mjs` with prepared failure transports and exact qualified consumers; assert independent diagnostic and preservation/recovery outcomes. Run `npm run check`, `zola check --skip-external-links` and `zola build`. Create named checks before use; record command exits, nonzero case counts, failures/skips, source/fixture/profile/artifact hashes and retained failure evidence. Planned material cannot pass runtime qualification.

Evidence: Separate progress entry `DOC-1.38` links canonical pages, source/example manifest and focused artifacts.
Handoff: Last completed page/fixture/check, exact unresolved dependency and next bounded action.
Blocked behavior: Leave `DOC-1.38` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.
