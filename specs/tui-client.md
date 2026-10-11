# Native terminal editor client

Status: development contract; the terminal UI is planned, not implemented by the scaffold.

The Rust `editac` client gains a built-in terminal UI using the same document
sessions, commands, source reconciliation and persistence as its external-editor
mode. The terminal UI is a presenter over those services. It does not maintain a
second authoritative document and does not require an MCP connection to edit.
The [CLI contract](cli.md), [shared client contracts](client-contracts.md) and
[change/diff contract](change-diffs.md) own their respective behavior.

## Targets and opening

The intended entry point is `editac tui <target>`, preserving existing CLI
commands. Targets include local Markdown files, explicit literal UTF-8 files,
authorized hosted URLs supported by configured adapters, and `ac://DOC_ID`
references as specified by the shared URI contract. Missing files require an
explicit creation action. The local catalog resolves document identities before
optional service discovery; an existing cached document opens offline. An
uncached remote identity gives an unavailable result without creating an empty
replacement. Local file editing never uploads content merely because an online
profile is configured.

An `ac://` reference identifies a mutable document. It is neither a bearer
credential nor a promise of immutable content hashes. An authority profile is
configuration for an authorized host adapter; neither a URI nor an arbitrary
web-page URL grants read or write authority. The adapter supplies authorization,
document/epoch/schema identity and receipt capabilities. Do not reinterpret
unrecognized HTTP pages as editable hosted documents or put credentials in
references, document buffers, terminal output or diagnostic artifacts.

## Interaction and terminal ownership

Use a maintained Rust terminal backend only after a bounded decision records its
official documentation, exact versions, compiler requirements, platform support,
license, input/PTY behavior and compatibility with the pinned workspace. The
choice is uncommitted until that task passes. Reuse the selected backend's event
and drawing primitives; implement product session behavior in this repository.

The first interface contains a source buffer, selection/caret, target and save
status, command/help surface and optional change/conflict view. Support keyboard
navigation, multiline editing, bracketed paste, resize and clear focus ownership.
Decode terminal input separately from engine offsets: screen columns, Unicode
scalar values, grapheme clusters, source byte offsets and UTF-16 units are not
interchangeable. Combining characters, emoji/ZWJ, wide characters, tabs, CRLF,
zero-width content and bidirectional source need explicit rendering/caret rules.
Rendering must not emit untrusted document text as terminal control sequences.

Plain-text editing keeps text literal. Markdown editing retains the user's source
spelling and uses the shared prepared source-reconciliation API. No-op commits
preserve source bytes. Unsupported module content remains recoverable and is
displayed with an honest source/opaque fallback; viewing a fallback does not
authorize destructive normalization. Unknown data cannot disappear during copy,
save, diff, undo or reconnect.

## Prepared changes, history and review

Each editable buffer names its opening revision, exact source/projection and
identity/anchor mapping. On commit, prepare and validate changes through the
shared session API before one semantic history group and its local persistence
barrier. Rejected preparation preserves the live replica and edited source.
Undo/redo uses the shared origin-aware history, including explicit grouping
boundaries; terminal key handling never mutates the document independently.

Change views consume the shared diff result and disclose whether the comparison
is local source bytes, a hosted Markdown projection or semantic data. Show base
and current revision labels, unchanged context, added/deleted ranges and any
opaque-content limitation. The view is a review surface, not a second patch
engine. Applying a reviewed edit revalidates its baseline; stale previews cannot
authorize writes. Read-only capability disables all mutation routes, including
paste, undo/redo and command shortcuts, while allowing copy/export according to
host permissions.

## Concurrent updates and recoverability

Remote structured updates apply to the existing shared replica. A clean source
buffer may refresh from the new projection while restoring mapped selection.
For a dirty buffer, retain opening source, local candidate and current remote
projection. Reconcile provably disjoint changes using the shared FMT-1.12
identity/anchor rules; never silently replace the user's draft or submit stale
whole-document text. Overlap, deleted targets, incompatible epoch and ambiguous
mapping open a bounded three-way conflict view. An explicit resolution becomes
a newly prepared change against current state, with another stale check before
commit. Keep unresolved drafts exportable and recoverable across exit/crash.

Display locally committed, pending upload, remotely committed, remote durability
unknown, conflict, authorization failure and incompatible-state results
separately. Network absence or revocation does not discard local work. Reuse the
native journal/checkpoint/outbox and actual receipt matching; no terminal-specific
saved flag may outrun those services.

Raw mode, alternate screen, cursor visibility, event tasks and adapter sessions
have one owner and idempotent teardown. Normal quit, failed startup, I/O error,
interrupt and supported suspend/resume paths restore the terminal. A flush
failure exposes recoverable unsaved work and an explicit exit choice; quitting
cannot imply remote durability. Forced termination is covered by journal/draft
recovery rather than a promise to run signal handlers in every circumstance.

## Qualification and artifacts

Use deterministic screen/event tests and PTY-driven packaged-client tests with
fixed dimensions, scripted keys, prepared engine updates and mocked host/auth/
receipt transports. Cover local Markdown/text, no-op, cancel, source preservation,
diff/read-only, undo/redo, dirty-buffer remote edits, three-way resolution, offline
restart, storage failure, resize and teardown. Test terminal-control injection and
Unicode position conversions without relying on network access or credentials.

Declare the actual terminal/OS capability matrix. PTY simulation proves only its
tested behavior; real terminal and accessibility support claims need their own
recorded evidence. Package the existing Rust client with immutable shared-engine
dependencies and executable help/examples. TUI delivery does not require an
MCP server, mobile SDK or desktop publication. Publishing and final cross-client
qualification follow their owning release track; no paid provider calls or
production document writes are automated checks.
