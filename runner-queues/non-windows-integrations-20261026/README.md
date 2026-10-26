# Continue integrations without Windows

The user requested deferring Windows-dependent work and continuing integrations on
2026-10-26. This controller selection supersedes the stopped integration run
`40dbc63346f0611067cef7d6`; the editor lane remains independent.

The [selection manifest](manifest.json) references the unchanged
[dependency-closed plan](../dependency-closed-ui-20261025/manifest.json). Its 65
source/progress pairs and 270 parent contracts remain required. The selection
retains 31 completed sources, schedules 21 unfinished non-Windows sources containing
78 parents, and defers 13 sources. Completed tasks and receipts are reused after
checking their applicable inputs; they are never redispatched solely for this
transition.

The continuation starts with the C/C++ ownership and binding contracts, then keeps
the existing prerequisite order for Linux input, native UI contracts, Apple,
Android, desktop shells, React Native, Expo and Flutter. The completed Linux host
setup is retained as an accepted input rather than run again. Windows references
in an export map or unsupported-platform feasibility decision do not authorize
Windows runtime work or establish Windows support.

Five Windows sources remain deferred: host readiness, native input, break routing,
bindings and WinUI presentation. The packaging/support source depends on that
branch and remains deferred as a whole. Seven final verification/support sources
retain the original requirement that all selected functionality is delivered
before comprehensive qualification. Their acceptance and open checkboxes remain
unchanged. Completing this continuation cannot claim full integration, Windows,
packaging, release or final qualification.

The original Windows failure evidence and progress remain intact. Resume the
Windows branch only after explicit scope resumption and changed host setup:
completed first-run/account provisioning, working SSH and an unlocked QA desktop,
followed by real toolchain and native bootstrap proof. A skipped prerequisite never
unlocks its dependents. The manifest records the exact resume condition for every
deferred source.

Launch only through `architecture/scripts/guarded-roadmap-runner.py`. Pass
`runtime.initial.source` and its original progress path as the first entry;
[queue-spec.json](queue-spec.json) contains only the remaining 20 FIFO entries.
Retain Codex, gpt-6.1-sol, medium effort, a 50-minute worker timeout, notifications
off, no sleep inhibition and source-checkbox tracking. Stop before resolver
dispatch on a blocked worker and require a live guard receipt. Do not edit
runner-owned state, snapshots, task requirements or progress to reorder work.

Run the existing execution-queue validator against the basis and its reordered
effective graph. The inherited basis currently reports stale requirement metadata
for completed UDM-1.9: its completed table-rectangle repair receipt was added after
the basis was pinned, and narrative self-references are parsed as dependencies.
Preserve and report that diagnostic rather than rewriting completed source or
claiming a full-plan pass. UDM-1.9 is outside the transitive prerequisites of all
78 runnable parents. Any different error, or an error in a runnable contract,
blocks launch.

Before launch, independently verify every runnable task's declared dependencies,
the full mapped prerequisite order, exact source/progress partitioning, all
predecessor pairs, completed prerequisite checkmarks, unchanged source bytes, the
queue-spec tail and exclusion of deferred sources. Keep generated checks and
runtime receipts in ignored root
`.roadmap-runner/non-windows-integrations-20261026/`.

One integration runner owns the root workspace. Preserve the active editor lane,
all unrelated dirty work and the existing shared integration lock/checkpoints.
No paid product inference, secret loading, new providers, publication, push or
deployment is authorized.
