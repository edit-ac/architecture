# Optional assistive input contract

Device sequencing (superseding user decision, 2026-10-18): every device/target-runtime/OS-input/AT observation in this document is owned by [final roadmap43](../roadmaps/43-physical-device-verification.md) under the [web feature-first policy](../operations/web-feature-first-20261018.md). Feature implementation keeps focused deterministic correctness/data-safety checks; device rows and D observations run later on accepted simulators/emulators/VMs/OS hosts without waiting for physical hardware. Preserve original case IDs and criteria; deferred observations remain unchecked and do not block web feature completeness. Exhaustive qualification/performance follows the stated later phase.

Qualification amendment (user decision, 2026-10-14): Named target-platform simulators/emulators and desktop OS VMs/test hosts may satisfy platform and release gates when physical hardware is unavailable. Follow the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms) for required runtime checks, tested virtual equivalents for hardware-only observations, counts and physical/virtual provenance. Earlier physical-only/manual-only wording in this document is superseded. This changes accepted evidence, not required implementation or correctness.

Status: development contract; no dictation, voice-control or assistive-technology qualification is asserted.
Scope: an optional portable extension for discoverable editing commands, dictation status and host-supplied assistance. Baseline accessible editing and OS text input remain requirements when this extension is absent or disabled.

Read [editor interactions](editor-interactions.md) for ordinary editing, [web](web.md) for browser composition and selection, [native SDK parity](native-sdk-parity.md) for native text controls, and [extension library](extension-library.md) for registration and portable presenters. [Research evidence](../evidence/assistive-input-research.md) records source dates and platform limitations. This contract adds assistance without transferring committed document ownership from Rust/Yrs.

## Baseline and optional capabilities

Every editor surface retains its required keyboard, selection, composition, screen-reader and OS dictation behavior without installing this extension. Optional assistance cannot repair an otherwise inaccessible document or turn baseline support into an add-on feature. The terminal's qualified nonvisual command/text fallback remains available without a microphone or speech service.

The portable descriptor exposes named commands, applicability, presenter hooks, status, disposal and optional host transport capabilities through the existing extension interfaces. It adds no CRDT root, persisted raw/interim transcript metadata, executable document payload or parallel history. Use existing public package/crate boundaries; a separate speech package or provider is outside this track.

Distinguish these capabilities explicitly:

| Capability | Owner and qualification |
|---|---|
| OS text input, including dictation | Existing browser/native input adapter; actual OS/input-service evidence |
| Accessible editing commands | Shared semantic command plus platform presenter; available through ordinary controls without speech |
| Optional assistance status and controls | Extension presenter; advertise only operations the host actually exposes |
| Host-supplied recognition or transcript transport | Explicit injected host capability; deterministic mock qualification only in automated checks |
| Screen-reader document editing | Baseline editor/native accessibility implementation; real assistive-technology evidence |

OS input availability does not imply programmatic start/stop controls, microphone access, offline recognition or support for every language. If a capability is unavailable, provide an accurate disabled reason or ordinary text/command route. Do not install or select a speech provider implicitly.

## OS input is the default route

Receive committed text through the qualified `beforeinput`/`input`/composition and bounded DOM-reconciliation path, or the platform-native text-input contract. Dictation is not a sequence of synthetic key presses. Do not depend on a universal dictation-specific `inputType`, source flag or cancelable `beforeinput` event. When the OS does not expose dictation state, report ordinary editing state rather than inferred listening status.

The temporary composing subtree/native marked text remains owned by the input control under the existing composition gate. Keep intermediate alternatives out of the authoritative document unless the qualified baseline policy explicitly commits them. Each accepted edit passes the same prepare/validate/commit, read-only, selection and history rules as ordinary text. One input update must never be committed by both the OS adapter and the optional transport route.

The extension must tolerate ordinary typing, OS dictation and accessibility command activation while absent, enabled or being disposed. Preserve the chosen input route across focus changes; a provider result cannot start a new edit after the host has switched documents or destroyed the editor.

## Optional host transport lifecycle

Hosts may inject a bounded transport interface for an explicitly requested assistance session. No built-in speech provider, ambient credential discovery, automatic microphone request or Web Speech API fallback is part of this contract. Hosts expose start/stop/cancel and result/error callbacks only when those operations exist. Stopping requests completion under the declared final-result policy; cancellation rejects further results. The implementation task fixes the typed interface, size/time limits and version before consumers depend on it.

Capture document/epoch, a stable selection, session identity and request generation before asynchronous work. Provisional transcript text is disposable presenter state, visibly distinguished from committed content. Final results identify their session and result sequence; duplicate, out-of-order, cancelled and prior-generation callbacks cannot produce duplicate commits or reopen a session.

Define observable transitions for idle, starting, active, preparing, completed, cancelled, stale and failed. Permission denial, unavailable input, host disconnect and malformed/oversized results have typed recoverable outcomes. Cancellation is idempotent and revokes pending result acceptance before releasing resources. Abort/dispose on document switch, read-only transition or editor destruction; blur behavior is explicit and fixture-covered.

Browser presenters treat the editor and its assistance controls as one focus boundary. Internal focus movement keeps the accepted session; leaving that boundary, closing the panel, window blur or hiding the document cancels pending results and clears provisional presentation without moving later user focus. Starting from a keyboard control transfers focus to an enabled Stop or Cancel control while awaiting the final result. Missing host, permission or stop capability has visible ordinary-input/cancellation guidance associated with the affected controls.

