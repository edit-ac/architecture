# Deliver shared block actions and extension contracts

Status: IN_PROGRESS

## Goal and entry conditions

The preceding source has verified SFC-3.1, SFC-3.2, SFC-3.3. Consume its bounded progress and source-pinned interface proof. These are entry prerequisites, not local task dependencies. Read SFC-1.1/1.2 handoff once; do not rerun inventory or refresh completed source prose.

## Execution policy

Superseding user decision, 2026-10-23: follow `architecture/decisions/006-single-format-before-publication.md` and `architecture/specs/document-durability.md`. One production document schema/profile (the existing witnessed v5 format) and one current implementation per API/wire/ABI contract until publication. Retired development readers and fabricated previous/current release matrices are fixture history only; preserve useful behavior assertions on current-format cases. Never silently relabel, migrate, reset or reseed real data. Retain actual protocol/update-encoding semantics, external formats and document revision/history. Older version-specific runtime clauses in copied historical acceptance are superseded by this decision, not by dropping their semantic regressions.

One serial controller, root `/Users/bpstr/Github/edit-ac`, existing main branches only; no worktree, parallel lane, subagents or second run. Use only active source/progress and its named prerequisite summary. Prior run f6915e733a5ecb9c1c64e7ff is stopped, not restarted. Preserve its dirty work and exact successful/failing evidence. Workers may change only task checkboxes and the Status line in this source. Put delivery summaries, source hashes, reconciliation receipts, timestamps and counts only in the separate progress file or ignored receipts. Never add or update a Current delivery paragraph here: changing acceptance prose on each pass forces another reconciliation. Read current prerequisites from `.roadmap-runner/single-format-feature-first-20261023/readiness.json` and its bounded handoff rows. The first source adapts existing collectors to this successor manifest; old matrix paths are historical evidence only.

Canonical shared-format cleanup and a focused safety gate precede native consumers. Then complete independent features before remaining optimization and comprehensive final suites. Size/latency work gets at most 45 minutes OR two materially different measured hypotheses per batch, whichever comes first. Checkpoint useful code and honest unresolved numbers, then advance independent feature work. Parent completion for a bounded optimization batch never closes its original hard-budget predicate; QPF final gates still own unchanged 512 KiB total/32 KiB editor-JS gzip caps and complete resource/tail proof. Never rerun an unchanged failing inventory. A true semantic/data-safety defect or missing required interface blocks only its dependents.

Use existing narrow deterministic checks during delivery, record meaningful counts and exact input hashes, and add a small regression only for a concrete shared-contract risk. Full test development/matrices stay with final owners; the focused format cutover gate is an explicit prerequisite to safely continue feature work. Port rather than suppress useful old regression assertions. Missing commands, zero cases, failures and required skips cannot pass. Historical fixture-oracle executions do not establish production legacy support. No new production legacy flag or old compatibility crate is allowed.

No paid inference, credentials, `.secrets`, subscription proxy, live fixture recording, paid services, physical-device qualification, publication, push, deployment or new external integration. Use prepared/mock transports for every automated provider case. Appropriate simulators/emulators and OS hosts/VMs must prove claimed target behavior; host-only JNA and responsive browser viewports are not mobile OS proof. Unknown/retired envelopes reject before mutation and preserve original checkpoint/journal recovery bytes. Optional encrypted/cloud release claims remain out of profile without removing baseline or discovered required tests.

One parent per worker, normally 15–45 minutes including focused checks. Commit only validated owned source on current main at safe checkpoints, under the coordination lock; never blindly stage prior dirty paths, stash/reset, or edit another worker's files. Generated evidence/binaries stay ignored and task-owned; keep concise counts/pins/failure dispositions, remove inactive reproducible bulk output. Tear down owned browsers/servers and check disk after substantial builds. Select another local ready parent beside a blocker; when none is ready, record task/source/error/prerequisite fingerprint, owner, attempted repair and exact changed-input resume condition, return BLOCKED, and let the event guard stop the controller. No unchanged retry or automatic restart.

## Epic CANONICAL_PROJECTION_AND_CONSUMERS — Converge current projection, commands and consumer ports

### Task BTA-1.1 — Implement lossless captured block conversion

- [ ] BTA-1.1 Implement paragraph/heading conversion over captured block targets.

