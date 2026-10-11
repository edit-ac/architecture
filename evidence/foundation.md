# Portable engine foundation evidence

FND-1.14 consolidates the local foundation qualification. Final acceptance commands,
counts, tested source hashes, compiled bytes and teardown are recorded in
[the approval receipt](foundation-approval/receipt.json). This evidence supports
starting the dependent engine tasks within the exact profile below. It supplies
no deployment, package publication, durability or production command claim.

## Frozen profile and reconstruction

The supported update pair is **Yrs 0.28.0 with `small-client` and explicit
`OffsetKind::Utf16` ↔ Yjs 13.6.33**, using update/state-vector encoding v1.
y-protocols is pinned to 1.0.7, Rust/compiler and rustdoc to 1.97.1, Node to
24.19.0 and wasm-bindgen crate/CLI to 0.2.129. Yjs remains fixture-only;
one Yrs replica owns committed production semantics. No Tiptap document
compatibility, update v2 or arbitrary library-pair compatibility is claimed.

[Schema v1](../specs/schema-v1.md) specifies the five exact map roots, nested
rich texts, atomic placement and ownership arrays, stable logical IDs and UTF-16
relative cuts. [Protocol v1](../specs/protocol-v1.md) specifies the immutable
document/epoch envelope, one initializer, fresh restored writer identities,
origins and exact metadata admission. Unsupported profile/schema/version/encoding
or offsets reject before live mutation; wrong document/epoch and malformed
metadata have explicit results. Restored empty documents are not reseeded.
Rejected user-owned state requires preserved recovery, not conversion or repair.
These are frozen contracts and fixture admission proofs, not implemented
production storage/network/resource admission.

The reconstructible seed and JS mapping are in `core/fixtures/schema-v1/seed.json`,
`mapping.mjs` and `exchange.mjs`; Rust construction is in
`core/crates/editac-core/tests/schema_profile.rs`. The receipt hashes the exact
fixtures and contracts. Peers restore one seed update rather than independently
initialize equivalent JSON. The schema supports ordinary retained nodes and only
the documented fixed ownership pair; transformations cannot be generalized
without a separately qualified revision.

## Structural decision and evidence chain

[Decision 002](../decisions/002-document-structure.md) selects persistent rich-text
identities with atomic placements and read-only deterministic projection. Moves
retain text identity; permanent tombstones hide retained recovery spans; split/join
transfer ownership without cloning. Cycles detach the smallest ASCII logical ID,
invalid/missing parents project at root, and traversal is bounded. No repair write
feedback loop or unresolved identity/cycle contradiction remains in the qualified
fixtures. Unknown valid kinds/marks remain opaque without fetching extension code.

| Original gates | Durable implementation and verification evidence |
| --- | --- |
| FND-1.1–1.3 | [Toolchain](foundation-toolchain/receipt.json), [reproducible fixtures](foundation-fixtures/receipt.json), [bidirectional XML/text exchange](foundation-interop/receipt.json) |
| FND-1.4–1.6 | [XML alternative](foundation-xml/receipt.json), [registry](foundation-registry/receipt.json), [same-seed comparison](structure-probe.md) and [comparison receipt](foundation-structure/receipt.json) |
| FND-1.7–1.10 | [Delete/edit](foundation-delete-edit/receipt.json), [split/join](foundation-split-join/receipt.json), [hierarchy](foundation-hierarchy/receipt.json), [composed conflict policy](foundation-conflicts/receipt.json) |
| FND-1.11 | [Exact local schema/profile freeze](foundation-schema/README.md) and [receipt](foundation-schema/receipt.json) |
| FND-1.12 | [Frozen structural exchange](foundation-schema-interop/README.md) and [receipt](foundation-schema-interop/receipt.json) |
| FND-1.13 | [Actual compiled loading boundary](foundation-wasm/README.md) and [receipt](foundation-wasm/receipt.json) |
| FND-1.14 | [Combined acceptance receipt](foundation-approval/receipt.json), full logs and prerequisite integrity audit in `foundation-approval/` |

