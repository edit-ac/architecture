# Correct key intent and text boundaries

Status: IN_PROGRESS

## Editor-lane adoption — user decision, 2026-10-26

The user explicitly authorized this plan to lead the existing EDITOR queue before performance improvements and testing. Execute in `/Users/bpstr/Github/edit-ac-editor-20261026`; PRIMARY integrations remain untouched in `/Users/bpstr/Github/edit-ac`. This authority supersedes the original planning-only/root-main execution wording below, without changing any task ID, acceptance, dependency or validation requirement. Use one ready parent per worker; workers update only verified live-source checkboxes and Status, with evidence/handoff in the named separate progress file. Retain current ES/EDX/BTA/BTU proof only where exact input applicability holds. Current plan inputs and read-only PRIMARY comparison provenance are preserved; do not edit PRIMARY source, queue, index, progress, artifacts or worker.

Read the active shared lane coordination section before every parent. Require the guarded launcher and live readiness. Checkpoint validated editor-owned deltas under the shared integration lock every two parents/source boundary; preserve inherited dirty bytes and defer mixed hunks. No second EDITOR controller, delegated agents, silent migration, alternate runtime format, paid inference, credentials, external provisioning, push, publication or deployment. Current Rust prepared semantics/shared history remain authoritative. Functional sources01/02/02b lead the FIFO; final source03 follows all functionality and bounded performance improvements. Preserve prepared/mock transports, zero-match/skip failures and exact OS/browser scope. Stop on BLOCKED and do not restart unchanged input.


## Goal and execution contract

Close F01/F02 and qualify R01/R02/R03 from the [comparison](../../research/prosemirror-input-navigation-20261026.md). Read only the finding and named source/spec sections for the selected parent. Progress: `.roadmap-runner/prosemirror-input-20261026/01-key-intent-and-text-boundaries.progress.md` from the workspace root.

Planning does not authorize runner execution or changes to an active queue. Preserve the existing guarded serial root-main lane. Use one current format and existing prepared Rust commands; no alternative history, compatibility reader, normalization or silent data conversion. Update the relevant authoritative spec and task acceptance together before changing a shared semantic contract. Earlier completed EDX/ES owners remain completed only for their original acceptance; consume current-source receipts rather than reopening them.

Select one ready parent per session. All parents here are independently eligible; there are no ordering-only dependencies. Read evidence against the current source before reusing it. Functional delivery uses the bounded checks below; new permanent tests and comprehensive matrices belong to final source 03. A small task-owned deterministic adapter probe is allowed for a concrete defect; it does not qualify the semantic engine or OS input. Keep output ignored, source-bound and small; never load provider credentials or make paid inference calls.

For every parent, Evidence means its separate progress section: changed paths, exact selector/manual steps, loaded-source identity, executed/passed/failed/skipped counts, limits and compatible evidence reused. Handoff means next unchecked step, target symbol, failure input, expected/actual result and task-owned process/output paths. On a blocker record owner, fingerprint and exact changed-input resume condition; continue another ready parent without unchanged retries. Keep hashes and delivery prose out of this source. Finish browsers/servers in teardown. An over-budget task needs a controller split, not reduced acceptance.

## Epic PKI-1 — Resolve key ownership before mutation

### Task PKI-1.1 — Respect break intent and shortcut policy before typing rules

- [x] PKI-1.1 Correct typing-rule command precedence.

Purpose: Shift+Enter and host-owned keys retain their intended action; ordinary unmodified fence Enter still converts when enabled.
Context: comparison F01; `core/packages/web/src/input/text.ts` event dispatcher; `input/keyboard.ts::action`; `core/packages/markdown/src/shortcuts.ts::convert/reverse`; `specs/editing-experience.md` break matrix.
Entry receipts: Applicable current-source ES/EDX and named comparison findings; authenticate required interfaces rather than replay completed work.
Dependencies: none.
Independent work: PKI-1.2–1.5.
Session scope: one dispatcher/rule eligibility boundary, 30–45 minutes including focused checks.
Acceptance: Shift+Enter after a fence inserts one LF in the same paragraph; reserved/remapped Enter and Backspace never trigger the original conversion/reversal ahead of their owner. A trusted Enter/Backspace already canceled by a host capture listener invokes no conversion/reversal and makes zero semantic changes. Default Enter conversion, immediate reversal and one history action remain correct. Paste, correction, composition and code content cannot gain direct-key eligibility accidentally. The canceled-key case is supported by the [additional editor review](../../research/open-source-editor-input-20261026.md).

