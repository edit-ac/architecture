# Full-delivery scenarios and capability matrix

Qualification amendment (user decision, 2026-10-14): Named target-platform simulators/emulators and desktop OS VMs/test hosts may satisfy platform and release gates when physical hardware is unavailable. Follow the [platform qualification policy](../specs/verification.md#platform-qualification-with-simulators-emulators-and-vms) for required runtime checks, tested virtual equivalents for hardware-only observations, counts and physical/virtual provenance. Earlier physical-only/manual-only wording in this document is superseded. This changes accepted evidence, not required implementation or correctness.

Status: qualification contract, not completed product evidence. Roadmap 20 qualifies the ordinary profile; roadmap 24 qualifies optional encrypted profiles after independent security review. The initial browser release is still independently gated by roadmap 10.

## Required scenarios

| Scenario | Concrete deliverable | Evidence required |
|---|---|---|
| PM ticket rich-text editing | Small host integration with text/marks/lists/links/checklists/table/image/reference preset, readonly/edit states and lifecycle disposal | Web/React plus genuine iOS, Android, macOS, Windows and Linux controls pass the same semantic corpus |
| Collaborative documents | Multiple platform clients edit the same identity online and offline, restore after local commit, reconnect and see converged content | Distinct live IDs, reorder/duplicate delivery, composition races, history and local/remote durability evidence |
| Agent edits through the app | Sample existing app MCP uses read/export, bounded Markdown upload/prepare/diff/apply and receipts while human views remain open | Prepared MCP requests, auth/readonly denial, stale conflict, crash-safe retries and realtime patches without remount |
| Local file and hosted terminal client | External-editor CLI plus built-in TUI edit Markdown/literal text, local files and configured ac:// documents | Exact source/no-op preservation, changed-on-disk detection, dirty buffer plus peer changes, recovery and reconnect |
| Review and change tracking | Web/native/terminal views of exact source/projected/semantic changes with available history | Byte-hash patch roundtrip, visible mark/attribute/move changes, unavailable-history handling and restore as new edit |
| Third-party extension | Portable custom mark, inline atom and host-authorized reference resolver using public documented entrypoints | No engine fork for data-only types; schema/codec/command/presenter conformance and full mandatory-platform editing |
| Optional protected documents | Explicit local-at-rest or E2EE profile with real key providers and authorized plaintext endpoints | Protected creation/history/attachments, tamper/replay/rotation/offline recovery, no downgrade and actual security review |

## Mandatory and optional capability rules

Mandatory rich-text semantics, selection, readonly, undo/redo, safe clipboard, composition, local persistence, collaboration, references/custom atoms and exact change model have a per-platform `capability.json`. Native table/image editing must actually work to satisfy parity; preserved fallback alone does not pass. All native desktop platforms were explicitly requested. Separate unsupported OS versions from supported configurations.

TUI is a Markdown/literal-source client. Terminal glyphs, source syntax and attachment placeholders need not reproduce graphical rendering, but edits must preserve supported shared semantics/unknown data and clearly reject unrepresentable changes. It does not implement a second CRDT or replace an entire hosted document on save.

Optional math typesetting, encryption and other extras have separate capability entries. Source preservation/editing is distinguished from typeset rendering. Optional absence never erases document data or silently changes the active security profile. A feature absent from one platform cannot be described as universal full parity.

## Multiple web editors and configurations

DEL-1.2 includes a task-description editor and comment-body editor mounted on the same page, plus task-description/document-body configurations on different site routes. Follow the [resource-sharing contract and SHR cases](web.md#shared-resources-across-editors-and-site-routes): reuse compatible engine/glue/common assets and the union of enabled optional code while preserving each document's identity, undo/redo, storage namespace, sync attachment, save/error callbacks, read-only state and host permissions. Exercise equal and mixed configurations, both mount orders, independent edits/saves, disposal during loading, one surviving editor and route-away/back. A feature loaded for the document configuration cannot silently enable it in a plain comment or grant resolver access.

Reuse SDK-1.10's installed-tarball site and exact-artifact receipt for resource assertions; add real product embedding/permission outcomes through the existing ticket scenario. Separate client navigation's in-memory reuse from full navigation's controlled HTTP-cache reuse and fresh initialization. Report default, optional union and incremental costs under verification.md; historical single-editor or native-control receipts do not establish web site deduplication. Native instances retain their existing per-platform/session qualification without a new browser-runtime-sharing obligation.

## Test and release discipline

Commit deterministic cross-client fixtures and a machine-readable product manifest tying capability, implementation/package revisions, platform/toolchain/device, command/case IDs and resulting evidence. Production account data, live model providers and paid inference are not test fixtures. A sample host's mock auth is explicitly test infrastructure, not a production security deployment.

Run shared semantic/session/format/diff conformance plus each presenter adapter's focused tests. Then execute OS/platform IME, keyboard/touch, screen-reader, clipboard and lifecycle cases on physical or named virtual target runtimes. Apply verification.md virtual-equivalent checks to unavailable hardware-only observations. Missing physical hardware does not block qualification; missing implementation, required runtime tooling or passing behavior evidence does. A completed package build alone does not prove parity.

Record performance against the declared enabled profile: minimal core versus task preset versus review or encrypted mode. Reuse the fixed Task/Long/Large/Aged corpus and honest visibility/editability/durability metrics. The extra clients do not justify silently dropping the earlier correctness or performance gates.

Full delivery requires the whole requested base matrix, which may be qualified entirely on named target-platform virtual runtimes under verification.md. Partial browser/iOS success may be released with its actual support table but cannot close the all-platform milestone. Encryption remains an additional profile with a separate completed roadmap; basic delivery can finish while its security review remains blocked.
