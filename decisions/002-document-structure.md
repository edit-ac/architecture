# Select stable rich-text identities and deterministic structural projection

Status: selected disposable policy for the foundation probes; schema/profile freeze and Rust/JS structural qualification remain FND-1.11 and FND-1.12. This record does not adopt a production schema or command API.

## Evidence and choice

Choose a registry of stable shared rich texts plus atomic placement and ownership descriptors. The seeded XML/registry comparison in [structure-probe.md](../evidence/structure-probe.md) rejects XML clone/remove moves: they replace identity, can duplicate moved blocks and leave concurrent edits outside the visible destination. The registry retains original Yrs rich-text identities without a second writable replica. Implementation cost and limitations are recorded in that comparison.

The canonical Rust regression aggregator is `core/crates/editac-core/tests/structure_conflicts.rs`. It directly includes all four delete/edit, five split/join and seven hierarchy checks, retaining their explicit expected semantic assertions and real Yrs update harnesses. Eight additional same-document cases exercise precedence across families. Validation evidence lives in [foundation-conflicts](../evidence/foundation-conflicts/README.md). Existing generic XML/text JS exchange does not qualify this structural policy across languages.

## Selected policy

- A move replaces one complete parent/order tuple in a Y.Map. Yrs selects the integrated tuple using its pinned conflict semantics; parent and order are never independently merged. Tests reverse writer assignment and arrival order. Sibling ties sort by stable logical ID after numeric order.
- Hierarchy projection reads retained logical nodes. Missing/invalid placements, nonexistent parents and non-list parents project at root. For each directed cycle, detach its smallest logical ID at root. Traversal is iterative, emits each logical node once and bounds edge visits by N². These are read decisions; no platform or projector emits repair updates. A late valid parent can restore the original placement.
- Deletion writes a permanent tombstone for the logical ID in these probes. Never delete its shared text or placement. Known deletion rejects local edits before mutation in the delete/edit command fixture. Offline edits still merge, retaining marks and original identities. Recovery is an explicit hidden-content read; it does not resurrect the owner. Undo, explicit restoration and compaction are outside this policy proof.
- Split partitions the first persistent text at a left-affinity relative UTF-16 boundary. Inserts at the cut belong to the right output. If the cut's character is deleted, replacement content stays in the source according to the tested resolved anchor. Reject surrogate-interior/unresolvable cuts before writes. The new output inherits the first placement with order + 1 and its fixture-defined ID `block-split`.
- Join concatenates references to both original texts under the first logical owner and keeps that owner's placement. The second logical owner becomes absorbed, while its text and placement stay registered. One atomic pair descriptor selects original/split/join ownership, preventing partial joins. Concurrent split/join chooses one complete descriptor; it never clones text. Marks remain attached to original characters. Selection anchors retain their source identity and resolve to the projected owning block. The engine requires explicit deleted/unresolvable results for deleted async targets; the composed fixtures prove visibility/recovery, not a new async command API.

## Interaction precedence

Apply ownership, deletion and hierarchy as one read projection over the same replica:

1. Resolve raw placements and cut cycles across retained logical nodes; compute span ownership from the atomic layout descriptor.
2. A tombstoned logical owner hides every span it owns. A tombstoned source hides its spans even when a split or join transfers their owner. Partition visible and recoverable spans without cloning, dropping or resurrecting text. Thus deleting the split source hides both split outputs; deleting the joined first owner hides both sources; deleting only the absorbed second source retains the first source visibly and recovers the second separately.
3. Transfer the hierarchy's resolved placement to each projected owner; a split output inherits its source's resolved placement. If a visible output's parent is hidden or absorbed, project that child at root. Do not write a repaired parent. Order surviving outputs by deterministic preorder with numeric order/ID sibling ties. Recovery records retain the pre-visibility projected placement for inspection.

A split-right output can follow another sibling with equal order: `block-2` sorts before `block-split`. This ordering is explicit, not an assumed adjacent insertion.

The composed cases assert exact visible/recovery text, marked concurrent edits, original shared identities and expected root placement. All 24 arrival permutations per case include initialization; each runs on three receiving replicas with duplicate delivery, reverse replay and fresh restore, then merges back into all writers. Original family checks retain endpoint anchors, writer-order inversion, nested subtrees, orphans, invalid commands and deep traversal coverage.

## Boundaries for schema adoption

No unresolved identity or cycle behavior remains within these bounded fixtures once the aggregator passes. A failed identity/projection assertion blocks FND-1.11; the bounded question is: which descriptor or precedence rule must change to preserve the original shared text and one expected semantic owner in that named fixture?

These fixtures do not define arbitrary overlapping pairs, production IDs, unknown extension/version admission, resource limits or wire roots. FND-1.11 must specify the supported pair scope, stable ID format, exact root/value mapping, initialization/epoch and unsupported-version behavior without claiming broader ownership semantics. FND-1.12 must qualify that exact mapping and relative anchors with pinned Yjs. Unknown nodes/marks must be retained without extension execution under the engine contract; this ADR adds no silent deletion or fetch rule. Further engine commands, undo and persistence require their own named acceptance gates. No Tiptap compatibility, durability, performance envelope or deployment is asserted.
