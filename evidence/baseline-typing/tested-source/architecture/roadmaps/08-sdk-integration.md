# Integrate and package the browser SDK

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Deliver only the outcomes below. Read `../architecture/specs/packages-release.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Upstream entry gates: `04-browser-input.md` complete at current source revision with passing artifact evidence, `05-markdown-content.md` complete at current source revision with passing artifact evidence, `06-synchronization.md` complete at current source revision with passing artifact evidence, `07-extension-modules.md` complete at current source revision with passing artifact evidence.

Retain the [baseline typing/rendering gate](../specs/web.md#baseline-typing-and-rendering-guarantees): `npm run check:browser-baseline` passes unfiltered at the reviewed source/artifact revisions before SDK acceptance. Public examples use the common surface mount. Tracks 38/42 expand regression coverage without deferring basic editing or presentation fixes.

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
Dependencies: SDK-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Consumers resolve only tarball contents, no source/workspace paths; one core runtime owner; WASM and declarations load under documented hosting.

Implementation:

- [ ] SDK-1.4-I1 Pack local built SDKs and install into isolated plain browser and React/SSR fixtures; verify declarations, exports, asset URL/CSP loading and Apache license inclusion.

Validation:

- [ ] SDK-1.4-V1 npm run build:wasm; npm run build; node --test tests/packed-consumers.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SDK-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SDK-1.4`.
Blocked behavior: Leave `SDK-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task SDK-1.5 — Implement scoped Tiptap JSON migration

- [ ] SDK-1.5 Implement scoped Tiptap JSON migration.

Purpose: Deliver implement scoped Tiptap JSON migration as one reviewable boundary.
Context: `crates/editac-core/src/import/tiptap.rs`; `crates/editac-core/tests/migration.rs`; `../architecture/specs/packages-release.md`.
Dependencies: SDK-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Supported fixture content survives; unknown nodes preserve bounded source with diagnostics; old Yjs sessions cannot merge silently into the new schema.

Implementation:

- [ ] SDK-1.5-I1 Map only supported node/mark JSON to prepared semantic content with a versioned converter and diagnostics. Start a new explicit epoch/session for migrated collaborative data.

Validation:

- [ ] SDK-1.5-V1 cargo test -p editac-core --test migration --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SDK-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SDK-1.5`.
Blocked behavior: Leave `SDK-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task SDK-1.6 — Write integration and recovery examples

- [ ] SDK-1.6 Write integration and recovery examples.

Purpose: Deliver write integration and recovery examples as one reviewable boundary.
Context: `docs/integration.md`; `docs/migration.md`; `examples/task-editor/`; `tests/docs-examples.test.mjs`; `../architecture/specs/packages-release.md`.
Dependencies: SDK-1.4, SDK-1.5.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Every advertised example builds against packed artifacts; format limitations and unsupported native features are visible without reading internal docs.

Implementation:

- [ ] SDK-1.6-I1 Document actual package names, async init, literal paste, save/remote statuses, host auth/uploads, cleanup and migration limitations; keep examples executable.

Validation:

- [ ] SDK-1.6-V1 node --test tests/docs-examples.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `SDK-1.6` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `SDK-1.6`.
Blocked behavior: Leave `SDK-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.
