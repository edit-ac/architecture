# Deliver accessible default DOM controls

Status: COMPLETE

## Goal and entry conditions

Goal: Deliver accessible default DOM controls. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/editor-ui-integrations.md#default-product-surface); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/03-default-dom-controls.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

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

## Epic UDM-1 — Deliver accessible default DOM controls

### Task UDM-1.1 — Build the toolbar navigation primitive

- [x] UDM-1.1 Build the toolbar navigation primitive.

Purpose: Build the toolbar navigation primitive so applications can reuse this integration boundary.
Deliverable: `packages/web/src/ui/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#default-product-surface); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [UCS-1.6](02-controls-state.md), [UIS-1.4](01-default-styles.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Default toolbar has named groups, one roving tab stop, orientation/RTL navigation and defined focus behavior when an item disables or disappears; native input keys are not captured globally.

Implementation:

- [x] UDM-1.1-I1 Implement scoped toolbar focus management and the button/group/separator parts over UCS state; retain 44px touch hit areas.
- [x] UDM-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UDM-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UDM-1.1`: Use one deterministic keyboard fixture for arrows, Home/End, disable/remove and RTL; inspect actual focus target. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UDM-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UDM-1.2 — Compose the default formatting toolbar

- [x] UDM-1.2 Compose the default formatting toolbar.

Purpose: Compose the default formatting toolbar so applications can reuse this integration boundary.
Deliverable: `packages/web/src/ui/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#default-product-surface); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UDM-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Configured formatting/history/block-type controls show accurate active/mixed/disabled states and use one semantic activation per gesture; layout can be reordered/replaced by host slots.

Implementation:

- [x] UDM-1.2-I1 Connect the agreed default layout to existing commands and block-action capability; add shortcut labels and icon accessibility names.
- [x] UDM-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UDM-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UDM-1.2`: Activate bold, undo and one admitted block type from pointer and keyboard in the same prepared document. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UDM-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UDM-1.3 — Add menus and link dialog parts

- [x] UDM-1.3 Add menus and link dialog parts.

Purpose: Add menus and link dialog parts so applications can reuse this integration boundary.
Deliverable: `packages/web/src/ui/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#default-product-surface); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UDM-1.1, UDM-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Menu actions and parameter dialogs retain guarded targets, validate values, announce errors, cancel cleanly and restore focus only to the valid owner.

Implementation:

- [x] UDM-1.3-I1 Build default menu/dialog parts and connect existing link and block-action flows; unsupported conversions remain explicitly unavailable.
- [x] UDM-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UDM-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UDM-1.3`: Open/edit/cancel one link dialog and activate one block menu action with a stale-target rejection. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UDM-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UDM-1.4 — Add selection toolbar placement

- [x] UDM-1.4 Add selection toolbar placement.

Purpose: Add selection toolbar placement so applications can reuse this integration boundary.
Deliverable: `packages/web/src/ui/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#default-product-surface); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UDM-1.1, UDM-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Optional floating controls follow the captured selection through scroll/resize/zoom, avoid viewport clipping and remain keyboard reachable without overriding native selection/composition.

Implementation:

- [x] UDM-1.4-I1 Mount the selection-toolbar presenter using UCS overlay hooks; add keyboard entry/exit and explicit host disable option.
- [x] UDM-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UDM-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UDM-1.4`: Inspect one multiline selection at a scrolled viewport edge and keyboard entry/Escape; no document mutation on placement. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UDM-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UDM-1.5 — Add slash and reference result presenters

- [x] UDM-1.5 Add slash and reference result presenters.

