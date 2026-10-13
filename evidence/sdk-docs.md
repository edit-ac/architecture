# SDK integration and recovery examples

SDK-1.6 is implemented and verified at immutable roadmap snapshot `f25826744758a4d358c8cd675da4073dc3bcd11f976b91d8b8d2ed2dfac8b803`. Implementation is HEAD `f24b52043e4b7b429d81da0f2a2371635c332475` plus the dirty source hashes in the [receipt](../../evidence/sdk-docs/iteration3/receipt.json). No publication, deployment or paid inference occurred.

The public [integration guide](../../core/docs/integration.md) and getting-started links point to shipped plain-browser, React and Astro static/SSR entries. They document package names, async loading, explicit WASM hosting/CSP, task/literal paste, local and remote status separation, host auth/uploads, cleanup, recovery exports and supported-format/native limitations. Astro uses one shared SDK with no React runtime. Content migration remains deferred under its separate activation gate.

The documentation checker reuses the packed-consumer harness but compiles the actual public sources from four installed tarballs. It exercises real WASM, IndexedDB, typing/selection, literal paste, offline identity/content recovery, read-only hosts, ClientRouter navigation and visible failed-save/load controls. Prepared journal and opening failures never call external providers. Downloaded disposal reports retain unsaved byte data across plain/React cleanup and Astro navigation; this is not a qualified recovery-file import or device test.

## Verification

- `npm run build`: exit 0 under Node 24.19.0.
- `node --test --test-reporter=tap tests/docs-examples.test.mjs`: exit 0, 34/34, zero failures/skips/cancellations. Includes 30 browser cases and four package/type/SSR/guide checks; all 14 pack/install/build/type/SSR/archive commands pass.
- `npm run check:astro`: exit 0, 3/3 with pinned static/SSR builds and server checks.
- `npm run test:browser -- sdk --test-reporter=tap`: exit 0, 12/12 across three engines.
- Astro lifecycle regression: initial 36/42 passed; six assertions counted the new host save-status label globally. Scoped them to `edit-ac-editor` hosts, preserving the duplicate-SDK-status condition. The exact failed-name rerun passes 6/6, zero failures/skips/cancellations; unchanged 36 passing cases are reused. Final unique Astro coverage is 42/42.
- `git diff --check` for changed tracked paths: exit 0. Prior SDK-1.4 232/232 unfiltered baseline evidence remains valid; Rust/core/web semantic source is unchanged by this task.

The final combined result is 91 unique checks passed, zero remaining failures/skips. Full logs, tarballs, hashes, generated consumer archives, recovered byte reports and failed evidence live beside the receipt. Earlier Node 26.4.0 failed the pin guard without executing feature cases. The first pinned run's 15 download-path/caret failures are retained and superseded by the repaired complete run.

Exact candidates: React/DOM 19.3.0, Astro 7.3.8, Node adapter 11.1.7, Node 24.19.0, npm 11.17.0; Chromium 156.0.8078.4, Firefox 157.0, WebKit 27.2. These establish automated integration mechanics only; no physical Safari/mobile/native, performance, remote-settlement or release claim follows.

## Teardown

[Cleanup evidence](../../evidence/sdk-docs/iteration3/cleanup.json) confirms 89 recorded PIDs exited, 72 recorded ports closed and both isolated consumer roots removed. Archived this session's compiled Astro fixture consumers, then removed only `core/examples/astro/dist-static` and `dist-ssr` (8,256,041 logical bytes). Other tasks/services, source and qualification evidence remain preserved. About 8.27 GiB remains free. Preserved cleanup candidates: pre-existing `core/target` 11 GiB, root `node_modules` 218 MiB, example `node_modules` 71 MiB. Expanding cleanup requires separate user approval.
