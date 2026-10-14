# Add optional portable assistive input

Status: IN_PROGRESS

Qualification amendment (user decision, 2026-10-14): Physical devices, named target-platform simulators/emulators and desktop OS VMs/test hosts are accepted for platform and release qualification under the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms). Missing physical hardware does not block completion. Execute required behavior against the implemented target-platform runtime; document and test virtual equivalents for unavailable hardware-only input/accessibility cases. Record physical versus virtual provenance and measure performance in the tested environment. This supersedes earlier physical-only or manual-only clauses below; it does not complete unchecked tasks or waive implementation, correctness, security or artifact gates.

## Goal and entry conditions

Workspace: `core`; only AIN-1.9 implements in sibling `cli`. Paths below are workspace-relative unless explicitly prefixed `../cli/` or `../architecture/`. Read `../architecture/specs/assistive-input.md` and only the active task's named context. Planned implementation paths, test suites and commands are created by their owning task. This source defines delivery; it makes no current capability claim.

Required upstream tracks: `38-editor-interactions.md` and `21-extension-library.md` complete at reviewed immutable source/implementation revisions with passing artifact evidence. Native SDK and terminal gates are task-specific below; their absence does not block portable/web tasks or independent platform work. Local Dependencies fields refer only to this file.

Baseline OS input, screen-reader editing and accessible commands remain mandatory without this optional extension. Use existing engine/extension semantics and the default OS text-input route. Optional recognition is an explicit injected host capability; this track adds no speech provider.

## Execution rules

The controller owns this source. Keep checkmarks, evidence and interruption handoff in the separate progress file. Run one parent per iteration with its implementation and validation substeps. Read task-local context. Create named checks before invoking them; unknown suites, zero matches and skipped required platforms cannot pass. Automated checks use deterministic events, prepared transcripts and mocked transports only: no microphone, provider calls, paid inference, credential loading or automatic fixture recording. Actual-device OS/accessibility qualification is separate, uses non-sensitive documents and does not authorize host-provider dogfood.

Record automated, manual and evidence-validator counts separately. Missing device access blocks the task requiring that evidence, never an independent ready task. Preserve failure/skip evidence and capability limitations. Do not launch another controller, install a speech service or publish packages. Close task-owned test browsers/servers and release input/transport sessions after checks.

## Epic AIN-1 — Deliver optional assistance without weakening baseline editing

### Task AIN-1.1 — Define the portable assistive input descriptor

- [ ] AIN-1.1 Define the portable assistive input descriptor.

Purpose: Fix the optional capability and session envelopes before platform presenters depend on them.
Context: `crates/editac-core/src/extensions/assistive_input.rs`; `crates/editac-core/tests/assistive_input_contract.rs`; `packages/core/src/extensions/assistive-input.ts`; `../architecture/specs/extension-library.md`; `../architecture/specs/assistive-input.md`.
Dependencies: none.
Session scope: One named boundary, normally 15–45 minutes plus focused validation. If its implementation or required device matrix cannot fit, propose a stable controller-reviewed split before implementation; retain full acceptance.
Acceptance: Registration is optional and leaves baseline editing intact. The descriptor uses existing extension boundaries, names command/status/transport capabilities and resource bounds, and rejects incompatible versions without mutation. No new document schema, recognition provider or parallel history is introduced.

Implementation:

- [ ] AIN-1.1-I1 Create the descriptor and public typed envelopes for command applicability, presenter status, stable target/session identity, cancellation and optional injected host transport. Add fixed valid/invalid descriptors and compatibility fixtures to the extension conformance harness; record which lifecycle fields are host-owned.

Validation:

- [ ] AIN-1.1-V1 `cargo test -p editac-core --test assistive_input_contract --locked`. Create this suite in this task. Exercise absent/disabled extension, invalid registration, bounded envelopes, disposal and unknown capability handling; verify document/update/history state is unchanged by registration and status. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes.

