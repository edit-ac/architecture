# Expose safe realtime editing through host-app MCP

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core`; paths below are core-relative unless prefixed `../architecture/`. Follow `../architecture/specs/agent-editing.md` and the active task context. This is planned follow-up delivery, not implemented capability.

Required upstream tracks: `08-sdk-integration.md`, `12-client-contracts.md`, `13-change-diffs.md`, `21-extension-library.md` complete at reviewed source/implementation revisions with passing evidence. Check these gates before launching; source dependencies below are local to this file.

## Execution rules

The controller owns this source. Write progress/checkmarks/evidence in the configured separate progress file. Each iteration implements at most one parent with its implementation and validation substeps. Aim for 15–45 minutes plus checks; if the boundary cannot fit, propose a stable controller-approved split before implementation. Use named fixtures/checks, creating planned test commands before running them. Missing checks, zero matches, failures and skips are not passing acceptance.

Use deterministic fixtures and mocked transports only; no paid model/provider calls, .secrets loading or production document writes. Other ready local tasks are permitted independent work. Unavailable device/toolchain/review evidence blocks its qualified claim, not unrelated platform work. Do not launch another runner or publish before an explicit release task.

## Epic AGT-1 — Expose safe realtime editing through host-app MCP

### Task AGT-1.1 — Freeze host-owned tool and receipt contract

- [ ] AGT-1.1 Freeze host-owned tool and receipt contract.

Purpose: Freeze host-owned tool and receipt contract as one bounded reusable delivery boundary.
Context: `examples/host-mcp/`; `packages/web/src/host/`; `../architecture/evidence/agent-contract.md`; `../architecture/specs/agent-editing.md`; `../architecture/specs/verification.md`.
Dependencies: none.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Document permissions and actor identity come from the host; CLI/MCP-server creation is not a prerequisite; tool examples report actual capabilities and unknown outcomes.

Implementation:

- [ ] AGT-1.1-I1 Map planned read/prepare/apply/receipt/observe operations to a sample embedding apps existing MCP with versioned schemas and fake authorization. Keep MCP transport out of the engine.

Validation:

- [ ] AGT-1.1-V1 node --test tests/host-agent-contract.test.mjs. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `AGT-1.1` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `AGT-1.1`.
Blocked behavior: Leave `AGT-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task AGT-1.2 — Implement revision-bound Markdown export and upload

- [ ] AGT-1.2 Implement revision-bound Markdown export and upload.

Purpose: Implement revision-bound Markdown export and upload as one bounded reusable delivery boundary.
Context: `packages/web/src/host/markdown.ts`; `tests/agent-markdown.test.mjs`; `../architecture/specs/agent-editing.md`; `../architecture/specs/verification.md`.
Dependencies: AGT-1.1.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Complete uploads prepare through shared reconciliation; partial/oversized/mismatched uploads do not mutate; unsupported atoms are retained or explicitly block the proposal.

Implementation:

- [ ] AGT-1.2-I1 Return source/profile/revision/hash/diagnostics; accept bounded candidate Markdown or patches against the retained baseline. Add checksummed chunk admission/expiry without document mutation.

Validation:

- [ ] AGT-1.2-V1 npm run build; node --test tests/agent-markdown.test.mjs. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `AGT-1.2` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `AGT-1.2`.
Blocked behavior: Leave `AGT-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task AGT-1.3 — Prepare anchored agent changes and previews

- [ ] AGT-1.3 Prepare anchored agent changes and previews.

Purpose: Prepare anchored agent changes and previews as one bounded reusable delivery boundary.
Context: `packages/web/src/host/prepare.ts`; `tests/agent-prepare.test.mjs`; `../architecture/specs/agent-editing.md`; `../architecture/specs/verification.md`.
Dependencies: AGT-1.2.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Concurrent overlap and deleted targets return structured conflicts without stale full replacement; readonly/unauthorized writes fail regardless of MCP annotations.

Implementation:

- [ ] AGT-1.3-I1 Use the shared edit service for bounded semantic or Markdown-derived proposals and source/semantic diff previews. Recheck current permissions/capabilities and stale anchors.

Validation:

- [ ] AGT-1.3-V1 npm run build; node --test tests/agent-prepare.test.mjs. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `AGT-1.3` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `AGT-1.3`.
Blocked behavior: Leave `AGT-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task AGT-1.4 — Implement durable idempotency and apply receipts

- [ ] AGT-1.4 Implement durable idempotency and apply receipts.

