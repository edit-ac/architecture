# Packages, repositories and release contract

## Canonical ownership

| Repository | Contents | Distribution |
|---|---|---|
| `edit-ac/core` | Rust crates, WASM, framework-independent browser SDK, first-party React/Astro integrations, fixtures and native probes | npm SDKs; Rust crates later if useful |
| `edit-ac/architecture` | Contracts, roadmaps and evidence | Documentation; private npm tooling package only |
| `edit-ac/docs` | Public guides, generated references and release-backed demo consumers | Static documentation/demo site; no editor implementation |
| `edit-ac/cli` | Local-first Markdown/text editor client with optional hosted document sync | Native CLI artifacts, separately qualified |

Cargo names in the current scaffold use `editac-*` (Rust imports `editac_*`). npm names use `@edit-ac/*`. Preserve these established names. The draft's `@editac` imports are superseded.

Initial npm packages are `@edit-ac/core`, `@edit-ac/web`, `@edit-ac/react`. The core package owns one WASM engine, the web package owns imperative DOM plus storage/sync/module subpaths, and React owns lifecycle bindings. Additional packages require a real independently consumed boundary. The user-approved 2026-10-13 packaging change makes Markdown an optional first-party extension, exposed through a separately consumed `@edit-ac/markdown` boundary and an independently loadable Rust/WASM parser artifact. The default Task engine and browser entry do not import, instantiate or request Markdown code. The extension prepares interchange data and semantic commands for the existing engine; it never creates another authoritative writable document. The portable `editac-markdown` crate remains available to CLI and native consumers that explicitly include it. This supersedes the original decision to compile Markdown into every Task preset engine.

The 2026-10-13 integration scope adds planned `@edit-ac/astro` alongside React. Framework bindings are optional first-party packages over the same core/web contracts; framework runtimes stay out of the shared SDK. Astro supplies a .astro host and browser lifecycle bridge, requires no React runtime, preserves safe static/SSR rendering and disposes editors on ClientRouter navigation. SDK-1.7 owns implementation, SDK-1.4 packed consumers and SDK-1.6 executable integration guidance. This supersedes Decision 001's React-only initial integration scope. Future frameworks can reuse this package boundary when separately scoped, with verified peer versions, lifecycle tests, packed consumers and useful getting-started examples.

Astro 7's [Rust compiler rewrite](https://astro.build/blog/astro-7/) supports the shared Rust-first positioning. Its compiler is a build-time concern; edit.ac's Rust/WASM engine remains the editor runtime. This rationale does not substitute for Astro compatibility or editor performance qualification.

## Current scaffold and future release

Scaffold packages deliberately export no editor API and have `private:true`; Rust crates have `publish=false`. They can be built, typechecked and packed locally but are not registry releases. Do not reserve names by publishing empty editor packages. The organization already owns its scope. Release work makes the flags public only after documented functionality and tarball-consumer validation exist.

Use exact direct tooling pins and lockfiles. Current compiler/tooling provenance and candidate runtime pins live in [dependency verification](../evidence/dependencies.md). Evaluate transitive licenses and advisories at installation/release; current metadata alone is not a compatibility or security proof. Prefer package-manager lockfile checks and immutable action commit references; retain Apache license and third-party notices in distributed artifacts.

## Optional Markdown delivery

The default Task preset supports rich-text editing, durable local storage, direct collaboration, supported clipboard formats and safe links without the Markdown parser. Markdown import/export, Markdown paste and Markdown typing shortcuts require explicit extension registration. Disabled capabilities expose an accurate availability result and a documented recoverable diagnostic; they never silently claim a successful Markdown operation. Ordinary text paste remains literal when the extension is absent.

The Markdown extension retains the qualified grammar, prepared-operation/anchor/history boundaries, diagnostics, recovery data and optional-content preservation in formats.md. Explicit configuration opts plain, React and Astro consumers into Markdown without making their base imports pull it in. Qualification proves default import/request absence and isolated installed-tarball operation with the extension enabled; record its JS/WASM/CSS transfer cost and end-to-end combined totals separately. An enabled extension may load before its first operation or through an explicit async action with cancellation and anchor validation; it must not introduce a blocking fetch in the typing path or silently load on an ordinary default mount. No publication is authorized by this packaging change.

## Artifact requirements

