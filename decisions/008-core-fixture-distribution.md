# Separate production core and fixture distributions

Status: Proposed; awaiting adoption. Owner: WSD-1.2; implementation owner: WSD-2.1.
Date: 2026-10-29.

## Decision and adoption gate

Recommend a separate private **`@edit-ac/core-test-support`** distribution for the
foundation fixture. Freeze the layout below for WSD-2.1, subject to an explicit
controller/user adoption reference approving the two removed core exports, the
consumer migration and the generated-wrapper identity trade-off below. There is
no adoption reference yet. Completing WSD-1.2 delivers this proposal only; it does
not adopt an API change, authorize implementation, publication, another runner,
or renew size-tuning time. Both packages retain `private: true`, `type: module`,
version `0.0.0` and license `Apache-2.0` until a separate release decision.

This boundary changes npm installation contents. It preserves production loading,
comparison, extensions, links and all their declarations. Fixture tests must still
instantiate the actual `foundation-fixture` Wasm, never a stub or production Wasm.
No new kernel, engine-wrapper implementation or compatibility alias is proposed.

## Retained baseline

The authenticated archive is
`core/.artifacts/wex-production-repair-20261028/inventories/default-task/edit-ac-core-0.0.0.tgz`
(workspace-relative), SHA-256
`2ea46027b39f0e39a30224617a895dc2a9e3e57598666069d357b16c2f662035`.
All 75 file entries equal current `core/packages/core/` bytes, including metadata.
The archive is 1,733,053 bytes compressed / 6,499,669 unpacked bytes.
The six fixture entries are:

| Archive path (under `package/`) | Unpacked bytes |
| --- | ---: |
| `dist/fixture.js` | 2,210 |
| `dist/fixture.d.ts` | 2,206 |
| `dist/wasm-fixture/editac_wasm.js` | 28,362 |
| `dist/wasm-fixture/editac_wasm.d.ts` | 6,754 |
| `dist/wasm-fixture/editac_wasm_bg.wasm` | 2,671,326 |
| `dist/wasm-fixture/editac_wasm_bg.wasm.d.ts` | 3,650 |
| Total | 2,714,508 |

Fixture Wasm SHA-256:
`d98ae3c5ecc68e73ce3935b1c77fda2d0b740fbe312ff7c41ff963bba2e59df5`.
These are retained inventory values, not measured savings. Changed manifests and
README bytes affect unpacked totals; paired actual packs are required to measure
compressed differences. Tar compression is not additive. Browser-cap failures
remain unchanged by moving unrequested fixture payload.

## Exact export maps

The current `@edit-ac/core` map is:

```json
{
  ".": {
    "types": "./dist/index.d.ts",
    "import": "./dist/index.js",
    "default": "./dist/index.js"
  },
  "./comparison": {
    "types": "./dist/comparison.d.ts",
    "import": "./dist/comparison.js",
    "default": "./dist/comparison.js"
  },
  "./comparison/wasm": "./dist/comparison-wasm/editac_comparison_wasm_bg.wasm",
  "./wasm": "./dist/wasm/editac_wasm_bg.wasm",
  "./fixture": {
    "types": "./dist/fixture.d.ts",
    "import": "./dist/fixture.js",
    "default": "./dist/fixture.js"
  },
  "./fixture/wasm": "./dist/wasm-fixture/editac_wasm_bg.wasm",
  "./extensions": {
    "types": "./dist/extensions/index.d.ts",
    "import": "./dist/extensions/index.js",
    "default": "./dist/extensions/index.js"
  },
  "./links": {
    "types": "./dist/links/index.d.ts",
    "import": "./dist/links/index.js",
    "default": "./dist/links/index.js"
  }
}
```

The proposed production `@edit-ac/core` map is exactly:

