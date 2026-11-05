# Backend SDKs and framework adapters

Planning decision: 2026-10-24. The user requested extensive language SDK and framework-specific adapter planning after identifying the Laravel save/load integration gap. This is planned delivery, not a claim that these packages or endpoints exist. The [delivery index](../runner-queues/backend-sdk-adapters-20261024/README.md) owns scope, sequencing, acceptance mapping and deferred qualification.

## Product outcome

An application developer installs an editor binding and the matching backend package, connects application authorization and database storage, and gets canonical document create/load/save with honest save status. Collaboration is an explicit additional capability. A Laravel developer must not have to implement CRDT framing, checkpoint identity, deduplication, recovery or remote receipt matching from scratch.

Three independently declared capabilities define the product:

| Capability | Developer outcome | Required authority |
|---|---|---|
| Checkpoint persistence | Create, open, save, reopen and resolve concurrent save conflicts | Application database transaction, expected durable revision and canonical engine validation |
| Collaborative persistence | Append/replay incremental updates, synchronize, reconnect and retain pending work | Serialized document admission, update/operation ledger, outbox and covered durable receipts |
| Server document operations | Inspect, edit, merge or export semantic content on a backend | Existing Rust engine through the Rust library, a qualified binding, or a private companion service |

Checkpoint-only support must not advertise collaboration. A language HTTP client must not advertise a local editor or local semantic engine. Readiness manifests separately report language client, server middleware, storage adapter, transport, semantic bridge and UI host support.

## Existing authorities and delivery owners

Reuse [canonical durability](document-durability.md), [engine](engine.md), [storage/sync](storage-sync.md), [client contracts](client-contracts.md), [cloud store](cloud-document-store.md), [native parity](native-sdk-parity.md) and [one current format](../decisions/006-single-format-before-publication.md). The project is pre-alpha: require schema `editac.registry.editor` and profile `editac.yrs-yjs.editor`, with no `.v5` or other development-version suffix. Protocol 1, update encoding 1 and UTF-16 remain real wire/encoding discriminators with one supported value. HTTP package versions are not document-format identities. No alternate PHP/Go/Python schema, numbered production variants, runtime legacy reader, previous/current support matrix, silent migration or CRDT implementation is added.

BSC-1.1 records the existing core/Session cutover owner and exact acceptance; BSC-1.7 cannot pass against binaries or current fixtures still emitting the retired suffixed labels. Creation, restore, journal scope, sync and WASM/FFI/native consumers must all use the same unversioned tuple, with unsupported envelopes rejected before mutation. The cutover uses the existing coordinator at a safe checkpoint and preserves stored originals; no runtime alias or automatic database relabel is allowed. This planning clarification does not claim the implementation has already changed.

Tracks 03/06/12 own local storage and synchronization; track 28 owns the Rust durable authority and provider ports. Tracks 08/21 own browser composition and extensions. Tracks 09/16/17/18/22/23 own native preparation and editor surfaces. This plan consumes targeted implemented interfaces and contributes repairs to their owner; it does not repeat their entire roadmap or declare unchecked work completed. Actual target-runtime/device verification remains with track 43 through explicit new adapter case handoffs. Tracks 10/20/24/37 retain applicable release/security qualification. Their existing tasks are not presumed to cover an adapter that did not exist when their cases were written.

Keep the current web → features → alpha → native → docs → qualification → native tests → beta → integrations sequencing. This additive integration plan does not reprioritize the active queue, alter running snapshots, start a runner or authorize publication. Adoption uses the existing coordinator at a safe checkpoint, the guard and live readiness receipt. Correctness/API prerequisites block only consumers that actually require them; full unrelated roadmaps and publication are not development prerequisites.

## Package and ownership boundaries

Repository planning update, 2026-10-26: [Decision 007](../decisions/007-integration-repositories-and-packages.md) and the [integration distribution plan](integration-distribution.md) require a dedicated repository and installable distribution for each maintained language SDK and adapter, including PHP, Laravel, Filament and Drupal separately. The paths below describe current/staged implementation locations, not permanent ownership. Existing task IDs retain feature ownership; extraction and registry/listing readiness are separate follow-up acceptance at a safe coordinator checkpoint. No active source or running worker is moved by this amendment.

