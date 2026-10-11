# Full-delivery requirements review

Date: 2026-10-11. This records planning verification, not implemented editor behavior or a production security claim.

## Decisions and scope

The user confirmed native macOS, Windows and Linux in addition to iOS, Android and web. The three public Apache-2.0 repositories and existing npm package boundaries remain. No placeholder npm release was published. The initial browser release remains independently deliverable; full client delivery and optional encrypted profiles have separate qualification gates.

[Requirements](../requirements.md) map each requested behavior to specifications and tasks. [Primary-source research](followup-research.md) examines Yjs local persistence, Automerge Repo storage/network/catalog patterns, Loro history/diffs, Git source diffs, MCP host responsibilities and protected relay patterns. Examples inform contracts; they are not assumed drop-in implementations for Yrs.

## Resolved conflicts

- Added native storage/session/identity/authorization ports without a second writable semantic document or mandatory cloud host.
- Kept local CLI editing and hosted reconciliation; added a separate TUI track. The host application's MCP integration does not require a CLI MCP server.
- Defined ac:// as a locator resolved through configured authorities, not a credential or permission.
- Separated exact source-byte diffs, canonical Markdown projections and semantic changes. Immutable history storage is distinct from undo state and CRDT garbage collection.
- Required deletion-aware revision validation; a state vector alone cannot enforce the promised edit precondition.
- Bound agent proposals and durable retries to authenticated actor/document/epoch/payload. Receipt lookup precedes new-request expiry/revision checks. Persistence failure freezes dependent mutation/sync publication until journal and receipt recovery succeeds.
- Kept all five native platform tracks independent. iOS and Android require only their specific preparation evidence, not completion of the other platform's probes.
- Gated encryption on a threat model, selected maintained protocol, actual history/attachment integration, platform key providers and independent review. Opaque relays do not provide plaintext agent editing. Optional encryption does not block the base profile.
- Split key-provider delivery by browser, iOS, Android, macOS, Windows, Linux and terminal; named exact planned validation commands. Mock-only evidence cannot establish actual platform key security.

## Checks and preserved work

`npm run check` passed using Roadmap Runner 0.8.0: **24 roadmap files, 292 parent tasks, 876 checkboxes, zero errors**. See [validator result](followup-roadmap-validation.json). The manifest covers the sources and checks acyclic upstream gates; local task dependencies pass the runner validator. Every task has context, bounded scope, acceptance, implementation, validation, evidence, handoff and blocked behavior. Future implementation/test paths are planned artifacts, not claims that those files already exist.

All 102 committed baseline task IDs remain. The eight prior source-reconciliation/CLI additions remain, giving 110 initial-track tasks and 182 follow-up tasks. All 44 reviewed overview/spec/decision/roadmap Markdown documents have resolvable local Markdown links; see [document check](followup-document-check.json).

The active foundation source is byte-identical (SHA-256 `38b5b9d96921dc419471bdce3a85537df40e7bc3255ebbdc4a20c0ace71d0897`). No controller was started, stopped or messaged by this requirements review. Its separate progress and implementation evidence are not part of this planning commit. Runtime checks, platform support, editor capability and encryption remain subject to their development acceptance gates. No model/provider calls, paid inference tests, package installs, editor builds or temporary servers were used for this follow-up review.

## GitHub milestones

Twelve new milestones were created and the existing CLI milestone was updated. The source roadmaps remain the task authority; milestones link to those files rather than duplicating all tasks as issues. See [recorded milestone metadata](followup-milestones.json).

| Milestone | Roadmaps |
|---|---|
| [M6 Shared clients and exact change review](https://github.com/edit-ac/core/milestone/7) | 12, 13 |
| [M7 Host-app agent editing](https://github.com/edit-ac/core/milestone/8) | 14 |
| [M8 First-class extension library](https://github.com/edit-ac/core/milestone/9) | 21 |
| [N2 Native iOS SDK](https://github.com/edit-ac/core/milestone/10) | 16 |
| [N3 Native Android SDK](https://github.com/edit-ac/core/milestone/11) | 17 |
| [N4 Native macOS SDK](https://github.com/edit-ac/core/milestone/12) | 18 |
| [N5 Native Windows SDK](https://github.com/edit-ac/core/milestone/13) | 22 |
| [N6 Native Linux SDK](https://github.com/edit-ac/core/milestone/14) | 23 |
| [M9 Full client product qualification](https://github.com/edit-ac/core/milestone/15) | 20 |
| [S1 Optional document protection](https://github.com/edit-ac/core/milestone/16) | 19 |
| [S2 Encrypted profile qualification](https://github.com/edit-ac/core/milestone/17) | 24 |
| [C1 Local-first and hosted document editing](https://github.com/edit-ac/cli/milestone/1) | 11 |
| [C2 Built-in collaborative TUI](https://github.com/edit-ac/cli/milestone/2) | 15 |
