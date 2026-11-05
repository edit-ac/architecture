# Deliver React controls composition

Status: COMPLETE

## Goal and entry conditions

Goal: Deliver React controls composition. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/editor-ui-integrations.md#package-plan); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/04-react-ui.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

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

## Epic URC-1 — Deliver React controls composition

### Task URC-1.1 — Bind React command selectors

- [x] URC-1.1 Bind React command selectors.

Purpose: Bind React command selectors so applications can reuse this integration boundary.
Deliverable: `packages/react/src/controls/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#package-plan); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BWF-1.1](../dependency-closed-ui-20261025/13-react-astro-next-bindings.md), [UCS-1.6](02-controls-state.md), [UDM-1.7](03-default-dom-controls.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Framework state mirrors command snapshots with stable lifetime and no independently writable content. Use useSyncExternalStore selectors; keep React out of editable descendants and tolerate Strict Mode effect replay.

Implementation:

- [x] URC-1.1-I1 Extend the existing BWF-owned lifecycle binding with selector/controller hooks; preserve its async disposal and persistence callbacks.
- [x] URC-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] URC-1.1-V1 Run `node scripts/ui-integration-delivery.mjs URC-1.1`: Compile one lifecycle-backed counter/format-state consumer and observe a prepared selection change without replacing the host. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave URC-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task URC-1.2 — Add React toolbar parts and slots

- [x] URC-1.2 Add React toolbar parts and slots.

Purpose: Add React toolbar parts and slots so applications can reuse this integration boundary.
Deliverable: `packages/react/src/ui/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#package-plan); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: URC-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Toolbar, button/group/separator and block-type parts expose idiomatic slots/props and share UCS semantics; framework rendering never owns the editable subtree.

Implementation:

- [x] URC-1.2-I1 Compose framework-native wrappers using default presentation tokens; wire event/ref composition without duplicate activation.
- [x] URC-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] URC-1.2-V1 Run `node scripts/ui-integration-delivery.mjs URC-1.2`: Build one custom-order toolbar and activate a formatting action once from pointer and keyboard. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave URC-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task URC-1.3 — Add React overlay and suggestion composition

- [x] URC-1.3 Add React overlay and suggestion composition.

Purpose: Add React overlay and suggestion composition so applications can reuse this integration boundary.
Deliverable: `packages/react/src/ui/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#package-plan); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: URC-1.1, URC-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Menu/dialog/status and suggestion slots preserve captured targets, host portals and cancellation; no default DOM keyboard manager runs beneath a framework widget.

Implementation:

- [x] URC-1.3-I1 Expose overlay ownership context, typed result builders and status binding; reuse UCS session/queries rather than fork behavior.
- [x] URC-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] URC-1.3-V1 Run `node scripts/ui-integration-delivery.mjs URC-1.3`: Mount one reference picker in a host dialog and cancel an in-flight prepared result after unmount. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave URC-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task URC-1.4 — Export React UI subpaths and one example

- [x] URC-1.4 Export React UI subpaths and one example.

Purpose: Export React UI subpaths and one example so applications can reuse this integration boundary.
Deliverable: `packages/react/package.json; examples/ui/react/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#package-plan); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: URC-1.1, URC-1.2, URC-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Lifecycle-only imports exclude UI/CSS; UI imports resolve types and peer versions in an installed consumer; SSR has no DOM/WASM work and client mount owns one editor.

Implementation:

- [x] URC-1.4-I1 Add optional controls/UI exports and example import/stylesheet instructions; reuse BWF SSR/lifecycle evidence rather than new lifecycle suite.
- [x] URC-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] URC-1.4-V1 Run `node scripts/ui-integration-delivery.mjs URC-1.4`: Pack/install the affected binding in one existing isolated consumer; run its compile/SSR-import selection and one client composition check. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave URC-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/04-react-ui.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- BWF-1.1: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/13-react-astro-next-bindings.progress.md`.
- UCS-1.6: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/02-controls-state.progress.md`.
- UDM-1.7: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/03-default-dom-controls.progress.md`.
