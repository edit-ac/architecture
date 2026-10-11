# Run a bounded development roadmap

Verified against `@bpstr/roadmap-runner` 0.8.0 and its `write-runner-roadmap` task contract. This guide does not start a runner. The checked-in package uses the runner's pure contract validator, without model calls.

## Validation

In architecture, run `npm ci --ignore-scripts` then `npm run check`. The script validates the official task contract plus file coverage, IDs, status header and cross-roadmap manifest DAG. For an already-built runner checkout, use `node scripts/validate-roadmaps.mjs --runner-contract /absolute/path/to/roadmap-runner/dist/roadmap-contract.js`.

The validator cannot establish that code, evidence or human acceptance is correct. Each roadmap's first task checks its upstream gate; all later tasks name exact local prerequisites. Cross-file dependencies do not belong in a task's Dependencies field because the runner resolves only IDs in the same source file.

## Local toolchain selection

Use Node 24.19.0/npm 11.17.0 for the core scaffold; select it explicitly with the installed version manager before npm commands. This Mac also has Node 26, which correctly fails the core engine-strict check. Use the pinned rustup 1.97.1 compiler for target-specific builds: a Homebrew cargo/rustc can bypass the target installed under rustup. The dependency probe README records an explicit compiler selection command. A successful native build does not prove the browser target exists.

## Start one track

Replace `/path/to/edit-ac` with the parent directory containing `core`, `architecture`, `cli` and `docs`. Ensure upstream tracks are COMPLETE at the current source revision with reproducible passing evidence. Native/CLI are independent branches; they do not gate web release.

```sh
roadmap-runner /path/to/edit-ac/architecture/roadmaps/01-foundation.md \
  --workspace /path/to/edit-ac/core \
  --progress-file /path/to/edit-ac/architecture/progress/01-foundation.md \
  --client codex --timeout 45m
```

For CLI use `--workspace /path/to/edit-ac/cli`; for public documentation use `--workspace /path/to/edit-ac/docs`. Sources and progress use distinct absolute paths. One runner per workspace/progress file; isolated worktrees require an explicitly coordinated integration plan. The model must be one actually available in the selected client; specify `--model` only after choosing it. A smaller model should read the task context and complete one parent, not expand the entire product in one iteration.

`--timeout 45m` bounds an individual worker, not total runtime or total inference cost. Runner execution uses the selected client's configured model access; this planning task did not authorize unattended runs. The prohibition on paid synthetic AI testing still applies to all implementation validation.

Runner 0.8.0 rejects managed `start` when source/progress paths are outside the authorized workspace, as they are in this sibling-directory layout. The foreground command above supports those paths and still registers a run ID for `status`/`stop`. Keep its terminal open, or use an owned detached launcher with redirected output and verify readiness through `status`.

Select the verified executable explicitly after changing Node PATH. On this Mac `/opt/homebrew/bin/roadmap-runner` is 0.8.0, while the Node 24 bin directory also contains 0.7.0. The foundation run used `--model gpt-6.1-sol --effort medium`. Completion lives in progress at the recorded source revision; preserved source checkboxes are not the completion record.

## Control and handoff

```sh
roadmap-runner status RUN_ID --workspace /path/to/edit-ac/core --json
roadmap-runner stop RUN_ID --workspace /path/to/edit-ac/core
```

Source roadmaps are controller-owned. The worker writes checked steps, exact results/counts, artifact paths and the next precise action to its separate progress file. BLOCKED, SKIPPED, NEEDS_INFO and PROBLEM stay unchecked with an owner/unblock condition/retry trigger. Skipped prerequisites do not unlock dependents. BLOCKED is nonterminal and can cause retries: do not launch a track with an unavailable entry gate; stop the controller run when no ready work remains.

Each task adds its named checks before invoking them. A missing command/file or zero matched Rust tests is not a pass. Manual device qualification remains incomplete until actual device evidence exists. COMPLETE is a worker assertion requiring evidence review, not independent proof.

Publish only after the explicit final browser release task's gates. Routine implementation tasks cannot enable npm publication, deploy the test relay, run paid inference or rewrite acceptance to clear a blocker.
