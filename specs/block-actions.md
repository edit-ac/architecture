# Block conversion and configurable block actions

User requirement, 2026-10-23: **Turn into is an alpha requirement of the shared block API and extension system.** It is not a block-menu-only feature. Heading to ordinary text means a lossless conversion to a paragraph, not plain-text extraction or removal of inline formatting. This contract defines required behavior; it does not claim that the new API or presenters are implemented.

Implementation and final test ownership live in the [bounded block-actions plan](../runner-queues/alpha-block-actions-20261023/README.md). Follow the [single-format decision](../decisions/006-single-format-before-publication.md) and [durability invariants](document-durability.md). Use one current document format and one semantic implementation. UI configuration and conversion identifiers are not new document-format versions.

## Lossless presentation changes

Alpha must support paragraph to heading levels 1–6, heading to paragraph, and heading-level changes. The target must be admitted by the host's configured content policy. Converting to the current presentation is a successful no-op with no update, persistence entry or undo group.

These conversions change only the requested presentation. Preserve exact Unicode text and line breaks; supported marks, links and inline atoms; bounded opaque marks and unrelated metadata; block ID and original text/source identities; parent, sibling order and descendants; comments/reference targets and stable anchors. Preserve directional selection and caret position through the existing result-selection contract. A heading's outline section is not its block subtree: conversion must not consume or convert following paragraphs or subheadings. Changing heading level is intentional presentation change, not data loss.

Use the existing prepared format/block primitives where their semantics meet this contract. Do not delete and recreate the block, round-trip through Markdown/HTML, replace its full text, or simulate a transaction with sequential commits. One accepted user action has one semantic transaction and one undo group. Undo and redo restore presentation while retaining concurrent unrelated text and peer edits. Refuse a target shape that cannot meet these invariants rather than downgrade the operation to plain text.

The current prepared batch binding exposes `setHeading { owner, level }` (levels 1–6)
beside `setParagraph`. Both delegate to the existing canonical presentation primitive;
they introduce no second conversion model or document envelope. The default web command
controls capture the selection before taking focus and apply paragraph/heading changes
atomically, preserving directional selection. Slash activation deletes only its captured
query and applies the same primitive in one prepared batch.

## Conversion classification and advanced operations

| Class | Required behavior |
| --- | --- |
| Lossless | Execute directly after current target/policy validation; no confirmation for paragraph/heading changes. |
| Review required | Prepare a concrete impact report and preview. Commit requires explicit approval of that exact still-valid plan. The API defaults to refusing such a commit without that approval. |
| Unavailable | Return a stable reason; expose a disabled item or omit it according to host configuration. Never fall back to text extraction. |

Lossless means preserving the source content and unrelated semantics, not merely producing the same visible string. Undo availability alone does not make a destructive conversion lossless. An extension's assertion of safety is not authorization to discard data.

Advanced conversion families need explicit mappings before they become available:

- Lists, tasks and quotes: preserve item order, nesting, descendants, ordered start, checklist state and container relationships. Specify whether the target is an item, its content block or a container. Flattening or discarding task state requires a report; paragraph-to-heading inside a list must not implicitly unwrap it.
- Code: preserve literal LF/whitespace, language and retained formatting/opaque data. Define how dormant formatting behaves when leaving code, and preserve it through checkpoints and undo. Never parse code text as Markdown during conversion. If a mapping loses language, formatting, or structure, classify and report that loss.
- Tables: define stable row/cell identities, headers, alignment, rich cell blocks, ordering and concurrent-edit behavior before table-to-text or text-to-table is enabled. Do not implement these by serializing a whole table to a string and reparsing it. The outstanding table concurrency design is a prerequisite only for table conversions.
- Assets, embeds, callouts and custom blocks: define preservation of payloads, references, captions, source provenance, children and host permissions. A fallback label is not an equivalent payload. Unknown or disabled-extension data remains retained; absent a qualified mapping, conversion is unavailable.
- Page/database/host-object transformations: require an explicit host operation and its own atomicity, permission and recovery contract. They are not implied by a local block conversion or by copying Notion's menu labels.

Initial alpha support for advanced families is a validated availability/impact contract with unsupported mappings disabled. Shipping an enabled advanced mapping additionally requires its mapping specification and focused preservation proof. Its support cannot be inferred from the presence of both source and destination renderers.

The initial `BLOCK_CONVERSION_CATALOG` in `@edit-ac/core/extensions` publishes these
dispositions. Paragraph/heading content blocks remain lossless, including inside
retained containers; the unavailable container rows do not prohibit changing a
paragraph's presentation inside that container.

