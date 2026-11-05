# Integrate existing host and Laravel plans

Status: COMPLETE

## Goal and entry conditions

Goal: Integrate existing host and Laravel plans. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/editor-ui-integrations.md#laravel-vite-shadcn-and-filament-reference-application); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/14-web-host-integrations.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

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

## Epic UWH-1 — Integrate existing host and Laravel plans

### Task UWH-1.1 — Compose Astro default controls

- [x] UWH-1.1 Compose Astro default controls.

Purpose: Compose Astro default controls so applications can reuse this integration boundary.
Deliverable: `packages/astro/; examples/ui/astro/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#laravel-vite-shadcn-and-filament-reference-application); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BWF-1.1](../dependency-closed-ui-20261025/13-react-astro-next-bindings.md), [UDM-1.7](03-default-dom-controls.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Existing Astro host mounts default DOM UI and CSS without React; route-away disposal uses the BWF-owned lifecycle and preserves its save/recovery behavior.

Implementation:

- [x] UWH-1.1-I1 Add an optional UI configuration/slot bridge around the existing custom element; do not create another lifecycle host.
- [x] UWH-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UWH-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UWH-1.1`: Compile an existing Astro static/SSR consumer and one navigation-mounted toolbar composition. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UWH-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UWH-1.2 — Add client-framework UI boundary recipes

- [x] UWH-1.2 Add client-framework UI boundary recipes.

Purpose: Add client-framework UI boundary recipes so applications can reuse this integration boundary.
Deliverable: `examples/ui/next/; examples/ui/nuxt/; examples/ui/sveltekit/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#laravel-vite-shadcn-and-filament-reference-application); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BWF-1.2](../dependency-closed-ui-20261025/13-react-astro-next-bindings.md), [BWF-1.4](../dependency-closed-ui-20261025/14-vue-nuxt-bindings.md), [BWF-1.6](../dependency-closed-ui-20261025/15-svelte-kit-bindings.md), [URC-1.4](04-react-ui.md), [USV-1.4](06-svelte-ui.md), [UVU-1.4](05-vue-ui.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Each recipe uses its existing BWF client boundary and corresponding UI adapter; SSR imports do not initialize editor UI, and assets/themes load only in the documented client entry.

Implementation:

- [x] UWH-1.2-I1 Add small UI composition recipes to existing Next/Nuxt/SvelteKit examples without new server or lifecycle packages; split if any missing host API exceeds this boundary.
- [x] UWH-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UWH-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UWH-1.2`: Compile each changed example entry only and inspect declared client imports; reuse BWF SSR results. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UWH-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UWH-1.3 — Style the existing Filament field

- [x] UWH-1.3 Style the existing Filament field.

Purpose: Style the existing Filament field so applications can reuse this integration boundary.
Deliverable: `adapters/admin/filament/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#laravel-vite-shadcn-and-filament-reference-application); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BFA-1.2](../dependency-closed-ui-20261025/19-filament-bindings.md), [BFA-1.4](../dependency-closed-ui-20261025/19-filament-bindings.md), [UDM-1.7](03-default-dom-controls.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Existing field uses default DOM controls and a Filament token mapping without React; labels/errors, disabled state, modal overlay container and nested field identity remain owned by BFA.

Implementation:

- [x] UWH-1.3-I1 Add theme/control options to the BFA field and lazy asset registration; no whole-document Livewire entanglement or new persistence implementation.
- [x] UWH-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UWH-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UWH-1.3`: Render one existing nested/modal field with dark theme and a guarded formatting action; confirm admin edit.ac asset graph excludes React. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UWH-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UWH-1.4 — Add Laravel React shadcn frontend composition

- [x] UWH-1.4 Add Laravel React shadcn frontend composition.

