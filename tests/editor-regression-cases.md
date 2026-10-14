# Additional regression sequences

Qualification amendment (user decision, 2026-10-14): Named target-platform simulators/emulators and desktop OS VMs/test hosts may satisfy platform and release gates when physical hardware is unavailable. Follow the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms) for required runtime checks, tested virtual equivalents for hardware-only observations, counts and physical/virtual provenance. Earlier physical-only/manual-only wording in this document is superseded. This changes accepted evidence, not required implementation or correctness.

Status: planned acceptance, not executed editor support. [Research](../evidence/editor-regressions-round2.md) records the primary issue/report scope; [suite methods](../evidence/editor-testsuite-methods.md) supports the test approach. These cases add precise event/history/architecture sequences to the existing catalogs. A closed issue is not assumed fixed unless the research establishes the patch/release relationship.

Each case uses the real engine and owning adapter, a fresh fixture, explicit before/after semantic state, directional selection/affinity, pending marks, history outcome and attributable update counts. Assert intermediate checkpoints and a next typed sentinel where relevant. Exact fixtures and case bindings are owned by [track 42](../roadmaps/42-editing-regression-suite.md); broader feature cases remain with their original tracks.

## Compound commands and pending marks — RGS-1.2

| ID | Priority | Sequence | Required outcome |
|---|---|---|---|
| REG-05 | P0 | Toggle Bold at collapsed caret → align left through a block command → type; separately remove a preceding rule trigger/atom, and move away/back before typing | Explicit pending-mark lifecycle; no ghost span/default, inherited allowed marks only and no loss on relevant deletion |
| REG-06 | P0 | Plain-only `ab` followed by a block with bold `cd`; backward-delete `b…c` and retain bold `d`; separately replace/format a mixed-context selection | Preserve the unselected bold suffix using the declared no-join/split policy or reject atomically; never strip it or half-delete before discovering incompatibility |
| REG-07 | P0 | Paste prepared `<pre>A</pre><br><pre>B</pre>` into an existing code block and an empty-root control; separately paste across selected text/code boundaries, then undo | Exact retained text/code whitespace, no dropped intermediate range; one undo restores the full source and selection |
| REG-13 | P0 | Prepare text+mark+structure batch; inject final validation failure; retry a valid batch | Failed attempt changes no content, revision/state vector, history, updates or journal enqueue; retry commits once |

## History, grouping and mapping — RGS-1.3

| ID | Priority | Sequence | Required outcome |
|---|---|---|---|
| REG-01 | P0 | Start with end-caret; outer command selects all before its first document operation, invokes nested Bold, restores caret, then undo/redo; separately move caret after an edit; heading-end before a list → type X → undo X → undo paragraph creation → redo twice | Undo restores the intended pre-edit selection; later caret cannot overwrite the history bookmark; paragraph removal restores the original heading-end caret and redo restores the paragraph caret |
| REG-02 | P0 | Type `a`, paste single-character `X`, type `d` with a fixed clock; undo at each boundary | Paste is isolated from adjacent typing; exact content/selection at every undo/redo checkpoint |
| REG-03 | P0 | Type, cut a selection, then type into the collapse point; undo cut separately | Clipboard/cut event and input notifications create one action; cut stays distinct from surrounding typing |
| REG-04 | P0 | Pending local edit → remote insert → rebase through inverse/reapplied mapping → undo/redo; reuse the pinned upstream mapping trace; separately test permitted reparenting | History bookmarks map through the permitted remote changes; unrelated remote content and identity survive |

## Input correlation and composition — RGS-1.4

| ID | Priority | Sequence | Required outcome |
|---|---|---|---|
| REG-14 | P0 | compositionend → input → commit Enter with isComposing=false → deliberate Enter | One finalized composition, no accidental split on commit key, then one deliberate split; no blanket timeout swallowing |
| REG-16 | P0 | Missing/noncancelable beforeinput → native input/observer echo for `a`; next deliberate identical `a` | Exactly `aa` with one commit per actual intent; duplicate notification produces none; payload equality does not deduplicate real input |

## Normalization and schema properties — RGS-1.5

| ID | Priority | Sequence | Required outcome |
|---|---|---|---|
| REG-08 | P0 | Prepare malformed-but-recoverable import under two interacting normalization rules; normalize result again | Bounded fixed point and explicit diagnostics/source preservation; no oscillating repair transactions or silent dropped content |

## Notification and lifetime failure injection — RGS-1.6

| ID | Priority | Sequence | Required outcome |
|---|---|---|---|
| REG-12 | P0 | Commit edit while subscriber throws, unsubscribes and requests another command in separate variants | First commit remains durable/observable once; callback runs after lock release; next command follows declared queue/rejection policy |
| REG-15 | P0 | Queue renderer/subscriber/async completion, destroy editor or replace session, then drain queues | No detached DOM write, refocus, duplicate update or new edit; released resources and old callbacks cannot affect a new editor |

## Custom views and event ownership — RGS-1.7

| ID | Priority | Sequence | Required outcome |
|---|---|---|---|
| REG-09 | P0 | Change a selected heading/custom-view tag and type sentinel as the base case; then add composition and delayed presenter mount variants | Stable semantic identity/mapping, no content loss or stale caret, old view disposed once; native composing ownership respected |
| REG-10 | P0 | Retain an outer selection, focus embedded node-view input, paste/type/cut and deliver secondary controlled-insertion notification; then invoke an outer-editor command | Inner input owns its events; outer document stays unchanged until its own action; selection/focus routing recovers |
| REG-11 | P0 | Drop one internal/external payload across nested handlers with move/copy modifiers; trailing input/observer notifications | Exactly one applicable move/copy/import, correct preserved source and selection; native cancellation or rejected drop leaves content unchanged |

| REG-17 | P0 | Place an insertion anchor before/after a table or atom versus explicitly selecting the node; then type/delete/format | Insertion anchors create adjacent text where allowed; node selection performs the applicable node action; no accidental table overwrite or lost anchor |

## Qualification

Recipes and trace variants use synthetic content and fixed clocks; failures retain minimized traces and upstream links. The machine-readable manifest verifies every catalog ID and existing roadmap owner, but a valid file is not a passed behavior test. Semantic, browser-replay, native-browser and physical or virtual platform claims remain separate. Every guard in the suite contract needs a negative control before its runtime evidence is accepted.
