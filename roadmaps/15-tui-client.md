# Deliver the native Rust terminal editor

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `cli` (sibling of `architecture`). Read [the owning contract](../specs/tui-client.md), [shared client contracts](../specs/client-contracts.md) and the active task's named context. Paths below are relative to `cli` unless explicitly prefixed with `../architecture/`. Planned implementation/test files are created by their task. Source is controller-owned; write checkmarks, state and evidence only in the separate progress file.

Upstream entry gates: `11-offline-cli.md`, `12-client-contracts.md`, `13-change-diffs.md` complete at current source revisions with passing artifact evidence. Cross-roadmap IDs are context references; dependencies below name only parents in this file. Do not launch implementation while an upstream gate is unavailable.

The terminal UI consumes the existing local/hosted CLI services and shared source-buffer API. MCP is an app-owned optional feature, not a prerequisite for terminal editing. Local targets remain usable without a network/account; configured host adapters add online synchronization. This track produces qualified artifacts; final publication and cross-client claims belong to their release owner.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus focused validation. Inspect actual symbols before editing; reuse the qualified owning implementation. If the named boundary is larger, record the exact remaining acceptance and a proposed controller split rather than silently expanding scope or weakening it. Other dependency-ready parents in this track are permitted independent work; unmet prerequisites remain unchecked.

Create the named tests before invoking them. Capture full logs locally; record nonzero executed/passed/failed/skipped counts, exact commands, fixture/artifact hashes and revisions in progress. Missing tests, zero-match filters, failed checks and skipped required cases never prove completion. Use deterministic fixtures and mocked host/auth/receipt transports. No model/provider calls, live credential loading, production document writes, background runner startup or publication are authorized by this implementation track.

## Epic TUI-1 — Deliver the native Rust terminal editor


### Task TUI-1.1 — Verify shared terminal-client entry gates

- [ ] TUI-1.1 Implement and validate verify shared terminal-client entry gates.

Purpose: Establish the existing session, URI and diff services that the terminal presenter will consume.
Context: `Cargo.toml`; `src/`; `../architecture/evidence/`; `../architecture/specs/cli.md`; `../architecture/specs/change-diffs.md`; `../architecture/specs/tui-client.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Current CLI, client-contract and change/diff gates pass; the shared source-buffer/session API exposes explicit revision, prepared edit, history, storage and capability results. Missing APIs are reported to their owning task rather than cloned in TUI code.

Implementation:

- [ ] TUI-1.1-I1 Map qualified entry points and immutable engine dependency revisions. Record one prepared local source session and one hosted cached session fixture, including their read-only/diff/save states; name the existing API each subsequent task consumes.

Validation:

- [ ] TUI-1.1-V1 Rerun the owning CLI session/source-buffer and shared diff fixture commands recorded in upstream evidence; verify their selected tests execute. Record a small interface map in ../architecture/evidence/tui-entry.md. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `TUI-1.1` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `TUI-1.1`.
Blocked behavior: Leave `TUI-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task TUI-1.2 — Select and pin the terminal backend

- [ ] TUI-1.2 Implement and validate select and pin the terminal backend.

Purpose: Choose a supported Rust event/render backend with reproducible compatibility evidence.
Context: `Cargo.toml`; `Cargo.lock`; `../architecture/decisions/tui-backend.md`; `tests/tui_backend.rs`; `../architecture/specs/tui-client.md`.
Dependencies: TUI-1.1.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: A bounded comparison cites official docs and exact candidate versions; selected compiler/license/OS/input/PTY requirements fit the workspace, and a headless event/draw probe compiles without network services. Unsupported platform capabilities are explicit.

Implementation:

- [ ] TUI-1.2-I1 Time-box the choice to one session and at most two viable candidates. Verify official documentation and declared versions/features before pinning one backend and its lockfile. Add only the minimal deterministic probe; do not implement a bespoke terminal renderer or expand into benchmarking.

Validation:

