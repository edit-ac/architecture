#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath, pathToFileURL } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const roadmapDirectory = path.join(root, 'roadmaps');
const expectedVersion = '0.8.0';
const errors = [];
const report = { runnerVersion: expectedVersion, files: 0, tasks: 0, checkboxes: 0, contextLinks: 0, errors };
const fail = (message) => errors.push(message);
const readJson = (file) => JSON.parse(fs.readFileSync(file, 'utf8'));

async function main() {
  const args = process.argv.slice(2);
  let contract;
  if (args.length === 2 && args[0] === '--runner-contract' && path.isAbsolute(args[1])) {
    contract = args[1];
  } else if (args.length === 0) {
    const require = createRequire(import.meta.url);
    let packageFile;
    try { packageFile = require.resolve('@bpstr/roadmap-runner/package.json'); }
    catch { throw new Error('Install dependencies with npm ci, or provide --runner-contract /absolute/path/to/roadmap-runner/dist/roadmap-contract.js.'); }
    contract = path.join(path.dirname(packageFile), 'dist', 'roadmap-contract.js');
  } else {
    throw new Error('Usage: node scripts/validate-roadmaps.mjs [--runner-contract /absolute/path/to/dist/roadmap-contract.js]');
  }
  const runner = readJson(path.resolve(path.dirname(contract), '..', 'package.json'));
  if (runner.name !== '@bpstr/roadmap-runner' || runner.version !== expectedVersion) {
    throw new Error(`Expected @bpstr/roadmap-runner ${expectedVersion}; found ${runner.name} ${runner.version}. Review contract compatibility before upgrading.`);
  }
  const { validateRoadmap } = await import(pathToFileURL(contract).href);
  if (typeof validateRoadmap !== 'function') throw new Error('Runner contract does not export validateRoadmap().');

  const manifest = readJson(path.join(roadmapDirectory, 'manifest.json'));
  if (!Array.isArray(manifest.roadmaps) || !manifest.roadmaps.length) throw new Error('manifest.json must contain a nonempty roadmaps array.');
  const files = fs.readdirSync(roadmapDirectory).filter((file) => file.endsWith('.md')).sort();
  report.files = files.length;
  const entries = new Map();
  const prefixes = new Set();
  for (const entry of manifest.roadmaps) {
    if (!entry || typeof entry.file !== 'string' || !/^[A-Za-z0-9_.-]+\.md$/.test(entry.file)) {
      fail('Manifest file must be a Markdown filename relative to roadmaps/.');
      continue;
    }
    if (entries.has(entry.file)) fail(`${entry.file}: duplicate manifest entry`);
    entries.set(entry.file, entry);
    if (!files.includes(entry.file)) fail(`${entry.file}: manifest file does not exist`);
    if (typeof entry.prefix !== 'string' || !/^[A-Z][A-Z0-9]*$/.test(entry.prefix)) fail(`${entry.file}: invalid task prefix`);
    if (prefixes.has(entry.prefix)) fail(`${entry.file}: duplicate task prefix ${entry.prefix}`);
    prefixes.add(entry.prefix);
    if (!['core', 'cli', 'docs'].includes(entry.workspace)) fail(`${entry.file}: workspace must be core, cli or docs`);
    if (!Array.isArray(entry.upstream) || entry.upstream.some((file) => typeof file !== 'string')) fail(`${entry.file}: upstream must be an array of filenames`);
  }
  for (const file of files) if (!entries.has(file)) fail(`${file}: missing manifest entry`);
  for (const [file, entry] of entries) {
    if (!Array.isArray(entry.upstream)) continue;
    if (new Set(entry.upstream).size !== entry.upstream.length) fail(`${file}: duplicate upstream prerequisite`);
    for (const upstream of entry.upstream) if (!entries.has(upstream)) fail(`${file}: missing upstream roadmap ${upstream}`);
  }
  const visited = new Set();
  const active = new Set();
  function visit(file) {
    if (active.has(file)) { fail(`${file}: upstream roadmap dependency cycle`); return; }
    if (visited.has(file)) return;
    active.add(file);
    const upstream = entries.get(file)?.upstream;
    for (const next of Array.isArray(upstream) ? upstream : []) if (entries.has(next)) visit(next);
    active.delete(file);
    visited.add(file);
  }
  for (const file of entries.keys()) visit(file);

  const globalIds = new Map();
  for (const file of files) {
    const fullPath = path.join(roadmapDirectory, file);
    const text = fs.readFileSync(fullPath, 'utf8').replace(/\r\n/g, '\n');
    for (const error of validateRoadmap(text)) fail(`${file}: ${error}`);
    const statuses = [...text.matchAll(/^Status:.*$/gm)];
    const firstSection = text.search(/^#{2,}\s/m);
    if (statuses.length !== 1 || !/^Status: (IN_PROGRESS|COMPLETE|BLOCKED)$/.test(statuses[0]?.[0] || '') || (firstSection >= 0 && statuses[0]?.index >= firstSection)) {
      fail(`${file}: require exactly one Status: IN_PROGRESS, COMPLETE or BLOCKED line before the first section`);
    }
    const parents = [...text.matchAll(/^### Task ([A-Za-z0-9_.-]+)/gm)];
    report.tasks += parents.length;
    for (const parent of parents) {
      if (!parent[1].startsWith(`${entries.get(file)?.prefix}-`)) fail(`${file}: parent ${parent[1]} does not use its manifest prefix`);
    }
    for (const checkbox of text.matchAll(/^- \[[ x]\] ([A-Za-z0-9_.-]+)(?:\s|$)/gm)) {
      report.checkboxes++;
      const previous = globalIds.get(checkbox[1]);
      if (previous && previous !== file) fail(`${file}: checkbox ID ${checkbox[1]} also exists in ${previous}`);
      globalIds.set(checkbox[1], file);
    }
    // Verify explicit Markdown links in Context paragraphs. Implementation paths
    // may intentionally name files that a future task will create.
    for (const context of text.matchAll(/^Context:[^\n]*(?:\n(?!\s*$|[A-Za-z][A-Za-z ]*:|#)[^\n]+)*/gm)) {
      for (const link of context[0].matchAll(/\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)/g)) {
        const destination = link[1].replace(/^<|>$/g, '').split('#')[0];
        if (!destination || /^[a-z][a-z0-9+.-]*:|^\/\//i.test(destination)) continue;
        report.contextLinks++;
        if (path.isAbsolute(destination)) { fail(`${file}: Context link must be repository-relative: ${destination}`); continue; }
        let target;
        try { target = path.resolve(path.dirname(fullPath), decodeURIComponent(destination)); }
        catch { fail(`${file}: invalid Context link ${destination}`); continue; }
        if (!fs.existsSync(target)) fail(`${file}: missing Context link target ${destination}`);
      }
    }
  }
}

try { await main(); }
catch (error) { fail(error.message); }
console.log(JSON.stringify(report, null, 2));
process.exitCode = errors.length ? 1 : 0;
