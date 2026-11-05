# Deliver the standalone PHP SDK

Status: PLANNED

## Goal and entry conditions

Deliver the 01a-php-sdk milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: 00-contracts BSC-1.2/1.5/1.7 and 01-authority-and-storage BAS-1.2/1.6 supply the unversioned current DTOs, validator bridge and checkpoint authority. BPH-1.10 additionally needs BAS-1.7; database profiles need the selected real local engine. No Laravel, Symfony, Filament or Livewire implementation is a prerequisite. Record source selectors/results in 01a-php-sdk.progress.md.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is functional delivery. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/01a-php-sdk.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

PHP SDK boundary: plain Composer/PHP consumers own no framework dependency. The SDK owns envelope/receipt validation, canonical validator calls, repository/transaction interfaces, conditional commit orchestration, retries and optional append/resume. Laravel and Symfony only map framework services to these interfaces. See the [layering contract](../../specs/backend-sdk-adapters.md#php-sdk-laravel-wrapper-and-filament).

## Epic BPH-1 — Deliver the standalone PHP SDK

### Task BPH-1.1 — Implement the PHP envelope and HTTP client

- [ ] BPH-1.1 Implement the PHP envelope and HTTP client.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/php/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Composer autoload exposes exact binary/base64 handling, scoped identity, typed errors and caller-supplied transport without Laravel/Illuminate, Filament or Livewire dependencies; loading the library performs no I/O. A plain PHP application can use it directly.

Implementation:

- [ ] BPH-1.1-I1 Implement the PHP envelope and HTTP client. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPH-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BPH-1.1`: A plain PHP consumer without Laravel/Filament round-trips non-ASCII current checkpoint bytes through a prepared HTTP response and preserves unknown bounded fields. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPH-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPH-1.2 — Implement PHP conditional saves and commit recovery

- [ ] BPH-1.2 Implement PHP conditional saves and commit recovery.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/php/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BPH-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Framework-independent create/load/save client operations use durable expected revision, stable operation keys and explicit commit-unknown lookup; canceled writes are not reported rolled back. No Laravel service, model or facade appears in the SDK API.

Implementation:

- [ ] BPH-1.2-I1 Implement PHP conditional saves and commit recovery. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPH-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BPH-1.2`: One prepared lost reply resolves the same operation; a different payload under that key rejects and a stale revision stays conflicted. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPH-1.2 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPH-1.9 — Implement framework-neutral PHP persistence orchestration

- [ ] BPH-1.9 Implement framework-neutral PHP persistence orchestration.

Purpose: Deliver this integration boundary while keeping shared persistence behavior in the framework-independent PHP SDK.
Deliverable: sdk/php/src/Persistence/; sdk/php/storage/pdo/; sdk/php/src/Admission/.
Context: [SDK contract: PHP SDK, Laravel wrapper and Filament](../../specs/backend-sdk-adapters.md#php-sdk-laravel-wrapper-and-filament); actual source exports and named predecessor results only.
Dependencies: BPH-1.2.
Independent work: Other validated entry/local boundaries remain eligible; optional UI and collaboration do not gate the plain PHP client.
Session scope: One boundary, 15–45 minutes including focused checks; split before expanding into a missing shared API.
Acceptance: The SDK owns application-supplied policy/repository/transaction ports, private Rust validation calls, predecessor-bound CAS, exact bytes, operation-ledger outcomes and after-commit receipt construction. A minimal optional PDO SQLite repository runs in plain PHP; framework adapters map their connections/transactions without reimplementing this algorithm. CMS consumers additionally use SDK-owned immutable snapshot read/retain/release interfaces; Drupal BDR-1.3 repairs a missing port with this owner before claiming revision support, without a second history store.

Implementation:

- [ ] BPH-1.9-I1 Connect the existing shared authority/transaction contract to framework-neutral PHP services and one minimal PDO repository. Keep application authentication callbacks and injected connection ownership explicit. Register one focused delivery selector; defer broad test authoring to the final testing files.

Validation:

- [ ] BPH-1.9-V1 Run `node scripts/sdk-adapter-delivery.mjs BPH-1.9`: In plain PHP without Laravel/Filament, save/reopen one current checkpoint through actual local SQLite, then force rollback and a stale predecessor; only the committed write receives a receipt. Budget: 1–3 minutes or at most 5 minutes for local build/bootstrap; reuse unchanged passing results.

Evidence: The ignored progress path above records source inputs, command/runtime/exit and meaningful executed/passed/failed/skipped counts; retain only active failure diagnostics.
Handoff: Delivered interface, exact last substep, missing prerequisite and next bounded action.
Blocked behavior: Leave BPH-1.9 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPH-1.5 — Add MySQL and MariaDB transaction profiles

- [ ] BPH-1.5 Add MySQL and MariaDB transaction profiles.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/php/storage/pdo/; sdk/contracts/support.json
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BPH-1.9
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: SDK-owned PDO profiles select and document each supported MySQL and MariaDB runtime, binary column/unique key behavior and CAS/isolation policy. Shared driver semantics are available without Laravel; Eloquent only maps the application connection/transaction. MariaDB results are independent of MySQL results.

Implementation:

- [ ] BPH-1.5-I1 Add MySQL and MariaDB transaction profiles. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BPH-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BPH-1.5`: Run one two-connection same-document CAS fixture per selected real local backend; missing engines remain blocked/unqualified, never substituted by SQLite evidence. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BPH-1.5 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPH-1.10 — Implement optional PHP append and resume services

- [ ] BPH-1.10 Implement optional PHP append and resume services.

Purpose: Deliver this integration boundary while keeping shared persistence behavior in the framework-independent PHP SDK.
Deliverable: sdk/php/src/Collaboration/; sdk/php/src/Receipts/.
Context: [SDK contract: PHP SDK, Laravel wrapper and Filament](../../specs/backend-sdk-adapters.md#php-sdk-laravel-wrapper-and-filament); actual source exports and named predecessor results only.
Dependencies: BPH-1.9.
Independent work: Other validated entry/local boundaries remain eligible; optional UI and collaboration do not gate the plain PHP client.
Session scope: One boundary, 15–45 minutes including focused checks; split before expanding into a missing shared API.
Acceptance: Append/read/resume/commit lookup and deduplication behavior live in the PHP SDK over BAS-1.7; exact update/receipt scope is shared by plain PHP, Laravel and Symfony. Baseline checkpoint-only use imports no broadcaster, queue or WebSocket service.

Implementation:

- [ ] BPH-1.10-I1 Expose the optional update/receipt services through the existing injected transport and persistence ports, retaining original operation IDs and typed errors. Register one focused delivery selector; defer broad test authoring to the final testing files.

Validation:

- [ ] BPH-1.10-V1 Run `node scripts/sdk-adapter-delivery.mjs BPH-1.10`: Use the shared prepared duplicate-append/lost-response transcript from plain PHP and confirm one operation outcome, exact covered updates and no optional-service boot for checkpoint-only use. Budget: 1–3 minutes or at most 5 minutes for local build/bootstrap; reuse unchanged passing results.

Evidence: The ignored progress path above records source inputs, command/runtime/exit and meaningful executed/passed/failed/skipped counts; retain only active failure diagnostics.
Handoff: Delivered interface, exact last substep, missing prerequisite and next bounded action.
Blocked behavior: Leave BPH-1.10 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BPH-1.11 — Package and demonstrate plain PHP usage

- [ ] BPH-1.11 Package and demonstrate plain PHP usage.

Purpose: Deliver this integration boundary while keeping shared persistence behavior in the framework-independent PHP SDK.
Deliverable: sdk/php/composer.json; sdk/php/README.md; examples/sdk-adapters/php/.
Context: [SDK contract: PHP SDK, Laravel wrapper and Filament](../../specs/backend-sdk-adapters.md#php-sdk-laravel-wrapper-and-filament); actual source exports and named predecessor results only.
Dependencies: BPH-1.1, BPH-1.2, BPH-1.9.
Independent work: Other validated entry/local boundaries remain eligible; optional UI and collaboration do not gate the plain PHP client.
Session scope: One boundary, 15–45 minutes including focused checks; split before expanding into a missing shared API.
Acceptance: A local Composer package and minimal plain PHP example install and perform canonical create/save/load without Laravel/Illuminate, Symfony, Filament or Livewire. Optional drivers/semantic companion/collaboration requirements are explicit; no registry publish occurs.

Implementation:

- [ ] BPH-1.11-I1 Add authored install metadata, license/notices and a minimal fixture-backed usage recipe. Keep packed dependencies and generated output ignored and separate from source. Register one focused delivery selector; defer broad test authoring to the final testing files.

Validation:

- [ ] BPH-1.11-V1 Run `node scripts/sdk-adapter-delivery.mjs BPH-1.11`: Install into a fresh ignored plain PHP consumer, inspect the dependency graph for framework absence and run the documented SQLite checkpoint save/reopen using prepared content. Budget: 1–3 minutes or at most 5 minutes for local build/bootstrap; reuse unchanged passing results.

Evidence: The ignored progress path above records source inputs, command/runtime/exit and meaningful executed/passed/failed/skipped counts; retain only active failure diagnostics.
Handoff: Delivered interface, exact last substep, missing prerequisite and next bounded action.
Blocked behavior: Leave BPH-1.11 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Record delivered interfaces, actual selectors/results and remaining qualification in the separate ignored progress path above. Reuse accepted evidence; the two final testing files own comprehensive cases and full-plan qualification. No publication or runner start is authorized.
