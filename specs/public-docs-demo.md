# Public documentation and demo delivery

Repository: `edit-ac/docs`, public Apache-2.0. The initial repository contains Markdown guides, checked navigation and dependency-free CI. It is not yet a published documentation website or an editor demo.

## Public information architecture

Organize a clear landing page; getting started by web/React/native/CLI; local-first and collaboration guides; extension authoring and recipes; custom/internal links; import/export matrix; cloud host operations; host-app MCP; security profiles; generated API reference; troubleshooting, migration and release notes. Separate tutorials, task guides, conceptual explanations and reference tables. Keep internal tasks and architecture decisions in architecture, linked when useful.

Every API snippet is compiled/executed against named immutable artifacts. Mark conceptual contracts as such until the API exists. Generate versioned API pages from the owning packages and native bindings. Public feature tables consume the qualified capability/release profile. Show unsupported/experimental modes clearly, including **PDF export only**. Do not publish an install tutorial for empty placeholder packages.

The static site needs keyboard/screen-reader navigation, readable code and tables, responsive layouts, search, theme contrast, stable versioned URLs, a useful 404 and redirect/migration policy. Search indexes public docs only. Keep a plaintext/Markdown reading path available. Pin the selected maintained generator at its implementation gate; no custom documentation framework is required.

## Playground contract

Use the actual packaged editor. Keep the playground in this repository as a consumer, with editor semantics in core. Offer a PM-ticket preset, a collaborative document scenario, code/table/asset/reference examples, a read-only view, undo/redo, diff review and conversion actions supported by its exact version. Show enabled extensions and relevant profile limits. Include keyboard/touch paths and reset/export controls.

Default public mode uses redistributable fixture documents and local browser storage. Disclose local persistence and provide reset; do not imply browser data is permanent. Multi-view/tab collaboration uses real qualified local transport. A remote collaborative room is an optional deployment mode requiring the cloud service's qualified auth/retention/abuse configuration; the public static demo does not secretly depend on an unqualified backend.

No ambient credentials, private examples, live model provider or anonymous arbitrary URL proxy. Link-preview examples use approved public fixtures or a clearly configured host policy. Avoid arbitrary external embeds. Imported user data stays local unless an explicitly selected sharing mode declares its destination and authority. Conversion itself remains local-only in the qualified profile; remote conversion is out of scope. Bound conversion/highlighting work and show cancellation/recovery.

## Release and operation

Build, check local links/navigation, execute supported snippets/consumers, run browser accessibility/interaction checks and verify production base paths/CSP/WASM/worker assets before publication. Use existing organization GitHub Pages or another explicitly selected static destination; domain purchase and paid provisioning are not required.

Publish from immutable revisions with least-privilege CI and retained artifacts. Record public URL, SDK and docs revisions, smoke results and a tested previous-artifact rollback. A working build is not evidence that the deployment URL works. The final public demo task must verify the actual page and real edits.

A docs release can describe currently qualified web features while native implementation progresses. Native/format/cloud guides must state their maturity. Roadmap29 uses task-specific upstream gates for qualified examples/demo; it has no whole-track SDK prerequisite so documentation structure can proceed now.

## Candidate-to-publication ordering

EQL-1.9 publishes tested immutable prerelease artifacts after feature/platform qualification and before advanced DOC examples and demo publication. DOC-1.6/1.10/1.13 consume those recorded candidates, then DOC-1.14 supplies deployment evidence to EQL-1.7. EQL-1.8 promotes the same artifacts after public verification; it does not rebuild them. Roadmap37 therefore does not require all of29 at entry. This task-level gate prevents a docs/package publication cycle while keeping source-documentation work available early.
