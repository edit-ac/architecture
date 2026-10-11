# Initial project setup evidence

Date: 2026-10-11. This is preparation evidence, not editor implementation or release qualification.

## Created and preserved

Public Apache-2.0 repositories: [core](https://github.com/edit-ac/core), [architecture](https://github.com/edit-ac/architecture), [cli](https://github.com/edit-ac/cli). Existing core/cli remotes and history were preserved; CLI visibility was changed from private to public following the user's explicit selection. The parent workspace is not a repository.

Core contains a Rust workspace, an explicit UTF-16 offset type, an empty WASM boundary, private `@edit-ac/core`, `@edit-ac/web`, `@edit-ac/react` workspaces, pinned toolchains/lockfiles, CI and package checks. CLI supports help/version and rejects unknown commands with exit 2. Neither scaffold implements an editor.

The npm organization lookup returned `bpstr: owner`; its package inventory was empty. These are verified publishing permissions, not existing registry packages. No placeholder package or real release was published; no trusted publisher or end-to-end publish claim is made before the package release gate.

## Planning verification

The actual Roadmap Runner 0.8.0 validator passed 11 files, 102 parent tasks and 306 standalone checkboxes, with zero errors. The manifest also passed coverage, unique IDs and acyclic upstream checks. A negative fixture with a missing dependency was correctly rejected. No roadmap worker ran and no inference/provider test was made.

Independent review added full semantic/update WASM bridge tasks, frozen-schema Rust/JS interoperability, a parser qualification gate and smaller structural probes. It moved real-device acceptance to final qualification and made crash rehearsal independent of hardware availability. The current browser release does not depend on native preparation or CLI release.

## Scaffold checks

- Core: Rust formatting, locked offline compilation and Rust test commands passed. There are zero editor tests at scaffold stage; this is compilation evidence only.
- npm: TypeScript typecheck/build passed for three workspaces, and all three compiled ESM modules imported. Empty exports are intentional and documented.
- Package dry runs: all three manifests include LICENSE, README, compiled index.js and index.d.ts, and package.json. No source-only export or missing distribution path was found.
- CLI: formatting, locked offline compilation/test commands, help/version and unsupported-command exit 2 passed. No document commands are advertised.
- Both locked npm trees returned zero known advisories in `npm audit` at setup time. This is a point-in-time advisory check, not a security guarantee.
- CI action v7 tags were resolved to actual immutable commit objects: checkout `3d3c42e5aac5ba805825da76410c181273ba90b1`; setup-node `949feb2413d6458794dcd2491c4babbbce0c15c1`.

GitHub scaffold CI passed for core commit `f3d4d35182ee4a96ec99bc5b30832cee22c9bb14` ([run](https://github.com/edit-ac/core/actions/runs/38140888302)) and CLI commit `a6baa615627d8f3c7c57624f36a93920f306c586` ([run](https://github.com/edit-ac/cli/actions/runs/38140891597)).

See [dependency verification](dependencies.md) and the dependency-probe source/lockfile for runtime metadata and compile evidence. Protocol/schema correctness, WASM loading, real IME, crash safety, parser conformance and performance remain unchecked development milestones.

## Preserved failure evidence

The first CLI format check failed and was fixed before the passing rerun. Initial npm installation selected host Node 26 instead of pinned Node 24 and failed its engine check; explicit pinned PATH succeeded. A package dry run could not write the default sandboxed npm cache; a session-local cache succeeded. An initial validation command ran in the parent workspace rather than architecture and failed ENOENT; the documented command from architecture passed. These environment/check failures were not represented as passing implementation tests.

Full small verification logs are retained under `setup-logs/`. Session-local tool/registry diagnostics were not made portable dependencies. Commands in README and task contracts use repository working directories explicitly.

## GitHub milestones

| Milestone | Roadmaps |
|---|---|
| [M1 Foundation and semantic kernel](https://github.com/edit-ac/core/milestone/1) | 01–02 |
| [M2 Durable browser editing](https://github.com/edit-ac/core/milestone/2) | 03–04 |
| [M3 Markdown and collaboration](https://github.com/edit-ac/core/milestone/3) | 05–06 |
| [M4 Modules and consumable SDK](https://github.com/edit-ac/core/milestone/4) | 07–08 |
| [M5 Browser release qualification](https://github.com/edit-ac/core/milestone/5) | 10 |
| [N1 Native preparation](https://github.com/edit-ac/core/milestone/6) | 09 |
| [C1 Offline document tools](https://github.com/edit-ac/cli/milestone/1) | 11 |

Task contracts remain authoritative in roadmap files; GitHub milestones link to them without maintaining a second 102-item checklist.
