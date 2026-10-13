#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { isDeepStrictEqual } from 'node:util';

const defaultRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const marks = new Set(['bold', 'italic', 'strike', 'code', 'link']);
const actions = new Set(['insertText', 'insertParagraph', 'insertHardBreak', 'toggleMark', 'setSelection', 'backspace', 'deleteForward', 'undo', 'redo', 'pasteText', 'beginPaste', 'completePaste', 'remoteDeleteBlock', 'applyBatch', 'nativeInsert']);
const outcomes = new Set(['applied', 'rejected', 'no-op', 'selection-only', 'staged']);
const casePattern = /^[A-Z][A-Z0-9]*-[A-Z]?\d{2,}$/;
const taskPattern = /\b[A-Z][A-Z0-9]*-\d+\.\d+\b/g;
const claimKeys = /^(executed|passed|failed|skipped|pass|execution|executionStatus|runtimeResult|actualState|qualified|supported)$/i;
const nonempty = (value) => typeof value === 'string' && value.trim().length > 0;
const object = (value) => value !== null && typeof value === 'object' && !Array.isArray(value);

function shape(value, keys, at, errors) {
  if (!object(value)) { errors.push(`${at}: expected object`); return false; }
  for (const key of Object.keys(value)) if (!keys.includes(key)) errors.push(`${at}: unknown field ${key}`);
  for (const key of keys) if (!(key in value)) errors.push(`${at}: missing field ${key}`);
  return true;
}

function array(value, at, errors, required = false) {
  if (!Array.isArray(value)) { errors.push(`${at}: expected array`); return []; }
  if (required && !value.length) errors.push(`${at}: must not be empty`);
  return value;
}

function unique(values, at, errors) {
  if (new Set(values).size !== values.length) errors.push(`${at}: duplicate values`);
}

function boundary(text, offset) {
  if (!Number.isInteger(offset) || offset < 0 || offset > text.length) return false;
  return !(offset > 0 && offset < text.length && /[\uD800-\uDBFF]/.test(text[offset - 1]) && /[\uDC00-\uDFFF]/.test(text[offset]));
}

function selection(value, blocks, at, errors) {
  if (!shape(value, ['anchor', 'focus', 'affinity'], at, errors)) return;
  if (!['forward', 'backward'].includes(value.affinity)) errors.push(`${at}.affinity: invalid affinity`);
  for (const end of ['anchor', 'focus']) {
    const point = value[end];
    if (!shape(point, ['block', 'offset'], `${at}.${end}`, errors)) continue;
    const block = blocks.get(point.block);
    if (!block) errors.push(`${at}.${end}: unknown block ${point.block}`);
    else if (typeof block.text !== 'string' || !boundary(block.text, point.offset)) errors.push(`${at}.${end}: invalid UTF-16 boundary`);
  }
}

