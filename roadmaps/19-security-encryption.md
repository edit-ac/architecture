# Optional protected storage and encrypted collaboration

Status: IN_PROGRESS

Delivery sequencing (superseding user decision, 2026-10-18): follow [web → features → alpha → native → docs → qualification → native tests → beta → integrations](../operations/web-feature-first-20261018.md). All device/target-runtime observations in this source belong to [roadmap43](43-physical-device-verification.md), including simulator/emulator/OS/IME/AT/clipboard device matrices. They do not gate feature development. Original predicate text below remains the later verification contract; its transfer owner and exact paragraphs are in the [device requirement register](../operations/device-requirements-20261018.json). Feature tasks retain focused correctness/data-safety checks; exhaustive performance/platform/release qualification is later. Windows/Linux implementation waits for web feature completeness; cloud28 retains its explicit deferral. Historical source/progress/checkmarks/failures are not rewritten or declared complete.

## Goal and entry conditions

Workspace: `core`; paths below are core-relative unless prefixed `../architecture/`. Follow `../architecture/specs/security-encryption.md` and the active task context. This is planned follow-up delivery, not implemented capability.

Required upstream tracks: `12-client-contracts.md`, `13-change-diffs.md`, `21-extension-library.md` complete at reviewed source/implementation revisions with passing evidence. These supply the actual history and attachment adapters protected in SEC-1.8. Check these gates before launching; source dependencies below are local to this file.

## Execution rules

The controller owns this source. Write progress/checkmarks/evidence in the configured separate progress file. Each iteration implements at most one parent with its implementation and validation substeps. Aim for 15–45 minutes plus checks; if the boundary cannot fit, propose a stable controller-approved split before implementation. Use named fixtures/checks, creating planned test commands before running them. Missing checks, zero matches, failures and skips are not passing acceptance.

Use deterministic fixtures and mocked transports only; no paid model/provider calls, .secrets loading or production document writes. Other ready local tasks are permitted independent work. Unavailable device/toolchain/review evidence blocks its qualified claim, not unrelated platform work. Do not launch another runner or publish before an explicit release task.

## Epic SEC-1 — Optional protected storage and encrypted collaboration

### Task SEC-1.1 — Freeze threat model and profile boundaries

- [ ] SEC-1.1 Freeze threat model and profile boundaries.

Purpose: Freeze threat model and profile boundaries as one bounded reusable delivery boundary.
Context: `../architecture/decisions/003-encryption-profiles.md`; `../architecture/specs/security-encryption.md`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: none.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Document creation, offline revocation, agent access and attachment/history handling have explicit guarantees/limits; TLS is not labeled E2EE.

Implementation:

- [ ] SEC-1.1-I1 Specify baseline/local-at-rest/E2EE assets, attackers, trusted plaintext endpoints, metadata, membership/write permissions and recovery. Separate host server auth from encryption-key access.

Validation:

- [ ] SEC-1.1-V1 Review each stated attack/asset against a named invariant and planned fixture; record resolved/open design decisions. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `SEC-1.1` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `SEC-1.1`.
Blocked behavior: Leave `SEC-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task SEC-1.2 — Select and compile reviewed crypto protocol dependencies

- [ ] SEC-1.2 Select and compile reviewed crypto protocol dependencies.

Purpose: Select and compile reviewed crypto protocol dependencies as one bounded reusable delivery boundary.
Context: `crates/editac-security/`; `../architecture/evidence/crypto-selection.md`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: SEC-1.1.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Candidate compiles for intended WASM/native targets and has an independent-review plan; unresolved primitive/protocol design prevents production encryption code.

Implementation:

- [ ] SEC-1.2-I1 Evaluate maintained protocol/library candidates against actual membership, authenticated writers, key epochs and all target constraints; pin exact versions/lock/licenses after a bounded decision.

Validation:

- [ ] SEC-1.2-V1 Create `scripts/check-security-targets.mjs` and its explicit supported-target manifest; run `node scripts/check-security-targets.mjs --all`. The dispatcher invokes locked compile probes, rejects unknown or empty target sets and records unavailable targets as not qualified. Record exact exit results, nonzero target counts, failures/skips and artifact hashes.

Evidence: Separate progress entry `SEC-1.2` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `SEC-1.2`.
Blocked behavior: Leave `SEC-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task SEC-1.3 — Implement authenticated envelope admission

- [ ] SEC-1.3 Implement authenticated envelope admission.

Purpose: Implement authenticated envelope admission as one bounded reusable delivery boundary.
Context: `crates/editac-security/src/envelope.rs`; `crates/editac-security/tests/envelopes.rs`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: SEC-1.2.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Prepared wrong-key/tamper/replay/cross-document/counter-restore cases cannot apply plaintext updates; malicious read-only members cannot claim authenticated writes.

Implementation:

- [ ] SEC-1.3-I1 Use the selected protocol for authenticated document/epoch/schema/key-epoch/update envelopes, sender authorization, size limits and replay/nonce lifecycle. Keep core unaware of cryptographic implementation.

Validation:

- [ ] SEC-1.3-V1 cargo test -p editac-security --test envelopes --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `SEC-1.3` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `SEC-1.3`.
Blocked behavior: Leave `SEC-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task SEC-1.4 — Implement key-provider and locked-state ports

- [ ] SEC-1.4 Implement key-provider and locked-state ports.

Purpose: Implement key-provider and locked-state ports as one bounded reusable delivery boundary.
Context: `crates/editac-security/src/keys.rs`; `crates/editac-security/tests/key_lifecycle.rs`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: SEC-1.2.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Key absence never falls back to plaintext; loss/recovery behavior is honest; decoded key material is scoped and cleanup responsibilities are documented.

Implementation:

- [ ] SEC-1.4-I1 Define host key acquisition/wrapping/unlock/recovery interfaces with prepared providers and explicit locked/revoked/unavailable states. Prevent keys in locators, logs or tool responses.

Validation:

- [ ] SEC-1.4-V1 cargo test -p editac-security --test key_lifecycle --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `SEC-1.4` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `SEC-1.4`.
Blocked behavior: Leave `SEC-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task SEC-1.5 — Protect local journals and document creation

