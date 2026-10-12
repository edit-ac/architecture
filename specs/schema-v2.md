# Versioned block metadata

Status: development contract for ENG-1.16; not qualified until its receipt passes. Schema v1 and its foundation evidence remain unchanged.

## Profile and admission

Use schema `editac.registry.blocks.v2` and profile `editac.yrs-yjs.blocks.v2`. Keep protocol version 1, update encoding 1, UTF-16 offsets and the foundation's pinned Yrs/Yjs dependencies. A schema version is not a Yjs update-encoding version.

The immutable external envelope has the fields defined in [protocol-v1.md](protocol-v1.md). Require an exact supported profile/schema pair and matching document/epoch before any live mutation. A v1 replica must reject this profile, not ignore its extra root or interpret its blocks as opaque v1 content. Wrong schema/profile/epoch, malformed tuples and unsupported shared types leave content, state vector and history unchanged. Preserve rejected user-owned bytes for recovery under the existing admission/resource policy.

No automatic or in-place v1 upgrade is authorized. New v2 documents initialize once; restores, including empty documents, never seed twice and use fresh writer identities. Any future explicit migration uses a new epoch and retains the original checkpoint. Legacy v1 construction, projection and admission fixtures must continue to pass.

## Exact storage

Retain the five roots, shared types, placements, nested rich texts, tombstones and bounded ownership descriptor defined by [schema-v1.md](schema-v1.md). Add root `registry-block-attributes`, a `MapRef` / `Y.Map`. Its keys are logical block owner IDs; each value is one complete immutable array value (`Any::Array` in Rust, a plain JavaScript array, never a nested shared `Y.Array`) replaced in a single map write:

| Value | Meaning |
| --- | --- |
| `["paragraph"]` | Paragraph presentation |
| `["heading", level]` | Heading presentation; integral numeric level 1 through 6 |

Add known immutable registry kind `block` for ordinary editable text blocks. Creation reserves kind, persistent nested rich text, placement and initial block tuple together. Changing paragraph to heading never changes the registered kind, clones the rich text or stores block state on a character. Existing `list`/`item` structural kinds retain their v1 meaning; they do not become paragraphs by relabeling. Formatting unsupported or opaque kinds returns a typed unsupported-target result before mutation. This gate does not introduce list/quote/code/separator metadata; their own tasks must define and qualify their contract extensions before using them.

An ordinary `block` without a tuple reads as paragraph, without emitting a repair update. An absent tuple differs from malformed data: wrong tuple type/arity, invalid heading level or a tuple attached to an unsupported registered kind requires explicit recovery on untrusted restore/admission. Unknown tuple discriminants with a valid array/JSON value shape are retained opaquely with a safe fallback; local commands cannot edit them or execute/fetch extensions. Unknown mark attributes retain the existing character-level policy.

Block metadata persists independently of text length. Empty blocks can be formatted, checkpointed and restored. Metadata changes are observable projection changes even when visible text is identical. Prepared mixed text-mark/block batches validate every target, tuple, resource limit and current state before one explicit-origin transaction; one invalid or stale target rejects the entire batch. Preserve the marks implementation and its existing rejection guarantees.

## Bounded ownership and metadata

This profile still supports only the v1 fixed ownership pair and transformations from `original`. It must not advertise arbitrary pairs or repeated transformations. ENG-1.17/1.18 qualify and integrate those operations under a separate profile; block qualification alone does not unlock general structural commands.

For a v2 pair, both original members have immutable kind `block` and each keeps its own metadata tuple. A derived split owner has no registered text/kind/placement entry. Its effective tuple is the explicit `registry-block-attributes["block-split"]` override when present, otherwise the first original owner's current tuple (including the paragraph default). This is a live inherited value until an explicit override is committed. The first owner keeps its tuple. A heading split therefore initially produces two headings of the same level, including empty left/right ranges.

For join, the first owner keeps its metadata; the absorbed second owner's tuple and original text remain retained for recovery. A tombstoned or absorbed target rejects local formatting; metadata does not resurrect it. A concurrent split-owner override delivered before its split descriptor is retained dormant. It becomes effective only if that owner exists; losing/unsupported structural branches do not synthesize visible owners. Unregistered IDs other than the reserved derived owner are invalid metadata targets.

Concurrent writes to the same owner replace the entire tuple under the pinned Yrs/Yjs map conflict rule: never merge heading type and level independently. Concurrent writes to different owners coexist. Duplicate/reordered delivery must converge to the same tuple, visible/recovery content and stable anchor outcomes. Projection is read-only.

## Required qualification

ENG-1.16 creates `core/crates/editac-core/tests/block_profile.rs` and `core/fixtures/schema-v2/` with one seeded initializer, a machine-readable descriptor and a reproducible Yjs exchange mapping. Its receipt must cover paragraph/heading switching; levels 1/6; invalid 0/7/fraction/string/tuple shapes; empty restore; concurrent atomic tuple conflicts; split inheritance/override; absorbed/deleted targets; unknown retention; mixed-batch rejection and exact profile/epoch rejection. Exercise both Rust-to-Yjs and Yjs-to-Rust plus duplicate/reordered delivery with real prepared updates, not mocked convergence assertions.

Record exact commands, nonzero test counts, zero unresolved failures/skips, source/fixture hashes and profile envelope in `architecture/evidence/engine-block-profile/`. Rerun initialization, projection, anchors, text/format commands and existing v1 structural interoperability after admission/projection changes. Publish no profile compatibility claim before that evidence exists. ENG-1.6 consumes the qualified mapping and still requires its complete original mixed-format acceptance.