/** Validate a logical test projection, never an engine schema or executable oracle. */
export function validateState(state, at = 'state') {
  const errors = [];
  if (!shape(state, ['blocks', 'selection', 'pendingMarks'], at, errors)) return errors;
  const blocks = new Map();
  for (const [index, block] of array(state.blocks, `${at}.blocks`, errors, true).entries()) {
    const where = `${at}.blocks[${index}]`;
    if (!shape(block, ['id', 'kind', 'text', 'hardBreaks', 'marks'], where, errors)) continue;
    if (!nonempty(block.id)) errors.push(`${where}: invalid block id`);
    if (blocks.has(block.id)) errors.push(`${where}: duplicate block id ${block.id}`);
    blocks.set(block.id, block);
    if (!['paragraph', 'code'].includes(block.kind)) errors.push(`${where}: invalid block kind`);
    if (typeof block.text !== 'string' || !block.text.isWellFormed()) { errors.push(`${where}: text must be well-formed Unicode`); continue; }
    const breaks = array(block.hardBreaks, `${where}.hardBreaks`, errors);
    unique(breaks, `${where}.hardBreaks`, errors);
    for (const offset of breaks) if (!boundary(block.text, offset) || block.text[offset] !== '\n') errors.push(`${where}.hardBreaks: offset must point to LF`);
    if (block.kind === 'code' && breaks.length) errors.push(`${where}: code LF is not a hard break`);
    if (block.kind === 'paragraph' && [...block.text.matchAll(/\n/g)].some((match) => !breaks.includes(match.index))) errors.push(`${where}: paragraph LF must be declared as a hard break`);
    const ranges = array(block.marks, `${where}.marks`, errors);
    unique(ranges.map((mark) => JSON.stringify(mark)), `${where}.marks`, errors);
    for (const [markIndex, mark] of ranges.entries()) {
      const markAt = `${where}.marks[${markIndex}]`;
      if (!shape(mark, ['from', 'to', 'type'], markAt, errors)) continue;
      if (!marks.has(mark.type)) errors.push(`${markAt}: unknown mark`);
      if (!boundary(block.text, mark.from) || !boundary(block.text, mark.to) || mark.from >= mark.to) errors.push(`${markAt}: invalid UTF-16 mark range`);
    }
  }
  selection(state.selection, blocks, `${at}.selection`, errors);
  // null derives marks from the current context; [] explicitly suppresses them.
  if (state.pendingMarks !== null) {
    const pending = array(state.pendingMarks, `${at}.pendingMarks`, errors);
    unique(pending, `${at}.pendingMarks`, errors);
    if (pending.some((mark) => !marks.has(mark))) errors.push(`${at}.pendingMarks: unknown mark`);
  }
  return errors;
}

function rejectExecutionClaims(value, at, errors) {
  if (!value || typeof value !== 'object') return;
  for (const [key, child] of Object.entries(value)) {
    if (claimKeys.test(key)) errors.push(`${at}.${key}: execution/support claims are forbidden in a plan`);
    rejectExecutionClaims(child, `${at}.${key}`, errors);
  }
}

