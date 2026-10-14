# Ship explicit Markdown and clipboard semantics

Status: IN_PROGRESS

Qualification amendment (user decision, 2026-10-14): Physical devices, named target-platform simulators/emulators and desktop OS VMs/test hosts are accepted for platform and release qualification under the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms). Missing physical hardware does not block completion. Execute required behavior against the implemented target-platform runtime; document and test virtual equivalents for unavailable hardware-only input/accessibility cases. Record physical versus virtual provenance and measure performance in the tested environment. This supersedes earlier physical-only or manual-only clauses below; it does not complete unchecked tasks or waive implementation, correctness, security or artifact gates.

Progress (2026-10-13): 14 of 15 parent tasks complete. Software implementation and deterministic qualification are complete; FMT-1.15-V1 is blocked on actual-device observations. Final native/package/WASM/browser/architecture results and cleanup are recorded in `../evidence/markdown/session-20261013/qualification.json`. Checkmarks in this file are maintained under the user's explicit progress-tracking instruction.

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Deliver only the outcomes below. Read `../architecture/specs/formats.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Upstream entry gates: `02-engine.md` complete at current source revision with passing artifact evidence, `04-browser-input.md` complete at current source revision with passing artifact evidence.

Packaging amendment (2026-10-13): The user made Markdown an explicit optional extension. This track continues to qualify the full enabled grammar, interchange, paste and shortcut behavior. References to Task Markdown defaults mean the extension-enabled Task configuration; the bare Task preset pastes Markdown-looking text literally and does not load the parser. SDK-1.8 owns extraction and separate default/enabled artifact qualification. Preserve historical results, the roadmap-05 completion assumption and the outstanding FMT-1.15 actual-device gate; this amendment does not claim new qualification.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus validation; if a boundary is too large, stop with a precise proposed split for the controller. Pick a task only when every named dependency is implemented and validated. Other ready tasks are permitted independent work; a roadmap entry gate remains mandatory for its dependents. Do not launch this roadmap while its upstream gate is unavailable.

Create named checks before invoking them. Record nonzero executed/passed/failed/skipped counts; missing tests and zero-match Rust filters fail acceptance. Run the narrow check, then relevant integration checks. Use prepared fixtures and transports only. No model API tests, live dogfood, background runner startup or publication outside an explicit release task.

## Epic FMT-1 — Ship explicit Markdown and clipboard semantics

### Task FMT-1.1 — Verify semantic and clipboard entry gates

- [x] FMT-1.1 Verify semantic and clipboard entry gates.

Purpose: Deliver verify semantic and clipboard entry gates as one reviewable boundary.
Context: `crates/editac-core/`; `packages/web/src/clipboard/`; `../architecture/specs/formats.md`; `../architecture/specs/formats.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Markdown crate depends on portable model contracts only; existing clipboard and history regressions pass.

Implementation:

- [x] FMT-1.1-I1 Confirm core rich types, one-batch commands, fragment paste and undo evidence. Create editac-markdown crate boundary without browser dependencies.

Validation:

- [x] FMT-1.1-V1 cargo test -p editac-core --test history --locked; npm run test:browser -- clipboard. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Progress (2026-10-12): Created portable `editac-markdown` workspace crate depending only on `editac-core`. Existing prepared fragment boundary admits one staged update, retained anchors, marks/list metadata and selective history. `PATH=/Users/bpstr/.nvm/versions/node/v24.19.0/bin:$PATH EDITAC_HISTORY_EXCHANGE=/Users/bpstr/Github/edit-ac/architecture/evidence/markdown/entry/history-pinned cargo test -p editac-core --test history --locked --offline`: exit 0, 28 executed/passed, 0 failed/skipped. `EDITAC_CLIPBOARD_OUTPUT=../architecture/evidence/markdown/entry/clipboard-retry npm run test:browser -- clipboard`: exit 0, 81 executed/passed (27 per Chromium/Firefox/WebKit), 0 failed/skipped. Receipts include source/package hashes and successful browser/server teardown. Logs and initial environment failures retained in `../evidence/markdown/entry/`. Roadmap checkmarks updated directly under the user's explicit tracking instruction.

Evidence: Progress entry `FMT-1.1` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.1`.
Blocked behavior: Leave `FMT-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.2 — Qualify parser options against required dialect

