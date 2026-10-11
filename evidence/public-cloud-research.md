# edit-ac ecosystem readiness review

Reviewed 2026-10-11. This is a planning review, not implementation, deployment, security certification, or provider qualification. Scope: architecture README/requirements; client, storage, encryption and package contracts; roadmap gates06/08/10/12/19/20/24; the newly available rich-content25 contract. No infrastructure was provisioned and no paid/provider calls or repository publishing were performed by this review.

## Findings and concrete boundaries

1. **Public documentation needs a first-class ownership and release boundary.** `specs/packages-release.md:43` still restricts follow-ups to three repositories. SDK-1.6 (`08-sdk-integration.md:129`) delivers integration/migration examples and REL-1.8 assembles release docs; neither establishes a public docs repository, site versioning, navigation, deployment, or rollback. Update canonical repository ownership, requirements and the final release matrix when the docs repository is created. Keep architecture decisions in architecture, generated API truth in core artifacts, and reader-facing guides/site source in docs. Avoid duplicated hand-maintained API definitions.

2. **npm qualification does not establish a usable public demo.** REL-1.9 (`10-web-qualification.md:195`) checks registry installation and explicitly needs no production endpoint. DEL-1.8 qualifies client artifacts, not a publicly hosted editor. A demo needs an owned source/build/deploy path, an exact SDK artifact version, safe seeded content, visible capability/availability states, actual hosted-WASM checks, and a rollback procedure. A static deployment can serve the web editor; collaboration requires a separately qualified service. Do not imply that a prepared relay, screenshot, mocked provider, or localhost test establishes the public behavior.

3. **The existing cloud basis is contractual, not a production store.** `specs/storage-sync.md:29` and SYN-1.5 (`06-synchronization.md:107`) explicitly scope the current reference relay to loopback, prepared authorization and integration tests. CAP-1.3 supplies portable ports and CAP-1.4 local native persistence. Neither implements tenant-scoped cloud metadata, production credential verification, asset publication, retention, isolated restore, operator configuration or deployment operations. New track28 now supplies the bounded reference-host delivery plan.

4. **Revision and receipt semantics must stay separate.** CAP's content revision, catalog metadata revision, provider object ETag, update receipt and asset-finalization receipt represent different facts. HTTP conditional requests do not create a database transaction, and an uploaded object is not a committed document. The new cloud spec explicitly preserves distinct RCH asset/update receipts, allows pending asset descriptors without blocking local edits, and uses a publication record to join verified available assets, catalog effects and updates where an operation requires them. It never claims a distributed object-store/database transaction.

5. **Readiness claims need an evidence level.** Real local backend/fault/restore evidence qualifies the reference implementation only. A named configured provider, permissions, region, consistency settings, retention and topology need their own authorized evidence before a production claim. Protected envelope byte transport does not qualify E2EE: tracks19/24 and the final server/profile gate still apply. Missing provider or independent security evidence must block that claim while allowing unrelated implementation work.

## Bounded public docs follow-ups for the root plan

Each item should become a 15–45 minute parent with a named check; split before implementation if it exceeds that boundary.

| Boundary | Acceptance/check |
| --- | --- |
| Establish docs repo ownership and version map | Canonical repos, Apache license, contribution route and architecture/API/source boundaries agree; cross-repo links resolve |
| Bootstrap the static site | Pinned maintained dependencies, reproducible lockfile and a clean build; no live provider needed |
| Publish install and first document guide | Copyable example compiles against the exact packed/registry SDK artifact; initialization, WASM assets and teardown are real |
| Publish offline/recovery and authorization guide | Local commit, remote receipt, pending asset, denied write and recovery states match fixtures; no unsupported promise |
| Generate and link API reference | Rust/TypeScript source versions and generated anchors are recorded; unresolved symbols and broken links fail |
| Add feature/platform/profile matrix | Capabilities consume a versioned release manifest, distinguishing implemented, qualified, optional and unavailable states |
| Add migration and protocol compatibility pages | SDK/server/schema/profile compatibility is explicit; upgrade examples run against old/new prepared fixtures |
| Verify accessibility and navigation | Keyboard navigation, readable code, heading structure, search fallback and broken-link checks pass on built pages |
| Build previews safely | Public PR inputs cannot obtain deployment secrets; build artifacts carry source/package hashes and bounded expiration |
| Prepare production publication and rollback | Exact artifact/config/URL, owner, hosting requirements and prior release recovery are concrete before publishing |

