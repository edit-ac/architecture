# Correct rich-context input and navigation

Status: COMPLETE

## Editor-lane adoption — user decision, 2026-10-26

The user explicitly authorized this plan to lead the existing EDITOR queue before performance improvements and testing. Execute in `/Users/bpstr/Github/edit-ac-editor-20261026`; PRIMARY integrations remain untouched in `/Users/bpstr/Github/edit-ac`. This authority supersedes the original planning-only/root-main execution wording below, without changing any task ID, acceptance, dependency or validation requirement. Use one ready parent per worker; workers update only verified live-source checkboxes and Status, with evidence/handoff in the named separate progress file. Retain current ES/EDX/BTA/BTU proof only where exact input applicability holds. Current plan inputs and read-only PRIMARY comparison provenance are preserved; do not edit PRIMARY source, queue, index, progress, artifacts or worker.

Read the active shared lane coordination section before every parent. Require the guarded launcher and live readiness. Checkpoint validated editor-owned deltas under the shared integration lock every two parents/source boundary; preserve inherited dirty bytes and defer mixed hunks. No second EDITOR controller, delegated agents, silent migration, alternate runtime format, paid inference, credentials, external provisioning, push, publication or deployment. Current Rust prepared semantics/shared history remain authoritative. Functional sources01/02/02b lead the FIFO; final source03 follows all functionality and bounded performance improvements. Preserve prepared/mock transports, zero-match/skip failures and exact OS/browser scope. Stop on BLOCKED and do not restart unchanged input.


## Goal and execution contract

Close F03–F06 and qualify R04–R06 in the [comparison](../../research/prosemirror-input-navigation-20261026.md). Progress: `.roadmap-runner/prosemirror-input-20261026/02-rich-context-and-navigation.progress.md` from the workspace root. Read only the selected finding, task and named source/spec sections.

This planned source does not alter or start a runner. Preserve the guarded serial root-main lane, existing work and one current format. Rust prepared commands own semantic changes; browser layout/temporary input owns visual navigation. Update the authoritative semantic spec and acceptance together before adding a contract. Reuse current-format EDX, ES and BTA/BTU receipts for their exact boundaries. No paid inference, provider credentials, publication or automatic document conversion.

All six parents are independently eligible unless their named entry receipt is missing. A later serial file cannot run around a blocked source without a controller decision. For an affected optional-API boundary, PKI-2.5 consumes the ES-1.2 repair; it does not implement that repair again. Keep ordinary block-selection UX with ES-3.1/3.2 and generic Insert after with BTA/BTU. Source 01's IME/layout work is reused when present, but its completion is not an artificial gate on table whitespace or focus fixes.

One parent per session. Functional checks below are bounded; all new permanent tests and complete matrices belong to source 03. Evidence for each parent goes in its progress section: changed paths, current loaded source, exact check/steps, executed/passed/failed/skipped counts, expected/actual effects and reused evidence. Handoff records the next unchecked step, target symbol, precise failure and owned process/output paths. Record blocker fingerprint, owner and changed-input resume condition; stop unchanged retries and select independent ready work. Preserve source checkbox/Status-only updates. Tear down task-owned browsers/servers and remove inactive routine artifacts.

## Epic PKI-2 — Keep each rich editing scope predictable

### Task PKI-2.1 — Scope table keyboard commands and expire focus escape

- [x] PKI-2.1 Fix table native-control ownership and one-shot Escape.

Purpose: Typing in a table toolbar field cannot undo the document, and intervening navigation cannot leave an old Escape armed.
Context: comparison F03/F04; `core/packages/web/src/modules/tables/current.ts::keyboard` and cell listeners; `input/keyboard.ts::action`; `input/focus.ts::leaveEditor`; ES-KEY-1 and `specs/platform-editing-services.md`.
Entry receipts: Applicable current-source ES/EDX and named comparison findings; authenticate required interfaces rather than replay completed work.
Dependencies: none.
Independent work: PKI-2.2–2.6.
Session scope: the table keyboard/focus boundary, 45 minutes including checks.
Acceptance: Link field undo/redo and native control keys belong to that control. Cell/grid history uses the platform profile and applicable reservations. Escape → Tab escapes; Escape → Shift → Shift+Tab escapes backwards; Escape → arrow/pointer/blur → Tab follows normal cell navigation. IME Escape wins. First/last cell, repeat and read-only focus behavior remain explicit and nontrapping.

Implementation:

- [x] PKI-2.1-I1 Resolve the actual control/cell/grid target before command handling, reusing shared shortcut policy where applicable.
- [x] PKI-2.1-I2 Apply the root's one-shot focus-escape state rules to table activity and teardown.

