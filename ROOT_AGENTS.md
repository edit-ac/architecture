# Workspace root agent instructions

This is the version-controlled copy of the user's root agent rules. From the parent directory containing `architecture`, `core`, `cli` and `docs`, copy this file to `AGENTS.md`:

```sh
cp architecture/ROOT_AGENTS.md AGENTS.md
cmp architecture/ROOT_AGENTS.md AGENTS.md
```

Install it at the workspace root, alongside the repository directories. Keep repository-specific `AGENTS.md` files in place. Edit this canonical copy and sync the root copy after shared-rule changes; preserve existing local additions before replacing a root file. See [workspace setup](architecture/WORKSPACE_SETUP.md) when installed at the root, or `WORKSPACE_SETUP.md` alongside this canonical file.

The rules below are copied from the root instructions without changes.

## Code discovery

Use Codanna MCP before text search when discovering code:

1. `find_symbol` or `search_symbols` to locate definitions.
2. `find_symbol` with the returned `symbol_id` to disambiguate and read a definition.
3. `find_callers`, `get_calls`, or `analyze_impact` to trace behavior and dependencies.
4. `semantic_search_with_context` for broad code queries with relationship context.
5. `semantic_search_docs` for broader meaning-based code search.

Use `get_index_info` when repository coverage is uncertain. The Codanna server watches indexed files; run `codanna index .` from the current workspace when the index is missing or stale. Fall back to `rg` for literals, error messages, configuration, non-code files, or incomplete Codanna results.

## Tool selection

- Prefer a purpose-built MCP tool or CLI for supported operations before using browser automation.
- When browser interaction is needed, prefer the Codex in-app browser over the Chrome extension whenever it can access the page and perform the task. Use Chrome when the user explicitly requests it or the in-app browser lacks the needed session or capability.

## Tool output and context

- Discover tool names first; read the schema of only the tool needed for the next action. Return selected names/fields rather than dumping `ALL_TOOLS`, full tool catalogs or complete response envelopes. Reuse schemas already read in the session.
- Read required instructions fully. For other code and documents, locate the relevant symbol, heading or matches first, then read the smallest range that answers the current question. Expand only for a concrete missing dependency.
- Start shell results at `max_output_tokens: 2000` (up to 3000 for a coherent code excerpt). Bound the total returned from a batched `functions.exec` to 3000 tokens with its execution pragma; several nested limits do not bound their combined output. Return command `.output` or selected MCP text/fields, with necessary error/status information.
- Keep large logs, search inventories and diffs in local artifacts; return a short result, path and relevant excerpt. When output is truncated, narrow or paginate the next read before drawing a conclusion. Preserve required failures, skipped counts and evidence; a truncated result is incomplete evidence.
- Before running a command likely to print substantial output (builds, tests, recursive searches, logs, large files, JSON, or diffs), save the full output to a local artifact and return only its exit status, size, failure/skip counts, and the smallest relevant excerpt. Keep the original available for targeted follow-up reads.
- Bound both individual command output and the combined outer tool response. Never forward full logs, base64 media, large JSON objects, or repeated console output into the model context; extract selected fields or line ranges. If a tool emits a large response unexpectedly, summarize its metadata and inspect the saved source in small slices.
- Before another call, identify what remains unknown. Reuse prior results while their source is unchanged. Resolve simple lookup requests with direct evidence; expand into audits or benchmarks only when the requested scope calls for them.

## Token discipline

- Minimize model round trips: batch independent reads, reuse unchanged evidence, and verify only what the requested scope requires. After required checks pass, finish unless new evidence warrants more work.
- For waiting, use event-driven or bounded waits with backoff; recheck unchanged state only when a meaningful change is expected.
- Use subagents only when the user or applicable instructions request delegation; give each a narrow scope and only the context it needs.
- When a long task changes phase, keep a compact checkpoint of decisions, completed checks, and remaining work instead of repeatedly reconstructing its history. Preserve required evidence and completion criteria.

## Deep Review invocation

Use `deep-review` or `deep-code-review:deep-review` only when the user specifically requests the Deep Review skill. Never invoke either skill automatically for PR reviews, code reviews, audits, or implementation verification. A general request to review code or a PR does not authorize Deep Review. This rule overrides automatic trigger guidance in either skill's description or instructions.

## Git commit messages

- Write plain-English, imperative commit subjects without type or scope prefixes.
- Do not use Conventional Commit prefixes such as `feat:`, `fix:`, `docs:`, or `feat(scope):`.
- Prefer subjects such as `Add project filtering` or `Fix mobile navigation`.

## Humanizer scope

Use Humanizer skills only for public-facing documentation, articles, and other writing intended for publication. Write internal documents, architecture records, reports, plans, task notes, evidence, and agent instructions without Humanizer.

