# Integrate rich extensions into the native Android SDK

Status: IN_PROGRESS

Qualification amendment (user decision, 2026-10-14): Physical devices, named target-platform simulators/emulators and desktop OS VMs/test hosts are accepted for platform and release qualification under the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms). Missing physical hardware does not block completion. Execute required behavior against the implemented target-platform runtime; document and test virtual equivalents for unavailable hardware-only input/accessibility cases. Record physical versus virtual provenance and measure performance in the tested environment. This supersedes earlier physical-only or manual-only clauses below; it does not complete unchecked tasks or waive implementation, correctness, security or artifact gates.

## Goal and entry conditions

Workspace: `core`; paths below are workspace-relative unless prefixed `../architecture/` or another explicit sibling. Read `../architecture/specs/ecosystem-maintainability.md` and only the active task's named context. Planned paths and commands are created by their owning task. This source describes delivery; it is not a capability claim or live progress.

Required upstream tracks: `17-android-sdk.md`, `25-rich-content-extensions.md`, `26-link-resolution.md`, `27-document-conversion.md`, `30-architecture-fitness.md` at reviewed immutable source/implementation revisions with passing evidence.  Local Dependencies fields refer only to this file.

## Execution rules

The controller owns this source. Keep checkmarks, evidence and interruption handoff in the separate progress file. Run one parent per iteration, with its implementation and validation substeps. Read task-local context rather than the complete ecosystem. Create named checks before invoking them; unknown suites, zero matches and skipped platforms cannot pass. Use deterministic fixtures and prepared transports, no live model/provider calls or paid inference. Do not load `.secrets`. Missing toolchains or upstream evidence block only their dependent tasks. Do not launch another controller or publish outside a named release task.

## Epic NAX-1 — Integrate rich extensions into the native Android SDK

### Task NAX-1.1 — Verify extension services and bind the native dispatchers

- [ ] NAX-1.1 Verify extension services and bind the native dispatchers.

Purpose: Verify extension services and bind the native dispatchers as one bounded integration or qualification boundary.
Context: `native/android/`; `native/android/capability.json`; `../architecture/specs/native-sdk-parity.md`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: none.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: The existing native SDK is qualified at a named revision; public service descriptors/FFI and platform thread ownership are fixed before feature wiring. Bind the published official profile and document-search/code-command capabilities; missing presenters are explicit, not an implied web parity pass.

Implementation:

- [ ] NAX-1.1-I1 Check all entry tracks, bind shared capability/service envelopes, add extension fixture suites to the existing native dispatcher, and reject unknown/zero-case suite names. Do not duplicate semantics.

Validation:

- [ ] NAX-1.1-V1 `bash native/android/scripts/check.sh extension-entry`. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NAX-1.1` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NAX-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task NAX-1.2 — Integrate incremental code-block presentation

- [ ] NAX-1.2 Integrate incremental code-block presentation.

Purpose: Integrate incremental code-block presentation as one bounded integration or qualification boundary.
Context: `native/android/`; `native/android/capability.json`; `../architecture/specs/native-sdk-parity.md`; `native/android/extensions/code/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: NAX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Code edits use shared text commands; syntax spans are derived, versioned, cancellable and composition-safe with supported fonts/contrast. Large block typing does not wait for full highlighting. Bind IDE-01–IDE-06 where the code-tools profile is advertised, preserving native focus/IME and shared command history.

Implementation:

- [ ] NAX-1.2-I1 Wire the qualified25 highlighter port, offset conversion and native text decorations with stale-result discard, visible-range work and plain-code fallback on limits; retain exact whitespace and language metadata.

Validation:

- [ ] NAX-1.2-V1 `bash native/android/scripts/check.sh extension-code`; run code block input/scroll/composition fixtures and record raw timing/memory. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NAX-1.2` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NAX-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task NAX-1.3 — Integrate table formatting and bounded rich editing

- [ ] NAX-1.3 Integrate table formatting and bounded rich editing.

Purpose: Integrate table formatting and bounded rich editing as one bounded integration or qualification boundary.
Context: `native/android/`; `native/android/capability.json`; `../architecture/specs/native-sdk-parity.md`; `native/android/extensions/table/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: NAX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Formatter/row/column/alignment commands preserve identity/selection and one intended undo group; native table layout and accessible navigation meet the supported envelope.

