# Targeted editing regression cases

Wordcraft refinement (2026-10-16): selected existing IDs below include additional variants; [provenance and overlap](../evidence/wordcraft-research.md) distinguish them from the new WCF cases. Previous case evidence does not qualify added variants.

Qualification amendment (user decision, 2026-10-14): Named target-platform simulators/emulators and desktop OS VMs/test hosts may satisfy platform and release gates when physical hardware is unavailable. Follow the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms) for required runtime checks, tested virtual equivalents for hardware-only observations, counts and physical/virtual provenance. Earlier physical-only/manual-only wording in this document is superseded. This changes accepted evidence, not required implementation or correctness.

Status: planned executable coverage, not test results. The owning task creates the fixture and assertions. Expected behavior comes from [editor-interactions](../specs/editor-interactions.md); citations and issue scope live in [research](../evidence/editor-interaction-research.md) and [assistive research](../evidence/assistive-input-research.md).

## Fixture protocol

`|` denotes a collapsed caret; `[text]` denotes a selected range and is not literal content. `↵` denotes a semantic hard break, `¶` a block boundary. Record real text as escaped Unicode plus readable labels to distinguish spaces, NBSP, LF and code units. Record selection endpoints, direction and affinity separately; run every selection case forward and backward. Each row becomes one or more executable cases with the stable ID in the test title.

Use a small shared semantic seed, a real engine instance and a real mounted adapter. Assertions cover resulting blocks/text/marks, UTF-16 selection, DOM mapping, mutation count and undo/redo. Mock only external transports and observed platform event sequences. An array of expected answers is not an implementation test. Navigation, cancellation, invalid commands and read-only input produce zero content changes. Every editor command must be exercised through its relevant user entry point, including toolbar focus loss. The matrix is a bounded minimum; add minimized cases when failures emerge.

Priorities: **P0** prevents data loss, broken basic input or inaccessible operation; **P1** covers context fidelity and interoperability. `browser` means pinned Chromium/Firefox/WebKit mechanics; `device` requires an actual OS/browser/keyboard/assistive-tool version and a reproducible manual sequence. Event replays cannot satisfy device rows.

## Breaks and block structure — INT-1.2

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| BRK-01 | P0 | Paragraph `ab|cd`; Enter; type `X` | `ab¶Xcd`; caret after X in new block, one split transaction |
| BRK-02 | P0 | Paragraph `ab|cd`; Shift+Enter; type X | `ab↵Xcd` in one block; caret follows break; no paragraph split |
| BRK-03 | P0 | Empty paragraph and `abc|`; repeated Shift+Enter | Authored empty lines/trailing breaks persist across render, export and restore; filler not serialized |
| BRK-04 | P0 | `a[bc]d`; Enter and Shift+Enter separately | Selected text replaced and split/break committed atomically; undo restores text and selection |
| BRK-05 | P1 | Heading at middle/end/empty; Enter, including end immediately before a list with/without trailing spaces | Middle retains heading level; end/empty transitions match specified paragraph policy; next typed sentinel enters the new paragraph before the unchanged list; undo/redo restore content; G07 separately qualifies stored-selection restoration |
| BRK-06 | P1 | Nested nonempty/empty list or checked task; Enter/Shift+Enter | Continue/split, reset new task checked state, outdent/exit empty item, or same-item break as appropriate |
| BRK-07 | P1 | Quote nonempty/empty final paragraph; Enter | Split within quote or exit one quote level without losing siblings |
| BRK-08 | P0 | Code and table cell; Enter/Shift+Enter | Code inserts LF; cell inserts hard break without splitting table or parsing Markdown |

## Formatting and toolbar selection — INT-1.3

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| MRK-01 | P0 | Select `bc` in `abcd`, click toolbar Bold | Exactly bc bold; selection retained despite toolbar focus; one undo restores original marks |
| MRK-02 | P0 | Backward multi-block mixed-bold selection; toggle twice | First makes full eligible range bold, second removes bold; other marks and direction preserved |
| MRK-03 | P0 | Collapsed caret; toggle Bold, move caret, type | Toggle creates no empty node/history entry; move recomputes typing marks; insertion uses destination state |
| MRK-04 | P1 | Bold+italic at caret; Shift+Enter then type | Applicable marks survive break; no accidental empty span or discarded formatting |
| MRK-05 | P1 | Type inside link, at end of link and beside inline code | Interior link retained; end-of-link typing outside; literal code and exclusions match policy |
| MRK-06 | P1 | Clear formatting across link/custom mark and heading | Remove supported presentation marks only; preserve link/custom data/text/block kind |
| MRK-07 | P0 | Open link toolbar then remote-delete captured range | Typed recoverable conflict; no formatting at current unrelated caret |
| MRK-08 | P1 | Underline/color/custom mark unsupported by Markdown exporter | Preserve via declared format or explicit loss diagnostic; no Unicode lookalike substitution |
| MRK-09 | P1 | Bold/italic caret; Enter then type, versus leave/revisit empty destination then type | Immediate typing inherits allowed marks; revisiting recomputes destination marks with no hidden persisted defaults |

