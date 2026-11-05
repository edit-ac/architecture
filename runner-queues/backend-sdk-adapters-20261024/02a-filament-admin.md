# Deliver the optional Filament admin adapter

Status: PLANNED

## Goal and entry conditions

Workspace: `core`; paths are core-relative and planned. Provide a separately installable Filament editor field over the thin Laravel wrapper and standalone PHP SDK. No protocol or save algorithm belongs in this package. The one current schema/profile have no version suffix.

Entry: 01a-php-sdk BPH-1.9/1.11 and 02-php-laravel-symfony BPH-1.3/1.4/1.7 provide the SDK transaction API, Laravel bindings and actual browser mount/save example. Existing `packages/web/` supplies canonical create/restore/export/flush through its accepted public boundary; a missing API is repaired with its owner, not copied into Filament. No later Node adapter is required. Read the named predecessors' ignored progress for actual accepted selectors/results.

Authority: [PHP SDK, Laravel wrapper and Filament contract](../../specs/backend-sdk-adapters.md#php-sdk-laravel-wrapper-and-filament), [canonical durability](../../specs/document-durability.md), and [Filament custom field extension points](https://filamentphp.com/docs/5.x/forms/custom-fields). The official reference documents custom fields, nested state paths, binding modifiers and lazy third-party assets; select one maintained Filament/Livewire baseline at implementation instead of promising historical generations.

## Execution and validation rules

One parent is one 15–45 minute boundary including a focused check; split before implementing a missing shared API or larger matrix. Register each planned command below with `scripts/sdk-adapter-delivery.mjs` from BSC-1.7; a missing selector fails. Use existing package/compiler checks or one prepared risk fixture. Comprehensive Livewire/form/modal/browser cases belong to BNT-1.2; byte/receipt/authorization cases belong to their BFT owners. Functional completion is not qualification.

Use only prepared data and local/mock transports, with real local SQLite for the focused commit check. Never load production credentials, call paid inference, publish packages or deploy. Generated assets/packages/reports remain ignored; source and deterministic inputs belong in Git. Track/reuse suitable servers and tear down only confirmed task-owned processes. Existing user data and dirty work remain preserved.

This planning file starts/enqueues no runner and changes no active snapshot. Adopt at the coordinator's safe checkpoint using the existing guard/readiness receipt. Workers update only verified checkboxes/Status; hashes/results and handoff belong in separate progress. Stop on BLOCKED or unchanged failed input rather than auto-retry.

Progress: `.roadmap-runner/backend-sdk-adapters-20261024/02a-filament-admin.progress.md` (architecture-relative, ignored). Record exact commands/runtime/inputs and meaningful pass/fail/skip counts, retain only active failure diagnostics and reuse unchanged results.

## Epic BFA-1 — Deliver the optional Filament admin adapter

### Task BFA-1.1 — Create the separately installable Filament wrapper

- [ ] BFA-1.1 Create the separately installable Filament wrapper.

Purpose: Deliver this integration boundary while keeping shared persistence behavior in the framework-independent PHP SDK.
Deliverable: adapters/admin/filament/composer.json; adapters/admin/filament/src/.
Context: [SDK contract: PHP SDK, Laravel wrapper and Filament](../../specs/backend-sdk-adapters.md#php-sdk-laravel-wrapper-and-filament); actual source exports and named predecessor results only.
Dependencies: none (validated PHP SDK and Laravel entry only).
Independent work: Other validated entry/local boundaries remain eligible; optional UI and collaboration do not gate the plain PHP client.
Session scope: One boundary, 15–45 minutes including focused checks; split before expanding into a missing shared API.
Acceptance: A distinct optional Composer package requires the Laravel wrapper and declared Filament/Livewire baseline, registers field/assets configuration and has no independent persistence implementation. Plain PHP and Laravel installs do not pull in Filament.

Implementation:

- [ ] BFA-1.1-I1 Add package/service-provider metadata and dependencies that reuse the Laravel and browser SDK services. Declare actual capability/runtime ranges before claiming support. Register one focused delivery selector; defer broad test authoring to the final testing files.

Validation:

- [ ] BFA-1.1-V1 Run `node scripts/sdk-adapter-delivery.mjs BFA-1.1`: Boot a minimal local Filament application with the package and inspect the plain PHP/Laravel install graphs to confirm Filament remains optional. Budget: 1–3 minutes or at most 5 minutes for local build/bootstrap; reuse unchanged passing results.

Evidence: The ignored progress path above records source inputs, command/runtime/exit and meaningful executed/passed/failed/skipped counts; retain only active failure diagnostics.
Handoff: Delivered interface, exact last substep, missing prerequisite and next bounded action.
Blocked behavior: Leave BFA-1.1 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BFA-1.2 — Mount the real editor as a Filament field

- [ ] BFA-1.2 Mount the real editor as a Filament field.

Purpose: Deliver this integration boundary while keeping shared persistence behavior in the framework-independent PHP SDK.
Deliverable: adapters/admin/filament/src/Forms/; adapters/admin/filament/resources/views/; adapters/admin/filament/resources/js/.
Context: [SDK contract: PHP SDK, Laravel wrapper and Filament](../../specs/backend-sdk-adapters.md#php-sdk-laravel-wrapper-and-filament); actual source exports and named predecessor results only.
Dependencies: BFA-1.1.
Independent work: Other validated entry/local boundaries remain eligible; optional UI and collaboration do not gate the plain PHP client.
Session scope: One boundary, 15–45 minutes including focused checks; split before expanding into a missing shared API.
Acceptance: Custom field/Blade/Alpine glue lazily mounts the existing browser SDK using stable document identity and proper nested state path. Label/error/accessibility associations, configured extensions and disabled/read-only state are preserved; rerenders do not re-import content.

Implementation:

- [ ] BFA-1.2-I1 Connect documented field/asset extension points to one existing editor lifecycle. Keep editor-owned DOM stable and register explicit teardown without copying renderer or history code. Register one focused delivery selector; defer broad test authoring to the final testing files.

Validation:

- [ ] BFA-1.2-V1 Run `node scripts/sdk-adapter-delivery.mjs BFA-1.2`: Mount one real field, perform an edit and a prepared Livewire state refresh, then dispose; verify unchanged document identity, one engine instance and no readonly mutation. Budget: 1–3 minutes or at most 5 minutes for local build/bootstrap; reuse unchanged passing results.

Evidence: The ignored progress path above records source inputs, command/runtime/exit and meaningful executed/passed/failed/skipped counts; retain only active failure diagnostics.
Handoff: Delivered interface, exact last substep, missing prerequisite and next bounded action.
Blocked behavior: Leave BFA-1.2 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BFA-1.3 — Connect form submission to SDK persistence

- [ ] BFA-1.3 Connect form submission to SDK persistence.

Purpose: Deliver this integration boundary while keeping shared persistence behavior in the framework-independent PHP SDK.
Deliverable: adapters/admin/filament/src/Forms/; adapters/admin/filament/src/Save/.
Context: [SDK contract: PHP SDK, Laravel wrapper and Filament](../../specs/backend-sdk-adapters.md#php-sdk-laravel-wrapper-and-filament); actual source exports and named predecessor results only.
Dependencies: BFA-1.2.
Independent work: Other validated entry/local boundaries remain eligible; optional UI and collaboration do not gate the plain PHP client.
Session scope: One boundary, 15–45 minutes including focused checks; split before expanding into a missing shared API.
Acceptance: Livewire binds compact document reference/revision/form metadata, not full binary content per keystroke. Submit coordinates SDK flush and configured model association transaction; optional independent autosave declares its separate commit. Validation/conflict/authorization failure preserves edits and cannot manufacture a receipt.

Implementation:

- [ ] BFA-1.3-I1 Delegate saving to the Laravel SDK wrapper and define explicit create/draft/submit/autosave ownership. Do not infer durability from dehydration or a successful Livewire response. Register one focused delivery selector; defer broad test authoring to the final testing files.

Validation:

- [ ] BFA-1.3-V1 Run `node scripts/sdk-adapter-delivery.mjs BFA-1.3`: Using real local SQLite and prepared policy, submit one edited record and reopen it; force a form/storage rejection and verify no false saved state or committed model association. Budget: 1–3 minutes or at most 5 minutes for local build/bootstrap; reuse unchanged passing results.

Evidence: The ignored progress path above records source inputs, command/runtime/exit and meaningful executed/passed/failed/skipped counts; retain only active failure diagnostics.
Handoff: Delivered interface, exact last substep, missing prerequisite and next bounded action.
Blocked behavior: Leave BFA-1.3 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BFA-1.4 — Handle nested fields and modal lifetimes

- [ ] BFA-1.4 Handle nested fields and modal lifetimes.

Purpose: Deliver this integration boundary while keeping shared persistence behavior in the framework-independent PHP SDK.
Deliverable: adapters/admin/filament/src/Forms/; adapters/admin/filament/resources/js/.
Context: [SDK contract: PHP SDK, Laravel wrapper and Filament](../../specs/backend-sdk-adapters.md#php-sdk-laravel-wrapper-and-filament); actual source exports and named predecessor results only.
Dependencies: BFA-1.3.
Independent work: Other validated entry/local boundaries remain eligible; optional UI and collaboration do not gate the plain PHP client.
Session scope: One boundary, 15–45 minutes including focused checks; split before expanding into a missing shared API.
Acceptance: Resource create/edit and action-modal fields have stable distinct identities across repeater/nested paths, modal reopen and Livewire navigation. Required/validation/read-only states and explicit unsaved-close policy apply; no duplicate session, writer or stale callback crosses field lifetimes.

Implementation:

- [ ] BFA-1.4-I1 Map documented field paths/operation and lifecycle hooks to existing mount/dispose behavior. Keep configurable upload/collaboration capabilities opt-in and routed through existing policies/ports. Register one focused delivery selector; defer broad test authoring to the final testing files.

Validation:

- [ ] BFA-1.4-V1 Run `node scripts/sdk-adapter-delivery.mjs BFA-1.4`: Run one prepared two-field nested/modal open-close-reopen fixture and confirm isolated content, stable identities, retained recovery and one teardown per owned editor. Budget: 1–3 minutes or at most 5 minutes for local build/bootstrap; reuse unchanged passing results.

Evidence: The ignored progress path above records source inputs, command/runtime/exit and meaningful executed/passed/failed/skipped counts; retain only active failure diagnostics.
Handoff: Delivered interface, exact last substep, missing prerequisite and next bounded action.
Blocked behavior: Leave BFA-1.4 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

### Task BFA-1.5 — Deliver the Filament Resource example and install guide

- [ ] BFA-1.5 Deliver the Filament Resource example and install guide.

Purpose: Deliver this integration boundary while keeping shared persistence behavior in the framework-independent PHP SDK.
Deliverable: examples/sdk-adapters/filament/; adapters/admin/filament/README.md.
Context: [SDK contract: PHP SDK, Laravel wrapper and Filament](../../specs/backend-sdk-adapters.md#php-sdk-laravel-wrapper-and-filament); actual source exports and named predecessor results only.
Dependencies: BFA-1.4.
Independent work: Other validated entry/local boundaries remain eligible; optional UI and collaboration do not gate the plain PHP client.
Session scope: One boundary, 15–45 minutes including focused checks; split before expanding into a missing shared API.
Acceptance: Runnable local Resource create/edit/action example documents the three-package dependency chain, canonical storage/model-reference mapping, assets, application policies and honest local/remote/conflict states. Collaboration/assets are optional; no registry publication or third-party credentials are needed.

Implementation:

- [ ] BFA-1.5-I1 Provide a minimal admin example using the delivered SDK/wrappers and documented local setup. State the selected baseline and unsupported modes without adding alternate editor versions. Register one focused delivery selector; defer broad test authoring to the final testing files.

Validation:

- [ ] BFA-1.5-V1 Run `node scripts/sdk-adapter-delivery.mjs BFA-1.5`: Follow the documented local install and one Resource edit/save/reopen plus canceled-modal flow with prepared data; reuse prior byte/transaction results and tear down owned browsers/servers. Budget: 1–3 minutes or at most 5 minutes for local build/bootstrap; reuse unchanged passing results.

Evidence: The ignored progress path above records source inputs, command/runtime/exit and meaningful executed/passed/failed/skipped counts; retain only active failure diagnostics.
Handoff: Delivered interface, exact last substep, missing prerequisite and next bounded action.
Blocked behavior: Leave BFA-1.5 unchecked; record owner, source/error fingerprint, attempted repair and changed-input resume condition. No unchanged retry.

## Milestone handoff

Record delivered interfaces, actual selectors/results and remaining qualification in the separate ignored progress path above. Reuse accepted evidence; the two final testing files own comprehensive cases and full-plan qualification. No publication or runner start is authorized.
