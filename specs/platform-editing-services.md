# Platform editing services and user preferences

Device sequencing (superseding user decision, 2026-10-18): every device/target-runtime/OS-input/AT observation in this document is owned by [final roadmap43](../roadmaps/43-physical-device-verification.md) under the [web feature-first policy](../operations/web-feature-first-20261018.md). Feature implementation keeps focused deterministic correctness/data-safety checks; device rows and D observations run later on accepted simulators/emulators/VMs/OS hosts without waiting for physical hardware. Preserve original case IDs and criteria; deferred observations remain unchecked and do not block web feature completeness. Exhaustive qualification/performance follows the stated later phase.

Status: planned contract amendment, 2026-10-17. Reuse browser/OS editor facilities where their behavior can be admitted through the existing editor boundaries. This document refines existing roadmap parents; it does not qualify a platform, start a runner or change historical completion evidence. [Environment cases](../tests/platform-editing-cases.md) expand existing DXC/EVT/HIS/KEY/NAT cases rather than creating a second editing suite.

## Ownership

Browser and native controls own temporary composition, platform presentation and user interaction. The shared engine/session remains the owner of committed content, selection bookmarks, command admission and semantic history. Native text storage and the DOM are projections. Reusing an OS feature must not introduce another writable document, undo stack, spell dictionary or service account in the engine.

Configuration and learned/ignored words are host/user preferences, not synchronized document marks. Spelling underlines, candidate windows and suggestions are transient presentation. Only an accepted correction or other committed platform edit becomes a normal semantic command. Preserve existing readonly, permission, composition, UTF-16, captured-target and disposal rules.

## Spellcheck modes

The public configuration exposes the following meanings; SDK-1.11 freezes the exact typed API and native adapters expose equivalent policy. The default is `platform`.

| Mode | Required behavior |
|---|---|
| `platform` | Reuse available browser/native spelling indicators, suggestion menus and dictionaries. Respect user/browser/OS settings and host-provided per-user preferences. Preserve inherited/default behavior where a platform exposes no reliable preference query. Do not force spelling on, change global preferences or import a custom checker. |
| `off` | Disable editor-owned spell checking and request suppression of platform spelling indicators/suggestions for this surface where supported. Do not disable unrelated keyboard services or change global/user dictionaries. Report any platform limitation rather than silently changing autocorrection or claiming complete suppression. |
| `custom` | Require an explicitly configured checker and optional dictionary/locale assets. Load them only for that editor's enabled custom mode. Suppress equivalent platform spelling presentation where independently supported; if exclusive presentation cannot be guaranteed, expose that limitation and reject exclusive activation or require an explicit host/user choice before accepting overlapping presentation. Never silently fall back to another checker. |

