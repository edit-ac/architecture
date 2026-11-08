# Editor UI and native integration delivery plan

Status: PLANNED. User scope: 2026-10-24. 31 focused roadmap files, 165 parent tasks. This controller index is not a worker queue entry. No active runner, backend/framework source, runtime configuration or existing progress is changed by creating this plan.

[Web product/API contract](../../specs/editor-ui-integrations.md) · [Native/Expo/Flutter contract](../../specs/native-ui-integrations.md) · [Staged ownership map](adoption-map.md) · [Machine-readable queue/requirements](manifest.json)

## Intended outcome

A styled default editor with replaceable controls and content/chrome themes; optional React/Vue/Svelte UI packages; first-class Base UI/React Aria/Radix/Reka/Bits adapters; source-owned shadcn kits; a Laravel/shadcn frontend and native Filament field; platform-native controls; and required React Native/Expo and Flutter mobile/web integrations over the existing engine and backend owners.

Expo uses custom development builds, not stock Expo Go. Native RN/Flutter use existing native surfaces, not WebViews. Expo web and Flutter web are explicit browser profiles. Desktop RN/Flutter embedding is a required bounded feasibility decision with no automatic parity claim.

## Queue and entry order

Packaging follow-up, 2026-10-26: [dedicated integration repositories/packages and registry listings](../../specs/integration-distribution.md) apply to framework, component-library, native and source-kit integrations. Preserve current feature ownership and progress; reconcile UPG-1.1–1.3 packaging handoffs and emit bounded extraction sources at a safe checkpoint. Dedicated Next/Nuxt/SvelteKit packages remain thin compositions. This index amendment does not change a running source snapshot or authorize publication.

This is a proposed serial topological order for future safe adoption, not a start/enqueue instruction. Use only the existing guarded root coordinator and preserve current global sequencing. A blocked queue file holds later files; the coordinator may select another independent ready subset at a safe checkpoint, never silently skip requirements or restart unchanged failures. No native/backend/release-wide gate blocks independent web styling.

Read one source file plus its named contract section and prerequisite receipt. Keep each parent within 15–45 minutes including focused checks; split oversized missing APIs before work. Paths below are architecture-relative; distinct progress paths are ignored. All final case/test development is in 26–29 after functionality.

Source budget: at most 24 KiB and ten parents per file. Most sources are smaller; the final web file groups nine related UI case families under one shared evidence policy, and the Expo file keeps eight closely related packaging/profile boundaries together. Split either before expansion exceeds this budget.

