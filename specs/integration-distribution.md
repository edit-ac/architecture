# Integration repositories, packages and listings

Planning update: 2026-10-26. [Decision 007](../decisions/007-integration-repositories-and-packages.md) makes dedicated repositories and packages the target for maintained integrations. All repository slugs, new package names and channels below are candidates pending inventory and ownership checks. This is an authored planning catalog, not evidence of registration, extraction, publication or qualified support.

## Ownership and identity

One integration owns one repository and its ecosystem distribution. Subpaths, CSS, closely coupled build products and platform variants may share that integration's repository; an independent framework or optional library adapter does not. The central engine/web contracts stay in `core`. Existing feature owners in the [backend](backend-sdk-adapters.md), [web UI](editor-ui-integrations.md), [surface ledger](editor-ui-surface-ledger.md) and [native UI](native-ui-integrations.md) plans remain the implementation owners until a validated extraction handoff.

The tables are a minimum inventory of the named integration scope, not permission to silently drop an implemented adapter that the inventory discovers. Every distinct item separated by commas below gets its own row, repository and distribution in the finalized machine-readable catalog; these grouped rows save repetition here. Existing names take precedence over candidates. Registry normalization/case rules, name availability, account ownership and supported publication routes must be verified before names become final. No empty package is published to reserve a name.

## Browser and UI catalog

Repository names are relative to `edit-ac/`. Each listed slug is a separate repository; npm candidates use `@edit-ac/<slug>`.

| Integration | Dedicated repository slug(s) | Distribution target |
| --- | --- | --- |
| React, Astro, Vue, Svelte, Angular | `react`, `astro`, `vue`, `svelte`, `angular` | npm; preserve existing names and useful controls/UI/style subpaths |
| Next.js, Nuxt, SvelteKit | `next`, `nuxt`, `sveltekit` | npm; thin host/server configuration over the matching binding/SDK |
| Base UI, React Aria, Radix | `react-base-ui`, `react-aria`, `react-radix` | npm; only matching optional component-library peers |
| Reka, Bits UI | `vue-reka`, `svelte-bits` | npm; Vue/Svelte peers remain separate |
| shadcn React Base UI and Radix kits | `shadcn-react-base-ui`, `shadcn-react-radix` | Separate versioned shadcn registry source distributions |
| shadcn Vue and Svelte kits | `shadcn-vue`, `shadcn-svelte` | Separate versioned framework registry source distributions |
| React Native, Expo | `react-native`, `expo` | npm; Expo adds configuration/host integration over the RN module |
| React Native Paper | `react-native-paper` | npm; optional Paper adapter over RN |
| React Native Reusables | `react-native-reusables` | Versioned source-kit registry distribution; exact host route to be settled |
| Electron, Tauri | `electron`, `tauri` | npm host integration; Tauri's coupled Rust bridge may be a crate in the same repository |

Default DOM UI remains an opt-in `@edit-ac/web` surface in `core`. Plain JS, Blade and Alpine recipes do not create synthetic adapter packages. MUI, Mantine, Chakra/Ark, Ant Design, PrimeVue, Vuetify, Solid and Web Components remain at their currently declared recipe/assessment status. Promotion to maintained integration requires a catalog row and dedicated repository/package; mentioning a recipe does not claim adapter support.

## Backend SDK and adapter catalog

Every adapter depends on its language SDK or shared contract, rather than duplicating protocol or persistence orchestration. Split combined implementation tasks into the separate distributions below without repeating their implementation.

