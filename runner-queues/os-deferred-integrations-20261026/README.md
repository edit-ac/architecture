# Finish integrations while OS checks are deferred

The user's 2026-10-26 instruction defers all native OS checks and authorizes
completion of the remaining independent integration roadmap work. This selection
supersedes stopped PRIMARY run `9cdfb7a64b6787268ab4fe0d`. The independent editor
lane remains unchanged.

[manifest.json](manifest.json) partitions all 270 parents in the unchanged
[basis plan](../dependency-closed-ui-20261025/manifest.json): 137 already accepted,
19 selected, and 114 deferred. The selected set is maximal under the existing
dependency graph after excluding native OS checks. No task depends on a deferred
prerequisite. The 29 direct OS gates and their 85 dependent parents stay unchecked;
their original sources, progress, failed evidence and full acceptance remain intact.

## Ordered execution

| Source | Selected outcome | Parents |
| --- | --- | ---: |
| [01](01-native-ui-contracts.md) | Native command, theme/state, overlay and export contracts | 4 |
| [02](02-web-package-exports.md) | Web exports, CSS/types and peer manifests | 1 |
| [03](03-desktop-feasibility.md) | Flutter/RN desktop API feasibility and explicit gaps | 1 |
| [04](04-swift-headless-facade.md) | Headless Swift storage/authority facade | 1 |
| [05](05-kotlin-headless-facade.md) | Headless Kotlin storage/authority facade | 1 |
| [06](06-dart-toolchain.md) | Local Dart/Flutter compiler profile | 1 |
| [07](07-dart-authority-client.md) | Portable Dart authority client | 1 |
| [08](08-backend-final-cases.md) | Backend parity, transactions, retries, security and transitions | 6 |
| [09](09-web-host-final-cases.md) | Host case ownership, browser integrations and resource teardown | 3 |

All ten environment/functional parents precede the nine backend/web verification
parents. The phase barrier covers this explicitly selected scope. Deferring native
work does not imply its completion or qualify a native target. Browser and backend
checks retain their actual runtime, nonzero-case and failure-reporting requirements.

Guest/VM operations, native target bootstrap, simulator/device qualification,
native UI/IME and native desktop-shell execution are excluded. Local builds,
headless Swift/Kotlin/Dart consumers, Node/PHP/SQLite, schema checks and browser
fixtures are allowed. Flutter/Dart doctor/compiler metadata may describe available
or missing host capabilities; it must not launch a native target or present that
inspection as OS qualification. The broader basis scope still leaves unselected
databases/languages outstanding. No provider spending, secret loading, publication,
push, deployment or VM ownership changes are authorized.

## Contract ownership and preservation

The selected extracts are the current execution owners of the original stable
task IDs. They preserve every implementation and acceptance clause, with only
source/progress links adapted to their current owners. The original broad sources
remain read-only historical owners; do not dispatch them in parallel or infer that
their full milestones are complete. Current acceptance is read from this manifest's
task owners and their verified progress. This separates web packaging from native
packaging, and headless facades from UI/runtime tasks, without passing a skipped
prerequisite or duplicating implementation.

Validation must prove exact task-body equivalence after link relocation, unique
ownership and progress paths, declared dependency coverage and order, existing
prerequisite checkmarks/receipts, functional-before-verification order, complete
270-parent coverage and unchanged original source bytes. The inherited full basis
has stale completed UDM-1.9 metadata diagnostics; retain them separately. That parent
is outside the selected prerequisite closure, and its issue is not a full-plan pass.

Start through `architecture/scripts/guarded-roadmap-runner.py`, using the first
source/progress in the manifest and [queue-spec.json](queue-spec.json) for the other
eight entries. Retain Codex, gpt-6.1-sol, medium effort, 50-minute workers,
notifications off and no sleep inhibition. Require a live guard, stop before
resolver dispatch on BLOCKED, and never restart unchanged input. Preserve the
stopped predecessor, both indexes, unrelated dirty work and the active editor lane.
Use the shared integration lock for two-parent/source checkpoints. Keep generated
checks, patches and runtime receipts in ignored root
`.roadmap-runner/os-deferred-integrations-20261026/`.