Implementation:

- [ ] NAX-1.3-I1 Bind25 table commands, formatting preview and bounded layout/presenter metadata. Add keyboard/touch selection and resize/alignment UI without a platform semantic fork or whole-document layout per cell edit.

Validation:

- [ ] NAX-1.3-V1 `bash native/android/scripts/check.sh extension-tables`; measure changed-cell invalidation, visible rows, paste and resizing. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NAX-1.3` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NAX-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task NAX-1.4 — Integrate assets and safe embed presentation

- [ ] NAX-1.4 Integrate assets and safe embed presentation.

Purpose: Integrate assets and safe embed presentation as one bounded integration or qualification boundary.
Context: `native/android/`; `native/android/capability.json`; `../architecture/specs/native-sdk-parity.md`; `native/android/extensions/assets/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: NAX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Pick/upload/finalize/cancel/retry/download uses host authorization and actual asset state; unsupported embeds remain safe accessible cards with recoverable data.

Implementation:

- [ ] NAX-1.4-I1 Wire25 asset/blob ports and OS file/image pickers; enforce size/decode limits and approved native embed presenters, dispose previews, and retain recoverable failed/offline transfers.

Validation:

- [ ] NAX-1.4-V1 `bash native/android/scripts/check.sh extension-assets`; exercise permission loss, abort, orphan cleanup, image limits and offline recovery. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NAX-1.4` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NAX-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task NAX-1.5 — Integrate customizable references and automatic link display

- [ ] NAX-1.5 Integrate customizable references and automatic link display.

Purpose: Integrate customizable references and automatic link display as one bounded integration or qualification boundary.
Context: `native/android/`; `native/android/capability.json`; `../architecture/specs/native-sdk-parity.md`; `native/android/extensions/links/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: NAX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Public auto-paste metadata and private references follow26 policy; principal changes clear private caches, revoked titles never enter shared labels, and activation rechecks permission.

Implementation:

- [ ] NAX-1.5-I1 Bind public/internal resolver ports, cancellation, native title/icon cards and custom host reference rendering. Internal denial never invokes generic external fetch.

Validation:

- [ ] NAX-1.5-V1 `bash native/android/scripts/check.sh extension-links`; use prepared public/private resolver fixtures with redaction assertions. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NAX-1.5` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NAX-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task NAX-1.6 — Integrate document import and export actions

- [ ] NAX-1.6 Integrate document import and export actions.

Purpose: Integrate document import and export actions as one bounded integration or qualification boundary.
Context: `native/android/`; `native/android/capability.json`; `../architecture/specs/native-sdk-parity.md`; `native/android/extensions/conversion/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: NAX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Qualified directions support OS open/save, loss preview, cancellation and atomic output; PDF is export-only. Missing optional converter has explicit diagnostics.

Implementation:

- [ ] NAX-1.6-I1 Connect27 conversion jobs and native file grants/sandbox paths, font/assets and staged import admission. Resolve chosen revision at job start and revalidate imports at commit; exports do not mutate the document.

Validation:

- [ ] NAX-1.6-V1 `bash native/android/scripts/check.sh extension-conversion`; test DOCX/Markdown and declared secondary formats plus PDF output and PDF-input rejection. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NAX-1.6` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NAX-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task NAX-1.7 — Complete slash and block-reorder interaction parity

- [ ] NAX-1.7 Complete slash and block-reorder interaction parity.

Purpose: Complete slash and block-reorder interaction parity as one bounded integration or qualification boundary.
Context: `native/android/`; `native/android/capability.json`; `../architecture/specs/native-sdk-parity.md`; `native/android/extensions/interaction/`; `../architecture/specs/ecosystem-maintainability.md`.
Dependencies: NAX-1.1.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: Local slash suggestions and block movement work with keyboard/touch, screen readers and a non-drag single-pointer alternative; remote edits do not open menus. Bind FND-01–FND-07 through native find/command surfaces when advertised; distinguish selected-text drag from block handles and preserve native text services.

Implementation:

- [ ] NAX-1.7-I1 Apply25 interaction upgrades to actual native menu/pointer controls; validate cancellation, autoscroll, stale move targets and composition. Keep one identity-preserving shared semantic move.

Validation:

- [ ] NAX-1.7-V1 `bash native/android/scripts/check.sh extension-interaction`; execute declared pointer, keyboard and accessibility cases. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NAX-1.7` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NAX-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task NAX-1.9 — Integrate formatted extension clipboard and literal paste