/** Check handwritten expectations and structural invariants without running actions. */
export function validateRecipe(recipe, { catalogIds = new Set(), at = 'recipe' } = {}) {
  const errors = [];
  rejectExecutionClaims(recipe, at, errors);
  if (!shape(recipe, ['schemaVersion', 'id', 'layer', 'covers', 'requires', 'context', 'initial', 'steps'], at, errors)) return errors;
  if (recipe.schemaVersion !== 1) errors.push(`${at}: schemaVersion must be 1`);
  if (!/^SEQ-\d{2,}$/.test(recipe.id)) errors.push(`${at}: invalid recipe id`);
  if (!['semantic', 'browser-replay'].includes(recipe.layer)) errors.push(`${at}: invalid layer`);
  const covers = array(recipe.covers, `${at}.covers`, errors, true);
  unique(covers, `${at}.covers`, errors);
  for (const id of covers) if (!catalogIds.has(id)) errors.push(`${at}.covers: unknown case ${id}`);
  const requires = array(recipe.requires, `${at}.requires`, errors, true);
  unique(requires, `${at}.requires`, errors);
  if (requires.some((item) => !nonempty(item))) errors.push(`${at}.requires: expected nonempty strings`);
  if (shape(recipe.context, ['document', 'editor', 'epoch'], `${at}.context`, errors)) {
    if (!nonempty(recipe.context.document) || !nonempty(recipe.context.editor) || !Number.isInteger(recipe.context.epoch) || recipe.context.epoch < 0) errors.push(`${at}.context: invalid document, editor or epoch`);
  }
  errors.push(...validateState(recipe.initial, `${at}.initial`));
  let previous = recipe.initial;
  const stepIds = new Set();
  for (const [index, step] of array(recipe.steps, `${at}.steps`, errors, true).entries()) {
    const where = `${at}.steps[${index}]`;
    if (!shape(step, ['id', 'action', 'expect'], where, errors)) continue;
    if (!nonempty(step.id)) errors.push(`${where}: invalid step id`);
    if (stepIds.has(step.id)) errors.push(`${where}: duplicate step id ${step.id}`);
    stepIds.add(step.id);
    if (!object(step.action) || !actions.has(step.action.type)) errors.push(`${where}: unknown action type`);
    if (!shape(step.expect, ['outcome', 'state', 'effects'], `${where}.expect`, errors)) continue;
    const expected = step.expect;
    if (!outcomes.has(expected.outcome)) errors.push(`${where}: unknown outcome`);
    errors.push(...validateState(expected.state, `${where}.expect.state`));
    if (shape(expected.effects, ['localCommits', 'remoteCommits'], `${where}.expect.effects`, errors)) {
      const counts = Object.values(expected.effects);
      if (counts.some((count) => !Number.isInteger(count) || count < 0)) errors.push(`${where}: commit counts must be nonnegative integers`);
      else if (expected.outcome === 'applied' && counts.every((count) => count === 0)) errors.push(`${where}: applied outcome requires a commit`);
      else if (expected.outcome !== 'applied' && counts.some((count) => count !== 0)) errors.push(`${where}: non-applied outcome must have zero commits`);
    }
    if (['rejected', 'no-op'].includes(expected.outcome) && !isDeepStrictEqual(previous, expected.state)) errors.push(`${where}: ${expected.outcome} must preserve state`);
    if (['selection-only', 'staged'].includes(expected.outcome) && !isDeepStrictEqual(previous?.blocks, expected.state?.blocks)) errors.push(`${where}: ${expected.outcome} must preserve document blocks`);
    // Intentionally invalid arguments are permitted only for rejection fixtures.
    if (object(step.action) && expected.outcome !== 'rejected') {
      if (['insertText', 'pasteText', 'nativeInsert'].includes(step.action.type) && typeof step.action.text !== 'string') errors.push(`${where}.action: text is required`);
      if (step.action.type === 'toggleMark' && !marks.has(step.action.mark)) errors.push(`${where}.action: valid mark is required`);
      if (step.action.type === 'setSelection') selection(step.action.selection, new Map((Array.isArray(previous?.blocks) ? previous.blocks : []).filter(object).map((block) => [block.id, block])), `${where}.action.selection`, errors);
    }
    previous = expected.state;
  }
  return errors;
}

