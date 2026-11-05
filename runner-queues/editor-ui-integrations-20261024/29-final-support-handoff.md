# Close UI support and adoption gates

Status: IN_PROGRESS

## Goal and entry conditions

Goal: Close UI support and adoption gates. Planning source: 2026-10-24. Workspace: `core`. This is final-testing work; no completed capability is implied.

Authority: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/29-final-support-handoff.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

Entry receipts are scoped to each parent below. Verify the named public interface and focused acceptance against its consumed source revision; a queued predecessor or whole-file title is not evidence. Earlier-file progress has the same basename under `.roadmap-runner/editor-ui-integrations-20261024/`; existing backend-owner receipts live under `.roadmap-runner/backend-sdk-adapters-20261024/`. Read only the named parent receipt.

Final-phase entry: all required functionality in files 00–25 is delivered. This is a testing-sequencing gate, not permission to require unrelated language SDKs. Within this file consume only the platform/semantic/backend receipts needed for the current case. Actual browser/native/AT observations are registered with and consumed from roadmap43; mock/compile results cannot substitute.

## Execution and validation rules

All implementation paths below are core-relative unless prefixed `../architecture` or `../docs`; proposed paths must be reconciled to existing exports before creating files. Read the owning repository AGENTS.md before edits. A missing bridge/semantic API belongs to its named existing owner; do not implement a parallel one in a UI package.

One parent is one 15–45 minute session including focused validation. Split at a concrete boundary before exceeding the budget, preserving its acceptance and stable ID mapping. Budget inputs to this file, its named contract section, required predecessor receipt and only affected code; the controller index and other milestone bodies are not mandatory worker input.

The future core command `node scripts/ui-integration-delivery.mjs <task-id>` is introduced by UIC-1.5. It is a planned selector interface, not an existing command or passing test claim. Each later task registers the smallest relevant existing compiler/fixture/manual-observation wrapper; unknown/missing selectors and zero-case runs fail. Contract tasks before that dispatcher use the explicit direct checks below. Functional checks normally take 1–3 minutes, at most 5 minutes for an already provisioned native compiler/startup. Cold SDK installation, broad suites and comprehensive case authoring do not fit a delivery check. Final-testing tasks may spend up to 10 minutes on one declared bounded selector; split longer profiles across parents before starting them.

Use deterministic documents and local/mock transports only: no paid inference, credentials loaded into tests, provider recording, paid cloud builds, production access, deployment or publication. Keep generated packages, binaries, screenshots and logs in ignored task-owned directories. Preserve source, real user data and active processes. Use one current format, engine, command/history and persistence authority.

Independent work: a sibling with satisfied local dependencies and named entry receipts is eligible; queue order is not a dependency. Stop the affected worker on BLOCKED, record task/source/error/prerequisite fingerprint, owner, attempted repair and exact changed-input resume condition. Do not retry unchanged input or skip acceptance. A serial queue cannot jump a blocked file: only the existing coordinator may adopt a different ready subset at a safe guarded checkpoint. No runner start, enqueue, state edits or snapshot replacement is authorized by this source.

Workers may update verified checkboxes and Status only under the current installed runner policy. Hashes, results and handoff prose stay in separate ignored progress. A checked functional parent means its own narrow checks passed; it does not claim final UI/platform/accessibility qualification. Reuse compatible evidence and name the changed input before rerunning or widening. Final test/case development is in files 26–29 after all functional delivery, with existing BNT and roadmap43 owners retained.

## Epic UTH-1 — Close UI support and adoption gates

### Task UTH-1.1 — Reconcile final case ownership and remaining failures

- [ ] UTH-1.1 Reconcile final case ownership and remaining failures.

