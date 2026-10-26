# ProseMirror input and keyboard comparison

Reviewed 2026-10-26. This is an authored source comparison and follow-up plan, not a claim of editor or operating-system qualification. Implementation is assigned in the [input follow-up plan](../runner-queues/prosemirror-input-20261026/README.md), extended by the [additional open-source editor review](open-source-editor-input-20261026.md). No runtime source, live runner source, queue, progress receipt or canonical product-track count changes here.

## Scope and evidence

Compared ProseMirror's browser adapter, command chains, keymap, input rules and table helpers with edit.ac's browser input, selection, Markdown shortcuts and current addressed-table presenter. Native SDKs and the terminal were not re-audited; existing ES/EDX owners retain those obligations.

The local basis is the working tree over core `a52882953875a8a3a28f17b33c821f779a76612c` and architecture `def1ab3cbac2f86be1f18ad9d1112a02755a7b84`. Both contained extensive pre-existing changes; these commit IDs alone do not reproduce the inspected source. Reauthenticate the named symbols before implementation. Codanna MCP and CLI were unavailable, so discovery used focused source searches.

Eight small Chromium probes exercised the current TypeScript adapter code with a mocked engine or minimal DOM. They observed: the extra Tab target, nested-control undo interception, stale table Escape, table whitespace inheritance, a lone-BR reader result, keyCode 229 reaching Enter resolution, missing Primary+Enter resolution and missing non-Latin Primary+Z resolution. These establish adapter decisions only. They do not establish real IME event ordering, semantic engine transactions, persistence, Firefox/WebKit behavior or physical keyboard support. The probe scaffold required one correction to provide the render method's element context; the corrected probe completed. No paid inference was used. Generated probes and downloaded source are temporary, outside Git.

## Upstream mechanism and intentional differences