export function validateSuite({ root = defaultRoot, manifest } = {}) {
  const errors = [];
  const report = { kind: 'planning-validation', cases: 0, recipes: 0, steps: 0, guards: 0, errors };
  let base;
  try { base = fs.realpathSync(root); } catch (error) { errors.push(`root: ${error.message}`); return report; }
  function read(relative) {
    if (!nonempty(relative) || path.isAbsolute(relative) || relative.includes('\\') || /^[a-z][a-z0-9+.-]*:/i.test(relative)) throw new Error(`invalid root-relative path: ${relative}`);
    const resolved = path.resolve(base, relative);
    const inside = (target) => target !== base && !path.relative(base, target).startsWith(`..${path.sep}`) && path.relative(base, target) !== '..' && !path.isAbsolute(path.relative(base, target));
    if (!inside(resolved)) throw new Error(`path escapes root: ${relative}`);
    if (!inside(fs.realpathSync(resolved))) throw new Error(`path escapes root through symlink: ${relative}`);
    return fs.readFileSync(resolved, 'utf8');
  }
  try { manifest ??= JSON.parse(read('tests/editing-suite/suite.json')); } catch (error) { errors.push(error.message); return report; }
  rejectExecutionClaims(manifest, 'manifest', errors);
  if (!shape(manifest, ['schemaVersion', 'kind', 'status', 'catalogs', 'recipes', 'guards'], 'manifest', errors)) return report;
  if (manifest.schemaVersion !== 1 || manifest.kind !== 'editing-regression-plan' || manifest.status !== 'planned') errors.push('manifest: must be schemaVersion 1, editing-regression-plan, planned');
  const owners = new Set();
  try {
    for (const file of fs.readdirSync(path.join(base, 'roadmaps')).filter((name) => name.endsWith('.md'))) {
      for (const match of read(`roadmaps/${file}`).matchAll(/^### Task ([A-Z][A-Z0-9]*-\d+\.\d+)(?:\s|$)/gm)) owners.add(match[1]);
    }
  } catch (error) { errors.push(`roadmaps: ${error.message}`); }
  const catalogIds = new Set();
  const catalogPaths = [];
  for (const catalog of array(manifest.catalogs, 'manifest.catalogs', errors, true)) {
    if (!shape(catalog, ['path', 'expectedCases'], 'catalog', errors)) continue;
    catalogPaths.push(catalog.path);
    if (!Number.isInteger(catalog.expectedCases) || catalog.expectedCases < 1) errors.push(`${catalog.path}: expectedCases must be positive`);
    let count = 0;
    try {
      let headingOwners = [];
      for (const line of read(catalog.path).split(/\r?\n/)) {
        if (/^#{1,6}\s/.test(line)) {
          headingOwners = line.match(taskPattern) ?? [];
          for (const owner of headingOwners) if (!owners.has(owner)) errors.push(`${catalog.path}: unknown owner ${owner}`);
        }
        const id = line.match(/^\|\s*([^|]+?)\s*\|/)?.[1];
        if (!id || !casePattern.test(id)) continue;
        count++;
        if (!headingOwners.length) errors.push(`${catalog.path}: ${id} has no owning task heading`);
        if (catalogIds.has(id)) errors.push(`${catalog.path}: duplicate case id ${id}`);
        catalogIds.add(id);
      }
      if (count !== catalog.expectedCases) errors.push(`${catalog.path}: expected ${catalog.expectedCases} cases, found ${count}`);
      if (!count) errors.push(`${catalog.path}: zero catalog cases`);
      report.cases += count;
    } catch (error) { errors.push(`${catalog.path}: ${error.message}`); }
  }
  unique(catalogPaths, 'manifest.catalogs paths', errors);
  const recipePaths = array(manifest.recipes, 'manifest.recipes', errors, true);
  unique(recipePaths, 'manifest.recipes paths', errors);
  const recipeIds = new Set();
  for (const file of recipePaths) {
    try {
      const recipe = JSON.parse(read(file));
      errors.push(...validateRecipe(recipe, { catalogIds, at: file }));
      if (recipeIds.has(recipe?.id)) errors.push(`${file}: duplicate recipe id ${recipe?.id}`);
      recipeIds.add(recipe?.id);
      report.recipes++;
      report.steps += Array.isArray(recipe?.steps) ? recipe.steps.length : 0;
    } catch (error) { errors.push(`${file}: ${error.message}`); }
  }
  const guardIds = new Set();
  for (const guard of array(manifest.guards, 'manifest.guards', errors, true)) {
    if (!shape(guard, ['id', 'title', 'owner', 'negativeControl'], 'guard', errors)) continue;
    if (Object.values(guard).some((value) => !nonempty(value))) errors.push('guard: all fields require nonempty strings');
    if (guardIds.has(guard.id)) errors.push(`guard: duplicate guard id ${guard.id}`);
    guardIds.add(guard.id);
    if (!owners.has(guard.owner)) errors.push(`guard ${guard.id}: unknown owner ${guard.owner}`);
    report.guards++;
  }
  return report;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const args = process.argv.slice(2);
  const report = args.length ? { kind: 'planning-validation', errors: ['Usage: node scripts/validate-editing-suite.mjs'] } : validateSuite();
  console.log(JSON.stringify(report, null, 2));
  process.exitCode = report.errors.length ? 1 : 0;
}
