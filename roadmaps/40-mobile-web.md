# Support touch devices and mobile browser editing

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Read [mobile web](../specs/mobile-web.md), the active task's [case group](../tests/mobile-web-cases.md), and its named paths. Paths are relative to core unless explicitly prefixed. This roadmap implements baseline mobile web behavior; device emulation does not establish real mobile support.

Upstream entry gates: `08-sdk-integration.md` and `38-editor-interactions.md` complete at reviewed current source/implementation revisions with passing evidence. Track 40 does not require rich extensions, all native SDKs or optional assistance. Browser release track 10 requires this track; richer optional mobile presenters are qualified separately in 41.

## Execution rules

The controller owns this source; write progress/checkmarks/evidence separately. Execute at most one parent per iteration, normally 15–45 minutes plus validation. Propose a controller split when a boundary or required device matrix outgrows that scope; preserve complete acceptance. Dependencies contain only local IDs. Create named suites/dispatchers before running them; missing/zero-match checks fail. Use real engine/adapters and prepared event/transport fixtures. No paid inference, secrets loading, provider probes, automatic recordings or background runner startup. Preserve failures and distinguish measured device outcomes from mocked mechanics. Track and clean up task-owned test resources; preserve other tasks' work.

## Epic MWB-1 — Support touch devices and mobile browser editing

### Task MWB-1.1 — Freeze mobile capabilities, fixtures and baseline cost

- [ ] MWB-1.1 Freeze mobile capabilities, fixtures and baseline cost.

Purpose: Freeze mobile capabilities, fixtures and baseline cost as one bounded integration boundary.
Context: `tests/mobile-web/fixtures/`; `tests/mobile-web/harness.ts`; `packages/web/package.json`; [mobile web contract](../specs/mobile-web.md); [case catalog](../tests/mobile-web-cases.md).
Dependencies: none.
Session scope: One named group and its validation; touch only named paths and directly required test/configuration glue.
Acceptance: All 59 catalog IDs have an owner and explicit mechanics/device receipt type; packaged baseline artifacts and mandatory device/mode/keyboard sample are frozen. Record the proposed 5 KB gzip JS incremental allowance inside the approved 32 KiB JS / 512 KiB total gzip hard caps, preferred-size results (16 KB JS / 256 KB total), capability fallback matrix and exact upstream evidence. Use the measurement/counting contract in verification.md; missing measurements or either hard-cap overrun fail baseline admission.

Implementation:

- [ ] MWB-1.1-I1 Reuse the RGS shared driver/receipt format behind test:mobile-web with validated --group dispatch; extend it with mobile event/geometry fixtures and semantic/selection/resource counters. Reuse INT fixtures, declare the host viewport/focus contract and capture before-change bundle/startup measurements. Capabilities are runtime observations, not user-agent categories.

Validation:

- [ ] MWB-1.1-V1 npm run test:mobile-web -- --group harness. Missing IDs, invalid group, absent real engine or an intentionally wrong expected snapshot fail. This task admits the cost profile; it does not claim actual device support. Record exact command/exit, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWB-1.1` with case IDs, implementation/profile/fixture revisions, exact commands/counts and retained artifacts under `../architecture/evidence/mobile-web/`.
Handoff: Record the last completed substep, changed files/symbols, failing case/missing capability and next bounded action.
Blocked behavior: Leave `MWB-1.1` unchecked with reason, owner, unblock condition and retry trigger; select only dependency-ready work and stop when none remains.

### Task MWB-1.2 — Preserve native touch selection and pointer cancellation

- [ ] MWB-1.2 Preserve native touch selection and pointer cancellation.

Purpose: Preserve native touch selection and pointer cancellation as one bounded integration boundary.
Context: `packages/web/src/input/`; `packages/web/src/dom/selection.ts`; `tests/mobile-web/touch.spec.ts`; [mobile web contract](../specs/mobile-web.md); [case catalog](../tests/mobile-web-cases.md). [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: MWB-1.1.
Session scope: One named group and its validation; touch only named paths and directly required test/configuration glue.
Acceptance: MBT-01–MBT-07 mechanics pass; native scrolling/selection/zoom remain available. Scoped handle gestures commit once only on success and release capture/auto-scroll on cancellation. No default gesture framework is introduced. SEL-06/SEL-07 and XFR-07 ensure native text gestures coexist with drag handles; cancel autoscroll and preserve selection through viewport changes.

Implementation:

- [ ] MWB-1.2-I1 Reuse native editable selection and Pointer Events; implement only missing focus/range mapping and a bounded handle lifecycle. Keep broad root listeners passive where possible, preserve context menus, and provide tap alternatives without suppressing document selection.

Validation:

- [ ] MWB-1.2-V1 npm run test:mobile-web -- --group touch. Assert cancel/lost-capture/multi-pointer/compatibility-click branches, no mutation on provisional moves, exact resource cleanup and target accessibility. Native handles/zoom need MWB-1.11 device evidence. Record exact command/exit, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWB-1.2` with case IDs, implementation/profile/fixture revisions, exact commands/counts and retained artifacts under `../architecture/evidence/mobile-web/`.
Handoff: Record the last completed substep, changed files/symbols, failing case/missing capability and next bounded action.
Blocked behavior: Leave `MWB-1.2` unchecked with reason, owner, unblock condition and retry trigger; select only dependency-ready work and stop when none remains.

