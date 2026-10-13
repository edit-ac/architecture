# Build the continuous browser editing surface

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Deliver only the outcomes below. Read `../architecture/specs/web.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Upstream entry gates: `02-engine.md` complete at current source revision with passing artifact evidence, `03-local-storage.md` complete at current source revision with passing artifact evidence.

## Execution rules

Exit gate: retain all task-specific checks and pass the unfiltered [baseline typing/rendering gate](../specs/web.md#baseline-typing-and-rendering-guarantees), `npm run check:browser-baseline`, against current built artifacts. WEB-1.2 owns whitespace/presentation and shared mounting; WEB-1.8 owns heading-end destination/caret. Planned tracks 38/42 do not postpone these guarantees.

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus validation; if a boundary is too large, stop with a precise proposed split for the controller. Pick a task only when every named dependency is implemented and validated. Other ready tasks are permitted independent work; a roadmap entry gate remains mandatory for its dependents. Do not launch this roadmap while its upstream gate is unavailable.

Create named checks before invoking them. Record nonzero executed/passed/failed/skipped counts; missing tests and zero-match Rust filters fail acceptance. Run the narrow check, then relevant integration checks. Use prepared fixtures and transports only. No model API tests, live dogfood, background runner startup or publication outside an explicit release task.

## Epic WEB-1 — Build the continuous browser editing surface

### Task WEB-1.1 — Verify engine, storage and WASM entry contracts

- [ ] WEB-1.1 Verify engine, storage and WASM entry contracts.

Purpose: Deliver verify engine, storage and WASM entry contracts as one reviewable boundary.
Context: `packages/core/`; `packages/web/`; `../architecture/specs/web.md`; `../architecture/specs/web.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Real engine and persistence attach before ready; missing prerequisites leave this track blocked with exact evidence gaps.

Implementation:

- [ ] WEB-1.1-I1 Confirm engine patches/anchors, local flush, WASM init and storage recovery evidence; make the browser fixture load the real packed core.

Validation:

- [ ] WEB-1.1-V1 npm run build:wasm; npm run test:browser -- recovery. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.1` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.1`.
Blocked behavior: Leave `WEB-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.2 — Render and map a single contenteditable root

- [ ] WEB-1.2 Render and map a single contenteditable root.

Purpose: Deliver render and map a single contenteditable root as one reviewable boundary.
Context: `packages/web/src/dom/render.ts`; `packages/web/src/surface.ts`; `tests/browser/render.spec.ts`; `tests/browser/web-example.test.mjs`; `../architecture/specs/web.md`.
Dependencies: WEB-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Text/heading/marks/lists render; a one-character edit does not replace unrelated nodes; read-only rendering uses safe text/attributes. Enforce the baseline typing/rendering guarantees in specs/web.md: exact leading/trailing/repeated authored spaces have visible advance across paragraphs, headings, marked runs, list items and code, including incremental updates and heading tag replacement under ordinary host CSS. Both public mount paths and examples share adapter assembly/defaults, reject duplicate root ownership and release adapters without disposing a borrowed engine.

Implementation:

- [ ] WEB-1.2-I1 Render semantic blocks/marks in one contenteditable root, with stable node-to-DOM mapping and explicit noneditable atoms. Patch only changed spans. Own whitespace presentation in the renderer and reuse the shared surface binding in persistent mounts and host-owned examples.

Validation:

- [ ] WEB-1.2-V1 npm run test:browser -- render. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.2` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.2`.
Blocked behavior: Leave `WEB-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.3 — Map DOM selections to relative anchors

- [ ] WEB-1.3 Map DOM selections to relative anchors.

Purpose: Deliver map DOM selections to relative anchors as one reviewable boundary.
Context: `packages/web/src/dom/selection.ts`; `tests/browser/selection.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Cross-block, emoji, empty-block and deleted-node selections have stable tested behavior without stale absolute targets.

Implementation:

- [ ] WEB-1.3-I1 Translate forward/backward multi-block selections, caret affinity and UTF-16 positions to engine anchors. Restore selection after local/remote patches.

Validation:

- [ ] WEB-1.3-V1 npm run test:browser -- selection. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.3` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.3`.
Blocked behavior: Leave `WEB-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.13 — Qualify the input and composition protocol before routing

