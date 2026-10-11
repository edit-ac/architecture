# FND-1.11 schema and profile freeze

Implemented and locally verified 2026-10-11, not deployed. Normative contracts: [schema-v1](../../specs/schema-v1.md) and [protocol-v1](../../specs/protocol-v1.md). `receipt.json` records immutable roadmap/prompt revisions, repository bases, tested working-tree hashes, exact commands, counts and full-log hashes. Prior changes were preserved; all 17 FND-1.10 tested source hashes remain unchanged.

The exact five historical root maps, nested XmlText identities, atomic placement/layout values, fixed optional pair, UTF-16 anchors, IDs, tombstones and deterministic hierarchy/visibility are specified. Metadata stays outside the CRDT. The profile defines one initializer per document/epoch, restore without reseeding, exact negotiation/rejection, origin classes and preserved recovery. Unknown kinds/marks retain content without extension execution. Unsupported pair generalization and production admission/persistence are explicit boundaries.

`core/fixtures/schema-v1/seed.json`, `mapping.mjs` and `README.md` give the recipe and JS mapping. `schema_profile.rs` demonstrates explicit Rust construction against the selected composed projector. Local checks prove roots/types/values/marks, restored original identities, opaque retention and profile rejection before invalid-byte decoding. No structural cross-language exchange is claimed: FND-1.12 remains open. Existing XML/text interop remains its earlier qualified disposable schema.

Checks, all exit 0:

- `cargo test -p editac-core --test schema_profile --locked`: 3 executed/passed.
- `node --test tests/schema-profile.test.mjs`: 4 executed/passed.
- Original `cargo test -p editac-core --test structure_conflicts --locked`: 24 executed/passed, unfiltered.
- Original `node --test tests/interop.test.mjs`: 3 executed/passed; setup asserts one additional Rust interop pass.
- `cargo test -p editac-core --locked`: 56 executed/passed, including 24 canonical and 3 new construction checks. Empty unit/doc harnesses are compile-only.
- `cargo fmt --all -- --check` and both repository `git diff --check`: passed.

All suites have zero failed/skipped/filtered/cancelled checks. Logs are retained separately; no failed feature checks arose. Matching Rust/rustdoc 1.97.1 and Node 24.19.0 were explicitly selected. No provider calls, credentials, publishing, servers or browsers.

The latest supervisor's measurable delivery target is met: both contracts plus the fixture mapping, durable hashes and passing original canonical/interop plus core integration. Next parent FND-1.12 must prove frozen structural outcomes, relative anchors and retained identities in both language directions; text-only exchange is insufficient. FND-1.13 remains independently ready; FND-1.14 awaits both.

Hygiene: stopped no processes; other-workspace listeners preserved. Removed only inactive session-created `core/target/debug/incremental/schema_profile-2pqtxq0dw4l1o` (17,354,961 bytes), after `lsof +D` confirmed no open files. Final data-volume free space: 18,649,579,520 bytes (~17.4 GiB). Remaining local reproducible directories are `core/target` (~273 MiB) and `core/node_modules` (~42 MiB), mostly prior-session work; they are preserved. Broader cleanup requires a separate scope decision. `hygiene.json`, process/listener inventories preserve the check. This session added less than 1 MiB of durable evidence/source.
