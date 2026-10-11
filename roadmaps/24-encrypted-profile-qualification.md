# Qualify the optional encrypted client profile

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core`; paths below are core-relative unless prefixed `../architecture/`. Follow `../architecture/specs/security-encryption.md` and the active task context. This is planned follow-up delivery, not implemented capability.

Required upstream tracks: `19-security-encryption.md`, `20-product-scenarios.md` complete at reviewed source/implementation revisions with passing evidence. Check these gates before launching; source dependencies below are local to this file.

## Execution rules

The controller owns this source. Write progress/checkmarks/evidence in the configured separate progress file. Each iteration implements at most one parent with its implementation and validation substeps. Aim for 15–45 minutes plus checks; if the boundary cannot fit, propose a stable controller-approved split before implementation. Use named fixtures/checks, creating planned test commands before running them. Missing checks, zero matches, failures and skips are not passing acceptance.

Use deterministic fixtures and mocked transports only; no paid model/provider calls, .secrets loading or production document writes. Other ready local tasks are permitted independent work. Unavailable device/toolchain/review evidence blocks its qualified claim, not unrelated platform work. Do not launch another runner or publish before an explicit release task.

## Epic ENC-1 — Qualify the optional encrypted client profile

### Task ENC-1.1 — Freeze encrypted profile deployment and trust matrix

- [ ] ENC-1.1 Freeze encrypted profile deployment and trust matrix.

Purpose: Freeze encrypted profile deployment and trust matrix as one bounded reusable delivery boundary.
Context: `../architecture/evidence/encrypted-profile.md`; `fixtures/security/profile-matrix.json`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: none.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Profile labels map to exact implemented functions; opaque relays do not advertise plaintext agents/search and no platform inherits encryption support by implication.

Implementation:

- [ ] ENC-1.1-I1 Add the encrypted scenarios/evidence checks to the existing manifest-driven dispatcher, with no synthetic review pass. Specify which actual platforms/hosts offer local encryption or E2EE, authorized plaintext endpoints, key custody, metadata disclosure and recovery. Require protocol evidence from roadmap19.

Validation:

- [ ] ENC-1.1-V1 node tests/scenarios/run.mjs encrypted-profile-matrix. Assert all acceptance cases; record exact command/exit, nonzero executed/passed/failed/skipped counts, fixture/revision hashes and unavailable-platform evidence.

Evidence: Separate progress entry `ENC-1.1` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `ENC-1.1`.
Blocked behavior: Leave `ENC-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task ENC-1.5 — Implement and qualify browser key wrapping

- [ ] ENC-1.5 Implement and qualify browser key wrapping.

Purpose: Protect browser document keys through the selected profile without claiming native-keystore or XSS guarantees.
Context: `packages/web/src/security/key-provider.ts`; `tests/browser/security-keys.spec.ts`; `tests/scenarios/run.mjs`; `tests/manual/security-browser.md`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: ENC-1.1.
Session scope: One host adapter or evidence boundary, 15–45 minutes plus focused checks. Reuse qualified key ports/protocol and existing host harnesses; propose a controller split before adding another provider or cryptographic mechanism.
Acceptance: The selected browser wrapping/persistence provider passes real-browser create/unlock/lock/reload, unavailable/wrong/lost-key and authorized recovery cases. Declared persistence/eviction and authorized-page limitations are explicit; no missing capability silently stores plaintext or an unwrapped document key.

Implementation:

- [ ] ENC-1.5-I1 Bind the selected profile to the existing browser key port using its approved wrapping/unlock mechanism. Add key-provider-browser to the scenario dispatcher, invoking actual browser tests and verifying named manual evidence; record behavior on the exact claimed browser versions. Do not design a new wrapping scheme in this task.

Validation:

- [ ] ENC-1.5-V1 node tests/scenarios/run.mjs key-provider-browser; execute tests/manual/security-browser.md with isolated prepared test material. Assert protected-store inspection, reload recovery and visible locked/unavailable states. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, profile/provider/platform revisions and fixture/artifact hashes. Missing required real-provider cases remain unchecked; mock success cannot qualify an OS/browser key provider.

