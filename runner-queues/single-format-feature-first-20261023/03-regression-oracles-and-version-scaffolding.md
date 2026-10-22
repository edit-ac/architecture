# Port regression semantics and retire unused version scaffolding

Status: IN_PROGRESS

## Goal and entry conditions

SFC-3 current projection/command/consumer interfaces are applicable; exact prior source tests remain available for semantic mapping, without requiring old readers in production.

## Execution policy

Superseding user decision, 2026-10-23: follow `architecture/decisions/006-single-format-before-publication.md` and `architecture/specs/document-durability.md`. One production document schema/profile (the existing witnessed v5 format) and one current implementation per API/wire/ABI contract until publication. Retired development readers and fabricated previous/current release matrices are fixture history only; preserve useful behavior assertions on current-format cases. Never silently relabel, migrate, reset or reseed real data. Retain actual protocol/update-encoding semantics, external formats and document revision/history. Older version-specific runtime clauses in copied historical acceptance are superseded by this decision, not by dropping their semantic regressions.

One serial controller, root `/Users/bpstr/Github/edit-ac`, existing main branches only; no worktree, parallel lane, subagents or second run. Use only active source/progress and its named prerequisite summary. Prior run f6915e733a5ecb9c1c64e7ff is stopped, not restarted. Preserve its dirty work and exact successful/failing evidence. Live progress is separate; source files stay immutable. Read current prerequisites from `.roadmap-runner/single-format-feature-first-20261023/readiness.json` and its bounded handoff rows. The first source adapts existing collectors to this successor manifest; old matrix paths are historical evidence only.

Canonical shared-format cleanup and a focused safety gate precede native consumers. Then complete independent features before remaining optimization and comprehensive final suites. Size/latency work gets at most 45 minutes OR two materially different measured hypotheses per batch, whichever comes first. Checkpoint useful code and honest unresolved numbers, then advance independent feature work. Parent completion for a bounded optimization batch never closes its original hard-budget predicate; QPF final gates still own unchanged 512 KiB total/32 KiB editor-JS gzip caps and complete resource/tail proof. Never rerun an unchanged failing inventory. A true semantic/data-safety defect or missing required interface blocks only its dependents.

Use existing narrow deterministic checks during delivery, record meaningful counts and exact input hashes, and add a small regression only for a concrete shared-contract risk. Full test development/matrices stay with final owners; the focused format cutover gate is an explicit prerequisite to safely continue feature work. Port rather than suppress useful old regression assertions. Missing commands, zero cases, failures and required skips cannot pass. Historical fixture-oracle executions do not establish production legacy support. No new production legacy flag or old compatibility crate is allowed.

No paid inference, credentials, `.secrets`, subscription proxy, live fixture recording, paid services, physical-device qualification, publication, push, deployment or new external integration. Use prepared/mock transports for every automated provider case. Appropriate simulators/emulators and OS hosts/VMs must prove claimed target behavior; host-only JNA and responsive browser viewports are not mobile OS proof. Unknown/retired envelopes reject before mutation and preserve original checkpoint/journal recovery bytes. Optional encrypted/cloud release claims remain out of profile without removing baseline or discovered required tests.

One parent per worker, normally 15–45 minutes including focused checks. Commit only validated owned source on current main at safe checkpoints, under the coordination lock; never blindly stage prior dirty paths, stash/reset, or edit another worker's files. Generated evidence/binaries stay ignored and task-owned; keep concise counts/pins/failure dispositions, remove inactive reproducible bulk output. Tear down owned browsers/servers and check disk after substantial builds. Select another local ready parent beside a blocker; when none is ready, record task/source/error/prerequisite fingerprint, owner, attempted repair and exact changed-input resume condition, return BLOCKED, and let the event guard stop the controller. No unchanged retry or automatic restart.

## Epic REGRESSION_ORACLES_AND_VERSION_SCAFFOLDING — Port regression semantics and retire unused version scaffolding

### Task SFC-4.1 — Port useful behavioral regression fixtures

- [ ] SFC-4.1 Port useful behavioral regression fixtures.

Purpose: Deliver this named canonical-format boundary safely without retaining unpublished runtime versions.
Context: `architecture/decisions/006-single-format-before-publication.md`; `architecture/specs/document-durability.md`; only task-local original APIs/specs and prerequisite rows; constructor/callsite inventory; original core initialization/format/text/projection/anchor/structural/profile tests
Dependencies: none.
Independent work: Other local parents with their named prerequisite interfaces available.
Session scope: One boundary normally 15–45 minutes including checks; record a concrete split request rather than silently expanding input or acceptance.
Acceptance: Every useful original semantic regression has a current-format fixture/test owner, with the same intended safety invariant or explicit corrected witnessed behavior. No required test disappears as a skip/ignore, zero group or renamed unsupported positive.

