# Integrate rich extensions into the native Linux SDK

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core`; paths below are workspace-relative unless prefixed `../architecture/` or another explicit sibling. Read `../architecture/specs/ecosystem-maintainability.md` and only the active task's named context. Planned paths and commands are created by their owning task. This source describes delivery; it is not a capability claim or live progress.

Required upstream tracks: `23-linux-native.md`, `25-rich-content-extensions.md`, `26-link-resolution.md`, `27-document-conversion.md`, `30-architecture-fitness.md` at reviewed immutable source/implementation revisions with passing evidence.  Local Dependencies fields refer only to this file.

## Execution rules

The controller owns this source. Keep checkmarks, evidence and interruption handoff in the separate progress file. Run one parent per iteration, with its implementation and validation substeps. Read task-local context rather than the complete ecosystem. Create named checks before invoking them; unknown suites, zero matches and skipped platforms cannot pass. Use deterministic fixtures and prepared transports, no live model/provider calls or paid inference. Do not load `.secrets`. Missing toolchains or upstream evidence block only their dependent tasks. Do not launch another controller or publish outside a named release task.

## Epic NLX-1 — Integrate rich extensions into the native Linux SDK

### Task NLX-1.1 — Verify extension services and bind the native dispatchers

- [ ] NLX-1.1 Verify extension services and bind the native dispatchers.

Purpose: Verify extension services and bind the native dispatchers as one bounded integration or qualification boundary.
Context: `native/linux/`; `native/linux/capability.json`; `../architecture/specs/native-sdk-parity.md`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: none.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: The existing native SDK is qualified at a named revision; public service descriptors/FFI and platform thread ownership are fixed before feature wiring.

Implementation:

- [ ] NLX-1.1-I1 Check all entry tracks, bind shared capability/service envelopes, add extension fixture suites to the existing native dispatcher, and reject unknown/zero-case suite names. Do not duplicate semantics.

Validation:

- [ ] NLX-1.1-V1 `bash native/linux/scripts/check.sh extension-entry`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NLX-1.1` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NLX-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task NLX-1.2 — Integrate incremental code-block presentation

- [ ] NLX-1.2 Integrate incremental code-block presentation.

Purpose: Integrate incremental code-block presentation as one bounded integration or qualification boundary.
Context: `native/linux/`; `native/linux/capability.json`; `../architecture/specs/native-sdk-parity.md`; `native/linux/extensions/code/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: NLX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Code edits use shared text commands; syntax spans are derived, versioned, cancellable and composition-safe with supported fonts/contrast. Large block typing does not wait for full highlighting.

Implementation:

- [ ] NLX-1.2-I1 Wire the qualified25 highlighter port, offset conversion and native text decorations with stale-result discard, visible-range work and plain-code fallback on limits; retain exact whitespace and language metadata.

Validation:

- [ ] NLX-1.2-V1 `bash native/linux/scripts/check.sh extension-code`; run code block input/scroll/composition fixtures and record raw timing/memory. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NLX-1.2` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NLX-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task NLX-1.3 — Integrate table formatting and bounded rich editing

- [ ] NLX-1.3 Integrate table formatting and bounded rich editing.

Purpose: Integrate table formatting and bounded rich editing as one bounded integration or qualification boundary.
Context: `native/linux/`; `native/linux/capability.json`; `../architecture/specs/native-sdk-parity.md`; `native/linux/extensions/table/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: NLX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Formatter/row/column/alignment commands preserve identity/selection and one intended undo group; native table layout and accessible navigation meet the supported envelope.

Implementation:

- [ ] NLX-1.3-I1 Bind25 table commands, formatting preview and bounded layout/presenter metadata. Add keyboard/touch selection and resize/alignment UI without a platform semantic fork or whole-document layout per cell edit.

Validation:

- [ ] NLX-1.3-V1 `bash native/linux/scripts/check.sh extension-tables`; measure changed-cell invalidation, visible rows, paste and resizing. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NLX-1.3` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NLX-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task NLX-1.4 — Integrate assets and safe embed presentation

- [ ] NLX-1.4 Integrate assets and safe embed presentation.

