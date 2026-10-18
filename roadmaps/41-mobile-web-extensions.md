# Qualify optional extensions on mobile browsers

Status: IN_PROGRESS

Delivery sequencing (superseding user decision, 2026-10-18): follow [web → features → alpha → native → docs → qualification → native tests → beta → integrations](../operations/web-feature-first-20261018.md). All device/target-runtime observations in this source belong to [roadmap43](43-physical-device-verification.md), including simulator/emulator/OS/IME/AT/clipboard device matrices. They do not gate feature development. Original predicate text below remains the later verification contract; its transfer owner and exact paragraphs are in the [device requirement register](../operations/device-requirements-20261018.json). Feature tasks retain focused correctness/data-safety checks; exhaustive performance/platform/release qualification is later. Windows/Linux implementation waits for web feature completeness; cloud28 retains its explicit deferral. Historical source/progress/checkmarks/failures are not rewritten or declared complete.

Physical follow-up sequencing (user decision, 2026-10-18): transfer deferred physical-only observations to [roadmap 43](43-physical-device-verification.md) after development. Accepted target-platform virtual checks and tested equivalents remain valid; no physical device is required to finish this development roadmap. Failed implementation, virtual input/semantic checks and applicable performance budgets remain blockers. Preserve original case IDs and historical evidence; do not mark deferred physical runs passed.

Qualification amendment (user decision, 2026-10-14): Physical devices, named target-platform simulators/emulators and desktop OS VMs/test hosts are accepted for platform and release qualification under the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms). Missing physical hardware does not block completion. Execute required behavior against the implemented target-platform runtime; document and test virtual equivalents for unavailable hardware-only input/accessibility cases. Record physical versus virtual provenance and measure performance in the tested environment. This supersedes earlier physical-only or manual-only clauses below; it does not complete unchecked tasks or waive implementation, correctness, security or artifact gates.

## Goal and entry conditions

Workspace: `core`. Read `../architecture/specs/mobile-web.md` and only the active task's named context. Paths below are workspace-relative unless explicitly prefixed `../architecture/`. Planned implementation paths, suites and commands are created by their owning task. This is a delivery contract, not evidence of implemented mobile support.

Required upstream tracks: `40-mobile-web.md`, `25-rich-content-extensions.md`, `26-link-resolution.md`, `27-document-conversion.md` and `30-architecture-fitness.md` complete at reviewed immutable source/implementation revisions with passing artifacts. These gates supply baseline mobile editing and existing optional semantic capabilities. AIN-1.2, AIN-1.3 and AIN-1.10 from track 39 gate only MWX-1.7; this track does not wait for native assistance tasks or all of track 39. Local Dependencies fields refer only to this file.

Rust continues to own content, commands, validation, anchors and history. This track adapts browser presenters and consumes existing portable modules; it adds no native SDK implementation, document schema, alternate selection/history model or browser policy to Rust. Baseline editing and portable extension work remain independently owned. Missing portable commands are reported to their owner rather than recreated in a mobile presenter.

## Execution rules

The controller owns this source. Record checkmarks, exact commands, counts, evidence and interruption handoff in the separate progress file. Run at most one parent per iteration. Each parent targets 15–45 minutes plus focused validation; if its implementation or physical or virtual platform matrix cannot fit, propose a stable controller-reviewed split before implementation and retain its full acceptance. Required failed/skipped prerequisites remain locked.

The [mobile extension catalog](../tests/mobile-extension-cases.md) contains 32 planned cases. MWX-1.1 creates its executable index; each owner adds its assertions; MWX-1.8 records final physical or virtual platform observations and measured overhead. Create named suites and dispatcher entries before invoking them. Unknown suites, missing assertions and zero matches fail acceptance. Record automated, physical or virtual platform and evidence-validator counts separately. Deterministic fixtures and mocked transports cover all automated checks; no paid inference, provider calls, credential loading or automatic fixture recording is authorized.

