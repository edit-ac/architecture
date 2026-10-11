# Requirement review and delivery mapping

Reviewed against the current docs on 2026-10-11. “Covered” below means planned contract/tasks, not shipped functionality. The existing scaffold does not establish editor behavior. The user's native desktop clarification includes macOS, Windows and Linux.

| Requirement | Existing coverage | Adjustment and delivery gate |
|---|---|---|
| First-class local-first/offline collaborative editing | 02 engine, 03 journal/recovery, 06 reconnect/receipts, 11 hosted CLI | 12 adds portable sessions, native stores, local channels, source catalog and offline policy; 20 verifies actual multi-client scenarios |
| Markdown/literal file editing and hosted CLI | Expanded 11 uses external editor; FMT-1.12 reconciles source | Preserve this work; 15 adds built-in TUI, ac:// routing, dirty-buffer conflicts and deterministic terminal qualification |
| Agent Markdown editing/uploads through embedding app MCP | Portable source reconciliation, commands/anchors and host auth responsibilities | 12 adds shared revision/policy/operation service; 14 adds host-tool schemas, prepare/diff/apply, durable retries and realtime observation; CLI MCP stays optional |
| Exact Git-like diffs and tracking | CRDT update/patch metadata only; no review/history API | 13 adds immutable representation-specific revisions, exact patches, semantic changes, review UI and restore-as-new-edit; native/TUI presenters consume it |
| PM ticket web/mobile/desktop embedding | Browser preset and React integration, native probes | 16/17/18/22/23 deliver real native editors; 20 qualifies the same mandatory ticket capabilities across all five native OS targets and web |
| Collaborative cross-platform documents | Browser/Rust fixtures; native future scope | Shared session/update profile and every actual client participate in 20 offline/crash/reconnect/composition tests |
| Native iOS/Android with same capabilities | 09 probes only | 16/17 deliver complete adapters, typed bindings, storage/sync, mandatory module UI and packaged consumers; actual device evidence closes in 20 |
| Native macOS/Windows/Linux | Not previously planned | Independent 18/22/23 platform tracks with toolkit feasibility, real native controls, bindings, package consumers and qualified support matrix |
| Readonly, undo/redo, custom references/extensions | Engine history and browser modules | Enforce readonly in shared mutation admission including MCP; qualify native/terminal histories and host-authorized reference hooks in every client |
| First-class extension library and thin core | Built-in browser modules and descriptors | 21 publishes coherent portable contracts, conformance harness, adapter hooks and third-party recipes; keep UI/network/MCP/crypto out of the semantic core |
| Optional encryption/private documents | Baseline safe import/auth only | 19 builds explicit local/E2EE profiles after threat-model/protocol selection; 24 gates real key providers, protected scenarios and independent review |

## Corrections to the proposed statements

- **Offline-first** includes cached/new local documents, supported crash recovery and explicit pending/rejected uploads. It cannot make uncached remote data available, prevent browser eviction, or erase a revoked user's already-held plaintext.
- **CLI/TUI collaboration** uses the same identity and command/recovery contracts. URLs resolve through configured hosts/catalogs; ordinary web pages and hash-looking strings do not confer edit authority.
- **MCP readiness** is a reusable host-app integration. Annotation hints are insufficient for permissions/idempotency; a Markdown candidate upload is revision-checked input to shared reconciliation, not a stale whole-document replacement.
- **Exact diff** names exact source bytes or a declared normalized projection and provides a separate semantic view. A Yjs state vector alone is not an exact revision token, and CRDT update bytes are not a review diff.
- **Native parity** needs actual editing/IME/accessibility/module evidence. Bindings and data-preserving fallbacks do not alone satisfy same-capability claims.
- **Encrypted mode** needs key/membership/rotation/recovery and a declared agent plaintext endpoint. An opaque relay cannot simultaneously decrypt Markdown or provide plaintext search/diffs.

## Why the planned core can support this

One portable authoritative replica, stable node identities/anchors, validated commands, origin-aware history, incremental patches and shared format reconciliation are the right prerequisites. New companion modules provide session/identity, revision/diff and optional security functions; presenters and MCP remain adapters. This is architectural compatibility by design, not proof that the future implementation meets every requirement.

The follow-up entry gates check the implemented schema/ABI and require a migration/compatibility decision if evidence contradicts the plan. The active foundation source/IDs remain untouched. Existing CLI amendments are preserved. See [decision 002](decisions/002-full-delivery.md), [scenario contract](specs/delivery-scenarios.md) and [primary-source implementation research](evidence/followup-research.md).
