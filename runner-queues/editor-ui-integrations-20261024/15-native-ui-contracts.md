# Map shared controls to native hosts

Status: IN_PROGRESS

## Goal and entry conditions

Goal: Map shared controls to native hosts. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/native-ui-integrations.md#portable-ui-contract); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/15-native-ui-contracts.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

Entry receipts are scoped to each parent below. Verify the named public interface and focused acceptance against its consumed source revision; a queued predecessor or whole-file title is not evidence. Earlier-file progress has the same basename under `.roadmap-runner/editor-ui-integrations-20261024/`; existing backend-owner receipts live under `.roadmap-runner/backend-sdk-adapters-20261024/`. Read only the named parent receipt.

## Execution and validation rules

All implementation paths below are core-relative unless prefixed `../architecture` or `../docs`; proposed paths must be reconciled to existing exports before creating files. Read the owning repository AGENTS.md before edits. A missing bridge/semantic API belongs to its named existing owner; do not implement a parallel one in a UI package.

One parent is one 15–45 minute session including focused validation. Split at a concrete boundary before exceeding the budget, preserving its acceptance and stable ID mapping. Budget inputs to this file, its named contract section, required predecessor receipt and only affected code; the controller index and other milestone bodies are not mandatory worker input.

The future core command `node scripts/ui-integration-delivery.mjs <task-id>` is introduced by UIC-1.5. It is a planned selector interface, not an existing command or passing test claim. Each later task registers the smallest relevant existing compiler/fixture/manual-observation wrapper; unknown/missing selectors and zero-case runs fail. Contract tasks before that dispatcher use the explicit direct checks below. Functional checks normally take 1–3 minutes, at most 5 minutes for an already provisioned native compiler/startup. Cold SDK installation, broad suites and comprehensive case authoring do not fit a delivery check. Final-testing tasks may spend up to 10 minutes on one declared bounded selector; split longer profiles across parents before starting them.

Use deterministic documents and local/mock transports only: no paid inference, credentials loaded into tests, provider recording, paid cloud builds, production access, deployment or publication. Keep generated packages, binaries, screenshots and logs in ignored task-owned directories. Preserve source, real user data and active processes. Use one current format, engine, command/history and persistence authority.

Independent work: a sibling with satisfied local dependencies and named entry receipts is eligible; queue order is not a dependency. Stop the affected worker on BLOCKED, record task/source/error/prerequisite fingerprint, owner, attempted repair and exact changed-input resume condition. Do not retry unchanged input or skip acceptance. A serial queue cannot jump a blocked file: only the existing coordinator may adopt a different ready subset at a safe guarded checkpoint. No runner start, enqueue, state edits or snapshot replacement is authorized by this source.

Workers may update verified checkboxes and Status only under the current installed runner policy. Hashes, results and handoff prose stay in separate ignored progress. A checked functional parent means its own narrow checks passed; it does not claim final UI/platform/accessibility qualification. Reuse compatible evidence and name the changed input before rerunning or widening. Final test/case development is in files 26–29 after all functional delivery, with existing BNT and roadmap43 owners retained.

## Focused delivery validation authority

Focused runtime delivery checks are authorized by the controller: /Users/bpstr/Github/edit-ac/architecture/runner-queues/dependency-closed-ui-20261025/delivery-check-policy.md. Read that bounded policy before interpreting this source’s validation scope. Execute only the deterministic compiler/fixture/browser/native/manual check named by the current parent; register its minimal missing wrapper when needed and report actual runtime counts separately. Comprehensive suites, case matrices and final qualification remain after functional delivery. A phase label alone is not a runtime prohibition; preserve every acceptance gate and reuse compatible passing evidence.

## Epic UNC-1 — Map shared controls to native hosts

### Task UNC-1.1 — Map actual native command and view exports

- [ ] UNC-1.1 Map actual native command and view exports.

