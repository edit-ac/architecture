# Native editing research: text services and desktop expectations

Research date: 2026-10-12. This is source research and proposed acceptance detail,
not implementation, execution evidence or a support claim. It extends the existing
[native contract](../specs/native-sdk-parity.md), [interaction contract](../specs/editor-interactions.md)
and platform tracks; it creates no roadmap or alternate editor architecture.

The existing contracts already require selection replacement, native composition,
dictation, Unicode-safe navigation, accessible commands, shared undo and real-device
qualification. The gaps below make less obvious platform behavior testable rather
than restating those requirements. “Owner” names existing tasks that can absorb the
detail. Platform availability must be pinned to the supported OS/toolkit versions;
current documentation, including GTK development documentation, is not evidence that
an API exists in the chosen minimum deployment target.

## Text services need protocol-specific cases

| Additional case | Required observation and boundary | Existing owner |
| --- | --- | --- |
| Android surrounding-text deletion with a nonempty selection | Exercise both `deleteSurroundingText` and `deleteSurroundingTextInCodePoints` with emoji on both sides of the selection. The former counts Java characters; the latter counts code points, excludes the selected range, and rejects invalid surrogate pairs as documented. Do not route either through a generic “delete selection” shortcut or assume either unit is a grapheme. Convert the protocol operation to the shared command without duplicating it. | AND-1.4, AND-1.5, AND-1.6 |
| Android composition/batch callbacks after editor replacement | Start an input batch, change the active view/session, then deliver old input callbacks and a handwriting completion. Verify the old connection cannot edit the new document, leave the new view in a batch, or report success for rejected work. Test nested batch completion separately from the engine's semantic undo boundary. | AND-1.3, AND-1.6, AND-1.14 |
| GTK surrounding context has three coordinate systems | Exercise accented UTF-8, supplementary emoji and reversed selection. Surrounding-text cursor/anchor indices are byte offsets; `delete-surrounding` uses character offsets/counts; the engine uses its qualified UTF-16 mapping. Exclude provisional preedit from the supplied surrounding text and convert each API at its own boundary. | LNX-1.4, LNX-1.6 |
| Windows reconversion of already committed text | Select existing Japanese text, invoke a supported IME's reconversion, change candidate, then separately commit and cancel. Include remote changes outside and overlapping the selected range. A replacement must target the captured range and preserve shared history; reconversion must not be treated as fresh typing at an unrelated caret. | WIN-1.6, WIN-1.7; actual input DEL-1.7 |
| Windows text-service reentrancy | During text/selection notification, request another read/lock and enqueue a remote patch. Verify no deadlock, recursive duplicate edit or inconsistent snapshot. If the chosen native control owns TSF, qualify its observable adapter behavior; implement a custom TSF text store only if the feasibility task proves one necessary. | WIN-1.2, WIN-1.4, WIN-1.6 |