- [x] FMT-1.2 Qualify parser options against required dialect.

Purpose: Deliver qualify parser options against required dialect as one reviewable boundary.
Context: `crates/editac-markdown/tests/parser_profile.rs`; `../architecture/evidence/parser-profile.md`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Every required feature has a fixture result and gap owner; the named profile remains authoritative. A parser flag alone cannot pass the gate.

Implementation:

- [x] FMT-1.2-I1 Before production mapping, run raw parser events against CommonMark0.31.2 and each required extension: task lists, strike, tables and extended autolinks. Record exact flags, gaps and an implementation decision.

Validation:

- [x] FMT-1.2-V1 cargo test -p editac-markdown --test parser_profile --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Progress (2026-10-12): Pinned 0.13.4 profile and qualified portable extended-autolink adapter. All 652 official CommonMark examples and all 23 official required GFM extension examples pass grammar comparison with explicitly documented HTML serialization normalization. Six Rust tests passed, zero failed/skipped, command `cargo test -p editac-markdown --test parser_profile --locked --offline`. Candidate gaps, flags, negative cases, decision and preserved failures: `../evidence/parser-profile.md`, `../evidence/markdown/parser-profile-qualified.log`.

Evidence: Progress entry `FMT-1.2` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.2`.
Blocked behavior: Leave `FMT-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.3 — Map CommonMark parse events to prepared content

- [x] FMT-1.3 Map CommonMark parse events to prepared content.

Purpose: Deliver map CommonMark parse events to prepared content as one reviewable boundary.
Context: `crates/editac-markdown/src/import.rs`; `crates/editac-markdown/tests/commonmark.rs`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Supported constructs produce expected semantics; unsupported constructs preserve bounded source plus diagnostics; no live document mutates during parse.

Implementation:

- [x] FMT-1.3-I1 Use the pinned parser for paragraphs/headings/lists/quotes/fences/links/code and marks. Import selected official CommonMark0.31.2 fixtures including references and nested fences as a document.

Validation:

- [x] FMT-1.3-V1 cargo test -p editac-markdown --test commonmark --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Progress (2026-10-12): 7 named Rust tests executed/passed, 0 failed/skipped. Mapped whole-document events to bounded inert fragments, exact source/ranges and explicit diagnostics; selected authored semantics and all 652 official sources pass. Core URL admission is reused via the public normalize_link_url helper. Required command cargo test -p editac-markdown --test commonmark --locked --offline passed; changed-core formatting regression passed 41/41 with pinned Node and isolated exchange evidence. Logs: ../evidence/markdown/commonmark-retry.log and format-regression-pinned.log.

Evidence: Progress entry `FMT-1.3` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.3`.
Blocked behavior: Leave `FMT-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.4 — Implement the named GFM subset

- [x] FMT-1.4 Implement the named GFM subset.

Purpose: Deliver implement the named GFM subset as one reviewable boundary.
Context: `crates/editac-markdown/src/profile.rs`; `crates/editac-markdown/tests/gfm.rs`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Each advertised feature passes a pinned fixture list and negative cases; unsupported GFM is reported rather than lost.

Implementation:

- [x] FMT-1.4-I1 Explicitly configure task-list, strike and table options and validate literal autolinks separately; fill every required gap; excluding a required extension needs a reviewed scope-changing ADR. Do not equate ENABLE_GFM with full GFM.

Validation:

- [x] FMT-1.4-V1 cargo test -p editac-markdown --test gfm --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Progress (2026-10-12): 5 named Rust tests executed/passed, 0 failed/skipped. Qualified named GFM semantic mappings with nested checklist states, strike, autolink destinations/punctuation, code/escape negatives and all 23 extension sources. Optional table codecs remain explicitly disabled until FMT-1.6; nonadmitted URL schemes retain source plus diagnostics. Required command cargo test -p editac-markdown --test gfm --locked --offline passed. Log: ../evidence/markdown/gfm.log.

