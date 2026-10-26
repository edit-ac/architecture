# Handle native formatting and replacement intentions

Status: IN_PROGRESS

## Editor-lane adoption — user decision, 2026-10-26

The user explicitly authorized this plan to lead the existing EDITOR queue before performance improvements and testing. Execute in `/Users/bpstr/Github/edit-ac-editor-20261026`; PRIMARY integrations remain untouched in `/Users/bpstr/Github/edit-ac`. This authority supersedes the original planning-only/root-main execution wording below, without changing any task ID, acceptance, dependency or validation requirement. Use one ready parent per worker; workers update only verified live-source checkboxes and Status, with evidence/handoff in the named separate progress file. Retain current ES/EDX/BTA/BTU proof only where exact input applicability holds. Current plan inputs and read-only PRIMARY comparison provenance are preserved; do not edit PRIMARY source, queue, index, progress, artifacts or worker.

Read the active shared lane coordination section before every parent. Require the guarded launcher and live readiness. Checkpoint validated editor-owned deltas under the shared integration lock every two parents/source boundary; preserve inherited dirty bytes and defer mixed hunks. No second EDITOR controller, delegated agents, silent migration, alternate runtime format, paid inference, credentials, external provisioning, push, publication or deployment. Current Rust prepared semantics/shared history remain authoritative. Functional sources01/02/02b lead the FIFO; final source03 follows all functionality and bounded performance improvements. Preserve prepared/mock transports, zero-match/skip failures and exact OS/browser scope. Stop on BLOCKED and do not restart unchanged input.


## Goal and execution contract

Close F07–F10 from the [additional editor comparison](../../research/open-source-editor-input-20261026.md), informed by Lexical, Slate, Quill, CKEditor 5 and CodeMirror 6. Progress: `.roadmap-runner/prosemirror-input-20261026/02b-native-editing-intents.progress.md` from the workspace root. Read only the selected finding and its named source/spec sections.

This is a planned extension of the existing queue, not runner execution authorization. Preserve one guarded serial root-main lane, dirty work, existing source IDs and one current format. Browser events describe intent; existing Rust prepared commands own mutation/history. No new editor engine, provider call, secret loading, input recording, publication or data migration. Update the affected authoritative spec and acceptance together before changing a shared contract.

All four parents are independently eligible. Reuse the exact relevant EDX/ES/PKI receipt if a shared boundary has already changed; unrelated feature or release work is not an entry gate. If a prerequisite is missing, record owner, blocker fingerprint and exact changed-input resume condition, then select another ready parent. A serial queue does not skip a blocked source automatically. Split an oversized task rather than weaken acceptance or loop on an unchanged failure.

One parent per session. Functional checks below use existing fixtures or small task-owned source-bound probes. New permanent tests and full matrices are owned by PKI-3.4/3.5 in final source 03. Evidence for every parent goes in its separate progress section: changed/loaded source, exact selector or manual steps, executed/passed/failed/skipped counts, semantic versus adapter evidence, reused receipts and limitations. Handoff records the next unchecked step, target method, exact failing event/range and task-owned process/output paths. Keep only checkboxes/Status in source; tear down temporary browsers/servers and remove inactive routine output.

## Epic PKI-4 — Preserve non-keyboard edit intent

### Task PKI-4.1 — Route native formatting intentions through semantic commands

- [x] PKI-4.1 Handle supported native beforeinput formatting.

Purpose: A browser/OS formatting action without a shortcut key uses the same selected marks, permissions and history as the existing editor command.
Context: comparison F07; `core/packages/web/src/commands/catalog.ts::resolveCommand`, `input/keyboard.ts::action/execute`, `input/text.ts` beforeinput owner, `commands/formatting.ts`; `specs/platform-editing-services.md` command ownership and ES-FMT-1.
Entry receipts: Applicable current-source ES/EDX and named comparison findings; authenticate required interfaces rather than replay completed work.
Dependencies: none.
Independent work: PKI-4.2–4.4.
Session scope: supported root formatting intentions and rejection ownership, 30–45 minutes including checks. No new mark types or table range-formatting API.
Acceptance: `formatBold`, `formatItalic`, `formatUnderline` and `formatStrikeThrough` reach the existing mark commands once for admitted root targets without a keydown. Forward/backward ranges, pending typing marks and read-only/permission checks agree with shortcut behavior. Native controls, foreign editors and embedded scopes retain ownership. Inapplicable formatting cannot leave browser-only markup or fabricate a semantic commit; noncancelable events use explicit reconciliation/recovery. Unimplemented formatting types are not silently advertised as supported.

Implementation:

- [x] PKI-4.1-I1 Map supported native intention names to existing commands after resolving the actual editing owner and applicability.
- [x] PKI-4.1-I2 Preserve cancelability, duplicate-event correlation, pending marks and history through the current formatting path; document unavailable scopes.

Validation:

- [x] PKI-4.1-V1 Exercise one selected native format intent, its shortcut equivalent and a nested-control/read-only negative control in the existing command-surface fixture. Check marks, selection and semantic commit count. Budget: 3 minutes; final owner PKI-3.4.

Evidence: parent progress entry with native-intent versus actual-menu provenance.
Handoff: exact unsupported input type, target or cancelability case.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-4.2 — Read transfer-carried plain input payloads

- [x] PKI-4.2 Use available plain input text before DOM fallback.