Purpose: Change presentation without recreating content or identity.
Context: Originating interface owner SFC-3.2; `specs/block-actions.md` sections Lossless presentation changes and Shared command and target contract; `core/crates/editac-core/src/commands/format.rs`, `commands/blocks.rs`, `commands/editor.rs`, `history.rs`.
Dependencies: none.
Independent work: Inspect binding and registry interfaces while the shared entry gate is pending.
Session scope: One prepared conversion boundary, 30–45 minutes including focused validation; split only through the controller if necessary.
Acceptance: Paragraph, heading 1–6 and heading-level changes preserve rich/opaque content, IDs, sources, placement, descendants and directional selection. Capture presentation as well as structural preconditions. Multi-target conversion is all-or-none; current-type requests are no-ops. Read-only/protected/stale/unsupported targets reject atomically. One undo/redo action preserves peer text.

Implementation:

- [ ] BTA-1.1-I1 Add typed captured targets and prepare/availability routing through existing format semantics; preserve source/owner data and return existing result-selection resources.

Validation:

- [ ] BTA-1.1-V1 Run `cargo test -p editac-core --locked --offline --test block_actions heading_to_paragraph_is_lossless -- --exact` and the same command with `stale_conversion_is_atomic`. These minimal regressions protect the data-loss boundary; reuse applicable existing formatting/history results. Budget: 5 minutes; record nonzero passed/failed/skipped counts. Comprehensive combinations belong to BTQ-1.1.

Evidence: Separate progress entry with changed symbols, current-format pins, focused counts and reused checks.
Handoff: Exact captured-target fields, no-op behavior, returned resource ownership and any failed preservation invariant.
Blocked behavior: Leave unchecked; record missing primitive, owner and changed-input resume condition. Do not substitute text export/import.

### Task BTA-1.2 — Expose one portable typed command contract

- [ ] BTA-1.2 Expose conversion through Rust, WASM and Session/FFI ports.

Purpose: Give extensions and all clients the same action without menu dependencies.
Context: Shared command section of the contract; BTA-1.1 handoff; `core/packages/core/src/engine.ts`, `core/crates/editac-wasm/src/bridge.rs`, `core/crates/editac-session/src/`, `core/crates/editac-ffi/src/session.rs`.
Dependencies: BTA-1.1.
Independent work: Record existing per-runtime binding/command adapter ownership before the prerequisite is ready.
Session scope: Thin binding of one prepared command and typed outcomes, 30–45 minutes; no platform presenter work.
Acceptance: One named capture/enumerate/prepare/commit capability exposes no-op, unavailable reasons, stale target and existing storage errors consistently. Prepare/commit recheck permissions and touched preconditions. Engine/Session clients work without optional UI. No document identity or format bump is introduced for this action; no duplicate legacy alias is published.

Implementation:

- [ ] BTA-1.2-I1 Freeze concrete binding names and schemas, route adapters to the shared primitive and document plan/selection ownership and capability availability.

Validation:

- [ ] BTA-1.2-V1 Run `npm run typecheck --workspace @edit-ac/core`, `node --test --test-name-pattern='lossless port' tests/wasm-block-actions.test.mjs` and `cargo test -p editac-session -p editac-ffi --locked --offline block_actions_lossless_port`. Add one minimal round trip per changed binding; require nonzero cases in each crate. Budget: 5 minutes beyond compilation; full cross-port negatives belong to BTQ-1.1.

Evidence: Progress with the exact API/ABI shape, selected compile/probe results and runtime scope.
Handoff: Command descriptor and captured-target/result examples for extension and native/TUI owners.
Blocked behavior: Record the exact missing binding or capability; do not route around shared admission.

### Task BTA-1.3 — Register extension conversions safely

- [ ] BTA-1.3 Add conversion declarations and indexed preparation to the existing extension registry.

Purpose: Make custom block types participate in Turn into through public extension APIs.
Context: Contract section Extension participation; BTA-1.2 handoff; `core/packages/core/src/extensions/registry.ts`, `core/packages/web/src/extensions/authoring.ts`, `extensions/contract.ts`, `core/packages/web/src/modules/conformance.ts` (ExtensionCommandSession).
Dependencies: BTA-1.2.
Independent work: Prepare a deterministic custom source/destination fixture from admitted data types.
Session scope: One registry/preparation integration, 30–45 minutes.
Acceptance: Namespaced source/destination declarations, bounded options, capability requirements and preservation constraints validate before attachment. Duplicate registrations reject. Providers use prepared primitives and existing cancellation/history; unknown payloads survive extension disable/re-enable. Menu-off leaves the API available; absent native providers report unavailable without pretending JavaScript is portable.

