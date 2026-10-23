# Close table, journal and structural lifetime durability gaps

Status: IN_PROGRESS

## Goal and entry conditions

The preceding source has verified SFC-2.1, SFC-2.2, SFC-2.3. Consume its bounded progress and source-pinned interface proof. These are entry prerequisites, not local task dependencies. Read SFC-1.1/1.2 handoff once; do not rerun inventory or refresh completed source prose.

## Execution policy

Superseding user decision, 2026-10-23: follow `architecture/decisions/006-single-format-before-publication.md` and `architecture/specs/document-durability.md`. One production document schema/profile (the existing witnessed v5 format) and one current implementation per API/wire/ABI contract until publication. Retired development readers and fabricated previous/current release matrices are fixture history only; preserve useful behavior assertions on current-format cases. Never silently relabel, migrate, reset or reseed real data. Retain actual protocol/update-encoding semantics, external formats and document revision/history. Older version-specific runtime clauses in copied historical acceptance are superseded by this decision, not by dropping their semantic regressions.

One serial controller, root `/Users/bpstr/Github/edit-ac`, existing main branches only; no worktree, parallel lane, subagents or second run. Use only active source/progress and its named prerequisite summary. Prior run f6915e733a5ecb9c1c64e7ff is stopped, not restarted. Preserve its dirty work and exact successful/failing evidence. Workers may change only task checkboxes and the Status line in this source. Put delivery summaries, source hashes, reconciliation receipts, timestamps and counts only in the separate progress file or ignored receipts. Never add or update a Current delivery paragraph here: changing acceptance prose on each pass forces another reconciliation. Read current prerequisites from `.roadmap-runner/single-format-feature-first-20261023/readiness.json` and its bounded handoff rows. The first source adapts existing collectors to this successor manifest; old matrix paths are historical evidence only.

Canonical shared-format cleanup and a focused safety gate precede native consumers. Then complete independent features before remaining optimization and comprehensive final suites. Size/latency work gets at most 45 minutes OR two materially different measured hypotheses per batch, whichever comes first. Checkpoint useful code and honest unresolved numbers, then advance independent feature work. Parent completion for a bounded optimization batch never closes its original hard-budget predicate; QPF final gates still own unchanged 512 KiB total/32 KiB editor-JS gzip caps and complete resource/tail proof. Never rerun an unchanged failing inventory. A true semantic/data-safety defect or missing required interface blocks only its dependents.

Use existing narrow deterministic checks during delivery, record meaningful counts and exact input hashes, and add a small regression only for a concrete shared-contract risk. Full test development/matrices stay with final owners; the focused format cutover gate is an explicit prerequisite to safely continue feature work. Port rather than suppress useful old regression assertions. Missing commands, zero cases, failures and required skips cannot pass. Historical fixture-oracle executions do not establish production legacy support. No new production legacy flag or old compatibility crate is allowed.

No paid inference, credentials, `.secrets`, subscription proxy, live fixture recording, paid services, physical-device qualification, publication, push, deployment or new external integration. Use prepared/mock transports for every automated provider case. Appropriate simulators/emulators and OS hosts/VMs must prove claimed target behavior; host-only JNA and responsive browser viewports are not mobile OS proof. Unknown/retired envelopes reject before mutation and preserve original checkpoint/journal recovery bytes. Optional encrypted/cloud release claims remain out of profile without removing baseline or discovered required tests.

One parent per worker, normally 15–45 minutes including focused checks. Commit only validated owned source on current main at safe checkpoints, under the coordination lock; never blindly stage prior dirty paths, stash/reset, or edit another worker's files. Generated evidence/binaries stay ignored and task-owned; keep concise counts/pins/failure dispositions, remove inactive reproducible bulk output. Tear down owned browsers/servers and check disk after substantial builds. Select another local ready parent beside a blocker; when none is ready, record task/source/error/prerequisite fingerprint, owner, attempted repair and exact changed-input resume condition, return BLOCKED, and let the event guard stop the controller. No unchanged retry or automatic restart.

## Epic CANONICAL_ADMISSION_AND_REPLAY — Converge production admission and structural replay

### Task DRA-1.1 — Specify independently mergeable table content

- [x] DRA-1.1 Specify independently mergeable table content.

