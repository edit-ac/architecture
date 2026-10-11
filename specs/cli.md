# Local-first CLI editor client

Status: development contract; editing and hosted connectivity are planned, not implemented by the current scaffold.
Scope: the `editac` client in `edit-ac/cli`, consuming the shared Rust engine and Markdown implementation.

## User workflow and targets

The CLI is an editor client for local text and online hosted documents. Markdown is the user-facing editable representation. Local editing requires neither an account nor a network connection; hosting adds synchronization to the same editing workflow.

The initial interaction opens a working text file in an explicitly configured editor, then `$VISUAL` or `$EDITOR`. A built-in terminal UI is a separately scoped follow-up. Run the configured executable with arguments and the file path; document configuration parsing and never interpolate document contents or targets into a shell command. Missing editor configuration, editor failure and cancellation return actionable results without committing changes.

The planned command surface is:

- `editac edit <path>` opens or explicitly creates a local Markdown document. An existing file is an edit target; creating a missing file requires `--create`.
- `editac edit <path> --format text` edits literal UTF-8 text without interpreting Markdown. `.txt` targets default to literal text; `.md` targets default to Markdown. Other suffixes require an explicit format.
- `editac edit <hosted-document-url>` opens an authorized edit.ac-compatible hosted document, or its existing local cache when offline. The configured service adapter resolves document identity; an arbitrary HTTP page is not a writable document API.
- `editac status <target>` reports local persistence, pending synchronization and remote durability separately.
- `editac sync <hosted-document-url>` explicitly retries pending work using the configured adapter. Local file editing never attaches a transport implicitly.

These names are planned contracts, not executable examples for the scaffold. Help advertises only implemented capabilities. Validation/conversion/inspection remain secondary operations; JSON and CRDT bytes are not the user's editing buffer.

## Markdown and shared state

Use the dialect, safety limits and diagnostics in [formats](formats.md). Literal text mode retains literal text and does not run Markdown typing shortcuts. One Yrs replica owns committed semantics during a session. The source buffer and parsed candidates are temporary input projections, as native text controls are in other hosts; there is no parallel writable editor model.

Keep the exact source baseline alongside semantic identities and stable anchors. Compare edited source with that baseline, prepare a bounded semantic change using the shared Rust parser/engine, validate it, then commit through the shared command/history boundary. A no-op preserves file bytes, whitespace and source spelling. Successful local source edits preserve the user's edited Markdown spelling; normalized Markdown serialization is an explicit export action. Importing a local file into a fresh session is permitted; re-importing a whole hosted snapshot on each save is not.

The shared source-reconciliation API must be qualified before advertising editing: source ranges alone do not prove stable identity mapping. Preserve unchanged nodes, marks and unknown module data. If a proposed Markdown change cannot retain unsupported semantics or map safely to current anchors, reject the commit with diagnostics and retain the edited source for recovery. A deliberate lossy export must be a separate explicit action. Invalid UTF-8, malformed input, resource-limit failures and rejected edits never partially mutate the live document.

Hosted exports use the deterministic Markdown representation, not the original author's source spelling. Retain the opening projection and its identity/anchor mapping as the edit baseline. Parse only user-edited source; received structured updates go directly into the existing replica. Source editing does not reinterpret remote updates as Markdown or reset collaborative history/epoch.

## Local files and recovery

Ordinary local text files are portable inputs and outputs, usable with other editors. Cache/journal files are recoverable session state, not a mandatory proprietary document container. New files remain local unless the user explicitly chooses a hosted destination; editing a local path must not upload content.

Capture target identity and content fingerprint when opening. Before publishing an edit, verify the baseline has not been replaced or changed. Use a cooperating client lock and same-directory temporary write, flush, atomic publication and the supported platform's directory durability mechanism. Refuse a detected external edit or replacement; retain both the user's candidate and current target for explicit resolution. Document the limit of conflict detection with non-cooperating external writers; an atomic rename alone is not a compare-and-swap. Do not silently follow a changed symlink or overwrite an unrelated destination. The normal save authorizes changes to the opened target; export to an existing different path requires an explicit overwrite option.

An unchanged buffer or canceled session leaves the original untouched. Failures before publication preserve the original and recoverable draft. Report local saved status only after the tested durability boundary, and report uncertain publication explicitly. Retain recovery data until that boundary succeeds. UTF-8/Unicode, line-ending policy, file permissions, missing/read-only targets, full disk and process interruption need deterministic fixtures.

For hosted documents, persist CRDT checkpoint, journal, pending update identities and bytes using a native adapter for [storage/sync](storage-sync.md). Keep drafts that have not yet passed semantic reconciliation separately from committed updates. Local Markdown export does not replace the checkpoint or outbox. Restore once with a distinct live replica/writer identity; subsequent network attachment must not initialize a second document.

## Hosted documents and concurrency

Use a configured service adapter with explicit endpoint, document ID, schema and epoch. Reuse saved credentials through the configured credential store; authentication and authorization remain service responsibilities. Keep tokens out of document files, working buffers and diagnostic output. No production service, new server protocol or automatic background daemon is implied by this client plan.

First open requires an authorized bootstrap; cached documents can be edited offline. Persist local changes before sending them, retain the outbox across exit/crash, and reuse the qualified sync protocol and receipt semantics. Authentication failure, revocation or unavailable service leaves local work recoverable and exportable. An uncached offline target returns a clear unavailable result rather than an empty editable replacement.

While the editor buffer is open, remote changes may advance the replica. Revalidate source-derived changes against current anchors before commit. Disjoint proven mappings may merge through the shared engine; overlapping changes, deleted targets or ambiguous source mappings produce an explicit conflict with retained base/local/current representations. Never overwrite the hosted document with stale full-text Markdown or claim CRDT synchronization resolves an arbitrary whole-source replacement.

Expose at least locally saved, pending upload, remotely committed, remote durability unknown, conflict, authorization failure and incompatible schema/epoch. `remoteCommitted` requires the negotiated durable application receipt; socket delivery or a matching state vector is insufficient. Services without receipts may synchronize but cannot be reported as remotely saved. Schema/epoch mismatch requires an explicit supported transition and must not discard old offline edits.

## Delivery and qualification

Local editing depends on the qualified engine and Markdown contracts. Native persistence is implemented in the CLI track; browser IndexedDB code is not reused as a native filesystem adapter. Hosted tasks additionally require the qualified synchronization track at the current revision. These are staged gates so an unavailable host does not block local delivery. CLI release remains independent of browser package publication and native UI parity.

Use prepared fixtures, a fake editor executable and mocked service/auth/receipt transports. Cover local Markdown and literal text, no-op/cancel, source preservation, supported semantic changes, unknown content, stale file save, crash recovery, cached offline edit, concurrent hosted edits, reconnect, revocation and wrong/missing receipts. Record actual executed/passed/failed/skipped counts and preserved failures. No paid inference, live credential loading or production hosted writes belong in automated qualification.

## Full client follow-up

Roadmap 15 delivers the built-in TUI in [tui-client](tui-client.md), reusing this external-editor/local/hosted baseline and [shared client contracts](client-contracts.md). Both clients accept validated ac:// document locators through the same catalog/authority resolver; IDs are not bearer credentials. Diff preview uses [change-diffs](change-diffs.md). Host-app MCP is a separate adapter and is not required to use or release the CLI/TUI.
