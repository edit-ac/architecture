# Complete web UI coverage after functional delivery

Status: IN_PROGRESS

## Goal and entry conditions

Goal: Complete web UI coverage after functional delivery. Planning source: 2026-10-24. Workspace: `core`. This is final-testing work; no completed capability is implied.

Authority: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/26-final-web-ui-testing.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

Entry receipts are scoped to each parent below. Verify the named public interface and focused acceptance against its consumed source revision; a queued predecessor or whole-file title is not evidence. Earlier-file progress has the same basename under `.roadmap-runner/editor-ui-integrations-20261024/`; existing backend-owner receipts live under `.roadmap-runner/backend-sdk-adapters-20261024/`. Read only the named parent receipt.

Final-phase entry: all required functionality in files 00–25 is delivered. This is a testing-sequencing gate, not permission to require unrelated language SDKs. Within this file consume only the platform/semantic/backend receipts needed for the current case. Actual browser/native/AT observations are registered with and consumed from roadmap43; mock/compile results cannot substitute.

## Execution and validation rules

All implementation paths below are core-relative unless prefixed `../architecture` or `../docs`; proposed paths must be reconciled to existing exports before creating files. Read the owning repository AGENTS.md before edits. A missing bridge/semantic API belongs to its named existing owner; do not implement a parallel one in a UI package.

One parent is one 15–45 minute session including focused validation. Split at a concrete boundary before exceeding the budget, preserving its acceptance and stable ID mapping. Budget inputs to this file, its named contract section, required predecessor receipt and only affected code; the controller index and other milestone bodies are not mandatory worker input.

The future core command `node scripts/ui-integration-delivery.mjs <task-id>` is introduced by UIC-1.5. It is a planned selector interface, not an existing command or passing test claim. Each later task registers the smallest relevant existing compiler/fixture/manual-observation wrapper; unknown/missing selectors and zero-case runs fail. Contract tasks before that dispatcher use the explicit direct checks below. Functional checks normally take 1–3 minutes, at most 5 minutes for an already provisioned native compiler/startup. Cold SDK installation, broad suites and comprehensive case authoring do not fit a delivery check. Final-testing tasks may spend up to 10 minutes on one declared bounded selector; split longer profiles across parents before starting them.

Use deterministic documents and local/mock transports only: no paid inference, credentials loaded into tests, provider recording, paid cloud builds, production access, deployment or publication. Keep generated packages, binaries, screenshots and logs in ignored task-owned directories. Preserve source, real user data and active processes. Use one current format, engine, command/history and persistence authority.

Independent work: a sibling with satisfied local dependencies and named entry receipts is eligible; queue order is not a dependency. Stop the affected worker on BLOCKED, record task/source/error/prerequisite fingerprint, owner, attempted repair and exact changed-input resume condition. Do not retry unchanged input or skip acceptance. A serial queue cannot jump a blocked file: only the existing coordinator may adopt a different ready subset at a safe guarded checkpoint. No runner start, enqueue, state edits or snapshot replacement is authorized by this source.

Workers may update verified checkboxes and Status only under the current installed runner policy. Hashes, results and handoff prose stay in separate ignored progress. A checked functional parent means its own narrow checks passed; it does not claim final UI/platform/accessibility qualification. Reuse compatible evidence and name the changed input before rerunning or widening. Final test/case development is in files 26–29 after all functional delivery, with existing BNT and roadmap43 owners retained.

## Epic UTW-1 — Complete web UI coverage after functional delivery

### Task UTW-1.1 — Register UI-only final cases and reuse decisions

- [ ] UTW-1.1 Register UI-only final cases and reuse decisions.

