# Build the Windows native editor SDK

Status: IN_PROGRESS

Qualification amendment (user decision, 2026-10-14): Physical devices, named target-platform simulators/emulators and desktop OS VMs/test hosts are accepted for platform and release qualification under the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms). Missing physical hardware does not block completion. Execute required behavior against the implemented target-platform runtime; document and test virtual equivalents for unavailable hardware-only input/accessibility cases. Record physical versus virtual provenance and measure performance in the tested environment. This supersedes earlier physical-only or manual-only clauses below; it does not complete unchecked tasks or waive implementation, correctness, security or artifact gates.

## Goal and entry conditions

Workspace: `core`. Deliver an embeddable Windows editor using real native controls, the shared Rust model and portable modules. Paths are relative to `core`; planned paths are created by their task. Read [native parity](../specs/native-sdk-parity.md), [client contracts](../specs/client-contracts.md), [extension library](../specs/extension-library.md), and only the active task's context.

Upstream entry gates: `12-client-contracts.md`, `07-extension-modules.md`, `13-change-diffs.md` and `21-extension-library.md` complete at the current revision with passing evidence.
This OS branch runs independently of the other desktop roadmaps. Missing hosts or failed probes on another OS do not block its dependency-ready tasks.


## Execution rules

One parent per iteration, 15–45 minutes plus focused validation. Reuse qualified shared behavior. If a required primitive or boundary is larger, propose a concrete controller split before broad edits. Failed/skipped prerequisites stay unchecked; task counts are not delivery estimates.

Task 1 creates the real dispatcher/bootstrap suite. Later tasks create their named suites before use; unknown suites, missing tooling and zero tests fail. These are planned commands. Tests live in `native/windows/tests/`. Preserve commands, executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and failures in separate progress; source checkmarks are controller-owned.

Use deterministic fixtures and mocked services; no provider calls, live credentials, production writes, WebViews or publication. Target-platform simulator/emulator/VM input and accessibility observations or tested virtual equivalents may satisfy qualification under verification.md; label the tested environment. Roadmap 20 owns actual OS/device/manual qualification; this track delivers implementation/package readiness.

## Epic WIN-1 — Implement the native adapter

### Task WIN-1.1 — Bootstrap the native SDK test host

- [ ] WIN-1.1 Bootstrap the native SDK test host.

Purpose: bootstrap.
Context: `native/windows/` (project/test bootstrap only).
Dependencies: none.
Session scope: 15–45m; split if larger.
Acceptance: Pinned tooling builds a native control and runs a real bootstrap test; missing tools name an exact unblock condition.

Implementation:

- [ ] WIN-1.1-I1 Pin Windows SDK, Windows App SDK/WinUI, MSVC, deployment range and CPU architectures. Create a native C++/WinRT test host and dispatcher with one real bootstrap test; inventory the required build/test tools. Initialize capability.json as unqualified.

Validation:

- [ ] WIN-1.1-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite bootstrap`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.2 — Qualify the native control candidate

- [ ] WIN-1.2 Qualify the native control candidate.

Purpose: toolkit.
Context: `native/windows/probe/`.
Dependencies: WIN-1.1.
Session scope: 15–45m; split if larger.
Acceptance: A native fixture proves composition and editable cell/atom feasibility; unsupported required routes block dependents.

Implementation:

- [ ] WIN-1.2-I1 Probe WinUI RichEditBox and native text services; record selected input/selection hooks and table/atom limitations. Choose real native child controls when needed; this is feasibility, not parity.

Validation:

- [ ] WIN-1.2-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite toolkit`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.3 — Bind session ownership and native disposal

- [ ] WIN-1.3 Bind session ownership and native disposal.

Purpose: session.
Context: `native/windows/src/Editac.Windows/session/`.
Dependencies: WIN-1.1.
Session scope: 15–45m; split if larger.
Acceptance: Open/dispose, failure and cancellation preserve ownership and callback order; disposed views receive no callbacks.

Implementation:

