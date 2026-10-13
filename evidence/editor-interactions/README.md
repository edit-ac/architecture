# Interaction planning evidence — 2026-10-11

This change is researched behavior specification and roadmap/test planning. It does not implement or qualify browser keyboard handling, dictation, screen-reader support or a speech provider.

## Delivered scope

- Primary-source research: [editor behavior and upstream regressions](../editor-interaction-research.md), [dictation and accessibility](../assistive-input-research.md).
- Authoritative additions: [everyday interactions](../../specs/editor-interactions.md), [optional assistance](../../specs/assistive-input.md).
- [Case catalog](../../tests/editor-interaction-cases.md): 87 unique cases in 12 behavior groups, with initial state/action/expected result and explicit automated/device ownership.
- [Track 38](../../roadmaps/38-editor-interactions.md): 14 parents; [track 39](../../roadmaps/39-assistive-input.md): 11 parents. Browser release now requires track 38; expanded ecosystem qualification requires track 39. Platform prerequisites in 39 remain task-specific.
- Baseline browser/slash acceptance and shared specs point to the new contracts. Existing rich-content slash work reuses the baseline semantics and owns catalog-scale qualification.

## Implementation boundary

Inspected core paths: `packages/web/src/index.ts` and `packages/react/src/index.ts` are empty module scaffolds. Rust has prepared text/format commands and grapheme/anchor helpers, but the inspected text commands reject cross-node replacement and existing split/join tests restrict the frozen original block pair. These primitives do not establish browser editing behavior. Track 04 requires the engine and local-storage gates; this task does not bypass them or modify the active engine work/progress.

Repository HEADs at final validation: architecture `26d3502`, core `2696304`. Both have pre-existing working changes; these commit IDs are context, not immutable evidence of this uncommitted planning change. [Plan integrity](plan-integrity.json) records hashes of the new contracts, case catalog, roadmaps and manifest.

## Checks performed

| Check | Result and evidence |
|---|---|
| Baseline roadmap validator | 37 files, 446 parent tasks, 1,338 checkboxes, zero errors; [raw report](roadmaps-before.json) |
| Final `PATH=/Users/bpstr/.nvm/versions/node/v24.19.0/bin:$PATH npm run check` | Exit 0; 39 files, 471 parent tasks, 1,413 checkboxes, 30 context links, zero errors; [log](roadmaps-after.log) |
| Planning integrity inspection | 20 documents, 159 local links checked, 87 unique case IDs in 12 groups, valid referenced INT owners; zero errors in [report](plan-integrity.json) |
| `git diff --check` | Exit 0, no diagnostics; [log](diff-check.log). New planning Markdown also received a whitespace/link inspection |
| Runtime behavior tests / actual OS or AT checks | Not executed; no implementation was added and all such coverage remains planned |

The initial one-off case counter used a letters-only prefix expression and omitted `A11` IDs. Its failed cardinality report is preserved in [initial failure](plan-integrity-initial-failed.json). Correcting the checker to accept alphanumeric prefixes recovered those rows; no acceptance case was removed. One explicit default-shortcut case was then added, bringing the final catalog to 87.

Research review corrected inline-vs-fenced-code equivalence, formatting inheritance after Enter, popup internal-focus activation, unclassified input eligibility, IME commit-Enter ordering, extension-disabled device qualification, and accepted-text versus raw-transcript privacy boundaries.

## Process and disk check

No browser, temporary server, controller, provider session or microphone was started. Existing Assign Vite and Astro listeners were outside this task and preserved. No process signals were sent. The data volume had approximately 16 GiB available. This session produced small documentation/evidence files, no reproducible build output eligible for cleanup; removed paths: none, reclaimed space: zero. The inspected 1.8 GiB `core/target` belongs to existing engine work and was preserved along with dependencies and qualification evidence. Broader disk cleanup is outside this change.
