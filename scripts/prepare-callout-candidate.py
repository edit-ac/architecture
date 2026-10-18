#!/usr/bin/env python3
"""Append the qualified callout recipe as a separate immutable local candidate."""
import argparse
import copy
import importlib.util
import json
from pathlib import Path
import re
import subprocess

spec = importlib.util.spec_from_file_location('admission', Path(__file__).with_name('admit-local-candidates.py'))
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)


def prepare(core, output, receipt_path, commit, base="v3", version="v4", ident="structural-callout-v1", summary_name="callout-receipt.json"):
    previous = output / f'local-candidates-{base}.json'
    a.admit(previous, core, a.digest(previous.read_bytes()))
    result = copy.deepcopy(json.loads(previous.read_bytes()))
    receipt = json.loads(receipt_path.read_bytes())
    a.require(receipt['counts'] == {'executed': 12, 'passed': 12, 'failed': 0, 'skipped': 0, 'omitted': 0}, 'Callout consumer is incomplete')
    a.require(receipt['installedMembersMatch'] and all(receipt['cleanup'].values()), 'Installed provenance or teardown missing')
    a.require(all(c['passed'] for c in receipt['cases']), 'Failed callout case')

    def blob(path):
        return subprocess.check_output(['git', '-C', str(core), 'show', commit + ':' + path])

    def freeze(target, data):
        path = output / target
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            a.require(path.read_bytes() == data, 'Refusing to replace frozen artifact: ' + target)
        else:
            path.write_bytes(data)
        return {'path': target, 'sha256': a.digest(data)}

    def frozen_json(target, value):
        return freeze(target, (json.dumps(value, indent=2) + '\n').encode())

    for pin in receipt['sources'] + receipt['engineBuild']['sources']:
        a.require(a.digest(blob(pin['path'])) == pin['sha256'], 'Consumer/build source differs from committed input: ' + pin['path'])
    tracked = subprocess.check_output(['git', '-C', str(core), 'ls-tree', '-r', '--name-only', commit], text=True).splitlines()
    paths = [p for p in tracked if p.startswith(('packages/core/src/', 'packages/web/src/', 'packages/markdown/src/', 'crates/'))
             or p in ['Cargo.toml', 'Cargo.lock', 'rust-toolchain.toml', 'scripts/build-wasm.mjs', 'scripts/share-wasm-glue.mjs', 'scripts/build-extension-runtime.mjs', 'scripts/build-math-assets.mjs', 'package.json', 'package-lock.json', 'tsconfig.json']
             or p.startswith(('examples/extensions/structural-callout/', 'tests/extension-dx/structural-callout'))
             or p == 'scripts/test-structural-callout.mjs'
             or p in [f'packages/{n}/{f}' for n in ['core', 'web', 'markdown'] for f in ['package.json', 'tsconfig.json']]]
    sources = frozen_json(ident + '/source-pins.json', [{'path': p, 'sha256': a.digest(blob(p))} for p in paths])
    candidate = {'id': ident, 'sourceCommit': commit, 'sources': sources, 'packages': [], 'runtime': [], 'proofs': [], 'artifacts': []}
    for package in receipt['packs']:
        path = Path(package['path'])
        data = path.read_bytes()
        a.require(a.digest(data) == package['sha256'], 'Qualified package changed')
        members = a.archive_members(path)
        a.require({n: a.digest(b) for n, b in members.items()} == package['members'], 'Qualified package members changed')
        candidate['packages'].append({**freeze(ident + '/packages/' + path.name, data),
                                     'name': package['name'], 'version': package['version'], 'published': False,
                                     'bytes': len(data), 'members': package['members']})
        for name, content in members.items():
            if '/dist/wasm/' in name or name == 'package/dist/engine.js':
                candidate['runtime'].append({'package': package['name'], 'member': name, 'sha256': a.digest(content)})
    names = [c['name'] for c in receipt['cases']]
    packages = [p['name'] for p in candidate['packages']]
    candidate['proofs'].append({**freeze(ident + '/consumer.json', receipt_path.read_bytes()), 'id': 'callout', 'kind': 'retained-production-consumer', 'binding': 'packs-sha256', 'packages': packages, 'requiredCases': names})
    ranges = []
    for path, marker, length in [
        ('crates/editac-core/src/commands/editor.rs', '                EditorCommand::AtomicContent {', 135),
        ('crates/editac-core/src/modules/content.rs', '            Self::Callout { kind, body, source } => {', 10),
        ('crates/editac-markdown/src/optional.rs', 'fn apply_callouts(', 90),
        ('packages/web/src/extensions/authoring.ts', 'export const Extension =', 60),
        ('packages/core/src/extensions/registry.ts', 'export class ModuleRegistry', 65),
    ]:
        lines = blob(path).splitlines(keepends=True)
        start = next(i for i, line in enumerate(lines) if marker.encode() in line)
        end = min(start + length, len(lines))
        ranges.append({'path': path, 'start': start + 1, 'end': end, 'sha256': a.digest(b''.join(lines[start:end]))})
    recipe_path = 'examples/extensions/structural-callout/recipe.mjs'
    candidate['recipes'] = [{'id': 'project-kickoff-callout-v1', 'gitPath': recipe_path,
                            'source': freeze(ident + '/recipe.mjs', blob(recipe_path)),
                            'proof': 'callout', 'cases': names, 'ownerRanges': ranges}]
    candidate['artifacts'].append(freeze(ident + '/README.md', blob('examples/extensions/structural-callout/README.md')))
    candidate['artifacts'].append(frozen_json(ident + '/generated-build.json', receipt['engineBuild']))
    result['candidates'].append(candidate)
    for cell in result['cells']:
        if cell['id'] == 'structural-callout':
            cell.clear()
            cell.update(id='structural-callout', state='supported', candidate=candidate['id'], proof='callout', packages=packages, cases=names)
    if 'structural-callout' not in result['requiredCells']:
        result['requiredCells'].append('structural-callout')
    result['composition'] = 'Separate immutable candidate families. The structural-callout family contains its own current engine/WASM, web and Markdown packages. Do not mix same-version archives or infer optional-loader/framework/native/release support.'
    pin = frozen_json(f'local-candidates-{version}.json', result)
    checked = a.admit(output / pin['path'], core, pin['sha256'])
    native_log = (output / 'callout/checks/rust-2.log').read_text()
    native_runs = re.findall(r'test result: ok\. (\d+) passed; 0 failed; 0 ignored; 0 measured; 0 filtered out', native_log)
    a.require(len(native_runs) == 2 and sum(map(int, native_runs)) == 18, 'Native correctness checks incomplete')
    control_log = (output / 'callout/checks/admission-controls.log').read_text()
    a.require(re.search(r'Ran 22 tests', control_log) and control_log.rstrip().endswith('OK'), 'Admission controls incomplete')
    summary = {'task': 'LCR-1.2', 'scope': 'local-only', 'published': False, 'releaseQualified': False,
               'coreCommit': commit, 'manifest': pin, 'candidate': candidate['id'], 'counts': receipt['counts'],
               'native': {'executed': 18, 'passed': 18, 'failed': 0, 'skipped': 0, 'log': 'callout/checks/rust-2.log'},
               'admissionControls': {'executed': 22, 'passed': 22, 'failed': 0, 'skipped': 0, 'log': 'callout/checks/admission-controls.log'},
               'consumer': candidate['proofs'][0], 'ownerRanges': ranges, 'admission': checked,
               'failedEvidence': ['callout/checks/run-1/receipt.json', 'callout/checks/run-2/receipt.json', 'callout/checks/run-3/receipt.json', 'callout/checks/run-4/receipt.json', 'callout/checks/rust-1.log'],
               'boundary': 'Configured public authoring and advanced content presenter use separate sequential mounts of the same local document. Callout body is retained Markdown source, not a nested rich-text replica.',
               'cleanup': receipt['cleanup'], 'noOriginalReleasePlatformGateClosed': True}
    frozen_json(summary_name, summary)
    return {'manifest': pin, 'admission': checked, 'browser': receipt['counts']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--core', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--receipt', type=Path, required=True)
    parser.add_argument('--commit', required=True)
    parser.add_argument('--base', default='v3')
    parser.add_argument('--version', default='v4')
    parser.add_argument('--candidate', default='structural-callout-v1')
    parser.add_argument('--summary', default='callout-receipt.json')
    args = parser.parse_args()
    print(json.dumps(prepare(args.core.resolve(), args.output.resolve(), args.receipt.resolve(), args.commit, args.base, args.version, args.candidate, args.summary)))
