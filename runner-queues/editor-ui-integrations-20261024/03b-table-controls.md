# Refine contextual table controls

Status: PLANNED

## Goal and entry conditions

Deliver the 2026-11-08 [table-control contract](../../specs/table-controls.md) through the existing default presenter. This is a follow-up to completed direct-cell work, not a reopened UDM-1.8/1.9 or an active queue/snapshot edit. Core-relative implementation paths below are current source owners or explicitly planned modules.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/03b-table-controls.progress.md` (architecture-relative, ignored). RCH-1.34's separate semantic receipt destination is planned only; no run is configured or started here.

Use one current format, Rust/Yrs command/history owner and guarded target lifecycle. No providers, .secrets, paid inference, deployment or publication from these workers. Preserve host themes and temporary input/IME ownership. Each parent uses one changed mounted delivery case; compatible semantic passes carry forward. Comprehensive NTC/TPT authoring and packed visual/AT/device matrices remain UTW-1.2/1.9 and roadmap43 after functionality. Missing semantic receipt blocks only its dependent parent, not independent web controls. This source does not alter the active coordinator, queue or runner progress.

## Epic UDM-1 — Refine table controls after direct cell delivery

### Task UDM-1.10 — Add contextual table, axis and cell menus

- [ ] UDM-1.10 Add contextual table, axis and cell menus.

Purpose: Deliver this named table presentation boundary over existing semantics.
Deliverable: packages/web/src/modules/tables/current.ts; planned scoped table controls module; existing guarded menu/target parts.
Context: [table controls](../../specs/table-controls.md); [NTC cases](../../tests/notion-table-cases.md); actual named public exports/current receipt only.
Entry receipts: [UDM-1.3](03-default-dom-controls.md), [UDM-1.8](03-default-dom-controls.md).
Dependencies: none.
Independent work: Ready siblings remain eligible; missing native/platform support does not block independent browser delivery.
Session scope: One presenter boundary, 15–45 minutes including its focused check; split oversized semantic work to its named owner before implementation.
Acceptance: NTC-01/02/03/06/10/12: compact table/row/column/cell menus retain exact targets and accurate aggregate header states; visible selection, keyboard/touch entry, Escape and valid focus return work without document reflow, per-cell idle button lists or competing toolbars. Row/column header associations are correct; unsupported color/span actions remain honest.

Implementation:

- [ ] UDM-1.10-I1 Compose scoped action groups over the current command/selection lifecycle, add aggregate header presenters using the semantic owner, and replace default long/per-cell control presentation while preserving accessible equivalents.
- [ ] UDM-1.10-I2 Wire the existing default control/slot/part and host-theme lifecycle with teardown, readonly and protected-target handling; expose the same capabilities to optional adapters without framework-owned editable descendants.

Validation:

- [ ] UDM-1.10-V1 Register/run node scripts/ui-integration-delivery.mjs UDM-1.10: One real mounted row/column menu plus keyboard cancel/focus-return and header state; inspect geometry and confirm unchanged content/history on cancel. Budget 1–3 minutes; nonzero executed/passed/failed/skipped counts, no required failures/skips. Reuse compatible semantic evidence; do not author/run the final matrix here.

Evidence: Separate progress above; exact source/interface/fixture/runtime and counts, inspected visuals, reused receipts and explicit unverified cases. No screenshots/generated diagnostics in Git.
Handoff: Record the last substep/symbol, missing semantic receipt or failing input, and next bounded action.
Blocked behavior: Keep unchecked with owner/fingerprint and changed-input resume condition; no unchanged retry, runner mutation, alternate replica or DOM-only semantic workaround.

### Task UDM-1.11 — Add guarded table sizing controls

- [ ] UDM-1.11 Add guarded table sizing controls.

Purpose: Deliver this named table presentation boundary over existing semantics.
Deliverable: packages/web/src/modules/tables/current.ts; planned scoped table geometry presenter; existing part/theme styles.
Context: [table controls](../../specs/table-controls.md); [NTC cases](../../tests/notion-table-cases.md); actual named public exports/current receipt only.
Entry receipts: [UDM-1.8](03-default-dom-controls.md), [RCH-1.34](../../roadmaps/25-rich-content-extensions.md).
Dependencies: UDM-1.10.
Independent work: Ready siblings remain eligible; missing native/platform support does not block independent browser delivery.
Session scope: One presenter boundary, 15–45 minutes including its focused check; split oversized semantic work to its named owner before implementation.
Acceptance: NTC-07/08/11: divider resize, bounded keyboard adjustment, distinct fit/distribute actions, guide/cancel and repeated/interrupted gestures preserve the RCH-1.34 ownership policy, content and undo. Only the table scrolls; controls stay aligned/reachable through viewport edges, RTL, scroll and zoom. No implicit destructive corner trim.

Implementation:

- [ ] UDM-1.11-I1 Consume the exact RCH-1.34 capabilities; separate transient drag preview from semantic commit and keyboard adjustment. Include independent usable hit regions and reliable release/cancel teardown.
- [ ] UDM-1.11-I2 Wire the existing default control/slot/part and host-theme lifecycle with teardown, readonly and protected-target handling; expose the same capabilities to optional adapters without framework-owned editable descendants.

Validation:

- [ ] UDM-1.11-V1 Register/run node scripts/ui-integration-delivery.mjs UDM-1.11: One real resize/cancel/repeat and keyboard/fit case; inspect alignment and table-local overflow, assert one accepted command/undo and no mutation on cancel. Budget 1–3 minutes; nonzero executed/passed/failed/skipped counts, no required failures/skips. Reuse compatible semantic evidence; do not author/run the final matrix here.

Evidence: Separate progress above; exact source/interface/fixture/runtime and counts, inspected visuals, reused receipts and explicit unverified cases. No screenshots/generated diagnostics in Git.
Handoff: Record the last substep/symbol, missing semantic receipt or failing input, and next bounded action.
Blocked behavior: Keep unchecked with owner/fingerprint and changed-input resume condition; no unchanged retry, runner mutation, alternate replica or DOM-only semantic workaround.

### Task UDM-1.12 — Add direct axis manipulation and insertion cues

- [ ] UDM-1.12 Add direct axis manipulation and insertion cues.

Purpose: Deliver this named table presentation boundary over existing semantics.
Deliverable: packages/web/src/modules/tables/current.ts; existing prepared table commands; planned axis presenter.
Context: [table controls](../../specs/table-controls.md); [NTC cases](../../tests/notion-table-cases.md); actual named public exports/current receipt only.
Entry receipts: [UDM-1.8](03-default-dom-controls.md).
Dependencies: UDM-1.10.
Independent work: Ready siblings remain eligible; missing native/platform support does not block independent browser delivery.
Session scope: One presenter boundary, 15–45 minutes including its focused check; split oversized semantic work to its named owner before implementation.
Acceptance: NTC-04/05/09/10/15: axis grips and adjacent add controls offer insert, duplicate, drag and non-drag move, clear and structural delete over the current RCH-1.6/1.8 semantics. Define last-axis focus, width/header movement, visible drop/insertion cues, autoscroll and cancel; selection, resize and scrolling do not compete. Missing semantic operations return to their existing owner rather than disappearing from acceptance.

Implementation:

- [ ] UDM-1.12-I1 Inspect the current moveAxis/shape/clear preparation and wire its guarded capabilities into the contextual shell. Preserve stable identities, one intentional history group and readonly/remote-removal rejection.
- [ ] UDM-1.12-I2 Wire the existing default control/slot/part and host-theme lifecycle with teardown, readonly and protected-target handling; expose the same capabilities to optional adapters without framework-owned editable descendants.

Validation:

- [ ] UDM-1.12-V1 Register/run node scripts/ui-integration-delivery.mjs UDM-1.12: One mounted move action with undo plus pointer cancel/remote-target invalidation; assert exact cell order/content and no cancel history. Record remaining touch/IME profiles for final qualification. Budget 1–3 minutes; nonzero executed/passed/failed/skipped counts, no required failures/skips. Reuse compatible semantic evidence; do not author/run the final matrix here.

Evidence: Separate progress above; exact source/interface/fixture/runtime and counts, inspected visuals, reused receipts and explicit unverified cases. No screenshots/generated diagnostics in Git.
Handoff: Record the last substep/symbol, missing semantic receipt or failing input, and next bounded action.
Blocked behavior: Keep unchecked with owner/fingerprint and changed-input resume condition; no unchanged retry, runner mutation, alternate replica or DOM-only semantic workaround.
