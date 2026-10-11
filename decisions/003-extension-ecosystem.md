# 003 — Complete the extension and public integration ecosystem

Accepted planning scope: 2026-10-11. Extends decisions 001 and 002. The user requested first-class content extensions, broad document interchange, public docs/demo and cloud document-store readiness. The user explicitly limited PDF to **export only**; PDF import and OCR are out of scope.

## Ownership and delivery

Keep the Rust semantic engine authoritative and small. Optional highlighting, document conversion, link metadata and cloud hosting consume its prepared commands, portable data and capability ports. They cannot bypass revision checks, readonly mode, recovery or extension preservation.

Add `edit-ac/docs` as a fourth public Apache-2.0 repository for learning material, generated references and the release-backed playground. Architecture remains the authority for contracts and tasks. The docs site links immutable SDK versions; it does not maintain another editor implementation. Core contains portable extensions, native adapters and the reference document service; CLI contains terminal presentation.

Baseline tracks 01–24 retain their task identities and original browser delivery gate. New rich-content, link, conversion and cloud tracks extend qualified baseline modules instead of replacing them. Native integrations are separate per-OS tracks to avoid making one unavailable platform block another. Public documentation can be prepared before SDK qualification, but executable tutorials and the demo cannot advertise a working editor before the matching package passes.

## Resolve the missing contracts

Syntax highlighting is derived presentation, never CRDT text or a per-keystroke whole-document pass. Table formatting preserves identities and distinguishes Markdown source alignment from semantic table commands. Assets have a staged upload/finalize/cancel lifecycle; embeds use approved host presenters and safe cards. Slash and reorder modules include touch and non-drag pointer alternatives.

URL display has a policy-controlled automatic mode for local paste and explicit refresh. Resolvers separate public metadata from principal-scoped private references. A preview never grants access, silently publishes a private title, or falls back from an internal permission failure to an external fetch.

Document conversion has a direction-specific support matrix and loss reports. Markdown, DOCX and other supported formats have explicit import/export adapters; PDF has export only. Heavy parsers, font/layout engines and image decoders stay outside minimum SDK loading. There is no promise that arbitrary office documents map losslessly to an editor schema.

A test relay is not cloud storage. The reference document host needs durable receipts, tenant isolation, staged asset finalization, retention, restore and adapter conformance. One deployable service is sufficient initially; no mandatory hosted edit.ac service or provider provisioning is implied.

## Architecture improvements

Use a versioned capability/release profile as the shared source for package checks, native capability reports, docs, demo controls and cloud negotiation. Keep permissions separate from declared features. Add executable layer checks, compatibility fixtures, dependency/license inventories and bounded resource policies. Tests prove user-visible invariants and recovery behavior; they do not mirror every internal function or require live model calls.

The existing provisional performance budgets remain provisional until measured. Feature claims include enabled modules, document sizes, hardware, device/OS and cold/warm behavior. Independent package loading and cancellation are part of the contract.

No foundation source or active runner is changed by this planning extension. See the [ecosystem review](../evidence/extension-ecosystem-review.md), [maintainability contract](../specs/ecosystem-maintainability.md) and [public delivery contract](../specs/public-docs-demo.md).
