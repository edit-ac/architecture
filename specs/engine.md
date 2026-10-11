# Shared engine contract

Status: development contract; structural representation remains behind an evidence gate.
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
- Persistence and synchronization consume immutable update bytes and metadata through ports.

## Compatibility profile

Start the compatibility spike with Yrs 0.28.0, Yjs 13.6.33 and y-protocols 1.0.7.
These pins are candidates until the lockfiles and interoperability evidence qualify them.
Enable Yrs `small-client` for the stable Yjs 13 line; the 0.28 default is different.
Set `OffsetKind::Utf16` explicitly in a single document-construction path.
Use update encoding v1 for the baseline; v2 requires a separate qualified profile.
Record schema version, document identity and session/epoch separately from transport identity.
Generate a distinct client ID for every independently editing live replica, including tabs.
Never restore one persisted writer ID into two simultaneously active writers.
Freeze root shared-type names and types with the schema decision.
Pin dependency versions and options in fixtures; upgrades rerun the compatibility suite.

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
