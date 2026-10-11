# Deliver public documentation and the real editor demo

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `docs`; paths below are workspace-relative unless prefixed `../architecture/` or another explicit sibling. Read `../architecture/specs/public-docs-demo.md` and only the active task's named context. Planned paths and commands are created by their owning task. This source describes delivery; it is not a capability claim or live progress.

Required upstream tracks: none for documentation bootstrap at reviewed immutable source/implementation revisions with passing evidence. Tasks name additional SDK/profile gates where required; documentation bootstrap does not wait for complete editor delivery. Local Dependencies fields refer only to this file.

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
Acceptance: Web/React/native/CLI paths, concepts, recipes and references are discoverable; current versus planned support is visible on entry pages.

Implementation:

- [ ] DOC-1.3-I1 Map the public information architecture to real pages; add consistent prerequisites, tested-version labels, failure/recovery sections and migration links without copying architecture roadmaps.

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
Acceptance: Generated signatures match named qualified artifacts; absent/unqualified APIs never receive install-ready examples. Capability tables derive from core profiles.

Implementation:

- [ ] DOC-1.4-I1 Consume immutable core public exports/binding metadata and roadmap30 profile schema; record external entry evidence from08 and30 before claiming executable API coverage. Create generation drift checks.

Validation:

- [ ] DOC-1.4-V1 `node scripts/generate-reference.mjs --check`; `node --test tests/reference-profile.test.mjs`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.4` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task DOC-1.5 — Publish executable web and React quickstarts

- [ ] DOC-1.5 Publish executable web and React quickstarts.

Purpose: Publish executable web and React quickstarts as one bounded integration or qualification boundary.
Context: `examples/web/`; `examples/react/`; `examples/releases.json`; `../architecture/specs/public-docs-demo.md`.
Dependencies: DOC-1.4.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Tutorials install real pinned registry artifacts, demonstrate lifecycle/read-only/save errors and dispose cleanly without workspace aliases.

Implementation:

- [ ] DOC-1.5-I1 Require08 and10 release-consumer evidence and the qualified package version; create plain browser and React/SSR consumers and derive snippets from tested files.

Validation:

- [ ] DOC-1.5-V1 `npm run check:examples -- --suite web-react`; create the dispatcher and reject unknown/empty suites. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

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

- [ ] DOC-1.6-I1 External task gate: require EQL-1.9 immutable candidate publication receipts plus25/26 evidence for enhanced features; build prepared-host examples from public extension entry points. Clearly separate auto-paste metadata policy from permission or document-open fetch.

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

- [ ] DOC-1.7-I1 Require27 and each claimed platform’s31–35 package-consumer evidence for runnable examples. Unavailable platforms retain explicitly conceptual guides and no executable-support claim; this documentation task does not require every native platform to qualify. Generate the support table and author short file-picker/preview/cancel/import/export recipes per qualified host.

Validation:

- [ ] DOC-1.7-V1 `npm run check:examples -- --suite formats-native`; native examples use recorded platform checks and cannot pass on missing devices. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

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

- [ ] DOC-1.8-I1 Require14 and28 evidence for runnable service instructions. Provide a local reference deployment and operational checklist without provisioning paid services or adding credentials.

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

- [ ] DOC-1.12-I1 Use actual production build; fix navigation, long-content and interaction failures. Record manual accessibility evidence, generator/search indexes, redistributable asset licenses and raw load samples.

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
Acceptance: SDK/profile references resolve to immutable releases and docs cannot silently advertise unqualified or removed capabilities.

Implementation:

- [ ] DOC-1.14-I1 Add release-note/migration/update procedure with owner and exact profile inputs; make snippet/reference drift fail CI. Keep internal architecture tasks out of public navigation.

Validation:

- [ ] DOC-1.14-V1 `node scripts/check-release-links.mjs`; `npm run check`; `npm run check:examples -- --suite published-profile`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `DOC-1.14` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `DOC-1.14` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.
