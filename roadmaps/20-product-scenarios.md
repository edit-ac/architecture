# Qualify real product workflows across clients

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core`; paths below are core-relative unless prefixed `../architecture/`. Follow `../architecture/specs/delivery-scenarios.md` and the active task context. This is planned follow-up delivery, not implemented capability.

Required upstream tracks: `08-sdk-integration.md`, `10-web-qualification.md`, `13-change-diffs.md`, `14-host-agent-editing.md`, `15-tui-client.md`, `16-ios-sdk.md`, `17-android-sdk.md`, `18-desktop-native.md`, `21-extension-library.md`, `22-windows-native.md`, `23-linux-native.md` complete at reviewed source/implementation revisions with passing evidence. Check these gates before launching; source dependencies below are local to this file.

## Execution rules

The controller owns this source. Write progress/checkmarks/evidence in the configured separate progress file. Each iteration implements at most one parent with its implementation and validation substeps. Aim for 15–45 minutes plus checks; if the boundary cannot fit, propose a stable controller-approved split before implementation. Use named fixtures/checks, creating planned test commands before running them. Missing checks, zero matches, failures and skips are not passing acceptance.

Use deterministic fixtures and mocked transports only; no paid model/provider calls, .secrets loading or production document writes. Other ready local tasks are permitted independent work. Unavailable device/toolchain/review evidence blocks its qualified claim, not unrelated platform work. Do not launch another runner or publish before an explicit release task.

## Epic DEL-1 — Qualify real product workflows across clients

### Task DEL-1.1 — Freeze the supported product profile matrix

- [ ] DEL-1.1 Freeze the supported product profile matrix.

Purpose: Freeze the supported product profile matrix as one bounded reusable delivery boundary.
Context: `fixtures/product-scenarios/manifest.json`; `../architecture/evidence/delivery-matrix.md`; `../architecture/specs/delivery-scenarios.md`; `../architecture/specs/verification.md`.
Dependencies: none.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Every mandatory web/iOS/Android/macOS/Windows/Linux/TUI capability has a real implementation reference; known terminal presentation differences are explicit.

Implementation:

- [ ] DEL-1.1-I1 Create `tests/scenarios/run.mjs` as a manifest-driven deterministic dispatcher; reject unknown scenarios and zero-case/absent commands. Map required capabilities to exact package/platform versions, devices, fixtures and prerequisite evidence. Treat encrypted mode as separately qualified roadmap24, not a silent default claim.

Validation:

- [ ] DEL-1.1-V1 node tests/scenarios/run.mjs validate-matrix. Assert all acceptance cases; record exact command/exit, nonzero executed/passed/failed/skipped counts, fixture/revision hashes and unavailable-platform evidence.

Evidence: Separate progress entry `DEL-1.1` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DEL-1.1`.
Blocked behavior: Leave `DEL-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task DEL-1.2 — Qualify PM-ticket editor embedding

- [ ] DEL-1.2 Qualify PM-ticket editor embedding.

Purpose: Qualify PM-ticket editor embedding as one bounded reusable delivery boundary.
Context: `examples/pm-ticket/`; `tests/scenarios/ticket-editor.*`; `../architecture/specs/delivery-scenarios.md`; `../architecture/specs/verification.md`.
Dependencies: DEL-1.1.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Ticket text/marks/lists/table/image/reference edits, undo/redo and focus/disposal match mandatory semantics; no WebView/native fallback passes native parity.

Implementation:

- [ ] DEL-1.2-I1 Embed the same schema/preset in web plus each native host with host-owned reference resolver and readonly/edit modes. Use actual native controls and prepared host auth.

Validation:

- [ ] DEL-1.2-V1 node tests/scenarios/run.mjs ticket-editor. Assert all acceptance cases; record exact command/exit, nonzero executed/passed/failed/skipped counts, fixture/revision hashes and unavailable-platform evidence.

Evidence: Separate progress entry `DEL-1.2` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DEL-1.2`.
Blocked behavior: Leave `DEL-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task DEL-1.3 — Qualify offline and reconnect document editing

- [ ] DEL-1.3 Qualify offline and reconnect document editing.

Purpose: Qualify offline and reconnect document editing as one bounded reusable delivery boundary.
Context: `tests/scenarios/offline-reconnect.*`; `fixtures/product-scenarios/offline/`; `../architecture/specs/delivery-scenarios.md`; `../architecture/specs/verification.md`.
Dependencies: DEL-1.1.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: All acknowledged supported edits recover/converge; uncached offline targets are unavailable; local pending work and durable remote receipts remain distinct on every UI.

Implementation:

- [ ] DEL-1.3-I1 Create offline and edit cached docs on each client, inject native/browser lifecycle failures after local acknowledgment, reconnect shuffled peers and distinguish expired policy from transport failure.

Validation:

- [ ] DEL-1.3-V1 node tests/scenarios/run.mjs offline-reconnect. Assert all acceptance cases; record exact command/exit, nonzero executed/passed/failed/skipped counts, fixture/revision hashes and unavailable-platform evidence.

Evidence: Separate progress entry `DEL-1.3` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DEL-1.3`.
Blocked behavior: Leave `DEL-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task DEL-1.4 — Qualify local files and URI-launched TUI sessions

- [ ] DEL-1.4 Qualify local files and URI-launched TUI sessions.

Purpose: Qualify local files and URI-launched TUI sessions as one bounded reusable delivery boundary.
Context: `tests/scenarios/tui-files.*`; `fixtures/product-scenarios/files/`; `../architecture/specs/delivery-scenarios.md`; `../architecture/specs/verification.md`.
Dependencies: DEL-1.1.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: No-op preserves bytes; conflicts retain base/local/current data; local editing needs no server; cached hosted work reconnects without whole-source replacement.

Implementation:

- [ ] DEL-1.4-I1 Open Markdown/literal files and configured ac:// documents in the terminal client; include changed-on-disk files, dirty source plus remote edits, unsupported atoms and terminal restart.

Validation:

- [ ] DEL-1.4-V1 node tests/scenarios/run.mjs tui-files. Assert all acceptance cases; record exact command/exit, nonzero executed/passed/failed/skipped counts, fixture/revision hashes and unavailable-platform evidence.

Evidence: Separate progress entry `DEL-1.4` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DEL-1.4`.
Blocked behavior: Leave `DEL-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task DEL-1.5 — Qualify host-MCP agent and human coediting

- [ ] DEL-1.5 Qualify host-MCP agent and human coediting.

Purpose: Qualify host-MCP agent and human coediting as one bounded reusable delivery boundary.
Context: `tests/scenarios/agent-human.*`; `examples/host-mcp/`; `../architecture/specs/delivery-scenarios.md`; `../architecture/specs/verification.md`.
Dependencies: DEL-1.2, DEL-1.3.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Web, iOS, Android, macOS, Windows and Linux views each receive normal realtime changes; stale overlap conflicts, duplicate insertion is prevented, readonly denial and operation attribution remain accurate.

Implementation:

- [ ] DEL-1.5-I1 Use prepared MCP requests to export/edit/upload/preview/apply while a human-view fixture edits another range; repeat requests after injected timeout/restart.

Validation:

- [ ] DEL-1.5-V1 node tests/scenarios/run.mjs agent-human. Assert all acceptance cases; record exact command/exit, nonzero executed/passed/failed/skipped counts, fixture/revision hashes and unavailable-platform evidence.

Evidence: Separate progress entry `DEL-1.5` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DEL-1.5`.
Blocked behavior: Leave `DEL-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task DEL-1.6 — Qualify exact review and change tracking

- [ ] DEL-1.6 Qualify exact review and change tracking.

Purpose: Qualify exact review and change tracking as one bounded reusable delivery boundary.
Context: `tests/scenarios/change-review.*`; `fixtures/product-scenarios/diffs/`; `../architecture/specs/delivery-scenarios.md`; `../architecture/specs/verification.md`.
Dependencies: DEL-1.2, DEL-1.4, DEL-1.5.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Exact patches reproduce hashes, every mandatory semantic change is visible and historical inspection never rewinds a live replica or invents authorship.

Implementation:

- [ ] DEL-1.6-I1 Review source/projected/semantic diffs across web, native and TUI, including formatting-only edits, moves, newlines, unknown modules and unavailable old history; restore as a new edit.

Validation:

- [ ] DEL-1.6-V1 node tests/scenarios/run.mjs change-review. Assert all acceptance cases; record exact command/exit, nonzero executed/passed/failed/skipped counts, fixture/revision hashes and unavailable-platform evidence.

Evidence: Separate progress entry `DEL-1.6` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DEL-1.6`.
Blocked behavior: Leave `DEL-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task DEL-1.7 — Complete cross-platform input and accessibility evidence

- [ ] DEL-1.7 Complete cross-platform input and accessibility evidence.

Purpose: Complete cross-platform input and accessibility evidence as one bounded reusable delivery boundary.
Context: `tests/manual/full-platform-matrix.md`; `../architecture/evidence/full-platform-input.md`; `../architecture/specs/delivery-scenarios.md`; `../architecture/specs/verification.md`. [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: DEL-1.2, DEL-1.3.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Every claimed native platform has actual input/accessibility evidence; desktop/mobile emulation and synthetic events cannot stand in for missing required device cases. Require each native SDK owned NAT/SEL/MOV/CMD variant and actual-device PRF-07 evidence with exact OS/toolkit/IME/profile versions.

Implementation:

- [ ] DEL-1.7-I1 Execute actual IME/marked text, screen reader, keyboard/touch, selection, autocorrection/dictation and supported desktop OS matrix. Preserve device-specific failures and public support limits.

Validation:

- [ ] DEL-1.7-V1 node tests/scenarios/run.mjs verify-manual-evidence; execute tests/manual/full-platform-matrix.md on actual declared devices. Assert all acceptance cases; record exact command/exit, nonzero executed/passed/failed/skipped counts, fixture/revision hashes and unavailable-platform evidence.

Evidence: Separate progress entry `DEL-1.7` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DEL-1.7`.
Blocked behavior: Leave `DEL-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task DEL-1.9 — Qualify native mobile clipboard on physical devices

- [ ] DEL-1.9 Qualify native mobile clipboard on physical devices.

Purpose: Deliver the named transfer boundary with reproducible evidence and explicit qualification status.
Context: `tests/manual/native-mobile-clipboard.md`; `native/ios/qualification/`; `native/android/qualification/`; [native clipboard cases](../tests/native-clipboard-cases.md)
Dependencies: DEL-1.7.
Session scope: One named boundary; target 15–45 minutes plus focused validation. These are future tasks; this roadmap revision does not execute native tests or authorize device runs.
Acceptance: Every claimed iOS/iPadOS and Android OS/device profile has NCL-01–NCL-28 physical-device results using the packaged SDK, native editor and OS pasteboard. Simulator/emulator replay does not replace these runs. Minimum matrix includes iPhone and iPad, supported Android stock and one vendor keyboard/device profile, touch and attached keyboard, cross-app rich/plain/image flavors and accessibility-driven paste.

Implementation:

- [ ] DEL-1.9-I1 Write and execute the physical-device runbook only in this future qualification task. Record device model, OS build, keyboard/IME/accessibility versions, app/package/codec revisions, transfer flavors, expected semantic/selection/history/journal results, permission behavior and evidence for canceled/failed operations. Keep unavailable profiles unchecked.

Validation:

- [ ] DEL-1.9-V1 Run the documented on-device protocol and linked device test dispatchers; inspect captured OS events and semantic/undo/storage receipts independently. Require nonzero matching cases and record executed/passed/failed/skipped counts, immutable fixture/source/package revisions and preserved failures. Missing tools/devices or skipped mandatory cases do not qualify support.

Evidence: Separate progress entry with commands, exact environment and artifact hashes; catalogs remain planned until the corresponding runs exist.
Handoff: Last completed substep, unavailable environment or failing case, owner and next bounded action.
Blocked behavior: Leave unchecked; name owner, unblock condition and retry trigger. Never substitute simulation for physical-device evidence.

### Task DEL-1.10 — Qualify native desktop clipboard on real OS installations

- [ ] DEL-1.10 Qualify native desktop clipboard on real OS installations.

Purpose: Deliver the named transfer boundary with reproducible evidence and explicit qualification status.
Context: `tests/manual/native-desktop-clipboard.md`; `native/macos/qualification/`; `native/windows/qualification/`; `native/linux/qualification/`; [native clipboard cases](../tests/native-clipboard-cases.md)
Dependencies: DEL-1.7.
Session scope: One named boundary; target 15–45 minutes plus focused validation. These are future tasks; this roadmap revision does not execute native tests or authorize device runs.
Acceptance: Each claimed macOS, Windows and Linux desktop profile has physical-machine clipboard/menu/shortcut and assistive-input evidence. Linux separately records X11 and Wayland clipboard ownership and PRIMARY where claimed. A VM/mock pass cannot become an undocumented hardware or accessibility claim.

Implementation:

- [ ] DEL-1.10-I1 Prepare and execute the real-OS NCL matrix only in this future task, including RTF/HTML/plain/internal formats, selection direction, ownership after source app exit, delayed clipboard providers, match-style shortcuts, two native editors, table-cell transfer and extension fallback. Record unavailable cases and exact environments.

Validation:

- [ ] DEL-1.10-V1 Execute the documented physical-machine protocol and capture OS/toolkit, desktop session, shortcuts, codec/package revisions and failure artifacts. Require nonzero matching cases and record executed/passed/failed/skipped counts, immutable fixture/source/package revisions and preserved failures. Missing tools/devices or skipped mandatory cases do not qualify support.

Evidence: Separate progress entry with commands, exact environment and artifact hashes; catalogs remain planned until the corresponding runs exist.
Handoff: Last completed substep, unavailable environment or failing case, owner and next bounded action.
Blocked behavior: Leave unchecked; name owner, unblock condition and retry trigger. Never substitute simulation for physical-device evidence.

### Task DEL-1.8 — Release the qualified full client profile

- [ ] DEL-1.8 Release the qualified full client profile.

Purpose: Release the qualified full client profile as one bounded reusable delivery boundary.
Context: `../architecture/evidence/full-delivery.md`; `docs/platform-support.md`; `scripts/release-profile.mjs`; `../architecture/specs/delivery-scenarios.md`; `../architecture/specs/verification.md`.
Dependencies: DEL-1.6, DEL-1.7, DEL-1.9, DEL-1.10.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: PM embedding, collaborative docs, host-agent edits and all declared native/TUI capabilities have reproducible evidence and honest support claims; partial platform success is not labeled full parity.

Implementation:

- [ ] DEL-1.8-I1 Assemble current passing evidence, consumer packages/native SDK artifacts, documented install/deep-link flows, licenses and known limits. Stage publication by component without claiming unqualified encryption.

Validation:

- [ ] DEL-1.8-V1 node scripts/release-profile.mjs --check; node tests/scenarios/run.mjs validate-matrix. Assert all acceptance cases; record exact command/exit, nonzero executed/passed/failed/skipped counts, fixture/revision hashes and unavailable-platform evidence.

Evidence: Separate progress entry `DEL-1.8` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `DEL-1.8`.
Blocked behavior: Leave `DEL-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.
