# Registry schema v1

Status: frozen foundation contract, locally reconstructible; structural Rust/JS exchange is a separate FND-1.12 gate. This is not a production command API or a Tiptap document format.

## Scope and authority

Schema identifier: `editac.registry.v1`. The selected [structural policy](../decisions/002-document-structure.md) and passing `core/crates/editac-core/tests/structure_conflicts.rs` supply its semantics. One Yrs replica owns all committed content. Projection never writes repairs. The machine-readable seed and language mapping are in `core/fixtures/schema-v1/`; protocol metadata lives outside the CRDT as defined in [protocol-v1.md](protocol-v1.md).

Version 1 supports ordinary retained nodes and exactly one optional ownership pair: first `block-1`, second `block-2`, derived split owner `block-split`. A pair cannot be rebound or overlap another pair. Arbitrary pairs, repeated transformations, restoration of tombstones, compaction and production undo are not qualified. A document needing these operations requires a separately qualified schema revision; it must not silently reuse this descriptor.

## Exact roots and values

Create these five named root maps before the first write transaction. Empty root maps contain no update items; every receiver must request them with these exact shared types, even when absent from decoded bytes. There is no XML document root and no second document tree.

| Root name | Rust / JS shared type | Keys and values |
| --- | --- | --- |
| `registry-parents` | `MapRef` / `Y.Map` | logical node ID → immutable string kind; known kinds `list`, `item` |
| `registry-texts` | `MapRef` / `Y.Map` | same node ID → nested `XmlTextRef` / `Y.XmlText` |
| `registry-placements` | `MapRef` / `Y.Map` | same node ID → one immutable array `[parentId, order]` |
| `delete-probe-tombstones` | `MapRef` / `Y.Map` | deleted logical ID → boolean `true`; absence means not deleted |
| `probe-split-join` | `MapRef` / `Y.Map` | optional sole key `pair` → one immutable ownership array |

The historical probe root names are deliberate wire names. Do not rename them during construction. `parentId` is an ID or sentinel `@root`; `order` is an integral Number in 0…4294967295 (Rust `Any::Number`, JS number). Place a complete tuple in one map write, never nested independently merged parent/order fields. Missing/malformed placement is projected as `[@root, 0]` while the original raw value remains retained. Other malformed root/value shapes require preserved recovery rather than a partial projection.

Each registered node has one persistent nested rich text. Insert it once; moves, deletion, splitting and joining never replace/remove/clone it. Its integrated CRDT identity is distinct from its logical map key. All inserted content in this profile is text, with JSON-compatible attribute values; rich-text runs retain their original attributes. Known fixture marks are boolean `bold`, `italic`, `code`, `underline`. Unknown kinds are opaque string values: retain their text, marks and placement, render a safe fallback, and do not treat them as list parents. Unknown mark names/JSON values remain on their original characters without extension fetch or execution. Opaque retention is required; semantic commands for unknown extensions are unsupported.

## IDs and creation

Logical IDs use ASCII grammar `[a-z][a-z0-9-]{0,63}`. ASCII byte lexicographic order is the universal ID tie-break. `@root` is a sentinel, never a registered node. `block-split` is reserved for the derived owner and must not be a text/kind/placement registry entry. `block-1` and `block-2` are reserved pair members when `pair` exists. Fixtures also use fixed aliases `a`…`e`, `left`, `right`; the latter section aliases belong only to older disposable probes, not the v1 seed.

New ordinary IDs are `n-<client>-<counter>`, where each component is lowercase hexadecimal without leading zeros (zero is `0`). Client is the independent Yjs-compatible writer ID; counter is a writer-local monotonically increasing allocation counter, persisted with that writer session and never reused in the epoch. Use a fresh writer identity on restore; do not share a writer ID across live replicas. Check ID absence before insertion and reserve the ID with its node/text/placement in the same prepared transaction. Never resolve a collision by replacing an existing rich text; reject local creation, retain incoming conflicting bytes for explicit recovery. CRDT map convergence alone cannot detect every competing logical creation: production admission/collision guards remain required downstream. Fixtures use distinct fixed client IDs, not a production random-ID allocator.

