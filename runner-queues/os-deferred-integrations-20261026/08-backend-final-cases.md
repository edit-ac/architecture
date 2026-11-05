# 08 backend final cases

Status: IN_PROGRESS

Workspace: `core` from root `/Users/bpstr/Github/edit-ac`; task paths are core-relative unless repository-prefixed.
Progress: `/Users/bpstr/Github/edit-ac/.roadmap-runner/os-deferred-integrations-20261026/08-backend-final-cases.progress.md`.
Origin: `/Users/bpstr/Github/edit-ac/architecture/runner-queues/dependency-closed-ui-20261025/80-backend-final-cases.md`.

## Current controller authority and scope

The user explicitly requested deferring all OS checks and completing remaining independent integration work on 2026-10-26. This is the current selected owner of the original task contracts below; the broad originating sources remain preserved as history. Current controller: `architecture/runner-queues/os-deferred-integrations-20261026/manifest.json`. Read the current PRIMARY section of `.roadmap-coordination/parallel-clients.md` before each parent. One serial guarded PRIMARY runner, one bounded original parent per iteration; the independent EDITOR lane is protected.

Defer VM/guest operations, emulator or simulator/device checks, native UI/IME execution, native target bootstrap/readiness qualification and native desktop-shell execution. Do not start, stop, inspect for readiness or wait on a guest; do not turn a fixture or compilation into target-OS proof. Headless Swift/Kotlin/Dart consumers, local compiler/package checks, Node/PHP/SQLite and browser fixtures are allowed. Flutter/Dart doctor/compiler metadata checks on the current host are permitted; toolchain discovery may report platform capabilities as available/unknown/unsupported without launching a native target or running native OS qualification probes. No paid cloud provisioning, model/provider calls, secret loading, publication, push or deployment. All automated checks use prepared deterministic content and mocked provider/network transports.

Preserve every acceptance criterion below. A headless consumer must use the actual declared binding and existing shared authority; a stub is not a replacement for that boundary. If a selected check unexpectedly needs an excluded OS operation, record the exact unmet owner and changed-input condition, leave acceptance unchecked and return BLOCKED. Never retry unchanged input. Planned selectors and missing local wrappers are owned implementation work. Reuse compatible passing receipts; run only the affected named focused delivery check during functionality. Comprehensive backend/web verification follows all ten selected environment/functional parents; deferred native work is outside this run's phase barrier, not marked complete or used as a passed prerequisite. Broader native/all-platform qualification remains required and deferred. Current scope retains the basis plan's Node/browser, PHP/Laravel/Filament/SQLite and actually delivered headless clients; unselected languages, databases and OS targets gain no support claim. Existing caps, unknown-data preservation and single current production format remain unchanged.

Workers update only verified checkbox states and Status in this selected source. Store delivery text, source/artifact hashes and counts in the separate progress file; never write a source delivery summary. After two parents and at source boundaries, hold root `.roadmap-coordination/integration.lock`; checkpoint only validated safely separable owned source. Preserve inherited/unrelated dirty bytes and indexes; do not stage snapshots, source from the EDITOR checkout, generated artifacts or unrelated work. Keep mixed inherited implementation pending with exact owned patches if safe landing is unavailable. Clean task-owned inactive outputs/browsers/servers, preserve active processes and check disk. No agents or extra controllers.

## Selected original contracts

### Task BFT-1.1 — Build the final requirement-to-case map

- [x] BFT-1.1 Build the final requirement-to-case map.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: tests/sdk-adapters/backend/; sdk/contracts/qualification.json.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Each backend requirement B01–B06 in the index has exactly one final owner/case family, uncovered cases are authored once, and reusable focused results are referenced by exact source input rather than rerun.

Implementation:

- [x] BFT-1.1-I1 Build the final requirement-to-case map. Reuse compatible evidence; author only uncovered cases and connect runtime results to the named qualification owner.

Validation:

- [x] BFT-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BFT-1.1` as a bounded final selector: Locally validate the requirement map and result references; every planned language/DB has an executed or explicitly outstanding disposition. Budget: at most 10 minutes of execution per selected boundary; shard a larger matrix into controller-defined parents before running.

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