Evidence: Separate progress entry `ENC-1.5` links changed files, source/implementation revisions, scenario IDs, provider capability evidence and preserved failures. Use isolated prepared test keys only; never retain live key material or secrets in artifacts.
Handoff: Last completed substep, exact host/provider case, relevant symbol, remaining acceptance and next bounded action for `ENC-1.5`.
Blocked behavior: Leave `ENC-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, missing host/provider/tooling, explicit unblock condition and bounded retry trigger. Other independent host tasks remain eligible in later iterations; do not poll unavailable hosts or count excluded/skipped cases as passed.

### Task ENC-1.6 — Implement and qualify iOS key storage

- [ ] ENC-1.6 Implement and qualify iOS key storage.

Purpose: Connect the iOS host to its approved OS key provider and explicit recovery behavior.
Context: `native/ios/security/`; `native/ios/tests/security-keys/`; `native/ios/scripts/check.sh`; `tests/scenarios/run.mjs`; `tests/manual/security-ios.md`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: ENC-1.1.
Session scope: One host adapter or evidence boundary, 15–45 minutes plus focused checks. Reuse qualified key ports/protocol and existing host harnesses; propose a controller split before adding another provider or cryptographic mechanism.
Acceptance: The actual supported iOS key provider passes create/unlock/lock/app-restart, unavailable/wrong/lost-key and authorized restore cases with declared access-control/backup behavior. Device-only claims have device evidence; simulator results do not establish those claims.

Implementation:

- [ ] ENC-1.6-I1 Implement the thin iOS key-port adapter for the selected profile, using existing lifecycle/error contracts. Add the security-keys native suite and key-provider-ios scenario that invokes it and validates manual receipts. Keep test key items isolated and clean them after evidence collection.

Validation:

- [ ] ENC-1.6-V1 node tests/scenarios/run.mjs key-provider-ios; execute tests/manual/security-ios.md on required declared devices. Assert locked-state behavior, app restart/recovery and denied/unavailable access without plaintext fallback. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, profile/provider/platform revisions and fixture/artifact hashes. Missing required real-provider cases remain unchecked; mock success cannot qualify an OS/browser key provider.

Evidence: Separate progress entry `ENC-1.6` links changed files, source/implementation revisions, scenario IDs, provider capability evidence and preserved failures. Use isolated prepared test keys only; never retain live key material or secrets in artifacts.
Handoff: Last completed substep, exact host/provider case, relevant symbol, remaining acceptance and next bounded action for `ENC-1.6`.
Blocked behavior: Leave `ENC-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, missing host/provider/tooling, explicit unblock condition and bounded retry trigger. Other independent host tasks remain eligible in later iterations; do not poll unavailable hosts or count excluded/skipped cases as passed.

### Task ENC-1.7 — Implement and qualify Android key storage

- [ ] ENC-1.7 Implement and qualify Android key storage.

Purpose: Connect the Android host to its approved OS key provider without overstating hardware protection.
Context: `native/android/security/`; `native/android/tests/security-keys/`; `native/android/scripts/check.sh`; `tests/scenarios/run.mjs`; `tests/manual/security-android.md`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: ENC-1.1.
Session scope: One host adapter or evidence boundary, 15–45 minutes plus focused checks. Reuse qualified key ports/protocol and existing host harnesses; propose a controller split before adding another provider or cryptographic mechanism.
Acceptance: Actual Android provider create/unlock/lock/process-restart, unavailable/wrong/lost-key and authorized recovery cases pass for declared API/device profiles. Key invalidation and hardware-backed versus software-backed capability are recorded as observed; unavailable capabilities never trigger an insecure fallback.

Implementation:

- [ ] ENC-1.7-I1 Implement the Android key-port adapter using the selected profile and existing typed lifecycle/error states. Add security-keys to the native dispatcher and key-provider-android to the product dispatcher with real provider cases and named manual evidence; isolate and remove prepared test aliases.

Validation:

- [ ] ENC-1.7-V1 node tests/scenarios/run.mjs key-provider-android; execute tests/manual/security-android.md on required declared devices. Assert provider invalidation, process restart and recovery behavior with prepared test keys. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, profile/provider/platform revisions and fixture/artifact hashes. Missing required real-provider cases remain unchecked; mock success cannot qualify an OS/browser key provider.

