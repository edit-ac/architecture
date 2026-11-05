# Text and block editing standards gap plan

Status: PLANNED

This controller index adds 18 bounded parents to close the specific residuals in the [standards research](../../research/text-editing-standards.md) and [behavior contract](../../specs/editing-behavior-standards.md). It is a planning supplement to existing owners, not a new editor architecture or a 44th canonical product track. The review inspected the current dirty workspace on 2026-10-24; reauthenticate implementation and accepted receipts before delivery. These files neither establish runtime conformance nor authorize starting, enqueueing, resuming or refreshing an active runner source.

The existing guarded serial root-main runner and its sources/progress remain unchanged. The [editing-experience queue](../editing-experience-20261024/README.md) already owns current-consumer prerequisites, shared/native history selection, breaks, platform delivery and feature boundaries. Its checked CFC and EDX-1 parents are not reopened here. Consume their valid current-source receipts. BTA/BTU/BTQ retain conversion, general Insert after and optional block-menu ownership; ES tasks amend targeted selection/applicability/movement seams rather than implement those features again. No new runner, alternate worktree, provider call, publication or production-data conversion is part of this plan.

## Ordered sources

Only the four worker sources below are prospective queue entries; this index is not a worker input. All source checkboxes remain unchecked until actual implementation and scoped checks pass. Each progress path is relative to the workspace root and lives outside source Git.

| Order | Source | Parents | Outcome | Progress |
|---|---|---:|---|---|
| 1 | [01-text-boundaries-and-composition.md](01-text-boundaries-and-composition.md) | 4 | Declared deployed Unicode profile, safe optional browser APIs, shared replacement applicability, web cross-block IME staging | `.roadmap-runner/editing-standards-20261024/01-text-boundaries-and-composition.progress.md` |
| 2 | [02-platform-input-and-navigation.md](02-platform-input-and-navigation.md) | 4 | macOS direct/IME replacement, host language/direction, conventional TUI navigation | `.roadmap-runner/editing-standards-20261024/02-platform-input-and-navigation.progress.md` |
| 3 | [03-block-targets-and-movement.md](03-block-targets-and-movement.md) | 5 | Ephemeral contiguous block selection, accessible explicit entry, mixed applicability, preserved typed-atom moves | `.roadmap-runner/editing-standards-20261024/03-block-targets-and-movement.progress.md` |
| 4 | [04-final-conformance.md](04-final-conformance.md) | 5 | All new test development, missing-case coverage, current consumer build evidence and honest support handoff | `.roadmap-runner/editing-standards-20261024/04-final-conformance.progress.md` |

[The planning manifest](manifest.json) records source order, local parent dependencies and progress paths. It is not an executable runner configuration. ES-1.3 is the true shared prerequisite for ES-1.4 and native ES-2.1/2.2. ES-2.3/2.4 can progress independently of native input once their own receipts exist. ES-3.4 move admission is independent of the block selection UI. Earlier-file prerequisites appear as named entry receipts, not cross-file `Dependencies:`. A serial queue does not execute later independent files around a blocked current source; the controller decides any safe reordering explicitly. No functional parent depends on final testing as an ordering convention.

## Requirement and existing-owner crosswalk

Each row has one final coverage owner for its distinct assertions. A shared task may feed several rows; its test cases must not be copied across suites. Preserve existing case IDs and reuse compatible EDX/BTQ/INT results. An existing owner that already proves the precise residual requires receipt reconciliation rather than duplicate code.

