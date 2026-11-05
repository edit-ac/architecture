# Deliver Python and its backend framework adapters

Status: PLANNED

## Goal and entry conditions

Deliver the 04-python milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: 00-contracts BSC-1.2/1.5/1.7 and 01-authority-and-storage BAS-1.2/1.6; append consumers additionally need BAS-1.7. The PHP/Node packages are examples of contract usage, not code prerequisites.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is functional delivery. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/04-python.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

## Epic BPY-1 — Deliver Python and its backend framework adapters

### Task BPY-1.1 — Implement Python envelopes and synchronous client

- [ ] BPY-1.1 Implement Python envelopes and synchronous client.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/python/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Typed models retain exact bytes, bounded unknown data and integer values; an injected synchronous transport maps the agreed errors and performs no import-time work.

Implementation:

- [ ] BPY-1.1-I1 Implement Python envelopes and synchronous client. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPY-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BPY-1.1`: One prepared fixture round-trip and local wheel/import consumer preserve the input digest. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPY-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPY-1.2 — Add asynchronous transport and cancellation

- [ ] BPY-1.2 Add asynchronous transport and cancellation.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/python/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BPY-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Async API shares the same models and save semantics; cancellation after a write yields an uncertain operation that can be looked up and clients close only owned transports.

Implementation:

- [ ] BPY-1.2-I1 Add asynchronous transport and cancellation. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPY-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BPY-1.2`: One prepared asynchronous timeout resolves through the same operation key; caller-owned transport remains open. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPY-1.2 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPY-1.3 — Implement saves and update receipt workflows

- [ ] BPY-1.3 Implement saves and update receipt workflows.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/python/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BPY-1.1, BPY-1.2.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Both clients expose conditional checkpoint save, incremental append/resume and commit lookup without divergent retry or receipt parsing.

Implementation:

- [ ] BPY-1.3-I1 Implement saves and update receipt workflows. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPY-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BPY-1.3`: Run the same prepared save/conflict transcript through synchronous and asynchronous clients and compare typed normalized outcomes. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPY-1.3 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPY-1.4 — Add SQLAlchemy repository transactions

- [ ] BPY-1.4 Add SQLAlchemy repository transactions.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/python/storage/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BPY-1.3.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Sync/async session lifetimes do not emit receipts before commit; scoped constraints and CAS survive a rollback and preserve exact binary values.

Implementation:

- [ ] BPY-1.4-I1 Add SQLAlchemy repository transactions. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPY-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BPY-1.4`: One actual SQLite transaction save/reopen/rollback through the repository, with one chosen async boundary checked if supported. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPY-1.4 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPY-1.5 — Add Django and DRF integration

- [ ] BPY-1.5 Add Django and DRF integration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/django/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BPY-1.3.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Django URLs/views and DRF serializers/permissions call application auth and use atomic transactions/on_commit semantics; DRF remains an optional adapter dependency.

Implementation:

- [ ] BPY-1.5-I1 Add Django and DRF integration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPY-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BPY-1.5`: One real local Django SQLite request/reopen plus a prepared permission rejection, with no after-commit event on rollback. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPY-1.5 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPY-1.6 — Add FastAPI and Starlette integration

- [ ] BPY-1.6 Add FastAPI and Starlette integration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/fastapi/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BPY-1.2, BPY-1.3, BPY-1.4.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Explicit lifespan/dependency wiring exposes bounded routes and async policy/storage/validator hooks; per-request tasks cannot leak or outlive a closed app.

Implementation:

- [ ] BPY-1.6-I1 Add FastAPI and Starlette integration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPY-1.6-V1 Run `node scripts/sdk-adapter-delivery.mjs BPY-1.6`: One local ASGI lifespan save/reopen and canceled request smoke; resource close counts match ownership. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPY-1.6 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPY-1.7 — Add Python application recipes

- [ ] BPY-1.7 Add Python application recipes.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: examples/sdk-adapters/python/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BPY-1.5, BPY-1.6.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Minimal Django and FastAPI apps document application policy and canonical storage plus optional collaboration without live providers or copied CRDT logic.

Implementation:

- [ ] BPY-1.7-I1 Add Python application recipes. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPY-1.7-V1 Run `node scripts/sdk-adapter-delivery.mjs BPY-1.7`: Execute one documented command per example against a prepared local store and compare one save/reopen result. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPY-1.7 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Summarize delivered source interfaces and capability flags, focused selectors/results, true prerequisite gaps and remaining final qualification in `.roadmap-runner/backend-sdk-adapters-20261024/04-python.progress.md`. Do not copy hashes/delivery summaries into this source. The two final testing files own comprehensive case authoring and qualification; functional completion alone is not whole-plan completion.