- [ ] WIN-1.3-I1 Bind a reviewed versioned C ABI consumed by C++/WinRT; generated Swift/Kotlin alone is insufficient to the shared session. Use owned buffers, serialized calls and typed failures; reuse roadmap-12 ports.

Validation:

- [ ] WIN-1.3-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite session`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.4 — Project patches and map native selection

- [ ] WIN-1.4 Project patches and map native selection.

Purpose: projection.
Context: `native/windows/src/Editac.Windows/projection/`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: WIN-1.2, WIN-1.3.
Session scope: 15–45m; split if larger.
Acceptance: Incremental patches preserve stable identity and selection across Unicode, bidi text and attachment boundaries. The coordinate/range-mapping portion of NAT-04 covers selection direction and stale target rejection; full protocol sequences stay with the input owner.

Implementation:

- [ ] WIN-1.4-I1 Project shared snapshots/range patches; map native text positions, paragraph terminators, embedded objects and the shared UTF-16 contract. Reuse conversion and anchor contracts; avoid a second semantic model.

Validation:

- [ ] WIN-1.4-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite projection`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.5 — Route committed native text edits

- [ ] WIN-1.5 Route committed native text edits.

Purpose: edits.
Context: `native/windows/src/Editac.Windows/input/`.
Dependencies: WIN-1.4.
Session scope: 15–45m; split if larger.
Acceptance: Insert/delete/replacement each commits once; rejection leaves a consistent projection without recursive input.

Implementation:

- [ ] WIN-1.5-I1 Route native rich-edit input and range-change events through prepared commands. Distinguish native-origin callbacks from applied patches and test rejected edits.

Validation:

- [ ] WIN-1.5-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite edits`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.6 — Integrate composition and OS replacements

- [ ] WIN-1.6 Integrate composition and OS replacements.

Purpose: composition.
Context: `native/windows/src/Editac.Windows/input/`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: WIN-1.5.
Session scope: 15–45m; split if larger.
Acceptance: Commit/cancel, OS replacement and remote overlap preserve text/selection; synthetic input does not qualify actual IMEs. Qualify NAT-04 through deterministic native protocol fixtures; preserve captured targets/composition and supply OS/IME runbooks and preliminary observations for DEL-1.7 physical or virtual platform qualification.

Implementation:

- [ ] WIN-1.6-I1 Integrate native text-service composition, replacement and selection state with the shared overlap policy. Handle supported autocorrect/dictation replacements without committing provisional input twice.

Validation:

- [ ] WIN-1.6-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite composition`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.7 — Route commands, history and read-only state

- [ ] WIN-1.7 Route commands, history and read-only state.

Purpose: commands.
Context: `native/windows/src/Editac.Windows/commands/`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: WIN-1.5, WIN-1.6.
Session scope: 15–45m; split if larger.
Acceptance: Existing native actions honor shared history/capabilities and read-only state; later adapters must use this same mutation gate. NAT-07 command enablement/routing uses the appropriate first-party profile and injected transfer/service ports; unavailable optional services are explicit. Full NAT-10/NAT-11 transfer behavior remains with the clipboard owner, not an entry prerequisite here.

Implementation:

- [ ] WIN-1.7-I1 Route key/menu/touch actions, structural commands and undo/redo through the shared command catalog. Subscribe to enabled state; suppress independent native-history mutation.

Validation:

- [ ] WIN-1.7-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite commands`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.8 — Map portable text styles and lists

- [ ] WIN-1.8 Map portable text styles and lists.

Purpose: styles.
Context: `native/windows/src/Editac.Windows/styles/`.
Dependencies: WIN-1.4, WIN-1.7.
Session scope: 15–45m; split if larger.
Acceptance: The shared mark/block/list corpus retains semantic equality, including links, mixed marks, nesting and checked items.

Implementation:

- [ ] WIN-1.8-I1 Map roadmap-21 descriptors to ITextDocument range formatting and native structural views in one registry. Existing engine commands own edits; use qualified fixtures for standard marks, headings/code/quotes and lists.

Validation:

- [ ] WIN-1.8-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite styles`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.9 — Render native table structure