Evidence: Separate progress entry `AIN-1.1` links changed paths, immutable inputs and focused artifacts; retain failed evidence and identify physical or virtual platform versus prepared-fixture results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `AIN-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task AIN-1.2 — Add accessible web assistance presenters

- [ ] AIN-1.2 Add accessible web assistance presenters.

Purpose: Make optional editing assistance discoverable through ordinary accessible controls.
Context: `packages/web/src/modules/assistive-input.ts`; `tests/browser/assistive-presenter.spec.ts`; `../architecture/specs/web.md`; `../architecture/specs/assistive-input.md`.
Dependencies: AIN-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused validation. If its implementation or required device matrix cannot fit, propose a stable controller-reviewed split before implementation; retain full acceptance.
Acceptance: Named controls expose command applicability, cancellation and recovery with keyboard/nonpointer access. Visible and accessible names agree. Dedicated search/menu semantics, selection retention, dismissal and focus restoration work without reclassifying the rich document as a combobox; absence of the extension preserves baseline controls.

Implementation:

- [ ] AIN-1.2-I1 Implement presenter hooks using shared semantic commands and the qualified selection mapping. Add bounded status announcements and explicit unsupported-capability reasons. Preserve editing anchors during control focus, respect read-only/composition state, and retain routes independent of slash input or global printable shortcuts.

Validation:

- [ ] AIN-1.2-V1 `npm run test:browser -- assistive-presenter`. Create the named suite and dispatcher entry in this task. Check keyboard focus, labels/roles, command applicability, status transitions, extension teardown and unchanged selection/content on cancelled controls; structural accessibility checks are not screen-reader qualification. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes.

Evidence: Separate progress entry `AIN-1.2` links changed paths, immutable inputs and focused artifacts; retain failed evidence and identify physical or virtual platform versus prepared-fixture results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `AIN-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task AIN-1.3 — Implement deterministic assistance session lifecycle

- [ ] AIN-1.3 Implement deterministic assistance session lifecycle.

Purpose: Integrate OS input and optional prepared host results with one authoritative edit lifecycle.
Context: `packages/core/src/extensions/assistive-input-session.ts`; `packages/web/src/modules/assistive-input.ts`; `tests/browser/assistive-dictation.spec.ts`; `../architecture/specs/assistive-input.md`; `../architecture/specs/engine.md`.
Dependencies: AIN-1.1, AIN-1.2.
Session scope: One named boundary, normally 15–45 minutes plus focused validation. If its implementation or required device matrix cannot fit, propose a stable controller-reviewed split before implementation; retain full acceptance.
Acceptance: OS input stays on the existing event/composition route. An injected mock transport commits each final result once through captured stable anchors and shared history. Cancellation, deleted targets, document/epoch changes, read-only, late callbacks and disposal cannot redirect or duplicate edits; provisional text remains bounded presenter state.

Implementation:

- [ ] AIN-1.3-I1 Create the session state machine and mock transport with explicit generation/result sequencing and resource cleanup. Exercise missing/noncancelable beforeinput, composition overlap, UTF-16 replacement, remote edits, denied capability/permission, blur, destroy and stale recovery. Keep OS input and transport commits mutually exclusive per accepted result; document privacy and processing-locality capability fields.

Validation:

- [ ] AIN-1.3-V1 `npm run test:browser -- assistive-dictation`. Create the named suite/fixtures and dispatcher entry in this task. Assert semantic text/selection, origin/undo groups, no duplicate commits, nonmutating errors and cleanup. Use prepared events/transcripts only: no microphone, external provider, credentials or fixture recording. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes.

