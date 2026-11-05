# Deliver Ruby and explicit C/C++ embedding boundaries

Status: PLANNED

## Goal and entry conditions

Deliver the 07-ruby-c-cpp milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: 00-contracts BSC-1.2/1.5/1.7 and 01-authority-and-storage BAS-1.1/1.2/1.6 supply the common contracts. C/C++ tasks additionally inspect existing editac-ffi and native ABI ownership; reuse a qualified current boundary rather than add aliases. Ruby and C families are independent.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is functional delivery. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/07-ruby-c-cpp.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

## Epic BRC-1 — Deliver Ruby and explicit C/C++ embedding boundaries

### Task BRC-1.1 — Implement Ruby client models and transport

- [ ] BRC-1.1 Implement Ruby client models and transport.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/ruby/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Gem exposes idiomatic byte-safe identities/errors/receipts and injected HTTP transport, bounded reads and operation IDs with no require-time I/O.

Implementation:

- [ ] BRC-1.1-I1 Implement Ruby client models and transport. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BRC-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BRC-1.1`: One local gem consumer round-trips the prepared current checkpoint and unknown bounded data. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BRC-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BRC-1.2 — Implement Ruby saves and commit lookup

- [ ] BRC-1.2 Implement Ruby saves and commit lookup.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/ruby/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BRC-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Conditional checkpoint save and optional append/resume share deterministic retry identities; unknown commit and conflict remain recoverable typed outcomes.

Implementation:

- [ ] BRC-1.2-I1 Implement Ruby saves and commit lookup. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BRC-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BRC-1.2`: One prepared lost acknowledgment resolves without another mutation and one stale save rejects. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BRC-1.2 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BRC-1.3 — Add Rails and ActiveRecord integration

- [ ] BRC-1.3 Add Rails and ActiveRecord integration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/backend/rails/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BRC-1.2.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Engine/routes/policy hooks and optional ActiveRecord migrations/repository transact checkpoint and operation outcome atomically; after_commit callbacks cannot fire for a rollback.

Implementation:

- [ ] BRC-1.3-I1 Add Rails and ActiveRecord integration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BRC-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BRC-1.3`: One actual Rails SQLite save/reopen and rollback request yields correct bytes and after-commit event count. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BRC-1.3 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BRC-1.4 — Freeze the minimal C ABI ownership contract

- [ ] BRC-1.4 Freeze the minimal C ABI ownership contract.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/c/include/; sdk/contracts/c-abi.md; crates/editac-ffi/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Opaque handles, owned buffers, explicit destroy, cancellation, error codes and thread/session affinity map the existing engine; size/version descriptor validation does not introduce legacy runtime support.

Implementation:

- [ ] BRC-1.4-I1 Freeze the minimal C ABI ownership contract. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BRC-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BRC-1.4`: Compile one header-only C consumer and inspect a prepared invalid descriptor/ownership transcript against the contract. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BRC-1.4 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BRC-1.5 — Implement C checkpoint and authority entry points

- [ ] BRC-1.5 Implement C checkpoint and authority entry points.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/c/; crates/editac-ffi/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BRC-1.4.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Current checkpoint validation/load/export and typed save/receipt transport hooks cross the ABI without unwinding, dangling callbacks or assuming caller buffers remain alive.

Implementation:

- [ ] BRC-1.5-I1 Implement C checkpoint and authority entry points. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BRC-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BRC-1.5`: Run one compiled C current-format round-trip consumer and explicit destroy path with a prepared transport. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BRC-1.5 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BRC-1.6 — Add an ownership-safe C++ wrapper

- [ ] BRC-1.6 Add an ownership-safe C++ wrapper.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/cpp/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BRC-1.5.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: RAII handles/move-only buffers and typed results wrap C ownership without a second engine or exception across ABI; cancel/dispose invalidates callbacks.

Implementation:

- [ ] BRC-1.6-I1 Add an ownership-safe C++ wrapper. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BRC-1.6-V1 Run `node scripts/sdk-adapter-delivery.mjs BRC-1.6`: Compile one C++ consumer that moves a handle, saves/reopens a checkpoint and disposes with a pending prepared callback. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BRC-1.6 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BRC-1.7 — Add Ruby and C embedding examples

- [ ] BRC-1.7 Add Ruby and C embedding examples.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: examples/sdk-adapters/ruby/; examples/sdk-adapters/c/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BRC-1.3, BRC-1.5, BRC-1.6.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Rails and headless C/C++ recipes identify storage/semantic capability, ownership and current unsupported UI features; local packages include authored licenses/notices.

Implementation:

- [ ] BRC-1.7-I1 Add Ruby and C embedding examples. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BRC-1.7-V1 Run `node scripts/sdk-adapter-delivery.mjs BRC-1.7`: Run the documented local Ruby save/load and C binary reopen examples, using the same oracle digest. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BRC-1.7 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Summarize delivered source interfaces and capability flags, focused selectors/results, true prerequisite gaps and remaining final qualification in `.roadmap-runner/backend-sdk-adapters-20261024/07-ruby-c-cpp.progress.md`. Do not copy hashes/delivery summaries into this source. The two final testing files own comprehensive case authoring and qualification; functional completion alone is not whole-plan completion.
