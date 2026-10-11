# Browser adapter contract

Status: development contract; real input support requires browser and device evidence.
Scope: framework-independent web editor plus a thin React lifecycle wrapper.
Public packages use the `@edit-ac` npm organization.
No full native editor parity is required for the initial web release.

## Mounting and state

- One editor handle owns one Rust/WASM document handle and one coherent editing surface.
- Use a continuous contenteditable text flow with semantic block/inline mappings.
- Do not create a separate editable root for every paragraph.
- The imperative adapter owns DOM patches, selection mapping and input listeners.
- React mounts/destroys the handle and subscribes to scoped state; it does not render the document tree.
- Ordinary edits stay on the browser thread with the authoritative engine.
- Workers may prepare large parsing/export jobs; they do not mediate every keystroke.
- Multiple mounts reuse WASM initialization where safe, while retaining distinct replica identities.

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
