# WEB-1.14 unchanged-v5 construction decision

Authority: immutable source `source-e70e728e1701.md`, revision `6fed2016c7ca49b14c374ff211c9850ac5726ce44570f42d2c69f4d0a0cdd06d`; WEB-1.14/I1/V1, C2 stable destination/caret requirement. This decision changes no source/spec/API/schema.

## Demonstrated candidates

| Candidate | Existing admitted operations / symbols | Destination ownership | Required original cut | Decision |
| --- | --- | --- | --- | --- |
| Current split + paragraph attributes | `prepare_editor` HeadingEnd branch; `editor::split`; v5 `split` | Empty span of heading source; later typing belongs to older shared-source sibling | Resolves to older sibling | Preserved three native failures and pending packed guard; no unchanged feature rerun |
| Fresh original paragraph, placed after heading | `register` / Create + `editor::place` / Place | Fresh `n` source; typing X stays in paragraph; unrelated IDs/spans/marks preserved | Still resolves to older sibling, because fresh source cannot match its source identity | Executed positive diagnostic; also lacks the specified split operation |
| Fresh empty original, placed after heading, joined into heading, split on its fresh end span, paragraph attributes | Same register/place; `editor::join`; v5 `join`/`split`; `anchors::capture` on staged fresh source | Fresh source in derived `o` paragraph; original heading identity/level/runs and sibling IDs/spans/runs/parents retained; typing X stays in paragraph | Still resolves to older sibling; a *new* fresh-source right anchor works | Executed positive diagnostic; satisfies admitted source creation and actual split construction, but cannot return the required original cut through unchanged routing |

Both new probes prepare on a disposable real v5 Document and admit one aggregate Yrs update on the target. This is a construction experiment, not a production HeadingEnd prepared command or semantic history qualification. Restored checkpoints preserve both the new anchor's correct destination and the original cut's sibling routing. Enable(false) of a fresh original yields Deleted; disabling the derived split is structural undo, restoring its retained source (and X) to the joined heading. Those existing policies remain unchanged.

## Exact constraint

`engine.md` Atomic heading-end Enter requires resolving the right-biased cut to the resulting paragraph at zero, preserving unrelated blocks/remote edits and current v5. `schema-v5.md` Profile/version and Presentation-independent structural replay retain source-relative cuts and v4/v3 span rules. `schema-v3.md` Atomic operations and Presentation/anchors/deletion require immutable source identities, no copying/delete-reinsert for structure, and After choosing the latest starting span at an empty tie.

Production `anchors::capture` stores source identity plus StickyIndex; `anchors::resolve` filters by that same source identity and chooses `candidates.last()` for Right. With authored order heading, new empty paragraph, existing tail sibling, the original source cut is still the tail sibling's start. If the destination uses that source it loses the Right tie to the later sibling. If the destination owns a fresh source, it does not match the original anchor. Register/place/join/split/presentation/control operations cannot make the original source token refer to the fresh source; moving/deleting the existing sibling, reseeding/copying its tail or changing candidate ranking breaks the stated preservation/routing contracts. This is the collision-shape conflict, not a claim that all v5 paragraph constructions are impossible.

The fresh Join+Split candidate demonstrates an admitted construction; blanket source-creation impossibility is disproven. The remaining controller choice is narrower than the previous proposal: reconcile the result identity, or explicitly version shared-boundary ownership/routing.

## Exact external unblock action

Preferred controller design decision: revise the next authoritative WEB-1.14 snapshot and Atomic heading-end Enter spec to distinguish the input cut from an explicit engine-owned fresh-source stable *result* anchor. Name the prepared/commit result fields and packed token allocation/release/resource policy in `commands/editor.rs`, `bridge.rs`, `packages/core/src/engine.ts` and their checks. Authorize staged Create+Place+Join+Split (or another specified admitted construction); retain unchanged original-anchor behavior and all heading preservation, selected replacement, one local update/history group, rejection and peer-preserving undo/redo criteria. No v5 schema/replay change is needed for the demonstrated construction itself. Update the three original-cut guards and packed guard only under that reconciled result contract, preserving their failed logs.

Alternative: if the *same original cut* must identify the new paragraph even before an existing shared-source sibling, provide a versioned ownership/anchor contract and explicitly name mapper/admission/anchor paths plus qualification. That changes the latest-starting-span rule and cannot be smuggled into this additive command.

Neither option is adopted by this worker. Retry only when the next immutable source/spec supplies the selected result/ownership construction. Remaining unchecked WEB-1.8 (including I2/I3), WEB-1.9, WEB-1.10, WEB-1.11 and WEB-1.12 depend sequentially on WEB-1.14; no second parent is ready. Original I1/V1/C2 remain open. No build/WASM/feature regression suite rerun, deployment or provider call occurred.

## Diagnostic evidence and limits

`cargo test -p editac-core --test heading_end heading_end_v5_construction --locked --offline`: final exit 0; 2 executed / 2 passed / 0 failed / 0 ignored or skipped; 12 existing cases filtered out. The filtered acceptance cases are not counted as passes. `constructions-qualified-diagnostic.log` and `.exit` retain exact results. Initial 2/2 probe log remains. The added control-policy check had a zero-executed compile error (wrong variant name), then 1 passed / 1 failed under an incorrect deletion oracle for disabling a split; both failures remain. The oracle was corrected to the existing structural-undo rule, with no production change.

No original acceptance criterion closes. This delivers the supervisor's bounded permitted-construction/conflict decision, rather than another unchanged hash audit or repeated failed feature check.
