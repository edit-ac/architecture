# Deliver UIKit and SwiftUI controls

Status: IN_PROGRESS

## Goal and entry conditions

Goal: Deliver UIKit and SwiftUI controls. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/16-apple-mobile-ui.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

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

## Epic UIA-1 — Deliver UIKit and SwiftUI controls

### Task UIA-1.1 — Add UIKit command-state and theme binding

- [ ] UIA-1.1 Add UIKit command-state and theme binding.

Purpose: Add UIKit command-state and theme binding so applications can reuse this integration boundary.
Deliverable: `native/ios/Sources/; native/ios/Package.swift`.
Context: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BNA-1.2](../dependency-closed-ui-20261025/21-apple-ui-bindings.md), [UNC-1.4](15-native-ui-contracts.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: An optional UIKit UI product observes one existing native host on the main actor, maps dynamic colors/type and disposes observers without replacing the Session.

Implementation:

- [ ] UIA-1.1-I1 Bind UNC snapshots/theme to the actual UIKit export and expose readonly host customization props.
- [ ] UIA-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UIA-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UIA-1.1`: Compile the UI target and run one prepared state/theme observer transcript with the existing host fixture. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIA-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UIA-1.2 — Add UIKit toolbar and parameter menu

- [ ] UIA-1.2 Add UIKit toolbar and parameter menu.

Purpose: Add UIKit toolbar and parameter menu so applications can reuse this integration boundary.
Deliverable: `native/ios/Sources/`.
Context: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UIA-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Formatting/history/block-type controls use shared availability/mixed state and native actions; parameter controls retain captured targets across presentation.

Implementation:

- [ ] UIA-1.2-I1 Implement configurable toolbar/groups/actions and link parameter presentation using existing host capture APIs.
- [ ] UIA-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UIA-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UIA-1.2`: Execute one toolbar action and canceled link dialog in an existing native host delivery fixture. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIA-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UIA-1.3 — Integrate system edit menu and suggestions

- [ ] UIA-1.3 Integrate system edit menu and suggestions.

Purpose: Integrate system edit menu and suggestions so applications can reuse this integration boundary.
Deliverable: `native/ios/Sources/`.
Context: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UIA-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Custom actions supplement system edit menus without replacing copy/paste/input services; suggestion popovers preserve responder/composition and bounded query lifecycle.

Implementation:

- [ ] UIA-1.3-I1 Connect UIEditMenuInteraction contributions and one reference/command result view to shared target/query state.
- [ ] UIA-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UIA-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UIA-1.3`: Use one prepared edit-menu invocation and canceled reference query; inspect original responder and event order. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIA-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UIA-1.4 — Expose SwiftUI control composition

- [ ] UIA-1.4 Expose SwiftUI control composition.

Purpose: Expose SwiftUI control composition so applications can reuse this integration boundary.
Deliverable: `native/ios/Sources/; native/ios/Package.swift`.
Context: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BNA-1.3](../dependency-closed-ui-20261025/21-apple-ui-bindings.md), [UNC-1.4](15-native-ui-contracts.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: SwiftUI toolbar/menu/status wrappers use the existing representable and UI state; view updates do not remount or reimport the document.

Implementation:

- [ ] UIA-1.4-I1 Add observable view state and native SwiftUI builders for toolbar/menu/status with explicit platform availability.
- [ ] UIA-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UIA-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UIA-1.4`: Compile one representable consumer and replay a theme/recomposition update with stable native session ID. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIA-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UIA-1.5 — Map mobile viewport and accessibility preferences

- [ ] UIA-1.5 Map mobile viewport and accessibility preferences.

Purpose: Map mobile viewport and accessibility preferences so applications can reuse this integration boundary.
Deliverable: `native/ios/Sources/`.
Context: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UIA-1.2, UIA-1.3, UIA-1.4.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Toolbar/overlays adapt to safe area, keyboard, Dynamic Type and direction; native text and chrome do not double-scale and async UI does not dismiss/reopen the keyboard unexpectedly.

Implementation:

- [ ] UIA-1.5-I1 Wire host geometry/accessibility preferences to UIKit/SwiftUI UI resources; preserve platform defaults and minimum target sizes.
- [ ] UIA-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UIA-1.5-V1 Run `node scripts/ui-integration-delivery.mjs UIA-1.5`: Inspect one large-text/RTL/keyboard-inset prepared layout plus unchanged document identity; final VoiceOver observation stays final-owned. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIA-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/16-apple-mobile-ui.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- BNA-1.2: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/21-apple-ui-bindings.progress.md`.
- BNA-1.3: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/21-apple-ui-bindings.progress.md`.
- UNC-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/15-native-ui-contracts.progress.md`.
