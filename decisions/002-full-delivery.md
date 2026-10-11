# 002 — Full client delivery beyond the first browser release

Accepted planning scope: 2026-10-11. This decision extends 001; it does not turn planned features into implementation claims.

## Requested outcomes

Deliver an embeddable PM-ticket editor, collaborative documents and agent-mediated edits on one semantic engine. Local editing and recovery are first-class. Additional clients include a Markdown/literal-text CLI, a built-in TUI, native iOS/Android and native macOS/Windows/Linux adapters. The user explicitly confirmed native desktop controls, as well as desktop browsers. No WebView may be represented as an OS-native editor.

The first browser release remains independently deliverable through roadmap 10. Roadmaps 12–21 are committed follow-up scope for shared client contracts, precise diffs, host-owned MCP, TUI, full native SDKs, optional encryption, portable extensions and scenario qualification. Roadmap 09 proves feasibility only; it does not satisfy native parity. Roadmap 11's existing external-editor/local/hosted work remains the base for the TUI.

## Capability, not marketing adjectives

“Excellent offline support” means cached and newly created local documents accept edits without network waits, durable local acknowledgment survives the supported process-crash model, multiple local writers exchange updates, pending work survives disconnect/auth failure, and reconnect converges. An uncached hosted document cannot be opened offline. Browser eviction/user deletion and revocation while a device is unreachable have explicit limits.

“Exact diffs” means a deterministic patch between identified immutable byte representations reproduces the expected output hash, alongside a separate semantic view of node/mark/attribute/move changes. CRDT update differences and normalized Markdown are not original-source diffs. Revision storage is explicit and bounded; undo, audit provenance and historical retention are distinct capabilities.

“Agent ready” means the embedding app can expose its existing MCP through reusable read/prepare/preview/apply interfaces with current authorization, revisions, durable retry identities and normal realtime propagation. The core contains no model provider or MCP server. CLI/TUI delivery does not depend on MCP, and a standalone edit.ac MCP product is not required.

“Same capabilities” means the mandatory document/edit/readonly/history/offline/collaboration/extension fixtures pass on every claimed platform. Native typography need not be pixel-identical. A fallback that preserves a table cannot satisfy a claim that native table editing is supported. Optional features have explicit platform matrices, not implied parity.

## Keep the core thin

Core responsibilities are schema/state, identity, prepared commands, anchors, history policy and incremental patches. Portable session/storage, source reconciliation, revision/diff and optional cryptography are cohesive companion crates or modules behind ports. OS rendering, terminal presentation, transport/auth, MCP and resolver credentials stay in adapters/hosts. Shared helpers are promoted out of a single client once; no platform forks of semantics.

Do not add a second authoritative CRDT, mandatory network startup, full-document Markdown serialization on every keystroke, or mandatory encryption/diff UI assets to the minimal editor. Size and latency targets include the features actually enabled by each qualified profile.

## Safety and trust boundaries

`ac://<document-id>` resolves through a local catalog; `ac://<authority>/<document-id>` selects a configured hosted authority. The final grammar and canonicalization have a test gate. An ID/hash is a locator, not an access token, immutable content address or permission grant. Arbitrary HTTP content is not a writable collaboration endpoint.

Optional local encryption and end-to-end encrypted collaboration are separate profiles. A ciphertext-only relay cannot also parse Markdown or run plaintext MCP edits. Agent editing occurs at an authorized decryption-capable endpoint, with that trust disclosed. No automatic plaintext downgrade is allowed. Baseline host authorization, safe import and resource limits apply in every profile.

## Execution compatibility

The existing foundation source and task IDs remain unchanged while its independently managed runner is active. Follow-ups begin with evidence checks; any discovered conflict with the frozen schema requires a controller-reviewed compatibility/migration decision before implementation. This documentation review neither starts nor stops a runner.
