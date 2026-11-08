# Table controls and presentation

Status: accepted interaction direction from the 2026-11-08 table research request; feature delivery and qualification remain pending. [Research](../rea/notion-tables.md), [rich table semantics](rich-content-extensions.md#table-editing-layout-and-source-formatting), [direct cell editing](table-paste-and-editing.md) and [UI integration ownership](editor-ui-integrations.md) remain linked authorities. This contract adds control requirements without claiming new engine support.

## Targets and control ownership

Expose four scopes: table, row, column and cell/rectangle. Keep the captured target visible while its controls are open; native text selection and IME retain their own input ownership. Idle presentation is one coherent document grid. Controls occupy stable edge/overlay space, without reflowing neighboring content, repeating one button per cell in the default idle UI, or competing with a second active formatting toolbar. Accessibility equivalents remain discoverable.

Use the existing guarded target/contribution/menu lifecycle and one semantic command/history/replica owner. Click, keyboard and touch expose equivalent supported actions. Menus have precise localized scope labels, correct on/off/mixed/disabled states, directional navigation, Escape/cancel and focus return to a surviving owner. Scrolling, resize, zoom, RTL, two editor roots and portaled host themes retain placement and scope. Remote removal, protection/revocation, readonly, host switch and teardown close or reject stale actions without repair writes.

Row/column menus expose insert before/after, duplicate, move and distinct Clear contents versus structural Delete. Provide non-drag movement as well as direct manipulation, with insertion/drop cues, autoscroll and cancellation that do not steal cell selection or page scrolling. Define last-axis behavior, header/width movement and post-command focus. Accepted shape/content changes use one intentional undo group; target selection and canceled gestures have no semantic/history effects.

Aggregate Header row/column actions consume existing header semantics and report mixed states. First-row headers associate with columns; first-column headers associate with rows, including an explicit top-left/intersection policy. A blanket scope=col for every header cell does not satisfy this outcome. Supported marks/alignment retain scoped formatting; content copies exclude control chrome.

## Geometry and capability decisions

Provide automatic content sizing, Fit to container, Distribute columns and explicit bounded column widths as distinct supported operations. Preserve authored widths through admitted structural edits, history, save/reopen and interchange, with a declared fallback where a format cannot express them. RCH-1.34 must settle typed column-width ownership, units/bounds, shared versus host-local presentation, conflict behavior and format loss before implementation. Generic namespaced metadata acceptance is not a portable width API. Do not add a second state store/replica or numbered production format.

Resize has a visible guide, cursor, cancel/recovery and keyboard alternative. Separate its hit region from the small painted grip. Long/interrupted/repeated drags remain usable without reload; no selection/scroll/block-drag conflict, intermediate history flood or unexpected commit on cancel. Bounded horizontal overflow belongs to the table, with controls/menus reachable at viewport edges and zoom. Adjacent add affordances have keyboard/menu equivalents. Do not make destructive corner shrinking an implicit gesture over populated cells.

Hover, keyboard focus and touch each reveal a usable context entry. Touch targets should be generous independently of their visual mark; no capability may require hover, precision dragging or a long press alone. Menus/popovers respect the viewport and do not hide the active target. Preserve existing content/chrome tokens and host themes; provide readable active/text/rectangle selection in light, dark and forced colors.

Cell/axis text/background color and merged-cell support require the explicit RCH-1.35 capability disposition. Current merges remain unsupported with recoverable, nonmutating rejection. A future supported merge must have an approved content-preservation, identity/anchor, history, concurrency and codec contract before a presenter. Notion's documented clearing of non-anchor content is not adopted. Do not store arbitrary CSS, claim a formatting color from generic metadata, automatically convert documents or expose database properties/views/formulas.

## Delivery and acceptance

RCH-1.6/1.7/1.8/1.23 retain shape/header/selection/format semantics; RCH-1.34/1.35 own the new width contract and capability decisions. UDM-1.10/1.11/1.12 deliver menus, geometry and axis manipulation respectively, preserving completed UDM-1.8 direct cells and UDM-1.9 paste. The actual default, optional adapters and host override maps must identify the same semantic and presentation owner; no framework-owned editable descendants.

[NTC-01–16](../tests/notion-table-cases.md) are final acceptance inputs to UTW-1.2, with compatible semantic evidence reused. During delivery run only the affected mounted selector and changed semantic selectors. Final OS/device/browser/IME/AT proof remains roadmap43 and existing UI/native owners; unavailable native profiles do not block independent web feature delivery. Source checks, screenshots alone and prepared observations are not runtime support qualification. No active runner, source snapshot, progress state, provider or deployment is changed by this plan.