## Deletion and Unicode — INT-1.4

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| DEL-01 | P0 | `1a|`; Backspace; ArrowLeft in separate fixture | Delete/move one intended character; do not treat digit+letter as one grapheme |
| DEL-02 | P0 | `e\u0301`, astral emoji, skin tone, family ZWJ, flag, variation selector, Indic cluster | Backspace/Delete cover qualified graphemes at start/middle/end; no split surrogate/cluster |
| DEL-03 | P0 | Selection crosses marked text, blocks and inline atom; delete | Only selected semantics removed, retained prefix/suffix joined by prepared policy, undo restores IDs/marks |
| DEL-04 | P0 | Backspace at block start; Delete at prior block end | Valid join preserves content/marks/caret; unsupported join has no partial mutation |
| DEL-05 | P1 | At nested list/quote boundary; Backspace | Outdent/exit policy works before inappropriate structural joining |
| DEL-06 | P0 | Adjacent noneditable atom; Backspace/Delete twice | First selects atom, second deletes once; preselected atom deletes immediately |
| DEL-07 | P0 | Start/end of entire document; deletion and key repeat | Boundary no-op, no empty history; repeats never remove unselected neighboring content |
| DEL-08 | P1 | Platform word/line delete in punctuation, whitespace and RTL | Native profile range mapped correctly; one semantic deletion and undo |

## Selection and movement — INT-1.5

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| NAV-01 | P0 | Shift+Left/Right then Shift+Up/Down across blocks | Anchor fixed, focus moves in correct direction, no content transaction |
| NAV-02 | P1 | Wrapped long paragraph; vertical arrows/Home/End/PageUp/Down | Visual line navigation and preferred x preserved; caret visible without jumping to document start |
| NAV-03 | P0 | Platform word/line/document modifiers with and without Shift | Correct platform movement/extension; no blanket capture of browser/OS shortcuts |
| NAV-04 | P0 | Select All then replace/copy; editor has atoms and multiple roots on page | Selection scoped to focused editor; full document retained in copy; other editor untouched |
| NAV-05 | P1 | Hebrew/Arabic + Latin/numbers/punctuation, including RTL heading | Visual left/right and selections follow qualified platform behavior; logical text unchanged |
| NAV-06 | P0 | Pointer/touch caret in empty block, after hard break, near atom | DOM-to-core and round-trip caret mapping correct; no hidden placeholder offset |
| NAV-07 | P0 | Remote edit before caret / unrelated block rerender | Anchored selection remains valid; no focus theft or full subtree replacement |

## Tab and shortcut dispatch — INT-1.6

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| KEY-01 | P0 | Ordinary prose; Tab and Shift+Tab | Focus moves to next/previous control; no literal tab and no keyboard trap |
| KEY-02 | P1 | List selection; Tab/Shift+Tab including first item and nesting bound | Applicable indent/outdent once; invalid action does not mutate or swallow focus escape |
| KEY-03 | P1 | Code single caret / multi-line selection; Tab then Shift+Tab | Tab/indent and bounded dedent preserve authored whitespace and selection |
| KEY-04 | P1 | Table interior/last/first cell; Tab/Shift+Tab | Move cells; append at most one allowed row at last; backward first and bounded last can exit |
| KEY-05 | P0 | Code/list/table with popup open/closed; Escape then Tab or Shift+Tab | Popup dismissal arms one-shot forward/backward exit; other editing clears it; IME Escape remains native; focus/help visible |
| KEY-06 | P0 | Hungarian/AltGraph/dead-key/non-US layout; Ctrl/Cmd editing shortcuts Include Right Alt versus Left Alt with menus/keytips active on the claimed Linux/Wayland profile. | Characters insert correctly; browser find/zoom and OS/AT shortcuts remain available AltGr characters never enter menu navigation or duplicate a command; preserve the host modifier profile. |
| KEY-07 | P0 | Default Primary+B/I/K/Z/Shift+Z/A/C/X/V, Windows Control+Y, optional U and host submit | Each applicable shortcut matches toolbar/menu semantic behavior; unsupported bindings remain native, input is committed once, ordinary Enter does not submit |