Evidence: Separate progress entry `ENC-1.7` links changed files, source/implementation revisions, scenario IDs, provider capability evidence and preserved failures. Use isolated prepared test keys only; never retain live key material or secrets in artifacts.
Handoff: Last completed substep, exact host/provider case, relevant symbol, remaining acceptance and next bounded action for `ENC-1.7`.
Blocked behavior: Leave `ENC-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, missing host/provider/tooling, explicit unblock condition and bounded retry trigger. Other independent host tasks remain eligible in later iterations; do not poll unavailable hosts or count excluded/skipped cases as passed.

### Task ENC-1.8 — Implement and qualify macOS key storage

- [ ] ENC-1.8 Implement and qualify macOS key storage.

Purpose: Bind the macOS host to its approved OS credential/key service and lifecycle.
Context: `native/macos/security/`; `native/macos/tests/security-keys/`; `native/macos/scripts/check.sh`; `tests/scenarios/run.mjs`; `tests/manual/security-macos.md`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: ENC-1.1.
Session scope: One host adapter or evidence boundary, 15–45 minutes plus focused checks. Reuse qualified key ports/protocol and existing host harnesses; propose a controller split before adding another provider or cryptographic mechanism.
Acceptance: Actual macOS provider create/unlock/lock/application-restart, denied/unavailable/lost-key and authorized restore cases pass. Access prompts, key custody and backup/export policy match the profile; state and logs contain no key material or silent plaintext fallback.

Implementation:

- [ ] ENC-1.8-I1 Implement the macOS key-port adapter and security-keys suite using existing app session boundaries. Add key-provider-macos to the scenario dispatcher, invoking real provider tests and checking manual evidence. Use a namespaced isolated test item and explicit teardown.

Validation:

- [ ] ENC-1.8-V1 node tests/scenarios/run.mjs key-provider-macos; execute tests/manual/security-macos.md on the declared OS. Check locked/denied behavior, application restart, protected recovery and artifact inspection. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, profile/provider/platform revisions and fixture/artifact hashes. Missing required real-provider cases remain unchecked; mock success cannot qualify an OS/browser key provider.

Evidence: Separate progress entry `ENC-1.8` links changed files, source/implementation revisions, scenario IDs, provider capability evidence and preserved failures. Use isolated prepared test keys only; never retain live key material or secrets in artifacts.
Handoff: Last completed substep, exact host/provider case, relevant symbol, remaining acceptance and next bounded action for `ENC-1.8`.
Blocked behavior: Leave `ENC-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, missing host/provider/tooling, explicit unblock condition and bounded retry trigger. Other independent host tasks remain eligible in later iterations; do not poll unavailable hosts or count excluded/skipped cases as passed.

### Task ENC-1.9 — Implement and qualify Windows key storage

- [ ] ENC-1.9 Implement and qualify Windows key storage.

Purpose: Bind the Windows host to the selected user/device protection profile.
Context: `native/windows/security/`; `native/windows/tests/security-keys/`; `native/windows/scripts/check.ps1`; `tests/scenarios/run.mjs`; `tests/manual/security-windows.md`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: ENC-1.1.
Session scope: One host adapter or evidence boundary, 15–45 minutes plus focused checks. Reuse qualified key ports/protocol and existing host harnesses; propose a controller split before adding another provider or cryptographic mechanism.
Acceptance: The actual Windows provider passes create/unlock/lock/process-restart, unavailable/wrong-context/lost-key and authorized restore cases. User/device binding and recovery limits are explicit; moving protected data to an unauthorized context does not unlock it or produce an empty replacement.

Implementation:

- [ ] ENC-1.9-I1 Implement the Windows key-port adapter against the selected profile, reusing native typed errors and session lifecycle. Add the security-keys PowerShell suite and key-provider-windows scenario with real provider/manual evidence. Isolate test credentials/data and remove only the task-created entries without modifying unrelated user credentials.

Validation:

- [ ] ENC-1.9-V1 node tests/scenarios/run.mjs key-provider-windows; execute tests/manual/security-windows.md on the declared Windows host. Assert context binding, process restart/recovery and no secret-bearing output. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, profile/provider/platform revisions and fixture/artifact hashes. Missing required real-provider cases remain unchecked; mock success cannot qualify an OS/browser key provider.

