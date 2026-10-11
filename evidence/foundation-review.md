# Foundation completion and code review

The foundation runner exited successfully after 14 iterations. All 42 original
implementation and validation checkboxes are checked in its separate progress
file. The review corroborated the final approval receipt, verified 48 tested
source hashes, 1,299 evidence hashes and 13 prerequisite receipt hashes before
making corrections, with no mismatches. Historical receipts remain unchanged.

Core commit: `2696304e556cb528f7fec4e5ec3ea3307dc8d74b`.
The [review receipt](foundation-review/receipt.json) verifies all 101 committed
files against the isolated checkout used for the final checks. The active engine
runner's document implementation and initialization tests are outside this commit.

## Findings and corrections

| Priority | Finding | Correction |
| --- | --- | --- |
| P2 | A concurrent split and move to the maximum unsigned placement order can overflow Rust projection; JS emits an out-of-range derived order. Local split preparation also lacks the rejection already required by schema v1. | Reject the local split before mutation. Checked Rust projection returns a recovery reason and preserved v1 update; JS raises an explicit recovery error carrying the update. Regression tests cover reordered/duplicate delivery, reverse replay and restored snapshots without repair writes or loss of marked text. |
| P2 | CI runs Rust probes but omits frozen JS schema/admission, structural JS exchange and compiled browser/packed-consumer WASM qualification. | Wire schema checks into `npm run check`; CI installs the matching wasm-bindgen CLI and headless Chromium and invokes `npm run check:wasm`. |
| P3 | The README attributes the core fixture loader to the still-empty web and React packages. | Restore their scaffold descriptions and describe the actual foundation checks. |
| P3 | The runner guide uses managed `start` with sibling source/progress paths that 0.8.0 rejects; changing Node PATH can select a different installed runner. | Document the supported foreground command, owned detached launch/readiness checks and explicit executable selection. |

No unresolved blocking finding remains within this foundation scope. The maximum
order behavior implements the existing frozen contract; no schema, wire or
production ABI change was introduced. The old `project` helpers assert trusted
positive fixtures; recovery-capable Rust callers use `try_project`. Neither that
helper nor the JS example is a production resource-bounded admission service.

## Validation

| Command in isolated core checkout | Executed / passed / failed / skipped |
| --- | --- |
| `cargo test -p editac-core --locked --offline` | 59 / 59 / 0 / 0 |
| `npm run check:schema` | 19 / 19 / 0 / 0 |
| `npm run check:wasm` | 6 / 6 / 0 / 0 |

Source/document whitespace checks and Rust formatting passed. Raw historical
logs are retained byte-for-byte; 38 log/text artifacts contain captured whitespace
that is intentionally not normalized.

The Node suites also recorded zero cancellations; Rust recorded zero filtered
tests. Empty unit/doc harnesses are compilation evidence only. Tests use the
pinned local toolchains, real deterministic CRDT fixtures and compiled WASM;
there are no provider calls, paid AI tests or live-content dogfood. Local command
validation does not establish a successful future Ubuntu CI run.

The original failing JS regressions, isolated Rust overflow, a live Rust probe
that encountered unrelated in-progress engine compilation, and an interrupted
repair attempt are retained. The interrupted repair acquired a root while a read
transaction was held; moving root acquisition before the transaction resolved it.
Only the final complete passing suites qualify the corrections.

The Chromium process, controller, local HTTP server and temporary package consumer
exited. Their teardown facts are retained in the receipt. Review-created build and
dependency directories are temporary; original qualification assets and concurrent
engine outputs are preserved.

## Complexity assessment and continuation criteria

Requirement-to-complexity ratio: 3/10. The small fixture bridge and loader expose
one concrete runtime; most code is test-only convergence and reconstruction
evidence required by the roadmap. No unjustified plugin framework, deployment
infrastructure or additional abstraction was found. There is no measured vanity
maintenance debt to quantify. The maintenance question is when the engine can
replace disposable fixture adapters while preserving their qualification evidence.

For this non-production foundation, the proposed gate owner is the project owner
`bpstr`, separate from the implementation worker. The evaluation window is each
dependent track's entry gate. Production adoption, operating-budget, latency,
incident and staffing thresholds are inapplicable to a private qualification
fixture and were not invented here.

- A missing, zero-match, failed or skipped required check prevents a qualification
  claim until a complete passing rerun is recorded; retain failures and data.
- Any change to the exact dependency pair, schema, ownership descriptors or wire
  profile requires new qualification before compatibility claims continue.
- Keep packages private. Production resource admission, semantic commands,
  history, durability and broader browser/device/performance proof remain the
  [documented downstream gates](foundation.md).
- Add abstractions only for concrete consumers; justify dependencies against the
  task boundary; keep production and disposable fixture interfaces separate.
- Reassess fixture adapters at the engine entry and exit reviews. This report
  proposes no deployment, automated shutdown, extra services or paid experiments.
