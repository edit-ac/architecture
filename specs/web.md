# Browser adapter contract

Status: development contract; real input support requires browser and device evidence.
Scope: framework-independent web editor plus a thin React lifecycle wrapper.
Public packages use the `@edit-ac` npm organization.
No full native editor parity is required for the initial web release.

## Mounting and state

- One editor surface binds one Rust/WASM document handle and one coherent editing flow.
- Use a continuous contenteditable text flow with semantic block/inline mappings.
- Do not create a separate editable root for every paragraph.
- The imperative adapter owns DOM patches, selection mapping and input listeners.
- React mounts/destroys the handle and subscribes to scoped state; it does not render the document tree.
- Ordinary edits stay on the browser thread with the authoritative engine.
- Workers may prepare large parsing/export jobs; they do not mediate every keystroke.
- Multiple mounts reuse WASM initialization where safe, while retaining distinct replica identities.

The persistent `mountEditor` facade and synchronous `mountEditorSurface` for a
host-owned engine use one adapter binding for rendering, selection and input.
Reserve the root before asynchronous recovery; duplicate mounts through either
API fail before replacing DOM or attaching listeners. Detaching a host-owned
surface releases adapters and anchors while leaving its engine with the host.
The persistent facade retains its recovery, durability and destruction contract.
Examples consume the public package mount and the same behavior defaults.

## Baseline typing and rendering guarantees

Baseline browser work owns authored whitespace and heading-end Enter. These
guarantees are required before the follow-up interaction/regression infrastructure.
The renderer preserves leading, trailing and repeated U+0020 spaces on paragraphs,
headings, marked runs and list items independently of the host stylesheet. Prose
text blocks use `white-space: break-spaces`; code preserves literal unwrapped
spacing. Tag replacement, incremental patches and read-only rendering retain this
policy. Presentation does not trim text or replace authored spaces with NBSP.
Hosts retain renderer-owned whitespace properties when customizing presentation.

At a nonempty heading end, Enter retains the heading and inserts a sibling
paragraph before the next sibling, including an immediately following list.
One prepared engine transaction supplies the resulting stable caret; the next
typed character enters that paragraph. The list's identity, parentage and text
remain intact. Undo/redo restore content at each intent boundary. Stored-selection
restoration across undo/redo is separately qualified by RGS-1.3/G07, including
undo that removes the newly created paragraph; content-only checks do not pass
that selection gate.

`npm run check:browser-baseline` in core builds the pinned WASM engine from current
Rust sources and builds the adapter packages, then runs the unfiltered baseline
exit gate over renderer, keyboard and public-example suites in Chromium, Firefox
and WebKit. Existing generated WASM alone cannot qualify a changed engine source.
Assert exact semantic/DOM code points, visible advances for authored spaces,
resulting caret and subsequent typing, unchanged neighbors and history effects.
Record nonzero executed/passed/failed/skipped counts and source/artifact hashes.
Prove whitespace assertions fail when leaf rendering collapses spaces. Text-only
equality or screenshots alone cannot qualify these guarantees. Tracks 38/42 extend
this coverage; their availability does not defer a failing baseline regression.

## WASM distribution

Use an explicit browser ES-module build and asynchronous initialization contract.
The initial candidate is wasm-bindgen 0.2.129 with matching CLI and wasm-pack 0.15.0.
Keep crate, generator and generated artifacts version-compatible and reproducible.
Ship the required `.wasm` file in the packed package and expose a host-controlled asset URL/init option.
Avoid implicit DOM access during module import so SSR hosts can load the package safely.
SSR import safety does not mean the editor can mount without a browser.
Test package exports/types and the packed tarball from an independent consumer directory.
Test a bundler host and direct browser asset loading; document CSP, MIME and CDN requirements.
Generated package metadata must not overwrite maintained public exports, license or publication settings.
Report complete JS, WASM and essential CSS bytes, including transitive editing dependencies.

## Lifecycle and loading

`visible` means a content projection has been displayed.
`ready` means authoritative recovery, input handlers, selection mapping and persistence attachment are complete.
`localCommitted` identifies an update whose local storage transaction completed.
`remoteCommitted` identifies an update with a durable service receipt.
These signals are distinct; showing a preview does not authorize editing it.

