# FND-1.5 stable-registry probe evidence

Implemented and locally verified 2026-10-11; not deployed. FND-1.5 and I1/V1 passed.
Source revision `38b5b9d96921dc419471bdce3a85537df40e7bc3255ebbdc4a20c0ace71d0897`.
[Receipt](receipt.json) records base revisions, tested working-tree hashes, fixture,
runtime, commands, counts, artifact hashes and cleanup. Core changes are uncommitted.

## Candidate and observations

`core/crates/editac-core/tests/structure_registry.rs` is isolated test code.
Each independently editing replica has exactly one Yrs document. Two parent records,
a map of stable block IDs to integrated rich XML text, and one placement map all live
in that document. Moves replace one immutable `(parent, order)` array value at the
block's placement key; they never copy, remove or reinsert its shared text.

The fixture matches the XML candidate: parents left/right, block-1, `a😀b`, bold
emoji at UTF-16 1..3 and concurrent italic `!` insertion at 3. No final schema,
anchor, split/join, deletion, cycle or production command qualification is claimed.

In-place editing and sequential relocation retain text BranchID `<11#2>` and exact
marks. Sequential binary restore retains the same identity and placement. Concurrent
writer 22 moves to right/0 while writer 33 edits the original text. Both writers
converge to right/0 with `a😀!b`, bold emoji, italic insertion and original identity.
For concurrent placements, writer 22 requests right/10 and writer 33 left/20.
Pinned Yrs selects the complete writer-33 left/20 tuple on both writers; no mixed
parent/order tuple is observed. Each race additionally covers all six permutations
of baseline/two-operation delivery, duplicated updates and reverse replay on fresh
observers, comparing exact semantic projections and text identity.

Four identity/projection traces and seven v1 binary updates are in `artifacts/`.
Receipt of update bytes establishes CRDT integration, not durable acknowledgment.
These results inform the FND-1.6 comparison; no structural representation is adopted.

## Verification

| Check | Executed / passed / failed / skipped | Exit | Log |
|---|---|---|---|
| `cargo test -p editac-core --test structure_registry --locked` | 4 / 4 / 0 / 0; 0 filtered | 0 | `rust.log` |
| `cargo test -p editac-core --locked` | binary tests 11 / 11 / 0 / 0; 0 filtered; subsequent doctest compile failed | 1 | `core-integration.log` |
| Matching pinned `RUSTDOC`, `cargo test -p editac-core --doc --locked` | 0 examples; compile probe only | 0 | `doc-repair.log` |
| `node --test tests/interop.test.mjs` | 3 / 3 / 0 / 0; setup also runs 1 Rust test | 0 | `interop-node.log` |
| `cargo fmt --all -- --check` | formatting probe | 0 | `format-check.log` |
| `git diff --check` and new-file whitespace check | whitespace probes | 0 | `diff-check.log`, `new-file-whitespace.log` |

The initial registry compilation failed before any tests ran because `yrs::Number`
was treated as a primitive number. `rust-initial-compile-failure.log` preserves it;
lossless integer conversion and checked u32 conversion repaired the source before
the passing narrow check. The broad binary suites passed, but Homebrew rustdoc
rejected rustup-built dependencies (E0514). Retrying only that failed compile boundary
with `RUSTDOC="$(rustup which rustdoc)"` succeeded. There are no doc examples; that
zero-test probe contributes no acceptance evidence. Nonzero registry, XML, protocol
and interoperability tests establish the selected gate's local verification.

## Cleanup

No task-owned server/browser was started. Observed Assign browsers and servers
belong to other active work and were preserved. After test processes exited and an
immediate empty `lsof +D` check, this session's newly created `core/target` was removed:
185,085,952 allocated bytes (195,162,786 logical file bytes). Data volume free space
after removal: 21,875,798,016 bytes, about 20.37 GiB. Source, dependencies, credentials
and qualification evidence remain intact; no cleanup outside this session's output.
