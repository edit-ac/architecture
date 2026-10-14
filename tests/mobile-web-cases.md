# Mobile web regression catalog

Qualification amendment (user decision, 2026-10-14): Named target-platform simulators/emulators and desktop OS VMs/test hosts may satisfy platform and release gates when physical hardware is unavailable. Follow the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms) for required runtime checks, tested virtual equivalents for hardware-only observations, counts and physical/virtual provenance. Earlier physical-only/manual-only wording in this document is superseded. This changes accepted evidence, not required implementation or correctness.

Status: planned executable/device coverage. [Mobile web](../specs/mobile-web.md) defines the policies; [track 40](../roadmaps/40-mobile-web.md) owns these cases. Reuse the [87 everyday cases](editor-interaction-cases.md) where their exact implementation/fixture revision remains applicable. [Optional extension cases](mobile-extension-cases.md) have separate owners and do not gate the minimal browser surface.

## Fixture and evidence protocol

Each ID becomes a test title/device receipt with initial document, directional selection, host scrolling/embedding mode, capabilities, action sequence and expected semantic/UI result. Use the real Rust/WASM engine and mounted adapter. Prepared event/geometry/capability fixtures mock platform delivery, never the editor's committed outcome. Record text/marks/block IDs, UTF-16 selection/affinity, transaction and history counts, focus, scroll/caret visibility, resources and any diagnostics relevant to the row. Failed/canceled/read-only actions and geometry-only changes commit zero edits attributable to that action; independently observed OS composition commits or remote edits in the same trace are counted under their own origin. A successful command commits once.

Use text near block/document boundaries, emoji/combining/RTL, composing text, nested scrollers, two editors and an inline atom as targeted variants. Combine high-risk pairs (composition + toolbar, remote edit + selection handles, keyboard + rotation, pointer capture + pagehide); document the sampled matrix instead of claiming every Cartesian combination. Keep transcripts/clipboard/files synthetic and nonsensitive. No inference provider, live microphone, credential loading or automatic recording belongs in automated tests.

`mechanics` means deterministic browser checks; `device` means actual OS/browser/keyboard/AT evidence. Desktop touch emulation, synthetic events and Playwright WebKit do not satisfy device rows. MWB-1.10 integrates mechanics; MWB-1.11 owns device observations, including mechanically covered rows whose native behavior cannot be simulated. P0 = lost/corrupted input, unusable access or gesture/focus trap; P1 = fidelity and optional capability handling.

## Native touch and pointer ownership — MWB-1.2

| ID | Priority | Setup and action | Expected outcome |
|---|---|---|---|
| MBT-01 | P0 | Tap/double-tap/long-press text, empty block, trailing hard break and inline atom | Native placement/selection/context menu remains available; model mapping has no filler offset; device |
| MBT-02 | P0 | Drag native selection handles across marked blocks while an unrelated remote patch arrives | Stable selected text/direction and native handles; no subtree replacement or focus theft; device |
| MBT-03 | P0 | Pan/nested-scroll/pinch zoom over editor and optional control edges | Browser scroll/zoom stays available; no broad preventDefault/touch-action:none or content mutation; device |
| MBT-04 | P0 | Handle gesture: pointerdown/move → pointercancel/lost capture → compatibility click | Provisional state cleared; no semantic commit, stuck capture, auto-scroll or duplicate click |
| MBT-05 | P0 | Successful handle pointerup then lost capture/click; unrelated pointer events in a separate variant | Ignore unrelated pointers; exactly one command from tracked pointer, with no repeat/rollback after completion; a competing second-touch/pinch before acceptance cancels instead |
| MBT-06 | P1 | Touch then mouse/trackpad/pen, coarse+fine pointer availability changes | Controls remain usable; stale touch-only mode does not disable hover/keyboard or native pen text |
| MBT-07 | P0 | Touch controls under zoom/large text/forced colors; no drag capability | Reachable named targets meet declared size/spacing; tap alternative and visible focus work; device |

## Mobile typing — MWB-1.3

