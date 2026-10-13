# Build the iOS native editor SDK

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core`. Deliver an embeddable iOS editor using real native controls, the shared Rust model and portable modules. Paths are relative to `core`; planned paths are created by their task. Read [native parity](../specs/native-sdk-parity.md), [client contracts](../specs/client-contracts.md), [extension library](../specs/extension-library.md), and only the active task's context.

Upstream entry gates: `12-client-contracts.md`, `07-extension-modules.md`, `13-change-diffs.md` and `21-extension-library.md` complete at the current revision with passing evidence.

Platform preparation gate from [roadmap 09](09-native-preparation.md): `NAT-1.1` (portable engine entry), `NAT-1.2` (bounded native bindings), `NAT-1.3` (Swift headless round-trip host) and `NAT-1.5` (iOS text-control patch) must have passing evidence for the consumed engine/binding revisions. Read those task records and their individual artifacts. Completion of the whole preparation roadmap, joined follow-up `NAT-1.7`, and Android tasks are not prerequisites.

## Execution rules

One parent per iteration, 15–45 minutes plus focused validation. Reuse qualified shared behavior. If a required primitive or boundary is larger, propose a concrete controller split before broad edits. Failed/skipped prerequisites stay unchecked; task counts are not delivery estimates.

Task 1 creates the real dispatcher/bootstrap suite. Later tasks create their named suites before use; unknown suites, missing tooling and zero tests fail. These are planned commands. Tests live in `native/ios/tests/`. Preserve commands, executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and failures in separate progress; source checkmarks are controller-owned.

Use deterministic fixtures and mocked services; no provider calls, live credentials, production writes, WebViews or publication. Simulations cannot qualify real IMEs/accessibility. Roadmap 20 owns actual OS/device/manual qualification; this track delivers implementation/package readiness.

## Epic IOS-1 — Implement the native adapter

### Task IOS-1.1 — Bootstrap the native SDK test host

- [ ] IOS-1.1 Bootstrap the native SDK test host.

Purpose: bootstrap.
Context: `native/ios/` (project/test bootstrap only); [roadmap 09](09-native-preparation.md) task records and individual artifacts for `NAT-1.1`, `NAT-1.2`, `NAT-1.3`, `NAT-1.5`.
Dependencies: none.
Session scope: 15–45m; split if larger.
Acceptance: The four named preparation tasks have passing fixture/build evidence matching the consumed engine/binding revisions. Pinned tooling builds a native control and runs a real bootstrap test; missing evidence/tools name an exact unblock condition.

Implementation:

- [ ] IOS-1.1-I1 Verify the four preparation records and artifact revisions, without requiring Android or the joined follow-up. Pin Xcode, Swift, iOS SDK, deployment range and supported device/simulator slices. Create a Swift SDK target, native test host and dispatcher with one real XCTest bootstrap case. Initialize capability.json as unqualified.

Validation:

- [ ] IOS-1.1-V1 `bash native/ios/scripts/check.sh bootstrap`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.2 — Qualify the native control candidate

- [ ] IOS-1.2 Qualify the native control candidate.

Purpose: toolkit.
Context: `native/ios/probe/`.
Dependencies: IOS-1.1.
Session scope: 15–45m; split if larger.
Acceptance: A native fixture proves composition and editable cell/atom feasibility; unsupported required routes block dependents.

Implementation:

- [ ] IOS-1.2-I1 Probe UIKit UITextView/TextKit with native cell/attachment views; record selected input/selection hooks and table/atom limitations. Choose real native child controls when needed; this is feasibility, not parity.

Validation:

- [ ] IOS-1.2-V1 `bash native/ios/scripts/check.sh toolkit`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.3 — Bind session ownership and native disposal

- [ ] IOS-1.3 Bind session ownership and native disposal.

Purpose: session.
Context: `native/ios/Sources/EditacIOS/session/`.
Dependencies: IOS-1.1.
Session scope: 15–45m; split if larger.
Acceptance: Open/dispose, failure and cancellation preserve ownership and callback order; disposed views receive no callbacks.

Implementation:

- [ ] IOS-1.3-I1 Bind the qualified UniFFI Swift interface to the shared session. Use owned buffers, serialized calls and typed failures; reuse roadmap-12 ports.

Validation:

- [ ] IOS-1.3-V1 `bash native/ios/scripts/check.sh session`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.4 — Project patches and map native selection

- [ ] IOS-1.4 Project patches and map native selection.

Purpose: projection.
Context: `native/ios/Sources/EditacIOS/projection/`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: IOS-1.2, IOS-1.3.
Session scope: 15–45m; split if larger.
Acceptance: Incremental patches preserve stable identity and selection across Unicode, bidi text and attachment boundaries. The coordinate/range-mapping portion of NAT-05 covers selection direction and stale target rejection; full protocol sequences stay with the input owner.

Implementation:

- [ ] IOS-1.4-I1 Project shared snapshots/range patches; map NSRange/UITextRange and UTF-16, including surrogate pairs. Reuse conversion and anchor contracts; avoid a second semantic model.

Validation:

- [ ] IOS-1.4-V1 `bash native/ios/scripts/check.sh projection`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.5 — Route committed native text edits

- [ ] IOS-1.5 Route committed native text edits.

Purpose: edits.
Context: `native/ios/Sources/EditacIOS/input/`.
Dependencies: IOS-1.4.
Session scope: 15–45m; split if larger.
Acceptance: Insert/delete/replacement each commits once; rejection leaves a consistent projection without recursive input.

Implementation:

- [ ] IOS-1.5-I1 Route UITextView input/delegate hooks through prepared commands. Distinguish native-origin callbacks from applied patches and test rejected edits.

Validation:

- [ ] IOS-1.5-V1 `bash native/ios/scripts/check.sh edits`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.6 — Integrate composition and OS replacements

- [ ] IOS-1.6 Integrate composition and OS replacements.

Purpose: composition.
Context: `native/ios/Sources/EditacIOS/input/`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: IOS-1.5.
Session scope: 15–45m; split if larger.
Acceptance: Commit/cancel, OS replacement and remote overlap preserve text/selection; synthetic input does not qualify actual IMEs. Qualify NAT-05 through deterministic native protocol fixtures; preserve captured targets/composition and supply OS/IME runbooks and preliminary observations for DEL-1.7 actual-device qualification.

Implementation:

- [ ] IOS-1.6-I1 Integrate markedTextRange and selectedTextRange with the shared overlap policy. Handle supported autocorrect/dictation replacements without committing provisional input twice.

Validation:

- [ ] IOS-1.6-V1 `bash native/ios/scripts/check.sh composition`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.7 — Route commands, history and read-only state

- [ ] IOS-1.7 Route commands, history and read-only state.

Purpose: commands.
Context: `native/ios/Sources/EditacIOS/commands/`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: IOS-1.5, IOS-1.6.
Session scope: 15–45m; split if larger.
Acceptance: Existing native actions honor shared history/capabilities and read-only state; later adapters must use this same mutation gate. NAT-07 command enablement/routing uses the appropriate first-party profile and injected transfer/service ports; unavailable optional services are explicit. Full NAT-10/NAT-11 transfer behavior remains with the clipboard owner, not an entry prerequisite here.

Implementation:

- [ ] IOS-1.7-I1 Route key/menu/touch actions, structural commands and undo/redo through the shared command catalog. Subscribe to enabled state; suppress independent native-history mutation.

Validation:

- [ ] IOS-1.7-V1 `bash native/ios/scripts/check.sh commands`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.8 — Map portable text styles and lists

- [ ] IOS-1.8 Map portable text styles and lists.

Purpose: styles.
Context: `native/ios/Sources/EditacIOS/styles/`.
Dependencies: IOS-1.4, IOS-1.7.
Session scope: 15–45m; split if larger.
Acceptance: The shared mark/block/list corpus retains semantic equality, including links, mixed marks, nesting and checked items.

Implementation:

- [ ] IOS-1.8-I1 Map roadmap-21 descriptors to attributed text and native paragraph/list projections in one registry. Existing engine commands own edits; use qualified fixtures for standard marks, headings/code/quotes and lists.

Validation:

- [ ] IOS-1.8-V1 `bash native/ios/scripts/check.sh styles`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.9 — Render native table structure

- [ ] IOS-1.9 Render native table structure.

Purpose: table-projection.
Context: `native/ios/Sources/EditacIOS/tables/`.
Dependencies: IOS-1.8.
Session scope: 15–45m; split if larger.
Acceptance: Native table/cell views retain identity under incremental updates; source or image fallback fails required parity.

Implementation:

- [ ] IOS-1.9-I1 Render the bounded shared table through native cell controls. Preserve cell identity and the engine model; defer command wiring to the next task.

Validation:

- [ ] IOS-1.9-V1 `bash native/ios/scripts/check.sh table-projection`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.10 — Wire table cell editing and navigation

- [ ] IOS-1.10 Wire table cell editing and navigation.

Purpose: table-editing.
Context: `native/ios/Sources/EditacIOS/tables/`.
Dependencies: IOS-1.7, IOS-1.9.
Session scope: 15–45m; split if larger.
Acceptance: Cell edits/navigation, supported selections and row/column actions preserve identity through remote updates and undo.

Implementation:

- [ ] IOS-1.10-I1 Connect cell views to shared commands and logical focus transitions. Expose accessible action hooks and enforce the qualified table limits.

Validation:

- [ ] IOS-1.10-V1 `bash native/ios/scripts/check.sh table-editing`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.11 — Bind native image and reference views

- [ ] IOS-1.11 Bind native image and reference views.

Purpose: attachments.
Context: `native/ios/Sources/EditacIOS/attachments/`.
Dependencies: IOS-1.7, IOS-1.8.
Session scope: 15–45m; split if larger.
Acceptance: Images expose alt/error/edit states; references retain IDs/labels. Both reject stale or cancelled host resolutions.

Implementation:

- [ ] IOS-1.11-I1 Bind portable image/reference descriptors to native views and shared asset/resolver policy. Add activation, selection and replacement/removal controls.

Validation:

- [ ] IOS-1.11-V1 `bash native/ios/scripts/check.sh attachments`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.12 — Expose portable renderer hooks and math capabilities

- [ ] IOS-1.12 Expose portable renderer hooks and math capabilities.

Purpose: extensions.
Context: `native/ios/Sources/EditacIOS/extensions/`.
Dependencies: IOS-1.8, IOS-1.11.
Session scope: 15–45m; split if larger.
Acceptance: Custom marks/atoms render, select, edit and dispose; unknown data survives. Math source editing never implies typesetting.

Implementation:

- [ ] IOS-1.12-I1 Expose roadmap-21 native hooks and its bounded math source editor. Record source/typeset capabilities separately; fallback cannot qualify mandatory content.

Validation:

- [ ] IOS-1.12-V1 `bash native/ios/scripts/check.sh extensions`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.13 — Adapt native clipboard and drop formats

- [ ] IOS-1.13 Adapt native clipboard and drop formats.

Purpose: clipboard.
Context: `native/ios/Sources/EditacIOS/clipboard/`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: IOS-1.7, IOS-1.10, IOS-1.11, IOS-1.12.
Session scope: 15–45m; split if larger.
Acceptance: Rich copy/cut/paste preserves supported structure; hostile data is diagnosed, while read-only/cancelled drops cannot mutate. NAT-10/NAT-11 adds multiple views, delayed providers, cross-app copy/move and source preservation under the shared transfer contract; qualify platform clipboard lifetime.

Implementation:

- [ ] IOS-1.13-I1 Connect native clipboard/drop formats to shared codecs, validation and asset policy. Preserve format precedence, plain text and one history operation; reuse sanitization.

Validation:

- [ ] IOS-1.13-V1 `bash native/ios/scripts/check.sh clipboard`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.14 — Connect durable sessions to app lifecycle

- [ ] IOS-1.14 Connect durable sessions to app lifecycle.

Purpose: durability.
Context: `native/ios/Sources/EditacIOS/storage/`.
Dependencies: IOS-1.3, IOS-1.7.
Session scope: 15–45m; split if larger.
Acceptance: Offline edit/restore needs no account; commit status follows durable receipts. Close/reopen and storage errors preserve recovery.

Implementation:

- [ ] IOS-1.14-I1 Bind qualified LocalStore and native lifecycle notifications to the shared session. Surface pending/committed/error states; reuse journal/checkpoint/outbox logic.

Validation:

- [ ] IOS-1.14-V1 `bash native/ios/scripts/check.sh durability`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.15 — Bind collaboration and reconnect state

- [ ] IOS-1.15 Bind collaboration and reconnect state.

Purpose: collaboration.
Context: `native/ios/Sources/EditacIOS/transport/`.
Dependencies: IOS-1.6, IOS-1.14.
Session scope: 15–45m; split if larger.
Acceptance: Two fixtures converge across reconnect; remote selection, revocation and document switching preserve receipt/input semantics.

Implementation:

- [ ] IOS-1.15-I1 Bind host-injected Transport/Authorization and presence to native UI state. Reuse qualified sync logic; exercise cancellation and remote composition overlap with mocks.

Validation:

- [ ] IOS-1.15-V1 `bash native/ios/scripts/check.sh collaboration`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.16 — Expose accessible text and editor actions

- [ ] IOS-1.16 Expose accessible text and editor actions.

Purpose: accessibility-text.
Context: `native/ios/Sources/EditacIOS/accessibility/`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: IOS-1.6, IOS-1.7, IOS-1.8.
Session scope: 15–45m; split if larger.
Acceptance: Native accessibility exposes text, selection, command/read-only state and keyboard focus at declared scaling settings. NAT-13/NAT-14 checks current accessible text geometry and safe text-service lock/reentrancy behavior; record actual platform evidence.

Implementation:

- [ ] IOS-1.16-I1 Expose native text/actions for VoiceOver. Programmatically check labels and selection; preserve OS input. Actual screen-reader qualification belongs to roadmap 20.

Validation:

- [ ] IOS-1.16-V1 `bash native/ios/scripts/check.sh accessibility-text`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.17 — Expose accessible tables and attachments

- [ ] IOS-1.17 Expose accessible tables and attachments.

Purpose: accessibility-structure.
Context: `native/ios/Sources/EditacIOS/accessibility/`.
Dependencies: IOS-1.10, IOS-1.11, IOS-1.12, IOS-1.16.
Session scope: 15–45m; split if larger.
Acceptance: Tables/cells, alt text, reference labels and atom actions have accessible relationships and a pointer-free focus route.

Implementation:

- [ ] IOS-1.17-I1 Add native structure/actions for tables and attachments using shared labels and capabilities; test focus transitions and bounded announcements.

Validation:

- [ ] IOS-1.17-V1 `bash native/ios/scripts/check.sh accessibility-structure`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-1.18 — Present native change and revision views

- [ ] IOS-1.18 Present native change and revision views.

Purpose: change-review.
Context: `native/ios/Sources/EditacIOS/change-review/`.
Dependencies: IOS-1.10, IOS-1.11, IOS-1.16, IOS-1.17.
Session scope: 15–45m; split if larger.
Acceptance: Read-only unified/semantic changes retain profile labels and trusted/unknown attribution; stale revisions remain visible.

Implementation:

- [ ] IOS-1.18-I1 Render roadmap-13 changes in accessible native views with range navigation. Reuse its algorithm, revision and attribution contracts; never rewind the live replica.

Validation:

- [ ] IOS-1.18-V1 `bash native/ios/scripts/check.sh change-review`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

## Epic IOS-2 — Package the adapter and prepare platform qualification

### Task IOS-2.1 — Build the distributable native SDK artifact

- [ ] IOS-2.1 Build the distributable native SDK artifact.

Purpose: package.
Context: `native/ios/packaging/`.
Dependencies: IOS-1.13, IOS-1.14, IOS-1.15, IOS-1.17, IOS-1.18.
Session scope: 15–45m; split if larger.
Acceptance: The package contains supported binaries, API/version metadata, resources and notices, with immutable hashes and no publication.

Implementation:

- [ ] IOS-2.1-I1 Build a Swift package and declared XCFramework slices. Pin runtime/generator compatibility, check contents via xcodebuild, and record OS/CPU support. Signing/publication are separate release actions.

Validation:

- [ ] IOS-2.1-V1 `bash native/ios/scripts/check.sh package`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-2.2 — Verify a clean native consumer

- [ ] IOS-2.2 Verify a clean native consumer.

Purpose: consumer.
Context: `native/ios/consumer/`.
Dependencies: IOS-2.1.
Session scope: 15–45m; split if larger.
Acceptance: A clean consumer needs no sibling checkout and runs actual local/rich/offline/mocked-collaboration and change-review smoke cases.

Implementation:

- [ ] IOS-2.2-I1 Build a native sample against the immutable packed SDK; test install/open/edit/review/dispose and reject missing resources. Keep every mandatory feature discoverable.

Validation:

- [ ] IOS-2.2-V1 `bash native/ios/scripts/check.sh consumer`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task IOS-2.4 — Add simulator or OS-host clipboard format regressions

- [ ] IOS-2.4 Add simulator or OS-host clipboard format regressions.

Purpose: Deliver the named transfer boundary with reproducible evidence and explicit qualification status.
Context: `native/`; [native clipboard cases](../tests/native-clipboard-cases.md); `../architecture/specs/native-sdk-parity.md`
Dependencies: IOS-1.13, IOS-1.16, IOS-2.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. These are future tasks; this roadmap revision does not execute native tests or authorize device runs.
Acceptance: iOS/iPadOS Simulator runs NCL-01–NCL-20 against the installed native control and OS clipboard, with declared unsupported OS features. Exercise actual menu/shortcut APIs, rich and literal flavors, formatting, two views/apps, delayed providers, denial, read-only, undo and disposal. Headless/mock transport checks remain separately labeled; emulator/VM success is not real-device, IME or accessibility qualification.

Implementation:

- [ ] IOS-2.4-I1 Create the named dispatcher suite and deterministic fixture app on iOS/iPadOS Simulator. Seed and read the OS pasteboard/clipboard through documented test APIs, record selected virtual device/OS image and native SDK package hash, and author a step-by-step physical-device handoff for NCL-21–NCL-28. Include platform plain-paste shortcuts and reachable touch commands; do not run this future task during roadmap editing.

Validation:

- [ ] IOS-2.4-V1 `bash native/ios/scripts/check.sh clipboard-simulator`. Record virtual versus physical provenance and each unsupported/failed clipboard flavor. Require nonzero matching cases and record executed/passed/failed/skipped counts, immutable fixture/source/package revisions and preserved failures. Missing tools/devices or skipped mandatory cases do not qualify support.

Evidence: Separate progress entry with commands, exact environment and artifact hashes; catalogs remain planned until the corresponding runs exist.
Handoff: Last completed substep, unavailable environment or failing case, owner and next bounded action.
Blocked behavior: Leave unchecked; name owner, unblock condition and retry trigger. Never substitute simulation for physical-device evidence.

### Task IOS-2.3 — Hand off exact platform qualification inputs

- [ ] IOS-2.3 Hand off exact platform qualification inputs.

Purpose: qualification-readiness.
Context: `native/ios/qualification/`; `native/ios/capability.json`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: IOS-2.2, IOS-2.4.
Session scope: 15–45m; split if larger.
Acceptance: Every mandatory capability links implemented tests/artifacts; real device, IME, accessibility and OS-support claims await roadmap 20. Hand off the owned NAT/SEL/MOV/CMD fixtures, PRF-07 device runbooks and any preliminary observations with unqualified status. DEL-1.7 owns mandatory actual-device/IME/performance qualification; this readiness handoff cannot claim support from synthetic or unmeasured inputs. Include NCL simulator/host receipts and an unchecked physical-device transfer matrix; DEL-1.9 and DEL-1.10 own the actual hardware runs.

Implementation:

- [ ] IOS-2.3-I1 Prepare the iOS runbook and fixture manifest for roadmap 20, including VoiceOver, tool/device/IME versions and failure counts. Validate links and qualification states.

Validation:

- [ ] IOS-2.3-V1 `bash native/ios/scripts/check.sh qualification-readiness`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.
