# Mobile browser extension case catalog

Qualification amendment (user decision, 2026-10-14): Named target-platform simulators/emulators and desktop OS VMs/test hosts may satisfy platform and release gates when physical hardware is unavailable. Follow the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms) for required runtime checks, tested virtual equivalents for hardware-only observations, counts and physical/virtual provenance. Earlier physical-only/manual-only wording in this document is superseded. This changes accepted evidence, not required implementation or correctness.

Status: planned acceptance matrix; none of these rows claims an executed runtime test or supported device.

Scope: browser presenters for existing optional extensions. [Track 41](../roadmaps/41-mobile-web-extensions.md) owns integration; [the mobile contract](../specs/mobile-web.md) and track 40 own baseline browser geometry/input behavior. Rust remains authoritative for content, commands, anchors and history. Track 25 owns rich semantics, 26 links, 27 formats and 39 optional assistance. This catalog adds no native SDK coverage.

MWX-1.1 creates an executable index for all 32 IDs. Each owning parent adds its assertions; MWX-1.8 qualifies the required physical or virtual platform rows. A row may need multiple assertions and device observations. Priorities: **P0** protects content, input, accessibility, authority and resource isolation; **P1** checks presentation and supported integration. **A** means deterministic automated mechanics; **D** means physical or virtual platform evidence; **A+D** requires both. Mocked APIs, event replay, device emulation and Playwright WebKit never satisfy D.

For every row, record feature set, source/implementation/fixture revisions, outcome and artifact link; preserve failures/skips. Device receipts include actual hardware, OS/browser/keyboard/locale/assistive-tool versions, pointer mode, viewport/zoom/orientation and reproducible actions. Actual iPhone/iOS Safari, iPad/iPadOS Safari and Android/Chrome are required families; declare exact versions before execution. Use non-sensitive fixtures. Optional capabilities are recorded as available/enabled/authorized/qualified separately; an unavailable optional API must execute its fallback row rather than erase required behavior.

Common assertions: preserve anchor/focus direction and composition; canceled/read-only/stale operations make no content/history change; accepted semantic operations use one validated command/history group. Touch controls require visible labels or discoverable accessible names, no hover-only route, and a tap alternative to every gesture operation. Meet WCAG 2.2 AA 24 by 24 CSS-pixel target size or document the applicable spacing/exception; use 44 by 44 CSS pixels as the primary touch-control usability target. Record exceptions individually. Native selection, ordinary scroll and pinch zoom remain available, including with extensions disabled. Limits are declared before measurements and failures retained.

## Capability and absence — MWX-1.1

| ID | Priority / evidence | Setup and action | Required outcome |
|---|---|---|---|
| MWX-C01 | P0 / A | Pack a baseline consumer with all optional mobile presenters disabled; import without DOM globals, then mount/type/scroll/destroy | No disabled extension module/CSS/asset load, listeners, observers, timers, workers or network requests; baseline typing/selection survives; baseline resources are counted separately |
| MWX-C02 | P0 / A | Enable one advertised module at a time, then dispose; repeat with unknown/disabled capability and missing optional APIs | Only explicitly enabled dependencies load; unsupported state is explicit and nonmutating; declared fallback remains reachable; resources return to baseline |
| MWX-C03 | P1 / A | Present every optional command in editable, read-only, denied and unknown states; replay remote changes | Shared applicability controls enabled/disabled state; no presenter invents authority/semantics or opens itself due to remote updates; capability record separates availability from qualification |
| MWX-C04 | P0 / A | Compare captured document/update/history before and after registration, viewport changes, popup reposition and destroy | Geometry/registration/status are derived state with zero content transactions; executable index maps every catalog ID to owner and evidence type |

## Menus and reference controls — MWX-1.2