| Target/mapping family | Initial disposition | Design owner / stable reason |
| --- | --- | --- |
| Paragraph ↔ heading 1–6; heading level | Lossless, no confirmation | Canonical block presentation primitive |
| List/task/quote containers, code, assets/embeds/callouts/custom semantics | Unavailable | Each semantic mapping owner; `mapping-required` |
| Table ↔ other content | Unavailable | Table concurrency/mapping owner; `table-design-required` |
| Page/database/host objects | Unavailable | Host atomic operation owner; `host-operation-required` |

A registered provider may request review for a qualified presentation primitive.
It still declares full preservation; review does not admit a lossy declaration.
Unsupported destinations/sources return `unsupported-mapping`, including when a
provider requests review. No initial advanced loss mapping is enabled.

## Shared command and target contract

The [standards supplement's selection and operation matrices](editing-behavior-standards.md#es-sel-1--text-block-and-embedded-selection) add planned ephemeral contiguous-block targets, mixed text/object applicability and qualified module movement. They preserve this document's conversion classification, BTA/BTU/BTQ ownership and current durable model; selecting multiple blocks does not make an unqualified conversion available.

Provide one typed capability to capture block targets, enumerate applicable conversions with reasons, prepare a conversion and commit through the existing semantic/persistence owner. Freeze concrete language binding names during the shared API task; do not add competing aliases to every presenter. Menu, slash, keyboard, extension callbacks and headless clients use this capability.

The Rust paragraph/heading boundary is `Document::capture_block_targets`,
`can_convert_blocks`, `prepare_block_conversion` and `commit_block_conversion`.
`CapturedBlockTargets` retains the document identity, ordered IDs, exact structural
versions and presentation tuples, plus optional original directional selection.
Duplicate IDs and ancestor/descendant pairs reject; the API never expands a heading
into its outline section. `BlockConversion` selects paragraph or heading 1–6.
`BlockConversionPolicy` supplies read-only/protected targets and admitted presentations
at preparation and again at commit. Availability uses the same preparation path.
`PreparedBlockConversion` is single-use and delegates to the existing editor
transaction and history owner, returning `EditorCommit` and its selection resources.
Current-presentation targets are omitted only after validating the entire capture;
an entirely unchanged request emits no update or history action. Captures tolerate
unrelated text edits; a prepared transaction still follows the existing exact
admission witness and must be prepared again if that witness changes.

### Atomic transient query cleanup

The current `blockConversion` prepare request may carry one optional
`transientCleanup: { range: StableRange, expectedText: string }` descriptor. This
is ephemeral prepared input, not stored document metadata or a new document format.
Its stable range must resolve to the exact bounded captured trigger/query inside
an admitted conversion target. Validate Unicode/UTF-16 boundaries, expected current
text, target identity, policy and bounds before mutation and again at canonical
commit. A stale, mismatching, foreign-owner, malformed or protected cleanup rejects
the whole intent with no document, update, history or storage side effect.

Prepare cleanup and presentation conversion together through the existing Rust
editor preparation and transaction owner. Preserve all unrelated rich content and
identity, return the post-cleanup selection through the same result owner, and
produce one undoable durable action. Removing a nonempty query remains a real edit
when the target presentation already matches; an absent descriptor preserves the
existing conversion and no-op behavior. Callers cannot delete first, recapture the
modified block, or follow conversion with a separate cleanup commit.

The current WASM and typed engine/extension conversion staging paths carry that
same descriptor without an alternate editor-batch route. Review-required actions
bind cleanup and its exact source preconditions into the frozen impact/prepared
plan; changing the query, target, permissions or reviewed impact invalidates the
approval. Cancellation, expiry, disposal and single-use ownership apply to cleanup
as well as conversion. A provider cannot replace cleanup after approval. Native
ports not exposing this optional web transient input continue through the one
current shared implementation with cleanup absent; no compatibility alias or
persisted wire/ABI change is implied. Corrective owner BTA-2.1 supplies focused
shared/WASM proof before BTU-1.2 resumes.

The current Rust request is `BlockConversionCleanup { range: Selection,
expected_text: String }`, passed as `Option<&BlockConversionCleanup>` to
`prepare_block_conversion` before policy/origin. Native Session forwards `None`.
The WASM `block_actions` prepare request accepts `transientCleanup` with stable
anchor tokens and exact `expectedText`; its nested objects reject unknown fields.
The typed `PrepareRequest` carries the same optional descriptor, while
`prepareBlockConversion(capture, conversion, origin, transientCleanup?)` returns
`plan`, `noOp` and the actual admitted Rust `preview` nodes. Extension
`ConversionIndex.prepare` and `.stage` accept cleanup as their final optional
argument, copy it before yielding to providers, and include it in frozen review
impact. Review fields compare original nodes with this canonical staged projection,
including removed text and retained marks; no JavaScript cleanup transaction or
semantic preview engine is introduced. Approval remains a single-use object bound
to that exact prepared plan, never a serializable command recipe.


Captured targets include document/epoch, stable block IDs, structural versions and the presentation/descriptor preconditions needed by the selected conversion. A presentation change can occur without a structural-version change: structural version alone is insufficient. A delayed action must never retarget the current caret or a replacement block. Unrelated peer text can remain valid for a presentation-only conversion when all touched preconditions still hold; do not reject every peer change solely because the whole-document revision changed.

Multi-block conversion is explicit and ordered. Validate the complete target set on a staged replica and commit all or none. Overlapping ancestor/descendant targets require a declared normalization or rejection rule; no duplicated conversion. Unsupported, read-only, protected, deleted or stale targets reject without partial history, updates or recovery writes. Apply resource bounds to the whole batch.

An advanced plan reports affected blocks/descendants and exact removed, replaced, retained or reinterpreted fields. Preview is derived and causes no mutation. Confirmation binds to the prepared plan, captured preconditions and impact report; expiry, cancellation, permission changes or relevant peer edits invalidate it. Recompute and ask again if the impact changes. Programmatic callers supply explicit policy/approval for that exact plan, never an ambient global allow-loss switch. Use existing single-use plan and cancellation lifetimes.

Return typed outcomes for success, no-op, unavailable, stale target, review required, cancelled and failed admission, with existing storage failure semantics. Availability is advisory; prepare and commit recheck capability, permissions, target validity and bounds. Menu visibility does not confer write permission. Read-only/composition/nested-control ownership is enforced at the appropriate engine/host/input boundary, not by disabling a button alone.

The extension binding is `ConversionIndex.stage(...)`, returning `lossless` with
the ordinary prepared request, `review-required` with an opaque `ConversionReview`,
`unavailable` with a reason, or `cancelled`. Existing typed engine/schema/storage
failures retain their owners. A review contains frozen affected block and descendant
IDs, field-level before/after values and dispositions (`removed`, `replaced`,
`retained`, `reinterpreted`), captured-selection retention and derived presentation
preview. The initial qualified primitive emits retained fields and reinterpreted
presentation only. Report data passes the existing bounded inert-data validator;
there are at most eight live reviews per capture and a five-minute approval lifetime.

`prepare(...)` refuses review-required entries by default. Only explicit
`approve(review, signal)` on the same registry can grant a single-use local request
for that exact already-prepared engine plan. Copying, serializing or editing report
data cannot grant approval. The provider is not rerun at approval. The engine's local
`reviewedBlockConversion` request adapter passes that same token through the existing
host semantic/storage/history commit; it introduces no wire command or document data.
Current capability, policy, target/descendant contents and identity/epoch are checked
again at approval, plan acquisition and commit. For dynamic capability grants, pass
a current-capabilities callback to `stage`, or a live readonly grant collection.
Abort, disposal, expiry, relevant peer changes and permission loss invalidate the
review; recomputation requires a new review. The exact prepared admission witness
can additionally reject an intervening change at the canonical commit boundary.

The attachment-owned `captureConversions` resource exposes `stage` and `approve`
beside direct `run`. It uses the existing `ExtensionCommandSession` and host ports.
Starting another stage or direct run supersedes the previous review; attachment or
capture teardown cancels it. Headless callers dispose reviews in `finally`, including
when host admission refuses them. An approved plan cannot be repurposed for the
separate asset-import reservation path.

## Extension participation

Extend the existing frozen extension registry with bounded, namespaced conversion declarations: source/destination type selectors, label/ordering metadata, option schema, required capabilities, preparation provider and declared preservation constraints. Duplicate/conflicting conversion identities reject before attachment. Core paragraph/heading semantics remain available without a presenter extension; a custom converter cannot override or weaken them.

Providers produce proposals using admitted prepared primitives. Rust validates the resulting command plan, declared field preservation, opaque data and permissions before mutation. No raw CRDT access, DOM serialization, executable document payloads or private secondary history. New data semantics require their engine owner to add a qualified primitive; callbacks cannot fake it with unrelated edits.

Use existing extension-command cancellation and managed resource lifetimes. Registration/indexing occurs at attachment; enumerate only conversions relevant to the captured block types. Disabled menus must not add per-keystroke scans or load optional presenter code. Unknown extension data survives save/reopen/sync while the extension is disabled. On re-enable, registry admission determines which conversions become available.

Conversion identity and the prepared command contract are portable across Rust, WASM and Session/FFI. A JavaScript preparation callback does not imply a native implementation: publish per-runtime availability and require an equivalent provider or portable plan before enabling it there. Native/TUI presenters consume the same actions through their existing platform owners.

## Optional block menu and Insert after

Expose independently configurable menu visibility, reorder handles, allowed conversion destinations, menu items, labels/order and host additions. A configuration that omits the block-actions presenter loads no menu UI; convenience presets must list their inclusion explicitly. Hiding the menu or drag handle does not remove the semantic conversion API; content capability/authorization remains a separate policy. Host additions obey the same captured-target and prepared-command rules.

When the menu is enabled for an editable supported block, include Turn into and Insert after. Turn into is populated from the conversion registry, with an accessible current-type indication and disabled reasons. Keep the captured block selected while moving focus through the menu; Escape/cancel returns predictably without mutation. Touch and keyboard users have equivalent access, and nested controls retain their input owner. Reuse semantic reorder rather than creating a separate move implementation.

Insert after captures a block and creates a sibling immediately after it in its existing parent, even when it has descendants. It does not split, replace or consume the original block. The initial command inserts an empty paragraph when the parent permits it; other types require admitted creation descriptors and explicit host configuration. Revalidate placement and source preconditions, create a stable new identity and focus its editable start in one undoable operation. Unsupported parents, stale/deleted targets and read-only policy reject atomically. The former separator-specific insertParagraph command is not evidence of this general capability.

The captured insertion port is `Document::prepare_insert_after` / `commit_insert_after`,
`EngineHandle.prepareInsertAfter(capture, origin)` (or `prepare({kind:"insertAfter",
capture, origin})`), `EditService::prepare_insert_after` with existing `apply`, and
`NativeSession::prepare_insert_after` with existing commit/cancel methods. It accepts
exactly one target from `captureBlockTargets` / `capture_block_targets`, including
supported containers, code and noneditable atoms; conversion enumeration still
refuses non-paragraph/heading sources. The initial insertion policy uses the current
block policy's read-only, paragraph and protected-target fields, including protected
ancestors. Captures freeze identity/epoch, target structural version/presentation
and optional directional entry selection. Preparation stages one fresh empty paragraph,
same-parent placement after the full subtree and a collapsed result selection at
UTF-16 zero. The canonical transaction establishes causal sibling adjacency, preserves
all original source content and descendants, and owns one history group. Admission
rechecks current witnesses, parent eligibility and policy; no richer creation descriptor
is enabled. Bindings retain bounded engine-local capture/plan/result resources and
report existing typed block-action rejection reasons. Session previews project the
exact staged update, retaining the new stable identity before durable apply.

The web `continue-after` catalog action binds Primary+Enter in a code block or
on an exactly selected noneditable block atom. It uses this same captured port,
result selection and history path with no menu dependency. It always creates a
fresh paragraph, including beside an existing empty paragraph; navigation into
an existing paragraph is not substituted for insertion. See
[explicit continuation](editing-experience.md#explicit-continuation-after-code-and-atoms)
for keyboard ownership and refusal behavior.


## Alpha acceptance and durability

The final block-actions test owners cover exact rich-content preservation; single/multi-target atomicity; stale and deleted targets; metadata-only peer changes; Unicode and directional selection; undo/redo and peer edits; initialized-empty and checkpoint/journal reopening; unknown/disabled-extension retention; custom conversion registration and review/cancellation; identical shared command behavior across direct API, extension, menu and slash/keyboard entry; menu-off API availability; general Insert after; and disposal/read-only/composition/accessibility behavior. Reuse valid prior evidence and add only missing checks. Pure planning or historical v4 checks do not close current-format acceptance.

The default heading/paragraph conversions use the canonical format's existing presentation storage. Do not serialize menu configuration, transient previews, callback code or approval tokens. If advanced content semantics need a storage redesign, finish that design before freezing the one published format. This feature does not close the separate table-concurrency, journal-rollover, document-lifetime or final size/readiness gates.

## Interaction references

[Notion's transformation guide](https://www.notion.com/help/guides/transforming-content-blocks-in-notion) provides the discovery pattern: a block handle menu, slash commands and a formatting toolbar reach transformations. [Obsidian's formatting guide](https://help.obsidian.md/syntax) describes heading levels as presentation expressed through Markdown syntax. These are interaction references, not evidence of either product's data-preservation guarantees. edit.ac's required preservation, concurrency and extension behavior is defined above; conversion is a semantic command, not a Markdown rewrite.