Purpose: Prevent an ordinary edit to one cell from overwriting a peer edit to another cell.
Context: Originating interface owner SFC-2.3; `architecture/specs/alpha-durability-closures.md`; `architecture/specs/document-durability.md`; `core/crates/editac-core/src/commands/editor.rs` table commands; `architecture/specs/rich-content-extensions.md`; current table codecs and projection owners.
Dependencies: none.
Independent work: Inspect only another local parent's named interface while a dependency is pending; never claim its proof.
Session scope: One 15–45 minute design or implementation boundary. Checkpoint a coherent substep and exact continuation if more work is needed; do not mark the parent complete early.
Acceptance: An authored current-format table descriptor defines stable row/column/cell identity, independently mergeable cell content, structural insert/delete/reorder semantics, same-cell text behavior, unknown metadata and retained conflict policy. Concurrent edits to distinct cells both survive. Explicitly resolve interaction with block conversion, offline peers, undo and serialization. A whole-table winner or warning alone cannot satisfy the requirement.

Implementation:

- [x] DRA-1.1-I1 Choose the current representation before publication; amend rich-content/format contracts and exact consumer acceptance together. Preserve real written bytes and require explicit offline adoption if an incompatible representation is necessary. Retired experimental layouts remain fixtures only, never another runtime reader.

Validation:

- [x] DRA-1.1-V1 Write deterministic input fixtures and expected merged values for two cells, same-cell text and row/column edit-versus-delete. Review every serialized field against core, WASM, Session, HTML/Markdown and native projection consumers; design assertions must not be reported as runtime passes.

Evidence: Separate progress records exact current source/runtime/fixture pins, changed contract, commands and nonzero executed/pass/fail/skip counts. Reuse unchanged applicable proof; generated output stays ignored.
Handoff: Record the chosen representation or lifecycle invariant, remaining concrete substep, interface consumers and final-suite owner. A design parent is not delivered implementation.
Blocked behavior: Keep unproved criteria unchecked. Record the exact failed invariant, owner, attempted repair and changed-input resume condition; no unchanged retry loop, silent data reset or alternate production format.

### Task DRA-1.2 — Implement table merge and identity semantics

- [ ] DRA-1.2 Implement table merge and identity semantics.

Purpose: Deliver the agreed table model before alpha freezes the document contract.
Context: `architecture/specs/alpha-durability-closures.md`; `architecture/specs/document-durability.md`; DRA-1.1 descriptor and fixtures; current core table commands, import/export, WASM and Session/FFI table projections.
Dependencies: DRA-1.1.
Independent work: Inspect only another local parent's named interface while a dependency is pending; never claim its proof.
Session scope: One 15–45 minute design or implementation boundary. Checkpoint a coherent substep and exact continuation if more work is needed; do not mark the parent complete early.
Acceptance: Implement the chosen model in the single production format and every affected consumer. Two replicas editing different cells retain both edits under either delivery order and duplicate/reordered updates; same-cell and structural conflicts follow the authored policy without silent loss. Local undo preserves unrelated peer changes. Current checkpoint reopen and converter round trips preserve cell IDs/content/unknown data. Ordinary table commands cannot replace the whole atom and discard independent edits.

Implementation:

- [ ] DRA-1.2-I1 Replace whole-atom mutation where necessary and adapt command preparation, projection and bindings. Keep one shared owner. Add current-format regression fixtures reproducing the observed LEFT EDIT/RIGHT EDIT loss and structural conflicts; preserve original real data outside any explicit conversion.

- [x] DRA-1.2-I2 Complete stable addressed cell-block creation/order/style/deletion/recovery and unknown metadata preservation in the chosen model, with scoped selective history and staged refusal.

- [ ] DRA-1.2-I3 Complete declared Markdown/HTML/formats, clipboard and native-format transfer: fresh-ID external import and explicit external limitations; validated identity-scoped internal recovery preserves exact IDs, hidden/losing content, unknown data and retained source snapshots.

- [ ] DRA-1.2-I4 Complete the descriptor consumer-field matrix across current WASM/Session/FFI and web/native/terminal DTO consumers. Retire obsolete whole-atom table paths only after current replacements and affected assertions pass; full target-runtime suites retain their existing final owners.


- [x] DRA-1.2-I5 Deliver the shared visible-content export view and explicit limitations, Markdown/native table-text adapters, fresh-ID external import and separate exact recovery capture. Capture whole-document recovery once per export job and preserve the current semantic/history assertions.

- [x] DRA-1.2-I6 Complete HTML and clipboard transfer using the same current visible/export and recovery owners, fresh-ID ordinary import and explicit external limitations. Declared internal recovery retains unknown/hidden/source data; ordinary paste never implicitly activates document-wide recovery.


Validation:

- [ ] DRA-1.2-V1 Run focused core table concurrency and current WASM/Session round trips with both merge orders, checkpoint recovery and undo. Planned regression target `core/crates/editac-core/tests/table_concurrency.rs` must execute nonzero cases. Full discovery and native runtime proof remain QSH/QWB/native final owners.

Evidence: Separate progress records exact current source/runtime/fixture pins, changed contract, commands and nonzero executed/pass/fail/skip counts. Reuse unchanged applicable proof; generated output stays ignored.
Handoff: Record the chosen representation or lifecycle invariant, remaining concrete substep, interface consumers and final-suite owner. A design parent is not delivered implementation.
Blocked behavior: Keep unproved criteria unchecked. Record the exact failed invariant, owner, attempted repair and changed-input resume condition; no unchanged retry loop, silent data reset or alternate production format.

### Task DRA-1.3 — Roll over covered recovery journals safely

- [x] DRA-1.3 Roll over covered recovery journals safely.

Purpose: Keep an actively edited browser document reopenable beyond the 4096-entry bridge limit.
Context: Originating interface owner SFC-2.2; `architecture/specs/alpha-durability-closures.md`; `architecture/specs/document-durability.md`; `core/packages/web/src/storage/checkpoint.ts`, `storage/outbox.ts`, `entry.ts`; `core/crates/editac-wasm/src/bridge.rs`; actual IndexedDB transaction boundaries.
Dependencies: none.
Independent work: Inspect only another local parent's named interface while a dependency is pending; never claim its proof.
Session scope: One 15–45 minute design or implementation boundary. Checkpoint a coherent substep and exact continuation if more work is needed; do not mark the parent complete early.
Acceptance: A durable checkpoint plus bounded uncovered tail can reopen after more than 4096 accepted updates and repeated rollovers. Retire covered recovery entries only after atomic durable publication. Preserve previous-checkpoint fallback, all unacknowledged outbox payloads and receipt ordering; a previous checkpoint must have its required tail. Missing/corrupt newest checkpoints, duplicate updates, empty documents and crashes at each publication/pruning boundary recover or fail explicitly without reseeding or loss. Raising the replay limit or pruning by count alone is insufficient.

Implementation:

- [x] DRA-1.3-I1 Implement a transactional journal/checkpoint retention policy, separating recovery coverage from outbound acknowledgement. Reconcile restore and writer state so covered entries are not passed as an unbounded replay tail. Add focused current-format crash fixtures; do not use memory-only storage as final IndexedDB proof.

Validation:

- [x] DRA-1.3-V1 Exercise 4096/4097 boundaries and at least three rollover cycles on the real current WASM engine with deterministic updates, including unsent updates and fallback to the previous checkpoint. Run focused storage tests during delivery; QWB-1.5 owns full installed IndexedDB/crash/browser qualification.

Evidence: Separate progress records exact current source/runtime/fixture pins, changed contract, commands and nonzero executed/pass/fail/skip counts. Reuse unchanged applicable proof; generated output stays ignored.
Handoff: Record the chosen representation or lifecycle invariant, remaining concrete substep, interface consumers and final-suite owner. A design parent is not delivered implementation.
Blocked behavior: Keep unproved criteria unchecked. Record the exact failed invariant, owner, attempted repair and changed-input resume condition; no unchanged retry loop, silent data reset or alternate production format.

### Task DRA-1.4 — Define the lifetime of retained structural history

- [x] DRA-1.4 Define the lifetime of retained structural history.

Purpose: Separate bounded hostile-input protection from a document that becomes unusable after a fixed number of edits.
Context: Originating interface owner SFC-2.3; `architecture/specs/alpha-durability-closures.md`; `architecture/specs/document-durability.md`; `core/crates/editac-core/src/editor_replay.rs` 4096-record limits; `document.rs` immutable roots and full checkpoints; offline update, anchor and history contracts.
Dependencies: none.
Independent work: Inspect only another local parent's named interface while a dependency is pending; never claim its proof.
Session scope: One 15–45 minute design or implementation boundary. Checkpoint a coherent substep and exact continuation if more work is needed; do not mark the parent complete early.
Acceptance: Specify a viable current-format retention/replay design for long-lived documents, including immutable witnesses, offline replicas, stable anchors, undo/review revisions, unknown data, bounded decoding and resource refusal before mutation. The policy must explain why repeated ordinary moves/splits/joins do not hit a lifetime operation ceiling. If compaction is used, define eligibility, covered state, old-update admission and crash-safe persistence; never silently discard unknown peers or rebase user identity. Merely increasing 4096 is not a design.

