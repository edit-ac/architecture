# FND-1.4 XML structural probe evidence

Implemented and locally verified 2026-10-11; not deployed. FND-1.4 and I1/V1 passed.
Source revision `38b5b9d96921dc419471bdce3a85537df40e7bc3255ebbdc4a20c0ace71d0897`.
[Receipt](receipt.json) records source/base/working-tree hashes, fixed fixture, runtime,
commands, test counts, update/trace hashes and cleanup. Core changes are uncommitted.

## Candidate and observed identity

`core/crates/editac-core/tests/structure_xml.rs` is isolated test code. Two XML
sections contain one paragraph with logical ID `block-1` and rich XML text `a😀b`.
The emoji is bold at UTF-16 1..3; an italic `!` is inserted at offset 3. This is the
minimal FND-1.2 astral input, not a corpus benchmark or production schema.

Editing in place preserves element `<11#4>` and text `<11#6>` BranchIDs.
Sequential relocation snapshots with `AsPrelim`, inserts under the other parent,
and removes the original: text/marks/logical ID survive, but element/text IDs become
`<11#16>`/`<11#18>`. A fresh replica restored from v1 bytes has those same new IDs.
These observations apply to this clone/remove candidate; no general claim about
all possible XML representations or move implementations is made.

Concurrent writers 22 and 33 relocate and edit respectively from the same writer-11
baseline. The editor retains original text identity before delivery. The mover
creates a replacement subtree. Both writers and fresh replay observers converge
to the moved **initial** rich text. The concurrent `!`/italic edit does not appear
in the visible destination. All six base/move/edit arrival orders, duplicate delivery
and reverse replay assert exact visible content, marks, parent and branch identities.
Convergence does not meet the engine's eventual identity-preserving move requirement;
this result informs FND-1.5/FND-1.6 rather than adopting a schema or recovery policy.

Three text traces and base/move/edit binary updates are retained in `artifacts/`.
Receipt of these bytes is CRDT integration, not durable acknowledgment.

## Verification

| Command | Executed / passed / failed / skipped | Exit | Log |
|---|---|---|---|
| `cargo test -p editac-core --test structure_xml --locked` | 3 / 3 / 0 / 0; 0 filtered | 0 | `rust.log` |
| `cargo test -p editac-core --test interop --locked` | 1 / 1 / 0 / 0; 0 filtered | 0 | `interop-rust.log` |
| `node --test tests/interop.test.mjs` | 3 / 3 / 0 / 0; setup runs Rust harness | 0 | `interop-node.log` |
| `cargo fmt --all -- --check` | formatting probe | 0 | `format-check.log` |
| `git diff --check` | whitespace probe | 0 | `diff-check.log` |

Initial feature run passed 3 tests with an unused-import warning, then the unused
import was removed and the narrow suite passed again. Import wrapping caused a
formatting check failure (exit 1); `format-check-initial.log` preserves it. Rustfmt
repaired that whitespace before the passing formatting check. No feature test failed,
was skipped, or was filtered away. Final source only wraps imports differently from
the narrow tested source; semantic test evidence is unchanged.

No paid inference, network transport, server, browser, publication or background
runner was started. Other tasks' processes/listeners were preserved. The session-created
inactive `core/target` was removed after all tests exited and an immediate open-file
check found no users: 162,764 KiB by `du` (185,183,048 summed logical file bytes).
Remaining data-volume free space was 20.55 GiB; concurrent system activity also changes
free space. Source, dependencies and evidence remain intact.