- [ ] WEB-1.13 Qualify the input and composition protocol before routing.

Purpose: Resolve the pre-input qualification boundary using the delivered engine, storage, DOM renderer and selection bridge.
Context: `tests/browser/input-policy.spec.ts`; `fixtures/browser-input-policy/`; `packages/web/src/input/protocol.ts`; `packages/web/src/dom/`; `scripts/test-browser.mjs`; `../architecture/decisions/004-browser-input-composition.md`; `../architecture/specs/web.md`; `../architecture/specs/editing-regression-suite.md` (G01/G05/G09 and Input and command protocol).
Dependencies: WEB-1.3.
Session scope: One protocol and qualification probe; reuse the packed-WASM/storage/selection fixture. Create only the named paths and directly required test/configuration glue. Production text routing remains WEB-1.4; production composition/remote routing remains WEB-1.6/1.7. Track 42's shared recipe driver is a later integration boundary and is not an entry prerequisite here.
Acceptance: A versioned ADR fixes native temporary composition ownership, buffered intermediate updates, finalization/cancellation, blur/read-only/dispose handling, stable-target remote overlap/deletion policy, intent identity/terminal disposition, commit-key handling and identified renderer-echo suppression. Its implementation basis is nonzero passing real-DOM/real-engine protocol probes, including duplicate notifications followed by a deliberate identical edit. Drafting the ADR alone does not pass. Qualified browser mechanics and prepared event replay are explicitly separated from actual OS/IME/device support evidence.

Implementation:

- [ ] WEB-1.13-I1 Build a minimal input-protocol probe around real packed engine commands, production renderer/selection/storage, real DOM mutations and actual protocol handlers. Capture native browser key/input/observer traces; exercise prepared missing/noncancelable/observer-first/duplicate permutations, separate composition sessions and commit keys, buffered finalization/cancel, remote insertion/deleted stable targets and disposed generations. Define the ADR from the observed outcomes before production routing changes. Track attributable commit/update/history/journal effects and use bounded generation-aware settling without fixed sleeps; identity cannot be text equality or a blanket debounce.

Validation:

- [ ] WEB-1.13-V1 Create and run npm run test:browser -- input-policy against pinned Chromium/Firefox/WebKit with the real packed WASM; assert authored content/caret expectations, final disposition, one commit per real intent, zero intermediate/canceled commits, retained independent deliberate edits and identified echo suppression. Record exact command/exit, nonzero executed/passed/failed/skipped counts per engine, source/fixture/artifact hashes and native-versus-prepared trace provenance. Run relevant render/selection regressions for changed shared paths. Missing engines/checks or skipped required mechanics remain incomplete; actual OS IME/device runs remain final qualification work.

Evidence: Progress entry `WEB-1.13` and `../architecture/evidence/browser-input-policy/receipt.json` identify the ADR revision, probe/engine revisions, passing case/guard coverage, actual browser profiles, retained traces and qualification limits.
Handoff: Record last completed substep, missing proof or minimal failing trace, exact changed paths and next bounded action for `WEB-1.13`.
Blocked behavior: Leave `WEB-1.13` unchecked with owner/unblock condition/retry trigger. Propose a controller split if the probe exceeds the session boundary; preserve its acceptance. WEB-1.4 remains dependent on passing qualification.

### Task WEB-1.4 — Reconcile ordinary input exactly once

- [ ] WEB-1.4 Reconcile ordinary input exactly once.

Purpose: Deliver reconcile ordinary input exactly once as one reviewable boundary.
Context: `packages/web/src/input/text.ts`; `tests/browser/input.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.13.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Typing/deleting never double-applies, model and DOM agree after each input, and unrelated DOM remains intact.

Implementation:

- [ ] WEB-1.4-I1 Handle cancelable beforeinput commands and native browser input reconciliation for ordinary insert/delete. Suppress observer echoes and emit one prepared semantic operation.

Validation:

- [ ] WEB-1.4-V1 npm run test:browser -- input. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.4`.
Blocked behavior: Leave `WEB-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.5 — Support noncancelable input fallback

- [ ] WEB-1.5 Support noncancelable input fallback.

Purpose: Deliver support noncancelable input fallback as one reviewable boundary.
Context: `packages/web/src/input/reconcile.ts`; `tests/browser/reconcile.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.4.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Prepared spellcheck/autocorrect/paste-like mutation fixtures reconcile once or surface an explicit unsupported recovery state; no whole-document HTML diff.

