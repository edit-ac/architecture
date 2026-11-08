# Notion table-control acceptance cases

Status: planned cases, 2026-11-08. These are authored requirements, not runnable tests or passing observations. [Table controls](../specs/table-controls.md) owns behavior; [research](../rea/notion-tables.md) separates live and documented reference evidence.

Fixtures: a 3×3 basic table; 20×10 multiline/long/Unicode/RTL content; a table beside each viewport edge; an empty/readonly/protected table; merged input for explicit safe rejection under the current profile. Each operation records exact content, selection, history and authorization effects. No provider calls or external clipboard fixtures.

| ID | Observable outcome |
| --- | --- |
| NTC-01 | Idle grid has one copy of cell text, neutral borders and consistent spacing; activating/dismissing controls does not move surrounding document content. |
| NTC-02 | Table/axis/cell/rectangle targets are visually distinct; native text selection remains legible in light/dark/forced colors, including inline code. |
| NTC-03 | Click and keyboard activation open the same scoped menu; search, arrow navigation, Escape and focus return preserve its captured target through scroll/resize. A deleted/stale target closes or rejects safely. |
| NTC-04 | Insert before/after, duplicate, non-drag move and drag move preserve cell data/order, defined header/width behavior and one intentional undo group. |
| NTC-05 | Clear contents retains shape and supported metadata; row/column/table delete affects exactly the labelled target, with explicit last-row/column behavior and predictable post-action focus. |
| NTC-06 | Header row/column actions report on/off/mixed accurately and produce correct row/column header associations, including the top-left intersection. |
| NTC-07 | Divider hit regions do not steal cell selection; resize has a visible guide/cursor, bounds, cancel and keyboard alternative. Prolonged/interrupted/repeated drags recover without reload or stray history. |
| NTC-08 | Fit to container, distribute and automatic content sizing are separate operations; explicit widths survive supported edits/reopen. Resize/scroll/zoom preserves alignment across rows/spans. |
| NTC-09 | Newline, Tab/Shift+Tab, final-cell append or exit, arrows in text versus rectangle mode and Escape-to-exit have explicit documented outcomes; no focus trap or accidental structural action during IME. |
| NTC-10 | Hover and keyboard focus reveal the relevant affordance; touch has a persistent context entry and move/resize alternatives, with generous hit areas independent of the grip's painted size. |
| NTC-11 | Only the table scrolls when needed; axis handles, menus and insertion/drop cues track the visible grid and stay reachable at 390×844, 1024×768, 1440×900, zoom and RTL. |
| NTC-12 | Table formatting uses supported tokens, readable selection and accurate scope; unsupported colors/merge/data operations are hidden or explained, without fake successful mutation. |
| NTC-13 | Supported merge/split preserves the declared content policy and undo; unsupported merged input retains recovery data and rejects without mutation. Never silently adopt Notion's clearing policy. |
| NTC-14 | Internal/HTML/TSV/Markdown and permitted CSV preserve declared boundaries/marks/empty cells; copied data contains no controls, and formulas remain literal. |
| NTC-15 | Readonly/protection/revocation, remote axis removal, host switch and teardown cancel transient gestures/menus, preserve data and do not leak listeners or captures. |
| NTC-16 | Default/host themes, two editor roots, portaled controls and each declared optional UI adapter are visually inspected separately. Packed/editable runtime, browser, fixture, viewport, focus/AT/device provenance and outstanding gaps are recorded. |


## Execution ownership

RCH-1.6/1.7/1.8/1.23 retain changed semantic selectors; RCH-1.34 owns width admission/history and RCH-1.35 owns explicit capability decisions. UDM-1.10 runs one scoped menu/focus case; UDM-1.11 one resize/cancel case; UDM-1.12 one axis move/undo case. Case authoring and the remaining packed visual/interaction matrix stay UTW-1.2 after functional delivery, reusing compatible TPT and semantic receipts. UTW-1.9 and roadmap43 retain manual AT, native/device and browser-runtime observations. Missing or skipped mandatory behavior cannot be called supported. Do not run all cases per development slice.
