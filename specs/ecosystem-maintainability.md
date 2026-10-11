# Maintainable ecosystem contracts

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

## Asynchronous service contracts

Every heavy service uses bounded inputs, stable document/session identity, expected revision or content hash, cancellation, deadline and a typed result. Apply only after permission and revision revalidation. Dispose workers/subscriptions and discard stale results. Highlighter spans, link metadata and conversion previews are derived caches; they cannot become competing writable state.

Set per-service concurrency, byte/item/decompression/pixel/depth limits, queue admission and recovery behavior. Measure preparation, transfer, apply and rendering separately. Worker execution does not remove copy cost or UI layout cost. Do not run expensive work merely because an unrelated block changed.

## Compatibility and release maintenance

Test exact supported previous/current combinations for schema, wire, extension descriptors, public JS/Rust APIs and native ABI. Reject unsupported versions with actionable recovery/export options. Upgrade and rollback fixtures must account for persisted data; reverting a package alone does not reverse a schema migration.

Build consumers from packed/released artifacts on clean workspaces. Check imports and Cargo feature graphs so disabled optional services and heavy dependencies do not enter minimum clients. Pin executable tooling/fixtures, retain licenses/notices and check known advisories at release without claiming that a clean advisory scan proves safety.

Keep dependency choices in short decision records with verified API, target, license, bundle and maintenance evidence. The choice gate must block on missing evidence, not silently choose an unqualified substitute. Avoid invented universal provider interfaces: the common ports are the actual repeated session, asset, resolver, conversion and lifecycle contracts.

## Performance, accessibility and diagnosis

Use the existing verification envelope plus feature-specific fixtures from roadmap25. Capture raw p50/p95/p99, long tasks, incremental invalidation size, memory plateau, active worker count and cold/lazy load bytes. Set reviewed release limits before advertising a profile; do not silently raise them after a failed run.

Require keyboard, touch, screen-reader and non-drag pointer paths where relevant. Platform appearance can differ while semantic capability remains test-equivalent. Record real device/OS input separately from deterministic fixtures.

Observability records bounded operation IDs, error codes, queue/durability state and timings. Redact document text, titles, URLs with credentials, tokens and keys. No live LLM/provider calls or synthetic paid inference are necessary for architecture fitness checks.
