# Deliver Apple and Android persistence adapters

Status: PLANNED

## Goal and entry conditions

Deliver the 09-apple-android milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: 00-contracts BSC-1.6/1.7 and the private/hosted authority from 01 provide shared outcomes. Native tasks require only their actual current-format engine/Session/FFI and target surface exports owned by tracks 09/16/17/18; record exact accepted source/check selectors. Missing surfaces block dependent UI work, not unrelated headless transport. Preserve native-parity.md and track 43 observation ownership.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is functional delivery. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/09-apple-android.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

## Epic BNA-1 — Deliver Apple and Android persistence adapters

### Task BNA-1.1 — Add the Swift storage and authority facade

- [ ] BNA-1.1 Add the Swift storage and authority facade.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/apple/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Typed Swift async identity/receipt/transport facade wraps existing native Session/FFI; actor isolation respects its single owner and cancellation preserves uncertain saves.

Implementation:

- [ ] BNA-1.1-I1 Add the Swift storage and authority facade. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BNA-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BNA-1.1`: Compile one Swift headless consumer with a prepared save/lookup and fresh-writer checkpoint reopen. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BNA-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BNA-1.2 — Add UIKit persistence host integration

- [ ] BNA-1.2 Add UIKit persistence host integration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/apple/UIKit/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BNA-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Existing UIKit editor host exposes local/remote state, policy and transport binding without a second text/history model; view disposal releases only owned tasks.

Implementation:

- [ ] BNA-1.2-I1 Add UIKit persistence host integration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BNA-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BNA-1.2`: One existing UIKit host delivery fixture wires a prepared save and dispose; actual target-runtime observations transfer to final native testing/43. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BNA-1.2 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BNA-1.3 — Add SwiftUI representable integration

- [ ] BNA-1.3 Add SwiftUI representable integration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/apple/SwiftUI/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BNA-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Representable/coordinator wraps the existing UIKit/AppKit surface and Session; view recomposition does not recreate the document or replay a value import.

Implementation:

- [ ] BNA-1.3-I1 Add SwiftUI representable integration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BNA-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BNA-1.3`: Compile one SwiftUI consumer and use the existing host fixture to verify repeated update calls retain one session identity. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BNA-1.3 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BNA-1.4 — Add AppKit persistence host integration

- [ ] BNA-1.4 Add AppKit persistence host integration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/apple/AppKit/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BNA-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: macOS native host shares Swift facade and engine undo/selection, with explicit window/document close recovery and application-owned URL/credential policy.

Implementation:

- [ ] BNA-1.4-I1 Add AppKit persistence host integration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BNA-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BNA-1.4`: One existing macOS host fixture reports pending work on a prepared denied save and does not claim close saved it. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BNA-1.4 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BNA-1.5 — Add the Kotlin Android coroutine facade

- [ ] BNA-1.5 Add the Kotlin Android coroutine facade.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/android/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Existing Android engine binding receives typed storage/authority operations, structured cancellation and exact receipt scope without blocking input on network I/O.

Implementation:

- [ ] BNA-1.5-I1 Add the Kotlin Android coroutine facade. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BNA-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BNA-1.5`: Compile one Kotlin headless consumer and run a prepared uncertain-write lookup through the existing Session binding. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BNA-1.5 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BNA-1.6 — Add Android Views lifecycle integration

- [ ] BNA-1.6 Add Android Views lifecycle integration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/android/views/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BNA-1.5.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Native editor View binds to the host lifecycle and saved document identity; reattachment/rotation cannot reinitialize or duplicate writer identity.

Implementation:

- [ ] BNA-1.6-I1 Add Android Views lifecycle integration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BNA-1.6-V1 Run `node scripts/sdk-adapter-delivery.mjs BNA-1.6`: One existing View fixture detaches/reattaches with prepared transport and one stable document/fresh live writer on reopen. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BNA-1.6 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BNA-1.7 — Add Jetpack Compose integration

- [ ] BNA-1.7 Add Jetpack Compose integration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/android/compose/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BNA-1.5, BNA-1.6.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: AndroidView/composable state wraps the existing native View, stable session holder and save-state flow without rebuilding text on recomposition.

Implementation:

- [ ] BNA-1.7-I1 Add Jetpack Compose integration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BNA-1.7-V1 Run `node scripts/sdk-adapter-delivery.mjs BNA-1.7`: Compile the minimal Compose consumer and run a prepared recomposition fixture showing one active session/subscription. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BNA-1.7 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BNA-1.8 — Add native background and restoration hooks

- [ ] BNA-1.8 Add native background and restoration hooks.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/apple/; adapters/native/android/; examples/sdk-adapters/native/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BNA-1.2, BNA-1.3, BNA-1.4, BNA-1.6, BNA-1.7.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: App suspension requests bounded local flush or recovery export; background task/network expiry never implies remote receipt; process recreation loads committed bytes before editing.

Implementation:

- [ ] BNA-1.8-I1 Add native background and restoration hooks. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BNA-1.8-V1 Run `node scripts/sdk-adapter-delivery.mjs BNA-1.8`: One prepared suspend/timeout/reopen transcript per shared facade preserves pending outbox and exact identity; remaining OS observations are explicitly registered. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BNA-1.8 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Summarize delivered source interfaces and capability flags, focused selectors/results, true prerequisite gaps and remaining final qualification in `.roadmap-runner/backend-sdk-adapters-20261024/09-apple-android.progress.md`. Do not copy hashes/delivery summaries into this source. The two final testing files own comprehensive case authoring and qualification; functional completion alone is not whole-plan completion.
