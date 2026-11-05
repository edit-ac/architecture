# Deliver Flutter web and bound desktop embedding claims

Status: IN_PROGRESS

## Goal and entry conditions

Goal: Deliver Flutter web and bound desktop embedding claims. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/native-ui-integrations.md#flutter); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/24-flutter-web-and-desktop-profiles.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

Entry receipts are scoped to each parent below. Verify the named public interface and focused acceptance against its consumed source revision; a queued predecessor or whole-file title is not evidence. Earlier-file progress has the same basename under `.roadmap-runner/editor-ui-integrations-20261024/`; existing backend-owner receipts live under `.roadmap-runner/backend-sdk-adapters-20261024/`. Read only the named parent receipt.

## Execution and validation rules

All implementation paths below are core-relative unless prefixed `../architecture` or `../docs`; proposed paths must be reconciled to existing exports before creating files. Read the owning repository AGENTS.md before edits. A missing bridge/semantic API belongs to its named existing owner; do not implement a parallel one in a UI package.

One parent is one 15–45 minute session including focused validation. Split at a concrete boundary before exceeding the budget, preserving its acceptance and stable ID mapping. Budget inputs to this file, its named contract section, required predecessor receipt and only affected code; the controller index and other milestone bodies are not mandatory worker input.

The future core command `node scripts/ui-integration-delivery.mjs <task-id>` is introduced by UIC-1.5. It is a planned selector interface, not an existing command or passing test claim. Each later task registers the smallest relevant existing compiler/fixture/manual-observation wrapper; unknown/missing selectors and zero-case runs fail. Contract tasks before that dispatcher use the explicit direct checks below. Functional checks normally take 1–3 minutes, at most 5 minutes for an already provisioned native compiler/startup. Cold SDK installation, broad suites and comprehensive case authoring do not fit a delivery check. Final-testing tasks may spend up to 10 minutes on one declared bounded selector; split longer profiles across parents before starting them.

Use deterministic documents and local/mock transports only: no paid inference, credentials loaded into tests, provider recording, paid cloud builds, production access, deployment or publication. Keep generated packages, binaries, screenshots and logs in ignored task-owned directories. Preserve source, real user data and active processes. Use one current format, engine, command/history and persistence authority.

Independent work: a sibling with satisfied local dependencies and named entry receipts is eligible; queue order is not a dependency. Stop the affected worker on BLOCKED, record task/source/error/prerequisite fingerprint, owner, attempted repair and exact changed-input resume condition. Do not retry unchanged input or skip acceptance. A serial queue cannot jump a blocked file: only the existing coordinator may adopt a different ready subset at a safe guarded checkpoint. No runner start, enqueue, state edits or snapshot replacement is authorized by this source.

Workers may update verified checkboxes and Status only under the current installed runner policy. Hashes, results and handoff prose stay in separate ignored progress. A checked functional parent means its own narrow checks passed; it does not claim final UI/platform/accessibility qualification. Reuse compatible evidence and name the changed input before rerunning or widening. Final test/case development is in files 26–29 after all functional delivery, with existing BNT and roadmap43 owners retained.

## Focused delivery validation authority

Focused runtime delivery checks are authorized by the controller: /Users/bpstr/Github/edit-ac/architecture/runner-queues/dependency-closed-ui-20261025/delivery-check-policy.md. Read that bounded policy before interpreting this source’s validation scope. Execute only the deterministic compiler/fixture/browser/native/manual check named by the current parent; register its minimal missing wrapper when needed and report actual runtime counts separately. Comprehensive suites, case matrices and final qualification remain after functional delivery. A phase label alone is not a runtime prohibition; preserve every acceptance gate and reuse compatible passing evidence.

## Epic UFW-1 — Deliver Flutter web and bound desktop embedding claims

### Task UFW-1.1 — Define the Flutter web platform interface

- [ ] UFW-1.1 Define the Flutter web platform interface.

