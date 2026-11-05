# Alpha durability closures

These are required pre-publication corrections from the 2026-10-23 editor audit. They supplement [document durability](document-durability.md) and [block actions](block-actions.md). The [active adoption map](../runner-queues/alpha-block-actions-20261023/README.md) assigns delivery and final qualification. This document records observed risks and required outcomes, not completed fixes or release qualification.

## Table data must merge independently

The reviewed current table commands replaced the whole atom tuple; the rich-content contract allowed a whole-atom winner. A deterministic two-replica current-format probe edited separate cells to `LEFT EDIT` and `RIGHT EDIT`. Both replicas converged, but the left edit disappeared. Convergence alone is insufficient: edits to distinct cells must both survive.

DRA-1.1 specifies stable row/column/cell identities and independently mergeable cell content, including same-cell text, row/column insertion/deletion/reorder, retained conflicts, unknown metadata, undo and offline peers. DRA-1.2 implements that contract across the single current document and affected consumers. No whole-table winner, UI warning or disabled collaboration may substitute for preserving independent edits. Advanced table Turn into remains unavailable until an exact safe mapping exists; generic conversion must never flatten cells implicitly.

## Recovery journals must roll over transactionally

The reviewed browser checkpoint writer retained covered journal bytes, restore passed the complete journal to WASM, and the bridge rejected more than 4096 entries. A deterministic probe using an actual current engine and a checkpoint plus repeated valid updates reopened at 4096 entries and rejected at 4097. This exposes a lifetime failure even when the updates are already checkpointed.

DRA-1.3 must distinguish recovery coverage from outbound acknowledgement. A validated durable checkpoint may retire covered recovery entries only when its replacement and any retained fallback are crash-safe. The previous checkpoint needs its own recoverable tail. Unacknowledged outbox payloads must survive recovery compaction. Test publication and pruning failure boundaries, missing/corrupt latest checkpoints, duplicate/reordered updates, empty initialized documents, offline pending updates and at least three rollovers. Final proof uses actual installed WASM and IndexedDB, not only a memory store. Raising the entry bound does not close the defect.

## Structural history must support long-lived documents

The reviewed replay code bounded kinds and ownership-operation records at 4096 and controls at 8192, while validation required retained structural records to remain immutable and checkpoints serialized the full state. This is a code-level lifetime risk; the audit did not claim to have run the proposed long-session qualification.

DRA-1.4 defines the retention/replay policy before implementation, explicitly accounting for all retained roots, immutable witnesses, stable identities/anchors, revision and undo history, unknown data and disconnected replicas. DRA-1.5 implements it and demonstrates at least 16384 ordinary structural operations across multiple save/reopen cycles, with a peer disconnected across any retention boundary. A resource bound must protect decoding and live complexity without making a modest document fail merely because it has been edited repeatedly. If history compaction is chosen, prove eligibility, old-update admission and crash safety; do not silently discard offline edits, unknown peers or retained anchors. Merely lifting a constant is insufficient. Final resource/latency caps still apply.

## One current format and explicit adoption

Resolve these representation decisions before publishing the format. Use the current selector and one implementation per actual document/API/wire/ABI contract. Existing experimental readers and synthetic previous-release matrices are not runtime obligations. Useful regression assertions must run on current fixtures; keep unsupported-envelope negative tests and unknown-data/history preservation tests.

Current format identifiers already written to real checkpoints cannot be silently reinterpreted. Any necessary incompatible adoption must be explicit and offline, retain originals, produce a separately validated destination and prove semantic/opaque-data preservation under [decision 006](../decisions/006-single-format-before-publication.md). No automatic open-time migration, reseeding, cosmetic format-version proliferation or beta deferral closes a known alpha data-loss issue.

## Evidence and release ownership

Implementation parents use focused deterministic regressions. QSH owns complete core and installed cross-boundary coverage; QWB-1.5 owns full browser recovery; QWB-1.7 owns rich-content/table behavior; native owners execute applicable actual platform routes. BTQ owns the additional shared block-action semantic, extension and UI predicates. Reuse applicable passing results and run only missing or invalidated cases. No paid provider calls are permitted.

QRD-1.3 cannot declare alpha ready while an audit requirement lacks current implementation and nonzero final proof, or while original required full-suite/runtime/accessibility/performance gates remain open. Original 512 KiB total and 32 KiB editor-JS gzip caps are unchanged. Earlier oversized measurements are a follow-up lead, not a fresh benchmark or permission to delay independent feature delivery.
