# Native SDK delivery and semantic parity

Qualification amendment (user decision, 2026-10-14): Named target-platform simulators/emulators and desktop OS VMs/test hosts may satisfy platform and release gates when physical hardware is unavailable. Follow the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms) for required runtime checks, tested virtual equivalents for hardware-only observations, counts and physical/virtual provenance. Earlier physical-only/manual-only wording in this document is superseded. This changes accepted evidence, not required implementation or correctness.

This is the delivery contract for roadmaps 16–18, 22 and 23: iOS, Android, macOS,
Windows and Linux. Roadmap 09 remains preparation evidence. Completing a binding or a
toolkit probe does not complete a native editor. These tracks deliver embeddable
native editor components, native sample hosts, supported package artifacts, and
the platform evidence consumed by roadmap 20.

## Ownership and prerequisites

All clients use the qualified engine, module registry, shared client/session
contracts, change model and extension library from roadmaps 02, 07, 12, 13 and 21.
Mobile preparation gates are task-specific within roadmap 09: both require
`NAT-1.1` portable engine evidence and `NAT-1.2` bounded binding evidence. iOS
additionally requires `NAT-1.3` Swift headless and `NAT-1.5` iOS control evidence;
Android requires `NAT-1.4` Kotlin headless and `NAT-1.6` Android control evidence.
Each bootstrap verifies those individual task artifacts against the consumed
engine/binding revisions. Neither mobile track waits for the other platform,
the joined `NAT-1.7` follow-up, or completion of all of roadmap 09. See
[client contracts](client-contracts.md), [changes](change-diffs.md) and
[extension library](extension-library.md).
The shared session owns document identity, commands, durable updates, history,
capabilities and transport state. Native adapters own input, OS selection,
presentation, accessibility and host integration. Native text storage is a
projection; it cannot become a second authoritative document. The same command
and fixture must produce the same semantic result across clients, while native
controls retain platform-appropriate appearance and interaction.

