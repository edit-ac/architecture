# Integrate and package the browser SDK

Status: IN_PROGRESS

Qualification amendment (user decision, 2026-10-14): Physical devices, named target-platform simulators/emulators and desktop OS VMs/test hosts are accepted for platform and release qualification under the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms). Missing physical hardware does not block completion. Execute required behavior against the implemented target-platform runtime; document and test virtual equivalents for unavailable hardware-only input/accessibility cases. Record physical versus virtual provenance and measure performance in the tested environment. This supersedes earlier physical-only or manual-only clauses below; it does not complete unchecked tasks or waive implementation, correctness, security or artifact gates.

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Deliver only the outcomes below. Read `../architecture/specs/packages-release.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Upstream entry gates: `04-browser-input.md` complete at current source revision with passing artifact evidence, `05-markdown-content.md` complete at current source revision with passing artifact evidence, `06-synchronization.md` complete at current source revision with passing artifact evidence, `07-extension-modules.md` complete at current source revision with passing artifact evidence.

Retain the [baseline typing/rendering gate](../specs/web.md#baseline-typing-and-rendering-guarantees): `npm run check:browser-baseline` passes unfiltered at the reviewed source/artifact revisions before SDK acceptance. Public examples use the common surface mount. Tracks 38/42 expand regression coverage without deferring basic editing or presentation fixes.

Framework integration scope (2026-10-13): The Rust/WASM engine and imperative web SDK are framework-independent. Deliver first-party React and Astro bindings as thin, optional consumers of the same lifecycle and document contracts. SDK-1.7 adds Astro independently of React; SDK-1.4 and SDK-1.6 qualify and document both integrations. Reuse this boundary for future framework integrations with their own lifecycle, packed-consumer and executable-example evidence. Integration guides and examples are a product adoption channel; additional frameworks remain candidates until explicitly scoped and qualified. Astro 7's [Rust compiler rewrite](https://astro.build/blog/astro-7/) aligns with edit.ac's Rust-first philosophy, without establishing editor compatibility or performance evidence.

Controller handoff (2026-10-13): Continue this track with GPT-6.1 Sol, medium effort, and hourly monitoring; the user authorized resolving roadmap implementation/tooling/prerequisite blockers without asking. Accept roadmap 05 as the upstream baseline under the user’s earlier explicit "Assume roadmap 5 as completed" instruction; preserve its outstanding FMT-1.15 physical or virtual platform qualification and do not claim that evidence exists. Tracks 06 and 07 completed at their current source revisions; controller completion reviews are in `../../evidence/roadmap-06-runner/completion-review.json` and `../../evidence/roadmap-07-runner/completion-review.json`. Track 04’s old progress-header revision is superseded by the baseline-typing verification at the current roadmap source revision (`../evidence/baseline-typing/verification.json`); retain historical evidence and the separately tracked history-selection limitation. SDK-1.1 must run the unfiltered `npm run check:browser-baseline` against current implementation/artifacts before SDK acceptance, alongside its named package checks. Do not waive footprint/performance/release gates or claim native/device parity. Repairs must be serialized against the active core worker; no unchanged retry, publication, deployment, paid synthetic inference or later-track expansion is authorized.

Migration sequencing (2026-10-13): SDK-1.5 content conversion and DOC-1.15–1.27 editor migration guides are deferred until the entire application is completed and correctly qualified, by explicit user instruction. Their unchanged original contracts and activation gate live in `../operations/deferred-content-migrations.md`. Preserve partial code/evidence; do not implement or test migration features in this track. SDK-1.6 delivers integration/recovery examples independently of migration. This deferral does not waive ordinary data preservation, internal version compatibility or app qualification.

Controller direction (2026-10-13, optional Markdown): The user explicitly authorized making Markdown an extension to resolve the default bundle-size gate. Prioritize SDK-1.8-I3 extraction of the portable parser and Markdown browser adapters into an independently consumed optional boundary before further generic micro-optimizations. Default Task no longer requires Markdown assets or syntax interpretation; extension-enabled consumers retain full existing Markdown behavior. This supersedes only the earlier default-Markdown packaging and no-Markdown-exclusion restriction. Both hard caps, all other required default features, safe international links, one state owner, portable/native support, migration deferral and inference/release restrictions remain unchanged. Reconcile previous I1/I2/V2 evidence against the new profiles; source change is not a completed implementation or size pass.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus validation; if a boundary is too large, stop with a precise proposed split for the controller. Pick a task only when every named dependency is implemented and validated. Other ready tasks are permitted independent work; a roadmap entry gate remains mandatory for its dependents. Do not launch this roadmap while its upstream gate is unavailable.

Create named checks before invoking them. Record nonzero executed/passed/failed/skipped counts; missing tests and zero-match Rust filters fail acceptance. Run the narrow check, then relevant integration checks. Use prepared fixtures and transports only. No model API tests, live dogfood, background runner startup or publication outside an explicit release task.

## Epic SDK-1 — Integrate and package the browser SDK

### Task SDK-1.1 — Verify public SDK prerequisites

- [ ] SDK-1.1 Verify public SDK prerequisites.

Purpose: Deliver verify public SDK prerequisites as one reviewable boundary.
Context: `packages/core/`; `packages/web/`; `../architecture/evidence/modules.md`; `../architecture/specs/packages-release.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: No exported method returns fake success or hides unsupported behavior; API examples map to working symbols.

