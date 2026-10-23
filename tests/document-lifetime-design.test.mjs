// DRA-1.4 authored design checks. This finite schedule/graph/segment model does
// not execute Yrs, production replay, a checkpoint, a browser or a durable store.
// DRA-1.5 must run the specified fixtures on those actual boundaries.
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';

const read = path => readFileSync(new URL(path, import.meta.url), 'utf8');
const cases = JSON.parse(read('../fixtures/document-lifetime/cases.json'));
const consumers = JSON.parse(read('../fixtures/document-lifetime/consumers.json'));
const policy = read('../specs/structural-lifetime.md');
const workspaceRead = path => read(`../../${path}`);
const numericId = id => id.split(':').slice(1).map(BigInt);
function compareId(a, b) {
  const aa = numericId(a), bb = numericId(b);
  for (let i = 0; i < aa.length; i++) {
    if (aa[i] !== bb[i]) return aa[i] < bb[i] ? -1 : 1;
  }
  return 0;
}

// Each known dependency is visited once to index and once to release. A missing
// semantic version propagates dormancy; it does not suppress cycle validation.
function graph(records) {
  const byId = new Map(), degree = new Map(), children = new Map();
  const height = new Map(), dormant = new Map();
  let edges = 0, edgeVisits = 0;
  for (const record of records) {
    if (byId.has(record.id)) assert.deepEqual(byId.get(record.id), record);
    else byId.set(record.id, record);
  }
  for (const record of byId.values()) {
    let known = 0, missing = false;
    for (const dep of new Set(record.deps)) {
      if (!byId.has(dep)) { missing = true; continue; }
      known++; edges++; edgeVisits++;
      if (!children.has(dep)) children.set(dep, []);
      children.get(dep).push(record.id);
    }
    degree.set(record.id, known);
    height.set(record.id, 1);
    dormant.set(record.id, missing);
  }
  const queue = [...byId.keys()].filter(id => degree.get(id) === 0);
  for (let cursor = 0; cursor < queue.length; cursor++) {
    const id = queue[cursor];
    for (const child of children.get(id) ?? []) {
      edgeVisits++;
      height.set(child, Math.max(height.get(child), height.get(id) + 1));
      dormant.set(child, dormant.get(child) || dormant.get(id));
      degree.set(child, degree.get(child) - 1);
      if (degree.get(child) === 0) queue.push(child);
    }
  }
  if (queue.length !== byId.size) throw new Error('cycle');
  const ordered = [...byId.keys()].filter(id => !dormant.get(id)).sort((a, b) =>
    height.get(a) - height.get(b) || compareId(a, b));
  return { ordered, height, dormant, edges, edgeVisits };
}

// Tiny semantic schedule: all text cuts are the original source's offset zero.
// Counts preserve the empty segments that exact persisted span indices address.
// No binary sticky index, text convergence or witness admission is simulated.
function schedule(fixture) {
  let clock = fixture.operationFirstClock, originalVersion = 'base';
  let spanCount = 1, peakOwners = 1, maxInheritance = 0;
  const records = [], checkpoints = [], witnesses = { splits: 0, joins: 0 };
  const add = deps => {
    const id = `o:${fixture.operationWriter}:${clock++}`;
    records.push({ id, deps: [...new Set(deps.filter(v => v !== 'base'))] });
    if (fixture.saveAfterOperations.includes(records.length)) {
      checkpoints.push(records.length);
    }
    return id;
  };
  if (fixture.schedule === 'chained-place') {
    for (let n = 0; n < fixture.operations; n++) originalVersion = add([originalVersion]);
  } else {
    assert.equal(fixture.schedule, 'nested-splits-reverse-joins');
    for (let cycle = 0; cycle < fixture.cycles; cycle++) {
      const owners = [{ id: cases.initial.owner, version: originalVersion, spans: spanCount, inheritance: 0 }];
      for (let n = 0; n < fixture.splitsPerCycle; n++) {
        const left = owners.at(-1);
        const segmentIndex = n === 0 ? cycle * fixture.splitsPerCycle : fixture.laterSplitSpanIndex;
        assert.equal(segmentIndex, left.spans - 1, 'cut final original-source segment');
        const id = add([left.version]);
        left.version = id;
        // Split the full-text segment at zero. The left keeps a new empty
        // segment; right has the original nonempty segment, so left count stays.
        const right = { id, version: id, spans: 1, inheritance: left.inheritance + 1 };
        owners.push(right);
        witnesses.splits++;
        maxInheritance = Math.max(maxInheritance, right.inheritance);
        peakOwners = Math.max(peakOwners, owners.length);
      }
      while (owners.length > 1) {
        const right = owners.pop(), left = owners.at(-1);
        left.version = add([left.version, right.version]);
        left.spans += right.spans;
        witnesses.joins++;
      }
      originalVersion = owners[0].version;
      spanCount = owners[0].spans;
    }
  }
  return { records, checkpoints, spanCount, peakOwners, maxInheritance, witnesses, originalVersion };
}