Validation:

- [x] PKI-2.1-V1 Replay nested URL-input undo, stale-Escape navigation and direct backward escape against the current handler; verify history-call count and focus target. Budget: 3 minutes; final owner PKI-3.2.

Evidence: parent progress entry with control/cell/grid distinction.
Handoff: exact key/target that still has ambiguous ownership.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-2.2 — Preserve table whitespace and authored breaks visually

- [x] PKI-2.2 Give cell prose and code an explicit whitespace/caret projection.

Purpose: Spaces and LF in cells appear and navigate as authored under the default host stylesheet.
Context: comparison F05; `modules/tables/current.ts::render`, `modules/tables/cell-dom.ts::cellDOMText/point/domPoint`, `dom/render.ts` whitespace/placeholder code; `specs/editing-experience.md` repeated breaks and tables; INT-1.8.
Entry receipts: Applicable current-source ES/EDX and named comparison findings; authenticate required interfaces rather than replay completed work.
Dependencies: none.
Independent work: the other PKI-2 parents.
Session scope: table rendering and its existing text-offset projection, 45 minutes including checks.
Acceptance: Prose preserves repeated/leading/trailing spaces, TAB and LF while wrapping; code retains its declared literal layout. One/two trailing LF and an empty owner have reachable correct UTF-16 carets. Filler BR contributes zero and authored LF one; provenance is explicit. Host CSS cannot be required to make ordinary breaks visible. Source characters and cell identities remain exact; no NBSP or zero-width normalization.

Implementation:

- [x] PKI-2.2-I1 Apply the existing whitespace contract at cell text owners, keeping controls readable and code layout intentional.
- [x] PKI-2.2-I2 Resolve the sole-BR ambiguity using canonical text/projection provenance and align DOM/model positions for trailing breaks without persistent sentinel characters.

Validation:

- [x] PKI-2.2-V1 In an unstyled mounted cell, inspect computed whitespace, visual line placement and caret after `a  b\n`, then type X. Check one empty/filler control. Budget: 3 minutes; exact round-trip matrix belongs to PKI-3.2.

Evidence: parent progress entry separating stored text from visual/caret observations.
Handoff: unresolved filler/native-shape mapping.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-2.3 — Correlate noncancelable cell input

- [x] PKI-2.3 Give table beforeinput/input/mutations one edit owner.

Purpose: A browser edit that cannot be canceled cannot run after a duplicate synchronous semantic edit.
Context: comparison F06; `modules/tables/current.ts` cell `beforeinput`, `input`, `edit`, `insert` and composition listeners; `input/text.ts` ownership patterns; `specs/table-paste-and-editing.md` and EDX cell-break contract.
Entry receipts: Applicable current-source ES/EDX and named comparison findings; authenticate required interfaces rather than replay completed work.
Dependencies: none.
Independent work: the other PKI-2 parents. Reuse PKI-1.3 correlation if available; do not wait for unrelated root functionality.
Session scope: one cell input lifecycle, 45 minutes; no new table storage/API version.
Acceptance: Cancelable and noncancelable Enter/Shift+Enter plus later input/mutations produce one LF and one history group. Selected text replacement preserves unselected content and identities. Missing-keydown/final-composition input is neither replayed nor dropped. Unsupported structure retains recoverable text, canonical state and a stable target; read-only rejection adds no mutation. Reported correction/deletion ranges do not redirect edits to a later caret.

Implementation:

- [x] PKI-2.3-I1 Separate cancelable command handling from native reconciliation and bind the complete sequence to its captured cell target.
- [x] PKI-2.3-I2 Correlate final notifications and rejection/blur cleanup with the existing table history and recovery path.

Validation:

- [x] PKI-2.3-V1 Replay one noncancelable break plus native mutation/input and one cancelable selected replacement; observe text, caret and transaction/history counts. Budget: 4 minutes; final owner PKI-3.2.

Evidence: parent progress entry including each event's cancelability.
Handoff: exact unsupported event/DOM shape and recovery state.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-2.4 — Expose keyboard continuation beside code and atoms

- [x] PKI-2.4 Add a discoverable continuation command through existing block actions.