Evidence: Separate progress entry `ENC-1.9` links changed files, source/implementation revisions, scenario IDs, provider capability evidence and preserved failures. Use isolated prepared test keys only; never retain live key material or secrets in artifacts.
Handoff: Last completed substep, exact host/provider case, relevant symbol, remaining acceptance and next bounded action for `ENC-1.9`.
Blocked behavior: Leave `ENC-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, missing host/provider/tooling, explicit unblock condition and bounded retry trigger. Other independent host tasks remain eligible in later iterations; do not poll unavailable hosts or count excluded/skipped cases as passed.

### Task ENC-1.10 — Implement and qualify Linux key storage

- [ ] ENC-1.10 Implement and qualify Linux key storage.

Purpose: Support the selected Linux key provider while making absent or locked desktop services explicit.
Context: `native/linux/security/`; `native/linux/tests/security-keys/`; `native/linux/scripts/check.sh`; `tests/scenarios/run.mjs`; `tests/manual/security-linux.md`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: ENC-1.1.
Session scope: One host adapter or evidence boundary, 15–45 minutes plus focused checks. Reuse qualified key ports/protocol and existing host harnesses; propose a controller split before adding another provider or cryptographic mechanism.
Acceptance: Actual declared Linux provider create/unlock/lock/process-restart, missing-service/denied/lost-key and authorized restore cases pass. Supported desktop/session environments are named; headless or missing-provider cases remain locked/unavailable and never fall back to plaintext key files.

Implementation:

- [ ] ENC-1.10-I1 Implement the Linux key-port adapter for the approved provider and existing session/error contracts. Add security-keys and key-provider-linux dispatcher suites with actual service tests plus manual receipts. Keep isolated test secrets separate from personal items and verify cleanup.

Validation:

- [ ] ENC-1.10-V1 node tests/scenarios/run.mjs key-provider-linux; execute tests/manual/security-linux.md on each declared provider/environment. Assert missing-service behavior, restart/recovery and protected artifact inspection. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, profile/provider/platform revisions and fixture/artifact hashes. Missing required real-provider cases remain unchecked; mock success cannot qualify an OS/browser key provider.

Evidence: Separate progress entry `ENC-1.10` links changed files, source/implementation revisions, scenario IDs, provider capability evidence and preserved failures. Use isolated prepared test keys only; never retain live key material or secrets in artifacts.
Handoff: Last completed substep, exact host/provider case, relevant symbol, remaining acceptance and next bounded action for `ENC-1.10`.
Blocked behavior: Leave `ENC-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, missing host/provider/tooling, explicit unblock condition and bounded retry trigger. Other independent host tasks remain eligible in later iterations; do not poll unavailable hosts or count excluded/skipped cases as passed.

### Task ENC-1.11 — Integrate and qualify terminal key-provider UX

- [ ] ENC-1.11 Integrate and qualify terminal key-provider UX.

Purpose: Expose secure unlock/recovery through the CLI/TUI using already-qualified desktop providers.
Context: `../cli/src/security/key_provider.rs`; `../cli/tests/security_keys.rs`; `../cli/tests/tui_security_pty.rs`; `tests/scenarios/run.mjs`; `tests/manual/security-terminal.md`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: ENC-1.8, ENC-1.9, ENC-1.10.
Session scope: One host adapter or evidence boundary, 15–45 minutes plus focused checks. Reuse qualified key ports/protocol and existing host harnesses; propose a controller split before adding another provider or cryptographic mechanism.
Acceptance: The packaged terminal client uses the declared qualified provider on each supported desktop OS. Unlock/lock/restart/lost-key/recovery states are explicit; PTY input is non-echoing and keys never enter command arguments, ac URLs, buffers, logs or MCP results. Missing/denied provider access remains recoverable without plaintext fallback.

Implementation:

- [ ] ENC-1.11-I1 Bind the existing terminal session/key port to the qualified host providers, reusing platform storage rather than implementing another keystore. Add non-echoing unlock and protected recovery activation with cancel/error cleanup. Register key-provider-terminal to run packaged-client PTY/provider checks and verify actual-host manual receipts.

Validation:

- [ ] ENC-1.11-V1 node tests/scenarios/run.mjs key-provider-terminal; execute tests/manual/security-terminal.md with the packaged binary on declared desktop hosts. Assert PTY/no-echo behavior with prepared input, terminal restoration and actual provider routing/recovery. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, profile/provider/platform revisions and fixture/artifact hashes. Missing required real-provider cases remain unchecked; mock success cannot qualify an OS/browser key provider.

