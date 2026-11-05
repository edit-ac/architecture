# Complete Expo and Flutter UI/package coverage

Status: IN_PROGRESS

## Goal and entry conditions

Goal: Complete Expo and Flutter UI/package coverage. Planning source: 2026-10-24. Workspace: `core`. This is final-testing work; no completed capability is implied.

Authority: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/28-final-expo-flutter-testing.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

Entry receipts are scoped to each parent below. Verify the named public interface and focused acceptance against its consumed source revision; a queued predecessor or whole-file title is not evidence. Earlier-file progress has the same basename under `.roadmap-runner/editor-ui-integrations-20261024/`; existing backend-owner receipts live under `.roadmap-runner/backend-sdk-adapters-20261024/`. Read only the named parent receipt.

Final-phase entry: all required functionality in files 00–25 is delivered. This is a testing-sequencing gate, not permission to require unrelated language SDKs. Within this file consume only the platform/semantic/backend receipts needed for the current case. Actual browser/native/AT observations are registered with and consumed from roadmap43; mock/compile results cannot substitute.

## Execution and validation rules

All implementation paths below are core-relative unless prefixed `../architecture` or `../docs`; proposed paths must be reconciled to existing exports before creating files. Read the owning repository AGENTS.md before edits. A missing bridge/semantic API belongs to its named existing owner; do not implement a parallel one in a UI package.

One parent is one 15–45 minute session including focused validation. Split at a concrete boundary before exceeding the budget, preserving its acceptance and stable ID mapping. Budget inputs to this file, its named contract section, required predecessor receipt and only affected code; the controller index and other milestone bodies are not mandatory worker input.

The future core command `node scripts/ui-integration-delivery.mjs <task-id>` is introduced by UIC-1.5. It is a planned selector interface, not an existing command or passing test claim. Each later task registers the smallest relevant existing compiler/fixture/manual-observation wrapper; unknown/missing selectors and zero-case runs fail. Contract tasks before that dispatcher use the explicit direct checks below. Functional checks normally take 1–3 minutes, at most 5 minutes for an already provisioned native compiler/startup. Cold SDK installation, broad suites and comprehensive case authoring do not fit a delivery check. Final-testing tasks may spend up to 10 minutes on one declared bounded selector; split longer profiles across parents before starting them.

Use deterministic documents and local/mock transports only: no paid inference, credentials loaded into tests, provider recording, paid cloud builds, production access, deployment or publication. Keep generated packages, binaries, screenshots and logs in ignored task-owned directories. Preserve source, real user data and active processes. Use one current format, engine, command/history and persistence authority.

Independent work: a sibling with satisfied local dependencies and named entry receipts is eligible; queue order is not a dependency. Stop the affected worker on BLOCKED, record task/source/error/prerequisite fingerprint, owner, attempted repair and exact changed-input resume condition. Do not retry unchanged input or skip acceptance. A serial queue cannot jump a blocked file: only the existing coordinator may adopt a different ready subset at a safe guarded checkpoint. No runner start, enqueue, state edits or snapshot replacement is authorized by this source.

Workers may update verified checkboxes and Status only under the current installed runner policy. Hashes, results and handoff prose stay in separate ignored progress. A checked functional parent means its own narrow checks passed; it does not claim final UI/platform/accessibility qualification. Reuse compatible evidence and name the changed input before rerunning or widening. Final test/case development is in files 26–29 after all functional delivery, with existing BNT and roadmap43 owners retained.

## Epic UTX-1 — Complete Expo and Flutter UI/package coverage

### Task UTX-1.1 — Register stack-specific UI and installer observations

- [ ] UTX-1.1 Register stack-specific UI and installer observations.

Purpose: Register stack-specific UI and installer observations so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/cross-platform/; ../architecture/tests/`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BNT-1.2](../dependency-closed-ui-20261025/81-host-final-cases.md), [BNT-1.3](../dependency-closed-ui-20261025/81-host-final-cases.md), [BNT-1.4](../dependency-closed-ui-20261025/81-host-final-cases.md), [BNT-1.6](../dependency-closed-ui-20261025/81-host-final-cases.md), [UPG-1.4](25-packages-and-guides.md), [UPG-1.5](25-packages-and-guides.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Bare RN, Expo iOS/Android/web, Flutter iOS/Android/web and design-system variants have exact UI/package case owners; native input/recovery stays BNT-owned.

Implementation:

- [ ] UTX-1.1-I1 Map required stack profiles to package/artifact/runtime versions and roadmap43 observations; record unsupported desktop candidates separately.
- [ ] UTX-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTX-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UTX-1.1`: Inspect matrix completeness and reuse receipts; missing required profile cannot be relabeled optional. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTX-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTX-1.2 — Verify bare RN and native design-system kits

