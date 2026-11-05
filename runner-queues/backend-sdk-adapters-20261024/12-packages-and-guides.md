# Make adapters installable and document adoption

Status: PLANNED

## Goal and entry conditions

Deliver the 12-packages-and-guides milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: Relevant preceding functional file must supply its own package API and focused delivery result. This file consumes only the family a task documents, not all files by default; the combined capability manifest requires every planned family disposition. Existing public-docs/migration deferrals remain: these are new integration guides, not deferred editor-content migration tooling.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is functional delivery. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/12-packages-and-guides.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

## Epic BPG-1 — Make adapters installable and document adoption

### Task BPG-1.1 — Write the PHP SDK and PHP adapter adoption guide

- [ ] BPG-1.1 Write the PHP SDK and PHP adapter adoption guide.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/php/README.md; examples/sdk-adapters/laravel/README.md; examples/sdk-adapters/filament/README.md; examples/sdk-adapters/drupal/README.md; sdk/contracts/guides/laravel.md.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Guide shows standalone PHP SDK use, the thin Laravel wrapper, optional Filament Resource field and direct-SDK Drupal field module, plus local install, application policy, new adapter-table migration, validator topology, editor mount, DB save/reopen, conflicts and optional collaboration; every step identifies its actual package and capability.

Implementation:

- [ ] BPG-1.1-I1 Write the PHP SDK and PHP adapter adoption guide. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPG-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BPG-1.1`: Follow the documented minimal local flow with prepared content using the delivered Laravel example; reuse unchanged package checks. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPG-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPG-1.2 — Write backend language recipes

- [ ] BPG-1.2 Write backend language recipes.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/contracts/guides/backend/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Each language has a minimal client and framework-owned/delegated-authority recipe plus exact policy/transaction/validator wiring; no language is told to recreate the wire contract.

Implementation:

- [ ] BPG-1.2-I1 Write backend language recipes. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPG-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BPG-1.2`: Compare documented APIs to delivered declarations and compile only changed recipe entry points for PHP/TS/Python/Go/Rust/JVM/.NET/Ruby/C. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPG-1.2 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPG-1.3 — Write web framework integration recipes

- [ ] BPG-1.3 Write web framework integration recipes.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/contracts/guides/web/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: React/Astro/Next/Vue/Nuxt/Svelte/SvelteKit/Angular recipes state SSR, form ownership, explicit reset, multiple editors and optional sync behavior with one canonical format.

Implementation:

- [ ] BPG-1.3-I1 Write web framework integration recipes. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPG-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BPG-1.3`: Compile changed minimal recipe consumers and check links against delivered package source; reuse retained SSR evidence. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPG-1.3 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPG-1.4 — Write native and desktop embedding recipes

- [ ] BPG-1.4 Write native and desktop embedding recipes.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/contracts/guides/native/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Apple/Android/Windows/Linux/Flutter/RN/Electron/Tauri/Qt headless docs declare real host, thread/lifetime, native vs web surface and exact unsupported combinations; no device qualification is inferred from compilation.

Implementation:

- [ ] BPG-1.4-I1 Write native and desktop embedding recipes. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPG-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BPG-1.4`: Compare each documented host to its capability declaration and compile changed snippets only on an available declared toolchain. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPG-1.4 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPG-1.5 — Add local packaging and install manifests

- [ ] BPG-1.5 Add local packaging and install manifests.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: scripts/sdk-adapter-packages.mjs; sdk/contracts/distributions.json.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Separate local Composer distributions preserve PHP SDK → Laravel → optional Filament and PHP SDK → Drupal dependency chains; reproducible local Composer/npm/PyPI-wheel/Go/Cargo/Maven/NuGet/gem/C/C++/Swift/Kotlin/Dart distributions and notices are defined; generated/packed/binary outputs stay outside Git and no registry publish occurs.

Implementation:

- [ ] BPG-1.5-I1 Add local packaging and install manifests. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPG-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BPG-1.5`: Build/install one changed consumer per supported distribution into ignored task-owned directories; missing toolchains remain unqualified, never fabricated passes. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPG-1.5 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPG-1.6 — Assemble the authored support and handoff register

- [ ] BPG-1.6 Assemble the authored support and handoff register.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/contracts/support.json; sdk/contracts/qualification.json.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BPG-1.1, BPG-1.2, BPG-1.3, BPG-1.4, BPG-1.5.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Every package maps runtime/framework/DB ranges and optional capabilities to source owner, focused results, final test owner and existing track 43/release handoff; planned/delivered/qualified remain separate.

Implementation:

- [ ] BPG-1.6-I1 Assemble the authored support and handoff register. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPG-1.6-V1 Run `node scripts/sdk-adapter-delivery.mjs BPG-1.6`: Validate source declarations and count coverage of all matrix rows; a missing result leaves its qualification flag false and final testing outstanding. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPG-1.6 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Summarize delivered source interfaces and capability flags, focused selectors/results, true prerequisite gaps and remaining final qualification in `.roadmap-runner/backend-sdk-adapters-20261024/12-packages-and-guides.progress.md`. Do not copy hashes/delivery summaries into this source. The two final testing files own comprehensive case authoring and qualification; functional completion alone is not whole-plan completion.
