# Extension DX and optional-loading acceptance cases

Device sequencing (superseding user decision, 2026-10-18): every device/target-runtime/OS-input/AT observation in this document is owned by [final roadmap43](../roadmaps/43-physical-device-verification.md) under the [web feature-first policy](../operations/web-feature-first-20261018.md). Feature implementation keeps focused deterministic correctness/data-safety checks; device rows and D observations run later on accepted simulators/emulators/VMs/OS hosts without waiting for physical hardware. Preserve original case IDs and criteria; deferred observations remain unchecked and do not block web feature completeness. Exhaustive qualification/performance follows the stated later phase.

Status: planned acceptance catalog for [the extension DX contract](../specs/extension-dx.md). These cases are not executed support claims. The existing SDK, extension-library and architecture-fitness follow-ups create the named executable groups; reuse the existing engine, packed consumers, browser input, byte inventory and shared-resource harnesses.

| Case | Independent expected outcome | Owner |
|---|---|---|
| DXC-01 | One public facade import plus extensions configuration enables a qualified feature without manual codec/worker/registry assembly. | EXT-1.14, SDK-1.11 |
| DXC-02 | Configuring one factory twice yields isolated options; absent preset and arbitrary host use cases do not restrict extension choice. | SDK-1.11 |
| DXC-03 | Invalid options, duplicate identities, dependencies and equal-priority conflicts fail before attachment with actionable diagnostics; legacy options have deterministic migration/conflict behavior. | EXT-1.14, SDK-1.11 |
| DXC-04 | Disabled-only packed builds and browser requests contain no disabled implementation, font, dictionary, converter or worker assets; an eager-loading negative fixture fails. | SDK-1.12 |
| DXC-05 | Enabling math, Markdown or a qualified converter loads its dedicated implementation and shared prerequisites, excludes unrelated formats, and exposes ready/loading/failure/retry states. | SDK-1.12 |
| DXC-06 | SSR import does no I/O; bundler defaults and one direct-browser asset override work, with correct MIME/CSP/CORS failure diagnostics and retained source. | SDK-1.11, SDK-1.12 |
| DXC-07 | Concurrent instances share compatible code loads but not mutable options, authority, requests or document state; dispose/late-load failure leaves the other instance operational. | SDK-1.12, FIT-1.11 |
| DXC-08 | A third-party behavior extension and data-defined mark/atom compile from public imports against unchanged WASM and retain unknown-data fallbacks. | EXT-1.15 |
| DXC-09 | Matching examines only bounded changed text/context; composition, code, existing links, remote updates and literal bypass obey declared exclusions. | EXT-1.16 |
| DXC-10 | Typing ASD-123 leaves text unchanged while pending; a found fixture task creates exactly one safe link over the same text and preserves adjacent marks/selection. | EXT-1.17 |
| DXC-11 | Not-found, denial, failure, timeout and unsafe URL produce no link and no document/history effects; no templated fallback URL is fabricated. | EXT-1.17 |
| DXC-12 | Editing/deleting the match, undo-invalidating its intent, read-only, reconfiguration and disposal reject stale completions; unrelated edits preserve the anchored target when still valid. | EXT-1.16, EXT-1.17 |
| DXC-13 | Repeated matches, changed queries and out-of-order results respect bounded concurrency, deduplication, principal-scoped cache limits and cancellation without cross-editor application. | EXT-1.16, EXT-1.17 |
| DXC-14 | Successful link application converges through existing peer updates; undo/redo is explicit and undo does not immediately retrigger linking. Reopen/export causes no lookup. | EXT-1.17 |
| DXC-15 | Platform spellcheck is the default and respects user settings; off/custom modes and independent autocorrection expose unsupported/coupled controls. Platform/off load no SDK checker assets. Explicit custom checking avoids duplicate presentation, bounds changed ranges and excludes composition without CRDT effects. See ENV-01–06. | SDK-1.11, EXT-1.18 |
| DXC-16 | Accepting a current platform/custom suggestion produces one prepared replacement; stale suggestions do nothing, and formatting/selection/shared undo/disable/disposal remain correct. ENV-04/07 distinguish prepared mechanics from actual browser/native observations. | EXT-1.18, INT-1.7, INT-1.12 |
| DXC-17 | Custom parsing prepares one admitted fragment; literal/unsupported/invalid/stale input retains recoverable source and creates no partial edit. | EXT-1.19 |
| DXC-18 | URL insertion uses only a validated found result and a current stable target; invalid URLs, denied resolution and absent custom-reference presenters preserve explicit fallbacks. | EXT-1.19 |
| DXC-19 | Baseline/per-feature/combined inventories include raw, gzip and Brotli sizes, required lazy code, glue and assets; duplicates/eager loads and missing artifacts fail the existing admission harness. | FIT-1.10 |
| DXC-20 | Local server tests prove gzip/Brotli negotiation, MIME, Vary, versioned URLs, uncompressed fallback and cache provenance with decoded bytes identical to the inventoried artifacts. | FIT-1.10 |
| DXC-21 | A measured reduction preserves feature-equivalent editing, Unicode/graphemes, persistence, history, peer convergence and unknown-data recovery; startup/compile regressions remain visible. | SDK-1.13 |
| DXC-22 | Public beginner snippets compile/run from a clean installed tarball with no private imports, workspace aliases or copied initialization plumbing; source/version drift is rejected. | EXT-1.20, FIT-1.11 |
| DXC-23 | Plain, React and Astro integrations use the same extension configuration/lifecycle; keymaps, focus, options and optional loading remain isolated across remount/routes. | FIT-1.11 |
| DXC-24 | Required-ready and command-lazy behavior are distinct; parser load failures retain input, exporters do not block ordinary typing, and cancellation/disposal release owned resources. | SDK-1.11, SDK-1.12, FIT-1.11 |
| DXC-25 | Basic formatting options independently enable/disable commands, shortcuts and controls without per-command behavior-extension plumbing; disabling UI preserves existing admitted marks, undo and unknown data. Invalid combinations fail before attachment. | EXT-1.14, SDK-1.11 |
| DXC-26 | A local editor works with no collaboration provider, connection, authorization lookup or remote-ready wait; disabled sync/presence adds no subscriptions, timers, sockets or provider assets. Byte graphs count shared Yrs/local-storage primitives separately and an eager-provider negative control fails. | SDK-1.12, FIT-1.10 |
| DXC-27 | A comment field, local formatted editor and collaborative document coexist with isolated content, configuration, authority, selection and history. Sync and presence are independently selected; shared code never activates a sibling or sends its edits. | SDK-1.11, FIT-1.11 |
| DXC-28 | Sync attach/detach/reconfigure/dispose and delayed/out-of-order provider completions preserve the same local document/history and recoverable unsent edits. Invalid identity/schema/authority is rejected, late callbacks are inert, and ordinary input continues during remote bursts. | SDK-1.11, SDK-1.12, FIT-1.11 |
| DXC-29 | Empty/disabled/1/10/100 unrelated descriptors produce no disabled/uninterested callbacks and no whole-registry/document input scans. Operation/source/range/selection filters remain correct for text, format and structural patches; disposal removes interests. Work-count negative controls fail. | EXT-1.15, FIT-1.10, FIT-1.11 |
| DXC-30 | Direct-port vs facade runs with identical features attribute dispatch, host callbacks, JS/WASM calls, copies and allocations. Short-field typing, formatting/selection, IME commit, Task/Long, paste and mixed-extension workloads meet their predeclared limits or retain explicit failed/inconclusive results. | SDK-1.13, FIT-1.11 |
| DXC-31 | Equivalent pure JS/WASM candidates cover tiny/medium/large inputs, single/batched calls and cold/warm conditions with correctness parity. Encoding/copying/glue/compile/memory costs, raw distributions and crossover or rejected hypotheses are visible; no second authoritative model is introduced. | SDK-1.13 |
| DXC-32 | Packed consumers enforce the predeclared latency/work budgets, cold first-edit and warm activation costs, remote-burst behavior and repeated-disposal memory. Unrelated wrapper state does not repaint the document or every extension; per-character boundary-call and whole-document-export controls are rejected. | FIT-1.11 |

Use prepared task catalogs, local dictionaries, in-memory resolvers and explicit delayed/error transports. Do not contact production task systems, hosted spellcheck or model providers. Negative fixtures must detect stale application, eager imports and drift rather than merely exercise the happy path. Byte measurements and runtime correctness are separately recorded. Execution counts, failures/skips, immutable inputs, applicable browser runtimes and teardown are mandatory; native support stays with its owning qualification tasks.

## Local structural-callout return (LCR-1.2)

The Project kickoff consumer must construct a real v1 callout via the production
codec/engine, edit its body via one same-owner atomic command, and independently
check invalid registration/nonmutation, exact descriptor/fallback undo and redo,
serialization/local reopen, Markdown roundtrip and explicit highlight loss recovery,
absent/future extension preservation, remote text with semantic undo, cancelled/stale
preparation and complete presenter/menu teardown. Configured authoring and advanced
presenter remount use the same stored document sequentially; their unsupported
mixed configuration must still reject. Native/device and full EQL stay pending.
