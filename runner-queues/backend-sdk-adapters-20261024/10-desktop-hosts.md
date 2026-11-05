# Deliver desktop host integration and C++ interoperability

Status: PLANNED

## Goal and entry conditions

Deliver the 10-desktop-hosts milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: 00-contracts BSC-1.6/1.7; 07-ruby-c-cpp BRC-1.5/1.6 for C/C++ consumers; 03-typescript-node BTS-1.8 for browser desktop shells. Actual WinUI/GTK/current native surface exports remain owned by tracks 22/23; Windows/Linux follow existing web-feature-complete sequencing. Each family below has only its named prerequisites.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is functional delivery. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/10-desktop-hosts.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

## Epic BDH-1 — Deliver desktop host integration and C++ interoperability

### Task BDH-1.1 — Add the .NET native Session bridge

- [ ] BDH-1.1 Add the .NET native Session bridge.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/windows/bridge/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: C# SafeHandle/callback ownership wraps the current native ABI and single-owner Session, separate from the .NET HTTP client; late callbacks cannot reach disposed UI.

Implementation:

- [ ] BDH-1.1-I1 Add the .NET native Session bridge. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BDH-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BDH-1.1`: Compile one headless .NET native consumer against current ABI and dispose during a prepared save callback. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BDH-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BDH-1.2 — Add WinUI host save/load integration

- [ ] BDH-1.2 Add WinUI host save/load integration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/windows/winui/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BDH-1.1.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Existing Windows native surface binds one Session to application policy/local store/authority facade and retains engine undo/selection; no WebView substitute is claimed.

Implementation:

- [ ] BDH-1.2-I1 Add WinUI host save/load integration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BDH-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BDH-1.2`: One existing WinUI host fixture wires a prepared load/save and close-recovery state; OS observations remain final-owned. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BDH-1.2 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BDH-1.3 — Add a WPF native host wrapper

- [ ] BDH-1.3 Add a WPF native host wrapper.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/windows/wpf/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BDH-1.1, BDH-1.2.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: A bounded interop wrapper embeds the qualified Windows native surface and shared Session; no independent WPF text renderer/history stack is introduced and unsupported hosting returns a capability error.

Implementation:

- [ ] BDH-1.3-I1 Add a WPF native host wrapper. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BDH-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BDH-1.3`: Compile one WPF host consumer with a named existing Windows surface; if embedding is unavailable record the exact missing host API and split before adding a new renderer. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BDH-1.3 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BDH-1.4 — Add GTK persistence integration

- [ ] BDH-1.4 Add GTK persistence integration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/linux/gtk/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Existing GTK native surface consumes shared C/Session boundaries with UTF-16 conversion and save-state/lifetime signals; disposal preserves pending recovery.

Implementation:

- [ ] BDH-1.4-I1 Add GTK persistence integration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BDH-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BDH-1.4`: One existing GTK host fixture wires prepared save/conflict and exact checkpoint reopen without resetting selection/history on network attachment. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BDH-1.4 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BDH-1.5 — Deliver Qt headless use and a bounded GUI decision

- [ ] BDH-1.5 Deliver Qt headless use and a bounded GUI decision.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/qt/; sdk/cpp/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Qt/C++ application can use headless persistence safely; a 30-minute probe records native surface feasibility, required platform APIs and a concrete follow-up if no existing surface embeds; GUI support stays unqualified.

Implementation:

- [ ] BDH-1.5-I1 Deliver Qt headless use and a bounded GUI decision. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BDH-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BDH-1.5`: Compile one Qt headless checkpoint consumer and record the GUI probe's reproducible result; no generic full Qt renderer is a completion requirement here. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BDH-1.5 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BDH-1.6 — Add Electron process-boundary integration

- [ ] BDH-1.6 Add Electron process-boundary integration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/electron/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Browser editor stays renderer-owned; preload/main handles allowlisted document operations and application credentials through bounded IPC, without node access from editor content.

Implementation:

- [ ] BDH-1.6-I1 Add Electron process-boundary integration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BDH-1.6-V1 Run `node scripts/sdk-adapter-delivery.mjs BDH-1.6`: One local prepared save/load across actual preload IPC denies an arbitrary operation and closes owned listeners; tear down the test shell. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BDH-1.6 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BDH-1.7 — Add Tauri host integration

- [ ] BDH-1.7 Add Tauri host integration.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: adapters/native/tauri/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Browser editor talks to allowlisted Rust commands using existing authority/storage ports; web host capabilities are explicit and document content cannot invoke arbitrary filesystem/network operations.

Implementation:

- [ ] BDH-1.7-I1 Add Tauri host integration. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BDH-1.7-V1 Run `node scripts/sdk-adapter-delivery.mjs BDH-1.7`: Compile one local Tauri consumer and execute one prepared command-boundary save/denial fixture without publishing or signing. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BDH-1.7 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BDH-1.8 — Add desktop application recipes and close policy

- [ ] BDH-1.8 Add desktop application recipes and close policy.

Purpose: Make this integration boundary usable without application-owned protocol reimplementation.
Deliverable: examples/sdk-adapters/desktop/.
Context: [SDK contract: Planned support matrix](../../specs/backend-sdk-adapters.md#planned-support-matrix); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BDH-1.2, BDH-1.3, BDH-1.4, BDH-1.5, BDH-1.6, BDH-1.7.
Independent work: Select only siblings with validated entry capabilities and local prerequisites.
Session scope: One boundary, 15–45 minutes including checks; split before expanding missing APIs or matrices.
Acceptance: Windows, GTK, Qt headless, Electron and Tauri recipes identify native vs browser surface, capability gaps, thread ownership and unsaved-close policy without assuming every toolkit ships every renderer.

Implementation:

- [ ] BDH-1.8-I1 Add desktop application recipes and close policy. Reuse the existing owner and wire the minimum usable consumer at the named paths. Register its focused selector; defer comprehensive suites.

Validation:

- [ ] BDH-1.8-V1 Run `node scripts/sdk-adapter-delivery.mjs BDH-1.8`: Compile documented recipe entry points and reuse prior prepared close/reopen evidence; no repeated device matrix. Budget: 1–3 minutes, or at most 5 minutes for a declared compiler/package/database startup; reuse unchanged passing prerequisite results.

Evidence: Progress path above; changed source inputs, actual command/runtime/exit and meaningful pass/fail/skip counts. Contract inspections record cases, not invented test results.
Handoff: Delivered interface, last substep, failing input/selector and next bounded action.
Blocked behavior: Leave BDH-1.8 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Summarize delivered source interfaces and capability flags, focused selectors/results, true prerequisite gaps and remaining final qualification in `.roadmap-runner/backend-sdk-adapters-20261024/10-desktop-hosts.progress.md`. Do not copy hashes/delivery summaries into this source. The two final testing files own comprehensive case authoring and qualification; functional completion alone is not whole-plan completion.