| ID | Priority / evidence | Setup and action | Required outcome |
|---|---|---|---|
| MWX-C05 | P0 / A+D | Select a phrase with native handles; open named command control by tap while keyboard is visible; apply format, then undo | Control is discoverable without slash/hover, captured selection survives focus transfer, one command changes only the selected phrase and one undo restores it |
| MWX-C06 | P1 / A+D | Open a long bounded command/reference list near the viewport bottom; rotate, zoom and show/hide keyboard; scroll list/page and open native selection menu | Active result, native menu and dismissal remain reachable without trapping caret/controls; list/page scrolling is scoped and native pinch zoom works; hit areas meet recorded target rules |
| MWX-C07 | P0 / A | Trigger reference lookup, change query/session or delete target remotely, then deliver delayed/reordered/error responses and tap a former result | Stale results neither redirect insertion nor activate a link; query/recovery text is preserved; cancellation/revalidation uses existing resolver authority and anchors |
| MWX-C08 | P0 / A+D | With IME active, tap an enabled result through pointerdown/blur/activation; separately dismiss and move focus elsewhere | Composition is not prematurely committed or duplicated; internal composite focus permits valid activation; dismissal/restoration never steals a subsequent user focus change |

## Code and table controls — MWX-1.3

| ID | Priority / evidence | Setup and action | Required outcome |
|---|---|---|---|
| MWX-C09 | P0 / A+D | Edit long code with software keyboard; invoke labeled available indentation/language/copy controls; disable highlighter or exceed its limit | Literal text and qualified code semantics persist; required actions do not rely only on hardware shortcuts; immediate plain-code fallback keeps editing/selection usable |
| MWX-C10 | P0 / A+D | Select a cell/range in the bounded mixed Unicode table; use tap row/column/alignment/header controls in editable/read-only states | Existing commands/applicability own results; cell anchors and semantic snapshots match desktop fixtures, one accepted command forms one history group, read-only stays nonmutating |
| MWX-C11 | P0 / A+D | Pan a wide table/code region horizontally, vertically scroll its surrounding page and use native handles/pinch zoom | Wide-content overflow is bounded; native selection, page scrolling and zoom remain usable; no document-wide touch-action suppression or gesture capture |
| MWX-C12 | P1 / A | Format one selected Markdown table and edit one cell with many unrelated tables/code blocks present | Surrounding source bytes and unrelated tables remain unchanged; existing formatter/renderer limits and incremental counters hold; mobile controls cause no whole-document scan |

## Reorder and resize gestures — MWX-1.4

| ID | Priority / evidence | Setup and action | Required outcome |
|---|---|---|---|
| MWX-C13 | P0 / A+D | Drag only the explicit reorder handle across a scroll boundary; repeat using Move before/after; undo each | Same identity-preserving semantic move and selection result; bounded auto-scroll that refreshes coordinates without self-canceling, zero hover mutations and one accepted move/history group; tap route works with gestures disabled |
| MWX-C14 | P0 / A+D | For each advertised resize command, drag its handle; repeat via labeled size/preset controls; begin on ordinary text and pinch with two fingers | Drag and tap controls reach the same validated value; ordinary text retains OS selection/scroll/zoom; absent portable resize semantics remain honestly unsupported without creating document fields |
| MWX-C15 | P0 / A | During captured gesture emit pointercancel/lostpointercapture, competing second-touch/pinch (unrelated pointer events are ignored), viewport/orientation change, blur/read-only and destroy; separately follow successful pointerup with click/capture-loss | Canceled previews make no mutation and release capture/listeners/frame callbacks/auto-scroll; completed gestures commit exactly once; delayed events cannot revive or duplicate a terminal session |
| MWX-C16 | P0 / A | Begin move/resize, remotely delete/reparent target or change session, then release; repeat with valid unrelated remote edit | Current stable anchors/applicability decide acceptance; stale target rejects recoverably without redirecting mutation; valid acceptance preserves identity and other edits |

## Assets, embeds and file/camera affordances — MWX-1.5

