# Desktop conventions, native protocols and first-party combinations

Status: planned acceptance cases, not executed tests. Extends the existing catalogs; BRK-04 already owns selected Enter, REG-11 owns nested drag routing, and RCH-1.17 owns block reordering. Sources: [desktop](../evidence/desktop-editing-research.md), [native](../evidence/native-editing-research.md), [extensions/performance](../evidence/editing-performance-extension-research.md). Contracts: [interactions](../specs/editor-interactions.md), [rich content](../specs/rich-content-extensions.md), [native parity](../specs/native-sdk-parity.md), [verification](../specs/verification.md).

## Coverage protocol — RGS-1.1, RGS-1.8

Each row binds an implementation owner, semantic/browser/native/device layer and exact profile. Enumerate variants rather than reporting one row as all-platform coverage. Common oracle: content and retained marks/identity, anchor/focus/direction/affinity, pending marks, focus, history, observed commits/publication/persistence, cancellation and resources. Assert next typed sentinel and undo/redo where relevant. No-op, canceled, rejected, navigation and preview actions emit zero document updates. Mock only external services, not the engine under test. Manual native/IME/device evidence is independent of event replay.

Risk dimensions: empty/start/end; forward/backward/collapsed/cell/node selection; plain/marked/bidi/grapheme text; paragraph/list/code/table/atom; keyboard/pointer/touch/OS command; editable/read-only/permission-change; local/remote/stale-session; baseline/official preset/conflicting configuration. Full Cartesian coverage is unbounded: require fixed P0 cases, every relevant boundary and explicit high-risk pairs/triads; record exclusions and seeded-property gaps. Optional feature absence is tested, not silently counted as supported execution. A newly reproduced failure adds a minimized deterministic fixture.

## Replacement and pointer selection — INT-1.2, INT-1.15

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| SEL-01 | P0 | `a[bc]d`, forward then backward; Enter and Shift+Enter separately | `a¶d` or `a↵d`; one replacement transaction; correct caret; undo restores exact text and directional selection |
| SEL-02 | P0 | `ab[c¶de]f`; Enter; hard break separately | `ab¶f`; hard-break case `ab↵f` only with qualified structural join; otherwise complete rejection, never partial deletion |
| SEL-03 | P0 | One paragraph `[abc]`: type X, Enter, Delete separately; repeat whole-document variants with final empty block | Exact base outcomes `X`, two empty paragraphs `¶`, and one empty paragraph respectively; qualified multi-block policy preserves valid structure, no phantom marks; undo restores original |
| SEL-04 | P0 | Selection crosses marked text, list/code boundaries, table or noneditable atom | Apply only qualified replacement semantics; preserve unselected prefix/suffix and identities or reject atomically |
| SEL-05 | P1 | Click, Shift-click, double-click/word-drag, platform paragraph gesture; reverse direction across wrapped bidi text | Native profile's range granularity and visual selection; no mutation; drag begins from the captured selection |
| SEL-06 | P0 | Press within selection, release without drag; repeat past platform drag threshold | Click follows platform collapse; drag keeps original source, never collapses prematurely |
| SEL-07 | P0 | Extend selection beyond viewport through nested scroller, zoom/transform; pointercancel/blur/dispose | Correct logical endpoints including unmounted text; autoscroll ceases and no late refocus/selection update |
| SEL-08 | P1 | Right-click inside/outside selection, keyboard context menu, open/cancel toolbar dialog | Named platform range policy; captured target preserved, cancel leaves content/history intact |

