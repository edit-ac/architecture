# Deliver the thin Laravel and Symfony wrappers

Status: PLANNED

## Goal and entry conditions

Deliver the 02-php-laravel-symfony milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: 01a-php-sdk BPH-1.1/1.2/1.9/1.11 provide the standalone Composer SDK, validation/persistence ports and focused plain-PHP results. BPH-1.6 additionally needs SDK BPH-1.10 and the shared BAS-1.7 authority. Optional MySQL/MariaDB claims require SDK BPH-1.5 only. Read 01a-php-sdk.progress.md for exact selectors; no Filament dependency is required.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is functional delivery. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/02-php-laravel-symfony.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

Wrapper boundary: require the standalone PHP SDK and adapt only Laravel container/config, application policies/routes, Eloquent/connection transactions and after-commit events. Symfony maps its own services to the same SDK. No duplicate DTO decoder, semantic validator, retry state machine, ledger or receipt algorithm. See the [layering contract](../../specs/backend-sdk-adapters.md#php-sdk-laravel-wrapper-and-filament).

## Epic BPH-1 — Deliver the thin Laravel and Symfony wrappers

### Task BPH-1.3 — Add the Laravel service provider and policy boundary

- [ ] BPH-1.3 Add the Laravel service provider and policy boundary.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/laravel/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (validated standalone PHP SDK entry only)
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: A separate Laravel Composer wrapper requires the PHP SDK and binds configuration/container/routes to its services. Middleware calls the application tenant/document policy; protocol, semantic validation, persistence orchestration and retry/receipt rules remain SDK-owned. No default allow policy or Filament dependency exists.

Implementation:

- [ ] BPH-1.3-I1 Add the Laravel service provider and policy boundary. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPH-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BPH-1.3`: Boot one local Laravel application with prepared principals; one allowed and one denied request have the expected typed outcomes. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPH-1.3 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPH-1.4 — Bind Eloquent to PHP SDK transactions

- [ ] BPH-1.4 Bind Eloquent to PHP SDK transactions.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/laravel/database/; adapters/backend/laravel/src/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BPH-1.3.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Thin Eloquent/connection adapters map the existing application transaction and schema to SDK-owned repository/commit interfaces. Adapter table migrations and model bindings preserve exact checkpoint/revision/operation data; SDK receipts/events follow actual commit. No second CAS, ledger or retry implementation exists in Laravel.

Implementation:

- [ ] BPH-1.4-I1 Bind Eloquent to PHP SDK transactions. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPH-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BPH-1.4`: Save and reopen using real local SQLite, then force a rollback and verify neither checkpoint nor committed event changed. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPH-1.4 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPH-1.6 — Add Laravel collaboration and background integration

- [ ] BPH-1.6 Add Laravel collaboration and background integration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/laravel/src/Collaboration/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BPH-1.4.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Routes and optional Laravel queue/broadcast hooks delegate append/resume/commit lookup to PHP SDK BPH-1.10. Notifications follow commit and are not receipts; no duplicate update/receipt parser, mandatory Redis or broadcaster is added.

Implementation:

- [ ] BPH-1.6-I1 Add Laravel collaboration and background integration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPH-1.6-V1 Run `node scripts/sdk-adapter-delivery.mjs BPH-1.6`: Duplicate one prepared append and deliver one after-commit notification; only one operation receipt and retained resume coverage result. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPH-1.6 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPH-1.7 — Build the Laravel editor save/load example

- [ ] BPH-1.7 Build the Laravel editor save/load example.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: examples/sdk-adapters/laravel/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BPH-1.4.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: A documented Blade/Vite page mounts the real editor, saves to the application DB and reopens formatting/unknown data; it displays local vs remote pending/conflict states and preserves unsaved work on denial.

Implementation:

- [ ] BPH-1.7-I1 Build the Laravel editor save/load example. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPH-1.7-V1 Run `node scripts/sdk-adapter-delivery.mjs BPH-1.7`: Run one local browser create/edit/save/reopen flow plus a prepared stale-save conflict using the actual adapter; capture concise counts and tear down owned resources. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPH-1.7 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPH-1.8 — Add the Symfony adapter

- [ ] BPH-1.8 Add the Symfony adapter.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/symfony/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (validated standalone PHP SDK entry only)
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Symfony route/security and Doctrine transaction callbacks wrap the same PHP SDK policy/repository/validator/receipt services; no dependency on Laravel or Filament and no second save algorithm. Application authorization and after-commit semantics remain required.

Implementation:

- [ ] BPH-1.8-I1 Add the Symfony adapter. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPH-1.8-V1 Run `node scripts/sdk-adapter-delivery.mjs BPH-1.8`: One local Symfony SQLite save/reopen and denied-policy smoke preserve exact bytes and emit no receipt for denial. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPH-1.8 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Record delivered interfaces, actual selectors/results and remaining qualification in the separate ignored progress path above. Reuse accepted evidence; the two final testing files own comprehensive cases and full-plan qualification. No publication or runner start is authorized.