- [ ] NAX-1.9 Integrate formatted extension clipboard and literal paste.

Purpose: Deliver the named transfer boundary with reproducible evidence and explicit qualification status.
Context: `native/`; [native clipboard cases](../tests/native-clipboard-cases.md); `../architecture/specs/extension-library.md`; `../architecture/specs/rich-content-extensions.md`
Dependencies: NAX-1.6, NAX-1.7.
Session scope: One named boundary; target 15–45 minutes plus focused validation. These are future tasks; this roadmap revision does not execute native tests or authorize device runs.
Acceptance: Native table-cell, image-caption, reference and math transfer preserves every admitted format and structural field through the shared extension codecs. Native menu and keyboard plain-paste commands bypass formatting while remaining discoverable and accessible. Emulator/OS-host fixtures and physical or virtual platform runbooks have separate qualification labels; no native tests run during roadmap editing.

Implementation:

- [ ] NAX-1.9-I1 Wire EXT-1.13 codec capabilities and full-palette import/export into native transfer routing. Add formatted table cells, cross-app flavors, selected rich replacement, two editors, delayed providers, unavailable extension fallback and atomic undo/cancel fixtures; provide the physical or virtual platform handoff to final ecosystem qualification.

Validation:

- [ ] NAX-1.9-V1 Run the platform extension dispatcher suite `clipboard-formatting` in the future task; validate package and fixture hashes and table/extension semantics. Require nonzero matching cases and record executed/passed/failed/skipped counts, immutable fixture/source/package revisions and preserved failures. Missing required runtime tooling, failed behavior or untested mandatory cases do not qualify support; use accepted virtual runtimes/equivalents when physical hardware is unavailable.

Evidence: Separate progress entry with commands, exact environment and artifact hashes; catalogs remain planned until the corresponding runs exist.
Handoff: Last completed substep, unavailable environment or failing case, owner and next bounded action.
Blocked behavior: Leave unchecked; name owner, unblock condition and retry trigger. Accept target-platform simulators/emulators/VMs under verification.md and retain virtual provenance; never relabel their results as physical-device observations.

### Task NAX-1.8 — Qualify the packed native extension consumer

- [ ] NAX-1.8 Qualify the packed native extension consumer.

Purpose: Qualify the packed native extension consumer as one bounded integration or qualification boundary.
Context: `native/android/`; `native/android/capability.json`; `../architecture/specs/native-sdk-parity.md`; `native/android/examples/`; `../architecture/specs/ecosystem-maintainability.md`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: NAX-1.2, NAX-1.3, NAX-1.4, NAX-1.5, NAX-1.6, NAX-1.7, NAX-1.9.
Session scope: One named boundary, normally 15–45 minutes plus focused checks. If it cannot fit, propose a stable controller-reviewed split before implementation; do not hide additional platform/features in this task.
Acceptance: A clean packaged consumer exposes the supported feature/direction profile with real native UI; missing actual OS evidence blocks its support claim. Run advertised FND/IDE and relevant FPX combinations with PRF-07 physical or virtual platform evidence; required preset capabilities cannot be silently marked optional to pass.

Implementation:

- [ ] NAX-1.8-I1 Install immutable SDK/extension artifacts into the platform consumer, run the combined feature fixtures, update shared capability evidence and hand off remaining full scenario qualification to37.

Validation:

- [ ] NAX-1.8-V1 `bash native/android/scripts/check.sh extension-consumer`; execute real OS input/accessibility cases and record exact devices/OS/toolchain, bundle and performance evidence. Record exact commands/exits, nonzero case counts, failures/skips, implementation/profile revisions and artifact hashes. Missing required manual evidence stays unqualified.

Evidence: Separate progress entry `NAX-1.8` links changed paths, immutable inputs and focused check artifacts; retain failed evidence.
Handoff: Last completed substep, current file/symbol, exact failure or unresolved choice, and the next bounded action.
Blocked behavior: Leave `NAX-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and bounded retry trigger. Select another dependency-ready task; otherwise stop and report.
