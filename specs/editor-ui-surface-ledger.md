# UI surface and package ownership ledger

UIC-1.1 freezes the ownership boundary below against the current authored source. This is an internal implementation inventory, not a support, publication, accessibility or runtime qualification claim. The [shared customization contract](editor-ui-integrations.md#shared-customization-apis) owns the required behavior; [native scope](native-ui-integrations.md#scope-and-authority) owns native handoffs. Paths below are core-relative unless stated otherwise. The separate UIC-1.1 progress receipt records consumed revisions and inspection counts.

`Existing` means an authored export or rendered surface exists. `Planned` means a required addition has an owner but is not an importable API. `Unsupported` means no implementation/support claim follows from this inventory. Every action still needs its existing readiness, readonly, extension, permission, composition and captured-target checks at execution. Rendering a button, finding a manifest key or importing a descriptor never enables a feature.

## Existing manifest exports

Each row is one actual package export key. All six packages are private at version `0.0.0`; names below do not authorize publication. Targets are manifest paths, not claims that a generated `dist` file is present. UI adapters consume these boundaries instead of deep-importing private files.

| Package | Export key | Existing target | Owner / dependency boundary |
| --- | --- | --- | --- |
| @edit-ac/core | . | dist/index.js | Engine loading and semantic types; SDK/core owner; no UI peer |
| @edit-ac/core | ./wasm | dist/wasm/editac_wasm_bg.wasm | Current engine asset; same owner |
| @edit-ac/core | ./fixture | dist/fixture.js | Explicit fixture tooling; not a second production engine |
| @edit-ac/core | ./fixture/wasm | dist/wasm-fixture/editac_wasm_bg.wasm | Fixture-only asset |
| @edit-ac/core | ./extensions | dist/extensions/index.js | Existing extension contract; track 21 |
| @edit-ac/core | ./links | dist/links/index.js | Existing link contract |
| @edit-ac/web | . | dist/index.js | Browser SDK and existing UI exports; SDK track 08; core dependency only |
| @edit-ac/web | ./editor | dist/editor.js | Existing BrowserEditor entry |
| @edit-ac/web | ./controls | dist/ui/controls.js | UCS-1.6 current ESM/types controls barrel; same root identities, no framework/CSS/engine initialization |
| @edit-ac/web | ./host | dist/host/index.js | Existing host-agent adapter; no UI semantic authority |
| @edit-ac/web | ./styles.css | styles/editor.css | Existing opt-in CSS; UIS extends appearance |
| @edit-ac/web | ./structure.css | styles/structure.css | UIS-1.1 opt-in command/slash layout without decorative CSS |
| @edit-ac/web | ./ui.css | styles/ui.css | UIS-1.2 opt-in scoped default chrome/theme/state styles; no headless CSS import |
| @edit-ac/web | ./highlight-worker | dist/modules/code/worker-entry.js | Optional code worker |
| @edit-ac/web | ./math | dist/modules/math.js | Optional math presenter |
| @edit-ac/web | ./modules | dist/modules/index.js | Existing optional module/presenter exports |
| @edit-ac/web | ./links | dist/modules/links/index.js | Browser link integration |
| @edit-ac/web | ./ai | dist/extensions/ai/actions.js | Optional host-backed writing UI; no provider credentials |
| @edit-ac/web | ./ai/completion | dist/extensions/ai/completion.js | Optional host-backed completion UI |
| @edit-ac/web | ./highlighting | dist/extensions/highlighting.js | Managed optional highlighting |
| @edit-ac/web | ./formats | dist/modules/formats.js | Optional format controls; converter boundary remains separate |
| @edit-ac/web | ./assets | dist/sync/assets.js | Existing asset transport/receipt boundary |
| @edit-ac/react | . | dist/index.js | BWF-1.1 lifecycle binding; web dependency; React `19.3.x` peer |
| @edit-ac/astro | . | dist/index.js | BWF-1.1 host lifecycle; web dependency; Astro `7.3.x` peer |
| @edit-ac/astro | ./Editor.astro | src/Editor.astro | Same host owner; framework component input |
| @edit-ac/markdown | . | dist/index.js | Optional stateless codec; core/web dependencies |
| @edit-ac/markdown | ./wasm | dist/wasm/editac_markdown_wasm_bg.wasm | Optional Markdown codec asset |
| @edit-ac/markdown | ./web | dist/web.js | Existing web codec attachment |
| @edit-ac/formats | . | dist/index.js | Optional document converter; core `0.0.0` peer |
| @edit-ac/formats | ./worker | dist/worker.js | Optional converter worker |
| @edit-ac/formats | ./capabilities | capabilities.json | Converter capability data; not automatic action admission |

The web manifest marks its code worker, vendor modules and `**/*.css` as side effects. CSS and optional workers remain explicit dependencies. None of these manifests exports `/controls`, `/ui` or `/ui.css`. React and Astro roots are lifecycle bindings, not complete toolbars. Additional exports must preserve existing entries and the single core/web asset graph.

## Existing consumer and semantic seams

These names are already exported. Proposed state, slot and contribution names must extend these owners; this ledger introduces no second registry or content model.

| Public entry / symbol | Source authority | Present behavior and missing work owner |
| --- | --- | --- |
| web root: `CommandControls` | src/ui/commands.ts | Optional DOM controls, search, captured command/paste targets, cancellation and disposal. Hard-coded labels/layout; UIS/UDM own presentation changes. This is not a DOM-free descriptor API. |
| web root: `commandCatalog`, `resolveCommand`, `PortableCommand`, `ShortcutProfile`, `CapturedCommand` | src/commands/catalog.ts | 24 existing IDs/aliases/shortcuts; captured target has active/execute/dispose. UIC-1.2/UCS extend projection; UIC-1.3 extends contribution/target interfaces. |
| web root: `projectCommandView`, `CommandPressed`, `CommandValue`, `CommandPermission`, `CommandObservation`, `CommandViewInput`, `CommandViewState`, `CommandViewSnapshot`, `CommandViewSelector`, `CommandViewEquality`, `CommandView`; `createCommandView`, `CommandViewOwner`, `CommandObservationSource` | src/commands/view.ts; src/ui/command-view.ts | UIC-1.2 pure immutable projection over existing catalog/owner observations and typed subscription contract. UCS-1.1 implements per-editor lifecycle/explicit observation-source subscriptions and selector equality/disposal; it never captures or executes targets. UCS-1.6 owns the `/controls` subpath. |
| web root: `prepareUIContributions`, `UIContributionError`, target/contribution/suggestion types | src/commands/target-session.ts; src/extensions/ui-contributions.ts; src/ui/suggestions.ts | UIC-1.3 public declarations and pure metadata admission over existing catalog/slash references. UCS-1.2 adds UITargetRequest and live revocable sessions through BrowserEditor.captureUITarget; UCS-1.3 adds the layout/activation row below; UCS-1.4 adds createUISuggestions with UISuggestionSource/UISuggestionOptions: bounded prepared query state, current registration/policy observations, abort generation and existing guarded contribution activation; reference-atom options retain their separate owner. |
| web root: `resolveUILayout`, `activateUIContribution`, layout/presentation/surface model types | src/ui/layout.ts; src/ui/contribution-action.ts | UCS-1.3 immutable host filtering/group/order/localization over admitted metadata; delegates to matching captured command or already-open owning slash presenter. No optional feature loading, semantic registration or widget mounting. `/controls` remains UCS-1.6. |
| web root: `UI_THEME_TOKENS`, `UI_PARTS`, theme/context/slot types | src/ui/theme.ts; contracts/ui-theme.schema.json | UIC-1.4 token/part naming and bounded native data declarations. UCS/UDM/UIS and existing native bridges retain live theme/overlay application; no new CSS or package subpath. |
| web root: `mountUIOverlay`, overlay lifecycle/options/position types | src/ui/overlay.ts; src/ui/elements.ts; src/platform/viewport.ts | UCS-1.5 explicit target-owned wrapper, initiating dialog containment, resolved theme/direction/locale inheritance, frozen client geometry hook and revocation/unmount. Existing viewport floats only the active owner's controls within dialog bounds. Widget keys and collision/transform policy remain presenter/host-owned; no focus restoration or CSS import. |
| `BrowserEditor.editorId`, `captureUITarget` | src/editor.ts; src/ui/target-session.ts | UCS-1.2 per-editor session over guarded command/formatting/history targets, explicit overlay focus, revocable callbacks and abort/disposal. No current-caret fallback or semantic registry. |
| `BrowserEditor.captureCommand`, `captureHistory`, `captureToolbar`, `capturePlainPaste`, `capturePaste` | src/editor.ts; src/input/keyboard.ts | Existing guarded execution routes. UIC-1.3/UCS reuse these; no fallback to the current caret on stale execution. |
| web root: `ToolbarTarget`, `MarkState`, `FormattingChanges` | src/commands/formatting.ts | Existing applicable/state/format/apply/clear/dispose over retained selection. Mixed state is not a complete subscribed command snapshot. |
| `BrowserEditor.state`, `subscribe` and web root `EditorState` | src/editor.ts; src/lifecycle.ts | Lifecycle and scoped patch subscriptions. Lifecycle getter currently copies state; it does not promise referentially stable command snapshots. UIC-1.2 owns that contract; UCS owns selectors. |
| web root/modules: `ModuleRegistry`, `ModuleRuntime` | src/modules/registry.ts; src/modules/runtime.ts | Existing registration and presenter lifecycle, not a new UI contribution registry. Track 21 retains semantic registration. |
| web root/modules: `slashCommands`, `SlashPresenter`, `referenceSuggestions`, `ReferencePresenter` | src/modules/slash.ts; src/modules/references.ts | Existing command/suggestion sessions. UIC-1.3/UCS own portable presentation metadata and cancellation projection. |
| web root: `reorderControls`, `contentModules`, `documentSearch`, `codeCommands`, `assistiveInput` | src/modules/; src/extensions/code.ts | Existing optional presenters; UI styling does not create their underlying semantic capabilities. |
| web root: `ChangeReview`, `HistoryReview`; modules: rich presenters | src/review/; src/modules/ | Existing review/history and rich-content boundaries retain their safety and permission checks. |
| web formats: `formatControls`, `FormatControls` | src/modules/formats.ts | Existing optional import/export UI; capability profile plus host authority gates each action. |
| web assets: `assetInputControls`, `AssetInputControls` | src/modules/asset-input.ts; src/sync/assets.ts | Existing asset picker/host/receipt path through `EditorSurface.enableAssetInputControls`. UI never creates a parallel uploader or embeds credentials. |
| web ai: `aiActions`, `AiActions`; ai/completion: `aiCompletion`, `AiCompletion` | src/extensions/ai/ | Optional explicit host transport. Inventory only; no inference is authorized by inspecting or rendering it. |
| React root: `useEditor`, `useEditorState`, `EditorHost` | packages/react/src/index.ts | Lifecycle/external-store host. URC adds command selectors/components; BWF-1.1 retains mount/teardown ownership. |
| Astro root: `mountEditorHost`, `defineEditorHost`, `installEditorHosts`; `/Editor.astro` | packages/astro/src/ | Non-React host lifecycle/navigation. UWH-1.1 composes default controls; BWF-1.1 retains lifecycle ownership. |

## Rendered control and status inventory

Rows enumerate concrete source-controlled controls or repeated control families. A family row lists every fixed member; data-driven rows describe the bounded collection instead of inventing a fixed number of DOM nodes. Status rows include the surface's messages, errors, unavailable/empty states and previews. Static content wrappers, style elements, parsing templates and detached clipboard serialization are accounted for below separately. Host examples can mount these surfaces but do not create new SDK exports.

| Row | Existing controls or status | Source authority | Gate / presentation owner |
| --- | --- | --- | --- |
| S01 | Editor root label, readonly/ready/input authority | src/editor.ts | Lifecycle owner; UDM frame composition |
| S02 | Local loading, waiting for configured collaboration, ready, save failure and read-only recovery alert | src/editor.ts | Real Session/storage owner; UDM status must not invent durable-save receipts |
| S03 | Optional standalone Paste without formatting button and rejection message | src/editor.ts | Existing paste guard; UDM |
| S04 | Search commands button and Search editing commands input | src/ui/commands.ts | Host-mounted CommandControls; UIS/UDM |
| S05 | Insert paragraph, Insert line break, Undo, Redo, Indent, Outdent buttons | src/ui/commands.ts | Existing catalog/keyboard commands; UDM |
| S06 | Bold, Italic, Underline, Edit link, Strikethrough, Inline code buttons | src/ui/commands.ts | Formatting configuration and captured commands; UDM |
| S07 | Text paragraph, Heading 1–6, Bullet list, Numbered list buttons | src/ui/commands.ts | Existing catalog; UDM block selector replaces presentation only |
| S08 | Paste with formatting, Paste without formatting, Cancel paste buttons | src/ui/commands.ts | Existing clipboard targets; UDM |
| S09 | Select-text prompt, reading clipboard, formatted/plain paste success, tap-to-continue, command/clipboard unavailable, canceled and pending aria-busy status | src/ui/commands.ts | Existing command result/generation guard; UCS/UDM |
| S10 | Preparing paste / Applying paste live status and temporary Cancel paste button | src/clipboard/pending.ts | Existing job lifetime; UDM overlay owner must include body-mounted status |
| S11 | Keyboard help text and focus exit sentinel | src/input/keyboard.ts; src/input/focus.ts | Existing input policy; UDM must preserve native navigation |
| S12 | Edit link dialog, Link URL input, Apply link and Cancel link buttons | src/input/keyboard.ts | Captured formatting target; UDM dialog composition |
| S13 | Link rejection status | src/input/keyboard.ts | Command result, bounded display; UDM |
| S14 | Find in document, Find in selection, Find text and Replacement text fields | src/modules/search.ts | Existing DocumentSearchSession; UDM |
| S15 | Previous match, Next match, Replace current, Replace all, Close find | src/modules/search.ts | Scoped target and existing semantic replace; UDM |
| S16 | Match count/wrapped, search unavailable, bounded search and replacement rejection status; highlight styling | src/modules/search.ts | Existing search owner; UIS/UDM |
| S17 | Slash commands launcher, command-ID menuitem buttons, Close commands | src/modules/slash.ts | Configured existing commands; UDM suggestion composition |
| S18 | Result count/active label, disabled reason title, unavailable/failure with retained query | src/modules/slash.ts | Existing session and command admission; UCS/UDM |
| S19 | Insert reference, Search references input, dynamic result menuitems, Close references | src/modules/references.ts | Existing resolver and captured target; UDM |
| S20 | Searching, count/empty, query limit, failed/unavailable insertion and retained source status | src/modules/references.ts | Request cancellation and current admission; UCS/UDM |
| S21 | Move block up, Move block down, Drag selected block controls | src/modules/reorder.ts | Existing block move/copy semantics; UDM |
| S22 | Move destination, moved, boundary, unavailable and canceled/changed-target status | src/modules/reorder.ts | Existing guarded move; UIS/UDM |
| S23 | Seven code controls: Move code lines up/down, Duplicate code lines, Indent/Outdent code lines, Surround code selection, Toggle code comments | src/extensions/code.ts | Existing prepared code semantics; UDM |
| S24 | Code select-first, applied, boundary/unchanged and unavailable/error status | src/extensions/code.ts | Same code owner; UIS/UDM |
| S25 | Table structure: Insert row before/after, Remove rows, Insert column before/after, Remove columns | src/modules/tables/current.ts | Existing table semantics; UDM-1.8/1.9 |
| S26 | Table formatting: Table cell link input; Bold, Italic, Underline, Strike, Code, Link cells and Remove cell link buttons | src/modules/tables/current.ts | Existing prepared table commands; UDM-1.8/1.9 |
| S27 | Table styles: Paragraph cells, Heading 1–6 cells, Code block cells | src/modules/tables/current.ts | Same semantic owner; UDM-1.8/1.9 |
| S28 | Header cells, Body cells, Align cells none/left/center/right | src/modules/tables/current.ts | Same semantic owner; UDM-1.8/1.9 |
| S29 | Paste cells as literal text checkbox; Extend table selection toggle; per-cell Select row/column buttons | src/modules/tables/current.ts | Existing cell-range owner; UDM-1.8/1.9 |
| S30 | Per-cell textarea plus rich preview, grid, navigation help, retained-data diagnostics | src/modules/tables/current.ts | Existing scaffolding is a known product defect, not direct rich cell editing; UDM-1.8/1.9 and UIS-1.4 |
| S31 | Table updated/rejected, selection limits/dimensions, copy/paste and retained-data status | src/modules/tables/current.ts | Existing command/clipboard results; UTW-1.2 retains final TPT proof |
| S32 | Unsupported table source readonly textarea and preserved-data status | src/modules/content.ts | Existing safe fallback; UDM/UIS |
| S33 | Add file, optional Take photo, matching hidden file inputs, Cancel adding asset | src/modules/asset-input.ts | Existing describe/host/receipt path, optional capture; UDM |
| S34 | Choose/waiting for file, adding asset, local asset added with distinct asset/document receipts, canceled and error status | src/modules/asset-input.ts | Existing host availability and asset session; UDM |
| S35 | Load image, Cancel image load, Image source readonly textarea, image/alt/caption fallback | src/modules/images/presenter.ts | Existing image asset authorization; UIS |
| S36 | Image loading/ready/unavailable/canceled state, source preserved | src/modules/images/presenter.ts | Existing presenter; UIS |
| S37 | Open file, Download file, Select source to copy, Cancel file action; Attachment source readonly textarea | src/modules/attachments/presenter.ts | Existing file action authorization; UIS |
| S38 | Attachment filename/detail/fallback and file state/source-copy status | src/modules/attachments/presenter.ts | Binary data remains outside source/clipboard; UIS |
| S39 | Refresh card, Activate embed, Deactivate embed, Embed source readonly textarea | src/modules/embeds/presenter.ts | Existing link policy and explicit sandbox activation; UIS |
| S40 | Embed title/URL/description, fallback and state; optional sandboxed iframe | src/modules/embeds/presenter.ts | Same existing presenter; UIS |
| S41 | Math source, preview and loading/unavailable/rendered status | src/modules/math.ts; src/modules/math-renderer.ts | Existing optional renderer; UIS |
| S42 | Code highlighting colors and plain-code fallback | src/modules/code/presenter.ts | No new semantic controls; UIS |
| S43 | Link metadata title/icon and loading/status/fallback | src/modules/links/enrichment.ts | Existing request/permission boundary; UIS |
| S44 | Refresh reference, Open reference; private reference label/title/preview/icon | src/modules/references/display.ts | Existing private display policy; UIS |
| S45 | Reference refreshing, available/unavailable, locked/unsupported/canceled/expired status | src/modules/references/display.ts | Missing/forbidden remain non-disclosing; UIS |
| S46 | File and sharing launcher, Import format and Export format selectors | src/modules/formats.ts | Baseline text, optional Markdown, installed admitted profiles only; UDM |
| S47 | Show installed format profiles; metadata catalog, unavailable profiles and system/share/clipboard alternatives | src/modules/formats.ts | Metadata load does not start conversion; UDM |
| S48 | Table file line endings LF/CRLF, first row header checkbox, approve reported loss checkbox, table selector | src/modules/formats.ts | Explicit dialect/loss/table selection; UDM |
| S49 | Import file fallback input, Use system file picker, Confirm import, Download original file, Import source preview readonly textarea | src/modules/formats.ts | Existing preparation and guarded confirm; UDM |
| S50 | Output filename, Prepare export, Prepared export text readonly textarea | src/modules/formats.ts | Existing converter/target authority; UDM |
| S51 | Save file, Download file, Share file, Copy output, Select output for manual copy, Cancel preparation, Close file and sharing | src/modules/formats.ts | Explicit host/browser capability and cancellation; UDM |
| S52 | File preparation, profile loading, loss/unsupported/error/cancel/recovery status | src/modules/formats.ts | No PDF import or implicit conversion; UDM |
| S53 | Editing assistance launcher, Search assistance commands, configured catalog command buttons (default bold/italic/undo/redo) | src/modules/assistive-input.ts | Existing registration validates commands; UDM |
| S54 | Optional Start assistance, Stop assistance; Cancel assistance, Recover assistance, Close assistance | src/modules/assistive-input.ts | Explicit host capabilities; UDM |
| S55 | Command disabled reasons, host/transport privacy/availability, live status and uncommitted/recovery preview | src/modules/assistive-input.ts | Existing host session, no provider calls in inventory; UDM |
| S56 | Ask AI, Fill text, Continue writing, Ask AI about selection, Rewrite selection launchers | src/extensions/ai/actions.ts | Optional host-owned AiActions; UDM |
| S57 | Writing action, Target language, Requested tone, Instruction, Context scope, Proposal target fields | src/extensions/ai/actions.ts | Existing bounded explicit context/target; UDM |
| S58 | Generate, Stop, Reject, Accept, Regenerate, Close | src/extensions/ai/actions.ts | Existing proposal/session gates; UDM |
| S59 | AI answer/proposed plain text, request/review/error/availability status | src/extensions/ai/actions.ts | Transport configured by host, rendering is not authorization; UDM |
| S60 | Suggest writing, Accept completion, Dismiss completion; ghost preview and live suggestion/disabled/host unavailable status | src/extensions/ai/completion.ts | Existing explicit completion session and captured target; UDM |
| S61 | Review unified/inline/side-by-side toggles, Show whitespace, Previous page, Next page | src/review/view.ts | Existing bounded view model; UIS |
| S62 | Per-source-hunk checkboxes, Accept selected hunks; selected count, readonly/attribution/hash/page/empty/value-limit explanations | src/review/view.ts | Writable mode plus host revalidation; UIS |
| S63 | Inspect revision buttons, Previous revisions, Next revisions; readonly historical details | src/review/history.ts | Existing history access/retention owner; UIS |
| S64 | Preview restore as new edit, Apply restore as new edit; preview/conflict/unchanged/restored/unavailable status | src/review/history.ts | Existing restorer and current revision validation; UIS |
| S65 | Checked/Unchecked noninteractive task marker, separator, semantic blocks/links and extension inline labels/decorations | src/dom/render.ts | Existing DOM projection; never replace with framework editable children; UIS |
| S66 | Unsupported extension source readonly textarea and codec-unavailable/preserved-data status | src/modules/transfer.ts | Existing lossless fallback; UIS |
| S67 | Remote presence caret layer | src/sync/presence.ts | Optional configured presence, not a durable-save or permission signal; UIS |
| S68 | React EditorHost div; Astro edit-ac-editor and data-editor-surface host | packages/react/src/index.ts; packages/astro/src/Editor.astro | Existing lifecycle only; BWF-1.1 retains ownership, URC/UWH compose UI |
| S69 | Example-only Bold, Heading 2 and Undo buttons; Formatting status for applied/unavailable/select-text/error outcomes | ../docs/examples/recipes/toolbar.mjs | Host composition, not a package API; UIS-1.5 reconciles the Document formatting label with stylesheet hooks |

Non-surface helpers: `src/clipboard/html.ts` and `src/modules/tables/clipboard.ts` create detached parsing/serialization containers, not mounted controls. `src/dom/presentation.ts` and the code/math renderers create styles/presentation content, covered by S41/S42/S65. The focus sentinel is S11. `src/modules/transfer.ts` renders fallback content covered by S66. `src/platform/viewport.ts` manages geometry/control ownership without introducing another toolbar. No unlisted widget is inferred from a semantic command or a package's presence.

## Planned export and optional peer boundaries

The [2026-10-26 distribution plan](integration-distribution.md) adds dedicated repository ownership and registry/listing acceptance to these package boundaries. This ledger continues to own existing exports and feature/task handoffs; core-relative paths remain current implementation locations until extraction. No package or subpath listed here is renamed solely by a repository move.

Each row has one implementation owner. Handoff means the existing owner must supply the prerequisite; it does not authorize this inventory task to create a replacement. Package names remain provisional until their owning package task checks registry availability and pins actual peer ranges. Rows without a framework/library peer must remain framework-free.

| Planned boundary | Single UI implementation owner | Existing prerequisite / optional peer boundary |
| --- | --- | --- |
| @edit-ac/web/controls | UCS-1.6 delivered | Explicit current ESM/types barrel over existing command/target/layout/suggestion/overlay/theme owners; same root identities, no framework peer or automatic CSS |
| @edit-ac/web/ui | UDM | Existing CommandControls/presenters; DOM runtime only when mounted; no framework or Tailwind |
| @edit-ac/web/ui.css | UIS | Existing styles.css preserved; UIC-1.4 names tokens/slots; optional CSS import |
| @edit-ac/react/controls | URC-1.1 | Existing React/BWF-1.1 lifecycle, web controls; React peer only |
| @edit-ac/react/ui | URC-1.4 | URC components; no component-library dependency in root lifecycle export |
| @edit-ac/vue (lifecycle root) | BWF-1.3 | Existing backend framework owner; Vue peer; do not create a second binding |
| @edit-ac/vue/controls and /ui | UVU-1.4 | BWF-1.3 host and UVU selectors/components; Vue peer only |
| @edit-ac/svelte (lifecycle root) | BWF-1.5 | Existing backend framework owner; Svelte peer |
| @edit-ac/svelte/controls and /ui | USV-1.4 | BWF-1.5 host and USV selectors/components; Svelte peer only |
| Existing @edit-ac/astro composition | UWH-1.1 | BWF-1.1 host, default DOM UI/CSS; Astro peer, no React island |
| @edit-ac/react-base-ui | UBU-1.1 | React binding and Base UI peers; chosen library owns widget focus |
| @edit-ac/react-aria | URA-1.1 | React binding and React Aria Components peers |
| @edit-ac/react-radix | URD-1.1 | React binding and selected Radix peers |
| @edit-ac/vue-reka | URK-1.1 | Vue binding and Reka peers |
| @edit-ac/svelte-bits | UBT-1.1 | Svelte binding and Bits peers |
| React shadcn registry sources | USR | Application-owned Base UI or Radix family; matching adapter/React peers |
| Vue shadcn registry sources | USK-1.1 | Application-owned Reka family; matching Vue adapter |
| Svelte shadcn registry sources | USK-1.4 | Application-owned Bits family; matching Svelte adapter |
| Next/Nuxt/SvelteKit UI composition | UWH | Existing BWF-1.2/1.4/1.6 lifecycle profiles, matching framework peer; no semantic SDK |
| Angular / secondary design-system recipes | UWH-1.6 | BWF-1.7/1.8 host/forms; optional host library, not web baseline |
| PHP SDK / Laravel wrapper | BPH | Existing backend protocol/persistence owner; UWH consumes receipts, no UI save implementation |
| Filament field UI/theme composition | UWH-1.3 | BFA-1.1–1.5 field/lifecycle/form-save owner; optional Filament/Livewire boundary; no React |
| Apple mobile controls product | UIA | BNA-1.2/1.3 host and existing SDK; UIKit/optional SwiftUI; no second Session/text view |
| macOS controls product | UMA | BNA-1.4 existing AppKit host; optional SwiftUI; same engine binary |
| Android controls modules | UAN | BNA-1.6/1.7/1.8 host; Views baseline, optional Compose peer/artifact |
| Windows controls module | UWI | BDH existing desktop host; optional WPF adapter; no new FFI owner |
| Linux controls module | ULX | BDH existing GTK host; optional libadwaita and existing Electron/Tauri hosts |
| @edit-ac/react-native/controls and /ui | URN | BCP-1.4/1.5 canonical module/Fabric component; RN peer; bare RN excludes Expo |
| @edit-ac/expo plugin/host integration | UEX | Same BCP RN native module; optional Expo tooling; no Expo-specific second editor module |
| RN Paper / Reusables adapters | URN | Optional Paper peer or application-owned source kit; default RN controls independent |
| editac_flutter UI exports/package | UFL | BCP-1.1 Dart remains Flutter-free; BCP-1.2/1.3 plugin owns platform view/channel; Material/Cupertino UI |
| Expo web presentation | UEX-1.8 | Explicit browser implementation over existing web editor; no native-engine claim |
| Flutter web presentation | UFW | Existing web editor and bounded JS bridge; no native-engine claim |
| Native theme DTOs / target geometry | UIC-1.4 | Existing core/contracts (planned sdk/contracts reconciled here) and native host executor; bounded data, no CSS/DOM/callbacks |

There is no new package in UIC-1.1. The ledger is consumed from the shared spec and the existing web UI source instructions; later owners wire only their named subpaths. UIC-1.5 introduces the dispatcher. Before it exists, UIC-1.1's focused selector is direct manifest/surface inspection followed by owning-repository `git diff --check`, as required by its original V1; do not invent a passing dispatcher run.

## Unsupported and deferred capability claims

| Boundary | Disposition / owner |
| --- | --- |
| Generic @edit-ac/ui installing all frameworks | Unsupported design; use optional per-framework boundaries above |
| Framework-rendered editable descendants or a second simultaneous toolbar owner | Unsupported; existing DOM/native input owner remains authoritative |
| Automatic durable-save/offline/conflict status inferred from UI | Unsupported; real storage/transport receipts required by UDM and existing persistence owners |
| Current table textarea plus preview as completed direct-cell product UI | Unsupported claim; UDM-1.8/1.9, UIS-1.4 and UTW-1.2 retain the correction |
| Native platform qualification inferred from browser UI or DTO compilation | Unsupported; existing native/BNT and roadmap43 observations required |
| RN macOS/Windows or Flutter desktop embedding inferred from native SDK availability | Candidate only; UFW-1.4 requires feasibility and existing BDH/BCP handoff |
| Native mobile editor implemented as hidden WebView/iframe | Unsupported architecture; reuse BCP-owned native platform surface |
| Shadcn universal runtime / all-family dependency bundle | Unsupported; application-owned family-specific source kits |
| Registry availability, packed-consumer compatibility or package publication inferred from names | Unverified; respective package owner and final UTH gates |

## Bounded inspection recipe

1. Compare every existing-export row against `packages/*/package.json` names, export keys/targets, dependencies, peers and side-effect declarations. Record mismatches; `dist` existence is not part of this source inspection.
2. Compare the public seam names with their existing index exports and owning methods. Check every surface row at its named constructor/render/status code, including data-driven controls, conditional launchers, readonly fallbacks and temporary body-mounted paste UI. Count inspected rows separately from runtime cases.
3. Compare planned boundaries to the owning task's declared path and the existing BWF/BFA/BCP/BNA/BDH handoff. A missing planned API remains with that owner and is not a current runtime failure of the inventory task.
4. Run `git diff --check` only in each edited owning repository. No browser, native startup, AI/provider transport, broad test suite, generated package or external service is required. Keep inspection receipts in ignored runner evidence, not source Git.
