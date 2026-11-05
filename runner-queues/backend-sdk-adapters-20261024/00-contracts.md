# Freeze the common backend and adapter contracts

Status: PLANNED

## Goal and entry conditions

Deliver the 00-contracts milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: Existing current-format identity and staged admission from document-durability.md; existing Session/store/receipt interfaces from client-contracts.md. Missing current-format cuts block only their dependent contract. Inventory actual exports rather than assuming a roadmap Status is implementation evidence.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is functional delivery. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/00-contracts.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

## Epic BSC-1 — Freeze the common backend and adapter contracts

### Task BSC-1.1 — Map existing interfaces and package ownership

- [ ] BSC-1.1 Map existing interfaces and package ownership.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/contracts/ownership.md; crates/editac-session/; services/document-store/; packages/web/.
Context: [SDK contract: Logical operation contract](../../specs/backend-sdk-adapters.md#logical-operation-contract); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Every logical operation has one existing owner, actual source path, reuse decision and declared missing interface; provisional paths do not duplicate existing packages. Record the existing core/Session cutover owner and exact prerequisite checks for unversioned schema `editac.registry.editor` and profile `editac.yrs-yjs.editor` across creation/restore, journal scope, sync and WASM/FFI/native consumers. No suffixed runtime alias or previous/current compatibility matrix is planned; the cutover is not claimed complete by this inventory.

Implementation:

- [ ] BSC-1.1-I1 Map existing interfaces and package ownership. Reuse the existing owner and wire the minimum usable consumer at the named paths.

Validation:

- [ ] BSC-1.1-V1 Direct bounded contract check: Compare the ownership map to named existing source exports and record gaps; no code suite required. Budget: 1–3 minutes; record the exact local command or inspected prepared transcript.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BSC-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BSC-1.2 — Author the HTTP and DTO contract

- [ ] BSC-1.2 Author the HTTP and DTO contract.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/contracts/openapi.yaml; sdk/contracts/errors.md.
Context: [SDK contract: Logical operation contract](../../specs/backend-sdk-adapters.md#logical-operation-contract); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BSC-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: One authored HTTP schema defines operations, binary base64 fields, identity, integer ranges, nullability, revisions, conditional headers and typed errors; baseline sync and awareness remain distinct.

Implementation:

- [ ] BSC-1.2-I1 Author the HTTP and DTO contract. Reuse the existing owner and wire the minimum usable consumer at the named paths.

Validation:

- [ ] BSC-1.2-V1 Direct bounded contract check: Lint the authored schema locally and inspect one prepared checkpoint request/response against it. Budget: 1–3 minutes; record the exact local command or inspected prepared transcript.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BSC-1.2 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BSC-1.3 — Specify checkpoint persistence and conflicts

- [ ] BSC-1.3 Specify checkpoint persistence and conflicts.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/contracts/checkpoint.md; sdk/contracts/receipts.md.
Context: [SDK contract: Logical operation contract](../../specs/backend-sdk-adapters.md#logical-operation-contract); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BSC-1.2.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Create/load/save/initialized-empty and expected-revision CAS have explicit outcomes; a stale writer cannot overwrite a newer checkpoint; remote receipts follow transaction completion.

Implementation:

- [ ] BSC-1.3-I1 Specify checkpoint persistence and conflicts. Reuse the existing owner and wire the minimum usable consumer at the named paths.

Validation:

- [ ] BSC-1.3-V1 Direct bounded contract check: Walk one prepared two-writer save/conflict transcript against the contract and independent expected revision values. Budget: 1–3 minutes; record the exact local command or inspected prepared transcript.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BSC-1.3 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BSC-1.4 — Specify collaborative updates and mode transitions

- [ ] BSC-1.4 Specify collaborative updates and mode transitions.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/contracts/collaboration.md.
Context: [SDK contract: Logical operation contract](../../specs/backend-sdk-adapters.md#logical-operation-contract); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BSC-1.3.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Append/resume/commit lookup, deduplication floors and checkpoint-to-collaboration promotion share one authority and ledger; presence never acknowledges content; operation reuse with changed input rejects.

Implementation:

- [ ] BSC-1.4-I1 Specify collaborative updates and mode transitions. Reuse the existing owner and wire the minimum usable consumer at the named paths.

Validation:

- [ ] BSC-1.4-V1 Direct bounded contract check: Inspect a prepared duplicate update, lost reply and stale checkpoint transcript without contacting a host. Budget: 1–3 minutes; record the exact local command or inspected prepared transcript.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BSC-1.4 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BSC-1.5 — Specify the private semantic admission bridge

- [ ] BSC-1.5 Specify the private semantic admission bridge.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/contracts/admission.md; sdk/contracts/openapi.yaml.
Context: [SDK contract: Logical operation contract](../../specs/backend-sdk-adapters.md#logical-operation-contract); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BSC-1.2, BSC-1.3.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: A staged Rust result binds predecessor, identity and exact input digest; framework CAS rejects changed predecessors; PHP FFI and client validation assertions are not mandatory/trusted admission paths.

Implementation:

- [ ] BSC-1.5-I1 Specify the private semantic admission bridge. Reuse the existing owner and wire the minimum usable consumer at the named paths.

Validation:

- [ ] BSC-1.5-V1 Direct bounded contract check: Trace one validation/CAS race and one unavailable companion outcome; verify neither can return committed. Budget: 1–3 minutes; record the exact local command or inspected prepared transcript.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BSC-1.5 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BSC-1.6 — Specify web and native adapter lifetimes

- [ ] BSC-1.6 Specify web and native adapter lifetimes.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/contracts/lifecycle.md; sdk/contracts/capabilities.schema.json.
Context: [SDK contract: Logical operation contract](../../specs/backend-sdk-adapters.md#logical-operation-contract); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BSC-1.3, BSC-1.4.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Mount/open/save/flush/dispose, SSR, form reset, native suspension, cancellation-after-send and optional sync share explicit ownership and state transitions; UI history remains engine-owned.

Implementation:

- [ ] BSC-1.6-I1 Specify web and native adapter lifetimes. Reuse the existing owner and wire the minimum usable consumer at the named paths.

Validation:

- [ ] BSC-1.6-V1 Direct bounded contract check: Compare one browser unmount and one native suspension transcript with existing Session lifecycle states. Budget: 1–3 minutes; record the exact local command or inspected prepared transcript.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BSC-1.6 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BSC-1.7 — Add the minimal offline delivery oracle

- [ ] BSC-1.7 Add the minimal offline delivery oracle.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: fixtures/sdk-adapters/current/; scripts/sdk-adapter-delivery.mjs.
Context: [SDK contract: Logical operation contract](../../specs/backend-sdk-adapters.md#logical-operation-contract); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BSC-1.2, BSC-1.3, BSC-1.4, BSC-1.5, BSC-1.6.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: A tiny current-format binary/unknown-data/receipt fixture and selector dispatcher execute a named built-in or package check without credentials; unknown/missing selectors fail; generated output is task-owned and ignored. The fixture and actual core/Session/WASM/FFI identity selectors use the unversioned schema/profile, with matching create/reopen/sync results and rejection of retired suffixed envelopes before mutation. Missing cutover evidence blocks this parent; there is no compatibility reader or automatic relabel.

Implementation:

- [ ] BSC-1.7-I1 Add the minimal offline delivery oracle. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BSC-1.7-V1 Run `node scripts/sdk-adapter-delivery.mjs BSC-1.7`: Run node scripts/sdk-adapter-delivery.mjs BSC-1.7 with no network; one known fixture passes and one unknown selector rejects. This small data-loss guard is the early regression exception; broad suite development is deferred. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BSC-1.7 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BSC-1.8 — Publish ownership and support manifests

- [ ] BSC-1.8 Publish ownership and support manifests.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/contracts/support.json; sdk/contracts/adoption.md.
Context: [SDK contract: Logical operation contract](../../specs/backend-sdk-adapters.md#logical-operation-contract); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BSC-1.1, BSC-1.2, BSC-1.3, BSC-1.4, BSC-1.5, BSC-1.6, BSC-1.7.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Every planned package has an owner role, capability flags, target runtime selection rule and existing-track handoff; unknown versions stay planned; unsupported protected/Qt GUI combinations are explicit.

Implementation:

- [ ] BSC-1.8-I1 Publish ownership and support manifests. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BSC-1.8-V1 Run `node scripts/sdk-adapter-delivery.mjs BSC-1.8`: Validate authored declarations with one named local manifest selector; every requested language and platform maps to a planned owner. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BSC-1.8 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Summarize delivered source interfaces and capability flags, focused selectors/results, true prerequisite gaps and remaining final qualification in `.roadmap-runner/backend-sdk-adapters-20261024/00-contracts.progress.md`. Do not copy hashes/delivery summaries into this source. The two final testing files own comprehensive case authoring and qualification; functional completion alone is not whole-plan completion.
