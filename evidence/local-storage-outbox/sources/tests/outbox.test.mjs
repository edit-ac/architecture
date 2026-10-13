import assert from 'node:assert/strict';
import { test, after } from 'node:test';
import { readFile, writeFile, mkdir, mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { chromium } from 'playwright';
import { init } from '../packages/core/dist/index.js';
import { UpdateJournal } from '../packages/web/dist/storage/journal.js';
import { CheckpointStorage } from '../packages/web/dist/storage/checkpoint.js';
import { UpdateOutbox, durableReceiptProtocol } from '../packages/web/dist/storage/outbox.js';
import { CheckpointIndexedDB } from './helpers/checkpoint-storage.mjs';

const output = process.env.EDITAC_OUTBOX_OUTPUT ?? await mkdtemp(join(tmpdir(), 'editac-outbox-'));
await mkdir(output, { recursive: true });
const facts = { cases: [], processes: [] };
function check(name, fn) { test(name, async () => { const c = { name, passed: false }; facts.cases.push(c); await fn(); c.passed = true; }); }
const tick = () => new Promise(resolve => setImmediate(resolve));
const runtime = await init('data:application/wasm;base64,' + (await readFile(new URL('../packages/core/dist/wasm/editac_wasm_bg.wasm', import.meta.url))).toString('base64'));
const options = { profile: 'v5', documentId: '45678901-4567-4567-8567-45678901abcd', epoch: '56789012-5678-4678-8678-56789012abcd', nodes: [{ text: 'a😀b' }] };
const engine = runtime.createEngine(options), initial = engine.checkpoint(), updates = [];
const sub = engine.subscribe({ type: 'updates' }, p => { if (p.update) updates.push({ identity: p.identity, writerId: p.writerId, sequence: p.sequence, origin: p.origin, bytes: p.update.bytes }); });
for (const word of ['B','C']) { const a = engine.anchor(engine.read().visible[0].id, 3, 'right'); engine.commit(engine.prepare({ kind: 'text', origin: 'outbox:test', command: { type: 'insert', at: a, text: word } })); engine.releaseAnchor(a); }
const latest = engine.checkpoint(); sub.dispose(); engine.dispose();
const receipt = entry => ({ protocol: durableReceiptProtocol, state: 'durable', identity: { ...entry.identity }, writerId: entry.writerId, sequence: entry.sequence, checksum: entry.checksum, updateId: entry.updateId });
async function commit(db, operation) { const p = operation(); const tx = await db.nextWrite(); await tick(); tx.complete(); return p; }
async function setup(capability = durableReceiptProtocol) {
  const db = new CheckpointIndexedDB(), journal = await UpdateJournal.open(db), points = await CheckpointStorage.open(db), outbox = await UpdateOutbox.open(db, 'test', capability);
  await commit(db, () => points.publish(initial, []));
  for (const update of updates) await commit(db, () => journal.append(update));
  const entries = await journal.read(initial.identity);
  return { db, journal, points, outbox, entries };
}
function restore(state) { const e = runtime.restoreEngine(initial.identity, state.checkpoint, state.tail.map(u => ({ identity: u.identity, bytes: u.bytes }))); try { return e.read().visible[0].runs.map(r => r.text).join(''); } finally { e.dispose(); } }
facts.fixtures = { initial: { ...initial, bytes: Array.from(initial.bytes) }, latest: { ...latest, bytes: Array.from(latest.bytes) }, updates: updates.map(u => ({ ...u, bytes: Array.from(u.bytes) })) };

check('deterministic checkpoint coverage retains every pending identity and retransmittable real update', async () => {
  const { db, points, outbox, entries } = await setup();
  await commit(db, () => points.publish(latest, entries.map(e => e.updateId)));
  assert.deepEqual(await outbox.pending(initial.identity), entries);
  assert.equal((await points.restore(initial.identity, restore)).value, 'a😀CBb');
  assert.equal(db.stores.receipts.size, 0);
});
check('deterministic sync events, socket delivery and state vectors cannot acknowledge updates', async () => {
  const { outbox, entries, db } = await setup();
  for (const event of [{ state: 'synced' }, { state: 'delivered' }, { stateVector: [1] }, { ...receipt(entries[0]), state: 'synced' }, { ...receipt(entries[0]), protocol: 'yjs-sync' }]) await assert.rejects(outbox.accept(event), { name: 'JournalIntegrityError' });
  assert.deepEqual(await outbox.pending(initial.identity), entries); assert.equal(db.stores.receipts.size, 0);
});
check('deterministic absent negotiated receipt capability reports unknown durability and retains updates', async () => {
  const { db, outbox, entries } = await setup(null);
  assert.equal(outbox.receiptProtocol, null);
  assert.equal((await outbox.accept(receipt(entries[0]))).reason, 'capability-unavailable');
  assert.deepEqual(await outbox.pending(initial.identity), entries); assert.equal(db.stores.receipts.size, 0);
});
for (const field of ['documentId','epoch','schema','profile','writerId','sequence','checksum','updateId']) check(`deterministic wrong receipt ${field} cannot prune pending updates`, async () => {
  const { db, outbox, entries } = await setup(); const r = receipt(entries[0]);
  if (field in r.identity) r.identity[field] = 'other'; else if (field === 'writerId' || field === 'sequence') r[field]++; else r[field] = field === 'checksum' ? '0'.repeat(64) : 'other';
  assert.equal((await commit(db, () => outbox.accept(r))).state, 'ignored');
  assert.deepEqual(await outbox.pending(initial.identity), entries); assert.equal(db.stores.receipts.size, 0);
});
check('deterministic receipt acknowledgment and pruning wait for completion, not request success', async () => {
  const { db, outbox, entries } = await setup(); const input = receipt(entries[0]);
  let settled = false; const p = outbox.accept(input).then(v => { settled = true; return v; }); input.identity.epoch = 'mutated'; input.updateId = 'mutated';
  const tx = await db.nextWrite(); await tick(); tx.requestSuccess();
  assert.equal(settled, false); assert.deepEqual(await outbox.pending(initial.identity), entries);
  tx.complete(); assert.deepEqual(await p, { state: 'remoteCommitted', updateId: entries[0].updateId });
  assert.deepEqual(await outbox.pending(initial.identity), [entries[1]]); assert.equal(db.stores.updates.size, 2);
});
for (const boundary of ['before-lookup','after-write-success']) check(`deterministic receipt abort ${boundary} retains outbox and permits retry`, async () => {
  const { db, outbox, entries } = await setup(); const p = outbox.accept(receipt(entries[0])); const rejection = assert.rejects(p, { name: 'AbortError' });
  const tx = await db.nextWrite(); if (boundary === 'after-write-success') { await tick(); tx.requestSuccess(); } tx.abort(); await rejection;
  assert.deepEqual(await outbox.pending(initial.identity), entries);
  assert.equal((await commit(db, () => outbox.accept(receipt(entries[0])))).state, 'remoteCommitted');
  assert.deepEqual(await outbox.pending(initial.identity), [entries[1]]);
});
check('deterministic quota, permission and receipt write failures propagate without pruning', async () => {
  const { db, outbox, entries } = await setup();
  for (const error of [new DOMException('quota', 'QuotaExceededError'), new DOMException('permission', 'SecurityError')]) {
    db.writeCreationError = error; await assert.rejects(outbox.accept(receipt(entries[0])), e => e === error); db.writeCreationError = null;
    db.putError = error; await assert.rejects(outbox.accept(receipt(entries[0])), e => e === error); db.putError = null; await db.nextWrite();
    assert.deepEqual(await outbox.pending(initial.identity), entries);
  }
});
check('deterministic duplicate/reordered durable receipts survive reopen and duplicate append', async () => {
  const { db, outbox, journal, points, entries } = await setup();
  for (const i of [1,1,0,1,0]) assert.equal((await commit(db, () => outbox.accept(receipt(entries[i])))).state, 'remoteCommitted');
  assert.deepEqual(await outbox.pending(initial.identity), []); assert.equal(db.stores.receipts.size, 2);
  await commit(db, () => journal.append(updates[0])); await commit(db, () => points.publish(latest, entries.map(e => e.updateId)));
  outbox.close(); const reopened = await UpdateOutbox.open(db, 'test', durableReceiptProtocol);
  assert.deepEqual(await reopened.pending(initial.identity), []); assert.equal((await points.restore(initial.identity, restore)).value, 'a😀CBb');
  assert.equal(db.stores.updates.size, 2);
});
check('deterministic unknown receipt cannot pre-acknowledge a future journal append', async () => {
  const reference = await setup();
  const db = new CheckpointIndexedDB(), journal = await UpdateJournal.open(db), outbox = await UpdateOutbox.open(db, 'future', durableReceiptProtocol);
  await commit(db, () => journal.append(updates[0]));
  assert.equal((await commit(db, () => outbox.accept(receipt(reference.entries[1])))).reason, 'unknown-update');
  assert.equal(db.stores.receipts.size, 0);
  await commit(db, () => journal.append(updates[1]));
  assert.deepEqual(await outbox.pending(initial.identity), reference.entries);
});
check('deterministic corrupt receipt or journal fails explicitly instead of hiding pending work', async () => {
  const { db, outbox, entries } = await setup(); await commit(db, () => outbox.accept(receipt(entries[0])));
  const marker = [...db.stores.receipts.values()][0]; marker.sequence++;
  await assert.rejects(outbox.pending(initial.identity), { name: 'JournalIntegrityError' }); marker.sequence--;
  [...db.stores.updates.values()][0].bytes[0] ^= 1;
  await assert.rejects(outbox.pending(initial.identity), { name: 'JournalIntegrityError' });
});
check('deterministic detached pending bytes and unsupported strict durability preserve identity', async () => {
  const { db, outbox, entries } = await setup(); const pending = await outbox.pending(initial.identity); pending[0].bytes.fill(0); pending[0].identity.epoch = 'mutated';
  assert.deepEqual(await outbox.pending(initial.identity), entries); db.strictSupported = false;
  assert.equal((await commit(db, () => outbox.accept(receipt(entries[0])))).state, 'remoteCommitted');
  assert.deepEqual(await outbox.pending(initial.identity), [entries[1]]);
});

let controller, browser;
check('actual Chromium v2 upgrade, receipt abort boundaries, checkpoint retention and restart preserve real Rust updates', async () => {
  controller = await chromium.launchServer({ headless: true }); const child = controller.process();
  facts.processes.push({ pid: child.pid, launcher: child.spawnfile, workspace: process.cwd(), purpose: 'outbox IndexedDB integration', port: null, log: 'full.log' });
  browser = await chromium.connect(controller.wsEndpoint()); facts.browser = { version: browser.version(), playwright: JSON.parse(await readFile(new URL('../node_modules/playwright/package.json', import.meta.url))).version };
  const context = await browser.newContext();
  try {
    await context.route('https://outbox.test/**', async route => {
      const path = new URL(route.request().url()).pathname;
      if (path === '/') return route.fulfill({ contentType: 'text/html', body: '<!doctype html><title>Outbox qualification</title>' });
      if (path.includes('..') || !/^\/(core|web)\//.test(path)) return route.abort();
      const prefix = path.startsWith('/core/') ? '../packages/core/dist/' : '../packages/web/dist/';
      await route.fulfill({ contentType: path.endsWith('.wasm') ? 'application/wasm' : 'text/javascript', body: await readFile(new URL(prefix + path.replace(/^\/(core|web)\//, ''), import.meta.url)) });
    });
    const page = await context.newPage(); await page.goto('https://outbox.test/');
    const result = await page.evaluate(async ({ options }) => {
      const { init } = await import('/core/index.js'), { UpdateJournal } = await import('/web/storage/journal.js'), { CheckpointStorage } = await import('/web/storage/checkpoint.js'), { UpdateOutbox, durableReceiptProtocol } = await import('/web/storage/outbox.js');
      const rt = await init('/core/wasm/editac_wasm_bg.wasm'), engine = rt.createEngine(options), initial = engine.checkpoint(), updates = [];
      const sub = engine.subscribe({ type: 'updates' }, p => { if (p.update) updates.push({ identity: p.identity, writerId: p.writerId, sequence: p.sequence, origin: p.origin, bytes: p.update.bytes }); });
      let journal, points, outbox;
      const nativePut = IDBObjectStore.prototype.put, nativeTransaction = IDBDatabase.prototype.transaction;
      let boundary = '', completed = 0; const errors = [], observed = [];
      const r = e => ({ protocol: durableReceiptProtocol, state: 'durable', identity: e.identity, writerId: e.writerId, sequence: e.sequence, checksum: e.checksum, updateId: e.updateId });
      try {
        // Seed the actual old v2 schema with an immutable update, then exercise production upgrade.
        for (const word of ['B','C']) { const a = engine.anchor(engine.read().visible[0].id, 3, 'right'); engine.commit(engine.prepare({ kind: 'text', origin: 'outbox:browser', command: { type: 'insert', at: a, text: word } })); engine.releaseAnchor(a); }
        const old = await new Promise((resolve, reject) => { const q = indexedDB.open('outbox-integration', 2); q.onupgradeneeded = () => { const s = q.result.createObjectStore('updates', { keyPath: ['identity.documentId','identity.epoch','identity.schema','writerId','sequence'] }); s.createIndex('documentEpochSchema', ['identity.documentId','identity.epoch','identity.schema']); q.result.createObjectStore('checkpoints'); }; q.onsuccess = () => resolve(q.result); q.onerror = () => reject(q.error); });
        try {
          const u = updates[0], hash = Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', u.bytes)), b => b.toString(16).padStart(2,'0')).join('');
          const identityKey = JSON.stringify(['profile','schema','documentId','epoch','protocolVersion','updateEncoding','offsets'].map(f => u.identity[f]));
          const entry = { ...u, checksum: hash, updateId: JSON.stringify([identityKey,u.writerId,u.sequence,hash]) };
          await new Promise((resolve, reject) => { const tx = old.transaction('updates','readwrite'); tx.objectStore('updates').add(entry); tx.oncomplete = resolve; tx.onabort = () => reject(tx.error); });
        } finally { old.close(); }
        journal = await UpdateJournal.open(indexedDB, 'outbox-integration'); points = await CheckpointStorage.open(indexedDB, 'outbox-integration'); outbox = await UpdateOutbox.open(indexedDB, 'outbox-integration', durableReceiptProtocol);
        observed.push((await outbox.pending(initial.identity)).length);
        await journal.append(updates[1]); const entries = await journal.read(initial.identity);
        await points.publish(initial, []); await points.publish(engine.checkpoint(), entries.map(e => e.updateId));
        observed.push((await outbox.pending(initial.identity)).length);
        const unknown = await UpdateOutbox.open(indexedDB, 'outbox-integration'); const absent = await unknown.accept(r(entries[0])); unknown.close();
        const wrong = await outbox.accept({ ...r(entries[0]), identity: { ...initial.identity, epoch: 'wrong' } });
        let syncRejected = false; try { await outbox.accept({ state: 'synced' }); } catch { syncRejected = true; }
        IDBDatabase.prototype.transaction = function(...args) { const tx = nativeTransaction.apply(this,args); if (args[1] === 'readwrite' && Array.isArray(args[0]) && args[0].includes('receipts')) tx.addEventListener('complete', () => completed++); return tx; };
        IDBObjectStore.prototype.put = function(...args) { const q = nativePut.apply(this,args); if (this.name === 'receipts' && boundary === 'before-success') this.transaction.abort(); if (this.name === 'receipts' && boundary === 'after-success') q.addEventListener('success', () => this.transaction.abort()); return q; };
        for (const phase of ['before-success','after-success']) { boundary = phase; try { await outbox.accept(r(entries[0])); } catch (e) { errors.push(e.name); } boundary = ''; observed.push((await outbox.pending(initial.identity)).length); }
        for (const i of [1,1,0,0]) { const before = completed; if ((await outbox.accept(r(entries[i]))).state !== 'remoteCommitted' || completed !== before + 1) throw Error('Receipt acknowledgment preceded completion'); }
        outbox.close(); outbox = await UpdateOutbox.open(indexedDB, 'outbox-integration', durableReceiptProtocol); await journal.append(updates[0]);
        observed.push((await outbox.pending(initial.identity)).length);
        const restored = await points.restore(initial.identity, state => { const e = rt.restoreEngine(initial.identity, state.checkpoint, state.tail.map(u => ({ identity:u.identity,bytes:u.bytes }))); try { return e.read().visible[0].runs.map(r => r.text).join(''); } finally { e.dispose(); } });
        return { observed, errors, completed, absent: absent.reason, wrong: wrong.state, syncRejected, content: restored.value, journalCount: (await journal.read(initial.identity)).length, entries: entries.map(e => ({ ...e, bytes: Array.from(e.bytes) })) };
      } finally { IDBObjectStore.prototype.put = nativePut; IDBDatabase.prototype.transaction = nativeTransaction; sub.dispose(); engine.dispose(); outbox?.close(); points?.close(); journal?.close(); }
    }, { options });
    assert.deepEqual(result.observed, [1,2,2,2,0]); assert.deepEqual(result.errors, ['AbortError','AbortError']); assert.equal(result.completed,4); assert.equal(result.absent,'capability-unavailable'); assert.equal(result.wrong,'ignored'); assert.equal(result.syncRejected,true); assert.equal(result.content,'a😀CBb'); assert.equal(result.journalCount,2); facts.integration = result;
  } finally { await context.close(); }
});
after(async () => { try { await browser?.close(); } finally { await controller?.close(); facts.teardown = { browserClosed: !browser?.isConnected(), browserProcessExited: !controller || controller.process().exitCode !== null, fixtureServersStarted: 0 }; await writeFile(join(output,'harness.json'), JSON.stringify(facts,null,2)); if (!process.env.EDITAC_OUTBOX_OUTPUT && facts.cases.every(c => c.passed)) await rm(output,{recursive:true}); } });
