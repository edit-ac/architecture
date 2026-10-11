# Packages, repositories and release contract

## Canonical ownership

| Repository | Contents | Distribution |
|---|---|---|
| `edit-ac/core` | Rust crates, WASM, browser SDK, React integration, fixtures and native probes | npm SDKs; Rust crates later if useful |
| `edit-ac/architecture` | Contracts, roadmaps and evidence | Documentation; private npm tooling package only |
| `edit-ac/cli` | Local-first Markdown/text editor client with optional hosted document sync | Native CLI artifacts, separately qualified |

Cargo names in the current scaffold use `editac-*` (Rust imports `editac_*`). npm names use `@edit-ac/*`. Preserve these established names. The draft's `@editac` imports are superseded.

Initial npm packages are `@edit-ac/core`, `@edit-ac/web`, `@edit-ac/react`. The core package owns one WASM engine, the web package owns imperative DOM plus storage/sync/module subpaths, and React owns lifecycle bindings. Additional packages require a real independently consumed boundary. Markdown is a portable Rust crate initially compiled into the task preset engine; moving parser preparation into an isolated worker cannot create another authoritative writable document.

## Current scaffold and future release

Scaffold packages deliberately export no editor API and have `private:true`; Rust crates have `publish=false`. They can be built, typechecked and packed locally but are not registry releases. Do not reserve names by publishing empty editor packages. The organization already owns its scope. Release work makes the flags public only after documented functionality and tarball-consumer validation exist.

Use exact direct tooling pins and lockfiles. Current compiler/tooling provenance and candidate runtime pins live in [dependency verification](../evidence/dependencies.md). Evaluate transitive licenses and advisories at installation/release; current metadata alone is not a compatibility or security proof. Prefer package-manager lockfile checks and immutable action commit references; retain Apache license and third-party notices in distributed artifacts.

## Artifact requirements

Build ESM and declarations into real exported paths. Package only dist, required WASM assets, README/license/notices. Test `npm pack` outputs by installing them into isolated plain browser and React/SSR examples without workspace symlinks. Verify asynchronous init, explicit asset URL, CSP/CDN loading, SSR import without DOM access, types, one runtime state owner and cleanup.

Keep WASM code generation separate from hand-maintained package metadata. Pin wasm-bindgen crate/CLI together and verify wasm-pack output target; do not assume bundler and browser-native outputs are interchangeable. Wasm binary/API changes participate in package versioning and compatibility tests.

## Publishing

Use public scoped packages, a `next` tag for the first qualified prerelease, a reviewed immutable revision, clean artifacts and declared version. Publish in dependency order core → web → react. Test exact registry versions in isolated consumer fixtures and record tarball integrity/provenance. Promotion to latest is a later release decision.

Prefer npm trusted publishing from GitHub-hosted Actions with `contents:read`, `id-token:write`, exact repository/workflow and protected environment. Configure only the intended publish permissions. Initial package bootstrap may require an authenticated owner/2FA before a package-level trusted publisher can be registered; verify npm's current flow when executing the release task. Never copy a browser session credential into the repository or add long-lived publish credentials to CI as a convenience.

Current setup verifies organization ownership but publishes no package. Do not report npm readiness as an existing registry version or an end-to-end OIDC test. The release roadmap owns those actions and checks; ordinary roadmap execution cannot bypass the artifact gate.

## CLI

The CLI is a local-first editor client consuming a reviewed immutable engine revision or released crate. A distributed manifest cannot depend on `../core` or an uncommitted worktree. The [CLI contract](cli.md) defines local Markdown/literal-text editing, hosted document targets, source reconciliation, recovery and durability states. Use the shared Markdown parser and semantic commands; Markdown is the editing representation, while hosted CRDT identity/history remains intact. Local editing requires no account/network; hosted transport is optional and uses the qualified sync contract. Preserve format version and error/diagnostic semantics. Save the opened target atomically with stale-file checks; overwriting a different export destination requires an explicit option. CLI release is independent of browser release and native platform SDK support.

Sources: [Cargo workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html), [npm trusted publishers](https://docs.npmjs.com/trusted-publishers/), [npm package files](https://docs.npmjs.com/cli/v11/configuring-npm/package-json/).

## Full-client packaging

Follow-ups keep the existing three repositories. Shared session/diff/optional security crates and native SDK artifacts live in core; CLI/TUI distributions remain in cli. Portable module entrypoints and host-app MCP helpers are optional surfaces qualified before publication. Roadmap 20 qualifies the full base client matrix; roadmap 24 qualifies encrypted profiles separately. No new monolithic cloud product or mandatory standalone MCP daemon is introduced.
