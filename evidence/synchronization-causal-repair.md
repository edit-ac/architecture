# Bounded causal replay repair

SYN-1.3 / I1 / V1 / R1 are implemented and locally verified at source revision `9fb151bc16cc567c2c66700209baff239d192e1893ab4746d98f4c8dc329a17d`, iteration 8, 2026-10-13. [Receipt](synchronization-causal-repair/receipt.json) records commands, exact source/compiled/fixture hashes, archived copies, failures and cleanup.

`SyncSession` retains only the atomic Rust missing-dependency rejection within its existing receive count/byte budget. Revision changes permit bounded reconciliation; idle pumps do not retry. Other admission errors still end attachment. Detach/reconnect retains local outbox recovery. Remote observers may replace attachment without modifying the replacement queues.

Pinned Node build passes. Canonical reconnect: **19 executed, 19 passed, zero failures/skips/cancellations**. Final integration: **71 executed, 71 passed, zero failures/skips/cancellations** (protocol 7, outbox 23, awareness 13, receipts 17, relay 11). Eight new regressions cover reverse/duplicate causal deltas, pending delete sets, idle/local progress, handshake recovery, queue bounds, malformed input, offline detach, observer replacement and the exact SYN-1.7 browser failure corpus. The initial browser module-import failure (54 passed/17 failed) is preserved; removing the new value import repairs direct browser loading before final validation.

Reconnect uses actual Rust WASM and pinned Yjs with prepared storage/socket transport. Integration additionally exercises real Chromium IndexedDB and loopback SQLite receipts. No credentials, paid inference, production authorization, deployment or power-loss qualification. **SYN-1.7 remains open**: exact frozen causal regression is prerequisite evidence, not the complete two-browser process-crash/convergence oracle.

Teardown confirms 8 recorded PIDs and 56 listeners gone; three disposable scratch roots removed, no unrelated process stopped. About 4.1 MiB evidence retained, roughly 19.6 GiB free. No session-created large artifact cleanup; scratch reclaimed size unmeasured.