| Order/source | Outcome | Parents | Separate progress |
| --- | --- | --- | --- |
| 00 [00-contracts.md](00-contracts.md) | Freeze shared UI contracts and ownership | 6 | `.roadmap-runner/editor-ui-integrations-20261024/00-contracts.progress.md` |
| 01 [01-default-styles.md](01-default-styles.md) | Style current product surfaces | 5 | `.roadmap-runner/editor-ui-integrations-20261024/01-default-styles.progress.md` |
| 02 [02-controls-state.md](02-controls-state.md) | Implement reusable controls and suggestion state | 6 | `.roadmap-runner/editor-ui-integrations-20261024/02-controls-state.progress.md` |
| 03 [03-default-dom-controls.md](03-default-dom-controls.md) | Deliver accessible default DOM controls | 9 | `.roadmap-runner/editor-ui-integrations-20261024/03-default-dom-controls.progress.md` |
| 03b [03b-table-controls.md](03b-table-controls.md) | Refine contextual table controls | 3 | `.roadmap-runner/editor-ui-integrations-20261024/03b-table-controls.progress.md` |
| 04 [04-react-ui.md](04-react-ui.md) | Deliver React controls composition | 4 | `.roadmap-runner/editor-ui-integrations-20261024/04-react-ui.progress.md` |
| 05 [05-vue-ui.md](05-vue-ui.md) | Deliver Vue controls composition | 4 | `.roadmap-runner/editor-ui-integrations-20261024/05-vue-ui.progress.md` |
| 06 [06-svelte-ui.md](06-svelte-ui.md) | Deliver Svelte controls composition | 4 | `.roadmap-runner/editor-ui-integrations-20261024/06-svelte-ui.progress.md` |
| 07 [07-base-ui.md](07-base-ui.md) | Integrate Base UI controls | 5 | `.roadmap-runner/editor-ui-integrations-20261024/07-base-ui.progress.md` |
| 08 [08-react-aria.md](08-react-aria.md) | Integrate React Aria controls | 5 | `.roadmap-runner/editor-ui-integrations-20261024/08-react-aria.progress.md` |
| 09 [09-radix.md](09-radix.md) | Integrate Radix controls | 5 | `.roadmap-runner/editor-ui-integrations-20261024/09-radix.progress.md` |
| 10 [10-reka.md](10-reka.md) | Integrate Reka controls | 5 | `.roadmap-runner/editor-ui-integrations-20261024/10-reka.progress.md` |
| 11 [11-bits.md](11-bits.md) | Integrate Bits controls | 5 | `.roadmap-runner/editor-ui-integrations-20261024/11-bits.progress.md` |
| 12 [12-shadcn-react.md](12-shadcn-react.md) | Deliver React shadcn source kits | 6 | `.roadmap-runner/editor-ui-integrations-20261024/12-shadcn-react.progress.md` |
| 13 [13-shadcn-vue-svelte.md](13-shadcn-vue-svelte.md) | Deliver Vue and Svelte shadcn source kits | 6 | `.roadmap-runner/editor-ui-integrations-20261024/13-shadcn-vue-svelte.progress.md` |
| 14 [14-web-host-integrations.md](14-web-host-integrations.md) | Integrate existing host and Laravel plans | 6 | `.roadmap-runner/editor-ui-integrations-20261024/14-web-host-integrations.progress.md` |
| 15 [15-native-ui-contracts.md](15-native-ui-contracts.md) | Map shared controls to native hosts | 4 | `.roadmap-runner/editor-ui-integrations-20261024/15-native-ui-contracts.progress.md` |
| 16 [16-apple-mobile-ui.md](16-apple-mobile-ui.md) | Deliver UIKit and SwiftUI controls | 5 | `.roadmap-runner/editor-ui-integrations-20261024/16-apple-mobile-ui.progress.md` |
| 17 [17-macos-ui.md](17-macos-ui.md) | Deliver AppKit and SwiftUI desktop controls | 4 | `.roadmap-runner/editor-ui-integrations-20261024/17-macos-ui.progress.md` |
| 18 [18-android-ui.md](18-android-ui.md) | Deliver Android Views and Compose controls | 5 | `.roadmap-runner/editor-ui-integrations-20261024/18-android-ui.progress.md` |
| 19 [19-windows-ui.md](19-windows-ui.md) | Deliver WinUI and WPF controls | 4 | `.roadmap-runner/editor-ui-integrations-20261024/19-windows-ui.progress.md` |
| 20 [20-linux-desktop-ui.md](20-linux-desktop-ui.md) | Deliver GTK and desktop web UI composition | 4 | `.roadmap-runner/editor-ui-integrations-20261024/20-linux-desktop-ui.progress.md` |
| 21 [21-react-native-ui.md](21-react-native-ui.md) | Deliver React Native controls and design-system kits | 6 | `.roadmap-runner/editor-ui-integrations-20261024/21-react-native-ui.progress.md` |
| 22 [22-expo-integration.md](22-expo-integration.md) | Deliver first-class Expo integration | 8 | `.roadmap-runner/editor-ui-integrations-20261024/22-expo-integration.progress.md` |
| 23 [23-flutter-mobile-ui.md](23-flutter-mobile-ui.md) | Deliver Flutter mobile controls and themes | 7 | `.roadmap-runner/editor-ui-integrations-20261024/23-flutter-mobile-ui.progress.md` |
| 24 [24-flutter-web-and-desktop-profiles.md](24-flutter-web-and-desktop-profiles.md) | Deliver Flutter web and bound desktop embedding claims | 4 | `.roadmap-runner/editor-ui-integrations-20261024/24-flutter-web-and-desktop-profiles.progress.md` |
| 25 [25-packages-and-guides.md](25-packages-and-guides.md) | Prepare installable UI packages and integration guides | 5 | `.roadmap-runner/editor-ui-integrations-20261024/25-packages-and-guides.progress.md` |
| 26 [26-final-web-ui-testing.md](26-final-web-ui-testing.md) | Complete web UI coverage after functional delivery | 9 | `.roadmap-runner/editor-ui-integrations-20261024/26-final-web-ui-testing.progress.md` |
| 27 [27-final-native-ui-testing.md](27-final-native-ui-testing.md) | Complete native toolkit UI coverage | 6 | `.roadmap-runner/editor-ui-integrations-20261024/27-final-native-ui-testing.progress.md` |
| 28 [28-final-expo-flutter-testing.md](28-final-expo-flutter-testing.md) | Complete Expo and Flutter UI/package coverage | 6 | `.roadmap-runner/editor-ui-integrations-20261024/28-final-expo-flutter-testing.progress.md` |
| 29 [29-final-support-handoff.md](29-final-support-handoff.md) | Close UI support and adoption gates | 4 | `.roadmap-runner/editor-ui-integrations-20261024/29-final-support-handoff.progress.md` |