Implementation:

- [x] DRA-1.4-I1 Choose and document the shared representation/retention policy and concrete limits. Define deterministic long-session, disconnected-peer, retained-anchor/history and malformed-resource fixtures before changing implementation. Resolve any incompatible current-layout change before the publication freeze; preserve real inputs with explicit offline conversion only where required.

Validation:

- [x] DRA-1.4-V1 Review every retained root and consumer against the proposed algorithm and memory/time bounds. Specify a current-format test with at least 16384 structural operations across multiple save/reopen cycles and a peer disconnected across retention boundaries; design review alone cannot close DRA-1.5 or alpha readiness.

Evidence: Separate progress records exact current source/runtime/fixture pins, changed contract, commands and nonzero executed/pass/fail/skip counts. Reuse unchanged applicable proof; generated output stays ignored.
Handoff: Record the chosen representation or lifecycle invariant, remaining concrete substep, interface consumers and final-suite owner. A design parent is not delivered implementation.
Blocked behavior: Keep unproved criteria unchecked. Record the exact failed invariant, owner, attempted repair and changed-input resume condition; no unchanged retry loop, silent data reset or alternate production format.

### Task DRA-1.5 — Implement durable structural replay over long sessions

- [ ] DRA-1.5 Implement durable structural replay over long sessions.

Purpose: Make the lifetime policy real in the engine and all persistence paths.
Context: `architecture/specs/alpha-durability-closures.md`; `architecture/specs/document-durability.md`; DRA-1.4 chosen policy; core replay/checkpoint/history; WASM and Session storage/update admission.
Dependencies: DRA-1.4.
Independent work: Inspect only another local parent's named interface while a dependency is pending; never claim its proof.
Session scope: One 15–45 minute design or implementation boundary. Checkpoint a coherent substep and exact continuation if more work is needed; do not mark the parent complete early.
Acceptance: Implement the agreed lifecycle without an ordinary 4096-operation lifetime failure, loss of retained document semantics or a second runtime format. The long-session fixture preserves content, identities, anchors, revision/undo semantics and unknown data over at least 16384 structural operations and multiple reopen cycles. A peer disconnected across retention boundaries rejoins under the documented policy without silent edit loss. Malformed/unbounded inputs still reject atomically, with final resource and size caps unchanged.

Implementation:

- [ ] DRA-1.5-I1 Adapt replay/storage/admission consumers together and add `core/crates/editac-core/tests/document_lifetime.rs` as a planned current-format regression owner. Keep structural witness retention distinct from browser journal rollover. Document explicit resource errors and ensure failed changes leave document bytes/history unchanged.

- [x] DRA-1.5-I2 Share one work/node budget across baseline/candidate structural replay, source text/owner/segment indices and qualified-view reuse; preserve typed atomic refusal and existing caps.

- [x] DRA-1.5-I3 Preserve hidden table/source delayed-peer edits and immutable witnesses; prove live selective undo/redo and retained/stale/pruned HistoryStore review across publication.

- [ ] DRA-1.5-I4 Carry the current long-session checkpoint through actual WASM and Session reopen with fresh writers, retained identity/unknown data and typed refusal.

- [ ] DRA-1.5-I5 Adapt Session qualified storage rollover beyond 4096 journal records, fallback, required-tail integrity and independent outbox/quota continuation; preserve recovery bytes and never infer remote acknowledgement.

- [ ] DRA-1.5-I6 Adapt CLI qualified storage rollover beyond 4096 journal records, fallback, required-tail integrity and independent outbox/quota continuation using current documents and atomic durable publication.


Validation:

- [ ] DRA-1.5-V1 Run focused current-format long-session, delayed-peer, retained-history/anchor and negative resource cases, plus the affected WASM/Session reopen boundary. QSH and QWB own complete final functional suites; QPF owns unchanged final memory/latency/size caps. Reuse focused evidence where source pins still apply.

Evidence: Separate progress records exact current source/runtime/fixture pins, changed contract, commands and nonzero executed/pass/fail/skip counts. Reuse unchanged applicable proof; generated output stays ignored.
Handoff: Record the chosen representation or lifecycle invariant, remaining concrete substep, interface consumers and final-suite owner. A design parent is not delivered implementation.
Blocked behavior: Keep unproved criteria unchecked. Record the exact failed invariant, owner, attempted repair and changed-input resume condition; no unchanged retry loop, silent data reset or alternate production format.
