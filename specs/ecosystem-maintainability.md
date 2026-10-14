# Maintainable ecosystem contracts

Qualification amendment (user decision, 2026-10-14): Named target-platform simulators/emulators and desktop OS VMs/test hosts may satisfy platform and release gates when physical hardware is unavailable. Follow the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms) for required runtime checks, tested virtual equivalents for hardware-only observations, counts and physical/virtual provenance. Earlier physical-only/manual-only wording in this document is superseded. This changes accepted evidence, not required implementation or correctness.

Status: planned strengthening of the existing Rust-first architecture. This is a set of executable boundaries, not a new framework or runtime.

## Dependency direction and ownership

| Layer | Owns | May depend on | Must not import |
|---|---|---|---|
| Semantic engine | Schema, identity, prepared commands, anchors, incremental patches | Qualified CRDT and small deterministic primitives | DOM, OS UI, HTTP, host auth, MCP, cloud SDK, PDF/layout/highlighting runtime |
| Portable companions | Session/recovery, Markdown reconciliation, diff, extension descriptors | Engine contracts and explicit store/transport ports | A second authoritative document or platform globals |
| Optional services | Highlighting, conversion, link resolution, security profiles | Bounded snapshots/patches and declared host ports | Direct mutable engine internals or ambient credentials |
| Client adapters | Web/native/TUI input, view, permissions UI, file pickers | Public portable contracts and optional providers | Another platform's renderer or duplicated semantic policy |
| Reference cloud host | Membership/catalog, durable updates/assets, receipt service | Versioned wire and storage ports | Client UI or authority inferred from document content |
| Public docs/demo | Learning material and packed SDK consumers | Immutable public artifacts and release profiles | Private workspace imports or a second editor implementation |

A cloud host may run all service boundaries in one process. Split deployment only for measured operational need. Share deterministic contract fixtures, not cross-repository source aliases. Keep the existing three npm SDK boundaries until an independently consumed optional package earns a separate release surface.

## One compatibility and capability vocabulary

Define a small versioned `contracts/capabilities.schema.json` and `contracts/profiles/` registry in core. It records semantic schema, update/sync profile, extension descriptor versions, FFI/API version, source dialect, converter direction/fidelity, platform and qualified resource envelope. Each entry references immutable implementation/package and evidence revisions. These files describe versions; document content cannot install providers or enable privileged operations.

Distinguish available, enabled, authorized and qualified capabilities. Permission and principal-specific availability remain runtime host answers, never trusted from imported documents or peer advertisements. Fail unsupported writes explicitly and preserve bounded unknown data for reads/copy/export where possible.

Avoid parallel inventories: adapt existing `native/<platform>/capability.json` and release-profile checks to the shared schema, then generate public support tables and demo controls from the same reviewed release record. Manual qualification evidence remains explicit; a generated green table cannot manufacture it.

### Profile producer and consumer boundary

`core/contracts/profiles/producers.json` is the reviewed build-time producer list.
Native `capability.json` files use the shared capability schema. Preparation
receipts are observations with their original scope, counts, input hashes and
physical/virtual provenance; a passing preparation receipt cannot admit SDK
support. Source drift remains visible and never upgrades an observation.

`core/scripts/release-profile.mjs` emits one content-addressed JSON record for
docs, demo and cloud. Its profiles retain the exact implementation/package,
version tuple, producer hash and evidence identities. Static authorization stays
null. Consumers pin the entire record's SHA-256 from their reviewed distribution
channel; neither this record nor its digest grants current host permission.

Native support admission requires a separate reviewed owning-platform policy and
receipt, bound to the profile's implementation, versions, platform and input
identities. The policy names required capability cases and packaged artifacts;
every required case must pass directly on the named target runtime or through a
linked, executed virtual equivalent. Nonzero exact counts, no failures/skips,
matching artifact hashes and capability-scoped evidence are mandatory. Accepted
provenance is physical-device, simulator, emulator, VM or OS host as appropriate
to the claimed platform. Prepared transports exercise this admission contract
only. Pending producers remain pending until their owning SDK qualification is
reviewed; admission does not publish a release or establish resource budgets.

## Asynchronous service contracts

Every heavy service uses bounded inputs, stable document/session identity, expected revision or content hash, cancellation, deadline and a typed result. Apply only after permission and revision revalidation. Dispose workers/subscriptions and discard stale results. Highlighter spans, link metadata and conversion previews are derived caches; they cannot become competing writable state.

