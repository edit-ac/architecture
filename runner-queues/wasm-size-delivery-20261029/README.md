# Wasm and package reduction delivery plan

Status: DESIGN PHASE QUEUED — source 01 follows terminal recovery in the existing
single-main runner, under the user's 29 October 2026 queue request. Sources 02–05
remain pending their explicit adoption/authority gates. Source 06 qualification
is excluded under the user's current no-qualification instruction. No tuning
allowance or package/Markdown design adoption is inferred from queueing.

The [investigation](../../research/wasm-size-delivery-investigation-20261029.md)
binds current artifacts and ranks the opportunities. This plan breaks the work
into **21 parents across six focused files**, generally 15–45 minutes each,
including local checks. Each parent has a deliverable, bounded context, affected
paths, prerequisites, implementation, validation, acceptance and interrupted-work
handoff. All implementation checkboxes start unchecked.

The principal target is actual code/data removal: the current engine is 759,022,
highlighting 1,285,730 and Markdown 585,582 canonical gzip bytes. Default Task
still needs 323,888 total / 56,168 JS bytes removed; expanded needs 1,817,022
total / 101,438 JS bytes removed. Shipping fixture files separately can remove
2,714,508 known unpacked bytes from the core npm archive, but its compressed
saving is unmeasured and it does not reduce browser delivery.

## Ordered delivery plan and admitted queue

This is a controller index, not a worker input or live runner queue. Give a worker
one file and its separate progress file, then one ready parent. Progress paths use
the prefix `.roadmap-runner/wasm-size-delivery-20261029/` at the workspace root.
The [manifest](manifest.json) records exact paths, local prerequisites and entry
conditions. The [admitted queue](queue-spec.json) currently contains only source
01; the runtime queue preserves terminal recovery first. The remaining files are
the pending delivery plan, not automatically dispatched work.

| Order | Focused source | Parents | Outcome | Progress suffix |
| --- | --- | ---: | --- | --- |
| 1 | [Baseline and decisions](01-baseline-and-decisions.md) | 3 | Reused baseline, explicit experiment protocol, concrete package and Markdown proposals | `01-baseline-and-decisions.progress.md` |
| 2 | [Package and production link](02-package-and-production-link.md) | 3 | Adopted fixture distribution; one verified shipping LTO policy | `02-package-and-production-link.progress.md` |
| 3 | [Highlighting grammar](03-highlighting-grammar.md) | 3 | Pinned transitive source closure, deterministic generator, production subset | `03-highlighting-grammar.progress.md` |
| 4 | [Markdown data boundary](04-markdown-data-boundary.md) | 4 | Pure codec helpers, kernel projections, atomic adapter cutover, removed restoration roots | `04-markdown-data-boundary.progress.md` |
| 5 | [Core and browser sharing](05-core-and-browser-sharing.md) | 5 | Shared JS helpers, one Math import candidate, attributed Rust sharing, one JS dispatch consolidation | `05-core-and-browser-sharing.progress.md` |
| 6 | [Final verification](06-final-verification.md) | 3 | Remaining semantic coverage, packed delivery, final unchanged cap checks | `06-final-verification.progress.md` |

Order is a preference except for the explicit dependencies below. A serial queue
cannot jump a blocked file: before dispatch, the controller includes only admitted
work and puts independent work before a branch awaiting adoption/authority. Do not
enqueue this whole draft as if all its gates were satisfied. Final testing follows
all functional work selected for the adopted delivery scope; rejected candidates
do not count as implemented reductions. Required but deferred work stays open.

## True dependencies and adoption gates

- WSD-1.1 binds every measured candidate to a valid baseline, authority ledger and
  regression protocol. Existing authority is zero candidate seconds; this request
  grants research/roadmap work only. Per-task time estimates do not replenish it.
- WSD-1.2's concrete package proposal must be adopted before WSD-2.1. One atomic
  migration keeps declared production/test-support imports coherent.
- WSD-2.2 must pass before WSD-2.3. All companion LTO changes are part of the same
  recorded hypothesis; applying it to another crate does not reset the clock.
- WSD-3.1 → WSD-3.2 → WSD-3.3. Source/license analysis is independent of LTO;
  generator and production comparisons require candidate authority.
- WSD-1.3's exact Markdown schema must be explicitly adopted before
  WSD-4.1 → WSD-4.2 → WSD-4.3 → WSD-4.4. Pure extraction and private kernel
  preparation precede one atomic public cutover. No worker invents another wire
  contract to unblock itself.