## Browser and web-server process hygiene

After browser tests or dev-server work, before finishing a task, and when the user reports a slow Mac, check for leftover automated browsers and temporary web servers.

1. Reuse a suitable existing server. Track the PID, launcher, workspace, port, purpose, and log path of processes you start. Close test browsers and stop temporary servers in teardown, including failure and interruption paths. Keep a preview running only when the user requested it or another active task needs it; report its port and purpose.
2. Identify cleanup candidates from process trees, working directories, listening ports, controller connections, logs, and task status. Age, low CPU, or parent PID 1 alone does not prove a process is stale. A duplicate fixture server may still support active browser checks. Check relevant Codex chats before stopping shared resources.
3. Stop confirmed abandoned headless Chrome/Playwright/Lighthouse instances and unused Astro/Vite/preview servers without another approval request. Preserve ordinary Chrome tabs, active tests, and previews used by another task. For Assign, preserve the main supervised dev server and its API, Knowledge service, and database; discover their current PIDs and ports each time. Ask only when ownership or continued use remains unclear.
4. Revalidate each PID's command and ownership immediately before signaling it. Use graceful browser shutdown or SIGTERM, stop an unused server's launcher as well as its captured descendants, then verify exit. Use SIGKILL only for a confirmed stale process that ignores graceful shutdown. Target exact processes; broad process-name kills and unverified process-group kills can interrupt unrelated work. Preserve browser profiles, source, data, and qualification evidence.
5. Confirm removed listeners stay gone and protected services remain available. Report what stopped and what remains. When diagnosing slowness, distinguish CPU load from memory pressure and active swap I/O; a small cleanup does not establish that the Mac has recovered.

## Post-session disk hygiene

After a substantial coding session—especially one involving builds, tests, profiling, simulators or emulators, containers, or package installation—check free space on the data volume before finishing. Treat several GiB of new artifacts or less than 50 GiB free as a cleanup trigger.

1. Inspect the sizes of build, cache, temporary, container, and simulator directories touched by the session, and verify that no relevant process is still using them.
2. Remove only inactive, reproducible artifacts created by the current session, such as project build outputs, session-created container build cache, package-manager cache entries, and stale temporary workspaces.
3. Preserve source files, uncommitted work, databases, Git history, credentials, active process output, and release or qualification evidence. Do not prune unrelated projects or run broad recursive deletions without explicit user approval.
4. Recheck disk usage and report the exact paths removed, space reclaimed, and remaining free space. If space is still low, list the largest cleanup candidates and ask before expanding the scope.

## Paid inference prohibition — user decision, 2026-09-06

Use prepared responses, deterministic fixtures and mocked provider transports for all automated tests, CI, synthetic scenarios, smoke/readiness probes, benchmarks, model grading, calibration and retry experiments. Paid token/API testing is forbidden, including opt-in flags, ambient credentials, local subscription proxies and automatic fixture recording. Never load `.secrets` into test runners or use a cheaper model/project/key as a workaround.

The user's AI credits are reserved for explicitly requested, meaningful live-content dogfood, not synthetic test generation or validation. Dogfood is a separate manual workflow with the exact real-content scope, a user-approved hard monetary/request cap and a stop condition before any call; broad implementation/deployment authorization or restored credit balance does not authorize spending. No paid dogfood is authorized by this incident remediation. Preserve historical failed evidence; prepared results must never be represented as provider quality, real usage, settlement or launch qualification.

Before changing or running AI tests or dogfood, read `architecture/operations/paid-inference-testing-policy.md` in the Assign workspace.

## Parallel roadmap delivery checkpoints

For the explicitly authorized concurrent 08–09 and shared-client runners, read `../.roadmap-coordination/parallel-clients.md` from a repository (or `.roadmap-coordination/parallel-clients.md` from the workspace root) before every parent. Respect lane ownership and the integration lock. Commit validated owned work and reconcile with main after every two completed parents and at roadmap boundaries. The primary lane processes integration requests only at a safe checkpoint; the parallel lane must not modify a checkout with an active worker. Record merged commits, progress locations and deferred conflicts in the shared ledger so later tasks reuse completed work. Keep paid synthetic inference and publication prohibited.

## Hourly runner health and drift repair

The user-authorized hourly monitor actively resolves roadmap blockers and integrates validated completed work into local main. Use the shared coordination plan and lock, compare exact dirty paths, prepare/test merges in an isolated worktree if needed, and pause affected workers only for a safe landing checkpoint. Preserve unrelated nonoverlapping work byte-for-byte and never blindly stash/reset or stage another task's unvalidated changes. Record tested merged commits and restart IDs, synchronize the parallel branch with main, and stop unchanged blocked retry loops.
