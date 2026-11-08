# Notion-inspired block acceptance catalog

- **Status:** Planned cases; zero executable recipes or passing runtime claims added by this document
- **Owner:** Existing track 38 and track 25 producers/final consumers
- **Last reviewed:** 2026-11-08
- **Related:** [Research](../rea/notion-block-editor.md), [interaction contract](../specs/editor-interactions.md), [rich-content contract](../specs/rich-content-extensions.md)

## Ownership and execution

These 40 descriptions are future acceptance inputs. They do not enter the shared suite as runnable recipes until their owner supplies real APIs/fixtures and registers the affected recipe. During development, use only the minimal meaningful changed case; comprehensive recipe development and coverage reconciliation stay with INT-1.14 for NBM/NBR-01–07 and RCH-1.20 for NBR-08 and the rich-content families. Those consumers reuse compatible producer receipts and add only missing/invalidated assertions. NAD entries are decision checks, not runtime support tests. All automated provider/network behavior uses prepared/mock transports; no live AI or credential loading.

| ID | Required observable outcome | Producer | Final consumer |
| --- | --- | --- | --- |
| NBM-01 | With caret in A, click B's handle: B's type/actions open and only B can change. | INT-1.19 | INT-1.14 |
| NBM-02 | An admitted conversion retains child text, attributes and checked state; one Undo restores the original. | INT-1.19 | INT-1.14 |
| NBM-03 | A click/tap opens the menu; an intentional thresholded drag moves; ordinary text selection/scroll does neither accidentally. | INT-1.19 | INT-1.14 |
| NBM-04 | Keyboard opening, submenu traversal and Escape/cancel retain a valid target and restore useful visible focus. | INT-1.19 | INT-1.14 |
| NBM-05 | Deleted, stale, denied and unregistered/inapplicable targets/actions cannot mutate a successor or unsupported kind. | INT-1.19 | INT-1.14 |
| NBR-01 | Canonical ordered block membership deduplicates selected descendants under a selected parent. | INT-1.20 | INT-1.14 |
| NBR-02 | Copies obtain fresh identities; moves retain identities, nested content and relative selection. | INT-1.20 | INT-1.14 |
| NBR-03 | Bulk delete/duplicate affect exactly the range and one Undo restores the complete accepted result. | INT-1.20 | INT-1.14 |
| NBR-04 | Preparation is bounded; intervening structural/revision/permission changes preserve accepted human edits or produce a located refusal, with no partial live update. | INT-1.20 | INT-1.14 |
| NBR-05 | Escape/Enter and Shift-arrow expose explicit text/single/range states with visible and announced scope. | INT-1.21 | INT-1.14 |
| NBR-06 | Two editors, nested controls, IME and table-cell selection retain correct focus and separate selection ownership. | INT-1.21 | INT-1.14 |
| NBR-07 | Keyboard and non-drag menu bulk commands use the same prepared range/move owner and reject self/descendant/incompatible destinations. | INT-1.21 | INT-1.14 |
| NBR-08 | The optional rich pointer-reorder profile moves the captured range/subtrees through the qualified range/move owners with cancellation and bounded drag geometry. | RCH-1.17 consumes INT-1.21 | RCH-1.20 |
| NTG-01 | A selected current-format representation defines title/children/heading rules and unsupported-input source preservation before admission. | RCH-1.24 | RCH-1.20 |
| NTG-02 | Nested checked-child conversion and Undo retain every authored child and its state. | RCH-1.24 | RCH-1.20 |
| NTG-03 | Move, remote edit and Markdown/export fallback preserve folded child identity/content. | RCH-1.24 | RCH-1.20 |
| NTG-04 | Disclosure state and keyboard/touch focus are accessible; close/open restores the same checked child. | RCH-1.25 | RCH-1.20 |
| NTG-05 | Search/navigation/selection/copy to folded content have explicit behavior; folding cannot silently delete or omit authored content. | RCH-1.25 | RCH-1.20 |
| NPA-01 | Text color, inline highlight and block background have distinct declared applicability without losing existing marks, links or children. | RCH-1.26 | RCH-1.20 |
| NPA-02 | Finite tokens, default/clear, inheritance, themes/contrast and interchange/fallback behave as the accepted contract states. | RCH-1.26 | RCH-1.20 |
| NPA-03 | Palette cancel/stale target preserves source; successful apply/clear is one Undo group. | RCH-1.26 | RCH-1.20 |
| NCO-01 | Two-column conversion/Undo preserve every child and its identity; tables remain distinct. | RCH-1.27 | RCH-1.20 |
| NCO-02 | Child/nesting/count/width bounds, cycle rejection, reading/export order and unsupported-input preservation are explicit. | RCH-1.27 | RCH-1.20 |
| NCO-03 | Resize/drag previews are derived; final width/move commits once and keyboard alternatives work. | RCH-1.28 | RCH-1.20 |
| NCO-04 | Narrow and actual selected mobile modes retain usable reading/focus order; a desktop resize is not phone qualification. | RCH-1.28 | RCH-1.20 |
| NOU-01 | Empty/duplicate/nested headings generate understandable hierarchy and the correct target. | RCH-1.29 | RCH-1.20 |
| NOU-02 | Rename/reorder/removal and resource replacement update/fence the outline incrementally without unrelated navigation. | RCH-1.29 | RCH-1.20 |
| NOU-03 | Read-only/folded-target navigation changes no document/Undo state and avoids full-document/layout work per caret event. | RCH-1.29 | RCH-1.20 |
| NBL-01 | A conforming host copies a read-back value that resolves to the intended authorized block; missing clipboard/host capability is truthful. | RCH-1.30 | RCH-1.20 |
| NBL-02 | Durable host navigation survives move/reload/migration within the selected identity contract and refuses deleted/revoked targets. | RCH-1.30 | RCH-1.20 |
| NBL-03 | Duplicate/import and late cross-resource results cannot alias or expose another block; private editing anchors are not assumed public URLs. | RCH-1.30 | RCH-1.20 |
| NAN-01 | Host-authorized creation/reply/resolution targets selected text/blocks without changing accepted body content. | RCH-1.31 | RCH-1.20 |
| NAN-02 | Edits/moves/deleted or ambiguous anchors retain a truthful navigable/orphaned discussion state and host audit identity. | RCH-1.31 | RCH-1.20 |
| NAN-03 | View/comment/edit permissions, reconnect and stale session callbacks cannot expose or write unauthorized discussions. | RCH-1.31 | RCH-1.20 |
| NHR-01 | Human proposals are visibly distinct from accepted content and require no AI capability. | RCH-1.32 | RCH-1.20 |
| NHR-02 | Authorized accept/reject uses the current revision/target exactly once, preserving intervening human work and the existing history/apply owner. | RCH-1.32 | RCH-1.20 |
| NHR-03 | Stale/conflicted/revoked/failed review retains recoverable original text and cannot silently retarget. | RCH-1.32 | RCH-1.20 |
| NAD-01 | Synced-block decision covers source/instance identity, access/editing, propagation, unlink and deletion/recovery; default remains deferred. | RCH-1.33 | RCH-1.20 consumes decision |
| NAD-02 | Database-view decision names host data/query/access/export bounds and its distinction from table content; default remains deferred. | RCH-1.33 | RCH-1.20 consumes decision |
| NAD-03 | Button decision restricts typed actions, permissions, consequential-write confirmation, idempotency/audit and forbids arbitrary execution; default remains deferred. | RCH-1.33 | RCH-1.20 consumes decision |

## Current publication and runtime policy

Follow ADR 006: one current document format, with unsupported-input preservation/rejection and external-format fallbacks; historical fixtures do not create a production version matrix. Final target-runtime/device/AT observations belong to roadmap 43 and may use appropriate simulators/emulators/VMs. The producer/final-consumer column below identifies functional and deterministic coverage ownership; incomplete target-runtime observations keep support claims open without blocking independent features. Do not commit generated test reports or captures.

## Evidence requirements

Use exact source/compiled/packed identities, operation/fixture IDs and nonzero executed/passed/failed/skipped counts when a case becomes executable. A copied-link toast, available enum, source checkbox, prerecorded competitor interaction, mock host or unavailable device is not independent proof of the SDK's corresponding user journey. Keep actual device/AT/clipboard, host-domain authorization and native client claims separate from deterministic semantic proof.
