# Browser adapter contract

Qualification amendment (user decision, 2026-10-14): Named target-platform simulators/emulators and desktop OS VMs/test hosts may satisfy platform and release gates when physical hardware is unavailable. Follow the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms) for required runtime checks, tested virtual equivalents for hardware-only observations, counts and physical/virtual provenance. Earlier physical-only/manual-only wording in this document is superseded. This changes accepted evidence, not required implementation or correctness.

Status: development contract; real input support requires browser and device evidence.
Scope: framework-independent web editor plus a thin React lifecycle wrapper.
Public packages use the `@edit-ac` npm organization.
No full native editor parity is required for the initial web release.

## Optional Markdown in the Task preset

Under the user-approved 2026-10-13 profile change, the default persistent Task mount has no Markdown parser or automatic Markdown asset request. Hosts explicitly register the first-party Markdown extension to enable its paste, typing-shortcut and import/export behavior under formats.md. Without it, Markdown-looking plain text remains literal and unavailable codec operations retain source with diagnostics. Internal fragments, supported safe HTML, ordinary rich-text editing, persistence and collaboration retain their default guarantees. Examples and regression fixtures name whether Markdown is enabled; default and enabled configurations are qualified separately. React and Astro remain thin consumers of the same configuration.

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

## Shared resources across editors and site routes

This is planned delivery under SDK-1.9/1.10, with independent loading checks in FIT-1.6 and release measurements in REL-1.3. Existing module-local initialization and multi-mount tests are useful prerequisites; they do not establish the complete site-wide contract below.

Two host scenarios are mandatory: a task description and comment body mounted together, and task-description/document-body configurations on different routes of one site. A comment configuration is a host configuration over admitted capabilities, not a new mandatory preset. Use the existing Task and optional Markdown/presenter boundaries; document-tools/code-tools combinations become qualified only when their owning features are implemented. Configuration differences alone must not produce another engine binary or another copy of common JS/assets.

### Resource ownership and identity

| Resource | Sharing boundary | Instance-owned state |
|---|---|---|
| Core JS, generated glue and engine WASM | One resolved core module and initialized runtime per supported artifact identity in a browser realm; concurrent callers reuse its initialization promise | Each editor retains its own engine handle, document/epoch and live replica identity, selection, history, subscriptions and disposal |
| Optional Markdown and presenter libraries, grammars, essential CSS/fonts | Reuse the same versioned static artifact when multiple enabled instances need it; optional assets remain separate from the baseline graph | Registration, commands/keymaps, schema admission, parser options, mutable macro/grammar configuration, DOM and error/fallback state remain scoped to each editor |
| Injected styles and other static DOM resources | One installation per artifact and owner Document where injection is needed; teardown observes remaining users | An editor cannot remove resources still used by another editor |
| Workers and derived services | Reuse code/assets; pool execution only through an existing service contract that supports bounded, identity-scoped multiplexing and cancellation | Requests, outputs, permissions, queues and cancellation remain session-scoped; no new worker pool is required by this plan |

Share executable resources, never the writable document. Different task/comment documents retain separate history, document storage namespaces, active sync bindings and callback targets. Hosts may reuse stateless handlers and transport/auth/resolver services when every request remains bound to its initiating document/session and current permission scope; loading shared code cannot grant authority to a sibling instance. Deliberate collaboration on the same document continues through the existing identity/session/sync contracts. User uploads, private media, resolved metadata and signed URLs are content, not globally reusable static assets; their caches retain existing tenant/principal/security boundaries.

Artifact identity includes the exact compatible package/build, generated glue, ABI and resolved asset URL. All plain, React and Astro entry points in the supported site build resolve to the same core dependency and common chunks. Presets configure instances rather than embedding their own engine. Host build examples use one reviewed asset manifest and stable versioned URLs across routes; editor IDs, route names and preset fingerprints cannot become cache-busting suffixes. Detect duplicate resolved SDK copies/common artifacts in production output, including identical bytes emitted under different URLs. Prefer the existing dependency/export and host bundler/import-map controls over a new global runtime registry.

