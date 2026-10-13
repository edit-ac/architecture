# AI extension roadmap review

Reviewed: 2026-10-12. This is planning research, not implementation or provider-quality evidence. Context7 tools were unavailable in this session; official Tiptap and Vercel AI SDK documentation was read directly.

## Existing coverage and missing scope

Before the AI additions, existing assistance (39), host-app MCP edits (14), exact proposal/diff application (13), native writing-tool/input hooks, first-party configurations (21), rich content (25) and mobile presenters (41) supplied foundations but did not explicitly own the requested AI writing profile. The 14 AI parents are now consolidated into the existing rich-content roadmap 25 as RCH-2.1–RCH-2.14, reusing those semantic, history, diff, speech and platform-input boundaries.

## Primary references

- [Tiptap Basic AI Generation overview](https://tiptap.dev/docs/ai/basic/overview): optional AI commands, custom prompts/transports, streaming and completion. This informs the feature grouping, not edit.ac's provider or package choice.
- [Built-in commands](https://tiptap.dev/docs/ai/basic/text-generation/built-in-commands): selected-text transformations, completion, summarization, translation and custom prompts inform the initial action profile.
- [Autocompletion](https://tiptap.dev/docs/ai/basic/text-generation/autocompletion): reference for the dedicated completion surface, separate from explicit generation actions.
- [Manage responses](https://tiptap.dev/docs/ai/basic/text-generation/manage-responses): reference for response review, acceptance, rejection and regeneration.

edit.ac retains its own Rust/CRDT, input and review contracts. Tiptap feature precedent is not evidence that edit.ac supports its plugins/schema or that a particular model performs accurately.

## Vercel AI SDK evaluation and default decision

Decision, 2026-10-12: recommend Vercel AI SDK Core as the default **TypeScript host/backend adapter** for autocomplete, Ask AI and fill/continue text. Keep the public editor transport portable and the feature optional. This is an architectural recommendation based on documented capabilities and the current contracts, not a runtime benchmark or model-quality assessment. RCH-2.1/2.6/2.14 now specify the default adapter and reference recipe rather than leaving SDK adoption as an unresolved candidate.

The SDK supplies generation and streaming APIs through provider adapters, so all three features can share one bounded request/error/cancellation implementation. This removes repeated provider-specific transport work while preserving host model choice. [AI SDK introduction](https://ai-sdk.dev/docs/introduction), [generating text](https://ai-sdk.dev/docs/ai-sdk-core/generating-text).

| Feature | Recommended initial SDK use | Work that edit.ac must still own | Fit |
|---|---|---|---|
| Autocomplete | Short bounded `generateText` response through the host; one current request and one complete suggestion | Debounce, bounded context, IME protection, caret/anchor validity, ghost text, acceptance keymap, request caps and stale-result rejection | Good transport fit; latency-sensitive editor behavior still needs custom integration |
| Ask AI | `streamText` into an answer panel; one request with explicit instruction/context | Permission checks, captured selection, bounded session, stop/error handling; answers do not change the document automatically | Strong fit for incremental answers |
| Fill/continue text | `streamText` into a provisional insertion/replacement proposal | Safe content parsing, preserved structure/atoms, preview, captured targets, explicit acceptance and one semantic undo group | Strong fit for generation; proposal application remains shared edit.ac work |

These API choices are our initial design judgment, using the documented [generation/streaming primitives](https://ai-sdk.dev/docs/ai-sdk-core/generating-text). Start autocomplete without incremental ghost-text chunks; consider them only when measured user benefit justifies the extra state handling. Prepared transport measurements cannot establish real provider/model latency.

The React `useCompletion` helper manages completion request/UI state; it does not establish rich-editor caret, CRDT, IME or ghost-text correctness. Keep it optional and keep SDK UI state separate from the editable document and proposal session. [Completion documentation](https://ai-sdk.dev/docs/ai-sdk-ui/completion).

Cancellation requires the host runtime to propagate the client disconnect and forward its abort signal to the SDK. Stopping the visible stream alone may leave server generation running. Qualify the deployed runtime's actual propagation; do not equate cancellation with refunded usage. [Stopping streams](https://ai-sdk.dev/docs/advanced/stopping-streams).

Disable automatic retries explicitly (`maxRetries: 0`, plus any stream/provider retry setting in the pinned version). Admit each request against host limits before dispatch, including regenerate/manual retry. Pin a released stable SDK/provider-adapter pair and map its error, finish/abort and available usage metadata into our bounded envelope. No tools, agent loops, implicit gateway, provider fallback or workspace retrieval is needed for the initial profile. [streamText reference](https://ai-sdk.dev/docs/reference/ai-sdk-core/stream-text).

A TypeScript backend can run independently of the editor and native clients. The official Node.js quickstart supports explicit provider choice; Vercel hosting/AI Gateway is not a prerequisite for the portable adapter. The upstream SDK source is Apache-2.0; record licenses and runtime requirements for the exact selected dependency set during implementation. Native/terminal clients consume the host protocol without embedding JavaScript. [Node.js quickstart](https://ai-sdk.dev/docs/getting-started/nodejs), [upstream license](https://raw.githubusercontent.com/vercel/ai/main/LICENSE).

The tradeoff is an additional backend dependency and responsibility for SDK/provider version compatibility and stream-protocol mapping. A direct provider SDK can be adequate for a host committed to one provider; a Rust/Go/native-only backend can implement the same transport instead. For our default TypeScript integration, shared adapters and mocks justify AI SDK Core. This choice does not promise lower model cost or faster/better completion. All qualification here uses prepared mock models and simulated streams, with exact abort/retry-count assertions; no live inference is authorized. [SDK testing](https://ai-sdk.dev/docs/ai-sdk-core/testing).

## Roadmap consolidation

Roadmap 43 is removed from the source and manifest. All 14 parents move to the AI epic in [roadmap 25](../roadmaps/25-rich-content-extensions.md#epic-rch-2--deliver-optional-ai-writing-through-existing-edit-contracts): former `AIX-1.n` maps to `RCH-2.n` for n=1–14, including implementation/validation IDs and local dependencies. No AI progress entries existed to migrate. The pre-move source snapshot is retained at `/tmp/editac-ai-roadmap-fold-before/roadmaps/43-ai-extensions.md`; immutable historical controller/qualification records remain unchanged.

Existing rich-content tasks retain their gates. Former AI upstream requirements become AI-epic entry conditions, preserving independent native/TUI/docs gates. RCH-2.6 also waits for RCH-1.20 before claiming actual rich-feature consumer combinations. Roadmap 25 now has 36 parents; total task scope is preserved. Whole-track consumers of 25 require the enlarged track, including AI platform qualification; baseline browser release still has no 25 prerequisite.

## Additional first-party candidates

These are recommendations for subsequent prioritization, not new committed tasks or release gates. Value and ordering are product judgments.

| Priority | Candidate | User value and bounded first slice | Existing foundation |
|---|---|---|---|
| Next | Brand terminology and glossary checks | Flag inconsistent names or forbidden terms with an explanation and reviewed replacement; start with deterministic rules, AI explanation optional | AI selected-text actions and versioned official profiles |
| Next | Notes to structured content | Turn a selected passage into an outline, checklist or action items; preview supported blocks and keep ownership/dates explicitly unset unless present in the source | Existing list/table commands and AI proposals |
| Next | Explain selection with source references | Answer questions about selected text and identify the exact supplied passages; show missing evidence rather than invented citations | Ask AI and permission-scoped context |
| Next | Reusable templates and snippets | Insert approved meeting, specification or issue templates through slash/command search; AI-assisted fill is optional and reviewed | Existing command palette, descriptors and fill text |
| Later | Anchored editorial comments | Persist human review notes against stable anchors, with resolve/reopen and clear stale-anchor behavior; requires a separately reviewed storage/access contract | Existing anchors and change-review UI; comments are not already promised by AI preview |
| Later | Outline and reading tools | Accessible heading navigation, word/reading-time counts and section summaries; keep local deterministic tools independent of AI | Existing headings, navigation and optional presenters |

Spelling/grammar, rewrite, summarize and translation are included in the new initial profile. Code highlighting, tables, images/embeds, public/internal links, document conversion, find/replace and official presets are already planned in existing tracks; they need no duplicate AI roadmap tasks. Image generation, autonomous document agents and automatic multi-document retrieval are deferred because they add transport, asset or authorization scope beyond this writing request.

## Planning validation

Before consolidation, `npm run check` passed with 43 roadmap files, 542 parents, 1,629 checkboxes and 181 context links. These are planning-source counts, not implementation results. Final consolidated validation is recorded below after the move. No AI implementation, live provider call, browser/device qualification or model-quality test is performed by this change.

After consolidation, `npm run check` passes with 42 files, 542 parents, 1,629 checkboxes and 181 context links, with zero errors. Editing-suite planning counts remain 272 cases, 14 recipes, 45 steps and 14 guards; all 14 validator contract tests pass, with zero failures/skips. Structural preservation checks confirm the original RCH-1 source and all 42 migrated AI parent/implementation/validation checkbox IDs are retained. Full logs: `/tmp/editac-ai-fold-before.log` and `/tmp/editac-ai-fold-after.log`.
