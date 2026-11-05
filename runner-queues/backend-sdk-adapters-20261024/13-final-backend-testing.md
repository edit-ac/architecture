# Complete backend conformance and failure testing

Status: PLANNED

## Goal and entry conditions

Deliver the 13-final-backend-testing milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: All functional files 00–12 have validated their required parents or an explicit controller-approved scope revision. Reuse their exact selectors/results; a missing package, database or framework is not a skipped pass. Full plan completion requires this file and 14-final-framework-native-testing. No functional task depends on these final tests merely for ordering.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is final testing. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/13-final-backend-testing.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

## Epic BFT-1 — Complete backend conformance and failure testing

### Task BFT-1.1 — Build the final requirement-to-case map

- [ ] BFT-1.1 Build the final requirement-to-case map.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: tests/sdk-adapters/backend/; sdk/contracts/qualification.json.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Each backend requirement B01–B06 in the index has exactly one final owner/case family, uncovered cases are authored once, and reusable focused results are referenced by exact source input rather than rerun.

Implementation:

- [ ] BFT-1.1-I1 Build the final requirement-to-case map. Reuse compatible evidence; author only uncovered cases and connect runtime results to the named qualification owner.

Validation:

- [ ] BFT-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BFT-1.1` as a bounded final selector: Locally validate the requirement map and result references; every planned language/DB has an executed or explicitly outstanding disposition. Budget: at most 10 minutes of execution per selected boundary; shard a larger matrix into controller-defined parents before running.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BFT-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BFT-1.2 — Verify cross-language current-format parity

- [ ] BFT-1.2 Verify cross-language current-format parity.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: tests/sdk-adapters/backend/parity/.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BFT-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Every delivered language preserves exact bytes, canonical identity, initialized-empty, Unicode and bounded unknown data; unsupported envelopes and malformed base64/counters reject before mutation.

Implementation:

- [ ] BFT-1.2-I1 Verify cross-language current-format parity. Reuse compatible evidence; author only uncovered cases and connect runtime results to the named qualification owner.

Validation:

- [ ] BFT-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BFT-1.2` as a bounded final selector: Run only missing parity cases across actual declared runtimes and compare independent oracle digests and typed errors; preserve nonzero counts. Budget: at most 10 minutes of execution per selected boundary; shard a larger matrix into controller-defined parents before running.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BFT-1.2 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BFT-1.3 — Verify database atomicity and concurrent saves

- [ ] BFT-1.3 Verify database atomicity and concurrent saves.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: tests/sdk-adapters/backend/storage/.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BFT-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: SQLite/PostgreSQL/MySQL/MariaDB actual driver claims prove binary reopen, transaction rollback, multi-process CAS and operation uniqueness; no receipt precedes commit or represents weaker undeclared durability.

Implementation:

- [ ] BFT-1.3-I1 Verify database atomicity and concurrent saves. Reuse compatible evidence; author only uncovered cases and connect runtime results to the named qualification owner.

Validation:

- [ ] BFT-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BFT-1.3` as a bounded final selector: Run remaining real local DB cases including forced rollback/restart; missing services/toolchains remain BLOCKED and cannot qualify a driver. Budget: at most 10 minutes of execution per selected boundary; shard a larger matrix into controller-defined parents before running.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BFT-1.3 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BFT-1.4 — Verify retry and commit-unknown recovery

- [ ] BFT-1.4 Verify retry and commit-unknown recovery.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: tests/sdk-adapters/backend/retries/.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BFT-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Lost response, duplicate/reordered append, operation-key collision, cancellation and retention floor outcomes remain idempotent across all clients/adapters without discarding pending data.

Implementation:

- [ ] BFT-1.4-I1 Verify retry and commit-unknown recovery. Reuse compatible evidence; author only uncovered cases and connect runtime results to the named qualification owner.

Validation:

- [ ] BFT-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BFT-1.4` as a bounded final selector: Execute the uncovered deterministic fault/transport cases and compare ledger/receipt coverage, reusing identical shared retry evidence where valid. Budget: at most 10 minutes of execution per selected boundary; shard a larger matrix into controller-defined parents before running.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BFT-1.4 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BFT-1.5 — Verify authorization and staged admission

- [ ] BFT-1.5 Verify authorization and staged admission.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: tests/sdk-adapters/backend/security/.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BFT-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Cross-tenant requests, readonly policy, expired auth, oversized input, forged client validation and validation/CAS races reject without data/receipt leakage or live mutation; protected capability is never inferred from opaque storage.

Implementation:

- [ ] BFT-1.5-I1 Verify authorization and staged admission. Reuse compatible evidence; author only uncovered cases and connect runtime results to the named qualification owner.

Validation:

- [ ] BFT-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BFT-1.5` as a bounded final selector: Run remaining prepared principal and malformed-input cases against actual adapter middleware/private bridge, including Filament/Livewire submissions through Laravel policies and Drupal endpoint scope/CSRF; no production credentials or external security service. Budget: at most 10 minutes of execution per selected boundary; shard a larger matrix into controller-defined parents before running.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BFT-1.5 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BFT-1.6 — Verify checkpoint and collaboration transitions

- [ ] BFT-1.6 Verify checkpoint and collaboration transitions.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: tests/sdk-adapters/backend/collaboration/.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BFT-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Checkpoint-only installation works without optional services; promotion shares one authority; two offline peers converge with exact durable receipt coverage, compaction fallback and pending assets correctly separated.

Implementation:

- [ ] BFT-1.6-I1 Verify checkpoint and collaboration transitions. Reuse compatible evidence; author only uncovered cases and connect runtime results to the named qualification owner.

Validation:

- [ ] BFT-1.6-V1 Run `node scripts/sdk-adapter-delivery.mjs BFT-1.6` as a bounded final selector: Execute one uncovered prepared end-to-end host transition and failure/reopen flow; state-vector convergence alone cannot satisfy the receipt oracle. Budget: at most 10 minutes of execution per selected boundary; shard a larger matrix into controller-defined parents before running.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BFT-1.6 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BFT-1.7 — Publish backend qualification dispositions

- [ ] BFT-1.7 Publish backend qualification dispositions.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/contracts/qualification.json; sdk/contracts/guides/backend/.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BFT-1.2, BFT-1.3, BFT-1.4, BFT-1.5, BFT-1.6.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Runtime/framework/database claims correspond to executed results; plain PHP package installs exclude Laravel/Filament, Laravel remains usable without Filament, Drupal uses the PHP SDK without either framework wrapper, and adapters reuse the SDK save/receipt logic; failed/skipped/missing environments remain unqualified and release/security handoffs name exact outstanding owners; no provider/deployment readiness claim appears.

Implementation:

- [ ] BFT-1.7-I1 Publish backend qualification dispositions. Reuse compatible evidence; author only uncovered cases and connect runtime results to the named qualification owner.

Validation:

- [ ] BFT-1.7-V1 Run `node scripts/sdk-adapter-delivery.mjs BFT-1.7` as a bounded final selector: Validate every claimed backend capability has matching current-source evidence; report total executed/passed/failed/skipped counts without a broad rerun. Budget: at most 10 minutes of execution per selected boundary; shard a larger matrix into controller-defined parents before running.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BFT-1.7 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Summarize delivered source interfaces and capability flags, focused selectors/results, true prerequisite gaps and remaining final qualification in `.roadmap-runner/backend-sdk-adapters-20261024/13-final-backend-testing.progress.md`. Do not copy hashes/delivery summaries into this source. The two final testing files own comprehensive case authoring and qualification; functional completion alone is not whole-plan completion.