### Task MWB-1.3 — Reconcile mobile keyboard and non-keyboard text input

- [ ] MWB-1.3 Reconcile mobile keyboard and non-keyboard text input.

Purpose: Reconcile mobile keyboard and non-keyboard text input as one bounded integration boundary.
Context: `packages/web/src/input/`; `tests/mobile-web/input.spec.ts`; [mobile web contract](../specs/mobile-web.md); [case catalog](../tests/mobile-web-cases.md).
Dependencies: MWB-1.2.
Session scope: One named group and its validation; touch only named paths and directly required test/configuration glue.
Acceptance: MBI-01–MBI-08 mechanics pass with no-keydown, replacement, repeated deletion, composition ordering, handwriting/dictation-like event sequences and changing keyboard capabilities. Synthetic traces cannot establish real IME/voice support.

Implementation:

- [ ] MWB-1.3-I1 Extend existing bounded reconciliation/composition gates with observed mobile traces. Preserve actual replacement ranges/characters and conservative shortcut eligibility. Share engine commands with desktop; avoid keyboard-specific content models or guessed autocorrection.

Validation:

- [ ] MWB-1.3-V1 npm run test:mobile-web -- --group input. Run named Unicode/selection vectors through real Rust/WASM/browser paths and assert one commit/history boundary, retained marks and stale-target rejection. Preserve trace provenance and failed sequences. Record exact command/exit, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWB-1.3` with case IDs, implementation/profile/fixture revisions, exact commands/counts and retained artifacts under `../architecture/evidence/mobile-web/`.
Handoff: Record the last completed substep, changed files/symbols, failing case/missing capability and next bounded action.
Blocked behavior: Leave `MWB-1.3` unchecked with reason, owner, unblock condition and retry trigger; select only dependency-ready work and stop when none remains.

### Task MWB-1.4 — Keep caret and controls visible across viewport changes

- [ ] MWB-1.4 Keep caret and controls visible across viewport changes.

Purpose: Keep caret and controls visible across viewport changes as one bounded integration boundary.
Context: `packages/web/src/platform/viewport.ts`; `packages/web/src/dom/`; `tests/mobile-web/viewport.spec.ts`; [mobile web contract](../specs/mobile-web.md); [case catalog](../tests/mobile-web-cases.md).
Dependencies: MWB-1.3.
Session scope: One named group and its validation; touch only named paths and directly required test/configuration glue.
Acceptance: MBV-01–MBV-09 mechanics pass for resize/overlay modes, safe areas, nested roots, zoom offsets, rotation and capability absence. Geometry changes produce no content mutation, focus theft or scroll loops.

Implementation:

- [ ] MWB-1.4-I1 Implement a disposable per-owning-window viewport service only where consumers share it; use ordinary scrolling/CSS first. Schedule bounded coordinate reads/writes, follow local active caret requests, respect host meta viewport and leased overlay policy, and retain reachable fallback controls.

Validation:

- [ ] MWB-1.4-V1 npm run test:mobile-web -- --group viewport. Assert coordinate-space cases, burst coalescing, two-editor ownership, cancellation on unrecoverable geometry changes and continued owned auto-scroll after valid coordinate refresh, no double insets/compensation and no continuous frame work. Actual keyboard occlusion remains a device gate. Record exact command/exit, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWB-1.4` with case IDs, implementation/profile/fixture revisions, exact commands/counts and retained artifacts under `../architecture/evidence/mobile-web/`.
Handoff: Record the last completed substep, changed files/symbols, failing case/missing capability and next bounded action.
Blocked behavior: Leave `MWB-1.4` unchecked with reason, owner, unblock condition and retry trigger; select only dependency-ready work and stop when none remains.

