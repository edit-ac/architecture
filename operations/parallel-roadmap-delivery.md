# Parallel roadmap delivery and integration

Created 2026-10-13 by explicit user request. Primary workspace: `/Users/bpstr/Github/edit-ac`. Parallel workspace: `/Users/bpstr/Github/edit-ac-parallel-clients`. Every parallel repository uses `runner/parallel-clients-20261013`; see the parallel root worktree-manifest.json for base commits.

## Ownership and queue

Primary runner `f8ac8f9bb10d07675936cfbc` owns completed roadmap 08 SDK, active roadmap 09 native preparation, then queued roadmaps 42 regression suite, 30 architecture fitness, 14 host-agent editing, 16 iOS SDK and 17 Android SDK. Parallel runner owns this FIFO queue: 12 shared client contracts, 13 exact change review, 21 extension library, 11 offline CLI, 15 TUI, 26 link resolution, 19 optional protection. Do not launch duplicate controllers or take another runner's parents. The remaining roadmaps stay outside these two queues; their missing SDK/native/client/content/device prerequisites need fresh scheduling.

The queue is dependency-ordered, not a claim that later tracks already pass their gates. Recheck each entry against current code, named evidence and merged progress. Reuse the committed engine, storage, Markdown SourceBaseline/prepare/commit, synchronization and module implementations. Preserve roadmap 05's explicit physical-device FMT-1.15 gap; portable FMT-1.12 and the already recorded module/SDK implementation baseline are the headless entry evidence, not a device/release claim. CAP-1.1 must verify the reviewed contracts at the actual isolated source hashes. If a required portable gate fails, stop with the concrete blocker; do not waive acceptance or retry indefinitely.

## Isolation and source control

Implement only in the parallel repositories and write progress under parallel architecture/progress, one parent per iteration. Sources remain controller-owned. The primary checkouts contain active, uncommitted SDK/Markdown work; do not copy, stage, stash, reset, overwrite or claim it. Baseline the new worktrees on committed main. Before changing shared Cargo manifests/locks, WASM/engine public interfaces, browser module runtimes or authoritative specs, consult both workspaces' diffs and the shared delivery ledger. Coordinate an unavoidable contract overlap through an integration-request file instead of independently implementing the same API. Use new session/diff/library adapters around existing semantics.

Commit each validated delivery in its owning parallel repository with a plain-English imperative subject. Stage exact owned paths, never git add -A across another task's changes. Record the task ID, branch commit, source hashes, checks/counts, progress and artifact locations in `.roadmap-coordination/deliveries.jsonl` at the shared primary root; include failures and unresolved gates. Progress files are ignored: publish their locations/hashes and copy the parallel-owned progress file to the primary architecture/progress only at an agreed integration checkpoint. Never copy 08/09 progress in either direction.

## Periodic integration

After every two completed parent tasks and every roadmap boundary, and before each next roadmap entry gate, reconcile with main in every repository changed by this lane. Read the shared ledger first so merged tasks are reused rather than recreated. Take the shared `.roadmap-coordination/integration.lock` with an atomic mkdir for the brief integration transaction; write owner, PID, task, time and repository details inside. Respect an existing lock; never remove one based on age alone. Release your own lock in teardown.

Incoming sync: from a clean parallel tree, merge the repository's local main into this branch, resolve conflicts against both owners' validated behavior, rerun the checks affected by the merge and record the merge commit. Fetch and compare origin/main when useful, but never force-update main or silently drop another task's work.

Outgoing sync: integrate validated parallel commits to the local primary main periodically. The primary lane owns modification of its live checkouts. The parallel lane writes `.roadmap-coordination/integration-request.json` with per-repository branch/commits, exact changed paths, checks, progress paths and any conflicts. The primary lane processes it at its next completed-parent or roadmap checkpoint, after preserving/committing its own validated work and checking unrelated user changes. Merge core/API delivery first, then CLI consumers and architecture evidence/contracts in a coherent dependency order. Use normal git merge, preserve both branches' implementations and rerun meaningful affected checks. Record exact merged revisions and acknowledge in `.roadmap-coordination/integration-ack.json`.

Never run a merge into the primary checkout while its implementation worker is mutating it, nor merge over unrelated dirty work. If no safe checkpoint exists, record the deferred request and continue independent work in the parallel branch; refresh incoming main at the next checkpoint. A running controller alone is not stale and must not be stopped for integration. Neither lane may push, publish packages, deploy or use paid synthetic inference under this plan. Local main integration is explicitly requested.

## Validation and resource ownership

Read the root/repository instructions and only active task specs. Codanna MCP/CLI is unavailable in the controller session: discover it again in a worker before code discovery; if unavailable use narrow rg fallbacks and record coverage limits. All tests use deterministic fixtures/mock transports, never provider calls or .secrets. For core tests set unique absolute exchange/evidence directories for this worktree following architecture/WORKSPACE_SETUP.md. Use Node 24.19.0/npm 11.17.0 and rustup 1.97.1 explicitly, including child PATH. Build output, browser ports, fixture profiles and logs must be worktree-owned. Do not symlink mutable target/dist/node_modules output to primary. Preserve failed evidence.

Stop only verified task-owned temporary browsers/servers; preserve primary runner and other tasks' services. Check data-volume space after substantial builds and remove only inactive reproducible output from this lane. At a blocked gate or exhausted ready work, save a precise handoff and stop instead of uncontrolled model retries.