| ID | Priority | Setup and action | Expected outcome |
|---|---|---|---|
| MBI-01 | P0 | Insert/delete from virtual keyboard with no keydown or Unidentified; observer echoes | Correct content/range once; identical result to ordinary input route |
| MBI-02 | P0 | Accept predictive word, autocorrect phrase or double-space punctuation over marked selection | Actual committed replacement/marks/spacing preserved; no duplicate or guessed text |
| MBI-03 | P0 | CJK/Indic composition with partial delete and commit Enter before/after compositionend | OS candidate ownership retained; no accidental split/slash activation, next intentional Enter works; device |
| MBI-04 | P0 | Swipe typing, emoji picker, native dictation correction and handwriting/Scribble | Correct replacement and grapheme/UTF-16 selection without requiring physical key events; device |
| MBI-05 | P0 | Hold Backspace/autorepeat around emoji, adjacent blocks and empty editor | Platform deletion reconciles once; no double delete, split surrogate or unrelated block loss; device |
| MBI-06 | P0 | During composing text: remote edit, toolbar selection, read-only, blur or pagehide | Qualified commit/cancel/conflict policy preserves recoverable text and rejects stale mutation |
| MBI-07 | P1 | Hardware keyboard connect/disconnect, virtual keyboard switch, AltGraph/dead keys/RTL | Correct platform shortcuts/characters and no stale occlusion or forced model reset; device |
| MBI-08 | P0 | Same slash/Markdown trigger inserted by direct typing and unclassified replacement | Only positively qualified input auto-converts; explicit mobile command route remains available |

## Viewport and occlusion — MWB-1.4

| ID | Priority | Setup and action | Expected outcome |
|---|---|---|---|
| MBV-01 | P0 | Focus bottom-of-document caret, open/close keyboard with browser visual/layout resize variants | Caret and essential controls reachable; original semantic selection retained; device |
| MBV-02 | P0 | Keyboard overlay geometry plus resize notifications; two editor mounts | One host-owned policy and one compensation; destroying one mount preserves other's/host policy |
| MBV-03 | P0 | Keyboard open → portrait/landscape rotation or split-screen resize | Stable document/focus and usable caret/toolbar; obsolete insets/gesture state cleared; device |
| MBV-04 | P1 | Floating/split keyboard or hardware keyboard leaves non-bottom occlusion | No invented full-width keyboard height; available geometry or reachable scroll/control fallback; device |
| MBV-05 | P0 | Pinch zoom with nonzero viewport offset/scale then tap caret/menu item | Correct CSS-coordinate mapping and target hit; no double DPR/scale compensation; device |
| MBV-06 | P1 | Browser address bar expands/collapses, safe-area changes, small/dynamic viewport layouts | No false keyboard command, double bottom inset, hidden action or fixed-100vh clipping; device |
| MBV-07 | P0 | Nested scroller, sticky toolbar, same-origin iframe and isolated cross-origin host | Correct owning window/scroll root; no top-window assumption or unauthorized parent access |
| MBV-08 | P0 | Many viewport/scroll events in one frame; remote edit during scroll | Bounded read/write batch, no continuous scrollIntoView loop, no remote scroll/focus jump |
| MBV-09 | P0 | VisualViewport/keyboard geometry missing or throwing; tiny available viewport | Native scroll and reachable static/sheet controls work; fallback does not disable editing |

## Focus, hints and reachable controls — MWB-1.5

| ID | Priority | Setup and action | Expected outcome |
|---|---|---|---|
| MBF-01 | P0 | Select text via handles then tap Bold/Link/soft break, including pointerdown→blur→click | Captured selection used once; valid internal focus transition is not premature dismissal; device |
| MBF-02 | P0 | Open command-search input/dialog, dismiss, then user focuses another editor before async result | Intentional control focus works; stale completion cannot steal focus or reopen keyboard |
| MBF-03 | P1 | Browser declines programmatic focus/keyboard show without activation | No false keyboard-visible state or retry loop; direct user action can continue |
| MBF-04 | P0 | Virtual keyboard without Shift/Escape/Tab; apply break, undo/redo, indent, literal paste | All advertised commands have reachable labeled controls and correct semantic result; device |
| MBF-05 | P1 | Switch prose/code/search hints during composition and after commit | No remount/lost text/forced keyboard reopen; code input remains literal; supported hints applied safely |
| MBF-06 | P0 | Enter key labeled Done/Go/Send inside form-embedded editor | Existing multiline/explicit host-submit policy wins; no accidental form submit or blur |

