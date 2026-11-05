# Integrate Base UI controls

Status: COMPLETE

## Goal and entry conditions

Goal: Integrate Base UI controls. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/editor-ui-integrations.md#framework-and-component-library-coverage); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/07-base-ui.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

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

## Epic UBU-1 — Integrate Base UI controls

### Task UBU-1.1 — Create optional Base UI package and control adapter

- [x] UBU-1.1 Create optional Base UI package and control adapter.

Purpose: Create optional Base UI package and control adapter so applications can reuse this integration boundary.
Deliverable: `packages/react-base-ui/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#framework-and-component-library-coverage); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [UCS-1.6](02-controls-state.md), [UIS-1.4](01-default-styles.md), [URC-1.4](04-react-ui.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: The package has only its framework and selected primitive peers, side-effect-free exports and one command-state adapter; importing another library is unnecessary.

Implementation:

- [x] UBU-1.1-I1 Reconcile pinned maintained primitives and the complete surface matrix; implement the descriptor-to-widget boundary using render composition and toolbar navigation; compose triggers using the upstream render API.
- [x] UBU-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UBU-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UBU-1.1`: Compile a single installed peer consumer and assert a disabled/pressed state mapping with no editor initialization at import. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UBU-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UBU-1.2 — Implement Base UI formatting toolbar

- [x] UBU-1.2 Implement Base UI formatting toolbar.

Purpose: Implement Base UI formatting toolbar so applications can reuse this integration boundary.
Deliverable: `packages/react-base-ui/src/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#framework-and-component-library-coverage); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UBU-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Toolbar/button/toggle/group/separator and block selector follow the library keyboard model; each activation reaches the existing guarded command exactly once.

Implementation:

- [x] UBU-1.2-I1 Connect toolbar parts, accessible names and mixed/value states; use upstream composition for tooltips/select triggers and retain host-render customization.
- [x] UBU-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UBU-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UBU-1.2`: Run one upstream-compatible keyboard/press smoke over bold and block selector; inspect no nested focus managers. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UBU-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UBU-1.3 — Implement Base UI menus and parameter overlays

- [x] UBU-1.3 Implement Base UI menus and parameter overlays.

Purpose: Implement Base UI menus and parameter overlays so applications can reuse this integration boundary.
Deliverable: `packages/react-base-ui/src/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#framework-and-component-library-coverage); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UBU-1.1, UBU-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Block menu, link dialog and selection-toolbar overlays retain target, theme and focus owner inside a host modal; cancel/reopen does not leak captures.

Implementation:

- [x] UBU-1.3-I1 Map existing overlay/session hooks into library portal/dialog/menu primitives; wire error/pending/status presentation without persistence logic.
- [x] UBU-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UBU-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UBU-1.3`: Use one two-editor/modal fixture with cancel, stale-target rejection and dialog reopen. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UBU-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UBU-1.4 — Implement Base UI command and reference pickers

- [x] UBU-1.4 Implement Base UI command and reference pickers.

Purpose: Implement Base UI command and reference pickers so applications can reuse this integration boundary.
Deliverable: `packages/react-base-ui/src/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#framework-and-component-library-coverage); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UBU-1.1, UBU-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Separate command-menu and reference-option patterns cover query/loading/empty/error/disabled states and stable activation. Interactive reference-row children require a suitable grid/dialog pattern, not a listbox option.

Implementation:

- [x] UBU-1.4-I1 Bind UCS suggestions to the selected library collections/combobox/menu facilities; document own-search versus inline-editor focus support and prevent duplicated keyboard handlers.
- [x] UBU-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UBU-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UBU-1.4`: Replay prepared out-of-order results and one valid command/reference activation; verify active option/command and cancellation. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UBU-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UBU-1.5 — Finish Base UI surface coverage and consumer

- [x] UBU-1.5 Finish Base UI surface coverage and consumer.

Purpose: Finish Base UI surface coverage and consumer so applications can reuse this integration boundary.
Deliverable: `packages/react-base-ui/; examples/ui/react-base-ui/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#framework-and-component-library-coverage); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UBU-1.2, UBU-1.3, UBU-1.4.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: All required toolbar/selection/block-menu/slash/reference/link/status surfaces are listed as implemented or explicit blockers; typed slots permit host styling and no unsupported feature is silently enabled.

Implementation:

- [x] UBU-1.5-I1 Complete token mapping, public exports, notices and one composed example; record precise peer and surface receipt for registry consumers.
- [x] UBU-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UBU-1.5-V1 Run `node scripts/ui-integration-delivery.mjs UBU-1.5`: Pack/install one representative example, compile and inspect selected themed states; comprehensive keyboard/AT coverage remains final-owned. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UBU-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/07-base-ui.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- UCS-1.6: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/02-controls-state.progress.md`.
- UIS-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/01-default-styles.progress.md`.
- URC-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/04-react-ui.progress.md`.
