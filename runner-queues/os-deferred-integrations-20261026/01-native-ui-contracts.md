# 01 native ui contracts

Status: COMPLETE

Workspace: `core` from root `/Users/bpstr/Github/edit-ac`; task paths are core-relative unless repository-prefixed.
Progress: `/Users/bpstr/Github/edit-ac/.roadmap-runner/os-deferred-integrations-20261026/01-native-ui-contracts.progress.md`.
Origin: `/Users/bpstr/Github/edit-ac/architecture/runner-queues/editor-ui-integrations-20261024/15-native-ui-contracts.md`.

## Current controller authority and scope

The user explicitly requested deferring all OS checks and completing remaining independent integration work on 2026-10-26. This is the current selected owner of the original task contracts below; the broad originating sources remain preserved as history. Current controller: `architecture/runner-queues/os-deferred-integrations-20261026/manifest.json`. Read the current PRIMARY section of `.roadmap-coordination/parallel-clients.md` before each parent. One serial guarded PRIMARY runner, one bounded original parent per iteration; the independent EDITOR lane is protected.

Defer VM/guest operations, emulator or simulator/device checks, native UI/IME execution, native target bootstrap/readiness qualification and native desktop-shell execution. Do not start, stop, inspect for readiness or wait on a guest; do not turn a fixture or compilation into target-OS proof. Headless Swift/Kotlin/Dart consumers, local compiler/package checks, Node/PHP/SQLite and browser fixtures are allowed. Flutter/Dart doctor/compiler metadata checks on the current host are permitted; toolchain discovery may report platform capabilities as available/unknown/unsupported without launching a native target or running native OS qualification probes. No paid cloud provisioning, model/provider calls, secret loading, publication, push or deployment. All automated checks use prepared deterministic content and mocked provider/network transports.

Preserve every acceptance criterion below. A headless consumer must use the actual declared binding and existing shared authority; a stub is not a replacement for that boundary. If a selected check unexpectedly needs an excluded OS operation, record the exact unmet owner and changed-input condition, leave acceptance unchecked and return BLOCKED. Never retry unchanged input. Planned selectors and missing local wrappers are owned implementation work. Reuse compatible passing receipts; run only the affected named focused delivery check during functionality. Comprehensive backend/web verification follows all ten selected environment/functional parents; deferred native work is outside this run's phase barrier, not marked complete or used as a passed prerequisite. Broader native/all-platform qualification remains required and deferred. Current scope retains the basis plan's Node/browser, PHP/Laravel/Filament/SQLite and actually delivered headless clients; unselected languages, databases and OS targets gain no support claim. Existing caps, unknown-data preservation and single current production format remain unchanged.

Workers update only verified checkbox states and Status in this selected source. Store delivery text, source/artifact hashes and counts in the separate progress file; never write a source delivery summary. After two parents and at source boundaries, hold root `.roadmap-coordination/integration.lock`; checkpoint only validated safely separable owned source. Preserve inherited/unrelated dirty bytes and indexes; do not stage snapshots, source from the EDITOR checkout, generated artifacts or unrelated work. Keep mixed inherited implementation pending with exact owned patches if safe landing is unavailable. Clean task-owned inactive outputs/browsers/servers, preserve active processes and check disk. No agents or extra controllers.

## Selected original contracts

### Task UNC-1.1 — Map actual native command and view exports

- [x] UNC-1.1 Map actual native command and view exports.

Purpose: Map actual native command and view exports so applications can reuse this integration boundary.
Deliverable: `sdk/contracts/; native/*/; ../architecture/specs/native-ui-integrations.md`.
Context: [named contract section](../../specs/native-ui-integrations.md#portable-ui-contract); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [UIC-1.2](../editor-ui-integrations-20261024/00-contracts.md), [UIC-1.3](../editor-ui-integrations-20261024/00-contracts.md), [UIC-1.4](../editor-ui-integrations-20261024/00-contracts.md), [UIC-1.5](../editor-ui-integrations-20261024/00-contracts.md), [UIC-1.6](../editor-ui-integrations-20261024/00-contracts.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Each native command-state/target field maps to an existing Session/presenter capability or an exact owner gap; no UI task silently implements a new semantic command or duplicate host.

Implementation:

- [x] UNC-1.1-I1 Inspect current Swift/Kotlin/C ABI and desktop APIs; record needed control-state handles and per-platform entry receipts.
- [x] UNC-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UNC-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UNC-1.1`: Direct inspection of one command and one capture/dispose mapping per declared platform; count supported/gap rows. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UNC-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UNC-1.2 — Define native theme and control data bindings

- [x] UNC-1.2 Define native theme and control data bindings.

Purpose: Define native theme and control data bindings so applications can reuse this integration boundary.
Deliverable: `sdk/contracts/; native/*/`.
Context: [named contract section](../../specs/native-ui-integrations.md#portable-ui-contract); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UNC-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: One bounded data schema covers semantic tokens, locale/direction, accessibility preferences, control descriptors and state; no callbacks/components/DOM strings cross bridges.

Implementation:

- [x] UNC-1.2-I1 Map UIC token/state declarations to native public types and platform naming; declare executor/buffer/event ownership.
- [x] UNC-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UNC-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UNC-1.2`: Type/schema-check one prepared light/dark/mixed state DTO and reject an oversized/unknown required field. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UNC-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UNC-1.3 — Define cross-host overlay and event rules

- [x] UNC-1.3 Define cross-host overlay and event rules.

Purpose: Define cross-host overlay and event rules so applications can reuse this integration boundary.
Deliverable: `sdk/contracts/; ../architecture/specs/native-ui-integrations.md`.
Context: [named contract section](../../specs/native-ui-integrations.md#portable-ui-contract); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UNC-1.1, UNC-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Native overlay owners preserve captured targets, async completion ordering and session identity; coalescing UI snapshots cannot drop completion/error/dispose events.

Implementation:

- [x] UNC-1.3-I1 Specify explicit focus/coordinate conversion, target revocation and bounded event payload rules as additions to existing BCP/BNA/BDH contracts.
- [x] UNC-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UNC-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UNC-1.3`: Inspect prepared command/popup/dispose transcripts against existing native ownership rules; record gaps for the owning bridge. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UNC-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UNC-1.4 — Freeze per-platform UI export/support map

- [x] UNC-1.4 Freeze per-platform UI export/support map.

Purpose: Freeze per-platform UI export/support map so applications can reuse this integration boundary.
Deliverable: `native/*/; adapters/native/; ../architecture/specs/native-ui-integrations.md`.
Context: [named contract section](../../specs/native-ui-integrations.md#portable-ui-contract); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UNC-1.1, UNC-1.2, UNC-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: UIKit/SwiftUI/AppKit/Views/Compose/WinUI/WPF/GTK plus RN/Expo/Flutter mobile/web have exact planned UI ownership and maintained-baseline inputs; desktop RN/Flutter remain explicit feasibility profiles.

Implementation:

- [x] UNC-1.4-I1 Set optional UI product/module boundaries and per-surface capability declarations; preserve independent host and backend prerequisite edges.
- [x] UNC-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UNC-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UNC-1.4`: Review package/peer map and every required profile against the adoption table; no runtime support claim from this inspection. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UNC-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.
