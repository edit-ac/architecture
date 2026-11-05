# Editing experience: observable behavior and delivery checklist

Authority: supplements [everyday editing](editor-interactions.md), [regression boundaries](editing-regression-suite.md), [platform services](platform-editing-services.md) and [durability](document-durability.md). Research reviewed 2026-10-24; [source review and local archive](../research/editing-reference-review.md). These are acceptance requirements, not a claim of implementation or platform qualification. Keep existing case IDs, task dependencies and the single current document format. No new runner is started by this amendment.

## What a line means

Three different things can look like a new line:

1. **Visual wrapping** occurs when a line exceeds the available width. It changes layout only. Narrowing the window, changing zoom or moving Down must not insert text, create history or enqueue storage writes.
2. **A line break within a paragraph** is authored content. Shift+Enter in rich prose inserts it and places the caret immediately after it. Typing continues in the SAME paragraph, list item, heading, quote paragraph or table cell. The current engine's `hardBreak` operation represents this with an LF within the existing text owner. DOM `<br>` nodes are a projection; a filler used to position the caret is not authored content. CKEditor describes its Shift+Enter interaction as a “soft line break”; our specification calls this a semantic hard break. Neither term means a width-dependent wrap or a Markdown source soft break.
3. **A paragraph break** is structural. Enter splits a paragraph at the selection. The suffix moves to the new sibling and the caret goes to its start. Paragraph spacing and paragraph-level attributes belong to blocks, not to extra newline characters inserted for appearance.

For `ab|cd`, Shift+Enter must yield one owner containing `ab\n|cd`; typing X yields `ab\nX|cd`. Enter must yield two blocks `ab` and `|cd`; typing X yields `ab` and `X|cd`. A caret merely moving down is a failure even if the screenshot resembles the intended result. So is an extra paragraph, a lost suffix, an invisible authored break, a double insertion or typing X at the old caret.

Use **New paragraph** and **Line break within paragraph** as distinct command descriptions. In code, say **New line in code**. A compact toolbar may omit a line-break button, but mobile and accessibility surfaces must provide a discoverable equivalent when the keyboard cannot express the chord. A rich message composer must not silently reinterpret Enter as Send; an explicit, visible host sending profile is a separate action, suppressed during composition. Unsupported rich operations are disabled with an explanation, never simulated by cursor movement.

## Break behavior by context

The existing Enter table remains normative. These details make its observations testable:

| Context | Required behavior and preserved state |
|---|---|
| Paragraph | Enter splits; Shift+Enter retains owner, parent, paragraph attributes and applicable inline marks. At start, middle and end preserve all unselected text. |
| Heading | Middle/start Enter splits at the same level; end Enter creates a paragraph; empty heading Enter becomes a paragraph. Shift+Enter retains heading level. A following list must remain unchanged. |
| List/task item | Enter splits a nonempty item; new task item is unchecked. Empty nested item exits one level, then an empty outer item exits to prose. Shift+Enter never creates a bullet, increments numbering, changes checked state or changes nesting. |
| Quote | Enter splits the quoted paragraph; empty final paragraph exits one quote level. Shift+Enter keeps the quote and its paragraph. A visual blank line alone is not a quote-exit instruction. |
| Code | Enter and Shift+Enter insert literal LF in the code owner. Preserve language, indentation and literal punctuation; no prose parsing, smart quotes or automatic list conversion. |
| Table cell | Enter and Shift+Enter insert a break inside the cell's text. Row/column counts, spans, widths, table identity and neighboring cells remain unchanged. Cell selection and text selection are distinct. |
| Selected text | Delete the selected content and insert/split in one prepared command. Test forward and backward ranges. Rejected structural combinations leave content, selection, revision, history and persistence unchanged. |
| Repeated/trailing breaks | Empty paragraph + two breaks contains exactly two authored LF characters; typing X follows both. Copy, save/reopen and supported lossless exports retain them. Export to a format unable to express them reports loss rather than inventing a paragraph. |
| Composition/read-only | Composition owns its confirmation keys; confirming a candidate does not add a break. A later deliberate Enter works. Read-only rejects at the command boundary even for synthetic events, menus and accessibility actions. |

