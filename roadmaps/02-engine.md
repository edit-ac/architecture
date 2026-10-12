# Implement the semantic document kernel

Status: IN_PROGRESS

## Goal and entry conditions

Workspace: `core` (sibling of `architecture`). Deliver only the outcomes below. Read `../architecture/specs/engine.md`, `../architecture/specs/verification.md` and the active task's named context. Paths below are relative to `core` unless explicitly prefixed with `../architecture/`. Planned files are created by their task. Source is controller-owned; write state/evidence in the separate progress file.

Upstream entry gates: `01-foundation.md` complete at current source revision with passing artifact evidence.

Controller update 2026-10-11: The missing paragraph/heading mapping is now specified in `../architecture/specs/schema-v2.md`; ENG-1.16 is authorized implementation/qualification work, not an external information wait. After the in-flight fixed-pair ENG-1.7 boundary, prefer ready ENG-1.16, then finish ENG-1.6. ENG-1.17 selects/qualifies general ownership and ENG-1.18 integrates it before downstream structural work. These new parents split profile qualification from command integration to preserve bounded sessions. Preserve prior marks/foundation evidence and all original acceptance; do not claim the new profiles pass before their own receipts. Workers adopt this source between sessions and reconcile the stale ENG-1.6 mapping deferral against the new fact without the controller rewriting their progress file.

Controller structural unblock 2026-10-11: `../architecture/specs/schema-v4.md` now supplies the exact nested list/quote, check/numbering, code/separator, versioned place and reversible history-control contract. Preserve completed v3 work and ENG-1.8-P1; retire the old unspecified ENG-1.8/1.9 mapping deferrals against this new source. Ready order is ENG-1.19, ENG-1.20, ENG-1.21, then the original ENG-1.8/1.9 boundaries. Qualifications are separate from production integration and original command acceptance. Implement these authorized contracts; if a concrete contradiction/failure remains, provide the exact failing rule, a deterministic reproducer and a bounded repair/split rather than repeatedly asking whether schema work is authorized. All original acceptance remains mandatory. If no ready implementation or unfinished material prerequisite exists, report BLOCKED with a precise controller handoff and stop instead of spending further iterations on unchanged hashes or summaries.

Controller retained-join resolution 2026-10-12: `../architecture/specs/schema-v5.md` supplies the exact ENG-1.9-F1 resolution. Compatibility/editability is captured in immutable split/join preparation witnesses; replay does not re-evaluate it from mutable presentation. Preserve frozen v4 and its positive failure/guard evidence. New profile/tuple qualification ENG-1.22 is ready from completed ENG-1.21; then integrate ENG-1.23 and close full ENG-1.9 acceptance. The previous unspecified contract wait is replaced by these authorized gates. Do not repeat unchanged blocked recovery or feature failures while the new prerequisite is ready. Existing 15 checked parents remain bounded evidence; future consumers use the qualified v5 correction without automatic migration. Reuse matching final checks when only closing a bookkeeping parent: identify the original executed command/counts/receipt and revalidate source hashes instead of rerunning unchanged broad suites.

## Execution rules

Each iteration may implement at most one parent task, including all its implementation and validation substeps. Target 15–45 minutes plus validation; if a boundary is too large, stop with a precise proposed split for the controller. Pick a task only when every named dependency is implemented and validated. Other ready tasks are permitted independent work; a roadmap entry gate remains mandatory for its dependents. Do not launch this roadmap while its upstream gate is unavailable.

Create named checks before invoking them. Record nonzero executed/passed/failed/skipped counts; missing tests and zero-match Rust filters fail acceptance. Run the narrow check, then relevant integration checks. Use prepared fixtures and transports only. No model API tests, live dogfood, background runner startup or publication outside an explicit release task.

Toolchain preflight: before Node/npm or Rust/Yjs exchange checks, explicitly select the installed Node 24.19.0 runtime in the command environment and verify `node --version`. On this Mac prepend `/Users/bpstr/.nvm/versions/node/v24.19.0/bin` to PATH after shell initialization; do not rely on an inherited launcher PATH that a login shell may replace. Use the workspace's pinned rustup toolchain. A runtime mismatch is a local environment repair, not a contract blocker: preserve its failed log, select the pinned runtime, and retry only the affected checks. Do not change dependencies or repeat unaffected passing suites for this repair.

## Epic ENG-1 — Implement the semantic document kernel

### Task ENG-1.1 — Verify the foundation entry gate

- [ ] ENG-1.1 Verify the foundation entry gate.

Purpose: Deliver verify the foundation entry gate as one reviewable boundary.
Context: `../architecture/evidence/foundation.md`; `../architecture/specs/schema-v1.md`; `../architecture/specs/engine.md`.
Dependencies: none.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Foundation evidence is complete and the chosen schema is available; missing evidence blocks this track without changing its acceptance.

Implementation:

- [ ] ENG-1.1-I1 Check upstream completion against the current source revision and rerun the pinned interop fixture. Record schema/profile hashes in this progress file.

Validation:

