#!/usr/bin/env node
// Source-only validation. Does not import, invoke or modify Roadmap Runner.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const directory = path.join(root, 'runner-queues/editor-ui-integrations-20261024');
const manifest = JSON.parse(fs.readFileSync(path.join(directory, 'manifest.json'), 'utf8'));
const errors = [];
const fail = message => errors.push(message);
const tasks = new Map();
const files = new Map();
const progress = new Set();
const external = new Map();
const fields = ['Purpose', 'Deliverable', 'Context', 'Entry receipts', 'Dependencies', 'Independent work', 'Session scope', 'Acceptance', 'Evidence', 'Handoff', 'Blocked behavior'];
const read = filename => fs.readFileSync(filename, 'utf8');
const slug = heading => heading.toLowerCase().replace(/[^\p{L}\p{N}\s_-]/gu, '').replace(/\s/g, '-');

if (manifest.status !== 'PLANNED' || !manifest.planningOnly || manifest.activeRunnerMutationAllowed !== false) fail('Manifest must remain explicitly planning-only.');
let sawFinal = false;
let maxBytes = 0;
let checkboxCount = 0;
for (const [index, entry] of manifest.roadmaps.entries()) {
  if (files.has(entry.file)) fail(`Duplicate file ${entry.file}`);
  const text = read(path.join(directory, entry.file));
  const bytes = Buffer.byteLength(text);
  maxBytes = Math.max(maxBytes, bytes);
  if (bytes > 24 * 1024) fail(`${entry.file}: exceeds 24 KiB source budget; split this milestone.`);
  if (!['functional', 'final-testing'].includes(entry.kind)) fail(`${entry.file}: unknown work kind`);
  if (entry.kind === 'final-testing') sawFinal = true;
  else if (sawFinal) fail(`${entry.file}: functional delivery follows final testing`);
  if (!/^\.roadmap-runner\/editor-ui-integrations-20261024\/.+\.progress\.md$/.test(entry.progress) || progress.has(entry.progress)) fail(`${entry.file}: invalid or duplicate progress path`);
  progress.add(entry.progress);
  if (!text.includes(`\`${entry.progress}\``)) fail(`${entry.file}: progress not documented`);
  if (!/^Status: (PLANNED|IN_PROGRESS|COMPLETE)$/m.test(text)) fail(`${entry.file}: missing status`);
  const headings = [...text.matchAll(/^### Task ([A-Z][A-Z0-9]*-\d+\.\d+) — (.+)$/gm)];
  if (headings.length !== entry.tasks.length || headings.length < 1 || headings.length > 10) fail(`${entry.file}: task count mismatch or oversized milestone`);
  files.set(entry.file, { ...entry, index, text });
  for (const [i, heading] of headings.entries()) {
    const id = heading[1];
    const block = text.slice(heading.index, headings[i + 1]?.index ?? text.length);
    const model = entry.tasks[i];
    if (model?.id !== id || !id.startsWith(`${entry.prefix}-`)) fail(`${entry.file}: manifest/heading mismatch ${id}`);
    if (tasks.has(id)) fail(`Duplicate parent ${id}`);
    const boxes = [...block.matchAll(/^- \[([ x])\] (\S+) /gm)];
    checkboxCount += boxes.length;
    if (!boxes.some(box => box[2] === id)) fail(`${id}: no standalone parent checkbox`);
    for (const suffix of ['-I1', '-I2', '-V1']) if (!boxes.some(box => box[2] === id + suffix)) fail(`${id}: missing ${suffix}`);
    if (new Set(boxes.map(box => box[2])).size !== boxes.length) fail(`${id}: duplicate substep`);
    for (const field of fields) if (!new RegExp(`^${field}: .+`, 'm').test(block)) fail(`${id}: missing ${field}`);
    for (const line of block.split('\n')) if (line.includes('- [') && !/^- \[[ x]\] /.test(line)) fail(`${id}: inline checkbox`);
    const actualDeps = block.match(/^Dependencies: (.+)\.$/m)?.[1];
    const expectedDeps = model?.dependencies.length ? model.dependencies.join(', ') : 'none';
    if (actualDeps !== expectedDeps) fail(`${id}: local dependencies differ from manifest`);
    const entryLine = block.match(/^Entry receipts: (.+)$/m)?.[1] ?? '';
    const actualEntries = [...entryLine.matchAll(/\[([A-Z][A-Z0-9]*-\d+\.\d+)\]/g)].map(match => match[1]);
    if (JSON.stringify(actualEntries) !== JSON.stringify(model?.entryReceipts)) fail(`${id}: entry receipts differ from manifest`);
    if (entry.prefix !== 'UIC' && !block.includes(`node scripts/ui-integration-delivery.mjs ${id}`)) fail(`${id}: missing focused selector`);
    tasks.set(id, { ...model, file: entry.file, kind: entry.kind, index, block });
  }
}

for (const owner of manifest.externalOwners) {
  if (external.has(owner.id)) fail(`Duplicate external owner ${owner.id}`);
  const filename = path.resolve(directory, owner.file);
  if (!fs.existsSync(filename)) fail(`${owner.id}: missing external source ${owner.file}`);
  else if (!read(filename).includes(`### Task ${owner.id} — `)) fail(`${owner.id}: external parent definition absent`);
  external.set(owner.id, owner);
}
for (const [id, task] of tasks) {
  for (const dependency of task.dependencies) {
    const target = tasks.get(dependency);
    if (!target || target.file !== task.file) fail(`${id}: nonlocal/missing dependency ${dependency}`);
  }
  for (const dependency of task.entryReceipts) {
    const target = tasks.get(dependency);
    if (target && target.index >= task.index) fail(`${id}: entry ${dependency} is not in an earlier file`);
    else if (!target && !external.has(dependency)) fail(`${id}: unknown external receipt ${dependency}`);
    if (task.kind === 'functional' && target?.kind === 'final-testing') fail(`${id}: functional work depends on final testing`);
    if (dependency === 'BNT-1.7') fail(`${id}: aggregate BNT closure is downstream of UI handoff, not an entry gate`);
  }
}
const colors = new Map();
function visit(id, chain = []) {
  if (colors.get(id) === 1) { fail(`Dependency cycle: ${[...chain, id].join(' -> ')}`); return; }
  if (colors.get(id) === 2) return;
  colors.set(id, 1);
  const task = tasks.get(id);
  for (const dependency of [...task.dependencies, ...task.entryReceipts]) if (tasks.has(dependency)) visit(dependency, [...chain, id]);
  colors.set(id, 2);
}
for (const id of tasks.keys()) visit(id);

const requirements = new Set();
const covered = new Set();
for (const requirement of manifest.requirements) {
  if (requirements.has(requirement.id)) fail(`Duplicate requirement ${requirement.id}`);
  requirements.add(requirement.id);
  if (!requirement.outcome || !requirement.implementation.length) fail(`${requirement.id}: empty acceptance mapping`);
  if (tasks.get(requirement.finalOwner)?.kind !== 'final-testing') fail(`${requirement.id}: missing unique final owner`);
  for (const id of requirement.implementation) {
    if (tasks.get(id)?.kind !== 'functional') fail(`${requirement.id}: invalid functional parent ${id}`);
    covered.add(id);
  }
  for (const id of requirement.existingEvidenceOwners) if (!external.has(id)) fail(`${requirement.id}: unknown existing evidence owner ${id}`);
}
for (const [id, task] of tasks) if (task.kind === 'functional' && !covered.has(id)) fail(`${id}: no requirement coverage`);
for (const name of fs.readdirSync(directory).filter(name => name.endsWith('.md'))) if (!files.has(name) && !['README.md', 'adoption-map.md'].includes(name)) fail(`Unlisted roadmap ${name}`);

let localLinks = 0;
const sources = [...fs.readdirSync(directory).filter(name => name.endsWith('.md')).map(name => path.join(directory, name)), path.join(root, 'specs/editor-ui-integrations.md'), path.join(root, 'specs/native-ui-integrations.md')];
for (const source of sources) {
  for (const match of read(source).matchAll(/\]\(([^)]+)\)/g)) {
    const href = match[1];
    if (/^https?:\/\//.test(href)) continue;
    localLinks++;
    const [relative, anchor] = href.split('#');
    const target = path.resolve(path.dirname(source), relative || path.basename(source));
    if (!fs.existsSync(target)) { fail(`${path.relative(root, source)}: missing link ${href}`); continue; }
    if (anchor && target.endsWith('.md')) {
      const anchors = [...read(target).matchAll(/^#{1,6} (.+)$/gm)].map(match => slug(match[1]));
      if (!anchors.includes(anchor)) fail(`${path.relative(root, source)}: missing heading ${href}`);
    }
  }
}
const report = { roadmaps: files.size, parents: tasks.size, checkboxes: checkboxCount, requirements: requirements.size, externalOwners: external.size, localLinks, maxSourceBytes: maxBytes, failures: errors.length };
console.log(JSON.stringify(report));
if (errors.length) { for (const error of errors) console.error(error); process.exitCode = 1; }
