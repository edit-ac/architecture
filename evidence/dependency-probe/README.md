# Dependency compilation probe

Recorded on 2026-10-11 with Rust and Cargo 1.97.1 on macOS arm64. This unpublished,
isolated Cargo package checks the proposed Rust dependencies together. It is not
part of the production editor workspace and adds no production SDK API.

| Dependency | Exact pin | Configuration |
| --- | --- | --- |
| Yrs | 0.28.0 | Default features plus `small-client` |
| pulldown-cmark | 0.13.4 | Default features |
| wasm-bindgen | 0.2.129 | Default features |
| UniFFI | 0.32.2 | Optional; enabled only by `native-probe` |

`Cargo.lock` fixes the resolved transitive graph. The WASM dependency tree confirms
that UniFFI is absent when `native-probe` is disabled.

## Recorded results

| Command | Exit code | Evidence |
| --- | --- | --- |
| `cargo fmt --all -- --check` | 0 | `logs/fmt.log` |
| Native `cargo check --features native-probe` | 0 | `logs/native.log` |
| Install `wasm32-unknown-unknown` for Rust 1.97.1 | 0 | `logs/wasm-target.log` |
| Initial WASM `cargo check --locked --target wasm32-unknown-unknown --no-default-features` | 101 | `logs/wasm-initial.log` |
| WASM check with explicit rustup compiler, `--locked --offline` | 0 | `logs/wasm-verified.log` |
| Native check with explicit rustup compiler, `--locked --offline --features native-probe` | 0 | `logs/native-locked.log` |
| WASM `cargo tree --locked --offline --target wasm32-unknown-unknown --no-default-features` | 0 | `logs/wasm-tree.log` |

There were seven recorded command attempts: six passed, one failed, zero skipped.
The failure was environmental: Cargo selected a Homebrew compiler that did not
own the target installed under rustup. Setting `RUSTC` to the compiler returned
by `rustup which --toolchain 1.97.1 rustc` fixed the WASM check without changing
dependency versions or features. Both final target checks pass from the lockfile.
No test cases were executed.

Full original logs remain at `/private/tmp/edit-ac-dependency-*.log` on the setup
machine. Repository copies replace the local checkout prefix with `$WORKSPACE`;
compiler output is otherwise unchanged.

## Reproduce

Run from this directory with rustup installed:

```sh
rustup toolchain install 1.97.1 --profile minimal --component rustfmt
rustup target add --toolchain 1.97.1 wasm32-unknown-unknown
export RUSTC="$(rustup which --toolchain 1.97.1 rustc)"
export CARGO_TARGET_DIR="${TMPDIR:-/tmp}/edit-ac-dependency-target"
rustup run 1.97.1 cargo fmt --all -- --check
rustup run 1.97.1 cargo check --locked --features native-probe
rustup run 1.97.1 cargo check --locked --target wasm32-unknown-unknown --no-default-features
```

Add `--offline` after dependencies have been fetched. Keep UniFFI disabled for
the browser target. Do not infer a native SDK implementation from the native
dependency check.

## Limits

`cargo check` verifies target-specific type checking and dependency resolution.
It does not link a release WASM artifact, instantiate it in JavaScript, generate
or execute UniFFI bindings, exchange Yjs updates, validate an editor schema,
measure size/performance, or establish runtime compatibility. Yjs interoperability,
client identity constraints, UTF-16 semantics, Markdown behavior, and native ABI
qualification remain separate foundation/native roadmap work.

## Cleanup

After all probe commands completed, `lsof` found no open files in the temporary
target directory. Removing `/private/tmp/edit-ac-dependency-target` reclaimed
514.31 MiB of allocated build output; 22.66 GiB remained free on the data volume.
`cleanup.json` records the measurement. Full logs, the lockfile, global Cargo
caches, and the installed Rust WASM target were retained.
