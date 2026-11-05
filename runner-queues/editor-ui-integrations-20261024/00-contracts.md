# Freeze shared UI contracts and ownership

Status: COMPLETE

## Goal and entry conditions

Goal: Freeze shared UI contracts and ownership. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/editor-ui-integrations.md#shared-customization-apis); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/00-contracts.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

Entry receipts are scoped to each parent below. Verify the named public interface and focused acceptance against its consumed source revision; a queued predecessor or whole-file title is not evidence. Earlier-file progress has the same basename under `.roadmap-runner/editor-ui-integrations-20261024/`; existing backend-owner receipts live under `.roadmap-runner/backend-sdk-adapters-20261024/`. Read only the named parent receipt.

## Execution and validation rules

All implementation paths below are core-relative unless prefixed `../architecture` or `../docs`; proposed paths must be reconciled to existing exports before creating files. Read the owning repository AGENTS.md before edits. A missing bridge/semantic API belongs to its named existing owner; do not implement a parallel one in a UI package.

One parent is one 15–45 minute session including focused validation. Split at a concrete boundary before exceeding the budget, preserving its acceptance and stable ID mapping. Budget inputs to this file, its named contract section, required predecessor receipt and only affected code; the controller index and other milestone bodies are not mandatory worker input.

The future core command `node scripts/ui-integration-delivery.mjs <task-id>` is introduced by UIC-1.5. It is a planned selector interface, not an existing command or passing test claim. Each later task registers the smallest relevant existing compiler/fixture/manual-observation wrapper; unknown/missing selectors and zero-case runs fail. Contract tasks before that dispatcher use the explicit direct checks below. Functional checks normally take 1–3 minutes, at most 5 minutes for an already provisioned native compiler/startup. Cold SDK installation, broad suites and comprehensive case authoring do not fit a delivery check. Final-testing tasks may spend up to 10 minutes on one declared bounded selector; split longer profiles across parents before starting them.

Use deterministic documents and local/mock transports only: no paid inference, credentials loaded into tests, provider recording, paid cloud builds, production access, deployment or publication. Keep generated packages, binaries, screenshots and logs in ignored task-owned directories. Preserve source, real user data and active processes. Use one current format, engine, command/history and persistence authority.

Independent work: a sibling with satisfied local dependencies and named entry receipts is eligible; queue order is not a dependency. Stop the affected worker on BLOCKED, record task/source/error/prerequisite fingerprint, owner, attempted repair and exact changed-input resume condition. Do not retry unchanged input or skip acceptance. A serial queue cannot jump a blocked file: only the existing coordinator may adopt a different ready subset at a safe guarded checkpoint. No runner start, enqueue, state edits or snapshot replacement is authorized by this source.

Workers may update verified checkboxes and Status only under the current installed runner policy. Hashes, results and handoff prose stay in separate ignored progress. A checked functional parent means its own narrow checks passed; it does not claim final UI/platform/accessibility qualification. Reuse compatible evidence and name the changed input before rerunning or widening. Final test/case development is in files 26–29 after all functional delivery, with existing BNT and roadmap43 owners retained.

## Epic UIC-1 — Freeze shared UI contracts and ownership

### Task UIC-1.1 — Inventory actual exports and freeze package boundaries

- [x] UIC-1.1 Inventory actual exports and freeze package boundaries.

Purpose: Inventory actual exports and freeze package boundaries so applications can reuse this integration boundary.
Deliverable: `packages/*/package.json; packages/web/src/ui/; ../architecture/specs/editor-ui-integrations.md`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shared-customization-apis); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: An authored surface/package ledger distinguishes existing, planned and unsupported capabilities; each proposed export maps to one owner and optional peer boundary. All existing rendered controls and statuses have an inventory row; no feature is enabled by its presence in UI.

Implementation:

- [x] UIC-1.1-I1 Inspect current exports, command/presenter symbols and UI surfaces; reconcile proposed names and record native/framework handoffs without editing active queue files.
- [x] UIC-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UIC-1.1-V1 Direct inspection: check the ledger against the actual package manifests and current rendered control inventory; record counted rows and mismatches, then git diff --check. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIC-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UIC-1.2 — Define immutable command view state

- [x] UIC-1.2 Define immutable command view state.

Purpose: Define immutable command view state so applications can reuse this integration boundary.
Deliverable: `packages/web/src/commands/; packages/web/src/ui/; ../architecture/specs/editor-ui-integrations.md`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shared-customization-apis); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UIC-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: One typed projection exposes availability/reason, pressed/mixed/value and pending states over existing commands. Snapshots remain referentially stable until relevant state changes; no second registry or writable content model is created.

