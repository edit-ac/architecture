# Shared engine contract

Status: development contract; the bounded foundation profile is locally qualified in [foundation evidence](../evidence/foundation.md). Production engine behavior remains subject to its own gates.
Scope: web editor release, with portable Rust interfaces for later native adapters.
The initial roadmap's full native SDK parity requirement is deferred by the current project scope.
This document describes required behavior; it does not assert that the engine is implemented.

## Ownership and dependency boundary

- Yrs is the only writable authoritative document state, including offline single-user sessions.
- Rust owns committed content, schemas, semantic commands, relative anchors and local history.
- DOM, native attributed strings, read indexes and exports are derived projections.
- Adapters may retain temporary composition state under the browser/native input contract.
- React owns the host lifecycle; it never owns a second document tree.
- Yjs is used in interoperability fixtures. Do not mirror production state into a second `Y.Doc`.
- Core code has no DOM, React, IndexedDB, socket, UIKit or Android dependencies.
- Prepared optional content uses validated v1 image/table descriptors in existing
  opaque block tuples. FMT-1.6 stages descriptor presentation after fragment text,
  marks and containers; one final admitted update preserves unknown source/data
  and history. Unknown blocks remain inert and are not generic text-edit targets.
- V5 source registration appends a new immutable root placement after existing
  root registrations. A later original source must not interleave the baseline
  adjacency witnessed by historical joins before its own Place operation replays.
  This uses the existing placement shape/bounds; v4's frozen creation rule stays
  unchanged. Fragment payloads use distinct original sources, with existing
  prefix/suffix sources retained, so redo cannot shift cuts into reinserted text.
- Persistence and synchronization consume immutable update bytes and metadata through ports.

## Compatibility profile

Start the compatibility spike with Yrs 0.28.0, Yjs 13.6.33 and y-protocols 1.0.7.
These exact pins are qualified for the bounded foundation profile; upgrades require new interoperability evidence.
Enable Yrs `small-client` for the stable Yjs 13 line; the 0.28 default is different.
Set `OffsetKind::Utf16` explicitly in a single document-construction path.
Use update encoding v1 for the baseline; v2 requires a separate qualified profile.
Record schema version, document identity and session/epoch separately from transport identity.
Generate a distinct client ID for every independently editing live replica, including tabs.
Never restore one persisted writer ID into two simultaneously active writers.
Freeze root shared-type names and types with the schema decision.
Pin dependency versions and options in fixtures; upgrades rerun the compatibility suite.

The foundation freeze specifies exact roots and bounded ownership in
[schema-v1.md](schema-v1.md), and metadata/admission in
[protocol-v1.md](protocol-v1.md). FND-1.12 qualifies this exact fixed-pair mapping
with pinned Yrs/Yjs moves, deletion, overlapping edits, split/join ownership and
binary relative anchors from both languages; see
[structural exchange evidence](../evidence/foundation-schema-interop/README.md).
This is deterministic local interoperability evidence. The actual compiled fixture
WASM boundary is separately qualified by [loading evidence](../evidence/foundation-wasm/README.md)
for supplied-URL and local packed native ESM consumers, with SSR-safe import.
It uses the earlier XML/text fixture, not production registry commands.
Production commands, admission ports and persistence remain subsequent gates.

### Controller-qualified schema evolution

The frozen foundation supplies bounded interoperability, not every engine primitive.
[Versioned block metadata](schema-v2.md) defines the ENG-1.16 qualification mapping
for paragraph/heading state, including empty blocks and split owners. ENG-1.6 may
use it only after the exact profile/admission and Rust/Yjs evidence pass. Keep the
foundation contract, fixtures and historical receipts unchanged; new schemas are
explicit profile/epoch boundaries, not extra roots silently added to v1.

[Ownership evolution](schema-evolution.md) defines ENG-1.17's representation proof
and ENG-1.18's production integration for arbitrary, repeatable split/join. Existing
ENG-1.7 evidence remains the fixed-pair baseline. Downstream structural commands
depend on the new integration gate. Missing representation evidence must stay
unchecked; controller-authorized qualification work resolves the mapping, rather
than polling for an unspecified external decision or reducing acceptance.

[Nested structural profile v4](schema-v4.md) supplies the controller contract for
list/quote containers, numbering/check state, code/separator presentation,
versioned placement and reversible structural history controls. ENG-1.19 and
ENG-1.20 qualify the exact representation and code policy separately; ENG-1.21
integrates it before ENG-1.8/1.9. Preserve existing v3 receipts and recognize their
ordinary-block scope. The new profile is explicit qualification work, not an
external schema wait or permission to weaken the remaining parents.

[Stable presentation v5](schema-v5.md) resolves ENG-1.9-F1: split/join command
eligibility captures immutable preparation witnesses, so later valid formatting
does not replay an established join as losing or resurrect its absorbed owner.
ENG-1.22 qualifies that separately versioned rule; ENG-1.23 integrates it before
full ENG-1.9 acceptance. Preserve v4's mapping and historical guard/failure
evidence; do not call a presentation-conflict rejection positive conversion proof.

