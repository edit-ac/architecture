# 04 swift headless facade

Status: IN_PROGRESS

Workspace: `core` from root `/Users/bpstr/Github/edit-ac`; task paths are core-relative unless repository-prefixed.
Progress: `/Users/bpstr/Github/edit-ac/.roadmap-runner/os-deferred-integrations-20261026/04-swift-headless-facade.progress.md`.
Origin: `/Users/bpstr/Github/edit-ac/architecture/runner-queues/dependency-closed-ui-20261025/21-apple-ui-bindings.md`.

## Current controller authority and scope

The user explicitly requested deferring all OS checks and completing remaining independent integration work on 2026-10-26. This is the current selected owner of the original task contracts below; the broad originating sources remain preserved as history. Current controller: `architecture/runner-queues/os-deferred-integrations-20261026/manifest.json`. Read the current PRIMARY section of `.roadmap-coordination/parallel-clients.md` before each parent. One serial guarded PRIMARY runner, one bounded original parent per iteration; the independent EDITOR lane is protected.

Defer VM/guest operations, emulator or simulator/device checks, native UI/IME execution, native target bootstrap/readiness qualification and native desktop-shell execution. Do not start, stop, inspect for readiness or wait on a guest; do not turn a fixture or compilation into target-OS proof. Headless Swift/Kotlin/Dart consumers, local compiler/package checks, Node/PHP/SQLite and browser fixtures are allowed. Flutter/Dart doctor/compiler metadata checks on the current host are permitted; toolchain discovery may report platform capabilities as available/unknown/unsupported without launching a native target or running native OS qualification probes. No paid cloud provisioning, model/provider calls, secret loading, publication, push or deployment. All automated checks use prepared deterministic content and mocked provider/network transports.

Preserve every acceptance criterion below. A headless consumer must use the actual declared binding and existing shared authority; a stub is not a replacement for that boundary. If a selected check unexpectedly needs an excluded OS operation, record the exact unmet owner and changed-input condition, leave acceptance unchecked and return BLOCKED. Never retry unchanged input. Planned selectors and missing local wrappers are owned implementation work. Reuse compatible passing receipts; run only the affected named focused delivery check during functionality. Comprehensive backend/web verification follows all ten selected environment/functional parents; deferred native work is outside this run's phase barrier, not marked complete or used as a passed prerequisite. Broader native/all-platform qualification remains required and deferred. Current scope retains the basis plan's Node/browser, PHP/Laravel/Filament/SQLite and actually delivered headless clients; unselected languages, databases and OS targets gain no support claim. Existing caps, unknown-data preservation and single current production format remain unchanged.

Workers update only verified checkbox states and Status in this selected source. Store delivery text, source/artifact hashes and counts in the separate progress file; never write a source delivery summary. After two parents and at source boundaries, hold root `.roadmap-coordination/integration.lock`; checkpoint only validated safely separable owned source. Preserve inherited/unrelated dirty bytes and indexes; do not stage snapshots, source from the EDITOR checkout, generated artifacts or unrelated work. Keep mixed inherited implementation pending with exact owned patches if safe landing is unavailable. Clean task-owned inactive outputs/browsers/servers, preserve active processes and check disk. No agents or extra controllers.

## Selected original contracts

### Task BNA-1.1 — Add the Swift storage and authority facade

- [ ] BNA-1.1 Add the Swift storage and authority facade.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/apple/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none.
Entry receipts: [BAS-1.6](../dependency-closed-ui-20261025/11-local-authority.md), [BAS-1.7](../dependency-closed-ui-20261025/11-local-authority.md), [BSC-1.6](../dependency-closed-ui-20261025/10-shared-sdk-contracts.md), [BSC-1.7](../dependency-closed-ui-20261025/10-shared-sdk-contracts.md).
Prior progress: /Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/10-shared-sdk-contracts.progress.md; /Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/11-local-authority.progress.md.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Typed Swift async identity/receipt/transport facade wraps existing native Session/FFI; actor isolation respects its single owner and cancellation preserves uncertain saves.

Implementation:

- [ ] BNA-1.1-I1 Add the Swift storage and authority facade. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BNA-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BNA-1.1`: Compile one Swift headless consumer with a prepared save/lookup and fresh-writer checkpoint reopen. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BNA-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.
