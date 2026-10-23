// Finite DRA-1.1 design examples only. This is not the production table engine,
// a Yjs implementation, or evidence for DRA-1.2 concurrency/round-trip acceptance.
import assert from 'node:assert/strict';
import test from 'node:test';
import { readFileSync, existsSync } from 'node:fs';

const fixtures = JSON.parse(readFileSync(new URL('../fixtures/table-merge/cases.json', import.meta.url)));
const review = JSON.parse(readFileSync(new URL('../fixtures/table-merge/consumers.json', import.meta.url)));
const workspace = new URL('../../', import.meta.url);
const rank = a => [a.lamport, ...a.id.split(':').slice(1).map(BigInt)];
function compare(a, b) {
  const aa = rank(a), bb = rank(b);
  for (let i = 0; i < aa.length; i++) if (aa[i] !== bb[i]) return aa[i] < bb[i] ? -1 : 1;
  return 0;
}

// A deliberately finite reference for the authored cases: every splice addresses
// the common baseline. Arbitrary causal text edits must use actual Yrs/Yjs in
// DRA-1.2. No model result is called a production checkpoint or update.
function example(initial, delivered) {
  const unique = new Map();
  for (const action of delivered) {
    assert.match(action.id, /^e:[1-9][0-9]*:[1-9][0-9]*$/);
    assert.ok(Number.isSafeInteger(action.lamport) && action.lamport > 0);
    if (unique.has(action.id)) assert.deepEqual(unique.get(action.id), action, 'immutable event ID');
    unique.set(action.id, action);
  }
  const actions = [...unique.values()].sort(compare);
  const enabled = new Map(), undoneText = new Set();
  for (const action of actions) {
    if (action.kind === 'control' || action.kind === 'undo-text') {
      const target = unique.get(action.target);
      assert.ok(target && compare(target, action) < 0, 'causal control target');
      if (action.kind === 'undo-text') {
        assert.equal(target.kind, 'text');
        undoneText.add(action.target);
      } else {
        assert.notEqual(target.kind, 'control');
        enabled.set(action.target, action.enabled);
      }
    }
  }
  const rows = [...initial.rows], columns = [...initial.columns];
  const deletedRows = new Set(), deletedColumns = new Set();
  const attributes = {}, edits = new Map();
  const place = (list, action, birth) => {
    if (birth) assert.ok(!list.includes(action.axis), 'unique axis birth');
    else assert.ok(list.includes(action.axis), 'registered axis');
    for (const anchor of [action.left, action.right]) {
      if (anchor != null) assert.ok(list.includes(anchor) && anchor !== action.axis, 'registered gap');
    }
    const old = list.indexOf(action.axis);
    if (old >= 0) list.splice(old, 1);
    const index = action.right != null ? list.indexOf(action.right)
      : action.left != null ? list.indexOf(action.left) + 1 : list.length;
    list.splice(index, 0, action.axis);
  };
  for (const action of actions) {
    if (enabled.get(action.id) === false || undoneText.has(action.id)) continue;
    switch (action.kind) {
      case 'row': place(rows, action, true); break;
      case 'column': place(columns, action, true); break;
      case 'place-row': place(rows, action, false); break;
      case 'place-column': place(columns, action, false); break;
      case 'delete-row': assert.ok(rows.includes(action.axis)); deletedRows.add(action.axis); break;
      case 'delete-column': assert.ok(columns.includes(action.axis)); deletedColumns.add(action.axis); break;
      case 'attribute': attributes[`${action.scope}/${action.key}`] = structuredClone(action.value); break;
      case 'text': {
        const key = `${action.row}/${action.column}`;
        assert.ok(rows.includes(action.row) && columns.includes(action.column));
        const original = initial.cells[key] ?? '';
        assert.ok(Number.isInteger(action.at) && Number.isInteger(action.delete));
        assert.ok(action.at >= 0 && action.delete >= 0 && action.at + action.delete <= original.length);
        for (const at of [action.at, action.at + action.delete]) {
          assert.ok(!(at > 0 && at < original.length && /[\uD800-\uDBFF]/u.test(original[at - 1]) && /[\uDC00-\uDFFF]/u.test(original[at])), 'scalar-safe UTF-16 boundary');
        }
        const changes = edits.get(key) ?? [];
        changes.push(action); edits.set(key, changes);
        break;
      }
      case 'control': case 'undo-text': break;
      default: assert.fail(`Unspecified fixture action ${action.kind}`);
    }
  }
  const cells = {}, hidden = {};
  for (const row of rows) for (const column of columns) {
    const key = `${row}/${column}`, original = initial.cells[key] ?? '';
    const changes = edits.get(key) ?? [];
    let value = '';
    // Same baseline gap: the fixture's pinned Yjs rule orders insertions by
    // client ID. Lamport orders semantic events, never text-item ties.
    for (let i = 0; i <= original.length; i++) {
      const inserted = changes.filter(c => c.at === i).sort((a,b) => {
        const aa = BigInt(a.id.split(':')[1]), bb = BigInt(b.id.split(':')[1]);
        return aa === bb ? compare(a,b) : aa < bb ? -1 : 1;
      });
      value += inserted.map(c => c.insert).join('');
      if (i < original.length && !changes.some(c => c.at <= i && i < c.at + c.delete)) value += original[i];
    }
    (deletedRows.has(row) || deletedColumns.has(column) ? hidden : cells)[key] = value;
  }
  return {
    rows: rows.filter(row => !deletedRows.has(row)),
    columns: columns.filter(column => !deletedColumns.has(column)),
    cells, hidden, attributes,
    recovery: !rows.some(row => !deletedRows.has(row)) || !columns.some(column => !deletedColumns.has(column)) ? 'deleted-geometry' : undefined,
    extensions: structuredClone(initial.extensions), metadata: structuredClone(initial.metadata),
    retainedEvents: actions.map(a => a.id),
  };
}