## Composition and replacement input — INT-1.7

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| EVT-01 | P0 | Same edit through cancelable beforeinput vs native input/observer echo | Equivalent model/selection, exactly one commit, no duplicate observer commit |
| EVT-02 | P0 | Noncancelable or absent beforeinput, empty target ranges, replacement text | Bounded input/DOM fallback reconciles real affected range; original text not duplicated |
| EVT-03 | P0 | Japanese/Korean/Chinese composition; Enter while slash visible Compose in the middle of existing text and inspect the candidate/composing range geometry. | IME confirms candidate; no command acceptance or extra block until distinct committed intent Interim composition remains legible without overlapping the untouched suffix; layout observation accompanies final semantic assertions. |
| EVT-04 | P0 | Interim composition, final input before/after compositionend, compositionend before final Enter with isComposing=false | One finalized semantic result and undo boundary; commit Enter does not split/accept popup, next deliberate Enter works |
| EVT-05 | P0 | Tab in code or existing literal tab then Korean IME (including Safari device row) | Caret/input stay responsive and composing span is not replaced; no freeze |
| EVT-06 | P0 | Native dictation insertion, selected phrase correction and punctuation; no keydown | Correct insert/replace and mark inheritance, one committed result; no assumed dictation inputType |
| EVT-07 | P0 | Autocorrect/spellcheck, handwriting or virtual keyboard replaces marked text | Correct target and retained permitted marks; undo returns original phrase |
| EVT-08 | P0 | Blur/read-only/destroy/paste/undo or target deletion during composition | Explicit cancellation/conflict policy; recover text, no stale mutation or lost committed text |
| EVT-09 | P0 | Identical insertText from eligible direct typing and unclassified/no-keydown input | Ordinary insertion in both; shortcuts/slash open only with positively qualified eligibility, no synthetic dictation tag assumption |
| EVT-10 | P0 | Compose in bold text then click plain paragraph before confirmation and type | Qualified finalize/cancel policy preserves text; subsequent plain paragraph typing has no stale bold mark |

## Whitespace and special characters — INT-1.8

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| SPC-01 | P0 | Type/paste leading, trailing and repeated U+0020; reopen document | Exact authored spacing retained; browser NBSP compensation does not leak into semantic text |
| SPC-02 | P1 | Literal NBSP, narrow NBSP, tabs and zero-width spaces | Distinct characters survive copy, undo and supported export; no trim/collapse |
| SPC-03 | P0 | CRLF/CR/LF literal paste including blank final lines | Normalize line endings once; preserve count and same-block hard-break/code LF policy |
| SPC-04 | P1 | Precomposed/decomposed accents, bidi isolates and directional marks | Preserve code points; optional invisible-character display changes no content |
| SPC-05 | P0 | Malformed UTF-16 and disallowed control payloads | Typed rejection/diagnostic before mutation, recoverable source, never replacement by silent truncation |

## Slash menu — INT-1.9

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| SLH-01 | P0 | Type slash at start/after space vs URL/path/escaped slash/code/link target | Open only valid local typed context; literal excluded contexts unchanged |
| SLH-02 | P0 | Paste/import/remote-replay slash; composition intermediate slash | Never auto-open menu |
| SLH-03 | P0 | Up/Down/Home/End across disabled and zero-result entries; Enter | Only enabled active result commits once; no result cannot mutate |
| SLH-04 | P0 | Escape; Tab; Shift+Enter in menu | Escape preserves query, Tab dismisses and follows context, Shift+Enter inserts same-block break |
| SLH-05 | P1 | Backspace query/trigger; move caret out; blur/read-only/destroy | Update/dismiss as specified, no focus theft or lingering active-descendant reference |
| SLH-06 | P0 | Reordered async query responses and remote deletion of trigger | Stale response ignored; only current valid anchor can commit; failure preserves literal query |
| SLH-07 | P0 | Pointerdown → editor blur → item click, internal AT focus transition, or keyboard activation | Composite focus preserves valid activation; external focus dismisses; same semantic result/selection and one undo; clear name/state/result announcement |

## Paste formats and failure paths — INT-1.10

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| PST-01 | P0 | Fragment + Markdown + HTML + plain flavors together | Existing documented precedence; invalid/unknown fragment falls back safely with diagnostic |
| PST-02 | P0 | Paste Markdown normally and via visible literal action into prose/code/cell | Host policy honored; literal/code paths do not format, cell literal paste does not add rows |
| PST-03 | P1 | Synthetic Word/Google Docs/Notes HTML, PDF/terminal text, TSV Add multiline plain paste midway through a styled RTL paragraph, retaining prefix/suffix. | Safe supported semantics or explicit fidelity fallback; whitespace/list/table policy stated Declare destination paragraph/mark inheritance for every new paragraph within admitted properties and the platform bidi policy; preserve the untouched suffix without accidental default-direction reset. |
| PST-04 | P0 | HTML handlers/scripts, encoded unsafe URL, deep nesting and oversized fragments | Inert bounded preparation, no execution/fetch, atomic reject or declared safe fallback |
| PST-05 | P0 | Cross-block selected paste/cut, clipboard failure or denial | Success one transaction and undo; failed cut retains original document |
| PST-06 | P0 | Cancel delayed paste; edit/move selection/delete target/switch editor meanwhile | Cancel zero mutation, stale target rejected, valid result uses original anchors without moving later caret |
| PST-07 | P1 | Internal copy with hard breaks, atom, unknown mark and backward selection | Supported semantics and unknown bounded data preserved on round-trip |

