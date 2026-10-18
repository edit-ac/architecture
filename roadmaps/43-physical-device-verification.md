# Verify all device requirements after feature delivery

Status: IN_PROGRESS

## Goal and entry conditions

User decision, 2026-10-18: this final roadmap owns every device/target-runtime observation from all editor roadmaps and their referenced specs/case catalogs. Follow [the delivery sequence](../operations/web-feature-first-20261018.md): web → feature complete → internal alpha → native platforms → public docs → qualifications → native tests here → beta candidate → integrations/feedback. No physical device wait: accepted iOS simulators, Android emulators and desktop OS hosts/VMs satisfy eligible runtime checks. Physical-only claims remain separately deferred if unavailable, never counted as passing.

Workspace: `core`. Entry requires implemented features and the relevant qualified immutable native/browser artifacts. The [transfer register](../operations/device-requirements-20261018.json) preserves original IDs/paragraphs. Original01–42 feature development does not wait on this roadmap. Earlier source/progress/failed evidence remain preserved; no migration marks an unexecuted criterion complete. Focused feature correctness/data safety stays with implementation. Windows/Linux hardware is available but not a priority before editor feature completeness. No paid inference, credentials, publication, deployment or external service integration.

## Execution rules

One bounded15–45minute profile/task per worker; split a larger matrix before execution. Use an existing accepted simulator/emulator/OS host; preserve exact runtime/image/browser/keyboard/IME/AT and source/package/fixture hashes. Synthetic callbacks or desktop mobile viewports do not prove target OS behavior. Optional physical observations never hold virtual-runtime completion. Retain actual nonzero counts and every failed/inconclusive receipt; no unsupported case is silently dropped. Preserve original case IDs in each return. Independent platform groups remain eligible beside another unavailable profile.

### Task PHY-1.1 — Freeze the migrated device matrix

- [ ] PHY-1.1 Freeze the migrated device matrix.

Purpose: Finish the final device verification slice without reblocking editor features.
Context: [verification policy](../specs/verification.md); [device transfer register](../operations/device-requirements-20261018.json); task-local original case catalog and existing dispatcher named by that register.
Dependencies: none.
Session scope: One profile/case group,15–45minutes plus focused checks; split before a larger campaign.
Acceptance: Every original task/device predicate has an owner, accepted virtual method, source pin and honest executed/deferred state; no feature roadmap waits for a device.

Implementation:

- [ ] PHY-1.1-I1 Reconcile every transfer-register entry and referenced device case into named platform/profile/case groups; reuse exact applicable existing virtual or physical evidence without replaying it.

Validation:

- [ ] PHY-1.1-V1 Create/reuse the original named deterministic dispatcher, then run the declared accepted-runtime group. Record exact command/exit, nonzero executed/passed/failed/skipped counts, source/package/fixture/runtime pins and preserved failures. Missing commands, zero matches and skipped required cases fail; optional physical observations are separately deferred.

Evidence: Separate progress entry `PHY-1.1` and immutable receipts under `../architecture/evidence/device-verification/`; map every originating task/case ID.
Handoff: Last completed case, exact remaining substep/error/profile, owner and changed-input resume condition.
Blocked behavior: Retain failed required behavior for its implementation owner; use an available accepted virtual runtime and continue independent profile work. Do not wait for physical hardware or mark missing evidence passed.

### Task PHY-1.2 — Verify iOS and iPadOS device behavior

- [ ] PHY-1.2 Verify iOS and iPadOS device behavior.

Purpose: Finish the final device verification slice without reblocking editor features.
Context: [verification policy](../specs/verification.md); [device transfer register](../operations/device-requirements-20261018.json); task-local original case catalog and existing dispatcher named by that register.
Dependencies: PHY-1.1.
Session scope: One profile/case group,15–45minutes plus focused checks; split before a larger campaign.
Acceptance: Actual packaged engine/native controls and Safari cases execute with independent semantic/history/reopen assertions and exact nonzero counts; virtual limitations and optional physical observations are explicit.

Implementation:

- [ ] PHY-1.2-I1 Run existing mobile Safari/native iOS clipboard, IME, selection, touch, lifecycle, recovery and extension cases in the accepted iOS/iPadOS Simulator. Use available physical devices only as optional additional observations.

Validation:

- [ ] PHY-1.2-V1 Create/reuse the original named deterministic dispatcher, then run the declared accepted-runtime group. Record exact command/exit, nonzero executed/passed/failed/skipped counts, source/package/fixture/runtime pins and preserved failures. Missing commands, zero matches and skipped required cases fail; optional physical observations are separately deferred.

Evidence: Separate progress entry `PHY-1.2` and immutable receipts under `../architecture/evidence/device-verification/`; map every originating task/case ID.
Handoff: Last completed case, exact remaining substep/error/profile, owner and changed-input resume condition.
Blocked behavior: Retain failed required behavior for its implementation owner; use an available accepted virtual runtime and continue independent profile work. Do not wait for physical hardware or mark missing evidence passed.

### Task PHY-1.3 — Verify Android device behavior

- [ ] PHY-1.3 Verify Android device behavior.

Purpose: Finish the final device verification slice without reblocking editor features.
Context: [verification policy](../specs/verification.md); [device transfer register](../operations/device-requirements-20261018.json); task-local original case catalog and existing dispatcher named by that register.
Dependencies: PHY-1.1.
Session scope: One profile/case group,15–45minutes plus focused checks; split before a larger campaign.
Acceptance: Accepted emulator cases have real target-input/runtime traces and independent semantic/storage/history assertions; physical hardware is never an entry dependency.

Implementation:

- [ ] PHY-1.3-I1 Run Android Chrome/native input, IME, clipboard, selection, lifecycle/recovery and extension cases using Android Emulator with recorded image/vendor input profile. Retain historical HONOR evidence only if applicable.

Validation:

- [ ] PHY-1.3-V1 Create/reuse the original named deterministic dispatcher, then run the declared accepted-runtime group. Record exact command/exit, nonzero executed/passed/failed/skipped counts, source/package/fixture/runtime pins and preserved failures. Missing commands, zero matches and skipped required cases fail; optional physical observations are separately deferred.

Evidence: Separate progress entry `PHY-1.3` and immutable receipts under `../architecture/evidence/device-verification/`; map every originating task/case ID.
Handoff: Last completed case, exact remaining substep/error/profile, owner and changed-input resume condition.
Blocked behavior: Retain failed required behavior for its implementation owner; use an available accepted virtual runtime and continue independent profile work. Do not wait for physical hardware or mark missing evidence passed.

### Task PHY-1.4 — Verify device input accessibility and resources

- [ ] PHY-1.4 Verify device input accessibility and resources.

Purpose: Finish the final device verification slice without reblocking editor features.
Context: [verification policy](../specs/verification.md); [device transfer register](../operations/device-requirements-20261018.json); task-local original case catalog and existing dispatcher named by that register.
Dependencies: PHY-1.1.
Session scope: One profile/case group,15–45minutes plus focused checks; split before a larger campaign.
Acceptance: Required virtual behavior/fallbacks and resource cases have honest measurements; no synthetic callback is represented as physical recognition, thermal or hardware proof.

Implementation:

- [ ] PHY-1.4-I1 Reuse native/browser instrumentation for VoiceOver/TalkBack/AT, dictation fallback, hardware-input equivalents and device/resource observations, using accepted virtual boundary/action equivalents where actual virtual hardware is unavailable.

Validation:

- [ ] PHY-1.4-V1 Create/reuse the original named deterministic dispatcher, then run the declared accepted-runtime group. Record exact command/exit, nonzero executed/passed/failed/skipped counts, source/package/fixture/runtime pins and preserved failures. Missing commands, zero matches and skipped required cases fail; optional physical observations are separately deferred.

Evidence: Separate progress entry `PHY-1.4` and immutable receipts under `../architecture/evidence/device-verification/`; map every originating task/case ID.
Handoff: Last completed case, exact remaining substep/error/profile, owner and changed-input resume condition.
Blocked behavior: Retain failed required behavior for its implementation owner; use an available accepted virtual runtime and continue independent profile work. Do not wait for physical hardware or mark missing evidence passed.

### Task PHY-1.6 — Verify desktop runtime device behavior

- [ ] PHY-1.6 Verify desktop runtime device behavior.

Purpose: Finish the final device verification slice without reblocking editor features.
Context: [verification policy](../specs/verification.md); [device transfer register](../operations/device-requirements-20261018.json); task-local original case catalog and existing dispatcher named by that register.
Dependencies: PHY-1.1.
Session scope: One profile/case group,15–45minutes plus focused checks; split before a larger campaign.
Acceptance: Each claimed desktop toolkit/OS profile has executable target-runtime observations and exact semantic/history/recovery assertions. A missing physical host never blocks an accepted VM method.