## Same-document text move/copy — INT-1.16

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| MOV-01 | P0 | `ab[CD]ef` drag before `a`, then undo/redo | `CDabef`, inserted `CD` selected; one history group; undo restores source and original selection |
| MOV-02 | P0 | Same source drag after `f` | `abefCD`; destination remapped through source deletion, not an off-by-range-length insertion |
| MOV-03 | P0 | Drop at start/interior/end of source as move | Exact no-op, zero commits/history entries |
| MOV-04 | P0 | Request copy modifier, change modifier mid-drag | Final supported effect is shown and honored; source retained for copy, one inserted fragment |
| MOV-05 | P0 | Marked multi-block range, hard breaks, emoji, atom and backward selection | Qualified fragment fidelity and identity policy; no duplicated node IDs or split surrogate; full undo |
| MOV-06 | P0 | Drop into incompatible code/table/read-only region; final prepare fails | Source and destination unchanged; indicator cannot imply success |
| MOV-07 | P0 | Escape, outside drop, pointer cancel or destroy target before completion | Source intact; temporary state/resources cleared, no new history |
| MOV-08 | P0 | Remote edit outside source versus overlapping/deleting source during drag | Outside anchors remap; changed source cancels unless qualified identity validation permits; no deletion of remote content |
| MOV-09 | P0 | drop + insertFromDrop + deleteByDrag + observer echoes | Exactly one accepted semantic intent; later identical legitimate drag still works |
| MOV-10 | P1 | Same document in two views; nested code control; keyboard-accessible move alternative | One shared-session transaction/history entry and view-local selection; Undo from focused B reverses A→B move, then Undo in A cannot replay it independently. Separate sessions follow origin/transfer policy; inner owner prevents outer duplicate; keyboard alternative has equivalent content |

## Cross-document and external transfer — INT-1.17

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| XFR-01 | P0 | Drag across two documents with default profile | Copy, preserving source and separate history; no false cross-document atomicity claim |
| XFR-02 | P0 | Host advertises move; destination import/commit fails or acknowledgement is lost | No source deletion; retry is idempotent within declared receipt scope; failure is visible |
| XFR-03 | P0 | Destination succeeds; source permission/revision changes before deletion | Preserve both copies, report incomplete move; never delete a changed source |
| XFR-04 | P0 | Async external data provider resolves after document switch/disposal | Old target cannot edit/refocus new editor; source retained on failed transfer |
| XFR-05 | P0 | Foreign payload forges internal MIME/schema/session metadata; oversized/malformed HTML or files | Use untrusted import/size/authority policy, no privileged path or unexpected network; explicit fallback/rejection |
| XFR-06 | P0 | Outbound drag to external application requests unqualified move | Offer qualified copy effect; no delete on dragend or bare OS effect acknowledgement |
| XFR-07 | P1 | Drop under autoscroll, touch/system drag, and unsupported gesture/API | Correct mapped destination where supported; reachable clipboard/move alternative and explicit capability evidence |

## OS command and context ownership — INT-1.18, INT-1.7, INT-1.12

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| CMD-01 | P0 | Same edit from keyboard, Edit menu, context menu, toolbar and accessibility action | Same applicability/content/history and one commit; only focused editor handles it |
| CMD-02 | P0 | Find field, host input or nested widget focused; Enter, Select All, undo/cut | Focus owner handles command; outer document unchanged |
| CMD-03 | P0 | OS spelling/correction/reconversion range differs from visible selection | Captured supplied target replaced once; stale/invalid range rejects, never latest-caret fallback |
| CMD-04 | P0 | Read-only changes while menu/dialog is open; cancel/close/reopen | Enablement revalidated at activation; no stale write or swallowed native focus action |
| CMD-05 | P1 | Redo stack empty; repeat shortcut/menu; save between edit and undo | No accidental repeat-as-redo; save alone does not clear semantic history under the current session policy |
| CMD-06 | P1 | Non-US layout, OS reserved key or remapped screen-reader command | Respect focused profile/OS ownership; visible discoverable command remains available |

## First-party document search — RCH-1.21

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| FND-01 | P0 | Search text in unmounted blocks; next/previous/wrap and selection-seeded query | Complete bounded logical search; transient highlight, explicit count/wrap; zero semantic changes |
| FND-02 | P0 | `cat [cat] cat`: capture scope, focus/select query field, search cat, Replace All dog; repeat with outside remote insert | Exactly `cat dog cat`, one undo restores original; outside remote content/matches preserved after revalidation. Query-field selection never changes scope; Enter only navigates |
| FND-03 | P0 | `cat cat`; Replace Current then separate Replace All from initial state | `dog cat` versus `dog dog`; inserted replacement not recursively re-searched; each command one undo group |
| FND-04 | P0 | Empty query; limits exceeded; unsupported regex/zero-width query | Clear/reject explicitly with bounded work and no partial replacement |
| FND-05 | P0 | Remote edit or permission change between match scan and apply | Revalidate/recompute or reject; no stale-offset replacement or silent protected-range skip |
| FND-06 | P1 | Bidi, NFC/NFD, case expansion, marks, atom/table boundaries | Literal default preserves code points; optional matching profile maps whole original characters; no implicit cross-structure match |
| FND-07 | P0 | Escape/cancel search after deliberate caret move; disable feature with pending scan | No late highlights/refocus/mutation; current user navigation wins; baseline OS/browser Find remains available |