## Dependency and ownership rules

Local `Dependencies:` refer only to parents in the same file. `Entry receipts:` identify exact earlier-file or existing-backend parent IDs, not whole roadmap completion. Verify interface/source/runtime compatibility before use. Where an entry is a candidate feasibility receipt, it never blocks an unrelated required platform. Missing native views/modules go back to BNA/BDH/BCP; missing framework lifecycle goes to BWF; PHP/Laravel/Filament persistence remains BPH/BFA. The [adoption map](adoption-map.md) specifies every handoff without editing their current source.

UIC freezes current names and the surface matrix before implementations. UCS is shared browser interaction state; UNC is the native data/ownership mapping and does not import the browser runtime. Framework/library widgets own their own keyboard behavior. UI observes one semantic authority and one save/receipt authority.

Progress must include exact source/API revision, command/runtime/exit and nonzero executed/passed/failed/skipped or inspected-case counts. Before UIC-1.5, contract checks are direct inspection/compilation. After it, `node scripts/ui-integration-delivery.mjs ID` is the planned bounded selector entry; it is not a claim the script already exists. Unknown/missing selectors and zero cases fail. Reuse unchanged evidence; new sessions and milestones do not justify repeated broad suites.

## Requirement coverage and final ownership

User correction, 2026-10-25: [proper table paste and direct cell editing](../../specs/table-paste-and-editing.md) adds UDM-1.8/1.9 and final TPT-01–08 acceptance at UTW-1.2. These are pending UI source amendments; the active editing worker, queue paths/order and progress are unchanged. Earlier semantic/textarea presenter passes do not qualify the new product UI.