Evidence: Separate progress entry `AIN-1.3` links changed paths, immutable inputs and focused artifacts; retain failed evidence and identify physical or virtual platform versus prepared-fixture results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `AIN-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task AIN-1.4 — Integrate assistive input in the iOS adapter

- [ ] AIN-1.4 Integrate assistive input in the iOS adapter.

Purpose: Bind the portable assistance contract to the qualified iOS text and accessibility control.
Context: `native/ios/`; `native/ios/capability.json`; `native/ios/scripts/check.sh`; `../architecture/specs/native-sdk-parity.md`; `../architecture/specs/assistive-input.md`.
Dependencies: AIN-1.1, AIN-1.3.
Task-specific entry gate: `16-ios-sdk.md` complete at a reviewed source/implementation revision with passing artifacts; this gate applies only to AIN-1.4 and consumers of its evidence.
Session scope: One named boundary, normally 15–45 minutes plus focused validation. If its implementation or required device matrix cannot fit, propose a stable controller-reviewed split before implementation; retain full acceptance.
Acceptance: The native input route, marked text, stable selection and shared history remain authoritative. Accessible iOS actions/status, optional host-session disposal and unsupported controls follow the descriptor. Declared iOS Simulator or physical-device accessibility and OS dictation cases have recorded results or tested virtual equivalents under verification.md; prepared transcripts qualify routing behavior, not recognition quality.

Implementation:

- [ ] AIN-1.4-I1 Attach the descriptor to the existing native presenter and UI-thread lifecycle, preserving OS dictation and baseline accessibility when disabled. Create the assistive-input dispatcher suite, mock callback fixtures and a focused physical or virtual platform protocol; capture OS/device/locale/tool versions, permission/cancel/replacement/stale-target cases and retained failures.

Validation:

- [ ] AIN-1.4-V1 `bash native/ios/scripts/check.sh assistive-input`. Create the suite and manual protocol in this task. Run deterministic native cases and the declared physical or virtual platform cases; record their counts separately. Simulator execution plus tested virtual equivalents for unavailable hardware-only/manual cases may complete this acceptance under verification.md. Missing implemented behavior or failed required checks remains a blocker. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes.

Evidence: Separate progress entry `AIN-1.4` links changed paths, immutable inputs and focused artifacts; retain failed evidence and identify physical or virtual platform versus prepared-fixture results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `AIN-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task AIN-1.5 — Integrate assistive input in the Android adapter

- [ ] AIN-1.5 Integrate assistive input in the Android adapter.

Purpose: Bind assistance to the qualified Android input connection and accessibility presenter.
Context: `native/android/`; `native/android/capability.json`; `native/android/scripts/check.sh`; `../architecture/specs/native-sdk-parity.md`; `../architecture/specs/assistive-input.md`.
Dependencies: AIN-1.1, AIN-1.3.
Task-specific entry gate: `17-android-sdk.md` complete at a reviewed source/implementation revision with passing artifacts; this gate applies only to AIN-1.5 and consumers of its evidence.
Session scope: One named boundary, normally 15–45 minutes plus focused validation. If its implementation or required device matrix cannot fit, propose a stable controller-reviewed split before implementation; retain full acceptance.
Acceptance: IME/dictation replacement and composing text use the existing native path; the extension neither infers voice commands from ordinary text nor maintains another undo stack. TalkBack-reachable actions/status, stale results and disposal follow the portable contract with recorded actual declared device/IME evidence.

Implementation:

- [ ] AIN-1.5-I1 Integrate the descriptor with the existing Android text control and UI-thread ownership. Add mock transport and input-connection cases for permission/cancellation, composition, selection replacement, remote deletion and destruction. Create the named suite and a physical or virtual platform protocol recording Android/device, keyboard/voice input service, locale and TalkBack versions.

Validation:

- [ ] AIN-1.5-V1 `bash native/android/scripts/check.sh assistive-input`. Create the suite/protocol in this task, then run deterministic and physical or virtual platform cases with separate counts. Emulator execution with prepared recognition results and tested platform-boundary equivalents may satisfy unavailable hardware-only cases under verification.md. Record unavailable input services and do not claim speech-recognition quality from prepared transcripts. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes.