Implementation:

- [ ] SFC-4.1-I1 Port original legacy setup/IDs/expected outputs to the current engine while preserving independent semantic assertions. Keep format-specific historical qualification tests independent from runtime and labelled as fixture-oracle history. Remove transitional old constructor aliases after compile callers are accounted for.

Validation:

- [ ] SFC-4.1-V1 Compile affected test targets and run their changed selections. Compare discovered original semantic case IDs to current tests/oracles; report unavoidable changed behavior with its approved spec, never erase the old failure disposition.

Evidence: Separate progress contains changed interfaces, exact input/fixture/runtime hashes, selector/command/exit, executed/passed/failed/skipped counts, reuse decisions and concise failure dispositions. Detailed output remains ignored.
Handoff: Last verified substep, remaining file/symbol, exact missing predicate and next bounded action.
Blocked behavior: Keep unfinished criteria unchecked, continue an independent local parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task SFC-4.2 — Isolate historical readers from production inputs

- [ ] SFC-4.2 Isolate historical readers from production inputs.

Purpose: Deliver this named canonical-format boundary safely without retaining unpublished runtime versions.
Context: `architecture/decisions/006-single-format-before-publication.md`; `architecture/specs/document-durability.md`; only task-local original APIs/specs and prerequisite rows; `core/fixtures/schema-v1` through v5, current library dependency modules and WASM packaging
Dependencies: SFC-4.1.
Independent work: Other local parents with their named prerequisite interfaces available.
Session scope: One boundary normally 15–45 minutes including checks; record a concrete split request rather than silently expanding input or acceptance.
Acceptance: Historical v1–v4 readers/mappers exist only as independent fixture oracles or archived source, outside all production imports/dependency graphs/exported features. The runtime contains only current decoder/replay/model helpers. Required current/native regression tests still execute meaningful cases.

Implementation:

- [ ] SFC-4.2-I1 Audit actual module/feature/dependency closure. Move reusable current helpers into src rather than importing old fixture mappers, without introducing a legacy-runtime feature flag or compatibility crate. Keep bounded old test bytes/provenance; no bulk generated snapshot restoration.

Validation:

- [ ] SFC-4.2-V1 Use deterministic module/graph/static negative controls and affected canonical/oracle test runs. One changed production build may confirm closure; no repeated size tuning. Verify current and old fixture oracles are labelled separately.

Evidence: Separate progress contains changed interfaces, exact input/fixture/runtime hashes, selector/command/exit, executed/passed/failed/skipped counts, reuse decisions and concise failure dispositions. Detailed output remains ignored.
Handoff: Last verified substep, remaining file/symbol, exact missing predicate and next bounded action.
Blocked behavior: Keep unfinished criteria unchecked, continue an independent local parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.

### Task SFC-4.3 — Remove synthetic previous-release and unused API variants

- [ ] SFC-4.3 Remove synthetic previous-release and unused API variants.

Purpose: Deliver this named canonical-format boundary safely without retaining unpublished runtime versions.
Context: `architecture/decisions/006-single-format-before-publication.md`; `architecture/specs/document-durability.md`; only task-local original APIs/specs and prerequisite rows; `core/scripts/compatibility-policy.mjs`; compatibility policy/tests; capability/API/ABI descriptor factories; current guides
Dependencies: none.
Independent work: Other local parents with their named prerequisite interfaces available.
Session scope: One boundary normally 15–45 minutes including checks; record a concrete split request rather than silently expanding input or acceptance.
Acceptance: Before publication there is one supported current API/ABI/protocol contract per actual boundary. Fabricated previous/current SDK revision closures and obsolete unpublished adapters/aliases no longer create runtime support or gate same-format reopening. Real external formats, document revisions, wire/encoding/descriptor validation and deterministic unsupported-input tests remain.

Implementation:

- [ ] SFC-4.3-I1 Inventory alternate-version code by actual current consumers. Replace synthetic release-matrix qualification with independently packed current consumers and exact unsupported-tuple/unknown-data recovery tests. Remove only unused unpublished alternatives; do not conflate distinct real contracts or require an exact old Git hash for same-format data.

Validation:

- [ ] SFC-4.3-V1 Run affected compatibility/contract/export/consumer tests with real current round trips, bad tuple/revision nonmutation and retained recovery data. No live provider/network service or full performance campaign.

Evidence: Separate progress contains changed interfaces, exact input/fixture/runtime hashes, selector/command/exit, executed/passed/failed/skipped counts, reuse decisions and concise failure dispositions. Detailed output remains ignored.
Handoff: Last verified substep, remaining file/symbol, exact missing predicate and next bounded action.
Blocked behavior: Keep unfinished criteria unchecked, continue an independent local parent, otherwise record fingerprint/owner/repair/resume condition and return BLOCKED for controller stop.
