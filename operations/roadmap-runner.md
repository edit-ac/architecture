# Run a guarded development roadmap

Use one serial runner in the root workspace containing `core`, `architecture`, `cli` and `docs`, on the existing main branches. The installed managed CLI observed on 2026-10-25 is Roadmap Runner 0.11.0. Check the selected tracking mode and actual worker context; the version alone does not establish whether task state lives in source checkboxes or separate progress. The current managed queue uses source checkboxes with separate evidence/progress, while requirements remain read-only. The package-pinned 0.8.0 contract validator remains a pure local validation dependency; it does not select the runtime executable.

## Validation and toolchains

In architecture, run `npm run check`. This validates the task contract, canonical roadmap coverage and manifest dependencies; it does not establish runtime acceptance. Cross-file prerequisites belong in bounded entry conditions, while each task's Dependencies names only local tasks. Validate queue source hashes, parent counts, progress isolation and requirement ownership after controller amendments. Run the loop safety tests with `python3 -m unittest discover -s tests -p test_roadmap_recovery_guard.py`.

Use the core-pinned Node 24.19.0/npm 11.17.0 for product checks and the pinned rustup compiler for target builds. Resolve the actual runner executable before starting: this Mac currently uses `/Users/bpstr/.nvm/versions/node/v24.21.0/bin/roadmap-runner`. Do not assume an older Homebrew path or version exists.

## Start and resume

Every new start or changed-input resume uses the guarded launcher. Pass the existing ordered FIFO with repeated `--queue`; preserve completed entries and their receipts instead of re-running them. Check the coordination ledger and the existing runner status before starting. A live worker must not be duplicated or have its source overwritten.

```sh
python3 /path/to/edit-ac/architecture/scripts/guarded-roadmap-runner.py \
  --cli /absolute/path/to/roadmap-runner \
  start /path/to/edit-ac/architecture/roadmaps/TRACK.md \
  --workspace /path/to/edit-ac \
  --progress-file /path/to/edit-ac/.roadmap-runner/TRACK/progress.md \
  --client codex --timeout 90m --supervisor-every 2 \
  --supervisor-timeout 10m --notify off --no-prevent-sleep \
  --idempotency-key UNIQUE_DELIVERY_ID --json
```

The launcher passes the runner's options through and returns its JSON plus `loopGuard`. It verifies the guard's live PID and readiness receipt. If the guard cannot arm, it requests a stop for that exact run ID/workspace and fails visibly. It never restarts a stopped runner. The timeout bounds one worker, not total execution cost. Automated product/provider validation remains deterministic and mocked; no paid synthetic inference or secret loading is authorized.

To attach protection to an existing run without starting a worker or modifying its queue:

```sh
python3 /path/to/edit-ac/architecture/scripts/guarded-roadmap-runner.py \
  --cli /absolute/path/to/roadmap-runner \
  attach RUN_ID --workspace /path/to/edit-ac --json
```

## Loop detection and handoff

The guard stops the exact managed run on a BLOCKED worker, or after two distinct successful workers repeat the same completed source contract. It catches the original failure even when a `Current delivery` paragraph changes a source hash each pass. Duplicate events, other run IDs, interrupted/failed workers, real acceptance changes and advancement to a different source do not count as this loop. An invalid/truncated event stream or the guard's seven-day monitoring deadline also requests a stop rather than leaving an unprotected controller.

The guard watches the managed run's `artifacts.events` stream, which follows every FIFO source and distinguishes `runner.roadmap_completed` from run completion. Never attach it to a progress-side per-roadmap event file. Guard receipts and logs live under ignored `.roadmap-runner/guards/`. A stop records its reason, iteration, source, CLI response and changed-input resume condition. Preserve source, progress, dirty code, original data and exact failure evidence. Never restart unchanged blockers or a detected loop. Correct the cause, validate the repair, then resume from the next genuinely ready task through the guarded launcher.

Acceptance text stays controller-owned. In the current source-checkbox tracking mode, workers update only verified source checkboxes and the `Status:` line. Store delivery summaries, source hashes, reconciliation notes, counts and timestamps in separate progress/ignored receipts. Never write a self-referential `Current delivery` paragraph into source: the runner treats that prose as a new requirement revision. A COMPLETE label still needs applicable passing evidence; missing commands, zero cases and required skips cannot pass.

Use `roadmap-runner status RUN_ID --workspace ROOT --json` to inspect and `roadmap-runner stop RUN_ID --workspace ROOT --json` to stop. Physical-device qualification is deferred; declared simulator/emulator/OS-host proof, full functional suites and unchanged performance gates remain required. Publication, push and deployment remain separately controlled by the user's instructions.

## Current format and bounded optimization

Before first publication, apply [decision 006](../decisions/006-single-format-before-publication.md) and the [durability contract](../specs/document-durability.md). Do not preserve executable old document profiles or synthetic previous/current package matrices just because an old task named them. Preserve useful behavior assertions in current-format tests and independent historical fixture oracles. The single root-workspace queue must put the canonical cutover and focused safety gate first, then independent feature work, then remaining optimization and full suites. One optimization batch is at most 45 minutes or two different measured repair hypotheses; checkpoint and move on when the budget ends. Hard size/resource gates remain required before final readiness/publication.

## Validate dependency closure before replacing a queue

Run `npm run validate:execution-queue -- runner-queues/dependency-closed-ui-20261025/manifest.json` and `npm run test:execution-queue` for the current [dependency-closed UI queue](../runner-queues/dependency-closed-ui-20261025/README.md). Contract syntax and a live guard do not prove prerequisite availability. The validator checks actual task owners, receipt paths, cycles, prerequisite order, preserved original tasks/pairs, runtime status headers and functional-before-verification phase order. Its requirement pins ignore verified checkbox and Status changes only. Toolchain installation is explicit implementation work; missing user-supplied Windows host/license input remains a real gate and must never be represented as a prepared-fixture pass.

The CLI queue operation appends; it does not insert or replace pending entries. Prepare and validate a replacement plan separately. Stop the exact run at a completed worker checkpoint, preserve its source/progress/dirty work and all completed evidence, then start the successor through the guarded launcher and verify every source/progress pair. Do not modify runner-owned state or snapshots to reorder work.

## Focused runtime delivery checks

Follow the current queue’s [delivery-check policy](../runner-queues/dependency-closed-ui-20261025/delivery-check-policy.md). Functional-before-final-verification ordering permits each parent’s explicitly required narrow runtime observation and minimal wrapper. It does not permit replacing actual behavior with source inspection, or moving comprehensive matrices and qualification into implementation. Resolve phase-only blockers with explicit controller authority and changed source pins; retain original acceptance and compatible passing evidence.

## Periodic editor integration

The user authorized periodic local-main integration on2026-10-26. Follow [the delivery/landing procedure](editor-worktree-integration.md): EDITOR queues validated source after two completed parents and at source boundaries; PRIMARY lands eligible closed units in its next completed-parent integration phase, preserving unrelated dirty work/indexes. An outside coordinator waits for a successful worker exit before pausing dispatch and landing. EDITOR syncs from main at its own checkpoint. Both lanes check outstanding deliveries before continuing or ending; the hourly follow-up reconciles missed checkpoints. Old inherited source-closure gates require a concrete authenticated repair, not indefinite parking or unchanged retries. Native OS deferrals, existing qualification/caps, mocked-only checks and no publication/push remain unchanged.