| ID | Priority / evidence | Setup and action | Required outcome |
|---|---|---|---|
| MWX-C17 | P0 / A+D | Tap add-file; optionally choose camera capture when advertised; repeat with capture absent/declined/canceled and a prepared file | Explicit user action starts picker/capture; file-selection fallback is usable; cancellation preserves content/selection; opening a document/menu requests no camera permission or asset network work |
| MWX-C18 | P0 / A+D | Paste mixed image/file/HTML clipboard representations; separately begin asset selection/upload, background/change document or delete target, then deliver success/denied/revoked/offline results | Existing import precedence inserts one intended result without duplication; asset authority/session checks reject stale mutation; queued/failed/missing states remain visible/cancelable; asset and document receipts remain distinct |
| MWX-C19 | P1 / A+D | Open malformed/oversized image and missing/offline attachment fixtures; inspect metadata/alt-text controls at zoom with keyboard shown; destroy repeatedly | Bounded decode/request behavior, accessible alt/fallback text and reachable named controls; no leaked object URLs, decoders, requests or subscriptions |
| MWX-C20 | P0 / A+D | View an embed card; explicitly activate, dismiss/leave, then test denied/unsupported activation and nested scrolling | Card does no implicit privileged load; authority is checked at activation; exit/focus remains reachable, scrolling is usable and rejection returns to a safe card without losing selection |

## Format import, export and sharing — MWX-1.6

| ID | Priority / evidence | Setup and action | Required outcome |
|---|---|---|---|
| MWX-C21 | P0 / A+D | Import a prepared supported document via file input; preview/confirm; repeat with unavailable advanced picker, cancel and over-limit file | File-input fallback works; direction/fidelity and errors are truthful; cancellation/failed preparation makes no mutation; confirmed import uses current anchor/revision and one history group |
| MWX-C22 | P1 / A+D | Export supported Markdown/text and a qualified binary format; deny/omit advanced file-saving API and retry with download | Exact bytes/hash, filename and media type survive fallback; actual device delivery is observed separately; unresolved delivery exposes retained output and explicit recovery steps, never false success |
| MWX-C23 | P0 / A+D | Prepare export, invoke supported native share from an explicit tap; test share absent, denied, canceled or unable to share that file | No implicit share or permission prompt; unsupported/rejected path retains bytes and offers download or appropriate manual alternative; dismissal is distinct from confirmed delivery |
| MWX-C24 | P0 / A+D | Use copy/export when clipboard API is absent/denied; select manual text fallback; switch document during long mocked conversion/import | Manual selection/copy remains reachable with native handles; stale work cannot apply to another document; PDF remains export-only and menus expose only qualified format directions |

## Optional web assistance — MWX-1.7

| ID | Priority / evidence | Setup and action | Required outcome |
|---|---|---|---|
| MWX-C25 | P0 / A+D | With qualified AIN web controls, open assistance using tap, VoiceOver/TalkBack and supported voice-control label while keyboard/zoom changes | Visible/accessibility names agree; command, cancel and recovery remain reachable; bounded status/focus follow qualified AIN behavior and no hover/global printable shortcut is required |
| MWX-C26 | P0 / A | Start an explicit injected mocked assistance session; deliver prepared provisional/final/late results after cancel, read-only or target deletion | Provisional UI stays bounded; finals commit once at valid anchors only; rejected results preserve recoverable text without redirecting, duplicating or adding canceled history |
| MWX-C27 | P0 / A+D | Disable optional assistance; edit/correct with real OS dictation, IME and screen reader on declared devices | Baseline OS input and accessible commands remain available; no assistance module/assets/listeners/network start; real outcomes reference matching AIN/baseline device receipts |
| MWX-C28 | P0 / A+D | While assistance is enabled, select text, move focus to controls, cancel, then focus another host control; repeat with capability denied/unsupported | Selection is retained/revalidated, focus restoration respects newer user focus, denial is named and nonmutating; no microphone/provider path is inferred from text events |

## Device and overhead qualification — MWX-1.8