Evidence: Separate progress entry `AIN-1.5` links changed paths, immutable inputs and focused artifacts; retain failed evidence and identify physical or virtual platform versus prepared-fixture results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `AIN-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task AIN-1.6 — Integrate assistive input in the macOS adapter

- [ ] AIN-1.6 Integrate assistive input in the macOS adapter.

Purpose: Expose assistance through the qualified macOS text system and accessible native controls.
Context: `native/macos/`; `native/macos/capability.json`; `native/macos/scripts/check.sh`; `../architecture/specs/native-sdk-parity.md`; `../architecture/specs/assistive-input.md`.
Dependencies: AIN-1.1, AIN-1.3.
Task-specific entry gate: `18-desktop-native.md` complete at a reviewed source/implementation revision with passing artifacts; this gate applies only to AIN-1.6 and consumers of its evidence.
Session scope: One named boundary, normally 15–45 minutes plus focused validation. If its implementation or required device matrix cannot fit, propose a stable controller-reviewed split before implementation; retain full acceptance.
Acceptance: Dictation/text-service edits, native menu actions and Voice Control activation preserve selection, semantic command routing and origin-aware history. VoiceOver reads the required controls/status. OS/service capability and processing-locality claims are accurate for the tested system.

Implementation:

- [ ] AIN-1.6-I1 Bind presenter/session hooks to the existing macOS adapter with explicit UI-thread disposal and unsupported-operation states. Create the named deterministic suite plus a focused actual-machine protocol covering Dictation, Voice Control, VoiceOver, cancellation, replacement, IME coexistence, remote target deletion and disabled-extension baseline behavior.

Validation:

- [ ] AIN-1.6-V1 `bash native/macos/scripts/check.sh assistive-input`. Create the suite/protocol in this task. Run mock lifecycle/semantic fixtures and actual supported OS input/accessibility cases separately, recording exact hardware/OS/language/tool versions and failures; synthetic key events do not satisfy native service evidence. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes.

Evidence: Separate progress entry `AIN-1.6` links changed paths, immutable inputs and focused artifacts; retain failed evidence and identify physical or virtual platform versus prepared-fixture results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `AIN-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task AIN-1.7 — Integrate assistive input in the Windows adapter

- [ ] AIN-1.7 Integrate assistive input in the Windows adapter.

Purpose: Connect assistance to the qualified Windows text and accessibility adapter.
Context: `native/windows/`; `native/windows/capability.json`; `native/windows/scripts/check.ps1`; `../architecture/specs/native-sdk-parity.md`; `../architecture/specs/assistive-input.md`.
Dependencies: AIN-1.1, AIN-1.3.
Task-specific entry gate: `22-windows-native.md` complete at a reviewed source/implementation revision with passing artifacts; this gate applies only to AIN-1.7 and consumers of its evidence.
Session scope: One named boundary, normally 15–45 minutes plus focused validation. If its implementation or required device matrix cannot fit, propose a stable controller-reviewed split before implementation; retain full acceptance.
Acceptance: Native text-service/dictation input and accessible command invocation preserve the same selection, read-only and history semantics. The matrix distinguishes the tested Voice Access and voice typing routes, including actual network/language constraints; offline recognition is never inferred from native integration.

Implementation:

- [ ] AIN-1.7-I1 Wire portable presenter/session capabilities into the native adapter and accessibility actions. Add deterministic mock lifecycle/input cases and an actual-machine protocol for supported Voice Access/voice typing plus declared Narrator/NVDA paths, including correction, replacement, cancellation, composition, stale anchors and disposal.

Validation:

- [ ] AIN-1.7-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite assistive-input`. Create the suite/protocol in this task. Record deterministic and real-service/screen-reader cases separately with exact Windows, toolkit, service, language and assistive-technology versions. Missing hardware/service evidence remains pending; no host-provider or paid-recognition test is authorized. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes.

Evidence: Separate progress entry `AIN-1.7` links changed paths, immutable inputs and focused artifacts; retain failed evidence and identify physical or virtual platform versus prepared-fixture results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `AIN-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task AIN-1.8 — Integrate assistive input in the Linux adapter

- [ ] AIN-1.8 Integrate assistive input in the Linux adapter.