Android documents the distinct deletion units, composing/batch lifecycle and invalidated
connection results in [InputConnection](https://developer.android.com/reference/android/view/inputmethod/InputConnection).
GTK specifies byte-based cursor and selection indices, with preedit excluded, in
[set_surrounding_with_selection](https://docs.gtk.org/gtk4/method.IMContext.set_surrounding_with_selection.html),
and character-based removal in [delete-surrounding](https://docs.gtk.org/gtk4/signal.IMContext.delete-surrounding.html).
Windows exposes range-based reconversion through
[ITfFnReconversion](https://learn.microsoft.com/en-us/windows/win32/api/ctffunc/nn-ctffunc-itffnreconversion).
Its [RequestLock contract](https://learn.microsoft.com/en-us/windows/win32/api/textstor/nf-textstor-itextstoreacp-requestlock)
forbids document mutation/change notification inside the request itself, and
[OnTextChange](https://learn.microsoft.com/en-us/windows/win32/api/textstor/nf-textstor-itextstoreacpsink-ontextchange)
distinguishes application changes from edits made through text-store interfaces.
These sources justify targeted adapter tests, not a requirement to build a second
input subsystem around a stock native control.

## Handwriting is more than recognized text insertion

Android's [custom editor handwriting guide](https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/custom-text-editors)
distinguishes gesture execution, display-only previews, cancellation, fallback text
and cursor/visible-line geometry. Stock text fields and custom text surfaces have
different integration work. New AND-1.6 acceptance should exercise:

- Select/delete/insert gestures over text, whitespace, wrapped lines, table cells
  and adjacent atomic attachments; advertise only the supported gesture set.
- Cancel a gesture preview, then compare document, semantic selection and undo
  depth with their pre-preview values. Preview must not commit an operation.
- Fail a gesture hit test and apply its provided fallback text exactly once;
  cancellation or an invalidated connection must not replay that fallback later.
- Scroll or resize between preview and completion; update geometry and reject a
  stale target instead of applying the gesture to the old screen coordinates.
- Start handwriting within a nested scroll view; qualify stylus-vs-scroll ownership,
  focus and connection state on the actual device/IME combination.

IOS-1.6 should similarly qualify Scribble on the actual editable text surface and
cell/attachment boundaries. Apple's [UIScribbleInteraction](https://developer.apple.com/documentation/uikit/uiscribbleinteraction)
customizes or suppresses Scribble for text-input views;
[UIIndirectScribbleInteraction](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteraction)
is for views that look editable but do not implement `UITextInput`. Do not add the
indirect interaction to every attachment or create a second input owner when the
qualified native text control already handles handwriting. IOS/AND-1.16 own the
accessible alternative, and DEL-1.7 owns actual device evidence. Browser handwriting
traces or prepared transcripts cannot substitute for either native platform.

## Desktop text commands and transfer routes

| Additional case | Acceptance addition | Existing owner |
| --- | --- | --- |
| Native Find and Replace | Find may select/scroll in read-only mode; Replace/Replace All must obey shared applicability, current document identity and history. Search UI focus and dismissal preserve the appropriate editor selection. Native search must not directly rewrite projected text or bypass codec/schema rules. Host chooses how commands appear in menus. | IOS/DSK/WIN/LNX-1.7 and -1.16; native -1.4 for result ranges |
| AppKit smart insertion/deletion and substitutions | Test prose with smart spacing, quotes/dashes and configured substitutions enabled and disabled, including cut, drag, paste and immediate undo. Record whether the native operation expanded its replacement range. Preserve the OS-committed text exactly once. Code/literal profiles must not silently acquire prose substitutions; a programmatic remote patch must not trigger local correction. | DSK-1.5, DSK-1.6, DSK-1.7, DSK-1.13 |
| AppKit Services/standard contextual actions | A Services-provided replacement and pasteboard-based replacement enter the same prepared mutation path as paste. Cover mixed marks, selection changed while service work is pending, read-only transition and undo. The SDK supplies safe text/action integration; the application owns its service/menu availability and invocation policy. | DSK-1.7, DSK-1.13 |
| Linux primary selection | Qualify selecting text in one view and primary-selection paste into another, independently from the regular clipboard. Changing focus or selecting a target must not replace the captured source with unrelated text. Test empty selection, ownership loss, read-only destination and view disposal on each claimed display-system profile. | LNX-1.13; DEL-1.7 |
| Native selection drag and move/copy identity | Distinguish same-view, second-view/same-session, different-document and external-app drops. Same-view movement must preserve source until a valid destination and operation are accepted; cancellation or an unsupported target leaves source intact. A second view of one shared session must not cause deletion twice. Copy modifiers and drop proposals must match actual platform semantics and retain a non-drag action. | IOS/AND/DSK/WIN/LNX-1.13; shared interaction owner |
| Delayed transfer completion | Resolve transferred text/assets after focus or document changes, target deletion, permission loss and disposal. Check captured source/destination anchors and operation identity. A late item load must never insert into the newly active document. Preserve source for failed moves and record whether a cross-document move is a supported atomic operation or a host-mediated transfer. | All native -1.13, FIT-1.4 |

UIKit exposes a built-in [Find interaction](https://developer.apple.com/documentation/uikit/uitextview/isfindinteractionenabled).
AppKit's [NSTextView](https://developer.apple.com/documentation/appkit/nstextview)
provides Find, substitutions, service and pasteboard integration; its
[smart insertion/deletion property](https://developer.apple.com/documentation/appkit/nstextview/smartinsertdeleteenabled)
explicitly allows spacing changes around selected words. The
[subclassing guidance](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextEditing/Tasks/Subclassing.html)
is archival behavior guidance; pin current availability independently.
GTK's [selection clipboard registration](https://docs.gtk.org/gtk4/method.TextBuffer.add_selection_clipboard.html)
identifies the primary clipboard as a separate selection route. UIKit's
[drop proposal](https://developer.apple.com/documentation/uikit/uitextdropdelegate/textdroppableview(_:proposalfordrop:))
and [UITextDropRequest](https://developer.apple.com/documentation/uikit/uitextdroprequest)
expose acceptance and same-view information. The move/cancel/stale-target rules
above are proposed edit.ac acceptance derived from these platform distinctions,
not claims that the toolkit provides a cross-document transaction.

First-party presenters should inherit these routes and the same enabled-state
catalog. A table cell, code block, image caption or reference presenter must not
install an independent key handler, undo stack, drag transaction or clipboard
priority that silently overrides the baseline native control. Profiles with
unsupported native commands expose an explicit disabled state or documented
alternative. OS settings, menu customization, window management and service
availability remain application/platform policy, outside the Rust semantic core.

## Test design that exposes native-only failures

Extend each platform's existing named suites; do not create another runner. Use
the platform -1.4/-1.6/-1.7/-1.13 suites for deterministic protocol tests and
-1.16/-1.17 suites for text/action/structure inspection. Reuse shared before/after
semantic fixtures while keeping platform event traces independent.

Every new mutation fixture observes document/marks, native projection, selection,
undo depth, command count and active session identity. Include the rejected path,
not only the successful one. Every preview fixture observes zero semantic edits.
Two-view fixtures expose callbacks accidentally directed at the currently focused
view instead of the originating connection. Read-only cases retain navigation,
selection and copy while disabling every mutation route.

DEL-1.7 should add a small real-device matrix of operations that cannot be proved
by key injection: actual IME reconversion/correction, Android gesture preview and
fallback, iPad Scribble, desktop selection drag across windows, Linux primary
selection and screen-reader editing during menu/search focus changes. Record the
OS build, toolkit, input method, keyboard/layout, assistive technology, device and
artifact revision. Hardware-keyboard and touch-only routes are independent rows.
Unreachable OS features remain skipped/unqualified with an owner and unblock
condition; a mocked pass cannot promote them to supported.

No paid inference, speech-provider test, credential loading or automatic fixture
recording is introduced. OS dictation qualification remains the previously scoped
manual native workflow; deterministic automation uses prepared input events and
mocked transports and does not activate cloud recognition or OS writing services.

## Native performance must be measured at the boundary users feel

Apple's [TextKit 2 presentation](https://developer.apple.com/videos/play/wwdc2021/10061/)
describes viewport-based layout and warns that offscreen layout information may
need explicit layout. This supports a bounded-layout investigation, not a promise
that every text view or document shape is automatically fast. Android's
[FrameTimingMetric](https://developer.android.com/reference/androidx/benchmark/macro/FrameTimingMetric)
and [JankStats](https://developer.android.com/topic/performance/jankstats)
provide frame evidence and contextual UI-state tagging.

FIT-1.8 and each native -1.2/-1.4 owner should include:

- Selection drag/auto-scroll, correction/reconversion, handwriting preview,
  opening Find and replace-all, and remote edits during local composition on
  large documents; include a long single paragraph as well as many short blocks.
- Event-to-visible-caret/text latency and frame misses at the display's actual
  refresh rate, plus peak/resident memory, bridge calls/bytes, patched range size,
  layout invalidations and main-thread work. A fast Rust command alone is not
  evidence of responsive native input.
- Baseline, one official extension and the supported combined profile using the
  same fixture and hardware. Tag table/code/image/assistance state so an expensive
  optional presenter cannot hide within aggregate results.
- Offscreen result navigation and accessibility queries while viewport layout is
  active. Avoid scanning or forcing full-document layout on every selection,
  cursor-geometry request or frame; preserve correct geometry when explicitly
  navigating to an offscreen target.
- Idle after closing a popup, ending drag/handwriting, detaching a second view and
  disposing the editor: callbacks/timers/observers settle and retained native
  objects do not accumulate across repeated mount/dispose cycles.

Budgets and supported envelopes remain in the existing verification profile;
freeze them before measurement, retain raw samples and compare equivalent runs.
These are measurement proposals. No benchmark was executed for this research,
and neither “best experience” nor an architectural/performance improvement has
been demonstrated by these documentation changes.
