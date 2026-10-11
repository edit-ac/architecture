# FND-1.10 conflict policy and regression aggregation

Implemented and locally verified on 2026-10-11. Selected policy: [document structure ADR](../../decisions/002-document-structure.md). `receipt.json` records immutable source/prompt revisions, repository bases, tested working-tree hashes, fixture/update hashes, exact commands/counts and full-log hashes. Existing unrelated changes were preserved. No production schema adoption, deployment or structural JS qualification is claimed.

## Delivered boundary

`core/crates/editac-core/tests/structure_conflicts.rs` includes all 16 original conflict-family checks and eight composed real-Yrs cases. Its shared support projector combines persistent text-span ownership, tombstone visibility/recovery and hierarchy read rules over one replica. It exposes the existing split/join rich-run slicer for reuse; no existing family policy changes. The ADR defines ordering, atomic winners, tie-breaking, cycles, orphans, split/join ownership, marked content/selection behavior and delete recovery, and separates remaining profile/interop gates.

The additional cases cover deletion of split source, joined owner and absorbed source; deletion of a nested parent; joined owner under an absorbed parent; concurrent cycle/deletion; and split/join competition with both writer assignments. They assert exact visible/recoverable text, marked edits, original identities and root promotion. Each case applies all 24 permutations including initialization, on three receiving replicas, with duplicate updates, reverse replay and 576 total fresh restores. All 24 editing writers merge to the same projection. Repeated reads preserve full update bytes and state vector. Eight traces and 32 binary updates are retained in `artifacts/`.

The split output's order + 1 can tie an existing sibling. The expected order explicitly follows stable ID ordering, placing `block-2` before `block-split`; no adjacency promise is added. Deleted owner hides all owned spans; deleted source hides that source's spans even under another owner. Visible children of hidden/absorbed parents project at root without repair writes. Existing family checks still cover Unicode/marks, anchors, offline dependent deltas, writer-order inversion, invalid pre-mutation rejection, late parent arrival and bounded deep traversal.

## Checks and preserved failures

- Initial canonical check: 22 started, 16 passed and 6 interrupted after the new fixture attempted a root lookup inside a write transaction. The exact task-owned binary was terminated; `interrupted-root-lock.log` is preserved. Root lookup was moved before the transaction.
- Next canonical check: 24 executed, 23 passed, 1 failed, zero skipped/filtered. `ordering-expectation-failure.log` preserves the incorrect expected sibling order. The fixture was corrected to the documented order/ID policy.
- Repaired case only: 1 passed, 23 filtered, zero failed/skipped. Passing cases were reused until combined integration; filters are not counted as execution.
- Full `cargo test -p editac-core --locked`: 53 passed, zero failed/skipped/filtered, including the entire unfiltered canonical `structure_conflicts` 24/24. Empty unit/doc harnesses are compile-only. This is the final complete aggregator proof after repair.
- Pinned `node --test tests/interop.test.mjs`: 3 passed, zero failed/skipped; setup additionally executes one Rust interop check. This proves existing XML/text exchange only. Formatting passed.

Toolchain: Rust/rustdoc 1.97.1, Node 24.19.0, Yrs 0.28.0 small-client, explicit UTF-16 and update v1. No providers, paid inference, credentials or browsers/servers were used. FND-1.6 supervisor target remains supported by its existing seeded comparison receipt and current broad comparison pass.

## Handoff and hygiene

FND-1.10 is complete within the bounded fixtures. FND-1.11 must freeze the exact supported mapping, pair scope, stable IDs, initialization/epoch and unsupported-version behavior; FND-1.12 must prove that structural mapping and anchors across Rust/JS. Arbitrary overlapping layouts, undo, compaction and a production resource envelope remain outside these probes.

No task-owned browsers/servers remain. Other-workspace listeners were preserved; process/listener inventories remain here. Removed only inactive session-created `core/target/debug/incremental/structure_conflicts-29vhwon1njp10`, 54,869,309 bytes. Data-volume free space after cleanup: about 18.4 GiB. Source, credentials, prior caches and qualification evidence were preserved; no broader cleanup was performed.