Evidence: Progress entry `FMT-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.4`.
Blocked behavior: Leave `FMT-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.5 — Serialize semantic Markdown deterministically

- [x] FMT-1.5 Serialize semantic Markdown deterministically.

Purpose: Deliver serialize semantic Markdown deterministically as one reviewable boundary.
Context: `crates/editac-markdown/src/export.rs`; `crates/editac-markdown/tests/roundtrip.rs`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.4.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Import-export-import preserves supported semantic content and code whitespace; underline/unknown atoms use documented diagnostics/fallback.

Implementation:

- [x] FMT-1.5-I1 Implement escaping, code delimiters/whitespace, list nesting, link destinations and unsupported mark policy. Define normalized output, not original source spelling.

Validation:

- [x] FMT-1.5-V1 cargo test -p editac-markdown --test roundtrip --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Progress (2026-10-12): Deterministic LF/trailing-newline serializer preserves tested escaping, code delimiters/whitespace, nested containers, checklist states, links and Unicode. Underline, unknown tuples, unrepresentable code and crossing mark boundaries retain typed recovery data with diagnostics. Shared-parser representability check prevents silent export loss. Command cargo test -p editac-markdown --test roundtrip --locked --offline: 7 executed/passed, 0 failed/skipped. Logs and earlier failures: ../evidence/markdown/roundtrip*.log.

Evidence: Progress entry `FMT-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.5`.
Blocked behavior: Leave `FMT-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.6 — Preserve optional image and table content

- [x] FMT-1.6 Preserve optional image and table content.

Purpose: Deliver preserve optional image and table content as one reviewable boundary.
Context: `crates/editac-core/src/modules/content.rs`; `crates/editac-markdown/tests/optional_content.rs`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.4.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Rows/cells/alt text survive round-trip; disabled modules retain source and warn; resource limits reject oversized shapes before mutation.
Descriptor contract: Use validated v1 `module:editac.image`/`module:editac.table`
opaque tuples under the existing v5 envelope; retain exact source and inert text,
stage descriptor presentation after text/marks/containers, and qualify one-update
engine history. No wire-profile migration or renderer/upload service is implied.

Controller split (2026-10-12): This boundary exposed a prerequisite in source
registration and fragment history, beyond descriptor mapping. Preserve the
parent's complete acceptance; execute these bounded children sequentially.

- [x] FMT-1.6-C1 Qualify fresh-source atomic fragments: preserve existing source
  identities and literal destination marks; append new v5 registrations after
  existing root placements so historical joins remain eligible; preserve edge
  atom prefix/suffix text/presentation and the resulting caret; qualify empty,
  cross-block, repeated undo/redo, core regressions and all three packed clipboard
  engines. Retain historical failures and exact source/package hashes.
- [x] FMT-1.6-C2 Qualify registered image/table descriptors after C1: bounded
  metadata, rectangular rich simple cells/alignment/alt text, disabled/unknown
  source recovery, unsafe/version/resource rejection without mutation, optional
  round-trips and one-update selective history. Run the named optional suite.

Implementation:

- [x] FMT-1.6-I1 Add bounded image metadata and rectangular table schemas with simple cells. Preserve unsupported or disabled renderer content as explicit opaque/source fallback; no merged cells or upload service.

Validation:

- [x] FMT-1.6-V1 cargo test -p editac-markdown --test optional_content --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Progress (2026-10-12): Qualified the C1 prerequisite and C2 descriptors. Fresh payload sources preserve selective undo/redo; v5 registrations append after existing root placements so replayed joins remain eligible. Image/table tuples retain exact source and inert fallback text with bounded typed metadata. Commands: `cargo test -p editac-markdown --locked --offline` (32 passed); pinned-Node `cargo test -p editac-core --test history --test format_commands --test editor_profile --test stable_editor_profile --test heading_end --locked --offline` (129 passed); `npm run build:wasm` (exit 0); `EDITAC_CLIPBOARD_OUTPUT=../architecture/evidence/markdown/fragment-clipboard npm run test:browser -- clipboard` (81 passed, 27 per Chromium/Firefox/WebKit). Zero final failures/skips; teardown receipts complete. Logs: portable-final.log, fragment-core-final.log, fragment-build-wasm.log, fragment-clipboard.log. WASM SHA-256 5924ef11a65fc1562bc9203183e360b62da45a74ef510297eb94dda1deab1c5c; packed receipts record source/package hashes. Earlier failures are retained.

