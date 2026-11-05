# Deliver React Native controls and design-system kits

Status: IN_PROGRESS

## Goal and entry conditions

Goal: Deliver React Native controls and design-system kits. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/21-react-native-ui.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

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

## Epic URN-1 — Deliver React Native controls and design-system kits

### Task URN-1.1 — Expose UI selectors over the existing native component

- [ ] URN-1.1 Expose UI selectors over the existing native component.

Purpose: Expose UI selectors over the existing native component so applications can reuse this integration boundary.
Deliverable: `adapters/native/react-native/; packages/react-native/`.
Context: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BCP-1.4](../dependency-closed-ui-20261025/28-flutter-react-native-bindings.md), [BCP-1.5](../dependency-closed-ui-20261025/28-flutter-react-native-bindings.md), [UNC-1.4](15-native-ui-contracts.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Existing BCP Fabric/module exports expose stable command/theme/view observations to JS; no React DOM, Expo dependency or second native view implementation is added. Missing bridge fields are returned to BCP with precise acceptance.

Implementation:

- [ ] URN-1.1-I1 Add RN UI selectors/context and bounded prop/state mapping using the canonical native bridge; preserve serialized handle ownership and late-event invalidation.
- [ ] URN-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] URN-1.1-V1 Run `node scripts/ui-integration-delivery.mjs URN-1.1`: Compile the JS consumer and existing native entry points, then replay one prepared state/dispose transcript; no target-runtime support claim. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave URN-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task URN-1.2 — Build default native toolbar controls

- [ ] URN-1.2 Build default native toolbar controls.

Purpose: Build default native toolbar controls so applications can reuse this integration boundary.
Deliverable: `packages/react-native/src/ui/; adapters/native/react-native/`.
Context: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: URN-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Native toolbar/button/group/block-type parts expose configurable builders, pressed/mixed/disabled accessibility states, native hit targets and host theme props; each activation reaches one native command.

Implementation:

- [ ] URN-1.2-I1 Implement the default native components over RN UI selectors using native views/press events, without DOM CSS or copied editor semantics.
- [ ] URN-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] URN-1.2-V1 Run `node scripts/ui-integration-delivery.mjs URN-1.2`: Use one existing RN host fixture for formatting and readonly transition; inspect accessibility role/state props. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave URN-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task URN-1.3 — Add native overlay and suggestion parts

- [ ] URN-1.3 Add native overlay and suggestion parts.

Purpose: Add native overlay and suggestion parts so applications can reuse this integration boundary.
Deliverable: `packages/react-native/src/ui/`.
Context: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: URN-1.1, URN-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Menu/link/reference/command/status parts preserve native target ownership across modal/sheet placement, keyboard/safe-area changes and canceled async results.

Implementation:

- [ ] URN-1.3-I1 Bind native overlay/container and query lifecycle to RN renderers; distinguish command actions from selectable options and retain native IME ownership.
- [ ] URN-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] URN-1.3-V1 Run `node scripts/ui-integration-delivery.mjs URN-1.3`: Replay one sheet-based reference picker with a late result after dismissal and one valid link action. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave URN-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task URN-1.4 — Add Paper theme adapter

- [ ] URN-1.4 Add Paper theme adapter.

Purpose: Add Paper theme adapter so applications can reuse this integration boundary.
Deliverable: `packages/react-native-paper/; examples/ui/react-native-paper/`.
Context: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: URN-1.2, URN-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Optional Paper controls map the agreed tokens and state while the base RN package stays independent of Paper; navigation and editor themes can be coordinated without remount.

Implementation:

- [ ] URN-1.4-I1 Wrap default control builders with the maintained Paper primitives and explicit peer ranges; include toolbar/dialog/status composition.
- [ ] URN-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] URN-1.4-V1 Run `node scripts/ui-integration-delivery.mjs URN-1.4`: Compile one Paper consumer and inspect light/dark plus disabled/mixed states with a stable editor ID. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave URN-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task URN-1.5 — Add React Native Reusables source kit

- [ ] URN-1.5 Add React Native Reusables source kit.

Purpose: Add React Native Reusables source kit so applications can reuse this integration boundary.
Deliverable: `registry/react-native/; examples/ui/react-native-reusables/`.
Context: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: URN-1.2, URN-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: A native source kit installs a frame/toolbar and contextual composition over RN UI APIs with one pinned NativeWind or Uniwind baseline; no React DOM/Radix DOM dependency or hidden WebView.

Implementation:

- [ ] URN-1.5-I1 Author source items and ecosystem installer metadata, mapping theme variables/icons/portal host to the RN adapter; preserve application-owned files.
- [ ] URN-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] URN-1.5-V1 Run `node scripts/ui-integration-delivery.mjs URN-1.5`: Install one composition in a disposable native app and compile JS/native imports; inspect production style generation and no DOM dependency. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave URN-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task URN-1.6 — Expose custom native content and controls theme API

- [ ] URN-1.6 Expose custom native content and controls theme API.

Purpose: Expose custom native content and controls theme API so applications can reuse this integration boundary.
Deliverable: `packages/react-native/; adapters/native/react-native/`.
Context: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: URN-1.1, URN-1.2, URN-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Theme, locale/direction and supported content-style props update the existing native host without replacing document/session; unsupported style capabilities are typed and cannot alter semantic marks.

Implementation:

- [ ] URN-1.6-I1 Wire the UNC typed theme fields to existing bridge setters and document limits; expose native custom-control builders and per-editor themes.
- [ ] URN-1.6-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] URN-1.6-V1 Run `node scripts/ui-integration-delivery.mjs URN-1.6`: Replay one two-editor theme/large-text update and verify unchanged canonical identity plus independent control state. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave URN-1.6 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/21-react-native-ui.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- BCP-1.4: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/28-flutter-react-native-bindings.progress.md`.
- BCP-1.5: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/28-flutter-react-native-bindings.progress.md`.
- UNC-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/15-native-ui-contracts.progress.md`.