| Integration(s) | Dedicated repository slug(s) | Candidate distribution/channel |
| --- | --- | --- |
| PHP SDK | `php` | `edit-ac/php` via Composer/Packagist |
| Laravel, Symfony, Filament | `laravel`, `symfony`, `filament` | `edit-ac/<slug>` via Composer/Packagist; Filament depends on Laravel → PHP |
| Drupal | `drupal` | Drupal module distribution/Composer channel; coordinate Drupal project identity and listing separately; direct PHP SDK dependency |
| Node SDK | `node` | `@edit-ac/node` via npm |
| Express, Fastify, NestJS | `express`, `fastify`, `nestjs` | `@edit-ac/<slug>` via npm |
| Python SDK | `python` | `editac` candidate via PyPI; distribution and import names recorded separately |
| SQLAlchemy, Django, DRF, FastAPI, Starlette | `sqlalchemy`, `django`, `drf`, `fastapi`, `starlette` | Separate `editac-<slug>` candidates via PyPI |
| Go SDK | `go` | Versioned Go module; canonical module path and pkg.go.dev indexing |
| net/http, Gin, Echo | `go-http`, `gin`, `echo` | Separate versioned Go modules; framework-specific route bindings |
| Rust application SDK, Axum | `rust-sdk`, `axum` | Separate `editac-sdk`, `editac-axum` crate candidates via crates.io; shared engine crates remain core-owned |
| Java SDK, Kotlin extensions | `java`, `kotlin` | Separate Maven artifacts; verify namespace and Maven Central route |
| Spring Boot, Ktor | `spring-boot`, `ktor` | Separate Maven artifacts over the JVM SDKs |
| .NET SDK, ASP.NET Core, EF Core | `dotnet`, `aspnet-core`, `ef-core` | Separate NuGet packages; candidate `EditAc.*` identities |
| Ruby SDK, Rails | `ruby`, `rails` | Separate `editac`, `editac-rails` candidates via RubyGems |
| C SDK, C++ wrapper | `c`, `cpp` | Versioned CMake/installable SDK distributions; Conan/vcpkg eligibility and listing ownership must be resolved, not assumed |

Next.js server routes belong to `next`, alongside its client integration, and use the Node SDK. Common HTTP DTOs, native ABI inputs, database ports and deterministic fixtures remain shared authorities. A database driver with a separate maintained install boundary gets its own catalog row; internal driver modules and examples do not become placeholder repositories. Final inventory must explicitly classify the planned PDO/MySQL/MariaDB, Node SQL and Go database/sql boundaries.

## Native catalog

| Integration(s) | Dedicated repository slug(s) | Candidate distribution/channel |
| --- | --- | --- |
| Swift SDK | `swift` | SwiftPM package over the shared engine artifact |
| UIKit, SwiftUI, AppKit | `uikit`, `swiftui`, `appkit` | Separate SwiftPM packages; platform availability and binary dependency recorded |
| Android SDK, Views, Compose | `android`, `android-views`, `android-compose` | Separate Maven artifacts; optional Compose peers; shared native engine artifact |
| Windows native bridge, WinUI, WPF | `windows`, `winui`, `wpf` | Separate NuGet packages and declared native runtime assets |
| GTK, libadwaita | `gtk`, `libadwaita` | Separate installable integration packages; freeze language/registry from existing host implementation before choosing coordinates |
| Qt | `qt` | Installable CMake/Qt distribution; preserve headless support and bounded GUI feasibility status |
| Dart SDK | `dart` | `editac` candidate via pub.dev; remains Flutter-free |
| Flutter | `flutter` | Preserve `editac_flutter` candidate via pub.dev; Material/Cupertino exports share the plugin |
| Flutter web | `flutter-web` | Separate pub.dev platform implementation over the existing web editor; no second native engine |

Federated Flutter platform implementations get dedicated repositories/packages when they are independently maintained distributions. Do not create empty platform packages for unsupported targets. React Native/Expo and Electron/Tauri are cataloged above; each appears only once. Keep shared engine binaries versioned and referenced through the qualified artifact channel, not copied into tracked source or vendored per adapter. No new native support claim follows from a package manifest.

## Required catalog and listing fields

The future authored catalog records one row per distribution: integration ID, feature owner/task, implementation source path, target repository, extraction status, package coordinates and import name, registry/channel, namespace owner, availability verification date/result, release owner, source revision/tag, peer/runtime constraints, dependency edges, entry points/products, optional assets, tested capability profiles, license/notices and provenance route. Registry lookup is read-only; an available spelling does not prove account ownership. Unresolved names or access are explicit blockers for that distribution, not for independent integration work.

