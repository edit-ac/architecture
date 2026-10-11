# Build a local-first Markdown editor client

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `cli` (sibling of `architecture`). Deliver local Markdown/literal-text editing and optional online hosted document editing through the same client, as defined in [the CLI contract](../specs/cli.md). Read `../architecture/specs/packages-release.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `cli` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Base upstream entry gates: `02-engine.md` and `05-markdown-content.md` complete at the current source revision with passing artifact evidence, including FMT-1.12 source reconciliation. These base gates also appear in the manifest. Additional hosted gate: tasks CLI-1.7 through CLI-1.9 and CLI-1.12 require `06-synchronization.md` complete at the current revision with qualified protocol/receipt evidence. This task-specific gate is explicit here because the manifest models whole-track entry edges only. Local tasks CLI-1.1 through CLI-1.6, secondary diagnostics CLI-1.10 and local qualification/packaging CLI-1.11 can proceed without hosted readiness.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus validation; if a boundary is too large, stop with a precise proposed split for the controller. Pick a task only when every named dependency and applicable upstream gate is implemented and validated. Other ready tasks are permitted independent work. Do not launch implementation while its entry gate is unavailable.

Create named checks before invoking them. Record nonzero executed/passed/failed/skipped counts; missing tests and zero-match Rust filters fail acceptance. Run the narrow check, then relevant integration checks. Use prepared fixtures, fake editor executables and mocked service/auth/receipt transports only. No model API tests, live credential loading, production hosted writes, live dogfood, background runner startup or publication outside an explicit release task.

Local editing is the first deliverable. Hosted connectivity adds to that client; it must never make local file editing require a network or account. The historical filename is retained for existing links/configuration; it no longer limits this track to diagnostics.

## Epic CLI-1 — Build a local-first Markdown editor client

### Task CLI-1.1 — Pin the shared editor integration boundary

- [ ] CLI-1.1 Pin the shared editor integration boundary.

Purpose: Deliver pin the shared editor integration boundary as one reviewable boundary.
Context: `Cargo.toml`; `Cargo.lock`; `tests/help.rs`; `../architecture/specs/cli.md`; `../architecture/specs/formats.md`; `../architecture/specs/packages-release.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: A clean checkout builds with its lockfile and no sibling repository; help names only implemented capabilities.

Implementation:

- [ ] CLI-1.1-I1 Consume reviewed immutable engine/Markdown revisions or released crates. Define the editor-client capability boundary without advertising planned commands.

Validation:

- [ ] CLI-1.1-V1 cargo test --test help --locked; cargo run --locked -- --help. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `CLI-1.1` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.1`.
Blocked behavior: Leave `CLI-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task CLI-1.2 — Resolve local Markdown and literal-text targets

- [ ] CLI-1.2 Resolve local Markdown and literal-text targets.

Purpose: Deliver resolve local Markdown and literal-text targets as one reviewable boundary.
Context: `src/target.rs`; `tests/targets.rs`; `../architecture/specs/cli.md`; `../architecture/specs/formats.md`; `../architecture/specs/packages-release.md`.
Dependencies: CLI-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Existing Markdown and literal UTF-8 text open offline with no credential access; explicit creation, format selection and rejected targets have stable results.

Implementation:

- [ ] CLI-1.2-I1 Resolve local paths and declared format without attaching a transport. Require --create for a missing file; preserve source bytes and target identity/fingerprint. Reject invalid UTF-8, ambiguous formats and unsupported targets before mutation.

Validation:

- [ ] CLI-1.2-V1 cargo test --test targets --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `CLI-1.2` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.2`.
Blocked behavior: Leave `CLI-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task CLI-1.3 — Run recoverable text-editor sessions

- [ ] CLI-1.3 Run recoverable text-editor sessions.

Purpose: Deliver run recoverable text-editor sessions as one reviewable boundary.
Context: `src/editor.rs`; `tests/editor.rs`; `tests/fixtures/editor/`; `../architecture/specs/cli.md`; `../architecture/specs/formats.md`; `../architecture/specs/packages-release.md`.
Dependencies: CLI-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: A deterministic fake editor can change the source, leave it unchanged, cancel or fail; only successful changed buffers advance to preparation.

