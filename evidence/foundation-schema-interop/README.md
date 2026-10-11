# Frozen structural Rust/JS exchange

FND-1.12 is implemented and locally verified with Yrs 0.28.0 (`small-client`, explicit UTF-16), Yjs 13.6.33, Rust/rustdoc 1.97.1 and Node 24.19.0. This qualifies the exact five-root frozen schema and fixed ownership pair. It establishes no production admission, durability, arbitrary pair, WASM or deployment claim.

`core/crates/editac-core/tests/schema_interop.rs` uses the existing composed Rust projector. `core/fixtures/schema-v1/exchange.mjs` constructs the same pinned Yjs schema and implements the frozen read projection independently. The bridge exchanges actual binary v1 updates, state-vector diffs and encoded relative anchors; no prepared transport replaces either CRDT boundary. Content and schedules are deterministic fixtures, with no credentials, providers or recording.

There are 13 cases: Rust-authored move/edit, move/move, delete/edit, overlapping insert/delete edits, split/edit, join/edit, split/join and cycle/edit; plus JS-authored move/edit, delete/edit, split/edit, join/edit and overlapping insert/delete edits. Each runs with a Rust initializer and a JS initializer, restored from one seed rather than initialized independently. Writers use distinct IDs 101/202; restored peers use fresh IDs. Four anchors per case cover both cut affinities, a growing first-text endpoint and the second original source. The overlapping edit deletes the character referenced by the right-affinity anchor; it still resolves correctly.

Both projectors assert expected content/marks, visible and recovery spans, atomic placements, bounded hierarchy, no copied text, unchanged original nested text identities and no projection writes. Binary anchors resolve to the original source identity and the same UTF-16 position, projected owner and hidden status in both languages. JS checks explicit expected family outcomes before emitting canonical JSON; Rust compares its existing policy against that JSON, and JS compares the final Rust artifact. Node tests also pin anchor offsets and split/join ownership.

Each language runs 26 scenarios × six arrival permutations = 156 observer schedules, with duplicate delivery, reverse replay and 156 checkpoint restores. Rust additionally checks 312 restored-peer state-vector deltas; JS checks 52. Neither byte nor state-vector equality substitutes for semantic assertions. All three original structural race families and local construction remain in the broad core check.

Commands (prepend pinned Cargo/Node PATH and matching RUSTDOC; see receipt):

- `cargo test -p editac-core --test schema_interop --locked`: 1 passed, 0 failed/skipped/filtered. One orchestration test exercises all cases and invokes actual Node exchange.
- `node --test tests/schema-interop.test.mjs`: 13 passed, 0 failed/skipped/cancelled/todo; setup additionally asserts the real Rust check passed 1/1.
- `cargo test -p editac-core --locked`: 57 integration tests passed, 0 failed/skipped/filtered. Empty unit/doc harnesses are compile-only. Existing dead-code warnings remain in older disposable helpers; the new harness compiles without warnings.
- `node --test tests/schema-profile.test.mjs`: 4 passed, 0 failed/skipped/cancelled/todo; unchanged mapping/admission regression evidence.
- Formatting and both repository diff checks: exit 0.

`receipt.json` records source revisions, tested tree hashes, full logs, update/anchor/semantic artifact hashes and exact counts. `artifacts/` is the retained Rust acceptance exchange; `node-artifacts/` is the independent Node acceptance exchange. Earlier compile errors and the interrupted root-lock run remain in `schema-rust-1.log`, `schema-rust-2.log`, `schema-rust-3.log`. The lock was repaired by acquiring roots before the write transaction and text references before anchor-resolution transactions. The final suite was expanded after the initial eight-case pass to cover structural authorship in both directions; the corresponding earlier passing logs are retained as superseded coverage, not final qualification.

No servers or browsers were started. The owned hung test was stopped after exact command/parent validation; unrelated services were preserved. `hygiene.json` records removal of only this session's inactive schema_interop incremental cache, approximately 36 MiB, and about 18.1 GiB remaining free space. Existing target outputs, dependencies, source and all evidence were retained.