Each listing needs a useful short description and ecosystem keywords; canonical repository/homepage/docs/issues links; Apache-2.0 and required notices; supported runtime/peer/platform constraints; a package-specific README with install/import, minimal real example, lifecycle/disposal and limitations; changelog/release notes; and a named maintenance/security contact. Record ecosystem-specific equivalents rather than copying npm fields into every manifest. Public listings describe delivered capabilities and link to support status; planned features remain labeled planned.

Local release preparation must include an explicit file allowlist/exclusions, complete source/type/style/native assets, clean dependency coordinates, reproducible build instructions, package version and artifact integrity. Published artifacts cannot depend on sibling checkouts, workspace protocols, source-tree relative paths or unpublished placeholder versions. Generated bindings, binaries, archives and reports remain outside Git. Registry credentials and signing material never enter the catalog, source or test fixtures.

Registry/channel work includes npm scope/publisher access; Composer package and Packagist linkage; Drupal project/channel requirements; PyPI project ownership; Go module tagging/indexability; crates.io crate ownership; Maven namespace/signing/publication; NuGet ownership/signing; RubyGems ownership; pub.dev publisher/plugin metadata; SwiftPM repository/tag and binary checksum delivery; native C/C++ package-manager routes; and versioned shadcn/source-kit manifests, item dependencies, files and install URLs. These are work items, not verified current platform requirements. Use the channel's current official documentation during implementation, and record which optional directories are actually eligible. SwiftPM and Go discovery are not treated as npm-style upload registries.

## Delivery handoff

This is a controller plan, not an executable queue. Before execution, emit focused sources using the roadmap task contract, with stable per-integration IDs, exact paths, 15–45 minute parents, prerequisites, independent work, deterministic selectors, progress and interruption handoff. Do not insert a single unbounded “extract every integration” parent. Reuse the current feature and package owners, including BPG-1.5, BPG-1.6 and UPG-1.1–1.3, rather than implementing competing SDKs.

| Checkpoint | Required output and acceptance | Owner / resume condition |
| --- | --- | --- |
| Inventory | Finalize one machine-readable row per integration/distribution, current paths, existing names, ownership, channel and dependency graph; classify recipes and unimplemented profiles honestly | Packaging coordinator; read-only inventory can proceed independently of registry credentials |
| Prepare repositories | Review per-repository source boundary, README/license/security/contribution files, build/lockfiles, CI and consumer migration; resolve remote ownership and each registry namespace | Packaging coordinator plus ecosystem owner; remote creation is a later explicit action |
| Extract | One integration at a time, dependencies first; move authored source with history where practical, preserve package identity, update consumers/CI/docs atomically, remove the old implementation after handoff | Existing feature owner at a safe worker checkpoint; exact source/artifact prerequisite required |
| Package and prepare listings | Build and install the actual artifact in an isolated consumer outside all sibling checkouts; verify declared peers, assets, links, versions and release metadata | BPG/UPG package owners, split by integration/registry; local artifacts and mocked transports only |
| Final validation | One final owner reconciles remaining cross-repository coverage and verifies a mixed-integration consumer resolves one engine/contracts graph; reuse unchanged focused results | Existing final backend/UI qualification owners; fill gaps after functional extraction, preserve original release gates |
| Publish and confirm listings | After qualification and explicit release authorization, publish in dependency order and verify real registry install, listing links and provenance; keep URL/version/status in the catalog | Release owner; missing access blocks only the affected release/dependents; no publication through routine roadmap execution |

States are `planned`, `implemented-in-core`, `extracted`, `locally-packaged`, `registry-ready`, `published` and `qualified` with separate capability evidence. A completed in-core feature is not undone by this plan; extraction and listing readiness remain open until their own acceptance passes. Registry-ready means name/access and release configuration are checked, not that a package exists. No paid inference or live provider calls are needed for any automated extraction or packaging validation.