The XML clone/remove alternative was rejected for replacement identities,
duplicate placements and concurrent edits absent from the visible destination.
Its traces/updates remain preserved, alongside comparison cost artifacts in
`core/benchmarks/structure/`. CRDT byte convergence alone did not select the
registry. Earlier compiler/rustdoc, transaction-lock and expected-order failures
remain in the linked receipts/logs; repaired final passes do not erase them.

The exact structural mapping exchanges real v1 bytes and binary relative anchors
in both languages: 13 cases × two initializers, six observer arrival schedules per
case, duplicate/reverse replay and checkpoint restores. Assertions compare expected
visible/recovery text, marks, placement, source and projected anchor ownership and
original nested identities, not just state vectors. Unicode fixtures cover emoji,
combining, ZWJ, flags and RTL; UTF-16 cuts and surrogate-interior rejection remain
in the canonical family checks. This is deterministic correctness evidence.

## Compiled WASM boundary and reproduction

The preserved actual release module is
`foundation-wasm/artifacts/editac_wasm_bg.wasm` (**664,648 bytes**); generated web
glue is `foundation-wasm/artifacts/editac_wasm.js` (**8,523 bytes**). Their hashes
and the raw pre-bindgen module are retained in the original WASM receipt. The
combined receipt also hashes the current packaged assets used by acceptance.

The real Chromium/local HTTP harness loads a supplied URL and an offline-installed
local tarball consumer. SSR imports touch no window/document, fetch, WASM
initialization or document creation. Explicit async initialization, concurrent
call sharing, URL conflicts, failed-load retry, marked Unicode update exchange
and malformed decode rejection have assertions. This compiled bridge uses the
earlier XML/text fixture: the structural Rust/JS qualification is separate.

From `core`, with the pinned toolchains installed and deterministic dependencies
available, prepend `/Users/bpstr/.cargo/bin` and the Node 24.19.0 bin directory to
PATH and set RUSTDOC to the Rust 1.97.1 toolchain's `bin/rustdoc`. Run:

```sh
npm run build:wasm
cargo test -p editac-core --locked
node --test tests/schema-interop.test.mjs tests/wasm-load.test.mjs
```

The original build evidence is reused; FND-1.14 executes the latter two original
checks after consolidation. Node schema setup additionally runs the real Rust
exchange check. Empty Rust unit/doc harnesses are compile-only, not acceptance
tests. Full logs retain every failure/skip/count; zero matches cannot qualify a
gate. No providers, credentials, automatic fixture recording or paid inference
are involved. Local HTTP fixture transport and actual CRDT/WASM boundaries are
not replaced by prepared results.

## Remaining risks and accountable follow-up

| Boundary | Owner and required follow-up |
| --- | --- |
| Production semantic commands, validation, history and deletion-sensitive revisions | Engine track owner: implement and qualify the engine roadmap; do not infer command safety or selective undo from fixture projections. |
| Arbitrary/overlapping ownership pairs, repeated transforms, tombstone restoration or compaction | Schema/engine owner: propose an explicit revision and new semantic/identity/anchor qualification before extending v1. |
| Logical-ID collisions, untrusted binary/resource validation and authenticated admission | Engine and synchronization owners: implement disposable bounded decoding, collision guards and authorization before accepting untrusted updates. The minimal WASM fixture accepts trusted test bytes. |
| Journal/checkpoint durability, acknowledgment, initialization authority and migrations | Local-storage/synchronization owners: prove crash/recovery and durable receipts. Receipt of bytes or a state vector is not a durable acknowledgment. |
| Production registry WASM API, bundler asset rewriting, full browser/device matrix and performance envelope | Engine/browser/release owners: qualify these separately. Current native ESM/Chromium loading proof and artifact bytes establish neither native SDK parity nor latency/compressed-size targets. |
| Publication and release gates | Release owner: keep scaffold packages private until documented API, consumer and release requirements pass; no publication was authorized here. |

These are explicit downstream limits, not unresolved structural uncertainty within
the frozen foundation fixtures. The receipt identifies the uncommitted tested
working tree and repository base revisions; it does not invent a commit or
deployed revision.