Evidence: Progress entry `FMT-1.6` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.6`.
Blocked behavior: Leave `FMT-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.7 — Bind one-transaction Markdown paste

- [x] FMT-1.7 Bind one-transaction Markdown paste.

Purpose: Deliver bind one-transaction Markdown paste as one reviewable boundary.
Context: `crates/editac-wasm/`; `packages/web/src/clipboard/markdown.ts`; `tests/browser/markdown-paste.spec.ts`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.5, FMT-1.6.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: The first document frame after normal paste is formatted, one undo removes the paste and redo restores it; reference links/nested fences remain correct.

Implementation:

- [x] FMT-1.7-I1 Expose portable parser/serializer through the WASM bridge and insert a prepared batch once. Apply explicit clipboard precedence and preset policy for plain text; code stays literal.

Validation:

- [x] FMT-1.7-V1 npm run build:wasm; npm run test:browser -- markdown-paste. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Progress (2026-10-13): Portable parser/serializer exposed through WASM; registered content transfers are bounded; task/minimal/plain policy and named Markdown flavor routing commit one batch. `npm run build:wasm` and `npm run build`: exit 0. `cargo test -p editac-wasm --lib markdown_bridge_tests --locked --offline`: 3 passed. `EDITAC_MARKDOWN_PASTE_OUTPUT=../architecture/evidence/markdown/markdown-paste-qualified npm run test:browser -- markdown-paste`: 21 passed (7 each Chromium/Firefox/WebKit), zero failures/skips. Qualified first formatted frame, references/nested fences, precedence, source recovery, literal code and repeated undo/redo. Receipts include source/package hashes and complete teardown. WASM SHA-256 616ada10aaa7b1c18849b9a3c17ce633d25aab30abbb91ef3744b28370a97de0. Initial build/lock/type and assertion failures preserved in bridge-* and markdown-paste logs.

Evidence: Progress entry `FMT-1.7` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.7`.
Blocked behavior: Leave `FMT-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.14 — Expose bounded Markdown extensions

- [x] FMT-1.14 Expose bounded Markdown extensions (user request, 2026-10-13).

Purpose: Let hosts extend supported syntax and serialization without replacing the qualified portable parser or bypassing atomic admission.
Context: `crates/editac-markdown/src/extensions.rs`; `crates/editac-markdown/tests/extensions.rs`; `tests/browser/markdown-extensions.spec.ts`; `../architecture/specs/formats.md`.
Session scope: One portable extension/admission boundary with native and packed browser checks.
Dependencies: FMT-1.7. Execute before FMT-1.8.
Acceptance: Explicit built-in image/table/GitHub-callout options; ordered custom import/export hooks with stable names; extensions receive exact source and portable prepared semantics; bounded outputs, diagnostics and failure recovery; no live mutation from preparation; disabled content remains recoverable. One paste remains one semantic/history/storage batch. Native and packed three-engine fixtures qualify custom syntax, callouts, disabled codecs, rejection and round-trip.

Implementation:

- [x] FMT-1.14-I1 Define portable extension hooks and host options; implement callouts and custom syntax/serialization examples.
Validation:

- [x] FMT-1.14-V1 Run portable extension tests and `npm run test:browser -- markdown-extensions`, with nonzero counts, preserved failures and source/package hashes.

Progress (2026-10-13, in progress): Added native Extension trait and host MarkdownOptions with ordered stable-name prepare/serialize hooks, data-only WASM transport and native semantic round-trip comparison. Optional callout v1 descriptors preserve kind/body/exact source with inert fallback. Five portable extension tests pass (zero failures/skips); browser qualification follows the package build.

Progress (2026-10-13, completed): Fixed the interrupted browser fixture syntax and qualified existing extensions. `cargo test -p editac-markdown --test extensions --locked --offline`: 5 executed/passed, 0 failed/skipped. Pinned Node `EDITAC_MARKDOWN_EXTENSIONS_OUTPUT=../architecture/evidence/markdown/session-20261013/extensions-qualified npm run test:browser -- markdown-extensions`: 18 executed/passed (6 per engine), 0 failed/skipped. Build exit 0. Receipts retain source/package hashes and complete browser/server/consumer teardown. Native log and both startup failures retained under `../evidence/markdown/session-20261013/`.

