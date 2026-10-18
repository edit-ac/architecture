# Verify physical devices after development

Status: IN_PROGRESS

User decision, 2026-10-18: “lets move physical device verification to a dedicated roadmap and finish the development before that.” This roadmap owns deferred physical-device observations. It starts after the relevant implementation and accepted virtual-platform development checks pass. Its unchecked tasks do not block those development roadmaps. No runner is started by this planning change.

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Preserve the [accepted simulator/emulator/VM policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms). That policy already permits eligible release profiles on named virtual runtimes and tested virtual equivalents; this roadmap does not impose a new physical-only release requirement. Physical-device capability claims require the corresponding physical evidence here. Missing implementation, failed semantic/input/history/storage checks, unsupported required behavior and failed applicable performance budgets remain development blockers.

Entry gate: the relevant iOS, Android, mobile-web and extension implementation has passed its owning development checks at exact source/package revisions. Consume current reports from tracks 05, 10, 16, 17, 20, 30, 31, 32, 37, 38, 39, 40 and 41. Preserve their historical receipts and failures. Transfer only deferred physical observations, not failing virtual tests, missing APIs, incomplete conversion/media features, unmeasured budgets or unfinished accessibility-tree/action equivalents.

## Handoff from existing development owners

| Original owner | Physical observation deferred here | Required development evidence remains with owner |
|---|---|---|
| FMT-1.15-V1 | Physical clipboard providers and hardware-specific transfer behavior on the declared mobile devices | Complete accepted-runtime case/profile matrix; the old five-case development subset alone is insufficient |
| INT-1.14 / INT-1.18 | Physical keyboard, stylus and device-only gesture observations | Available OS menu/replacement behavior, semantic targets and Undo/Redo; the Safari Edit Undo gap is not deferred as hardware work |
| AIN-1.10 | Physical VoiceOver/TalkBack exploration and hardware-dependent dictation/recognition observations | Executed accessibility-tree/action and native input-boundary equivalents, semantic preservation and working advertised fallbacks |
| MWB-1.11 / MWX-1.8 | Physical mobile viewport/gesture, vendor input and extension observations | Actual named mobile virtual-runtime coverage and required lifecycle/input/extension behavior |
| FIT-1.8 / PRF-07 | Physical thermal, compositor, peak-memory and device-specific timing observations | Comparable simulator/OS-host performance and raw attribution; observed native Long latency failure and insufficient tail samples remain development work |
| REL-1.6 / DEL-1.7, DEL-1.9, DEL-1.10 | Physical-device-specific capability and release-envelope claims | Complete accepted virtual-platform release evidence and all other correctness, security and artifact gates |

PHY-1.1 binds the exact retained source case/profile IDs for each row before physical execution. No row changes the status of historical results or turns an untested equivalent into a pass.

## Execution rules

The controller owns this source. Record progress separately; do not check off planning templates. Run one parent per iteration. Before touching a device, record its ownership, OS/build, app/browser/package identity, input/accessibility configuration and exact case manifest. Use deterministic fixtures and mocked provider transports. No paid inference, secrets, publication or deployment. Restore changed device settings and clean only owned test resources. Missing hardware blocks this roadmap's affected parent, not accepted virtual development. Never count a deferred physical observation as an executed or passed test.

## Epic PHY-1 — Qualify the physical observations deferred during development

### Task PHY-1.1 — Bind the deferred physical-device matrix

- [ ] PHY-1.1 Bind the deferred physical-device matrix.

Purpose: Bind the deferred physical-device matrix as one bounded qualification boundary.
Context: [verification policy](../specs/verification.md); [desktop input cases](../tests/desktop-editing-cases.md); [mobile cases](../tests/mobile-web-cases.md); [extension cases](../tests/mobile-extension-cases.md). Planned implementation paths are core-relative.
Dependencies: none.
Session scope: One declared device/profile group; split a larger matrix before execution.
Acceptance: Inventory the physical-only observations deferred by each owning roadmap; retain original case IDs and virtual equivalents. Select supported device/OS/input profiles and freeze sample counts, correctness oracles, latency/resource limits and comparison policy before measurements.