Planned implementation paths are core-relative: `sdk/contracts/`, `sdk/reference/`, `sdk/<language>/`, `adapters/backend/<framework>/`, `adapters/admin/<framework>/`, `adapters/cms/<framework>/`, `adapters/web/<framework>/`, `adapters/native/<platform>/`, `examples/sdk-adapters/`, and `scripts/sdk-adapter-delivery.mjs`. These are proposed paths, not existing implementation claims. Contract adoption first inventories current exports and maps these paths to reusable existing packages; preserve an established package rather than create an alias or competing implementation. Provisional package/distribution names must be settled before examples use them.

The boundaries are:

1. Shared authored HTTP/DTO/error contract and current-format fixture inputs. An OpenAPI description covers the HTTP resource operations; baseline CRDT sync frames and ephemeral awareness retain their own protocol contracts. A single DTO authority may produce reproducible local generated clients; generated output, caches, packed packages and reports stay ignored under the source-only policy. If a registry requires generated files, build them outside Git at packaging time.
2. Small idiomatic language SDKs: exact bytes, typed identities/errors/receipts, bounded HTTP transport, cancellation, commit lookup, and explicit retry policy. No implicit provider, server process or database connection on import.
3. Backend framework adapters: route registration, application identity/policy callbacks, validation bridge, transaction/repository ports and optional collaboration endpoint integration. Authentication remains the application's responsibility; credentials never enter document bodies or logs.
4. Storage drivers: migrations and transaction adapters for declared databases, independent of a framework ORM. A framework adapter may map the same port through Eloquent, SQLAlchemy, ActiveRecord, EF Core or Spring Data without inventing another save protocol.
5. Web/native host bindings: one engine/session per document lifetime, save-state observation, offline recovery and optional transport. UI and OS-specific ownership stay outside the semantic engine.

The minimal install must support checkpoint save/load without a WebSocket server, presence service, queue worker, object store or server-side editing module. Those capabilities are opt-in. They may require a separate Rust validation companion; that requirement must be explicit in the install recipe and capability manifest, never hidden in a package side effect.

### PHP SDK, Laravel wrapper and Filament

User clarification, 2026-10-24: PHP is a standalone SDK; Laravel is a small wrapper around that SDK. Filament admin support and the Drupal field module are optional adapters, not additional persistence implementations. Keep separate install boundaries (distribution names remain provisional):

| Package boundary | Owns | Dependency rule |
|---|---|---|
| `sdk/php/` | Framework-independent identity/byte/receipt types, transport, canonical validation bridge, repository/transaction interfaces, conditional commit orchestration, retries, commit lookup and optional append/resume | Works in plain PHP without Laravel, Illuminate, Filament or Livewire; optional PDO drivers remain SDK-owned |
| `adapters/backend/laravel/` | Service container/configuration, application policy/route hooks, Eloquent/connection transaction mapping, adapter table migrations and after-commit event wiring | Requires the PHP SDK and Laravel; delegates protocol and persistence orchestration to the SDK; installation does not require Filament |
| `adapters/admin/filament/` | Custom editor field, Blade/Alpine/browser asset bridge, Livewire field state/lifetime and Resource/action form recipes | Requires the Laravel wrapper and Filament; reuses the browser editor SDK and Laravel policy/storage wiring; optional for other Laravel consumers |
| `adapters/cms/drupal/` | Drupal module/services, configurable document field type, editor widget, safe display formatter, entity revision/translation and access/transaction mapping | Requires the standalone PHP SDK and Drupal; does not depend on Laravel or Filament; no independent CRDT, canonical decoder or receipt algorithm |

The PHP SDK owns the shared save algorithm for both framework-owned storage and delegated authority. Laravel adapts application services and storage callbacks to those interfaces; it does not decode a second envelope, validate a second schema or implement its own retry/receipt rules. Eloquent writes still use the application's actual database transaction and connection; adapting that transaction does not transfer commit ownership to a queued event. Symfony reuses the same PHP SDK rather than depending on the Laravel wrapper.