Implementation:

- [ ] BTA-1.3-I1 Add typed registration and captured-target enumeration, adapting the existing command session and public authoring hooks rather than creating another dispatcher.

Validation:

- [ ] BTA-1.3-V1 Run `npm run typecheck --workspace @edit-ac/web` and `node --test --test-name-pattern='registration|custom lossless' tests/block-actions-contract.test.mjs`, adapting the existing extension authoring/command fixture for one custom conversion and a rejected registration. Budget: 5 minutes; record counts. BTQ-1.2 owns the remaining lifecycle/unknown-data matrix.

Evidence: Progress with declaration shape, public import recipe and focused outcomes.
Handoff: Relevant type indexes, provider lifecycle and per-runtime availability.
Blocked behavior: Name a missing admitted primitive and its owner; never expose raw document mutation as a workaround.

### Task BTA-1.4 — Enforce advanced conversion review and refusal

- [ ] BTA-1.4 Implement typed impact plans and exact-plan approval for advanced conversions.

Purpose: Prevent silent loss when richer block structures are transformed.
Context: Contract sections Conversion classification and Shared command and target contract; BTA-1.3 registry; existing prepared-plan/cancellation and error owners.
Dependencies: BTA-1.3.
Independent work: Classify list/task/quote/code/table/asset/custom examples from the contract while registry work proceeds.
Session scope: One plan/admission policy boundary, 30–45 minutes; do not implement every advanced mapping.
Acceptance: Lossless built-ins need no confirmation. A review-required provider returns a staged field/structure impact report; approval binds to that plan and preconditions. Changed impact, stale targets, cancellation or permission loss reject without mutation. Unspecified advanced mappings remain unavailable with reasons. Undo support alone cannot certify losslessness; confirmation never overrides schema/permission/bounds checks.

Implementation:

- [ ] BTA-1.4-I1 Add classification, review-required outcomes and single-use approval binding; publish the initial available/unavailable mapping catalog without enabling unqualified table/page conversions.

Validation:

- [ ] BTA-1.4-V1 Run `node --test --test-name-pattern='review approval' tests/block-actions-contract.test.mjs` with refusal, exact approval and relevant-peer-change rejection; assert unchanged bytes on rejection. Budget: 5 minutes; this minimal regression protects a concrete destructive-edit boundary. Remaining cases belong to BTQ-1.2.

Evidence: Progress with impact schema, mapping dispositions and focused counts.
Handoff: UI review data, disabled reasons and exact approval invalidation conditions.
Blocked behavior: Keep an unresolved mapping disabled and record its design owner; do not block safe paragraph/heading delivery on table redesign.

### Task BTA-1.5 — Add general captured Insert after

- [ ] BTA-1.5 Insert an empty paragraph after any eligible captured sibling.

Purpose: Supply the second required block-menu action without splitting or replacing content.
Context: Contract section Optional block menu and Insert after; BTA-1.2 target/command ports; `core/crates/editac-core/src/commands/blocks.rs`, `commands/editor.rs`, `core/packages/core/src/engine.ts` and changed bridge/Session adapters.
Dependencies: BTA-1.2.
Independent work: BTA-1.3 and BTA-1.4 do not block paragraph insertion.
Session scope: One shared insertion command and thin bindings, 30–45 minutes; richer creation descriptors stay disabled unless already admitted.
Acceptance: Create a stable empty paragraph immediately after the target in the same parent, after its subtree in display order. Preserve the target and descendants; select the new editable start. Reject invalid parents, stale/deleted targets and policy failures. One undo removes only the inserted block while preserving peer changes. Separator-specific insertion is not the implementation of this general contract.

Implementation:

- [ ] BTA-1.5-I1 Prepare creation/placement/result selection as one shared transaction and expose it through the same captured block-action ports.

Validation:

- [ ] BTA-1.5-V1 Run `cargo test -p editac-core --locked --offline --test block_actions insert_after` and `node --test --test-name-pattern='insert after port' tests/wasm-block-actions.test.mjs`. Cover root/nested placement, unchanged original content, one undo group and stale rejection. Budget: 5 minutes. Broader history/concurrency cases belong to BTQ-1.1.

Evidence: Separate progress with command shape, focused results and reused primitive evidence.
Handoff: Functional API summary and exact source pins for all BTA parents; do not repeat passing suites at the file boundary.
Blocked behavior: Record a missing parent-creation semantic and its owner; never flatten the target to make insertion possible.