Preserve OS text selection, scrolling and pinch zoom. Controls are discoverable without hover; every gesture operation has a simple tap/control alternative and an accessible keyboard route where applicable. Meet the scoped WCAG 2.2 AA target-size rule: at least 24 by 24 CSS pixels, or a recorded applicable spacing/exception condition; aim for 44 by 44 CSS pixels for primary touch controls. A compact document or fine pointer is not a blanket exception. Feature-detect optional APIs, handle rejection and retain the catalog's fallback paths. Reuse track 40 geometry/focus/lifecycle primitives. Stop only verified task-owned test browsers/servers and preserve other tasks' services and retained evidence.

## Epic MWX-1 — Adapt and qualify existing extension presenters for mobile web

### Task MWX-1.1 — Establish extension capability and absence checks

- [ ] MWX-1.1 Establish extension capability and absence checks.

Purpose: Make mobile-extension qualification consume existing feature contracts and a measurable disabled baseline.
Context: `tests/browser/mobile-extensions/index.ts`; `tests/browser/mobile-extensions/capabilities.spec.ts`; `tests/consumers/mobile-extensions/`; `../architecture/specs/mobile-web.md`; `../architecture/specs/ecosystem-maintainability.md`; [case catalog](../tests/mobile-extension-cases.md).
Dependencies: none.
Session scope: One capability/index boundary, normally 15–45 minutes plus focused checks; propose a controller-reviewed split if necessary.
Acceptance: MWX-C01–MWX-C04 map to executable assertions with fixture hashes and named feature/platform capabilities. Minimal packed consumers omit disabled mobile-extension JS/CSS/assets and install zero extension-owned listeners, observers, timers, workers or network activity. Baseline mobile editing stays available; registering a disabled capability does not mutate content/history or read browser globals at import.

Implementation:

- [ ] MWX-1.1-I1 Create the case index and packed-consumer harness using existing FIT capability/loading profiles. Record available/enabled/authorized/qualified states separately, ownership of every measured resource and byte contribution, and absent/rejected optional API fixtures. Declare profile limits before measuring; retain existing baseline performance limits.

Validation:

- [ ] MWX-1.1-V1 `npm run test:mobile-extensions -- --group capabilities`; `node --test tests/consumers/mobile-extensions/disabled.test.mjs`. Create these checks here. Assert import/asset graphs, zero disabled extension work and nonmutating unsupported states; count baseline resources separately. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, source/implementation/fixture revisions and artifact hashes.

Evidence: Separate progress entry `MWX-1.1` links immutable inputs, per-case counts and production bundle/resource artifacts; retain failed evidence.
Handoff: Last completed substep, changed paths/symbols, unresolved capability or failing case, and next bounded action.
Blocked behavior: Leave `MWX-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and retry trigger. Select another dependency-ready task; otherwise stop and report.

### Task MWX-1.2 — Adapt command and reference controls for touch

- [ ] MWX-1.2 Adapt command and reference controls for touch.

Purpose: Make existing slash, command and reference presenters usable around the mobile keyboard and native selection.
Context: `packages/web/src/modules/slash/`; `packages/web/src/modules/references/`; `tests/browser/mobile-extensions/menus.spec.ts`; `../architecture/specs/editor-interactions.md`; `../architecture/specs/link-resolution.md`; [case catalog](../tests/mobile-extension-cases.md).
Dependencies: MWX-1.1.
Session scope: One presenter interaction boundary, normally 15–45 minutes plus focused checks; split through the controller if the existing presenters require broader repair.
Acceptance: MWX-C05–MWX-C08 pass. Named tap controls expose commands without typing slash or hovering; anchored menus remain reachable after keyboard/viewport changes and internal focus transfer. Selection, composing text and one-command history semantics survive activation, dismissal and stale results. References retain permission-checked preview/activation and no implicit fetch policy.

Implementation:

- [ ] MWX-1.2-I1 Reuse INT-1.9 and RCH-1.16 command/focus logic with track 40 geometry and native-selection preservation. Add touch hit areas, bounded popup scrolling, accessible names/states, dismissal and tap activation. Keep latest-request/session checks and cancellation in existing resolver contracts; opening controls does not grant authority or open remote links.

Validation:

- [ ] MWX-1.2-V1 `npm run test:mobile-extensions -- --group menus`. Create deterministic keyboard/viewport, pointer-to-focus, composition and delayed resolver fixtures; assert selection/history, control reachability and target metrics. Check native-scroll/zoom preservation mechanically, and retain actual touch/AT rows for MWX-1.8. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWX-1.2` links per-ID results, target measurements and preserved failures; synthetic mechanics are labeled separately from device observations.
Handoff: Last completed substep, changed paths/symbols, unresolved focus/geometry case, and next bounded action.
Blocked behavior: Leave `MWX-1.2` unchecked with owner, unblock condition and retry trigger; continue dependency-ready work and stop when none remains.