### Task MWB-1.5 — Expose mobile commands and preserve selection through focus

- [ ] MWB-1.5 Expose mobile commands and preserve selection through focus.

Purpose: Expose mobile commands and preserve selection through focus as one bounded integration boundary.
Context: `packages/web/src/commands/`; `packages/web/src/ui/`; `tests/mobile-web/focus.spec.ts`; [mobile web contract](../specs/mobile-web.md); [case catalog](../tests/mobile-web-cases.md).
Dependencies: MWB-1.3, MWB-1.4.
Session scope: One named group and its validation; touch only named paths and directly required test/configuration glue.
Acceptance: MBF-01–MBF-06 pass mechanically: toolbar selection, explicit command search, declined programmatic focus, absent modifier keys, prose/code hints and form embedding. Async work cannot steal focus or force the keyboard open.

Implementation:

- [ ] MWB-1.5-I1 Provide reachable soft-break/history/indent/literal-paste/format controls using existing commands and stable selection. Apply supported keyboard hints without remount/composition loss, distinguish control-owned focus from selection-preserving actions, and expose fallback guidance when browser focus requests decline.

Validation:

- [ ] MWB-1.5-V1 npm run test:mobile-web -- --group focus. Test pointerdown/blur/activation order, user focus changes, no keyboard-state claims from focus alone, enterkeyhint independence and no accidental host form submission. Record exact command/exit, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWB-1.5` with case IDs, implementation/profile/fixture revisions, exact commands/counts and retained artifacts under `../architecture/evidence/mobile-web/`.
Handoff: Record the last completed substep, changed files/symbols, failing case/missing capability and next bounded action.
Blocked behavior: Leave `MWB-1.5` unchecked with reason, owner, unblock condition and retry trigger; select only dependency-ready work and stop when none remains.

### Task MWB-1.6 — Handle mobile clipboard and browser lifecycle recovery

- [ ] MWB-1.6 Handle mobile clipboard and browser lifecycle recovery.

Purpose: Handle mobile clipboard and browser lifecycle recovery as one bounded integration boundary.
Context: `packages/web/src/clipboard/`; `packages/web/src/lifecycle/`; `tests/mobile-web/lifecycle.spec.ts`; [mobile web contract](../specs/mobile-web.md); [case catalog](../tests/mobile-web-cases.md).
Dependencies: MWB-1.3, MWB-1.5.
Session scope: One named group and its validation; touch only named paths and directly required test/configuration glue.
Acceptance: MBC-01–MBC-07 mechanics pass: permission and native-paste fallback, delayed results, picker/share blur, two-editor isolation, pagehide/pageshow and recovery. Failed cut/cancel leaves content intact; local durability semantics stay unchanged.

Implementation:

- [ ] MWB-1.6-I1 Reuse bounded imports, stable anchors and storage recovery. Suspend disposable gesture/viewport state, restore session ownership without duplicate listeners and reject late callbacks after document switch/disposal. Keep native paste usable without scripted clipboard access.

Validation:

- [ ] MWB-1.6-V1 npm run test:mobile-web -- --group lifecycle. Assert exact mutation count, no eager permission prompts, clipboard failure recovery and listener/session teardown. Device BFCache/eviction/offline observations must distinguish committed from uncommitted content. Record exact command/exit, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWB-1.6` with case IDs, implementation/profile/fixture revisions, exact commands/counts and retained artifacts under `../architecture/evidence/mobile-web/`.
Handoff: Record the last completed substep, changed files/symbols, failing case/missing capability and next bounded action.
Blocked behavior: Leave `MWB-1.6` unchecked with reason, owner, unblock condition and retry trigger; select only dependency-ready work and stop when none remains.

### Task MWB-1.7 — Add progressive keyboard and browser API adapters

- [ ] MWB-1.7 Add progressive keyboard and browser API adapters.

Purpose: Add progressive keyboard and browser API adapters as one bounded integration boundary.
Context: `packages/web/src/platform/capabilities.ts`; `packages/web/src/platform/keyboard.ts`; `tests/mobile-web/capabilities.spec.ts`; [mobile web contract](../specs/mobile-web.md); [case catalog](../tests/mobile-web-cases.md).
Dependencies: MWB-1.4, MWB-1.6.
Session scope: One named group and its validation; touch only named paths and directly required test/configuration glue.
Acceptance: MBA-01–MBA-07 pass for absent, available, denied, throwing and changing APIs. Default editing takes no keyboard lock or microphone access. Optional API code is lazy; failure retains qualified contenteditable/native controls.

