# Editing standards: Unicode, input and structural coverage

This map binds ES-4.1, ES-4.2 and the selected ES-4.3 structural cases to the current [editing behavior profile](../specs/editing-behavior-standards.md). It describes test scope, not a platform qualification receipt. Generated results and source/build pins belong in the editor lane's ignored ES-4.1 evidence and progress file.

## Independent logical boundary oracle

The deployed profile is Unicode 16.0.0, untailored extended graphemes, `unicode-segmentation` 1.12.0. Expectations below are authored from [UAX #29 revision 45](https://www.unicode.org/reports/tr29/tr29-45.html) and the [Unicode 16 grapheme break data](https://www.unicode.org/Public/16.0.0/ucd/auxiliary/GraphemeBreakTest.txt), independently of Rust helper output and browser ICU. Offsets are UTF-16 units. This is selected rule coverage, not execution of the full Unicode conformance corpus.

| Vector (code points) | Expected logical boundaries | Rule |
| --- | --- | --- |
| `0915 094D 0924` | 0, 3 | GB9c Indic linker conjunct |
| `0915 094D 200D 0924` | 0, 4 | GB9/9c linker with ZWJ |
| `0915 094D 200C 0924` | 0, 3, 4 | GB9 Extend; ZWNJ prevents conjunct continuation |
| `0915 093E` | 0, 2 | GB9a spacing mark |
| `1F469 1F3FD 200D 1F4BB` | 0, 7 | GB9/11 modifier and pictographic ZWJ |
| `2708 FE0F` | 0, 2 | GB9 variation selector |
| `1F1ED 1F1FA 1F1E6` | 0, 4, 6 | GB12/13 regional indicator parity |
| `05D0 05B7 05D1` | 0, 2, 3 | GB9 RTL combining mark; logical traversal |

## Clause-to-behavior/build map

| Clause | Permanent selector / production boundary | What the assertion establishes | Limit |
| --- | --- | --- | --- |
| ES-TEXT-1/2 | `anchors::unicode16_declared_profile_deltas_have_fixed_utf16_boundaries` | Forward/backward movement and deletion at every expected boundary; every interior scalar/surrogate cut rejects; declared library data version is 16.0.0. | Engine logical cuts only; no shaping or visual order. |
| ES-TEXT-1 | `anchors::unicode16_scalar_ranges_and_replay_preserve_normalization_and_controls` | Current document creation/checkpoint/restore preserves composed/decomposed text, NBSP, narrow NBSP, zero-width and bidi controls byte for byte. Scalar-aligned API ranges remain distinct from character-deletion cuts; exact UTF-16/scalar counts and UTF-8 conversions. | No old reader, migration, normalization or plain-file encoding claim. |
| ES-TEXT-2 | Existing `anchors::grapheme_movement_and_deletion_are_extended_and_logical` and fixed emoji/ZWJ/combining/flag/RTL fixtures | Retained common boundary vectors, CRLF and edge no-ops. | Older raw-Yrs replay seed helpers in this file are historical fixture scope; new replay coverage uses current creation. |
| ES-TEXT-2 | Navigation `ES-4.1 optional movement capability …` | Missing Segmenter/modify/containing, exceptions after movement, stopped/cycling/out-of-owner movement and bounded repair preserve text, checkpoint, revision, commands, history and persistence; owned native endpoints remain available. | Prepared host API/native stops exercise robustness; not OS-generated input. |
| ES-TEXT-2 | Navigation `ES-4.1 differing host segmentation cannot authorize … cuts` | Deliberately differing host reports scalar stops inside combining/Indic/emoji graphemes. Engine admission rejects both deletion directions; actual Backspace/Delete leave semantic state unchanged. | Host version mismatch is prepared, not a claim that a named browser has a specific ICU version. |
| ES-TEXT-2/3 | Navigation `ES-4.1 styled … movement respects native layout boundaries` | Actual browser arrows and range extension across styled combining/Indic/emoji splits match an unmanaged unsplit editable. The RTL combining row independently asserts safe logical endpoints and records both unmanaged styled/unsplit controls and editor repair. | Native styled RTL controls can stop inside a grapheme, and Firefox's repaired affinity can differ from the unsplit control. Styled RTL shaping/visual-affinity parity remains unqualified; native observations do not redefine engine deletion. |
| ES-TEXT-3/ES-KEY-1 | Navigation `ES-4.1 inherited … native layout profile` | Hindi/ltr, Hebrew/rtl and Arabic/auto inherit host language/direction into real surface assembly and descendants, match unmanaged native visual arrows/extension and resolve live host changes without semantic mutation. | Host intent only; no persisted paragraph language/direction or shaping guarantee. |
| ES-TEXT-3/ES-KEY-1 | Existing `NAV-02 native Home/End/PageDown/PageUp and scrolling`, `NAV-03`, `NAV-05` | Native modifier/bidi behavior and an independent identical-DOM scrolling oracle. Scroll-only Home/End retain the native insertion point; keys that reveal the native caret must reveal the editor caret. | Browser/OS profile determines behavior; no logical-arrow approximation. |

Run from `core` using pinned Node 24.19.0/npm 11.17.0 and Rust 1.97.1:

```sh
cargo +1.97.1 test --locked --offline -p editac-core --test anchors unicode16_
npm run test:interactions -- --group navigation
node scripts/test-browser.mjs selection
```

The existing dispatchers run Chromium, Firefox and WebKit. Browser receipts name their exact versions and packed WASM/package hashes; production Rust source changes invalidate a previously built WASM even when its file hash has not changed. Node executes the browser tests as TypeScript with erased types; workspace typecheck/compilation and syntax admission remain separate checks. Unchanged passing groups can be retained when a later test-only change adds cases or corrects a demonstrated native oracle; report the original failure and exact rerun scope.

## Real-runtime observations retained by roadmap43

| Adapter / observation | Current boundary | Final owner |
| --- | --- | --- |
| macOS native layout, keyboard layout/IME and AT affinity | Native Commands/composition receipts qualify their selected cases only; browser controls do not supply AppKit/OS/VoiceOver proof. | roadmap43 and existing native adapter owners |
| Styled RTL shaping/caret affinity | Browser observations are retained separately from logical GB9 cut safety. Exact unsplit-control affinity parity is unavailable for the observed Firefox styled row; no visual-parity claim is made from a safe logical endpoint. | roadmap43/native layout observation owners |
| Windows, Linux, mobile keyboards and AT | No real target-runtime observation is supplied by these browser or Rust fixtures. An unavailable row stays unqualified. | roadmap43 and existing platform owners |
| Terminal source navigation | Logical source order with documented display-width/escaped-control policy; not visual RTL rich-text parity. | Existing TUI owner; final terminal/AT observation in roadmap43 |

No new format, compatibility matrix, second segmentation implementation, provider call or publication gate is introduced.

## ES-INPUT-1: cross-block replacement and composition

ES-4.2 uses the current production WASM/Session and native prepared-input interfaces. `tests/browser/composition-cross-block.ts` shares only fixture setup, exact state assertions and bookmark restoration; it contains no editor implementation. Browser cases replay prepared DOM events. Native Composition cases call AppKit input methods against actual Session/SQLite; Commands cases obtain actual active/key/first-responder focus. Neither supplies an OS-generated IME, keyboard-layout, dictation or accessibility observation.

| Clause / boundary | Named permanent cases | Exact proof and limit |
| --- | --- | --- |
| Retained replacement; prefix/suffix; result/history | `composition.spec.ts`: `ES-4.2 cross-block commit …`, `ES-4.2 cross-block direct …`; native `CommandsTests.testCrossBlockReplacementBreaksRestoreDirectedSharedBookmarks` | Both directions, paragraph/heading starts, direct text/Enter/hard break, one update/journal/undo group, first-owner prefix and last-owner suffix, returned caret. Undo restores directed shared bookmarks; redo restores result content/caret. Native matrix has twelve fixtures within one XCTest. |
| Start/update/cancel | Browser `ES-4.2 cross-block commit …`, `… cancel backward=…`; native `CompositionTests.testCrossBlockCompositionCommitOnceAndDirectedHistory`, `…CancelRestoresDirectionWithoutMutation` | Durable bytes/revision/content/history/journal unchanged during browser preedit; affected projections held and released. Native durable revision/upload/content unchanged. Cancel restores directed selection; duplicate final notifications do not add commits. |
| Focus change | Browser `ES-4.2 cross-block focus loss …`; native `CommandsTests.testCrossBlockCompositionFocusLossCommitsOnceIntoOriginalTarget` | Declared commit-on-blur policy runs once into retained target. External button/native text field keeps focus and its own content; no delayed redirection. Scripted/native-method mechanics only. |
| Outside peer; cancel/undo retains peer | `composition-remote.spec.ts`: `ES-4.2 cross-block outside peer …`, `… cancel retains outside peer …`; native `CompositionTests.testCrossBlockCompositionOutsidePeerSurvivesCommitAndUndo` | Browser prefix/suffix/independent peer edits survive commit and undo/redo; cancel remaps backward endpoints after peer insertion. Native second Session/SQLite writer delivers prefix edit; local undo preserves it. No socket-transport qualification. |
| Inside peer / stale endpoint | Browser `ES-4.2 cross-block inside peer …`, `… deleted endpoint …`; native `CompositionTests.testCrossBlockCompositionInsidePeerRejectsWithoutDeletion` and retained single-owner stale/revoked/cancelled-token tests | Endpoint/intermediate overlap and deleted endpoint preserve current durable bytes/revision/history/journal, recover composed text and reject without current-caret fallback. Browser endpoint deletion is a deliberately prepared Yrs peer update. |
| Mixed-scope refusal | Browser `ES-4.2 cross-block mixed …`; native `CommandsTests.testCrossBlockMixedReplacementAndBreakRefuseAtomically` | Code/separator browser ranges refuse before staging; invalid native selection is cleared at rejection. Mixed native container direct input/Enter/hard break refuse without content/revision/upload/history/selection changes in both directions (six fixtures). No flattening of unqualified structures. |
| Candidate Enter / single-owner ordering | Retained `composition.spec.ts` candidate-Enter, duplicate-final, cancellation and history-group cases; `composition-remote.spec.ts` retained conflict/lifecycle cases; existing EDX shared-history owners | Existing behavior is exercised by affected groups, without duplicating a second semantic/history matrix. Native shared-history bookmarks are consumed by the same production projection refresh used by Commands. |

Run affected web groups through `node scripts/test-browser.mjs composition` and `composition-remote`; use `--test-name-pattern` only for changed assertions or new cases. Current test-only additions reuse source-authenticated WASM and six consumer builds/typechecks; native test sources compile for both pinned CPU slices. A zero-match, interrupted or failed invocation is never passing proof. Reconciled distinct-case results and exact source/build pins live in ignored ES-4.2 evidence, with all original failures preserved.

The existing roadmap43 native keyboard/IME/dictation/VoiceOver, browser OS IME and other OS/AT rows remain unqualified by these scripted cases. This map does not close those owners, comprehensive EDX history qualification, endpoint performance, release or publication gates.


## Structural selection, mixed content and retained moves

ES-4.3 uses the existing move, reorder, paste and text-drag families. Expected order, text, payload and history states are authored independently of their production projection. New tests consume only the current format and current move allowlist. Block selection is ephemeral; the native adapter and OS input observations retain their existing owners.

| Clause | Permanent selector | Independent oracle and coverage boundary |
| --- | --- | --- |
| ES-SEL-1 | Reorder `ES-4.3 contiguous block extension return and typing` | Forward/backward contiguous extension, sibling/root boundary stop and ordinary focus movement produce no document bytes, revision, command, journal or history changes. Enter returns to the selected editable owner; actual typing uses the returned caret. |
| ES-SEL-1/ES-BLOCK-2 | Reorder `ES-4.3 contiguous move one update undo peer redo reopen` | Two paragraph roots retain their order, IDs, backing spans and marks through one prepared command/update/history group. A peer insertion survives undo/redo; current storage reopen preserves the result. |
| ES-BLOCK-1/ES-FMT-1 | Paste `ES-4.3 mixed structural` | Both directions through partial paragraph, whole image and partial ordered-list item: exact clipped copy, original tuple/opaque marks, no mutation on failed clipboard write, qualified formatting and preserved unselected siblings/container metadata. Compatible root cut preserves `le` + `ga`, one update and a usable caret; undo restores the directed selection and redo/reopen retains the result. Incompatible root-to-list deletion and partial-atom removal/formatting refuse with byte/state equality. |
| ES-BLOCK-1 | Paste `ES-4.3 mixed nested descendant` | Unselected nested quote/leaf remains byte-for-byte in the projected node oracle while eligible prose endpoints are formatted; undo restores all nodes. |
| ES-BLOCK-2/ES-INT-1 | Rust `moves::es43_retained_{image,asset,reference,callout,inert_extension}_move` | Five current descriptor families retain complete tuple, source/owner identities, spans, marks and external reference/asset identifiers through move, reopen and one undo/redo unit. Independent peer text survives. Same-position move emits no revision, bytes or history change. Inert unknown extension payload is preserved without execution. |
| ES-BLOCK-2 | Rust `moves::es43_typed_move_refusals_leave_bytes_history_sources_and_revision_equal` and `es43_current_addressed_table_move_is_unavailable_without_changing_cell_storage` | Stale target/parent/sibling and invalid destinations preserve exact state. Unknown/future tuples and addressed tables remain unavailable through MoveCommand; no inferred payload conversion or cell-storage rewrite. |
| ES-BLOCK-2 | Existing Rust `self_and_descendant_cycles_reject_before_live_mutation`, `malformed_root_version_rejects`, `mixed_batch_cycle_and_stale_version_reject_every_staged_move`; reorder invalid-nested/stale/empty-destination cases | Existing independent cycle/root/stale compound rejection assertions are reused by their original names and focused current execution, rather than duplicated. |
| ES-BLOCK-1/ES-INT-1 | Existing `MOV-06/07 directed source preservation` | Failed destination and Escape cancellation retain directed Unicode source bytes and selection, with subsequent typing still usable. This is prepared drag/cancellation mechanics, not an OS clipboard claim. |

### Reconciled structural prerequisite

`ES-4.3 mixed block group move preserves payload and Escape return bookmark typing` retains its original independent oracle: moving the paragraph/image pair after its next sibling must produce `[next, paragraph, image]`. The ES-3.5/ES-3.1 shared Move repair validates captured roots together and places the ordered group through witnessed successor relationships. The unchanged case now passes in Chromium, Firefox and WebKit, including complete payload/source identity, one history/update group, decorations, absent conversion capability, Escape bookmark return and actual typing at the returned caret. The earlier `[next, image, paragraph]` failures remain in the original evidence.

The selected ES-4.3 union is 100 distinct passing cases: 36 current reorder cases, 10 current named Rust cases, and 54 compatible paste/drag cases reused after source and execution-path review. The current full reorder run additionally passes 42 existing cases outside that selected denominator. The enclosing current Rust moves suite has 45 passes and one retained legacy-profile fixture failure; it is not a passing full suite. No test oracle, format or unsupported conversion gate was weakened.

The source-bound direct command/harness receipts and retained failures are in the editor lane's ignored `ES-4.3` evidence. Production compile/build proof is reused only after input/artifact authentication. Historical EDX-2.6 links/assets receipts remain mechanism references where their source pins differ; they do not qualify the current package. No BTQ/BTA conversion receipt or provider is admitted by these cases, and no conversion support is inferred. Existing table companion PST-04 directed-cell tests still use obsolete textbox labels; their recorded timeouts remain with the INT/PST owner, separate from current engine table-move refusal and the new mixed-content assertions.

## Terminal commands and accessible selection

ES-4.4 owns the missing automated cases under ES-KEY-1, ES-AX-1 and the terminal boundary of ES-TEXT-3. This map consumes the current ES-2.4 dispatcher/help and ES-3.2/3.5 selection/capability interfaces. These selection-only cases do not exercise or qualify the separately reconciled ES-4.3 Move behavior. ES-4.4 changed no production semantics, keyboard protocol, schema or history implementation.

| Clause / case family | Production boundary and independent oracle | Support / limitation |
| --- | --- | --- |
| ES-KEY-1; `tui_input::es44_reported_word_*`, `es44_document_*`, `es44_word_deletion_*` | Actual `InputState::handle_source`: reported Control and Alt word movement, both directed extensions/collapse, UTF-16 document bounds and word deletion over exact combining/emoji/Hebrew/CRLF source. Read-only deletion refuses without selection/source mutation. | Deterministic crossterm events exercise dispatcher semantics; they do not show that an emulator/OS reports a chord. Basic/conflict input remains a separate owner. |
| ES-KEY-1; `es44_picker_all_named_commands_*` | All fourteen F1 entries are chosen using reported navigation/Enter, each against a hand-authored expected source/anchor/caret. Picker typing/paste does not edit the source. | F1 is the named fallback for unreported modifiers, not a new terminal protocol. |
| ES-KEY-1/ES-TEXT-3; `es44_terminal_viewport_*`, `es44_terminal_reserved_*`, `es44_unreported_*` | Actual `TerminalOwner` with deterministic backend: viewport-sized page navigation/Shift extension/resize retains preferred column and exact semantic checkpoint; reserved callbacks precede picker; Escape cancels before exit. Ctrl-H/W/D, Alt letters, combined modifiers and release reports do not become destructive word edits. Ordinary Backspace retains ordinary behavior. | Source draft and committed semantic history remain distinct. A callback priority test does not qualify every global command's semantic behavior. |
| ES-KEY-1; `tui_pty::es44_packaged_xterm_*` | Real packaged binary under controlling PTY/crossterm: CSI 1;5C word movement, CSI 1;6C extension, CSI 1;5H/F document bounds, literal bracketed-paste replacement/save and F1 (`ESC O P`) picker cancellation. Exact saved/current source and pending semantic-update count; child reaping and terminal restoration. | xterm-256color reports on macOS arm64 only. These injected bytes are real PTY/parser evidence, not physical keyboard, enhanced protocol or emulator-interception qualification. |
| ES-KEY-1/ES-TEXT-3; `tui_help::es44_terminal_profile_*` | Executable offline help and authored support text expose word/document/page commands, Shift extension, F1 fallback, ambiguous Ctrl-H/W/D/Alt reports, Shift-Enter indistinguishability and logical source order. No session/file acquisition. | No visual bidi rich-text parity, unreported modifier support or screen-reader claim. |
| ES-AX-1/ES-KEY-1; accessibility `ES-4.4 keyboard block entry*` and `selected blocks Escape*` | Production shortcut-profile/catalog and sole retained block target: keyboard entry/extension/contraction, root order, selected/focused descriptions, visible outlines and polite atomic mode/count/type text. Enter restores bookmark and actual next typing; Escape then Tab/Shift+Tab reaches adjacent controls. Nodes/revision/history/journal/commands/patches stay exact during selection. | Explicit fixture F8 remap; catalog has no global default block-entry chord. DOM status/description and browser focus prove mechanics, not speech/braille or authoring across all viewports. |
| ES-AX-1/ES-KEY-1; accessibility `ES-4.4 composition and popup*`, `reserved host chord*` | Prepared composing flags/lifecycle and actual link popup retain priority; composing Escape is uncanceled. Host reservation wins over remap; named command remains available; block typing/deletion does not edit a hidden caret. Popup cancellation/one-shot Tab returns predictable focus. | Prepared IME observations only. Original OS/native input and AT gates stay open. |

The host accessibility fixture captures a toolbar target before Escape arms the one-shot exit, rather than clearing that route on Tab or passive selection notifications. Slash and block live regions are asserted separately; invalid-link feedback uses the current atomic alert. Static `assistive-input` package imports are recorded as such; the baseline no-assistance case checks that every request stays on the local fixture origin, not that a filename is absent. No provider or optional assistance service is configured.

Production WASM/core/web and current consumer build/typecheck receipts are reused only after exact current source/artifact-pin authentication. CLI tests compile the current native binding and executable. Browser tests run packed packages with pinned Node 24.19.0/npm 11.17.0 and Playwright 1.64.0; exact engine versions, artifact hashes, counts and historical failures remain in the ignored ES-4.4 evidence. Source-only fixture/test edits do not claim new product runtime qualification.

The [platform observation inputs](editing-experience-platform-matrix.md#terminal-and-block-selection-observation-inputs) name the remaining actual terminal/OS/IME/AT recipes under original roadmap43 owners. Desktop browser, AppKit, UIKit, Android, Windows, Linux and mobile support remain separate: only the executed selected runtime is qualified for its stated mechanical boundary.