Purpose: Define the Flutter web platform interface so applications can reuse this integration boundary.
Deliverable: `adapters/native/flutter/web/; packages/flutter/`.
Context: [named contract section](../../specs/native-ui-integrations.md#flutter); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [UCS-1.6](02-controls-state.md), [UFL-1.1](23-flutter-mobile-ui.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Dart-facing controls/capabilities map to the existing browser editor through one bounded JS bridge; no iframe, separate document model or native-support assertion.

Implementation:

- [ ] UFW-1.1-I1 Extend the existing plugin platform interface for explicit web capabilities and web-host lifecycle using maintained Dart JS interop.
- [ ] UFW-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UFW-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UFW-1.1`: Type-check one prepared command/state mapping and absent-native-service capability response. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UFW-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UFW-1.2 — Embed the browser editor and optional Flutter chrome

- [ ] UFW-1.2 Embed the browser editor and optional Flutter chrome.

Purpose: Embed the browser editor and optional Flutter chrome so applications can reuse this integration boundary.
Deliverable: `adapters/native/flutter/web/; packages/flutter_ui/`.
Context: [named contract section](../../specs/native-ui-integrations.md#flutter); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UFW-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: HTML host view owns one browser editor with explicit WASM/assets/CSS loading; widget rebuild/theme update does not reimport document or create another instance.

Implementation:

- [ ] UFW-1.2-I1 Implement host mount/disposal and coordinate/overlay handoff; choose one chrome owner and prevent duplicate DOM/Flutter toolbars.
- [ ] UFW-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UFW-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UFW-1.2`: Build one web example and mount/rebuild/dispose with an existing deterministic browser fixture. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UFW-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UFW-1.3 — Deliver the Flutter web example and capability guide

- [ ] UFW-1.3 Deliver the Flutter web example and capability guide.

Purpose: Deliver the Flutter web example and capability guide so applications can reuse this integration boundary.
Deliverable: `examples/sdk-adapters/flutter/web/`.
Context: [named contract section](../../specs/native-ui-integrations.md#flutter); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UFW-1.1, UFW-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: The installed web plugin works with declared browser assets and UI imports, uses existing backend DTOs and clearly separates native-only capabilities; unsupported inputs reject before mutation.

Implementation:

- [ ] UFW-1.3-I1 Add web installation/build instructions and one custom toolbar/reference composition using the existing Flutter app backend facade.
- [ ] UFW-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UFW-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UFW-1.3`: Production-build the example and run one prepared edit/control/save-state transcript; reuse persistence owner evidence. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UFW-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UFW-1.4 — Resolve Flutter and React Native desktop host feasibility

- [ ] UFW-1.4 Resolve Flutter and React Native desktop host feasibility.

Purpose: Resolve Flutter and React Native desktop host feasibility so applications can reuse this integration boundary.
Deliverable: `adapters/native/flutter/; adapters/native/react-native/; ../architecture/specs/native-ui-integrations.md`.
Context: [named contract section](../../specs/native-ui-integrations.md#flutter); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [UNC-1.4](15-native-ui-contracts.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: A bounded decision for macOS/Windows/Linux records actual available embedding APIs, missing prerequisite and owner, and per-stack supported/unsupported status. Native SDK availability alone is never claimed as Flutter/RN desktop support.

Implementation:

- [ ] UFW-1.4-I1 Time-box documentation/API inspection to 30 minutes; name an implementable extension task set for any proven path, otherwise return typed unsupported capability and exact unblock condition. Do not create a new renderer.
- [ ] UFW-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UFW-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UFW-1.4`: Inspect one capability response per candidate stack/OS and verify every claimed available path cites a current host API; report investigation counts rather than fabricated runtime passes. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UFW-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/24-flutter-web-and-desktop-profiles.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- UCS-1.6: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/02-controls-state.progress.md`.
- UFL-1.1: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/23-flutter-mobile-ui.progress.md`.
- UNC-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/15-native-ui-contracts.progress.md`.
