# Retained structural history over a document lifetime

Authority: DRA-1.4, [document durability](document-durability.md),
[schema-v5](schema-v5.md), [table merge](table-merge.md), and
[decision 006](../decisions/006-single-format-before-publication.md).
This is an authored design. DRA-1.5 implements it; design checks do not prove
production replay, storage recovery, performance, or alpha readiness.

## Decision and compatibility

Use **lossless retained records with bounded indexed replay**. Keep the existing
witnessed v5 identity, roots, tuple shapes, source item identities, operation IDs,
controls, and original placement records. Do not compact, checkpoint away, rewrite,
or rebase semantic records. A checkpoint encodes the complete retained Yrs state,
including losing assignments and deleted structs (`skip_gc: true`). Browser journal
rollover removes redundant recovery payloads, not document history. Receipt of an
update conveys neither peer retirement nor permission to remove its intentions.

Replace the 4096-operation, 8192-control/derived-span, and 128-operation-ancestry
ceilings with accounting against the admitted state and bounded replay algorithm
below. The 128 **container nesting** limit remains: nesting and causal age are
different dimensions. Keep the 4096 original source/container registration limit,
per-source text limits and all final memory/latency/bundle caps. A modest document
may have a long causal chain with few visible owners. Neither a deeply dependent
split nor another move consumes a fixed remaining lifetime allowance.

This is not unlimited storage. Every retained byte/value/struct consumes capacity,
even if hidden or disabled. A document can exhaust the unchanged 16 MiB admission
budget or another actual resource budget. Refuse the proposed mutation explicitly,
preserve its input and the existing document, and allow export/recovery from the
last admitted state. Never claim that a larger counter alone resolves lifetime.
The mandatory 16384-operation fixtures must fit the existing budgets; if they do
not, DRA-1.5 remains open and the representation decision must return to review.

There is no persisted layout change and no real-data converter required by this
algorithm. Existing admissible same-format states retain their exact semantics.
This authorizes no incompatible reinterpretation, automatic migration or relabel.
Any future compaction needs a separate reviewed format decision with proof of
eligibility, covered state, old-update admission and crash-safe publication. In
particular, a state vector, checkpoint, elapsed time, disconnected peer or absent
peer list is insufficient evidence that a record is safe to collect.

## Replay algorithm

Let B be admitted encoded bytes, V bounded decoded values/structs, N retained
ownership operations, E distinct known dependency edges (at most four per
operation), M retained projected owners, S logical span segments, and T text.

1. Decode into disposable state, with aggregate resource accounting across the
   **merged state**, not just fresh records or individual journal entries. Validate
   all roots, immutable assignments (including losing/deleted assignments), tuple
   shapes, witnesses, source identities and references before publication. Preserve
   the existing distinction between a missing binary dependency (rejection) and a
   structurally dormant intention with a missing operation version (retained).
2. Build one operation-ID index and reverse dependency adjacency. Count each
   distinct known edge once. Use an iterative Kahn traversal: zero-known-indegree
   records enter a work queue; compute height as one plus the maximum known-parent
   height, and propagate missing/dormant status. Missing operation versions make
   descendants dormant, not deleted. A residual known cycle rejects, including a
   cycle on a dormant or disabled branch. Validate disabled/losing witnesses too.
3. Sort eligible records by **(height, numeric operation client, numeric clock)**,
   exactly the existing order. Queue visitation order must not change this order.
   Controls affect application, not dependency heights. Replay losing, disabled,
   dormant and applied outcomes under the existing qualification rules. Late
   records may precede earlier-seen records; replay the affected suffix, including
   descendants whose height/outcome changed. Never apply only the arriving suffix
   by arrival order or freeze a formerly winning intention.
   A control, tombstone, source-text deletion, newly resolved sticky cut, container
   change or late registration can invalidate earlier outcomes without adding an
   operation. Find the earliest affected rank and replay its entire suffix, or
   safely do a full cold replay. Attribute edits also invalidate derived effective
   presentation while leaving committed presentation witnesses unchanged.
