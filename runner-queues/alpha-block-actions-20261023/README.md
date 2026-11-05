# Alpha audit adopted by the active roadmap runner

User request, 2026-10-23: make the alpha polish findings and mandatory shared Turn into support part of the active runner before it can declare alpha ready.

Adopted in existing run `6bd65538752cad53b001fcb8`, workspace `/Users/bpstr/Github/edit-ac`, using its existing 55 FIFO paths and separate progress files. The queue now has **226 parents, including 16 new audit parents**. The opening source/current worker and verified progress were preserved; no second runner, restart or queue append was needed. Roadmap Runner 0.10.2 loads each pending file when its entry starts. The [manifest](../single-format-feature-first-20261023/manifest.json) and [requirement map](../single-format-feature-first-20261023/requirement-map.json) are the executable ownership plan. Adoption is not implementation or a readiness pass.

## Delivery order

| Existing queued source | Added work | New parents |
|---|---|---:|
| [01 — Admission and replay](../single-format-feature-first-20261023/01-canonical-admission-and-replay.md) | DRA-1.1–1.5: table representation/implementation, journal rollover, structural-lifetime design/implementation | 5 |
| [02 — Commands and consumers](../single-format-feature-first-20261023/02-canonical-projection-and-consumers.md) | BTA-1.1–1.5: lossless Turn into, portable command ports, extension registration, advanced conversion policy, general Insert after | 5 |
| [03 — Regressions and API cleanup](../single-format-feature-first-20261023/03-regression-oracles-and-version-scaffolding.md) | BTU-1.1–1.3: configurable menu/handle, shared slash/keyboard actions, public API and extension recipes | 3 |
| [04 — Focused safety and handoff](../single-format-feature-first-20261023/04-durability-gate-and-guide-handoff.md) | Strengthened SFC-5.1/5.2 gate, native handoffs and final audit-result validator | Existing owners |
| [43 — Complete shared suites](../single-format-feature-first-20261023/43-full-shared-suites.md) | BTQ-1.1/1.2: final semantic/persistence and extension/review coverage | 2 |
| [45 — Complete web suites](../single-format-feature-first-20261023/45-full-web-suites-part-2.md) | BTQ-1.3: final menu/product/packed-consumer coverage, reusing engine-specific results | 1 |
| [54 — Aggregate readiness](../single-format-feature-first-20261023/54-aggregate-readiness.md) | Mandatory audit-row reconciliation and explicit NOT READY FOR ALPHA on unresolved predicates | Existing owners |

The former three unqueued block-action proposals were folded into these actual pending sources; they are not a second executable plan. Cross-file prerequisites are explicit in the manifest, local dependencies stay within their source, and all original parents/acceptance remain required. Complete native/terminal suites 46–51 also own their actual installed shared-action routes, focus and lifecycle behavior.

## Findings and release owners

| Requirement | Observed gap or required behavior | Delivery owner | Final proof |
|---|---|---|---|
| ALPHA-TABLE | Two replicas editing separate current-format table cells converged with one edit lost under whole-atom replacement. | DRA-1.1/1.2 | QSH-1.1/1.2 and QWB-1.7 |
| ALPHA-JOURNAL | A current checkpoint plus valid journal entries reopened at 4096, rejected at 4097; covered entries were retained. | DRA-1.3 | QWB-1.5 real WASM/IndexedDB rollover, fallback, outbox and crash cases |
| ALPHA-LIFETIME | Retained immutable structural records had fixed replay bounds; long-session qualification was missing. | DRA-1.4/1.5 | QSH-1.1/1.2 and QWB-1.5 long-session/reopen/disconnected-peer proof |
| ALPHA-CURRENT | Legacy creation/admission/consumer branches and old-format test coverage still needed current-format convergence. | Existing SFC-2–5 owners | QSH-1.1/1.2 and QRD-1.1 |
| ALPHA-TURN-INTO | No general captured shared conversion API; heading/paragraph conversion must be lossless and identity-preserving. | BTA-1.1/1.2 | BTQ-1.1 |
| ALPHA-EXTENSION | Extensions need conversion registration; advanced mappings need exact impact/review or explicit refusal. | BTA-1.3/1.4 | BTQ-1.2 |
| ALPHA-INSERT-AFTER | Existing separator insertion did not provide generic block insertion after a subtree. | BTA-1.5 | BTQ-1.1/1.3 |
| ALPHA-MENU | Optional reorder existed; generic block property menu and block-local discovery were missing. Menu and reorder configuration must remain independent. | BTU-1.1/1.2 | BTQ-1.3 and applicable target-platform owners |
| ALPHA-API-DX | Installed public command/extension recipes must match the same implementation, including menu-off use. | BTU-1.3 | BTQ-1.2/1.3 |
| ALPHA-FINAL-GATES | Earlier recorded size results exceeded the hard caps; full current runtime/functional qualification remains required. | SFC-5.2 preserves ownership; existing bounded optimization owner repairs | Existing QPF, native/web full suites and QRD-1.1–1.3 |

These observations came from the 2026-10-23 review; owners must inspect current code and reuse any applicable fix evidence before making changes. Temporary probes are not permanent prerequisites: authored deterministic regressions must reproduce the invariant in the repository. The audit's 42 browser reorder passes used an existing packed build, and its 35 historical move tests were not current-format qualification. Current-format focused assertions and SDK typechecks likewise did not close complete product/native readiness. Do not relabel these observations as full release proof.

## Durable contract and alpha decision

Follow [block actions](../../specs/block-actions.md) and [alpha durability closures](../../specs/alpha-durability-closures.md). Paragraph/heading conversions preserve IDs, sources, content, rich/opaque data, descendants, selection and one undo. Advanced conversions cannot silently flatten or discard data. The API remains available when block menus are off. Table and lifetime representation decisions are resolved before freezing the single current production format, with original real data preserved and explicit offline adoption only when needed.

SFC-5.2 must deliver the audit-result validator and its deterministic negative fixtures; QRD-1.3 must run it against actual current results. Every `alphaAuditRequirements` row is required. Missing, stale, design-only, zero-case, failed or required-skipped proof means **NOT READY FOR ALPHA**. This strengthens the existing release gate; it does not waive complete original suites, target-runtime evidence, accessibility, the 512 KiB total/32 KiB editor-JS gzip caps or resource limits. Focused delivery checks precede native consumers; broad final suites stay after feature delivery and reuse matching proof.