| ID | Priority / evidence | Setup and action | Required outcome |
|---|---|---|---|
| MWX-C29 | P0 / D | Run required touch/input/viewport/selection rows on physical or simulated iPhone/iOS Safari and iPad/iPadOS Safari, plus physical or emulated Android/Chrome at declared versions, including keyboard open/closed, rotation and zoom | Every mandatory device cell has observations and exact setup; native handles, scrolling and pinch zoom work; physical, virtual and tested virtual-equivalent rows remain separately labeled; unavailable hardware does not block qualification |
| MWX-C30 | P0 / A+D | Inspect all advertised controls with touch and relevant VoiceOver/TalkBack; test target dimensions/spacing, focus at zoom, tap alternatives and iPad hardware pointer/keyboard where claimed | Target-size conformance/exceptions and 44-pixel usability deviations are recorded; no operation is hover-only or gesture-only; accessible names/states and actual activation results match claims |
| MWX-C31 | P1 / A+D | On fixed phone/tablet profiles compare disabled, individual and combined enabled extensions with Task/Long fixtures, cold/warm loads and active menus/gestures | Raw bytes, loads, p50/p95/p99 latency, geometry/invalidation work, long tasks and memory fit predeclared feature limits and existing baseline targets; optional costs are separate, failed samples retained |
| MWX-C32 | P0 / A+D | Repeat mount/enable/disable/destroy, picker background return, pointer cancellation and session switch; validate all case receipts and production disabled artifact graphs | Disabled extension work/resources/network remain zero and enabled resources return to baseline; no stale callback mutates content; immutable evidence is complete/current and physical or virtual platform counts remain distinct from receipt-validator counts |

## Evidence sources and overlap

Use [mobile platform research](../evidence/mobile-web-platform-research.md) for browser input/viewport distinctions and [touch extension research](../evidence/touch-extension-research.md) for control/gesture/API constraints. The authoritative [mobile contract](../specs/mobile-web.md) resolves implementation policy. This matrix consumes INT/AIN/RCH behavior instead of defining competing input, command, resolver, asset or format semantics. Reuse exact-revision upstream observations when their full setup/outcome matches; a changed presenter or consumed dependency requires the affected cases to be requalified.

## Portable touch formatting projection — MEX-1.9 / MWX-1.9

MTF-1.1–1.3 implement the portable production-browser subset of MEX-1.9-I1/V1. Original catalog IDs and platform criteria above remain unchanged. The executable registration is `core/tests/browser/mobile-extensions/touch-predicates.json`; the canonical packed-consumer suite is `npm run test:browser -- mobile-extension-formatting`. Its receipt reconciles every named case and pins original catalog rows. A passing projection does not close full platform rows or MWX-1.8/roadmap43.

| Original criterion / catalog overlap | Portable registration | Required proof and remaining observations |
|---|---|---|
| Every advertised caption/reference/extension/text mark; MWX-C05 | text-families, search-focus, target-guards | Six marks across nine carrier families plus five enabled presenters; captured reverse range, opaque/source preservation, one history effect and undo/redo. Native handles and platform accessibility pending. |
| Every advertised table-cell format; MWX-C10 | table-actions, target-guards | Six inline actions, paragraph, six heading levels, code block, header/body, four alignments and link removal on captured rectangle. Native handles/OS host observations pending. |
| Explicit formatted/literal paste; MWX-C05/C24 | paste-flavors, search-paste, code-paste | Internal precedence, HTML/plain, malformed/disabled/unsupported fallback, search focus and literal code policy. Real producer/OS delivery pending. |
| Captured cell/text selection survives menu focus; MWX-C05/C10 | native-event-replay, table-paste | beforeinput-only/noncancelable/menu event replacement, rich rectangle and literal single-cell policy; constructed events are prepared replay, never observed OS menus. |
| Async cancellation and editor isolation; MWX-C05/C24 | async-fences | Stale/foreign/read-only/background/dismiss/dispose/denied/empty/duplicate/later-selection fences. Full import/export/manual-copy C24 ownership is unchanged. |

The device handoff is `core/tests/manual/mobile-web-extensions.md`. All iPhone/iPad/Android OS cells are pending here; accepted simulator/emulator receipts must identify actual runtime versions and tested equivalents. Existing broader menu/IME/AT/overhead/release owners remain open. Final immutable portable receipts, counts and historical failures are linked from `evidence/mobile-extensions/touch-qualification-20261018/delivery.json` when delivered.