| Requirement | Outcome | New final UI owner | Existing evidence owners |
| --- | --- | --- | --- |
| UI-TABLE-PASTE | Normal pasted tables, direct cell editing and no repeated textbox chrome | [UTW-1.2](26-final-web-ui-testing.md) | Existing table/clipboard/history owners; exact compatible proof only |
| UI-CONTRACT | Shared descriptors, guarded targets, contributions, suggestions and customization | [UTW-1.3](26-final-web-ui-testing.md) | Existing semantic/presenter authority where applicable |
| UI-DEFAULT | Default styles, content/chrome separation and DOM product controls | [UTW-1.2](26-final-web-ui-testing.md) | Existing semantic/presenter authority where applicable |
| UI-DEFAULT-A11Y | Default toolbar/menu/dialog and inline-suggestion accessibility | [UTW-1.9](26-final-web-ui-testing.md) | Existing semantic/presenter authority where applicable |
| UI-FRAMEWORK | React/Vue/Svelte typed controls and optional imports | [UTW-1.8](26-final-web-ui-testing.md) | BNT-1.2 |
| UI-BASE | First-class Base UI surfaces | [UTW-1.4](26-final-web-ui-testing.md) | Existing semantic/presenter authority where applicable |
| UI-ARIA | First-class React Aria surfaces and correct collection semantics | [UTW-1.4](26-final-web-ui-testing.md) | Existing semantic/presenter authority where applicable |
| UI-RADIX | First-class Radix surfaces | [UTW-1.5](26-final-web-ui-testing.md) | Existing semantic/presenter authority where applicable |
| UI-REKA | First-class Vue/Reka surfaces | [UTW-1.5](26-final-web-ui-testing.md) | Existing semantic/presenter authority where applicable |
| UI-BITS | First-class Svelte/Bits surfaces | [UTW-1.5](26-final-web-ui-testing.md) | Existing semantic/presenter authority where applicable |
| UI-SHADCN | React Base UI/Radix, Vue and Svelte source registries | [UTW-1.6](26-final-web-ui-testing.md) | Existing semantic/presenter authority where applicable |
| UI-HOST | Astro, SSR framework recipes, Laravel/shadcn, Filament, Angular and secondary-library recipes | [UTW-1.7](26-final-web-ui-testing.md) | BNT-1.2 |
| NATIVE-CONTRACT | One native UI data/target/theme ownership map | [UTN-1.1](27-final-native-ui-testing.md) | BNT-1.3 |
| NATIVE-IOS | UIKit/SwiftUI mobile controls and accessibility preferences | [UTN-1.2](27-final-native-ui-testing.md) | BNT-1.3 |
| NATIVE-MAC | AppKit/SwiftUI toolbar/menu and window ownership | [UTN-1.3](27-final-native-ui-testing.md) | BNT-1.3 |
| NATIVE-ANDROID | Views/Compose controls and theme/geometry | [UTN-1.4](27-final-native-ui-testing.md) | BNT-1.3 |
| NATIVE-WINDOWS | WinUI/WPF controls and high contrast | [UTN-1.5](27-final-native-ui-testing.md) | BNT-1.3, BNT-1.5 |
| NATIVE-LINUX | GTK/libadwaita and desktop web-host UI | [UTN-1.6](27-final-native-ui-testing.md) | BNT-1.5 |
| RN-UI | Native controls, Paper and Reusables source kits | [UTX-1.2](28-final-expo-flutter-testing.md) | BNT-1.3 |
| EXPO-INSTALL | Expo CNG/native-module/development-build support | [UTX-1.3](28-final-expo-flutter-testing.md) | BNT-1.3 |
| EXPO-PROFILES | Expo Router, runtime policy, Expo UI and explicit web profile | [UTX-1.4](28-final-expo-flutter-testing.md) | BNT-1.2, BNT-1.4 |
| FLUTTER-MOBILE | Flutter Material/Cupertino UI and native platform views | [UTX-1.5](28-final-expo-flutter-testing.md) | BNT-1.3, BNT-1.4, BNT-1.6 |
| FLUTTER-WEB-DESKTOP | Flutter web and explicit RN/Flutter desktop feasibility | [UTX-1.6](28-final-expo-flutter-testing.md) | BNT-1.5 |
| PACKAGES-GUIDES | Installable exports/support manifest and accurate ecosystem guides | [UTH-1.3](29-final-support-handoff.md) | BNT-1.6 |

Each new final owner covers UI-specific cases only; existing BNT tests retain lifecycle/input/recovery/overhead ownership and roadmap43 owns target-runtime/AT observations. UTH closes support claims only with all required functional and final receipts. Required profiles stay incomplete on failures/skips; a mock transcript, build or screenshot cannot qualify native input/accessibility.

## Boundaries and verification

No paid inference, provider recording, loaded credentials, paid cloud builds, deployment or publication. One canonical document format and one engine/command/history owner remain mandatory. Generated artifacts remain ignored; authored specs, deterministic inputs and case definitions may be tracked. Native toolchains must be provisioned separately; a UI task cannot hide environment installation in its check budget. Existing hard caps remain final gates with the bounded optimization policy.

Run the source-only structural check from `architecture`:

```sh
node scripts/validate-editor-ui-roadmaps.mjs
```

It checks unique standalone IDs, fields, local/earlier/external dependencies, cycles/order, progress separation, requirement/final ownership, named local links and source size. It does not start the runner or validate implementation. Existing 43-track manifest and all current queues remain unchanged.

## Notion table follow-up — 2026-11-08

The [new source](03b-table-controls.md) adds three planning-only parents after the default DOM controls, preserving completed direct-cell/paste delivery. Its width parent consumes the new RCH-1.34 receipt; the reserved semantic progress destination is not active configuration. Final UTW-1.2 consumes these new functional receipts and NTC cases. No active queue, immutable snapshot, coordinator or progress is changed; adopt through the existing guarded source-refresh process.
