# Native controls, React Native, Expo and Flutter

Status: PLANNED. Research and user scope: 2026-10-24. The [UI delivery index](../runner-queues/editor-ui-integrations-20261024/README.md) owns bounded implementation and acceptance. This extends the [editor UI proposal](editor-ui-integrations.md), not the active runner. All package names below are provisional until inventory reconciles existing exports.

## Scope and authority

Required delivery includes native iOS, macOS, Android, Windows and Linux controls; React Native with bare and Expo development-build consumers on iOS/Android; Flutter controls and native editor embedding on iOS/Android; and explicit Expo web/Flutter web profiles over the existing browser editor. Each profile has its own qualification status. Native support is never inferred from a browser demonstration.

React Native macOS/Windows and Flutter desktop are separately assessed host candidates. The native desktop SDKs remain required, but a working AppKit/WinUI/GTK editor does not establish that Flutter or React Native can embed it. Record a concrete host boundary, supported runtime and follow-up implementation owner before advertising those combinations. A blocked feasibility result does not waive mandatory mobile or browser profiles.

The [backend SDK plan](backend-sdk-adapters.md) retains engine/transport/lifecycle ownership: BCP-1.1–1.3 own Dart and Flutter bridge/widget, BCP-1.4–1.5 own React Native module/Fabric component, BNA owns Apple/Android persistence hosts, and BDH owns desktop integration. New work extends those interfaces with UI state and controls rather than creating parallel views, native sessions, CRDTs, wire protocols or persistence algorithms. BCP-1.6 remains the base cross-platform save/load example owner; the new examples add themed controls and Expo installation to that base.

UIC-1.6's [individual staged owner rows](../runner-queues/editor-ui-integrations-20261024/adoption-map.md#existing-owner-acceptance-additions) resolve those handoffs against their named parent definitions and the package ledger. A native consumer requires the [source/interface receipt](../runner-queues/editor-ui-integrations-20261024/adoption-map.md#sourceinterface-receipts) for its actual state/theme/target/geometry boundary, executor and disposal behavior. An absent method, event or supported surface is a missing prerequisite of that existing BNA/BDH/BCP owner; it never authorizes a second bridge or independent runner. BNT and roadmap43 retain runtime and platform qualification. Resolved ownership and DTO declarations do not make native ingress or embedding available.

Reuse [native SDK parity](native-sdk-parity.md), [platform editing services](platform-editing-services.md), [extension presenters](extension-presenters.md), [block actions](block-actions.md), [durability](document-durability.md) and the one-current-format decision. Display preferences never rewrite document bytes. Every control targets the same engine history and current-format identity.

## Native design-system mapping

| Host | Default toolkit integration | Required behavior |
| --- | --- | --- |
| iOS / iPadOS UIKit | UIKit toolbar/actions, contextual edit menus, keyboard accessory where appropriate | Extend system editing actions; preserve input responder/composition and Dynamic Type, VoiceOver and safe areas |
| SwiftUI | Toolbar/Menu and existing representable host | Observable immutable command state; SwiftUI recomputation does not replace the editor/session |
| macOS AppKit | NSToolbar, validated NSMenu actions and responder commands | Cmd shortcuts and Edit menu use shared undo/redo; multiwindow targets cannot bleed |
| Android Views | Material-compatible buttons/menu/search and existing editor view | Respect focus, keyboard insets, font scale, TalkBack and system action mode |
| Jetpack Compose | Material 3 controls around the existing native view | Recomposition does not create an editor; host uses established Android view interoperability |
| Windows WinUI | Fluent command bars, menus/flyouts, theme resources and UI Automation | Shared command state, keyboard/access keys, high contrast and per-window ownership |
| WPF | Existing native host wrapper plus WPF commands/resources | Reuse WinUI/native Session bridge where owned; no new editor implementation |
| Linux GTK | GTK actions/menu models/popovers; optional libadwaita toolbar/header integration | GTK-only users do not require libadwaita; AT-SPI, scaling, theme and focus remain native |
| Electron / Tauri | Existing browser UI packages inside qualified desktop host | Consume existing IPC/security/backend boundary; no second desktop semantic implementation |

