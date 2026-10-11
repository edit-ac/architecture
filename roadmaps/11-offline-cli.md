# Build explicit offline document diagnostics

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `cli` (sibling of `architecture`). Deliver only the outcomes below. Read `../architecture/specs/packages-release.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `cli` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Upstream entry gates: `02-engine.md` complete at current source revision with passing artifact evidence, `05-markdown-content.md` complete at current source revision with passing artifact evidence.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus validation; if a boundary is too large, stop with a precise proposed split for the controller. Pick a task only when every named dependency is implemented and validated. Other ready tasks are permitted independent work; a roadmap entry gate remains mandatory for its dependents. Do not launch this roadmap while its upstream gate is unavailable.

Create named checks before invoking them. Record nonzero executed/passed/failed/skipped counts; missing tests and zero-match Rust filters fail acceptance. Run the narrow check, then relevant integration checks. Use prepared fixtures and transports only. No model API tests, live dogfood, background runner startup or publication outside an explicit release task.

## Epic CLI-1 — Build explicit offline document diagnostics

### Task CLI-1.1 — Pin the engine integration boundary

- [ ] CLI-1.1 Pin the engine integration boundary.

Purpose: Deliver pin the engine integration boundary as one reviewable boundary.
Context: `Cargo.toml`; `Cargo.lock`; `tests/help.rs`; `../architecture/specs/packages-release.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: A clean checkout builds with its lockfile and no sibling repository; help does not advertise unavailable commands.

Implementation:

- [ ] CLI-1.1-I1 Consume a reviewed immutable core revision or published crate, never an uncommitted sibling path in distributed CLI builds. Preserve current help/version behavior.

Validation:

- [ ] CLI-1.1-V1 cargo test --locked; cargo run --locked -- --help. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `CLI-1.1` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.1`.
Blocked behavior: Leave `CLI-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task CLI-1.2 — Validate versioned semantic interchange

- [ ] CLI-1.2 Validate versioned semantic interchange.

Purpose: Deliver validate versioned semantic interchange as one reviewable boundary.
Context: `src/validate.rs`; `tests/validate.rs`; `../architecture/specs/packages-release.md`.
Dependencies: CLI-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Valid fixtures pass; unknown schema/malformed/oversized inputs return stable nonzero exits without modifying source.

Implementation:

- [ ] CLI-1.2-I1 Add an explicit validate command for schema-versioned JSON with bounded input and typed diagnostics. Treat binary update format as a separately identified input, never guess arbitrary bytes.

Validation:

- [ ] CLI-1.2-V1 cargo test --test validate --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `CLI-1.2` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.2`.
Blocked behavior: Leave `CLI-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task CLI-1.3 — Convert supported Markdown and JSON

- [ ] CLI-1.3 Convert supported Markdown and JSON.

Purpose: Deliver convert supported Markdown and JSON as one reviewable boundary.
Context: `src/convert.rs`; `tests/convert.rs`; `../architecture/specs/packages-release.md`.
Dependencies: CLI-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Supported content round-trips and diagnostics are emitted for loss/fallback; failed conversion leaves original input/output intact.

Implementation:

- [ ] CLI-1.3-I1 Use shared Rust Markdown implementation and an explicit from/to format. Write new output atomically; refuse overwrite unless an explicit option permits it.

Validation:

- [ ] CLI-1.3-V1 cargo test --test convert --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `CLI-1.3` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.3`.
Blocked behavior: Leave `CLI-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task CLI-1.4 — Expose deterministic fixture inspection

- [ ] CLI-1.4 Expose deterministic fixture inspection.

Purpose: Deliver expose deterministic fixture inspection as one reviewable boundary.
Context: `src/inspect.rs`; `tests/inspect.rs`; `../architecture/specs/packages-release.md`.
Dependencies: CLI-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Prepared fixtures produce stable output; corrupt input errors are clear; no network, credentials or background service is used.

Implementation:

- [ ] CLI-1.4-I1 Print schema/document/epoch, semantic counts and safe update metadata without claiming server durability or dumping private contents by default.

Validation:

- [ ] CLI-1.4-V1 cargo test --test inspect --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `CLI-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.4`.
Blocked behavior: Leave `CLI-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task CLI-1.5 — Document and package the offline utility

- [ ] CLI-1.5 Document and package the offline utility.

Purpose: Deliver document and package the offline utility as one reviewable boundary.
Context: `README.md`; `.github/workflows/ci.yml`; `tests/commands.rs`; `../architecture/specs/packages-release.md`.
Dependencies: CLI-1.3, CLI-1.4.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Help/examples and executable commands agree; clean checkout tests pass; publication remains a separately recorded release action.

Implementation:

- [ ] CLI-1.5-I1 Add tested examples, Apache notices and release artifact build instructions; keep CLI distribution independent of npm/browser release and native parity.

Validation:

- [ ] CLI-1.5-V1 cargo test --locked; cargo run --locked -- --help. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `CLI-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.5`.
Blocked behavior: Leave `CLI-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.
