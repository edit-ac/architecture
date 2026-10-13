# Shared local-first client contracts

Status: planned portable interfaces, delivered by roadmap 12. Reuse engine, source reconciliation, storage/sync and CLI contracts. This document is an interface contract, not an implemented API.

## Document addressing

Document identity comprises opaque document ID, epoch/session and schema profile. Source identity is separate: a filesystem path, cached document, or configured authority locator can refer to the same document. Moving a file does not silently clone its collaboration identity; copying/importing creates a new explicit identity unless the host intentionally links it.

The frozen v1 locator grammar accepts `ac://<document-id>` for catalog resolution and `ac://<authority>/<document-id>` for a configured authority. Document IDs and epochs reuse the engine's canonical lowercase 36-byte hexadecimal UUID grammar. IDs are opaque, case-sensitive identities, not short hashes or content addresses. Uppercase UUIDs, Unicode (including normalization variants), percent encoding (including double encoding), whitespace, backslashes, dot segments, extra separators, userinfo, ports, queries and fragments reject rather than being decoded or silently normalized. Version queries are unsupported in v1. Canonical formatting round-trips the exact accepted form. Authorities are lowercase ASCII names of 1–63 bytes, starting with a letter, containing letters/digits/hyphens and ending with a letter/digit. They are host configuration keys, not arbitrary network hosts.

HTTPS app links are accepted only as `https://<configured-host>/ac/<document-id>` after the host explicitly maps that exact lowercase DNS host to a configured authority. DNS labels are 1–63 ASCII letters/digits/hyphens, without leading/trailing hyphens; the whole host is at most 253 bytes. No credentials, ports, queries, fragments, alternate prefixes or implicit redirects are accepted. Both input forms feed the same catalog resolver. Registering an authority or app-link host performs no network access and stores no credentials.

The local catalog maps an exact locator to a complete engine document identity (document ID, epoch, schema, profile, wire and offset metadata) and a host-selected source binding. Multiple locators may explicitly link to the same identity. Conflicting epochs/profiles for one document ID reject, including across authorities; rebinding an existing locator is not an implicit replacement/migration API. Local paths enter through a separate typed host-granted binding, never through URI text. The host must perform filesystem permission checks before inserting that binding. Moving a path is a host catalog operation; copying/importing requires explicit new identity. Engine profiles are validated using existing constructors; no schema migration is inferred.

Resolution is a read-only catalog lookup returning local/cached/hosted/locked/unavailable/unauthorized/incompatible outcomes. Unknown authorities reject even when an identically named document exists locally. An uncached hosted mapping returns unavailable offline and hosted metadata online; neither outcome fetches, initializes or creates a document. Cached populated and initialized-empty documents resolve identically, preserving their explicit existing identity. Policy states precede readiness. The resolver has no transport or document-creation port; a later lifecycle implementation must still restore/validate the actual checkpoint before editing. A locator contains no password, token or encryption key. Resolving arbitrary hosts or file paths cannot bypass host allowlists, path permissions or SSRF policy. Displaying or importing a link never performs an implicit network fetch. Launching an OS deep link requires host registration/activation policy; it cannot execute a shell command from URI text.

Executable grammar and catalog fixtures: `core/crates/editac-session/tests/locator.rs`, delivered under CAP-1.2-I1/V1 (the original parent acceptance remains unchanged).

## Local-first session

Provide a portable session companion to the engine with LocalStore, Transport, SourceResolver, AuthorizationPolicy and optional HistoryStore ports. IndexedDB, native transactional storage and CLI recovery implement the same journal/checkpoint/outbox conformance cases, without forcing a database crate or browser runtime into the semantic core. Promote CLI/native duplicated lifecycle logic into this shared boundary.

Opening a cached document first restores local state, then enables editing and optionally attaches networking. Creating a local document is offline and idempotent; subsequent hosting assigns an explicit authority mapping rather than re-importing content. An uncached offline hosted target returns unavailable. Local commands, undo/redo and readonly views never wait for a socket.

Expose restoring, ready, unsaved/pending local, locally committed, pending upload, synchronized-but-durability-unknown, remotely committed, conflict, locked and recovery-required states. Connectivity is orthogonal to durability. A completed local transaction is not an upload receipt. Native suspend/termination and browser tab close use the same recovery contract, without relying on an unload handler.

