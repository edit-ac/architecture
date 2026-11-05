# Complete native toolkit UI coverage

Status: IN_PROGRESS

## Goal and entry conditions

Goal: Complete native toolkit UI coverage. Planning source: 2026-10-24. Workspace: `core`. This is final-testing work; no completed capability is implied.

Authority: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/27-final-native-ui-testing.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

Entry receipts are scoped to each parent below. Verify the named public interface and focused acceptance against its consumed source revision; a queued predecessor or whole-file title is not evidence. Earlier-file progress has the same basename under `.roadmap-runner/editor-ui-integrations-20261024/`; existing backend-owner receipts live under `.roadmap-runner/backend-sdk-adapters-20261024/`. Read only the named parent receipt.

Final-phase entry: all required functionality in files 00–25 is delivered. This is a testing-sequencing gate, not permission to require unrelated language SDKs. Within this file consume only the platform/semantic/backend receipts needed for the current case. Actual browser/native/AT observations are registered with and consumed from roadmap43; mock/compile results cannot substitute.

## Execution and validation rules

All implementation paths below are core-relative unless prefixed `../architecture` or `../docs`; proposed paths must be reconciled to existing exports before creating files. Read the owning repository AGENTS.md before edits. A missing bridge/semantic API belongs to its named existing owner; do not implement a parallel one in a UI package.

One parent is one 15–45 minute session including focused validation. Split at a concrete boundary before exceeding the budget, preserving its acceptance and stable ID mapping. Budget inputs to this file, its named contract section, required predecessor receipt and only affected code; the controller index and other milestone bodies are not mandatory worker input.

The future core command `node scripts/ui-integration-delivery.mjs <task-id>` is introduced by UIC-1.5. It is a planned selector interface, not an existing command or passing test claim. Each later task registers the smallest relevant existing compiler/fixture/manual-observation wrapper; unknown/missing selectors and zero-case runs fail. Contract tasks before that dispatcher use the explicit direct checks below. Functional checks normally take 1–3 minutes, at most 5 minutes for an already provisioned native compiler/startup. Cold SDK installation, broad suites and comprehensive case authoring do not fit a delivery check. Final-testing tasks may spend up to 10 minutes on one declared bounded selector; split longer profiles across parents before starting them.

Use deterministic documents and local/mock transports only: no paid inference, credentials loaded into tests, provider recording, paid cloud builds, production access, deployment or publication. Keep generated packages, binaries, screenshots and logs in ignored task-owned directories. Preserve source, real user data and active processes. Use one current format, engine, command/history and persistence authority.

Independent work: a sibling with satisfied local dependencies and named entry receipts is eligible; queue order is not a dependency. Stop the affected worker on BLOCKED, record task/source/error/prerequisite fingerprint, owner, attempted repair and exact changed-input resume condition. Do not retry unchanged input or skip acceptance. A serial queue cannot jump a blocked file: only the existing coordinator may adopt a different ready subset at a safe guarded checkpoint. No runner start, enqueue, state edits or snapshot replacement is authorized by this source.

Workers may update verified checkboxes and Status only under the current installed runner policy. Hashes, results and handoff prose stay in separate ignored progress. A checked functional parent means its own narrow checks passed; it does not claim final UI/platform/accessibility qualification. Reuse compatible evidence and name the changed input before rerunning or widening. Final test/case development is in files 26–29 after all functional delivery, with existing BNT and roadmap43 owners retained.

## Epic UTN-1 — Complete native toolkit UI coverage

### Task UTN-1.1 — Register native UI observations and authority reuse

- [ ] UTN-1.1 Register native UI observations and authority reuse.

Purpose: Register native UI observations and authority reuse so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/native/; ../architecture/tests/`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BNT-1.3](../dependency-closed-ui-20261025/81-host-final-cases.md), [BNT-1.5](../dependency-closed-ui-20261025/81-host-final-cases.md), [BNT-1.6](../dependency-closed-ui-20261025/81-host-final-cases.md), [UPG-1.4](25-packages-and-guides.md), [UPG-1.5](25-packages-and-guides.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: UIKit/SwiftUI/AppKit/Views/Compose/WinUI/WPF/GTK have named UI cases and required OS/AT profiles; BNT input/history/lifecycle evidence is reused and roadmap43 owns execution.

Implementation:

- [ ] UTN-1.1-I1 Define missing toolbar/menu/theme/overlay cases and precise target artifact requests; no host simulation is relabeled native evidence.
- [ ] UTN-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTN-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UTN-1.1`: Inspect case/owner/profile map and input receipts with nonzero case counts. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTN-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTN-1.2 — Complete Apple mobile UI cases