Implementation:

- [ ] SDK-1.1-I1 Check browser lifecycle, module API, Markdown and synchronization evidence. Freeze only implemented public types and error variants.

Validation:

- [ ] SDK-1.1-V1 npm run check:packages. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SDK-1.1` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SDK-1.1`.
Blocked behavior: Leave `SDK-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task SDK-1.2 — Finish imperative SDK and task preset

- [ ] SDK-1.2 Finish imperative SDK and task preset.

Purpose: Deliver finish imperative SDK and task preset as one reviewable boundary.
Context: `packages/web/src/index.ts`; `examples/task-editor/`; `tests/browser/sdk.spec.ts`; `../architecture/specs/packages-release.md`.
Dependencies: SDK-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: One task example edits, pastes Markdown, recovers offline and attaches sync without recreating its document; chains validate before any mutation.

Implementation:

- [ ] SDK-1.2-I1 Expose createEditor, validated command chains/can, scoped subscribe, attachSync, flush and destroy; add explicit task preset options and a minimal standalone example.

Validation:

- [ ] SDK-1.2-V1 npm run test:browser -- sdk. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SDK-1.2` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SDK-1.2`.
Blocked behavior: Leave `SDK-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task SDK-1.3 — Implement the thin React wrapper

- [ ] SDK-1.3 Implement the thin React wrapper.

Purpose: Deliver implement the thin React wrapper as one reviewable boundary.
Context: `packages/react/`; `tests/browser/react.spec.ts`; `../architecture/specs/packages-release.md`.
Dependencies: SDK-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Typing/selection does not rerender the document through React; remount does not duplicate handles/listeners; SSR import is safe.

Implementation:

- [ ] SDK-1.3-I1 Add verified React peer dependency range and lifecycle host component/hooks. Keep document ownership outside React and handle strict-mode mount/unmount.

Validation:

- [ ] SDK-1.3-V1 npm run test:browser -- react. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SDK-1.3` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SDK-1.3`.
Blocked behavior: Leave `SDK-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task SDK-1.4 — Prove packed ESM and WASM consumers

- [ ] SDK-1.4 Prove packed ESM and WASM consumers.

Purpose: Deliver prove packed ESM and WASM consumers as one reviewable boundary.
Context: `tests/packed-consumers.test.mjs`; `packages/*/package.json`; `../architecture/specs/packages-release.md`.
Dependencies: SDK-1.3, SDK-1.7.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Consumers resolve only tarball contents, no source/workspace paths; one core runtime owner; WASM and declarations load under documented hosting.

Implementation:

- [ ] SDK-1.4-I1 Pack local built SDKs and install into isolated plain browser, React/SSR and Astro 7 static/SSR fixtures; verify declarations, exports, asset URL/CSP loading and Apache license inclusion. Astro consumes @edit-ac/astro plus the shared core/web artifacts without a React dependency; validate compiled .astro components and distributed client assets without workspace aliases.

Validation:

- [ ] SDK-1.4-V1 npm run build:wasm; npm run build; node --test tests/packed-consumers.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SDK-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SDK-1.4`.
Blocked behavior: Leave `SDK-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task SDK-1.6 — Write integration and recovery examples

- [ ] SDK-1.6 Write integration and recovery examples.

Purpose: Deliver write integration and recovery examples as one reviewable boundary.
Context: `docs/integration.md`; `examples/task-editor/`; `examples/astro/`; `packages/astro/README.md`; `tests/docs-examples.test.mjs`; `../architecture/specs/packages-release.md`.
Dependencies: SDK-1.4.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Every advertised example builds against packed artifacts; format limitations and unsupported native features are visible without reading internal docs.

Implementation:

- [ ] SDK-1.6-I1 Document actual package names, async init, literal paste, save/remote statuses, host auth/uploads, cleanup and current supported-format limitations; keep plain browser, React and Astro examples executable. Explain the shared framework-independent SDK, Astro static/SSR client initialization and navigation cleanup, and how future bindings reuse these contracts. Link the qualified integrations from getting started; publish support claims only for tested versions.

Validation:

- [ ] SDK-1.6-V1 node --test tests/docs-examples.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SDK-1.6` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SDK-1.6`.
Blocked behavior: Leave `SDK-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task SDK-1.7 — Implement the first-party Astro integration

- [ ] SDK-1.7 Implement the first-party Astro integration.

Purpose: Make the framework-independent editor directly consumable in Astro without requiring React.
Context: `packages/astro/`; `examples/astro/`; `tests/browser/astro.spec.ts`; `../architecture/specs/packages-release.md`.
Dependencies: SDK-1.2.
Session scope: One thin lifecycle integration and minimal consumer; target 15–45 minutes plus focused validation. Change only the named paths and directly required package/test/configuration glue.
Acceptance: A pinned Astro 7 consumer builds in static and SSR modes; server import/render does not initialize WASM or access browser globals. The .astro host mounts the common editor surface only in the browser, with one engine/document per instance. Editing, selection, read-only, save and load failures use the existing web contracts. Multiple instances, navigation away/back through Astro's ClientRouter, disposal and remount do not duplicate handles/listeners or lose a pending save silently. No React runtime is required.

Implementation:

- [ ] SDK-1.7-I1 Add optional @edit-ac/astro with a verified Astro peer range, a .astro host component and browser lifecycle bridge over @edit-ac/web. Keep editing semantics and document ownership in the shared SDK; expose explicit async loading, options, events and disposal. Add the minimal static/SSR consumer and ClientRouter cleanup using the pinned Astro lifecycle APIs; keep Astro dependencies out of core/web.

Validation:

- [ ] SDK-1.7-V1 npm run check:astro; npm run test:browser -- astro. Create check:astro to typecheck and build the minimal pinned static/SSR consumers, verify safe server import/render and absence of React dependencies, then execute the named browser lifecycle cases with deterministic content and prepared local save transports. Record exact commands/exits and nonzero executed/passed/failed/skipped counts. Packed-artifact qualification remains SDK-1.4.

Evidence: Progress entry `SDK-1.7` with changed paths, exact Astro/toolchain versions, commands/results, source and implementation revisions, fixture/artifact hashes and preserved failure logs. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact and next bounded action for `SDK-1.7`.
Blocked behavior: Leave `SDK-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task SDK-1.8 — Reduce the default browser editor below both gzip hard caps

- [ ] SDK-1.8 Reduce the default browser editor below both gzip hard caps.

Purpose: Ship smaller production artifacts for the unchanged default Task preset and make both size caps executable release gates. This task is part of SDK completion before mobile, editor-interaction and browser-release qualification; existing task IDs remain stable.
Context: `Cargo.toml`; `package.json`; `scripts/build-wasm.mjs`; `packages/core/src/index.ts`; `packages/core/package.json`; `packages/web/src/editor.ts`; `packages/web/src/surface.ts`; `packages/web/package.json`; `crates/editac-wasm/`; `crates/editac-markdown/`; planned `crates/editac-markdown-wasm/` and `packages/markdown/`; `packages/core/src/engine.ts`; `packages/web/src/clipboard/markdown.ts`; `packages/web/src/input/shortcuts.ts`; directly required module/preset/configuration, React/Astro example and build/packed-consumer glue; `../architecture/specs/formats.md`; directly required browser-profile/export boundaries in `crates/editac-core/`; planned `scripts/check-browser-size.mjs` and `tests/browser-size.test.mjs`; existing `tests/wasm-load.test.mjs`, `tests/module-bundles.test.mjs` and packed-consumer checks; `../architecture/specs/verification.md`; `../architecture/specs/packages-release.md`; `../evidence/bundle-size-20261013/findings.json` and `measurements.json`.
Dependencies: SDK-1.4.
Session scope: One default-browser artifact and budget boundary, with focused validation. Limit changes to build/export configuration, unused production roots and directly required local sharing of retained JS/WASM code. If reaching both caps requires a public ABI/semantic change or a larger rewrite, propose a controller split before that work; keep this parent unchecked until its full acceptance passes.
Acceptance: A freshly built, packed default Task consumer has total gzip JS + WASM + essential CSS/assets at most 524,288 bytes and editor JS at most 32,768 bytes, including generated glue, required runtime dependencies and required lazy code. Report preferred-size status against 256,000 total / 16,000 JS bytes. Preserve editing, anchors, formatting, undo/redo, checkpoint recovery, collaboration, international/safe URL handling, accessible/mobile baseline behavior and stored optional-content preservation. Neither disabled required capabilities nor host-owned persistence/sync substitution may create a size win. Markdown is available through an explicitly enabled extension retaining the qualified grammar, paste, shortcuts, import/export, diagnostics and preservation behavior. The default Task imports/requests no Markdown parser/codec assets and treats Markdown-looking text literally; enabled extension and combined costs are measured separately. Both cap assertions pass on the same default release artifacts; missing artifacts, failures, skips or partial measurements leave the task incomplete. Existing diagnostic eight-probe evidence is a starting point, not release qualification.

Implementation:

- [ ] SDK-1.8-I1 Freeze the current default Task consumer/import/asset inventory and add `npm run check:browser-size` backed by `scripts/check-browser-size.mjs` plus `tests/browser-size.test.mjs`. Use verification.md's gzip level-9/fixed-metadata counting contract, exact artifact hashes, both hard caps and preferred-size results; share this harness with REL-1.2/1.3, EXT-1.9 and FIT-1.6. Record fresh before/after measurements including essential CSS. Investigation reference: 974,832 total / 38,029 JS gzip bytes; tested compiler-only optimization reached 581,439 total / 38,331 JS bytes before essential CSS, still needing at least 69,439 total and 6,331 JS bytes removed.
- [ ] SDK-1.8-I2 Apply a browser-WASM build profile using the measured best settings (`opt-level="z"`, LTO, one codegen unit, symbol stripping and `panic="abort"`), preserving other target policies. Separate the exported foundation `Fixture`/creation-counter runtime from production while retaining an explicit fixture qualification build and documented package compatibility. Consider browser-v5 specialization only with explicit admission and preservation of historical shared/native support; the measured fixture/v5 cuts alone do not meet the caps. Do not assume raw-size wins are transfer wins: tested `wasm-opt -Oz`, `opt-level="s"` and `"3"` compressed worse; HTML-feature removal and reduced error detail had negligible benefit.
- [ ] SDK-1.8-I3 First extract the shared Rust Markdown parser and browser Markdown paste/shortcut/import/export adapters into an explicit optional first-party extension with a separately consumed package/entry and independently loadable parser artifact. The default core/web/React/Astro Task graphs must not retain or automatically request it. Preserve the same authoritative document owner, semantic node/mark schema, prepared-command and anchor/history boundaries, safe default HTML/internal/plain clipboard behavior, valid/unsafe/international link rules and portable Rust Markdown support. Provide typed opt-in and accurate unavailable-capability/source-preservation diagnostics. Update executable integration/recovery examples and package notices for default and Markdown-enabled consumers. Then close any remaining JS/total gaps through unused-root or duplication removal while preserving all remaining required default features; host-owned durability/sync substitution is not an equivalent Task result. Keep failed candidates and prior full-profile measurements. The user-approved optional-Markdown split is permitted; no other required feature exclusion, cap increase, schema migration or release is authorized.

Validation:

- [ ] SDK-1.8-V1 Run `npm run build:wasm`, `npm run build`, `node --test tests/browser-size.test.mjs` and `npm run check:browser-size` on packed production consumers. Prove each hard-cap assertion accepts its exact byte boundary and rejects one byte above; missing required assets, omitted glue/dependencies and hidden required lazy code must fail. Prove preferred-size misses are reported separately. Record full per-artifact manifests/hashes, gzip settings, exact commands/exits and nonzero executed/passed/failed/skipped counts; both real production totals must pass.
- [ ] SDK-1.8-V2 Run affected native Rust/protocol/package/WASM, module and packed-consumer checks plus unfiltered default browser baseline/input/recovery/sync regressions on the optimized default artifacts. Qualify Unicode editing/anchors/history, split/join, checkpoint restore and peer updates, safe/international links, rich-text formatting, default literal Markdown-looking paste/typing, internal fragments and supported safe HTML, optional image/table data preservation and baseline accessibility/mobile input. Prove default import/request graphs omit Markdown artifacts and no disabled codec fetches them. Separately run existing enabled Markdown grammar/import/export/paste/shortcut/round-trip/diagnostic and preservation regressions through the opt-in extension, including plain/React/Astro installed-tarball consumers with the same document owner; record extension and combined transfer manifests. Create missing named checks before invocation; maintain fixture coverage through the explicit qualification build and verify production fixture absence. Unfinished INT/MWB/device qualification stays in its owning track. Zero-match/missing/failing/skipped required checks cannot establish parity. Record immutable revisions, actual counts and teardown task-owned browsers/servers.

Evidence: Progress entry `SDK-1.8` with changed paths, exact commands/results, source/build/profile revisions, before/after packed manifests and byte totals, preferred-size status, semantic/browser receipts and preserved failed experiments. Durable implementation evidence belongs in `../architecture/evidence/browser-size-optimization/`; use `../architecture/progress/08-sdk-integration.md` for worker state, not this source.
Handoff: Record the last completed substep, current artifact hashes, both measured totals and remaining byte gaps, exact failing gate or missing fact, and the next bounded reduction for `SDK-1.8`.
Blocked behavior: Leave `SDK-1.8` unchecked while either cap or required parity gate fails; record BLOCKED/PROBLEM/NEEDS_INFO with owner, unblock condition and retry trigger. Propose a controller split if the reduction cannot fit this boundary; do not lower feature parity, waive caps, start paid inference or publish artifacts.
