# Portable extension entry evidence

MOD-1.1 / I1 / V1 passed at immutable source revision `621cbff280187a584cd0ceb5b9ac66d176b916c16f99ba34a48e6fd74c08c294`. See [receipt.json](receipt.json) for commands, source/artifact hashes, failed-oracle repairs and cleanup.

- Required Rust suites: 66 executed/passed, zero failures/skips; nested pinned Yjs move exchange: 11/11.
- Built and packed web/WASM clipboard/storage/DOM integration: 5 cases in each Chromium/Firefox/WebKit, 15/15, zero failures/skips/cancellations.
- Shared corpus: image/callout/table tuples, malformed/unsafe/version-incompatible tuples, future namespaced tuple and custom mark. Rust-produced unknown-content checkpoint is restored directly in real WASM, with safe DOM text and rejection before mutation.
- Builds and diff-check exit 0. Two failed fixture-oracle runs are preserved. These receipts prove portable entry and preservation; declarative registration belongs to MOD-1.2. No publication, native/device support or live provider claim.