Resolve captured anchors against the current authoritative state before preparing the final replacement. Independent remote edits rebase through existing anchor rules. A deleted, incompatible or otherwise unresolvable target yields a stale result; preserve bounded recovery text in session memory for an explicit user action, never redirect it to the current caret or document end. A changed current selection alone does not silently change the captured target. Replacement selections, combining marks, surrogate pairs, ZWJ emoji, flags and RTL follow the shared UTF-16/grapheme contract.

Commit a final accepted result using the existing semantic command and intentional history boundary. Provisional updates and status changes create no document/history entries. Undo and redo preserve unrelated remote changes. Committing a final result consumes it exactly once, including when persistence reports a later recoverable failure.

## Accessible command presenters and status

Provide visible, named controls and a keyboard/nonpointer route for every assistance action. Visible labels and accessible names agree so voice-control users can invoke them by name. Respect platform shortcut conventions, editable focus and composition; do not intercept global printable-character shortcuts. Slash input is never the only way to find an editing command. Keep focus visible when panels, suggestions or on-screen keyboards appear.

Use the appropriate native accessibility roles/actions and the established web control pattern. A dedicated command-search field may implement combobox/listbox behavior; a menu button follows its own focus/keyboard contract. Opening a slash popup does not turn the entire rich document into a combobox. Preserve a stable editing selection while focus moves into controls, and restore focus predictably after commit, cancellation or dismissal without overriding a subsequent user focus change.

Present availability, permission errors, active assistance, cancellation, stale targets and recovery actions in perceivable text. Announce meaningful status transitions through platform status/live-region facilities without repeating every provisional token or stealing editing focus. Do not announce private transcript content by default. Respect host language, direction, zoom, contrast and reduced-motion settings. Keyboard-only and screen-reader routes reach cancellation and recovery controls.

## Privacy and resource ownership

Native input does not establish that recognition runs on the device. Document the OS/service mode actually tested and any known network or language restrictions. An optional host transport declares whether it receives audio or transcript text, its processing destination, permission ownership, retention policy and cancellation behavior before the user starts it. Unknown processing locality is shown as unknown.

The editor retains only bounded session state needed for editing/recovery. It neither stores audio nor sends document context by default. Credentials remain host-owned. Accepted final text becomes ordinary document content and therefore may appear in document updates and user exports. Audio and raw/interim/unaccepted transcript metadata stay out of document updates, logs and telemetry; test artifacts use only prepared or non-sensitive qualification text. Export of retained recovery text requires an explicit user action. Release listeners, streams, callbacks and host session handles on all terminal states; late callbacks are inert. Normal OS dictation follows OS permissions rather than an additional extension permission prompt.

Automated fixtures use prepared event sequences, fixed transcript results and mock transports. They never open a microphone, contact a speech/model provider, load `.secrets`, record fixtures from a live provider or spend inference credits. Physical or named target-platform virtual runs, including tested hardware-only equivalents, validate OS input/accessibility with non-sensitive test documents and record only the minimum evidence. A separate host-provider dogfood workflow requires its own exact content scope, hard request/monetary cap and stop condition; this track does not authorize it.

## Platform obligations and qualification

Web, iOS, Android, macOS, Windows and Linux presenters call the same semantic operations. Each native adapter uses its qualified text control, UI thread and platform accessibility mechanisms. It may expose explicit unsupported assistance capabilities where the OS has no relevant API; the baseline native parity obligations remain unchanged. Terminal assistance uses explicit commands, readable status and pasted/text input; it does not claim native speech capture or infer voice commands from arbitrary text.

Maintain a capability matrix by OS/device, browser or native toolkit, input method/service, language, screen reader and tested version. Each cell distinguishes baseline editing, OS dictation, voice activation, extension controls and optional host transport. State whether evidence is deterministic, physical or virtual platform, unsupported or pending; a prepared transcript proves neither speech recognition quality nor actual device compatibility.

Deterministic cases cover extension absent/disabled, ordinary input during assistance, noncancelable/missing input events, selection replacement, composition overlap, remote insertion/deletion, final-result deduplication, cancellation, denied permission, read-only transition, blur, document switch, destruction and resource release. Assert semantic content, UTF-16 selection, origin/history, status/focus and unchanged state on rejection. Include accessible names and keyboard behavior; screen-reader behavior is observed where the runtime supports it; otherwise executed native accessibility-tree/action and focus checks are the accepted virtual equivalent, with physical exploration deferred.

Actual-device cases cover the declared web/mobile and native surfaces with real dictation and accessibility tools where supported: text insertion/correction/replacement, formatting controls, structural commands, selection, cancellation/recovery, IME coexistence and RTL. Record exact OS, browser/toolkit, hardware, locale, input service, assistive technology, case outcomes and retained failure/skip reasons. Native task evidence is platform-specific; missing one native environment does not block portable implementation or another platform's work. It does block an unqualified cross-platform completion claim.

Capability aggregation checks evidence provenance and omissions; it does not substitute a metadata validator for behavior tests. Keep unsupported/pending rows visible, preserve failures and link actual device artifacts. No publication, new provider integration or paid-content qualification follows automatically from this roadmap.

## Mobile browser assistance

Baseline mobile OS input/accessibility is qualified by [track 40](../roadmaps/40-mobile-web.md) with the extension disabled. Claimed optional mobile-web controls reuse its focus/viewport/capability ports and are integrated in MWX-1.7 under [track 41](../roadmaps/41-mobile-web-extensions.md). AIN-1.2/1.3/1.10 remain the prerequisite web presentation/lifecycle/device work; no native assistance task is required to begin the mobile-web integration. Soft keyboard occlusion, VoiceOver/TalkBack navigation, provider-error/cancel controls and explicit user-activation behavior need actual device evidence.