- [ ] SEC-1.5 Protect local journals and document creation.

Purpose: Protect local journals and document creation as one bounded reusable delivery boundary.
Context: `crates/editac-security/src/store.rs`; `crates/editac-security/tests/protected_store.rs`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: SEC-1.3, SEC-1.4.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Seeded plaintext never reaches stored blobs in encrypted mode, including first creation and failure fallback; crash recovery preserves acknowledged protected state.

Implementation:

- [ ] SEC-1.5-I1 Wrap the session store so creation, update journal/checkpoint/outbox and recovery are protected before publication. Add native/browser host adapter contracts without imposing a core dependency.

Validation:

- [ ] SEC-1.5-V1 cargo test -p editac-security --test protected_store --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `SEC-1.5` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `SEC-1.5`.
Blocked behavior: Leave `SEC-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task SEC-1.6 — Synchronize ciphertext with explicit receipts

- [ ] SEC-1.6 Synchronize ciphertext with explicit receipts.

Purpose: Synchronize ciphertext with explicit receipts as one bounded reusable delivery boundary.
Context: `crates/editac-security/src/sync.rs`; `crates/editac-security/tests/encrypted_sync.rs`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: SEC-1.5.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Opaque relay can store/acknowledge bounded ciphertext but never claims plaintext validation; incompatible peers fail closed and offline clients converge after authorized decrypt.

Implementation:

- [ ] SEC-1.6-I1 Negotiate encrypted profile, wrap updates before relay and decrypt/validate at authorized clients. Scope durable receipts to ciphertext identity and document/key epoch.

Validation:

- [ ] SEC-1.6-V1 cargo test -p editac-security --test encrypted_sync --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `SEC-1.6` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `SEC-1.6`.
Blocked behavior: Leave `SEC-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task SEC-1.7 — Handle rotation and offline membership changes

- [ ] SEC-1.7 Handle rotation and offline membership changes.

Purpose: Handle rotation and offline membership changes as one bounded reusable delivery boundary.
Context: `crates/editac-security/src/membership.rs`; `crates/editac-security/tests/rotation.rs`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: SEC-1.6.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Offline revoked clients cannot obtain new epoch access, already acquired plaintext is not claimed erased, and old pending data is not silently discarded or accepted.

Implementation:

- [ ] SEC-1.7-I1 Use selected protocol rotation/revocation rules for pending offline work, old epochs and future key access. Preserve rejected pending edits under the explicit recovery/export policy.

Validation:

- [ ] SEC-1.7-V1 cargo test -p editac-security --test rotation --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `SEC-1.7` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `SEC-1.7`.
Blocked behavior: Leave `SEC-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task SEC-1.8 — Protect revision history, attachments and exports

- [ ] SEC-1.8 Protect revision history, attachments and exports.

Purpose: Protect revision history, attachments and exports as one bounded reusable delivery boundary.
Context: `crates/editac-security/src/assets.rs`; `crates/editac-security/tests/assets.rs`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: SEC-1.5.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Seeded content is absent from unauthorized persistent artifacts/logs; missing old keys yield unavailable history instead of approximation; plaintext export cannot happen implicitly.

Implementation:

- [ ] SEC-1.8-I1 Apply the profile to attachment caches, history snapshots, backups and explicit recovery exports; label plaintext exports and require host authorization under document policy.

Validation:

- [ ] SEC-1.8-V1 cargo test -p editac-security --test assets --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `SEC-1.8` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `SEC-1.8`.
Blocked behavior: Leave `SEC-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task SEC-1.9 — Gate agent and host plaintext capabilities

- [ ] SEC-1.9 Gate agent and host plaintext capabilities.

Purpose: Gate agent and host plaintext capabilities as one bounded reusable delivery boundary.
Context: `crates/editac-security/src/capabilities.rs`; `crates/editac-security/tests/capabilities.rs`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: SEC-1.6, SEC-1.8.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Encrypted-mode capability fixtures reject incompatible host actions without downgrade; a permitted local endpoint uses the same readonly/edit authorization policy.

Implementation:

- [ ] SEC-1.9-I1 Expose whether a host endpoint can decrypt/export/diff/edit without granting keys implicitly. Refuse plaintext MCP/search/previews on an opaque relay and document local authorized routing.

Validation:

- [ ] SEC-1.9-V1 cargo test -p editac-security --test capabilities --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `SEC-1.9` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `SEC-1.9`.
Blocked behavior: Leave `SEC-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task SEC-1.10 — Publish protocol evidence and security review scope

- [ ] SEC-1.10 Publish protocol evidence and security review scope.

Purpose: Publish protocol evidence and security review scope as one bounded reusable delivery boundary.
Context: `../architecture/evidence/encryption.md`; `crates/editac-security/tests/profile_conformance.rs`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: SEC-1.7, SEC-1.9.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Mechanics evidence is complete and accurately limited; production encryption claims remain gated by roadmap24 review/platform evidence, not merely roundtrip success.

Implementation:

- [ ] SEC-1.10-I1 Run deterministic failure/tamper/no-downgrade suites and assemble exact protocol/dependency revisions, attack coverage and unresolved risks for independent review.

Validation:

- [ ] SEC-1.10-V1 cargo test -p editac-security --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `SEC-1.10` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `SEC-1.10`.
Blocked behavior: Leave `SEC-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.
