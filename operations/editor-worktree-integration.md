# Periodic editor integration into local main

User authorization, 2026-10-26: update both existing runners to merge validated
editor deliveries into local main periodically. This policy supersedes older
indefinite source-landing deferrals and blanket cross-lane pause prohibitions only
at the safe integration checkpoints described here. It does not authorize edits to
an active worker's inputs, blanket staging, resets, stashes, publication or push.

PRIMARY is `/Users/bpstr/Github/edit-ac`, on the existing local `main` branches of
`architecture`, `core`, `cli` and `docs`. EDITOR is the existing
`/Users/bpstr/Github/edit-ac-editor-20261026` workspace. Resolve current branches,
heads, runner successors and guard receipts each time; old run IDs are historical.
The shared authority is PRIMARY `.roadmap-coordination/parallel-clients.md` and its
`integration.lock`, including when accessed through EDITOR's coordination link.

## Cadence and ownership

EDITOR queues its validated delivery after every two completed parents and at
each source boundary, before starting another parent. PRIMARY checks and lands
ready deliveries in its next completed-parent integration phase, before the next parent.
Both lanes check again at roadmap boundaries and before ending. An hourly follow-up
in the current controller chat reconciles missed deliveries; it does not start a
second roadmap controller or interrupt live work. No changes means no merge and no
repeated notification.

EDITOR owns preparation of authentic editor deltas and eventual synchronization
from main. PRIMARY owns landing into the main checkout and its inherited source
closure. The follow-up coordinates either lane only when a checkpoint pause is
necessary. A merge may not modify inputs that another worker is editing or testing.
The owning PRIMARY worker may land after its own bounded parent/check phase is
complete; an outside coordinator must wait for worker exit and pause dispatch.
Committed editor changes may be read while EDITOR works, but its checkout is not changed by
PRIMARY; main changes enter EDITOR only at EDITOR's own safe checkpoint.

## Queue a delivery

Under the shared lock, record a compact request in ignored PRIMARY
`.roadmap-coordination/deliveries/` and append its pointer to the shared ledger.
Include repository, editor branch/head, main head, completed task IDs, exact owned
commits or authenticated launch/entry-relative patches, affected paths, required
source closure, and current passing check receipts with source/artifact pins.
Record the exact accepted base and any mixed inherited paths. Commit only validated
owned source when it is safely separable; keep mixed assemblies unstaged with
authenticated patches. Generated manifests, logs, caches and proof remain ignored.

A request is `pending-authentication` until its ownership, dependency closure and
proof are checked. A branch being ahead, a checkbox, a source review or an exit-zero
scheduling boundary does not establish a mergeable product delivery. Include
already pending validated work in the next request; do not count only work produced
since the last monitor. Preserve all old task/progress pairs and failure evidence.

## Land at a safe PRIMARY checkpoint

1. Finish the owning worker's current bounded implementation/check/cleanup phase,
   or wait for that worker to exit when acting as an outside coordinator. Record
   its handoff and retain its WIP. If a managed controller must pause, request its
   stop immediately after a successful worker checkpoint through the supported CLI;
   preserve every unfinished queue/source/progress pair. Never interrupt an active
   test or source edit to create a merge window. Do not hold the integration lock
   while waiting for a worker.
2. Acquire the shared lock. Revalidate exact run ownership, branches/heads, dirty
   paths, staged contents and delivery input pins. Record hashes of all unrelated
   dirty files and the staged patch before mutation. A lock alone does not prove
   that a worker is idle. Exclude generated artifacts and source snapshots.
3. Prefer a coherent validated commit/cherry-pick unit. Never merge the entire
   dirty editor worktree or blindly stage whole shared files. If the selected unit
   depends on inherited PRIMARY assembly, authenticate that source closure against
   its existing owner receipts and resolve it as part of this bounded landing.
   Prepare/test a merge in an isolated integration worktree if needed, with only
   the exact required authored inputs; preserve and later clean that worktree.
4. Reuse proof only for matching relevant inputs. Run the smallest affected local
   compiler/fixture/consumer checks for the assembled unit and actual conflicts.
   Changed merge inputs justify rechecking the affected boundary; a new checkpoint
   alone does not justify a broad suite. All automated provider cases remain mocked.
   Deferred OS qualification, hard caps and full final acceptance remain unchanged.
5. Land only the tested closed unit into local main. Keep unrelated dirty bytes
   and staged contents byte-identical; verify this afterwards. Do not use blind
   stash/reset, force movement of checked-out branches, broad checkout/restore or
   whole-file copies that erase nonowned changes. A conflicting or unqualified
   hunk stays pending with its exact owner and resume condition.
6. Record original editor commit/patch IDs, resulting main commits, check selectors
   and results, preserved-path/index checks, and any remaining conflict in the
   ignored delivery record and shared ledger. Mark that exact unit integrated so
   later checkpoints do not cherry-pick or revalidate it again. An already present
   change needs an authenticated equivalence disposition, not a duplicate commit.

## Synchronize EDITOR and continue

At EDITOR's next completed-worker checkpoint, reconcile its branch with the landed
main commits under the shared lock. Keep all unrelated or unfinished editor bytes
and staged work intact. Use a normal merge/fast-forward only when its dirty-path
analysis proves it safe; otherwise prepare the exact conflict resolution separately
and verify the affected boundary before changing EDITOR. Do not force-reset the
editor branch or feed it a source snapshot. Record synchronized heads and pending
conflicts. Continue independent work when synchronization of an unrelated unit is
blocked.

If a runner was paused, resume only through
`architecture/scripts/guarded-roadmap-runner.py` with a live readiness receipt,
the current ordered unfinished queue, original progress paths and the concrete
changed-input/landing receipt. Reuse completed sources and never restore an older
superseded FIFO or clear deferral memory manually. Do not start a duplicate worker.

## Blockers and follow-up

The hourly follow-up reads the latest delivery ledger, runner/guard states and
current heads. It actively lands eligible tested units or prepares a concrete
source-closure/conflict repair at a safe checkpoint. An old inherited-assembly
gate is not a permanent waiver of this responsibility. If proof is missing, name
the exact changed input and minimal owning revalidation instead of committing
unvalidated bytes.

Fingerprint each blocker by repository, source/main revisions, paths, error and
missing prerequisite, with owner, attempted repair and exact resume condition.
After an unchanged failed attempt, do not retry a worker, merge, test or notify
again without changed input or a concrete new repair hypothesis. Preserve the
request, continue independent work, and report a changed blocker once. Keep active
previews/services, credentials, data and the integration OS deferral protected.

When both runners have ended and all authenticated deliveries are integrated,
disable the hourly follow-up. If only externally blocked work remains, report
once and disable the unchanged follow-up loop until the user or an external change
provides the recorded resume condition. Report newly landed/synchronized commits
and meaningful changed blockers, rather than unchanged heartbeat summaries.