Implementation:

- [ ] PHY-1.1-I1 Create the physical-device manifest, receipt validator and runbook; link exact development receipts and explicit direct-versus-virtual evidence.

Validation:

- [ ] PHY-1.1-V1 Run the new validator against valid prepared manifests and deliberately missing devices, source hashes, cases and failure counts. Reject empty coverage and fabricated passes. Planning validation does not qualify hardware. Create named commands before invoking them; missing scripts, zero matches and skipped required cases fail.

Evidence: Separate progress entry `PHY-1.1` links immutable manifests, raw artifacts and commands/exits under `../architecture/evidence/physical-devices/`.
Handoff: Record the last completed case, changed paths, exact failure or missing device, owner and next bounded action.
Blocked behavior: Leave `PHY-1.1` unchecked with a stable fingerprint and exact resume condition; do not retry unchanged failures or reblock unrelated development.

### Task PHY-1.2 — Verify iOS and iPadOS physical editing

- [ ] PHY-1.2 Verify iOS and iPadOS physical editing.

Purpose: Verify iOS and iPadOS physical editing as one bounded qualification boundary.
Context: [verification policy](../specs/verification.md); [desktop input cases](../tests/desktop-editing-cases.md); [mobile cases](../tests/mobile-web-cases.md); [extension cases](../tests/mobile-extension-cases.md). Planned implementation paths are core-relative.
Dependencies: PHY-1.1.
Session scope: One declared device/profile group; split a larger matrix before execution.
Acceptance: On each declared iPhone/iPad profile, verify native SDK and mobile Safari or installed-app paths: IME candidate commit/cancel, selection/handles, clipboard and storage recovery, Undo/Redo, viewport/focus and extension lifecycle. Include physical keyboard/stylus observations only where advertised.

Implementation:

- [ ] PHY-1.2-I1 Implement the declared physical iOS drivers or reproducible operator protocol using the packaged native engine and real OS controls; preserve input and semantic ownership.

Validation:

- [ ] PHY-1.2-V1 Execute the pinned case matrix on actual devices and retain screenshots/traces, independent semantic/history/reopen assertions and exact nonzero counts. Do not replace physical runs with desktop WebKit or injected callbacks. Create named commands before invoking them; missing scripts, zero matches and skipped required cases fail.

Evidence: Separate progress entry `PHY-1.2` links immutable manifests, raw artifacts and commands/exits under `../architecture/evidence/physical-devices/`.
Handoff: Record the last completed case, changed paths, exact failure or missing device, owner and next bounded action.
Blocked behavior: Leave `PHY-1.2` unchecked with a stable fingerprint and exact resume condition; do not retry unchanged failures or reblock unrelated development.

### Task PHY-1.3 — Verify Android physical editing

- [ ] PHY-1.3 Verify Android physical editing.

Purpose: Verify Android physical editing as one bounded qualification boundary.
Context: [verification policy](../specs/verification.md); [desktop input cases](../tests/desktop-editing-cases.md); [mobile cases](../tests/mobile-web-cases.md); [extension cases](../tests/mobile-extension-cases.md). Planned implementation paths are core-relative.
Dependencies: PHY-1.1.
Session scope: One declared device/profile group; split a larger matrix before execution.
Acceptance: On declared Android vendor/device/IME profiles, verify native SDK and Chrome/installed-app paths, composition, selection, clipboard, lifecycle/recovery, Undo/Redo and extensions. Retain existing HONOR observations as historical evidence unless their source/profile pins still apply.

Implementation:

- [ ] PHY-1.3-I1 Implement physical Android drivers or reproducible operator protocol against the actual packaged engine and approved local fixtures.

Validation:

- [ ] PHY-1.3-V1 Run the named physical matrix with exact OS/vendor keyboard provenance and independent semantic, storage and lifecycle assertions. Preserve failures and unsupported capabilities without silently shrinking required coverage. Create named commands before invoking them; missing scripts, zero matches and skipped required cases fail.

