# 06 dart toolchain

Status: IN_PROGRESS

Workspace: `core` from root `/Users/bpstr/Github/edit-ac`; task paths are core-relative unless repository-prefixed.
Progress: `/Users/bpstr/Github/edit-ac/.roadmap-runner/os-deferred-integrations-20261026/06-dart-toolchain.progress.md`.
Origin: `/Users/bpstr/Github/edit-ac/architecture/runner-queues/dependency-closed-ui-20261025/02-cross-mobile-toolchain.md`.

## Current controller authority and scope

The user explicitly requested deferring all OS checks and completing remaining independent integration work on 2026-10-26. This is the current selected owner of the original task contracts below; the broad originating sources remain preserved as history. Current controller: `architecture/runner-queues/os-deferred-integrations-20261026/manifest.json`. Read the current PRIMARY section of `.roadmap-coordination/parallel-clients.md` before each parent. One serial guarded PRIMARY runner, one bounded original parent per iteration; the independent EDITOR lane is protected.

Defer VM/guest operations, emulator or simulator/device checks, native UI/IME execution, native target bootstrap/readiness qualification and native desktop-shell execution. Do not start, stop, inspect for readiness or wait on a guest; do not turn a fixture or compilation into target-OS proof. Headless Swift/Kotlin/Dart consumers, local compiler/package checks, Node/PHP/SQLite and browser fixtures are allowed. Flutter/Dart doctor/compiler metadata checks on the current host are permitted; toolchain discovery may report platform capabilities as available/unknown/unsupported without launching a native target or running native OS qualification probes. No paid cloud provisioning, model/provider calls, secret loading, publication, push or deployment. All automated checks use prepared deterministic content and mocked provider/network transports.

Preserve every acceptance criterion below. A headless consumer must use the actual declared binding and existing shared authority; a stub is not a replacement for that boundary. If a selected check unexpectedly needs an excluded OS operation, record the exact unmet owner and changed-input condition, leave acceptance unchecked and return BLOCKED. Never retry unchanged input. Planned selectors and missing local wrappers are owned implementation work. Reuse compatible passing receipts; run only the affected named focused delivery check during functionality. Comprehensive backend/web verification follows all ten selected environment/functional parents; deferred native work is outside this run's phase barrier, not marked complete or used as a passed prerequisite. Broader native/all-platform qualification remains required and deferred. Current scope retains the basis plan's Node/browser, PHP/Laravel/Filament/SQLite and actually delivered headless clients; unselected languages, databases and OS targets gain no support claim. Existing caps, unknown-data preservation and single current production format remain unchanged.

Workers update only verified checkbox states and Status in this selected source. Store delivery text, source/artifact hashes and counts in the separate progress file; never write a source delivery summary. After two parents and at source boundaries, hold root `.roadmap-coordination/integration.lock`; checkpoint only validated safely separable owned source. Preserve inherited/unrelated dirty bytes and indexes; do not stage snapshots, source from the EDITOR checkout, generated artifacts or unrelated work. Keep mixed inherited implementation pending with exact owned patches if safe landing is unavailable. Clean task-owned inactive outputs/browsers/servers, preserve active processes and check disk. No agents or extra controllers.

## Selected original contracts

### Task ECM-1.1 — Prepare a pinned local Flutter and Dart profile

- [ ] ECM-1.1 Prepare a pinned local Flutter and Dart profile.

Purpose: Replace a predictable missing-toolchain gate with owned reproducible setup.
Deliverable: architecture/toolchains/flutter-development.json; sdk/dart/; adapters/native/flutter/.
Context: Current consuming task/toolchain lockfiles and the selected platform's existing build scripts; use official maintained runtime sources.
Dependencies: none.
Independent work: Other ready source files are coordinator-selected; no second controller.
Session scope: One setup boundary,30–45minutes including focused checks; checkpoint exact remaining setup before the deadline. Package download/install is implementation time, not a five-minute validation loop.
Acceptance: Run the pinned doctor/compiler and compile one empty local Dart consumer; record actual toolchain/platform capabilities and ensure unsupported desktop targets are explicit. Do not call a synthetic app native-runtime proof.

Implementation:

- [ ] ECM-1.1-I1 Install/reuse one maintained local Flutter/Dart toolchain for the selected mobile/web plugins, using official archives and verified hashes. Keep downloaded SDK/cache outside Git, bound storage, and configure existing Xcode/Android SDK. No paid remote build or publishing.

Validation:

- [ ] ECM-1.1-V1 Execute only the concrete bootstrap in Acceptance, budget5minutes once installation finishes. Require real runtime/tool provenance, meaningful nonzero pass counts and zero unresolved failures/required skips; report installation/compile failures honestly. Keep receipt and downloaded outputs ignored.

Evidence: Configured progress, authored setup/config source, exact commands/version/digests/counts and cleanup. No credentials or compiled images in Git.
Handoff: Last successful installation/compiler step, paths and exact next command.
Blocked behavior: Stop only on a genuine unavailable external host/license or failed installation after a changed-input repair; record owner and precise unblock signal once. Never claim unsupported target success.