Evidence: Separate progress entry `ENC-1.11` links changed files, source/implementation revisions, scenario IDs, provider capability evidence and preserved failures. Use isolated prepared test keys only; never retain live key material or secrets in artifacts.
Handoff: Last completed substep, exact host/provider case, relevant symbol, remaining acceptance and next bounded action for `ENC-1.11`.
Blocked behavior: Leave `ENC-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, missing host/provider/tooling, explicit unblock condition and bounded retry trigger. Other independent host tasks remain eligible in later iterations; do not poll unavailable hosts or count excluded/skipped cases as passed.

### Task ENC-1.2 — Aggregate qualified platform key coverage

- [ ] ENC-1.2 Aggregate qualified platform key coverage.

Purpose: Join host-specific key custody and recovery evidence before encrypted collaboration claims.
Context: `fixtures/security/profile-matrix.json`; `tests/scenarios/run.mjs`; `../architecture/evidence/encrypted-profile.md`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: ENC-1.5, ENC-1.6, ENC-1.7, ENC-1.8, ENC-1.9, ENC-1.10, ENC-1.11.
Session scope: One host adapter or evidence boundary, 15–45 minutes plus focused checks. Reuse qualified key ports/protocol and existing host harnesses; propose a controller split before adding another provider or cryptographic mechanism.
Acceptance: Every required browser/iOS/Android/macOS/Windows/Linux/terminal key-provider cell maps to current passing real-host evidence and the selected threat model. Provider limitations and unqualified capabilities are explicit; missing devices/providers cannot be replaced with mocks or dropped from required coverage.

Implementation:

- [ ] ENC-1.2-I1 Register the platform-keys aggregation scenario over the seven host evidence manifests. Verify profile/provider versions, artifact hashes, executed/passed/failed/skipped counts and required real-provider/manual receipts; report stale or missing cells without rerunning unchanged host suites or implementing another adapter.

Validation:

- [ ] ENC-1.2-V1 node tests/scenarios/run.mjs platform-keys. Verify that the aggregation rejects missing, stale, skipped-required and mock-only evidence; inspect all required host coverage against ENC-1.1. Record exact commands/exits, nonzero executed/passed/failed/skipped counts, profile/provider/platform revisions and fixture/artifact hashes. Missing required real-provider cases remain unchecked; mock success cannot qualify an OS/browser key provider.

Evidence: Separate progress entry `ENC-1.2` links changed files, source/implementation revisions, scenario IDs, provider capability evidence and preserved failures. Use isolated prepared test keys only; never retain live key material or secrets in artifacts.
Handoff: Last completed substep, exact host/provider case, relevant symbol, remaining acceptance and next bounded action for `ENC-1.2`.
Blocked behavior: Leave `ENC-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with owner, missing host/provider/tooling, explicit unblock condition and bounded retry trigger. Other independent host tasks remain eligible in later iterations; do not poll unavailable hosts or count excluded/skipped cases as passed.

### Task ENC-1.3 — Qualify encrypted collaboration and authorized agent edits

- [ ] ENC-1.3 Qualify encrypted collaboration and authorized agent edits.

Purpose: Qualify encrypted collaboration and authorized agent edits as one bounded reusable delivery boundary.
Context: `tests/scenarios/encrypted-collaboration.*`; `tests/scenarios/encrypted-agent.*`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: ENC-1.2.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: No downgrade or unauthorized plaintext exposure occurs; acknowledged protected work recovers; agent edits only succeed inside the declared decrypting trust boundary.

Implementation:

- [ ] ENC-1.3-I1 Repeat full offline/collaboration/diff/attachment/history flows with ciphertext storage/relay, rotation and a deliberately opaque MCP host versus an authorized decrypting endpoint.

Validation:

- [ ] ENC-1.3-V1 node tests/scenarios/run.mjs encrypted-collaboration; node tests/scenarios/run.mjs encrypted-agent. Assert all acceptance cases; record exact command/exit, nonzero executed/passed/failed/skipped counts, fixture/revision hashes and unavailable-platform evidence.

Evidence: Separate progress entry `ENC-1.3` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `ENC-1.3`.
Blocked behavior: Leave `ENC-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task ENC-1.4 — Resolve independent security review and release profile

- [ ] ENC-1.4 Resolve independent security review and release profile.

Purpose: Resolve independent security review and release profile as one bounded reusable delivery boundary.
Context: `../architecture/evidence/security-review.md`; `docs/security-profiles.md`; `../architecture/specs/security-encryption.md`; `../architecture/specs/verification.md`.
Dependencies: ENC-1.3.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Review scope and unresolved findings are explicit; production encrypted support is blocked until required findings close and claimed platform evidence passes. No compliance certification is inferred.

Implementation:

- [ ] ENC-1.4-I1 Provide threat model, dependency/protocol revisions, envelope/key lifecycle and evidence to an independent security reviewer; remediate findings with focused regressions before making a production claim.

Validation:

- [ ] ENC-1.4-V1 node tests/scenarios/run.mjs verify-security-review; rerun affected protocol/platform suites named by actual findings. Assert all acceptance cases; record exact command/exit, nonzero executed/passed/failed/skipped counts, fixture/revision hashes and unavailable-platform evidence.

Evidence: Separate progress entry `ENC-1.4` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `ENC-1.4`.
Blocked behavior: Leave `ENC-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.