An input adapter routes **intent**, not only a hardware key. Browser `insertParagraph` and `insertLineBreak`, native text-system selectors, toolbar commands, soft keyboards and assistive actions must reach the same shared command. For one physical action, keydown + beforeinput + input notifications produce one commit. A genuine second action produces a second commit even if its text is identical. Do not infer intent solely from the resulting DOM text.

## Feature descriptions and non-surprising boundaries

These descriptions are suitable for capability documentation and implementation acceptance. Existing format/schema contracts decide exact serialization; the reference site's historical HTML suggestions do not override them.

| Feature | User-facing meaning | Required edge behavior / existing case family |
|---|---|---|
| Bold, italic, underline, strike | Apply or remove the named property on selected text; at a caret, affect subsequent typing. | On/off/mixed/disabled is accurate for the entire selection. Mixed toggle applies uniformly. Unrelated marks remain. Pending marks are local state, not empty persisted spans. Selection direction does not change meaning. MRK, REG, WCF-19. |
| Highlight/color | Distinguish selected text with an explicit supported value. | A mixed-value surface changes only fields the user changed. Cancel/no-op creates no history. Unsupported values are disabled or preserved as bounded unknown data under the format contract; never silently normalized. MRK, WCF-19. |
| Heading | Give a paragraph a supported structural heading level. | Changing type preserves text, selection and compatible marks. Levels are configured capabilities, not a mandatory three-level subset from the old recommendation. BRK-05, formatting cases. |
| Bulleted/numbered/task lists | Group items with unordered markers, an ordered sequence or checked state. | Nest/outdent/split/join retain unselected items and explicit ordered starts. Marker decorations are not selectable text. Task splitting resets only the new item's check state. BRK-06, DEL, KEY. |
| Link | Attach a destination to selected text or insert a labeled destination. | Opening and editing are distinct actions. Capture the original selection before dialog focus. Validate destination and stale targets; cancel makes no edit. At the end, ordinary typing does not accidentally extend a link. Paste-as-link and auto-link have explicit policies. MRK, PST, keyboard-links. |
| Quote | Mark quoted content while preserving editable paragraphs. | Enter/exit nesting is predictable. Attribution/caption exists only when supported by the schema; do not synthesize new structure because a reference uses a figure wrapper. BRK-07, DEL. |
| Image/attachment | Insert a selectable content object with supported description/caption. | Preserve alt text, selection around the object and safe resource identity. Failure or canceled upload must not delete source content. Delete/select/undo and keyboard access work. PST, NAV, attachment owners. |
| Table | Edit structured rows and cells. | Text editing does not become row navigation. Tab follows the explicit cell policy and Escape then Tab exits. Merged-cell and incompatible-range operations reject atomically. BRK-08, SEL-04, table owners. |
| Code | Preserve literal text and optional language metadata. | Whitespace, tabs, blank lines and punctuation remain authored text. Inline code and code blocks are different features; neither silently runs code. BRK-08, SPC, parsing. |
| Undo/redo | Reverse/reapply the most recent eligible local semantic action. | Selected replacement plus break is one action. Restore semantic selection and pending-mark policy; a remote edit must not be undone as local work. Native undo managers and DOM rerenders cannot create a second history. HIS, REG. |
| Copy/cut/paste/drop | Transfer content at a captured, validated target. | Preserve supported semantics, sanitize external markup and enforce limits before mutation. Plain paste stays literal. Cut deletes only after successful clipboard preparation. Failed destination never deletes drag source. PST, transfer cases. |
| Navigation/deletion | Move or select without editing; delete a selection or qualified user-perceived character. | Respect graphemes, bidi visual movement, preferred horizontal position and block boundaries. UTF-16 public positions do not mean deleting one code unit. NAV, DEL, G06. |

### Explicit continuation after code and atoms

