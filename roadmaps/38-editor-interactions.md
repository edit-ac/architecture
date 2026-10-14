# Complete everyday typing and editing behavior

Status: IN_PROGRESS

Qualification amendment (user decision, 2026-10-14): Physical devices, named target-platform simulators/emulators and desktop OS VMs/test hosts are accepted for platform and release qualification under the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms). Missing physical hardware does not block completion. Execute required behavior against the implemented target-platform runtime; document and test virtual equivalents for unavailable hardware-only input/accessibility cases. Record physical versus virtual provenance and measure performance in the tested environment. This supersedes earlier physical-only or manual-only clauses below; it does not complete unchecked tasks or waive implementation, correctness, security or artifact gates.

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Read [editor interactions](../specs/editor-interactions.md), the active task's rows in the [case catalog](../tests/editor-interaction-cases.md), and its named paths. Paths are relative to `core` unless prefixed `../architecture/`. Planned implementation files and commands are created by their owner. This roadmap extends existing behavior; it does not claim a shipped browser editor.

Upstream entry gates: `04-browser-input.md`, `05-markdown-content.md`, `07-extension-modules.md` and `42-editing-regression-suite.md` complete at reviewed current source/implementation revisions with passing evidence. Baseline tasks remain responsible for basic input; this track closes concrete context and regression gaps. A missing engine primitive needs a qualified upstream schema/command change before its dependent task. Roadmap 10 requires this track; the optional assistance extension is separate in 39.