```json
{
  ".": {
    "types": "./dist/index.d.ts",
    "import": "./dist/index.js",
    "default": "./dist/index.js"
  },
  "./comparison": {
    "types": "./dist/comparison.d.ts",
    "import": "./dist/comparison.js",
    "default": "./dist/comparison.js"
  },
  "./comparison/wasm": "./dist/comparison-wasm/editac_comparison_wasm_bg.wasm",
  "./wasm": "./dist/wasm/editac_wasm_bg.wasm",
  "./extensions": {
    "types": "./dist/extensions/index.d.ts",
    "import": "./dist/extensions/index.js",
    "default": "./dist/extensions/index.js"
  },
  "./links": {
    "types": "./dist/links/index.d.ts",
    "import": "./dist/links/index.js",
    "default": "./dist/links/index.js"
  }
}
```

The new `@edit-ac/core-test-support` map is exactly:

```json
{
  ".": {
    "types": "./dist/fixture.d.ts",
    "import": "./dist/fixture.js",
    "default": "./dist/fixture.js"
  },
  "./wasm": "./dist/wasm-fixture/editac_wasm_bg.wasm"
}
```

`types` stays `./dist/index.d.ts` in core and is `./dist/fixture.d.ts` in
test-support. Core `sideEffects` becomes `["./dist/wasm/**"]`; support uses
`["./dist/wasm-fixture/**"]`. Keep other current production metadata unchanged.
No fixture shim remains in core: a re-export would require installing the support
payload in production. Removal is intentionally gated on adoption before the
first public editor contract, rather than silently breaking a declared export.

## Exact file allowlists