## Positions and anchors

- Public text offsets are UTF-16 code units with documented start/end affinity.
- Reject positions inside a surrogate pair before opening a live mutation transaction.
- Rust byte indexes and scalar counts are internal details; conversion must be explicit.
- Grapheme-aware movement/deletion must cover combining marks, ZWJ emoji, flags and RTL.
- Do not redefine a grapheme as a UTF-16 code unit or a Rust `char`.
- Asynchronous commands, selections and remote cursors use stable relative anchors.
- Resolving an anchor returns a position or an explicit deleted/unresolvable result.
- A deleted target never silently redirects an asynchronous insertion to the document end.
- Each fixture records the original string, UTF-16 range, expected text and anchor result.

The optional SYN-1.4 presence bridge adds read-only `exportAnchor` / `importAnchor`
to the packed handle (WASM `export_anchor` / `import_anchor`). Export returns the
versioned source/relative-position envelope in [storage-sync](storage-sync.md#optional-awareness-bridge);
import checks complete lineage, source identity, branch and current UTF-16/semantic
resolution before retaining an engine-scoped token. It does not mutate the replica,
history, selection, pending document plans or journal. Imported tokens use the
existing release policy and bounded anchor capacity. Presence frames remain outside
document update/schema/receipt contracts.

## Prepare, validate, commit

1. Parse arguments and resolve dependencies before acquiring a mutable Yrs transaction.
2. Resolve target anchors against the current revision and validate the entire command.
3. Prepare the complete mutation plan, including resource and schema checks.
4. Check that the prepared preconditions still hold immediately before applying it.
5. Apply one non-fallible semantic mutation phase with an explicit origin.
6. Emit a revision, dirty ranges, immutable update bytes and operation metadata.

Yrs commits when its mutable transaction is dropped. Error returns do not roll it back.
Never catch a partial mutation error and report the document as unchanged.
Validation failures must leave content, state vector, history and journal enqueue count unchanged.
`can(command)` uses preparation/validation without mutation or subscriber side effects.
A command chain validates all document mutations before any of them changes the live store.
Host focus/menu side effects are outside the atomic document mutation contract.
Reentrant adapter callbacks cannot mutate a document while a transaction is active.
Revision numbers are local observation tokens, not globally comparable CRDT timestamps.

## Atomic heading-end Enter

WEB-1.14 owns the engine/WASM prerequisite for WEB-1.8. Add the prepared Rust editor command `HeadingEnd { owner, at }` and the packed command `{ type: "headingEnd", owner, at }`, using the existing engine-owned stable anchor token and editor request envelope. This is an additive command API on the qualified v5 replica; it does not change the persisted schema or peer update protocol.

Prepare this command only for a nonempty heading whose resolved cut is its current text end. Earlier text deletions in the same prepared batch may produce that end cut; qualify both selected replacement and cross-block selected replacement without live intermediate mutations. Preserve the original heading identity, level, remaining text and marks. Create one empty paragraph immediately after it under the same parent. Preserve unrelated blocks and remote edits. The input cut retains its existing source-relative routing. Return a separate engine-owned fresh-source stable result caret resolving to the new paragraph at offset zero, under [Decision 005](../decisions/005-engine-command-result-caret.md); adapters do not guess generated owner IDs.

Stage the admitted fresh-source Create + Place + Join + Split construction and destination paragraph attributes together before one live mutation, with normal resource/schema/stale checks. `can` and rejected preparations leave content, state vector, history, updates and journal effects unchanged. Admission/read-only/disposed/stale rejection uses the existing boundary policies. One successful local command produces one update and one explicit semantic undo group. Undo/redo restores/reapplies the original heading and paragraph while retaining unrelated remote edits. Empty-heading Enter remains conversion of that owner to a paragraph; interior-heading Enter remains ordinary split; code, lists and quotes retain their existing contextual policies.

Qualify actual Rust semantics, packed WASM dispatch/types, UTF-16 anchors and independently authored undo/redo/peer outcomes before the browser switches from its explicit rejection. Full browser heading-end mechanics remain WEB-1.8 acceptance; neither a planned API nor filtered keyboard successes pass that parent.

## Structural representation gate

Implement disposable fixtures for conventional Yrs XML and stable block identities with placement metadata.
Use the same corpus and comparison outputs; do not implement two production engines.
The winning representation must preserve rich-text identity during semantic moves.
A registry candidate should test one replacement placement tuple rather than independently merged parent/order fields.
This candidate is not a promised wire schema; the spike must prove its behavior first.

The decision record must define:

- Ordering, winning concurrent placement and tie-breaking independent of arrival order.
- Cycles, orphan nodes, invalid references and duplicate placements.
- Delete/edit policy and recovery of concurrent content hidden by deletion.
- Split/edit and join/edit behavior, including marks and selections.
- Nested list moves and invalid ancestor/descendant operations.
- Unknown node/mark retention without fetching or executing extension code.
- Version admission, upgrade policy and rollback/recovery constraints.

No renderer or serializer may invent a structural repair by emitting platform-specific writes.
Projection must be deterministic and converge semantically on every supported replica.
Freeze the schema only after permutation/replay fixtures pass and the ADR names the choice.
Downstream production structural commands depend on that decision; standalone input spikes do not.

## Undo and redo

Use Yrs selective history with explicitly tracked local origins.
Exclude remote updates, restore replay, checkpoint loading and presence from local history.
UndoManager groups by capture interval and origin; one transaction is not automatically one undo item.
Place explicit history boundaries around paste, formatting, structural move and composition groups.
Define typing coalescing separately; selection changes alone do not create content history.
Include newly created shared text in history scope when the chosen representation requires it.
Undo must preserve unrelated remote edits and produce ordinary persisted/synchronized updates.
Bound history memory; clearing history must not change current document content.
Cross-restart restoration of the full undo stack is outside the initial release contract.

## Persistence and synchronization ports

Updates carry document/session identity, writer identity, sequence and schema version.
Restore CRDT state and its journal tail; JSON/Markdown imports create a new explicit document/session.
Do not initialize a recovered document again while waiting for a network response.
Duplicate/reordered updates must be harmless; origins prevent adapter echo loops.
`localCommitted` follows successful storage transaction completion, never enqueue time.
`remoteCommitted` requires an identified durable service receipt, never a generic synced event.
Retain unacknowledged local updates and recovery content on failed or unauthorized upload.
Publish checkpoint coverage transactionally and retain the prior recovery point until safe replacement.
Storage errors are observable state; no false saved indicator is permitted.
Apply bounded decoding/resource checks to untrusted updates before admission.
Invalid schema/version input requires an explicit rejection or preserved recovery state, not silent repair.

## Required deterministic evidence

- Three replicas with operation reordering, duplicate delivery, disconnection and replay.
- Rust-to-JS and JS-to-Rust fixtures using the exact same edit-ac schema.
- Every structural race listed above, including all distinct arrival permutations in small cases.
- Invalid-command tests proving no partial content/history/persistence change.
- Unicode boundary, relative-anchor and undo-after-remote-edit fixtures.
- Crash/fault injection at journal, checkpoint and receipt commit boundaries.
- Fresh initialization versus restored/empty-but-existing document cases.
- Bounded resource behavior for malformed updates, deep content and fragmented marks.

Record failures and skips. Prepared fixtures establish deterministic correctness, not provider quality.
All tests remain local or use deterministic transports; no paid inference belongs in this engine.

## Primary references

- [Yrs compatibility and transaction lifecycle](https://docs.rs/yrs/latest/yrs/)
- [Yrs UTF-16 configuration](https://docs.rs/yrs/latest/yrs/types/text/trait.Text.html)
- [Yrs selective history](https://docs.rs/yrs/latest/yrs/undo/struct.UndoManager.html)
- [Yjs update contract](https://docs.yjs.dev/api/document-updates)
- [IndexedDB durability](https://w3c.github.io/IndexedDB/)

## Full-client compatibility contract

Follow-up [client contracts](client-contracts.md) build on these primitives for every native/terminal/host-agent client. Stable identities, prepared commands, anchors and update ports must remain usable without DOM, MCP or a particular store. Revision validation must account for deletions; a state vector alone is not an exact content token. Companion revision/history/security modules remain optional boundaries. The existing foundation roadmap is unchanged; new follow-up entry gates verify the frozen implementation before claiming compatibility.

## Atomic portable clipboard fragments

`prepare({kind: 'fragment', origin, range, blocks})` captures stable UTF-16 endpoints and stages all replacement, block splitting, presentation, inline marks and optional list/quote hierarchy on an isolated Rust replica. It admits the final complete update once through the existing editor commit boundary; failed/stale/bounded/schema preparation produces zero live edits. Versioned transfer data uses paragraph/heading/code blocks, six admitted inline marks with the existing URL policy, bounded container paths and checklist state. It carries no live owner/source identity, executable markup or native platform policy. One commit produces one patch/update and one explicit clipboard undo group. Full table/asset/reference/math transfer awaits qualified extension codecs under EXT-1.13 and FMT-1.13.

### Bounded fragment preflight reuse

The TypeScript handle may retain one prepared fragment plan across repeated `can`/`prepare` for identical validated serialized input. The plan is consumed by `prepare`, released when replaced or disposed, and invalidated before document mutations. Explicit history boundaries do not alter its document preconditions. Native commit still checks the exact replica identity, revision and checkpoint. This avoids preparing a clipboard batch repeatedly without weakening admission or creating document/history/subscriber effects during preflight.

### Atomic disjoint prepared source edits

`Document::prepare_source_edits` stages bounded disjoint source-derived text/format/presentation commands on an isolated replica, validates the final immutable structure/hierarchy, and returns one prepared update. No live transaction opens until `commit_editor` accepts the original exact identity/revision/checkpoint. Failure in a later staged edit leaves all live content, history, state vector and subscribers unchanged. `fragment_for_node` exposes portable supported runs/presentation/container data without allowing unknown mark data to be erased during preparation.
