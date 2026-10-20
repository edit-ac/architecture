# Architecture and development planning

Read README.md for scope and roadmap entry gates. Read only the active task's named specs and implementation paths; planned paths are created by their task.

Roadmap sources are controller-owned. Workers record checkmarks, commands, nonzero executed/passed/failed/skipped counts, and interrupted-work handoff in the separate progress file. Each iteration implements at most one parent task with its implementation and validation steps. A failed or skipped prerequisite does not unlock dependents.

Before changing a shared semantic, storage, wire, or ABI contract, update its authoritative spec and the affected task acceptance together. Keep native platform policy out of the Rust engine. Use Codanna first for code discovery; use rg for documents/configuration or incomplete index results.

All automated validation uses deterministic fixtures and mocked network/provider transports. No paid inference, credential loading from .secrets, or automatic fixture recording. Live-content AI dogfood requires separate user-approved exact scope, monetary/request cap and stop condition; read the Assign workspace architecture/operations/paid-inference-testing-policy.md before AI test/dogfood work. No such work is part of these roadmaps.

Commit subjects are plain-English imperatives. Preserve source, data and qualification evidence during process/disk cleanup. Stop only verified task-owned test browsers and temporary servers; record any preview intentionally left running.

## Source-only Git policy — user decision, 2026-10-20

Keep source code, authored documentation, configuration and deterministic input fixtures in Git. Never commit generated caches, qualification evidence, screenshots, recordings, test reports, benchmark results, compiled binaries, packed dependencies, runtime/source snapshots or test databases. Exclude these outputs with .gitignore.

Run focused checks using ignored, task-owned temporary directories. Keep only the diagnostics needed for an active failure, then remove them after debugging; do not create gigabytes of evidence or routine artifact archives during development. Report concise pass/fail counts in the conversation or commit description. Release artifacts belong outside source repositories. This supersedes older blanket evidence-retention wording for generated development/test output; preserve source, real user data, credentials and active processes.