The portable `continue-after` command uses **Primary+Enter** (Command+Enter on
macOS, Ctrl+Enter elsewhere). With a caret or selection entirely in one code
block, it continues prose after that block without consuming its text. With an
exact selected noneditable block atom, the same command continues after the
selected block; it never fabricates an editable position inside the atom.
Ordinary Enter and Shift+Enter in code remain literal LF.

Continuation delegates to the existing captured **Insert after** action. It
always creates a fresh empty sibling paragraph immediately after the captured
block in its existing parent, including when an empty paragraph already follows;
it does not reuse or move that paragraph. One prepared edit preserves the source
and descendants, focuses the new paragraph at UTF-16 zero and forms one undo
group. Undo removes the new paragraph and restores the captured code selection
or atom selection. A delayed captured command cannot follow a later caret or
edit. Unsupported, stale, protected and read-only targets reject with an
accessible explanation. An owned rejected chord is consumed, preventing an
accidental host-form action. Host reservations/remaps and command permissions
remain effective; reserved chords retain host ownership. Keyboard help and the
command catalog expose the continuation action even when the block menu is off.
| Search/menus/popups | Act on the focused control and the captured target. | Search-field Enter navigates results; it must not split the document. Popup selection, Escape and focus return must not lose the editor range or override IME ownership. SLH, ENV, command-surfaces. |

Re-entering an empty paragraph derives pending formatting according to our existing local-state rule. Do not resurrect remembered persistent empty-paragraph styles from the reference site's unfinished inline-style draft. Multi-range editing and arbitrary HTML formatting are not implied capabilities. A disabled feature is documented as unavailable rather than advertised through a nonworking toolbar item.

## Required test oracle

Every new interaction regression uses the real engine and the relevant mounted adapter. Expected outputs are independently authored from this contract, never recorded from the implementation under test. At minimum record and assert:

- Owner IDs, parents, kinds, complete text including escaped whitespace, marks, block attributes and unaffected neighbors.
- Anchor/focus owner and UTF-16 offset, direction and affinity; a next typed sentinel proves the caret is usable.
- Exact change in semantic commit/publication, history group and journal/outbox enqueue counts. Movement/cancel/reject produces zero; one accepted break produces one.
- Undo restores text, structure and selection; redo restores the break and the next typing location. Do not treat a screenshot or a successful command return as sufficient.
- Rendered authored breaks versus fillers; save/reopen using the current identity; clipboard and supported import/export round trips. Use explicit loss diagnostics when a destination cannot encode a distinction.
- Delivery path: hardware key, beforeinput without keydown, duplicated notifications, native command/menu, soft input/IME and accessibility. A shared semantic pass does not prove a platform input path.

Boundary variants include empty/start/middle/end, two consecutive breaks, forward/backward selected ranges, emoji before the caret, marked text, a following list, cell boundaries, read-only, composition confirmation/cancel, focus loss, and unrelated remote edits. Reuse BRK-01–08, SEL-01–04, MRK-04, NAV-06, SPC-03 and G01–G07; do not count an old pass as evidence for a newly added variant.

## Concrete implementation actions and completion rules

The checklist is integrated with existing owners. It is not a second roadmap queue. Existing main-branch work and active worker inputs must be preserved; changes to a controller-owned queue require its safe checkpoint.