The additive native Session command boundary accepts the portable `EditorCommand` transport and shared anchor tokens, then uses the same Rust `EditService` planner and durable Session commit. Native presenters obtain current route/profile metadata from `commandCatalog` and check target applicability with `checkCommands`; admission metadata alone is not target enablement. Optional host services and pending profiles remain explicitly unavailable. See [native Session ownership](client-contracts.md#native-shared-session-ownership-nsr-11). This Rust boundary is a prerequisite for native key/menu/profile qualification, not evidence that those SDK or platform gates are complete.

An adapter consumes the shared native storage/session port rather than creating
another journal, sync protocol or reconciliation engine. Persisted/asynchronous
targets use stable anchors. Bridge buffers have explicit ownership and bounded
lifetime; UTF-16 boundary units are converted at toolkit boundaries. Keep handle
access serialized, callbacks outside Rust locks/transactions, and UI mutations
on the required UI executor. A failed command cannot leave accepted UI text that
disagrees with the semantic store.

macOS, Windows and Linux are separate branches. A missing Windows host does not
block macOS or Linux work, and one successful desktop build does not qualify the
others. Each OS must pass its own toolkit feasibility, implementation, packaged
consumer, input and accessibility gates. Cross-platform qualification records
each result separately; a missing mandatory target remains an open deliverable.

## Mandatory capability matrix

Every listed native platform must deliver the following semantics. Create the
machine-readable matrix in each `native/<platform>/capability.json` from the
shared client capability schema; start all delivery claims as unqualified.
Matrix entries separately record render/read, edit, selection/navigation,
clipboard, import/export and accessibility support, with fixture and evidence
references. The current task may qualify only the behavior its tests exercise.

| Capability | Required native behavior |
| --- | --- |
| Text and selection | Unicode paragraphs, headings, code blocks, quotes and line breaks; stable selection mapping; grapheme-safe user actions; bidi navigation and platform input behavior within the declared matrix |
| Rich marks and links | Engine-defined bold, italic, strike, inline code and links; mixed selections; validated link activation; equivalent semantic import/export |
| Lists | Engine-defined ordered, unordered and task lists, checked state, nesting and structural commands; native keyboard/touch operation and block moves |
| Tables | Render the bounded engine table; edit real cells, navigate/select cells, and invoke supported row/column commands; preserve cell identity and reject unsupported structure explicitly |
| Images | Visible native image presentation with alt text and metadata; accessible selection, replacement and removal; host-controlled asset loading and failure state |
| References | Persistent target ID and label, native display and invocation, explicit host resolver, cancellation and stale-result protection |
| Custom modules | Qualified data-only marks and atoms with native renderer hooks, command routing, selection, accessible labels and disposal; unknown versions preserve bounded source data |
| Read-only | Copy and navigation remain usable while every mutation route, including IME, paste, drop and host commands, obeys the shared capability/authorization state |
| History | Native menu, key and gesture actions call shared origin-aware undo/redo; local grouping and remote edits match engine fixtures; a parallel OS undo stack cannot mutate the projection independently |
| Change review | Accessible native read-only unified/semantic change presentation from the portable roadmap-13 model; revision and representation/profile labels, trusted or unknown attribution, range navigation, and explicit stale state; no independent diff algorithm or live-replica rewind |
| Offline and recovery | Local editing needs no account/network; the shared durable receipt controls the locally committed indicator; process-crash restoration retains committed document changes and pending updates |
| Collaboration | Native clients exchange the same qualified updates and receipts as web; reconnect, remote selection, authorization change and document/session switching preserve shared semantics |
| Input and accessibility | Real platform composition, autocorrect/dictation where supported, hardware input, focus, screen-reader text/structure and accessible editing actions on declared OS/device combinations |

Plain text, an image of a table, an inert attachment, or a source-code fallback
does not satisfy a mandatory rich editing cell. Toolkit-native child controls
may provide a table cell or attachment editor if their selection, focus, history
and accessibility remain integrated with the one semantic session. The host
must expose required commands through native controls or input actions; matching
browser toolbar layout, slash-menu visuals or pixels is unnecessary.

Unknown extension preservation is a distinct safe behavior. It cannot mark a
first-party mandatory table, image or reference as implemented. A failed
feasibility probe produces a smaller replacement design for that OS; it never
silently downgrades the matrix or introduces a WebView.

## Optional math and declared limitations

Math is separately reported as `preserve-source`, `edit-source` and
`typeset-render`. Source editing must retain the shared bounded LaTeX data and
diagnostics; typesetting needs an explicitly selected native renderer with
license, size, accessibility and malformed-input evidence. `edit-source` does
not imply typesetting. An optional unqualified renderer can remain unavailable
when disclosed, but its source fallback cannot satisfy mandatory rich features.
The platform reports source-only math honestly instead of advertising visual
math parity. Unsupported custom executable behavior is also declared separately
from supported portable module data.

## Native toolkit decisions and evidence

These are candidates for platform-specific feasibility gates, not a claim that
one stock widget supports every required structure. Pin the SDK, compiler,
toolkit and deployment range in each platform's bootstrap task using the actual
build host and official availability documentation.

| Platform | Candidate and constraint | Primary evidence |
| --- | --- | --- |
| iOS | UIKit `UITextView`/TextKit plus native attachment or cell views. Selected and marked ranges belong to the text-input lifecycle; a marked range contains provisional composition text. Table editing and custom attachments require their own feasibility fixtures. | [Apple text input and marked text](https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/LowerLevelText-HandlingTechnologies/LowerLevelText-HandlingTechnologies.html) |
| Android | `EditText`/`Editable`, spans and native child views; preserve `InputConnection` composing, selection and batch semantics. Standard styled text is not evidence of editable tables or custom atom parity. | [Android InputConnection](https://developer.android.com/reference/android/view/inputmethod/InputConnection) |
| macOS | AppKit `NSTextView` and its native text storage/layout system, with native attachments or cell views where required. Probe attributed ranges, tables and custom atom editing against the chosen TextKit path. | [Apple text system organization](https://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/TextSystemArchitecture/ArchitectureOverview.html) |
| Windows | WinUI `RichEditBox`/native text services as the initial candidate. Its `ITextDocument` exposes selection, text ranges and native history; adapt history to the shared engine and prove structured editing/IME integration before selecting the host. | [Microsoft RichEditBox](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/rich-edit-box) |
| Linux | GTK4 `TextView`/`TextBuffer` with tags and native child widgets. Character offsets must be converted to the shared UTF-16 contract; child-anchor support alone does not establish table editing or accessible structured navigation. | [GTK character offsets](https://docs.gtk.org/gtk4/method.TextBuffer.get_iter_at_offset.html), [GTK child anchors](https://docs.gtk.org/gtk4/method.TextView.add_child_at_anchor.html) |

None of these choices permits WebView/Electron rendering or a second custom
typography engine. A replacement candidate must still use real native text input,
native accessibility, a portable Rust semantic core, and the same capability gates.

## Verification and package delivery

Each platform bootstrap creates its actual build/test dispatcher and named suites
before later tasks invoke them. Dispatchers reject unknown suite names and zero
matching tests, propagate build failures, and record executed/passed/failed/skipped
counts. Commands in the roadmaps are future interfaces created by those tasks,
not claims that build projects or tests already exist. Missing SDKs, signing
identities, device access, display servers or accessibility tooling have an exact
host/owner/unblock condition; the affected gate remains unchecked.

Use shared deterministic semantic fixtures and mocked storage/network/asset
services for automation. Cover two views of the same session, remote updates,
mount/dispose, error/cancel, schema/version rejection, and native-origin history.
Preserve failures and skipped cases. No live service credentials or paid inference
are needed. A recorded physical or virtual platform/manual OS session is separate from synthetic
event tests and is mandatory for supported composition and screen-reader claims.

Platform packages must work in a clean consumer without a sibling checkout:
Swift package plus the declared Apple binary slices; Android library with the
declared ABI artifacts; a native Windows SDK package; and a native Linux package
with a declared GTK/runtime baseline. Lock runtime/generator versions and record
bridge/schema compatibility, third-party notices, symbols and immutable artifact
hashes. Signing and public publication occur only under their explicit release
tasks; locally building a package is not registry publication.

The final epic of each native roadmap builds the package, verifies a clean
consumer and prepares exact qualification inputs. This establishes implementation
and package readiness. Roadmap 20 performs the actual OS/device, real-input and
screen-reader qualification against those source/artifact revisions. Until that
evidence passes, support remains unqualified. Full native delivery is incomplete
while any mandatory platform/capability is blocked, unsupported, untested or
represented only by a binding demonstration.

## Everyday interactions and optional assistance

Reuse [editor interactions](editor-interactions.md) and its [case catalog](../tests/editor-interaction-cases.md) for shared semantic expectations while retaining native visual navigation, text-input and accessibility policy. Browser event replays do not qualify a native adapter. Track 39 adds [assistive input](assistive-input.md) presenters in independently gated iOS, Android, macOS, Windows, Linux and terminal tasks; baseline OS dictation and screen-reader editing stay required without the extension.


## Native editing protocol qualification

Apply the additional NAT cases in the [desktop/native catalog](../tests/desktop-editing-cases.md) with [platform research](../evidence/native-editing-research.md). Shared content outcomes are portable; selection geometry, text services, clipboard ownership and OS command routing remain platform responsibilities. Each relevant SDK task binds its protocol cases before the platform qualification task passes. Manual OS/IME/assistive observations remain distinct from deterministic fake-protocol tests.

Android InputConnection adapters distinguish UTF-16 deletion from code-point deletion, exclude the selection where the API requires it, bracket batch edits, handle nullable/bounded surrounding text and report selection updates without echo commits. Stylus gesture preview is transient; apply/cancel/fallback results and supported/unsupported gesture capabilities are explicit. Apple controls expose marked/selected ranges, responder Edit commands, find and text-checking/replacement only through captured semantic targets; an asynchronous item provider or writing tool cannot apply to a different session after focus changes. API availability is not permission to call an external AI service; validation uses prepared replacements only. Windows text services qualify selection/lock/reentrant update and composition behavior in the chosen native text stack; UI Automation text ranges remain mapped after edits. GTK adapters convert UTF-8 byte indices and character counts at their actual API boundaries into public UTF-16 positions, and distinguish PRIMARY selection from the clipboard on the qualified display backend. Invalid, stale or unavailable ranges reject without guessing.

All platforms qualify native Edit/context-menu enablement, physical keyboards, multiple editor instances, external/internal text transfer, permission loss during async delivery, accessibility text geometry after zoom/scroll and selection/history after OS replacement. iOS/Android additionally cover selection handles during viewport changes and drag from another app where supported. Native drag metadata alone does not establish a cross-document durable move. Clipboard providers must remain valid for their promised lifetime or fail explicitly without source loss.

Measure keystroke/IME-to-visible response, candidate/caret geometry, text-service queries, selection autoscroll, large logical lines, mixed extensions and repeated mount/dispose on real supported hardware. Record frame scheduling, main-thread work, memory growth and exact OS/IME/display configuration. Keep layout and OS callbacks outside the Rust semantic kernel; expensive analysis must not synchronously reenter native input locks. Unavailable devices and unmeasured profiles remain blocked/unsupported evidence, never a browser-derived native pass.

## Planned native clipboard qualification

[NCL cases](../tests/native-clipboard-cases.md) separate simulator/emulator/VM mechanics from physical-device and actual OS pasteboard evidence. IOS/AND/DSK/WIN/LNX-2.4 own deterministic native OS-host fixtures; DEL-1.9 and DEL-1.10 own physical-device/platform qualification. Native menu paste, rich/plain format precedence, optional match-style shortcuts, failed cut, delayed provider lifetime, cross-app transfer, tables/extension formatting, undo, read-only and disposal must be tested on their stated environment. These additions create future tasks only; no native support is established by authoring them.
