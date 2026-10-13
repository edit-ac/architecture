# Mobile web planning evidence — 2026-10-11

This is research, behavior-contract and roadmap/test planning. No mobile input handler, optional browser API adapter or extension presenter was implemented or device-qualified in this change.

## Delivered scope

- [Platform research](../mobile-web-platform-research.md): mobile input, viewport/keyboard APIs, compatibility sources and version-sensitive corrections.
- [Touch and extension research](../touch-extension-research.md): primary standards/vendor sources and scoped editor regressions, with proposed cases rather than support claims.
- [Mobile web contract](../../specs/mobile-web.md): minimal shared Rust semantics, required web baseline, progressive API/focus/viewport services, optional presenters, capability fallbacks and measured overhead gates.
- [Track 40](../../roadmaps/40-mobile-web.md): 11 parents with [59 cases](../../tests/mobile-web-cases.md). It gates browser release 10 and remains independent of rich extensions and native SDKs.
- [Track 41](../../roadmaps/41-mobile-web-extensions.md): 8 parents with [32 cases](../../tests/mobile-extension-cases.md). It gates expanded qualification 37; web assistance prerequisites are task-specific rather than waiting for all native assistance work.
- Shared specs, requirements, public-doc claim policy, manifest and README link the new owners. Existing runtime work and engine roadmap/progress remain unchanged by this follow-up.

## Decisions and source cautions

The proposed baseline mobile allowance is 5 KiB Brotli JS inside the existing total adapter budget. Freeze actual baseline/profile and admission limits before implementation measurements. Essential touch/input/accessibility behavior remains required; an overrun calls for decomposition or an explicit budget decision. Optional modules must have no import/evaluation, assets, requests or active resources when disabled. Enabled idle work is event-driven; active geometry work is bounded per frame.

Research exposed changing browser behavior and outdated guidance. The contract therefore records requested and observed viewport modes rather than assuming metadata support, treats keyboard/browser facilities as feature-dependent and fallible, and keeps experimental EditContext outside the default editor. API presence or a landed browser patch is not a released-device qualification result.

Review corrected two touch-contract ambiguities: owned drag auto-scroll may refresh coordinates without self-canceling, and unrelated pointers are distinct from competing second-touch/pinch cancellation. Mutation counters attribute changes to the action under test; independent remote updates and OS composition commits are counted separately.

## Validation

| Check | Observed result |
|---|---|
| Baseline validator | 39 files, 471 parents, 1,413 checkboxes, zero errors; [report](roadmaps-before.json) |
| `PATH=/Users/bpstr/.nvm/versions/node/v24.19.0/bin:$PATH npm run check` | Exit 0; 41 files, 490 parents, 1,470 checkboxes, 60 context links, zero errors; [log](roadmaps-after.log) |
| Planning integrity inspection | 19 documents, 190 local links, 91 unique new case IDs, valid referenced MWB/MWX owners and zero errors; [report and source hashes](plan-integrity.json) |
| `git diff --check` | Exit 0, no diagnostics; [log](diff-check.log). New planning Markdown also received whitespace/link inspection |
| Runtime, browser or actual-device tests | Not executed. All implementation and support acceptance remains planned |

These checks establish document/task consistency, not successful editor behavior or measured overhead. Actual browser/device, native selection, mobile IME, VoiceOver/TalkBack, API authorization and phone performance evidence remain owned by the new tasks.

## Resource hygiene

No browsers, temporary web servers, provider sessions or controllers were started. Existing Assign Vite/Astro services were identified and preserved; no process signals were sent. The data volume had approximately 15 GiB free at the final check. Session artifacts are small documentation/evidence files; removed paths: none, reclaimed bytes: zero. Existing build outputs, dependencies and qualification evidence belong to other work and were preserved. Broader disk cleanup is outside this task.
