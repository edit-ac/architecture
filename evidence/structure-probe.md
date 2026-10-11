# FND-1.6 structural comparison

Scope: disposable candidates for conflict-test selection; no production schema adoption or deployment. Source snapshot `source-68b66c0ed334.md`, revision `38b5b9d96921dc419471bdce3a85537df40e7bc3255ebbdc4a20c0ace71d0897`.

## Shared proof

`core/crates/editac-core/tests/structure_probe.rs` reuses extracted test-only XML and registry helpers. Seed 1592594996, wrapping LCG (1664525, 1013904223), four inputs beginning `a😀b` with combining, ZWJ, flag and RTL suffixes and seeded hex text. Both candidates use writer IDs 11/22/33, bold UTF-16 1..3, italic insertion `!` at 3, identical right/left placement requests and all six base/operation permutations with duplicate delivery and reverse replay. The XML same-parent clone/remove extension snapshots before removal; order is an attribute on each fresh clone, comparable to registry tuple order. Each real replica contains one Yrs document. Rich runs, lengths, block IDs, placements and text BranchIDs are asserted; update byte equality is not used as semantic proof.

## Implementation cost

XML move snapshots the entire rich subtree then removes/inserts a fresh subtree and assigns its order attribute: work and new shared content scale with subtree content/marks. Application ID is copied, shared text identity is replaced. Its tree provides direct hierarchy iteration, but conflict deduplication and edit recovery would require additional policy.

Registry move validates the parent and replaces one immutable `[parent, order]` value in one map key. Move payload scales with placement metadata rather than text length; rich text is untouched. It needs three roots plus stable-ID lookup and a read projection; general sorting, cycles/orphans and deletion/split/join policy remain future gates. Counts of source lines and actual fixture update bytes are recorded in the receipt/artifacts; neither constitutes a timing or memory benchmark. The comparison harness/reporting code is excluded from candidate LOC.

## Results and choice

Verified 2026-10-11: XML replaces text BranchIDs; move/edit loses the visible italic insertion; move/move produces two blocks with the same logical ID and different text identities. Registry retains the original text BranchID and exact rich runs; move/edit preserves the insertion, move/move selects writer 33’s complete `(left, order)` tuple on both writers and all replay observers. Select the stable registry for FND-1.7–1.9 conflict probes. This does not resolve delete, split/join, cycle/orphan, anchor or cross-language structural semantics and does not freeze a schema.

Canonical test: 2 executed/passed, 0 failed/skipped/filtered. Full core: 13 executed/passed, 0 failed/skipped/filtered, plus empty unit/doc harnesses (compile-only evidence). Node interop: 3 executed/passed, 0 failed/skipped; setup additionally runs 1 Rust interop test. Matching rustdoc prevents the previous compiler-artifact mismatch. Full logs, exact environments, tested working-tree hashes, artifact hashes and cleanup are in [receipt](foundation-structure/receipt.json). Artifacts: `core/benchmarks/structure/inputs.json`, `implementation-cost.json`, two detailed traces and 48 v1 binary updates.

Measured first-move update bytes (four seeded cases): XML [110, 118, 114, 113], registry [24, 24, 24, 24]. Source support sizes: XML 164 lines, registry 149 lines; XML comparison adapter extension is additional code, so these are component sizes, not a complete complexity ranking. Identity and semantic correctness justify selection; smaller payloads are supporting observations only. Prior failed XML alternative evidence remains in `foundation-xml/`; previous pinned-rustdoc mismatch remains in `foundation-registry/`.
