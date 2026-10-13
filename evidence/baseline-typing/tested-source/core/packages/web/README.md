# @edit-ac/web

Private development package for the edit.ac browser input, selection, clipboard,
local recovery, and incremental DOM adapter. Its API is under development.
Build from the repository root with `npm run build` before importing `dist/`.

```ts
import { mountEditor } from '@edit-ac/web';

const editor = mountEditor(root, {
  assetUrl, databaseName, identity, indexedDB, locks: navigator.locks,
  label: 'Document editor',
});
await editor.ready;
const unsubscribe = editor.subscribe(state => {
  // ready and localCommitted represent different events.
});
await editor.flush({ target: 'local' });
unsubscribe();
await editor.destroy({ policy: 'flush' });
```

The host supplies an initialized document identity and local checkpoint through
the core/storage contracts. Mounting recovers that document before accepting
input. Existing preview DOM stays read-only and is replaced with authoritative
content and current selection mappings. Initialization failure exposes a readable
recovery view. A failed flush/destroy leaves `recoveryExport()` available; explicit
`destroy({ policy: 'report' })` returns the checkpoint and unsaved updates before
releasing resources. Repeated destruction is safe.

For an already initialized, host-owned engine, `mountEditorSurface(root, engine)`
mounts the same renderer, selection bridge and input adapters synchronously.
It exposes `settle()`, `setReadOnly()`, recovery records and `dispose()`. The host
retains the engine and disposes it after detaching the surface. Supply a `commit`
option to route prepared commands through host persistence; the default commits
to the engine only. The in-memory web examples use this public mount path.
Both mount paths reserve the root, including during asynchronous recovery.

The renderer preserves authored leading, trailing and repeated spaces on text
blocks, including headings and list items, without a host stylesheet. Prose uses
`white-space: break-spaces`; code blocks retain literal, unwrapped whitespace.
Hosts may style fonts and spacing while retaining these renderer-owned properties.
`npm run check:browser-baseline` builds the pinned WASM engine and packages, then runs the complete renderer,
keyboard and example suites in Chromium, Firefox and WebKit. It is part of the
workspace's `npm run check` gate.

Clipboard support includes versioned internal fragments, safe supported HTML,
native-menu and mobile input event routing, and literal paste. The optional
**Paste without formatting** button reads the script clipboard only on activation;
set `plainPasteControl: false` to supply your own labeled control. Hosts can call
`pastePlainText()` or `paste(data, { literal: true })` explicitly. Ctrl/Command+Shift+V
and macOS Command+Option+Shift+V request literal paste. It preserves destination
text style, including inline code, while bypassing incoming formatting and syntax
parsing. Denied script clipboard access leaves native paste available.

`clipboardCodecs` connects qualified format importers to the common prepared-edit
path. Full CommonMark/GFM, table/asset and other extension codecs have separate
roadmap gates; the minimal host does not claim that complete palette yet. Basic
platform-primary B/I/U and Shift+X formatting shortcuts use the semantic command
gate. Actual mobile OS clipboard, IME and screen-reader support requires device
qualification; deterministic browser replay is not device evidence.

Publishing is disabled until the implementation and release gates in
[edit-ac/architecture](https://github.com/edit-ac/architecture) pass.
License: Apache-2.0.
