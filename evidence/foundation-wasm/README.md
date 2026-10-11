# Foundation WASM loading boundary

FND-1.13 is implemented and locally verified. The original build compiled Rust 1.97.1 / wasm-bindgen 0.2.129 into actual web-target WASM and glue. Original Node check: 6 executed, 6 passed, 0 failed/skipped/cancelled/todo. `receipt.json` records exact commands, revisions and source/artifact/log hashes. `harness.json` records pinned Chromium/Playwright, the installed tarball integrity, requested asset URLs and task-owned process teardown.

Both native browser ESM consumers initialized the real binary: a supplied URL and an offline-installed local package. Throwing SSR guards observed no window/document/fetch/WebAssembly access at import. Initialization created no replica. Concurrent calls, explicit URL conflicts and failed-load retry passed. Real WASM fixture updates preserve UTF-16 Unicode and bold/italic attributes through pinned Yjs; duplicate JS update delivery and malformed decode rejection passed.

WASM: 664,648 bytes; generated JS glue: 8,523 bytes. `artifacts/` preserves the real generated binary/glue/declarations, wrapper and raw pre-bindgen module. Binary fixture files preserve the actual tested updates. `cargo-check.log` is native workspace/all-target compilation (not a test suite); `packages.log` records all workspace typechecks/builds and three compiled imports. No feature check failed; no test rerun was needed. Documentation was updated after successful checks without changing tested implementation.

The minimal bridge uses the earlier disposable `interop` XML fixture. It is not production frozen-schema commands, an untrusted admission port or persistence proof. Native browser ESM is qualified; bundler-specific rewriting and the full browser release matrix are not. Packages remain private. No deployment, publishing, paid inference or live transport occurred.

The matching CLI was installed at `/Users/bpstr/.cargo/bin/wasm-bindgen`; normal `npm run build:wasm` uses it. The official web-target initialization model is documented in [wasm-bindgen's example](https://wasm-bindgen.github.io/wasm-bindgen/examples/without-a-bundler.html); the test uses the pinned [Playwright library](https://playwright.dev/docs/library).

Task browser/server PIDs exited, the owned port has no listener and the temporary consumer is gone. `hygiene.json` records the exact three removed session-created release/download paths (144,171,051 bytes) and about 17.85 GiB remaining free. Compiled qualification evidence, shared browser caches, other target artifacts and unrelated services were preserved.
