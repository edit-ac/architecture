# Repair the primary editing regression API blockers

Status: IN_PROGRESS

## Goal and entry conditions

User authorization, 2026-10-14: "Lets unblock primary." This is a temporary repair phase of the existing primary lane, not a third lane or a replacement for roadmap 42. Primary owns the missing upstream engine/ABI/profile repairs as well as their regression bindings. The old external-owner-only assignment is superseded for these three boundaries; unchanged engine source is the input to implementation, not a reason to repeat admission scans. Qualified APIs and original acceptance must be delivered, not waived.

Workspace: `/Users/bpstr/Github/edit-ac-primary-unblock-20261014`; repositories `core`, `architecture`, `cli`, `docs`; branch `runner/primary-unblock-20261014`. Main and parallel live source remain untouched during implementation. Read root/repository AGENTS.md and `.roadmap-coordination/parallel-clients.md` before every parent. Read queue.json for current IDs/workspaces and primary-unblock-ownership.json for shared-path ownership. Codanna discovery precedes narrow text fallback. Use Node 24.19.0 and Rust 1.97.1 with worktree-owned outputs and absolute fixture/exchange paths.

Consume the current original 42 fixture manifest, native/packed APIs, semantic adapter, independent expectations and retained failures. Historical receipts, failed traces and prior progress remain available read-only under `/Users/bpstr/Github/edit-ac/architecture/evidence/editing-regression-suite/` and `/Users/bpstr/Github/edit-ac/.roadmap-runner/`. Do not regenerate goldens, duplicate the authoritative fixture catalog, silently reduce variants, invent selection results in a JS adapter, or substitute sequential commits for one atomic action. Before changing semantics, update the authoritative engine/formats/suite contract and affected repair acceptance together. Preserve both native FFI and shared session/diff implementations and the main checkout's unrelated clipboard-spec patch.

## Execution and integration rules

Implement at most one named parent per iteration. Controller authorizes bounded implementation/qualification substeps within a parent when needed; record the concrete next substep, keep full original acceptance and leave parent/I1/V1 unchecked until all proof passes. A partially implemented API is work in progress, not an unchanged external blocker. Stop only for a specific new condition that cannot be addressed within this assignment; retain failures and name its owner and retry condition. Do not repeatedly run no-op source admission.

Use deterministic native and packed production-engine fixtures only; no paid inference, credential loading, live transports, automatic fixture recording, publication, pushing or deployment. Hard gzip caps are 524288 total / 32768 JavaScript; preferred targets remain 256000 / 16000. Emulator evidence is development only. Physical/hosted/renderer release gates remain open.

Commit only validated owned source/evidence with plain-English imperative subjects. Write delivery receipts and requests to the shared ledger. Reconcile with local main after every two completed parents and at this repair-phase boundary under integration.lock. Respect live locks. Prepare/test a union in isolation before landing; never stage unrelated dirty paths, blindly stash/reset, force branches, or merge into an actively mutating worker checkout. Main primary checkout has no active implementation worker during this phase. Parallel owns CLI/TUI/links/security; do not change its files or stop its worker independently. Request a monitor safe checkpoint when parallel synchronization requires pausing that controller. If integration is pending, identify exact revisions/paths; retain completed work instead of rerunning it. Before returning to 42, require the qualified repair commits in main and safe incoming-main reconciliation in both lanes. Preserve the existing 42 -> 30 -> 14 -> 16 -> 17 queue and checked progress; verify later prerequisites in merged main.

## Epic UPG-1 — Deliver the three missing primary API boundaries

### Task UPG-1.1 — Qualify atomic cross-owner code and text paste

- [ ] UPG-1.1 Qualify atomic cross-owner code and text paste.