Evidence: Native extension logs and packed browser receipts under `../architecture/evidence/markdown/session-20261013/`.
Handoff: Extension boundary qualified; continue FMT-1.8.
Blocked behavior: Leave failed or skipped mandatory extension checks unchecked and preserve their logs.

### Task FMT-1.8 — Add sanitized rich HTML import

- [x] FMT-1.8 Add sanitized rich HTML import.

Purpose: Deliver add sanitized rich HTML import as one reviewable boundary.
Context: `packages/web/src/clipboard/html.ts`; `tests/browser/html-paste.spec.ts`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.7.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Script/event/javascript URL/CSS/data URL attack fixtures cannot execute or trigger loads; normal links/lists/marks import with documented loss.

Implementation:

- [x] FMT-1.8-I1 Use inert parsing and explicit element/attribute/URL allowlists; strip executable content and preserve text/fallback diagnostics. Scope custom fragment MIME and arbitrary HTML independently.

Validation:

- [x] FMT-1.8-V1 npm run test:browser -- html-paste. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FMT-1.8` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.8`.
Blocked behavior: Leave `FMT-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

Progress (2026-10-13): Bounded inert template admission now reports dropped elements/attributes/CSS/URLs with exact HTML source recovery, rejects byte/nesting/attribute excess and imports the safe palette in one batch. `npm run build`: exit 0. Pinned Node `EDITAC_HTML_PASTE_OUTPUT=../architecture/evidence/markdown/session-20261013/html-qualified npm run test:browser -- html-paste`: 18 executed/passed (6 per engine), 0 failed/skipped. Receipts include hashes, no attack loads/execution, unchanged rejected state and complete teardown. Initial fixture expectation failure preserved in html.log.

### Task FMT-1.9 — Implement cancellable large paste

- [x] FMT-1.9 Implement cancellable large paste.

Purpose: Deliver implement cancellable large paste as one reviewable boundary.
Context: `packages/web/src/clipboard/pending.ts`; `tests/browser/large-paste.spec.ts`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.8.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Cancel/target-delete/remote-move/destroy races neither lose source nor silently redirect insertion; duplicate completion is ignored.

Implementation:

- [x] FMT-1.9-I1 Capture source and relative target, prepare asynchronously if measured useful, show pending/cancel state, revalidate anchor before one commit. Count transfer and main-thread apply costs.

Validation:

- [x] FMT-1.9-V1 npm run test:browser -- large-paste. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Additional qualification (2026-10-13): Preparation-hook cancellation is rechecked before entering atomic application; cancellation during publication cannot misreport a committed paste. Final `npm run test:browser -- large-paste` executes 24 tests across Chromium/Firefox/WebKit, all passed with zero failed/skipped. `session-20261013/pending-final.log` and `pending-final/` retain receipts and teardown.

Evidence: Progress entry `FMT-1.9` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.9`.
Blocked behavior: Leave `FMT-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

Progress (2026-10-13): Added public deferred paste with one-time flavor capture, cancel/status UI, stable owner/parent/version revalidation, source recovery and later-selection restoration. Preparation/apply timings remain separate; scheduling yields without claiming worker offload. `npm run build`: exit 0. Pinned Node `EDITAC_LARGE_PASTE_OUTPUT=../architecture/evidence/markdown/session-20261013/pending-qualified npm run test:browser -- large-paste`: 18 executed/passed (6 per engine), 0 failed/skipped. Cancellation/deletion/move/destroy have no paste effects; duplicate completion ignored; second-replica text survives. Receipts retain hashes and complete teardown. Initial fixture argument failure preserved in pending.log.

### Task FMT-1.10 — Implement local Markdown typing shortcuts

- [x] FMT-1.10 Implement local Markdown typing shortcuts.

Purpose: Deliver implement local Markdown typing shortcuts as one reviewable boundary.
Context: `packages/web/src/input/shortcuts.ts`; `tests/browser/shortcuts.spec.ts`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.9.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Shortcuts preserve expected undo grouping and escape/literal behavior; unrelated blocks and remote updates trigger no global scan.

Implementation:

- [x] FMT-1.10-I1 Recognize bounded current-context patterns for headings, lists, quote, fence and inline marks. Suspend during composition/code and never parse remote updates.

Validation:

- [x] FMT-1.10-V1 npm run test:browser -- shortcuts. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FMT-1.10` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.10`.
Blocked behavior: Leave `FMT-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