- [ ] UTN-1.2 Complete Apple mobile UI cases.

Purpose: Complete Apple mobile UI cases so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/native/apple-mobile/`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTN-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: UIKit/SwiftUI controls satisfy theme/Dynamic Type/keyboard inset, focus, native menu and VoiceOver observation requirements on declared supported profiles.

Implementation:

- [ ] UTN-1.2-I1 Author only missing UI assertions and observation recipes; consume existing native input/composition results.
- [ ] UTN-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTN-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UTN-1.2`: Run deterministic UI cases and collect exact roadmap43 mobile UI observations; absent observations remain unchecked. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTN-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTN-1.3 — Complete AppKit and SwiftUI desktop UI cases

- [ ] UTN-1.3 Complete AppKit and SwiftUI desktop UI cases.

Purpose: Complete AppKit and SwiftUI desktop UI cases so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/native/macos/`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTN-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Toolbar/menu validation, keyboard/focus, window isolation, appearance and VoiceOver UI observations pass for the current AppKit host/profile.

Implementation:

- [ ] UTN-1.3-I1 Add uncovered menu/popover/window UI cases; reuse existing command/history and persistence evidence.
- [ ] UTN-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTN-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UTN-1.3`: Run the affected AppKit UI selector and consume roadmap43 macOS observations. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTN-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTN-1.4 — Complete Android Views and Compose UI cases

- [ ] UTN-1.4 Complete Android Views and Compose UI cases.

Purpose: Complete Android Views and Compose UI cases so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/native/android/`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTN-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Views/Compose theme, recomposition, large text, RTL, keyboard insets and TalkBack/control focus cases qualify separately; no composition bug is masked by a JS-only transcript.

Implementation:

- [ ] UTN-1.4-I1 Add missing Android control assertions and per-toolkit observation requests over the same host.
- [ ] UTN-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTN-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UTN-1.4`: Run bounded Android UI selectors and consume the exact roadmap43 Views/Compose observations. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTN-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTN-1.5 — Complete WinUI and WPF UI cases

- [ ] UTN-1.5 Complete WinUI and WPF UI cases.

Purpose: Complete WinUI and WPF UI cases so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/native/windows/`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTN-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Each declared Windows host satisfies UI Automation labels/state, high contrast/scaling, keyboard/flyout and theme behavior with correct owner window.

Implementation:

- [ ] UTN-1.5-I1 Add remaining Windows UI case definitions and check resource/command bindings; consume BDH/BNT host evidence.
- [ ] UTN-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTN-1.5-V1 Run `node scripts/ui-integration-delivery.mjs UTN-1.5`: Run targeted controls cases and consume roadmap43 Windows observations; unavailable OS evidence remains a blocker. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTN-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTN-1.6 — Complete GTK and libadwaita UI cases

- [ ] UTN-1.6 Complete GTK and libadwaita UI cases.

Purpose: Complete GTK and libadwaita UI cases so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/native/linux/`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTN-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: GTK-only and libadwaita profiles have correct dependencies, theme/scaling, focus/popover and AT-SPI observations; web desktop samples are qualified only as web hosts.

Implementation:

- [ ] UTN-1.6-I1 Add remaining Linux UI assertions and observation recipes; link Electron/Tauri UI receipt to web cases rather than duplicate semantic tests.
- [ ] UTN-1.6-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTN-1.6-V1 Run `node scripts/ui-integration-delivery.mjs UTN-1.6`: Run bounded GTK UI selectors and consume roadmap43 Linux observations and matching BNT desktop isolation receipts. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTN-1.6 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/27-final-native-ui-testing.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- BNT-1.3: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/81-host-final-cases.progress.md`.
- BNT-1.5: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/81-host-final-cases.progress.md`.
- BNT-1.6: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/81-host-final-cases.progress.md`.
- UPG-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/25-packages-and-guides.progress.md`.
- UPG-1.5: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/25-packages-and-guides.progress.md`.