Purpose: Targeted correction does not ignore `text/plain` solely because `InputEvent.data` is null.
Context: comparison F08; `input/text.ts` ordinary beforeinput routing and `#apply`, `input/characters.ts`, reported StaticRange mapping; `specs/web.md` Input routing and ES-INPUT-1.
Entry receipts: Applicable current-source ES/EDX and named comparison findings; authenticate required interfaces rather than replay completed work.
Dependencies: none.
Independent work: the other PKI-4 parents. Existing compatible cross-block replacement remains ES-1.3; do not reimplement it.
Session scope: one input payload decoder and its current prepared replacement route, 30 minutes including checks.
Acceptance: For supported text/replacement intentions, prefer an actual string `data`, otherwise admit available `text/plain` transfer data, distinguishing empty text from missing payload. Preserve the exact reported target, first-selected-character formatting policy, Unicode/control checks and whitespace. Do not parse transfer HTML, invoke a rich paste policy, enable typing rules or read the clipboard service. Missing/ambiguous ranges or payloads keep the documented bounded native fallback/recovery; no guessed target or duplicate commit.

Implementation:

- [x] PKI-4.2-I1 Normalize plain input data with explicit absence/MIME handling and route it through the existing character/range validators.
- [x] PKI-4.2-I2 Connect the normalized value to current insertion/replacement and preserve duplicate, read-only and composition guards.

Validation:

- [x] PKI-4.2-V1 Compare string-data and transfer-data correction over the same reported range, plus empty text and no-plain-MIME controls. Inspect requested target/text and one real-engine result. Budget: 3 minutes; final owner PKI-3.5.

Evidence: parent progress entry separating prepared payload routing from native fallback observations.
Handoff: exact missing payload/range shape or shared replacement receipt.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-4.3 — Separate independent corrections from key notification echoes

- [ ] PKI-4.3 Stop a completed key intent from swallowing a new correction.

Purpose: A distinct replacement before the preceding keyup is processed once instead of canceled as a duplicate.
Context: comparison F09; `input/text.ts::#handle`, `#key/#pending` lifecycle and `TextIntent`; existing input-policy/editing-input correlation fixtures; `specs/web.md` Input routing and INT-1.7/1.12.
Entry receipts: Applicable current-source ES/EDX and named comparison findings; authenticate required interfaces rather than replay completed work.
Dependencies: none.
Independent work: the other PKI-4 parents. Use string-data replacement for delivery; PKI-4.2 is not an artificial prerequisite.
Session scope: ordinary key/beforeinput/input correlation, 45 minutes including checks; composition lifecycle remains with PKI-1.3/ES.
Acceptance: Space keydown → accepted insertText/input → a distinct reported-target replacement before keyup creates a separate accepted intent. The after-keyup equivalent has the same document result. True duplicate notifications still commit once; repeated identical deliberate input is not deduplicated by text equality. History boundaries, selection restoration, canceled keys, blur, missing keyup and composition remain correct. Classification uses actual operation/target evidence rather than clearing all ownership indiscriminately after input.

Implementation:

- [ ] PKI-4.3-I1 Define which event attributes/target evidence correlate an echo and which start a new ordinary edit; document this at the existing owner boundary.
- [ ] PKI-4.3-I2 Apply the correlation rule to terminal key intents while preserving cleanup and existing composition precedence.

Validation:

- [ ] PKI-4.3-V1 Replay the before-keyup correction, its after-keyup control and a genuine duplicate notification; require request counts 2/2/1 for the respective complete sequences and correct real-engine text/selection. Budget: 4 minutes; final owner PKI-3.5.

Evidence: parent progress entry with complete event order, target ranges, counts and synthetic/OS distinction.
Handoff: exact ambiguous event sequence or unchanged prerequisite.


Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.

### Task PKI-4.4 — Admit scoped non-keyboard table text commands

- [ ] PKI-4.4 Route supported generic deletion, line deletion and yank input in cells.

Purpose: Standard platform text intentions have an explicit table-cell policy instead of blanket allowlist rejection.
Context: comparison F10; `modules/tables/current.ts::createCell/edit/insert`, `modules/tables/cell-dom.ts`, existing tableCellInput and cell selection commands; `specs/table-paste-and-editing.md`, ES-KEY-1 and current cell-block identity policy.
Entry receipts: Applicable current-source ES/EDX and named comparison findings; authenticate required interfaces rather than replay completed work.
Dependencies: none.
Independent work: PKI-4.1–4.3. Reuse PKI-2.3 table sequence ownership if delivered; do not duplicate that lifecycle repair.
Session scope: three admitted single-cell-block intentions and safe fallback, 45 minutes including checks; no multi-cell delete or new kill-ring service.
Acceptance: `deleteContent` uses its supported selected/reported range; `deleteEntireSoftLine` honors a supplied/native visual-line target without guessing LF boundaries; `insertFromYank` inserts admitted literal text once. Respect distinct current versus reported selection, cancelability, read-only/protected cells and command applicability. Preserve neighboring cell blocks and table identities. Ambiguous or multi-block targets retain explicit refusal/recovery without partial mutation. Unknown input types remain safely classified rather than indiscriminately allowed.

Implementation:

- [ ] PKI-4.4-I1 Define target/payload requirements per supported input type and reuse current table text/selection commands.
- [ ] PKI-4.4-I2 Add intention routing with native fallback only where its cell scope is safely bounded, preserving the existing sequence owner and diagnostics.

Validation:

- [ ] PKI-4.4-V1 Run one reported-range deletion, one supplied visual-line range and one literal yank plus an unsupported cross-block negative control. Check one accepted transaction per edit and unchanged geometry. Budget: 4 minutes; final owner PKI-3.4.

Evidence: parent progress entry with range origin and actual supported platform scope.
Handoff: exact unsupported intent/range and the native evidence needed to expand it.

Blocked behavior: Record the task/source/error/prerequisite fingerprint, owner and exact changed-input resume condition; preserve original acceptance and dirty work. Select independent ready work when available; otherwise return BLOCKED for the guard. No unchanged retry.