Progress (2026-10-13): Bounded direct-key rules commit one prepared conversion, with separate undo boundary and immediate Backspace reversal. Trusted key correlation, composition/code/marked-context exclusions, Escape and a host switch preserve literal input; remote replay never triggers parsing. `npm run build`: exit 0. Pinned Node `EDITAC_SHORTCUTS_OUTPUT=../architecture/evidence/markdown/session-20261013/shortcuts-qualified npm run test:browser -- shortcuts`: 39 executed/passed (13 per engine), 0 failed/skipped, complete teardown and source/package hashes. Syntax/build failures retained in shortcuts*.log.

### Task FMT-1.13 — Integrate the complete clipboard format palette

- [x] FMT-1.13 Integrate the complete clipboard format palette.

Purpose: Deliver the named transfer boundary with reproducible evidence and explicit qualification status.
Context: `packages/web/src/clipboard/`; `tests/browser/clipboard-formats.spec.ts`; `crates/editac-markdown/`; `../architecture/specs/formats.md`; [mobile clipboard cases](../tests/mobile-web-cases.md)
Dependencies: FMT-1.8, FMT-1.9, FMT-1.10.
Session scope: One named boundary; target 15–45 minutes plus focused validation. These are future tasks; this roadmap revision does not execute native tests or authorize device runs.
Acceptance: The qualified Rust CommonMark/GFM importer and admitted extension codecs plug into WEB-1.9 transfer routing. Normal paste selects internal fragment, explicit Markdown, sanitized HTML, then host-configured plain-text Markdown policy without a raw intermediate document frame. The complete supported formatting palette round-trips, including nested/check lists, links, code, tables and images when registered; unsupported optional formats retain recoverable source plus diagnostics. Explicit plain paste never parses or formats.

Implementation:

- [x] FMT-1.13-I1 Add named codec adapters, host plain-text policy configuration and parameterized full-palette fixtures. Cover external word processors, browser and native producers, HTML/Markdown/plain/internal precedence, hostile/malformed data, codec absence, first formatted frame, Unicode/whitespace and prepared mobile event/platform plain-paste shortcut routing. Mobile target-runtime menus and OS shortcut observations retain their mandatory owner FMT-1.15; physical or virtual runtime evidence is accepted. Keep parser-conformance prerequisites intact; never substitute a browser-only Markdown parser.

Validation:

- [x] FMT-1.13-V1 `npm run test:browser -- clipboard-formats`. Exercise all supported formats across pinned Chromium/Firefox/WebKit and mobile event variants; require one semantic/history/storage operation per paste. Require nonzero matching cases and record executed/passed/failed/skipped counts, immutable fixture/source/package revisions and preserved failures. Missing tools or skipped mandatory mechanical cases do not qualify this task; platform support remains unqualified until FMT-1.15 passes on the accepted physical or virtual matrix.

Evidence: Separate progress entry with commands, exact environment and artifact hashes; catalogs remain planned until the corresponding runs exist.
Handoff: Last completed substep, unavailable environment or failing case, owner and next bounded action.
Controller split (2026-10-13): Separate browser/codec mechanics from physical OS/device observations so portable interchange and source reconciliation can be qualified independently. FMT-1.15 retains the original physical-device requirements and remains mandatory for roadmap completion; prepared variants never substitute for them.

Blocked behavior: Leave unchecked; name owner, unblock condition and retry trigger. Accept target-platform simulators/emulators/VMs under verification.md and retain virtual provenance; never relabel their results as physical-device observations.

Progress (2026-10-13): Full portable Markdown/internal palette qualified for registered images/tables, nesting/checklists, code, links, marks and Unicode. Public recovered/borrowed hosts honor preset/policy/content options; reserved or duplicate MIME codecs reject before allocating input owners. Unsupported RTF/TSV retains source. `npm run build`: exit 0. Pinned Node `EDITAC_CLIPBOARD_FORMATS_OUTPUT=../architecture/evidence/markdown/session-20261013/palette-final npm run test:browser -- clipboard-formats`: 33 executed/passed (11 per engine), 0 failed/skipped. Prepared mobile/shortcut variants are mechanics only; FMT-1.15 retains actual-device qualification. Receipts include package/source hashes and complete teardown. Initial origin/URL/event-fixture failures preserved in palette*.log.