- [ ] TUI-1.2-V1 cargo test --test tui_backend --locked; cargo tree --locked. Record the chosen feature set and compatibility decision with primary documentation links. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `TUI-1.2` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `TUI-1.2`.
Blocked behavior: Leave `TUI-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task TUI-1.3 — Open shared document targets in terminal sessions

- [ ] TUI-1.3 Implement and validate open shared document targets in terminal sessions.

Purpose: Reuse offline-first target resolution and host authorization without adding a terminal-specific identity model.
Context: `src/tui/session.rs`; `src/main.rs`; `tests/tui_targets.rs`; `../architecture/specs/client-contracts.md`; `../architecture/specs/tui-client.md`.
Dependencies: TUI-1.1, TUI-1.2.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: The planned editac tui target route opens local Markdown/text and cached ac references without network access; missing-file creation is explicit. Configured adapter URLs respect authority; unknown URLs, uncached offline identities and unauthorized targets never become empty editable documents.

Implementation:

- [ ] TUI-1.3-I1 Wire argument parsing and the shared local catalog/session factory to the TUI route. Carry document/epoch/schema and capability results unchanged. Treat ac://DOC_ID as a mutable identifier, not a credential/content hash; redact profile secrets and retain existing external-editor commands.

Validation:

- [ ] TUI-1.3-V1 cargo test --test tui_targets --locked. Cover URI normalization/catalog hits, literal text, explicit create, arbitrary HTTP targets, configured authority, cached/offline and read-only results using mocked adapters. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `TUI-1.3` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `TUI-1.3`.
Blocked behavior: Leave `TUI-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task TUI-1.4 — Own the terminal event and display lifecycle

- [ ] TUI-1.4 Implement and validate own the terminal event and display lifecycle.

Purpose: Provide a recoverable terminal shell before editing behavior is attached.
Context: `src/tui/terminal.rs`; `src/tui/view.rs`; `tests/tui_terminal.rs`; `../architecture/specs/tui-client.md`.
Dependencies: TUI-1.3.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Fixed-size frames expose source/status/help regions; resize/focus are deterministic. Raw mode, alternate screen and cursor state restore after normal exit, failed startup and injected draw/read errors; rendering document bytes cannot emit terminal control sequences.

Implementation:

- [ ] TUI-1.4-I1 Add one terminal guard and bounded event/draw loop over the selected backend. Render initial source and session status with untrusted-control escaping, explicit focus and resize policy. Keep event tasks/terminal handles under one idempotent owner.

Validation:

- [ ] TUI-1.4-V1 cargo test --test tui_terminal --locked. Check frame snapshots, malicious control bytes, resize, initialization failures and teardown via injected backend operations. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `TUI-1.4` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `TUI-1.4`.
Blocked behavior: Leave `TUI-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task TUI-1.5 — Edit Unicode source buffers and selections

- [ ] TUI-1.5 Implement and validate edit unicode source buffers and selections.

Purpose: Make terminal editing precise across source bytes, engine offsets and screen columns.
Context: `src/tui/input.rs`; `src/tui/positions.rs`; `tests/tui_input.rs`; `../architecture/specs/tui-client.md`.
Dependencies: TUI-1.4.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Movement, selection, insert/delete, multiline input and bracketed paste preserve valid source and documented caret behavior. Emoji/ZWJ, combining/wide characters, tabs, CRLF and bidi source have explicit fixtures; literal-text mode never invokes Markdown shortcuts.

Implementation:

- [ ] TUI-1.5-I1 Map terminal keys/events to the shared source-buffer API and its position conversions. Add a presentation-only source-to-screen mapping; do not create a second semantic document or confuse terminal columns with UTF-16. Keep paste bounded and literal at the buffer boundary.

Validation:

- [ ] TUI-1.5-V1 cargo test --test tui_input --locked. Assert cursor/selection and exact source bytes for the named Unicode cases, paste boundaries and malformed input; verify no semantic commit occurs before preparation. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `TUI-1.5` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `TUI-1.5`.
Blocked behavior: Leave `TUI-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task TUI-1.6 — Commit source edits with shared history and storage

- [ ] TUI-1.6 Implement and validate commit source edits with shared history and storage.

Purpose: Give save, undo and redo the same semantics and durability as other clients.
Context: `src/tui/commands.rs`; `src/tui/session.rs`; `tests/tui_commit.rs`; `../architecture/specs/tui-client.md`.
Dependencies: TUI-1.5.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Prepared commits occur once; rejected/no-op edits leave live state unchanged and retain source spelling. Undo/redo use local origin-aware groups; saved status appears only after qualified local persistence and remains distinct from remote receipt state.

Implementation:

- [ ] TUI-1.6-I1 Route commit/save/undo/redo through the existing source session and command/history interfaces. Surface invalid mapping, unsupported module data and storage failure as recoverable results. Reuse native journal/outbox flush barriers rather than adding terminal-owned saved flags.