Purpose: Add slash and reference result presenters so applications can reuse this integration boundary.
Deliverable: `packages/web/src/ui/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#default-product-surface); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UDM-1.1, UDM-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Command actions use menu semantics; reference options use listbox semantics with noninteractive option children. Own-search palette and inline editor-focus profiles are distinct and preserve composition.

Implementation:

- [x] UDM-1.5-I1 Implement renderers for UCS suggestions with query status and virtual-active state; use a qualified inline ownership pattern or keep that profile explicitly unqualified.
- [x] UDM-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UDM-1.5-V1 Run `node scripts/ui-integration-delivery.mjs UDM-1.5`: Run one prepared slash command and one reference selection, cancellation and IME-suppressed query fixture. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UDM-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UDM-1.6 — Add status and async action presentation

- [x] UDM-1.6 Add status and async action presentation.

Purpose: Add status and async action presentation so applications can reuse this integration boundary.
Deliverable: `packages/web/src/ui/; packages/web/src/host/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#default-product-surface); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BTS-1.8](../dependency-closed-ui-20261025/12-node-browser-orchestration.md).
Dependencies: UDM-1.2, UDM-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Local/saving/durably-saved/offline/conflict/recovery states come from the existing owner; upload/paste progress and cancel actions never imply durability or execute hidden provider requests.

Implementation:

- [x] UDM-1.6-I1 Compose existing status and host-service progress into default parts; expose error/retry callbacks without own retry/receipt algorithm.
- [x] UDM-1.6-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UDM-1.6-V1 Run `node scripts/ui-integration-delivery.mjs UDM-1.6`: Replay one prepared save-failure/recovery and one canceled action transcript; inspect announced states. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UDM-1.6 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UDM-1.7 — Expose document and compact UI presets

- [x] UDM-1.7 Expose document and compact UI presets.

