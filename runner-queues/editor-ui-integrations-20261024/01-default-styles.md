# Style current product surfaces

Status: COMPLETE

## Goal and entry conditions

Goal: Style current product surfaces. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/editor-ui-integrations.md#styling-contract-outside-inside-and-overlays); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/01-default-styles.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

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

## Epic UIS-1 — Style current product surfaces

### Task UIS-1.1 — Replace label-dependent styling hooks

- [x] UIS-1.1 Replace label-dependent styling hooks.

Purpose: Replace label-dependent styling hooks so applications can reuse this integration boundary.
Deliverable: `packages/web/src/ui/commands.ts; packages/web/styles/editor.css`.
Context: [named contract section](../../specs/editor-ui-integrations.md#styling-contract-outside-inside-and-overlays); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [UIC-1.1](00-contracts.md), [UIC-1.4](00-contracts.md), [UIC-1.5](00-contracts.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Current controls have stable data-part/state hooks and no CSS selector depends on an English label or sibling placement. Existing interaction logic and captured targets remain intact.

Implementation:

- [x] UIS-1.1-I1 Add the agreed hooks to existing DOM output; remove semantic-label/sibling selectors and move structural inline styles into scoped classes.
- [x] UIS-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UIS-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UIS-1.1`: Render one existing command group in two DOM positions and a translated-label variant; inspect computed styles and execute one existing command. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIS-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UIS-1.2 — Add default chrome tokens and states

- [x] UIS-1.2 Add default chrome tokens and states.

Purpose: Add default chrome tokens and states so applications can reuse this integration boundary.
Deliverable: `packages/web/styles/; packages/web/package.json`.
Context: [named contract section](../../specs/editor-ui-integrations.md#styling-contract-outside-inside-and-overlays); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UIS-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Optional chrome CSS covers buttons, groups, separators, inputs and status with hover/focus/pressed/mixed/disabled/pending/error states; headless entry imports no decorative CSS.

Implementation:

- [x] UIS-1.2-I1 Implement scoped low-specificity rules, light/dark defaults and export/CSS side-effect metadata; keep fonts and global reset application-owned.
- [x] UIS-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UIS-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UIS-1.2`: Build one plain browser consumer with and without the CSS entry; inspect selected state styles and confirm no framework imports. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIS-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UIS-1.3 — Separate content typography from chrome density

- [x] UIS-1.3 Separate content typography from chrome density.

Purpose: Separate content typography from chrome density so applications can reuse this integration boundary.
Deliverable: `packages/web/styles/editor.css; packages/web/styles/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#styling-contract-outside-inside-and-overlays); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UIS-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Changing toolbar density does not alter content semantics or typography; heading/list/code/table/media/link presentation is covered and unknown content remains visible.

Implementation:

- [x] UIS-1.3-I1 Bind existing content rules to documented tokens and add compact/document chrome presets without touching serialized marks.
- [x] UIS-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UIS-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UIS-1.3`: Compare one deterministic mixed-content document before/after theme/density changes; exact checkpoint bytes remain unchanged. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIS-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UIS-1.4 — Style overlays and extension surfaces

- [x] UIS-1.4 Style overlays and extension surfaces.

Purpose: Style overlays and extension surfaces so applications can reuse this integration boundary.
Deliverable: `packages/web/src/modules/; packages/web/src/ui/; packages/web/styles/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#styling-contract-outside-inside-and-overlays); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UIS-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Every currently implemented inventoried panel, tooltip, result row, link/asset state and cancellation control uses the scoped product tokens; unsupported features remain absent/disabled. Scoped table border/padding/wrapping and selected/readonly/empty tokens support [direct cell editing](../../specs/table-paste-and-editing.md). UDM-1.8 consumes these hooks; UTW-1.2 qualifies the resulting product. This style-only parent can close on tokens/hooks before the later direct-cell adapter implementation.

Implementation:

- [x] UIS-1.4-I1 Apply part hooks/theme inheritance to current presenters and overlay containers; map loading/empty/error/progress states from existing owners.
- [x] UIS-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UIS-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UIS-1.4`: Inspect one current overlay and one current extension presenter using two independently themed editors; record any unsupported surface explicitly. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIS-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UIS-1.5 — Adopt styles in the development preview

- [x] UIS-1.5 Adopt styles in the development preview.

Purpose: Adopt styles in the development preview so applications can reuse this integration boundary.
Deliverable: `examples/; packages/web/src/ui/; ../docs/examples/recipes/toolbar.mjs`.
Context: [named contract section](../../specs/editor-ui-integrations.md#styling-contract-outside-inside-and-overlays); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UIS-1.1, UIS-1.2, UIS-1.3, UIS-1.4.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: The existing preview and toolbar recipe use the default product stylesheet/hooks and still exercise real commands; narrow layout, RTL and forced colors remain usable without global styles.

Implementation:

- [x] UIS-1.5-I1 Locate the existing preview owner, wire scoped imports and remove preview-only presentation duplication; retain documented CSS override example.
- [x] UIS-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UIS-1.5-V1 Run `node scripts/ui-integration-delivery.mjs UIS-1.5`: Open the current local preview with deterministic content, check toolbar/status at narrow and wide sizes, and reuse focused existing command evidence. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIS-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/01-default-styles.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- UIC-1.1: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/00-contracts.progress.md`.
- UIC-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/00-contracts.progress.md`.
- UIC-1.5: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/00-contracts.progress.md`.