Purpose: Deliver the upstream fragment/prepared-edit repair and exact RGS-1.2-C2 binding.
Context: `core/crates/editac-core/src/commands/fragment.rs`; `core/crates/editac-core/src`; `core/crates/editac-wasm/src`; `core/packages/core/src/engine.ts`; `core/tests/editing/semantic-adapter.ts`; `core/tests/editing/semantic.test.mjs`; `architecture/specs/engine.md`; `architecture/specs/formats.md`; `architecture/specs/editing-regression-suite.md`; `architecture/tests/editing-suite`; retained `rgs-1.2-supported-20261014` and `rgs-1.2-remaining-vector-storage-20261014/source-gap-handoff.json`.
Dependencies: None.
Session scope: One missing prepared-fragment boundary, using the existing public/native ports rather than a parallel API.
Acceptance: Original REG-07 selected code/text cross-owner pre paste admits one atomic action preserving prefix, intermediate whitespace, retained suffix, semantic/source identities and stable result caret. Native and packed production-engine proof covers successful content/source undo and atomic rejection. Retained previously failed admissions are rerun only after the relevant repair; original variants are not weakened.

Implementation:

- [ ] UPG-1.1-I1 Inspect retained failing admissions, declare the exact contract repair, implement it in the owning native engine and ABI as needed, and bind the existing regression driver to the qualified result.

Validation:

- [ ] UPG-1.1-V1 Run nonzero focused native and packed C2 proof with independent expected content, source, identities, selection and one-action history assertions, rejection controls, immutable source/profile/fixture hashes and zero failures/skips. Preserve initial failed logs. Run meaningful affected checks and production bundle admission when public/generated code changes.

Evidence: `architecture/evidence/editing-regression-suite/primary-api-unblock-20261014/c2/receipt.json`, exact source commits, full logs, executed/passed/failed/skipped counts and qualified native/packed artifacts; shared delivery ledger.
Handoff: Record the last completed substep, exact repaired failing trace, remaining original assertions and next bounded action. A passing primitive alone does not close full RGS-1.2.
Blocked behavior: Leave unchecked for any unmet original assertion. Repair concrete source/fixture/toolchain issues within this scope; on a genuinely external condition preserve evidence and state owner/unblock condition without repeating unchanged retries.

### Task UPG-1.2 — Deliver native and packed history selection bookmarks

- [ ] UPG-1.2 Deliver native and packed history selection bookmarks.

Purpose: Deliver the upstream history/ABI repair and exact RGS-1.2-C3 binding.
Context: `core/crates/editac-core/src/history.rs`; native prepared-command/selection modules; `core/crates/editac-wasm/src`; `core/packages/core/src/engine.ts`; `core/tests/editing/semantic-adapter.ts`; original SEQ-03/07/13/14 and G03 fixtures; `architecture/specs/engine.md`; `architecture/specs/editing-regression-suite.md`; retained C3 gap evidence.
Dependencies: UPG-1.1.
Session scope: One history selection/result contract using stable native bookmarks, retaining existing content/source history semantics and FFI/session interfaces.
Acceptance: Real transaction-entry and mapped history-result bookmarks preserve both endpoints, backward direction and affinity through undo, redo, rebasing and the next sentinel for original SEQ-03/07/13/14 and G03. No fabricated JS selection, captured source-offset substitute, extra commits or unsupported-profile waiver. Native and packed results agree and invalid/rejected history operations do not partially mutate.

Implementation:

- [ ] UPG-1.2-I1 Specify and implement entry/result bookmarks in the owning native history/prepared boundary, expose the actual qualified result through existing ABI/public types, and bind original regression expectations.

Validation:

- [ ] UPG-1.2-V1 Run nonzero native and packed endpoint/direction/affinity/undo-redo/rebase/sentinel tests with independent expectations and rejection controls. Run meaningful affected history, atomic/prepared, FFI/shared-session and editing checks. Qualify production WASM/public artifacts and unchanged hard caps; record every failure/skip honestly.

Evidence: `architecture/evidence/editing-regression-suite/primary-api-unblock-20261014/c3/receipt.json` with exact commits, source/profile/fixture/artifact hashes and actual executed/passed/failed/skipped counts; shared delivery ledger and integration request at the two-parent checkpoint.
Handoff: Record qualified bookmark behavior and remaining assertions, not a claim that the entire 42 roadmap is complete.
Blocked behavior: Leave unchecked while any original bookmark assertion fails; fix owned contract/implementation gaps instead of waiting for an unnamed upstream owner. Stop on a named new external gate only.

### Task UPG-1.3 — Qualify alignment and preceding-atom pending-mark behavior

- [ ] UPG-1.3 Qualify alignment and preceding-atom pending-mark behavior.