Purpose: Map actual native command and view exports so applications can reuse this integration boundary.
Deliverable: `sdk/contracts/; native/*/; ../architecture/specs/native-ui-integrations.md`.
Context: [named contract section](../../specs/native-ui-integrations.md#portable-ui-contract); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [UIC-1.2](00-contracts.md), [UIC-1.3](00-contracts.md), [UIC-1.4](00-contracts.md), [UIC-1.5](00-contracts.md), [UIC-1.6](00-contracts.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Each native command-state/target field maps to an existing Session/presenter capability or an exact owner gap; no UI task silently implements a new semantic command or duplicate host.

Implementation:

- [ ] UNC-1.1-I1 Inspect current Swift/Kotlin/C ABI and desktop APIs; record needed control-state handles and per-platform entry receipts.
- [ ] UNC-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UNC-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UNC-1.1`: Direct inspection of one command and one capture/dispose mapping per declared platform; count supported/gap rows. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UNC-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UNC-1.2 — Define native theme and control data bindings

- [ ] UNC-1.2 Define native theme and control data bindings.

Purpose: Define native theme and control data bindings so applications can reuse this integration boundary.
Deliverable: `sdk/contracts/; native/*/`.
Context: [named contract section](../../specs/native-ui-integrations.md#portable-ui-contract); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UNC-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: One bounded data schema covers semantic tokens, locale/direction, accessibility preferences, control descriptors and state; no callbacks/components/DOM strings cross bridges.

Implementation:

- [ ] UNC-1.2-I1 Map UIC token/state declarations to native public types and platform naming; declare executor/buffer/event ownership.
- [ ] UNC-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UNC-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UNC-1.2`: Type/schema-check one prepared light/dark/mixed state DTO and reject an oversized/unknown required field. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UNC-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UNC-1.3 — Define cross-host overlay and event rules

- [ ] UNC-1.3 Define cross-host overlay and event rules.

Purpose: Define cross-host overlay and event rules so applications can reuse this integration boundary.
Deliverable: `sdk/contracts/; ../architecture/specs/native-ui-integrations.md`.
Context: [named contract section](../../specs/native-ui-integrations.md#portable-ui-contract); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UNC-1.1, UNC-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Native overlay owners preserve captured targets, async completion ordering and session identity; coalescing UI snapshots cannot drop completion/error/dispose events.

Implementation:

- [ ] UNC-1.3-I1 Specify explicit focus/coordinate conversion, target revocation and bounded event payload rules as additions to existing BCP/BNA/BDH contracts.
- [ ] UNC-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UNC-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UNC-1.3`: Inspect prepared command/popup/dispose transcripts against existing native ownership rules; record gaps for the owning bridge. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UNC-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UNC-1.4 — Freeze per-platform UI export/support map

- [ ] UNC-1.4 Freeze per-platform UI export/support map.

Purpose: Freeze per-platform UI export/support map so applications can reuse this integration boundary.
Deliverable: `native/*/; adapters/native/; ../architecture/specs/native-ui-integrations.md`.
Context: [named contract section](../../specs/native-ui-integrations.md#portable-ui-contract); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UNC-1.1, UNC-1.2, UNC-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: UIKit/SwiftUI/AppKit/Views/Compose/WinUI/WPF/GTK plus RN/Expo/Flutter mobile/web have exact planned UI ownership and maintained-baseline inputs; desktop RN/Flutter remain explicit feasibility profiles.

Implementation:

- [ ] UNC-1.4-I1 Set optional UI product/module boundaries and per-surface capability declarations; preserve independent host and backend prerequisite edges.
- [ ] UNC-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UNC-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UNC-1.4`: Review package/peer map and every required profile against the adoption table; no runtime support claim from this inspection. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UNC-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/15-native-ui-contracts.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- UIC-1.2: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/00-contracts.progress.md`.
- UIC-1.3: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/00-contracts.progress.md`.
- UIC-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/00-contracts.progress.md`.
- UIC-1.5: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/00-contracts.progress.md`.
- UIC-1.6: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/00-contracts.progress.md`.