### Task FMT-1.11 — Qualify Markdown interchange and paste costs

- [x] FMT-1.11 Qualify Markdown interchange and paste costs.

Purpose: Deliver qualify Markdown interchange and paste costs as one reviewable boundary.
Context: `benchmarks/paste/`; `tests/browser/markdown-collaboration.spec.ts`; `../architecture/evidence/markdown.md`; `../architecture/specs/formats.md`.
Dependencies: FMT-1.10, FMT-1.13.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Conformance, semantic round-trips and concurrent paste pass; measured budgets include first formatted frame and failures remain visible. Fragment preflight reuse retains at most one ready plan for identical serialized input, invalidates on mutation and preserves unchanged-state failure behavior.

Implementation:

- [x] FMT-1.11-I1 Replay 10/100KiB fixed pastes and undo/redo with a prepared second replica. Publish supported dialect table and diagnostics with raw timings.

Validation:

- [x] FMT-1.11-V1 cargo test -p editac-markdown --locked; npm run test:browser -- markdown-collaboration. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `FMT-1.11` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.11`.
Blocked behavior: Leave `FMT-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

Progress (2026-10-13): Pinned exact-byte 10/100 KiB fixtures, 2 warmups + 30 fresh-session samples per size/engine, separate prepare/transfer/apply/formatted-frame/undo/redo costs and converged two-replica selective-history evidence. Bounded fragment preflight reuse avoids triple preparation and invalidates on mutation. Portable tests: 37 executed/passed; native WASM: 35 executed/passed; Node compiled-WASM: 39 executed/passed; packed browser: 9 executed/passed; zero final correctness failures/skips. Commands and hashes in `../evidence/markdown.md` and session receipts. First formatted-frame p95 (10/100 KiB): Chromium 32.9/75.2 ms, Firefox 37/154 ms, WebKit 40/156 ms. Retain the 50/150 ms targets: Firefox/WebKit 100 KiB misses and accumulated-history admission/cost failures remain explicit release-qualification blockers; no phone/peak-memory/Aged support is claimed. Earlier failures, fresh baseline and candidate raw samples remain visible.

### Task FMT-1.12 — Qualify portable Markdown source reconciliation

- [x] FMT-1.12 Qualify portable Markdown source reconciliation.

Purpose: Deliver a shared source-to-semantic editing boundary for CLI and future text-based hosts.
Context: `crates/editac-markdown/src/reconcile.rs`; `crates/editac-markdown/tests/reconcile.rs`; `crates/editac-core/src/commands/`; `../architecture/specs/formats.md`; `../architecture/specs/cli.md`; `../architecture/specs/engine.md`.
Dependencies: FMT-1.11.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue. Propose a controller split before implementation if identity mapping or concurrent revalidation needs a separate boundary.
Acceptance: An exact source baseline, opening semantic identities/anchors and edited source produce validated prepared commands without whole-document replacement. No-op retains source bytes and identities; supported disjoint edits preserve unchanged nodes/marks; ambiguous, overlapping, deleted-target and unsupported-content changes produce recoverable diagnostics without partial mutation. Literal-text mode never interprets Markdown. Concurrent structured updates are not reparsed as source.

Implementation:

- [x] FMT-1.12-I1 Define the portable source-reconciliation API with the shared parser/command boundary. Preserve baseline source spelling, unchanged semantic identities and unknown module data; revalidate current anchors before commit. Return explicit conflicts rather than treating stale source replacement as a CRDT merge. Pin fixtures for Unicode, lists/fences/reference links, no-op, unsupported atoms and prepared second-replica changes.

Validation:

- [x] FMT-1.12-V1 cargo test -p editac-markdown --test reconcile --locked; cargo test -p editac-core --locked. Assert all acceptance cases and record nonzero executed/passed/failed/skipped counts, seeds/hashes, unchanged-state rejection evidence and preserved failures.

