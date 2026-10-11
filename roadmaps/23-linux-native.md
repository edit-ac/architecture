# Build the Linux native editor SDK

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core`. Deliver an embeddable Linux editor using real native controls, the shared Rust model and portable modules. Paths are relative to `core`; planned paths are created by their task. Read [native parity](../specs/native-sdk-parity.md), [client contracts](../specs/client-contracts.md), [extension library](../specs/extension-library.md), and only the active task's context.

Upstream entry gates: `12-client-contracts.md`, `07-extension-modules.md`, `13-change-diffs.md` and `21-extension-library.md` complete at the current revision with passing evidence.
This OS branch runs independently of the other desktop roadmaps. Missing hosts or failed probes on another OS do not block its dependency-ready tasks.


## Execution rules

One parent per iteration, 15–45 minutes plus focused validation. Reuse qualified shared behavior. If a required primitive or boundary is larger, propose a concrete controller split before broad edits. Failed/skipped prerequisites stay unchecked; task counts are not delivery estimates.

Task 1 creates the real dispatcher/bootstrap suite. Later tasks create their named suites before use; unknown suites, missing tooling and zero tests fail. These are planned commands. Tests live in `native/linux/tests/`. Preserve commands, executed/passed/failed/skipped counts, revisions, fixture/artifact hashes and failures in separate progress; source checkmarks are controller-owned.

Use deterministic fixtures and mocked services; no provider calls, live credentials, production writes, WebViews or publication. Simulations cannot qualify real IMEs/accessibility. Roadmap 20 owns actual OS/device/manual qualification; this track delivers implementation/package readiness.

## Epic LNX-1 — Implement the native adapter

### Task LNX-1.1 — Bootstrap the native SDK test host

- [ ] LNX-1.1 Bootstrap the native SDK test host.

Purpose: bootstrap.
Context: `native/linux/` (project/test bootstrap only).
Dependencies: none.
Session scope: 15–45m; split if larger.
Acceptance: Pinned tooling builds a native control and runs a real bootstrap test; missing tools name an exact unblock condition.

Implementation:

- [ ] LNX-1.1-I1 Pin Rust, GTK4 and system-library baseline plus supported distribution/display backend. Create a native GTK test host and dispatcher with one real display-backed bootstrap test; keep GTK dependencies outside web builds. Initialize capability.json as unqualified.

Validation:

- [ ] LNX-1.1-V1 `bash native/linux/scripts/check.sh bootstrap`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.2 — Qualify the native control candidate

- [ ] LNX-1.2 Qualify the native control candidate.

Purpose: toolkit.
Context: `native/linux/probe/`.
Dependencies: LNX-1.1.
Session scope: 15–45m; split if larger.
Acceptance: A native fixture proves composition and editable cell/atom feasibility; unsupported required routes block dependents.

Implementation:

- [ ] LNX-1.2-I1 Probe GTK4 TextView/TextBuffer with tags and child anchors; record selected input/selection hooks and table/atom limitations. Choose real native child controls when needed; this is feasibility, not parity.

Validation:

- [ ] LNX-1.2-V1 `bash native/linux/scripts/check.sh toolkit`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.3 — Bind session ownership and native disposal

- [ ] LNX-1.3 Bind session ownership and native disposal.

Purpose: session.
Context: `native/linux/src/session/`.
Dependencies: LNX-1.1.
Session scope: 15–45m; split if larger.
Acceptance: Open/dispose, failure and cancellation preserve ownership and callback order; disposed views receive no callbacks.

Implementation:

- [ ] LNX-1.3-I1 Bind the qualified Rust session API on the GTK main-context boundary to the shared session. Use owned buffers, serialized calls and typed failures; reuse roadmap-12 ports.

Validation:

- [ ] LNX-1.3-V1 `bash native/linux/scripts/check.sh session`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.4 — Project patches and map native selection

- [ ] LNX-1.4 Project patches and map native selection.

Purpose: projection.
Context: `native/linux/src/projection/`.
Dependencies: LNX-1.2, LNX-1.3.
Session scope: 15–45m; split if larger.
Acceptance: Incremental patches preserve stable identity and selection across Unicode, bidi text and attachment boundaries.

Implementation:

- [ ] LNX-1.4-I1 Project shared snapshots/range patches; map GTK character offsets and iterators converted to shared UTF-16 units. Reuse conversion and anchor contracts; avoid a second semantic model.

Validation:

- [ ] LNX-1.4-V1 `bash native/linux/scripts/check.sh projection`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.5 — Route committed native text edits

- [ ] LNX-1.5 Route committed native text edits.

Purpose: edits.
Context: `native/linux/src/input/`.
Dependencies: LNX-1.4.
Session scope: 15–45m; split if larger.
Acceptance: Insert/delete/replacement each commits once; rejection leaves a consistent projection without recursive input.

Implementation:

- [ ] LNX-1.5-I1 Route TextBuffer insert/delete and native input signals through prepared commands. Distinguish native-origin callbacks from applied patches and test rejected edits.

Validation:

- [ ] LNX-1.5-V1 `bash native/linux/scripts/check.sh edits`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.6 — Integrate composition and OS replacements

- [ ] LNX-1.6 Integrate composition and OS replacements.

Purpose: composition.
Context: `native/linux/src/input/`.
Dependencies: LNX-1.5.
Session scope: 15–45m; split if larger.
Acceptance: Commit/cancel, OS replacement and remote overlap preserve text/selection; synthetic input does not qualify actual IMEs.

Implementation:

- [ ] LNX-1.6-I1 Integrate GTK input-method preedit, committed text and selection state with the shared overlap policy. Handle supported autocorrect/dictation replacements without committing provisional input twice.

Validation:

- [ ] LNX-1.6-V1 `bash native/linux/scripts/check.sh composition`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.7 — Route commands, history and read-only state

- [ ] LNX-1.7 Route commands, history and read-only state.

Purpose: commands.
Context: `native/linux/src/commands/`.
Dependencies: LNX-1.5, LNX-1.6.
Session scope: 15–45m; split if larger.
Acceptance: Existing native actions honor shared history/capabilities and read-only state; later adapters must use this same mutation gate.

Implementation:

- [ ] LNX-1.7-I1 Route key/menu/touch actions, structural commands and undo/redo through the shared command catalog. Subscribe to enabled state; suppress independent native-history mutation.

Validation:

- [ ] LNX-1.7-V1 `bash native/linux/scripts/check.sh commands`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.8 — Map portable text styles and lists

- [ ] LNX-1.8 Map portable text styles and lists.

Purpose: styles.
Context: `native/linux/src/styles/`.
Dependencies: LNX-1.4, LNX-1.7.
Session scope: 15–45m; split if larger.
Acceptance: The shared mark/block/list corpus retains semantic equality, including links, mixed marks, nesting and checked items.

Implementation:

- [ ] LNX-1.8-I1 Map roadmap-21 descriptors to GTK text tags and native structural child views in one registry. Existing engine commands own edits; use qualified fixtures for standard marks, headings/code/quotes and lists.

Validation:

- [ ] LNX-1.8-V1 `bash native/linux/scripts/check.sh styles`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.9 — Render native table structure

- [ ] LNX-1.9 Render native table structure.

Purpose: table-projection.
Context: `native/linux/src/tables/`.
Dependencies: LNX-1.8.
Session scope: 15–45m; split if larger.
Acceptance: Native table/cell views retain identity under incremental updates; source or image fallback fails required parity.

Implementation:

- [ ] LNX-1.9-I1 Render the bounded shared table through native cell controls. Preserve cell identity and the engine model; defer command wiring to the next task.

Validation:

- [ ] LNX-1.9-V1 `bash native/linux/scripts/check.sh table-projection`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.10 — Wire table cell editing and navigation

- [ ] LNX-1.10 Wire table cell editing and navigation.

Purpose: table-editing.
Context: `native/linux/src/tables/`.
Dependencies: LNX-1.7, LNX-1.9.
Session scope: 15–45m; split if larger.
Acceptance: Cell edits/navigation, supported selections and row/column actions preserve identity through remote updates and undo.

Implementation:

- [ ] LNX-1.10-I1 Connect cell views to shared commands and logical focus transitions. Expose accessible action hooks and enforce the qualified table limits.

Validation:

- [ ] LNX-1.10-V1 `bash native/linux/scripts/check.sh table-editing`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.11 — Bind native image and reference views

- [ ] LNX-1.11 Bind native image and reference views.

Purpose: attachments.
Context: `native/linux/src/attachments/`.
Dependencies: LNX-1.7, LNX-1.8.
Session scope: 15–45m; split if larger.
Acceptance: Images expose alt/error/edit states; references retain IDs/labels. Both reject stale or cancelled host resolutions.

Implementation:

- [ ] LNX-1.11-I1 Bind portable image/reference descriptors to native views and shared asset/resolver policy. Add activation, selection and replacement/removal controls.

Validation:

- [ ] LNX-1.11-V1 `bash native/linux/scripts/check.sh attachments`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.12 — Expose portable renderer hooks and math capabilities

- [ ] LNX-1.12 Expose portable renderer hooks and math capabilities.

Purpose: extensions.
Context: `native/linux/src/extensions/`.
Dependencies: LNX-1.8, LNX-1.11.
Session scope: 15–45m; split if larger.
Acceptance: Custom marks/atoms render, select, edit and dispose; unknown data survives. Math source editing never implies typesetting.

Implementation:

- [ ] LNX-1.12-I1 Expose roadmap-21 native hooks and its bounded math source editor. Record source/typeset capabilities separately; fallback cannot qualify mandatory content.

Validation:

- [ ] LNX-1.12-V1 `bash native/linux/scripts/check.sh extensions`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.13 — Adapt native clipboard and drop formats

- [ ] LNX-1.13 Adapt native clipboard and drop formats.

Purpose: clipboard.
Context: `native/linux/src/clipboard/`.
Dependencies: LNX-1.7, LNX-1.10, LNX-1.11, LNX-1.12.
Session scope: 15–45m; split if larger.
Acceptance: Rich copy/cut/paste preserves supported structure; hostile data is diagnosed, while read-only/cancelled drops cannot mutate.

Implementation:

- [ ] LNX-1.13-I1 Connect native clipboard/drop formats to shared codecs, validation and asset policy. Preserve format precedence, plain text and one history operation; reuse sanitization.

Validation:

- [ ] LNX-1.13-V1 `bash native/linux/scripts/check.sh clipboard`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.14 — Connect durable sessions to app lifecycle

- [ ] LNX-1.14 Connect durable sessions to app lifecycle.

Purpose: durability.
Context: `native/linux/src/storage/`.
Dependencies: LNX-1.3, LNX-1.7.
Session scope: 15–45m; split if larger.
Acceptance: Offline edit/restore needs no account; commit status follows durable receipts. Close/reopen and storage errors preserve recovery.

Implementation:

- [ ] LNX-1.14-I1 Bind qualified LocalStore and native lifecycle notifications to the shared session. Surface pending/committed/error states; reuse journal/checkpoint/outbox logic.

Validation:

- [ ] LNX-1.14-V1 `bash native/linux/scripts/check.sh durability`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.15 — Bind collaboration and reconnect state

- [ ] LNX-1.15 Bind collaboration and reconnect state.

Purpose: collaboration.
Context: `native/linux/src/transport/`.
Dependencies: LNX-1.6, LNX-1.14.
Session scope: 15–45m; split if larger.
Acceptance: Two fixtures converge across reconnect; remote selection, revocation and document switching preserve receipt/input semantics.

Implementation:

- [ ] LNX-1.15-I1 Bind host-injected Transport/Authorization and presence to native UI state. Reuse qualified sync logic; exercise cancellation and remote composition overlap with mocks.

Validation:

- [ ] LNX-1.15-V1 `bash native/linux/scripts/check.sh collaboration`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.16 — Expose accessible text and editor actions

- [ ] LNX-1.16 Expose accessible text and editor actions.

Purpose: accessibility-text.
Context: `native/linux/src/accessibility/`.
Dependencies: LNX-1.6, LNX-1.7, LNX-1.8.
Session scope: 15–45m; split if larger.
Acceptance: Native accessibility exposes text, selection, command/read-only state and keyboard focus at declared scaling settings.

Implementation:

- [ ] LNX-1.16-I1 Expose native text/actions for Orca through the declared accessibility stack. Programmatically check labels and selection; preserve OS input. Actual screen-reader qualification belongs to roadmap 20.

Validation:

- [ ] LNX-1.16-V1 `bash native/linux/scripts/check.sh accessibility-text`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.17 — Expose accessible tables and attachments

- [ ] LNX-1.17 Expose accessible tables and attachments.

Purpose: accessibility-structure.
Context: `native/linux/src/accessibility/`.
Dependencies: LNX-1.10, LNX-1.11, LNX-1.12, LNX-1.16.
Session scope: 15–45m; split if larger.
Acceptance: Tables/cells, alt text, reference labels and atom actions have accessible relationships and a pointer-free focus route.

Implementation:

- [ ] LNX-1.17-I1 Add native structure/actions for tables and attachments using shared labels and capabilities; test focus transitions and bounded announcements.

Validation:

- [ ] LNX-1.17-V1 `bash native/linux/scripts/check.sh accessibility-structure`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-1.18 — Present native change and revision views

- [ ] LNX-1.18 Present native change and revision views.

Purpose: change-review.
Context: `native/linux/src/change-review/`.
Dependencies: LNX-1.10, LNX-1.11, LNX-1.16, LNX-1.17.
Session scope: 15–45m; split if larger.
Acceptance: Read-only unified/semantic changes retain profile labels and trusted/unknown attribution; stale revisions remain visible.

Implementation:

- [ ] LNX-1.18-I1 Render roadmap-13 changes in accessible native views with range navigation. Reuse its algorithm, revision and attribution contracts; never rewind the live replica.

Validation:

- [ ] LNX-1.18-V1 `bash native/linux/scripts/check.sh change-review`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

## Epic LNX-2 — Package the adapter and prepare platform qualification

### Task LNX-2.1 — Build the distributable native SDK artifact

- [ ] LNX-2.1 Build the distributable native SDK artifact.

Purpose: package.
Context: `native/linux/packaging/`.
Dependencies: LNX-1.13, LNX-1.14, LNX-1.15, LNX-1.17, LNX-1.18.
Session scope: 15–45m; split if larger.
Acceptance: The package contains supported binaries, API/version metadata, resources and notices, with immutable hashes and no publication.

Implementation:

- [ ] LNX-2.1-I1 Build a native Rust/GTK SDK package with explicit system-library and distribution requirements. Pin runtime/generator compatibility, check contents via the pinned Cargo/GTK build and display-backed test commands, and record OS/CPU support. Signing/publication are separate release actions.

Validation:

- [ ] LNX-2.1-V1 `bash native/linux/scripts/check.sh package`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-2.2 — Verify a clean native consumer

- [ ] LNX-2.2 Verify a clean native consumer.

Purpose: consumer.
Context: `native/linux/consumer/`.
Dependencies: LNX-2.1.
Session scope: 15–45m; split if larger.
Acceptance: A clean consumer needs no sibling checkout and runs actual local/rich/offline/mocked-collaboration and change-review smoke cases.

Implementation:

- [ ] LNX-2.2-I1 Build a native sample against the immutable packed SDK; test install/open/edit/review/dispose and reject missing resources. Keep every mandatory feature discoverable.

Validation:

- [ ] LNX-2.2-V1 `bash native/linux/scripts/check.sh consumer`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.

### Task LNX-2.3 — Hand off exact platform qualification inputs

- [ ] LNX-2.3 Hand off exact platform qualification inputs.

Purpose: qualification-readiness.
Context: `native/linux/qualification/`; `native/linux/capability.json`.
Dependencies: LNX-2.2.
Session scope: 15–45m; split if larger.
Acceptance: Every mandatory capability links implemented tests/artifacts; real device, IME, accessibility and OS-support claims await roadmap 20.

Implementation:

- [ ] LNX-2.3-I1 Prepare the Linux runbook and fixture manifest for roadmap 20, including Orca through the declared accessibility stack, tool/device/IME versions and failure counts. Validate links and qualification states.

Validation:

- [ ] LNX-2.3-V1 `bash native/linux/scripts/check.sh qualification-readiness`. Assert acceptance; require nonzero matching tests.

Evidence: Commands/counts/revisions in progress.
Handoff: Last substep and next action.
Blocked behavior: Unchecked; name owner/unblock condition.
