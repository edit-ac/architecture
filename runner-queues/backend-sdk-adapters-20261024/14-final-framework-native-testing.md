# Complete framework and native integration testing

Status: PLANNED

## Goal and entry conditions

Deliver the 14-final-framework-native-testing milestone of the backend SDK and framework adapter plan. Planning source dated 2026-10-24; no task is implemented or qualified by this document. Workspace: `core`; affected implementation paths below are core-relative and proposed until ownership inventory reconciles them.

Entry: All functional files 00–12 are delivered, and 13-final-backend-testing supplies the backend results needed for combined end-to-end claims. Existing browser baseline and native capability rules remain applicable. Compilation/prepared bridge checks cannot replace actual target-runtime observations: register the new cases under track 43 and consume their executed results before qualifying the corresponding platform.

Authority: [backend SDK contract](../../specs/backend-sdk-adapters.md), specifically the sections named by each task; [canonical durability](../../specs/document-durability.md) and [single-format policy](../../decisions/006-single-format-before-publication.md) remain authoritative. Read the current milestone and named code only; the controller index and other language roadmaps are not worker input.

## Execution and validation rules

This file is final testing. One parent is one 15–45 minute session including focused validation, normally one API or adapter boundary. If inspection shows more work, stop with a concrete split proposal before exceeding that scope; never mark a partial package complete. Required earlier-file selectors/results are in their separate progress files under `.roadmap-runner/backend-sdk-adapters-20261024/` (architecture-relative, ignored). Queue position does not prove prerequisites.

Use one current document format and existing Rust engine/Session; no independent CRDT, migration, reseed, provider credential or paid inference. All automated requests use deterministic prepared data and local/mock transports. Missing real database/target-runtime evidence remains a blocker for that claim; it is never replaced by a fixture pass. Preserve exact original bytes, dirty work and real data. Check official maintained versions when implementing a family; do not assume every historical runtime is supported.

The named delivery selector commands below are PLANNED, core-root-relative interfaces of `scripts/sdk-adapter-delivery.mjs`, introduced by BSC-1.7. Each task registers its own focused selector over the declared package compiler/existing fixture or minimal prepared risk check; a missing selector is an error, never a pass. No broad suite is hidden behind a delivery selector. Contracts before BSC-1.7 use the direct local inspection/lint described in Validation instead. New comprehensive tests and matrix work belong only to the two final testing files. Record actual commands and runtime versions at execution, not fabricated current results.

No runner start, enqueue, registry publication, deployment, signing, production access or live dogfood is authorized here. Adopt only at the existing coordinator’s safe checkpoint under the guard and live readiness receipt; use one root controller. Source edits follow installed runner policy: workers update only verified checkboxes/Status, with hashes, results and handoff in ignored progress. Stop on BLOCKED or unchanged failed input; record a precise resume condition rather than retry loops.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/14-final-framework-native-testing.progress.md` (architecture-relative; never commit generated reports). Keep the minimal diagnostics for an active failure; remove inactive reproducible session artifacts after debugging. Do not create routine evidence archives.

## Epic BNT-1 — Complete framework and native integration testing

### Task BNT-1.1 — Build the final adapter observation register

- [ ] BNT-1.1 Build the final adapter observation register.

Purpose: Reuse shared SDK behavior while delivering this named integration boundary.
Deliverable: tests/sdk-adapters/hosts/; sdk/contracts/qualification.json.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: none (only the relevant entry condition above).
Independent work: Other tasks with validated entry capabilities and local prerequisites remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: Each host requirement H01–H06 has one final owner, declared runtime/OS/framework versions and exact existing track 43 observation handoff; retained evidence is reused and actual missing environments remain outstanding.

Implementation:

- [ ] BNT-1.1-I1 Build the final adapter observation register. Reuse compatible evidence; author only uncovered cases and connect runtime results to the named qualification owner.

Validation:

- [ ] BNT-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BNT-1.1` as a bounded final selector: Validate case ownership and platform manifest; every native/framework combination has supported or explicit unsupported disposition. Budget: at most 10 minutes of execution per selected boundary; shard a larger matrix into controller-defined parents before running.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BNT-1.2 — Verify SSR, forms and component lifetimes

- [ ] BNT-1.2 Verify SSR, forms and component lifetimes.