4. Replace repeated owner-vector scans/shifts and full `normalize` walks per move
   with an owner-ID index and ordered parent/child sequences. Indexed preorder
   ranges must reproduce normalization after **each** applied placement, including
   deleted/disabled containers, root fallback, before-target versions, adjacency
   and initial deterministic cycle repair. Check actual containment depth/cycles
   separately. A data structure change cannot change the existing winner policy.
5. Represent replay spans as indexed segment sequences: rank/select by
   logical segment number, split and concatenate without copying an entire prefix
   after every split/join. Mutate only disposable staged trees; reclaim unreachable
   index nodes rather than retaining a tree snapshot for every historical record.
   Preserve empty segments, original source order, cut
   affinity and every segment boundary. Existing split records address a segment
   **index**, so silently coalescing adjacent same-source spans changes semantics.
   Materialize the exact ordered spans once for a requested view, bounded by the
   aggregate segment-node budget. Validate coverage with per-source sorted spans
   in one pass, rather than scanning every owner for every source.
   Index each source's text/mark runs once and slice by indexed UTF-16 interval;
   the current `slice_runs` walks a full text diff per segment. Empty retained
   segments must not trigger another full text walk. Preserve all marks and scalar
   boundaries while keeping total extraction O(T + S log(T + 1) + output runs).
6. Resolve presentation inheritance iteratively with explicit visiting/resolved
   states and memoized nearest explicit attributes. Detect cycles; do not recurse
   on the host stack or use `effective`'s current 128-step `unreachable!` fallback.
   Preserve immutable split/join witnesses independently of mutable effective
   attributes. Recompute affected inheritance when attributes/controls change.
7. Caches are disposable and revision-scoped. Key them to the admitted identity and
   complete integrated state (struct clocks **and deletion set**, plus relevant
   metadata/control/text changes), never a state vector alone. Missing/stale caches
   fall back to identical cold replay. A failed staged mutation changes neither
   the live cache nor document/history/receipt state. Never persist a second replay
   format or make a cache necessary to reopen a checkpoint.

Graph construction/ordering is O(N + E + N log N), inheritance O(M + N), and final
coverage O(S log S + T); indexed text extraction additionally costs
O(S log(T + 1) + output runs). Ordered owners and segment sequences must make each
applied replay edit O((D + 1) log(M + S + 1)), where D is actual containment depth
(at most 128), plus newly created nodes and text processing. Peak replay storage is
O(B + V + N + E + M + S + T). Charge traversal, comparisons and created segment
nodes; do not hide quadratic suffix copies or repeated whole-forest normalization
inside an uncharged helper. A cold restore may replay all N; it must not require
N passes over N dependencies or recurse through N ancestors. A late update can
invalidate all N records; that worst case is bounded cold work, not a reason to
discard it. Existing staging/encoding can still cost O(B) per admission. Warm
cache speed is optional for correctness; final QPF limits remain unproved until
measured on production code. Do not trade atomic validation for cache speed.

## Concrete admission and work limits

| Dimension | Policy |
| --- | --- |
| Restore corpus and resulting full checkpoint | At most 16777216 encoded bytes each; checked sums before allocation/application; duplicate input still counts toward corpus work. |
| Decoded state | At most 262144 structs and 262144 Any values, counted over the retained merged state as well as bounded per-input decoding. Losing/deleted CRDT payloads count. |
| JSON and tuple nesting | Maximum depth 32; existing 8192 entries per Any array/map, 1048576 decoded item length, and 2097152 generic varint allocation guard remain. These are not Y.Map root-entry or causal-depth limits. |
| Replay work | At most 16777216 charged work units over a candidate admission's replay phases; checked arithmetic. Include edges, ordering comparisons, containment traversal, inheritance, span/index allocation and materialization; repeated baseline/candidate projections share the admission budget. |
| Replay storage | At most 262144 simultaneously allocated segment/index nodes per candidate, including transient nodes; reserve/check before allocation and reclaim unreachable staged nodes. Cumulative allocation also consumes the work budget. Persisted values/structs remain separately counted. |
| Source geometry/text | At most 4096 original sources/containers; 262144 UTF-16 units per source and 1048576 aggregate UTF-8 source-text bytes. Preserve scalar boundaries. |
| Containers | At most 128 actual parent edges, independent of operation or inheritance chain length. |
| Table scope | Keep table-merge's 65536 events, 16384 named text roots, depth 32, 1 MiB per value/8 MiB JSON and 16 MiB text per table, and its visible geometry/command limits. Stricter whole-document budgets win. No table event/text GC. |
| Uncovered transport tail | WASM/browser 4096 entries; Session/CLI currently 4096 retained entries. This is separate from retained structural records. Publish qualified checkpoints before uncovered tails fill. |
| Storage/outbound quota | Existing adapter limits remain (Session default 64 MiB aggregate, 16 MiB record). Pending unsent updates and receipts have independent capacity, never inferred acknowledgements. |