Implementation:

- [x] PKI-1.1-I1 Resolve event ownership/profile and distinguish plain Enter from an explicit line break before conversion or reversal.
- [x] PKI-1.1-I2 Preserve the current direct-typing, permission, composition and conversion-history guards.

Validation:

- [x] PKI-1.1-V1 Use the existing browser-input/Markdown fixture for plain Enter, Shift+Enter and one reserved-key negative control after a fence; inspect owner, text, caret and transaction count. Budget: 3 minutes; defer full matrix to PKI-3.1.

Evidence: parent progress entry under the contract above.
Handoff: unresolved chord and exact rule/dispatcher boundary.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-1.2 — Use half-open block ranges for indentation

- [x] PKI-1.2 Exclude the untouched endpoint block from Tab commands.

Purpose: Tab and Shift+Tab act on the blocks actually selected.
Context: comparison F02; `core/packages/web/src/input/keyboard.ts::execute` indent/outdent branch; `specs/editing-behavior-standards.md` ES-BLOCK-1 and ES-KEY-1.
Dependencies: none.
Independent work: the other PKI-1 parents.
Entry receipts: consume existing mixed-applicability/ES-3.3 work if delivered; do not duplicate its target model.
Session scope: selected-block extent calculation and atomic command admission, 30 minutes including checks.
Acceptance: A range A:1 → B:0 and its reverse affect A only; B:1 includes B; a collapsed B:0 caret affects B. Preserve code-line endpoint exclusion, selection direction, list structure, min/max no-op behavior and one undo group. An invalid mixed selection has no partial indentation or stale selection restoration.

Implementation:

- [x] PKI-1.2-I1 Derive one ordered half-open block extent while retaining the original directional selection.
- [x] PKI-1.2-I2 Apply it to prose/list indentation and explicitly classify mixed code/prose applicability through prepared commands.

Validation:

- [x] PKI-1.2-V1 Run a current-source command-capture probe for the three endpoint forms and reverse direction, then one existing real-engine indent fixture. Record command owners separately from semantic proof. Budget: 3 minutes; final owner PKI-3.1.

Evidence: parent progress entry, including preserved endpoint/caret observations.
Handoff: exact mixed context or engine admission still unresolved.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-1.3 — Correlate IME confirmation across event boundaries

- [ ] PKI-1.3 Qualify and repair near-composition key ownership.

Purpose: Candidate confirmation produces one text commit without an accidental break, and a new deliberate Enter remains available.
Context: comparison R01; `input/composition.ts::handle/#dispatchBoundary`, `input/text.ts`, `input/keyboard.ts::action`, `modules/tables/current.ts` composition/keyboard handlers; existing `tests/browser/composition.spec.ts` commit-Enter cases.
Entry receipts: Applicable current-source ES/EDX and named comparison findings; authenticate required interfaces rather than replay completed work.
Dependencies: none.
Independent work: other PKI-1 parents. Cross-block staging stays with ES-1.4; this task uses a single existing text owner.
Session scope: one bounded lifecycle correction and reuse by the table boundary, 45 minutes; split if platform evidence demands a separate adapter change.
Acceptance: Delayed end-before-confirmation, key-before-end, missing keyup and 229/Dead/Process/Unidentified signals cannot be assumed to be ordinary Enter. Include 229 Backspace with `isComposing: false`: it must not reverse a typing rule or delete committed content when it belongs to candidate interaction. Pointer confirmation followed by deliberate Enter and repeated intentional Enter must not be swallowed. Define corroborating state and expiry rather than blanket time suppression. Table and root owners cannot double-commit final notifications.

Implementation:

- [ ] PKI-1.3-I1 Spend at most 10 minutes establishing a deterministic event trace and distinguishing existing passing cases from the missing order; record unsupported real-platform claims explicitly.
- [ ] PKI-1.3-I2 Add the smallest correlated ownership repair, or retain implementation with exact counter-evidence if the risky sequence is already safely handled; keep real target-runtime qualification open.