- [ ] ENG-1.1-V1 cargo test -p editac-core --test interop --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.1` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.1`.
Blocked behavior: Leave `ENG-1.1` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.2 — Implement document identity and initialization

- [ ] ENG-1.2 Implement document identity and initialization.

Purpose: Deliver implement document identity and initialization as one reviewable boundary.
Context: `crates/editac-core/src/document.rs`; `crates/editac-core/tests/initialization.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.1.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Opening existing data never imports defaults twice; duplicate/reordered initialization updates converge; wrong epochs return a typed error.

Implementation:

- [ ] ENG-1.2-I1 Implement new-document and restore as distinct operations; enforce document/epoch/schema identity, unique live clients and explicit initialized state. Reuse the frozen schema.

Validation:

- [ ] ENG-1.2-V1 cargo test -p editac-core --test initialization --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.2` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.2`.
Blocked behavior: Leave `ENG-1.2` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.3 — Implement read projection and incremental indexes

- [ ] ENG-1.3 Implement read projection and incremental indexes.

Purpose: Deliver implement read projection and incremental indexes as one reviewable boundary.
Context: `crates/editac-core/src/projection.rs`; `crates/editac-core/tests/projection.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.2.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Snapshots match fixed fixtures; a single text edit reports only affected nodes and does not rebuild a second mutable document.

Implementation:

- [ ] ENG-1.3-I1 Project stable nodes, attributed text and deterministic placement from Yrs. Build only necessary node/range indexes and update them from touched transaction ranges.

Validation:

- [ ] ENG-1.3-V1 cargo test -p editac-core --test projection --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.3` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.3`.
Blocked behavior: Leave `ENG-1.3` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.4 — Implement relative anchors and UTF-16 conversion

- [ ] ENG-1.4 Implement relative anchors and UTF-16 conversion.

Purpose: Deliver implement relative anchors and UTF-16 conversion as one reviewable boundary.
Context: `crates/editac-core/src/anchors.rs`; `crates/editac-core/tests/anchors.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.3.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Emoji, ZWJ, combining text, RTL and deleted targets have fixed results; malformed offsets fail before mutation.

Implementation:

- [ ] ENG-1.4-I1 Define anchor resolution/deletion results and biased selection endpoints. Validate UTF-16 boundaries with grapheme-aware editing helpers; preserve anchors across remote insert/delete.

Validation:

- [ ] ENG-1.4-V1 cargo test -p editac-core --test anchors --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.4` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.4`.
Blocked behavior: Leave `ENG-1.4` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.5 — Implement prepared text edits

- [ ] ENG-1.5 Implement prepared text edits.

Purpose: Deliver implement prepared text edits as one reviewable boundary.
Context: `crates/editac-core/src/commands/text.rs`; `crates/editac-core/tests/text_commands.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.4.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Invalid preparation leaves updates/state unchanged; valid replacements commit once and produce the expected touched range.

Implementation:

- [ ] ENG-1.5-I1 Separate fallible preparation from commit. Implement insert/delete/replace and nonmutating applicability, with bounded byte/depth limits and explicit transaction origin.

Validation:

- [ ] ENG-1.5-V1 cargo test -p editac-core --test text_commands --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.5` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.5`.
Blocked behavior: Leave `ENG-1.5` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.16 — Qualify versioned paragraph and heading metadata

- [ ] ENG-1.16 Qualify versioned paragraph and heading metadata.

Purpose: Resolve the ENG-1.6 schema dependency with a separately versioned, reproducible block mapping while preserving the frozen foundation.
Context: `../architecture/specs/schema-v2.md`; `../architecture/specs/protocol-v1.md`; `crates/editac-core/src/document.rs`; `crates/editac-core/tests/block_profile.rs`; `fixtures/schema-v2/`.
Dependencies: ENG-1.5.
Session scope: One block-profile qualification boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required projection/admission/test glue. Do not implement general ownership or finish another parent in this iteration.
Acceptance: The exact v2 envelope and sixth typed root reconstruct in Rust/Yjs; empty paragraph/heading metadata, atomic type/level tuples, inherited/overridden split-owner state, retained absorbed metadata, restore, unknown retention and invalid/profile/epoch rejection follow schema-v2. Both exchange directions and duplicate/reordered delivery pass with stable identities and no partial rejection mutation. Original v1 fixtures remain valid; no automatic migration or arbitrary/repeated structure claim.

Implementation:

- [ ] ENG-1.16-I1 Implement explicit v2 creation/restore/admission and the independent owner-metadata mapping, preserving v1 behavior. Create the machine-readable seed, Rust/Yjs exchange fixture and exact profile descriptor; qualify schema-v2's complete edge-case matrix before recording it as supported.

Validation:

- [ ] ENG-1.16-V1 cargo test -p editac-core --test block_profile --locked. Assert the complete schema-v2 matrix, including real pinned Rust/Yjs exchange in both directions, then rerun relevant initialization/projection/anchor/text/format and v1 interoperability checks; record exact nonzero executed/passed/failed/skipped counts and preserved failures.

