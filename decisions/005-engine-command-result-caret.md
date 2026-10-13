# Engine-owned heading-end result caret

Date: 2026-10-12. Authority: the user's request to resolve roadmap 04. Status: accepted implementation contract; qualification remains required by WEB-1.14.

## Decision

Keep v5 source identity and existing anchor routing unchanged. The input cut identifies the source edit; it is not the resulting paragraph's caret. HeadingEnd returns an explicit engine-owned result anchor on the new paragraph's fresh source. The shared-source sibling collision in `evidence/engine-heading-end/iteration-6/construction-decision.md` must be covered by positive production-command tests.

The admitted construction is staged Create + Place + Join + Split: register a fresh empty original source, place it after the heading, join it into the heading, split at its fresh end span, and give the destination paragraph attributes. Preparation may use existing helpers directly for these steps. Preserve the heading's identity, level, remaining text/marks, sibling order/identity/text and existing immutable source spans. Admit the aggregate update once on the live document. Creating a new empty source is allowed; copying/reseeding existing text, relocating the sibling or changing original-anchor tie breaking is not.

## Result API and lifetime

- `PreparedEditorEdit` retains `result_caret: Option<Anchor>` on the staged fresh destination, scoped to the document identity. `EditorCommit` exposes `pub result_caret: Option<Anchor>` only after a successful commit. A read-only plan accessor permits the bridge to inspect whether a result is needed before mutation.
- Packed/TypeScript `CommitResult` retains `revision: number` and adds optional `caret: AnchorToken`. HeadingEnd commits return that engine-owned token; existing commands without a result omit the field. A prepared batch returns at most one caret, for its last HeadingEnd; reject a batch that subsequently removes or invalidates that result during preparation.
- The bridge reserves one anchor registry slot and token during successful prepare, before any live mutation. Allocated anchors plus pending reservations share the existing MAX_ANCHORS limit. `can` checks the same capacity without allocating tokens, plans or reservations. Public `anchor()` also respects reservations.
- On successful commit, consume the plan and install its native result anchor under the reserved token without a post-mutation resource failure. Failed/stale commit, releasePlan and disposal release the reservation without exposing a caret. Token-counter overflow fails before mutation. The result is scoped to its engine and released by `releaseAnchor`; it never becomes a caller-chosen node ID or cross-engine handle.
- The keyboard adapter consumes the returned caret, restores native selection through the existing selection bridge and releases it in a finally path. It does not reuse the old input cut as the heading-end result or guess generated owner IDs. Other structural commands retain their current behavior.

## Qualification

Preserve the failed original-cut logs. Update the three native guards and packed guard to assert both unchanged original-cut behavior and the new explicit result caret. In the shared-source collision fixture, the result must resolve to the inserted empty paragraph, subsequent typing must stay there, and the existing sibling must retain its identity/text/marks. Include checkpoint recovery, selected/cross-block replacement, side-effect-free rejection/resource exhaustion/released/stale plans, one local update/history group, selective peer-preserving undo/redo and token release/disposal. Existing anchor, projection, editor and history suites must remain passing. WEB-1.8 then qualifies native keyboard behavior and all Shift+Tab cases on each pinned browser.
