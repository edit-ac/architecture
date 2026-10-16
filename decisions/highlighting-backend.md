# Select an optional portable highlighting backend

Decision: select **Syntect 5.3.0**, pure Rust `fancy-regex`, with
**two-face 0.5.2+bat-0.26.1**'s newline-aware syntax bundle for the initial
Rust, TypeScript and JSON envelope. RCH-1.2's native and executable WASM probes
pass. This is a derived-appearance companion, independently consumed from
`editac-highlighting`; the engine and minimum SDK have no dependency on it.

The [Syntect maintainer documentation](https://github.com/trishume/syntect)
describes the pure Rust regex option. The
[two-face versioned documentation](https://docs.rs/two-face/0.5.2+bat-0.26.1/two_face/)
provides TypeScript alongside the other grammars. This avoids introducing a C
parser build/sysroot prerequisite for wasm32-unknown-unknown. Tree-sitter remains
a candidate rather than an untested selection; no browser-only alternative was
benchmarked. No comparative size or startup win is claimed.

The immutable grammar identity is the complete newline-aware bundle and its crate
checksum, not a moving upstream branch. `core/fixtures/highlighting/backend.json`
pins the bundle SHA-256, package versions/checksums, grammar names/scopes and
license mapping. Rust uses MIT, TypeScript Apache-2.0, JSON the Sublime Packages
permissive license. Backend and complete bundled syntax notices are retained in
`core/licenses/highlighting/`, including dependencies embedded in the whole set.
No query files, HTML generation or themes are used.

The full syntax bundle is **959,011 raw bytes**. The optimized WASM qualification
binding is **2,698,711 raw / 1,379,603 gzip-9 bytes**, plus **4,725 raw / 1,472
gzip-9 bytes** of Node glue. These include a qualification-only JSON transport;
they are not a shipping browser worker inventory. Only the three named languages
are exposed. The full set is retained to preserve grammar cross-dependencies;
future subset work requires its own correctness/size evidence. These optional
costs do not fit the default Task cap and must remain outside that profile.
Dependency graph receipts prove their absence from editac-core and editac-wasm.
No new npm dependency/import or default profile asset was introduced.

A macOS 26.4.1 arm64 OS host (Apple A18 Pro, 8 GiB RAM), Rust 1.97.1 and
Node 24.19.0 executed the shared corpus. Optimized native first-tokenization times
were 26.92 ms Rust, 435.68 ms TypeScript and 3.28 ms JSON. WASM/Node first
calls were 40.31 / 186.59 / 1.94 ms respectively; module load was 8.63 ms.
One hundred warm samples per language are retained separately for each runtime
and native build profile. They qualify reproducible startup/work observations on
these small exact fixtures, not a responsiveness budget or a phone/UI envelope.
Cold TypeScript work is too expensive for a synchronous input handler. The
RCH-1.4 scheduler must isolate optional work and preserve immediate plain editing.
Native debug timings are diagnostic and must not be compared with release timings.

Plain fallback preserves every source byte and the original language label when
disabled, unknown, over input/run limits or on backend error; partial runs are
cleared. Initial admission caps are 100 KiB source, 16 KiB per line, 4096 lines and
16384 runs. These are resource caps, not measured worst-case time guarantees.
Malformed syntax remains literal and can still receive derived scopes. Successful
runs cover UTF-16 source offsets without splitting surrogate pairs; all source
remains immutable. No engine document, history, persistence, network or provider
operation occurs.

Incremental cache/revision/cancellation work belongs to RCH-1.3, browser scheduling
to RCH-1.4 and editing/IME-preserving rendering to RCH-1.5. Full workload/performance
qualification remains in RCH-1.20. No browser UI, native UI, other architecture,
phone, native/TUI presenter or release support is inferred from these probes.

See [the receipt](../evidence/highlighting-backend/receipt.json) for exact commands,
counts, raw samples, artifact/source hashes and preserved failed attempts. The
initial dependency-resolution failure was repaired by matching the workspace's
pinned serde versions. The first WASM runtime attempt failed before its cases
because CommonJS glue inherited an ESM package scope; an explicit generated
package setting repaired the harness. Its failed log remains intact.