Evidence: Progress entry `ENG-1.16` and durable `../architecture/evidence/engine-block-profile/receipt.json` with exact commands/counts, profile envelope, source/fixture hashes and unchanged foundation hashes.
Handoff: Record the last completed step and precise remaining mapping/check. Once qualified, target the unchecked block portion of ENG-1.6 in a separate iteration.
Blocked behavior: Leave unchecked on failed/skipped qualification; record owner, exact unblock condition and changed-evidence retry trigger. The supplied schema-v2 contract replaces the old unspecified mapping question. Propose a concrete controller split if this boundary cannot fit; do not silently reduce the matrix.

### Task ENG-1.6 — Implement marks and basic block attributes

- [ ] ENG-1.6 Implement marks and basic block attributes.

Purpose: Deliver implement marks and basic block attributes as one reviewable boundary.
Context: `crates/editac-core/src/commands/format.rs`; `crates/editac-core/tests/format_commands.rs`; `../architecture/specs/engine.md`; `../architecture/specs/schema-v2.md`; `../architecture/evidence/engine-block-profile/receipt.json`.
Dependencies: ENG-1.5, ENG-1.16.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Toggle/apply/remove behavior across mixed selections is deterministic; code and URL policy follow formats spec; invalid attributes do not partially apply. Use ENG-1.16's qualified block profile for paragraph/heading attributes, including empty blocks, levels 1–6, split inheritance/override, absorbed/deleted targets and mixed mark/block atomic rejection. Retain the verified six-mark portion; its partial receipt does not complete the parent. Legacy v1 returns explicit unsupported block formatting rather than acquiring new roots.

Implementation:

- [ ] ENG-1.6-I1 Add bold/italic/strike/underline/code/link marks and paragraph/heading attributes using one validated batch. Define invalid mark combinations and link attribute validation. Consume the qualified schema-v2 owner tuples and include block-only changes in projection/revision/staleness checks; finish empty/derived-owner and mixed mark/block coverage without duplicating the existing marks implementation.

Validation:

- [ ] ENG-1.6-V1 cargo test -p editac-core --test format_commands --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.6` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.6`.
Blocked behavior: Leave `ENG-1.6` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.7 — Implement paragraph split and join

- [ ] ENG-1.7 Implement paragraph split and join.