Restore a checkpoint plus bounded journal tail before accepting edits.
Adopt a preview only when its document/session, schema and revision metadata match recovered state.
If preview and recovery disagree, render recovered state before enabling input.
Never re-import initial Markdown/JSON into an existing document because the network is slow.
Initialization failure leaves an accessible read-only/recovery view with a visible error.
`flush({target: 'local'})` resolves after pending local commits or rejects with a typed storage error.
Destroy must settle or explicitly reject pending work and remove all listeners/observers/subscriptions.
Document whether failed persistence requires recovery export before a host discards the handle.

## Input routing

Handle `beforeinput`, `input`, composition events and a bounded MutationObserver fallback.
`beforeinput` is not always present or cancelable; check the actual event before preventing default.
Use semantic commands for structural operations and browser-native insertion where validated.
Maintain an origin/suppression mechanism for adapter-generated DOM changes.
Reconcile only the affected semantic range; one browser edit must not be committed twice.
Do not serialize the whole document or scan all formatting on the typing path.
Do not synchronously invoke networking, Markdown export or React document rendering from input handlers.
Honor read-only state in keyboard, paste, drag/drop, composition and command paths.
Selection-only changes emit scoped selection state without document updates.

Heading-end Enter uses the atomic `headingEnd` engine command qualified by WEB-1.14 under [the engine contract](engine.md#atomic-heading-end-enter). WEB-1.8 applies the resulting stable caret and qualifies the full keyboard suite. Separate live split/format commits or guessed generated owner IDs do not satisfy that behavior.

## Composition gate

The browser temporarily owns its active composing DOM subtree.
Remote updates may change the authoritative core, but must not replace the composing subtree underneath IME.
Capture composition anchors and the affected text/selection before it starts.
Reconcile committed composition against current core state using the proved anchor policy.
Do not convert intermediate IME events into independent typing/history groups.
If the target disappears, preserve composed text and report a recoverable conflict instead of redirecting it.
Define cancellation, blur, compositionend ordering and remote-overlap handling in the input ADR.
The ADR must specify whether intermediate composition is committed or buffered, with matching fixtures.
Do not select a policy by assuming all engines deliver the same event sequence.
No supported-IME claim is allowed until real OS input checks qualify the policy.

Required composition cases include Japanese/Korean/Chinese input, accents/dead keys, emoji and replacement selection.
Test remote insertion before/inside/after composition and remote deletion of its block.
Test paste, undo, blur, read-only transition and destruction during a composition.
Automated event fixtures cover regressions; synthetic events do not replace real-device evidence.

## Selection, navigation and DOM patches

Convert DOM positions to UTF-16 core positions through explicit mapping functions.
Preserve anchor/focus direction and affinity across incremental patches.
Use relative anchors across asynchronous operations and remote updates.
Test cross-block selection, empty blocks, hard breaks, inline atoms, lists and noneditable attachments.
Support keyboard navigation and screen-reader semantics through normal document structure.
Patch changed nodes/spans; do not replace the full editing subtree after every transaction.
Renderer caches are disposable derived data and must rebuild from core state.
Keep user selection stable when unrelated blocks change.
Avoid true viewport removal until selection, find, copy-all, accessibility and IME behavior are qualified.
Layout containment/deferred decorations must be measured and must not hide editable content from access tools.

## Clipboard and drag/drop

Follow the deterministic import precedence and safety policy in [formats.md](formats.md).
Paste prepares a single semantic edit and forms one explicit undo group.
Oversized preparation captures an anchor and supports cancellation/stale-target detection.
Pasting into code is literal; a visible plain-text paste command remains available elsewhere.
Drag/reorder UI invokes a semantic move only after the structural schema gate passes.
Cross-editor fragments are untrusted versioned input and use the same schema/resource checks as imports.
Do not execute embedded HTML handlers, document code or URLs during preview/import.

## Persistence and host events

IndexedDB adapter callbacks occur after transaction completion.
Surface quota/permission/closed-database errors and retain in-memory recovery content where possible.
Strict IndexedDB durability remains a hint; document its actual browser guarantee.
Do not depend on unload handlers for persistence or advertise universal power-loss survival.
Subscribers receive changed ranges, origin, revision/update metadata or selection state.
Full-document JSON/HTML/Markdown exports are explicit host actions, not implicit save callbacks.
Presence is throttled and ephemeral; it cannot delay local input or local persistence.
Attaching/detaching a transport must not replace the existing document or alter schema semantics.

## Browser qualification and performance

Record exact Chromium, Firefox and WebKit versions and OS/device versions in every release report.
Pin the automated browser toolchain separately from manual Safari/IME device evidence.
Measure first display and first accepted edit independently, including recovery and WASM startup.
Measure small/long/aged documents, paste peak memory, remote bursts and repeated mount/destroy.
Original roadmap budgets remain proposed targets until a reproducible report accepts or revises them.
Use feature-equivalent comparison fixtures and include optional-module bytes explicitly.
Keep failing/skipped evidence and a published supported/unsupported input matrix.
Close test browsers and temporary servers; preserve only explicitly requested previews.

## Primary references

- [Input Events composition/cancelability](https://www.w3.org/TR/input-events-2/)
- [Observed beforeinput browser constraints](https://developer.mozilla.org/en-US/docs/Web/API/Element/beforeinput_event)
- [wasm-pack build targets](https://rustwasm.github.io/docs/wasm-pack/commands/build.html)
- [IndexedDB durability](https://w3c.github.io/IndexedDB/)

## Everyday interaction acceptance

[Editor interactions](editor-interactions.md) defines Enter/Shift+Enter, selected and pending formatting, contextual Tab, platform navigation, Unicode/whitespace, slash controls and non-keyboard replacement. Use its [case catalog](../tests/editor-interaction-cases.md) for browser input work. Track 38 closes this coverage before browser release; it does not replace the baseline tasks or their engine/storage prerequisites. Baseline OS dictation and screen-reader editing remain mandatory with optional extensions disabled. [Assistive input](assistive-input.md) adds optional host-controlled presentation through track 39.

## Mobile web and touch

[Mobile web](mobile-web.md) defines native touch selection/scroll preservation, mobile keyboard/replacement events, focus/command access, viewport/keyboard occlusion, capability fallbacks and the incremental cost gate. Track 40 and its [59 cases](../tests/mobile-web-cases.md) qualify the baseline before browser release. APIs such as VirtualKeyboard, keyboard layout/lock and EditContext are progressive or experimental capabilities with explicit fallback; they are not universal browser prerequisites. Track 41 qualifies richer extension presenters separately. Real mobile browser modes/devices remain distinct from emulation and native SDKs.

## Regression guard integration

Apply G01–G14 in [the editing suite](editing-regression-suite.md) when implementing input, selection, composition, patching and module event ownership. Correlate actual intents across notifications without deduplicating identical deliberate text; suppress only identified renderer echoes. Capture semantic selection/pending-mark intent before preparing a compound command, and publish callbacks after commit/lock release under a declared queue/rejection policy. WEB input implementation requires the qualified composition ADR from WEB-1.13's real-DOM/real-engine protocol probes, before WEB-1.4. Track 42 later reuses that evidence and proves the shared driver and guard assertions against the completed adapter before interaction qualification. Native IME/device support remains separately qualified.

## Clipboard routing and plain paste

WEB-1.9 owns internal fragments, bounded inert rich-HTML mapping and literal text in the minimal host. Clipboard routing is independent of keyboard input: native menu ClipboardEvents and beforeinput-only/noncancelable mobile sequences are correlated by the event lifecycle, never payload equality or timing. Follow-on native DOM notifications cannot double-commit a handled transfer. Ctrl/Command+Shift+V and macOS Command+Option+Shift+V opt into literal paste; hosts must also expose a labeled Paste without formatting command. Reading the script clipboard is an explicit activated action, never a mount-time permission request. Denied/absent APIs leave native paste available.

Codec ports preserve the format precedence in formats.md; full Rust Markdown/GFM qualification remains FMT-1.2–FMT-1.8 and the full-palette integration task FMT-1.13. Tables and other extension formats require the registered semantic codec and EXT-1.13; unavailable codecs retain source and diagnostics rather than pretending to preserve rich structure. Plain paste and code targets bypass every rich codec. Async plain reads retain the initiating target and preserve later navigation, with cancellation on read-only or disposal. Native SDK simulator/emulator and physical-device testing is planned separately; browser event replay does not qualify mobile OS pasteboards.

The optional built-in plain-paste control has a labeled native button and accepts touch or keyboard activation; hosts can disable it while providing their own labeled command. Literal paste never brings incoming formatting or parses syntax, while retaining the destination's admitted text style, especially inline-code context. Common platform-primary B/I/U and Shift+X shortcuts use the same applicability-checked semantic formatting port as toolbar commands.
