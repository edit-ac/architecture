# Exact change and revision views

Status: planned, roadmap 13. “Exact” identifies what is compared; it does not claim a unique diff algorithm or byte-preserving rich-text serialization.

## Three representations

1. **Source diff:** immutable original and edited UTF-8 bytes for a file/source session, including newline style, final newline and source spelling. Retain both hashes and explicit decode limits. Binary/invalid UTF-8 input returns a diagnostic.
2. **Projected Markdown diff:** deterministic serialized before/after rich documents, tagged with serializer/dialect versions. Show that serialization may normalize author spelling. Never label this the original source diff.
3. **Semantic diff:** stable node IDs, insertion/deletion/move, attributed text, marks, attributes and unknown/opaque content changes. Formatting, link targets and table structure remain visible even where Markdown cannot represent them.

CRDT binary update exchange is a fourth, internal transport representation; it is never substituted for these review views. Review can align text and semantic changes, but if alignment is ambiguous it must show separate views rather than fabricate correspondence.

## Immutable revisions and retention

Revision requests bind document/epoch/schema/module profile, observed-state token, representation type and hash. Store snapshots or reconstructable immutable history in a separate bounded HistoryStore. Capture named revisions/checkpoints on demand and materialize incremental history outside the typing path; do not serialize the entire document every keystroke.

A locally monotonic generation may label revisions but must be persisted and scoped; it is not a cross-replica total order. Deletion effects participate in exact revision validation. Availability after pruning, encryption key rotation or schema migration is explicit. Return unavailable/locked/incompatible for a missing revision, never approximate it from the current document. Yrs GC and UndoManager are not an archival history API.

## Patch contract

Pin deterministic line/word diff algorithms and options. A patch carries before/after hashes, representation/profile, limits and hunk ranges. Applying it to the exact baseline must yield byte-for-byte expected output and the expected hash. Wrong baseline, overlapping hunks, malformed lengths, missing context or output-limit violations fail without mutation. Git-like unified output is an interoperability format, not a promise that tie-breaking matches every Git version/options combination.

Use fixed `git diff --no-index` golden cases to validate conventional unified output; exit 1 means differences. Test repeated lines, CRLF/LF, missing final newline, Unicode/emoji/combining text, large replacements and moves. Text offsets exposed to the editor convert through UTF-16/anchor validation; terminal columns and UTF-8 bytes are distinct units.

Applying a reviewed hunk to a live collaborative document uses source reconciliation or stable semantic commands and current revision checks. It never patches serialized Markdown and re-imports the whole live document. “Accept all” means apply the validated proposal. Partial hunk application recomputes a valid semantic plan and rejects unsafe fragments (for example half a fenced block).

## Views and attribution

Provide accessible unified, inline and side-by-side web views; a portable changes model feeds native and terminal presenters. Readonly current, readonly historical and writable live modes are distinct. History checkout cannot rewind the live replica. “Restore this version” produces a new authorized edit against the current state with a preview and conflict result.

Show authenticated operation attribution only when supplied by a trusted host, otherwise mark it unknown/unverified. Separate human/agent/import/replay origins and semantic undo groups. A reconstructed snapshot diff says what differs, not necessarily who typed each character; concurrent history cannot be turned into a single causal narrative without evidence.

No-loss criteria cover content, marks, URLs, unknown modules, whitespace and structural identity. Bounded review history, source files and recovery artifacts inherit optional encryption/access policies. Logs do not contain confidential source by default.

Sources and implementation examples: [Yjs updates](https://docs.yjs.dev/api/document-updates), [Loro diff API](https://www.loro.dev/docs/api/js), [Git diff](https://git-scm.com/docs/git-diff), [research](../evidence/followup-research.md).