Validation:

- [ ] PKI-1.3-V1 Replay the failing prepared sequence and a deliberately independent Enter control against current source; run the affected existing composition selector only. Budget: 4 minutes; broader/real-runtime coverage belongs to PKI-3.3 and existing MWB/43 owners.

Evidence: parent progress entry with event ordering and synthetic/OS provenance.
Handoff: exact missing native trace or remaining event order, never a generic IME-support claim.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-1.4 — Route native structural Enter through one prepared command

- [ ] PKI-1.4 Handle supported mobile and targetless Enter sequences once.

Purpose: An Enter delivered through native input does not disappear into unsupported-structure recovery or create a duplicate split.
Context: comparison R02; `input/text.ts` action/native jobs, `input/reconcile.ts::reconcileMutation`, `input/protocol.ts`; `specs/web.md` Input routing/Composition gate; `specs/mobile-web.md` keyboard input; EDX-1.4 break semantics.
Dependencies: none.
Independent work: other PKI-1 parents.
Entry receipts: existing EDX current-format/break commands must be usable; record their exact focused receipt, not a blanket release gate.
Session scope: one bounded recognized native Enter shape and its fallback, 45 minutes; any additional unrelated browser shape gets a controller split.
Acceptance: Keydown absent, noncancelable beforeinput or native paragraph/BR creation yields exactly one applicable split/break with preserved suffix and caret. Correlate later notifications. Unrecognized/multi-owner input retains recovery and performs no guessed mutation. IME precedence is preserved; device/browser sniffing alone is insufficient evidence.

Implementation:

- [ ] PKI-1.4-I1 Capture the missing native event/DOM shape in the existing fixture, compare with a normal Enter and document the bounded admission rule.
- [ ] PKI-1.4-I2 Route admitted intent through existing semantic commands and deduplication; leave unsupported shapes on explicit recovery.

Validation:

- [ ] PKI-1.4-V1 Run one recognized native-Enter sequence and one unsupported-shape negative control, checking text owners, selection, commit count and recovery. Budget: 4 minutes; final coverage owner PKI-3.3.

Evidence: parent progress entry with native-versus-prepared provenance.
Handoff: exact unsupported shape and which browser/runtime must supply changed evidence.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-1.5 — Resolve modified shortcuts across keyboard layouts safely

- [ ] PKI-1.5 Add a documented layout-aware shortcut fallback.

Purpose: Supported primary shortcuts remain usable when a layout produces a different character, without consuming AltGraph text or host commands.
Context: comparison R03; `input/keyboard.ts::action`, `commands/catalog.ts::shortcutCommand`; `specs/platform-editing-services.md` command ownership; ES-KEY-1.
Entry receipts: Applicable current-source ES/EDX and named comparison findings; authenticate required interfaces rather than replay completed work.
Dependencies: none.
Independent work: other PKI-1 parents.
Session scope: shortcut normalization/reservation boundary, 30–45 minutes including checks.
Acceptance: Specify event.key-first behavior and the supported modified-key fallback for non-Latin layouts and shifted punctuation. Explicit reservations/remaps win for all considered candidates. Ctrl+Alt/AltGraph, Dead/Process/229/composition and unsupported chords retain their owner. Ordinary printable input uses its authored characters. Do not override OS/browser shortcuts or advertise untested layouts as qualified.

Implementation:

- [ ] PKI-1.5-I1 Extend the existing shortcut profile documentation and normalize candidates in one place without introducing an unrelated global keymap.
- [ ] PKI-1.5-I2 Apply guarded fallback only to supported modified commands and expose accurate help labels.

Validation:

- [ ] PKI-1.5-V1 Probe a non-Latin Primary+Z, an explicit reservation and an AltGraph printable negative control; record resolved action and event ownership. Budget: 2 minutes; remaining layouts/shifted punctuation belong to PKI-3.1.

Evidence: parent progress entry, separating prepared events from actual OS layout use.
Handoff: remaining layout binding or host-policy ambiguity.

Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.
