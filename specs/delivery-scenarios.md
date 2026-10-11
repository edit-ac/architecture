# Full-delivery scenarios and capability matrix

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

## Test and release discipline

Commit deterministic cross-client fixtures and a machine-readable product manifest tying capability, implementation/package revisions, platform/toolchain/device, command/case IDs and resulting evidence. Production account data, live model providers and paid inference are not test fixtures. A sample host's mock auth is explicitly test infrastructure, not a production security deployment.

Run shared semantic/session/format/diff conformance plus each presenter adapter's focused tests. Then execute actual OS/device IME, keyboard/touch, screen-reader, clipboard and lifecycle cases. Missing device/toolchain evidence blocks that platform's qualified claim; it need not block independent implementation elsewhere. A completed package build alone does not prove parity.

Record performance against the declared enabled profile: minimal core versus task preset versus review or encrypted mode. Reuse the fixed Task/Long/Large/Aged corpus and honest visibility/editability/durability metrics. The extra clients do not justify silently dropping the earlier correctness or performance gates.

Full delivery requires the whole requested base matrix. Partial browser/iOS success may be released with its actual support table but cannot close the all-platform milestone. Encryption remains an additional profile with a separate completed roadmap; basic delivery can finish while its security review remains blocked.
