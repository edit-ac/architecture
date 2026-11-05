# Deliver first-class Expo integration

Status: IN_PROGRESS

## Goal and entry conditions

Goal: Deliver first-class Expo integration. Planning source: 2026-10-24. Workspace: `core`. This is functional work; no completed capability is implied.

Authority: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); [native ownership](../../specs/native-ui-integrations.md#scope-and-authority) where applicable; existing canonical format, input and durability contracts remain authoritative.

Progress: `.roadmap-runner/editor-ui-integrations-20261024/22-expo-integration.progress.md` (architecture-relative, ignored). Every task records its own source/interface receipt, actual selector/runtime/exit and meaningful executed/passed/failed/skipped counts here.

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

## Epic UEX-1 — Deliver first-class Expo integration

### Task UEX-1.1 — Freeze Expo package and native compatibility profile

- [ ] UEX-1.1 Freeze Expo package and native compatibility profile.

Purpose: Freeze Expo package and native compatibility profile so applications can reuse this integration boundary.
Deliverable: `packages/expo/; adapters/native/react-native/; examples/sdk-adapters/react-native/`.
Context: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [URN-1.1](21-react-native-ui.md).
Dependencies: none.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: One maintained Expo/RN/Hermes/New Architecture/toolchain profile maps to the existing native bridge; bare RN remains Expo-free, and native module absence yields actionable development-build guidance.

Implementation:

- [ ] UEX-1.1-I1 Add optional Expo package/config entry and compatibility declarations; use the canonical BCP module rather than a parallel Expo view.
- [ ] UEX-1.1-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UEX-1.1-V1 Run `node scripts/ui-integration-delivery.mjs UEX-1.1`: Compile native-module presence detection against prepared present/missing exports and inspect package peer graph. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UEX-1.1 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UEX-1.2 — Implement idempotent Expo config plugin

- [ ] UEX-1.2 Implement idempotent Expo config plugin.

Purpose: Implement idempotent Expo config plugin so applications can reuse this integration boundary.
Deliverable: `packages/expo/plugin/`.
Context: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UEX-1.1.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: CNG/prebuild applies only required native config, preserves app-owned keys and does not duplicate entries or grant unrelated permissions. Autolinking remains the owner where sufficient.

Implementation:

- [ ] UEX-1.2-I1 Implement plugin mods for actual required editor assets/build settings; document no-op behavior where no mods are needed and committed-native-project usage.
- [ ] UEX-1.2-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UEX-1.2-V1 Run `node scripts/ui-integration-delivery.mjs UEX-1.2`: Apply the plugin twice to deterministic iOS/Android config fixtures and compare outputs; reject unsupported baseline with useful diagnostics. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UEX-1.2 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UEX-1.3 — Wire iOS development-build consumer

- [ ] UEX-1.3 Wire iOS development-build consumer.

Purpose: Wire iOS development-build consumer so applications can reuse this integration boundary.
Deliverable: `examples/sdk-adapters/react-native/expo/`.
Context: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [URN-1.2](21-react-native-ui.md).
Dependencies: UEX-1.1, UEX-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: An Expo iOS development build includes the canonical native editor/view and default controls, with local build instructions and no Expo Go/WebView substitution.

Implementation:

- [ ] UEX-1.3-I1 Add iOS-specific example configuration and native package linkage over existing BCP host; require a prepared local toolchain and split cold provisioning to its owner.
- [ ] UEX-1.3-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UEX-1.3-V1 Run `node scripts/ui-integration-delivery.mjs UEX-1.3`: Compile one local iOS development target and inspect native view/module linkage; target-runtime interaction belongs to final observation. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UEX-1.3 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UEX-1.4 — Wire Android development-build consumer

- [ ] UEX-1.4 Wire Android development-build consumer.

Purpose: Wire Android development-build consumer so applications can reuse this integration boundary.
Deliverable: `examples/sdk-adapters/react-native/expo/`.
Context: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [URN-1.2](21-react-native-ui.md).
Dependencies: UEX-1.1, UEX-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: An Expo Android development build includes the same canonical bridge and default controls; ABI/native-library packaging is explicit and native-module absence does not become silent fallback.

Implementation:

- [ ] UEX-1.4-I1 Add Android configuration/autolinking/asset requirements to the shared example; reuse the existing Android native host and prepared local toolchain.
- [ ] UEX-1.4-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UEX-1.4-V1 Run `node scripts/ui-integration-delivery.mjs UEX-1.4`: Compile one local Android development target and inspect packaged native module/view registration. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UEX-1.4 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UEX-1.5 — Integrate Expo Router and screen presentation

- [ ] UEX-1.5 Integrate Expo Router and screen presentation.

Purpose: Integrate Expo Router and screen presentation so applications can reuse this integration boundary.
Deliverable: `packages/expo/; examples/sdk-adapters/react-native/expo/`.
Context: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [URN-1.3](21-react-native-ui.md), [URN-1.6](21-react-native-ui.md).
Dependencies: UEX-1.3, UEX-1.4.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Router screens/modals reuse RN lifecycle, overlay owners and safe-area/keyboard hooks; route transitions or theme changes do not silently lose edits or create duplicate sessions.

Implementation:

- [ ] UEX-1.5-I1 Add thin screen/container recipe and host-control configuration; delegate save/background/dispose algorithms to BCP/BNA and stage exact BNT acceptance additions.
- [ ] UEX-1.5-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UEX-1.5-V1 Run `node scripts/ui-integration-delivery.mjs UEX-1.5`: Compile one route/modal example and replay a prepared navigation/canceled-result UI transcript; reuse existing persistence lifecycle evidence. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UEX-1.5 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UEX-1.6 — Define runtime-version and native capability guard

- [ ] UEX-1.6 Define runtime-version and native capability guard.

Purpose: Define runtime-version and native capability guard so applications can reuse this integration boundary.
Deliverable: `packages/expo/; examples/sdk-adapters/react-native/expo/`.
Context: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UEX-1.1, UEX-1.2.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Native binary/view ABI changes require a matching build/runtime policy; a JS bundle expecting missing native control fields fails explicitly before mutation. No update is published by this task.

Implementation:

- [ ] UEX-1.6-I1 Add capability handshake and documented runtime-version/fingerprint guidance aligned with maintained Expo APIs; keep editor document identity independent.
- [ ] UEX-1.6-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UEX-1.6-V1 Run `node scripts/ui-integration-delivery.mjs UEX-1.6`: Run prepared compatible/missing-native capability inputs and inspect the local config policy; no network EAS command. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UEX-1.6 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UEX-1.7 — Add Expo UI control recipe

- [ ] UEX-1.7 Add Expo UI control recipe.

Purpose: Add Expo UI control recipe so applications can reuse this integration boundary.
Deliverable: `examples/ui/expo-ui/`.
Context: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: Inherited through the listed local dependencies; no additional earlier-file gate.
Dependencies: UEX-1.3, UEX-1.4, UEX-1.5.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: A supported Expo UI toolbar/menu recipe wraps the existing RN editor with proper Host nesting, native target/focus ownership and explicit per-platform control availability; no replacement editor surface.

Implementation:

- [ ] UEX-1.7-I1 Map UI state and theme to maintained Expo UI primitives in an optional example; make fallback controls explicit where an upstream primitive is absent.
- [ ] UEX-1.7-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UEX-1.7-V1 Run `node scripts/ui-integration-delivery.mjs UEX-1.7`: Compile one iOS and Android entry and replay one command through the same native bridge; qualify visual focus later. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UEX-1.7 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

### Task UEX-1.8 — Add explicit Expo web profile

- [ ] UEX-1.8 Add explicit Expo web profile.

Purpose: Add explicit Expo web profile so applications can reuse this integration boundary.
Deliverable: `packages/expo/; examples/sdk-adapters/react-native/expo/`.
Context: [named contract section](../../specs/native-ui-integrations.md#react-native-and-expo); actual exported symbols in Deliverable and the named predecessor receipt only.
Entry receipts: [URC-1.4](04-react-ui.md).
Dependencies: UEX-1.1, UEX-1.6.
Independent work: Any sibling with its own prerequisites satisfied; no inherited sibling-platform blocker.
Session scope: One named boundary, 15–45 minutes including checks; return missing host/semantic work to its owner.
Acceptance: Conditional exports select the existing React/browser editor on web with SSR-safe imports and shared controls; web bundles exclude native artifacts, and native bundles exclude DOM editor code.

Implementation:

- [ ] UEX-1.8-I1 Add the platform resolver and web example UI over existing React UI APIs; declare web/native capability differences and asset loading.
- [ ] UEX-1.8-I2 Wire the named consumer/exports and focused selector; record missing prerequisite APIs with their existing owner.

Validation:

- [ ] UEX-1.8-V1 Run `node scripts/ui-integration-delivery.mjs UEX-1.8`: Build web and inspect both platform import graphs; mount one prepared browser editor and command without native module lookup. Budget: 1–3 minutes; prepared native startup at most 5. Count inspection cases separately.

Evidence: Progress path above; source/interface, selector/runtime/exit, inspected or executed/passed/failed/skipped counts and reused receipt.
Handoff: In progress, record last substep/symbol, failing input, owner receipt and next bounded action.
Blocked behavior: Leave UEX-1.8 unchecked; record the blocking fingerprint and exact changed-input resume condition. No unchanged retry; independent ready work requires the coordinator policy above.

## Milestone handoff

In `.roadmap-runner/editor-ui-integrations-20261024/22-expo-integration.progress.md`, summarize delivered public interfaces/package boundaries, the scoped selector results and limitations needed by dependents. Consume compatible prior evidence without a fresh full run. Final acceptance remains with the designated files 26–29, existing BNT parents and roadmap43; source checkmarks alone cannot qualify a platform.

## Current prerequisite receipts

Controller repair2026-10-25: the selected prerequisite owners below are queued before their consumers. Read only the named task/interface result from its exact progress file; source order alone is not proof. Missing planned paths/selectors owned by the selected task must be implemented, not treated as someone else's absent roadmap. No acceptance criterion is waived.

- URC-1.4: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/04-react-ui.progress.md`.
- URN-1.1: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/21-react-native-ui.progress.md`.
- URN-1.2: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/21-react-native-ui.progress.md`.
- URN-1.3: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/21-react-native-ui.progress.md`.
- URN-1.6: `/Users/bpstr/Github/edit-ac/architecture/.roadmap-runner/editor-ui-integrations-20261024/21-react-native-ui.progress.md`.