| Order / owner | Action in existing implementation | Completion evidence |
|---|---|---|
| 1 — INT-1.2, engine/Session | Retain the shared `hardBreak` versus split distinction, prepared replacement, same owner, resulting anchors and single history boundary. Add missing context fixtures without changing current format identity. | Rust/Session real-engine vectors plus current codec/storage assertions. |
| 2 — INT-1.2, browser input | Test both native Shift+Enter and `beforeinput.insertLineBreak` without a keydown; retain the paired `insertParagraph` control. Check duplicate delivery separately. | `tests/browser/interactions/breaks.spec.ts` and `break-tables.spec.ts` on Chromium, Firefox and WebKit; nonzero per-browser counts. |
| 3 — macOS command/input owner (roadmap18) | Add an explicit shared hard-break command and route Shift+Return plus `insertLineBreak:` through it. Preserve active composition, read-only and target applicability. Do not let the text view independently commit a newline. | AppKit Commands XCTest: same owner, selected replacement, trailing breaks, sentinel, undo/redo; actual responder key and selector paths. |
| 4 — iOS input owner (roadmap16/31) | Expose an explicit in-paragraph break action; map supported hardware Shift+Return separately from Return. Preserve UITextInput marked/selected ranges and candidate geometry. | UIKit simulator/OS-host input tests with selection, composition, repeated breaks and durable reopen. Hardware path must be identified separately from software keyboard. |
| 5 — Android input owner (roadmap17/32) | Map InputConnection text/composition and keyboard actions to explicit semantic intents; never infer all newline commits as paragraph splits. Provide a break action where the IME has no chord. | Emulator/OS-host tests for commitText/composition/batch edits, action keys versus LF, UTF-16/code-point deletion, same-owner break and history. |
| 6 — Windows/Linux input owners (roadmap18/34/35) | Route TSF/CoreText or chosen Windows adapter and GTK IM-context commit/preedit through shared commands. Declare the actual toolkit; a capability JSON is not an editor. | Executed target runtime tests for Shift+Enter, composition commit/cancel, text ranges, focus, selection and restore. |
| 7 — terminal owner (roadmap15/36) | Preserve literal source editing: Enter inserts a source newline. In a rich semantic command surface, expose a named hard-break action; when the terminal cannot distinguish Shift+Enter, document an alternate chord/command. | Real CLI/TUI adapter tests distinguish source newline from rich hard break; PTY tests record terminal protocol and key support. Never silently claim modifier support. |
| 8 — INT-1.3–1.18 / platform services | Carry the feature-table edge cases into the existing formatting, deletion, navigation, paste, popup and command-surface groups. Capture any new minimized failure under the existing family. | Focused suite per changed behavior; zero missing fixtures/zero required skips. |
| 9 — PHY-1.4 / roadmap43 | Run the [cross-platform matrix](../tests/editing-experience-platform-matrix.md) on named browser/OS/keyboard/AT versions after feature implementation. | Separate engine, adapter, target-runtime and assistive observations; failures remain open and cannot be replaced with fixture-validation passes. |

Development can finish independent features before exhaustive platform qualification under the existing sequencing policy. Publication/readiness cannot claim a platform whose required runtime rows remain open. All automated cases are deterministic; no paid inference, credentials or network model calls are needed.

## Open regression: native history loses the editing selection

Priority P0; owners RGS-1.3 (history/rebased selection), DSK-1.7 (native commands) and shared Session/FFI. `testHardBreakSelectorReplacesSelectionInSameOwnerAndRestoresHistory` is an executable reproducer in `core/native/macos/tests/Commands/CommandsTests.swift`. Keep it enabled and its expected selection unchanged.

Starting with `a[bc]d`, `insertLineBreak:` correctly produces one owner containing `a\nd` and caret 2. Undo must restore selection `{location:1,length:2}` in `abcd`; redo must restore caret 2 in `a\nd`; typing X must yield `a\nXd`. The observed defect instead restores `{0,0}` for both history actions and then produces `Xa\nd`. Correct text alone cannot close this case.

Trace entry/result bookmarks through `crates/editac-session/src/{session,edit_service}.rs`, `crates/editac-ffi/src/session.rs`, `native/macos/Sources/EditacMacOS/session/NativeSessionExecutor.swift` and `commands/NativeCommands.swift`. The current native undo/redo response carries a commit receipt but no resulting semantic selection; the command refresh positions the caret only for `.inputCommitted`. Qualify selection capture/transport through the shared history boundary and resolve the returned anchors after projection. Do not add a second native content/history stack, restore a stale numeric offset, or special-case the test by moving the caret before typing X.

Closure requires this test plus rebased remote-edit, deleted-target, directed-selection, typing-group and nonmutating rejection variants at the shared boundary and affected adapters. Separately reconcile the pending macOS capability manifest with a validated source revision: its stale revision/input pins currently block the standard native gate before compilation. Neither a hash refresh alone nor a focused standalone XCTest closes that qualification gate. The hard-break route, native history selection and full platform qualification have separate acceptance states.
