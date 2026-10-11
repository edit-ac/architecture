# Ship explicit Markdown and clipboard semantics

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Deliver only the outcomes below. Read `../architecture/specs/formats.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Upstream entry gates: `02-engine.md` complete at current source revision with passing artifact evidence, `04-browser-input.md` complete at current source revision with passing artifact evidence.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus validation; if a boundary is too large, stop with a precise proposed split for the controller. Pick a task only when every named dependency is implemented and validated. Other ready tasks are permitted independent work; a roadmap entry gate remains mandatory for its dependents. Do not launch this roadmap while its upstream gate is unavailable.

Create named checks before invoking them. Record nonzero executed/passed/failed/skipped counts; missing tests and zero-match Rust filters fail acceptance. Run the narrow check, then relevant integration checks. Use prepared fixtures and transports only. No model API tests, live dogfood, background runner startup or publication outside an explicit release task.

## Epic FMT-1 — Ship explicit Markdown and clipboard semantics

### Task FMT-1.1 — Verify semantic and clipboard entry gates

- [ ] FMT-1.1 Verify semantic and clipboard entry gates.

Purpose: Deliver verify semantic and clipboard entry gates as one reviewable boundary.
Context: `crates/editac-core/`; `packages/web/src/clipboard/`; `../architecture/specs/formats.md`; `../architecture/specs/formats.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Markdown crate depends on portable model contracts only; existing clipboard and history regressions pass.

Implementation:

- [ ] FMT-1.1-I1 Confirm core rich types, one-batch commands, fragment paste and undo evidence. Create editac-markdown crate boundary without browser dependencies.

Validation:

- [ ] FMT-1.1-V1 cargo test -p editac-core --test history --locked; npm run test:browser -- clipboard. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FMT-1.1` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.1`.
Blocked behavior: Leave `FMT-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.2 — Qualify parser options against required dialect

- [ ] FMT-1.2 Qualify parser options against required dialect.

Purpose: Deliver qualify parser options against required dialect as one reviewable boundary.
Context: `crates/editac-markdown/tests/parser_profile.rs`; `../architecture/evidence/parser-profile.md`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Every required feature has a fixture result and gap owner; the named profile remains authoritative. A parser flag alone cannot pass the gate.

Implementation:

- [ ] FMT-1.2-I1 Before production mapping, run raw parser events against CommonMark0.31.2 and each required extension: task lists, strike, tables and extended autolinks. Record exact flags, gaps and an implementation decision.

Validation:

- [ ] FMT-1.2-V1 cargo test -p editac-markdown --test parser_profile --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FMT-1.2` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.2`.
Blocked behavior: Leave `FMT-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.3 — Map CommonMark parse events to prepared content

- [ ] FMT-1.3 Map CommonMark parse events to prepared content.

Purpose: Deliver map CommonMark parse events to prepared content as one reviewable boundary.
Context: `crates/editac-markdown/src/import.rs`; `crates/editac-markdown/tests/commonmark.rs`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Supported constructs produce expected semantics; unsupported constructs preserve bounded source plus diagnostics; no live document mutates during parse.

Implementation:

- [ ] FMT-1.3-I1 Use the pinned parser for paragraphs/headings/lists/quotes/fences/links/code and marks. Import selected official CommonMark0.31.2 fixtures including references and nested fences as a document.

Validation:

- [ ] FMT-1.3-V1 cargo test -p editac-markdown --test commonmark --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FMT-1.3` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.3`.
Blocked behavior: Leave `FMT-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.4 — Implement the named GFM subset

- [ ] FMT-1.4 Implement the named GFM subset.

Purpose: Deliver implement the named GFM subset as one reviewable boundary.
Context: `crates/editac-markdown/src/profile.rs`; `crates/editac-markdown/tests/gfm.rs`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Each advertised feature passes a pinned fixture list and negative cases; unsupported GFM is reported rather than lost.

Implementation:

- [ ] FMT-1.4-I1 Explicitly configure task-list, strike and table options and validate literal autolinks separately; fill every required gap; excluding a required extension needs a reviewed scope-changing ADR. Do not equate ENABLE_GFM with full GFM.

Validation:

- [ ] FMT-1.4-V1 cargo test -p editac-markdown --test gfm --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FMT-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.4`.
Blocked behavior: Leave `FMT-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.5 — Serialize semantic Markdown deterministically

- [ ] FMT-1.5 Serialize semantic Markdown deterministically.

Purpose: Deliver serialize semantic Markdown deterministically as one reviewable boundary.
Context: `crates/editac-markdown/src/export.rs`; `crates/editac-markdown/tests/roundtrip.rs`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.4.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Import-export-import preserves supported semantic content and code whitespace; underline/unknown atoms use documented diagnostics/fallback.

Implementation:

- [ ] FMT-1.5-I1 Implement escaping, code delimiters/whitespace, list nesting, link destinations and unsupported mark policy. Define normalized output, not original source spelling.

Validation:

- [ ] FMT-1.5-V1 cargo test -p editac-markdown --test roundtrip --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FMT-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.5`.
Blocked behavior: Leave `FMT-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.6 — Preserve optional image and table content

- [ ] FMT-1.6 Preserve optional image and table content.

Purpose: Deliver preserve optional image and table content as one reviewable boundary.
Context: `crates/editac-core/src/modules/content.rs`; `crates/editac-markdown/tests/optional_content.rs`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.4.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Rows/cells/alt text survive round-trip; disabled modules retain source and warn; resource limits reject oversized shapes before mutation.

Implementation:

- [ ] FMT-1.6-I1 Add bounded image metadata and rectangular table schemas with simple cells. Preserve unsupported or disabled renderer content as explicit opaque/source fallback; no merged cells or upload service.

Validation:

- [ ] FMT-1.6-V1 cargo test -p editac-markdown --test optional_content --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FMT-1.6` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.6`.
Blocked behavior: Leave `FMT-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.7 — Bind one-transaction Markdown paste