## Bounded public demo follow-ups for the root plan

| Boundary | Acceptance/check |
| --- | --- |
| Establish a demo build using published artifacts | Clean consumer resolves declared versions without sibling source links; package/WASM hashes are captured |
| Deliver the local-first editor scenario | Seeded document edits, reload/reopen, export, history and recovery use real core APIs and deterministic content |
| Expose requested extension scenarios | Tables, code, assets and other qualified features are reachable; unavailable features explain their state without fake success |
| Demonstrate diffs and change review | Same portable change model and source/profile labels as SDK/native clients; keyboard/accessibility checks pass |
| Add optional hosted collaboration configuration | Endpoint, wire/profile capability and auth are explicit; no configured host means a truthful local mode |
| Apply public content/privacy policy | Isolated disposable examples, reset, retention, upload bounds and telemetry avoid real-user content exposure; auth required for any persistent shared store |
| Qualify the hosted browser envelope | Real deployed WASM MIME/CSP/cache/base paths, secure context, worker/font/assets, offline behavior and browser matrix pass; isolation headers are required only by actual features |
| Publish a versioned demo release | Recorded source/SDK/service/profile versions, public smoke evidence, operator ownership and rollback; no paid inference during validation |

## Cloud work added by this review

Created only these repository files:

- `specs/cloud-document-store.md`: deployable single-host boundary; identity/tenant policy; control plane/catalog; exact revision CAS; idempotency; transactional publication and distinct receipts; staged assets; bounded relay/limits; offline compaction/deletion barriers; exports/retention/purge; isolated backup/restore; fencing and declared scaling; redacted telemetry; signed deployment configuration; explicit reference/provider/public/encrypted evidence levels.
- `roadmaps/28-cloud-document-store.md`: 21 parent tasks, 63 total checkboxes, 50 local dependency edges. Whole-track prerequisites: `06-synchronization.md`, `12-client-contracts.md`, `25-rich-content-extensions.md`. Prefix `CLD`; implementation workspace `core`, host path `services/document-store/`, Cargo package `editac-document-store`. Each parent names its future integration test target and all runner-required metadata.

The reference service is one deployable initially. Drivers stay outside semantic core; ports do not leak provider SDK types. Select one real durable local backend during bootstrap and ship reusable conformance cases, rather than building many speculative adapters. Actual configured-cloud-provider evidence is a final release/profile obligation, not an implicit network test or provisioning request.

## Maintainability recommendations

- Use one versioned capability/evidence manifest for docs, demo, package releases, native platform support and service profiles. It records source/artifact revisions and evidence status; a page or demo checkbox must not promote an unqualified feature.
- Keep a small compatibility matrix for SDK/wire/schema/security profile/service adapter versions. Semantic-version strings alone cannot prove wire or storage compatibility.
- Give each backend adapter a common conformance harness for authorization, CAS, commit outcome, retry, receipts, restart, quota accounting, deletion barriers and restore. Keep provider-specific durability assumptions visible alongside it.
- Keep the operator surface proportional: one binary/service, one authoritative commit store, immutable blobs, explicit migrations and runbook. Introduce separate control/relay services only after a measured need and a transactional design review.
- Preserve bounded task checks and separate implementation evidence from release evidence. Broad cloud tasks such as restore or publication can require a controller split; the 15–45 minute rule must not become a reason to omit failure cases.

## Primary references checked

- [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html): permission checks apply to each action/resource.
- [OWASP multi-tenant security](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html): tenant context comes from verified identity/membership; caller-supplied tenant IDs are selectors, not authority.
- [OWASP WebSocket security](https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html): origin controls, session expiry and authorization remain relevant after connection establishment.
- [RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html#name-if-match): entity tags are opaque representation validators; conditional writes do not establish broader storage atomicity.
- [RFC8725](https://www.rfc-editor.org/rfc/rfc8725.html): JWT verification requires disciplined algorithm, issuer, audience and key handling; tenant membership remains application policy.
- [GitHub Pages overview](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) and [custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages): a static docs/demo hosting example, not a provider selection or evidence of a cloud document backend.

Validation at authoring time: official installed roadmap-runner0.8.0 `validateRoadmap` returned zero errors for the new track, with21 parents/63 checkboxes. The future Rust tests are planned and were not run: no host implementation exists yet. Validation log: `/private/tmp/edit-ac-cloud-validation.log`. No test servers, browsers, installs, or build outputs were created during this review.