Purpose: Reuse shared SDK behavior while delivering this named integration boundary.
Deliverable: tests/sdk-adapters/hosts/web/.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BNT-1.1.
Independent work: Other tasks with validated entry capabilities and local prerequisites remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: Actual declared web frameworks demonstrate no SSR engine/network sessions, isolated requests/editors, stable hydration, explicit reset, conflict preservation and disposal without active owned work. Filament/Livewire Resource and action-modal fields additionally cover nested/repeater state paths, validation/readonly, lazy assets, rerender/navigation, submit vs independent autosave, canceled modal and no duplicate session or false receipt.

Implementation:

- [ ] BNT-1.2-I1 Verify SSR, forms and component lifetimes. Reuse compatible evidence; author only uncovered cases and connect runtime results to the named qualification owner.

Validation:

- [ ] BNT-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BNT-1.2` as a bounded final selector: Execute uncovered actual framework mount/SSR/navigation/form cases only; reuse accepted common editor baseline results at the same inputs. Budget: at most 10 minutes of execution per selected boundary; shard a larger matrix into controller-defined parents before running.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BNT-1.3 — Verify native text and widget bridging

- [ ] BNT-1.3 Verify native text and widget bridging.

Purpose: Reuse shared SDK behavior while delivering this named integration boundary.
Deliverable: tests/sdk-adapters/hosts/native/.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BNT-1.1.
Independent work: Other tasks with validated entry capabilities and local prerequisites remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: On declared simulator/emulator/OS hosts, Apple/Android/Windows/GTK/Flutter/RN native surfaces retain composition, selection, accessibility hooks and engine undo while view recreation preserves identity; Qt GUI remains unsupported without its separate approved host work.

Implementation:

- [ ] BNT-1.3-I1 Verify native text and widget bridging. Reuse compatible evidence; author only uncovered cases and connect runtime results to the named qualification owner.

Validation:

- [ ] BNT-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BNT-1.3` as a bounded final selector: Run new adapter cases through actual target runtimes registered with track 43; compile-only rows and unavailable hosts remain unqualified. Budget: at most 10 minutes of execution per selected boundary; shard a larger matrix into controller-defined parents before running.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BNT-1.4 — Verify offline recovery and background lifecycle

- [ ] BNT-1.4 Verify offline recovery and background lifecycle.

Purpose: Reuse shared SDK behavior while delivering this named integration boundary.
Deliverable: tests/sdk-adapters/hosts/recovery/.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BNT-1.1.
Independent work: Other tasks with validated entry capabilities and local prerequisites remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: App suspend, component disposal, process recreation, expired auth and lost replies preserve exact checkpoint/tail/outbox and fresh writer identities; local and remote save status never merge.

Implementation:

- [ ] BNT-1.4-I1 Verify offline recovery and background lifecycle. Reuse compatible evidence; author only uncovered cases and connect runtime results to the named qualification owner.

Validation:

- [ ] BNT-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BNT-1.4` as a bounded final selector: Run uncovered deterministic failure cases plus exact runtime-owned interruption observations; compare restored bytes and receipt scope. Budget: at most 10 minutes of execution per selected boundary; shard a larger matrix into controller-defined parents before running.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BNT-1.5 — Verify desktop isolation and packaged consumers

- [ ] BNT-1.5 Verify desktop isolation and packaged consumers.

Purpose: Reuse shared SDK behavior while delivering this named integration boundary.
Deliverable: tests/sdk-adapters/hosts/packages/.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BNT-1.1.
Independent work: Other tasks with validated entry capabilities and local prerequisites remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: Electron/Tauri IPC, C/C++/.NET ownership and actual declared package installs honor bounds/capabilities; generated artifacts are absent from Git; no signing or publication is performed.

Implementation:

- [ ] BNT-1.5-I1 Verify desktop isolation and packaged consumers. Reuse compatible evidence; author only uncovered cases and connect runtime results to the named qualification owner.

Validation:

- [ ] BNT-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BNT-1.5` as a bounded final selector: Execute remaining local install and IPC/ABI ownership cases for the stated matrix, reusing family-specific passing consumers. Budget: at most 10 minutes of execution per selected boundary; shard a larger matrix into controller-defined parents before running.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BNT-1.6 — Verify resource teardown and adapter overhead

- [ ] BNT-1.6 Verify resource teardown and adapter overhead.

Purpose: Reuse shared SDK behavior while delivering this named integration boundary.
Deliverable: tests/sdk-adapters/hosts/resources/.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BNT-1.1.
Independent work: Other tasks with validated entry capabilities and local prerequisites remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: Repeated mount/save/dispose leaves no task-owned browsers, listeners, subscriptions or servers; optional collaboration loads only when enabled; existing final size/latency caps remain unweakened and unqualified targets are explicit.