Purpose: Deliver implement paragraph split and join as one reviewable boundary.
Context: `crates/editac-core/src/commands/structure.rs`; `crates/editac-core/tests/split_join.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.5.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Beginning/middle/end/empty splits and joins pass including remote insert races and deleted targets.

Implementation:

- [ ] ENG-1.7-I1 Implement split/join around stable text anchors and placement rules, preserving marks and concurrent edits according to schema-v1.

Validation:

- [ ] ENG-1.7-V1 cargo test -p editac-core --test split_join --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.7` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.7`.
Blocked behavior: Leave `ENG-1.7` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.17 — Qualify arbitrary and repeatable ownership

- [ ] ENG-1.17 Qualify arbitrary and repeatable ownership.

Purpose: Resolve the fixed-pair representation limit before general engine commands, using one reproducible schema-selection/probe boundary.
Context: `../architecture/specs/schema-evolution.md`; `../architecture/specs/schema-v2.md`; `../architecture/specs/schema-v3.md`; `crates/editac-core/tests/ownership_profile.rs`; `fixtures/schema-v3/`.
Dependencies: ENG-1.7, ENG-1.16.
Session scope: One representation qualification boundary; target 15–45 minutes plus focused validation. Write the exact selected schema before testing; production command integration is the separate ENG-1.18 parent. Provide a concrete ordered split if the bounded probe cannot fit.
Acceptance: The selected v3 layout meets every schema-evolution obligation: non-reserved IDs, two disjoint pairs, at least three sequential transformations, split-after-join across multiple original sources, empty spans, retained marks/block metadata, stable text identities/anchors, deterministic conflict and deletion/recovery semantics, resource bounds and explicit profile admission. Both Rust/Yjs directions, reorder/duplicate permutations and restores converge semantically. No v1/v2 mutation, reseeding, copied text, arrival-order conflict choice or narrowed fixed-pair substitute.

Implementation:

- [ ] ENG-1.17-I1 Select and document exact v3 roots/types/values and ownership/conflict/metadata/admission rules in schema-v3.md. Implement the faithful Rust/Yjs qualification mapping and compare alternatives against the required identity, concurrency and resource constraints; preserve rejected evidence.

Validation:

- [ ] ENG-1.17-V1 cargo test -p editac-core --test ownership_profile --locked. Cover the complete schema-evolution qualification matrix with actual pinned Rust/Yjs binary exchange, semantic/recovery snapshots and nonzero executed/passed/failed/skipped counts; rerun the block-profile and legacy v1 structural interoperability checks.

Evidence: Progress entry `ENG-1.17` and `../architecture/evidence/engine-ownership-profile/receipt.json` with selected descriptor/profile, exact commands/counts, tested source/fixture hashes, rejected alternatives and supported resource envelope.
Handoff: Name the qualified representation and precise production integration work for ENG-1.18. Missing evidence leaves this gate unchecked.
Blocked behavior: Record exact failed requirement, owner/unblock condition and changed-evidence retry trigger; propose a bounded controller split rather than asking for an unspecified representation decision or reducing arbitrary/repeated acceptance.

### Task ENG-1.18 — Integrate qualified general structural commands

- [ ] ENG-1.18 Integrate qualified general structural commands.

Purpose: Upgrade the fixed-pair command baseline to the independently qualified general ownership profile without discarding earlier evidence.
Context: `../architecture/specs/schema-evolution.md`; `../architecture/specs/schema-v3.md`; `../architecture/evidence/engine-ownership-profile/receipt.json`; `crates/editac-core/src/commands/structure.rs`; `crates/editac-core/tests/split_join.rs`.
Dependencies: ENG-1.6, ENG-1.7, ENG-1.17.
Session scope: One production structural integration boundary; target 15–45 minutes plus focused validation. Change the named paths and directly required document/projection/anchor/text/format glue. Do not implement later list/code/history/WASM parents.
Acceptance: Production preparation/commit uses the exact qualified v3 representation. The full original split/join endpoint/empty/Unicode/mark/remote-race/deleted-target matrix passes for arbitrary pairs and repeated transformations, including split-after-join across original sources and mixed block/mark formatting. One validated explicit-origin commit preserves identity; invalid/stale/profile/epoch cases do not partially mutate. Legacy profile behavior and historical receipts remain bounded and intact.

Implementation:

- [ ] ENG-1.18-I1 Integrate v3 creation/restore/admission, owner projection and anchor routing into prepared text/format/structural commands. Replace reserved-pair restrictions only for the qualified v3 profile; preserve explicit legacy bounds and recovery, and define precise errors for unsupported/conflicting targets.

Validation:

- [ ] ENG-1.18-V1 cargo test -p editac-core --test split_join --locked. Verify the complete general-profile production matrix, then rerun ownership_profile, block_profile and relevant initialization/projection/anchor/text/format/v1 interoperability suites; record exact nonzero executed/passed/failed/skipped counts.

Evidence: Progress entry `ENG-1.18` and `../architecture/evidence/engine-general-structure/receipt.json` with exact profile/descriptor, original and added acceptance coverage, changed paths, tested revisions/hashes, commands/counts and preserved failures.
Handoff: Record precise remaining integration/check or the passing profile consumed by ENG-1.8/1.9. Do not reclassify ENG-1.7's fixed-pair receipt as general support.
Blocked behavior: Keep unchecked if any mapping/production acceptance fails or skips; state owner/unblock condition/retry trigger and a concrete controller split when needed. Downstream structural tasks stay locked.

### Task ENG-1.19 — Qualify nested structural metadata and placement

- [ ] ENG-1.19 Qualify nested structural metadata and placement.

Purpose: Resolve the list/quote representation dependency with the exact controller-supplied v4 profile and retained-source structural/history primitives.
Context: `../architecture/specs/schema-v4.md`; `../architecture/specs/schema-v3.md`; `crates/editac-core/tests/structural_profile.rs`; `fixtures/schema-v4/`; `crates/editac-core/src/commands/lists.rs`.
Dependencies: ENG-1.18.
Session scope: One faithful structural representation qualification boundary; target 15–45 minutes plus focused validation. Preserve/reuse ENG-1.8-P1 and existing v3 replay/exchange harnesses. Production profile integration and command behaviors are separate parents.
Acceptance: Exact ten-root Rust/Yjs mapping, nested list/quote/container membership, atomic list mode/start/check metadata, versioned place operations, split/join hierarchy interactions, malformed/profile/epoch/resource rejection, unknown retention and reversible entity controls satisfy schema-v4. Seeded bidirectional exchange, duplicate/reordered concurrent move/move/move/edit/cycle choices, restore, hidden-parent recovery, empty/derived owners and stable original text/mark/anchor identities converge semantically without repair writes or text copies. This is structural qualification only; full code/separator policy and production support await ENG-1.20/1.21.

Implementation:

- [ ] ENG-1.19-I1 Create the exact v4 descriptor, seed and faithful Rust/Yjs projection/admission fixture. Implement every schema-v4 structural/control rule, preserving immutable rows and original sources, and extend the read-only hierarchy validator's known container/depth rules where required. Retain failing and legacy evidence.

Validation:

- [ ] ENG-1.19-V1 cargo test -p editac-core --test structural_profile --locked. Cover every structural/control rule with actual pinned Rust/Yjs binary exchange and nonzero executed/passed/failed/skipped counts; rerun ownership_profile and the ENG-1.8-P1 hierarchy family. The profile remains partly qualified until ENG-1.20 passes.

Evidence: Progress entry `ENG-1.19` and `../architecture/evidence/engine-structural-profile/receipt.json` with exact descriptor/envelope, complete criterion-to-case mapping, commands/counts, source/fixture hashes and preserved failure logs.
Handoff: Record the exact unfinished proof or the passing structural descriptor consumed by ENG-1.20. Do not close ENG-1.8 using fixture-only persistence.
Blocked behavior: Keep unchecked on missing/failed/skipped requirements. Report the exact contract contradiction/reproducer and bounded repair/split with owner/unblock/retry trigger. The supplied v4 contract authorizes this work; another generic schema-selection approval is not a prerequisite.

### Task ENG-1.20 — Qualify code and separator presentation

- [ ] ENG-1.20 Qualify code and separator presentation.

Purpose: Resolve ENG-1.9's mapping dependency using v4's explicit literal-edit and nontrapping separator policy.
Context: `../architecture/specs/schema-v4.md`; `../architecture/evidence/engine-structural-profile/receipt.json`; `crates/editac-core/tests/block_kinds_profile.rs`; `fixtures/schema-v4/`.
Dependencies: ENG-1.19.
Session scope: One code/separator qualification boundary; target 15–45 minutes plus focused validation. Reuse the exact descriptor and exchange transport from ENG-1.19; do not mutate the frozen v3 profile or implement another parent.
Acceptance: Atomic paragraph/heading/code/separator tuples, code language bounds, literal unmarked insertion and retained dormant marks, whitespace/blank-line/empty restoration, matching-language split/join, invalid mixed-batch rejection, nonempty separator rejection and atomic accessible-neighbor reservation follow schema-v4. Both Rust/Yjs directions and duplicate/reordered concurrent metadata/text updates preserve exact content/identities. The combined ENG-1.19/1.20 receipts match one descriptor; production commands remain ENG-1.21/1.9.

Implementation:

- [ ] ENG-1.20-I1 Implement the faithful code/separator command-policy fixture and all schema-v4 block-kind admission cases under the same descriptor. Preserve original text/marks and opaque metadata; prove the last-editable-owner safeguard without partial writes or copied texts.

Validation:

- [ ] ENG-1.20-V1 cargo test -p editac-core --test block_kinds_profile --locked. Execute the full code/separator matrix with pinned Rust/Yjs exchange, then rerun structural_profile and existing formatting/ownership regressions; record exact nonzero executed/passed/failed/skipped counts and preserved failures.

Evidence: Progress entry `ENG-1.20` and `../architecture/evidence/engine-block-kinds/receipt.json` with matching v4 descriptor/hash, complete criterion-to-case matrix, exact commands/counts and source/fixture/artifact hashes.
Handoff: Record remaining exact code-policy proof or the jointly qualified v4 profile consumed by ENG-1.21.
Blocked behavior: Keep unchecked on failed/skipped qualification; name the deterministic failing case and bounded repair/split, owner/unblock condition and changed-evidence retry trigger. Do not defer for an unspecified code/separator mapping now supplied by schema-v4.

### Task ENG-1.21 — Integrate the qualified nested editor profile

- [ ] ENG-1.21 Integrate the qualified nested editor profile.

Purpose: Make the separately qualified structural profile usable by production commands without substituting fixtures for actual engine behavior.
Context: `../architecture/specs/schema-v4.md`; `../architecture/evidence/engine-structural-profile/receipt.json`; `../architecture/evidence/engine-block-kinds/receipt.json`; `crates/editac-core/src/document.rs`; `crates/editac-core/src/projection.rs`; `crates/editac-core/src/commands/structure.rs`; `crates/editac-core/tests/editor_profile.rs`.
Dependencies: ENG-1.19, ENG-1.20.
Session scope: One production profile integration boundary; target 15–45 minutes plus focused validation. Named paths and directly required anchor/text/format/hierarchy/admission glue only; preserve legacy readers and receipts. Original list/code/move/history/WASM parents remain separate and unchecked.
Acceptance: Production v4 create/restore/admission and read-only hierarchical projection match the qualified descriptor. Shared prepared placement, split/join, text/format and entity-control primitives preserve nested structure, original identities/marks/anchors, literal-code insertion and noneditable separator rejection; invalid/stale/profile/epoch/resource batches do not partially mutate. Actual production Rust/Yjs replay and checkpoint restore match the fixture profile, including unknown/recovery data. Legacy profile behavior remains exact; no automatic epoch migration or invented roots.

Implementation:

- [ ] ENG-1.21-I1 Integrate the exact v4 envelope/roots and qualified replay into production creation/restoration/admission, hierarchical snapshots and shared prepared command primitives. Adapt the existing hierarchy prerequisite for list/quote containers and retained descendants. Expose reusable primitives for ENG-1.8/1.9/1.10/1.11 without claiming their full command acceptance here.

Validation:

- [ ] ENG-1.21-V1 cargo test -p editac-core --test editor_profile --locked. Cover actual production bidirectional Rust/Yjs exchange and complete integration/rejection cases, then rerun structural_profile, block_kinds_profile and relevant initialization/projection/anchor/text/format/split_join/ownership/hierarchy/legacy interoperability suites; record exact nonzero executed/passed/failed/skipped counts.

Evidence: Progress entry `ENG-1.21` and `../architecture/evidence/engine-editor-profile/receipt.json` with exact descriptor/envelope, production criterion-to-case mapping, source/fixture/artifact hashes, commands/counts and preserved failures.
Handoff: Record precise remaining integration, or target the original ENG-1.8/1.9 acceptance in subsequent sessions. Retire stale mapping deferrals only against the actual passing qualification facts.
Blocked behavior: Keep unchecked on any missing/failed/skipped prerequisite or acceptance. Supply an exact failing case and bounded repair/split; do not weaken original parents or repeatedly spend sessions on unchanged external waits.

### Task ENG-1.8 — Implement list and quote structure

- [ ] ENG-1.8 Implement list and quote structure.

Purpose: Deliver implement list and quote structure as one reviewable boundary.
Context: `crates/editac-core/src/commands/lists.rs`; `crates/editac-core/tests/lists.rs`; `../architecture/specs/engine.md`; `../architecture/specs/schema-v4.md`; `../architecture/evidence/engine-editor-profile/receipt.json`.
Dependencies: ENG-1.7, ENG-1.18, ENG-1.21.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Nested enter/backspace/indent/outdent fixture transitions match semantic snapshots; illegal hierarchy is rejected before commit. Use the qualified v4 list/quote containers, atomic mode/start/check tuples and versioned placement. Include ordered/unordered/checklist/quote nesting, retained descendant identity/marks, empty-item exit, checked split defaults, numbering and concurrent replay. Reuse ENG-1.8-P1; its read-only proof does not close this production parent.

Implementation:

- [ ] ENG-1.8-I1 Add nested ordered/unordered/checklist and blockquote commands with indentation/outdent limits, list numbering and checked state. Use existing structure primitives.

Validation:

- [ ] ENG-1.8-V1 cargo test -p editac-core --test lists --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.8` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.8`.
Blocked behavior: Leave `ENG-1.8` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.22 — Qualify stable retained-structure presentation

- [ ] ENG-1.22 Qualify stable retained-structure presentation.

Purpose: Resolve ENG-1.9-F1 with immutable split/join preparation witnesses under a separately versioned profile, preserving frozen v4 behavior.
Context: `../architecture/specs/schema-v5.md`; `../architecture/specs/schema-v4.md`; `../architecture/evidence/engine-block-commands/contract-gap.md`; `crates/editac-core/tests/retained_presentation_profile.rs`; `fixtures/schema-v5/`.
Dependencies: ENG-1.21.
Session scope: One corrected representation qualification boundary; target 15–45 minutes plus focused validation. Reuse bounded transport/decoder concepts without modifying the qualified v4 descriptor/mappers. No production integration or second parent completion.
Acceptance: Exact v5 envelope and witnessed split/join tuple shapes reconstruct in Rust/Yjs. Established multi-source joins/splits preserve spans, versions, hierarchy, marks, original identities and anchors across valid later paragraph/heading/language/opaque/empty-separator presentation changes. Fresh incompatible/separator/opaque joins, malformed or incompatible witnesses and invalid mixed batches reject atomically. Seeded bidirectional exchange, concurrent metadata/structural delivery, duplicate/reordered updates, checkpoint restore and control history match schema-v5; no metadata-only resurrection or copied/reseeded text. Legacy v4 fixtures/hashes remain unchanged.

Implementation:

- [ ] ENG-1.22-I1 Create the exact v5 descriptor/seed and faithful Rust/Yjs witnessed operation mapping. Turn the preserved paragraph/language reproducers into positive qualification cases and cover the entire schema-v5 matrix, including split/derived/empty ownership and fresh command rejection.

Validation:

- [ ] ENG-1.22-V1 cargo test -p editac-core --test retained_presentation_profile --locked. Execute actual pinned Rust/Yjs exchange and full positive/negative matrix, then rerun v4 structural/block-kind and legacy ownership regression families. Record nonzero executed/passed/failed/skipped counts, exact source/fixture/profile hashes and preserved failures; no v5 compatibility claim before passing evidence.

Evidence: Progress entry `ENG-1.22` and `../architecture/evidence/engine-retained-presentation-profile/receipt.json` with exact descriptor/envelope, criterion-to-case matrix, original reproducers, commands/counts and tested hashes.
Handoff: Record the exact remaining qualification or the passing witnessed mapping for ENG-1.23. Retire the old generic ENG-1.9-F1 contract wait against this controller resolution without checking its production acceptance.
Blocked behavior: Keep unchecked on failed/skipped qualification; report the precise deterministic failed rule and bounded repair/split. The controller supplied the version/tuple/replay decision; no additional generic schema authorization is required.

### Task ENG-1.23 — Integrate stable presentation commands

- [ ] ENG-1.23 Integrate stable presentation commands.

Purpose: Fix production retained-join metadata conversion using the independently qualified v5 witnesses, retaining strict fresh-command validation and legacy safety.
Context: `../architecture/specs/schema-v5.md`; `../architecture/evidence/engine-retained-presentation-profile/receipt.json`; `crates/editac-core/src/document.rs`; `crates/editac-core/src/commands/blocks.rs`; `crates/editac-core/tests/blocks.rs`; `crates/editac-core/tests/editor_profile.rs`.
Dependencies: ENG-1.22.
Session scope: One production v5 integration boundary; target 15–45 minutes plus focused validation. Named paths and directly required profile/replay/projection/structural/text/format glue only. Do not finish another parent or mutate frozen v4 mapping files.
Acceptance: Actual v5 creation/restore/admission, preparation and replay match the qualified witnesses. The original joined-owner literal replacement/deletion/paragraph conversion and language-change positive cases pass with retained ownership/marks/anchors and one validated commit. Fresh incompatible joins and invalid/stale mixed batches reject without partial writes. V4's PresentationConflict guard remains explicitly legacy evidence; v5 does not use that rejection to substitute for valid metadata-only acceptance. Full blocks acceptance and actual Rust/Yjs checkpoint/replay pass; list/move/format/text/anchor/control and legacy regressions remain valid.

Implementation:

- [ ] ENG-1.23-I1 Integrate the exact v5 envelope and immutable preparation witnesses in production profile selection, staged admission and split/join/editor commands. Preserve the old profile reader and safety guard; scope the old negative regression to v4 and add v5 positive cases without deleting the historical failure or silently migrating epochs.

Validation:

- [ ] ENG-1.23-V1 cargo test -p editac-core --test blocks --locked. Pass the original full canonical code/separator suite including ENG-1.9-F1, then run retained_presentation_profile and relevant editor/list/move/text/format/anchor/structural/control/legacy integration suites with real pinned Rust/Yjs exchange. Record exact nonzero executed/passed/failed/skipped counts, criterion coverage, source hashes and preserved failures.

Evidence: Progress entry `ENG-1.23` and `../architecture/evidence/engine-stable-presentation/receipt.json` with exact v5 descriptor/envelope, original ENG-1.9-F1 positive criterion map, canonical/integration commands/counts and tested hashes. These results may support subsequent ENG-1.9 closure only while matching source hashes and all original criteria remain satisfied.
Handoff: Record the remaining integration failure or target full ENG-1.9 closure using current, matching canonical evidence. No historical safety guard or diagnostic test is positive feature acceptance.
Blocked behavior: Keep unchecked on any failed/skipped prerequisite or positive case; name the exact rule/reproducer and bounded repair/split. Do not defer again for the retained-join decision already specified in schema-v5.

### Task ENG-1.9 — Implement code blocks and separators

- [ ] ENG-1.9 Implement code blocks and separators.

Purpose: Deliver implement code blocks and separators as one reviewable boundary.
Context: `crates/editac-core/src/commands/blocks.rs`; `crates/editac-core/tests/blocks.rs`; `../architecture/specs/engine.md`; `../architecture/specs/schema-v5.md`; `../architecture/evidence/engine-stable-presentation/receipt.json`.
Dependencies: ENG-1.7, ENG-1.18, ENG-1.21, ENG-1.23.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Code whitespace and blank lines round-trip, literal editing avoids rich marks, separators do not trap a document without an editable position. Use the qualified v5 correction with v4's code-language/separator values and original-source identities; preserve dormant marks across conversion, reject newly incompatible joins/nonempty separator conversion and reserve a fresh accessible paragraph atomically when required. Valid presentation/language changes on established multi-source joins must preserve spans, version, parent, absorbed ownership and anchors; PresentationConflict rejection does not satisfy this positive acceptance. Validate stale/mixed-invalid/resource failure without partial writes. Reuse exact matching ENG-1.23 canonical evidence only when it covers every original criterion, recording original execution counts and current hash checks.

Implementation:

- [ ] ENG-1.9-I1 Add code language/text whitespace, hard breaks and separators with explicit insertion/navigation semantics and preserving unknown language labels.

Validation:

- [ ] ENG-1.9-V1 cargo test -p editac-core --test blocks --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.9` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.9`.
Blocked behavior: Leave `ENG-1.9` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.10 — Implement identity-preserving semantic move

- [ ] ENG-1.10 Implement identity-preserving semantic move.

Purpose: Deliver implement identity-preserving semantic move as one reviewable boundary.
Context: `crates/editac-core/src/commands/move.rs`; `crates/editac-core/tests/moves.rs`; `../architecture/specs/engine.md`; `../architecture/specs/schema-v4.md`.
Dependencies: ENG-1.8.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Move/move and move/edit converge without cloning/deleting text identity; nested moves and deleted destinations have explicit results. Use v4's qualified versioned place primitive for leaf/container targets, before-sibling/version checks, subtree identity and deterministic cycle rejection; do not request another unspecified placement schema.

Implementation:

- [ ] ENG-1.10-I1 Implement the selected placement operation, cycle rejection and selection anchoring using schema-v1. Reuse structural concurrency fixtures.

Validation:

- [ ] ENG-1.10-V1 cargo test -p editac-core --test moves --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.10` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.10`.
Blocked behavior: Leave `ENG-1.10` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.11 — Implement origin-aware undo groups

- [ ] ENG-1.11 Implement origin-aware undo groups.

Purpose: Deliver implement origin-aware undo groups as one reviewable boundary.
Context: `crates/editac-core/src/history.rs`; `crates/editac-core/tests/history.rs`; `../architecture/specs/engine.md`; `../architecture/specs/schema-v4.md`; `../architecture/specs/schema-v5.md`.
Dependencies: ENG-1.6, ENG-1.8, ENG-1.9, ENG-1.10.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Remote changes are excluded; one explicit operation produces one undo group even inside the capture timeout; undo after concurrent changes preserves others edits. Use v4's qualified reversible entity controls for structural creation/operation history and scoped text/metadata history; immutable original/container/operation rows and original rich-text identities survive undo/redo. Preserve permanent tombstones and remote bytes, with explicit recovery/anchor results for affected dependent intentions.

Implementation:

- [ ] ENG-1.11-I1 Use Yrs selective history with tracked local origins. Define typing/composition grouping and explicit reset boundaries around paste/format/move; cap history and clear redo correctly.

Validation:

- [ ] ENG-1.11-V1 cargo test -p editac-core --test history --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.11` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.11`.
Blocked behavior: Leave `ENG-1.11` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.12 — Expose batched patches and scoped subscriptions

- [ ] ENG-1.12 Expose batched patches and scoped subscriptions.

Purpose: Deliver expose batched patches and scoped subscriptions as one reviewable boundary.
Context: `crates/editac-core/src/patches.rs`; `crates/editac-core/tests/patches.rs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.11.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: No reentrant transaction panic; irrelevant listeners are not called; observer errors cannot corrupt committed state; unsubscribe removes callbacks.

