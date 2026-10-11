# Public URL metadata and private reference resolution

Status: planned portable host/backend and web contracts, roadmap 26. Consume shared client/extension interfaces; do not replace their resolver, authorization or source ownership. Actual native/TUI presenter wiring is qualified in roadmaps 31–36.

## Service and data ownership

Expose distinct public-URL metadata and private-catalog ports through documented Rust/browser APIs. The host owns authorization, egress, credentials, caches and approved endpoints. The semantic core receives validated bounded records and invokes prepared commands; it never fetches URLs inside a transaction. Browser helpers call host ports rather than assuming arbitrary cross-origin HTML is readable.

Each request includes a request ID, principal/tenant context supplied by the host, locator, initiating action, node/document/epoch/revision, policy version and cancellation token. Response variants include available, unavailable, forbidden, missing, locked, unsupported, canceled and stale, with bounded safe display fields and freshness. URI text or response metadata never supplies trusted actor identity or grants access.

Public metadata records contain the requested/validated canonical URL, title, optional description, icon/image asset references, provider identity and fetched/expiry metadata. These are untrusted descriptions, not executable markup or proven ownership. Private records carry stable host target identity, capability-scoped display data and activation capabilities; they are not interchangeable with public webpage fetches.

## Automatic enrichment policy

Hosts explicitly select disabled, automatic-on-local-paste/insert, or explicit-refresh behavior. An enabled local paste policy may request title/favicon without another per-link prompt; the setting and its network behavior remain visible to the host/user. Opening/rendering a document, remote edits, recovery replay and history inspection initiate no requests. Imported links may show existing safe fallback without enrichment.

Capture URL/node/revision/request identity before lookup; bound requests and cancel obsolete work. Results cannot replace user-edited labels, resurrect deleted links or write into another document/session. Metadata display caches update without CRDT writes by default. A deliberate metadata commit uses the shared authorization/revision/history contract and makes any shared-label disclosure explicit. No automatic full-document link scan runs on ordinary edits.

An offline lookup returns cached metadata permitted by current policy or an honest unavailable state. Never infer an empty title means a deleted target. Negative-cache lifetime and retry/backoff are bounded, and canceled failures do not create noisy repeated network requests.

## Public URL admission and egress

Accept only configured HTTP(S) locators after standards-based normalization. Reject credentials in URLs, unsupported schemes, malformed hosts, overlong input and disallowed ports. Keep query strings/paths out of ordinary logs because they may contain secrets. Allowlist targets where the host's business flow permits it; a permissive public-web policy still requires protected-address checks.

Public resolution uses a dedicated host transport with no browser session cookies, ambient authorization headers or forwarded client credentials. Apply explicit connection/total timeouts, response-byte/decompression/redirect limits, content-type checks and bounded HTML parsing. Disable redirects by default. A host-enabled redirect path revalidates every hop and the actual resolved connection address before sending another request.

Cover loopback, private, link-local, reserved and metadata-service addresses in IPv4/IPv6, unusual numeric forms, DNS changes/rebinding and allowed-to-forbidden redirects. DNS validation must bind to the address actually used for the connection; checking one resolution and letting another unrestricted lookup connect is insufficient. Network egress policy supplements application checks. Do not disable those protections to resolve private internal links.

Title extraction reads bounded inert metadata/text only. Prefer declared Open Graph/title fields according to a deterministic policy, normalize display length/control characters and retain the original URL as fallback. Canonical URLs are advisory until validated; a page cannot rename document identity. Favicon discovery uses validated icon links and an optional bounded favicon fallback under the same policy. Icons/Open Graph images are independent untrusted URLs and pass identical egress, media-size and credential checks.

Return safe metadata or host-managed asset references. Rendering must not turn a rejected remote icon URL into a new unchecked browser request. Avoid third-party favicon lookups by default because they disclose visited document URLs. `no-cors` is not a way to read protected cross-origin pages, and a browser CORS failure does not authorize a more privileged fetch.

## Private internal targets and disclosure

Use a separate host-authorized catalog resolver for `ac://`, task/user/document references and configured private app links. Resolve only configured authorities and require current principal capability for target lookup, title/icon/preview and activation. A permission to read the containing document does not imply permission to read its targets. Hidden/missing outcomes follow the host's non-disclosing policy.

Cache private results by principal, tenant, authority, target and relevant permission/policy revision. Never reuse another user's or tenant's title/icon cache entry. Expiry, logout, account switching, revocation and key-lock events invalidate or hide previously resolved private display data. Offline use respects the cached-capability/lease policy; it does not promise instantaneous remote revocation.

Keep fetched private titles, icons and previews in per-viewer presentation/cache state by default. The CRDT retains target identity plus a neutral or explicitly user-authored label. Automatically writing a secret title into shared node attributes would reveal it to all readers of that document. Sharing resolved metadata requires an explicit host disclosure decision; test the actual recipient/document scope. No subsequent revocation can guarantee erasure of text already authorized and copied.

Private fetch credentials remain inside the host adapter; no URL, document attribute, preview, log or MCP result carries bearer credentials. E2EE lookup/export follows the authorized plaintext endpoint model; an opaque relay cannot resolve encrypted private metadata. Resolver output is content, not an instruction to run tools or follow additional URLs.

## Activation and presenters

Web/native/TUI presenters receive safe text, bounded asset references, freshness and supported actions. They expose cancellation/disposal, accessible labels, focus restoration, offline/locked/forbidden fallback and explicit activation. Headless fixtures define the same contract for all platforms; roadmap 26 implements web consumers and portable ports, not native controls.

Opening a reference rechecks current host activation capability. External browser/deep-link launch uses a validated action object, never shell command interpolation. Users can copy a safe locator without copying credentials. Custom reference triggers reuse existing extension registration and menu behavior; read-only permits authorized navigation while denying document mutation. Stale asynchronous results cannot change which target a click opens.

## Test and performance contract

Prepared resolver/network fixtures are the default; no real private services, user credentials or paid providers are needed. Verify no-call-on-open/remote/replay, local-paste policy, duplicate/canceled work, revised labels/deleted targets, malicious page/icon URLs, every denied egress branch and response limits. Denied requests must produce zero outbound transport calls.

Use two principals and two tenants to test cache isolation, target revocation, same-ID/different-authority collisions and private title/icon disclosure. Verify shared CRDT snapshots contain no automatically fetched secret title. Keep user-authored shared text intact; policy cannot retroactively classify it as an unpublished cache.

Measure local policy/filtering, cache-hit presentation and network wait separately. Reuse existing input/menu targets: network lookup does not block typing, commit, persistence or focus. Set finite concurrency/queue/response/media limits in the host configuration and prove they apply under bursts. Record cold/warm p50/p95/p99, request counts, cancellation and cache memory at exact fixture/build revisions. Dispose leaves no live request/subscription or stale private display state.

## Primary references

- [Open Graph metadata fields](https://ogp.me/)
- [HTML icon links and fallback](https://html.spec.whatwg.org/multipage/links.html#rel-icon)
- [oEmbed security considerations](https://oembed.com/)
- [Fetch and CORS constraints](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [OWASP SSRF prevention](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [MCP resource URI/capability model](https://modelcontextprotocol.io/specification/2025-11-25/server/resources)
