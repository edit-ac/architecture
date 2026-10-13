# Editing regression suite planning verification

Date: 2026-10-11. Scope: researched regression contracts, fixture integrity and roadmap integration. No editor runtime, browser, device, dictation service or paid provider was exercised by these checks.

## Result

The [suite contract](../../specs/editing-regression-suite.md) records fourteen prevention boundaries. The [manifest](../../tests/editing-suite/suite.json) indexes 195 catalog cases: 87 interaction, 59 mobile baseline, 32 mobile extension and 17 additional regression cases. Twelve hand-authored recipes define 37 ordered checkpoints with document state, directional selection, pending marks and attributable commit counts. Case links indicate related scenarios, not complete variant coverage.

[Upstream regression research](../editor-regressions-round2.md) records twelve failure patterns from ProseMirror, Tiptap, Lexical, Slate and CKEditor, distinguishing reported bugs from confirmed fixes. [Testing-method research](../editor-testsuite-methods.md) adds independent oracles, fixed clocks, explicit settling, bounded property generation, failure minimization and assertion sensitivity.

The architecture audit found useful prepared text/format/structure primitives and stale-plan checks. Those do not yet prove atomic compound editing, resulting selection, pending marks, history or post-commit subscription behavior. The contract requires the responsible engine capability before dependent recipes may pass. Browser input and native-device compatibility likewise require their real drivers. These are implementation gates, not claims that the defects are already prevented at runtime.

Review tightened two details: applyBatch ranges address the virtually updated prepared state before one final commit; staged asynchronous work settles at each step while its declared request remains pending, allowing deterministic remote-edit races. Pending marks distinguish contextual derivation (`null`), explicit suppression (`[]`) and explicit overrides.

## Checks performed

- `PATH=/Users/bpstr/.nvm/versions/node/v24.19.0/bin:$PATH npm run check`: exit 0. [Raw output](check.log) records 42 roadmaps, 498 parent tasks, 1,494 checkboxes and no roadmap errors; 195 cases, 12 recipes, 37 steps, 14 guards and no fixture errors; 14 validator contract tests passed, zero failed/cancelled/skipped/todo. These fourteen tests exercise the planning validator, not the editor.
- A local relative-link check of the five new principal Markdown documents found 39 links and zero missing targets. [Report](link-check.json).
- `git diff --check`: exit 0. [Raw output](whitespace-check.log) is empty.
- [Source hashes](source-hashes.json) identify the planning inputs associated with these checks. Runtime binding and immutable engine/adapter/profile evidence remain track 42 work.

The [initial roadmap check](roadmaps-before-integration.json) intentionally predates manifest integration and contains nine errors: an unregistered track and its eight parent-prefix errors. It is retained as failed intermediate evidence; `check.log` records the corrected integrated result. [Initial fixture validation](corpus-first-check.json) and the [validator development run](validator-contract-tests.log) are retained separately.

## Workspace hygiene

No browser or server was started by this work. Existing Assign Vite/Astro services and an Assign Playwright run belong to other work and were preserved. No build or dependency installation was performed. The session's fixture and evidence directories were approximately 84 KiB before this note. The data volume had approximately 11 GiB available at the final check. No artifacts were removed and no disk space was reclaimed; existing builds and other workspaces were left intact.
