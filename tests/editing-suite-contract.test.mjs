import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { validateRecipe, validateState, validateSuite } from '../scripts/validate-editing-suite.mjs';

const clone = (value) => structuredClone(value);
const state = (text = 'a😀', offset = text.length) => ({
  blocks: [{ id: 'p', kind: 'paragraph', text, hardBreaks: [], marks: [] }],
  selection: { anchor: { block: 'p', offset }, focus: { block: 'p', offset }, affinity: 'forward' },
  pendingMarks: [],
});
const recipe = () => ({
  schemaVersion: 1, id: 'SEQ-01', layer: 'semantic', covers: ['REG-01'], requires: ['prepared text commands'],
  context: { document: 'doc-a', editor: 'editor-a', epoch: 1 }, initial: state(),
  steps: [{ id: 's1', action: { type: 'insertText', text: 'b' }, expect: {
    outcome: 'applied', state: state('a😀b'), effects: { localCommits: 1, remoteCommits: 0 },
  } }],
});
const checkRecipe = (value) => validateRecipe(value, { catalogIds: new Set(['REG-01']) });
const has = (errors, pattern) => assert.ok(errors.some((error) => pattern.test(error)), `Missing ${pattern} in ${JSON.stringify(errors)}`);

function corpus(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'editac-suite-contract-'));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  const write = (file, content) => {
    fs.mkdirSync(path.dirname(path.join(root, file)), { recursive: true });
    fs.writeFileSync(path.join(root, file), typeof content === 'string' ? content : JSON.stringify(content));
  };
  write('roadmaps/track.md', '# Roadmap\n### Task INT-1.1 — Implement editing\n');
  write('tests/catalog.md', '# Cases\n## Contract — INT-1.1\n| ID | Result |\n|---|---|\n| REG-01 | Expected behavior |\n| A11-01 | Assistive behavior |\n| MWX-C01 | Optional capability |\n');
  write('tests/recipe.json', recipe());
  const manifest = {
    schemaVersion: 1, kind: 'editing-regression-plan', status: 'planned',
    catalogs: [{ path: 'tests/catalog.md', expectedCases: 3 }], recipes: ['tests/recipe.json'],
    guards: [{ id: 'G-01', title: 'Prepared commands', owner: 'INT-1.1', negativeControl: 'Reject a partial write' }],
  };
  write('tests/editing-suite/suite.json', manifest);
  return { root, write, manifest };
}

test('valid file corpus reports planning counts without runtime results', (t) => {
  const { root } = corpus(t);
  assert.deepEqual(validateSuite({ root }), { kind: 'planning-validation', cases: 3, recipes: 1, steps: 1, guards: 1, errors: [] });
});

test('duplicate catalog, recipe, step, guard and coverage IDs are rejected', (t) => {
  const { root, write, manifest } = corpus(t);
  write('tests/duplicate.md', '## Cases — INT-1.1\n| REG-01 | Duplicate |\n');
  manifest.catalogs.push({ path: 'tests/duplicate.md', expectedCases: 1 });
  manifest.guards.push(clone(manifest.guards[0]));
  const duplicated = recipe();
  duplicated.covers.push('REG-01');
  duplicated.steps.push(clone(duplicated.steps[0]));
  write('tests/recipe.json', duplicated);
  write('tests/second.json', recipe());
  manifest.recipes.push('tests/second.json');
  const errors = validateSuite({ root, manifest }).errors;
  for (const pattern of [/duplicate case id/, /duplicate recipe id/, /duplicate step id/, /duplicate guard id/, /covers: duplicate/]) has(errors, pattern);
});

