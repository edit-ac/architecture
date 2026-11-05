# Deliver Flutter mobile controls and themes

Status: IN_PROGRESS

## Goal and entry conditions

Goal: Deliver Flutter mobile controls and themes. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/native-ui-integrations.md#flutter); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/23-flutter-mobile-ui.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

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

## Epic UFL-1 — Deliver Flutter mobile controls and themes

### Task UFL-1.1 — Expose a style-neutral Flutter controls controller

- [ ] UFL-1.1 Expose a style-neutral Flutter controls controller.

Purpose: Expose a style-neutral Flutter controls controller so applications can reuse this integration boundary.
Deliverable: `adapters/native/flutter/; packages/flutter/`.
Context: [named contract section](../../specs/native-ui-integrations.md#flutter); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BCP-1.1](../dependency-closed-ui-20261025/28-flutter-react-native-bindings.md), [BCP-1.2](../dependency-closed-ui-20261025/28-flutter-react-native-bindings.md), [BCP-1.3](../dependency-closed-ui-20261025/28-flutter-react-native-bindings.md), [UNC-1.4](15-native-ui-contracts.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Dart UI state observes the BCP-owned native plugin/widget with one Session and bounded events; Dart backend client remains independent of Flutter. Rebuild/dispose does not reimport content.

Implementation:

- [ ] UFL-1.1-I1 Add immutable controller/listenable projections and typed native theme/control setters to the existing plugin API; return missing native fields to BCP owner.
- [ ] UFL-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UFL-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UFL-1.1`: Compile one Dart/Flutter consumer and run the existing prepared event/dispose transcript with UI observations. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UFL-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UFL-1.2 — Build Material toolbar and status composition

- [ ] UFL-1.2 Build Material toolbar and status composition.

Purpose: Build Material toolbar and status composition so applications can reuse this integration boundary.
Deliverable: `packages/flutter_ui/; adapters/native/flutter/`.
Context: [named contract section](../../specs/native-ui-integrations.md#flutter); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UFL-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Optional Material controls expose toolbar/groups/history/formatting/block selector/status using shared state and app Theme; style-neutral/plugin imports do not require a design-system package.

Implementation:

- [ ] UFL-1.2-I1 Implement configurable Material builders using the maintained Flutter design-system baseline; preserve native text surface ownership.
- [ ] UFL-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UFL-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UFL-1.2`: Compile a Material consumer and inspect one command/disabled/theme transition with stable native host ID. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UFL-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UFL-1.3 — Build Cupertino toolbar and status composition

- [ ] UFL-1.3 Build Cupertino toolbar and status composition.

Purpose: Build Cupertino toolbar and status composition so applications can reuse this integration boundary.
Deliverable: `packages/flutter_ui/; adapters/native/flutter/`.
Context: [named contract section](../../specs/native-ui-integrations.md#flutter); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UFL-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Cupertino controls provide equivalent agreed command/status coverage with native-looking typography/actions and explicit builder overrides; no duplicate semantic logic.

Implementation:

- [ ] UFL-1.3-I1 Add separate Cupertino exports and map semantic tokens to the current Cupertino theme primitives.
- [ ] UFL-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UFL-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UFL-1.3`: Compile a Cupertino consumer and execute one command/theme transition without reimporting content. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UFL-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UFL-1.4 — Add Flutter dialogs and suggestion controls

- [ ] UFL-1.4 Add Flutter dialogs and suggestion controls.

Purpose: Add Flutter dialogs and suggestion controls so applications can reuse this integration boundary.
Deliverable: `packages/flutter_ui/; adapters/native/flutter/`.
Context: [named contract section](../../specs/native-ui-integrations.md#flutter); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UFL-1.2, UFL-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Dialog/menu/reference/command parts use guarded native targets, correct result semantics and bounded cancellation; overlay placement is explicit over platform views.

Implementation:

- [ ] UFL-1.4-I1 Compose shared controller/query state into Material/Cupertino overlay builders; convert native selection coordinates without changing native IME ownership.
- [ ] UFL-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UFL-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UFL-1.4`: Run one prepared reference/link flow and a canceled late result; inspect owner/coordinate data. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UFL-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UFL-1.5 — Integrate iOS platform-view geometry and preferences

- [ ] UFL-1.5 Integrate iOS platform-view geometry and preferences.

Purpose: Integrate iOS platform-view geometry and preferences so applications can reuse this integration boundary.
Deliverable: `adapters/native/flutter/platform/; packages/flutter_ui/`.
Context: [named contract section](../../specs/native-ui-integrations.md#flutter); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UFL-1.1, UFL-1.4.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: iOS platform-view overlays, hit testing, safe areas, text scale and focus/composition use the existing native host; theme/rebuild cannot replace the Session.

Implementation:

- [ ] UFL-1.5-I1 Wire the BCP iOS view geometry/accessibility callbacks into Flutter UI layout and gestures; repair bridge defects only under its owner.
- [ ] UFL-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UFL-1.5-V1 Run `node scripts/ui-integration-delivery.mjs UFL-1.5`: Compile the iOS plugin/example and run one existing prepared geometry/theme transcript; defer device/AT observation. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UFL-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UFL-1.6 — Integrate Android platform-view composition

- [ ] UFL-1.6 Integrate Android platform-view composition.

Purpose: Integrate Android platform-view composition so applications can reuse this integration boundary.
Deliverable: `adapters/native/flutter/platform/; packages/flutter_ui/`.
Context: [named contract section](../../specs/native-ui-integrations.md#flutter); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UFL-1.1, UFL-1.4.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: The declared Android composition mode supports editor focus, overlay z-order, keyboard insets and gestures; alternatives/limitations are explicit and no hidden WebView is used.

Implementation:

- [ ] UFL-1.6-I1 Select the supported mode from actual native view requirements, wire geometry/inset/theme callbacks and document the reason; no speculative renderer replacement.
- [ ] UFL-1.6-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UFL-1.6-V1 Run `node scripts/ui-integration-delivery.mjs UFL-1.6`: Compile the Android plugin/example and inspect one prepared keyboard/overlay/gesture transcript with stable host identity. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UFL-1.6 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UFL-1.7 — Extend the existing Flutter application example

- [ ] UFL-1.7 Extend the existing Flutter application example.

Purpose: Extend the existing Flutter application example so applications can reuse this integration boundary.
Deliverable: `examples/sdk-adapters/flutter/`.
Context: [named contract section](../../specs/native-ui-integrations.md#flutter); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BCP-1.6](../dependency-closed-ui-20261025/28-flutter-react-native-bindings.md).
Dependencies: UFL-1.2, UFL-1.3, UFL-1.4, UFL-1.5, UFL-1.6.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: The BCP example can select Material or Cupertino UI, customize one control and reopen the same document through its existing backend path; style/plugin packages are separable.

Implementation:

- [ ] UFL-1.7-I1 Add UI package installation and controller composition to the existing app; reuse BCP save/recovery code and describe mobile platform requirements.
- [ ] UFL-1.7-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UFL-1.7-V1 Run `node scripts/ui-integration-delivery.mjs UFL-1.7`: Build the changed app entry and reuse BCP prepared save/reopen evidence plus one UI-customization check. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UFL-1.7 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/23-flutter-mobile-ui.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- BCP-1.1: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/28-flutter-react-native-bindings.progress.md`.
- BCP-1.2: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/28-flutter-react-native-bindings.progress.md`.
- BCP-1.3: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/28-flutter-react-native-bindings.progress.md`.
- BCP-1.6: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/28-flutter-react-native-bindings.progress.md`.
- UNC-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/15-native-ui-contracts.progress.md`.