### Task MWX-1.3 — Adapt code and table controls without changing semantics

- [ ] MWX-1.3 Adapt code and table controls without changing semantics.

Purpose: Expose qualified code/table commands on small touch surfaces while retaining literal input and bounded rendering.
Context: `packages/web/src/modules/code/`; `packages/web/src/modules/table/`; `tests/browser/mobile-extensions/content-controls.spec.ts`; `../architecture/specs/rich-content-extensions.md`; [case catalog](../tests/mobile-extension-cases.md). [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: MWX-1.1.
Session scope: One code/table presenter-control boundary, normally 15–45 minutes plus focused checks; obtain a controller split if repairs exceed adaptation of existing commands.
Acceptance: MWX-C09–MWX-C12 pass. Code and table actions have labeled tap controls and applicable state; required operations remain available when no hardware Tab/shortcut exists. Native text selection and ordinary vertical scrolling coexist with explicitly scrollable wide content. Table edits, selected-table formatting and highlighting still use owning modules and incremental invalidation; source/plain-code fallback stays immediate when optional processing is absent or over budget. Apply advertised FND/IDE/TBL tools through reachable touch controls; keyboard-open query fields never edit the document on Enter.

Implementation:

- [ ] MWX-1.3-I1 Add responsive command surfaces around existing code/table presenters and track 40 focus/geometry contracts. Keep selected cell/range anchors, header/alignment/row/column applicability and read-only state from shared commands. Bound overflow and decoration work; use existing table/highlighter limits rather than a parallel mobile renderer or document-wide scan.

Validation:

- [ ] MWX-1.3-V1 `npm run test:mobile-extensions -- --group content-controls`. Create fixed code, bidi/Unicode and bounded table fixtures; assert semantic snapshots/undo, controls without keyboard shortcuts, incremental counters and overflow boundaries. Native selection/scroll arbitration requires MWX-1.8 device evidence. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWX-1.3` links per-ID outcomes, semantic/invalidation assertions and retained failures.
Handoff: Last completed substep, changed paths/symbols, missing owning command or failing case, and next bounded action.
Blocked behavior: Leave `MWX-1.3` unchecked with owner, unblock condition and retry trigger; continue dependency-ready work and stop when none remains.

### Task MWX-1.4 — Constrain reorder and resize gestures to explicit handles

- [ ] MWX-1.4 Constrain reorder and resize gestures to explicit handles.

Purpose: Adapt existing optional gesture presenters while preserving native text selection, scrolling and zoom.
Context: `packages/web/src/modules/reorder/`; `packages/web/src/modules/images/`; `packages/web/src/modules/table/`; `tests/browser/mobile-extensions/gestures.spec.ts`; `../architecture/specs/rich-content-extensions.md`; [case catalog](../tests/mobile-extension-cases.md).
Dependencies: MWX-1.1.
Session scope: One gesture lifecycle and alternative-control boundary, normally 15–45 minutes plus focused checks; propose a split before adding any missing portable capability.
Acceptance: MWX-C13–MWX-C16 pass. Only explicit handles enter optional drag/resize sessions; editable content retains native selection, scroll and pinch zoom. Reorder has Move before/after controls; an advertised resize operation has labeled size/preset controls. Pointer capture/cancel/loss, competing second-touch/pinch, blur, read-only, target deletion and teardown release all gesture resources without unintended commits. Hover/preview changes do not mutate Rust state; acceptance makes one validated command and history group.

Implementation:

- [ ] MWX-1.4-I1 Reuse RCH-1.17 sessions and existing advertised resize commands, adding scoped touch-action/capture handling and bounded hit-test/auto-scroll scheduling. Revalidate anchors, identity and applicability before commit. Keep all dimensions/geometry previews derived; if a portable resize command is unavailable, expose an honest unsupported capability and hand it to its owner rather than inventing schema semantics.

Validation:

- [ ] MWX-1.4-V1 `npm run test:mobile-extensions -- --group gestures`. Create deterministic competing-pointer, cancellation, viewport-change, remote-deletion and captured-pointer teardown fixtures. Assert zero mutations on canceled sessions, one accepted mutation/undo group despite trailing click/capture-loss events, equivalent tap results and zero retained capture/frame/listener resources. Run the declared native arbitration rows in MWX-1.8. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWX-1.4` links gesture/tap equivalence, resource counters and retained failures; unsupported resize semantics remain explicit.
Handoff: Last completed substep, changed paths/symbols, unresolved arbitration or missing portable capability, and next bounded action.
Blocked behavior: Leave `MWX-1.4` unchecked with owner, unblock condition and retry trigger; continue dependency-ready work and stop when none remains.

### Task MWX-1.5 — Adapt asset and embed actions to mobile host capabilities

- [ ] MWX-1.5 Adapt asset and embed actions to mobile host capabilities.

Purpose: Make existing asset/attachment/embed actions reachable from mobile browsers with explicit host authority and fallbacks.
Context: `packages/web/src/modules/assets/`; `packages/web/src/modules/images/`; `packages/web/src/modules/embeds/`; `tests/browser/mobile-extensions/assets.spec.ts`; `../architecture/specs/rich-content-extensions.md`; [case catalog](../tests/mobile-extension-cases.md).
Dependencies: MWX-1.1.
Session scope: One mobile asset-action presenter boundary, normally 15–45 minutes plus focused checks; split broader host asset work through the controller.
Acceptance: MWX-C17–MWX-C20 pass. Explicit labeled file/camera affordances use declared host/browser capabilities and retain file-selection fallback when capture is absent, declined or canceled. Opening content does not request camera permission, fetch arbitrary images, start an upload or activate an embed. Pending/offline/denied/revoked and alt-text states remain usable; object URLs, decode work and host requests obey existing limits and cleanup.

Implementation:

- [ ] MWX-1.5-I1 Wire tap actions to the existing host asset port and bounded file input path; expose camera capture only as an optional user-initiated affordance, never as a required API or implicit live-camera session. Preserve stable targets across picker/background transitions. Keep embed activation explicit with a reachable exit/focus path and return to a safe card on rejection.

Validation:

- [ ] MWX-1.5-V1 `npm run test:mobile-extensions -- --group assets`. Create prepared files, mixed image/file/HTML clipboard payloads and mocked picker/asset/embed results for absent, canceled, denied, delayed, oversized and revoked states. Assert owning import precedence prevents duplicate insertion, no automatic permission/network work, no stale mutation, preserved selection and released decode/object-URL resources. Actual picker/capture/native clipboard behavior is qualified separately in MWX-1.8 with non-sensitive local fixtures. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWX-1.5` links per-ID results, resource/authority assertions and preserved failures; optional capture support is recorded per device.
Handoff: Last completed substep, changed paths/symbols, missing host capability or failing lifecycle case, and next bounded action.
Blocked behavior: Leave `MWX-1.5` unchecked with owner, unblock condition and retry trigger; continue dependency-ready work and stop when none remains.

### Task MWX-1.6 — Provide import export and share fallbacks

- [ ] MWX-1.6 Provide import export and share fallbacks.

Purpose: Connect existing format capabilities to mobile browser file and sharing controls without depending on optional browser APIs.
Context: `packages/web/src/modules/formats/`; `tests/browser/mobile-extensions/formats.spec.ts`; `../architecture/specs/document-conversion.md`; `../architecture/specs/formats.md`; [case catalog](../tests/mobile-extension-cases.md).
Dependencies: MWX-1.1.
Session scope: One format-action presenter and fallback boundary, normally 15–45 minutes plus focused checks; portable parser/converter changes remain with track 27.
Acceptance: MWX-C21–MWX-C24 pass. Import/export menus advertise only qualified direction/fidelity profiles, including PDF export only. File-system, clipboard and share APIs are feature/permission/activation checked; absent or rejected APIs leave an explicit file-input, download or selectable-text/manual-copy path as appropriate. Cancellation preserves the document and generated output remains recoverable when sharing fails. Large preparation is bounded/cancelable and revision-checked.

Implementation:

- [ ] MWX-1.6-I1 Adapt existing conversion/file commands and preview/confirm flows to reachable mobile controls. Separate prepare/download/share success, preserve requested filenames/media types, and expose manual recovery instructions when a browser cannot deliver an artifact. Use immutable snapshots or captured import anchors and existing size/fidelity/error limits; opening the menu starts no conversion or permission request.

Validation:

- [ ] MWX-1.6-V1 `npm run test:mobile-extensions -- --group formats`. Create deterministic prepared artifacts and mocked absent/denied/canceled API variants, stale imports and over-limit inputs. Assert truthful outcome/fidelity labels, recoverable bytes, no unconfirmed import mutation and bounded cleanup. Actual file/download/share outcomes require MWX-1.8 device observations; mocks do not prove OS delivery. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, immutable revisions and artifact hashes.

Evidence: Separate progress entry `MWX-1.6` links artifact hashes, semantic/fallback assertions and retained failures with API support recorded separately.
Handoff: Last completed substep, changed paths/symbols, unresolved browser delivery or owning format defect, and next bounded action.
Blocked behavior: Leave `MWX-1.6` unchecked with owner, unblock condition and retry trigger; continue dependency-ready work and stop when none remains.

### Task MWX-1.7 — Integrate qualified web assistance controls

- [ ] MWX-1.7 Integrate qualified web assistance controls.

Purpose: Verify optional web assistance alongside mobile presenters without weakening ordinary OS input and accessibility.
Context: `packages/web/src/modules/assistive-input.ts`; `tests/browser/mobile-extensions/assistance.spec.ts`; `tests/manual/assistive-input-web.md`; `../architecture/specs/assistive-input.md`; [case catalog](../tests/mobile-extension-cases.md).
Dependencies: MWX-1.1, MWX-1.2.
Additional entry gate: AIN-1.2, AIN-1.3 and AIN-1.10 from `39-assistive-input.md` have passing exact-revision web presenter, lifecycle and physical or virtual platform evidence. Native/TUI AIN tasks and whole-track 39 completion are not prerequisites for this parent or any independent parent above.
Session scope: One integration boundary against qualified web assistance, normally 15–45 minutes plus focused checks; propose a split if upstream evidence needs broader requalification.
Acceptance: MWX-C25–MWX-C28 pass. Named assistance controls are reachable around virtual keyboards and magnified viewports, respect native selection/composition and restore focus predictably. Actual VoiceOver/TalkBack and supported voice-control observations retain visible-name parity, bounded status and cancel/recovery access. Disabling assistance leaves baseline OS dictation, screen-reader editing and ordinary commands available. Optional prepared host results still use AIN's session/anchor/history contract.

Implementation:

- [ ] MWX-1.7-I1 Reuse qualified AIN controls/session logic and track 40 focus/geometry primitives; adapt only the mobile presenter integration. Add enabled/disabled, permission/unsupported, stale target and teardown combinations to the case index. Keep the OS text-input route and explicit injected host capability distinct; add no speech provider, raw audio path or new command parser.

Validation:

- [ ] MWX-1.7-V1 `npm run test:mobile-extensions -- --group assistance`; reuse AIN web protocol rows for the consumed revision and execute changed mobile integration rows in MWX-1.8. Use prepared transcripts/mock transports only in automation. Assert selection/history, focus and resource outcomes; record real OS/AT observations separately with nonzero counts. Record exact commands/exits, immutable source/implementation/fixture/device revisions and artifact hashes; no provider-quality or spend claim follows from prepared results.

Evidence: Separate progress entry `MWX-1.7` links upstream AIN receipts, per-ID outcomes, enabled/disabled capability distinctions and retained failures.
Handoff: Last completed substep, changed paths/symbols, missing AIN evidence or failing mobile integration, and next bounded action.
Blocked behavior: Leave `MWX-1.7` unchecked with owner, unblock condition and retry trigger; missing AIN evidence permits independent ready MWX work, never a substituted native or synthetic proof.

### Task MWX-1.9 — Expose touch formatting and extension paste commands

- [ ] MWX-1.9 Expose touch formatting and extension paste commands.

Purpose: Deliver the named transfer boundary with reproducible evidence and explicit qualification status.
Context: `packages/web/src/modules/`; `tests/browser/mobile-extension-formatting.spec.ts`; `tests/manual/mobile-web-extensions.md`; `../architecture/specs/rich-content-extensions.md`; [mobile clipboard cases](../tests/mobile-web-cases.md)
Dependencies: MWX-1.3, MWX-1.6.
Session scope: One named boundary; target 15–45 minutes plus focused validation. These are future tasks; this roadmap revision does not execute native tests or authorize device runs.
Acceptance: Touch users can apply every advertised table-cell/caption/reference/extension format and choose formatted or literal paste without desktop-only shortcuts. Captured cell/text selections survive pointerdown/blur/click and native paste menus. Physical-or-virtual platform support remains the final MWX-1.8 gate; authoring and viewport replay alone do not qualify target-platform behavior.

Implementation:

- [ ] MWX-1.9-I1 Wire the shared extension formatting capability map into reachable labeled mobile controls. Add table rectangle/text selection, menu paste, beforeinput-only and noncancelable replacement, optional plain-paste action, disabled-codec/source-preserving fallback, async cancellation and two-editor fixtures. Extend the device runbook for physical iPhone/iPad and Android OS clipboard flows.

Validation:

- [ ] MWX-1.9-V1 `npm run test:browser -- mobile-extension-formatting`. Execute deterministic browser mechanics only in this future implementation task; hand off physical-device cases to MWX-1.8. Require nonzero matching cases and record executed/passed/failed/skipped counts, immutable fixture/source/package revisions and preserved failures. Missing required runtime tooling, failed behavior or untested mandatory cases do not qualify support; use accepted virtual runtimes/equivalents when physical hardware is unavailable.

Evidence: Separate progress entry with commands, exact environment and artifact hashes; catalogs remain planned until the corresponding runs exist.
Handoff: Last completed substep, unavailable environment or failing case, owner and next bounded action.
Blocked behavior: Leave unchecked; name owner, unblock condition and retry trigger. Accept target-platform simulators/emulators/VMs under verification.md and retain virtual provenance; never relabel their results as physical-device observations.

### Task MWX-1.8 — Qualify platform runtimes and bounded extension overhead

- [ ] MWX-1.8 Qualify platform runtimes and bounded extension overhead.

Purpose: Produce a truthful mobile-extension capability record from actual browser behavior and production artifacts.
Context: `tests/manual/mobile-web-extensions.md`; `benchmarks/browser/mobile-extensions/`; `tests/browser/mobile-extensions/qualification.test.mjs`; `../architecture/evidence/mobile-web-extensions/`; `../architecture/specs/mobile-web.md`; `../architecture/specs/verification.md`; [case catalog](../tests/mobile-extension-cases.md). [additional interaction cases](../tests/desktop-editing-cases.md).
Dependencies: MWX-1.2, MWX-1.3, MWX-1.4, MWX-1.5, MWX-1.6, MWX-1.7, MWX-1.9.
Session scope: One reviewed mobile-extension release-profile boundary, normally 15–45 minutes plus focused checks; if the declared physical or virtual platform matrix exceeds this, obtain a controller-reviewed split retaining all required cells before execution.
Acceptance: MWX-C29–MWX-C32 and all mandatory catalog rows have passing exact-revision assertions/observations. Physical or simulated iPhone/iOS Safari and iPad/iPadOS Safari, plus physical or emulated Android/Chrome evidence covers touch, OS selection, keyboard/viewport, scrolling/zoom and relevant VoiceOver/TalkBack; emulation, synthetic events and Playwright WebKit remain distinct. Every extension's disabled bundle/assets/resource/network contribution is zero; enabled contributions and responsiveness fit limits declared in MWX-1.1 and existing baseline budgets. Missing required runtime/equivalent evidence, stale artifacts or failed mandatory rows block qualification; unavailable physical hardware alone does not. Record actual official-preset FPX combinations and PRF continuous-input/resource evidence on real devices; desktop keyboard shortcuts are insufficient.

Implementation:

- [ ] MWX-1.8-I1 Create the bounded physical or virtual platform protocol and capability receipts; record device/browser/OS/keyboard/locale/AT versions, pointer mode, viewport/zoom/orientation and feature set. Reuse upstream observations only at matching consumed revisions, then execute new/changed rows. Measure per-feature and combined production JS/WASM/CSS/assets, cold/lazy loads, p50/p95/p99 input/frame latency, geometry/invalidation work, long tasks, memory plateau and resource cleanup against extension-disabled consumers. Record raw samples, limits and supported/unsupported/pending cells without altering a failed threshold after measurement.

Validation:

- [ ] MWX-1.8-V1 `npm run test:mobile-extensions -- --group all`; `npm run bench:mobile-extensions -- --profile release`; `node --test tests/browser/mobile-extensions/qualification.test.mjs`; execute `tests/manual/mobile-web-extensions.md` on the required physical or target-platform virtual runtimes. Create the benchmark, receipt validator and manual protocol here; validate evidence freshness/completeness without treating validation as device execution. Record separate automated/benchmark/manual/validator commands, nonzero counts, failures/skips, raw artifact hashes and source/implementation/fixture revisions. Close task-owned browsers/servers, verify resources/listeners are released and record disk hygiene required by the workspace instructions.

Evidence: Separate progress entry `MWX-1.8` links reviewed limits, raw measurements, per-ID/device receipts and retained failures under `../architecture/evidence/mobile-web-extensions/`; hand off qualified profiles to expanded qualification and public capability documentation.
Handoff: Last completed substep, device/profile or source revision, exact missing/failed row and next bounded action.
Blocked behavior: Leave `MWX-1.8` unchecked with owner, required environment/evidence and retry trigger. Do not relabel a missing required device unsupported merely to finish; request a scope decision or stop with the unmet gate.

## Shared suite handoff

Use the RGS driver, fixture bindings and receipt format from [the editing suite](../specs/editing-regression-suite.md), inherited through track 40. MWX cases retain their own variants and device observations; sharing a fixture link or passing metadata validation cannot mark a mobile-extension case complete.