Implementation:

- [ ] CLI-1.3-I1 Launch the configured editor or VISUAL/EDITOR against a private working copy using a documented argument parser and executable/argument invocation. Keep source and baseline on failure, return actionable errors, and leave the original untouched on no-op/cancel.

Validation:

- [ ] CLI-1.3-V1 cargo test --test editor --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `CLI-1.3` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.3`.
Blocked behavior: Leave `CLI-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task CLI-1.4 — Apply shared source reconciliation to local edits

- [ ] CLI-1.4 Apply shared source reconciliation to local edits.

Purpose: Deliver apply shared source reconciliation to local edits as one reviewable boundary.
Context: `src/reconcile.rs`; `tests/reconcile.rs`; `Cargo.toml`; `Cargo.lock`; `../architecture/specs/cli.md`; `../architecture/specs/formats.md`; `../architecture/specs/packages-release.md`.
Dependencies: CLI-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Supported Markdown and literal-text edits use shared prepared commands; unchanged semantic identities and unknown data survive, while ambiguous or lossy changes fail without partial mutation.

Implementation:

- [ ] CLI-1.4-I1 Consume the qualified FMT-1.12 portable reconciliation API and repin its immutable core revision. Retain exact source baselines and stable anchors, parse user edits outside mutation, and commit one shared history operation only after validation. Preserve edited local source spelling rather than normalizing it through export.

Validation:

- [ ] CLI-1.4-V1 cargo test --test reconcile --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `CLI-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.4`.
Blocked behavior: Leave `CLI-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task CLI-1.5 — Save local edits without stale-file overwrite

- [ ] CLI-1.5 Save local edits without stale-file overwrite.

Purpose: Deliver save local edits without stale-file overwrite as one reviewable boundary.
Context: `src/files.rs`; `tests/files.rs`; `../architecture/specs/cli.md`; `../architecture/specs/formats.md`; `../architecture/specs/packages-release.md`.
Dependencies: CLI-1.4.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Changed opened targets save atomically; no-op leaves bytes untouched; stale fingerprints, replaced targets, read-only/full-disk failures and failed publication preserve the original or report an explicitly uncertain publication with recoverable source.

Implementation:

- [ ] CLI-1.5-I1 Use cooperating locks, baseline revalidation, same-directory temporary writes and tested flush/publication ordering. Preserve permissions and declared line endings. Refuse changed symlink/target identity and stale content; require explicit overwrite for a different existing export path. Document races with non-cooperating writers rather than claiming atomic rename is compare-and-swap.

Validation:

- [ ] CLI-1.5-V1 cargo test --test files --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `CLI-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.5`.
Blocked behavior: Leave `CLI-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task CLI-1.6 — Recover locally committed sessions and pending updates

- [ ] CLI-1.6 Recover locally committed sessions and pending updates.

Purpose: Deliver recover locally committed sessions and pending updates as one reviewable boundary.
Context: `src/storage.rs`; `tests/storage.rs`; `tests/fixtures/recovery/`; `../architecture/specs/cli.md`; `../architecture/specs/storage-sync.md`; `../architecture/specs/packages-release.md`.
Dependencies: CLI-1.5.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Deterministic interruption/corruption fixtures recover committed state and drafts; two writers have distinct live identities; local acknowledgment cannot precede the native durability boundary.

Implementation:

- [ ] CLI-1.6-I1 Implement native checkpoint/journal/outbox persistence using the shared storage identity contract. Persist draft source separately from committed CRDT updates, publish coverage atomically and retain unacknowledged identities/bytes. Ordinary text files remain usable without a proprietary container.

Validation:

- [ ] CLI-1.6-V1 cargo test --test storage --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `CLI-1.6` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.6`.
Blocked behavior: Leave `CLI-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task CLI-1.7 — Open authorized hosted documents and offline caches

