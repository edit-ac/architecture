# Qualify the browser release

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Deliver only the outcomes below. Read `../architecture/specs/verification.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Upstream entry gates: `08-sdk-integration.md` complete at current source revision with passing artifact evidence.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus validation; if a boundary is too large, stop with a precise proposed split for the controller. Pick a task only when every named dependency is implemented and validated. Other ready tasks are permitted independent work; a roadmap entry gate remains mandatory for its dependents. Do not launch this roadmap while its upstream gate is unavailable.

Create named checks before invoking them. Record nonzero executed/passed/failed/skipped counts; missing tests and zero-match Rust filters fail acceptance. Run the narrow check, then relevant integration checks. Use prepared fixtures and transports only. No model API tests, live dogfood, background runner startup or publication outside an explicit release task.

## Epic REL-1 — Qualify the browser release

### Task REL-1.1 — Verify browser integration entry gate

- [ ] REL-1.1 Verify browser integration entry gate.

Purpose: Deliver verify browser integration entry gate as one reviewable boundary.
Context: `../architecture/evidence/`; `tests/packed-consumers.test.mjs`; `../architecture/specs/verification.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Each browser prerequisite is complete at reviewed revisions; no native parity is included in browser support claims.

Implementation:

- [ ] REL-1.1-I1 Check current browser, storage, collaboration, Markdown, module and SDK evidence and record artifact hashes. Native preparation and CLI do not block this browser gate.

Validation:

- [ ] REL-1.1-V1 node --test tests/packed-consumers.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `REL-1.1` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `REL-1.1`.
Blocked behavior: Leave `REL-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task REL-1.2 — Build feature-equivalent performance baselines

- [ ] REL-1.2 Build feature-equivalent performance baselines.

Purpose: Deliver build feature-equivalent performance baselines as one reviewable boundary.
Context: `benchmarks/baselines/`; `benchmarks/manifest.json`; `../architecture/specs/verification.md`.
Dependencies: REL-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Benchmark manifests declare versions, features/device/network settings and differences; no disabled durability or hidden WASM bytes create an artificial win.

Implementation:

- [ ] REL-1.2-I1 Pin optimized Tiptap, Lexical and plain-contenteditable baselines with comparable schema, collaboration, persistence and UI; record unavoidable capability differences.

Validation:

- [ ] REL-1.2-V1 Run the deterministic baseline sanity command added with the benchmark harness. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `REL-1.2` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `REL-1.2`.
Blocked behavior: Leave `REL-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task REL-1.3 — Measure loading, editability and paste

- [ ] REL-1.3 Measure loading, editability and paste.

Purpose: Deliver measure loading, editability and paste as one reviewable boundary.
Context: `benchmarks/browser/`; `../architecture/evidence/performance.md`; `../architecture/specs/verification.md`.
Dependencies: REL-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Task/Long targets are measured on declared desktop/phone profiles; Large/Aged are diagnostic until separately qualified; failures remain explicit.

Implementation:

- [ ] REL-1.3-I1 Measure fixed corpus cold/warm samples including transfer/decode/compile/restore/DOM/input costs, first visible and first accepted edit, p50/p95/p99 and raw samples.

Validation:

- [ ] REL-1.3-V1 Run the pinned benchmark command and record raw sample counts, percentiles and artifact hashes. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `REL-1.3` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `REL-1.3`.
Blocked behavior: Leave `REL-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task REL-1.4 — Measure leaks and backpressure

- [ ] REL-1.4 Measure leaks and backpressure.

Purpose: Deliver measure leaks and backpressure as one reviewable boundary.
Context: `tests/browser/stress.spec.ts`; `../architecture/evidence/stress.md`; `../architecture/specs/verification.md`.
Dependencies: REL-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: No monotonic retained-reference growth; bounded queue/recovery policy works; exact iterations and memory samples are retained.

Implementation:

- [ ] REL-1.4-I1 Exercise repeated mount/edit/destroy, ten editors, large paste and remote bursts with bounded queues; separate WASM allocator plateau from retained resource growth.

Validation:

- [ ] REL-1.4-V1 npm run test:browser -- stress. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `REL-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `REL-1.4`.
Blocked behavior: Leave `REL-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task REL-1.5 — Harden resource and trust boundaries

- [ ] REL-1.5 Harden resource and trust boundaries.

Purpose: Deliver harden resource and trust boundaries as one reviewable boundary.
Context: `tests/browser/security.spec.ts`; `crates/editac-core/tests/resource_limits.rs`; `../architecture/specs/verification.md`.
Dependencies: REL-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: All public ingest paths enforce the same declared limits; untrusted content cannot execute code or silently destroy preserved unknown data.

Implementation:

- [ ] REL-1.5-I1 Exercise hostile HTML/fragments/URLs, malformed updates, oversized attributes/nesting/queues, unsupported schemas and readonly mutation attempts with deterministic fixtures.

Validation:

- [ ] REL-1.5-V1 cargo test -p editac-core --test resource_limits --locked; npm run test:browser -- security. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `REL-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `REL-1.5`.
Blocked behavior: Leave `REL-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task REL-1.6 — Complete real-browser input qualification

- [ ] REL-1.6 Complete real-browser input qualification.

Purpose: Deliver complete real-browser input qualification as one reviewable boundary.
Context: `tests/manual/browser-input.md`; `../architecture/evidence/input-matrix.md`; `../architecture/specs/verification.md`.
Dependencies: REL-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Every publicly claimed combination has actual evidence; missing devices/cases remain unchecked and require narrower support claims or later qualification.

Implementation:

- [ ] REL-1.6-I1 Execute actual OS IME/mobile/keyboard/screen-reader cases for the declared support matrix; preserve failure reproduction and artifact references.

Validation:

- [ ] REL-1.6-V1 Execute tests/manual/browser-input.md with recorded OS/browser/device versions and pass/fail/skip counts. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `REL-1.6` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `REL-1.6`.
Blocked behavior: Leave `REL-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task REL-1.7 — Rehearse crash and offline release scenarios

- [ ] REL-1.7 Rehearse crash and offline release scenarios.

Purpose: Deliver rehearse crash and offline release scenarios as one reviewable boundary.
Context: `tests/browser/release-recovery.spec.ts`; `../architecture/evidence/recovery.md`; `../architecture/specs/verification.md`.
Dependencies: REL-1.4, REL-1.5.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Supported locally committed content recovers; saved indicators distinguish local/remote; all excluded durability cases are documented.

Implementation:

- [ ] REL-1.7-I1 Repeat acknowledged local crash, corrupt checkpoint fallback, quota failure, revoked sync and explicit migration epoch scenarios using release artifacts.

Validation:

- [ ] REL-1.7-V1 npm run test:browser -- release-recovery. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `REL-1.7` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `REL-1.7`.
Blocked behavior: Leave `REL-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task REL-1.8 — Prepare signed-off release artifacts

- [ ] REL-1.8 Prepare signed-off release artifacts.

Purpose: Deliver prepare signed-off release artifacts as one reviewable boundary.
Context: `scripts/release-check.mjs`; `../architecture/evidence/release-candidate.md`; `../architecture/specs/verification.md`.
Dependencies: REL-1.6, REL-1.7.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Packed consumers and CI pass on the release revision; archive all material failed evidence and accepted limitations; no empty package is eligible.

Implementation:

- [ ] REL-1.8-I1 Choose honest tested size/platform envelope; assemble tarballs, API docs, license notices, dependency audit, checksums and changelog. Replace scaffold private flags only after genuine API checks pass.

Validation:

- [ ] REL-1.8-V1 node scripts/release-check.mjs; node --test tests/packed-consumers.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `REL-1.8` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `REL-1.8`.
Blocked behavior: Leave `REL-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task REL-1.9 — Publish the first browser prerelease

- [ ] REL-1.9 Publish the first browser prerelease.

Purpose: Deliver publish the first browser prerelease as one reviewable boundary.
Context: `packages/*/package.json`; `.github/workflows/publish.yml`; `../architecture/specs/verification.md`.
Dependencies: REL-1.8.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Registry install from clean fixtures succeeds; public API/asset hashes match reviewed tarballs; no production endpoint or paid inference is required.

Implementation:

- [ ] REL-1.9-I1 Use the release procedure to publish vetted public @edit-ac packages under next; bootstrap npm authentication if required, then configure exact-repo/workflow trusted publishers. Record immutable versions and provenance.

Validation:

- [ ] REL-1.9-V1 npm view @edit-ac/core@VERSION dist; install exact published versions in isolated fixtures and rerun consumer checks. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `REL-1.9` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `REL-1.9`.
Blocked behavior: Leave `REL-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.