Implementation:

- [ ] MWB-1.7-I1 Add only demonstrated browser capability adapters: optional keyboard geometry, layout labels and explicit host keyboard policy with ownership/disposal. Document secure-context/activation/embedding constraints per API. Record EditContext feasibility in a separate probe/decision; lack of benefit/support keeps it excluded from production and the default bundle.

Validation:

- [ ] MWB-1.7-V1 npm run test:mobile-web -- --group capabilities. Exercise runtime detection and failure paths with prepared platform objects plus real-browser fallbacks. Record experimental support as evidence only; do not count mocked success as device/API availability or ship a second editor model. Record exact command/exit, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWB-1.7` with case IDs, implementation/profile/fixture revisions, exact commands/counts and retained artifacts under `../architecture/evidence/mobile-web/`.
Handoff: Record the last completed substep, changed files/symbols, failing case/missing capability and next bounded action.
Blocked behavior: Leave `MWB-1.7` unchecked with reason, owner, unblock condition and retry trigger; select only dependency-ready work and stop when none remains.

### Task MWB-1.8 — Integrate baseline modules with touch and small viewports

- [ ] MWB-1.8 Integrate baseline modules with touch and small viewports.

Purpose: Integrate baseline modules with touch and small viewports as one bounded integration boundary.
Context: `packages/web/src/modules/`; `tests/mobile-web/modules.spec.ts`; [mobile web contract](../specs/mobile-web.md); [case catalog](../tests/mobile-web-cases.md).
Dependencies: MWB-1.2, MWB-1.5, MWB-1.7.
Session scope: One named group and its validation; touch only named paths and directly required test/configuration glue.
Acceptance: MBX-01–MBX-05 pass mechanically: visible command invocation, native-menu overlap fallback, table/code scrolling and tap block actions. Baseline editing and OS input remain usable with enhanced presenters disabled.

Implementation:

- [ ] MWB-1.8-I1 Adapt existing MOD/INT module presenters to the shared viewport/focus contract, without introducing rich media/conversion dependencies. Keep commands available without hover, slash typing or drag; leave advanced feature semantics and integrations to track 41.

Validation:

- [ ] MWB-1.8-V1 npm run test:mobile-web -- --group modules. Verify supported semantic command parity, focus/selection retention, keyboard-open bounded panels, no scroll trap and no optional-feature imports when disabled. Real AT exploration is required downstream. Record exact command/exit, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWB-1.8` with case IDs, implementation/profile/fixture revisions, exact commands/counts and retained artifacts under `../architecture/evidence/mobile-web/`.
Handoff: Record the last completed substep, changed files/symbols, failing case/missing capability and next bounded action.
Blocked behavior: Leave `MWB-1.8` unchecked with reason, owner, unblock condition and retry trigger; select only dependency-ready work and stop when none remains.

### Task MWB-1.9 — Enforce mobile loading and runtime overhead limits

- [ ] MWB-1.9 Enforce mobile loading and runtime overhead limits.

