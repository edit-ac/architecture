# Direct baseline synchronization adapter

SYN-1.2 is implemented and locally verified against immutable roadmap revision `9fb151bc…a17d`. `packages/web/src/sync/protocol.ts` exchanges baseline step1/step2/update directly through the existing Rust WASM EngineHandle. Production state has no JS Y.Doc mirror. Frames and vectors are bounded; complete peer metadata must match before attachment; update admission remains staged in Rust. Update encoding and sync protocol remain v1; the real engine and pinned JS mapper share editor-v5 schema.

`npm run build` exits 0. Exact final `node --test tests/sync-protocol.test.mjs`: 7 executed, 7 passed, 0 failed/skipped/cancelled. Concurrent Unicode/marked updates, duplicate delivery and deletion-only sync converge by full schema snapshot and decoded state-vector clocks. Invalid inputs preserve live committed state/history. State-vector serialization order is nonnormative.

Existing outbox/interop integration: 27 distinct cases ultimately pass, with 0 unresolved failures/skips. The original combined run passed 23 and failed 4 because a relative evidence path resolved under Cargo's crate directory; only those four were rerun with an absolute output path and passed. Nested Rust exchange: 1 passed, 0 failed/ignored. Chromium passed with zero application network requests; its PID/control listener exited. This is local integration evidence, with no durable relay, authorization or deployed service claim.

[Receipt, source/build/fixture hashes, exact commands and preserved failures](synchronization-protocol/receipt.json). [Process and disk cleanup](synchronization-protocol/cleanup.json). Unrelated checkout changes and shared artifacts remain intact. SYN-1.3 reconnect/backpressure is the next dependency-ready gate.