test('unknown catalog owners, guard owners and coverage references fail', (t) => {
  const { root, write, manifest } = corpus(t);
  write('tests/catalog.md', '## Unknown — BAD-1.1\n| REG-01 | Expected |\n');
  manifest.catalogs[0].expectedCases = 1;
  manifest.guards[0].owner = 'BAD-1.2';
  const invalid = recipe(); invalid.covers = ['MISSING-01']; write('tests/recipe.json', invalid);
  const errors = validateSuite({ root, manifest }).errors;
  has(errors, /unknown owner BAD-1.1/); has(errors, /unknown owner BAD-1.2/); has(errors, /unknown case MISSING-01/);
});

test('catalog counts cannot hide missing or zero matching cases', (t) => {
  const { root, write, manifest } = corpus(t);
  has(validateSuite({ root, manifest: { ...manifest, catalogs: [{ path: 'tests/catalog.md', expectedCases: 4 }] } }).errors, /expected 4 cases, found 3/);
  write('tests/catalog.md', '# Empty catalog\n| ID | Result |\n');
  manifest.catalogs[0].expectedCases = 0;
  const errors = validateSuite({ root, manifest }).errors;
  has(errors, /expectedCases must be positive/); has(errors, /zero catalog cases/);
});

test('catalog rows need a parent-task owner heading', (t) => {
  const { root, write, manifest } = corpus(t);
  write('tests/catalog.md', '# Cases\n| REG-01 | Expected |\n');
  manifest.catalogs[0].expectedCases = 1;
  has(validateSuite({ root, manifest }).errors, /has no owning task heading/);
});

test('absolute, traversing and symlink paths cannot leave the architecture root', (t) => {
  const { root, manifest } = corpus(t);
  for (const file of ['../outside.json', '/tmp/outside.json', 'https://example.test/fixture.json']) {
    has(validateSuite({ root, manifest: { ...manifest, recipes: [file] } }).errors, /path escapes root|invalid root-relative path/);
  }
  fs.symlinkSync(os.tmpdir(), path.join(root, 'outside'));
  const outside = fs.mkdtempSync(path.join(os.tmpdir(), 'editac-suite-outside-'));
  t.after(() => fs.rmSync(outside, { recursive: true, force: true }));
  fs.writeFileSync(path.join(outside, 'recipe.json'), JSON.stringify(recipe()));
  has(validateSuite({ root, manifest: { ...manifest, recipes: [`outside/${path.basename(outside)}/recipe.json`] } }).errors, /escapes root through symlink/);
});

test('missing and malformed recipe files are validation errors', (t) => {
  const { root, write, manifest } = corpus(t);
  manifest.recipes = ['tests/missing.json'];
  assert.ok(validateSuite({ root, manifest }).errors.length > 0);
  write('tests/broken.json', '{'); manifest.recipes = ['tests/broken.json'];
  assert.ok(validateSuite({ root, manifest }).errors.length > 0);
});

test('execution claims and fabricated pass fields are forbidden at every recipe level', (t) => {
  const { root, manifest } = corpus(t);
  manifest.passed = 1;
  has(validateSuite({ root, manifest }).errors, /claims are forbidden/);
  for (const change of [
    (r) => { r.executed = true; },
    (r) => { r.steps[0].expect.passed = true; },
    (r) => { r.steps[0].action.args = { executionStatus: 'passed' }; },
  ]) {
    const invalid = recipe(); change(invalid); has(checkRecipe(invalid), /claims are forbidden/);
  }
});

test('unknown actions fail while intentional invalid arguments require a rejected result', () => {
  const invalid = recipe(); invalid.steps[0].action.type = 'inventInput'; has(checkRecipe(invalid), /unknown action type/);
  invalid.steps[0].action = { type: 'insertText', text: 42 }; has(checkRecipe(invalid), /text is required/);
  invalid.steps[0].expect = { outcome: 'rejected', state: clone(invalid.initial), effects: { localCommits: 0, remoteCommits: 0 } };
  assert.deepEqual(checkRecipe(invalid), []);
});

test('surrogate-interior selections, unknown blocks and malformed Unicode fail', () => {
  has(validateState(state('a😀', 2)), /invalid UTF-16 boundary/);
  const missing = state(); missing.selection.focus.block = 'deleted'; has(validateState(missing), /unknown block/);
  has(validateState(state('\ud800', 1)), /well-formed Unicode/);
});