Keep the [baseline guarantees](../specs/web.md#baseline-typing-and-rendering-guarantees) and `npm run check:browser-baseline` passing while extending BRK/SPC variants. INT-1.2 and INT-1.8 inherit the permanent heading-before-list and visible-whitespace regressions. Restore, additional Unicode, selection and platform variants remain explicitly qualified by their owning cases.

## Execution rules

The controller owns this source; workers write progress and evidence separately. Implement at most one parent per iteration, normally 15–45 minutes plus validation. If a boundary outgrows that limit, propose a controller split rather than weaken acceptance. Local Dependencies refer only to this file. Create named checks before running them and ensure filters match nonzero intended cases. Record exact commands, executed/passed/failed/skipped counts, revisions and fixture hashes; preserve failures. All automated input/provider cases use deterministic prepared fixtures and mocked external transports, with real engine/adapters. No paid inference, `.secrets`, automatic fixture recording or background runner launch is authorized. Actual OS/AT qualification is a separately recorded manual workflow.

## Epic INT-1 — Complete everyday typing and editing behavior

### Task INT-1.1 — Verify interaction prerequisites and create the case index

- [ ] INT-1.1 Verify interaction prerequisites and create the case index.

Purpose: Verify interaction prerequisites and create the case index as one bounded behavior and regression boundary.
Context: `tests/interaction-fixtures/`; `tests/browser/interaction-harness.ts`; [behavior contract](../specs/editor-interactions.md); [case catalog](../tests/editor-interaction-cases.md). [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: none.
Session scope: One named behavior group plus its focused validation; change only named paths and directly required test/configuration glue.
Acceptance: Every catalog ID maps to a real-engine fixture owner and expected semantic/selection state. Current engine and storage/browser/format/module evidence is verified; unsupported structural primitives block affected tasks instead of being emulated in DOM. Index desktop cases by owning task and supported profile; distinguish semantic, browser-replay and physical or virtual platform evidence.

Implementation:

- [ ] INT-1.1-I1 Reuse the RGS shared real-engine driver and fixture/receipt contract; create the test:interactions group wrapper, stable case-ID bindings and feature-specific expected-state helpers for model, marks, directional selection, mutation count and history; use a mounted real adapter with mocked external transports only. Audit baseline overlap so existing passing tests are reused.

Validation:

- [ ] INT-1.1-V1 npm run test:interactions -- --group harness. The harness must fail for a wrong expected snapshot, duplicate/missing case ID or absent real engine; record that mutation/failure probe. Record nonzero executed/passed/failed/skipped counts; missing tests and zero matches fail acceptance.

Evidence: Progress entry `INT-1.1` with case IDs, source/implementation/fixture revisions, exact commands/counts and preserved artifacts under `../architecture/evidence/editor-interactions/`.
Handoff: Record the last finished substep, changed paths/symbols, failing case or missing capability and next bounded action for `INT-1.1`.
Blocked behavior: Leave `INT-1.1` unchecked with the owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task INT-1.2 — Implement paragraph splits and same-block hard breaks

- [ ] INT-1.2 Implement paragraph splits and same-block hard breaks.

Purpose: Implement paragraph splits and same-block hard breaks as one bounded behavior and regression boundary.
Context: `crates/editac-core/src/commands/`; `packages/web/src/input/keyboard.ts`; `tests/browser/interactions/breaks.spec.ts`; [behavior contract](../specs/editor-interactions.md); [case catalog](../tests/editor-interaction-cases.md).
Dependencies: INT-1.1.
Session scope: One named behavior group plus its focused validation; change only named paths and directly required test/configuration glue.
Acceptance: BRK-01–BRK-08 pass: Enter versus Shift+Enter, selected replacement, list/heading/quote transitions, literal code and in-cell breaks preserve caret and semantic undo. A next typed sentinel lands in the intended block. SEL-01–SEL-04 deepen BRK-04 with backward, cross-block, whole-document and incompatible structural selections; assert independent selected Enter/hard-break snapshots and atomic rejection.

Implementation:

- [ ] INT-1.2-I1 Reuse qualified engine split/replace/break primitives; add only missing context routing and prepared semantic behavior. Qualify any hard-break schema/codec gap through the engine's schema-evolution gate first; preserve authored trailing breaks and distinguish renderer fillers.

Validation:

- [ ] INT-1.2-V1 npm run test:interactions -- --group breaks. Run the applicable Rust command/codec fixtures as well as the browser cases; round-trip hard breaks through storage and Markdown. Record nonzero executed/passed/failed/skipped counts; missing tests and zero matches fail acceptance.

Evidence: Progress entry `INT-1.2` with case IDs, source/implementation/fixture revisions, exact commands/counts and preserved artifacts under `../architecture/evidence/editor-interactions/`.
Handoff: Record the last finished substep, changed paths/symbols, failing case or missing capability and next bounded action for `INT-1.2`.
Blocked behavior: Leave `INT-1.2` unchecked with the owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task INT-1.3 — Preserve selection and typing marks across formatting actions

- [ ] INT-1.3 Preserve selection and typing marks across formatting actions.

Purpose: Preserve selection and typing marks across formatting actions as one bounded behavior and regression boundary.
Context: `crates/editac-core/src/commands/`; `packages/web/src/commands/`; `tests/browser/interactions/formatting.spec.ts`; [behavior contract](../specs/editor-interactions.md); [case catalog](../tests/editor-interaction-cases.md).
Dependencies: INT-1.2.
Session scope: One named behavior group plus its focused validation; change only named paths and directly required test/configuration glue.
Acceptance: MRK-01–MRK-09 pass for collapsed, forward/backward and cross-block mixed selections. Toolbar focus does not lose the target; pending marks create no empty content; links/custom marks and serialization policy are explicit.

Implementation:

- [ ] INT-1.3-I1 Implement selection capture/revalidation, on/off/mixed/disabled toolbar state, pending local marks, clear-formatting scope and link boundary policy. Route toolbar and key commands through the same semantic applicability path.

Validation:

- [ ] INT-1.3-V1 npm run test:interactions -- --group formatting. Assert exact mark spans, directional selection, subsequent typing, undo, stale-target rejection and unsupported-format diagnostics. Record nonzero executed/passed/failed/skipped counts; missing tests and zero matches fail acceptance.

Evidence: Progress entry `INT-1.3` with case IDs, source/implementation/fixture revisions, exact commands/counts and preserved artifacts under `../architecture/evidence/editor-interactions/`.
Handoff: Record the last finished substep, changed paths/symbols, failing case or missing capability and next bounded action for `INT-1.3`.
Blocked behavior: Leave `INT-1.3` unchecked with the owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task INT-1.4 — Complete grapheme and structural deletion

- [ ] INT-1.4 Complete grapheme and structural deletion.

Purpose: Complete grapheme and structural deletion as one bounded behavior and regression boundary.
Context: `crates/editac-core/src/commands/`; `crates/editac-core/src/anchors.rs`; `tests/browser/interactions/deletion.spec.ts`; [behavior contract](../specs/editor-interactions.md); [case catalog](../tests/editor-interaction-cases.md).
Dependencies: INT-1.2.
Session scope: One named behavior group plus its focused validation; change only named paths and directly required test/configuration glue.
Acceptance: DEL-01–DEL-08 pass with exact retained text/marks. Grapheme/word/line deletion, cross-block selection, atom selection-before-deletion and document-boundary no-ops preserve valid UTF-16 and history.

Implementation:

- [ ] INT-1.4-I1 Reuse grapheme and prepared range deletion helpers; implement missing boundary applicability in adapters and shared structural commands. Native word/line ranges follow named platform profiles rather than repeated code-unit deletes.

Validation:

- [ ] INT-1.4-V1 npm run test:interactions -- --group deletion. Run shared Rust/WASM deletion vectors; assert rejected joins and boundary no-ops produce zero mutation and zero history entries. Record nonzero executed/passed/failed/skipped counts; missing tests and zero matches fail acceptance.

Evidence: Progress entry `INT-1.4` with case IDs, source/implementation/fixture revisions, exact commands/counts and preserved artifacts under `../architecture/evidence/editor-interactions/`.
Handoff: Record the last finished substep, changed paths/symbols, failing case or missing capability and next bounded action for `INT-1.4`.
Blocked behavior: Leave `INT-1.4` unchecked with the owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task INT-1.5 — Preserve visual navigation and directional selections

- [ ] INT-1.5 Preserve visual navigation and directional selections.

Purpose: Preserve visual navigation and directional selections as one bounded behavior and regression boundary.
Context: `packages/web/src/dom/selection.ts`; `packages/web/src/input/keyboard.ts`; `tests/browser/interactions/navigation.spec.ts`; [behavior contract](../specs/editor-interactions.md); [case catalog](../tests/editor-interaction-cases.md).
Dependencies: INT-1.2.
Session scope: One named behavior group plus its focused validation; change only named paths and directly required test/configuration glue.
Acceptance: NAV-01–NAV-07 pass: Shift+arrows, platform movement, wrapped lines, bidi, atoms, empty blocks, pointer selection and remote patches retain valid caret/selection without content transactions.

Implementation:

- [ ] INT-1.5-I1 Keep correct browser visual movement native; repair DOM/core mapping, selection collapse/extension, preferred vertical position and scroll-to-caret only where evidence requires it. Scope Select All and event ownership to the active editor.

Validation:

- [ ] INT-1.5-V1 npm run test:interactions -- --group navigation. Record exact browser/OS/layout; assert selection anchor/focus/direction/affinity and zero mutation. Device bidi/touch rows remain pending until INT-1.14. Record nonzero executed/passed/failed/skipped counts; missing tests and zero matches fail acceptance.

Evidence: Progress entry `INT-1.5` with case IDs, source/implementation/fixture revisions, exact commands/counts and preserved artifacts under `../architecture/evidence/editor-interactions/`.
Handoff: Record the last finished substep, changed paths/symbols, failing case or missing capability and next bounded action for `INT-1.5`.
Blocked behavior: Leave `INT-1.5` unchecked with the owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task INT-1.6 — Implement contextual Tab and platform shortcuts

- [ ] INT-1.6 Implement contextual Tab and platform shortcuts.

Purpose: Implement contextual Tab and platform shortcuts as one bounded behavior and regression boundary.
Context: `packages/web/src/input/keyboard.ts`; `packages/web/src/commands/`; `tests/browser/interactions/keyboard.spec.ts`; [behavior contract](../specs/editor-interactions.md); [case catalog](../tests/editor-interaction-cases.md).
Dependencies: INT-1.5.
Session scope: One named behavior group plus its focused validation; change only named paths and directly required test/configuration glue.
Acceptance: KEY-01–KEY-07 pass for prose focus traversal, list indentation, literal code indentation, table-cell navigation, keyboard escape and default shortcut/toolbar parity. Modifier handling permits AltGraph/dead keys and preserves browser/OS commands.

Implementation:

- [ ] INT-1.6-I1 Implement explicit context dispatch and accessible keyboard help. Bound table row creation and code dedent; provide Escape-then-Tab escape without intercepting IME or unrelated host controls.

Validation:

- [ ] INT-1.6-V1 npm run test:interactions -- --group keyboard. Test applicable/inapplicable command branches, key repeat, selection after indentation and actual focus destination; non-US/AT device proof remains separate. Record nonzero executed/passed/failed/skipped counts; missing tests and zero matches fail acceptance.

Evidence: Progress entry `INT-1.6` with case IDs, source/implementation/fixture revisions, exact commands/counts and preserved artifacts under `../architecture/evidence/editor-interactions/`.
Handoff: Record the last finished substep, changed paths/symbols, failing case or missing capability and next bounded action for `INT-1.6`.
Blocked behavior: Leave `INT-1.6` unchecked with the owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task INT-1.7 — Handle composition and non-keyboard replacement exactly once

- [ ] INT-1.7 Handle composition and non-keyboard replacement exactly once.

Purpose: Handle composition and non-keyboard replacement exactly once as one bounded behavior and regression boundary.
Context: `packages/web/src/input/`; `tests/browser/interactions/replacement.spec.ts`; [behavior contract](../specs/editor-interactions.md); [case catalog](../tests/editor-interaction-cases.md).
Dependencies: INT-1.3, INT-1.6.
Session scope: One named behavior group plus its focused validation; change only named paths and directly required test/configuration glue.
Acceptance: EVT-01–EVT-10 deterministic replays pass, including missing/noncancelable beforeinput, empty target ranges, IME ordering, dictation/correction, spellcheck, read-only and disposal. These passes do not establish real OS support.

Implementation:

- [ ] INT-1.7-I1 Extend bounded input reconciliation and composition ownership for observed event variants; capture stable replacement targets and suppress echo commits. Keep composing Enter ahead of popup/structural commands; route OS dictation through ordinary editing events.

Validation:

- [ ] INT-1.7-V1 npm run test:interactions -- --group replacement. Use prepared traces with stated provenance; assert content, marks, selection, commit count and history. Actual IME/voice/keyboard observations are required in INT-1.14. Record nonzero executed/passed/failed/skipped counts; missing tests and zero matches fail acceptance.

Evidence: Progress entry `INT-1.7` with case IDs, source/implementation/fixture revisions, exact commands/counts and preserved artifacts under `../architecture/evidence/editor-interactions/`.
Handoff: Record the last finished substep, changed paths/symbols, failing case or missing capability and next bounded action for `INT-1.7`.
Blocked behavior: Leave `INT-1.7` unchecked with the owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task INT-1.8 — Preserve authored whitespace and special characters

- [ ] INT-1.8 Preserve authored whitespace and special characters.

Purpose: Preserve authored whitespace and special characters as one bounded behavior and regression boundary.
Context: `packages/web/src/dom/`; `packages/web/src/input/`; `tests/browser/interactions/whitespace.spec.ts`; [behavior contract](../specs/editor-interactions.md); [case catalog](../tests/editor-interaction-cases.md).
Dependencies: INT-1.4, INT-1.7.
Session scope: One named behavior group plus its focused validation; change only named paths and directly required test/configuration glue.
Acceptance: SPC-01–SPC-05 pass across insert/render/copy/restore. Authored spaces and Unicode survive; browser placeholders do not become content; malformed encodings produce diagnostics before mutation.

Implementation:

- [ ] INT-1.8-I1 Separate renderer compensation from semantic characters, preserve NBSP/zero-width/bidi data, normalize literal line endings once and add optional display-only invisible-character diagnostics without changing stored text.

Validation:

- [ ] INT-1.8-V1 npm run test:interactions -- --group whitespace. Compare escaped code points and UTF-16 positions as well as rendered appearance; verify no unintended NFC/NFKC, trimming or tab expansion. Record nonzero executed/passed/failed/skipped counts; missing tests and zero matches fail acceptance.

Evidence: Progress entry `INT-1.8` with case IDs, source/implementation/fixture revisions, exact commands/counts and preserved artifacts under `../architecture/evidence/editor-interactions/`.
Handoff: Record the last finished substep, changed paths/symbols, failing case or missing capability and next bounded action for `INT-1.8`.
Blocked behavior: Leave `INT-1.8` unchecked with the owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task INT-1.9 — Complete slash-menu command and focus behavior

- [ ] INT-1.9 Complete slash-menu command and focus behavior.

Purpose: Complete slash-menu command and focus behavior as one bounded behavior and regression boundary.
Context: `packages/web/src/modules/slash/`; `tests/browser/interactions/slash.spec.ts`; [behavior contract](../specs/editor-interactions.md); [case catalog](../tests/editor-interaction-cases.md).
Dependencies: INT-1.5, INT-1.7.
Session scope: One named behavior group plus its focused validation; change only named paths and directly required test/configuration glue.
Acceptance: SLH-01–SLH-07 pass for local trigger exclusions, disabled/empty results, navigation/commit/dismissal, composing Enter, anchored async results, pointer parity and one-group undo.

Implementation:

- [ ] INT-1.9-I1 Extend the existing MOD-1.4 presenter rather than create a second menu. Implement the specified key table, selection/query lifetime and accessible result state. Keep catalog-scale performance owned by RCH-1.16.

Validation:

- [ ] INT-1.9-V1 npm run test:interactions -- --group slash. Exercise deterministic stale/reordered responses and all dismissal branches; verify query preservation, focus restoration and accessible active-result attributes. Record nonzero executed/passed/failed/skipped counts; missing tests and zero matches fail acceptance.

Evidence: Progress entry `INT-1.9` with case IDs, source/implementation/fixture revisions, exact commands/counts and preserved artifacts under `../architecture/evidence/editor-interactions/`.
Handoff: Record the last finished substep, changed paths/symbols, failing case or missing capability and next bounded action for `INT-1.9`.
Blocked behavior: Leave `INT-1.9` unchecked with the owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task INT-1.10 — Qualify clipboard precedence and literal paste fidelity

- [ ] INT-1.10 Qualify clipboard precedence and literal paste fidelity.

Purpose: Qualify clipboard precedence and literal paste fidelity as one bounded behavior and regression boundary.
Context: `packages/web/src/clipboard/`; `crates/editac-core/src/formats/`; `tests/browser/interactions/paste.spec.ts`; [behavior contract](../specs/editor-interactions.md); [case catalog](../tests/editor-interaction-cases.md).
Dependencies: INT-1.3, INT-1.8.
Session scope: One named behavior group plus its focused validation; change only named paths and directly required test/configuration glue.
Acceptance: PST-01–PST-07 pass for every flavor/fallback, prose/code/table context, external-app synthetic payloads, cut failure and delayed paste races. One paste is one semantic history group.

Implementation:

- [ ] INT-1.10-I1 Reuse the qualified format importer; add source-labeled synthetic HTML/text/TSV payloads, explicit literal command, whitespace-preserving insertion and clipboard failure recovery. Apply existing URL/resource policy before mutation.

Validation:

- [ ] INT-1.10-V1 npm run test:interactions -- --group paste. Verify semantic snapshots, original content on failed cut, zero network during import, cancellation and session/anchor revalidation; no private clipboard recordings. Record nonzero executed/passed/failed/skipped counts; missing tests and zero matches fail acceptance.

Evidence: Progress entry `INT-1.10` with case IDs, source/implementation/fixture revisions, exact commands/counts and preserved artifacts under `../architecture/evidence/editor-interactions/`.
Handoff: Record the last finished substep, changed paths/symbols, failing case or missing capability and next bounded action for `INT-1.10`.
Blocked behavior: Leave `INT-1.10` unchecked with the owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task INT-1.11 — Qualify local typing rules and alternative formatting syntax

- [ ] INT-1.11 Qualify local typing rules and alternative formatting syntax.

Purpose: Qualify local typing rules and alternative formatting syntax as one bounded behavior and regression boundary.
Context: `crates/editac-core/src/formats/`; `packages/web/src/input/shortcuts.ts`; `tests/browser/interactions/parsing.spec.ts`; [behavior contract](../specs/editor-interactions.md); [case catalog](../tests/editor-interaction-cases.md).
Dependencies: INT-1.3, INT-1.10.
Session scope: One named behavior group plus its focused validation; change only named paths and directly required test/configuration glue.
Acceptance: PAR-01–PAR-08 pass for pinned grammar, equivalent spellings, escaping, incomplete syntax, immediate Backspace reversal and literal/code/IME/paste/dictation/remote exclusions.

Implementation:

- [ ] INT-1.11-I1 Define the finite input-rule trigger table and its independent enablement policy. Reuse FMT parser fixtures and canonical export; preserve source/diagnostics for nonrepresentable alternate formatting rather than guessing or normalizing Unicode.

Validation:

- [ ] INT-1.11-V1 npm run test:interactions -- --group parsing. Run pinned CommonMark/GFM regression vectors plus browser triggers; assert exact source restoration for reversed rules and no extra conversion on nonlocal input. Record nonzero executed/passed/failed/skipped counts; missing tests and zero matches fail acceptance.

Evidence: Progress entry `INT-1.11` with case IDs, source/implementation/fixture revisions, exact commands/counts and preserved artifacts under `../architecture/evidence/editor-interactions/`.
Handoff: Record the last finished substep, changed paths/symbols, failing case or missing capability and next bounded action for `INT-1.11`.
Blocked behavior: Leave `INT-1.11` unchecked with the owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task INT-1.12 — Verify undo and command races across input paths

- [ ] INT-1.12 Verify undo and command races across input paths.

Purpose: Verify undo and command races across input paths as one bounded behavior and regression boundary.
Context: `tests/browser/interactions/history.spec.ts`; `packages/web/src/commands/`; `packages/web/src/input/`; [behavior contract](../specs/editor-interactions.md); [case catalog](../tests/editor-interaction-cases.md).
Dependencies: INT-1.4, INT-1.9, INT-1.10, INT-1.11.
Session scope: One named behavior group plus its focused validation; change only named paths and directly required test/configuration glue.
Acceptance: HIS-01–HIS-05 pass through keyboard/menu/toolbar paths. Remote edits survive local undo; canceled/read-only/stale/cross-session actions produce no content or history changes.

Implementation:

- [ ] INT-1.12-I1 Add integrated deterministic race cases around finalized composition, formatting, paste, slash and structural commands; repair command routing or explicit history boundaries where mismatches occur.

Validation:

- [ ] INT-1.12-V1 npm run test:interactions -- --group history. Assert resulting selection and document state after undo/redo, exact emitted updates, rejected-command atomicity and listener cleanup after two-editor disposal. Record nonzero executed/passed/failed/skipped counts; missing tests and zero matches fail acceptance.

Evidence: Progress entry `INT-1.12` with case IDs, source/implementation/fixture revisions, exact commands/counts and preserved artifacts under `../architecture/evidence/editor-interactions/`.
Handoff: Record the last finished substep, changed paths/symbols, failing case or missing capability and next bounded action for `INT-1.12`.
Blocked behavior: Leave `INT-1.12` unchecked with the owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task INT-1.13 — Verify accessible focus and editing presentation

- [ ] INT-1.13 Verify accessible focus and editing presentation.

Purpose: Verify accessible focus and editing presentation as one bounded behavior and regression boundary.
Context: `packages/web/src/`; `tests/browser/interactions/accessibility.spec.ts`; [behavior contract](../specs/editor-interactions.md); [case catalog](../tests/editor-interaction-cases.md).
Dependencies: INT-1.6, INT-1.9, INT-1.12.
Session scope: One named behavior group plus its focused validation; change only named paths and directly required test/configuration glue.
Acceptance: A11-01/A11-03 and the mechanical portion of A11-06 pass: keyboard route, visible focus, names/state, zoom/reflow, forced colors and extension-disabled baseline. Automated checks are explicitly not screen-reader qualification.

Implementation:

- [ ] INT-1.13-I1 Reuse semantic rendering and named commands; fix focus restoration, accessible toolbar/popup states and bounded status announcements. Apply baseline support without requiring the optional assistance extension.

Validation:

- [ ] INT-1.13-V1 npm run test:interactions -- --group accessibility. Combine role/name/state and actual keyboard/focus assertions with screenshots where layout matters; publish unresolved AT observations for INT-1.14. Record nonzero executed/passed/failed/skipped counts; missing tests and zero matches fail acceptance.

Evidence: Progress entry `INT-1.13` with case IDs, source/implementation/fixture revisions, exact commands/counts and preserved artifacts under `../architecture/evidence/editor-interactions/`.
Handoff: Record the last finished substep, changed paths/symbols, failing case or missing capability and next bounded action for `INT-1.13`.
Blocked behavior: Leave `INT-1.13` unchecked with the owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.

### Task INT-1.15 — Qualify pointer selection and context targets

- [ ] INT-1.15 Qualify pointer selection and context targets.

Purpose: Qualify pointer selection and context targets within the existing editor architecture.
Context: `packages/web/src/selection/`; `tests/browser/interactions/pointer-selection.spec.ts`; `../architecture/specs/editor-interactions.md`; [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: INT-1.1, INT-1.6.
Session scope: One named behavior boundary and focused validation; use the existing qualified primitives. If it exceeds one bounded iteration, record the remaining acceptance and obtain a controller split before implementation.
Acceptance: SEL-05–SEL-08 pass native-profile selection granularity, drag threshold, backward/bidi ranges, context menu targeting and bounded autoscroll through unmounted content.

Implementation:

- [ ] INT-1.15-I1 Reuse native selection/hit-test ports and stable anchors; add gesture arbitration and teardown without altering semantic selection ownership.

Validation:

- [ ] INT-1.15-V1 npm run test:interactions -- --group pointer-selection. Assert document/history remain unchanged, native range endpoints and cancellation/teardown. Record exact revisions, fixture IDs, commands and nonzero executed/passed/failed/skipped counts. Missing tests, zero matches and skipped required cases fail; retain failures and native/device limitations.

Evidence: Progress entry `INT-1.15` links immutable implementation/profile/fixture revisions and artifacts under `../architecture/evidence/desktop-interactions/`; source checkboxes remain templates.
Handoff: Record last completed substep, failing case/missing primitive, changed paths and next bounded action for `INT-1.15`.
Blocked behavior: Leave `INT-1.15` unchecked with owner, unblock condition and retry trigger; never replace missing qualified engine behavior with a DOM-only workaround.

### Task INT-1.16 — Move and copy selected text within a document

- [ ] INT-1.16 Move and copy selected text within a document.

Purpose: Move and copy selected text within a document within the existing editor architecture.
Context: `packages/web/src/input/`; `crates/editac-core/src/commands/`; `tests/browser/interactions/text-drag.spec.ts`; `../architecture/specs/editor-interactions.md`; [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: INT-1.15, INT-1.10, INT-1.12.
Session scope: One named behavior boundary and focused validation; use the existing qualified primitives. If it exceeds one bounded iteration, record the remaining acceptance and obtain a controller split before implementation.
Acceptance: MOV-01–MOV-10 pass atomic source/destination mapping, copy effects, self-drop no-op, retained fragments, remote-source validation and complete undo. Missing prepared move/selection support is an upstream engine qualification blocker.

Implementation:

- [ ] INT-1.16-I1 Qualify/reuse prepared move or compound primitives; connect adapter drag sessions to explicit command targets and observed event correlation, preserving view-local state.

Validation:

- [ ] INT-1.16-V1 npm run test:interactions -- --group text-drag. Include rejection at final preparation, real browser gestures and independent source/destination/history snapshots. Record exact revisions, fixture IDs, commands and nonzero executed/passed/failed/skipped counts. Missing tests, zero matches and skipped required cases fail; retain failures and native/device limitations.

Evidence: Progress entry `INT-1.16` links immutable implementation/profile/fixture revisions and artifacts under `../architecture/evidence/desktop-interactions/`; source checkboxes remain templates.
Handoff: Record last completed substep, failing case/missing primitive, changed paths and next bounded action for `INT-1.16`.
Blocked behavior: Leave `INT-1.16` unchecked with owner, unblock condition and retry trigger; never replace missing qualified engine behavior with a DOM-only workaround.

### Task INT-1.17 — Qualify cross-document and external text transfers

- [ ] INT-1.17 Qualify cross-document and external text transfers.

Purpose: Qualify cross-document and external text transfers within the existing editor architecture.
Context: `packages/web/src/input/`; `tests/browser/interactions/text-transfer.spec.ts`; `../architecture/specs/editor-interactions.md`; [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: INT-1.16.
Session scope: One named behavior boundary and focused validation; use the existing qualified primitives. If it exceeds one bounded iteration, record the remaining acceptance and obtain a controller split before implementation.
Acceptance: XFR-01–XFR-07 pass copy-by-default, untrusted import, asynchronous target lifetime and source preservation. Host move is advertised only with qualified destination receipts/source validation/recovery; unqualified moves remain unavailable.

Implementation:

- [ ] INT-1.17-I1 Reuse clipboard/import and existing receipt/session ports. Implement bounded transfer staging and explicit fallback; do not introduce an unneeded distributed transaction service.

Validation:

- [ ] INT-1.17-V1 npm run test:interactions -- --group text-transfer. Inject destination/source failure, stale callbacks and forged payloads; qualify browser/OS effects separately from synthetic replay. Record exact revisions, fixture IDs, commands and nonzero executed/passed/failed/skipped counts. Missing tests, zero matches and skipped required cases fail; retain failures and native/device limitations.

Evidence: Progress entry `INT-1.17` links immutable implementation/profile/fixture revisions and artifacts under `../architecture/evidence/desktop-interactions/`; source checkboxes remain templates.
Handoff: Record last completed substep, failing case/missing primitive, changed paths and next bounded action for `INT-1.17`.
Blocked behavior: Leave `INT-1.17` unchecked with owner, unblock condition and retry trigger; never replace missing qualified engine behavior with a DOM-only workaround.

### Task INT-1.18 — Unify editing command surfaces and replacement targets

- [ ] INT-1.18 Unify editing command surfaces and replacement targets.

Purpose: Unify editing command surfaces and replacement targets within the existing editor architecture.
Context: `packages/web/src/commands/`; `tests/browser/interactions/command-surfaces.spec.ts`; `../architecture/specs/editor-interactions.md`; [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: INT-1.13, INT-1.15.
Session scope: One named behavior boundary and focused validation; use the existing qualified primitives. If it exceeds one bounded iteration, record the remaining acceptance and obtain a controller split before implementation.
Acceptance: CMD-01–CMD-06 pass focused-editor routing, menu/toolbar/accessibility equivalence, supplied replacement ranges and late permission changes; host and native controls retain ownership.

Implementation:

- [ ] INT-1.18-I1 Reuse the command registry and captured semantic targets for platform/context actions; expose applicability and shortcut profiles without adding a second command system.

Validation:

- [ ] INT-1.18-V1 npm run test:interactions -- --group command-surfaces. Exercise two editors, nested controls, stale ranges, canceled menus and actual OS replacement observations. Record exact revisions, fixture IDs, commands and nonzero executed/passed/failed/skipped counts. Missing tests, zero matches and skipped required cases fail; retain failures and native/device limitations.

Evidence: Progress entry `INT-1.18` links immutable implementation/profile/fixture revisions and artifacts under `../architecture/evidence/desktop-interactions/`; source checkboxes remain templates.
Handoff: Record last completed substep, failing case/missing primitive, changed paths and next bounded action for `INT-1.18`.
Blocked behavior: Leave `INT-1.18` unchecked with owner, unblock condition and retry trigger; never replace missing qualified engine behavior with a DOM-only workaround.

### Task INT-1.14 — Qualify actual typing and assistive-technology support

- [ ] INT-1.14 Qualify actual typing and assistive-technology support.

Purpose: Qualify actual typing and assistive-technology support as one bounded behavior and regression boundary.
Context: `tests/browser/interactions/`; `../architecture/evidence/editor-interactions/`; `../architecture/specs/verification.md`; [behavior contract](../specs/editor-interactions.md); [case catalog](../tests/editor-interaction-cases.md).
Dependencies: INT-1.12, INT-1.13, INT-1.17, INT-1.18.
Session scope: One named behavior group plus its focused validation; change only named paths and directly required test/configuration glue.
Acceptance: Every mandatory catalog case has passing exact-revision evidence across the declared browser/device matrix. IME, native dictation/correction, screen-reader editing, voice control and non-US layouts have physical or target-platform virtual observations or tested hardware-only equivalents under verification.md; record their limitations and untested combinations explicitly. Include the owned SEL/MOV/XFR/CMD variants and mandatory platform gesture/OS-command observations from the additional catalog. Optional rich tools remain owned by track 25.

Implementation:

- [ ] INT-1.14-I1 Run browser integration and actual device protocols for the named catalog rows; record browser/OS/keyboard/locale/AT versions and minimize failures. Reconcile baseline platform capability records and hand off the reviewed supported envelope to REL-1.1.

Validation:

- [ ] INT-1.14-V1 npm run test:interactions -- --group all. Record per-ID and per-platform executed/passed/failed/skipped counts, device steps and observations, revisions/hashes and logs. No missing suite, skipped mandatory row, synthetic-only IME proof or paid provider probe can pass. Record nonzero executed/passed/failed/skipped counts; missing tests and zero matches fail acceptance.

Evidence: Progress entry `INT-1.14` with case IDs, source/implementation/fixture revisions, exact commands/counts and preserved artifacts under `../architecture/evidence/editor-interactions/`.
Handoff: Record the last finished substep, changed paths/symbols, failing case or missing capability and next bounded action for `INT-1.14`.
Blocked behavior: Leave `INT-1.14` unchecked with the owner, unblock condition and retry trigger; continue only dependency-ready work and stop when none remains.
