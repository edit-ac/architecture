# 03 desktop feasibility

Status: COMPLETE

Workspace: `core` from root `/Users/bpstr/Github/edit-ac`; task paths are core-relative unless repository-prefixed.
Progress: `/Users/bpstr/Github/edit-ac/.roadmap-runner/os-deferred-integrations-20261026/03-desktop-feasibility.progress.md`.
Origin: `/Users/bpstr/Github/edit-ac/architecture/runner-queues/editor-ui-integrations-20261024/24-flutter-web-and-desktop-profiles.md`.

## Current controller authority and scope

The user explicitly requested deferring all OS checks and completing remaining independent integration work on 2026-10-26. This is the current selected owner of the original task contracts below; the broad originating sources remain preserved as history. Current controller: `architecture/runner-queues/os-deferred-integrations-20261026/manifest.json`. Read the current PRIMARY section of `.roadmap-coordination/parallel-clients.md` before each parent. One serial guarded PRIMARY runner, one bounded original parent per iteration; the independent EDITOR lane is protected.

Defer VM/guest operations, emulator or simulator/device checks, native UI/IME execution, native target bootstrap/readiness qualification and native desktop-shell execution. Do not start, stop, inspect for readiness or wait on a guest; do not turn a fixture or compilation into target-OS proof. Headless Swift/Kotlin/Dart consumers, local compiler/package checks, Node/PHP/SQLite and browser fixtures are allowed. Flutter/Dart doctor/compiler metadata checks on the current host are permitted; toolchain discovery may report platform capabilities as available/unknown/unsupported without launching a native target or running native OS qualification probes. No paid cloud provisioning, model/provider calls, secret loading, publication, push or deployment. All automated checks use prepared deterministic content and mocked provider/network transports.

Preserve every acceptance criterion below. A headless consumer must use the actual declared binding and existing shared authority; a stub is not a replacement for that boundary. If a selected check unexpectedly needs an excluded OS operation, record the exact unmet owner and changed-input condition, leave acceptance unchecked and return BLOCKED. Never retry unchanged input. Planned selectors and missing local wrappers are owned implementation work. Reuse compatible passing receipts; run only the affected named focused delivery check during functionality. Comprehensive backend/web verification follows all ten selected environment/functional parents; deferred native work is outside this run's phase barrier, not marked complete or used as a passed prerequisite. Broader native/all-platform qualification remains required and deferred. Current scope retains the basis plan's Node/browser, PHP/Laravel/Filament/SQLite and actually delivered headless clients; unselected languages, databases and OS targets gain no support claim. Existing caps, unknown-data preservation and single current production format remain unchanged.

Workers update only verified checkbox states and Status in this selected source. Store delivery text, source/artifact hashes and counts in the separate progress file; never write a source delivery summary. After two parents and at source boundaries, hold root `.roadmap-coordination/integration.lock`; checkpoint only validated safely separable owned source. Preserve inherited/unrelated dirty bytes and indexes; do not stage snapshots, source from the EDITOR checkout, generated artifacts or unrelated work. Keep mixed inherited implementation pending with exact owned patches if safe landing is unavailable. Clean task-owned inactive outputs/browsers/servers, preserve active processes and check disk. No agents or extra controllers.

## Selected original contracts

### Task UFW-1.4 — Resolve Flutter and React Native desktop host feasibility

- [x] UFW-1.4 Resolve Flutter and React Native desktop host feasibility.

Purpose: Resolve Flutter and React Native desktop host feasibility so applications can reuse this integration boundary.
Deliverable: `adapters/native/flutter/; adapters/native/react-native/; ../architecture/specs/native-ui-integrations.md`.
Context: [named contract section](../../specs/native-ui-integrations.md#flutter); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [UNC-1.4](01-native-ui-contracts.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: A bounded decision for macOS/Windows/Linux records actual available embedding APIs, missing prerequisite and owner, and per-stack supported/unsupported status. Native SDK availability alone is never claimed as Flutter/RN desktop support.

Implementation:

- [x] UFW-1.4-I1 Time-box documentation/API inspection to 30 minutes; name an implementable extension task set for any proven path, otherwise return typed unsupported capability and exact unblock condition. Do not create a new renderer.
- [x] UFW-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UFW-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UFW-1.4`: Inspect one capability response per candidate stack/OS and verify every claimed available path cites a current host API; report investigation counts rather than fabricated runtime passes. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UFW-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.