test('marks and hard breaks must describe valid UTF-16 ranges and literal LF positions', () => {
  for (const mark of [{ from: 1, to: 2, type: 'bold' }, { from: 1, to: 1, type: 'bold' }, { from: 0, to: 99, type: 'bold' }, { from: 0, to: 1, type: 'invented' }]) {
    const invalid = state(); invalid.blocks[0].marks.push(mark); has(validateState(invalid), /mark range|unknown mark/);
  }
  const valid = state('a\nb'); valid.blocks[0].hardBreaks = [1]; assert.deepEqual(validateState(valid), []);
  const wrong = clone(valid); wrong.blocks[0].hardBreaks = [0]; has(validateState(wrong), /must point to LF/);
  const duplicate = clone(valid); duplicate.blocks[0].hardBreaks = [1, 1]; has(validateState(duplicate), /duplicate values/);
  const code = clone(valid); code.blocks[0].kind = 'code'; has(validateState(code), /code LF is not a hard break/);
  code.blocks[0].hardBreaks = []; assert.deepEqual(validateState(code), []);
});

test('coherent no-op, selection-only and staged outcomes forbid document commits', () => {
  for (const outcome of ['no-op', 'rejected', 'selection-only', 'staged']) {
    const invalid = recipe(); invalid.steps[0].expect.outcome = outcome;
    has(checkRecipe(invalid), /must have zero commits/);
    invalid.steps[0].expect.effects.localCommits = 0;
    has(checkRecipe(invalid), /must preserve state|must preserve document blocks/);
  }
  const invalid = recipe(); invalid.steps[0].expect.effects.localCommits = 0; has(checkRecipe(invalid), /applied outcome requires a commit/);
  invalid.steps[0].expect.effects.localCommits = -1; has(checkRecipe(invalid), /nonnegative integers/);
});

test('derived, suppressed and explicit pending marks stay distinct without mutating snapshots', () => {
  for (const pendingMarks of [null, [], ['bold']]) {
    const snapshot = state(); snapshot.pendingMarks = pendingMarks;
    const original = clone(snapshot);
    assert.deepEqual(validateState(snapshot), []);
    assert.deepEqual(snapshot, original);
  }
  for (const pendingMarks of [undefined, false, 'bold', {}]) {
    const snapshot = state(); snapshot.pendingMarks = pendingMarks;
    has(validateState(snapshot), /pendingMarks: expected array/);
  }
  const missing = state(); delete missing.pendingMarks;
  has(validateState(missing), /missing field pendingMarks/);

  // Losing an explicit suppression during a no-op is observable state loss.
  const lostOverride = recipe();
  lostOverride.steps[0].action = { type: 'backspace' };
  lostOverride.steps[0].expect = {
    outcome: 'no-op', state: clone(lostOverride.initial), effects: { localCommits: 0, remoteCommits: 0 },
  };
  lostOverride.steps[0].expect.state.pendingMarks = null;
  has(checkRecipe(lostOverride), /no-op must preserve state/);
  // Deliberate local mark-state changes are selection-only, without content commits.
  lostOverride.steps[0].action = { type: 'setSelection', selection: clone(lostOverride.initial.selection) };
  lostOverride.steps[0].expect.outcome = 'selection-only';
  assert.deepEqual(checkRecipe(lostOverride), []);
});

test('every expected snapshot is checked, including a corrupt final step', () => {
  const invalid = recipe();
  invalid.steps.push({ id: 's2', action: { type: 'insertText', text: 'c' }, expect: {
    outcome: 'applied', state: state('a😀bc', 2), effects: { localCommits: 1, remoteCommits: 0 },
  } });
  has(checkRecipe(invalid), /steps\[1\].expect.state.selection.*invalid UTF-16 boundary/);
});