- [ ] FMT-1.7 Bind one-transaction Markdown paste.

Purpose: Deliver bind one-transaction Markdown paste as one reviewable boundary.
Context: `crates/editac-wasm/`; `packages/web/src/clipboard/markdown.ts`; `tests/browser/markdown-paste.spec.ts`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.5, FMT-1.6.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: The first document frame after normal paste is formatted, one undo removes the paste and redo restores it; reference links/nested fences remain correct.

Implementation:

- [ ] FMT-1.7-I1 Expose portable parser/serializer through the WASM bridge and insert a prepared batch once. Apply explicit clipboard precedence and preset policy for plain text; code stays literal.

Validation:

- [ ] FMT-1.7-V1 npm run build:wasm; npm run test:browser -- markdown-paste. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FMT-1.7` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.7`.
Blocked behavior: Leave `FMT-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.8 — Add sanitized rich HTML import

- [ ] FMT-1.8 Add sanitized rich HTML import.

Purpose: Deliver add sanitized rich HTML import as one reviewable boundary.
Context: `packages/web/src/clipboard/html.ts`; `tests/browser/html-paste.spec.ts`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.7.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Script/event/javascript URL/CSS/data URL attack fixtures cannot execute or trigger loads; normal links/lists/marks import with documented loss.

Implementation:

- [ ] FMT-1.8-I1 Use inert parsing and explicit element/attribute/URL allowlists; strip executable content and preserve text/fallback diagnostics. Scope custom fragment MIME and arbitrary HTML independently.

Validation:

- [ ] FMT-1.8-V1 npm run test:browser -- html-paste. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FMT-1.8` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.8`.
Blocked behavior: Leave `FMT-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.9 — Implement cancellable large paste

- [ ] FMT-1.9 Implement cancellable large paste.

Purpose: Deliver implement cancellable large paste as one reviewable boundary.
Context: `packages/web/src/clipboard/pending.ts`; `tests/browser/large-paste.spec.ts`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.8.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Cancel/target-delete/remote-move/destroy races neither lose source nor silently redirect insertion; duplicate completion is ignored.

Implementation:

- [ ] FMT-1.9-I1 Capture source and relative target, prepare asynchronously if measured useful, show pending/cancel state, revalidate anchor before one commit. Count transfer and main-thread apply costs.

Validation:

- [ ] FMT-1.9-V1 npm run test:browser -- large-paste. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FMT-1.9` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.9`.
Blocked behavior: Leave `FMT-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.10 — Implement local Markdown typing shortcuts

- [ ] FMT-1.10 Implement local Markdown typing shortcuts.

Purpose: Deliver implement local Markdown typing shortcuts as one reviewable boundary.
Context: `packages/web/src/input/shortcuts.ts`; `tests/browser/shortcuts.spec.ts`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.9.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Shortcuts preserve expected undo grouping and escape/literal behavior; unrelated blocks and remote updates trigger no global scan.

Implementation:

- [ ] FMT-1.10-I1 Recognize bounded current-context patterns for headings, lists, quote, fence and inline marks. Suspend during composition/code and never parse remote updates.

Validation:

- [ ] FMT-1.10-V1 npm run test:browser -- shortcuts. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FMT-1.10` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.10`.
Blocked behavior: Leave `FMT-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.11 — Qualify Markdown interchange and paste costs

- [ ] FMT-1.11 Qualify Markdown interchange and paste costs.

Purpose: Deliver qualify Markdown interchange and paste costs as one reviewable boundary.
Context: `benchmarks/paste/`; `tests/browser/markdown-collaboration.spec.ts`; `../architecture/evidence/markdown.md`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.10.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Conformance, semantic round-trips and concurrent paste pass; measured budgets include first formatted frame and failures remain visible.

Implementation:

- [ ] FMT-1.11-I1 Replay 10/100KiB fixed pastes and undo/redo with a prepared second replica. Publish supported dialect table and diagnostics with raw timings.

Validation:

- [ ] FMT-1.11-V1 cargo test -p editac-markdown --locked; npm run test:browser -- markdown-collaboration. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FMT-1.11` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.11`.
Blocked behavior: Leave `FMT-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.
