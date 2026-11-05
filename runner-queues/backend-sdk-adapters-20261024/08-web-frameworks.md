# Deliver browser framework lifecycle adapters

Status: PLANNED

## Goal and entry conditions

Deliver the 08-web-frameworks milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: 00-contracts BSC-1.6/1.7 and 03-typescript-node BTS-1.8 provide lifecycle and autosave orchestration. Existing React/Astro packages from track 08 are reused. Next server endpoints need BTS-1.7; other UI families need only one prepared conforming backend, not every language SDK.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is functional delivery. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/08-web-frameworks.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

## Epic BWF-1 — Deliver browser framework lifecycle adapters

### Task BWF-1.1 — Align the existing React and Astro bindings

- [ ] BWF-1.1 Align the existing React and Astro bindings.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: packages/react/; packages/astro/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Existing bindings expose shared save-state/transport configuration without new editor ownership, SSR side effects or repeated content imports; current public entry points are reused.

Implementation:

- [ ] BWF-1.1-I1 Align the existing React and Astro bindings. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BWF-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BWF-1.1`: One existing packed binding consumer per package mounts/disposes with prepared save transport and no cross-editor state leakage. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BWF-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BWF-1.2 — Add the Next.js client boundary

- [ ] BWF-1.2 Add the Next.js client boundary.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/web/nextjs/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BWF-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Client component wraps the React editor with SSR-safe lazy runtime loading and optional server route integration; navigation preserves or explicitly flushes recovery state.

Implementation:

- [ ] BWF-1.2-I1 Add the Next.js client boundary. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BWF-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BWF-1.2`: Server render creates no editor/transport; one local client mount/save/route-dispose uses the actual binding. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BWF-1.2 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BWF-1.3 — Add the Vue composition adapter

- [ ] BWF-1.3 Add the Vue composition adapter.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/web/vue/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Component/composable owns one editor session, reactive save status and explicit create/reset semantics; prop updates never re-import the document or duplicate history.

Implementation:

- [ ] BWF-1.3-I1 Add the Vue composition adapter. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BWF-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BWF-1.3`: One prepared reactive parent update leaves CRDT identity/history stable and one dispose releases subscriptions. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BWF-1.3 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BWF-1.4 — Add the Nuxt module and client plugin

- [ ] BWF-1.4 Add the Nuxt module and client plugin.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/web/nuxt/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BWF-1.3.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Client-only registration reuses Vue ownership and respects server request isolation, route lifetime and application endpoint configuration.

Implementation:

- [ ] BWF-1.4-I1 Add the Nuxt module and client plugin. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BWF-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BWF-1.4`: One server-render plus client-hydration smoke creates exactly one client editor and zero server sessions. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BWF-1.4 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BWF-1.5 — Add the Svelte action/component adapter

- [ ] BWF-1.5 Add the Svelte action/component adapter.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/web/svelte/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Lifecycle cleanup, stores and form hooks wrap the imperative SDK without content ownership loops; multiple editors keep independent state.

Implementation:

- [ ] BWF-1.5-I1 Add the Svelte action/component adapter. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BWF-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BWF-1.5`: One local two-editor mount/update/dispose fixture saves only the selected editor and restores its exact checkpoint. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BWF-1.5 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BWF-1.6 — Add SvelteKit client/server boundaries

- [ ] BWF-1.6 Add SvelteKit client/server boundaries.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/web/sveltekit/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BWF-1.5.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Browser binding reuses Svelte and server handlers use the common authenticated authority contract; load/navigation never shares a global session or initializes an existing empty document.

Implementation:

- [ ] BWF-1.6-I1 Add SvelteKit client/server boundaries. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BWF-1.6-V1 Run `node scripts/sdk-adapter-delivery.mjs BWF-1.6`: One SSR/hydration/route flow with prepared endpoint preserves initialized-empty identity and disposes owned work. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BWF-1.6 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BWF-1.7 — Add the Angular component and service

- [ ] BWF-1.7 Add the Angular component and service.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/web/angular/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Explicit component/service scope, change detection and ControlValueAccessor integration preserve one document lifetime; disabled/read-only/reset behavior respects engine admission.

Implementation:

- [ ] BWF-1.7-I1 Add the Angular component and service. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BWF-1.7-V1 Run `node scripts/sdk-adapter-delivery.mjs BWF-1.7`: One local form fixture verifies read-only denial and explicit reset/new identity without a feedback import loop. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BWF-1.7 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BWF-1.8 — Define common forms and multi-editor recipes

- [ ] BWF-1.8 Define common forms and multi-editor recipes.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: examples/sdk-adapters/web/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BWF-1.1, BWF-1.2, BWF-1.3, BWF-1.4, BWF-1.5, BWF-1.6, BWF-1.7.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Each framework documents uncontrolled canonical ownership, explicit form submission/validation/reset, multiple instances and optional collaboration; capability differences are declared.

Implementation:

- [ ] BWF-1.8-I1 Define common forms and multi-editor recipes. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BWF-1.8-V1 Run `node scripts/sdk-adapter-delivery.mjs BWF-1.8`: Compile the named minimal framework consumers and execute one shared prepared submit/conflict transcript; comprehensive matrix is deferred. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BWF-1.8 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Summarize delivered source interfaces and capability flags, focused selectors/results, true prerequisite gaps and remaining final qualification in `.roadmap-runner/backend-sdk-adapters-20261024/08-web-frameworks.progress.md`. Do not copy hashes/delivery summaries into this source. The two final testing files own comprehensive case authoring and qualification; functional completion alone is not whole-plan completion.
