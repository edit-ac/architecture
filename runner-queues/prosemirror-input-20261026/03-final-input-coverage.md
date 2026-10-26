# Complete input and navigation regression coverage

Status: IN_PROGRESS

## Editor-lane adoption — user decision, 2026-10-26

The user explicitly authorized this plan to lead the existing EDITOR queue before performance improvements and testing. Execute in `/Users/bpstr/Github/edit-ac-editor-20261026`; PRIMARY integrations remain untouched in `/Users/bpstr/Github/edit-ac`. This authority supersedes the original planning-only/root-main execution wording below, without changing any task ID, acceptance, dependency or validation requirement. Use one ready parent per worker; workers update only verified live-source checkboxes and Status, with evidence/handoff in the named separate progress file. Retain current ES/EDX/BTA/BTU proof only where exact input applicability holds. Current plan inputs and read-only PRIMARY comparison provenance are preserved; do not edit PRIMARY source, queue, index, progress, artifacts or worker.

Read the active shared lane coordination section before every parent. Require the guarded launcher and live readiness. Checkpoint validated editor-owned deltas under the shared integration lock every two parents/source boundary; preserve inherited dirty bytes and defer mixed hunks. No second EDITOR controller, delegated agents, silent migration, alternate runtime format, paid inference, credentials, external provisioning, push, publication or deployment. Current Rust prepared semantics/shared history remain authoritative. Functional sources01/02/02b lead the FIFO; final source03 follows all functionality and bounded performance improvements. Preserve prepared/mock transports, zero-match/skip failures and exact OS/browser scope. Stop on BLOCKED and do not restart unchanged input.


## Goal and entry conditions

Own all new permanent test development and comprehensive coverage for this plan after functional delivery. Progress: `.roadmap-runner/prosemirror-input-20261026/03-final-input-coverage.progress.md` from the workspace root. The [index](README.md) assigns each finding exactly once. Reuse current-source functional, EDX and ES evidence; do not duplicate general Unicode, cross-block composition or native/TUI suites.

Each parent below requires current delivery receipts only for its named findings. Check loaded package/source identities, observable effects and limitations, not just predecessor checkboxes. All functional sources precede this file in a prospective serial queue; blocked unrelated prerequisites require a controller scheduling decision, not skipped acceptance. Use the existing guarded root-main process only if execution is later authorized. This document does not start or append a runner.

Extend existing browser fixtures/case IDs where possible. Name new narrow cases `PKI-F01`, etc., so selectors have nonzero coverage. From `core/`, existing runner syntax is `npm run test:browser -- <suite> --test-name-pattern='<case selector>'`; it runs Chromium, Firefox and WebKit. Direct one-browser diagnosis may use the corresponding test file and existing `EDITAC_<SUITE>_BROWSER/OUTPUT` controls. Inspect harness output ownership before execution: outputs must go to ignored task-owned paths. Reuse a current valid packed consumer when supported; do not equate stale bundles with changed source. Missing prerequisites, zero matches and skipped cases are not passes.

Record exact selectors, loaded sources, expected/actual state, counts, browser/profile, reused evidence and remaining limitations in each parent's progress section. Handoff records the next unchecked assertion, failing fixture and exact changed-input resume condition. Preserve only active failure diagnostics; close task-owned browsers/servers. No paid provider calls, secret loading, automatic fixture recording, publication or fabricated OS/mobile keyboard evidence. Broaden checks only for a demonstrated impact or an applicable gate, with reason and expected cost recorded first.

## Epic PKI-3 — Test the remaining interactions once

### Task PKI-3.1 — Cover chords, selections, rules and boundary commands

- [ ] PKI-3.1 Complete F01/F02/R03/R04/R06 regression coverage.

Purpose: One deterministic case set for root command ownership and exact selection effects.
Context: `core/tests/browser/interactions/{keyboard,breaks,deletion,command-surfaces}.spec.ts`, `core/tests/browser/shortcuts.spec.ts`, existing browser-input fixtures; comparison F01/F02/R03/R04/R06.
Dependencies: none.
Entry receipts: validated PKI-1.1, PKI-1.2, PKI-1.5, PKI-2.4 and PKI-2.6 delivery receipts.
Independent work: fixture drafting; PKI-3.2/3.3 when their own receipts exist.
Session scope: missing test cases and affected selectors, 45 minutes; split before adding an unrelated matrix.
Acceptance: Plain/Shift/reserved/remapped/host-canceled Enter and Backspace, half-open Tab ranges in both directions, zero/end offsets, mixed blocks, non-Latin/shifted shortcuts and AltGraph negatives, code/atom continuation, and modifier deletion with/without target ranges have exact independent oracles. Include a trusted canceled-key case that reaches neither the conversion nor reversal hook. Check text, owner/parent IDs, selection direction, one undo group and no-op/rejection effects; do not rely on screenshots or command-call counts alone.

Implementation:

- [ ] PKI-3.1-I1 Reconcile retained coverage, then add only missing named cases and negative controls to existing suites; keep a single assertion owner per finding.