## User-approved emulator development entry amendment

2026-10-13: "Lets unblock, emulator should do for now" overrides the previous physical-only development blocker. Read the amended verification/formats/client specs and roadmaps 05/11/12/21. The resumed CAP-1.1 worker executes the five native clipboard assertions on an actual task-owned simulator/emulator and records FMT-1.15 development evidence; physical release evidence stays open. Reuse the completed audit matrix and passing tests, retain prior failed/BLOCKED evidence and stop on a new concrete unrecoverable blocker.

## User-approved binary hard caps

2026-10-13: "Lets increase hard caps to 512KB and 32KB" is adopted as 512 KiB total = 524,288 bytes and 32 KiB editor JS = 32,768 bytes. Preferred targets remain decimal 256,000 total / 16,000 JS bytes. Both architecture copies and both code contract/test copies were updated in place; historical measurements and failed evidence retain their original budget meaning. The primary runner was stopped for source adoption and will resume its preserved SDK progress plus queued native preparation on the revised source. A 31,996 JS / 478,907 total candidate already fit the old caps; prioritize full default/enabled parity, not unnecessary further size optimization. This budget decision does not close qualification or authorize publication.

Current primary controller after the cap amendment: `f8ac8f9bb10d07675936cfbc`; its 08/09 ownership is unchanged. Supervisor reviews now occur every two workers to strengthen handoff/integration checkpoints. The parallel controller is still `83cb6d69f62d4858e0234a36`.

## Primary queue expansion — user authorized

2026-10-13: user accepted the proposal with "Perfect lets queue them". Primary FIFO after 09 is **42 → 30 → 14 → 16 → 17**. The parallel queue remains **12 → 13 → 21 → 11 → 15 → 26 → 19**. Do not duplicate these owners.

42 consumes the completed 08 evidence. Before 30, safely integrate and validate completed parallel 12 and 21 plus current 08 evidence. Before 14, additionally integrate qualified 13. Before 16/17, verify the merged 07/12/13/21 contracts and their platform-specific 09 preparation receipts; 16 consumes NAT-1.1/1.2/1.3/1.5, 17 consumes NAT-1.1/1.2/1.4/1.6. Physical support claims remain with their designated release/device owners.

At the 09 and 42 completion checkpoints, review the pending integration request and reconcile main/parallel history under the shared lock. Preserve and commit only owned validated changes, resolve overlapping contracts with both lanes' passing behavior, rerun affected checks and record exact merged commits/progress hashes. Being queued does not satisfy an upstream gate. If required parallel delivery or a safe merge is unavailable when its roadmap reaches the front, save the precise handoff/unblock condition and stop that controller rather than retrying an unchanged gate or reproducing another lane's implementation.

## Hourly active monitor and integration

User authorization (2026-10-13): "Set up hourly monitor and resolve any blockers. Also make sure regular merge to main to avoid code drifts". Active thread heartbeat: monitor-edit-ac-runners-and-merge-progress. Read queue.json for current controller IDs; fix actionable code/toolchain/fixture/integration issues within existing roadmap scopes, and preserve paid-inference and publication restrictions.

Process validated unmerged deliveries on hourly checks, after two completed parents, and at roadmap boundaries. Generic dirty-tree deferral is insufficient: compare exact dirty paths with incoming changes and determine ownership/overlap. If needed, first prepare and test a union of immutable main/parallel commits in a separate integration worktree while preserving live work. Pause the affected controllers only for a safe landing checkpoint, retain partial source/logs and pending queues, preserve unrelated nonoverlapping changes byte-for-byte, land reviewed commits with normal Git merges, and reconcile merged main back into the parallel branch before resuming. Do not blindly stash/reset, overwrite active files, stage unvalidated work from another task, force-update main, or treat a queued prerequisite as completed.

The controller can commit explicitly user-authorized, reviewed planning/rule amendments after planning validation so they no longer prevent integration. Leave unrelated benchmark work and historical/generated qualification changes untouched. Record actual merged revisions, checks, preserved dirty-path hashes and resumed IDs in the ledger and acknowledgment. If overlap cannot be resolved safely, identify exact paths and an actionable next step instead of repeatedly polling the same blocker.

For each blocked parent, record a fingerprint of task, consumed source revision, error and missing prerequisite, plus owner, evidence, attempted repair and exact resume condition. After an unchanged failed repair, do not restart a worker or rerun validation without changed input or a concrete new repair hypothesis. Continue independent authorized work when dependencies permit; otherwise stop the affected controller and notify once. Hourly checks inspect pending validated deliveries as well as runner liveness; unchanged state must not create repeated notifications or model-driven retry loops.

The current roadmap runner automatically continues after a BLOCKED worker even
when dependencies are unchanged. Arm `scripts/guard-roadmap-recovery.py` for each
resumed lane with its exact managed run ID, workspace, event log, CLI path and
receipt path. This deterministic guard stops that controller after a completed
BLOCKED worker and preserves progress/FIFO; it never restarts a run. It ignores
active work, supervisor turns, foreign run IDs and foreign progress paths. The
hourly monitor may resume only after a qualified dependency return or a concrete
changed repair input, and must re-arm the guard for the new ID. Record guard PID,
log and receipt in queue.json; the guard exits with its runner or after seven days.
