# Converge production admission and structural replay

Status: IN_PROGRESS

## Goal and entry conditions

SFC-1.1/1.2 exact current-source ownership and durability rows are validated. No old-profile COMPLETE label or full performance pass is an entry gate.

## Execution policy

Superseding user decision, 2026-10-23: follow `architecture/decisions/006-single-format-before-publication.md` and `architecture/specs/document-durability.md`. One production document schema/profile (the existing witnessed v5 format) and one current implementation per API/wire/ABI contract until publication. Retired development readers and fabricated previous/current release matrices are fixture history only; preserve useful behavior assertions on current-format cases. Never silently relabel, migrate, reset or reseed real data. Retain actual protocol/update-encoding semantics, external formats and document revision/history. Older version-specific runtime clauses in copied historical acceptance are superseded by this decision, not by dropping their semantic regressions.

One serial controller, root `/Users/bpstr/Github/edit-ac`, existing main branches only; no worktree, parallel lane, subagents or second run. Use only active source/progress and its named prerequisite summary. Prior run f6915e733a5ecb9c1c64e7ff is stopped, not restarted. Preserve its dirty work and exact successful/failing evidence. Live progress is separate; source files stay immutable. Read current prerequisites from `.roadmap-runner/single-format-feature-first-20261023/readiness.json` and its bounded handoff rows. The first source adapts existing collectors to this successor manifest; old matrix paths are historical evidence only.

Canonical shared-format cleanup and a focused safety gate precede native consumers. Then complete independent features before remaining optimization and comprehensive final suites. Size/latency work gets at most 45 minutes OR two materially different measured hypotheses per batch, whichever comes first. Checkpoint useful code and honest unresolved numbers, then advance independent feature work. Parent completion for a bounded optimization batch never closes its original hard-budget predicate; QPF final gates still own unchanged 512 KiB total/32 KiB editor-JS gzip caps and complete resource/tail proof. Never rerun an unchanged failing inventory. A true semantic/data-safety defect or missing required interface blocks only its dependents.

Use existing narrow deterministic checks during delivery, record meaningful counts and exact input hashes, and add a small regression only for a concrete shared-contract risk. Full test development/matrices stay with final owners; the focused format cutover gate is an explicit prerequisite to safely continue feature work. Port rather than suppress useful old regression assertions. Missing commands, zero cases, failures and required skips cannot pass. Historical fixture-oracle executions do not establish production legacy support. No new production legacy flag or old compatibility crate is allowed.

No paid inference, credentials, `.secrets`, subscription proxy, live fixture recording, paid services, physical-device qualification, publication, push, deployment or new external integration. Use prepared/mock transports for every automated provider case. Appropriate simulators/emulators and OS hosts/VMs must prove claimed target behavior; host-only JNA and responsive browser viewports are not mobile OS proof. Unknown/retired envelopes reject before mutation and preserve original checkpoint/journal recovery bytes. Optional encrypted/cloud release claims remain out of profile without removing baseline or discovered required tests.

One parent per worker, normally 15–45 minutes including focused checks. Commit only validated owned source on current main at safe checkpoints, under the coordination lock; never blindly stage prior dirty paths, stash/reset, or edit another worker's files. Generated evidence/binaries stay ignored and task-owned; keep concise counts/pins/failure dispositions, remove inactive reproducible bulk output. Tear down owned browsers/servers and check disk after substantial builds. Select another local ready parent beside a blocker; when none is ready, record task/source/error/prerequisite fingerprint, owner, attempted repair and exact changed-input resume condition, return BLOCKED, and let the event guard stop the controller. No unchanged retry or automatic restart.

## Epic CANONICAL_ADMISSION_AND_REPLAY — Converge production admission and structural replay

### Task SFC-2.1 — Converge current identity and admission

- [ ] SFC-2.1 Converge current identity and admission.

Purpose: Deliver this named canonical-format boundary safely without retaining unpublished runtime versions.
Context: `architecture/decisions/006-single-format-before-publication.md`; `architecture/specs/document-durability.md`; only task-local original APIs/specs and prerequisite rows; `core/crates/editac-core/src/document.rs`; current identity factories and unsupported-profile tests
Dependencies: none.
Independent work: Other local parents with their named prerequisite interfaces available.
Session scope: One boundary normally 15–45 minutes including checks; record a concrete split request rather than silently expanding input or acceptance.
Acceptance: Production creation, restore and update admission support only the canonical schema/profile/encoding/protocol/offset tuple. `DocumentIdentity::current` is the public factory. All real document/epoch validation and typed rejection/nonmutation remain. Older metadata can be represented only as negative fixture inputs, never admitted through fallback.

Implementation:

- [ ] SFC-2.1-I1 Update factory callers before removing obsolete constructors/constants, with only temporary build-coherent aliases during this cutover and no new supported profile/legacy feature. Port positive semantic tests to current fixtures; preserve useful old input rejection tests. Give remaining unavoidable compile-callsite work an exact dependent owner, not runtime support.

Validation:

- [ ] SFC-2.1-V1 Run `current_document_format` and affected identity/locator/admission selectors with pinned tools. Verify old/future envelopes reject without bytes/history/receipts changes; no silent renaming or old-reader fallback.

Evidence: Separate progress contains changed interfaces, exact input/fixture/runtime hashes, selector/command/exit, executed/passed/failed/skipped counts, reuse decisions and concise failure dispositions. Detailed output remains ignored.
Handoff: Last verified substep, remaining file/symbol, exact missing predicate and next bounded action.
Blocked behavior: Keep unfinished criteria unchecked, continue an independent local parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task SFC-2.2 — Converge creation, restore and journal validation

- [ ] SFC-2.2 Converge creation, restore and journal validation.

Purpose: Deliver this named canonical-format boundary safely without retaining unpublished runtime versions.
Context: `architecture/decisions/006-single-format-before-publication.md`; `architecture/specs/document-durability.md`; only task-local original APIs/specs and prerequisite rows; current `Document` initialization/restore/replay; `core/crates/editac-session` stores and deterministic checkpoint fixtures
Dependencies: SFC-2.1.
Independent work: Other local parents with their named prerequisite interfaces available.
Session scope: One boundary normally 15–45 minutes including checks; record a concrete split request rather than silently expanding input or acceptance.
Acceptance: Current-only root initialization and staged restore preserve empty initialized state, exact checkpoints/journals, duplicate/reordered replay, unknown data, fresh writer leases and immutable sources. Old root-registration/initializer branches no longer implement alternate runtime schemas.

Implementation:

- [ ] SFC-2.2-I1 Remove obsolete initialization/validation dispatch only after current semantic assertions are ported. Keep bounds and missing-binary-dependency errors intact. Fix an actual durability defect if discovered; never reseed restored empty bytes or replace source identities.

Validation:

- [ ] SFC-2.2-V1 Run affected initialization/checkpoint/current-format and Session recovery selectors with independent content/identity/journal oracles and explicit failure/duplicate/reordered/empty cases. Reuse matching current-format passes.

Evidence: Separate progress contains changed interfaces, exact input/fixture/runtime hashes, selector/command/exit, executed/passed/failed/skipped counts, reuse decisions and concise failure dispositions. Detailed output remains ignored.
Handoff: Last verified substep, remaining file/symbol, exact missing predicate and next bounded action.
Blocked behavior: Keep unfinished criteria unchecked, continue an independent local parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task SFC-2.3 — Retain only witnessed structural replay

- [ ] SFC-2.3 Retain only witnessed structural replay.

Purpose: Deliver this named canonical-format boundary safely without retaining unpublished runtime versions.
Context: `architecture/decisions/006-single-format-before-publication.md`; `architecture/specs/document-durability.md`; only task-local original APIs/specs and prerequisite rows; interrupted `core/crates/editac-core/src/editor.rs` and `editor_replay.rs`; independent current/historical fixture mappers
Dependencies: SFC-2.1.
Independent work: Other local parents with their named prerequisite interfaces available.
Session scope: One boundary normally 15–45 minutes including checks; record a concrete split request rather than silently expanding input or acceptance.
Acceptance: One production current-format replay implementation has no v4/v5 policy flag or retired replay eligibility branch. Witness immutability, split/join/place semantics, original-source ownership and bounds remain exact. Production does not compile historical mapper implementations as alternate readers.

Implementation:

- [ ] SFC-2.3-I1 Authenticate interrupted G8 changes, keep useful factoring, and remove old policy rather than finish dual-version optimization. Move production-owned current replay/helpers into authored src modules; historical independent mappers remain fixture-only oracles. Do not fork semantics or reduce retained data/limits.

Validation:

- [ ] SFC-2.3-V1 Run the current stable/retained presentation, structural/history/anchor affected selectors and pinned Rust/Yjs exchanges after the actual change. Include metadata-after-join/split, Unicode/multi-source and malformed witness cases; record meaningful counts.

Evidence: Separate progress contains changed interfaces, exact input/fixture/runtime hashes, selector/command/exit, executed/passed/failed/skipped counts, reuse decisions and concise failure dispositions. Detailed output remains ignored.
Handoff: Last verified substep, remaining file/symbol, exact missing predicate and next bounded action.
Blocked behavior: Keep unfinished criteria unchecked, continue an independent local parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.