Purpose: Register UI-only final cases and reuse decisions so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/; ../architecture/tests/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BNT-1.2](../dependency-closed-ui-20261025/81-host-final-cases.md), [UPG-1.4](25-packages-and-guides.md), [UPG-1.5](25-packages-and-guides.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Each new UI case has one owner, exact package/profile/artifact inputs and a reuse link to unchanged existing semantic/lifecycle tests; zero/skipped observations cannot qualify a profile.

Implementation:

- [ ] UTW-1.1-I1 Inventory uncovered UI-01 through UI-12 criteria; define bounded selectors and register target-browser/AT observations with roadmap43 without running a new controller.
- [ ] UTW-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTW-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UTW-1.1`: Validate case uniqueness and selected prior receipt compatibility; report uncovered/blocking profiles. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTW-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTW-1.2 — Cover default styles and host overrides

- [ ] UTW-1.2 Cover default styles and host overrides.

Purpose: Cover default styles and host overrides so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/default/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [UDM-1.8](03-default-dom-controls.md), [UDM-1.9](03-default-dom-controls.md), [UDM-1.10](03b-table-controls.md), [UDM-1.11](03b-table-controls.md), [UDM-1.12](03b-table-controls.md).
Dependencies: UTW-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Content/chrome separation, all inventoried states, two-editor/portal themes, responsive layout, RTL and forced-color cases have passing focused evidence or explicit open observations. Table-paste product acceptance additionally requires [TPT-01–08](../../specs/table-paste-and-editing.md): actual packed direct cell editing/paste, coherent idle grid without repeated input/textarea chrome, formatting/target/history/reopen and nonmutating rejection; reuse semantic-owner proof and record exact remaining OS/AT observations. UDM-1.8/1.9 receipts are prerequisites for this added slice; no fixture-only or screenshot-only pass. The table-control follow-up additionally consumes UDM-1.10–1.12 and [NTC-01–16](../../tests/notion-table-cases.md): scoped menus/headers, stable geometry, safe axis actions and honest capability limits. Carry existing direct-cell/paste passes forward; repeat only invalidated scopes.

Implementation:

- [ ] UTW-1.2-I1 Add remaining deterministic style/override assertions and visual observation recipes; do not retest engine semantics.
- [ ] UTW-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTW-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UTW-1.2`: Run only new/changed default UI cases in one bounded batch and consume named roadmap43 observations where needed. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTW-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTW-1.3 — Cover shared control and suggestion risks

- [ ] UTW-1.3 Cover shared control and suggestion risks.

Purpose: Cover shared control and suggestion risks so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/controls/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTW-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Contribution layout, stale/readonly/revoked targets, async cancellation/out-of-order queries and no duplicate activation have UI-boundary coverage using existing semantic oracles.

Implementation:

- [ ] UTW-1.3-I1 Add missing control/session/race assertions and inspect one custom extension appearing across configured surfaces.
- [ ] UTW-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTW-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UTW-1.3`: Run the new controls selector and reuse existing semantic command/undo evidence; no provider calls. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTW-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTW-1.4 — Cover React Base UI and Aria widgets

- [ ] UTW-1.4 Cover React Base UI and Aria widgets.

Purpose: Cover React Base UI and Aria widgets so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/react/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTW-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Both adapters cover every agreed surface and their distinct focus/press/collection behavior without duplicate keyboard managers or invalid option children.

Implementation:

- [ ] UTW-1.4-I1 Add library-specific remaining widget cases and per-profile assistive-technology observation requests.
- [ ] UTW-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTW-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UTW-1.4`: Run one bounded selector per changed library; consume roadmap43 keyboard/AT observations before qualifying accessibility. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTW-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTW-1.5 — Cover Radix, Reka and Bits widgets

- [ ] UTW-1.5 Cover Radix, Reka and Bits widgets.

Purpose: Cover Radix, Reka and Bits widgets so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/adapters/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTW-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Each adapter has actual trigger/ref/slot/portal and state coverage for agreed surfaces; no framework cross-import or nested-button regression is hidden by a shared mock.

Implementation:

- [ ] UTW-1.5-I1 Add remaining adapter-specific cases, reusing shared control evidence and splitting a library batch if it exceeds session budget.
- [ ] UTW-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTW-1.5-V1 Run `node scripts/ui-integration-delivery.mjs UTW-1.5`: Run affected library selectors with explicit per-library counts; record target-runtime observations separately. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTW-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTW-1.6 — Cover all shadcn registry installers

- [ ] UTW-1.6 Cover all shadcn registry installers.

Purpose: Cover all shadcn registry installers so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/registry/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTW-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: React Base UI and Radix plus Vue and Svelte native installers accept real source items, preserve local files and produce correct utility CSS in production builds.

Implementation:

- [ ] UTW-1.6-I1 Author missing isolated installer inputs and no-overwrite/update cases; inspect source-owned customization and notices.
- [ ] UTW-1.6-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTW-1.6-V1 Run `node scripts/ui-integration-delivery.mjs UTW-1.6`: Run one bounded installer profile per affected variant using local prepared packages; separate long cold installs from task execution. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTW-1.6 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTW-1.7 — Cover frontend and Filament presentation integration

- [ ] UTW-1.7 Cover frontend and Filament presentation integration.

Purpose: Cover frontend and Filament presentation integration so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/hosts/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTW-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Astro/client framework composition and Laravel frontend/Filament admin themes, nested overlays and no-React boundaries are covered; persistence/form lifecycle results are consumed from BNT rather than duplicated.

Implementation:

- [ ] UTW-1.7-I1 Add UI-specific host cases and register missing BNT-1.2 acceptance for actual new fields/profiles through the adoption map.
- [ ] UTW-1.7-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTW-1.7-V1 Run `node scripts/ui-integration-delivery.mjs UTW-1.7`: Run selected UI host fixtures and consume exact BNT-1.2 receipts for lifecycle claims; keep missing receipts blocking only those claims. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTW-1.7 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTW-1.8 — Cover web installed dependency and asset isolation

- [ ] UTW-1.8 Cover web installed dependency and asset isolation.

Purpose: Cover web installed dependency and asset isolation so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/packages/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTW-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Installed plain/React/Vue/Svelte consumers have correct exports/CSS and one engine asset graph; default non-React paths exclude React and unused UI libraries.

Implementation:

- [ ] UTW-1.8-I1 Add remaining package graph/tree-shaking/stylesheet assertions using prepared local packages and production build outputs.
- [ ] UTW-1.8-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTW-1.8-V1 Run `node scripts/ui-integration-delivery.mjs UTW-1.8`: Run missing package selectors only, record JS/CSS separately and preserve existing hard caps without an unbounded optimization campaign. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTW-1.8 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UTW-1.9 — Qualify default DOM control accessibility

- [ ] UTW-1.9 Qualify default DOM control accessibility.

Purpose: Qualify default DOM control accessibility so applications can reuse this integration boundary.
Deliverable: `tests/ui-integrations/default/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UTW-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Default toolbar/menu/dialog/slash/reference controls have correct keyboard navigation, focus restoration, names/states and touch targets on declared browser/AT profiles; inline suggestions preserve editor IME and announcement ownership.

Implementation:

- [ ] UTW-1.9-I1 Add uncovered default-widget cases and exact roadmap43 observation requests; reuse existing editing/IME semantics evidence rather than authoring another input suite.
- [ ] UTW-1.9-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UTW-1.9-V1 Run `node scripts/ui-integration-delivery.mjs UTW-1.9`: Run the remaining deterministic default-widget cases and consume current keyboard/screen-reader/touch observations; missing observations remain unqualified. Budget: one declared selector batch up to 10 minutes; split before expanding.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UTW-1.9 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/26-final-web-ui-testing.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- BNT-1.2: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/81-host-final-cases.progress.md`.
- UDM-1.8: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/03-default-dom-controls.progress.md`.
- UDM-1.9: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/03-default-dom-controls.progress.md`.
- UPG-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/25-packages-and-guides.progress.md`.
- UPG-1.5: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/25-packages-and-guides.progress.md`.