- [ ] UTX-1.2 Verify bare RN and native design-system kits.

Purpose: Verify bare RN and native design-system kits so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/react-native/`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTX-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Default native, Paper and Reusables UI install and expose correct state/theme/portal behavior; base RN imports neither Expo nor React DOM.

Implementation:

- [ ] UTX-1.2-I1 Add remaining installer/dependency/widget assertions and native accessibility observation requests.
- [ ] UTX-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTX-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UTX-1.2`: Run bounded kit selectors and consume actual native UI observations; no screenshot-only support claims. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTX-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTX-1.3 — Verify Expo CNG and native builds

- [ ] UTX-1.3 Verify Expo CNG and native builds.

Purpose: Verify Expo CNG and native builds so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/expo/`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTX-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Plugin is repeatable, app config is preserved, iOS/Android artifacts contain the canonical module, missing-native guard is useful and stock Expo Go is explicitly unsupported.

Implementation:

- [ ] UTX-1.3-I1 Add final CNG/installed-native packaging cases and local build profile assertions; reuse successful compile evidence for unchanged artifacts.
- [ ] UTX-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTX-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UTX-1.3`: Run missing prepared config/packaging selectors and consume current development-build target observations. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTX-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTX-1.4 — Verify Expo web, native UI recipe and runtime policy

- [ ] UTX-1.4 Verify Expo web, native UI recipe and runtime policy.

Purpose: Verify Expo web, native UI recipe and runtime policy so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/expo/`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTX-1.1, UTX-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Web/native conditional exports separate artifacts; Router/Expo UI controls have correct host/focus behavior; incompatible native capability/runtime input rejects safely without publishing an update.

Implementation:

- [ ] UTX-1.4-I1 Add missing conditional-import/runtime-policy cases and UI recipe observations; consume BNT navigation/background results.
- [ ] UTX-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTX-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UTX-1.4`: Run affected web/runtime selectors and consume roadmap43 native UI observations plus exact BNT-1.2/1.4 receipts. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTX-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTX-1.5 — Verify Flutter mobile themes and platform-view overlays

- [ ] UTX-1.5 Verify Flutter mobile themes and platform-view overlays.

Purpose: Verify Flutter mobile themes and platform-view overlays so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/flutter/`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTX-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Material/Cupertino variants preserve native host identity through rebuild/theme changes, with correct iOS/Android z-order/gestures/insets/scaling and accessible control state.

Implementation:

- [ ] UTX-1.5-I1 Add missing UI/overlay assertions and platform-view observation recipes; route actual text input/selection/composition checks to BNT-1.3.
- [ ] UTX-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTX-1.5-V1 Run `node scripts/ui-integration-delivery.mjs UTX-1.5`: Run bounded mobile UI cases and consume both platform observations and BNT input/teardown receipts. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTX-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTX-1.6 — Verify Flutter web and unsupported desktop profiles

- [ ] UTX-1.6 Verify Flutter web and unsupported desktop profiles.

Purpose: Verify Flutter web and unsupported desktop profiles so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/flutter/`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTX-1.1, UTX-1.5.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Flutter web uses one browser editor and correct controls/assets without native lookup; unsupported desktop profiles return typed capability errors and no false native UI support claim.

Implementation:

- [ ] UTX-1.6-I1 Add installed web/JS bridge and capability-manifest cases; cross-check feasibility decisions against claimed support.
- [ ] UTX-1.6-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTX-1.6-V1 Run `node scripts/ui-integration-delivery.mjs UTX-1.6`: Build/run the missing web UI selector and inspect each desktop capability response; reuse browser semantic evidence. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTX-1.6 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/28-final-expo-flutter-testing.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- BNT-1.2: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/81-host-final-cases.progress.md`.
- BNT-1.3: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/81-host-final-cases.progress.md`.
- BNT-1.4: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/81-host-final-cases.progress.md`.
- BNT-1.6: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/81-host-final-cases.progress.md`.
- UPG-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/25-packages-and-guides.progress.md`.
- UPG-1.5: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/25-packages-and-guides.progress.md`.
