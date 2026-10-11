# FND-1.1 protocol toolchain evidence

Verified 2026-10-11. Parent and I1/V1 acceptance passed locally. No publication,
provider calls, schema qualification or browser WASM loading claim.

Source: immutable `source-68b66c0ed334.md`, revision
`38b5b9d96921dc419471bdce3a85537df40e7bc3255ebbdc4a20c0ace71d0897`.
Core base: `f3d4d35182ee4a96ec99bc5b30832cee22c9bb14`; implementation is uncommitted.
[Receipt](receipt.json) records SHA-256 for all implementation paths and artifacts.
Fixed Unicode test literals are the fixtures; no corpus/update artifact is claimed.

## Implemented boundary

Exact pins: Yrs 0.28.0 (`small-client`, empty default features; no `sync`/`weak`),
wasm-bindgen 0.2.129 (default `std`), dev-only Yjs 13.6.33 and y-protocols 1.0.7.
Both lockfiles resolve. [Feature tree](features.txt) records the actual graph.
`editac_core::new_document` is the single factory, with explicit UTF-16 and a fresh
Yrs-generated 32-bit client ID. It creates no schema roots. Tests cover Unicode
lengths and insertion/deletion after emoji. This does not yet reject invalid
surrogate-pair positions or qualify interop; those belong to subsequent gates.

Rust/Cargo 1.97.1, Node 24.19.0, npm 11.17.0. The pinned Rust target is installed;
CI installs it and fetches locked dependencies before offline checks. The compiler
baseline is required and verified, not an inferred minimum. Future binding tooling
must match wasm-bindgen 0.2.129. No bridge is exported yet.

The Homebrew `node@24` symlink resolves to Node 26 on this host. Node commands used
`PATH=/Users/bpstr/.nvm/versions/node/v24.19.0/bin:$PATH`; the workspace check also
prepended `/Users/bpstr/.cargo/bin`. Rust standalone commands used
`rustup run 1.97.1` before the commands listed below. No system links were changed.

## Results

| Command | Result | Evidence |
| --- | --- | --- |
| `cargo generate-lockfile` | exit 0; 45 registry packages resolved | [resolution](logs/cargo-resolution.log) |
| `npm install --ignore-scripts --no-audit --no-fund` | exit 0 | [resolution](logs/npm-resolution.log) |
| `cargo check --workspace --locked` | exit 0 | [native](logs/native.log) |
| `cargo check -p editac-wasm --target wasm32-unknown-unknown --locked` | exit 0 | [WASM](logs/wasm.log) |
| `cargo test -p editac-core --test protocol_toolchain --locked` | 3 executed / 3 passed / 0 failed / 0 skipped | [factory](logs/factory-tests.log) |
| `node --test tests/protocol-toolchain.test.mjs` | 3 executed / 3 passed / 0 failed / 0 skipped | [JS](logs/js-tests.log) |
| `node --input-type=module -e "import('yjs').then(y=>new y.Doc().destroy())"` | exit 0 (empty successful output) | [probe](logs/js-probe.log) |
| `npm run check` | exit 0; Rust 3/3, JS 3/3; 0 failures/skips; 3 compiled package imports; format/typecheck/build/native/WASM pass | [integration](logs/workspace-check.log) |

Workspace unit/doc harnesses have zero tests; they are not acceptance evidence.
The named factory suite executes three tests. Compilation probes have exit results,
not invented test counts. Initial factory test compilation exited 101 with zero
executed tests due to a missing `ReadTxn` import; [failure](logs/factory-tests-initial.log)
is retained. Adding the import materially repaired it before the passing rerun.

## Cleanup and continuation

No browsers or servers were started. Existing unrelated services remain untouched.
Session-created `core/target` had no open files and was removed after checks:
485.32 MiB allocated output removed. [Cleanup receipt](cleanup.json) records free
space before/after and the observed delta (other concurrent work affects it).
19.20 GiB remained free immediately afterward. Existing npm dependencies and
qualification evidence are preserved; broader disk cleanup is outside this batch.

Next gate: FND-1.2 reproducible semantic fixtures, now dependency-ready.
