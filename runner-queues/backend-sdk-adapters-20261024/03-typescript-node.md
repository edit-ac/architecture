# Deliver Node and TypeScript backend adapters

Status: PLANNED

## Goal and entry conditions

Deliver the 03-typescript-node milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: 00-contracts BSC-1.2/1.5/1.7 and 01-authority-and-storage BAS-1.2/1.6/1.7 supply the shared authority and prepared protocol. Reuse existing packages/web and packages/core exports. PHP completion is not a semantic prerequisite; the serial queue places it first for the requested Laravel outcome.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is functional delivery. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/03-typescript-node.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

## Epic BTS-1 — Deliver Node and TypeScript backend adapters

### Task BTS-1.1 — Implement Node DTOs and injected HTTP transport

- [ ] BTS-1.1 Implement Node DTOs and injected HTTP transport.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/typescript/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Typed client validates runtime responses, binary fields and JS-safe counters, supports AbortSignal, and has no provider/DB side effects on import; generated types stay derived from the one authored contract.

Implementation:

- [ ] BTS-1.1-I1 Implement Node DTOs and injected HTTP transport. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BTS-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BTS-1.1`: Compile one consumer and round-trip the binary/unknown-field fixture through prepared fetch responses. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BTS-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BTS-1.2 — Implement Node save and commit-unknown workflows

- [ ] BTS-1.2 Implement Node save and commit-unknown workflows.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/typescript/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BTS-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Checkpoint/update operations, durable CAS and receipt lookup retain stable identities; retry policy distinguishes read retries, safe exact writes and uncertain outcomes.

Implementation:

- [ ] BTS-1.2-I1 Implement Node save and commit-unknown workflows. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BTS-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BTS-1.2`: One prepared canceled save resolves by original operation key and one stale expected revision returns a typed conflict. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BTS-1.2 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BTS-1.3 — Add the Express adapter

- [ ] BTS-1.3 Add the Express adapter.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/express/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BTS-1.2.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Router factory accepts application policy, repository and validator dependencies; parser limits, error mapping and authenticated tenant scoping apply before semantic admission.

Implementation:

- [ ] BTS-1.3-I1 Add the Express adapter. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BTS-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BTS-1.3`: One prepared request through a real local Express app saves/reopens; a forbidden request leaves the repository unchanged. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BTS-1.3 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BTS-1.4 — Add the Fastify adapter

- [ ] BTS-1.4 Add the Fastify adapter.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/fastify/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BTS-1.2.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Scoped plugin registers bounded schema-aware routes with injected policy/repository and closes only owned resources.

Implementation:

- [ ] BTS-1.4-I1 Add the Fastify adapter. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BTS-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BTS-1.4`: Inject one prepared save and one oversized body into the actual plugin; no receipt exists for the rejected body. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BTS-1.4 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BTS-1.5 — Add the NestJS adapter

- [ ] BTS-1.5 Add the NestJS adapter.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/nestjs/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BTS-1.2.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Module/controller/guard bindings wrap the same Node boundary and permit application DI and policy hooks without creating per-request global sessions.

Implementation:

- [ ] BTS-1.5-I1 Add the NestJS adapter. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BTS-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BTS-1.5`: Boot one local Nest module with prepared repository and confirm guard denial and one committed save use the expected owner. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BTS-1.5 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BTS-1.6 — Add shared Node SQL repositories

- [ ] BTS-1.6 Add shared Node SQL repositories.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/typescript/storage/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BTS-1.2.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Node SQLite/PostgreSQL transaction ports preserve exact bytes and CAS/operation outcome semantics; ORM-specific mappings remain optional and do not acknowledge before commit.

Implementation:

- [ ] BTS-1.6-I1 Add shared Node SQL repositories. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BTS-1.6-V1 Run `node scripts/sdk-adapter-delivery.mjs BTS-1.6`: One actual SQLite save/reopen and rollback smoke; reuse the unchanged shared PostgreSQL contract evidence until driver-specific final testing. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BTS-1.6 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BTS-1.7 — Add Next.js server route handlers

- [ ] BTS-1.7 Add Next.js server route handlers.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/nextjs/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BTS-1.2, BTS-1.6.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: App Router handlers are explicitly server-only, reuse application authorization/Node repositories and select Node runtime when native DB/validator access needs it; no unsupported edge runtime claim.

Implementation:

- [ ] BTS-1.7-I1 Add Next.js server route handlers. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BTS-1.7-V1 Run `node scripts/sdk-adapter-delivery.mjs BTS-1.7`: One local route-handler save/load smoke and one server/client import-boundary compile check run without secrets. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BTS-1.7 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BTS-1.8 — Connect browser autosave and optional sync orchestration

- [ ] BTS-1.8 Connect browser autosave and optional sync orchestration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: packages/web/; sdk/typescript/browser/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BTS-1.2.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Existing editor lifetime maps local flush, remote checkpoint save and optional update transport to distinct statuses; bounded autosave preserves one operation identity on retries and never resets the document on a response.

Implementation:

- [ ] BTS-1.8-I1 Connect browser autosave and optional sync orchestration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BTS-1.8-V1 Run `node scripts/sdk-adapter-delivery.mjs BTS-1.8`: One prepared debounced-save plus later-edit fixture shows receipts cover only captured updates; dispose cancels orchestration and retains recovery. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BTS-1.8 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Summarize delivered source interfaces and capability flags, focused selectors/results, true prerequisite gaps and remaining final qualification in `.roadmap-runner/backend-sdk-adapters-20261024/03-typescript-node.progress.md`. Do not copy hashes/delivery summaries into this source. The two final testing files own comprehensive case authoring and qualification; functional completion alone is not whole-plan completion.
