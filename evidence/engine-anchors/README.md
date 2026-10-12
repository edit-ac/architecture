# Engine relative anchors and Unicode boundaries

ENG-1.4 is implemented and locally verified under immutable source revision `0c9ea1747d09797b35ad7d3923f79d61bae3725236a6c5b1bf13845d7e68c600`. No deployment or generalized schema compatibility is claimed.

`Document::anchor`, `selection`, `resolve_anchor` and `resolve_selection` retain original shared-text identity and endpoint bias. Resolution derives current projected owner/offset, reports hidden/deleted spans explicitly, and rejects wrong document/epoch or replaced/unreceived positions. Left bias stays before insertion; right bias stays after it, including empty and growing endpoints. Selection endpoint order is retained. UTF-16 conversion rejects surrogate interiors; movement/deletion uses extended grapheme boundaries in logical Unicode order.

The canonical local harness uses real frozen-schema Yrs replicas and v1 checkpoint/journal update bytes: seed writer 11, remote writers 21/22, reordered/duplicate schedules. Fixed strings/ranges/results live in `core/crates/editac-core/tests/anchors.rs`. Prepared deterministic evidence establishes correctness within this frozen profile. No model transport or paid inference was used.

Final named anchors suite: 24 passed, 0 failed/skipped. Related initialization/projection/schema/interop/hierarchy/split-join/structural suites: 76 passed, 0 failed/skipped. Exact commands, source/implementation hashes, fixture hash and logs are in [receipt.json](receipt.json). The failed compile, initial 19/20 run and initial formatting result are retained. The failed feature case exposed restore rejection of a derived-owner tombstone; admission now permits only that reserved tombstone while ordinary reserved-source registration remains rejected.

Process/disk cleanup is recorded in [cleanup.json](cleanup.json). Shared artifacts and the existing Assign server were preserved.