- [ ] CLI-1.7 Open authorized hosted documents and offline caches.

Purpose: Deliver open authorized hosted documents and offline caches as one reviewable boundary.
Context: `src/hosted.rs`; `src/auth.rs`; `tests/hosted.rs`; `tests/fixtures/hosted/`; `../architecture/specs/cli.md`; `../architecture/specs/storage-sync.md`; `../architecture/specs/packages-release.md`.
Dependencies: CLI-1.6.
Additional entry gate: `06-synchronization.md` complete with current passing protocol/receipt evidence.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: A mocked adapter resolves authorized document identity and restores once; cached offline opens work; uncached offline, auth failure and incompatible schema/epoch never initialize an empty replacement or erase local work.

Implementation:

- [ ] CLI-1.7-I1 Resolve edit.ac-compatible hosted URLs through an explicit service configuration and existing credential-store abstraction. Bootstrap once, persist a native cache, reuse saved credentials and keep tokens out of buffers/logs. No production backend or new wire format is implemented by implication.

Validation:

- [ ] CLI-1.7-V1 cargo test --test hosted --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `CLI-1.7` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.7`.
Blocked behavior: Leave `CLI-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task CLI-1.8 — Reconcile hosted Markdown edits against concurrent changes

- [ ] CLI-1.8 Reconcile hosted Markdown edits against concurrent changes.

Purpose: Deliver reconcile hosted Markdown edits against concurrent changes as one reviewable boundary.
Context: `src/reconcile.rs`; `src/hosted.rs`; `tests/hosted_edits.rs`; `../architecture/specs/cli.md`; `../architecture/specs/storage-sync.md`; `../architecture/specs/packages-release.md`.
Dependencies: CLI-1.7.
Additional entry gate: `06-synchronization.md` complete with current passing protocol/receipt evidence.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: A prepared second replica proves unchanged identities and disjoint edits survive; overlap/deletion/unknown semantics yield retained base/local/current conflict evidence instead of stale full-document replacement.

Implementation:

- [ ] CLI-1.8-I1 Capture the opening Markdown projection with semantic identity/anchor mappings, apply received updates directly to the current replica and revalidate source-derived edits before commit. Commit only safe prepared changes and retain unresolved editor buffers without resetting epoch/history.

Validation:

- [ ] CLI-1.8-V1 cargo test --test hosted_edits --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `CLI-1.8` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.8`.
Blocked behavior: Leave `CLI-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task CLI-1.9 — Synchronize pending work with explicit durability status

- [ ] CLI-1.9 Synchronize pending work with explicit durability status.

Purpose: Deliver synchronize pending work with explicit durability status as one reviewable boundary.
Context: `src/sync.rs`; `src/status.rs`; `tests/sync.rs`; `tests/status.rs`; `../architecture/specs/cli.md`; `../architecture/specs/storage-sync.md`; `../architecture/specs/packages-release.md`.
Dependencies: CLI-1.8.
Additional entry gate: `06-synchronization.md` complete with current passing protocol/receipt evidence.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Mocked disconnect/reconnect, duplicate/reordered updates, wrong/missing receipts and revocation preserve pending work; locally saved and remotely committed are distinct truthful states.

Implementation:

- [ ] CLI-1.9-I1 Attach the qualified transport to the restored replica only after local persistence. Implement explicit sync/status commands, bounded retries and receipt-driven pruning. Preserve outbox and exportability across authorization/schema failures; services without receipts report remote durability unknown.

Validation:

- [ ] CLI-1.9-V1 cargo test --test sync --test status --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `CLI-1.9` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.9`.
Blocked behavior: Leave `CLI-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task CLI-1.10 — Expose secondary interchange diagnostics

- [ ] CLI-1.10 Expose secondary interchange diagnostics.