Purpose: Expose document and compact UI presets so applications can reuse this integration boundary.
Deliverable: `packages/web/src/ui/; packages/web/package.json; examples/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#default-product-surface); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UDM-1.2, UDM-1.3, UDM-1.4, UDM-1.5, UDM-1.6.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Plain JS can mount/unmount default product UI with one import path and explicit CSS, or supply a custom layout; presets do not enable extensions or instantiate another editor.

Implementation:

- [x] UDM-1.7-I1 Compose the completed parts as optional factories; provide one small override example and teardown every UI-owned resource.
- [x] UDM-1.7-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UDM-1.7-V1 Run `node scripts/ui-integration-delivery.mjs UDM-1.7`: Mount document/compact presets on two existing editors and unmount one; verify the other editor remains usable. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UDM-1.7 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UDM-1.8 — Render and edit table cells directly

- [x] UDM-1.8 Render and edit table cells directly.

Purpose: Deliver the user's proper-table-paste correction through the existing table engine and presenter.
Deliverable: `packages/web/src/modules/tables/current.ts; existing cell input/selection helpers and product styles`.
Context: [table paste and direct editing](../../specs/table-paste-and-editing.md); the actual named adapters and only their current semantic receipt.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UDM-1.7.
Independent work: A ready sibling remains eligible; native-platform absence does not block web delivery.
Session scope: One adapter boundary, 15–45 minutes including focused checks; split a concrete missing shared boundary before overrunning, preserving all acceptance.
Acceptance: The default table is a semantic grid with directly editable admitted cell content and no permanent per-cell textarea/input, duplicated preview or field chrome. Marked and admitted multi-block content stays visible/editable, with composition, directed selection, navigation and existing cell-history bookmarks preserved. An accessible active textbox role is allowed; a hidden or borderless replica per cell is not the product.

Implementation:

- [x] UDM-1.8-I1 Reuse current cell commands/identities and render/input/selection boundaries. Mount one coherent table with an in-place active editing host; preserve IME ownership and readonly behavior. Missing shared APIs return to their semantic owner. Do not add per-cell engines, history or persistence.

- [x] UDM-1.8-I2 Wire this cell adapter into the default table lifecycle and scoped CSS; register its focused selector and preserve teardown/readonly states.

Validation:

- [x] UDM-1.8-V1 Register/run `node scripts/ui-integration-delivery.mjs UDM-1.8`: one real mounted marked/multiline cell: inspect idle/editing DOM and computed layout, composition/caret sentinel and one undo/redo; reuse shared semantic proof. Final TPT matrix stays UTW-1.2. Budget: 1–3 minutes; nonzero cases, no required failures/skips. No new broad suites during functionality.

Evidence: The existing separate progress path above; exact source/runtime, inspected/executed/passed/failed/skipped counts, compatible reuse and limitations. Generated media/logs stay ignored.
Handoff: Exact next boundary, missing API owner or failing input; no product/support claim before final gate.
Blocked behavior: Keep unchecked with fingerprint, owner and changed-input resume condition; no unchanged retry or parallel implementation.

### Task UDM-1.9 — Paste real tables through the existing clipboard policy

- [x] UDM-1.9 Paste real tables through the existing clipboard policy.

Purpose: Deliver the user's proper-table-paste correction through the existing table engine and presenter.
Deliverable: `packages/web/src/modules/tables/clipboard.ts; existing document clipboard/import adapter and declared formats`.
Context: [table paste and direct editing](../../specs/table-paste-and-editing.md); the actual named adapters and only their current semantic receipt.
Entry receipts: Inherited through the listed local dependencies. Before retrying the stopped UDM-1.9 prerequisite, consume DTR-1.1's public current-format rich rectangle API and passing source/artifact-pinned proof from root `.roadmap-runner/table-rectangle-repair-20261025/00-addressed-rich-rectangle.progress.md`; authenticate the affected inputs and reuse compatible proof. A completed queue entry alone does not prove the operation. The original failed prerequisite observations remain in this source's ignored UDM-1.9 evidence; do not retry unchanged input or weaken any acceptance below.
Dependencies: UDM-1.8.
Independent work: A ready sibling remains eligible; native-platform absence does not block web delivery.
Session scope: One adapter boundary, 15–45 minutes including focused checks; split a concrete missing shared boundary before overrunning, preserving all acceptance.
Acceptance: Admitted internal/HTML tables and spreadsheet TSV under declared policy paste as actual editable tables/rectangles, retaining supported formatting, empty cells and surrounding content. Text-range versus rectangle targets, plain mode and unsupported/unsafe input have explicit nonmutating behavior. One accepted paste has one history boundary and usable caret; no accidental nesting/expansion or imported form fields.

Implementation:

- [x] UDM-1.9-I1 Connect current format codecs and captured targets to the direct table adapter. Preserve flavor precedence, recoverable limitations and one shared mutation authority. Scope source fixtures to safe synthetic document/spreadsheet HTML/TSV; return missing codec/API work to FMT/RCH/DRA rather than create another parser.

- [x] UDM-1.9-I2 Wire copy/paste and literal mode to captured semantic targets; register the focused clipboard selector without importing another parser.

Validation:

- [x] UDM-1.9-V1 Register/run `node scripts/ui-integration-delivery.mjs UDM-1.9`: one prepared marked HTML-table paste and one bounded rectangular/literal TSV or rejection path through the real mounted adapter; assert nodes/marks, selection, one commit and undo/reopen. Full TPT-01–08 coverage stays UTW-1.2. Budget: 1–3 minutes; nonzero cases, no required failures/skips. No new broad suites during functionality.

Evidence: The existing separate progress path above; exact source/runtime, inspected/executed/passed/failed/skipped counts, compatible reuse and limitations. Generated media/logs stay ignored.
Handoff: Exact next boundary, missing API owner or failing input; no product/support claim before final gate.
Blocked behavior: Keep unchecked with fingerprint, owner and changed-input resume condition; no unchanged retry or parallel implementation.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/03-default-dom-controls.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- BTS-1.8: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/12-node-browser-orchestration.progress.md`.
- UCS-1.6: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/02-controls-state.progress.md`.
- UIS-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/01-default-styles.progress.md`.
