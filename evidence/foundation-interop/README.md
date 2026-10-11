# FND-1.3 binary update exchange evidence

Implemented and locally verified 2026-10-11. Parent FND-1.3 and I1/V1 passed.
Source snapshot SHA-256 / revision:
`38b5b9d96921dc419471bdce3a85537df40e7bc3255ebbdc4a20c0ace71d0897`.
Core base `f3d4d35182ee4a96ec99bc5b30832cee22c9bb14`; changes remain uncommitted.
[Receipt](receipt.json) records tested implementation hashes, binary hashes/bytes,
commands, counts, runtime pins and cleanup.

## Boundary

`core/fixtures/interop/bridge.mjs` and `core/crates/editac-core/tests/interop.rs`
compose actual Yjs/Yrs encoders and consumers. Disposable XML fragment `interop`
contains one `p` with string attributes and XML text with boolean formatting.
All six permutations of three dependent updates are delivered twice, then replayed
in reverse on both language consumers. Assertions compare semantic text, exact
marks, element attributes and UTF-16 length, independently of CRDT byte identity.
The fixture exercises emoji, combining accents, ZWJ, flags and RTL. Insert offset
3 follows the first supplementary emoji; deletion at 4 removes the original `b`.
State-vector differences work Rust→JS using a JS writer baseline and JS→Rust using
a Rust baseline with a new JS writer. Writer IDs are fixed, distinct and test-only.
No production schema, relative-anchor or structural-move claim is made.

The Node suite invokes the shared Rust harness in setup, then asserts the generated
Rust binary updates and state-vector deltas. `check:interop` is wired into the
workspace `check`. Both suites use only deterministic local inputs and runtimes.

## Verification

Pinned Rust 1.97.1 and Node 24.19.0 were placed on PATH as shown in the receipt.

| Command | Executed / passed / failed / skipped | Exit | Log |
|---|---|---|---|
| `cargo test -p editac-core --test interop --locked` | 1 / 1 / 0 / 0; 0 filtered | 0 | `rust.log` |
| `node --test tests/interop.test.mjs` | 3 / 3 / 0 / 0; setup Rust 1 / 1 / 0 / 0 | 0 | `node.log` |
| `cargo test -p editac-core --test protocol_toolchain --locked --offline` | 3 / 3 / 0 / 0 | 0 | `protocol-rust.log` |
| `node --test tests/protocol-toolchain.test.mjs` | 3 / 3 / 0 / 0 | 0 | `protocol-node.log` |
| `cargo fmt --all -- --check` | formatting probe | 0 | `format-check.log` |
| `git diff --check` | whitespace probe | 0 | `diff-check.log` |

Initial compile failed E0277 (`ClientID` lacks `From<u64>`), executing zero tests.
`rust-initial.log` preserves the failure; the initial yielded shell exit was not
captured. Replacing conversion with `ClientID::new` repaired the relevant code
before the successful run. No ignored/skipped/missing tests count as acceptance.

Generated `.bin` updates and state vectors are retained in `artifacts/`; binary
receipt means CRDT integration only and never durable acknowledgment. No network,
publication, paid API or background runner was started. Test temporary directories
were torn down. The inactive session-created `core/target` was removed after an
open-file and timestamp check: 152,478,981 logical bytes, 19.65 GiB remaining free.
Other existing browser/service candidates were preserved.