| Layer | ProseMirror reference | Consequence for this review |
| --- | --- | --- |
| Enter and deletion | [commands at 52a84a8](https://github.com/ProseMirror/prosemirror-commands/blob/52a84a842774fadec3b167bcdbd56085ec6c85df/src/commands.ts): `pcBaseKeymap`, `newlineInCode`, `createParagraphNear`, `liftEmptyBlock`, `splitBlock`, `exitCode`, backward/forward command chains | Commands try applicable structural operations before native fallback. There is a keyboard route out of code and a paragraph-near-node route. These are useful comparison points, not permission to replace our engine semantics. |
| Browser repair | [input at ca4c78e](https://github.com/ProseMirror/prosemirror-view/blob/ca4c78e9b56f1b164c0b3758b59d8748f11b7534/src/input.ts), [DOM changes](https://github.com/ProseMirror/prosemirror-view/blob/ca4c78e9b56f1b164c0b3758b59d8748f11b7534/src/domchange.ts) | Near-composition handling and Android/iOS Enter paths differ from ordinary desktop keydown. DOM changes can be recognized as structural intent. Copy only a workaround justified by a reproduced event sequence. |
| Selection repair | [capturekeys at ca4c78e](https://github.com/ProseMirror/prosemirror-view/blob/ca4c78e9b56f1b164c0b3758b59d8748f11b7534/src/capturekeys.ts): `selectHorizontally`, `selectVertically`, ignored-node skipping | Native visual movement is supplemented at atom, node-selection and decoration boundaries. Blanket native ownership needs evidence at those boundaries. |
| Shortcut normalization | [keymap at d60e244](https://github.com/ProseMirror/prosemirror-keymap/blob/d60e2447d63374d7612121675e9e7fa9ccfb2eb0/src/keymap.ts): `keydownHandler` | Modified character bindings have shifted-name and key-code fallback, with a Windows Ctrl+Alt exclusion for AltGr. Our fallback must respect layout, host reservations and composition. |
| Optional schema bindings | [example setup at b6fcf7a](https://github.com/ProseMirror/prosemirror-example-setup/blob/b6fcf7aed86a682bdcf91df7a85a770ab8ae7179/src/keymap.ts), [lists at 1501619](https://github.com/ProseMirror/prosemirror-schema-list/blob/15016199fc6defd2a605466f4ebffb4ef128620a/src/schema-list.ts) | Example setup adds schema-specific bindings. In particular, its Shift+Enter behavior can exit code; edit.ac deliberately requires literal LF for both Enter and Shift+Enter in code. Keep our selected contract. |
| Input rules | [inputrules at e3e5545](https://github.com/ProseMirror/prosemirror-inputrules/blob/e3e5545f21d8ff4050be6f3134d653dc087918d3/src/inputrules.ts) | Rules are a separate optional input layer with composition/code restrictions and undo support. Their precedence must not defeat a reserved key or explicit break command. |
| Tables | [table input at eb522f2](https://github.com/ProseMirror/prosemirror-tables/blob/eb522f25959a1e4515a4ff5ce7e3a939f19c55e9/src/input.ts), [commands](https://github.com/ProseMirror/prosemirror-tables/blob/eb522f25959a1e4515a4ff5ce7e3a939f19c55e9/src/commands.ts): arrow handlers and `goToNextCell` | Cell and document selection have separate applicability. Tab is not a universal ProseMirror base binding; consumers configure it. Our paragraph/list/code Tab behavior and last-cell row creation are product choices, not defects merely because they differ. |
| Whitespace | [view CSS at ca4c78e](https://github.com/ProseMirror/prosemirror-view/blob/ca4c78e9b56f1b164c0b3758b59d8748f11b7534/style/prosemirror.css) | ProseMirror establishes whitespace-preserving presentation. Every editable scope in our editor must preserve authored spacing independently of an accommodating host stylesheet. |

## Concrete gaps

“Observed” below means the bounded adapter probe above. “Source” means a reachable branch was traced but the full user interaction was not executed. Priorities describe follow-up order, not measured incident frequency.

### F01 — Shift+Enter and reserved keys can lose to typing rules — P1, source

In [`TextInput` event routing](../../core/packages/web/src/input/text.ts), `#eligibleKey` admits Enter without excluding Shift. The fence `shortcuts.convert(range, '\n', ...)` call occurs before `KeyboardInput.action`. [`TypingShortcuts.convert`](../../core/packages/markdown/src/shortcuts.ts) accepts a fence followed by LF without knowing the chord. Thus a plain paragraph containing a Markdown fence can convert on Shift+Enter instead of retaining the paragraph and inserting a break. Enter reservations/remaps and Backspace rule reversal also need precedence checks because they are consulted later.

Reproduce with a collapsed caret after three backticks, Markdown enabled, then Shift+Enter; compare plain Enter, reserved/remapped Enter and immediate Backspace after a conversion. Fix owner: **PKI-1.1**. Preserve existing direct-key-only and code-literal policy; do not turn pasted fences or IME completion into conversions.

### F02 — Tab includes a block touched only by the selection endpoint — P1, observed

[`KeyboardInput.execute`](../../core/packages/web/src/input/keyboard.ts) uses `nodes.slice(si, ei + 1)` for list/prose indentation. A range from paragraph A offset 1 to paragraph B offset 0 produced indent commands for both A and B. The code-line branch already excludes the following line when selection ends at its start; the block branch has no equivalent exclusion.

Fix owner: **PKI-1.2**. A noncollapsed half-open range must indent only intersected blocks in either selection direction. Cover paragraph/list/code combinations, a caret at offset zero, outdent, min/max indentation and preservation of selection direction. Do not silently mutate the applicable subset of an otherwise invalid mixed target.

### F03 — Table shortcuts intercept nested native controls — P1, observed

[`CurrentTableView.keyboard`](../../core/packages/web/src/modules/tables/current.ts) processes history before checking the event target. Primary+Z in the “Table cell link” URL input called semantic engine history once and prevented the event. It should undo the field's text. The handler also hardcodes Primary+Y and does not consume the root shortcut profile; root [`TextInput`](../../core/packages/web/src/input/text.ts) already has a native-control exclusion.

Fix owner: **PKI-2.1**. Resolve focus owner before history, selection or navigation; maintain platform redo policy and host reservations without stealing toolbar input, checkbox or button behavior.

### F04 — Table Escape remains armed after navigation — P1, observed

The same table handler clears `escape` on cell beforeinput/compositionstart or a consuming Tab, but not on Arrow movement or blur. Escape, ArrowRight, Tab in a cell moved focus outside the editor in the probe instead of to the next cell. The root `KeyboardInput.action` already resets its one-shot escape on intervening intent and preserves modifier-only Shift.

Fix owner: **PKI-2.1**, alongside F03 in the same routing boundary. Check Escape → Shift → Shift+Tab, Escape → arrow → Tab, blur/refocus, pointer relocation and IME Escape. A fresh direct Escape → Tab must still leave the editor.

### F05 — Table prose loses visible whitespace preservation — P1, observed

[`CurrentTableView.render`](../../core/packages/web/src/modules/tables/current.ts) emits text nodes in `p`/heading elements without a whitespace policy. [`DOMRenderer.#update`](../../core/packages/web/src/dom/render.ts) returns for content views before assigning its ordinary `break-spaces` style. In a normal unstyled host the table paragraph computed to `white-space: normal`; stored `a  b\nc` remained exact in `textContent` but displayed with collapsed spacing/breaks. This is a display/input-position risk, not an observed storage loss.

Fix owner: **PKI-2.2**. Apply the existing prose/code whitespace contract inside cells and qualify trailing LF/empty-line caret mapping. [`cellDOMText`](../../core/packages/web/src/modules/tables/cell-dom.ts) also treats every sole BR in an element as empty; the probe confirmed that branch. Establish filler provenance before changing it: an authored LF must count once and a browser filler zero times. No blanket NBSP/ZWSP replacement or Unicode normalization.

### F06 — Noncancelable table Enter still commits synchronously — P1, source

The table `beforeinput` branch calls `preventDefault()` and `insert(cell, '\n')` for both break types without checking `cancelable`. A noncancelable event can therefore continue its native edit after a semantic insertion. The following `input` handler then reconciles DOM content. Duplicate insertion or canonical restoration is a risk requiring a mounted sequence; neither was claimed as reproduced. Root `TextInput` explicitly distinguishes cancelable commands and native fallback.

Fix owner: **PKI-2.3**. One event sequence must have one owner and at most one accepted transaction; correlate its later input/mutations. Preserve selected text, history and recovery when browser structure is unsupported.

## Behavior and browser gaps requiring targeted qualification

### R01 — Near-composition confirmation and unknown-key signals — P1

[`CompositionInput`](../../core/packages/web/src/input/composition.ts) releases an unheld commit key at a MessageChannel boundary; existing tests cover same-dispatch end-before-key and explicitly expect the next dispatcher Enter to be independent. ProseMirror has a Safari-specific near-composition path. Our `KeyboardInput.action` probe also resolved Enter with keyCode 229 and `isComposing: false` to `enter`. These are concrete routing observations, not proof that every such event is an IME confirmation.

**PKI-1.3** must reproduce delayed confirmation versus a genuinely new Enter, including pointer candidate confirmation, missing keyup, Dead/Process/Unidentified, repeat and table-cell composition. Use correlated evidence; a blanket timeout that eats deliberate Enter is not acceptable. Cross-block IME staging remains **ES-1.4**, not new work here.

### R02 — Mobile or non-keyboard Enter lacks a bounded structural fallback — P1

Root [`TextInput`](../../core/packages/web/src/input/text.ts) eagerly runs physical Enter commands. Noncancelable structural beforeinput bypasses that command path; [`reconcileMutation`](../../core/packages/web/src/input/reconcile.ts) rejects added elements and multi-owner changes. ProseMirror has specific Android/iOS routes and recognizes bounded DOM shapes as Enter. This source difference needs runtime sequences, not copied browser sniffing.

**PKI-1.4** owns Enter with absent keydown, noncancelable beforeinput, missing inputType, delayed input and native paragraph/BR creation. A recognized gesture gets one prepared split/break and a correct caret; unrecognized changes retain recovery without partial mutation. Actual virtual-keyboard behavior remains a target-runtime qualification requirement under MWB/roadmap43.

### R03 — Layout-dependent shortcuts have no guarded fallback — P2, observed resolution gap

[`KeyboardInput.action`](../../core/packages/web/src/input/keyboard.ts) builds chords only from `event.key`. The probe's Primary+Z physical key with a Cyrillic `key` resolved to no command. ProseMirror keymap has modifier-aware fallback. **PKI-1.5** defines and implements our supported layout profile, respecting explicit host mappings, AltGraph/Ctrl+Alt, dead keys, composition and browser shortcuts. Do not replace normal text input with US key-code assumptions.

### R04 — Keyboard exit from terminal code/atoms is not explicit — P2, product gap

The [`command catalog`](../../core/packages/web/src/commands/catalog.ts) has no exit-code/paragraph-near-node action; Primary+Enter resolved to no command. Root Enter handles a text target; explicit selected-node handling is deletion-only. Users of a last code block or noneditable block need a discoverable way to continue prose without a pointer. Existing Insert after actions are reusable primitives.

**PKI-2.4** adds a documented keyboard continuation command using the existing prepared block-action path. Keep ordinary Enter/Shift+Enter in code as literal LF. Define selected-atom behavior explicitly rather than fabricating a text caret inside an atom. This is an additive product decision in the task, not a claim that ProseMirror's complete binding set is mandatory.

### R05 — Visual navigation at atoms relies on the browser alone — P2

[`DOMSelection.trackNativeMovement`](../../core/packages/web/src/dom/selection.ts) repairs grapheme cuts for plain horizontal arrows; `KeyboardInput.navigate` owns Select All only. Adjacent-atom handling is currently deletion-oriented. ProseMirror has additional horizontal/vertical node-selection and ignored-decoration repair. **PKI-2.5** measures arrow entry/exit from an atom selection and wrapped/bidi/decorated boundaries, implementing only demonstrated repairs. Preserve native visual movement, Shift anchor direction and zero semantic writes. Optional `Segmenter`/`Selection.modify` guards remain **ES-1.2**; block selection UI remains **ES-3.1/3.2**.

### R06 — Modified deletion at structural boundaries needs an owner — P1 risk

Root key routing leaves modified Backspace/Delete native. Reported beforeinput ranges can already perform compatible cross-block replacement, so the normal path must be retained. If those ranges are absent and native deletion changes block structure, the bounded DOM reconciler can reject it. ProseMirror's modified deletion chain first tries structural deletion/join/node selection.

**PKI-2.6** covers Control/Option/Command deletion at paragraph/list/quote/code/atom boundaries with and without target ranges, preserving native word/line behavior inside text and safe refusal at unsupported boundaries. A failed join must not leave a changed DOM, partial semantic edit or wrong history target.

## Coverage and reuse

Existing literal ingress checks in `input/characters.ts`, ordinary renderer whitespace, code literal LF, reported deletion/replacement ranges, selection history, composition buffering and explicit Escape → Tab are strengths to preserve. Do not reimplement them to resemble ProseMirror.

The [editing standards plan](../runner-queues/editing-standards-20261024/README.md) already owns Unicode-profile publication, optional browser API fallbacks, cross-block composition, language/direction, terminal navigation and block selections. The [editing experience plan](../runner-queues/editing-experience-20261024/README.md) owns shared history, ordinary breaks and native delivery. Its completed tasks are not reopened by this supplement. Reuse current-source receipts and add only uncovered assertions.

Final coverage has one owner per finding in the new plan. Include positive and negative controls: literal spaces, repeated/leading/trailing spaces, TAB, NBSP, narrow NBSP, ZWSP, combining marks, emoji/ZWJ, LF/CRLF import, mixed marks, empty owners, forward/backward selections, repeated keys, host reservations, nested controls, read-only state and composition. A synthetic event pass does not establish an OS IME, keyboard layout or mobile keyboard claim.
