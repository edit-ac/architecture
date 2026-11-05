# Deliver Go clients and Rust host integration

Status: PLANNED

## Goal and entry conditions

Deliver the 05-go-rust milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: 00-contracts BSC-1.2/1.5/1.7 and 01-authority-and-storage BAS-1.1/1.2/1.6/1.7 expose current validation/storage/transport outcomes. The Rust package must wrap existing crates/services rather than establish a competing semantic authority.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is functional delivery. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/05-go-rust.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

## Epic BGR-1 — Deliver Go clients and Rust host integration

### Task BGR-1.1 — Implement Go DTOs and context-aware client

- [ ] BGR-1.1 Implement Go DTOs and context-aware client.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/go/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Exported types preserve integer/byte/unknown data semantics and accept caller-owned http.Client; context cancellation, deadlines and bounded bodies are explicit.

Implementation:

- [ ] BGR-1.1-I1 Implement Go DTOs and context-aware client. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BGR-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BGR-1.1`: A prepared httptest endpoint round-trips the checkpoint digest and rejects a malformed response without changing caller state. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BGR-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BGR-1.2 — Implement Go conditional commit workflows

- [ ] BGR-1.2 Implement Go conditional commit workflows.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/go/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BGR-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Checkpoint and incremental operations share stable operation identity, typed conflicts and commit-unknown lookup; context cancellation after dispatch does not imply rollback.

Implementation:

- [ ] BGR-1.2-I1 Implement Go conditional commit workflows. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BGR-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BGR-1.2`: One lost-response fixture followed by lookup returns the original outcome; same key/different input rejects. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BGR-1.2 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BGR-1.3 — Add the Go database/sql repository

- [ ] BGR-1.3 Add the Go database/sql repository.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/go/storage/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BGR-1.2.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Caller-selected SQL driver and transaction lifecycle implement scoped CAS and binary/operation ledger atomically; supported databases are explicit.

Implementation:

- [ ] BGR-1.3-I1 Add the Go database/sql repository. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BGR-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BGR-1.3`: One real SQLite save/reopen and two-connection stale revision smoke; record exact driver/runtime selection. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BGR-1.3 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BGR-1.4 — Add standard net/http routes

- [ ] BGR-1.4 Add standard net/http routes.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/go-http/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BGR-1.2, BGR-1.3.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Handler constructor accepts policy/repository/validator, request limits and shutdown contexts; no ambient global document or database is created.

Implementation:

- [ ] BGR-1.4-I1 Add standard net/http routes. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BGR-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BGR-1.4`: One local httptest create/save/reopen and forbidden scope request traverse the real handler. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BGR-1.4 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BGR-1.5 — Add Gin and Echo bindings

- [ ] BGR-1.5 Add Gin and Echo bindings.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/gin/; adapters/backend/echo/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BGR-1.4.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Thin middleware/route bridges reuse net/http operations, application policy and error semantics; framework context does not escape its request lifetime.

Implementation:

- [ ] BGR-1.5-I1 Add Gin and Echo bindings. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BGR-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BGR-1.5`: One prepared request through each actual router yields the same normalized save/error result; split the two bridges before implementation if the session budget is exceeded. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BGR-1.5 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BGR-1.6 — Expose the Rust application SDK

- [ ] BGR-1.6 Expose the Rust application SDK.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/rust/; crates/editac-session/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Application-facing types re-export/reuse the existing engine/session/authority contract; async network access and optional local semantic operations have separate feature declarations.

Implementation:

- [ ] BGR-1.6-I1 Expose the Rust application SDK. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BGR-1.6-V1 Run `node scripts/sdk-adapter-delivery.mjs BGR-1.6`: Compile one Rust consumer with minimal features and one with semantic bridge enabled; current checkpoint identity is unchanged. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BGR-1.6 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BGR-1.7 — Add the Axum host adapter

- [ ] BGR-1.7 Add the Axum host adapter.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/axum/; services/document-store/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BGR-1.6.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Router integration wraps the existing authority and host policy with explicit state ownership, bounds and graceful shutdown; no duplicate store/CRDT is introduced.

Implementation:

- [ ] BGR-1.7-I1 Add the Axum host adapter. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BGR-1.7-V1 Run `node scripts/sdk-adapter-delivery.mjs BGR-1.7`: One prepared request against the actual local router returns the repository-owned receipt and rejects forbidden scope. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BGR-1.7 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BGR-1.8 — Add Go and Rust integration recipes

- [ ] BGR-1.8 Add Go and Rust integration recipes.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: examples/sdk-adapters/go/; examples/sdk-adapters/rust/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BGR-1.4, BGR-1.7.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Each example mounts one editor-facing endpoint and documents configured storage/validator ownership, exact install paths and optional collaborative mode.

Implementation:

- [ ] BGR-1.8-I1 Add Go and Rust integration recipes. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BGR-1.8-V1 Run `node scripts/sdk-adapter-delivery.mjs BGR-1.8`: Execute one local save/load command from each recipe with fixture data; no external provider access. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BGR-1.8 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Summarize delivered source interfaces and capability flags, focused selectors/results, true prerequisite gaps and remaining final qualification in `.roadmap-runner/backend-sdk-adapters-20261024/05-go-rust.progress.md`. Do not copy hashes/delivery summaries into this source. The two final testing files own comprehensive case authoring and qualification; functional completion alone is not whole-plan completion.