Implementation:

- [ ] PHY-1.6-I1 Run macOS then lower-priority Windows/Linux OS-host/VM native clipboard, keyboard/IME, accessibility, selection and lifecycle cases against their actual packaged native SDKs.

Validation:

- [ ] PHY-1.6-V1 Create/reuse the original named deterministic dispatcher, then run the declared accepted-runtime group. Record exact command/exit, nonzero executed/passed/failed/skipped counts, source/package/fixture/runtime pins and preserved failures. Missing commands, zero matches and skipped required cases fail; optional physical observations are separately deferred.

Evidence: Separate progress entry `PHY-1.6` and immutable receipts under `../architecture/evidence/device-verification/`; map every originating task/case ID.
Handoff: Last completed case, exact remaining substep/error/profile, owner and changed-input resume condition.
Blocked behavior: Retain failed required behavior for its implementation owner; use an available accepted virtual runtime and continue independent profile work. Do not wait for physical hardware or mark missing evidence passed.

### Task PHY-1.7 — Reconcile every transferred original requirement

- [ ] PHY-1.7 Reconcile every transferred original requirement.

Purpose: Finish the final device verification slice without reblocking editor features.
Context: [verification policy](../specs/verification.md); [device transfer register](../operations/device-requirements-20261018.json); task-local original case catalog and existing dispatcher named by that register.
Dependencies: PHY-1.2, PHY-1.3, PHY-1.4, PHY-1.6.
Session scope: One profile/case group,15–45minutes plus focused checks; split before a larger campaign.
Acceptance: All required accepted-runtime device predicates have passing evidence; optional physical observations remain unclaimed. Every original ID has an auditable return, no missing/zero-case/skipped required runtime counts as success.

Implementation:

- [ ] PHY-1.7-I1 Resolve all transfer-register tasks and all further device predicates in linked specs/catalogs to exact applicable receipts or explicit optional physical deferrals; retain failures and original unchecked historical evidence.

Validation:

- [ ] PHY-1.7-V1 Create/reuse the original named deterministic dispatcher, then run the declared accepted-runtime group. Record exact command/exit, nonzero executed/passed/failed/skipped counts, source/package/fixture/runtime pins and preserved failures. Missing commands, zero matches and skipped required cases fail; optional physical observations are separately deferred.

Evidence: Separate progress entry `PHY-1.7` and immutable receipts under `../architecture/evidence/device-verification/`; map every originating task/case ID.
Handoff: Last completed case, exact remaining substep/error/profile, owner and changed-input resume condition.
Blocked behavior: Retain failed required behavior for its implementation owner; use an available accepted virtual runtime and continue independent profile work. Do not wait for physical hardware or mark missing evidence passed.

### Task PHY-1.5 — Return the device qualification inventory internally

- [ ] PHY-1.5 Return the device qualification inventory internally.

Purpose: Finish the final device verification slice without reblocking editor features.
Context: [verification policy](../specs/verification.md); [device transfer register](../operations/device-requirements-20261018.json); task-local original case catalog and existing dispatcher named by that register.
Dependencies: PHY-1.7.
Session scope: One profile/case group,15–45minutes plus focused checks; split before a larger campaign.
Acceptance: Internal beta handoff distinguishes qualified simulator/emulator/VM/OS-host evidence, optional physical observations and failures; no publication or deployment occurs.

Implementation:

- [ ] PHY-1.5-I1 Compose exact profile/case returns for the existing qualification/release owners and the reviewable beta candidate; retain all source/receipt hashes and unresolved physical claims.

Validation:

- [ ] PHY-1.5-V1 Create/reuse the original named deterministic dispatcher, then run the declared accepted-runtime group. Record exact command/exit, nonzero executed/passed/failed/skipped counts, source/package/fixture/runtime pins and preserved failures. Missing commands, zero matches and skipped required cases fail; optional physical observations are separately deferred.

Evidence: Separate progress entry `PHY-1.5` and immutable receipts under `../architecture/evidence/device-verification/`; map every originating task/case ID.
Handoff: Last completed case, exact remaining substep/error/profile, owner and changed-input resume condition.
Blocked behavior: Retain failed required behavior for its implementation owner; use an available accepted virtual runtime and continue independent profile work. Do not wait for physical hardware or mark missing evidence passed.