Evidence: Separate progress entry `PHY-1.3` links immutable manifests, raw artifacts and commands/exits under `../architecture/evidence/physical-devices/`.
Handoff: Record the last completed case, changed paths, exact failure or missing device, owner and next bounded action.
Blocked behavior: Leave `PHY-1.3` unchecked with a stable fingerprint and exact resume condition; do not retry unchanged failures or reblock unrelated development.

### Task PHY-1.4 — Measure physical input accessibility and resource behavior

- [ ] PHY-1.4 Measure physical input accessibility and resource behavior.

Purpose: Measure physical input accessibility and resource behavior as one bounded qualification boundary.
Context: [verification policy](../specs/verification.md); [desktop input cases](../tests/desktop-editing-cases.md); [mobile cases](../tests/mobile-web-cases.md); [extension cases](../tests/mobile-extension-cases.md). Planned implementation paths are core-relative.
Dependencies: PHY-1.2, PHY-1.3.
Session scope: One declared device/profile group; split a larger matrix before execution.
Acceptance: Measure real touch, hardware keyboard/stylus and advertised native input services; exercise VoiceOver/TalkBack on the supported profiles. Measure Task/Long input/scroll, memory/disposal and physical thermal behavior with the pre-reviewed sample/tail policy. Simulator callbacks do not establish physical compositor, recognition or thermal behavior.

Implementation:

- [ ] PHY-1.4-I1 Reuse the existing input, assistive and fitness instrumentation; add only the physical observation adapters needed by the declared matrix. Keep platform policy outside the shared engine.

Validation:

- [ ] PHY-1.4-V1 Execute physical assistive/input and performance cases with raw samples, resource traces, semantic oracles and sufficient tail samples. A failed or inconclusive budget stays failed or inconclusive; do not widen limits after observing results. Create named commands before invoking them; missing scripts, zero matches and skipped required cases fail.

Evidence: Separate progress entry `PHY-1.4` links immutable manifests, raw artifacts and commands/exits under `../architecture/evidence/physical-devices/`.
Handoff: Record the last completed case, changed paths, exact failure or missing device, owner and next bounded action.
Blocked behavior: Leave `PHY-1.4` unchecked with a stable fingerprint and exact resume condition; do not retry unchanged failures or reblock unrelated development.

### Task PHY-1.5 — Publish the physical qualification return internally

- [ ] PHY-1.5 Publish the physical qualification return internally.

Purpose: Publish the physical qualification return internally as one bounded qualification boundary.
Context: [verification policy](../specs/verification.md); [desktop input cases](../tests/desktop-editing-cases.md); [mobile cases](../tests/mobile-web-cases.md); [extension cases](../tests/mobile-extension-cases.md). Planned implementation paths are core-relative.
Dependencies: PHY-1.2, PHY-1.3, PHY-1.4.
Session scope: One declared device/profile group; split a larger matrix before execution.
Acceptance: Reconcile each deferred physical observation with its owning case and exact implemented profile. Distinguish physical-qualified, virtual-qualified, failed, unavailable and diagnostic states; no universal hardware parity claim.

Implementation:

- [ ] PHY-1.5-I1 Assemble the immutable physical evidence index and update capability/progress evidence for only the profiles that passed; keep historical failed receipts and links to accepted virtual evidence.

Validation:

- [ ] PHY-1.5-V1 Run the receipt validator and owning qualification checks; verify all declared required physical cells have nonzero passing counts, current hashes and no failures/skips. Leave incomplete cells open. This internal return does not authorize public publication or deployment. Create named commands before invoking them; missing scripts, zero matches and skipped required cases fail.

Evidence: Separate progress entry `PHY-1.5` links immutable manifests, raw artifacts and commands/exits under `../architecture/evidence/physical-devices/`.
Handoff: Record the last completed case, changed paths, exact failure or missing device, owner and next bounded action.
Blocked behavior: Leave `PHY-1.5` unchecked with a stable fingerprint and exact resume condition; do not retry unchanged failures or reblock unrelated development.