Purpose: Implement durable idempotency and apply receipts as one bounded reusable delivery boundary.
Context: `crates/editac-session/src/receipts.rs`; `crates/editac-session/tests/request_replay.rs`; `../architecture/specs/agent-editing.md`; `../architecture/specs/verification.md`. [Wordcraft-derived cases](../tests/wordcraft-regression-cases.md).
Dependencies: AGT-1.3.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Same request after timeout/restart returns the original result even after proposal expiry or revision advancement; changed payload with same ID rejects. Unauthorized receipt lookup rejects. Crash/failure at each boundary cannot duplicate an acknowledged insertion; later human edits, checkpoints and state-vector resync cannot expose an unjournaled operation. WCF-02: Recheck queued execution expiry/cancellation at serialized admission; expired pre-commit work makes no mutation. Distinguish post-commit timeout from clean rejection and recover its outcome through the same durable request identity.

Implementation:

- [ ] AGT-1.4-I1 Authorize and look up existing receipts before new-request proposal/revision checks; bind immutable proposals to actor/document/epoch/base/profile/hash. Atomically persist update bytes, request identity, payload hash and resulting receipt before durable success/peer release. Freeze mutation/sync admission after persistence failure until ordered recovery; preserve read/recovery-export access without pretending rollback.

Validation:

- [ ] AGT-1.4-V1 cargo test -p editac-session --test request_replay --locked. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes. Execute the named WCF-02 variants through this owner's real boundary; record case/fixture revisions and work/effect counts. Planning validation is not runtime evidence.

Evidence: Separate progress entry `AGT-1.4` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `AGT-1.4`.
Blocked behavior: Leave `AGT-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task AGT-1.5 — Propagate agent edits into live views and history

- [ ] AGT-1.5 Propagate agent edits into live views and history.

Purpose: Propagate agent edits into live views and history as one bounded reusable delivery boundary.
Context: `packages/web/src/host/apply.ts`; `tests/browser/agent-realtime.spec.ts`; `../architecture/specs/agent-editing.md`; `../architecture/specs/verification.md`.
Dependencies: AGT-1.4.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Open human editors update without remount; agent undo grouping stays distinct; concurrent edits and revocation retain recoverable content without misreporting remote durability.

Implementation:

- [ ] AGT-1.5-I1 Apply successful proposals through ordinary engine patches, history origin policy, local outbox and sync; expose pending/local/remote receipt statuses accurately.

Validation:

- [ ] AGT-1.5-V1 npm run test:browser -- agent-realtime. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `AGT-1.5` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `AGT-1.5`.
Blocked behavior: Leave `AGT-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task AGT-1.6 — Add capability-negotiated MCP observation

- [ ] AGT-1.6 Add capability-negotiated MCP observation.

Purpose: Add capability-negotiated MCP observation as one bounded reusable delivery boundary.
Context: `examples/host-mcp/src/observe.ts`; `tests/agent-observe.test.mjs`; `../architecture/specs/agent-editing.md`; `../architecture/specs/verification.md`.
Dependencies: AGT-1.5.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Dropped/duplicated notifications cannot corrupt content or falsely claim durable sync; reconnect can read current revision, and revoked observers receive no protected source.

Implementation:

- [ ] AGT-1.6-I1 Implement resource invalidation/subscriptions where supported plus bounded polling/resync fallback and access revocation. Keep data events on the collaboration channel.

Validation:

- [ ] AGT-1.6-V1 node --test tests/agent-observe.test.mjs. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `AGT-1.6` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `AGT-1.6`.
Blocked behavior: Leave `AGT-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.

### Task AGT-1.7 — Qualify app integration and adversarial requests

- [ ] AGT-1.7 Qualify app integration and adversarial requests.

Purpose: Qualify app integration and adversarial requests as one bounded reusable delivery boundary.
Context: `examples/host-mcp/`; `tests/agent-integration.test.mjs`; `../architecture/evidence/agent-editing.md`; `../architecture/specs/agent-editing.md`; `../architecture/specs/verification.md`.
Dependencies: AGT-1.6.
Session scope: One named implementation/qualification boundary, 15–45 minutes plus focused checks; controller splits before exceeding scope.
Acceptance: Every mutation uses shared policy and durable request identity; no network fetch is triggered by document prose, and no live LLM/provider call is used for qualification.

Implementation:

- [ ] AGT-1.7-I1 Run prepared app-MCP clients, fixture uploads and a human peer through auth/readonly/retry/conflict flows. Treat embedded instructions as content; document local/hosted/E2EE endpoint limits.

Validation:

- [ ] AGT-1.7-V1 node --test tests/agent-integration.test.mjs; npm run test:browser -- agent-realtime. Assert the acceptance cases; record exact exit results, nonzero matching test counts where applicable, failures/skips and artifact hashes.

Evidence: Separate progress entry `AGT-1.7` with changed files, source/implementation revisions, commands, fixture IDs and durable artifact links; preserve failed evidence.
Handoff: Last completed substep, current symbol/file, exact failing case or missing decision, and next bounded action for `AGT-1.7`.
Blocked behavior: Leave `AGT-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO, owner/unblock condition and bounded retry trigger. Select another dependency-ready local task; if none exists stop and report rather than repeatedly polling.
