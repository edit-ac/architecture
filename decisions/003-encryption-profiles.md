# Decision 003: Optional protection profiles and plaintext authority

Status: accepted design boundary for SEC-1.1; encryption implementation and production qualification remain pending.

This decision supplements [the security specification](../specs/security-encryption.md). Its fixture plan is [security-profiles.json](../tests/security-profiles.json); its threat review is [security-threat-model.md](../evidence/security-threat-model.md). The other decision numbered 003 concerns extensions and remains unchanged.

## Profiles and assets

Baseline, local-at-rest and E2EE are explicit document/session profiles. Baseline requires host authentication, authorization, safe imports, bounds and transport confidentiality when networked; it promises no application-level at-rest confidentiality. Host services and storage administrators may see plaintext. TLS is transport protection, not E2EE.

Local-at-rest protects document creation, journals, checkpoints, outbox, revision snapshots, backups and attachment caches before persistent writes. Authorized running clients and explicitly configured plaintext synchronization services can read content. It does not protect plaintext from a compromised running host, nor provide encrypted collaboration merely because local files are encrypted.

E2EE protects those same assets before persistence and before transmission to remote storage or an opaque relay. Only explicitly authorized key-holding endpoints decrypt. This includes initial creation, restore, pending edits, previews and recovery paths. Locators, catalogs and transport routing carry no content or key material. Existing plaintext documents require an explicit conversion/import policy; choosing an encrypted profile does not erase historical plaintext, filesystem snapshots or host backups.

The profile is bound to document identity and the session contract. Unsupported versions, absent keys and incompatible peers fail closed with a visible state; neither reconnect nor recovery may select baseline as a fallback. The optional host adapter owns cryptography; the minimal semantic engine receives only admitted plaintext and gains no crypto dependency.

## Trusted endpoints and attackers

Trusted plaintext endpoints are the unlocked authorized client process, its explicitly authorized extensions, and any separately authorized decrypting host/agent endpoint. Local-at-rest additionally trusts its configured plaintext synchronization endpoint. Clipboard, display, accessibility, IME and explicit plaintext exports cross the host's existing policy boundary; they cannot be claimed confidential from that authorized host. An opaque E2EE relay is never such an endpoint.

Attackers include an unauthorized storage/backup reader, network observer, malicious or compromised relay, ciphertext injector, malicious read-only member, revoked former reader/writer, and caller with host credentials but no document keys. A compromised unlocked client, malicious authorized writer, endpoint supply-chain compromise, screen capture and exfiltration by an authorized export recipient remain outside the confidentiality guarantee. Membership limits cannot prevent an authorized reader copying plaintext. Denial of service, traffic analysis and global rollback cannot be claimed solved by content encryption.

## Creation and admission

Freeze profile and obtain the required key state before serializing the first document update. Encrypt before any journal/checkpoint/outbox/cache write or publish; key/encryption/storage failure aborts creation or leaves explicitly recoverable protected pending work. No error handler writes plaintext. Do not acknowledge local durability until the protected store's commit completes. Crash before commit may lose unacknowledged work; crash after acknowledged commit must recover the protected state through the ordinary journal/recovery contract.

Authenticated admission binds document ID, document epoch, schema, key epoch, sender and operation identity. Reject wrong key, tamper, cross-document/epoch/schema substitution, unauthorized writers and replay before the semantic engine applies bytes. Bound ciphertext size and decoded work before allocation/application. Crash, fork and counter restore must not reuse protocol nonces or silently reset replay protection. Selecting the reviewed protocol and exact lifecycle is SEC-1.2/1.3 work; no homegrown primitive, nonce scheme or group-key protocol is approved here. A restored client unable to establish safe freshness stays locked pending protocol-authorized recovery. A client with no trusted newer checkpoint cannot detect every malicious relay rollback or omission; receipts are not global freshness proofs.

An opaque relay may authenticate connections, enforce bounded metadata/rate limits, store ciphertext and issue a durable receipt scoped to ciphertext identity, document and key epoch. Such a receipt attests storage, never plaintext validity or convergence. Authorized clients independently verify/decrypt and perform normal semantic validation. Local persistence acknowledgment, remote storage receipt and semantic application are separate events.

## Metadata and authorization

Declared leakage includes document/routing identifiers, envelope sizes, counts, timing, connection addresses, participant/writer identifiers, epochs and access patterns, where required by the selected protocol/host. This design does not promise hidden membership, padded sizes or traffic anonymity. Titles, source text, attachment names/content and preview text are content, not implicitly public metadata. A host that intentionally publishes them needs explicit document policy authorization and must label that disclosure.

