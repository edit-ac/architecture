# Notion simple-table controls

Status: research/plans, 2026-11-08. No implementation, published package, mobile/AT or release qualification is claimed. [Table-control contract](../specs/table-controls.md) owns accepted behavior; [NTC-01–16](../tests/notion-table-cases.md) define planned observations.

## Current source baseline

This pass inspected current GitHub core a0ec43bc, fetched read-only on 2026-11-08, rather than the older local core baseline in [the first block-editor comparison](notion-block-editor.md). Sources are packages/web/src/modules/tables/current.ts, cell-input.ts, presenter.ts, packages/web/styles/ui.css, crates/editac-core/src/table.rs and table/. Codanna was bound to another project, so bounded source reads supplied this project's code evidence. Source availability is not execution or visual evidence.

The current presenter already renders a semantic table with direct rich cell hosts, retained identities, scoped input/IME handling, rich rectangles, header/alignment commands, structure actions, a live status and horizontal scroller. UDM-1.8 direct-cell delivery is checked in its source plan; do not recreate its old textarea/preview defect as the current implementation. The older surface-ledger description is superseded for these inspected sources.

Remaining control gaps: long structure/format groups and a separate per-cell selection-button group; no comparable table/row/column/cell menu shell; no width/fit/distribution control in the inspected presenter; no direct row/column drag or non-drag movement presenter. Header cells currently receive scope=col, so a first-column header action needs correct row-header associations. The kernel accepts alignment/header/style plus namespaced metadata; accepting generic metadata does not establish a typed, portable width or color capability. Merges remain outside the admitted simple-table contract.

## Live Notion observations

The authorized disposable page's synthetic 3×3 sample was checked in the in-app browser at an actual 1436×710 desktop viewport. Existing content and sharing were preserved; only our research sample was edited. It ended with its original shape, text, widths, headers and colors. Private page/account identifiers and screenshots are deliberately excluded from public Git.

| Scope | Observed behavior |
| --- | --- |
| Whole table | Block handle opens Fit to width, Header row/column and whole-block actions. Targeting tints the table. Database conversion was visible, not invoked. |
| Row | An edge grip exposes Move row; click opens Color, Insert above/below, Duplicate, Clear contents and Delete. A blue row-wide outline retains the target. |
| Column | A top grip opens Color, Insert left/right, Duplicate, Clear contents and Delete, with a full-height outline. |
| Cell | A blue active-cell outline has a right-edge menu handle. Menu: Color and Clear contents. Ordinary right-click did not open that menu in the checked state. |
| Rectangle | Shift-click produced a 2×2 outline. Rectangle menu/merge and corner-drag selection were not established. |
| Header | Header-row toggle shaded/emboldened the row and changed accessible cell descriptions to table header. Header-column toggle was visible, not exercised. |
| Insertion/history | Insert below changed 3 rows to 4; Undo restored 3. |
| Axis color | Blue background applied to all cells in one column, including its header. Undo restored defaults. Text/background palettes were separate. |
| Width | An 80px divider drag changed the first column from about 128.33px to 208.33px, leaving the other columns unchanged. Undo restored it. The measured 3px painted resize stripe is not a touch-target recommendation. |
| Fit | Fit to width yielded about 214.33px per column in this containing region. Undo restored original widths. The exact fit algorithm is unknown. |
| Appearance | Thin neutral borders, compact padding, subdued bold headers, a distinct active/axis outline and controls in edge/overlay space. Desktop/light observation only. |
| Keyboard | Ordinary-cell Tab movement was observed. Final-cell Tab behavior remained unresolved; do not infer its append/exit policy. |

## Official documentation

[Current Notion help](https://www.notion.com/help/columns-headings-and-dividers) additionally documents bottom/right add controls, corner dimension adjustment, divider resizing, cell color/clear, fit and merge/unmerge. It states that merge clears non-anchor content and unmerge restores empty covered cells. That policy was not exercised or adopted. The page also says multi-cell simple-table paste is unavailable; retain edit.ac's richer bounded transfer.

[Notion's simple-table guide](https://www.notion.com/help/guides/simple-tables-vs-databases) documents axis drag reordering and distinguishes document tables from database properties/views/formulas. Internal storage, merge algorithms and convergence remain unknown.

## Delivery disposition

| Gap | Owner and boundary |
| --- | --- |
| Compact table/axis/cell menus and aggregate headers | New UDM-1.10 consumes existing guarded targets and semantic commands; one default control owner, keyboard/touch entry and retained target. |
| Width/fit/distribute semantics | New RCH-1.34 defines typed ownership/admission/history/serialization before UDM-1.11 renders controls. No generic metadata or DOM-only persistence workaround. |
| Axis duplicate/move/clear and drag alternatives | Existing RCH-1.6/1.8 retain semantic operations; UDM-1.12 consumes their current receipt and builds the presenter. |
| Row/column headers | Existing RCH-1.7 retains header semantics, including associations; UDM-1.10 owns aggregate toggles. |
| Color and merged-cell capability | RCH-1.35 records a bounded accept/defer/reject decision. Current unsupported geometry retains safe rejection/recovery; no silent conversion or automatic schema variant. |
| Rich formatting and paste | Existing RCH-1.23 and UDM-1.9 keep ownership. No duplicate parser, per-cell engine, clipboard service or undo stack. |
| Visual/platform acceptance | UTW-1.2 retains NTC cases and TPT cases after functionality; roadmap43 owns actual browser/native/IME/AT observations. Optional UI adapters consume the same contracts and preserve their existing final owners. |

## Evidence boundaries and remaining gaps

REA 6.8.0 separately captured the public help page at 1280×900: ev_f01442c660ff8a9de432bfbb2d23aeb8c18ea27802efb2dc5883f822bdfadc97, Chromium 156.0.8078.80. Scenario steps completed and provider-owned browser cleanup reported terminated-owned-process. This is public reference rendering, not authenticated editing proof. Authenticated checks above used CUA AX/DOM and inspected screenshots; private/generated output stays outside source repositories.

The attempted 390×844 in-app viewport override left the measured page at 1436×710 and was reset; there is no narrow/mobile proof. Row/column reorder/duplicate/delete, live merge/unmerge, multi-user changes, cell-format export, physical touch, manual AT and current mounted edit.ac appearance were not qualified. No application test, package build, runner change, credential loading or inference request ran. Planning/document checks cannot complete these behavior cases.

## Planning checks

The changed root roadmap graph validates: 43 files, 592 parents, zero graph errors. The UI source validator sees 31 files and 165 parents; it still reports the same 36 preexisting failures as the unchanged bec606a baseline (receipt/manifest mismatches and two already oversized sources), with zero added failures. Those failures are retained, not waived or repaired through this research. All 27 added local document links/anchors and focused whitespace checks passed. No application runtime or device acceptance was rerun or recertified.