The aggregate state counters must cover both checkpoint and journal unions, local
commands, remote apply, undo/redo, import and extension mutation. Per-frame checks
alone allow fragmented updates to evade a state limit. Work exhaustion returns
typed `ResourceLimit` before live mutation. Malformed shapes, cycles, missing
binary dependencies, incompatible witnesses and unsupported envelopes keep their
specific typed admission errors. Do not catch one and accept a partial document.
Negative tests assert exact prior checkpoint bytes, full observed revision,
history availability, pending receipts/outbox and recovery input bytes unchanged.
Bound the decoder's JSON path before allocation as well: the current `read_json`
delegation validates shape only after its inner read and must not bypass value,
depth or allocation accounting.

## Retained roots and consumers

The machine-readable review is [consumers.json](../fixtures/document-lifetime/consumers.json).
It identifies each source boundary and its required implementation/proof owner.
All eleven fixed roots plus the table text namespace are covered:

| Retained data | Lifetime treatment |
| --- | --- |
| `registry-parents`, `registry-placements`, `registry-owner-origins` | Immutable registrations/initial placement; never rewritten to a materialized current position. |
| `registry-texts` | Original nested text identities, deleted units, marks and dormant/absorbed text survive checkpoints and late edits. |
| `delete-probe-tombstones` | Permanent deletion evidence; hiding never collects text, descendants or operation versions. |
| `registry-ownership-ops` | All split/join/place records and complete immutable witnesses remain, including losing/disabled/dormant records. |
| `registry-block-attributes`, `registry-container-attributes`, `registry-list-item-attributes` | Known and bounded unknown values remain; inheritance is derived, not a rewrite. Losing CRDT assignments remain under skip_gc. |
| `registry-entity-controls` | Mutable reversible enabled state and retained CRDT history; disabling does not erase a target or dependency. |
| `registry-table-records`, `table-text/<tableId>/<rowId>/<columnId>/<blockId>` | Preserve births, hidden axes/blocks, losing events, controls, snapshots and every named cell text identity. The exact namespace validation is table-merge's, not an arbitrary-root wildcard. |

Stable anchors retain original source/item identity and UTF-16 affinity. Long
chains must resolve to the same visible location or explicit retained/deleted
resolution, including anchors in absorbed, hidden and unknown-feature content.
Projection indices and owner versions can change; they are never substituted for
anchor identity. Portable table cuts and external recovery carriers follow the
same rule. No unknown data becomes executable or editable by being retained.

Local selective undo has its existing bounded **session** window (default 100
groups, 8 MiB retained payload, 256 commits per group). Evicting a UI undo group
does not remove CRDT records, peer changes or durable review/history data. Reopen
currently starts a new local undo manager; this policy does not promise restoration
of an unserialized manager. Within a live session, retained pre-boundary undo/redo
groups must still work after later structural replay and checkpoint publication,
preserving unrelated peer edits. Explicit host-authored history/checkpoint records
and review proposals retain their original bytes and lineage. Observed revisions
include deletion state; a stale review must fail explicitly, never rebase itself
onto new source identities or appear current after a save/reopen. Capture retained
revision endpoints separately from cache invalidation keys.