| Contract clause | Selected delta / preservation | New delivery parents | Existing canonical owner | New final owner |
|---|---|---|---|---|
| ES-TEXT-1 | Authenticate UTF-16 ingress and byte/scalar/grapheme boundaries; exact text/no silent normalization | ES-1.1; ES-1.3 for replacement seam | Engine/INT-1.4/1.8; current-format CFC/EDX gate | ES-4.1 |
| ES-TEXT-2 | Publish deployed Unicode data/tailoring; optional Segmenter/modify fallback and safe cuts | ES-1.1/1.2 | INT-1.4/1.5 | ES-4.1 |
| ES-TEXT-3 | Host language/base-direction inheritance and native visual layout; honest logical TUI scope | ES-2.3/2.4 | INT-1.5; existing native/TUI owners | ES-4.1 (GUI/profile); ES-4.4 (terminal) |
| ES-INPUT-1 | Cross-block compatible prose replacement and composition staging/commit/cancel | ES-1.3/1.4; ES-2.1/2.2 | INT-1.7; native input; EDX history/break owners | ES-4.2 |
| ES-KEY-1 | Preserve native modifiers/AltGraph/IME and add supported terminal word/document/page commands | ES-1.2; ES-2.4 | INT-1.6; [TUI 15](../../roadmaps/15-tui-client.md)/[36](../../roadmaps/36-terminal-extension-integration.md), EDX-2.5 | ES-4.1 (browser fallback); ES-4.4 (terminal/profile) |
| ES-SEL-1 | Add view-local contiguous sibling selection and typed captured command targets without changing text anchors | ES-3.1/3.2/3.5 | INT-1.5/1.15/1.18; existing table selection; BTA/BTU target seams | ES-4.3 |
| ES-BLOCK-1 | Explicit partial-text/whole-object applicability with preserved tails, one transaction and typed refusal | ES-3.3; consume ES-1.3 | INT-1.3/1.4/1.10/1.16; EDX-2.6; BTA for conversions only | ES-4.3 |
| ES-BLOCK-2 | Capability matrix and identity-preserving moves for qualified current typed atoms | ES-3.4/3.5 | Current Move/Place and reorder owners; DRA table/lifetime contracts; BTA/BTU | ES-4.3 |
| ES-FMT-1 | Preserve current mixed mark/pending mark/link/search behavior; repair only confirmed mixed-target applicability residuals | ES-3.3 | INT-1.3/1.18, EDX-2.6 and existing search/link owners | ES-4.3 for new mixed-target assertions; unchanged claims reuse existing evidence |
| ES-AX-1 | Visible keyboard block selection/return, ownership priority and announced selection; Escape-then-Tab unchanged | ES-3.2/3.5; ES-2.3 capability labels | INT-1.13/1.14, [assistive 39](../../roadmaps/39-assistive-input.md), final [43](../../roadmaps/43-physical-device-verification.md) | ES-4.4 |
| ES-INT-1 | Existing atomic fragment/cut/drag pipeline and unknown-data retention; qualify new typed targets/moves | ES-3.3/3.4 | INT-1.10/1.16/1.17, BTQ, current durability owners | ES-4.3 |
| All clauses / build compatibility | Exact current-source implementation, build/typecheck, deterministic behavior and runtime-support claims remain separate | Consume all delivery receipts | CFC/current consumers and existing final qualification owners | ES-4.5 |

Current BTA sources are [02b-shared-block-actions.md](../single-format-feature-first-20261023/02b-shared-block-actions.md); BTU remains in [03-regression-oracles-and-version-scaffolding.md](../single-format-feature-first-20261023/03-regression-oracles-and-version-scaffolding.md). Final conversion proof remains BTQ in [43-full-shared-suites.md](../single-format-feature-first-20261023/43-full-shared-suites.md) and [45-full-web-suites-part-2.md](../single-format-feature-first-20261023/45-full-web-suites-part-2.md). Their presence does not prove execution. New block selection may expose only currently available providers; unavailable conversions cannot silently become text extraction.

## Scope decisions

Adopt expected text editing, platform keyboard ownership and structured-block behavior through the existing prepared engine, stable identity and single shared history. The Unicode standard defines text algorithms; it does not prescribe every shortcut or editor UI. Record the implementation's deployed Unicode data rather than upgrading to the latest release merely to match a document date. Browser/native layout owns visual bidi navigation and affinity; the terminal keeps its documented source-order profile.

Block selection starts with contiguous siblings/subtrees, a visible keyboard-accessible command and explicit return to text. Keep existing table/embedded selection ownership. Do not adopt Notion's Escape takeover; active composition/popup cancellation and the existing Escape-then-Tab focus exit win. Keep view-local selection out of the durable document format. Typed-atom moves preserve original identities and payloads; unavailable unknown/custom/table kinds stay inert until the existing representation and preservation contract qualifies them.

Generic block Duplicate, synced blocks, page/database products, arbitrary discontiguous block selection, code multicursors and a new persisted language/direction property model are deferred product decisions. They are not prerequisites for baseline text/keyboard conformance. No new clipboard subsystem, custom bidi layout engine, secondary normalization algorithm or framework migration is introduced. Formatting/search/link changes are limited to confirmed residuals under existing owners.

## Validation and completion

Functional delivery uses a scoped package compile/typecheck plus an existing targeted test or bounded deterministic manual fixture. Every source provides named commands or a bounded existing-selector lookup where exact test names must be reauthenticated against active code. New automatic cases, complete cross-context matrices and integration coverage belong only to the final file. All artifacts use the one current format; test code cannot introduce runtime legacy aliases or synthetic previous/current consumers.

The current documentation task checks structure, dependencies, links and diff whitespace only. It does not run competing builds or claim editing/runtime conformance. During later execution, missing fixtures, zero tests, skips, uncompiled adapters and unsupported APIs remain visible failures/limitations. Reuse exact compatible compile and current-consumer receipts; a new session is not a reason to repeat full builds. Actual browser/OS/keyboard/IME/AT observations and required virtual-platform qualification remain [roadmap43](../../roadmaps/43-physical-device-verification.md). ES-4.5 must distinguish implemented, deterministic-verified, runtime-qualified, unavailable and deliberately deferred behavior.

Completion requires all 18 required parents and their current-source focused/final checks. It does not waive existing platform, durability, size, release or publication gates. Functional sources may finish before final coverage; the whole plan may not. No paid inference, provider credentials, automatic fixture recording, production writes or publication is authorized.
