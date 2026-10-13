# Touch interaction and mobile extension research

Research date: 2026-10-11. This is source review and proposed future acceptance work, not executed browser/device evidence or a claim of edit.ac support. No runtime changes, provider calls, paid inference, automated device tests, or live-content dogfood were performed for this research.

## Findings from primary sources

| Source | What the source establishes | Consequence for planned work |
|---|---|---|
| [Pointer Events Level 3][pe] — W3C Recommendation, 2026-06-30; sections 4, 8, 9 | `touch-action` governs browser panning/zooming, not text selection or link activation. Ancestors participate in its decision; changing it after the gesture starts does not change that gesture. Direct-manipulation inputs can have implicit capture. Stream suppression sends `pointercancel`; capture is released after cancellation or pointer-up. | Preserve native interaction on text. Scope gesture policy to explicit extension controls before a gesture starts. Treat cancellation/capture loss as ordinary lifecycle exits. |
| [DOM Standard][dom] — event listeners and cancellation | Passive listeners cannot cancel default actions. Some document-level touch/wheel listeners default to passive. Listener removal can be tied to an abort signal. | Specify listener options deliberately. Avoid installing document-wide non-passive cancellation to make a particular handle work; dispose listeners with their owner. |
| [Media Queries Level 4][mq] — interaction media features | `pointer`/`hover` describe the primary pointer; `any-pointer`/`any-hover` describe available pointers. These queries do not establish whether a keyboard exists. Primary-device classification can change. | Adapt affordance size/visibility without permanently selecting a “mobile input mode.” A tablet may use finger, pen, trackpad and keyboard in one session. |
| [Selection API][selection] — editor's draft, event scheduling | Selection changes schedule `selectionchange`; queued notifications can be coalesced. The document event does not bubble and is not cancelable. | Read actual current selection when reconciling it. Do not infer the selection solely from pointer event counts or assume a handle drag supplies ordinary DOM pointer events. |
| [Safari 27.0 release notes][webkit27] — WebKit, 2026-09-17 | WebKit reports a fix for JavaScript touch handlers preventing selection-handle adjustment on some websites, reference 151851274. | Include native-handle tests with all extensions enabled. The release note establishes a historical failure class, not success on every Safari build or embedded WebKit host. |
| [Apple system-selection guidance][apple-selection] — UIKit | Apple describes adopting system selection UI, including selection handles and the loupe, in custom native text views. | Native clients should qualify their platform selection integration separately. UIKit APIs are not browser DOM capabilities, and native success does not qualify a WKWebView editor. |
| [WCAG 2.2 SC 2.5.8 explanation][wcag-target] — informative interpretation of normative criterion | AA target minimum is 24 × 24 CSS pixels, with spacing, equivalent-control, inline, user-agent-control and essential exceptions. | Record the actual hit area and any justified exception. Do not describe the minimum as an ideal target size for every mobile control. |
| [WCAG 2.2 SC 2.5.7 explanation][wcag-drag] — informative interpretation of normative criterion | Author-controlled dragging needs a single-pointer alternative without dragging, unless an exception applies. Keyboard equivalence alone does not provide that pointer alternative. | Reorder, table sizing and media sizing need tap-operable alternatives. Keep keyboard commands too. Native selection handles are distinct from author-built drag controls. |
| [HTML file input][files] — living standard | File inputs represent user-selected files. `accept` is a file-type hint, not validation. Picker interactions can end without selection. | Provide a reachable file-picker path; validate ingestion independently of the picker hint. Canceling must not create a document edit or an orphan upload placeholder. |
| [Clipboard API and events][clipboard] — published draft | Synthetic clipboard events do not change the system clipboard or perform a real paste. Clipboard access is subject to user-gesture/permission rules. | Keep native paste as a first-class route. Fixture-based ingestion tests and real OS clipboard qualification must be reported separately. Handle refused access without losing the selection or content. |

These consequences are design recommendations inferred for edit.ac. Standards describe API contracts; they do not establish which combinations of OS, browser, keyboard, embedding host and editor extensions have passed this project's acceptance tests.

## Editor ecosystem evidence