Implementation:

- [ ] WEB-1.5-I1 Handle input events without usable beforeinput and a bounded MutationObserver fallback. Limit reconciliation to known affected blocks and guard renderer-authored mutations.

Validation:

- [ ] WEB-1.5-V1 npm run test:browser -- reconcile. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.5`.
Blocked behavior: Leave `WEB-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.6 — Preserve local composition ownership

- [ ] WEB-1.6 Preserve local composition ownership.

Purpose: Deliver preserve local composition ownership as one reviewable boundary.
Context: `packages/web/src/input/composition.ts`; `tests/browser/composition.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.5.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Multi-event composition generates one intended edit with no intermediate renderer replacement; cancel/blur paths do not duplicate or discard committed input.

Implementation:

- [ ] WEB-1.6-I1 Track composition lifecycle, baseline anchors and final commit boundary. Keep the active composing subtree browser-owned and group one completed composition intentionally in history.

Validation:

- [ ] WEB-1.6-V1 npm run test:browser -- composition. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.6` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.6`.
Blocked behavior: Leave `WEB-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.7 — Reconcile remote edits during composition

- [ ] WEB-1.7 Reconcile remote edits during composition.

Purpose: Deliver reconcile remote edits during composition as one reviewable boundary.
Context: `packages/web/src/input/composition.ts`; `tests/browser/composition-remote.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.6.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Remote insert and remote delete of the target do not silently overwrite local composition or redirect text; stale targets produce an explicit result.

Implementation:

- [ ] WEB-1.7-I1 Buffer/defer patches touching composition while applying independent remote changes. Define target-deleted behavior that preserves captured composition text for recovery.

Validation:

- [ ] WEB-1.7-V1 npm run test:browser -- composition-remote. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.7` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.7`.
Blocked behavior: Leave `WEB-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.14 — Add atomic heading-end Enter to the packed engine

- [ ] WEB-1.14 Add atomic heading-end Enter to the packed engine.

Purpose: Deliver the missing engine/WASM prerequisite for context-appropriate heading-end Enter without separate live split/format transactions.
Context: `crates/editac-core/src/commands/editor.rs`; `crates/editac-core/src/editor.rs`; `crates/editac-core/tests/heading_end.rs`; `crates/editac-wasm/src/bridge.rs`; `packages/core/src/engine.ts`; `packages/core/src/index.ts`; `tests/wasm-commands.test.mjs`; `tests/wasm-command-types.ts`; `crates/editac-core/src/anchors.rs` (reuse existing routing); `../architecture/specs/engine.md` (Atomic heading-end Enter); `../architecture/decisions/005-engine-command-result-caret.md`; `../architecture/evidence/browser-keyboard/iteration-8/controller-split.md`.
Dependencies: WEB-1.7.
Session scope: One additive prepared command and packed binding, including named Rust/WASM checks and directly required glue. The user/controller authorizes these engine and command-API changes here; this is prerequisite implementation within this track, not an external authorization wait. WEB-1.8 owns the subsequent browser adapter continuation. Preserve current v5 schema, source contracts and prior evidence.
Acceptance: Rust `HeadingEnd { owner, at }` and packed `{ type: "headingEnd", owner, at }` stage the entire operation before one live commit. A nonempty heading's end cut preserves its identity/level/text/marks, creates one following empty paragraph and returns a separate engine-owned fresh-source result caret at offset zero there; input-cut routing stays unchanged. Native prepared/commit result_caret and packed CommitResult.caret obey Decision 005 reservation, resource, release and lifetime rules. Selected and cross-block replacement work in the same prepared batch. `can`, stale/invalid/read-only/disposed rejection are side-effect free under the existing boundary policies. One local update/history group and peer-preserving undo/redo pass. Interior/empty headings and list/quote/code behavior remain with their existing commands.

Implementation:

- [ ] WEB-1.14-I1 Implement and export the additive headingEnd command under the authoritative engine contract, including staged destination attributes, real prepared-batch selected replacement, stable resulting caret, admission/resource checks and selective history. Create independently authored deterministic Rust and packed-WASM/type cases; use real engine updates and fixed peer schedules. Adapters must not guess generated owner IDs or emulate the operation using two live commits.
- [ ] WEB-1.14-I2 Complete the open C2 under Decision 005: stage admitted fresh-source Create + Place + Join + Split; retain PreparedEditorEdit.result_caret and return EditorCommit.result_caret, expose optional branded CommitResult.caret, and reserve its token/anchor capacity before live mutation. Qualify the shared-source sibling, follow-up typing, selected/cross-block, recovery and reservation/lifetime guards with unchanged original input-anchor behavior. This assignment authorizes the new result fields and construction; preserve historical failures rather than treating old input cuts as output carets.

Validation:

- [ ] WEB-1.14-V1 Run cargo test -p editac-core --test heading_end --locked --offline; npm run build:wasm; npm run build; node --test tests/wasm-commands.test.mjs; npm run typecheck. Every new Rust/WASM heading-end case must execute and pass; record exact command/exit and nonzero executed/passed/failed/skipped counts, semantic update/history effects, source/packed-artifact/fixture hashes and preserved failures. Run relevant anchor/projection/editor/history regressions and native bridge reservation checks for changed shared paths, including the previously failed shared-source guards under Decision 005. No paid inference or provider transports.

Evidence: Progress entry `WEB-1.14` and `../architecture/evidence/engine-heading-end/receipt.json` map each contract criterion to actual passing cases and record immutable source, implementation and packed-artifact revisions/hashes.
Handoff: Record last completed substep, changed symbols/files, exact missing proof or failing fixture and next bounded action for `WEB-1.14`.
Blocked behavior: Keep `WEB-1.14` unchecked until its command is qualified. Propose a concrete split if it outgrows the session boundary. WEB-1.8-C2/V1 remain pending on this prerequisite; unchanged absence of the API is the assigned implementation work, not a reason to repeat dependency scans.

### Task WEB-1.8 — Bridge structural keyboard commands and undo

- [ ] WEB-1.8 Bridge structural keyboard commands and undo.

Purpose: Deliver bridge structural keyboard commands and undo as one reviewable boundary.
Context: `packages/web/src/input/keyboard.ts`; `tests/browser/keyboard.spec.ts`; `../architecture/specs/web.md`; `../architecture/specs/editor-interactions.md` (Tab policy and keyboard shortcuts).
Dependencies: WEB-1.14.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Enter creates the context-appropriate block while Shift+Enter inserts a same-block hard break (literal LF in code); selected replacement, cross-block splits/joins and list indentation preserve selection. Enforce specs/web.md baseline heading-end behavior with an immediately following list, with and without trailing spaces: native selection/Enter, exact new paragraph/caret, next typed sentinel, unchanged list identity/parent/text, one commit/history boundary, and undo/redo. Toolbar formatting retains the captured selection. Tab/Shift+Tab indent/outdent applicable lists and indent/dedent code while preserving authored whitespace and selection direction; in prose they move focus forward/backward without document updates. Escape then Tab/Shift+Tab provides one-shot forward/backward focus escape from code/lists without mutation. Inapplicable list actions preserve native focus escape. Platform navigation follows specs/editor-interactions.md; keyboard/menu undo use only semantic history and exclude remote edits. Track 38 extends the regression matrix and table navigation once table presenters exist; basic guarantees remain baseline responsibilities.

Implementation:

- [ ] WEB-1.8-I1 Handle Enter/Shift+Enter/Backspace/Delete/contextual Tab/list navigation and platform historyUndo/historyRedo using engine commands; retain native navigation where correct. Add toolbar command applicability.
- [ ] WEB-1.8-I2 Replace heading-end-needs-engine-command with the qualified headingEnd command from WEB-1.14, consume and release its CommitResult.caret under Decision 005, including selected replacement and stable caret/history behavior; preserve prior C1 evidence and complete the existing C2 continuation before the full unfiltered keyboard check.
- [ ] WEB-1.8-I3 Verify explicit Shift+Tab behavior: list outdent, single-caret and multiline code dedent, native backward focus in prose, and Escape–Shift+Tab backward escape from code/lists. Reuse existing passing list/code cases and execute the added native backward-focus cases; any repair must preserve selection direction, whitespace, composition ownership and zero document/history/journal effects for focus-only actions.

Validation:

- [ ] WEB-1.8-V1 npm run test:browser -- keyboard. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.8` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.8`.
Blocked behavior: Leave `WEB-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.9 — Implement internal-fragment and literal clipboard

- [ ] WEB-1.9 Implement internal-fragment and literal clipboard.

Purpose: Deliver implement internal-fragment and literal clipboard as one reviewable boundary.
Context: `packages/web/src/clipboard/fragment.ts`; `tests/browser/clipboard.spec.ts`; `../architecture/specs/web.md`.; `crates/editac-core/src/commands/editor.rs`; `crates/editac-wasm/src/bridge.rs`; `packages/web/src/clipboard/html.ts`; `../architecture/specs/formats.md`
Dependencies: WEB-1.8.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Copy/cut across blocks round-trips supported semantics; malformed payloads never execute markup or cause partial edits; literal paste remains literal. Include native-menu and beforeinput-only mobile paste, noncancelable event replay, plain paste commands and Ctrl/Command+Shift+V (plus macOS Command+Option+Shift+V), codec precedence, safe rich HTML, supported marks/headings/code/lists/quotes, single undo/redo and zero edits after failed cut/canceled async paste. Full Markdown dialect and extension codecs retain their named future owners.

Implementation:

- [ ] WEB-1.9-I1 Version internal fragment payloads, validate bounds/schema, add copy/cut and literal paste, and keep paste into code literal. Fall back safely from invalid fragments.

Validation:

- [ ] WEB-1.9-V1 npm run test:browser -- clipboard. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.9` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.9`.
Blocked behavior: Leave `WEB-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.10 — Implement visible and ready lifecycle

- [ ] WEB-1.10 Implement visible and ready lifecycle.

Purpose: Deliver implement visible and ready lifecycle as one reviewable boundary.
Context: `packages/web/src/lifecycle.ts`; `tests/browser/lifecycle.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.9.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Stale preview cannot become editable and overwrite recovery; network is unnecessary for local activation; initialization failure leaves an accessible recovery view.

Implementation:

- [ ] WEB-1.10-I1 Adopt revision/schema-tagged previews only when matching recovered state; otherwise replace them before enabling input. Expose visible, ready, localCommitted and failed/recovery states.

Validation:

- [ ] WEB-1.10-V1 npm run test:browser -- lifecycle. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.10` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.10`.
Blocked behavior: Leave `WEB-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.11 — Dispose editor resources predictably

- [ ] WEB-1.11 Dispose editor resources predictably.

Purpose: Deliver dispose editor resources predictably as one reviewable boundary.
Context: `packages/web/src/editor.ts`; `tests/browser/dispose.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.10.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Repeated create/edit/destroy reaches a stable resource plateau; pending operations cannot mutate a destroyed editor; unsaved flush failures are observable.

Implementation:

- [ ] WEB-1.11-I1 Destroy observers/listeners/timers/subscriptions and WASM handles; abort pending async preparation. Define flush-before-destroy policy and idempotence.

Validation:

- [ ] WEB-1.11-V1 npm run test:browser -- dispose. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.11` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.11`.
Blocked behavior: Leave `WEB-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task WEB-1.12 — Add accessibility checks and device test protocol

- [ ] WEB-1.12 Add accessibility checks and device test protocol.

Purpose: Deliver add accessibility checks and device test protocol as one reviewable boundary.
Context: `tests/manual/browser-input.md`; `tests/browser/accessibility.spec.ts`; `../architecture/specs/web.md`.
Dependencies: WEB-1.11.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Automated mechanics pass and the manual protocol lists steps/expected outcomes and required devices. Device availability does not block this implementation track; actual support evidence belongs to REL-1.6. The manual protocol must include mobile native menu and keyboard plain-paste variants, clipboard permission denial and actual iOS/Android browser device records; no native SDK tests run in this track.

Implementation:

- [ ] WEB-1.12-I1 Add automated semantics/keyboard tests and a runnable manual protocol for real IME, RTL, screen readers, autocorrect and mobile selection. Label actual device runs as final qualification work.

Validation:

- [ ] WEB-1.12-V1 npm run test:browser -- accessibility; review tests/manual/browser-input.md for complete cases. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `WEB-1.12` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `WEB-1.12`.
Blocked behavior: Leave `WEB-1.12` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.