## First-party code conveniences — RCH-1.22

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| IDE-01 | P0 | Move/duplicate selected logical lines, backward selection ending at next line start | Exclude untouched endpoint line; exact LF/whitespace, selection and one undo group |
| IDE-02 | P0 | Last line without LF, blank lines, tabs/trailing spaces; boundary move | Preserve EOF/indentation; no-op at code boundary, no move into prose/table |
| IDE-03 | P0 | Surround selected text with supported pair; undo; incompatible selection | One prepared edit with specified retained selection; atomic reject across unsupported contexts |
| IDE-04 | P1 | Indent/outdent through visible command and keyboard; Escape then Tab | Identical code semantics; focus escape still works, no keyboard trap |
| IDE-05 | P0 | Comment command for known/unknown language; feature disabled | Use declared grammar or show unavailable; no guessed syntax or prose mutation |
| IDE-06 | P0 | Opt-in auto-pair under IME/paste/replacement/remote replay; overtype/backspace | Only qualified direct typing triggers; no double delimiters or swallowed commit key; fixed profile and undo |

## Table selection semantics — RCH-1.6, RCH-1.8

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| TBL-01 | P0 | Selected cell rectangle; Delete/Backspace versus Remove Rows/Columns | Clear contents retains geometry; explicit removal changes structure; undo restores identities and content |
| TBL-02 | P0 | Text inside one cell versus whole-cell selection; type/Enter/clipboard | Distinct selection kinds route to declared command, never accidentally delete table |
| TBL-03 | P0 | Rectangular paste mismatched dimensions, protected cells, merged cells if admitted | Profile's explicit expansion/rejection; no silent loss, partial writes or unsupported merge flattening |
| TBL-04 | P1 | Resize/reorder handle beside text selection, touch scroll or nested cell input | One gesture/event owner; cancellation restores preview; no drag theft or duplicate commit |

## Official extension configurations — EXT-1.12, EXT-1.5, RGS-1.7

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| FPX-01 | P0 | Load each named preset and baseline with none | Exact versions/capabilities and deterministic defaults; baseline input/selection/a11y remains functional |
| FPX-02 | P0 | Duplicate IDs, missing dependency, incompatible schema/version | Actionable pre-activation rejection with zero document mutation |
| FPX-03 | P0 | Keymap/input-rule conflicts, import/registration order permutations | Declared precedence or explicit conflict; no accidental order-dependent winner |
| FPX-04 | P0 | Table + search + history; code + pairs + IME; link/slash + replacement | Named high-risk triads satisfy shared ownership and undo; each combination independently recorded |
| FPX-05 | P0 | Disable/unload presenter with selection, stored content and pending callback | Content retained through lossless fallback; anchors/history valid; late completion inert |
| FPX-06 | P0 | Throw before preparation, during presenter work, and after committed update | No partial precommit edit; committed edit preserved; diagnostic/fallback without recursion |
| FPX-07 | P0 | Optional worker stalls or malformed result arrives | Bounded queue/timeout, cancellation and revision checks; baseline editing continues; no claim of same-thread infinite-loop containment |
| FPX-08 | P0 | Disabled feature import trace; repeated enable/disable/mount/dispose | No eager feature evaluation/network/workers while disabled; resources return to declared bounds |