Purpose: Integrate portable assistance with the chosen Linux toolkit and qualified accessibility stack.
Context: `native/linux/`; `native/linux/capability.json`; `native/linux/scripts/check.sh`; `../architecture/specs/native-sdk-parity.md`; `../architecture/specs/assistive-input.md`.
Dependencies: AIN-1.1, AIN-1.3.
Task-specific entry gate: `23-linux-native.md` complete at a reviewed source/implementation revision with passing artifacts; this gate applies only to AIN-1.8 and consumers of its evidence.
Session scope: One named boundary, normally 15–45 minutes plus focused validation. If its implementation or required device matrix cannot fit, propose a stable controller-reviewed split before implementation; retain full acceptance.
Acceptance: Accessible commands/status and optional host-session lifecycle use the native toolkit and shared semantics. Baseline text/IME input works without the extension; speech capture/control is explicitly unsupported when unavailable. Toolkit, display-server, input-service and Orca support claims name actual tested combinations.

Implementation:

- [ ] AIN-1.8-I1 Bind the descriptor to the existing Linux adapter, preserving toolkit text input, selection and UI-thread ownership. Create mock callback/input fixtures and a real-system accessibility/IME protocol; exercise OS dictation only where an existing supported service is available, without provisioning a new provider. Record unavailable speech capabilities explicitly.

Validation:

- [ ] AIN-1.8-V1 `bash native/linux/scripts/check.sh assistive-input`. Create the suite/protocol in this task. Run deterministic cases and actual declared toolkit/Orca/input-method cases, with speech-service evidence only for claimed combinations. An unsupported optional speech cell is honest scope; an untested mandatory baseline accessibility cell cannot pass. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes.

Evidence: Separate progress entry `AIN-1.8` links changed paths, immutable inputs and focused artifacts; retain failed evidence and identify physical or virtual platform versus prepared-fixture results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `AIN-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task AIN-1.9 — Add the terminal assistance fallback

- [ ] AIN-1.9 Add the terminal assistance fallback.

Purpose: Provide explicit nonvisual text/command routes without assuming a terminal speech API.
Context: `../cli/src/tui/`; `../cli/tests/assistive_input.rs`; `../architecture/specs/tui-client.md`; `../architecture/specs/assistive-input.md`.
Dependencies: AIN-1.1.
Task-specific entry gate: `15-tui-client.md` complete at a reviewed source/implementation revision with passing artifacts; this gate applies only to AIN-1.9 and consumers of its evidence.
Session scope: One named boundary, normally 15–45 minutes plus focused validation. If its implementation or required device matrix cannot fit, propose a stable controller-reviewed split before implementation; retain full acceptance.
Acceptance: The TUI exposes discoverable commands, readable bounded status and pasted/text replacement through shared semantics. Cancel, stale-target recovery, read-only and teardown work with mocked host results if supported. No raw audio capture, printable-key interception, ANSI-only status or implicit spoken-command parsing is introduced.

Implementation:

- [ ] AIN-1.9-I1 Add the portable command/status presenter using qualified TUI focus and accessible text behavior. Create deterministic fixtures for Unicode replacement, stable targets, cancellation and extension absent/disabled. Document terminal/screen-reader limits and verify the declared real terminal accessibility path without claiming native speech recognition.

Validation:

- [ ] AIN-1.9-V1 From `../cli`: `cargo test --test assistive_input --locked`. Create this suite in the CLI task and record separate real terminal/screen-reader cases for the claimed combinations. The mandatory fallback remains usable when optional transport and OS voice input are unavailable; runtime accessibility observations or tested virtual equivalents satisfy the gate; missing implemented accessibility/fallback behavior stays unqualified. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes.

Evidence: Separate progress entry `AIN-1.9` links changed paths, immutable inputs and focused artifacts; retain failed evidence and identify physical or virtual platform versus prepared-fixture results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `AIN-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task AIN-1.10 — Qualify real web dictation and accessible assistance

- [ ] AIN-1.10 Qualify real web dictation and accessible assistance.