## Clipboard and browser lifecycle — MWB-1.6

| ID | Priority | Setup and action | Expected outcome |
|---|---|---|---|
| MBC-01 | P0 | Long-press native Copy/Cut/Paste, including canceled/failed clipboard write | Supported format/selection retained; failed cut preserves content; device |
| MBC-02 | P0 | Rich/text/image clipboard flavors; script permission denied, API absent or activation expired | Safe bounded importer/fallback and native paste route remain usable; no prompt on mount |
| MBC-03 | P0 | Paste preparation pending then focus/document/read-only changes or target deletion | Original stable target/session revalidated; cancellation/rejection has zero edits |
| MBC-04 | P0 | Pagehide/visibility pause while typing or a gesture is active; pageshow/BFCache return | Durable state/session restored, provisional gestures canceled, no duplicate listeners or replayed input; device |
| MBC-05 | P0 | Browser process eviction/offline reopen after localCommitted versus uncommitted edit | Existing durability contract honored; no fabricated unload flush guarantee; device |
| MBC-06 | P1 | OS picker/share sheet blurs/backgrounds page then cancels/returns twice | Cancellation harmless, accepted result deduplicated, selected target preserved, no forced refocus |
| MBC-07 | P0 | Two editors with one disposed while clipboard/lifecycle work is pending | No cross-editor insertion or shared resource teardown; late callbacks inert |
| MBC-08 | P0 | Native mobile Paste menu produces ClipboardEvent plus beforeinput/input, beforeinput only, or a noncancelable replacement | Event lifecycle owns one prepared paste; no keyboard prerequisite, duplicate edit or history/journal echo; physical or target-platform virtual runtime evidence remains required |
| MBC-09 | P0 | Same native clipboard payload pasted twice deliberately, including soft-keyboard suggestions | Two distinct user intents both apply; payload equality and timing never suppress the second paste |
| MBC-10 | P0 | Rich internal/Markdown/HTML flavors and explicit Paste without formatting, with touch and hardware keyboard shortcuts | Declared full-palette codec precedence; plain mode bypasses parsing and formatting; native menu remains available after script-clipboard denial |
| MBC-11 | P0 | Mobile delayed paste crosses navigation, read-only, target deletion, backgrounding or disposal | Initiating stable target/session retained; later selection preserved; canceled/stale result has zero semantic/history/storage effects |
| MBC-12 | P0 | Formatted table cells, lists, links, code, captions and other registered extensions copied between mobile web and native apps | Admitted structure/formatting round-trips; missing codec preserves inert source with diagnostics; emulator replay and physical or virtual platform results recorded separately |

## Optional browser and keyboard APIs — MWB-1.7

| ID | Priority | Setup and action | Expected outcome |
|---|---|---|---|
| MBA-01 | P0 | Each API absent/present-but-rejecting/insecure/embedding-restricted | Same essential editing/fallback; no eager permission prompts or exception escape |
| MBA-02 | P1 | Optional VirtualKeyboard geometry/show/hide/overlay host request | Only explicit supported action attempted; failure recovers; host-global lease restored without fighting other editors |
| MBA-03 | P1 | getLayoutMap absent/rejected/layout changed and non-US hardware keyboard | Fallback shortcut labels; no altered semantic keys or blocked AltGraph/IME |
| MBA-04 | P0 | Default editor then explicit host kiosk keyboard-lock session; denial/exit/dispose | Default never locks keys; requested mode has escape and releases only owned capture; device if advertised |
| MBA-05 | P1 | Experimental EditContext enabled/unsupported/disabled in a separate probe | Feasibility evidence only; contenteditable fallback usable, no default dependency or second committed model |
| MBA-06 | P0 | Host viewport policy changes while multiple editors exist | SDK does not rewrite meta viewport; declared mode reconciled without double keyboard compensation |
| MBA-07 | P1 | File/Share/fullscreen/orientation capabilities missing, denied or unsupported MIME | User-visible action/fallback remains explicit; baseline editing independent of these APIs |