Purpose: Integrate assets and safe embed presentation as one bounded integration or qualification boundary.
Context: `native/linux/`; `native/linux/capability.json`; `../architecture/specs/native-sdk-parity.md`; `native/linux/extensions/assets/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: NLX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Pick/upload/finalize/cancel/retry/download uses host authorization and actual asset state; unsupported embeds remain safe accessible cards with recoverable data.

Implementation:

- [ ] NLX-1.4-I1 Wire25 asset/blob ports and OS file/image pickers; enforce size/decode limits and approved native embed presenters, dispose previews, and retain recoverable failed/offline transfers.

Validation:

- [ ] NLX-1.4-V1 `bash native/linux/scripts/check.sh extension-assets`; exercise permission loss, abort, orphan cleanup, image limits and offline recovery. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NLX-1.4` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NLX-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task NLX-1.5 — Integrate customizable references and automatic link display

- [ ] NLX-1.5 Integrate customizable references and automatic link display.

Purpose: Integrate customizable references and automatic link display as one bounded integration or qualification boundary.
Context: `native/linux/`; `native/linux/capability.json`; `../architecture/specs/native-sdk-parity.md`; `native/linux/extensions/links/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: NLX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Public auto-paste metadata and private references follow26 policy; principal changes clear private caches, revoked titles never enter shared labels, and activation rechecks permission.

Implementation:

- [ ] NLX-1.5-I1 Bind public/internal resolver ports, cancellation, native title/icon cards and custom host reference rendering. Internal denial never invokes generic external fetch.

Validation:

- [ ] NLX-1.5-V1 `bash native/linux/scripts/check.sh extension-links`; use prepared public/private resolver fixtures with redaction assertions. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NLX-1.5` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NLX-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task NLX-1.6 — Integrate document import and export actions

- [ ] NLX-1.6 Integrate document import and export actions.

Purpose: Integrate document import and export actions as one bounded integration or qualification boundary.
Context: `native/linux/`; `native/linux/capability.json`; `../architecture/specs/native-sdk-parity.md`; `native/linux/extensions/conversion/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: NLX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Qualified directions support OS open/save, loss preview, cancellation and atomic output; PDF is export-only. Missing optional converter has explicit diagnostics.

Implementation:

- [ ] NLX-1.6-I1 Connect27 conversion jobs and native file grants/sandbox paths, font/assets and staged import admission. Resolve chosen revision at job start and revalidate imports at commit; exports do not mutate the document.

Validation:

- [ ] NLX-1.6-V1 `bash native/linux/scripts/check.sh extension-conversion`; test DOCX/Markdown and declared secondary formats plus PDF output and PDF-input rejection. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NLX-1.6` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NLX-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task NLX-1.7 — Complete slash and block-reorder interaction parity

- [ ] NLX-1.7 Complete slash and block-reorder interaction parity.

Purpose: Complete slash and block-reorder interaction parity as one bounded integration or qualification boundary.
Context: `native/linux/`; `native/linux/capability.json`; `../architecture/specs/native-sdk-parity.md`; `native/linux/extensions/interaction/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: NLX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Local slash suggestions and block movement work with keyboard/touch, screen readers and a non-drag single-pointer alternative; remote edits do not open menus.

Implementation:

- [ ] NLX-1.7-I1 Apply25 interaction upgrades to actual native menu/pointer controls; validate cancellation, autoscroll, stale move targets and composition. Keep one identity-preserving shared semantic move.

Validation:

- [ ] NLX-1.7-V1 `bash native/linux/scripts/check.sh extension-interaction`; execute declared pointer, keyboard and accessibility cases. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NLX-1.7` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NLX-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task NLX-1.8 — Qualify the packed native extension consumer

- [ ] NLX-1.8 Qualify the packed native extension consumer.

Purpose: Qualify the packed native extension consumer as one bounded integration or qualification boundary.
Context: `native/linux/`; `native/linux/capability.json`; `../architecture/specs/native-sdk-parity.md`; `native/linux/examples/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: NLX-1.2, NLX-1.3, NLX-1.4, NLX-1.5, NLX-1.6, NLX-1.7.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: A clean packaged consumer exposes the supported feature/direction profile with real native UI; missing actual OS evidence blocks its support claim.

Implementation:

- [ ] NLX-1.8-I1 Install immutable SDK/extension artifacts into the platform consumer, run the combined feature fixtures, update shared capability evidence and hand off remaining full scenario qualification to37.

Validation:

- [ ] NLX-1.8-V1 `bash native/linux/scripts/check.sh extension-consumer`; execute real OS input/accessibility cases and record exact devices/OS/toolchain, bundle and performance evidence. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NLX-1.8` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NLX-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.