Implementation:

- [ ] BNT-1.6-I1 Verify resource teardown and adapter overhead. Reuse compatible evidence; author only uncovered cases and connect runtime results to the named qualification owner.

Validation:

- [ ] BNT-1.6-V1 Run `node scripts/sdk-adapter-delivery.mjs BNT-1.6` as a bounded final selector: Run only uncovered bounded lifecycle/performance selections with deterministic content; inspect exact process ownership and clean session artifacts; no unchanged optimization campaign. Budget: at most 10 minutes of execution per selected boundary; shard a larger matrix into controller-defined parents before running.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BNT-1.8 — Verify Drupal field and entity integration

- [ ] BNT-1.8 Verify Drupal field and entity integration.

Purpose: Reuse shared SDK behavior while delivering this named integration boundary.
Deliverable: tests/sdk-adapters/hosts/drupal/; sdk/contracts/qualification.json.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); named SDK and Drupal source exports only.
Dependencies: BNT-1.1.
Independent work: Other tasks with validated entry capabilities and local prerequisites remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: Actual declared Drupal runtime proves proper Field API registration/config/cardinality/empty values, immutable old revisions, translation/moderation isolation, AJAX widget lifetime, safe formatter/cache/access and retention-aware deletion. Shared SDK byte/transaction/security evidence is reused; missing rich renderer/snapshot/environment stays unqualified.

Implementation:

- [ ] BNT-1.8-I1 Review BDR-1.1–1.9 delivery evidence and author only missing Drupal kernel/browser cases. Reuse BFT database/authorization results; assign exact remaining field/entity/cache observations to H07. Register the bounded final selector and record actual runtime/source coverage.

Validation:

- [ ] BNT-1.8-V1 Run `node scripts/sdk-adapter-delivery.mjs BNT-1.8`: Execute uncovered Drupal kernel/browser selectors on a real task-owned site; compare snapshot refs, rendered/cache/access outcomes and session teardown. Split a larger selected matrix before running. Budget: at most 10 minutes per selected boundary; split larger matrices before running and reuse unchanged results.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BNT-1.7 — Close whole-plan qualification and adoption handoff

- [ ] BNT-1.7 Close whole-plan qualification and adoption handoff.

Purpose: Reuse shared SDK behavior while delivering this named integration boundary.
Deliverable: sdk/contracts/qualification.json; sdk/contracts/adoption.md.
Context: [SDK contract: Acceptance, qualification and adoption](../../specs/backend-sdk-adapters.md#acceptance-qualification-and-adoption); source paths in Deliverable. Inspect actual exports before editing.
Dependencies: BNT-1.2, BNT-1.3, BNT-1.4, BNT-1.5, BNT-1.6, BNT-1.8.
Independent work: Other tasks with validated entry capabilities and local prerequisites remain eligible.
Session scope: One boundary, 15–45 minutes including checks; split larger missing APIs or matrices.
Acceptance: Every B/H requirement and package has executed acceptance or an explicit unresolved blocker; no failed/skipped row becomes COMPLETE; track 43/security/release owners receive exact case/result references and public distribution remains separately authorized.

Implementation:

- [ ] BNT-1.7-I1 Close whole-plan qualification and adoption handoff. Reuse compatible evidence; author only uncovered cases and connect runtime results to the named qualification owner.

Validation:

- [ ] BNT-1.7-V1 Run `node scripts/sdk-adapter-delivery.mjs BNT-1.7` as a bounded final selector: Audit current-source result coverage and totals; require 13-final-backend-testing completion for combined claims; no full-suite repetition without changed input or an explicit existing gate. Budget: at most 10 minutes of execution per selected boundary; shard a larger matrix into controller-defined parents before running.

Evidence: Ignored progress above; exact source/runtime/selector/exit and meaningful pass/fail/skip counts.
Handoff: Delivered interface, last substep, failed input and next bounded action.
Blocked behavior: Leave task unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Summarize delivered source interfaces and capability flags, focused selectors/results, true prerequisite gaps and remaining final qualification in `.roadmap-runner/backend-sdk-adapters-20261024/14-final-framework-native-testing.progress.md`. Do not copy hashes/delivery summaries into this source. The two final testing files own comprehensive case authoring and qualification; functional completion alone is not whole-plan completion.