Purpose: Deliver expose secondary interchange diagnostics as one reviewable boundary.
Context: `src/diagnostics.rs`; `tests/diagnostics.rs`; `../architecture/specs/cli.md`; `../architecture/specs/formats.md`; `../architecture/specs/packages-release.md`.
Dependencies: CLI-1.5.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Prepared Markdown/JSON/identified-update fixtures produce stable diagnostics; malformed/oversized/unknown versions fail safely, and lossy output or existing export destinations are never silently accepted.

Implementation:

- [ ] CLI-1.10-I1 Add bounded explicit validation, conversion and safe metadata inspection through shared format APIs. Keep input/output types explicit, source untouched on failure and conversion atomic; JSON/binary inspection is secondary to editing and must not claim server durability.

Validation:

- [ ] CLI-1.10-V1 cargo test --test diagnostics --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `CLI-1.10` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.10`.
Blocked behavior: Leave `CLI-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task CLI-1.11 — Qualify and package the local editor client

- [ ] CLI-1.11 Qualify and package the local editor client.

Purpose: Deliver a separately qualified local-only client artifact without waiting for hosted connectivity.
Context: `README.md`; `.github/workflows/ci.yml`; `tests/local_workflows.rs`; `tests/commands.rs`; `tests/fixtures/workflows/`; `../architecture/evidence/cli.md`; `../architecture/specs/cli.md`; `../architecture/specs/formats.md`; `../architecture/specs/packages-release.md`.
Dependencies: CLI-1.6, CLI-1.10.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: A clean-checkout native artifact passes nonzero local Markdown/text, no-op/cancel, Unicode, source-preservation, stale-save and recovery tests plus packaged-binary probes without account/network access. Help/examples match the implemented local capabilities; unavailable hosted commands are not advertised. Publication remains a separately recorded action.

Implementation:

- [ ] CLI-1.11-I1 Qualify fake-editor local workflows and native artifacts across the supported platform/filesystem envelope. Document configured editor, literal text, recovery/conflict paths, limits and durability capability with tested examples, Apache notices and immutable dependency provenance. Record local-client evidence without claiming hosted qualification or registry publication.

Validation:

- [ ] CLI-1.11-V1 cargo test --test local_workflows --test commands --locked; cargo test --locked; cargo build --release --locked. Run named probes against the packaged binary, assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts (nonzero matching tests required).

Evidence: Progress entry `CLI-1.11` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.11`.
Blocked behavior: Leave `CLI-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task CLI-1.12 — Qualify and package hosted document editing

- [ ] CLI-1.12 Qualify and package hosted document editing.

Purpose: Deliver qualified hosted connectivity as an addition to the local editor client.
Context: `README.md`; `.github/workflows/ci.yml`; `tests/hosted_workflows.rs`; `tests/commands.rs`; `tests/fixtures/workflows/`; `../architecture/evidence/cli.md`; `../architecture/specs/cli.md`; `../architecture/specs/storage-sync.md`; `../architecture/specs/packages-release.md`.
Dependencies: CLI-1.9, CLI-1.11.
Additional entry gate: `06-synchronization.md` complete with current passing protocol/receipt evidence.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Nonzero mocked hosted workflow and packaged-binary probes cover cached offline editing, concurrent changes/conflicts, reconnect, revocation and wrong/missing receipts. Help/examples match implemented local and hosted commands; local editing remains usable without account/network. Actual limits and failures/skips are published as qualification evidence; publication is separately recorded.

Implementation:

- [ ] CLI-1.12-I1 Replay fake-editor and mocked-service hosted workflows, retain failures and document cache/authorization/conflict paths and local-versus-remote states. Probe native artifacts with hosted capabilities enabled while retaining the local-only guarantees. Keep distribution independent of npm/browser publication and native UI parity; use no live credentials, production document writes or provider inference.

Validation:

- [ ] CLI-1.12-V1 cargo test --test hosted_workflows --test commands --locked; cargo test --locked; cargo build --release --locked. Run named packaged-binary probes using mocked hosted transports, assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts (nonzero matching tests required).

Evidence: Progress entry `CLI-1.12` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `CLI-1.12`.
Blocked behavior: Leave `CLI-1.12` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.