Purpose: Reconcile final case ownership and remaining failures so applications can reuse this integration boundary.
Deliverable: `sdk/contracts/ui-support.json; ../architecture/runner-queues/editor-ui-integrations-20261024/adoption-map.md`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BNT-1.2](../dependency-closed-ui-20261025/81-host-final-cases.md), [BNT-1.3](../dependency-closed-ui-20261025/81-host-final-cases.md), [BNT-1.4](../dependency-closed-ui-20261025/81-host-final-cases.md), [BNT-1.5](../dependency-closed-ui-20261025/81-host-final-cases.md), [BNT-1.6](../dependency-closed-ui-20261025/81-host-final-cases.md), [UTN-1.2](27-final-native-ui-testing.md), [UTN-1.3](27-final-native-ui-testing.md), [UTN-1.4](27-final-native-ui-testing.md), [UTN-1.5](27-final-native-ui-testing.md), [UTN-1.6](27-final-native-ui-testing.md), [UTW-1.2](26-final-web-ui-testing.md), [UTW-1.3](26-final-web-ui-testing.md), [UTW-1.4](26-final-web-ui-testing.md), [UTW-1.5](26-final-web-ui-testing.md), [UTW-1.6](26-final-web-ui-testing.md), [UTW-1.7](26-final-web-ui-testing.md), [UTW-1.8](26-final-web-ui-testing.md), [UTW-1.9](26-final-web-ui-testing.md), [UTX-1.2](28-final-expo-flutter-testing.md), [UTX-1.3](28-final-expo-flutter-testing.md), [UTX-1.4](28-final-expo-flutter-testing.md), [UTX-1.5](28-final-expo-flutter-testing.md), [UTX-1.6](28-final-expo-flutter-testing.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Every required UI requirement has one final owner/result, and BNT/roadmap43 reused receipts match actual artifacts and profiles. Deferred or failed native/stack cases remain blockers for those support claims.

Implementation:

- [ ] UTH-1.1-I1 Compare new final UI results to existing semantic/input/lifecycle receipts and identify only missing or invalidated evidence.
- [ ] UTH-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTH-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UTH-1.1`: Validate support matrix versus exact passed/failed/skipped counts; no broad rerun unless a changed input invalidates prior evidence. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTH-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTH-1.2 — Close measured package and runtime cost profiles

- [ ] UTH-1.2 Close measured package and runtime cost profiles.

Purpose: Close measured package and runtime cost profiles so applications can reuse this integration boundary.
Deliverable: `sdk/contracts/ui-support.json; ../architecture/specs/verification.md`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTH-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Each shipped UI profile counts optional JS/CSS/native assets honestly, isolates unused peers and respects existing final hard caps; performance failures are not hidden by recategorization.

Implementation:

- [ ] UTH-1.2-I1 Consume BNT-1.6 and existing release/performance-owner measurements; add only uncovered UI dependency/overhead cases to their final owner.
- [ ] UTH-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTH-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UTH-1.2`: Inspect measured profile totals and run only a justified missing selector; use bounded optimization limits and leave unmet caps open. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTH-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTH-1.3 — Verify documented consumer paths and required stack support

- [ ] UTH-1.3 Verify documented consumer paths and required stack support.

Purpose: Verify documented consumer paths and required stack support so applications can reuse this integration boundary.
Deliverable: `../docs/content/docs/guides/; sdk/contracts/ui-support.json`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTH-1.1, UTH-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Plain/framework/shadcn/Laravel/Filament/native/Expo/Flutter required profiles have installable package evidence and accurate guides. Mobile/web stack gaps cannot be waived as desktop feasibility.

Implementation:

- [ ] UTH-1.3-I1 Review final documentation claims against actual peer/support manifests and qualified UI surfaces; remove premature claims while retaining open required work.
- [ ] UTH-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTH-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UTH-1.3`: Check docs/import links and consume existing installer receipts; identify exact missing profile instead of repeating all examples. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTH-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTH-1.4 — Produce safe coordinator handoff

- [ ] UTH-1.4 Produce safe coordinator handoff.

Purpose: Produce safe coordinator handoff so applications can reuse this integration boundary.
Deliverable: `../architecture/runner-queues/editor-ui-integrations-20261024/README.md; ignored progress`.
Context: [named contract section](../../specs/native-ui-integrations.md#acceptance-ownership); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTH-1.1, UTH-1.2, UTH-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: All required implementation and final acceptance is accounted for, remaining optional desktop feasibility work is explicit, and publication/start/enqueue remain separately authorized. Existing active sources/state were not changed by planning.

Implementation:

- [ ] UTH-1.4-I1 Record delivered interfaces, validated source revisions, source-map reconciliations and any unresolved owner handoffs in ignored progress; provide proposed safe adoption order.
- [ ] UTH-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTH-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UTH-1.4`: Run the roadmap structural validator, reconcile final manifest coverage and inspect outstanding blocked fingerprints; no runner mutation. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTH-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/29-final-support-handoff.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- BNT-1.2: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/81-host-final-cases.progress.md`.
- BNT-1.3: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/81-host-final-cases.progress.md`.
- BNT-1.4: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/81-host-final-cases.progress.md`.
- BNT-1.5: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/81-host-final-cases.progress.md`.
- BNT-1.6: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/81-host-final-cases.progress.md`.
- UTN-1.2: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/27-final-native-ui-testing.progress.md`.
- UTN-1.3: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/27-final-native-ui-testing.progress.md`.
- UTN-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/27-final-native-ui-testing.progress.md`.
- UTN-1.5: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/27-final-native-ui-testing.progress.md`.
- UTN-1.6: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/27-final-native-ui-testing.progress.md`.
- UTW-1.2: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/26-final-web-ui-testing.progress.md`.
- UTW-1.3: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/26-final-web-ui-testing.progress.md`.
- UTW-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/26-final-web-ui-testing.progress.md`.
- UTW-1.5: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/26-final-web-ui-testing.progress.md`.
- UTW-1.6: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/26-final-web-ui-testing.progress.md`.
- UTW-1.7: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/26-final-web-ui-testing.progress.md`.
- UTW-1.8: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/26-final-web-ui-testing.progress.md`.
- UTW-1.9: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/26-final-web-ui-testing.progress.md`.
- UTX-1.2: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/28-final-expo-flutter-testing.progress.md`.
- UTX-1.3: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/28-final-expo-flutter-testing.progress.md`.
- UTX-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/28-final-expo-flutter-testing.progress.md`.
- UTX-1.5: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/28-final-expo-flutter-testing.progress.md`.
- UTX-1.6: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/28-final-expo-flutter-testing.progress.md`.
