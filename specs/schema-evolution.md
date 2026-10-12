# Engine ownership qualification beyond the foundation

Status: development requirements for ENG-1.17/1.18, not a frozen wire layout or passing interoperability claim.

## Authority and scope

[Schema v1](schema-v1.md) qualifies one fixed pair transforming only from `original`. [Block metadata v2](schema-v2.md) deliberately preserves that limitation while qualifying empty paragraph/heading state. Those receipts remain valid for their recorded bounds. Neither proves an editor can split/join arbitrary blocks repeatedly.

ENG-1.17 must select and specify an ownership representation for schema `editac.registry.structure.v3`, profile `editac.yrs-yjs.structure.v3`, using the same pinned libraries, protocol version 1, update encoding 1 and UTF-16 offsets. Its normative layout belongs in `schema-v3.md`, created by that task before the qualification tests. Keep the v2 block-tuple semantics and independent empty-block metadata. Do not mutate v1/v2 roots or describe an untested layout as frozen. Exact profile admission, separate epochs, preserved recovery and no automatic migration remain mandatory.

## Representation obligations

The selected layout must support newly allocated logical IDs rather than the reserved fixture aliases; disjoint pairs; multiple splits of the same live owner; joins after splits; splits after joins, including an owner containing spans from multiple original texts; empty spans; and retained block formatting. At least three sequential transformations must work without resetting/reseeding the document or inventing an unrelated operation when the current owner is unsupported.

Each original nested rich text keeps its integrated identity. Structural commands cannot implement these operations by deleting/reinserting or cloning original text. The specification must define exact roots/shared types/value shapes, owner IDs and allocation, span/relative-cut representation, operation or descriptor conflict ordering, placement, metadata inheritance, deletion/recovery and unsupported-input behavior. If operation history is used, define dependency ordering and treatment of incomplete/concurrent branches; if descriptors are used, define atomic replacement and overlapping ownership. Do not pick a policy from arrival order or independently merged descriptor fields.

Every retained character belongs to exactly one visible or explicitly recoverable span owner. Relative anchors remain attached to original text identities and resolve to the current owner or a typed deleted/unresolvable result. Concurrent edits at both sides of a cut, concurrent overlapping split/join choices and deleted targets must have a documented deterministic outcome. Losing structural intentions and their content remain recoverable; projections emit no repair writes. Bound decode, projection and command preparation resources, including malformed or adversarial operation graphs.

## Qualification boundary: ENG-1.17

Create a disposable but faithful Rust/Yjs fixture mapping under `core/fixtures/schema-v3/` and `core/crates/editac-core/tests/ownership_profile.rs`. It must build the exact proposed roots in both languages and prove the obligations above with seeded replicas, real binary updates, both exchange directions, duplicate/reordered permutations, checkpoint restore, stable identities/anchors, marks, heading/empty-block metadata, deletion and malformed input. Include two independent pairs with non-reserved IDs and at least three sequential transformations on one lineage. Compare semantic visible and recovery snapshots, not state-vector/byte agreement alone.

Record rejected alternatives, the selected layout and its remaining resource envelope in `architecture/evidence/engine-ownership-profile/`. A precise bounded split proposal is required if the selection/probe cannot fit a session; no narrowing to a fixed pair or omission of original requirements clears this gate. No production representation is approved until its exact descriptor, matching source hashes and nonzero zero-failure/zero-skip receipt exist.

## Command integration boundary: ENG-1.18

Use the qualified v3 mapping in document creation/restore, projection, anchors, prepared text/format edits and structural commands. Preserve legacy profile readers/tests and explicit unsupported-profile results; never merge schemas/epochs. The ENG-1.7 fixed-pair implementation remains bounded evidence, not a substitute for this integration.

Production split/join tests must repeat the complete beginning/middle/end/empty, Unicode, mark retention, remote insertion race and deleted-target acceptance using arbitrary pairs and repeated transformations, including split-after-join across original sources. Test mixed mark/block batches and inherited/overridden heading state on these owners. Rerun the v3 interoperability probe and relevant initialization/projection/anchor/text/format suites. Subsequent list/code/move/history/patch/WASM gates consume this qualified mapping; they cannot bypass it by using the foundation aliases.
