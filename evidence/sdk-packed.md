# Packed SDK consumer qualification

SDK-1.4 is implemented and verified locally, with private tarballs; no publication or deployment. Immutable source revision f2582674, core HEAD f24b520 plus the source snapshots in the [receipt](../../evidence/sdk-packed/iteration2/receipt.json).

One isolated installed-tarball harness qualifies native ESM/CSP with a separate CORS asset origin, React 19.3.0/SSR and Astro 7.3.8 static/SSR. Types/exports, Apache/third-party notices, one installed core owner, real WASM/IndexedDB editing, cleanup and Astro ClientRouter recovery pass: 15/15 checks, zero failures/skips. Build/WASM probes exit 0; the unfiltered baseline passes 232/232, zero failures/skips. Four tarballs, compiled consumers, exact commands/hashes and repaired failures are retained with the receipt.

No React is installed in the Astro consumer. No workspace aliases or symlinked SDKs are used. Physical-device/history-selection and footprint/performance/release qualification remain separate gates. SDK-1.6 integration/recovery guidance is the next parent; migration remains deferred.
