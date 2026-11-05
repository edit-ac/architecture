# Deliver JVM and .NET SDKs and adapters

Status: PLANNED

## Goal and entry conditions

Deliver the 06-jvm-dotnet milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: 00-contracts BSC-1.2/1.5/1.7 and 01-authority-and-storage BAS-1.2/1.6/1.7 supply the same HTTP/receipt/validator authority. JVM and .NET families are independent within this file.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is functional delivery. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/06-jvm-dotnet.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

## Epic BJD-1 — Deliver JVM and .NET SDKs and adapters

### Task BJD-1.1 — Implement the Java HTTP client

- [ ] BJD-1.1 Implement the Java HTTP client.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/java/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Java DTOs/HTTP transport retain exact binary/counter values with typed errors, deadlines and caller-owned resources; no runtime-specific document format is added.

Implementation:

- [ ] BJD-1.1-I1 Implement the Java HTTP client. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BJD-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BJD-1.1`: Compile a minimal local consumer and round-trip one prepared current checkpoint through a local stub transport. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BJD-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BJD-1.2 — Add Kotlin coroutine extensions

- [ ] BJD-1.2 Add Kotlin coroutine extensions.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/kotlin/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BJD-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Coroutine facade reuses Java DTOs and receipt logic while propagating cancellation and uncertain-write lookup; it does not duplicate the Android engine binding.

Implementation:

- [ ] BJD-1.2-I1 Add Kotlin coroutine extensions. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BJD-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BJD-1.2`: One prepared canceled save retains its operation identity and resolves through Java commit lookup. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BJD-1.2 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BJD-1.3 — Add Spring Boot and Spring Security integration

- [ ] BJD-1.3 Add Spring Boot and Spring Security integration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/spring/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BJD-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Explicit auto-configuration/controller/security callbacks and JDBC transaction port honor application tenant policy and after-commit publication; defaults never permit anonymous writes.

Implementation:

- [ ] BJD-1.3-I1 Add Spring Boot and Spring Security integration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BJD-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BJD-1.3`: One local Spring SQLite request/reopen and rolled-back write show a single authoritative outcome. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BJD-1.3 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BJD-1.4 — Add the Ktor adapter

- [ ] BJD-1.4 Add the Ktor adapter.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/ktor/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BJD-1.2.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Ktor routes/plugins reuse coroutine client/models and application transaction/policy ports with explicit service lifetime; no implicit server or database on import.

Implementation:

- [ ] BJD-1.4-I1 Add the Ktor adapter. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BJD-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BJD-1.4`: One prepared request through a local Ktor app and cancellation returns matching typed outcomes and closes owned work. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BJD-1.4 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BJD-1.5 — Implement the C# asynchronous client

- [ ] BJD-1.5 Implement the C# asynchronous client.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/dotnet/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Task-based API preserves bytes and scoped revisions with CancellationToken, injected HttpClient and distinct commit-unknown; no engine/history copy exists in DTO code.

Implementation:

- [ ] BJD-1.5-I1 Implement the C# asynchronous client. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BJD-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BJD-1.5`: Compile a local .NET consumer and run one prepared binary save/lost-reply lookup transcript. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BJD-1.5 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BJD-1.6 — Add ASP.NET Core endpoint integration

- [ ] BJD-1.6 Add ASP.NET Core endpoint integration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/aspnet/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BJD-1.5.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Minimal API/controller registration accepts application authorization, repository and validator; problem responses map the shared error taxonomy and request limits.

Implementation:

- [ ] BJD-1.6-I1 Add ASP.NET Core endpoint integration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BJD-1.6-V1 Run `node scripts/sdk-adapter-delivery.mjs BJD-1.6`: One local endpoint save and denied-principal smoke leave the denied document unchanged. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BJD-1.6 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BJD-1.7 — Add EF Core repository transactions

- [ ] BJD-1.7 Add EF Core repository transactions.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/dotnet/storage/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BJD-1.5.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Scoped entities/migrations, concurrency token and operation uniqueness commit together; SaveChanges alone cannot emit a receipt before transaction completion.

Implementation:

- [ ] BJD-1.7-I1 Add EF Core repository transactions. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BJD-1.7-V1 Run `node scripts/sdk-adapter-delivery.mjs BJD-1.7`: One actual SQLite commit/reopen and rollback through EF Core yields exact bytes and no rollback receipt. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BJD-1.7 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BJD-1.8 — Add JVM and .NET application recipes

- [ ] BJD-1.8 Add JVM and .NET application recipes.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: examples/sdk-adapters/jvm/; examples/sdk-adapters/dotnet/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BJD-1.3, BJD-1.4, BJD-1.6, BJD-1.7.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Spring/Ktor and ASP.NET examples state runtime/capability ranges and actual policy/store/validator wiring; native Windows UI use remains a different capability.

Implementation:

- [ ] BJD-1.8-I1 Add JVM and .NET application recipes. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BJD-1.8-V1 Run `node scripts/sdk-adapter-delivery.mjs BJD-1.8`: Run one documented local save/load request per runtime family using prepared data; compile remaining recipe entry points without deployment. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BJD-1.8 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Summarize delivered source interfaces and capability flags, focused selectors/results, true prerequisite gaps and remaining final qualification in `.roadmap-runner/backend-sdk-adapters-20261024/06-jvm-dotnet.progress.md`. Do not copy hashes/delivery summaries into this source. The two final testing files own comprehensive case authoring and qualification; functional completion alone is not whole-plan completion.
