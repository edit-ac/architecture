# Architecture and development planning

Read README.md for scope and roadmap entry gates. Read only the active task's named specs and implementation paths; planned paths are created by their task.

Roadmap sources are controller-owned. Workers record checkmarks, commands, nonzero executed/passed/failed/skipped counts, and interrupted-work handoff in the separate progress file. Each iteration implements at most one parent task with its implementation and validation steps. A failed or skipped prerequisite does not unlock dependents.

Before changing a shared semantic, storage, wire, or ABI contract, update its authoritative spec and the affected task acceptance together. Keep native platform policy out of the Rust engine. Use Codanna first for code discovery; use rg for documents/configuration or incomplete index results.

All automated validation uses deterministic fixtures and mocked network/provider transports. No paid inference, credential loading from .secrets, or automatic fixture recording. Live-content AI dogfood requires separate user-approved exact scope, monetary/request cap and stop condition; read the Assign workspace architecture/operations/paid-inference-testing-policy.md before AI test/dogfood work. No such work is part of these roadmaps.

Commit subjects are plain-English imperatives. Preserve source, data and qualification evidence during process/disk cleanup. Stop only verified task-owned test browsers and temporary servers; record any preview intentionally left running.