Build ESM and declarations into real exported paths; the Astro package additionally exports its distributable .astro host and client assets. Package only required distribution files, README/license/notices. Test `npm pack` outputs by installing them into isolated plain browser, React/SSR and Astro 7 static/SSR examples without workspace symlinks. Verify asynchronous init, explicit asset URL, CSP/CDN loading, SSR import/render without DOM access or WASM initialization, types, one runtime state owner and cleanup. Verify Astro navigation away/back, multiple hosts and absence of a React dependency.

Keep WASM code generation separate from hand-maintained package metadata. Pin wasm-bindgen crate/CLI together and verify wasm-pack output target; do not assume bundler and browser-native outputs are interchangeable. Wasm binary/API changes participate in package versioning and compatibility tests.

The private foundation probe is an explicit qualification entry: `@edit-ac/core/fixture`
loads `@edit-ac/core/fixture/wasm` via `initFixture(assetUrl)` after
`npm run build:wasm:fixture`. The production `init` returns `EngineRuntime`
without fixture creation/count methods; pre-release scaffold probe consumers must
switch entries. Production WASM excludes the `foundation-fixture` Cargo feature.
The browser-only Cargo profile uses size optimization, LTO, one codegen unit,
symbol stripping and aborting panics; native release policy is unchanged.
Default Task size admission counts only its required delivered assets, including
generated glue and required lazy code, using `npm run check:browser-size`.
The separately requested qualification WASM is not loaded by production.


## Publishing

Use public scoped packages, a `next` tag for the first qualified prerelease, a reviewed immutable revision, clean artifacts and declared version. Publish in dependency order core → web → qualified framework integrations (react and astro are independent siblings). Test exact registry versions in isolated consumer fixtures and record tarball integrity/provenance. Promotion to latest is a later release decision.

Prefer npm trusted publishing from GitHub-hosted Actions with `contents:read`, `id-token:write`, exact repository/workflow and protected environment. Configure only the intended publish permissions. Initial package bootstrap may require an authenticated owner/2FA before a package-level trusted publisher can be registered; verify npm's current flow when executing the release task. Never copy a browser session credential into the repository or add long-lived publish credentials to CI as a convenience.

Current setup verifies organization ownership but publishes no package. Do not report npm readiness as an existing registry version or an end-to-end OIDC test. The release roadmap owns those actions and checks; ordinary roadmap execution cannot bypass the artifact gate.

## CLI

The CLI is a local-first editor client consuming a reviewed immutable engine revision or released crate. A distributed manifest cannot depend on `../core` or an uncommitted worktree. The [CLI contract](cli.md) defines local Markdown/literal-text editing, hosted document targets, source reconciliation, recovery and durability states. Use the shared Markdown parser and semantic commands; Markdown is the editing representation, while hosted CRDT identity/history remains intact. Local editing requires no account/network; hosted transport is optional and uses the qualified sync contract. Preserve format version and error/diagnostic semantics. Save the opened target atomically with stale-file checks; overwriting a different export destination requires an explicit option. CLI release is independent of browser release and native platform SDK support.

Sources: [Cargo workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html), [npm trusted publishers](https://docs.npmjs.com/trusted-publishers/), [npm package files](https://docs.npmjs.com/cli/v11/configuring-npm/package-json/).

## Full-client packaging

Decision003 adds the requested public docs repository alongside core, architecture and cli. Shared session/diff/optional security crates and native SDK artifacts live in core; CLI/TUI distributions remain in cli. Portable module entrypoints and host-app MCP helpers are optional surfaces qualified before publication. Roadmap 20 qualifies the full base client matrix; roadmap 24 qualifies encrypted profiles separately. No new monolithic cloud product or mandatory standalone MCP daemon is introduced.

## Expanded extension delivery

Optional highlighting and conversion dependencies use justified companion modules/crates and documented SDK entry points; no heavy runtime enters minimum loading merely by installing core. Roadmaps25–28 define shared services,31–36 wire actual native/terminal clients, and37 qualifies the expanded release. The protected profile24 additionally qualifies private assets, conversion, resolver and cloud behavior. Public docs/demo publication belongs to29; architecture fitness and capability compatibility belong to30. PDF is export-only.

## Migration sequencing decision — 2026-10-13

User-content/editor migration converters and adoption guides are deferred until the entire app is completed and correctly qualified. See [the preserved contracts and activation gate](../operations/deferred-content-migrations.md). Current SDK, integrations, executable examples and non-migration documentation do not depend on those deferred tasks; do not advertise unsupported migration capability. Internal version compatibility and data preservation required for current correctness remain mandatory.