Host/server authentication, document membership, writer authorization and encryption-key access are distinct checks. A valid host token or locator grants no key; a decryption key grants no write role. Owner/admin policy authorizes membership, writer roles, export policy and key distribution through the eventual authenticated protocol. A malicious read-only key holder must be unable to manufacture an admitted writer update; a shared symmetric decrypt key alone cannot enforce this. Claims about actor identity remain limited to the host/protocol authentication actually verified, never an untrusted origin label.

## Keys, offline revocation and recovery

Hosts own acquisition, wrapping (OS keystore/browser mechanism), unlock, scoped decoded key use, retention, backup and deletion. Keys/passwords never enter locators, tool replies, logs or diagnostics. Locked, unavailable-key, revoked, recovery-required and incompatible states are explicit. Decoded key lifetimes must be bounded and cleanup ownership documented by SEC-1.4; managed runtimes, OS paging and crash dumps prevent a universal secure-erasure guarantee.

Revocation takes effect for future epoch key distribution and admission at the current authorized boundary. An offline revoked client cannot receive new keys when it reconnects. Revocation cannot erase already acquired keys, old ciphertext, plaintext or copies. An offline endpoint may remain unaware of revocation and continue displaying cached old content; it cannot claim current membership until it synchronizes authenticated membership state. Honest current members must not distribute future keys to excluded members, but collusion by an authorized reader is outside this guarantee.

Old-epoch pending edits are quarantined on reconnect until the selected protocol and current membership/write policy explicitly authorize rebase/re-encryption/admission. Never silently accept them as current writes or discard acknowledged local work. Preserve the protected pending payload and reason. Offer an explicit authorized recovery/export path, which may require an old key and current host authorization; a revoked writer has no promise of automatic reinsertion. Protocol choice must resolve concurrent membership changes and any safe old-epoch admission window; until resolved, reject admission and preserve the pending work. Losing every authorized retained key/recovery path makes content unrecoverable. Password reset or server authentication alone cannot reconstruct keys.

## History, attachments and exports

Revision history uses the actual immutable revision/storage adapters, not approximate reconstructions from current state. Bind protected snapshots/backups to document, revision and key epoch. Retain old keys only under explicit host retention policy; missing old keys produce unavailable-history, never fabricated content. A restore is a newly authorized edit, not permission to bypass current write policy.

Protect attachment bytes, names, cached thumbnails and previews before storage/publication; bind attachment identity/version and document/key epoch to authenticated content. References must not authorize arbitrary cache reads or cross-document substitution. Browser/native caches and extension-owned persistence participate in the same host protection policy. Undeclared persistent plaintext caches are disallowed in encrypted mode.

Encrypted backups are the default under protected profiles. Plaintext export, recovery export, clipboard transfer and external destination writes require an explicit user/host action authorized by document policy; they are labeled plaintext, with destination/disclosure identified. No automatic error recovery, background backup or unavailable-key path may trigger plaintext export. Export recipients and their downstream copies are trusted separately; deletion promises do not extend to them.

## Agent and host capabilities

Opaque relays refuse plaintext MCP, search, preview, diff, export and edit requests. They may expose bounded ciphertext transport/storage operations only. Hosts advertise whether an endpoint can decrypt and which document operations policy permits; capability discovery never delegates credentials or keys. A local authorized plaintext endpoint may serve agents after explicit host routing and document authorization, using the same read-only/edit/revision checks as an ordinary client. Agent edit permission cannot elevate export permission or membership. An agent sees only the authorized tool result, never key material. Incompatible actions fail visibly without profile downgrade or automatic rerouting to a decrypting service.

## Resolved and open decisions

Resolved: three explicit profiles; protected creation before all sinks; distinct authentication/decryption/writer authority; honest offline revocation; protected retained pending work; unavailable old history; explicit plaintext export; no opaque-relay plaintext tools; no implicit downgrade; separate receipt semantics. These are design requirements, not shipped guarantees.

Open SEC-1.2 decisions: maintained reviewed protocol and exact versions/licenses; authenticated writer and membership representation; native/WASM support; crash/fork/restore freshness; concurrency and old-epoch rules; independent reviewer and review scope. SEC-1.4 must qualify concrete platform wrapping/cleanup/recovery implementations. SEC-1.8 must bind actual history and attachment adapters. No protocol is selected by this ADR, and unresolved protocol design prevents production encryption code. SEC-1.10 assembles mechanics evidence; roadmap 24's independent review and platform evidence gate production claims. Deterministic contract checks and roundtrips provide no cryptographic security review or compliance certification.
