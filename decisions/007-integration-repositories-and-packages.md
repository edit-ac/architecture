# Dedicated integration repositories and packages

Date: 2026-10-26. Status: accepted planning direction; names and extraction batches remain proposed.

The user requested dedicated repositories and packages for integrations, including proper package-registry listings. This supersedes the integration ownership in [packages/release](../specs/packages-release.md) and the core-relative delivery layout in the backend, web UI and native UI plans. It does not claim that repositories or listings already exist.

Each maintained language SDK, framework adapter, component-library adapter and native host integration has a dedicated `edit-ac` repository and an independently installable, versioned distribution. Existing public package identities are preserved. A framework's lifecycle, controls, CSS and default UI can remain subpaths/products of its package; they do not each require another repository. Optional component-library peers belong in their own integration. Source-owned shadcn kits have dedicated repositories and versioned registry distributions rather than an artificial editor runtime package.

`core` retains the engine, canonical document/protocol/ABI contracts, framework-independent web SDK, shared semantic implementation and deterministic contract inputs. Integrations consume those contracts and artifacts; extraction must not copy the engine, invent a second save protocol or create competing writable document models. The optional Markdown and format packages are not integration extractions under this decision.

Next.js, Nuxt and SvelteKit receive dedicated thin integration packages over React, Vue and Svelte respectively. This supersedes the earlier profile/subpath-only packaging choice, while preserving its shared semantic ownership. PHP, Laravel, Filament and Drupal remain separate packages and now also have separate repositories. Expo depends on React Native's canonical module rather than creating another native editor.

The [integration distribution plan](../specs/integration-distribution.md) records the repository/package/channel map, listing requirements and delivery handoff. Source extraction, registry readiness and publication are separate states. Local passing packages do not establish registry ownership or published support.

Adopt at a safe coordinator checkpoint. Existing core-relative paths remain the current implementation locations until each extraction lands with its consumers, build inputs and validation. Do not move an active worker's files or rewrite its immutable source. Reconcile completed delivery before emitting bounded extraction sources; completed feature work is reused. No new runner, remote repository creation, registry reservation, package publication or deployment is performed by this planning change. Publication remains subject to the existing release gates and explicit release authorization.
