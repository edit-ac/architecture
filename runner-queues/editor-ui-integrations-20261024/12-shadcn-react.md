# Deliver React shadcn source kits

Status: COMPLETE

## Goal and entry conditions

Goal: Deliver React shadcn source kits. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/editor-ui-integrations.md#shadcn-delivery); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/12-shadcn-react.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

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

## Epic USR-1 — Deliver React shadcn source kits

### Task USR-1.1 — Define registry inputs and library selection

- [x] USR-1.1 Define registry inputs and library selection.

Purpose: Define registry inputs and library selection so applications can reuse this integration boundary.
Deliverable: `registry/react/; examples/ui/shadcn-react/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shadcn-delivery); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [UBU-1.5](07-base-ui.md), [URA-1.5](08-react-aria.md), [URD-1.5](09-radix.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Authored registry items explicitly identify Base UI or Radix, peer/API ranges, aliases and CSS prerequisites; installation does not overwrite existing app components or switch primitive families.

Implementation:

- [x] USR-1.1-I1 Create source item schema/build inputs and select the ecosystem installer baseline; generated registry JSON/bundles remain ignored.
- [x] USR-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] USR-1.1-V1 Run `node scripts/ui-integration-delivery.mjs USR-1.1`: Validate one minimal item against the pinned registry schema and inspect its dependency/configuration plan. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave USR-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task USR-1.2 — Add Base UI toolbar and editor frame items

- [x] USR-1.2 Add Base UI toolbar and editor frame items.

Purpose: Add Base UI toolbar and editor frame items so applications can reuse this integration boundary.
Deliverable: `registry/react/base-ui/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shadcn-delivery); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: USR-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Frame/toolbar/formatting/block-type source items compose the Base UI adapter and map host shadcn variables; copied components contain no duplicate target/command semantics.

Implementation:

- [x] USR-1.2-I1 Author the minimal editor and toolbar source with local icon/component imports and host theme variables; expose editable layout.
- [x] USR-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] USR-1.2-V1 Run `node scripts/ui-integration-delivery.mjs USR-1.2`: Install the items into one disposable Base UI shadcn app and production-build its toolbar. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave USR-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task USR-1.3 — Add Base UI contextual item set

- [x] USR-1.3 Add Base UI contextual item set.

Purpose: Add Base UI contextual item set so applications can reuse this integration boundary.
Deliverable: `registry/react/base-ui/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shadcn-delivery); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: USR-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Selection toolbar, block menu, slash/reference panel, link dialog and status items declare optional feature dependencies and use adapter target/query lifetimes.

Implementation:

- [x] USR-1.3-I1 Author thin visual source compositions for the completed Base UI adapter; distinguish command and option row semantics.
- [x] USR-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] USR-1.3-V1 Run `node scripts/ui-integration-delivery.mjs USR-1.3`: Install one contextual composition and execute one prepared reference or link flow in the existing sample. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave USR-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task USR-1.4 — Add Radix toolbar and frame variants

- [x] USR-1.4 Add Radix toolbar and frame variants.

Purpose: Add Radix toolbar and frame variants so applications can reuse this integration boundary.
Deliverable: `registry/react/radix/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shadcn-delivery); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: USR-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Radix users install the frame/toolbar without Base UI or nested trigger buttons; the same semantics and host theme contract apply.

Implementation:

- [x] USR-1.4-I1 Author Radix visual variants over its adapter and explicit registry primitive metadata; preserve app aliases and icons.
- [x] USR-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] USR-1.4-V1 Run `node scripts/ui-integration-delivery.mjs USR-1.4`: Install in one existing-Radix fixture and production-build; inspect that Base UI is absent. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave USR-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task USR-1.5 — Add Radix contextual variants

- [x] USR-1.5 Add Radix contextual variants.

Purpose: Add Radix contextual variants so applications can reuse this integration boundary.
Deliverable: `registry/react/radix/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shadcn-delivery); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: USR-1.4.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: All contextual source items use Radix adapter primitives and explicit portal ownership; mixed primitive imports are absent.

Implementation:

- [x] USR-1.5-I1 Compose contextual source variants and dependency manifests without copying guarded-command logic.
- [x] USR-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] USR-1.5-V1 Run `node scripts/ui-integration-delivery.mjs USR-1.5`: Install one Radix contextual composition and run its prepared dialog/cancel smoke. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave USR-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task USR-1.6 — Provide update and production CSS guidance

- [x] USR-1.6 Provide update and production CSS guidance.

Purpose: Provide update and production CSS guidance so applications can reuse this integration boundary.
Deliverable: `registry/react/; examples/ui/shadcn-react/; packages/react-aria/README.md`.
Context: [named contract section](../../specs/editor-ui-integrations.md#shadcn-delivery); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: USR-1.3, USR-1.5.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Both primitive variants survive Tailwind production scanning and honor local edits; source updates are explicit. React Aria has the same token theme recipe but is not misrepresented as an official shadcn primitive variant.

Implementation:

- [x] USR-1.6-I1 Document source ownership/API updates and stylesheet discovery; add the Aria token recipe and no-overwrite installation example.
- [x] USR-1.6-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] USR-1.6-V1 Run `node scripts/ui-integration-delivery.mjs USR-1.6`: Build one item from each variant with the actual installer/config; review local-change preservation and the Aria recipe against real exports. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave USR-1.6 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/12-shadcn-react.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- UBU-1.5: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/07-base-ui.progress.md`.
- URA-1.5: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/08-react-aria.progress.md`.
- URD-1.5: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/09-radix.progress.md`.
