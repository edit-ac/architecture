# Deliver Flutter and React Native bridges

Status: PLANNED

## Goal and entry conditions

Deliver the 11-flutter-react-native milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: 00-contracts BSC-1.6/1.7; 09-apple-android BNA-1.2/1.4/1.6/1.8 provide existing native surfaces, stable handles and restoration hooks. Only a platform actually used by a task must be present. Desktop Flutter requires the matching 10-desktop-hosts surface export; unsupported combinations remain explicit. Browser framework packages are not substitutes for native widgets.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is functional delivery. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/11-flutter-react-native.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

## Epic BCP-1 — Deliver Flutter and React Native bridges

### Task BCP-1.1 — Implement the Dart authority client

- [ ] BCP-1.1 Implement the Dart authority client.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: sdk/dart/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Typed async client preserves exact bytes/receipt identities, explicit HTTP ownership, cancellation and uncertain-write lookup; no native engine is implied by client availability.

Implementation:

- [ ] BCP-1.1-I1 Implement the Dart authority client. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BCP-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BCP-1.1`: One prepared save/lost-response lookup and binary round-trip through a local Dart consumer match the shared oracle. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BCP-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BCP-1.2 — Add Flutter platform bridge ownership

- [ ] BCP-1.2 Add Flutter platform bridge ownership.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/flutter/platform/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BCP-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Plugin maps stable handles and save/flush/dispose events to existing Swift/Kotlin native Sessions with bounded method/event channels; unsupported platform returns typed capability failure.

Implementation:

- [ ] BCP-1.2-I1 Add Flutter platform bridge ownership. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BCP-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BCP-1.2`: Compile iOS/Android plugin entry points and run one prepared event ordering/dispose fixture against the existing native host bridge. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BCP-1.2 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BCP-1.3 — Add the Flutter native editor widget

- [ ] BCP-1.3 Add the Flutter native editor widget.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/flutter/widget/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BCP-1.2.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Widget embeds supported native editor views with one engine/session and explicit focus/composition/selection ownership; rebuild does not reimport text or create another undo stack.

Implementation:

- [ ] BCP-1.3-I1 Add the Flutter native editor widget. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BCP-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BCP-1.3`: One existing native host delivery fixture plus widget rebuild/dispose smoke preserves document identity and save state. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BCP-1.3 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BCP-1.4 — Add React Native native modules

- [ ] BCP-1.4 Add React Native native modules.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/react-native/bridge/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Native module/Fabric ownership uses existing Swift/Kotlin sessions, bounded events and stable IDs; JS teardown invalidates late callbacks and credentials remain application-owned.

Implementation:

- [ ] BCP-1.4-I1 Add React Native native modules. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BCP-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BCP-1.4`: Compile both native module entry points and run one prepared save/dispose callback transcript without mounting a WebView. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BCP-1.4 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BCP-1.5 — Add React Native editor components

- [ ] BCP-1.5 Add React Native editor components.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/react-native/component/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BCP-1.4.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Component embeds actual native surfaces and maps focus/read-only/save-state without controlled-value reimports, duplicate writer sessions or a private history stack.

Implementation:

- [ ] BCP-1.5-I1 Add React Native editor components. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BCP-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BCP-1.5`: One existing native view fixture and JS remount smoke preserve current checkpoint identity and explicit recovery on failed save. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BCP-1.5 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BCP-1.6 — Add cross-platform application examples

- [ ] BCP-1.6 Add cross-platform application examples.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: examples/sdk-adapters/flutter/; examples/sdk-adapters/react-native/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BCP-1.3, BCP-1.5.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Each example declares supported OS/host combinations and demonstrates canonical save/load, local/remote statuses and explicit offline recovery through the same backend contract.

Implementation:

- [ ] BCP-1.6-I1 Add cross-platform application examples. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BCP-1.6-V1 Run `node scripts/sdk-adapter-delivery.mjs BCP-1.6`: Compile the declared local example entry points and run one shared prepared save/reopen transcript per bridge; target-runtime observation remains final-owned. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BCP-1.6 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Summarize delivered source interfaces and capability flags, focused selectors/results, true prerequisite gaps and remaining final qualification in `.roadmap-runner/backend-sdk-adapters-20261024/11-flutter-react-native.progress.md`. Do not copy hashes/delivery summaries into this source. The two final testing files own comprehensive case authoring and qualification; functional completion alone is not whole-plan completion.