Purpose: Users can continue prose after a final code or noneditable block without a pointer.
Context: comparison R04; `commands/catalog.ts`, `input/keyboard.ts::execute`, `dom/selection.ts::selectedNode`; `specs/block-actions.md` Insert after; `specs/editing-experience.md` code/atom boundaries.
Dependencies: none.
Independent work: the other PKI-2 parents.
Entry receipts: authenticate the existing prepared Insert after capability or identify its BTA/BTU prerequisite owner; do not create a competing implementation.
Session scope: one continuation command and its keyboard/catalog integration, 45 minutes including checks.
Acceptance: Document Primary+Enter as the explicit code-continuation action and the corresponding selected-atom command/binding. It creates or targets the specified adjacent paragraph with one prepared edit, stable parent placement and correct undo/caret. Ordinary Enter and Shift+Enter in code remain literal LF. Unsupported/read-only targets are explained without inserting inside an atom or silently submitting a host form. Command reservations remain effective.

Implementation:

- [x] PKI-2.4-I1 Update the selected keyboard continuation contract and help, including reuse-versus-create behavior for an adjacent empty paragraph.
- [x] PKI-2.4-I2 Connect the captured code/atom target to the existing block action and result-selection path.

Validation:

- [x] PKI-2.4-V1 Run one terminal-code and one selected-atom continuation with undo, plus a Shift+Enter code preservation control. Budget: 3 minutes; final owner PKI-3.1.

Evidence: parent progress entry and prerequisite receipt.
Handoff: unresolved target applicability or block-action prerequisite.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-2.5 — Repair demonstrated atom navigation failures

- [x] PKI-2.5 Qualify visual movement into and out of atom selections.

Purpose: Arrow keys leave a valid native/text or atom selection without hidden caret stops or semantic edits.
Context: comparison R05; `dom/selection.ts::trackNativeMovement/toDOM/toModel/selectedNode`, `input/keyboard.ts::navigate`, renderer decoration maps; `specs/editing-behavior-standards.md` ES-TEXT-3/ES-SEL-1.
Dependencies: none.
Independent work: the other PKI-2 parents.
Entry receipts: consume ES-1.2's capability policy before modifying the Segmenter/modify repair seam; unrelated atom mapping can proceed immediately.
Session scope: one demonstrated atom/decoration boundary, 45 minutes; split independent browser quirks rather than build a general layout engine.
Acceptance: Arrow/Shift+Arrow from adjacent text or an exact atom range reaches a valid target and preserves the anchor, including vertical/wrapped/RTL cases selected for this boundary. No semantic commit, history item or persistent sentinel is introduced. Keep browser visual order and host/IME ownership. If native movement already meets a case, retain it with current-browser evidence.

Implementation:

- [x] PKI-2.5-I1 Bound the investigation to 10 minutes and one source-bound fixture; record the failing native movement or counter-evidence.
- [x] PKI-2.5-I2 Add only the required boundary repair using existing mapping/selection ports; keep optional capability and block-selection work with ES.

Validation:

- [x] PKI-2.5-V1 Exercise the demonstrated edge in both directions and one shifted range, recording DOM/model endpoints and zero writes. Budget: 3 minutes; remaining browser matrix belongs to PKI-3.3.

Evidence: parent progress entry with browser/version and native-versus-scripted motion.
Handoff: exact unresolved geometry/bidi/atom boundary.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-2.6 — Own modified deletion at structural boundaries

- [x] PKI-2.6 Preserve structural deletion when native ranges are missing.

Purpose: Word/line deletion at a block edge has an explicit semantic owner and safe fallback.
Context: comparison R06; `input/keyboard.ts::action/execute`, `input/text.ts` reported deletion, `input/reconcile.ts`; ES-KEY-1/ES-INPUT-1; existing fragment applicability and INT-1.4.
Dependencies: none.
Independent work: the other PKI-2 parents.
Entry receipts: reuse ES-1.3 compatible replacement when needed; existing native word deletion inside an owner remains independent.
Session scope: boundary classification plus delegation to existing join/outdent/atom operations, 45 minutes including checks.
Acceptance: With or without a target range, supported Control/Option/Command deletion at paragraph/list/quote/code edges chooses the documented join/outdent/select-first behavior once. Ordinary in-text word/line units remain browser/platform-owned. Unsupported cross-parent/atom structure is unchanged with explicit recovery where native DOM already moved. Forward/backward selections, history and read-only state remain safe.

Implementation:

- [x] PKI-2.6-I1 Reproduce the missing-range structural edge and document its platform chord/applicability without changing word segmentation.
- [x] PKI-2.6-I2 Delegate recognized boundaries to prepared commands and correlate any following beforeinput; preserve existing reported-range precedence.

Validation:

- [x] PKI-2.6-V1 Compare one boundary deletion without ranges, its reported-range equivalent and an in-text word-deletion control. Inspect semantic and DOM state plus history count. Budget: 4 minutes; final owner PKI-3.1.

Evidence: parent progress entry separating prepared traces from actual platform chords.
Handoff: precise unsupported parent/target-range combination.

Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.