Sharing a database is not live synchronization. Cross-tab/process adapters exchange committed updates with distinct writer/client IDs and echo suppression. Test a pair of offline local clients plus reconnect to a hosted peer. Backpressure bounds memory and preserves an outbox rather than dropping acknowledged edits.

Hosts define offline authorization policy/leases. Offline revocation cannot retroactively remove already acquired plaintext. An expired policy may block further writes while retaining recovery data; a host cannot promise both unrestricted offline writes and instantaneous remote revocation. Upload always rechecks server authorization. Readonly is enforced by every mutation entry point, including MCP and imports, not just controls.

## Revision and edit admission

Return opaque revision tokens bound to a specific document/epoch/schema/profile and immutable observed state. A Yjs state vector alone is insufficient because deletions can change visible state without advancing the same clocks. Choose and test a persisted generation/content-state validator including deletion effects; tokens are not globally ordered wall clocks.

Compare expected revision and prepared preconditions within the serialized commit boundary. Equality protects the endpoint's observed state; it is not a global lock against offline peers whose updates arrive later. Surface subsequent merged changes normally. No direct `replaceDocument(markdown)` shortcut is allowed to defeat source reconciliation.

The shared editor service exposes read snapshot/capabilities, prepare semantic commands or source changes, preview, apply, observe changes and receipt lookup. It uses FMT-1.12's exact baseline/source-to-identity mapping. Unsupported or ambiguous mappings return recoverable base/proposed/current data. Capability checks include document permissions, module support, readonly/history mode and resource limits.

A post-commit persistence failure enters recovery mode: freeze further mutation admission and outbound synchronization until ordered durable recovery succeeds. Keep reads and labeled recovery exports available; bound queued incoming updates. Later human edits, checkpoints or full-state synchronization must not publish an unjournaled predecessor. When the predecessor is an agent request, its durable dedup receipt belongs to the same publication barrier; see the host-agent contract.

## Operation identity and history

Each admitted operation has a request/operation ID, authenticated actor supplied by the host, origin, affected identities and observed before/after revision. Actor metadata from document prose or a client-supplied display name is not trusted attribution. CRDT client IDs alone are not authenticated authors.

History origin policy separates local human gestures, other humans, agent operations, imports and replay. Agent operations can be reviewed/reverted as authorized new changes without becoming unintended human typing undo groups. Cross-client operation records feed diff/history views, but are not described as a tamper-proof audit ledger without additional evidence.

## Readiness evidence

Run identical prepared command/recovery fixtures through web, headless native and CLI session adapters. Require no-network local startup, empty existing document vs new document, multi-writer delivery, crash boundary recovery, quota/full-disk errors, disconnected auth failure, wrong epoch, stale revision and locked-document cases. No paid model calls or production account access is needed.

Implementation patterns and limits: [research](../evidence/followup-research.md). Related contracts: [storage/sync](storage-sync.md), [CLI](cli.md), [diffs](change-diffs.md), [host agents](agent-editing.md).

## Simulator/emulator development qualification

Controller decision, 2026-10-13: the user authorized "Lets unblock, emulator should do for now". A named iOS Simulator or Android Emulator running its platform browser is accepted for development clipboard qualification. This is a virtual-device result, not physical-device, real IME/accessibility or release support. Playwright mobile viewports, synthetic ClipboardEvent/InputEvent and prepared desktop event variants alone do not meet this emulator gate.

Roadmap 05 provides two qualification levels: its qualified portable FMT-1.1–FMT-1.14 behavior, including FMT-1.12, plus a passing virtual-device development receipt may unblock development tracks 08, 11, 12 and 21. FMT-1.15-V1 remains the mandatory physical-device release criterion; leave FMT-1.15 and roadmap 05 release completion open until it passes. Missing physical observations must not reblock those development tracks after the virtual gate passes. Other failed portable gates remain blockers. CAP-1.1 may execute the virtual gate as its next bounded development entry step rather than requiring a receipt before starting that step.

Use the procedure in tests/clipboard-emulator-development.md and record evidence under evidence/markdown/emulator-development/receipt.json. Require nonzero actually executed native clipboard cases, exact simulator/emulator/browser/OS versions, source/package hashes, semantic/history/storage observations, test counts, failures/skips and reproduction instructions. Missing or failed virtual cases cannot be marked passing. Retain previous physical-device BLOCKED receipts unchanged. Release/device owners later collect physical evidence against the then-current artifacts.