for (const fixture of fixtures.cases) {
  test(`design only: ${fixture.id}`, () => {
    const { initial, actions, expected } = fixture;
    const results = [actions, [...actions].reverse(), [...actions.slice(1), actions[0], ...actions]]
      .map(order => example(initial, order));
    for (const actual of results) {
      assert.deepEqual(actual.rows, expected.rows);
      assert.deepEqual(actual.columns, expected.columns);
      for (const field of ['cells', 'hidden', 'attributes']) assert.deepEqual(actual[field], expected[field] ?? {});
      if (expected.recovery) assert.equal(actual.recovery, expected.recovery);
      for (const id of expected.retainedEvents ?? []) assert.ok(actual.retainedEvents.includes(id));
      assert.deepEqual(actual.extensions, initial.extensions);
      assert.deepEqual(actual.metadata, initial.metadata);
      assert.deepEqual(JSON.parse(JSON.stringify(actual)), JSON.parse(JSON.stringify(results[0])), 'finite design serialization/order consistency');
    }
    assert.equal(new Set(results[0].retainedEvents).size, actions.length, 'retain all authored events, including losers/undo');
  });
}

test('design field review includes every consumer family and existing source location', () => {
  assert.equal(review.parent, 'DRA-1.1');
  assert.equal(review.implementationOwner, 'DRA-1.2');
  assert.equal(new Set(fixtures.cases.map(c => c.id)).size, fixtures.cases.length);
  assert.equal(new Set(review.fields).size, review.fields.length);
  assert.equal(review.consumers.length, 5);
  assert.deepEqual(review.fieldRules.flatMap(rule => rule.fields).sort(), [...review.fields].sort());
  for (const consumer of review.consumers) {
    assert.deepEqual(consumer.fields, review.fields);
    assert.match(consumer.state, /implementation pending/);
    assert.ok(consumer.acceptance.length > 100);
    for (const path of consumer.sourcePaths) assert.ok(existsSync(new URL(path, workspace)), path);
  }
  assert.deepEqual(fixtures.descriptor.slice(0,2), ['module:editac.table',3]);
  assert.equal(fixtures.descriptor[2].tableId, fixtures.cases[0].initial.tableId);
});

test('finite design rejects a conflicting duplicate without changing fixture input', () => {
  const fixture = fixtures.cases[0], before = JSON.stringify(fixture);
  assert.throws(() => example(fixture.initial, [fixture.actions[0], {...fixture.actions[0], insert:'forged'}]), /immutable event ID/);
  assert.equal(JSON.stringify(fixture), before);
});


test('finite design rejects a split surrogate without changing fixture input', () => {
  const fixture = fixtures.cases.find(c => c.id === 'DRA-T17-utf16-same-cell');
  const before = JSON.stringify(fixture);
  assert.throws(() => example(fixture.initial, [{...fixture.actions[0], at:1}]), /scalar-safe UTF-16 boundary/);
  assert.equal(JSON.stringify(fixture), before);
});

test('serialized design examples cover exact record arities and text-root identities', () => {
  const data = JSON.parse(readFileSync(new URL('../fixtures/table-merge/serialized.json', import.meta.url)));
  const arities = {birth:4,row:6,column:6,'place-row':6,'place-column':6,'delete-row':4,'delete-column':4,block:9,'place-block':8,'delete-block':6,attribute:6,source:6,control:5};
  assert.equal(data.recordRoot, 'registry-table-records');
  const tags = new Set();
  for (const [id, record] of Object.entries(data.records)) {
    assert.match(id, /^e:[1-9][0-9]*:[1-9][0-9]*$/);
    assert.equal(record.length, arities[record[0]], record[0]);
    assert.equal(record[1], data.descriptor[2].tableId);
    tags.add(record[0]);
  }
  assert.deepEqual([...tags].sort(), Object.keys(arities).sort());
  for (const [name, value] of Object.entries(data.textRoots)) {
    const parts = name.split('/');
    assert.equal(parts.length, 5); assert.equal(parts[0], 'table-text');
    assert.equal(parts[1], data.descriptor[2].tableId); assert.equal(value.type, 'Y.Text');
  }
});