Retain `init(assetUrl)` and `initMarkdown(assetUrl)` semantics: one explicit URL per module instance, concurrent initialization sharing, rejection of a conflicting URL and retry after failure. Do not add an arbitrary URL-keyed runtime map over generated bindings that have one mutable WASM owner. Incompatible versions/glue or deliberately isolated realms are explicit separate owners, with separate costs; never alias them merely because a preset name or WASM filename matches. Imports and SSR rendering still perform no browser access, fetch, instantiation or document allocation.

### Loading and lifetime

Start optional loads only for enabled/needed features. A page with a Markdown-enabled description and a plain comment may load Markdown once for the description; that does not enable it in the comment. Test disabled-only pages for complete import/request absence and mixed pages against the union of enabled requirements. Adding a second enabled editor or visiting a route with overlapping capabilities loads only missing resources. Share initialization work without allowing one mount's abort/disposal to cancel another mount's required load. A failed load settles all affected waiters, preserves diagnostics/fallbacks and permits an explicit retry; no failed entry permanently poisons the loader. Disposed waiters cannot attach late DOM/listeners or leak a handle. Destroying one editor releases its state and pending work under the existing flush/report policy while other editors remain editable. The initialized module may remain ready for remount; retained runtime state must not retain disposed documents or grow with mount count.

Client-side navigation within the same realm reuses initialized resources. Full navigation, reload, tabs and frames have separate JS/WASM lifetimes: reuse stable URLs through normal HTTP caching where the browser permits, then initialize a fresh runtime in each realm. Document content-hashed/versioned deployment paths, appropriate cache headers, MIME/CORS/CSP behavior and version rollover without stale-glue/new-WASM mixing. A validated warm HTTP cache may avoid body downloads while still performing requests/revalidation; do not claim zero initialization or unconditional cache retention across pages. No service worker, SharedWorker or cross-tab mutable runtime is required.

### Required shared-resource cases

| Case | Required observation |
|---|---|
| SHR-01 | Concurrent task-description/comment mounts with the same configuration share one core load/initialization; edit, undo, save and destroy remain independent |
| SHR-02 | Mixed configurations in both mount orders, including two consumers of one optional parser/presenter, load the union once; a disabled instance keeps literal/fallback behavior and its own permissions |
| SHR-03 | Delayed initialization, disposal of one waiter, shared failure/retry and repeated mount/destroy leave the survivor usable, with no late handles/listeners or silent pending-save loss |
| SHR-04 | Packed plain, React and Astro production consumers, including mixed bindings, resolve one common runtime/artifact graph; SSR remains side-effect free |
| SHR-05 | Task route → document route → back via client navigation adds only newly needed features and preserves correct per-instance configuration and teardown |
| SHR-06 | The same journey through full navigation/reload in a controlled warm HTTP cache reuses asset bodies under declared cache policy while initializing each new realm; cold/cache-disabled results are separate |
| SHR-07 | Conflicting asset URLs and incompatible builds reject or use explicitly isolated owners; version rollover cannot mix stale glue/new WASM, and deliberately duplicated bundles/asset URLs are detected |
| SHR-08 | Concurrent optional rendering and teardown preserve shared styles/assets and isolate mutable renderer configuration, async results and private content/authority |

SDK-1.9 implements same-page sharing and SDK-1.10 owns the consolidated fixture/receipt rather than creating parallel framework harnesses. Record exact artifact/module URLs and hashes, import/chunk graphs, server requests/status/body bytes, browser cache provenance and initialization counts separately from live engine handles. Include cold/warm transfer, per-instance retained resources and first-visible/first-edit timing; reuse the gzip inventory and counting rules in verification.md. Unit loader counts alone cannot prove packed site deduplication or cross-route HTTP reuse. Missing required cases remain unqualified; existing progress receipts are preserved rather than relabeled as passes.

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
Automated event fixtures cover regressions; synthetic events do not replace physical or virtual platform evidence.

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