The SDK reports requested policy separately from observed availability/effective state, including `unknown` or `unsupported` where necessary. An absent underline, property value or unavailable locale is not proof that the user disabled spelling or that a dictionary is available. A disabled/unavailable platform checker leaves ordinary editing usable and does not trigger a custom download or service request. HTML explicitly permits user preferences to override the `spellcheck` attribute; its JavaScript property need not reflect effective checking. [HTML spelling contract](https://html.spec.whatwg.org/multipage/interaction.html#spelling-and-grammar-checking)

Do not set `spellcheck=true` merely because the SDK default is `platform`. Preserve the host's explicit attribute and inherited behavior unless a documented editor override was supplied. Supply document/region language hints only when known; do not override the user's chosen keyboard/dictionary. Define bounded code/literal/identifier exclusions where the control supports them and document unsupported per-range exclusions. Reconfiguration restores only SDK-owned attributes/traits and cannot overwrite newer host/user changes. Disposal removes custom presentation and cancels its work.

Custom analysis is bounded to changed ranges and excludes active composition. Validate the captured current text, stable anchors, session and permission before applying a suggestion. One acceptance produces one prepared replacement with formatting, directional selection and undo preserved. Stale results, unknown words, analysis errors and canceled suggestions have no document/history effect. `platform` and `off` load no SDK checker, dictionary or analysis worker; a custom mode in another editor cannot enable checking or share mutable request state here.

## Autocorrection and related preferences

Autocorrection is an independent setting with platform-default and explicit-off behavior. Changing spellcheck mode must not implicitly turn autocorrection on or off. Keep capitalization, prediction/completion, smart quotes/dashes and text replacement as separate platform capabilities/preferences; spelling is not a master switch for all input assistance. Defaults preserve platform/user choices. An unsupported combination is reported explicitly and never approximated by an unrelated global switch.

Some controls couple services. UIKit's default spelling behavior depends on autocorrection, and its explicit spelling trait can override the user's setting; adapters must validate their actual default/override mapping. Android's `TYPE_TEXT_FLAG_NO_SUGGESTIONS` also affects dictionary candidates and autocorrection, so it must not be used as a supposedly independent spelling toggle. Preserve gesture typing and IME behavior when choosing flags. [UIKit spelling](https://developer.apple.com/documentation/uikit/uitextinputtraits/spellcheckingtype), [Android input flags](https://developer.android.com/reference/android/text/InputType#TYPE_TEXT_FLAG_NO_SUGGESTIONS)

## Undo, redo and command surfaces

Reuse the platform's command affordances while retaining one shared semantic history. Support Cmd+Z and Cmd+Shift+Z on Apple profiles, Ctrl+Z and the declared Ctrl+Y/Ctrl+Shift+Z redo bindings on other profiles, plus applicable Edit menus, context menus, toolbars, accessibility actions and native undo gestures. Route each accepted intent to the focused editor/session exactly once. Browser `beforeinput` historyUndo/historyRedo intents are another entry point, not a second edit or a range-based replacement; their target ranges are empty in the standard. [Input Events Level 2](https://www.w3.org/TR/input-events-2/)

Native undo managers may be a forwarding facade to shared history. They must not record projection refreshes, remote changes or a second copy of accepted semantic edits. Disabling a native stack alone does not implement menu/gesture undo: qualification must prove routing, enabled/disabled state and resulting content/selection. Browser native-history leakage must be prevented or explicitly reconciled through the existing bounded input policy; never use a whole-document DOM diff as an undo strategy.

Menu/key enablement uses current shared command applicability and history state; execution rechecks it. Empty history, readonly/denied actions and disposed sessions do nothing. Preserve remote edits, correction undo/redo, typing groups, selection/pending marks and stable redo behavior under the existing history contract. During active IME/candidate editing, honor the qualified platform composition policy before issuing document history. Nested search fields, code controls and host inputs retain their own command ownership. Keydown plus beforeinput/menu delivery must not cause two undos.

## Other reusable environment features

These are refinements of existing owners, not a promise that every OS offers every facility. Prefer the selected control's capabilities and user preferences; expose unsupported optional services. Required core editing cannot be waived because an optional service is absent.

| Feature | Reuse and integration boundary | Existing owners |
|---|---|---|
| IME, dead keys, dictation, handwriting and emoji/character pickers | Keep native candidate/marked-text UI, surrounding-text queries and selection geometry. Route committed replacements by the reported range, preserve cancellation and avoid double commits or Markdown-triggering provisional/non-typing text. | INT-1.7, native input parents, tracks 39/40; ENV-09 |
| Selection, word/line movement and deletion | Reuse native pointer/touch handles and layout-aware movement where qualified. Preserve bidi/graphemes, directional selections and semantic structure; keep UTF-16 conversions at adapter boundaries. | INT-1.4/1.5, native selection parents; ENV-11 |
| Cut/copy/paste, plain paste and drag/drop | Reuse clipboard APIs, menus and delayed native providers; retain existing rich/plain precedence, sanitization, captured targets, cut atomicity, permissions and undo. | INT-1.10/1.15–1.17, native clipboard parents; ENV-10 |
| Focus and familiar shortcuts | Preserve Tab/Shift+Tab focus traversal and editor escape, Select All, context menus, browser/OS Find, reserved shortcuts and AltGraph. Only consume commands owned by the focused editor; optional document Find is explicit. | INT-1.6/1.18, native command parents; ENV-08 |
| Accessibility and presentation | Reuse text-control accessibility, text ranges, actions, caret/candidate geometry, system font scaling and contrast settings. Bridge structured content correctly; do not replace native text semantics with a generic inaccessible canvas. | INT-1.13, native accessibility parents; ENV-11 |
| Smart substitutions, reconversion, OS Services and writing tools | Preserve user settings and explicit invocation. Qualify accepted replacements through stable targets with readonly, permission, formatting and history checks; unsupported rich/multiple-range results retain recoverable content. Native API presence does not enable an external service or authorize paid calls. | INT-1.7, native input/command parents and NAT-08; ENV-12 |

## Platform research and constraints

Primary documentation checked 2026-10-17. These identify reusable APIs, not evidence that edit.ac has qualified them.

| Environment | Finding and implementation constraint |
|---|---|
| Browser | `contenteditable` supports spelling and separate autocorrection hints. Platform corrections can omit beforeinput or be noncancelable; keep bounded input/reconciliation handling and validate actual browser/OS behavior. [HTML interaction](https://html.spec.whatwg.org/multipage/interaction.html), [beforeinput behavior](https://developer.mozilla.org/en-US/docs/Web/API/Element/beforeinput_event) |
| macOS | NSTextView exposes spelling, correction and text-system facilities, and has its own undo option. Reuse its UI through adapter/session routing; do not enable a competing native history. [NSTextView](https://developer.apple.com/documentation/appkit/nstextview), [allowsUndo](https://developer.apple.com/documentation/appkit/nstextview/allowsundo) |
| iOS | UITextInputTraits exposes spelling, autocorrection, capitalization, smart substitutions, prediction and writing-tool policy. Treat availability/defaults as version-specific and verify each independent control. [UITextInputTraits](https://developer.apple.com/documentation/uikit/uitextinputtraits) |
| Android | InputType flags and the selected IME jointly determine candidates/correction behavior; a flag does not prove actual keyboard behavior. Preserve InputConnection composition, deletion units and surrounding-text contracts. [InputType](https://developer.android.com/reference/android/text/InputType) |
| Windows | The selected RichEditBox candidate supplies spell checking, selection and native editing facilities; its document also has native history that must be adapted to the shared engine. Prediction/input-scope controls are separate from spelling. [RichEditBox](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/rich-edit-box), [input scope](https://learn.microsoft.com/en-us/windows/apps/develop/input/use-input-scope-to-change-the-touch-keyboard) |
| Linux | GTK is not proof of an installed system spell checker. GNOME libspelling offers checking/menu adapters specifically for GtkSourceBuffer; compatibility with the chosen GTK TextBuffer/control must be established before selecting it. Do not add that dependency or a duplicate buffer implicitly. An unavailable provider is an explicit supported fallback for platform mode. [libspelling adapter](https://gnome.pages.gitlab.gnome.org/libspelling/libspelling-1/class.TextBufferAdapter.html) |

## Qualification and adoption

SDK-1.11 owns typed configuration/defaults/instance isolation; EXT-1.18 owns browser platform/off/custom behavior and the optional prepared-checker recipe. INT-1.7 owns replacement mechanics, INT-1.12 shared undo routing, and INT-1.14 browser/OS observations. IOS/AND/DSK/WIN/LNX-1.6 own native spelling/preferences/replacements; their -1.7 parents own command/history surfaces. Native release observations remain with DEL-1.7. Existing selection, clipboard and accessibility owners consume the relevant ENV variants. This does not make browser delivery depend on all native platforms or advance deferred native work.

Use the [case catalog](../tests/platform-editing-cases.md) and [qualification policy](verification.md#platform-qualification-with-simulators-emulators-and-vms). Deterministic prepared dictionaries/events/services prove policy and semantic correctness; they do not prove the OS actually shows suggestions, honors preferences or routes its menus. Require real control interactions on declared browser/OS or native runtime profiles, with exact versions, keyboard/locale, settings, source/artifact hashes, observations and executed/passed/failed/skipped counts. Target-platform simulators/emulators/VMs and tested hardware-only equivalents are accepted; desktop WebKit alone is not Safari/iOS qualification.

Observe enabled/disabled user settings in isolated test profiles and restore changes; never change the user's workstation preferences as a test shortcut. Unavailable optional services require an executed absence/fallback case, not a fabricated success or a skipped mandatory row. Only actually qualified combinations may be advertised. No live hosted checker, paid inference, subscription proxy or automatic provider recording is permitted for these tests; prepared replacements do not establish provider quality.

Adopt amended acceptance at existing coordinators' safe source-refresh checkpoints. Preserve immutable active snapshots and historical receipts; earlier completed parents need explicit supplemental evidence for these new variants. No new parent/lane or publication is authorized by this amendment.