- [ ] WIN-1.9 Render native table structure.

Purpose: table-projection.
Context: `native/windows/src/Editac.Windows/tables/`.
Dependencies: WIN-1.8.
Session scope: 15–45m; split if larger.
Acceptance: Native table/cell views retain identity under incremental updates; source or image fallback fails required parity.

Implementation:

- [ ] WIN-1.9-I1 Render the bounded shared table through native cell controls. Preserve cell identity and the engine model; defer command wiring to the next task.

Validation:

- [ ] WIN-1.9-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite table-projection`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.10 — Wire table cell editing and navigation

- [ ] WIN-1.10 Wire table cell editing and navigation.

Purpose: table-editing.
Context: `native/windows/src/Editac.Windows/tables/`.
Dependencies: WIN-1.7, WIN-1.9.
Session scope: 15–45m; split if larger.
Acceptance: Cell edits/navigation, supported selections and row/column actions preserve identity through remote updates and undo.

Implementation:

- [ ] WIN-1.10-I1 Connect cell views to shared commands and logical focus transitions. Expose accessible action hooks and enforce the qualified table limits.

Validation:

- [ ] WIN-1.10-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite table-editing`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.11 — Bind native image and reference views

- [ ] WIN-1.11 Bind native image and reference views.

Purpose: attachments.
Context: `native/windows/src/Editac.Windows/attachments/`.
Dependencies: WIN-1.7, WIN-1.8.
Session scope: 15–45m; split if larger.
Acceptance: Images expose alt/error/edit states; references retain IDs/labels. Both reject stale or cancelled host resolutions.

Implementation:

- [ ] WIN-1.11-I1 Bind portable image/reference descriptors to native views and shared asset/resolver policy. Add activation, selection and replacement/removal controls.

Validation:

- [ ] WIN-1.11-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite attachments`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.12 — Expose portable renderer hooks and math capabilities

- [ ] WIN-1.12 Expose portable renderer hooks and math capabilities.

Purpose: extensions.
Context: `native/windows/src/Editac.Windows/extensions/`.
Dependencies: WIN-1.8, WIN-1.11.
Session scope: 15–45m; split if larger.
Acceptance: Custom marks/atoms render, select, edit and dispose; unknown data survives. Math source editing never implies typesetting.

Implementation:

- [ ] WIN-1.12-I1 Expose roadmap-21 native hooks and its bounded math source editor. Record source/typeset capabilities separately; fallback cannot qualify mandatory content.

Validation:

- [ ] WIN-1.12-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite extensions`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.13 — Adapt native clipboard and drop formats

- [ ] WIN-1.13 Adapt native clipboard and drop formats.

Purpose: clipboard.
Context: `native/windows/src/Editac.Windows/clipboard/`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: WIN-1.7, WIN-1.10, WIN-1.11, WIN-1.12.
Session scope: 15–45m; split if larger.
Acceptance: Rich copy/cut/paste preserves supported structure; hostile data is diagnosed, while read-only/cancelled drops cannot mutate. NAT-10/NAT-11 adds multiple views, delayed providers, cross-app copy/move and source preservation under the shared transfer contract; qualify platform clipboard lifetime.

Implementation:

- [ ] WIN-1.13-I1 Connect native clipboard/drop formats to shared codecs, validation and asset policy. Preserve format precedence, plain text and one history operation; reuse sanitization.

Validation:

- [ ] WIN-1.13-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite clipboard`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.14 — Connect durable sessions to app lifecycle

- [ ] WIN-1.14 Connect durable sessions to app lifecycle.

Purpose: durability.
Context: `native/windows/src/Editac.Windows/storage/`.
Dependencies: WIN-1.3, WIN-1.7.
Session scope: 15–45m; split if larger.
Acceptance: Offline edit/restore needs no account; commit status follows durable receipts. Close/reopen and storage errors preserve recovery.

Implementation:

- [ ] WIN-1.14-I1 Bind qualified LocalStore and native lifecycle notifications to the shared session. Surface pending/committed/error states; reuse journal/checkpoint/outbox logic.

Validation:

- [ ] WIN-1.14-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite durability`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.15 — Bind collaboration and reconnect state