Validation:

- [ ] TUI-1.6-V1 cargo test --test tui_commit --locked. Use fixed commands and injected disk/receipt failures to cover no-op, unsupported data, one-group undo, redo and correct local/remote status transitions. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `TUI-1.6` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `TUI-1.6`.
Blocked behavior: Leave `TUI-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task TUI-1.7 — Present revision-labeled diffs and read-only states

- [ ] TUI-1.7 Implement and validate present revision-labeled diffs and read-only states.

Purpose: Let users inspect changes and understand when the current session cannot mutate a document.
Context: `src/tui/diff.rs`; `src/tui/commands.rs`; `tests/tui_diff.rs`; `../architecture/specs/change-diffs.md`; `../architecture/specs/tui-client.md`.
Dependencies: TUI-1.6.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: The view labels compared revisions and exact source versus hosted-projection semantics, displays additions/deletions and opaque limitations, and never applies a stale preview. Read-only sessions reject every mutation route while permitted copy/export remains usable.

Implementation:

- [ ] TUI-1.7-I1 Render shared change/diff results in a bounded review view with context/navigation and explicit return to editing. Reuse revision-checked commit behavior. Gate paste, keyboard commands and undo/redo through session capabilities; retain source/opaque fallback honestly.

Validation:

- [ ] TUI-1.7-V1 cargo test --test tui_diff --locked. Check source/projection labels, whitespace/Unicode changes, stale reviews, unknown module data, view navigation and attempts to mutate through each read-only command path. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `TUI-1.7` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `TUI-1.7`.
Blocked behavior: Leave `TUI-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task TUI-1.8 — Handle remote updates while a source buffer is dirty

- [ ] TUI-1.8 Implement and validate handle remote updates while a source buffer is dirty.

Purpose: Keep ongoing collaborative edits from overwriting local terminal drafts.
Context: `src/tui/collaboration.rs`; `src/tui/session.rs`; `tests/tui_remote.rs`; `../architecture/specs/tui-client.md`.
Dependencies: TUI-1.7.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: A clean buffer refreshes with stable selection; a dirty buffer retains base/local/current representations. Disjoint qualified mappings reconcile through shared source preparation; duplicate/reordered updates and detach/reconnect never replace the live replica or silently submit stale full source.

Implementation:

- [ ] TUI-1.8-I1 Subscribe to shared session changes and apply remote structured updates through the existing engine. Refresh only safe presentation state, retain dirty drafts and call the qualified FMT-1.12 reconciliation path. Bound pending UI work and surface current local/remote durability separately.

Validation:

- [ ] TUI-1.8-V1 cargo test --test tui_remote --locked. Drive prepared second-replica edits, duplicates, delayed receipts, disconnect and reconnect while clean/dirty; assert stable identity/history, source recovery and bounded queues. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `TUI-1.8` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `TUI-1.8`.
Blocked behavior: Leave `TUI-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task TUI-1.9 — Resolve overlapping edits with a three-way view

- [ ] TUI-1.9 Implement and validate resolve overlapping edits with a three-way view.

Purpose: Make concurrent source conflicts recoverable and explicit before another semantic commit.
Context: `src/tui/conflict.rs`; `src/tui/collaboration.rs`; `tests/tui_conflict.rs`; `../architecture/specs/tui-client.md`.
Dependencies: TUI-1.8.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Overlap, deleted targets, ambiguous mapping and incompatible epoch preserve base/local/current content without partial mutation. User-selected resolution is prepared against current revision; another remote change invalidates stale resolution safely. Cancel/export retains recoverable drafts.

Implementation:

- [ ] TUI-1.9-I1 Present shared conflict results with labeled base/local/current panes or equivalent accessible source views. Offer bounded explicit resolution and recovery/export actions; submit resolved source through the existing preparation/revision check instead of implementing a new merge algorithm.

Validation:

- [ ] TUI-1.9-V1 cargo test --test tui_conflict --locked. Cover overlap, removed targets, unknown content, repeated remote advancement, cancellation and a validated explicit resolution with exact semantic/source outcomes. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `TUI-1.9` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `TUI-1.9`.
Blocked behavior: Leave `TUI-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task TUI-1.10 — Recover drafts across quit and terminal interruption

- [ ] TUI-1.10 Implement and validate recover drafts across quit and terminal interruption.