## Ownership arrays and anchors

`pair` values are exactly `["original"]`, `["join"]`, or `["split", cutBytes]`. `cutBytes` is `Any::Buffer` / `Uint8Array`, containing a v1 encoded Yrs StickyIndex / Yjs relative position in the **first original text** with left affinity (`Assoc::Before` / association -1). It is not a JSON byte-number array, absolute offset, or copied text. The whole array is replaced atomically. Only local commands from `original` may transform; concurrent split/join writes resolve to the single integrated map value under the pinned CRDT conflict rule. Do not merge descriptor fields or choose by arrival time.

Resolve and validate the cut before mutation: UTF-16 offset 0…text length, outside surrogate interiors, resolvable in the first text. A right-affinity growing endpoint uses a type-relative anchor (`StickyIndex::from_type(..., Assoc::After)` / type endpoint association 0). Selections retain original source identity and affinity; projected owner and offset derive from the resolved source span. A deleted/unresolvable async target yields an explicit result, never an insertion at document end. Binary anchor interoperability is not established until FND-1.12 passes.

Ownership is a read:

- `original`: each pair member owns its entire original text and placement.
- `join`: first owner keeps its placement and concatenates spans of first then second original text. Second owner is absorbed; both shared texts and raw placements remain.
- `split`: resolve cut n in first text; first owns [0,n), `block-split` owns [n,length), second remains unchanged. Derived owner inherits first's parent and order + 1; reject local split at maximum order before mutation. Inserts at the cut go right under left affinity. Character deletion resolves the relative cut according to the pinned anchor semantics, not a stored integer.

Every character has exactly one span owner before visibility, including retained hidden content. Empty texts/ranges retain identities. Malformed/unresolvable descriptor, unsupported mode, missing pair texts, or out-of-range derived order sends the document to explicit preserved recovery; no fallback ownership is invented. With no `pair`, each ordinary node owns its own full text.

## Deterministic hierarchy and visibility

1. Read every retained logical node and its one integrated placement. Missing parent, unknown/non-list parent or malformed placement projects at root. Resolve cycles by detaching the smallest ASCII ID in each cycle. Iterative traversal visits at most N² edges; no repair update is emitted. A late valid parent can restore the stored placement.
2. Compute ownership spans. A tombstoned owner hides every span it owns. A tombstoned original source hides that source's spans even after ownership transfer. Hidden spans form explicit recovery content with marks and original identities; deletion never removes registry entries or causes automatic resurrection.
3. Transfer resolved placement to projected owners, including split's order + 1. A visible child whose parent is hidden/absorbed projects at root. Recovery keeps pre-visibility placement. Traverse visible owners in preorder, sorting siblings by numeric order then ASCII ID. With an order tie, `block-2` precedes `block-split`; split does not promise adjacency.

Known-deleted targets reject local edits during preparation; stale/offline edits merge into retained recovery text. Tombstones are permanent within this profile. Unknown content receives the same retention/visibility rules. Existing hierarchy family fixtures qualify orphan/cycle/late-parent behavior; composed fixtures qualify deletion plus ownership plus hierarchy for the fixed pair. More general command coverage is not implied.

## Reconstructing the seed

The v1 seed has `block-1` and `block-2`, both kind `list`, root placements 0 and 1, texts `a😀b` and `cאבd`, respectively. Format UTF-16 [1,3) with `bold:true` in first and `code:true` in second. Set `pair` to `["original"]`; tombstones are empty. Use seed writer 11 in deterministic fixtures. `core/crates/editac-core/tests/schema_profile.rs` constructs these five maps and typed values explicitly and compares the selected composed projection. `core/fixtures/schema-v1/mapping.mjs` constructs the same values with Yjs and demonstrates origin/admission mapping. Restored peers apply the one initializer's update; they do not independently rebuild this seed.

Construction checks establish local mapping consistency. Earlier `interop` checks establish disposable XML/text exchange only. Moves/deletes/overlapping edits, retained identities and anchors in this frozen mapping must still pass FND-1.12 before cross-language structural compatibility is claimed.