- WSD-5.1, WSD-5.2, WSD-5.3 and WSD-5.5 are independent candidates;
  WSD-5.4 depends on WSD-5.3's concrete retained-body design. Lack of Markdown
  adoption does not block this file. Available experiment authority determines
  which candidates may actually execute; this is not an authorized settings sweep.
- WSD-6.1 and WSD-6.2 consume all adopted functional changes and their evidence;
  WSD-6.3 depends on both. Missing performance inputs block candidate adoption or
  final claims, not independent contract design.

## Priority, stopping rules and unresolved decisions

First reuse the existing receipts and prepare the two concrete boundary proposals.
For the next explicitly authorized compiler experiment, prefer effective LTO over
another optimizer flag sweep. For structural work, highlighting data and Markdown
restoration are the largest identified optional costs. Start browser deduplication
with the proven catalog/composition overlap, then reassess; do not assume it closes
the much larger baseline JS gap. npm packaging is a separate install-size win.

No candidate has a promised percentage. Preserve the same features and consumers;
compare the whole required union, not only the improved file. Stop on a semantic,
ABI, feature, raw/gzip no-growth or bound runtime failure. Do not adopt a marginal
size change with missing regression evidence. If the limit remains unmet, record
the measured gap and next specific design need; never extend tuning automatically.

Pending decisions are explicit: available tuning scope/time, fixture distribution
layout, and the inert Markdown request/result schema. This roadmap does not adopt
them. The later worker must use a concrete accepted design, not ask a small model
to redesign packaging or the document boundary in the middle of implementation.
Any task that cannot fit its file/symbol/time boundary returns a proposed split
before expanding. Controllers preserve original unchecked acceptance throughout.

## Existing owner reconciliation

This decomposition is not authority to rewrite running WEX sources or
mark their unfinished tasks complete. At a safe future adoption checkpoint, the
controller records the one-to-one requirement handoff below and dispatches only
one implementation owner. Historical WEX progress, failures and exclusions remain.

| Requirement | Proposed delivery | Canonical consumer/owner |
| --- | --- | --- |
| Current receipt/build-control reuse | WSD-1.1 | WEX-9.1; do not repeat its completed audit |
| Fixture-free production package | WSD-1.2, WSD-2.1 | New packaging scope; existing package/export contract |
| Effective shipping LTO | WSD-2.2–2.3 | WEX-3.1/3.2; WEX-9.1 compiler proof |
| Required grammar closure | WSD-3.1–3.3 | WEX-6.2 and RCH behavior |
| Markdown proposal/adoption | WSD-1.3 | WEX-6.3 |
| Remove codec restoration | WSD-4.1–4.4 | WEX-6.4 |
| Browser/prebundle/Math sharing | WSD-5.1–5.2, WSD-5.5 | WEX-6.5 |
| Ordinary retained Rust investigation/refactor | WSD-5.3–5.4 | Newly requested WSD scope; **not** WEX-7.1/WEX-8.1 |
| Semantic preservation and missing runtime observations | WSD-6.1 | WEX-4.1, WEX-5.2/5.3 |
| Packed consumers, HTTP assets and identities | WSD-6.2 | WEX-4.2/4.3; reuse completed WEX-3.3 proof where valid |
| Required unions, hard caps and readiness reconciliation | WSD-6.3 | WEX-4.2/4.3, FIT and QPF |

WEX-7.1 and WEX-8.1 stay excluded. This investigation uses ordinary source/artifact
analysis, not the Deep Review skill; no missing skill is introduced as a new gate.
Completed highlighting producer alignment, stripping, HTTP compression and glue
sharing are reused rather than scheduled as new reductions.

## Verification ownership and completion

Focused existing checks belong to their functional parent. Source 06 alone owns
new comprehensive coverage and cross-file qualification. Its gap matrix assigns
each invariant one owner and reuses unchanged tests; entering a new file does not
justify another full suite. Output stays ignored and task-owned. No paid providers,
credentials, native qualification, release publication or deployment are included.

The final report must show npm archive and unpacked size separately from browser
raw/gzip/Brotli, initial/deferred and combined resource union. Actual default Task
must meet 524,288 total / 32,768 JS gzip bytes; the frozen expanded document must
meet 1,048,576 total / 131,072 JS. Unknown, skipped or over-budget cells remain
open. This plan cannot manufacture cap closure by shrinking the feature set,
moving bytes to required lazy files, applying Brotli numbers to gzip caps, or
relabeling a consumer. Required OS/backend gates keep their original owners.

Execution uses the existing single-main guarded controller only, after safe
source ownership and entry conditions are established. The original authoring
task did not stop, resume, enqueue or alter it. The later user queue request admits
source 01 after terminal recovery, without admitting gated implementation or
qualification sources.