Purpose: Preserve unsaved or unsynchronized work and restore the terminal on lifecycle failures.
Context: `src/tui/lifecycle.rs`; `src/tui/terminal.rs`; `tests/tui_recovery.rs`; `../architecture/specs/tui-client.md`.
Dependencies: TUI-1.9.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Normal quit, startup/I/O failure and supported interrupt/suspend/resume paths dispose resources and restore terminal settings. Flush failure offers explicit recoverable exit behavior; restart recovers locally committed data, pending outbox and unresolved draft/conflict state without claiming remote durability.

Implementation:

- [ ] TUI-1.10-I1 Connect terminal ownership to shared session flush/disposal and draft recovery. Handle supported signal/lifecycle events without using signal handlers as a guaranteed persistence mechanism. Stop task-owned event/transport loops and make repeated teardown safe.

Validation:

- [ ] TUI-1.10-V1 cargo test --test tui_recovery --locked. Inject failures before/after durability boundaries and restart sessions with prepared caches; assert resource disposal, draft recovery, outbox preservation and terminal restoration. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `TUI-1.10` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `TUI-1.10`.
Blocked behavior: Leave `TUI-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task TUI-1.11 — Qualify deterministic packaged-client PTY workflows

- [ ] TUI-1.11 Implement and validate qualify deterministic packaged-client pty workflows.

Purpose: Prove that the actual command behaves correctly through a terminal boundary.
Context: `tests/tui_pty.rs`; `tests/fixtures/tui/`; `scripts/`; `../architecture/evidence/tui-pty.md`; `../architecture/specs/tui-client.md`.
Dependencies: TUI-1.10.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Nonzero PTY cases exercise the built binary with fixed dimensions/keys and prepared local/hosted state. Markdown/text, diff/read-only, undo, dirty remote edits/conflict, offline restart, resize and error exit pass; all child processes/temporary files terminate cleanly.

Implementation:

- [ ] TUI-1.11-I1 Add a bounded PTY harness and recorded deterministic event/expected-result fixtures. Feed remote changes through a mock host transport and capture normalized frames plus final source/state hashes. Keep raw input/output and secrets out of public evidence.

Validation:

- [ ] TUI-1.11-V1 cargo test --test tui_pty --locked. Preserve failed PTY artifacts, exact terminal settings and executed/passed/failed/skipped counts; verify teardown after both success and intentionally failing child runs. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `TUI-1.11` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `TUI-1.11`.
Blocked behavior: Leave `TUI-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.


### Task TUI-1.12 — Package the terminal client with honest support claims

- [ ] TUI-1.12 Implement and validate package the terminal client with honest support claims.

Purpose: Make the implemented TUI usable from reproducible artifacts and executable instructions.
Context: `README.md`; `docs/tui.md`; `Cargo.toml`; `tests/tui_help.rs`; `../architecture/evidence/tui-client.md`; `../architecture/specs/tui-client.md`.
Dependencies: TUI-1.11.
Session scope: One named boundary; target 15–45 minutes plus validation. Limit edits to named paths and directly required test/configuration glue.
Acceptance: Clean packaged-binary consumers can discover and run supported TUI targets without a sibling checkout. Help matches behavior, external-editor commands remain available, and supported terminal/OS/accessibility claims identify actual evidence rather than inferring it from PTY simulation.

Implementation:

- [ ] TUI-1.12-I1 Document keys, target/authority rules, source/diff/conflict semantics, local/remote save states, fallback limitations and recovery. Assemble release artifacts using the existing CLI packaging path and record tested terminal/OS versions plus unresolved qualification cells for the final release gate.

Validation:

- [ ] TUI-1.12-V1 cargo test --test tui_help --locked; run the existing CLI clean-package consumer check with TUI help/local-file cases. Review claimed terminal/platform cells against recorded evidence; do not publish or assert untested support. Assert the acceptance cases above and record executed/passed/failed/skipped counts.

Evidence: Progress entry `TUI-1.12` links changed paths, implementation/source revisions, exact commands/results and fixture/artifact hashes. Preserve failures; milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, relevant symbols, remaining acceptance, exact failing fixture or missing decision and next bounded action for `TUI-1.12`.
Blocked behavior: Leave `TUI-1.12` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and bounded retry trigger. Continue another dependency-ready parent only in a later iteration; if none exists, report the external gate without polling.
