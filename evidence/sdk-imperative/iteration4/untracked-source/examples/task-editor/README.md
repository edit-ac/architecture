# Local task editor

Run `npm run build:wasm`, `npm run build`, then `npm run example:task` from core. Open the printed local URL. Stop the server with Ctrl+C.

The example creates one local document explicitly, then opens it with `createEditor` and `taskPreset`. Await `editor.ready` before commands. It uses the shared browser surface and IndexedDB journal; reopening recovers the same identity and content. Creation intent is retained if initialization fails, so a failed recovery cannot silently reset the document.

Native paste recognizes Markdown. “Paste without formatting” keeps literal text. “Save locally” waits for local journal commits; it does not confirm remote durability. “Reopen offline” flushes and destroys the old handle before mounting again. Hosts can call the exported `close()` before removing the example.

An embedding host can call `attachTaskSync({ transport, peerIdentity, authorized: true })` after authenticating its peer. The transport's synchronous `send(frame)` returns whether it accepted a copied binary frame. Route received binary frames to the returned attachment's `receive(frame)`. Drive `pump(monotonicMilliseconds)` on connection events, completed local saves, and its reported retry deadline. The host owns authentication, transport listeners and socket closure. `detach()` releases the editor's sync resources, and editor destruction also detaches. Attaching sync retains the existing document.

The deterministic SDK browser suite exercises this exact example against packed core/web artifacts and a prepared binary peer. It verifies editing, Markdown paste, offline recovery, atomic chains, scoped subscriptions and sync attachment. Packages remain private; this example establishes browser mechanics, without a hosted service or native/device qualification.