Purpose: Qualify the actual browser/device input paths that deterministic fixtures cannot establish.
Context: `tests/browser/assistive-presenter.spec.ts`; `tests/browser/assistive-dictation.spec.ts`; `tests/manual/assistive-input-web.md`; `../architecture/evidence/assistive-input-web/`; `../architecture/specs/verification.md`; `../architecture/specs/assistive-input.md`.
Dependencies: AIN-1.2, AIN-1.3.
Session scope: One named boundary, normally 15–45 minutes plus focused validation. If its implementation or required device matrix cannot fit, propose a stable controller-reviewed split before implementation; retain full acceptance.
Acceptance: A declared desktop/mobile browser matrix records real OS dictation, command voice activation where supported, screen-reader editing, IME coexistence and RTL behavior with the extension both enabled and disabled. Every required case has a target-runtime observation or tested virtual equivalent under verification.md; prepared transcripts and accessibility-tree/action checks may cover unavailable hardware-only observations. Desktop WebKit and metadata validation alone do not establish the target-platform matrix.

Implementation:

- [ ] AIN-1.10-I1 Create and execute the bounded manual protocol with non-sensitive text, exact OS/browser/device/locale/input-service/assistive-tool versions and separate mandatory/optional cells. Exercise selection/correction/replacement, command discovery, focus/status, permission/cancel, remote target deletion and disposal. Preserve failures and network/locality limitations; require a controller split if the selected matrix cannot fit one iteration.

Validation:

- [ ] AIN-1.10-V1 `npm run test:browser -- assistive-presenter assistive-dictation`; execute `tests/manual/assistive-input-web.md` on the declared physical devices or target-platform virtual runtimes. Reuse the suites created by AIN-1.2/3 and create the manual protocol/receipt format here. Record automated and physical or virtual platform executed/passed/failed/skipped counts separately. An unavailable required device blocks its qualification; it cannot be relabeled unsupported merely to close the task. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes.

Evidence: Separate progress entry `AIN-1.10` links changed paths, immutable inputs and focused artifacts; retain failed evidence and identify physical or virtual platform versus prepared-fixture results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `AIN-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task AIN-1.11 — Verify capability evidence and portable consumer behavior

- [ ] AIN-1.11 Verify capability evidence and portable consumer behavior.

Purpose: Produce an auditable cross-platform capability statement from behavior and physical or virtual platform receipts.
Context: `scripts/check-assistive-input-capabilities.mjs`; `tests/assistive-input-capabilities.test.mjs`; `fixtures/assistive-input-consumer/`; `../architecture/evidence/assistive-input/`; `../architecture/specs/assistive-input.md`; `../architecture/specs/extension-library.md`.
Dependencies: AIN-1.4, AIN-1.5, AIN-1.6, AIN-1.7, AIN-1.8, AIN-1.9, AIN-1.10.
Session scope: One named boundary, normally 15–45 minutes plus focused validation. If its implementation or required device matrix cannot fit, propose a stable controller-reviewed split before implementation; retain full acceptance.
Acceptance: An independent consumer imports the documented extension surface with prepared transports; extension absence keeps baseline editing available. The capability matrix links immutable implementation/fixture/device evidence for every claimed cell, preserves failures/unsupported/pending states and detects missing, stale or contradictory receipts. No speech quality, spend or provider qualification is inferred.

Implementation:

- [ ] AIN-1.11-I1 Create a packed/local consumer fixture and the bounded evidence validator with malformed/missing/stale-receipt fixtures. Aggregate portable, web, native and terminal behavior/device receipts; record public boundaries, disposal, privacy defaults and explicit limitations. This is qualification only, with no publication or provider deployment.

Validation:

- [ ] AIN-1.11-V1 `node --test tests/assistive-input-capabilities.test.mjs`; `node scripts/check-assistive-input-capabilities.mjs`. Create both checks and the independent consumer in this task. Record consumer behavior counts separately from receipt-validation counts; evidence validation cannot mark missing platform behavior as passed. Whole-track completion requires the declared mandatory cells and every task acceptance, with no hidden failures/skips. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable implementation/profile/fixture revisions and artifact hashes.

Evidence: Separate progress entry `AIN-1.11` links changed paths, immutable inputs and focused artifacts; retain failed evidence and identify physical or virtual platform versus prepared-fixture results.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `AIN-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.