Set per-service concurrency, byte/item/decompression/pixel/depth limits, queue admission and recovery behavior. Measure preparation, transfer, apply and rendering separately. Worker execution does not remove copy cost or UI layout cost. Do not run expensive work merely because an unrelated block changed.

### Bounded derived-work lifecycle

`core/contracts/services.json` records actual versus pending highlight, asset,
resolver and conversion registrations. The session companion's
`service_lifecycle` module and browser `services/lifecycle.ts` share document,
session, revision and transient permission identity checks. Hosts provide a
monotonic deadline, bounded byte/item counts, cancellation and reviewed per-port
concurrency/queue limits. Check identity/permission before provider invocation,
after completion and immediately before consuming a ready result. A ready
result is derived data, never a semantic commit or durability acknowledgment.

Admission is FIFO with explicit saturation/resource rejection. Every admitted
request has one terminal outcome. Cancellation, deadline and disposal settle
callers even when a provider ignores abort; its active slot remains occupied
until provider termination, preventing unbounded replacement work. Queued work
is removed on cancellation/invalidation without invoking its provider. Hosts
own actual worker termination and feature-specific output, decompression,
pixel/depth and content limits; this envelope cannot manufacture those proofs.
Durable journal acknowledgments remain owned by the store/session and survive
derived-work invalidation.

The production reference lookup and legacy resolver presenter both use this
boundary. The lookup keeps its existing query/target/catalog limits, aborts
superseded work, bounds noncooperative searches to two occupied slots and
revalidates scope before inserting a selected target. Presenter revisions follow
the selected-node subscription, preserving stable anchors across unrelated edits. Pending families have
prepared contract providers only. Their owning tracks must register and test
real adapters before optional-feature runtime qualification; synchronous image
URL policy and Markdown preparation do not count as asynchronous providers.
`node scripts/check-architecture.mjs --suite service-lifecycle` checks shared
scope vectors, queue/cancellation/deadline behavior, the real lookup adapter and
actual Rust session acknowledgment preservation without network/provider calls.

## Compatibility and release maintenance

Test exact supported previous/current combinations for schema, wire, extension descriptors, public JS/Rust APIs and native ABI. Reject unsupported versions with actionable recovery/export options. Upgrade and rollback fixtures must account for persisted data; reverting a package alone does not reverse a schema migration.

Build consumers from packed/released artifacts on clean workspaces. Check imports and Cargo feature graphs so disabled optional services and heavy dependencies do not enter minimum clients. Pin executable tooling/fixtures, retain licenses/notices and check known advisories at release without claiming that a clean advisory scan proves safety.

Keep dependency choices in short decision records with verified API, target, license, bundle and maintenance evidence. The choice gate must block on missing evidence, not silently choose an unqualified substitute. Avoid invented universal provider interfaces: the common ports are the actual repeated session, asset, resolver, conversion and lifecycle contracts.

## Performance, accessibility and diagnosis

Use the existing verification envelope plus feature-specific fixtures from roadmap25. Capture raw p50/p95/p99, long tasks, incremental invalidation size, memory plateau, active worker count and cold/lazy load bytes. Set reviewed release limits before advertising a profile; do not silently raise them after a failed run.

Require keyboard, touch, screen-reader and non-drag pointer paths where relevant. Platform appearance can differ while semantic capability remains test-equivalent. Record real device/OS input separately from deterministic fixtures.

Observability records bounded operation IDs, error codes, queue/durability state and timings. Redact document text, titles, URLs with credentials, tokens and keys. No live LLM/provider calls or synthetic paid inference are necessary for architecture fitness checks.

## Mobile web overhead boundary

[Mobile web](mobile-web.md) freezes an incremental baseline allocation within the [gzip bundle hard caps and preferred sizes](verification.md#browser-bundle-size-budgets); MWB-1.9 and MWX-1.8 own packed baseline/disabled/enabled cost evidence. FIT loading and budget checks consume these receipts where the mobile profile is claimed. The engine remains platform-neutral, optional APIs/dependencies load on demand, idle work is event-driven and per-frame geometry work is bounded. Budget failures require decomposition while preserving essential accessible editing; any hard-cap change requires an explicit user-approved budget decision.

## Editing boundary fitness

Track 42 tests [fourteen regression guards](editing-regression-suite.md) at existing command, input, renderer, history, normalization and lifecycle boundaries. Compound preparation, resulting selection and post-transaction notification are explicit capability gates; existing separate primitives cannot be silently composed into a purportedly atomic edit. Reuse production public boundaries with test-only instrumentation, maintain independent oracles and keep the harness out of shipped SDK bundles.