`HistoryStore` is a separate on-demand immutable representation store, not that
undo manager or an automatically durable archive. Its explicit `RetentionPolicy`
bounds revision count and total bytes; rejected captures must not evict anything.
An explicitly evicted capture reads as `Unavailable(Pruned)`, never the current
document. Hosts own archival persistence and representation provenance. Native
review currently caps this store at 128 revisions/32 MiB. Test retained captures
within the configured policy across replay/publication, and test explicit eviction
separately. Neither a replay optimization nor journal publication may initiate
history eviction or rewrite a retained capture's scope/hash/content bytes.

## Offline replicas and crash-safe storage

There is no semantic retention boundary: the only boundary is publication of a
recovery checkpoint/cache generation. A peer disconnected before it can send old
same-epoch source edits and structural intentions afterwards. Merge those exact
bytes through normal staged admission; deliver missing binary prerequisites as a
bounded corpus. Retained structural conflicts use the existing outcome inventory;
never silently drop a losing or hidden edit. Unknown/future envelopes reject with
original bytes available. Duplicate/reordered complete corpora are idempotent.

Browser DRA-1.3 qualified latest/previous checkpoint plus uncovered-tail policy is
the model, not proof for Session/CLI. DRA-1.5 must distinguish their recovery journal
from pending outbound data and bounded receipt bookkeeping. Publish replacement
and fallback coverage atomically (SQLite transaction or file fsync/rename/directory
sync); prune only entries covered by **both** retained recovery candidates, after
durable publication. Never remove an unacknowledged outbound payload. Bound receipt
deduplication without forgetting acknowledgements that pending entries require;
retain monotone scoped publication/receipt watermarks or equivalent exact coverage.
Existing store-version/receipt contracts require explicit review before changing
their encoding; no second document format is implied. A quota refusal is acceptable
only before mutation and with existing bytes intact, not after an accepted edit.

An indefinitely disconnected writer can fill the independent outbound quota even
while the complete checkpoint fits. Surface explicit capacity/backpressure; do not
erase its unsent edits, simulate remote receipts or turn checkpoint success into
a network acknowledgement. Long-session tests use actual prepared peer receipts
where needed to keep this independent capacity available, plus a separate
unacknowledged-preservation case. None authorizes a live external service.

## Deterministic fixtures and implementation exit

[cases.json](../fixtures/document-lifetime/cases.json) specifies schedules,
expected results and malformed/resource cases before implementation. Numeric
identities, content, split offset/affinity, save points, delayed updates and exact
outcomes are deterministic. The design test exercises a finite graph/segment
model and checks source-review coverage; it creates no production checkpoint.

DRA-1.5's `core/crates/editac-core/tests/document_lifetime.rs` must execute the
schedules through current engine admission/commands, then real checkpoint/update
encoding and fresh-writer restore. Include both 16384 chained moves and 16384
split/join operations with 512-deep ancestry and 8193 retained segments. Reopening
at 4096, 8192, 12288 and 16384 operations must preserve content, IDs, witnesses,
anchors, unknown values and retained outcome inventories. Run a disconnected peer
across all publications, both merge orders and duplicate/reordered complete replay,
live selective undo across publication, and stale/valid retained review endpoints.
The delayed edit must appear in original source/cell text even if its owner is
hidden; a losing structural intention remains explicitly inspectable.

Use the same canonical fixture corpus for WASM/Session reopen and the affected
Session/CLI storage continuation. Exercise qualified publication, corrupt newest
fallback, required-tail corruption, pending outbox retention and quota refusal.
Runtime fixture sizes/counters must be measured, not inferred from JSON-model
size. Any exceeded budget is a failed DRA-1.5 criterion, never a reason to silently
drop operations, reduce operation counts, omit chaining or raise final caps.
QSH/QWB/native and QPF retain complete functional/platform/crash/resource and
performance/size qualification. A design parent does not close those gates.