Purpose: Deliver the declared format/structure profile and exact RGS-1.2-C4 action/result binding.
Context: Native format/structure/prepared command modules; existing module/atom/selection public ports; `core/packages/core/src/engine.ts`; `core/tests/editing/semantic-adapter.ts`; `core/tests/editing/semantic.test.mjs`; original REG-05/REG-07 profile/recipes; `architecture/specs/engine.md`; `architecture/specs/formats.md`; `architecture/specs/editing-regression-suite.md`.
Dependencies: UPG-1.2.
Session scope: One declared alignment/atom profile and pending-mark lifecycle, preserving qualified fragment and history boundaries.
Acceptance: Original alignment and preceding-atom variants have a declared real profile and qualified atomic action/result-selection policy with pending-mark lifecycle. Rich-table metadata or atom cut/transfer proof does not substitute for typing/pending behavior. Original result selection, sentinel and undo/redo assertions pass in native and packed engines; unsupported cases remain honestly open.

Implementation:

- [ ] UPG-1.3-I1 Declare the supported profile in the authoritative contract/fixtures, implement any required native atomic/public behavior using existing APIs and modules, and bind the original variants without silent fixture reduction.

Validation:

- [ ] UPG-1.3-V1 Run nonzero focused original REG-05/07, pending lifecycle, atom/alignment action and result-selection proofs in native/packed layers, plus affected fragment/history/module/editing checks. Record source/fixture/profile/artifact hashes, failures/skips and production gzip admission.

Evidence: `architecture/evidence/editing-regression-suite/primary-api-unblock-20261014/c4/receipt.json` and shared delivery ledger with exact validated commits and nonzero counts.
Handoff: Name each qualified original variant and any remaining predicate; retain all earlier failures and C1/C5-C21 evidence.
Blocked behavior: Leave unchecked for any unmet original assertion; do not claim the profile from unrelated table/clipboard qualification or bypass pending lifecycle.

### Task UPG-1.4 — Integrate qualified repairs and return to roadmap 42

- [ ] UPG-1.4 Integrate qualified repairs and return to roadmap 42.

Purpose: Close the temporary repair phase at a reviewed merged-main checkpoint and resume the preserved primary FIFO with real new owner evidence.
Context: `.roadmap-coordination/queue.json`; integration request/ack/lock and delivery ledger; all c2/c3/c4 receipts; both lane branch/diffs; `architecture/roadmaps/42-editing-regression-suite.md`; preserved primary 42 progress and later queue prerequisites.
Dependencies: UPG-1.1, UPG-1.2, UPG-1.3.
Session scope: One safe integration and qualified handoff checkpoint; no unrelated roadmap implementation or publication.
Acceptance: Reviewed qualified repair commits are in local main; unrelated dirty files and both lane partial sources/logs are preserved; parallel receives main only at a safe checkpoint; meaningful merged-state native/packed/architecture/public-bundle checks pass at actual revisions. Queue and acknowledgments record exact revisions/counts. Existing 42 progress retains all checked work and unclosed original criteria and names the new qualified receipts. 30/14/16/17 remain queued behind full 42, with delivered prerequisites verified in main before each entry.

Implementation:

- [ ] UPG-1.4-I1 Reconcile reviewed completed commits under the lock, using isolated integration and monitor handshake for an affected live lane. Update the ledger, request/ack, queue, progress locations and the queued 42 handoff with actual qualification pins. Never stage another task's partial work or claim completion before safe integration.

Validation:

- [ ] UPG-1.4-V1 Verify actual main ancestry/source hashes and both-lane preservation; run only meaningful merged-state affected checks with nonzero counts and zero failures/skips. Verify the queued 42 worker consumes the new API receipts rather than the old no-op admission handoff; retain all original 42 gates and physical/release gaps.

Evidence: `architecture/evidence/editing-regression-suite/primary-api-unblock-20261014/integration/receipt.json` and exact shared queue/ledger/request/ack state.
Handoff: Mark only this repair phase complete, then enter the already queued original 42 from preserved progress. Do not independently recreate shared APIs or requeue completed 08/09.
Blocked behavior: If safe integration needs a monitor checkpoint, record precise commits, overlapping paths and required lane pause; preserve completed proof and request integration rather than running another feature retry. Do not advance to queued 42 before this gate passes.
