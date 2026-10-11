# Security profiles and optional encryption

Status: planned optional profile, roadmap 19. Security applies to all modes; encryption is opt-in and must not expand the minimal core or silently change trust boundaries.

## Profiles

| Profile | What is protected | Remaining trust |
|---|---|---|
| Baseline | Authenticated/authorized access, safe imports, resource limits, transport confidentiality where networked | Host/services may process plaintext; local data follows host storage policy |
| Encrypted local store | Journal/checkpoints/history and attachment cache at rest | Authorized running client and any plaintext sync endpoint can read content |
| E2EE collaboration | Content encrypted before remote storage/transport, authenticated update envelopes | Authorized key-holding clients can read plaintext; relay observes declared metadata and availability |

TLS or disk encryption alone is not E2EE. Selecting E2EE must protect creation/restore, edits, backups, attachments, revision history, previews and recovery exports under a documented policy. Never upload an initial plaintext update before an encryption wrapper attaches. Metadata leakage (document IDs, sizes, timing, participants, routing) is explicitly listed.

## Design gate

Write a threat model, key/identity lifecycle and protocol selection ADR before choosing cryptographic dependencies. Use a maintained, reviewed implementation/protocol; do not invent primitives, nonce schemes or a bespoke group-key protocol. Compile and license/advisory-check the selected dependency on WASM and all native targets. A library's existence or passing round trip is not a security review.

Associate authenticated ciphertext with document/epoch/schema/key epoch and operation identity. Define tamper/replay handling, secure nonce uniqueness across crash/fork/restore, sender/write authorization distinct from decryption ability, membership/key rotation and attachment binding. Untrusted ciphertext cannot cause unbounded decode/allocation or be applied before verification. Design authenticated membership and writer signatures if the threat model requires them; a shared decrypt key alone must not be advertised as read-only enforcement against malicious peers.

## Keys and offline behavior

The host owns key acquisition, OS keystore/browser key wrapping, user unlock, backup/recovery, retention and deletion. Keys/passwords never appear in ac:// URLs, logs, crash diagnostics or MCP responses. Define locked, unavailable-key, revoked, recovery and incompatible-key states. Keep encrypted pending updates recoverable without plaintext fallback.

Offline revocation cannot erase keys/plaintext already acquired by a former reader. Define future-key exclusion and admission of offline writes from old epochs, including conflict/export/recovery paths. Do not silently discard acknowledged local work after rotation. Loss of all recovery material may make content unrecoverable; do not promise recovery without a retained authorized key path.

## Host and agent boundaries

A ciphertext-only server can enforce envelope size/rate/auth metadata and durably acknowledge stored ciphertext; it cannot validate plaintext schema, search it or generate plaintext previews/diffs. Authorized clients validate decrypted semantics. Hosted search, plaintext export and agent editing require an explicitly trusted decrypting endpoint or remain unavailable.

The application's existing MCP may expose Markdown tools only within that authorized plaintext boundary. Credentials and keys are not delegated merely because an agent can edit. Different encryption profiles cannot join the same session by silently downgrading; capability negotiation fails visibly.

## Qualification

Use deterministic prepared ciphertext/test keys and offline transports, never real secrets or paid model calls. Cover protected creation, wrong key, tamper, replay, crash before/after journal commit, rotation with an offline peer, revoked reader/writer, lost-key recovery, oversized inputs, encrypted attachments/history and unsupported peers. Search stored bytes/logs/exports for seeded plaintext leakage, while noting that such checks do not prove absence of all leaks.

An independent security review with a precise scope and resolved findings is required before claiming the encrypted profile production-ready. Unavailable review blocks that profile's claim, not ordinary unencrypted editor development. Neither profile offers a compliance certification.

Implementation examples and caveats: [research](../evidence/followup-research.md). Source for the protected-creation/opaque relay example: [Automerge Keyhive](https://automerge.org/docs/keyhive/ark-api-guide/); treat its actual protocol/API maturity as a selection-gate question, not a preapproved dependency.