The initial source inventory includes `core/native/ios/Package.swift`, `core/native/macos/Package.swift`, native command tests, Android SDK/consumer sources and platform capability manifests. These are reuse locations, not evidence that the proposed controls already exist. The contract task must inspect actual exported symbols before selecting new source paths.

Official references: [UIKit edit menus](https://developer.apple.com/documentation/uikit/uieditmenuinteraction), [SwiftUI toolbars](https://developer.apple.com/documentation/swiftui/toolbars), [AppKit toolbar facilities](https://developer.apple.com/documentation/appkit/toolbar), [Compose Material 3](https://developer.android.com/develop/ui/compose/designsystems/material3), [Windows controls](https://learn.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/), and [AdwToolbarView](https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/class.ToolbarView.html). These inform presentation choices; they do not prove editor integration or permit replacement of existing input owners.

## Portable UI contract

Use the same command IDs, availability/reasons, active/mixed state, value, progress and stable target sessions as the browser. Platform adapters map those values to native properties and accessibility traits. Do not send React components, DOM nodes, closures or CSS strings across native bridges.

Theme data is a bounded typed record: semantic colors, typography categories, spacing/density, radii, icon identifiers, direction and accessibility preferences. Map to platform fonts/colors/resources on the UI thread. Leave platform default measurements intact unless the host deliberately overrides them. Live theme changes update presentation without reimporting content or recreating the native surface. Content typography and toolbar density are independent. Rich text marks remain validated semantic data, not appearance-only overrides.

Every command capture names document/epoch, native surface/session and permitted overlay owners. Validate at execution; reject stale/disposed targets without retargeting. Route callbacks outside engine locks onto the proper UI executor. Event streams use stable IDs and bounded payloads; UI state updates may coalesce, but completion/error/disposal receipts cannot be lost. Async suggestions cancel on query/session changes, never steal focus, and preserve composition. Framework state mirrors observations only.

Native controls expose slot/builders for button, group, menu, result row, dialog, status and icons in the host language. The native editor remains the sole owner of editable descendants. Native system cut/copy/paste, undo/redo, spellcheck and selection affordances remain available under platform policy. A custom toolbar must not enable an independent native undo stack or intercept every key before the input system.

### Actual native export mapping (UNC-1.1)

The [native command and target export map](../../core/sdk/contracts/native-ui.md)
and its source inventory `core/sdk/contracts/native-ui-exports.json` map every
portable command-state/captured-target field to the existing Session/presenter
boundary or an exact BNA/BDH host gap. UIKit, AppKit, Android Views, WinUI/WPF
and GTK each have command, capture and disposal source/interface entries;
SwiftUI/Compose wrappers and desktop shells retain their existing owners.
Native semantic route IDs are not browser control IDs. The C ABI owns engine
plans/anchors, while Swift/Kotlin and the narrow Linux C++ wrapper use the
existing generated-UniFFI NativeSession; neither exposes a common native UI
command view or overlay target session today. Existing narrow command/selection
operations are not that missing control bridge. All native UI/OS qualification
remains deferred and unchecked in its original owners.

`node scripts/ui-integration-delivery.mjs UNC-1.1` inspects those actual exports
and owner definitions, covering one command and capture/disposal mapping per
native OS and counting supported source rows separately from explicit gaps.
It does not execute a native host, qualify a platform or complete any missing
BNA/BDH/BCP hook. This factual inventory adds no semantic command, API/wire/ABI,
persistence host or second view.

### Native presentation record bindings (UNC-1.2)

The [native presentation contract](../../core/sdk/contracts/native-ui.md#native-presentation-data-bindings-unc-12)
and `core/sdk/contracts/native-ui.schema.json` define one closed data-only record:
existing UIC theme, control descriptors and nine-field command-state rows. The
schema references the existing theme schema; `core/sdk/contracts/native-ui.ts`
imports the canonical UIC types. Reject serialized UTF-8 input over 65536 bytes
before parsing, keep the theme's 4096-byte cap, validate the full schema and
existing descriptor/command authority before atomically applying any update.

Authored `EditacUIContracts` Swift values are shared and re-exported by the existing
Apple SDK targets; corresponding `ac.edit.android.ui` records live in the existing
Android SDK. Native pressed/value enums preserve UIC mixed/null and primitive
variants explicitly. Headless compile-only consumers and schema/source inspection
are selected by `node scripts/ui-integration-delivery.mjs UNC-1.2`; they do not
execute a native decoder or qualify a host. These declarations add no UniFFI/C ABI,
transport, Session or semantic command. Actual ingress must enforce caps, schema,
registered action/state ownership, copying and executor/lifecycle rules; the
existing BNA/BDH/BCP owners retain that implementation. Windows/Linux host records,
actual theme propagation/state observation and all native OS/UI/IME/AT qualification
remain deferred under their existing owners, with source gaps in UNC-1.1's map.

### Overlay ownership and event ordering (UNC-1.3)

The [overlay/event contract](../../core/sdk/contracts/native-ui.md#overlay-and-event-contract-unc-13)
adds explicit captured focus owners, native coordinate frames/conversion and
revocation rules to the existing BCP/BNA/BDH boundaries. Detached public types
are exported through `core/sdk/contracts/native-ui.ts`; the single closed
`native-ui-events.schema.json` reuses the UNC-1.2 presentation schema. These are
contract declarations, not a new bridge, wire transport, serializer or native
API implementation. Keep the existing Session, capture, command and buffer owners.

Capture before focus transfer; validate the exact document/epoch/editor/session/
surface, registered overlay and focus generation again before activation. Never
retarget on stale/revoked input. Geometry requires same-window current source and
destination frames, finite nonsingular conversion, all four corners and clipping;
never double-apply scale or infer another window. Async work retains its original
identity, invalidates superseded query generations and never restores focus.

Only UI snapshots coalesce between reliable barriers. Emit completion/error,
revocation and final disposal in stream sequence order, preserve one terminal
receipt per admitted request even after UI revocation, and never map uncertain
post-dispatch cancellation to rollback. Reserve bounded receipt capacity before
admission; reject overflow before dispatch. Disposal stops admission, revokes,
settles/drains admitted work and emits disposed last. No late result applies to
a replacement view. The named contract fixes payload/queue caps and executor/
buffer ownership; no lossy event channel satisfies it.

`node scripts/ui-integration-delivery.mjs UNC-1.3` inspects deterministic authored
transcripts/schema and compiles a public consumer without executing a native
host. Existing BNA/BDH/BCP owners retain missing registration, coordinate, target
and reliable-stream APIs; their exact host mapping is in the contract and
UNC-1.1 inventory. Native transport/UI/IME/AT qualification remains deferred.

### Per-platform planned export/support map (UNC-1.4)

The [frozen map and adoption table](../../core/sdk/contracts/native-ui.md#frozen-planned-ui-support-map-unc-14)
and authored `core/native/ui/support-map.ts` define 15 optional integration
boundaries and 26 explicit profiles: 19 required native/mobile/web, one optional
libadwaita composition and six per-OS RN/Flutter desktop feasibility profiles.
The public `nativeUISupportMap` and readonly types are exported through the
existing `core/sdk/contracts/native-ui.ts`; they are planning metadata, never
runtime capability detection or a new bridge/wire contract.

Decision007's dedicated repository/distribution map supersedes the older colocated
package shapes below while current source roots remain unchanged until extraction.
Exact planned exports, required/optional/excluded peers and separate common,
native and browser dependency branches preserve Views/Compose, UIKit/SwiftUI,
GTK/libadwaita and bare-RN/Expo independence. Material/Cupertino share the Flutter
plugin; Paper/Reusables have optional independent distributions. Expo UI remains
chrome over the canonical BCP Fabric view. Expo/Flutter web owns an explicit
browser entry and does not wait for BNA/BDH native host delivery.

Every profile names UI, host and backend owners independently, missing control
state/theme/capture/geometry/event APIs and exact receipt-based resume conditions.
Every baseline names local input paths, required framework/toolchain/ABI pins,
primary maintained-release sources and the existing freeze owner. Existing local
pins are inputs, not current-maintenance or support claims; absent Compose,
Windows, RN, Expo or Flutter package/peer locks remain owner gates. UEX-1.1 still
owns the compatible maintained Expo/RN/Hermes/toolchain freeze. UFW-1.4 retains
all desktop embedding decisions, including explicit unproven RN Linux hosting.
The [source inventory](../../core/sdk/contracts/native-ui-exports.json) retains
actual native exports; the map does not implement their missing host APIs.

`node scripts/ui-integration-delivery.mjs UNC-1.4` reviews package/peer/profile
consistency against the staged adoption map and exact owner definitions, then
compiles an importing public TS consumer. Counts are source inspection and
production compilation only, with no native startup or runtime support claim.
BNT/roadmap43 and the original UI owners retain all platform qualification.

### Frozen theme data mapping (UIC-1.4)

`core/contracts/ui-theme.schema.json` is the native theme ingress shape, using
the existing `core/contracts/` directory rather than the proposed absent
`sdk/contracts/`. `UITheme` in `core/packages/web/src/ui/theme.ts` declares the
same presentation data for web consumers; its `UI_THEME_TOKENS` map is the sole
CSS token naming authority. The native schema permits no extra fields at any
object level, callbacks, CSS expressions, DOM objects or arbitrary icon payloads.
The entire serialized UTF-8 theme is limited to 4096 bytes before parsing; schema
validation and the byte limit must pass before any update. Reject invalid data
atomically, preserving the prior theme and document. No transport or ABI has
been added by publishing declarations in source.

| Data field | Native UI-thread mapping / web token key |
| --- | --- |
| `colorScheme` | Resolved `light` or `dark`; host observes system changes |
| `colors` | Thirteen fixed semantic RGBA colors; unsigned 32-bit `0xRRGGBBAA`, decode as unsigned channels / matching `UI_THEME_TOKENS` keys |
| `contentFont` / `contentSize` | System, serif or monospace family; small/medium/large base category with platform text scaling applied once / contentFontFamily, contentFontSize |
| `chromeFont` | System font only, preserving platform control metrics / chromeFontFamily |
| `contentSpacing` | Tight/normal/relaxed paragraph spacing, independent of toolbar density / paragraphGap, contentLineHeight |
| `chromeDensity` | Compact/comfortable touch-aware control metrics / chromeGap, controlBlockSize, controlPaddingInline, chromeFontSize |
| `radius` | None/small/medium/large platform resource category / radius |
| `icons` | System/outline/solid built-in icon-set identifier; no images, paths or executable loaders |
| `direction` / `locale` | Explicit ltr/rtl layout and host-owned BCP-47 locale (1–63 ASCII characters); retain native text direction/composition authority |
| `highContrast` / `reducedMotion` | Resolved host preferences; preserve stronger platform accessibility settings |

`contentLineHeight`, `shadow`, `overlayZIndex` and `disabledOpacity` are web
presentation hooks where no native scalar equivalent exists. Native adapters
use platform layout, elevation, stacking and disabled traits; never transport
CSS strings or web z-indices. Forced colors/high contrast and user text scaling
take precedence over theme preferences. Native dialogs inherit the originating
surface's current theme/locale/direction and stable owner; per-window editors
cannot overwrite each other's resources. Theme updates never recreate a session,
replace content or change semantic marks. Existing BCP/BNA/BDH and native UI
owners retain bridge validation, UI executor and lifecycle implementation.
`core/tests/fixtures/ui-theme.json` contains a prepared valid native example;
UIC-1.4 does not claim that a native runtime has consumed it.

## Package and distribution boundaries

Repository planning update, 2026-10-26: [Decision 007](../decisions/007-integration-repositories-and-packages.md) and the [integration distribution catalog](integration-distribution.md#native-catalog) supersede repository placement in the shapes below. Each maintained host integration has a dedicated repository and installable ecosystem package. Closely coupled products/controls may stay within that integration, and shared engine artifacts remain core-owned. Existing BNA/BDH/BCP/UI task owners and capability limits remain intact; extraction and registry listings require separate handoff acceptance.

| Boundary | Proposed distribution shape |
| --- | --- |
| Apple | UI products/targets in existing Swift packages, separating UIKit/SwiftUI/AppKit as platform availability requires; reuse existing engine binary |
| Android | Optional Views and Compose UI modules/artifacts beside the existing SDK; Compose not required for a Views consumer |
| Windows/Linux | Controls module beside existing native SDK; optional WPF/libadwaita adapters; platform peers declared explicitly |
| React Native | Existing BCP-owned package, provisionally `@edit-ac/react-native`, with `/controls` and `/ui`; bare RN does not depend on Expo |
| Expo | Optional `@edit-ac/expo` configuration/plugin and host integration over the RN package; no second native editor module |
| RN design systems | Optional Paper adapter and React Native Reusables source kit; default controls work without either |
| Flutter | Existing BCP-owned plugin, provisionally `editac_flutter`, platform interface and implementations only where federation gives a real boundary; optional UI package/exports for Material and Cupertino |
| Flutter web | Explicit web implementation over `@edit-ac/web` through a bounded JS bridge; no native-engine claim, no hidden iframe/WebView |

Names must be reconciled before examples import them. Keep source/codegen input in Git; generate native bindings, binaries, Pods/build outputs and registry bundles outside tracked source. Do not publish packages or use paid build services as part of roadmap execution.

## React Native and Expo

[React Native native components](https://reactnative.dev/docs/fabric-native-components-introduction) provide the host-view boundary. BCP owns that implementation and New Architecture/codegen/autolinking choices. UI tasks consume its real native surface and stable event API. Do not introduce an Expo Modules view beside a competing Fabric view. If an Expo compatibility repair is needed, land it in the BCP owner with one canonical bridge.

Expo support is mandatory, specifically:

- iOS and Android development builds include the editor native code and work locally through supported Expo commands. The [development-build model](https://docs.expo.dev/develop/development-builds/introduction/) supports custom native libraries; [stock Expo Go does not](https://docs.expo.dev/faq/). Detect a missing native module and show actionable development-build guidance rather than silently falling back to a WebView.
- A [config plugin](https://docs.expo.dev/config-plugins/introduction/) applies only required native configuration. CNG/prebuild is repeatable and idempotent, preserves app-owned config, does not grant unrelated permissions, and documents projects with committed native folders. Use autolinking for capabilities it already owns.
- Freeze compatible Expo SDK, RN, Hermes, New Architecture, Xcode/Android toolchain and native package constraints from official maintained releases during implementation. No synthetic previous/current editor-format matrix is introduced.
- Expo Router navigation, screens/sheets, keyboard avoidance, safe areas, foreground/background and refresh/unmount retain session identity and observable unsaved recovery. Teardown is explicit; native callbacks cannot reach a replaced JS instance.
- Native ABI/view changes require a compatible rebuilt binary. Define a [runtime-version policy](https://docs.expo.dev/eas-update/runtime-versions/) so JS updates cannot assume missing native APIs. No EAS account, paid build, update publication or signing credentials are required for local validation.
- Expo web selects the browser binding explicitly through conditional exports. It imports no iOS/Android binary and remains SSR-safe. It is a distinct supported web profile, not proof of native parity.

Default RN controls use native accessibility roles/states, touch sizing and theme props. [React Native Reusables](https://reactnativereusables.com/docs) provides a shadcn-like application-owned source model, including NativeWind/Uniwind options; qualify one maintained styling baseline first. Its source is not interchangeable with React DOM shadcn or Radix DOM components. A [Paper theme integration](https://callstack.github.io/react-native-paper/docs/guides/theming) is an optional adapter, not a mandatory runtime dependency.

[Expo UI](https://docs.expo.dev/versions/latest/sdk/ui/universal/) offers native SwiftUI/Compose controls and a universal layer. Add a bounded control recipe over the same RN bridge; verify Host nesting, focus, menu placement and platform availability. Expo UI does not itself provide the editor's text surface. Do not claim every control exists on every platform merely because the package has a universal entry.

## Flutter

BCP-1.1 keeps the Dart backend client usable without Flutter; BCP-1.2/1.3 own plugin/native-view lifecycle. UI tasks supply controller views and styled widgets over those outputs. [Flutter plugin guidance](https://docs.flutter.dev/packages-and-plugins/developing-packages) informs package interfaces and optional federation. A UI package does not own a second engine or platform channel protocol.

Required mobile support uses the actual iOS and Android native surfaces through [iOS platform views](https://docs.flutter.dev/platform-integration/ios/platform-views) and [Android platform views](https://docs.flutter.dev/platform-integration/android/platform-views). Preserve text input, caret, selection/composition and accessibility in the native surface. Verify gesture arbitration, clipping, z-order, coordinate transforms, popovers over the view, keyboard insets, focus transfer and disposal. Choose Android composition mode based on the supported SDK/view needs and evidence rather than copying a map/video example.

Provide a style-neutral controls/controller layer plus separate Material and Cupertino compositions, using the maintained [Flutter design-system packages](https://docs.flutter.dev/ui/widgets) appropriate to the pinned SDK. Host builders can replace menus and result rows. A widget rebuild or Theme change must not reopen the document; state and theme subscriptions must stop on disposal. Native text scale and Flutter chrome scale must agree without double-scaling.

Flutter web uses the browser editor in an HTML host view with explicit JS resource/asset loading and disposal. The shared Dart-facing controls expose a platform capability record; unsupported native-only services stay unavailable. No dynamic content reimport on `build`, hidden WebView fallback, second WASM instance per control or invented native input claim is allowed.

Flutter desktop remains an explicit feasibility profile. Flutter's [architecture overview](https://docs.flutter.dev/resources/architectural-overview) currently describes limitations on desktop platform views. A desktop UI toolkit/theme package such as Fluent/macOS/GTK-style widgets does not remove that embedding constraint. Required feasibility output names each OS, actual supported embedding path or blocker, and implementation owner; unsupported profiles return typed capability errors and stay unqualified.


### Desktop feasibility decision (UFW-1.4)

Bounded documentation/API inspection on 2026-10-26 resolves all six UNC-1.4
feasibility profiles. These are **unsupported editor integrations**. Documented
upstream APIs and an existing native SDK do not establish an embedded editor,
maintained compatible package baseline or native input/accessibility qualification.
No native target was started and no new renderer is proposed.

The canonical authored responses live in
[`desktopHostDecisions`](../../core/native/ui/desktop-feasibility.ts).
`flutterDesktopCapability` and `reactNativeDesktopCapability` are actual typed
source exports under `core/adapters/native/flutter/index.ts` and
`core/adapters/native/react-native/index.ts`. They serve inspection and host/build
tooling; they are not installed Dart/Flutter plugins, RN modules or native views.
Each returns `status: unsupported`, `code: unsupported-desktop-host`,
`runtimeQualified: false`, exact prerequisite owners and changed-input conditions.
Unknown stack/OS inputs are rejected before any host activity. The earlier
`nativeUISupportMap` remains the package/profile planning authority.

| Original profile | Inspected upstream boundary | Existing local boundary and unmet owner gate | Editor status |
| --- | --- | --- | --- |
| `flutter-macos-feasibility` | [AppKitView and FlutterPlatformViewFactory](https://docs.flutter.dev/platform-integration/macos/platform-views) can contain an NSView; upstream warns incomplete support including gestures | `NativeEditorView: NSView` and async `dispose` exist; BCP-1.2/1.3 lack a pinned plugin factory/widget/lifecycle binding; BNA-1.4 owns persistence/unsaved-close integration | Unsupported; partial upstream API only |
| `flutter-windows-feasibility` | [Windows platform-view implementation issue31713](https://github.com/flutter/flutter/issues/31713) remains open at inspection; no proven native editor containment API | No declared WinUI host/command/capture/dispose surface; BDH-1.2 owns it, BCP-1.2 owns adoption after an upstream API exists | Unsupported |
| `flutter-linux-feasibility` | [Linux platform-view implementation issue41724](https://github.com/flutter/flutter/issues/41724) remains open at inspection | GTK `InputHost` exposes bootstrap with committed editing/composition/rich projection false; BCP-1.2 needs a maintained platform-view API, BDH-1.4/NLP-1.3 own host persistence/committed editing | Unsupported |
| `rn-macos-feasibility` | The inspected [macOS fork Fabric header](https://github.com/microsoft/react-native-macos/blob/9518426f653342d498b6dedc6f5ba74db0af1d40/packages/react-native/React/Fabric/Mounting/ComponentViews/View/RCTViewComponentView.h) exposes `RCTViewComponentView`, macOS branches and `RCTPlatformView *contentView` | Existing AppKit view is a containment candidate; BCP-1.4/1.5 lack pinned macOS module/codegen/component binding; BNA-1.4 owns the same host persistence/lifetime | Unsupported; candidate, no demonstrated editor embedding |
| `rn-windows-feasibility` | [RNW Native Components](https://microsoft.github.io/react-native-windows/docs/native-platform-components/) documents codegen, `ComponentView` and Composition `CreateVisual`; this does not prove arbitrary WinUI editor containment | BDH-1.2 must first deliver the native surface; BCP-1.4/1.5 must identify a compatible concrete containment/input/accessibility API and module/component binding | Unsupported; component API only |
| `rn-linux-feasibility` | The [official out-of-tree list](https://reactnative.dev/docs/out-of-tree-platforms) names community Skia on Linux, not a selected maintained GTK containment API | BCP-1.4/1.5 must identify/pin such a host; BDH-1.4/NLP-1.3 retain the incomplete GTK boundary | Unsupported; no proven path |

The concrete macOS extension work is bounded inside existing owners, without
adding roadmap tasks or declaring a proven complete input path:

1. BCP-1.2 freezes a maintained Flutter SDK exposing `AppKitView`, registers a
   `FlutterPlatformViewFactory` returning the existing `NativeEditorView`, and
   binds the canonical lifecycle/save-state API with one Session. BCP-1.3 adds
   the widget/controller with stable view identity, focus/read-only/state,
   coordinate conversion and async disposal; rebuilding never reimports content.
2. BCP-1.4 freezes a compatible macOS RN/Fabric/codegen baseline and canonical
   module lifetime API. BCP-1.5 supplies one macOS Fabric component containing
   the existing NSView through `contentView`, with layout, focus, read-only,
   target/event identity and late-callback rejection. No competing Expo view.
3. BNA-1.4 connects the same AppKit host's persistence and close recovery for
   either embedding. Denied/pending save remains explicit; no duplicate writer,
   document, history or storage protocol. BNT-1.3/1.5/1.6 and roadmap43 must
   qualify native input, accessibility, desktop lifecycle and teardown before
   either integration becomes supported. Flutter's gesture limitation stays open
   until a compatible maintained API and actual input evidence resolve it.

For Windows/Linux the precise retry conditions remain in each response:
BCP-1.2 requires a maintained documented Flutter platform-view API and compatible
pinned adoption; BCP-1.4/1.5 require a maintained RN host with concrete existing
surface containment/input/accessibility/disposal APIs. The matching BDH-1.2 or
BDH-1.4/NLP-1.3 host receipts are also required. A changed SDK version, FFI,
texture, theme kit, desktop embedder or native library alone is insufficient.
[CompositionHwndHost](https://microsoft.github.io/react-native-windows/docs/native-api/CompositionHwndHost/)
hosts RN in an HWND, the opposite containment direction, so it is not accepted
as evidence for a WinUI editor inside RN. No hidden WebView fallback or new
renderer is authorized by this decision.

`node scripts/ui-integration-delivery.mjs UFW-1.4` reads the six authored
capability responses and canonical inspection cases, checks their API citations,
original profile IDs, actual local surfaces/gaps, existing owners and source
exports, then compiles the importing TS consumer. Investigation predicates and
production compiler invocations are counted separately from zero native runtime
executions. It does not fetch mutable upstream docs, install/pin frameworks,
start a target or qualify package/native/OS support. Reinspect a source/API gate
only after its named prerequisite changes; retain these unsupported responses
until the owning implementation and qualification receipts pass.

## Acceptance ownership

The new final UI roadmaps own visual/widget/overlay/installer observations. Existing BNT-1.2 owns framework form/lifecycle behavior, BNT-1.3 native input/selection/composition, BNT-1.4 recovery/background behavior, BNT-1.5 desktop process/packaged host behavior, and BNT-1.6 teardown/overhead. Add exact Expo/Flutter profiles to those owners through the staged adoption map; reuse matching evidence rather than authoring duplicate cases here.

Roadmap 43 remains the executor/qualifier of target-runtime and assistive-technology observations under current sequencing. New UI tasks supply distinct cases and consume its returned results. Required profiles cannot be marked supported using TypeScript/Swift/Kotlin/Dart compilation, mocks or screenshots alone. Simulators/emulators/accepted OS hosts may satisfy applicable platform policy; record missing capabilities honestly.

All automated work uses deterministic documents and mocked/local backend transports. No AI credentials, paid inference, automatic provider recording, paid cloud builds, deployment or publication. Each task records exact source/runtime/selector and nonzero executed/passed/failed/skipped counts in ignored progress. Focused delivery checks do not imply final qualification.
