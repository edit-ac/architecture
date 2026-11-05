# Deliver Android Views and Compose controls

Status: IN_PROGRESS

## Goal and entry conditions

Goal: Deliver Android Views and Compose controls. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/18-android-ui.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

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

## Epic UAN-1 — Deliver Android Views and Compose controls

### Task UAN-1.1 — Add optional Views UI module and state binding

- [ ] UAN-1.1 Add optional Views UI module and state binding.

Purpose: Add optional Views UI module and state binding so applications can reuse this integration boundary.
Deliverable: `native/android/sdk/; native/android/ui-views/`.
Context: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BNA-1.6](../dependency-closed-ui-20261025/23-android-ui-bindings.md), [UNC-1.4](15-native-ui-contracts.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Views consumers get readonly state/theme controls with one existing Kotlin Session and UI-thread dispatch; Compose is not a dependency.

Implementation:

- [ ] UAN-1.1-I1 Add the optional UI module and bind UNC state/tokens to actual Android host exports with observer cleanup.
- [ ] UAN-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UAN-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UAN-1.1`: Compile a Views consumer and run one existing prepared state/disposal transcript. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UAN-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UAN-1.2 — Add Views toolbar, action menu and link control

- [ ] UAN-1.2 Add Views toolbar, action menu and link control.

Purpose: Add Views toolbar, action menu and link control so applications can reuse this integration boundary.
Deliverable: `native/android/ui-views/`.
Context: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UAN-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Toolbar/history/formatting/block actions reflect state and delegate to shared targets; system action mode and native clipboard remain available.

Implementation:

- [ ] UAN-1.2-I1 Compose configurable Material-compatible controls and parameter presentation without overriding native input ownership.
- [ ] UAN-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UAN-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UAN-1.2`: Activate one formatting action and cancel a link dialog using the existing host fixture. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UAN-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UAN-1.3 — Add Views suggestions and geometry mapping

- [ ] UAN-1.3 Add Views suggestions and geometry mapping.

Purpose: Add Views suggestions and geometry mapping so applications can reuse this integration boundary.
Deliverable: `native/android/ui-views/`.
Context: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UAN-1.1, UAN-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Result popup placement follows native selection and keyboard insets; query cancellation and focus transfer preserve composition and do not retarget another editor.

Implementation:

- [ ] UAN-1.3-I1 Map UNC geometry/owner context into command/reference popup parts with font scale and direction.
- [ ] UAN-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UAN-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UAN-1.3`: Inspect one prepared keyboard-inset query popup and late-result cancellation. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UAN-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UAN-1.4 — Add Compose toolbar and theme integration

- [ ] UAN-1.4 Add Compose toolbar and theme integration.

Purpose: Add Compose toolbar and theme integration so applications can reuse this integration boundary.
Deliverable: `native/android/ui-compose/`.
Context: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BNA-1.7](../dependency-closed-ui-20261025/23-android-ui-bindings.md), [UNC-1.4](15-native-ui-contracts.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Compose Material controls wrap the existing AndroidView host, use shared state and accept host builders; recomposition/theme changes do not replace the editor.

Implementation:

- [ ] UAN-1.4-I1 Create an optional Compose module with toolbar/menu/status builders and Material token mapping.
- [ ] UAN-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UAN-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UAN-1.4`: Compile one Compose host and observe state/theme recomposition with a stable Session handle. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UAN-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UAN-1.5 — Connect Compose overlays and adaptive states

- [ ] UAN-1.5 Connect Compose overlays and adaptive states.

Purpose: Connect Compose overlays and adaptive states so applications can reuse this integration boundary.
Deliverable: `native/android/ui-compose/`.
Context: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UAN-1.3, UAN-1.4.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Compose popup/dialog/suggestion parts share host targets and result states; large font, RTL and keyboard avoidance are explicit and native accessibility semantics remain intact.

Implementation:

- [ ] UAN-1.5-I1 Reuse native UI/query DTOs for Compose overlay parts; define focus/gesture handoff and dispose observers on leave.
- [ ] UAN-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UAN-1.5-V1 Run `node scripts/ui-integration-delivery.mjs UAN-1.5`: Run one prepared modal reference/cancel interaction and inspect semantics/geometry with large text. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UAN-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/18-android-ui.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- BNA-1.6: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/23-android-ui-bindings.progress.md`.
- BNA-1.7: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/23-android-ui-bindings.progress.md`.
- UNC-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/15-native-ui-contracts.progress.md`.