## Native coordinate and composition protocols — AND-1.4, AND-1.6, LNX-1.4, LNX-1.6, WIN-1.6, IOS-1.6, DSK-1.6

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| NAT-01 | P0 | Android surrounding deletion with selected text and supplementary emoji; UTF-16 and code-point variants | Correct API-specific units and excluded selected range; no generic delete-selection substitution or split surrogate |
| NAT-02 | P0 | Android batch/input connection replaced, then stale callbacks; nullable surrounding context | No edit in new session, unbalanced batch or false success; context is bounded and safely unavailable |
| NAT-03 | P0 | GTK accented UTF-8/emoji, backward range, preedit; surrounding/delete callbacks | Correct byte/character/public UTF-16 conversions at each API boundary; no provisional preedit in committed surrounding text |
| NAT-04 | P0 | Windows committed-text reconversion, commit/cancel; overlapping/outside remote changes | Captured target, qualified composition policy and no duplicate undo; cancellation preserves original |
| NAT-05 | P0 | Apple marked/selected ranges, replacement then caret changes; asynchronous completion | Correct captured semantic target or explicit stale rejection; no late write in another editor |

## Native commands, gestures and transfers — IOS-1.7, AND-1.6, AND-1.7, DSK-1.7, WIN-1.7, LNX-1.7, IOS-1.13, AND-1.13, DSK-1.13, WIN-1.13, LNX-1.13

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| NAT-06 | P0 | Android handwriting gesture preview, apply/cancel, unsupported gesture fallback | Preview is transient; accepted result once, correct fallback/result; geometry current after scroll/zoom |
| NAT-07 | P0 | Native Find/Edit/context menu across editor and query/host inputs | Focused responder and capability enablement; one shared semantic history, no outer-input theft |
| NAT-08 | P0 | AppKit Services/substitution returns replacement for captured text | One qualified replacement or stale rejection; unsupported formatting explicit; prepared service response only |
| NAT-09 | P0 | Linux PRIMARY selection vs clipboard, middle-click at different insertion target | Backend-specific supported policy, correct target, clipboard/source preserved; unsupported backend explicit |
| NAT-10 | P0 | Two native views of same session, cross-app drag, slow item provider | Correct move/copy/receipt policy; no double delete or source loss on cancellation |
| NAT-11 | P0 | Native cut/provider failure or source view disposed during promised transfer | Clipboard lifetime and deletion contract respected; failure visible, original text recoverable |
| NAT-12 | P1 | Mobile selection handles, physical keyboard, split/resize viewport during composition | Visible caret/candidate/handles, stable range, no fabricated browser-only platform pass |

## Native accessibility and locks — IOS-1.16, AND-1.16, DSK-1.16, WIN-1.16, LNX-1.16, FIT-1.8

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| NAT-13 | P0 | Accessibility range/geometry requests after edit, bidi movement, zoom/scroll | Correct current text/ranges/bounds and available actions without repeated whole-document work |
| NAT-14 | P0 | Reentrant text-service query/update under native lock while async feature completes | Follow native lock/thread protocol; no deadlock, recursive commit or blocked input; capture real native trace |

## Performance and resource boundaries — FIT-1.8, RCH-1.20, MWB-1.9, MWX-1.8

| ID | Priority | Setup and action | Required result |
|---|---|---|---|
| PRF-01 | P0 | Same typing/composition replay at several document sizes with baseline and official presets | Input-to-visible samples plus engine/FFI/render breakdown meet preregistered budgets; source/hardware/profile fixed |
| PRF-02 | P0 | Continuous range selection, text drag, nested autoscroll at actual refresh rate | Separate frame/long-task evidence; bounded per-frame geometry, no full-doc hit-test scan; cancel stops scheduling |
| PRF-03 | P0 | Search/highlighting plus edits, collaboration burst and stale result storm | Bounded queues/cancellation and changed-region invalidation; no waterfall commits or synchronous optional input work |
| PRF-04 | P0 | Very long logical line, large table/selection, images and bidi | Exact workload/size limits, memory peaks and tail latency; no silent truncation to pass |
| PRF-05 | P0 | Repeated mount/dispose and feature unload during canceled transfer | Listener/worker/observer/request counts bounded; memory plateau under fixed replay, no idle polling |
| PRF-06 | P0 | Pack baseline and presets from clean external consumer, cold/warm load | Existing bundle/startup budgets retained; disabled optional modules absent from import/evaluation traces |
| PRF-07 | P0 | Same native/mobile scenario with keyboard, IME, accessibility client and thermal metadata | Actual-device response/candidate geometry/frame evidence; browser measurements cannot substitute; unavailable devices block support claim |