Implementation:

- [ ] ENG-1.12-I1 Emit versioned changed-node/range, selection and update metadata once per commit. Defer observer callbacks until transactions/locks are released and make subscription disposal idempotent.

Validation:

- [ ] ENG-1.12-V1 cargo test -p editac-core --test patches --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.12` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.12`.
Blocked behavior: Leave `ENG-1.12` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.13 — Exercise seeded replica operation sequences

- [ ] ENG-1.13 Exercise seeded replica operation sequences.

Purpose: Deliver exercise seeded replica operation sequences as one reviewable boundary.
Context: `crates/editac-core/tests/replica_properties.rs`; `fixtures/replica-seeds/`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.12.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: All published seeds converge without losing acknowledged source content or violating schema; test count and bounded schedule coverage are recorded.

Implementation:

- [ ] ENG-1.13-I1 Run deterministic operation schedules for disconnect/reorder/duplicate, all structural commands and undo. Keep failing seeds and compare canonical semantic projections.

Validation:

- [ ] ENG-1.13-V1 cargo test -p editac-core --test replica_properties --locked. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.13` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.13`.
Blocked behavior: Leave `ENG-1.13` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.14 — Bind semantic commands and snapshots to WASM

- [ ] ENG-1.14 Bind semantic commands and snapshots to WASM.

