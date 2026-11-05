# Prepare installable UI packages and integration guides

Status: IN_PROGRESS

## Goal and entry conditions

Goal: Prepare installable UI packages and integration guides. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/25-packages-and-guides.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

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

## Epic UPG-1 — Prepare installable UI packages and integration guides

### Task UPG-1.1 — Finalize web exports and peer manifests

- [ ] UPG-1.1 Finalize web exports and peer manifests.

Purpose: Finalize web exports and peer manifests so applications can reuse this integration boundary.
Deliverable: `packages/*/package.json; registry/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [USK-1.3](13-shadcn-vue-svelte.md), [USK-1.6](13-shadcn-vue-svelte.md), [USR-1.6](12-shadcn-react.md), [UWH-1.6](14-web-host-integrations.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: All new web UI adapter exports resolve types and CSS, declare real optional peers and avoid mandatory cross-framework dependencies; generated outputs remain outside Git.

Implementation:

- [ ] UPG-1.1-I1 Reconcile package graph/exports with implementation receipts and authored license/notices; remove accidental aggregator imports.
- [ ] UPG-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UPG-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UPG-1.1`: Inspect export targets and build only changed package declarations; final all-consumer matrix remains final-owned. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UPG-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UPG-1.2 — Finalize native and cross-platform package metadata

- [ ] UPG-1.2 Finalize native and cross-platform package metadata.

Purpose: Finalize native and cross-platform package metadata so applications can reuse this integration boundary.
Deliverable: `native/*/; adapters/native/; packages/expo/; packages/flutter*/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [UAN-1.5](18-android-ui.md), [UEX-1.8](22-expo-integration.md), [UFL-1.7](23-flutter-mobile-ui.md), [UFW-1.3](24-flutter-web-and-desktop-profiles.md), [UIA-1.5](16-apple-mobile-ui.md), [ULX-1.3](20-linux-desktop-ui.md), [UMA-1.4](17-macos-ui.md), [URN-1.6](21-react-native-ui.md), [UWI-1.4](19-windows-ui.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Apple/Android/Windows/Linux/RN/Expo/Flutter consumers have explicit products/modules/platforms and minimum toolchains; no native binary or registry bundle is tracked in source.

Implementation:

- [ ] UPG-1.2-I1 Reconcile package metadata and optional design-system dependencies with actual delivered code; keep Dart SDK and bare RN independently consumable.
- [ ] UPG-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UPG-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UPG-1.2`: Build only changed metadata/codegen entry declarations and inspect tracked-file exclusions; no new target-runtime claim. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UPG-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UPG-1.3 — Publish authored support manifest and override examples

- [ ] UPG-1.3 Publish authored support manifest and override examples.

Purpose: Publish authored support manifest and override examples so applications can reuse this integration boundary.
Deliverable: `sdk/contracts/ui-support.json; examples/ui/; ../architecture/specs/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UPG-1.1, UPG-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: An authored support manifest distinguishes implementation from qualification by framework/library/OS/host/surface and records peer ranges; copied registry source ownership and fallback limits are explicit.

Implementation:

- [ ] UPG-1.3-I1 Write source support declarations and concise custom-control/theme examples using actual public names; link final evidence from ignored progress rather than committing generated reports.
- [ ] UPG-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UPG-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UPG-1.3`: Check each manifest claim against delivered receipts and compile the smallest custom-control example for each API family. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UPG-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UPG-1.4 — Write framework and Laravel UI guides

- [ ] UPG-1.4 Write framework and Laravel UI guides.

Purpose: Write framework and Laravel UI guides so applications can reuse this integration boundary.
Deliverable: `../docs/content/docs/guides/; examples/sdk-adapters/laravel/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UPG-1.1, UPG-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Guides install default/plain, React/Vue/Svelte/shadcn and Filament controls using actual package names; explain customization, content versus chrome styling and existing save/form ownership.

Implementation:

- [ ] UPG-1.4-I1 Extend existing backend/framework guides with UI-specific sections and one public/admin shared-document walkthrough; do not duplicate persistence setup.
- [ ] UPG-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UPG-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UPG-1.4`: Resolve local links and compare import/install examples to manifests; one representative example build, reuse earlier equivalent outputs. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UPG-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UPG-1.5 — Write native, Expo and Flutter integration guides

- [ ] UPG-1.5 Write native, Expo and Flutter integration guides.

Purpose: Write native, Expo and Flutter integration guides so applications can reuse this integration boundary.
Deliverable: `../docs/content/docs/guides/; examples/sdk-adapters/react-native/; examples/sdk-adapters/flutter/`.
Context: [named contract section](../../specs/editor-ui-integrations.md#acceptance-and-support-gates); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UPG-1.2, UPG-1.3.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Guides state required development builds, native linkage/runtime policy, Material/Cupertino/native source-kit choices, web profiles and unsupported desktop combinations; no Expo Go or WebView parity claim.

Implementation:

- [ ] UPG-1.5-I1 Add installation/customization recipes over BCP examples and per-platform availability notes; document local-only validation and upgrade/rebuild requirements.
- [ ] UPG-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UPG-1.5-V1 Run `node scripts/ui-integration-delivery.mjs UPG-1.5`: Check commands/imports against delivered metadata and source support manifest; no paid cloud service or production update execution. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UPG-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/25-packages-and-guides.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- UAN-1.5: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/18-android-ui.progress.md`.
- UEX-1.8: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/22-expo-integration.progress.md`.
- UFL-1.7: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/23-flutter-mobile-ui.progress.md`.
- UFW-1.3: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/24-flutter-web-and-desktop-profiles.progress.md`.
- UIA-1.5: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/16-apple-mobile-ui.progress.md`.
- ULX-1.3: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/20-linux-desktop-ui.progress.md`.
- UMA-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/17-macos-ui.progress.md`.
- URN-1.6: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/21-react-native-ui.progress.md`.
- USK-1.3: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/13-shadcn-vue-svelte.progress.md`.
- USK-1.6: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/13-shadcn-vue-svelte.progress.md`.
- USR-1.6: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/12-shadcn-react.progress.md`.
- UWH-1.6: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/14-web-host-integrations.progress.md`.
- UWI-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/19-windows-ui.progress.md`.
