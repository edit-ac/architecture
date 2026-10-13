# Desktop interaction research integration

Date: 2026-10-12. Scope: research and extension of existing development contracts. No editor implementation, release, benchmark, native-device run, provider call or runner startup was performed.

## Sources and decisions

- [Desktop conventions](../desktop-editing-research.md): Word/Pages/LibreOffice selection, moves, tables, history; TextEdit and IDE search/code conveniences; input/drag standards.
- [Native protocols](../native-editing-research.md): Apple, Android, Windows and GTK text services, native command surfaces, async transfers and device observations.
- [Architecture, extension and performance](../editing-performance-extension-research.md): explicit official profiles, deterministic command ownership, bounded work and measured mixed-feature interaction.

BRK-04 already required selected text plus Enter. The additional contract makes backward/cross-block/whole-document and incompatible selections explicit; two independently authored recipes assert replacement, undo, redo and a next typed sentinel. Text dragging is now distinct from block reordering: source/destination mapping, self-drop, copy effects, selection/history and cancellation are specified. External/cross-document copy remains the safe default; advertised move needs a qualified receipt and recovery policy without claiming distributed atomicity.

Optional first-party search and code tools reuse existing semantic commands, history and presenters. Known configurations get validated version/capability/precedence contracts; actual combinations qualify downstream, preventing a dependency cycle. Native OS behavior remains in adapters. Multi-cursor, macros, overwrite and paginated word-processing models are explicitly outside these scoped additions, rather than implied by comparison with Word or an IDE.

## Integration

Still **42 roadmap files**. Added seven bounded parents within existing tracks: EXT-1.12; RCH-1.21/1.22; INT-1.15–INT-1.18. Total **512 parents**. Existing handoff dependencies include the new tasks. Native SDK, native/terminal/mobile extension, architecture-fitness and qualification task acceptance is extended without changing whole-track dependency edges or worker progress.

[Additional catalog](../../tests/desktop-editing-cases.md): **77 cases**, bringing the planning manifest to **272 cases**, **14 recipes**, **45 independent state/effect checkpoints**, **14 guards**. Cases are planned; neither a row nor valid JSON establishes executable coverage. RGS infrastructure remains upstream of feature execution and records unimplemented/unsupported variants honestly. Existing performance budgets are preserved; new profiles require comparable raw samples and continuous-interaction/native evidence. No measured improvement or universal perfection is claimed.

## Validation evidence

- `check-before.log`: pre-edit architecture check succeeded, including 14 planning-validator tests (14 passed, 0 failed, 0 skipped).
- `check-after-initial.log`: first integrated architecture check succeeded with the expanded inventory, same 14/14 tests and zero failures/skips.
- `check-final.log`: final validation after focused review; see exact status/counts in the log.
- `plan-integrity.json`: unchanged roadmap identities, original task preservation, exact added tasks, no whole-track manifest edits, preserved budgets, and relative-link checks.
- `sources-before.json` and `status-before.txt`: source snapshot and pre-existing dirty/untracked state, retained to distinguish this extension from earlier work.
- `hygiene.txt`, `cleanup.json`, `disk-candidates.txt`: no task browser/server candidates; removed three finished-session helper files (195,568 bytes). Free space remains 7.8 GiB. Existing `core/target` is about 6.1 GiB and requires active-task/ownership review and authorization before any broader cleanup. Missing `docs/node_modules`/`docs/dist` are recorded inventory omissions, not removed paths.

These checks validate planning integrity and the fixture validator. Browser gestures, native APIs, full editor behavior, device compatibility and performance remain the responsibility of the named implementation/qualification tasks.


## Focused review corrections

Independent desktop, native and architecture/performance reviews found and resolved shared-session versus view-local history ambiguity; an insufficient whole-document replacement oracle; a missing destructive selection-scoped Replace All oracle; native clipboard/device evidence ordered before its actual owner; mismatched comparison variables; and a missing selected-text-drag prerequisite for mixed rich-content performance. These were planning reviews, not the Deep Review skill or implementation audits. Final check: 42 roadmaps, 512 parents, 272 cases, 14 recipes, 45 checkpoints, 14 guards; 14 planning-validator tests passed, 0 failed, 0 skipped. Whitespace check passed. Relative Markdown links resolved and all original parent IDs remained present.
