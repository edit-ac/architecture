# Expose reusable authority and storage boundaries

Status: PLANNED

## Goal and entry conditions

Deliver the 01-authority-and-storage milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: 00-contracts: BSC-1.2/1.3/1.4/1.5/1.7 validated schema, fixtures and admission contract, with selectors/results in 00-contracts.progress.md. Inspect core/services/document-store and existing Session ports; reuse their real implemented portions. Missing semantic validation or commit coordination is repaired under the track 28 owner before its dependent task.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is functional delivery. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/01-authority-and-storage.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

## Epic BAS-1 — Expose reusable authority and storage boundaries

### Task BAS-1.1 — Expose the existing Rust staged validator

- [ ] BAS-1.1 Expose the existing Rust staged validator.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/reference/admission/; services/document-store/src/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: The existing engine validates detached current-format checkpoint/update inputs without live mutation and returns digest/predecessor-bound results; no second parser or CRDT is introduced.

Implementation:

- [ ] BAS-1.1-I1 Expose the existing Rust staged validator. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BAS-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BAS-1.1`: One current-format checkpoint validates and one incompatible envelope rejects with unchanged fixture state. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BAS-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BAS-1.2 — Implement the bounded private validation companion

- [ ] BAS-1.2 Implement the bounded private validation companion.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/reference/companion/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BAS-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: A local authenticated companion exposes only the agreed validator operations with deadlines, size limits and redacted typed failures; no caller-supplied fetch URL or storage mutation exists.

Implementation:

- [ ] BAS-1.2-I1 Implement the bounded private validation companion. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BAS-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BAS-1.2`: One prepared request and deadline failure through the actual local companion return the expected typed results; shut it down afterward. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BAS-1.2 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BAS-1.3 — Define repository migrations and transaction port

- [ ] BAS-1.3 Define repository migrations and transaction port.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/reference/repository/; sdk/contracts/storage.md.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Scoped document/checkpoint/update/operation records have binary-safe fields, revision CAS and uniqueness constraints; install migrations create adapter-owned tables without rewriting existing documents.

Implementation:

- [ ] BAS-1.3-I1 Define repository migrations and transaction port. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BAS-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BAS-1.3`: Apply and inspect the planned schema in a fresh task-owned SQLite file; existing fixture bytes remain byte-identical. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BAS-1.3 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BAS-1.4 — Implement the SQLite repository adapter

- [ ] BAS-1.4 Implement the SQLite repository adapter.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/reference/sqlite/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BAS-1.3.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Real SQLite commit/rollback owns checkpoint and operation outcome atomically; receipts are emitted after commit and exact idempotent retries return the original result.

Implementation:

- [ ] BAS-1.4-I1 Implement the SQLite repository adapter. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BAS-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BAS-1.4`: Execute one save/reopen and one rolled-back save using the same local file; compare exact bytes and ledger result. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BAS-1.4 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BAS-1.5 — Implement the PostgreSQL transaction adapter

- [ ] BAS-1.5 Implement the PostgreSQL transaction adapter.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/reference/postgres/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BAS-1.3.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Declared maintained PostgreSQL version and isolation support multi-process CAS, unique operation keys and exact binary bytes; no in-memory mutex substitutes for DB arbitration.

Implementation:

- [ ] BAS-1.5-I1 Implement the PostgreSQL transaction adapter. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BAS-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BAS-1.5`: Run one two-connection revision conflict on a task-owned local database with prepared credentials; if unavailable record a blocker rather than a mock pass. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BAS-1.5 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BAS-1.6 — Connect checkpoint endpoints to application transactions

- [ ] BAS-1.6 Connect checkpoint endpoints to application transactions.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/reference/http/; sdk/reference/repository/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BAS-1.1, BAS-1.2, BAS-1.4.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Create/load/checkpoint-save/commit-lookup compose the private validator with framework-owned CAS or delegated authority; exactly one component owns each durable receipt.

Implementation:

- [ ] BAS-1.6-I1 Connect checkpoint endpoints to application transactions. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BAS-1.6-V1 Run `node scripts/sdk-adapter-delivery.mjs BAS-1.6`: One prepared create/save/lost-response lookup through local HTTP returns a matching committed receipt and stable reopen. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BAS-1.6 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BAS-1.7 — Connect incremental append and resume

- [ ] BAS-1.7 Connect incremental append and resume.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/reference/http/; services/document-store/src/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BAS-1.6.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Append/read/observe reuse existing committed update ledger and baseline sync adapter; resume and duplicate handling do not expose an uncommitted predecessor or upgrade presence to persistence.

Implementation:

- [ ] BAS-1.7-I1 Connect incremental append and resume. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BAS-1.7-V1 Run `node scripts/sdk-adapter-delivery.mjs BAS-1.7`: One prepared duplicate append and cursor resume preserve exact update coverage and one operation result. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BAS-1.7 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BAS-1.8 — Expose scoped asset and lifecycle integration points

- [ ] BAS-1.8 Expose scoped asset and lifecycle integration points.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/reference/http/; sdk/contracts/capabilities.schema.json.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BAS-1.6, BAS-1.7.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Existing asset finalization, tombstone and retention ports remain optional; document receipts do not claim attachment availability; checkpoint-only install has no blob/queue/WebSocket dependency.

Implementation:

- [ ] BAS-1.8-I1 Expose scoped asset and lifecycle integration points. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BAS-1.8-V1 Run `node scripts/sdk-adapter-delivery.mjs BAS-1.8`: A checkpoint-only consumer runs without optional services and a prepared pending asset stays explicitly unavailable. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BAS-1.8 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Summarize delivered source interfaces and capability flags, focused selectors/results, true prerequisite gaps and remaining final qualification in `.roadmap-runner/backend-sdk-adapters-20261024/01-authority-and-storage.progress.md`. Do not copy hashes/delivery summaries into this source. The two final testing files own comprehensive case authoring and qualification; functional completion alone is not whole-plan completion.