Validation:

- [ ] PKI-3.1-V1 Run the affected `shortcuts`, `interaction-keyboard`, `interaction-breaks`, `interaction-deletion` or `interaction-command-surfaces` selectors for this parent's `PKI-(F01|F02|R03|R04|R06)` cases. Select only suites containing new cases. Budget: 10 minutes; count each browser separately.
- [ ] PKI-3.1-V2 Reconcile passing delivery evidence, native-layout limitations and actual affected package checks; require a concrete changed input before repeating a passing selector.

Evidence: parent progress with selectors/counts and current-source oracle results.
Handoff: missing fixture or failed command/selection boundary and exact repair prerequisite.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-3.2 — Cover nested table input, spacing and focus

- [ ] PKI-3.2 Complete F03/F04/F05/F06 regression coverage.

Purpose: Current addressed-table consumers prove text visibility, control ownership and exactly-once input together.
Context: `core/tests/browser/current-table.spec.ts`, `core/tests/browser/interactions/{keyboard-tables,break-tables,cell-multiline,whitespace}.spec.ts`, current table fixtures and table DOM mapping; comparison F03–F06.
Dependencies: none.
Entry receipts: validated PKI-2.1, PKI-2.2 and PKI-2.3 receipts.
Independent work: fixture drafting or another ready final parent.
Session scope: missing table regression cases and narrow browser runs, 45 minutes.
Acceptance: Native URL-field undo leaves the document/history unchanged; cell/grid history still works; Escape/Shift/arrow/blur/pointer sequences reach the expected focus target. First/last cell, held Tab and read-only controls remain safe. Unstyled-host cells preserve ordinary/repeated/leading/trailing space, TAB, NBSP/narrow NBSP/ZWSP, emoji/combining text and LF; one/two trailing breaks plus typing/copy/reopen retain exact text and caret. Noncancelable Enter and duplicate notifications commit once. Preserve neighboring cells, geometry and identities. Filler and authored breaks have distinct oracles.

Implementation:

- [ ] PKI-3.2-I1 Extend current addressed-table fixtures with only the uncovered `PKI-F03`–`PKI-F06` cases, including plain-host presentation and negative controls; reuse baseline INT/EDX whitespace assertions.

Validation:

- [ ] PKI-3.2-V1 Run the affected `current-table`, `interaction-keyboard-tables`, `interaction-break-tables` or `interaction-cell-multiline` selectors matching `PKI-F0[3-6]`; use `interaction-whitespace` only if it owns a new case. Budget: 10 minutes across the declared browsers.
- [ ] PKI-3.2-V2 For the whitespace/one-edit case, verify one real current-engine undo and durable reopen; reuse an existing compatible receipt for unchanged table persistence rather than rerunning a broad suite.

Evidence: parent progress distinguishes computed style, rendered/caret effects, canonical text and durable state.
Handoff: exact browser/event/whitespace variant still failing.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-3.3 — Cover composition, mobile Enter and atom movement

- [x] PKI-3.3 Complete R01/R02/R05 coverage and runtime handoff.

Purpose: Prepared event mechanics and actual browser navigation are tested without overstating real keyboard/IME support.
Context: `core/tests/browser/{composition,editing-input}.spec.ts`, `core/tests/browser/interactions/navigation.spec.ts`, `core/tests/mobile-web/input.spec.ts`; comparison R01/R02/R05 and existing MWB/43 runtime owners.
Dependencies: none.
Entry receipts: validated PKI-1.3, PKI-1.4 and PKI-2.5 receipts; affected ES-1.2 capability receipt where consumed.
Independent work: prepared trace authoring or another ready final parent; unavailable OS input evidence does not prevent these mechanics checks.
Session scope: missing event-order/navigation cases and honest handoff, 45 minutes; target-runtime campaigns remain with existing owners.
Acceptance: Both composition orders, delayed confirmation, pointer confirmation then deliberate Enter, missing keyup, repeat, 229 Enter and Backspace/Dead/Process and duplicate final events produce the specified commit counts. Native Enter without keydown/cancelability handles one supported structural shape and preserves recovery for rejected shapes. Arrow/Shift+Arrow across atoms, decorations, wrapped lines and RTL/mixed-direction text keeps valid endpoints and zero semantic writes. Plain space/NBSP, ZWJ/combining boundaries and missing optional APIs reuse ES coverage rather than create a second Unicode policy. Real mobile/OS IME and assistive-input claims require their actual runtime evidence.

Implementation:

- [x] PKI-3.3-I1 Add only missing `PKI-R01`, `PKI-R02` and `PKI-R05` sequences, keeping synthetic event replay separate from trusted browser navigation.

Validation:

- [x] PKI-3.3-V1 Run the affected `composition`, `editing-input` and `interaction-navigation` selectors matching `PKI-R0[125]`; confirm nonzero per-browser counts. Budget: 10 minutes; no automatic full-suite rerun.
- [x] PKI-3.3-V2 Record a concise crosswalk for the original 12 findings: current tested source, fulfilled assertions, reused ES/EDX receipts and exact remaining target-runtime owner/case. PKI-3.4/3.5 supply the F07–F10 extension receipts for the controller's complete 16-finding summary. Required runtime observations remain unchecked with resume conditions; no prepared trace is promoted to device qualification.

Evidence: parent progress contains the final coverage crosswalk and provenance.
Handoff: precise unqualified browser/IME/mobile scenario, named MWB/43 owner and required runtime receipt.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-3.4 — Cover native formatting and table editing intentions

- [x] PKI-3.4 Complete F07/F10 native-intention coverage.

Purpose: Non-keyboard formatting and admitted table text intentions have deterministic semantic oracles independent of hardware shortcuts.
Context: [additional comparison](../../research/open-source-editor-input-20261026.md) F07/F10; `core/tests/browser/interactions/command-surfaces.spec.ts`, `core/tests/browser/current-table.spec.ts`, existing cell-multiline fixtures and current prepared engine commands.
Dependencies: none.
Entry receipts: validated PKI-4.1 and PKI-4.4 delivery receipts.
Independent work: fixture drafting or another ready final parent.
Session scope: missing native-intention cases and affected browser selectors, 45 minutes including checks.
Acceptance: Supported `formatBold/Italic/Underline/StrikeThrough` without keydown agree with command semantics, including reversed ranges, empty typing state, no-op/read-only and foreign-control ownership. Table `deleteContent`, `deleteEntireSoftLine` and `insertFromYank` have valid-range/payload, missing-data, noncancelable and protected/cross-block controls. A visual line target is not guessed from LF text. Observe marks/text, directional caret, history count and unchanged neighboring cells; unknown/unsupported intentions leave no uncontrolled browser-only mutation. Prepared events do not qualify actual OS menu, speech, gesture or yank support.

Implementation:

- [x] PKI-3.4-I1 Add only missing `PKI-F07` and `PKI-F10` cases to existing fixtures, reusing PKI-3.2's unchanged table input lifecycle and existing formatting matrices.

Validation:

- [x] PKI-3.4-V1 Run the affected `interaction-command-surfaces`, `current-table` or `interaction-cell-multiline` selectors matching `PKI-(F07|F10)`; use only suites containing these cases. Budget: 8 minutes across declared browsers; require nonzero per-browser counts.
- [x] PKI-3.4-V2 Record the actual supported input vocabulary and target scopes, real-engine result receipts and exact outstanding runtime cases for existing INT/MWB/43 owners. Reuse unchanged history/durability evidence.

Evidence: parent progress with input type, scope, result counts and native-versus-prepared provenance.
Handoff: exact unqualified native gesture or failing semantic target.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-3.5 — Cover replacement payloads and ordinary event correlation

- [ ] PKI-3.5 Complete F08/F09 replacement coverage.

Purpose: Authoritative replacement text is preserved and independent corrections cannot be mistaken for duplicate key notifications.
Context: [additional comparison](../../research/open-source-editor-input-20261026.md) F08/F09; `core/tests/browser/{input-policy,editing-input}.spec.ts`, `core/tests/browser/interactions/replacement.spec.ts`, existing source-bound browser-input fixtures.
Dependencies: none.
Entry receipts: validated PKI-4.2 and PKI-4.3 receipts.
Independent work: fixture drafting or another ready final parent.
Session scope: missing payload/sequence cases and bounded selectors, 45 minutes including checks.
Acceptance: String `data` and `dataTransfer` text resolve identically for valid reported targets; empty, absent, conflicting and unsupported MIME values are distinguished. Cover selected/reversed mixed-mark text, compatible cross-block replacement through existing ES ownership, exact whitespace/Unicode, permissions and stale targets. Space insert/input → independent correction before keyup and its after-keyup control each accept two edits; true notification echoes accept one. Missing keyup, intervening native selection changes, repeated identical deliberate input and composition boundaries preserve correct text/selection/history. Native fallback without payload retains recovery behavior; do not claim that the original fallback always loses text.

Implementation:

- [ ] PKI-3.5-I1 Add only missing `PKI-F08` and `PKI-F09` cases with independent state/effect oracles and positive/negative correlation controls; reuse existing composition and Unicode assertions.

Validation:

- [ ] PKI-3.5-V1 Run affected `input-policy`, `editing-input` or `interaction-replacement` selectors matching `PKI-F0[89]`; use only suites containing new cases. Budget: 8 minutes across declared browsers; require nonzero per-browser counts.
- [ ] PKI-3.5-V2 Combine these receipts with PKI-3.4 and the original final owners into the 16-finding controller summary. Keep actual spellchecker, IME and platform timing cases explicitly assigned to existing runtime owners and unqualified until their evidence exists; no repeated broad suite run is implied.

Evidence: parent progress with event order, operation target, payload source, loaded source and exact effect counts.
Handoff: remaining correlation ambiguity, unsupported native DOM shape or exact target-runtime observation.

Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.