## Parsing and typing rules — INT-1.11

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| PAR-01 | P1 | Asterisks/underscores, setext/ATX headings, fence lengths/languages, ordered delimiters | Equivalent declared CommonMark semantics; canonical output reparses consistently |
| PAR-02 | P0 | Escaped/unmatched delimiters, intraword underscores, nested marks and code spans | Partial syntax stays literal; valid nesting follows pinned grammar; code excluded |
| PAR-03 | P1 | List/quote/heading typing triggers and immediate Backspace | Exact local trigger converts; Backspace reverses conversion without losing typed source |
| PAR-04 | P0 | Same trigger in paste/dictation/replacement/remote replay/IME/read-only | No local typing shortcut; separate paste importer follows its own policy |
| PAR-05 | P1 | URL/email followed by Unicode punctuation; invalid URL or explicit literal mode | Correct boundary, safe scheme, no unexpected parsing or normalization |
| PAR-06 | P1 | Multiline inline-code literal paste and unsupported alternate formatting | Declared schema fallback/diagnostic preserves source rather than silently dropping breaks/marks |
| PAR-07 | P1 | Code contains triple backticks; export using a safe longer outer fence then reparse | Exact literal code text and code-block boundary preserved |
| PAR-08 | P1 | Parse `Hi. there`, `Ex) aside`, and a valid list starting at `0.` | First two remain ordinary text; valid ordered list preserves start value zero and content |

## History, races and command parity — INT-1.12

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| HIS-01 | P0 | Format, split, paste, slash, composition; undo/redo via keys and menu | Correct semantic grouping; browser native history does not replay same change again |
| HIS-02 | P0 | Remote edit between local edit and undo | Undo removes local intent while preserving remote content under qualified history policy |
| HIS-03 | P0 | Read-only toggled before toolbar/menu/paste/async commit | All command entry points reject; no pending mark or stale UI bypass |
| HIS-04 | P0 | Two mounted editors; delayed command from A after focus moves to B | No cross-session content/focus leakage; disposal settles listeners and pending actions |
| HIS-05 | P0 | Failed applicability or malformed prepared command | Content, selection and history remain unchanged; user sees actionable result |

## Accessibility and real input — INT-1.13 / INT-1.14

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| A11-01 | P0 | Keyboard-only route editor → toolbar → menu → document → next control | Visible focus, predictable restoration, named buttons, mixed/pressed/disabled states, no trap |
| A11-02 | P0 | Screen reader edit, select, format, read headings/lists/links/code; navigate popup | Actual supported AT/browser pair exposes correct content and states; bounded announcements |
| A11-03 | P1 | Zoom/reflow, forced colors/high contrast, reduced motion; caret/errors/status | Text, focus and essential state remain perceivable without relying on color/animation |
| A11-04 | P0 | Voice Control/Voice Access select visible command names and edit text | Discoverable accessible names match labels; selection/replacement works without mouse |
| A11-05 | P0 | Real OS dictation and correction on desktop/mobile; real IME/virtual keyboard | Device-qualified text/selection/undo, no duplicate or lost phrase; offline claims explicit per provider |
| A11-06 | P0 | Accessibility/dictation with optional assistance extension disabled | Baseline editing remains usable; extension adds presentation only |

## Execution and coverage gates

INT-1.1 creates a machine-readable fixture index from these IDs and ensures every row has an implementation test owner. INT-1.2–INT-1.13 run the corresponding deterministic cases; INT-1.14 closes physical or virtual platform rows (EVT-03/05/06/07, NAV-05/06, KEY-06 and A11-02/04/05/06) and browser integration. Semantic cases also run against native Rust/WASM with equivalent snapshots where relevant; DOM/layout assertions remain browser-specific. Platform adapters reuse the same expected semantics through AIN tasks and existing native qualification; they do not inherit a browser pass.

For each case record status (`planned`, `pass`, `fail`, `unsupported`, `blocked`), command/manual steps, executed/passed/failed/skipped counts, artifact and revision. Only actual assertions or device observations can mark pass. Zero matches, missing scripts, unchecked manual rows and skipped mandatory combinations prevent qualification. Retain failed evidence and describe the support envelope; adding these documents does not establish support.
