# Deliver GTK and desktop web UI composition

Status: IN_PROGRESS

## Goal and entry conditions

Goal: Deliver GTK and desktop web UI composition. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/20-linux-desktop-ui.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

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

## Epic ULX-1 — Deliver GTK and desktop web UI composition

### Task ULX-1.1 — Add GTK action and theme controls

- [ ] ULX-1.1 Add GTK action and theme controls.

Purpose: Add GTK action and theme controls so applications can reuse this integration boundary.
Deliverable: `native/linux/; adapters/native/linux/`.
Context: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BDH-1.4](../dependency-closed-ui-20261025/26-gtk-binding.md), [UNC-1.4](15-native-ui-contracts.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: GTK controls use existing host actions/state and theme settings; optional libadwaita is not required for a plain GTK consumer.

Implementation:

- [ ] ULX-1.1-I1 Expose action-enabled/state mapping and GTK toolbar/menu parts with UI-thread observer cleanup.
- [ ] ULX-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] ULX-1.1-V1 Run `node scripts/ui-integration-delivery.mjs ULX-1.1`: Compile one GTK host consumer and inspect prepared action/theme states. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave ULX-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task ULX-1.2 — Add GTK popovers, suggestions and status

- [ ] ULX-1.2 Add GTK popovers, suggestions and status.

Purpose: Add GTK popovers, suggestions and status so applications can reuse this integration boundary.
Deliverable: `native/linux/; adapters/native/linux/`.
Context: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: ULX-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Popover/result/status parts preserve owner window, focus and captured target; direction/scaling and accessible labels/states follow GTK.

Implementation:

- [ ] ULX-1.2-I1 Compose result/link views and query cancellation over existing target/service hooks.
- [ ] ULX-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] ULX-1.2-V1 Run `node scripts/ui-integration-delivery.mjs ULX-1.2`: Replay one canceled result and menu action with the existing GTK host fixture. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave ULX-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task ULX-1.3 — Add optional libadwaita composition

- [ ] ULX-1.3 Add optional libadwaita composition.

Purpose: Add optional libadwaita composition so applications can reuse this integration boundary.
Deliverable: `native/linux/; examples/ui/gtk/`.
Context: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: ULX-1.1, ULX-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: A libadwaita toolbar/header recipe themes existing GTK controls while GTK-only imports remain free of that dependency.

Implementation:

- [ ] ULX-1.3-I1 Add optional composition/module and example for adaptive toolbar layout without making page chrome part of the engine.
- [ ] ULX-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] ULX-1.3-V1 Run `node scripts/ui-integration-delivery.mjs ULX-1.3`: Compile the selected GTK-only and libadwaita entry points; inspect their dependency separation. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave ULX-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task ULX-1.4 — Wire Electron and Tauri UI recipes

- [ ] ULX-1.4 Wire Electron and Tauri UI recipes.

Purpose: Wire Electron and Tauri UI recipes so applications can reuse this integration boundary.
Deliverable: `examples/sdk-adapters/electron/; examples/sdk-adapters/tauri/`.
Context: [named contract section](../../specs/native-ui-integrations.md#native-design-system-mapping); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BDH-1.6](../dependency-closed-ui-20261025/27-desktop-shell-bindings.md), [BDH-1.7](../dependency-closed-ui-20261025/27-desktop-shell-bindings.md), [UDM-1.7](03-default-dom-controls.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Existing desktop web hosts consume default or chosen framework UI packages, preserve IPC/security constraints and use actual persistence status; no new desktop engine or transport.

Implementation:

- [ ] ULX-1.4-I1 Add small toolbar/theme/overlay compositions inside current renderer entries and document host container ownership.
- [ ] ULX-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] ULX-1.4-V1 Run `node scripts/ui-integration-delivery.mjs ULX-1.4`: Build each changed renderer entry and reuse existing BDH process-boundary evidence; one prepared UI command/status smoke each. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave ULX-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/20-linux-desktop-ui.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- BDH-1.4: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/26-gtk-binding.progress.md`.
- BDH-1.6: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/27-desktop-shell-bindings.progress.md`.
- BDH-1.7: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/27-desktop-shell-bindings.progress.md`.
- UDM-1.7: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/03-default-dom-controls.progress.md`.
- UNC-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/15-native-ui-contracts.progress.md`.