- [ ] WIN-1.15 Bind collaboration and reconnect state.

Purpose: collaboration.
Context: `native/windows/src/Editac.Windows/transport/`.
Dependencies: WIN-1.6, WIN-1.14.
Session scope: 15–45m; split if larger.
Acceptance: Two fixtures converge across reconnect; remote selection, revocation and document switching preserve receipt/input semantics.

Implementation:

- [ ] WIN-1.15-I1 Bind host-injected Transport/Authorization and presence to native UI state. Reuse qualified sync logic; exercise cancellation and remote composition overlap with mocks.

Validation:

- [ ] WIN-1.15-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite collaboration`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.16 — Expose accessible text and editor actions

- [ ] WIN-1.16 Expose accessible text and editor actions.

Purpose: accessibility-text.
Context: `native/windows/src/Editac.Windows/accessibility/`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: WIN-1.6, WIN-1.7, WIN-1.8.
Session scope: 15–45m; split if larger.
Acceptance: Native accessibility exposes text, selection, command/read-only state and keyboard focus at declared scaling settings. NAT-13/NAT-14 checks current accessible text geometry and safe text-service lock/reentrancy behavior; record actual platform evidence.

Implementation:

- [ ] WIN-1.16-I1 Expose native text/actions for Narrator. Programmatically check labels and selection; preserve OS input. Actual screen-reader qualification belongs to roadmap 20.

Validation:

- [ ] WIN-1.16-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite accessibility-text`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.17 — Expose accessible tables and attachments

- [ ] WIN-1.17 Expose accessible tables and attachments.

Purpose: accessibility-structure.
Context: `native/windows/src/Editac.Windows/accessibility/`.
Dependencies: WIN-1.10, WIN-1.11, WIN-1.12, WIN-1.16.
Session scope: 15–45m; split if larger.
Acceptance: Tables/cells, alt text, reference labels and atom actions have accessible relationships and a pointer-free focus route.

Implementation:

- [ ] WIN-1.17-I1 Add native structure/actions for tables and attachments using shared labels and capabilities; test focus transitions and bounded announcements.

Validation:

- [ ] WIN-1.17-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite accessibility-structure`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-1.18 — Present native change and revision views

- [ ] WIN-1.18 Present native change and revision views.

Purpose: change-review.
Context: `native/windows/src/Editac.Windows/change-review/`.
Dependencies: WIN-1.10, WIN-1.11, WIN-1.16, WIN-1.17.
Session scope: 15–45m; split if larger.
Acceptance: Read-only unified/semantic changes retain profile labels and trusted/unknown attribution; stale revisions remain visible.

Implementation:

- [ ] WIN-1.18-I1 Render roadmap-13 changes in accessible native views with range navigation. Reuse its algorithm, revision and attribution contracts; never rewind the live replica.

Validation:

- [ ] WIN-1.18-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite change-review`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

## Epic WIN-2 — Package the adapter and prepare platform qualification

### Task WIN-2.1 — Build the distributable native SDK artifact

- [ ] WIN-2.1 Build the distributable native SDK artifact.

Purpose: package.
Context: `native/windows/packaging/`.
Dependencies: WIN-1.13, WIN-1.14, WIN-1.15, WIN-1.17, WIN-1.18.
Session scope: 15–45m; split if larger.
Acceptance: The package contains supported binaries, API/version metadata, resources and notices, with immutable hashes and no publication.

Implementation:

- [ ] WIN-2.1-I1 Build a native Windows SDK package with declared headers/ABI, runtime dependencies and architecture artifacts. Pin runtime/generator compatibility, check contents via the pinned MSBuild/native test runner, and record OS/CPU support. Signing/publication are separate release actions.

Validation:

- [ ] WIN-2.1-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite package`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-2.2 — Verify a clean native consumer

- [ ] WIN-2.2 Verify a clean native consumer.

Purpose: consumer.
Context: `native/windows/consumer/`.
Dependencies: WIN-2.1.
Session scope: 15–45m; split if larger.
Acceptance: A clean consumer needs no sibling checkout and runs actual local/rich/offline/mocked-collaboration and change-review smoke cases.

Implementation:

- [ ] WIN-2.2-I1 Build a native sample against the immutable packed SDK; test install/open/edit/review/dispose and reject missing resources. Keep every mandatory feature discoverable.

Validation:

- [ ] WIN-2.2-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite consumer`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task WIN-2.4 — Add simulator or OS-host clipboard format regressions

- [ ] WIN-2.4 Add simulator or OS-host clipboard format regressions.

Purpose: Deliver the named transfer boundary with reproducible evidence and explicit qualification status.
Context: `native/`; [native clipboard cases](../tests/native-clipboard-cases.md); `../architecture/specs/native-sdk-parity.md`
Dependencies: WIN-1.13, WIN-1.16, WIN-2.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. These are future tasks; this roadmap revision does not execute native tests or authorize device runs.
Acceptance: Windows test host/VM runs NCL-01–NCL-20 against the installed native control and OS clipboard, with declared unsupported OS features. Exercise actual menu/shortcut APIs, rich and literal flavors, formatting, two views/apps, delayed providers, denial, read-only, undo and disposal. Headless/mock transport checks remain separately labeled; emulator/VM success may qualify the virtual platform, including tested IME/accessibility cases or documented virtual equivalents under verification.md; it is not physical-hardware evidence.

Implementation:

- [ ] WIN-2.4-I1 Create the named dispatcher suite and deterministic fixture app on Windows test host/VM. Seed and read the OS pasteboard/clipboard through documented test APIs, record selected virtual device/OS image and native SDK package hash, and author a step-by-step physical-device handoff for NCL-21–NCL-28. Include platform plain-paste shortcuts and reachable touch commands; do not run this future task during roadmap editing.

Validation:

- [ ] WIN-2.4-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite clipboard-host`. Record virtual versus physical provenance and each unsupported/failed clipboard flavor. Require nonzero matching cases and record executed/passed/failed/skipped counts, immutable fixture/source/package revisions and preserved failures. Missing required runtime tooling, failed behavior or untested mandatory cases do not qualify support; use accepted virtual runtimes/equivalents when physical hardware is unavailable.

Evidence: Separate progress entry with commands, exact environment and artifact hashes; catalogs remain planned until the corresponding runs exist.
Handoff: Last completed substep, unavailable environment or failing case, owner and next bounded action.
Blocked behavior: Leave unchecked; name owner, unblock condition and retry trigger. Accept target-platform simulators/emulators/VMs under verification.md and retain virtual provenance; never relabel their results as physical-device observations.

### Task WIN-2.3 — Hand off exact platform qualification inputs

- [ ] WIN-2.3 Hand off exact platform qualification inputs.

Purpose: qualification-readiness.
Context: `native/windows/qualification/`; `native/windows/capability.json`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: WIN-2.2, WIN-2.4.
Session scope: 15–45m; split if larger.
Acceptance: Every mandatory capability links implemented tests/artifacts; platform IME, accessibility and OS-support claims await roadmap 20, which accepts physical or virtual qualification. Hand off the owned NAT/SEL/MOV/CMD fixtures, PRF-07 device runbooks and any preliminary observations with unqualified status. DEL-1.7 owns mandatory physical or virtual platform/IME/performance qualification; this readiness handoff cannot claim support from synthetic or unmeasured inputs. Include NCL simulator/host receipts and an unchecked physical or virtual platform transfer matrix; DEL-1.9 and DEL-1.10 own the physical or virtual platform qualification runs.

Implementation:

- [ ] WIN-2.3-I1 Prepare the Windows runbook and fixture manifest for roadmap 20, including Narrator, tool/device/IME versions and failure counts. Validate links and qualification states.

Validation:

- [ ] WIN-2.3-V1 `powershell -NoProfile -File native/windows/scripts/check.ps1 -Suite qualification-readiness`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.