test('current identity and resource budgets are explicit; no second stored format', () => {
  assert.equal(cases.kind, 'authored-design-inputs-not-runtime-evidence');
  assert.deepEqual([cases.identity.schema, cases.identity.profile, cases.identity.protocol,
    cases.identity.updateEncoding, cases.identity.offsets],
  ['editac.registry.editor.v5', 'editac.yrs-yjs.editor.v5', 1, 1, 'utf16']);
  assert.equal(cases.limits.restoreBytes, 16 * 1024 * 1024);
  assert.equal(cases.limits.decodedValues, 262144);
  assert.equal(cases.limits.decodedStructs, 262144);
  assert.equal(cases.limits.workUnits, 16777216);
  assert.equal(cases.limits.containerDepth, 128);
  assert.equal(cases.limits.uncoveredTailEntries, 4096);
  for (const phrase of ['Do not compact', 'skip_gc: true', 'not unlimited storage',
    'merged state', 'Controls affect application, not dependency heights',
    'No table event/text GC', 'deletion set', 'warm', 'DRA-1.5']) {
    assert.ok(policy.toLowerCase().includes(phrase.toLowerCase()), phrase);
  }
});

for (const fixture of cases.longSessions) {
  test(`${fixture.id}: authored 16384-operation schedule crosses counts, depth and save boundaries`, () => {
    const model = schedule(fixture), ranked = graph(model.records);
    assert.equal(model.records.length, 16384);
    assert.equal(model.records.length, fixture.expected.retainedOperations);
    assert.deepEqual(model.checkpoints, [4096, 8192, 12288, 16384]);
    assert.equal(model.originalVersion, fixture.expected.finalVersion);
    assert.equal(model.spanCount, fixture.expected.spans);
    assert.equal(ranked.ordered.length, fixture.expected.appliedOperations);
    assert.equal(ranked.height.get(model.originalVersion), fixture.expected.maximumOperationDepth);
    assert.equal(ranked.edgeVisits, 2 * ranked.edges, 'linear graph visits even on deep chain');
    assert.ok(ranked.edgeVisits < cases.limits.workUnits);
    // Count only immutable operation Any values, not encoded bytes or other
    // roots. Actual aggregate state accounting remains a runtime requirement.
    const operationValues = fixture.schedule === 'chained-place'
      ? fixture.operations * 8 : model.witnesses.splits * 9 + model.witnesses.joins * 10;
    assert.equal(operationValues, fixture.expected.operationAnyValues);
    assert.ok(operationValues < cases.limits.decodedValues);
    const reversed = graph([...model.records].reverse().concat(model.records.slice(0, 32)));
    assert.deepEqual(reversed.ordered, ranked.ordered, 'reorder/duplicate graph inputs');
    if (fixture.schedule === 'nested-splits-reverse-joins') {
      assert.equal(model.peakOwners, fixture.expected.peakVisibleOwners);
      assert.equal(model.maxInheritance, fixture.expected.maximumInheritanceDepth);
      assert.equal(model.witnesses.splits, fixture.expected.immutableSplitWitnesses);
      assert.equal(model.witnesses.joins, fixture.expected.immutableJoinWitnessPairs);
      assert.ok(model.maxInheritance > 128);
      assert.ok(model.spanCount > 8192, 'cannot retain old derived-span lifetime ceiling');
    }
  });
}

test('canonical numeric rank, unresolved dormancy and cycles preserve existing graph semantics', () => {
  const rows = [
    { id: 'o:2:10', deps: [] }, { id: 'o:2:2', deps: [] },
    { id: 'o:3:1', deps: ['o:2:10', 'o:2:10'] },
    { id: 'o:3:2', deps: ['o:99:1'] }, { id: 'o:3:3', deps: ['o:3:2'] },
  ];
  const model = graph(rows);
  assert.deepEqual(model.ordered, ['o:2:2', 'o:2:10', 'o:3:1']);
  assert.equal(model.dormant.get('o:3:3'), true);
  assert.equal(model.height.get('o:3:3'), 2);
  assert.throws(() => graph([
    { id: 'o:1:1', deps: ['o:1:2', 'o:99:1'], disabled: true },
    { id: 'o:1:2', deps: ['o:1:1'] },
  ]), /cycle/);
  assert.throws(() => graph([{ id: 'o:1:1', deps: ['o:1:1'] }]), /cycle/);
});

