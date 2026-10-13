# Set up the edit.ac workspace

The workspace is one parent directory containing independent Git repositories. Keep the checkout names below: contracts, fixture tools and runner paths use sibling repositories. The parent directory is not a Git repository.

```text
edit-ac/
  AGENTS.md          # local copy of architecture/ROOT_AGENTS.md
  architecture/      # contracts, roadmaps and qualification evidence
  core/              # Rust engine and JavaScript SDK workspace
  cli/               # standalone Rust CLI checkout
  docs/              # public website and developer documentation
```

## Clone and install the root instructions

From the directory where you keep projects, with GitHub access configured:

```sh
mkdir -p edit-ac
cd edit-ac
git clone git@github.com:edit-ac/architecture.git architecture
git clone git@github.com:edit-ac/core.git core
git clone git@github.com:edit-ac/cli.git cli
git clone --recurse-submodules git@github.com:edit-ac/docs.git docs
cp architecture/ROOT_AGENTS.md AGENTS.md
cmp architecture/ROOT_AGENTS.md AGENTS.md
```

**Copy `architecture/ROOT_AGENTS.md` to the workspace root as `AGENTS.md`, not `ROOT_AGENTS.md`.** Agents discover the `AGENTS.md` filename in the parent of each checkout. Keep each repository's own `AGENTS.md` in place; it supplies repository-specific instructions.

For an existing workspace, compare any existing root `AGENTS.md` before replacing it and preserve local additions. Update the version-controlled `architecture/ROOT_AGENTS.md` when shared root rules change, then copy it to the parent again. Commit the canonical file in the architecture repository; the parent copy is intentionally outside Git. This file copies the user's root rules; it does not install or replace global agent configuration.

For an existing docs checkout, initialize the pinned theme:

```sh
git -C docs submodule update --init --recursive
```

## Select the checked-in toolchains

Read `core/package.json` for the exact Node/npm versions and `core/rust-toolchain.toml` and `cli/rust-toolchain.toml` for Rust, components and targets. Use the selected Node version before installing dependencies. Rust commands must use rustup's selected toolchain so the browser target is available; another `cargo` or `rustc` earlier on `PATH` can bypass it.

Install the wasm-bindgen CLI version that matches the locked crate, as described in [the core package guide](https://github.com/edit-ac/core/blob/main/packages/core/README.md). Install the Zola version from `docs/.zola-version`; the docs CI installer targets Linux and is not a macOS installer. Check `node --version`, `npm --version`, `rustc --version`, `cargo --version`, `wasm-bindgen --version` and `zola --version` before validation.

From the workspace root, prepare locked dependencies:

```sh
(cd architecture && npm ci --ignore-scripts)
(cd core && cargo fetch --locked && npm ci --ignore-scripts)
(cd cli && cargo fetch --locked)
```

For core browser checks, install the browsers belonging to the locked Playwright dependency from `core`: `npx --no-install playwright install chromium firefox webkit`. The default baseline check runs all three engines. Dependency installation may download packages and browsers; validation uses deterministic fixtures and prepared/mock transports. Follow the root paid-inference policy before any AI test or separately authorized live-content dogfood.

## Verify each checkout

Core interoperability tests require isolated exchange directories. In the shell used for checks, allocate a separate directory for each exchange so concurrent fixtures do not overwrite one another:

```sh
core_validation_evidence="$(mktemp -d)"
for exchange_variable in \
  EDITAC_BLOCK_COMMAND_EXCHANGE EDITAC_BLOCK_EXCHANGE EDITAC_BLOCK_KINDS_EXCHANGE \
  EDITAC_EDITOR_EXCHANGE EDITAC_FORMAT_BLOCK_EXCHANGE EDITAC_FORMAT_EXCHANGE EDITAC_GENERAL_EXCHANGE \
  EDITAC_HISTORY_EXCHANGE EDITAC_LIST_EXCHANGE EDITAC_MOVE_EXCHANGE \
  EDITAC_OWNERSHIP_EXCHANGE EDITAC_RETAINED_EXCHANGE EDITAC_SPLIT_JOIN_EXCHANGE \
  EDITAC_STABLE_EDITOR_EXCHANGE EDITAC_STABLE_JOIN_EXCHANGE EDITAC_STRUCTURAL_EXCHANGE
do
  mkdir -p "$core_validation_evidence/$exchange_variable"
  export "$exchange_variable=$core_validation_evidence/$exchange_variable"
done
export EDITAC_REPLICA_EVIDENCE="$core_validation_evidence/replica-properties"
export EDITAC_EXTENSION_ENTRY_OUTPUT="$core_validation_evidence/extension-entry"
mkdir -p "$EDITAC_REPLICA_EVIDENCE" "$EDITAC_EXTENSION_ENTRY_OUTPUT"
```

Retain the directory and failed logs with your validation record. Set Node/Rust toolchain paths explicitly for child processes as well as the interactive shell; checking only the shell's reported version is insufficient.

Run from the workspace root and retain full command output when recording qualification evidence:

```sh
(cd architecture && npm run check)
(cd core && npm run check && npm run check:wasm)
(cd cli && cargo fmt --all -- --check && cargo check --all-targets --locked --offline && cargo test --locked --offline)
(cd docs && npm run check && zola check --skip-external-links && zola build)
```

The architecture check validates planning sources and fixture contracts. Feature, browser and native qualification require the active task's named checks and their actual results. Consult each checkout's README and agent instructions for extra checks; planning validation alone does not establish shipped support.

## Resume work and maintain the workspace

Read the [architecture entry gates](README.md#start-here), the active task's named specs, and [runner operation](operations/roadmap-runner.md). Check for an existing controller before resuming one. Preserve separate progress files and their evidence; root setup does not start a runner or authorize model calls.

Commit and push from each repository separately. Keep progress, credentials and local caches outside commits. Stop task-owned test browsers and temporary preview servers after use, and preserve qualification evidence during cleanup. A root `AGENTS.md` identical to `architecture/ROOT_AGENTS.md`, initialized docs theme and passing applicable checkout checks complete setup.