Replace core's broad `files: ["dist", ...]` with this finite list. The 65 dist files
retain every current non-fixture entry, including comparison identity, both Wasm
declarations and the runtime/glue pair. No wildcard admits future instrumentation
or stale fixture output. npm also includes `package.json`; it is the only extra
expected archive file. The [npm 11 files contract](https://docs.npmjs.com/cli/v11/configuring-npm/package-json/#files)
also includes README/license metadata; compare the final archive's complete file
set, rather than assuming `files` alone proves exclusion.

Production `files`:

```json
[
  "dist/command-target.d.ts",
  "dist/command-target.js",
  "dist/comparison-contract.d.ts",
  "dist/comparison-contract.js",
  "dist/comparison-identity.json",
  "dist/comparison-wasm/editac_comparison_wasm.d.ts",
  "dist/comparison-wasm/editac_comparison_wasm.js",
  "dist/comparison-wasm/editac_comparison_wasm_bg.wasm",
  "dist/comparison-wasm/editac_comparison_wasm_bg.wasm.d.ts",
  "dist/comparison.d.ts",
  "dist/comparison.js",
  "dist/engine.d.ts",
  "dist/engine.js",
  "dist/extensions/ai-actions.d.ts",
  "dist/extensions/ai-actions.js",
  "dist/extensions/ai-session.d.ts",
  "dist/extensions/ai-session.js",
  "dist/extensions/ai.d.ts",
  "dist/extensions/ai.js",
  "dist/extensions/assistive-input-session.d.ts",
  "dist/extensions/assistive-input-session.js",
  "dist/extensions/assistive-input.d.ts",
  "dist/extensions/assistive-input.js",
  "dist/extensions/code.d.ts",
  "dist/extensions/code.js",
  "dist/extensions/conversions.d.ts",
  "dist/extensions/conversions.js",
  "dist/extensions/evolution.d.ts",
  "dist/extensions/evolution.js",
  "dist/extensions/index.d.ts",
  "dist/extensions/index.js",
  "dist/extensions/profiles.d.ts",
  "dist/extensions/profiles.js",
  "dist/extensions/registry.d.ts",
  "dist/extensions/registry.js",
  "dist/extensions/search.d.ts",
  "dist/extensions/search.js",
  "dist/extensions/transfer.d.ts",
  "dist/extensions/transfer.js",
  "dist/index.d.ts",
  "dist/index.js",
  "dist/links/activation.d.ts",
  "dist/links/activation.js",
  "dist/links/catalog.d.ts",
  "dist/links/catalog.js",
  "dist/links/contract.d.ts",
  "dist/links/contract.js",
  "dist/links/index.d.ts",
  "dist/links/index.js",
  "dist/links/locator.d.ts",
  "dist/links/locator.js",
  "dist/links/policy.d.ts",
  "dist/links/policy.js",
  "dist/links/presenter.d.ts",
  "dist/links/presenter.js",
  "dist/links/scope.d.ts",
  "dist/links/scope.js",
  "dist/reviewed-conversion.d.ts",
  "dist/reviewed-conversion.js",
  "dist/wasm/comparison-identity.js",
  "dist/wasm/editac_runtime.js",
  "dist/wasm/editac_wasm.d.ts",
  "dist/wasm/editac_wasm.js",
  "dist/wasm/editac_wasm_bg.wasm",
  "dist/wasm/editac_wasm_bg.wasm.d.ts",
  "README.md",
  "LICENSE",
  "THIRD-PARTY-NOTICES.txt"
]
```

Support `files` (14 dist files plus metadata):

```json
[
  "dist/command-target.d.ts",
  "dist/command-target.js",
  "dist/comparison-contract.d.ts",
  "dist/comparison-contract.js",
  "dist/engine.d.ts",
  "dist/engine.js",
  "dist/fixture.d.ts",
  "dist/fixture.js",
  "dist/reviewed-conversion.d.ts",
  "dist/reviewed-conversion.js",
  "dist/wasm-fixture/editac_wasm.d.ts",
  "dist/wasm-fixture/editac_wasm.js",
  "dist/wasm-fixture/editac_wasm_bg.wasm",
  "dist/wasm-fixture/editac_wasm_bg.wasm.d.ts",
  "README.md",
  "LICENSE",
  "THIRD-PARTY-NOTICES.txt"
]
```

The eight shared output files are the four `.js`/`.d.ts` pairs for
`engine`, `command-target`, `comparison-contract` and `reviewed-conversion`.
`fixture.js` imports engine and command-target; engine imports reviewed-conversion;
engine's declarations reference comparison-contract. The other declaration edges
return to engine. This complete small closure avoids a hidden deep import from
core or a new public raw-engine adapter API. Support contains neither production
Wasm nor comparison Wasm. No dependencies or peer dependencies are needed for this
self-contained support distribution; production packages must not depend on it.

## Source and build ownership

`core/packages/core/src/{fixture,engine,command-target,comparison-contract,reviewed-conversion}.ts`
remain the only authored wrapper sources. Keep the current core TypeScript build
as their sole compiler. Do not copy authored TypeScript into a new package or
fork `EngineHandle`, error handling, restore validation or command-target logic.

Add authored metadata at `core/packages/core-test-support/package.json` and a
fixture-specific README there. Keep it outside the root's explicit npm workspace
list; pack it by directory path. Its generated `dist`, LICENSE and notices are
ignored outputs copied from canonical producers, not a second implementation.
One proposed `core/scripts/stage-core-test-support.mjs` owns copying precisely the
14 support dist files and license/notices, validating the complete closure and
writing an input/hash manifest under ignored task output. It must fail on a
missing/stale input rather than silently using another build. Require the same
source/build binding for core and support wrapper bytes and record their hashes.

`core/scripts/build-wasm.mjs --fixture` remains the sole fixture-Wasm producer:
`editac-wasm`, browser profile, `--no-default-features --features foundation-fixture`,
locked/offline `wasm32-unknown-unknown`, pinned wasm-bindgen 0.2.129 web output.
It continues to write `packages/core/dist/wasm-fixture`; production writes
`packages/core/dist/wasm`. Do not reroute fixture output over production. Local
dist retains fixture files for source tests and existing prerequisite pins; only
the production archive excludes them. Do not delete live dist to achieve exclusion.

After adoption, the explicit preparation sequence is production/fixture generation
under their existing authority, core TypeScript build, support staging, then local
`npm pack --workspace @edit-ac/core` and `npm pack ./packages/core-test-support`
into ignored output. No pack/install lifecycle hook compiles, fetches credentials
or starts a browser. Tests install support explicitly as a development dependency;
production size preparation and production packed consumers install core only.
An existing valid producer receipt may replace generation only for its bound inputs.

Generated copies preserve wrapper behavior and structural types but are separate
ES module instances across the two package URLs. Today core and fixture share
`EngineError`/function object identity in one dist directory. The proposed support
runtime's error class is its own export; consumers must use its own `EngineError`
for `instanceof`, and must not mix module-local handles/tokens across runtimes.
The traced fixture consumers do not assert cross-package identity. Approval of
this explicit private-test boundary is part of adoption; WSD-2.1 must not silently
add a raw-engine production export or redesign packaging to hide the trade-off.
If cross-package identity is required, return for a revised decision before edits.

## Consumers and exact migration

| Current consumer or reference | Classification and adopted action |
| --- | --- |
| `core/tests/wasm-load.test.mjs:86` | The only executable bare fixture specifier found: `import.meta.resolve('@edit-ac/core/fixture/wasm')`. Resolve `@edit-ac/core-test-support/wasm` instead; assert the support package path. No current executable bare import of the fixture JS entry was found. |
| `wasm-load.test.mjs` setup, `loadFixture`, retry/Unicode/peer-update/negative-production cases | Real fixture users through `/built/fixture.js` and `/packed/fixture.js`; pack/install support as well as core. Serve built fixture routes from staged support dist and packed routes from installed support dist; use explicit `/built-core/` and `/packed-core/` routes for production SSR/assets. Read supplied fixture bytes from support and compare to canonical fixture producer. Migrate all these routes together, including production-Wasm rejection input and `facts.pack` fixture-membership assertion. Keep production metadata/export assertions on the core pack; assert fixture membership on a separate support pack fact. |
| `core/tests/browser-size.test.mjs:50–61` | Real direct local fixture file/import check; retain its canonical local dist paths and fixture-export assertions. It proves feature separation, not pack exclusion. Do not replace fixture bytes with production or remove its negative production-root checks. |
| `core/tests/packed-consumers.test.mjs` | `/fixture/editor.mjs`, `/fixture/react-built.mjs`, and `/fixture/wasm/` are served example namespaces, not fixture-runtime imports. They copy production core `dist/wasm` and call production `init`. Keep these routes/imports and the core/web/react/astro/markdown pack list; do not add support to production consumers. |
| `core/scripts/prepare-browser-size.mjs` | Packs production core/web/(Markdown), imports core root, copies production `dist/wasm` and rejects fixture exports. Keep production-only behavior and original fixture-baseline diagnostic restriction. No support input or budget credit. |
| `core/packages/core/README.md:94–107`; `architecture/specs/packages-release.md` foundation-probe paragraph | Declared fixture API documentation: replace both old specifiers with the support root/wasm exports and explicit build/staging/pack instructions. Keep `initFixture`, `FixtureRuntime`, fixture diagnostics and trusted-update warning. Support README owns the full recipe; production README links it. |
| `core/scripts/verify-prerequisite-qualification.mjs`; `core/tests/native/table-session-proof/qualify-current.py` | Local fixture-path prerequisite and explicit build-before-pack orchestration, not new package imports. Canonical local output is retained, so no path rewrite or native run is needed. Future qualification must report actual separate pack identities; never relabel old receipts. |
| `core/licenses/{policy,inventory}.json` | Current fixture artifact and core-tar member coverage. Preserve canonical source-path coverage; after adoption add current support distribution records and regenerate ignored inventory with current packs, preserving historical distribution records. Old qualification hashes remain historical evidence, not current pack proof. |
| `core/contracts/layers.json`; compatibility policy, loading IMQ record and native STB runtime snapshots | Source ownership/pins or historical fixture copies, not active npm consumers. Keep canonical fixture source/import ownership and all immutable history. Do not migrate/rebuild snapshots to make new packs match them. |

Literal searches cover the current tracked/unignored `core`, `cli`, `docs` and
`architecture` trees. They establish repository consumer coverage, not absence of
unknown external users. Exact source pins and full matching lines are in the
WSD-1.2 ignored static evidence. Findings are bound to those inputs.

## License coverage

Retain the complete existing `core/packages/core/LICENSE` and
`THIRD-PARTY-NOTICES.txt` in production; this decision authorizes no truncation or
notice deduplication. Support stages the same Apache-2.0 project license and the
full locked-Wasm notices, covering the copied JS wrappers and the fixture binary.
`core/crates/editac-wasm/Cargo.toml` declares `foundation-fixture = []`,
which currently adds no dependency, so the fixture uses the
same normal/build dependency closure as core. Verify that against the actual
selected feature graph at implementation time; if closure changes, add notices
before packing, never infer coverage from a smaller production manifest.

The canonical `core/scripts/build-wasm-notices.mjs` owns notice generation (locked,
offline Cargo metadata/tree, normal/build edges, vendored path dependencies and
the pinned Yrs 0.28.0 MIT fallback). Support staging copies its output; there is no
second license generator. Include the fixture artifact in `licenses/policy.json`
under a new current support distribution record while retaining local artifact provenance
and historical distribution records. The existing policy fixture hash
`1f50ea2d21a3b169e8dac0ec993a1f49ddee5ff97f80a5837a48aeab42cca0eb`
is historical and differs from the retained fixture hash above; its qualification
cannot be reused for these bytes. Add current pins/coverage under the existing
license owner, and regenerate ignored/derived inventory without rewriting old proof. Neither
archive may omit notices or claim license qualification from this static proposal.

## WSD-2.1 migration, verification and rollback

1. Record adoption of this exact map, source-copy ownership and identity trade-off;
   obtain released checkout/build ownership. Freeze input/source pins. The likely
   implementation touches more than eight files once documentation and license
   distribution policy are included: controller-split preparatory metadata/staging
   from the atomic export/consumer cutover before dispatch, preserving WSD-2.1's
   original acceptance. No independent new parent or unchecked requirement is added.
2. Add support metadata/README and deterministic staging. Preserve canonical source
   and local fixture output. Stage real fixture files plus the eight shared outputs
   from one bound build. Keep generated packages and tarballs ignored.
3. In the atomic cutover, narrow production `files`, remove only the two fixture
   exports/fixture sideEffects pattern, migrate wasm-load's real consumers and
   update the two declared API documents and add current license distribution coverage.
   Do not change packed example routes, production size preparation or snapshots.
4. Under WSD-2.1's permitted phase, inspect complete paired pack inventories, resolve
   all six production exports and their declarations from an isolated installed
   tarball, and resolve both support exports. Run the existing fixture behavior
   checks against actual installed support Wasm, retaining initialization/retry,
   Unicode/UTF-16, peer-update/free behavior and rejection of production Wasm.
   Inspect setup before execution: wasm-load packs/installs and launches Chromium;
   packed-consumers additionally builds framework examples and starts three browser
   engines. Freeze only affected selectors; comprehensive coverage stays source 06.
5. Report actual before/after compressed tgz and unpacked bytes separately, complete
   executed/passed/failed/skipped counts, and missing/failed gates. Preserve the
   original browser-cap failures. This proposal executes none of those checks.

Rollback before publication is one owned source unit restoring the previous core
manifest `files`, fixture exports and sideEffects, wasm-load pack/route assertions,
API docs and newly added current license distribution mapping. Regenerate only task-owned staging
from canonical producers, restore the core tarball layout and rerun invalidated
focused checks under current authority. Remove the newly introduced support
metadata/staging only after checking no active consumer uses it. Keep source,
local fixture Wasm, failed evidence and immutable snapshots. No Git reset/stash,
blind deletion, registry publication or data conversion belongs to rollback.

## Static completion and pending work

WSD-1.2 completes when both maps, the 65-production/14-support dist allowlists,
all six fixture files, every found actual fixture consumer, producer ownership
and license/migration/rollback boundaries are cross-checked against the pinned
inputs. Static review cannot prove a packed installation executes, savings, runtime
quality or license qualification. Those remain WSD-2.1 and existing final owners.
Adoption remains pending with the controller/user; do not dispatch its dependent
cutover until an explicit reference approves this decision. WSD-1.3 remains
independent. No optimization seconds or hypotheses were consumed.