Filament uses its documented [custom field and field state extension points](https://filamentphp.com/docs/5.x/forms/custom-fields). This is an implementation reference, not a promise to maintain multiple Filament generations; select and declare one maintained Filament/Livewire baseline at implementation. Preserve field label/error/accessibility associations and correct nested state paths. Load editor assets on demand and keep editor-owned DOM/lifetime stable across Livewire updates, modal opens/closes, repeaters and navigation. No hydration/dehydration or component rerender may re-import text, reset document lineage, create another writer or acknowledge a save.

Bind a compact document reference, expected durable revision and explicit form state to Livewire; do not entangle/retransmit the full binary document on every keystroke. Canonical content travels through the PHP SDK/Laravel save boundary. Create/edit/read-only modes and new-record draft ownership are explicit. Default submit integration coordinates the editor flush barrier and model association through the configured SDK transaction boundary. If independent autosave is enabled, declare its document commit separately from the enclosing form/model save: canceling a modal or failing another form field cannot be presented as undoing an already committed document. A dehydrated field value or successful Livewire request is never a remote-save receipt.

Filament scope includes a reusable field for Resource create/edit forms and action modals, nested/repeated fields, disabled/read-only/required/validation states, configurable editor extensions, honest local/remote/conflict states and a runnable admin example. Asset upload/attachment UI uses existing optional asset ports and the application's policies; it does not install another upload/storage authority. Collaboration remains opt-in. Table/infolist HTML rendering, additional admin frameworks and automatic content conversion are not implied by providing the editor field.

### Drupal document fields

User addition, 2026-10-24: provide a separately installable Drupal module using the standalone PHP SDK, with a proper [field type, editing widget and display formatter](https://api.drupal.org/api/drupal/core%21modules%21field%21field.api.php/group/field_types/11.x). Select and declare one maintained Drupal/PHP baseline at implementation; supporting Drupal does not introduce another editor format or a historical Drupal compatibility matrix. Distribution names are provisional and installation starts no external service implicitly.

The field type uses Drupal Typed Data, field/storage settings, configuration schema, constraints, cardinality and empty-state semantics. Each field item has a stable identity independent of its mutable delta. Its stored value identifies the canonical document/epoch and an exact immutable committed snapshot/revision through the SDK repository, rather than an HTML/Markdown projection or a pointer that always displays the latest document. An absent field and an initialized-empty document are distinct. Entity storage and SDK records use an explicitly shared transaction where atomic entity/document save is promised; a remote authority cannot join that transaction, so that topology requires an explicit staged publication/reconciliation protocol before claiming atomicity.

The PHP SDK owns immutable snapshot retrieval and retention; a missing exact-revision lookup or retention API is a named prerequisite, not permission for Drupal to implement a second checkpoint decoder or history store. Drupal entity revisions retain their exact snapshot references. Viewing/reverting an older revision, saving a draft or publishing content moderation cannot expose later unapproved document changes through the published field. Revision revert is an explicit write to the current working state under policy, preserving the original snapshot and history. Translation mappings isolate language-specific document content by default; host-authorized sharing/duplication must be explicit. Cloning an entity or reordering field items cannot silently link another entity's document or change item identity.

The widget wraps the existing browser editor through Drupal asset libraries and [JavaScript behaviors](https://www.drupal.org/docs/drupal-apis/javascript-api/javascript-api-overview), with bounded attach/detach and single initialization across AJAX/BigPipe/form rebuilds. It supports normal entity forms, multiple values, nested/paragraph-style forms when the host supplies standard field widgets, required/read-only/disabled/error states, extension settings and accessible labels/messages. Full canonical bytes are not resubmitted on every UI redraw; explicit save prepares exact SDK inputs and coordinates the entity save boundary. Failed validation, denied access, stale revisions or rebuilds preserve unsaved recovery and never turn an AJAX/form success into a durability receipt. There is no second Drupal undo stack or text model.

The formatter loads the exact committed snapshot and uses the qualified SDK read-only rendering/export boundary, then Drupal-safe render arrays/text-format policy. It never executes raw unknown data or trusts stored HTML as safe. Missing qualified rendering support blocks that capability; escaped/plain-text display may be declared separately without claiming rich rendering. Entity/field/revision/language access results and [render cache metadata](https://www.drupal.org/docs/drupal-apis/render-api/cacheability-of-render-arrays) propagate with the exact snapshot: tags, contexts and max-age must prevent cross-user/language leakage and draft content appearing in published caches. SDK render/lookup interface gaps are repaired with their existing owner before formatter acceptance.

Module routes and every widget/save/preview/render path enforce Drupal entity/field/revision access, configured permissions and CSRF where applicable, while forwarding only verified scope/policy to the SDK. Optional Media/File integration maps authorized Drupal asset selection and usage tracking to existing SDK/blob finalization; selection/upload alone is not availability. Field/entity/revision deletion releases references under declared retention and only then permits scoped SDK cleanup; uninstall/config changes never silently purge canonical documents or real user data. Configuration export contains settings, not document content, credentials or packed editor assets. The example covers node/custom entity fields, revision/translation behavior and the exact supported optional integrations; automatic replacement of core body fields, content migration and a new WYSIWYG format are outside this addition.

## Backend topology and semantic validation

There are two supported deployment shapes: a framework-owned database with an edit.ac repository/transaction adapter, or an application backend delegating persistence to the Rust document-store authority. They implement the same logical outcomes. Examples must say which shape owns the transaction and receipt; two services must not each claim independent authority for one document revision.

Plaintext canonical writes use the existing Rust staged admission validator. Rust backends may call it directly. PHP, Python, Go, JVM, .NET and Ruby backends use a private bounded companion interface by default; in-process FFI is an additional declared capability where qualified. PHP FFI must not be mandatory. A browser-reported validation result or a DTO shape check cannot authorize semantic admission of untrusted bytes.

In framework-owned storage, validation is against a captured predecessor. The validation result binds document/epoch, format, predecessor durable revision, exact input digest and proposed effect. Commit performs a compare-and-swap in the authoritative transaction. A changed predecessor requires fresh validation; never hold a database transaction across an unbounded network call or trust a reusable client-supplied validation token. Concurrent append/compaction/delete obey the same serialization. The private validator is authenticated, deadline-bound and not an arbitrary URL chosen by request content.

An opaque archive integration may preserve arbitrary bytes, but is not a qualified canonical document-save adapter and cannot emit canonical remote commit receipts. Protected/ciphertext profiles are separate capabilities owned by tracks 19/24: an opaque host cannot promise plaintext validation or semantic editing. Do not enable encrypted support merely because a byte column accepts ciphertext.

## Logical operation contract

Exact route names and public API spellings are authored in contract task BSC-1.2; the operations below define required behavior, not already implemented methods.

| Operation | Required behavior |
|---|---|
| Create document | Application-authorized creation with complete identity and explicit initialized checkpoint; idempotent request key; initialized-empty is existing data |
| Load document | Authorized coherent checkpoint, exact coverage, replay tail, current durable revision and resume floor; distinguish absent, forbidden and recovery-required under application disclosure policy |
| Save checkpoint | Complete format and bytes, expected durable revision, operation key and digest; validate then atomically commit or return typed conflict; never last-writer-wins over another save |
| Append updates | Stable writer/sequence/update identity and exact bytes; validate staged effects, deduplicate and durably commit with exact covered receipt |
| Read updates | Bounded cursor pagination/resume, scope and negotiated profile; no implicit initialization on empty response |
| Look up commit | Recover a lost acknowledgment using the original operation identity; unknown/pending/committed/rejected are distinct outcomes |
| Publish checkpoint | Engine-validated compaction and coverage with retained fallback; preserve retransmittable unacknowledged updates and real history |
| Observe changes | Authorized optional synchronization transport; resume from committed state, bounded queues, cancellation and backpressure |
| Assets/lifecycle | Existing blob finalization, tombstone, retention and purge ports; attachment availability has its own receipt; disposal never implies save or purge |

The initial HTTP representation uses JSON metadata and explicitly named base64 fields for exact binary bytes, with bounded decoded and encoded sizes. No text normalization or lossy number coercion is permitted. The contract task must settle integer encodings/ranges, nullability, date units, UUID grammar and unknown bounded data policy consistently across runtimes. Raw binary optimizations are deferred until justified and must not create a competing production wire contract before publication. Authenticate/sign exact byte digests, not JSON property order. Requests and responses have size/depth/time limits and redacted diagnostics.

ETags/If-Match, when exposed, carry the authoritative durable revision with scoped identity. They are not the engine's local observed revision or a Yjs state vector. Save response receipt fields bind tenant/document/epoch, exact operation/update identity and digest, covered revision and declared durability class. HTTP 200/202, socket delivery and CRDT convergence alone never establish a remote save. Conflicts preserve local unsaved content and offer reload/review or an explicitly supported merge path; automatic overwrite is forbidden.

## Save, load and recovery behavior

Every integration demonstrates create → edit → local commit → remote commit → close → reopen, plus initialized-empty and non-ASCII content. Before explicit application shutdown, the binding flushes according to declared policy or returns recoverable unsaved state; component unmount, server render and process destruction are not acknowledgments. Local and remote status remain separate.

Restore validates identity, initialized state, checkpoint and tail on a staged replica, obtains a fresh live writer identity and preserves original source/operation identities and unknown bounded data. No HTML/Markdown/JSON projection substitutes for a canonical checkpoint. Local history semantics remain owned by the existing engine; genuine revision/history data is retained according to the host contract, and no unsupported UI undo restoration promise is added.

Retries use the same operation identity and bytes. A repeated key with different input rejects. A lost reply enters commit-unknown and resolves through ledger lookup or exact idempotent retry, with no duplicate mutation or receipt upgrade. Cancellation after sending a write does not prove rollback. Authentication expiry/revocation, conflicts, quota, incompatible input, corrupt data and backend unavailability are typed outcomes preserving original work. Read-only and tenant authorization apply to every route and mutation entry point. Tenant/document selectors and forwarded client origin strings never grant authority.

Collaboration appends immutable updates and retains outbox state until matching remote receipts. Checkpoint-only and collaborative writers cannot race through independent stores: promotion to collaboration reuses the same identity, authority and serialized revision/operation ledger; stale checkpoint saves reject or reconcile explicitly. Awareness/cursors are optional, scoped, expiring and never journaled as document state. Use original relative anchors and UTF-16 conversion; adapters must not invent per-framework selections or a second history stack.

## Planned support matrix

These rows commit planning scope; none establishes shipped support, popularity ranking or a package-version promise. PHP/Laravel is the first complete vertical slice, followed by the remaining language and adapter families. Actual minimum/current runtime and framework versions are selected from official maintained releases during each family task, recorded in an authored support manifest and qualified in final checks; do not claim all historical versions.

| Family | Language SDK / headless binding | Backend or application adapters |
|---|---|---|
| PHP | Standalone Composer SDK, HTTP client and framework-neutral persistence orchestration | Thin Laravel routes/policies/Eloquent wrapper; optional Filament admin field/plugin; Symfony routing/security/Doctrine wrapper; Drupal document field/widget/formatter module |
| TypeScript/JavaScript | Node HTTP/server package; browser transport integration | Express, Fastify, NestJS; Next.js route handlers and SSR-safe binding |
| Python | Synchronous and asynchronous clients | Django/DRF, FastAPI/Starlette; SQLAlchemy repository port |
| Go | Context-aware client and repository interfaces | Standard `net/http`, Gin, Echo; `database/sql` driver |
| Rust | Native authority client and existing semantic library | Axum integration over the existing host; no duplicate document service |
| JVM | Java client plus idiomatic Kotlin extensions | Spring Boot/Spring Security; Ktor; JDBC transaction adapter |
| .NET | C# async client | ASP.NET Core, application authorization, EF Core repository |
| Ruby | Gem client | Rails/ActiveRecord; transaction and policy hooks |
| C and C++ | Explicit C ABI, ownership-safe C++ wrapper | Embedding/headless validation and native/desktop host consumption, not an HTTP framework |
| Swift | Existing engine binding plus typed storage/transport facade | iOS UIKit/SwiftUI; macOS AppKit/SwiftUI |
| Kotlin native Android | Existing engine binding plus coroutine storage/transport facade | Android Views and Jetpack Compose |
| Dart | Typed storage/transport SDK and native bridge | Flutter using existing native editor hosts where available |

Web UI adapters cover the existing React and Astro packages plus Next.js, Vue, Nuxt, Svelte, SvelteKit and Angular. They share lifecycle, autosave/status and optional collaboration orchestration; no framework owns a new document format or semantic engine. SSR never instantiates the DOM/WASM editor, starts network work or shares document sessions between requests. SPA route changes, form reset/validation, multiple mounted editors and disposal have explicit behavior. Uncontrolled document ownership is the default; a framework value prop cannot repeatedly re-import content or reset CRDT lineage.

Desktop integration covers Windows WinUI and a WPF host wrapper, Linux GTK, Electron and Tauri, with C++/Qt headless interoperability and a bounded native-surface feasibility decision. Qt GUI support is a candidate until a host surface is proved; this plan does not assume GTK can be embedded everywhere or promise a new Qt renderer in one task. Electron explicitly uses the qualified browser editor; Tauri's web host is likewise identified. Neither is represented as the native iOS/Android editor.

React Native and Flutter use native editor surfaces and the shared engine, with explicit text/selection/composition, event ordering and lifetime boundaries. Their functional bridge tasks require the relevant native host APIs and must split further if those APIs do not exist. Native embedding does not implement a parallel text model, WebView fallback, private undo stack or unsupported platform renderer. Unsupported platform/widget combinations return an explicit capability error.

## Storage and database support

Initial reference drivers target real local SQLite for deterministic conformance and PostgreSQL for production-shaped transactional integration. The standalone PHP SDK additionally owns MySQL/MariaDB transaction profiles; Laravel/Symfony map their connections and transactions to those shared SDK ports. Each database is a separately declared tested backend, not an assumed SQL alias. Database/version selection, isolation, binary encoding, row locking/CAS, uniqueness, parameter limits and schema migration locks are authored before driver acceptance.

Minimum records cover scoped document identity/initialized state, current durable revision, checkpoints and coverage/fallback, immutable journal updates, operation outcomes and receipt identities. Assets keep their existing immutable blob references and finalization ownership. Repository ports must not force every application to use the supplied schema, but a custom schema passes the same conformance contract. Installation migrations create new adapter tables only; existing document bytes are never reseeded, relabeled or silently converted. Backup and retention policies remain application choices with declared guarantees, not promises inferred from a successful query.

In-process memory/fault repositories are prepared fixtures only. No relational database, Redis/cache, queue delivery, ORM callback or object upload can emit a durable receipt before its owning transaction actually commits. Multi-process safety must be provided by the authoritative store rather than an in-process mutex. Redis/queue/service adapters beyond the named scope remain future candidates, not hidden prerequisites.

## Acceptance, qualification and adoption

Each functional task has a focused deterministic delivery check, normally one prepared request/fixture or compiler/package consumer. A tiny cross-language binary/receipt oracle is justified early by the data-loss risk; comprehensive test authoring and matrices belong after all functional files. Preserve useful existing conformance evidence instead of rerunning unrelated suites at each package boundary. No production credentials, paid inference, live provider calls or automatic fixture recording are permitted.

The final backend testing file owns current-format bytes/unknown-data parity, semantic admission, real database atomicity, retries/commit-unknown, authorization and checkpoint/collaboration transitions. The final framework/native testing file owns SSR/lifetimes, form binding, actual native host routing, composition/selection/history, offline recovery, packages, resource teardown and the exact runtime/platform matrix. Track 43 owns remaining actual device/target-runtime observations through a new adapter case register; a missing or skipped observation remains unqualified. Both final files are required for whole-plan completion. An individual delivered package may report its narrower focused results without claiming overall qualification.

Every package declares an owner, authoritative source path, install artifacts, runtime/framework ranges, database capabilities, semantic bridge dependency, cancellation/retry/durability behavior and unsupported features. A generated capability page is derived from authored declarations and validated results; planned entries must not appear as released badges. Local package creation and install checks precede any separately authorized registry publication, deployment, signing, production credentials or meaningful live-content dogfood. Public distribution remains a later approval boundary, not part of this planning request.