test('every retained root, exact table namespace and consumer review is source-located', () => {
  const replay = workspaceRead('core/crates/editac-core/src/editor_replay.rs');
  const table = workspaceRead('core/crates/editac-core/src/table.rs');
  const roots = [...replay.match(/pub const ROOTS[^=]*= \[([\s\S]*?)\];/)[1]
    .matchAll(/"([^"]+)"/g)].map(m => m[1]);
  assert.deepEqual(consumers.fixedRoots, [...roots, 'registry-table-records']);
  assert.ok(table.includes('"registry-table-records"'));
  assert.equal(consumers.textNamespace, 'table-text/<tableId>/<rowId>/<columnId>/<blockId>');
  for (const root of consumers.fixedRoots) assert.ok(policy.includes(root), root);
  assert.equal(new Set(consumers.reviews.map(r => r.id)).size, 12);
  for (const review of consumers.reviews) {
    for (const field of ['data', 'finding', 'requiredChange', 'bound', 'runtimeOwner']) {
      assert.ok(review[field], `${review.id}.${field}`);
    }
    assert.equal(review.runtimeOwner, 'DRA-1.5');
    for (const source of review.sources) {
      const text = workspaceRead(source.path);
      for (const marker of source.markers) assert.ok(text.includes(marker), `${source.path}: ${marker}`);
    }
  }
});

test('delayed peer, anchors, undo/review and storage fixtures retain separate acceptance', () => {
  assert.deepEqual(cases.initial.anchorUtf16Offsets, [0, 1, 3, 4]);
  assert.equal(cases.initial.text.length, 4);
  const peer = cases.crossBoundaryCases.find(c => c.id === 'LIFE-PEER');
  assert.equal(peer.rejoinAfterOperations, 16384);
  assert.equal(peer.disconnectAfterOperations, 0);
  assert.equal(peer.expectedText, 'APEER😀B');
  assert.equal(peer.expectedPeerPlaceOutcome, 'losing');
  assert.equal(peer.expectedPeerPlaceRetained, true);
  assert.deepEqual(peer.expectedAnchorOffsets, { left: [0, 1, 7, 8], right: [0, 5, 7, 8] });
  assert.deepEqual(peer.expectedUnknown, cases.initial.unknown);
  assert.equal(peer.deliveryOrders.length, 3);
  assert.equal(peer.peerActions.find(a => a.kind === 'insert-hidden-table-text').text, ' PEER');
  const controls = cases.crossBoundaryCases.find(c => c.id === 'LIFE-CONTROLS');
  assert.ok(controls.retainedDisabledOperations > 8192);
  const history = cases.crossBoundaryCases.find(c => c.id === 'LIFE-HISTORY');
  assert.ok(history.laterOperationOrigin.includes('not-local-history-capture'));
  assert.ok(history.reopen.includes('not-reconstructed'));
  assert.ok(history.staleReview.includes('no-mutation'));
  const storage = cases.crossBoundaryCases.find(c => c.id === 'LIFE-STORAGE');
  assert.equal(storage.publicationCycles, 4);
  assert.equal(storage.tailAtMost, 4096);
  assert.equal(storage.families.length, 3);
  assert.ok(storage.cases.includes('corrupt-required-tail-refuses'));
  assert.ok(storage.cases.includes('unacknowledged-outbox-preserved'));
  assert.ok(storage.outboundCapacity.includes('prepared-exact-peer-receipts'));
});

test('malformed/resource refusal fixtures keep atomic preservation and final ownership explicit', () => {
  assert.equal(new Set(cases.negativeCases.map(c => c.id)).size, 10);
  for (const fixture of cases.negativeCases) {
    assert.ok(fixture.input && fixture.error);
    assert.ok(policy.includes('before live mutation'));
  }
  assert.deepEqual(cases.allFailuresPreserve, [
    'checkpointBytes', 'observedRevisionIncludingDeletionSet', 'historyAvailability',
    'pendingOutboxAndReceipts', 'originalRecoveryInputBytes',
  ]);
  assert.ok(cases.plannedRuntimeTest.endsWith('/document_lifetime.rs'));
  assert.deepEqual(cases.requiredRuntimeOwners, ['DRA-1.5', 'QSH', 'QWB', 'QPF']);
  assert.match(policy, /512-deep ancestry and 8193 retained segments/);
  assert.match(policy, /Runtime fixture sizes\/counters must be measured/);
});