| Source inspected on 2026-10-11 | Observed status and scope | Use in our future test corpus |
|---|---|---|
| [Tiptap issue #6276][tiptap6276], filed 2025-04-16 | Open in the inspected issue. The reporter describes native text selection on iPhone/Android overlapping nearby controls and conflicts with fixed menus. The “all” version field is the reporter's assertion; it is not a verified affected-version range. | Select text, scroll it under fixed/floating controls, adjust handles, then invoke an external button. Verify that the selected range remains meaningful and both native and app actions remain reachable. Do not claim the problem is a simple DOM `z-index` defect merely because the report describes it that way. |
| [Lexical issue #4941][lexical4941], filed 2023-08-30 | Closed in the inspected issue. The original report names Lexical 0.11.3/0.12.0 and Chrome Android: repositioning the caret inside a word then backspacing removed two characters. This research did not establish a fixing release or verify present-day reproduction. | Add a touch-caret-placement followed by software-keyboard deletion case, including after toolbar dismissal. Closed status does not replace a regression test and does not imply a current Lexical defect. |
| [Tiptap drag-handle documentation][tiptap-drag] | Documents a separate extension with rendered handles, placement configuration and drag callbacks. The inspected documentation is not mobile-device qualification evidence. | Useful separation precedent: keep handle presentation and drag negotiation outside the portable mutation model. |
| [Tiptap table documentation][tiptap-table] | Documents a table extension with resizing configuration and semantic row/column operations. | Provide tap commands for the same semantic operations instead of making narrow resize boundaries or dragging the only controls. |
| [Tiptap slash-menu documentation][tiptap-slash] | Documents a separately configurable menu with enabled/custom items and selection callbacks. No mobile guarantee follows from the API description. | Treat menus as optional presenters over existing commands, with a touch-discoverable entry point in addition to `/`. |
| [Tiptap FileHandler documentation][tiptap-files] | Handles file paste/drop events and allowed types; explicitly does not implement server uploads. Its `consumePasteEvent` option addresses duplication when clipboard data includes both files and HTML. | Separate ingest arbitration, document insertion, presentation and transport. Use mixed HTML/file fixtures to require one intended insertion. |

Issue reports are regression inspiration, not an editor ranking or a browser-support survey. Reproduction and exact version scope remain future work. No current incompatibility of ProseMirror, Slate, Tiptap or Lexical is inferred from the absence of a report in this table.

## Small-core and extension boundary

The following is a proposed ownership split for the authoritative specs and roadmaps to adopt or refine.

| Layer | Responsibility | Boundary to preserve |
|---|---|---|
| Portable semantic engine | Existing document edits, selection/anchor transformations, command availability, history and deterministic results. | No browser pointer events, touch thresholds, hover detection, CSS policy, viewport geometry, OS menus or upload transport in Rust. |
| Required browser adapter | Native text editing and selection reconciliation; focus/composition lifecycle; safe baseline paste; position mapping; disposal; preserving browser scroll, zoom and native menu access. | Baseline editing must work with every optional interaction extension absent. Native selection is not an optional enhancement. |
| Shared host hooks | Selection snapshots/anchors, command execution, current geometry and lifecycle invalidation, host capability reporting. | Reuse the existing extension contracts; do not create a parallel “mobile document” or duplicate transaction/history pipeline. Geometry is transient host data. |
| Optional interaction presenters | Slash/insert menu, fixed/bubble formatting toolbar, block handles and reorder UI, table cell menus/resize UI, image/media controls. | Each invokes semantic commands, declares supported inputs and provides accessible pointer/keyboard routes. Enable/disable must release listeners, capture, overlays and pending actions. |
| Optional media service | File-picker, paste/drop ingestion, validation, local previews, prepared upload transport, retry/cancel states. | A file event is not a completed upload. Platform availability, denial and cancellation are explicit; lifecycle completion cannot insert into a disposed editor or deleted destination. |
| Native client adapters | System text-selection UI, platform menus, drag/drop and picker integrations, platform accessibility. | Qualify UIKit/AppKit/Android/desktop implementations independently from browsers. Native APIs do not belong in the portable engine. |

Further proposed rules:

- Keep the text surface's ordinary scroll, pinch zoom, long-press selection and context menu available. A custom gesture starts only from an explicit eligible affordance and has an abort path before commit.
- Prefer high-level button activation for commands. Low-level gesture handling must not make synthetic mouse events trigger a second command after a touch activation.
- Save a semantic selection/anchor before focus moves to a toolbar or picker. Revalidate it before applying the action; stale, deleted or read-only destinations fail safely instead of editing whichever selection happens to be current.
- Do not require hover to reveal the only insert, reorder, table or media action. Adapt presentation to viewport and input capability while keeping mixed input usable.
- Keep platform-specific thresholds, long-press durations and toolbar placement provisional until physical-device qualification. An arbitrary universal threshold is not a cross-platform contract.

## Proposed acceptance rows

Every row below is **planned; not run**. “Fixture” means deterministic DOM/transport/geometry fixtures. “Device” means observed physical-device interaction; emulation alone cannot close it. The complete recording envelope belongs in the parent qualification plan: exact OS/build, browser/build or webview host, hardware, pointer, keyboard/IME, screen orientation, viewport/zoom, enabled extensions and accessibility settings.

| ID | Scenario | Required observable result | Minimum evidence |
|---|---|---|---|
| TX-01 | Finger tap at start/middle/end of text, then type and backspace; repeat near checkbox, inline atom and block boundary. | Caret reflects the intended location; one ordinary deletion has one semantic effect; no duplicate touch/mouse command. | Fixture event reconciliation plus iOS and Android device capture. |
| TX-02 | Long-press select, drag both native handles across styled text, links, empty paragraphs and block boundaries. | Selection remains coherent and editable; custom controls do not capture native handle interaction. | Device video and before/after semantic selection, with extensions absent and enabled. |
| TX-03 | Open native copy/cut/paste menu; scroll selected text beneath a fixed or bubble toolbar; dismiss and resume typing. | Native actions and app controls remain reachable; no stuck overlay, unintended focus jump or lost selected content. | Device capture for each shipping toolbar layout. |
| TX-04 | Start vertical page/editor scrolling and pinch zoom from text, then near a handle and within a horizontally scrollable table. | Each region has a documented gesture policy; ordinary reading/selection remains possible and nested scrolling does not mutate the document. | Device capture plus inspected `touch-action` ancestry. |
| TX-05 | Begin a custom drag, then induce `pointercancel`, capture loss, target removal, editor disposal and a second competing pointer. | Preview/capture/listeners clear; canceled action does not commit; next interaction works. | Deterministic lifecycle fixtures; device checks for cancellation paths the platform can produce. |
| TX-06 | Run touch, stylus and trackpad/mouse consecutively, with a hardware keyboard attached and removed. | Commands remain reachable; pointer identity and buttons do not leak between gestures; no reload or permanent input-mode switch is needed. | Hybrid physical-device session; fixture capability-change assertions. |
| TX-07 | Scroll during touch movement with extension listeners installed; mount/unmount each extension repeatedly. | No unnecessary document-wide scroll cancellation; passive policy is explicit; unmount removes owned listeners/overlays and leaves editing usable. | Listener/cleanup fixture plus device scroll observation. |
| TX-08 | Open slash menu by typed `/` and a touch-visible insert control; filter while IME composition is active; scroll/tap results. | Composition is not prematurely committed; exactly one selected command applies; menu dismissal preserves ordinary input. | Mocked deterministic suggestions; device IME and tap capture. |
| TX-09 | Select text, invoke mark/link controls, edit a toolbar field, cancel/commit, then resume typing. | The action applies to its validated selection once; keyboard visibility/focus follows the declared workflow; cancel preserves content. | Fixture anchor revalidation plus device keyboard/selection capture. |
| TX-10 | Open menus near each viewport edge with software keyboard visible; rotate or resize during the interaction. | Current command, dismissal and caret remain reachable; no overlay covers its only recovery control or leaves a stale hit target. | Geometry fixtures plus portrait/landscape device capture. |
| TX-11 | Operate all compact toolbar, table, reorder and media targets using a finger. | Measured hit regions satisfy the selected WCAG target rule or record the exact applicable exception; nearby controls do not activate accidentally. | Hit-area measurements and device trials; no blanket compliance claim from target size alone. |
| TX-12 | Reorder a block by handle drag and by tap-only Move before/after or destination menu; undo/redo each. | Both paths produce equivalent semantic edits and history; drag cancellation preserves the original order and selection. | Semantic equivalence fixtures and device single-pointer path. |
| TX-13 | Choose a table cell, edit text, change selected cells through explicit controls, add/delete row/column and resize. | Text selection, table selection and table scrolling are distinguishable; resize has a tap-operable width/menu alternative; no accidental cell edit. | Table fixtures and physical touch/pen trials. |
| TX-14 | Select media, edit caption/alternative text, resize and use tap size presets or numeric controls. | Selection stays attached to the intended node; handles do not prevent reading/scrolling; alternate controls reach the same supported outcomes. | Deterministic command fixtures and device controls. |
| TX-15 | Insert via the system file picker; cancel; choose multiple allowed and rejected files; repeat with picker unavailable. | Cancel changes nothing; validation is independent of `accept`; rejection explains recovery; unavailable capabilities have a reachable alternative. | Prepared files/transport and actual device picker observation. |
| TX-16 | Paste plain text, HTML, image/file, and combined HTML+file representations from the native menu and keyboard shortcut. | Ingestion chooses one intentional result; sanitation/format policy is consistent; file+HTML does not duplicate insertion; denial leaves existing content intact. | Deterministic payload corpus plus separately recorded OS clipboard trials. |
| TX-17 | Start media insertion, move/delete the destination, toggle read-only, dispose the editor, then resolve prepared asynchronous work. | Completion revalidates identity/policy; no insertion into the wrong destination, resurrected editor or deleted block; preview resources are released. | Mocked transport and deterministic race fixtures only. |
| TX-18 | Activate slash, toolbar, table, media and reorder actions with keyboard and screen reader; repeat the non-drag route by single-pointer taps. | Labels, focus return and action state are understandable; functionality does not depend on hover, drag or an unseen gesture. | Accessibility tree/keyboard checks plus named platform assistive-technology session. |
| TX-19 | Disable every optional interaction extension and repeat ordinary typing, selection, scrolling, zoom and native clipboard operations. | Baseline editing remains usable; no optional package owns indispensable native selection/focus behavior. | Minimal consumer fixture plus representative physical devices. |

Automation may validate semantic state, cancellation, event deduplication, disposal and prepared media transport. It must not label constructed pointer/clipboard events as proof of native menus, handle dragging, keyboard behavior, palm rejection or system permission flows. Unsupported/unavailable device paths must be recorded as skipped with a reason, not as passes. This research has zero executed/passed/failed/skipped test cases; it defines future tests only.

## Sources

[pe]: https://www.w3.org/TR/2026/REC-pointerevents3-20260630/
[dom]: https://dom.spec.whatwg.org/#dom-addeventlisteneroptions-passive
[mq]: https://www.w3.org/TR/mediaqueries-4/#mf-interaction
[selection]: https://w3c.github.io/selection-api/#selectionchange-event
[webkit27]: https://webkit.org/blog/18325/webkit-features-for-safari-27-0/
[apple-selection]: https://developer.apple.com/documentation/uikit/adopting-system-selection-ui-in-custom-text-views
[wcag-target]: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
[wcag-drag]: https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html
[files]: https://html.spec.whatwg.org/multipage/input.html#file-upload-state-(type=file)
[clipboard]: https://www.w3.org/TR/clipboard-apis/
[tiptap6276]: https://github.com/ueberdosis/tiptap/issues/6276
[lexical4941]: https://github.com/facebook/lexical/issues/4941
[tiptap-drag]: https://tiptap.dev/docs/editor/extensions/functionality/drag-handle
[tiptap-table]: https://tiptap.dev/docs/editor/extensions/nodes/table
[tiptap-slash]: https://tiptap.dev/docs/ui-components/components/slash-dropdown-menu
[tiptap-files]: https://tiptap.dev/docs/editor/extensions/functionality/filehandler
