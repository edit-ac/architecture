# Editing standards: Unicode, navigation and input coverage

This map binds ES-4.1 and ES-4.2 to the current [editing behavior profile](../specs/editing-behavior-standards.md). It describes test scope, not a platform qualification receipt. Generated results and source/build pins belong in the editor lane's ignored ES-4.1 evidence and progress file.

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
