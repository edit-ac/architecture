# Implement reusable controls and suggestion state

Status: COMPLETE

## Goal and entry conditions

Goal: Implement reusable controls and suggestion state. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/editor-ui-integrations.md#shared-customization-apis); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/02-controls-state.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

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

## Epic UCS-1 — Implement reusable controls and suggestion state

### Task UCS-1.1 — Expose command snapshot selectors

- [x] UCS-1.1 Expose command snapshot selectors.

Purpose: Expose command snapshot selectors so applications can reuse this integration boundary.
Deliverable: `packages/web/src/ui/; packages/web/src/commands/; packages/web/package.json`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shared-customization-apis); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [UIC-1.2](00-contracts.md), [UIC-1.3](00-contracts.md), [UIC-1.4](00-contracts.md), [UIC-1.5](00-contracts.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: The controls export observes the owning editor, derives mixed/disabled/value state and notifies only changed selections; root/headless imports remain side-effect-free.

Implementation:

- [x] UCS-1.1-I1 Implement the UIC projection and selector subscription over current command state; dispose listeners without tearing down the shared editor.
- [x] UCS-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UCS-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UCS-1.1`: One prepared formatting/readonly transition updates the relevant selector while an unrelated selector retains identity. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UCS-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UCS-1.2 — Implement target sessions for external controls

- [x] UCS-1.2 Implement target sessions for external controls.

Purpose: Implement target sessions for external controls so applications can reuse this integration boundary.
Deliverable: `packages/web/src/ui/; packages/web/src/commands/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shared-customization-apis); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UCS-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: A control can retain an allowed target across toolbar/dialog focus, execute through existing guards and revoke it on close/disposal; stale targets never retarget another editor.

Implementation:

- [x] UCS-1.2-I1 Bridge existing capture/dispose and block-action preparation into one UI session; associate explicit overlay owners and avoid asynchronous focus restoration.
- [x] UCS-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UCS-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UCS-1.2`: Exercise capture, permitted overlay focus, disposal and stale activation on two deterministic editors. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UCS-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UCS-1.3 — Implement contribution layout resolution

- [x] UCS-1.3 Implement contribution layout resolution.

Purpose: Implement contribution layout resolution so applications can reuse this integration boundary.
Deliverable: `packages/web/src/ui/; packages/web/src/extensions/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shared-customization-apis); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UCS-1.1, UCS-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Host include/exclude/reorder/group settings combine predictably with registered extension controls; duplicate IDs are rejected and unavailable features do not load optional extensions.

Implementation:

- [x] UCS-1.3-I1 Resolve descriptor/layout inputs into immutable surface models; route activation to registered semantics and localize labels/icons without altering IDs.
- [x] UCS-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UCS-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UCS-1.3`: Resolve one toolbar/slash/block-menu contribution fixture and a duplicate-ID fixture; inspect unloaded-extension requests. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UCS-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UCS-1.4 — Implement bounded suggestions controller

- [x] UCS-1.4 Implement bounded suggestions controller.

Purpose: Implement bounded suggestions controller so applications can reuse this integration boundary.
Deliverable: `packages/web/src/ui/; packages/web/src/host/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shared-customization-apis); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UCS-1.2, UCS-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Queries have stable targets, bounded result counts, explicit loading/empty/error states and cancellation; stale/out-of-order completion cannot apply or steal focus.

Implementation:

- [x] UCS-1.4-I1 Implement query generation/cancel/activation state using prepared host-service results; keep command choices distinct from reference options.
- [x] UCS-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UCS-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UCS-1.4`: Run one out-of-order and one canceled prepared query, then activate one still-valid reference through the owning target. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UCS-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UCS-1.5 — Implement overlay and focus ownership service

- [x] UCS-1.5 Implement overlay and focus ownership service.

Purpose: Implement overlay and focus ownership service so applications can reuse this integration boundary.
Deliverable: `packages/web/src/ui/; packages/web/src/input/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shared-customization-apis); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UCS-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Overlay theme/direction/locale and permitted focus owner follow the initiating editor; mounting in a host dialog does not escape its focus boundary or open another editor keyboard.

Implementation:

- [x] UCS-1.5-I1 Expose container/position/focus lifecycle hooks using existing browser ownership facilities; leave widget keyboard management to the selected presenter.
- [x] UCS-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UCS-1.5-V1 Run `node scripts/ui-integration-delivery.mjs UCS-1.5`: Use one nested-dialog fixture with two editors and close/reopen; inspect disposal and correct target/focus ownership. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UCS-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UCS-1.6 — Export the current controls contract

- [x] UCS-1.6 Export the current controls contract.

Purpose: Export the current controls contract so applications can reuse this integration boundary.
Deliverable: `packages/web/package.json; packages/web/src/index.ts; packages/web/src/ui/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shared-customization-apis); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UCS-1.1, UCS-1.2, UCS-1.3, UCS-1.4, UCS-1.5.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Public controls exports and declarations cover the agreed API without duplicate aliases, framework runtime dependencies or automatic CSS; one existing installed-consumer fixture resolves them.

Implementation:

- [x] UCS-1.6-I1 Wire explicit export paths and document the UI/semantic ownership boundary; record API receipt for framework/native consumers.
- [x] UCS-1.6-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UCS-1.6-V1 Run `node scripts/ui-integration-delivery.mjs UCS-1.6`: Pack/install only the changed package into one existing isolated plain consumer and run its imports/types check. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UCS-1.6 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/02-controls-state.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- UIC-1.2: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/00-contracts.progress.md`.
- UIC-1.3: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/00-contracts.progress.md`.
- UIC-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/00-contracts.progress.md`.
- UIC-1.5: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/00-contracts.progress.md`.
