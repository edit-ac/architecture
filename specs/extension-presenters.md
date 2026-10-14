# Portable extension presenter protocol v1

EXT-1.6 supplies implementable host contracts and headless conformance, consuming
[the extension library](extension-library.md), [modules](modules-native.md) and
[client admission](client-contracts.md). Actual rendering, IME, accessibility and
OS clipboard qualification belongs to platform tracks. A passing adapter trace
is not evidence of native rendering or device parity.

The public `@edit-ac/web/modules` entry exports `PRESENTER_API_VERSION = 1`,
`PresenterAdapterV1`, `PresenterInputV1`, the typed focus/input/accessibility/
representation results, `PRESENTER_CAPABILITIES` and `ExtensionPresenterSession`.
These data shapes are the language-neutral protocol: Swift/Kotlin/terminal hosts
map their owning engine node IDs, UTF-16 anchor resolutions and committed patches
onto the same fields. They do not import a browser runtime into the Rust engine.
Callbacks are trusted per-view host resources; no callback or presenter object is
serialized in the document, descriptor payload or CRDT.

## Inputs and ownership

Each snapshot contains protocol version, stable `nodeId`/`sourceId`, validated
`ModuleViewContent`, current engine-resolved selection, current readonly state,
host theme and the named host capability record. Hosts derive snapshots from the
owning projection and frozen registry; a presenter must not infer editing
semantics from fallback text. Unknown/disabled module versions keep their bounded
opaque payload and explicit source fallback through the existing registry/codecs.
Snapshots and events are detached copies. The 1 MiB snapshot and representation
limit and 64 KiB temporary input limit reject oversized host data; these bounds
do not replace the engine's schema/command/codec resource checks. Typed-array
patch bytes are copied, never shared with engine storage.

| Obligation | Protocol and required behavior |
|---|---|
| Focus | `focus({owner, restore})` names editor, presenter or nested control ownership; cancellation restores editor focus according to host policy. |
| Input/composition | `input({type,text})` carries temporary host preedit only; composition cancels pending preparation and blocks command submission until end/cancel. No preedit is a semantic edit. |
| Selection/atom boundaries | `input.selection` and selection events use owning engine anchor resolutions/UTF-16 boundaries; hosts retain/release anchors. Atom navigation and semantic admission use qualified engine primitives, never inferred DOM offsets or a second document. |
| Accessibility | `accessibility()` returns a semantic label, explicit action names and readonly state; host widgets map these to their platform accessibility APIs. Unsupported rich views expose honest source/alt labels. |
| Clipboard/source | `representation(mime)` returns bounded inert `text/plain` or `text/markdown` plus explicit fallback. OS clipboard access is separately host-granted; rendering/representation performs no asset/reference fetch, formula execution or permission grant. Rich formatting transfer remains EXT-1.13. |
| Incremental patches | `update({input,event})` receives filtered `ModuleRuntime` events after engine transactions. Null event is initial/explicit host refresh. Selection is independent opt-in; irrelevant source patches do not invoke the adapter. |
| Cancellation | `cancel()` aborts pending command preparation and temporary input; request identity/revision checks suppress cancelled, superseded and stale completion. Host revision includes document/epoch/content and target validity; host capabilities recheck at commit. |
| Disposal | `dispose()` detaches subscriptions and pending requests before attempting adapter cancel/dispose; repeated teardown has no live callbacks. Hosts free focus, listener, observer, worker, view and anchor resources even when callbacks fail. |
| Readonly/history | `run(prepare)` uses `ExtensionCommandSession` and the host's shared can/commit boundary; UI readonly snapshots are advisory, current host admission is authoritative. Host owns one-intent atomic history and persistence recovery. |
| Theme/fallback | Host supplies theme; absent renderer/codec preserves source with an explicit fallback flag rather than claiming rich rendering/edit parity. |

Adapters synchronously implement update, focus, input, accessibility,
representation, cancel and dispose. Allocate resources exception-safely; a failure
before return must release any partial resources. The session detaches on callback
failure and attempts all teardown hooks. ModuleRuntime isolates callback errors
so a committed edit stays committed. This is exception isolation, not a claim to
preempt an infinite loop. Heavy/untrusted work needs the existing host worker or
process isolation and limits. No new event bus or writable semantic store exists.

## Host records and downstream qualification

All five records use engine stable UTF-16 selection, host-temporary composition,
semantic labels/actions, host-granted clipboard, inert Markdown fallback,
ModuleRuntime patch delivery, abort/stale cancellation and idempotent disposal.
The focus mode identifies the host binding, not availability of a full renderer.

| Host | Focus binding | Actual qualification owner |
|---|---|---|
| browser | DOM | Browser integration / [41 mobile web extensions](../roadmaps/41-mobile-web-extensions.md); actual DOM, touch/IME, accessibility and clipboard evidence |
| terminal | terminal focus/input | [15 TUI client](../roadmaps/15-tui-client.md); terminal navigation, paste and accessible fallback |
| swift-ios | native focus/input | [16 iOS SDK](../roadmaps/16-ios-sdk.md); Swift adapter, native IME/accessibility/clipboard and device observations |
| kotlin-android | native focus/input | [17 Android SDK](../roadmaps/17-android-sdk.md); Kotlin adapter, native IME/accessibility/clipboard and device observations |
| desktop | desktop focus/input | [18 desktop native](../roadmaps/18-desktop-native.md); desktop controls, selection, accessibility and OS clipboard |

Each owner consumes the fixed `core/fixtures/extensions/presenters/conformance.json`
IDs `PRES-<host>-<obligation>`, preserves the same command/source/capability
boundary and adds its actual platform receipts. Their evidence is pending; this
track depends on none of those completed renderers. Physical FMT-1.15 remains a
release gate; the existing virtual development receipt does not qualify real IME
or accessibility. Built-in per-module parity cells are delivered by EXT-1.7.

## Canonical conformance

Build current packages, set a unique absolute worktree-owned
`EDITAC_EXTENSION_PRESENTERS_OUTPUT`, then run from core:

```sh
npm run build
node --test tests/extension-presenters.test.mjs
```

The suite packs/installs public artifacts offline, typechecks independent public
imports and executes all five headless adapters over production WASM, actual
ModuleRuntime, prepared command admission and storage middleware. IndexedDB
transaction completion is deterministic prepared transport; there is no native
OS renderer, actual browser document or deployed storage claim. It checks every
manifest obligation, rejects missing/duplicate/zero host coverage, retains pack
and child logs/results, and cleans the temporary consumer on success/failure.
See [presenter evidence](../evidence/extension-presenters.md) for pinned revisions,
counts and honest platform limitations.