## Baseline module touch integration — MWB-1.8

| ID | Priority | Setup and action | Expected outcome |
|---|---|---|---|
| MBX-01 | P0 | Open baseline slash menu through visible control with keyboard open | Reachable results/dismissal; no hover/physical slash requirement; correct anchored command |
| MBX-02 | P0 | Native text-selection menu covers formatting controls | Alternate toolbar/command route works without disabling native selection/context menu; device |
| MBX-03 | P0 | Baseline table/code block scrolls horizontally while page scrolls vertically | Caret/native selection and touch command access coexist; no scroll trap or full-document mutation |
| MBX-04 | P0 | Baseline block action with no drag support; enhanced presenters disabled | Tap/keyboard equivalent retains core command access; no optional asset/listener load |
| MBX-05 | P0 | VoiceOver/TalkBack exploration and activation with keyboard and suggestion panel open | Correct accessible names/states/focus and reachable cancellation; device |

## Overhead and cleanup — MWB-1.9

| ID | Priority | Setup and action | Expected outcome |
|---|---|---|---|
| MBP-01 | P0 | Same packed minimal consumer before/after baseline support | Incremental/total Brotli budgets and cold-evaluation/startup limits pass; no new default runtime dependency |
| MBP-02 | P0 | Optional mobile API/gesture/media/converter modules absent or disabled | Zero optional import/evaluation/assets/network/workers/listeners/observers/frame callbacks |
| MBP-03 | P1 | Many viewport/pointer notifications across visible/hidden editors, small/long docs | At most one dirty geometry batch per window/frame; work scales with active surfaces, no full-text scan |
| MBP-04 | P0 | Repeated mount, keyboard cycles, rotate, cancel/dispose | Listener/observer/capture/object-URL ownership settles; memory plateaus, no active session-owned timers |
| MBP-05 | P1 | Real phone typing/menu/scroll with baseline and optional modules enabled | Comparable raw latency/frame/memory deltas satisfy reviewed limits; no emulated phone-performance claim |
| MBP-06 | P0 | Idle editor and hidden page with extensions registered but unused | No polling/perpetual frames/remote fetches; registration alone does not start feature work |

## Device and support claims — MWB-1.11

| ID | Priority | Setup and action | Expected outcome |
|---|---|---|---|
| MBQ-01 | P0 | Actual iPhone Safari and iPadOS Safari, software/hardware keyboards and touch/pen | Required row receipts with exact versions/modes; supported envelope is explicit |
| MBQ-02 | P0 | Actual Android Chrome and Firefox, named keyboard versions and vendor device | Replacement/viewport/selection/clipboard cases qualify independently; no stale browser-default assumptions |
| MBQ-03 | P0 | Browser tab versus installed web-app/embedded-host profile where advertised | Profile-specific lifecycle/viewport/permissions/keyboard evidence; one mode does not qualify another |
| MBQ-04 | P0 | Capability table contains untested API/platform or only emulated/desktop-WebKit evidence | Validator rejects support claim; preserve pending/unsupported/failure and actual fallback results |

## Completion rules

MWB-1.1 creates an executable index and named group dispatcher; no missing/zero-match suite passes. MWB-1.2–MWB-1.9 create and run their mechanical groups. MWB-1.10 combines real mounted browser tests with deliberate event/geometry variants; MWB-1.11 records all device rows and required actual-platform observations in the other groups. Freeze the mandatory device/keyboard/locale sample before testing. Missing mandatory hardware or failed input remains blocked; optional unavailable APIs pass only through their real fallback behavior, not by deleting the row.

Each receipt records case ID, exact source/implementation/profile/fixture revisions, command/manual steps, executed/passed/failed/skipped counts, raw artifact and limitation. New cases extend the corpus when field failures occur. Fixtures establish the tested envelope; the catalog is not an exhaustive guarantee for all mobile devices.