Progress (2026-10-13): Qualified portable baseline/prepare/commit reconciliation with exact source, explicit owner mapping, whole-document parse, opening anchors, literal mode, recoverable conflicts and one native owner-preserving source-edit update. No-op/unknown content and concurrent disjoint edits retain identity; overlap/deletion/move/late failure are atomic rejections. Required commands `cargo test -p editac-markdown --test reconcile --locked --offline` (13 passed) and `cargo test -p editac-core -p editac-markdown --locked --offline` with Node 24.19.0 and isolated exchange paths (585 core + 50 Markdown passed, zero failed/ignored) exit 0. Source/test/artifact hashes, exact profile and preserved failed fragment-staging/missing-environment attempts: `../evidence/markdown/source-reconciliation.md`, `session-20261013/native-qualified.log`, `reconcile-identity-final.log`, and `../evidence/markdown/device/manifest.json`.

Evidence: Progress entry `FMT-1.12` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `FMT-1.12`.
Blocked behavior: Leave `FMT-1.12` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task FMT-1.15 — Qualify physical or virtual platform clipboard entry points

- [ ] FMT-1.15 Qualify physical or virtual platform clipboard entry points.

Purpose: Preserve the platform-runtime qualification requirements extracted from FMT-1.13.

Controller amendment (2026-10-13): execute the separate simulator/emulator development gate under `../architecture/tests/clipboard-emulator-development.md`. A passing FMT-1.15-V2 receipt unblocks portable development tracks as defined in `specs/verification.md`; FMT-1.15-V1 and physical release completion remain open. CAP-1.1 may own this bounded virtual execution and publish its receipt; do not start a duplicate roadmap-05 worker.

Context: `tests/manual/`; `../architecture/tests/mobile-web-cases.md`; `../architecture/specs/formats.md`; `../architecture/specs/verification.md`.
Dependencies: FMT-1.13.
Session scope: One bounded device qualification boundary. The earlier five-case emulator development gate remains a subset of the complete FMT-1.15-V1 release matrix, which now accepts physical or virtual target runtimes.
Acceptance: Record native mobile paste menus and all platform plain-paste shortcuts using physical or target-platform virtual OS clipboard and the qualified packed palette. Record unavailable hardware-only cases and tested virtual equivalents; missing implemented behavior or untested required cases leaves this task and the roadmap incomplete.

Implementation:

- [x] FMT-1.15-I1 Prepare the exact-version physical or virtual platform protocol, fixture hashes and expected semantic/history/storage observations for native mobile paste menus and platform plain-paste shortcuts.

- [ ] FMT-1.15-I2 Execute the user-approved simulator/emulator development procedure on a task-owned virtual device using the current packed artifacts; retain virtual provenance and collect the remaining complete release matrix on accepted physical or virtual runtimes.

Validation:

- [ ] FMT-1.15-V2 Record a passing virtual-device receipt for all five representative clipboard/undo/durability/literal assertions, nonzero executed counts, exact versions/hashes, native action traces and preserved failures. This qualifies development only; no physical observations are inferred.

- [ ] FMT-1.15-V1 Execute the protocol on actual mobile Safari/Chrome and desktop OS shortcut entry points, with nonzero observed case counts, exact device/browser/OS versions, source/package hashes and preserved failures. Missing required runtime/equivalent evidence or failed mandatory cases does not qualify support; physical hardware availability is not required.

Progress (2026-10-13): I1 complete: `core/tests/manual/markdown-clipboard.md`, three native-copy fixtures and exact source/package/WASM hashes in `../evidence/markdown/device/manifest.json`. V1 BLOCKED: device operator must supply actual mobile Safari/Chrome native menu and macOS/Windows/Linux shortcut observations against those artifacts. Read-only availability checks found no Apple devices and only an offline Android emulator; zero physical cases executed. Logs `../evidence/markdown/session-20261013/apple-devices.log` and `android-devices.log` preserve this limitation. Retry when actual hardware or matching existing observations are available; prepared desktop variants cannot close this gate.

Evidence: Device observation records under `../architecture/evidence/markdown/`; prepared desktop event variants remain separate evidence.
Handoff: Device owner supplies recorded real clipboard/menu/shortcut observations against the pinned artifacts; rerun after artifact changes.
Blocked behavior: Leave unchecked and preserve the roadmap IN_PROGRESS until the mandatory device evidence exists.