Purpose: Add Laravel React shadcn frontend composition so applications can reuse this integration boundary.
Deliverable: `examples/sdk-adapters/laravel/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#laravel-vite-shadcn-and-filament-reference-application); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BPH-1.7](../dependency-closed-ui-20261025/18-laravel-bindings.md), [USR-1.6](12-shadcn-react.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: The existing Laravel example has a Vite/Inertia React page using the selected shadcn variant; app policy, CSRF, receipts and form-save transaction remain backend-owned.

Implementation:

- [x] UWH-1.4-I1 Wire the installed registry source to the existing Laravel storage facade and UI status; no new endpoint or PHP save algorithm.
- [x] UWH-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UWH-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UWH-1.4`: Build one page and replay a prepared save/error transcript through the existing backend fixture. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UWH-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UWH-1.5 — Add Laravel Vue and Svelte frontend variants

- [x] UWH-1.5 Add Laravel Vue and Svelte frontend variants.

Purpose: Add Laravel Vue and Svelte frontend variants so applications can reuse this integration boundary.
Deliverable: `examples/sdk-adapters/laravel/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#laravel-vite-shadcn-and-filament-reference-application); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BPH-1.7](../dependency-closed-ui-20261025/18-laravel-bindings.md), [USK-1.3](13-shadcn-vue-svelte.md), [USK-1.6](13-shadcn-vue-svelte.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Vue and Svelte pages use their native shadcn kits and the same Laravel DTO/store contract; neither page installs React through edit.ac.

Implementation:

- [x] UWH-1.5-I1 Add minimal alternative frontend examples sharing prepared backend data and receipt/status interfaces, not a multi-framework production bundle.
- [x] UWH-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UWH-1.5-V1 Run `node scripts/ui-integration-delivery.mjs UWH-1.5`: Production-build each alternative page and inspect one control/status smoke plus dependency graphs. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UWH-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UWH-1.6 — Add Angular and secondary design-system recipes

- [x] UWH-1.6 Add Angular and secondary design-system recipes.

Purpose: Add Angular and secondary design-system recipes so applications can reuse this integration boundary.
Deliverable: `packages/angular/; examples/ui/recipes/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#laravel-vite-shadcn-and-filament-reference-application); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [BWF-1.7](../dependency-closed-ui-20261025/16-angular-form-bindings.md), [BWF-1.8](../dependency-closed-ui-20261025/16-angular-form-bindings.md), [UDM-1.7](03-default-dom-controls.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Angular uses its BWF-owned binding and default controls with idiomatic field/disabled mapping; an authored MUI/PrimeVue/Ark recipe matrix distinguishes tested recipes from unimplemented adapters.

Implementation:

- [x] UWH-1.6-I1 Add one Angular toolbar wrapper and choose one small secondary-library example based on actual reusable boundary; list other candidates as unqualified, not supported.
- [x] UWH-1.6-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [x] UWH-1.6-V1 Run `node scripts/ui-integration-delivery.mjs UWH-1.6`: Compile the Angular consumer and the chosen recipe only; inspect binding to existing command state rather than a new command model. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UWH-1.6 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/14-web-host-integrations.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- BFA-1.2: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/19-filament-bindings.progress.md`.
- BFA-1.4: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/19-filament-bindings.progress.md`.
- BPH-1.7: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/18-laravel-bindings.progress.md`.
- BWF-1.1: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/13-react-astro-next-bindings.progress.md`.
- BWF-1.2: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/13-react-astro-next-bindings.progress.md`.
- BWF-1.4: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/14-vue-nuxt-bindings.progress.md`.
- BWF-1.6: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/15-svelte-kit-bindings.progress.md`.
- BWF-1.7: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/16-angular-form-bindings.progress.md`.
- BWF-1.8: `/Users/bpstr/Github/edit-ac/.roadmap-runner/dependency-closed-ui-20261025/16-angular-form-bindings.progress.md`.
- UDM-1.7: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/03-default-dom-controls.progress.md`.
- URC-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/04-react-ui.progress.md`.
- USK-1.3: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/13-shadcn-vue-svelte.progress.md`.
- USK-1.6: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/13-shadcn-vue-svelte.progress.md`.
- USR-1.6: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/12-shadcn-react.progress.md`.
- USV-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/06-svelte-ui.progress.md`.
- UVU-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/05-vue-ui.progress.md`.