Purpose: Deliver bind semantic commands and snapshots to WASM as one reviewable boundary.
Context: `crates/editac-wasm/src/`; `packages/core/src/`; `tests/wasm-commands.test.mjs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.13.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Built WASM executes shared engine command fixtures and rejects malformed input without partial mutation; disposal is explicit and idempotent.

Implementation:

- [ ] ENG-1.14-I1 Promote the fixture bridge to opaque real engine handles with typed create/read/prepare/commit/anchor/history operations. Validate JS boundary types and propagate structured errors.

Validation:

- [ ] ENG-1.14-V1 npm run build:wasm; npm run build; node --test tests/wasm-commands.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.14` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.14`.
Blocked behavior: Leave `ENG-1.14` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.

### Task ENG-1.15 — Bind updates, restoration and patch events to WASM

- [ ] ENG-1.15 Bind updates, restoration and patch events to WASM.

Purpose: Deliver bind updates, restoration and patch events to WASM as one reviewable boundary.
Context: `crates/editac-wasm/src/`; `packages/core/src/`; `tests/wasm-updates.test.mjs`; `../architecture/specs/engine.md`.
Dependencies: ENG-1.14.
Session scope: One named boundary; target 15–45 minutes plus focused validation. Change only the named paths and directly required test/configuration glue.
Acceptance: Browser storage and sync can use real update bytes; JS and Rust semantic snapshots agree after replay; disposed handles/subscriptions cannot be used.

Implementation:

- [ ] ENG-1.15-I1 Expose update/state-vector encoding, restore/apply, batched patch subscriptions and owned byte buffers with post-transaction callback scheduling.

Validation:

- [ ] ENG-1.15-V1 npm run build:wasm; npm run build; node --test tests/wasm-updates.test.mjs. Assert the acceptance cases above and record build/probe exit results and executed/passed/failed/skipped counts for actual test suites (nonzero matching tests required).

Evidence: Progress entry `ENG-1.15` with changed paths, exact command/result, source and implementation revisions, fixture/artifact hashes, and any preserved failure log. Durable milestone summaries belong in `../architecture/evidence/`.
Handoff: Record the last completed substep, changed symbols/files, exact failing fixture or missing fact, and next bounded action for `ENG-1.15`.
Blocked behavior: Leave `ENG-1.15` unchecked; record BLOCKED/PROBLEM/NEEDS_INFO with reason, owner/unblock condition and retry trigger. Select another dependency-ready task in this track; if none exists, report the gate and stop instead of polling.
