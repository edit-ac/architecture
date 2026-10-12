# Engine foundation entry qualification

ENG-1.1 is locally verified. The [receipt](receipt.json) ties the immutable engine source, current completed foundation revision, tested working-tree sources, frozen schema/profile and interop artifacts to exact commands and counts. No production engine behavior or deployment is asserted.

The deterministic [entry audit](check-entry.py) checks all 42 original foundation checkbox texts, the current upstream source revision, successful nonzero acceptance, and preserved hashes: 48 tested sources, 4 compiled assets, 1,299 evidence files, 13 prerequisite receipts. Run `python3 ../architecture/evidence/engine-entry/check-entry.py` from core. [Integrity results](integrity.json): 6/6 passed.

With the pinned toolchain PATH and RUSTDOC recorded in the receipt, `cargo test -p editac-core --test interop --locked` passed 1/1, and `node --test tests/interop.test.mjs` passed 3/3 (its setup also asserts real Rust exchange 1/1). Zero failures/skips/filtered/cancelled/todo. The existing fixture exchanges actual Yrs/Yjs v1 bytes, state vectors, XML/text marks and Unicode through six duplicate/reordered delivery schedules. It does not substitute for the separately preserved frozen structural mapping qualification.

Full logs, exits and named rerun binary artifacts are retained here. Profile `editac.yrs-yjs.v1`, schema `editac.registry.v1`, v1 bytes and UTF-16 remain frozen. Fresh passing evidence permits ENG-1.2 in the next iteration. Source roadmaps and prior/unrelated working-tree changes were preserved. No provider, credentials, server, browser, publication or runner startup was needed.