Purpose: Enforce mobile loading and runtime overhead limits as one bounded integration boundary.
Context: `tests/mobile-web/budgets.test.mjs`; `tests/mobile-web/resources.spec.ts`; `fixtures/mobile-web-consumers/`; [mobile web contract](../specs/mobile-web.md); [case catalog](../tests/mobile-web-cases.md). [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: MWB-1.6, MWB-1.7, MWB-1.8.
Session scope: One named group and its validation; touch only named paths and directly required test/configuration glue.
Acceptance: MBP-01–MBP-06 pass within the frozen incremental and total profile. Disabled optional features cause zero feature imports/assets/requests/listeners/observers/frames; idle/hidden states have no polling; resources return to the declared plateau. PRF-01–PRF-05/PRF-07 add continuous selection/drag and mixed optional work as applicable, preserving the baseline mobile bundle and idle budgets.

Implementation:

- [ ] MWB-1.9-I1 Compare packed feature-equivalent before/after and disabled/enabled consumers; measure bytes, evaluation/startup, latency, geometry batches, long tasks and repeated lifecycle resources. Move nonessential code behind optional boundaries when budgets fail; preserve required baseline access and keep failures visible.

Validation:

- [ ] MWB-1.9-V1 npm run test:mobile-web -- --group budgets. Record raw samples and exact hardware/browser/artifact profiles, not only summaries. Run deterministic resource assertions separately from actual phone timing; emulator results cannot qualify phone budgets. Record exact command/exit, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWB-1.9` with case IDs, implementation/profile/fixture revisions, exact commands/counts and retained artifacts under `../architecture/evidence/mobile-web/`.
Handoff: Record the last completed substep, changed files/symbols, failing case/missing capability and next bounded action.
Blocked behavior: Leave `MWB-1.9` unchecked with reason, owner, unblock condition and retry trigger; select only dependency-ready work and stop when none remains.

### Task MWB-1.10 — Qualify integrated mobile browser mechanics

- [ ] MWB-1.10 Qualify integrated mobile browser mechanics.

Purpose: Qualify integrated mobile browser mechanics as one bounded integration boundary.
Context: `tests/mobile-web/`; `../architecture/evidence/mobile-web/`; [mobile web contract](../specs/mobile-web.md); [case catalog](../tests/mobile-web-cases.md).
Dependencies: MWB-1.9.
Session scope: One named group and its validation; touch only named paths and directly required test/configuration glue.
Acceptance: Every mechanical case runs with nonzero matching assertions against pinned Chromium/Firefox/WebKit in the declared desktop/touch-emulation harness, with explicit distinction from actual mobile support. High-risk combined scenarios and legacy desktop behavior remain correct.

Implementation:

- [ ] MWB-1.10-I1 Run all owned groups, reuse exact-revision INT regressions and add composition+toolbar, keyboard+rotation, remote edit+selection and pointer-cancel+pagehide sequences. Reconcile model, focus, viewport and resource snapshots through the real packed consumer.

Validation:

- [ ] MWB-1.10-V1 npm run test:mobile-web -- --group all. Record per-ID/browser executed/passed/failed/skipped counts and raw failure artifacts. Zero matches, missing commands or skipped required mechanical cells fail; preserve unsupported API fallback results. Record exact command/exit, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWB-1.10` with case IDs, implementation/profile/fixture revisions, exact commands/counts and retained artifacts under `../architecture/evidence/mobile-web/`.
Handoff: Record the last completed substep, changed files/symbols, failing case/missing capability and next bounded action.
Blocked behavior: Leave `MWB-1.10` unchecked with reason, owner, unblock condition and retry trigger; select only dependency-ready work and stop when none remains.

### Task MWB-1.11 — Qualify real mobile devices and release handoff

- [ ] MWB-1.11 Qualify real mobile devices and release handoff.

Purpose: Qualify real mobile devices and release handoff as one bounded integration boundary.
Context: `tests/mobile-web/device-protocol.md`; `scripts/check-mobile-web-evidence.mjs`; `../architecture/evidence/mobile-web/`; [mobile web contract](../specs/mobile-web.md); [case catalog](../tests/mobile-web-cases.md). [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: MWB-1.10.
Session scope: One named group and its validation; touch only named paths and directly required test/configuration glue.
Acceptance: MBQ-01–MBQ-04 and all catalog device rows have actual evidence for the frozen required iPhone/iPadOS/Android browser/keyboard sample. Baseline access works with optional extensions disabled; failed required behavior blocks claims. Tab/PWA/embedded modes qualify only where advertised. Bind relevant SEL/MOV/XFR/CMD actual-device variants including hardware keyboards; unsupported text-drag APIs retain accessible transfer alternatives.

Implementation:

- [ ] MWB-1.11-I1 Create the reproducible manual protocol and receipt validator; observe native keyboards/handles/context menus, scroll/zoom, handwriting where advertised, VoiceOver/TalkBack, activation restrictions and lifecycle. Measure phone budgets and publish precise API/mode/version limitations; hand current reviewed evidence to REL-1.1.

Validation:

- [ ] MWB-1.11-V1 node scripts/check-mobile-web-evidence.mjs. Create nonzero receipt rejection fixtures, then run the actual device steps. Record real case/device/locale/keyboard/AT versions, counts, raw observations and feature costs. Receipt validation is not behavior evidence; absent optional APIs qualify only via working fallbacks. Record exact command/exit, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWB-1.11` with case IDs, implementation/profile/fixture revisions, exact commands/counts and retained artifacts under `../architecture/evidence/mobile-web/`.
Handoff: Record the last completed substep, changed files/symbols, failing case/missing capability and next bounded action.
Blocked behavior: Leave `MWB-1.11` unchecked with reason, owner, unblock condition and retry trigger; select only dependency-ready work and stop when none remains.