Implementation:

- [x] UIC-1.2-I1 Extend existing public types and projection subscription contract; separate pure state from DOM/runtime initialization and document selector equality/disposal.
- [x] UIC-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UIC-1.2-V1 Type-check the changed exports and inspect one prepared bold/mixed/readonly state transcript; record cases and ensure imports perform no DOM or WASM work. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIC-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UIC-1.3 — Define captured target and contribution interfaces

- [x] UIC-1.3 Define captured target and contribution interfaces.

Purpose: Define captured target and contribution interfaces so applications can reuse this integration boundary.
Deliverable: `packages/web/src/commands/; packages/web/src/extensions/; packages/web/src/ui/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shared-customization-apis); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UIC-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Toolbar, dialog and portaled owners share existing guarded targets; contributions use deterministic IDs/order and existing semantic registrations. Stale execution rejects explicitly, extension policy is rechecked, and disposal revokes callbacks.

Implementation:

- [x] UIC-1.3-I1 Specify target/overlay ownership, contribution validation and bounded async suggestion cancellation; map each field to the existing captured-command/presenter APIs rather than implement semantic commands.
- [x] UIC-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UIC-1.3-V1 Inspect one accepted and one revoked target transcript and duplicate contribution declaration with deterministic inputs; type-check boundary types. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIC-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UIC-1.4 — Define tokens, slots and native theme DTOs

- [x] UIC-1.4 Define tokens, slots and native theme DTOs.

Purpose: Define tokens, slots and native theme DTOs so applications can reuse this integration boundary.
Deliverable: `packages/web/styles/; packages/web/src/ui/; sdk/contracts/; ../architecture/specs/native-ui-integrations.md`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shared-customization-apis); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UIC-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Content/chrome/overlay parts and theme tokens have one documented naming authority; native DTOs contain bounded data, no callbacks/CSS/DOM. Two-editor themes, RTL and locale ownership are explicit.

Implementation:

- [x] UIC-1.4-I1 Write token and slot declarations plus native mapping table; define structural/content/chrome stylesheet separation and per-overlay inheritance.
- [x] UIC-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UIC-1.4-V1 Check declarations against one light/dark/RTL fixture and native DTO example; no visual/AT qualification claimed. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIC-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UIC-1.5 — Add bounded delivery selector dispatch

- [x] UIC-1.5 Add bounded delivery selector dispatch.

Purpose: Add bounded delivery selector dispatch so applications can reuse this integration boundary.
Deliverable: `scripts/ui-integration-delivery.mjs; scripts/ui-integration-selectors/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shared-customization-apis); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UIC-1.4.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: A selector maps exactly one task to its existing compiler/fixture or bounded manual inspection recipe, rejects unknown IDs and zero-case success, records counts/time/exit, and never launches paid inference or broad suites. No credentials or provider recording are supported.

Implementation:

- [x] UIC-1.5-I1 Implement the small dispatch wrapper and register only currently available contract checks; future tasks add their own focused selectors. Keep generated output in ignored task-owned directories.
- [x] UIC-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UIC-1.5-V1 Run the contract selector and an intentionally unknown selector; require nonzero inspected cases for the former and nonzero error exit for the latter. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIC-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UIC-1.6 — Reconcile staged owner handoffs

- [x] UIC-1.6 Reconcile staged owner handoffs.

Purpose: Reconcile staged owner handoffs so applications can reuse this integration boundary.
Deliverable: `../architecture/specs/editor-ui-integrations.md; ../architecture/specs/native-ui-integrations.md; ../architecture/runner-queues/editor-ui-integrations-20261024/adoption-map.md`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shared-customization-apis); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UIC-1.1, UIC-1.2, UIC-1.3, UIC-1.4.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Each reused BWF/BFA/BCP/BNA/BDH/BNT acceptance has one existing owner and a specific additional requirement. Native bridging gaps go to that owner; no duplicate bridge package or independent runner is introduced.

Implementation:

- [x] UIC-1.6-I1 Freeze the staged adoption table and exact source/interface receipt requirements; preserve existing IDs and any implemented evidence. Do not edit immutable active snapshots or enqueue work.
- [x] UIC-1.6-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UIC-1.6-V1 Direct inspection of the ownership table against named parent definitions and package ledger; count resolved/unresolved owner rows. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UIC-1.6 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/00-contracts.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.
