#!/usr/bin/env python3
"""Freeze already qualified, requested local inputs without consuming moving dist/HEAD."""
import argparse
import importlib.util
import json
from pathlib import Path

spec = importlib.util.spec_from_file_location('admission', Path(__file__).with_name('admit-local-candidates.py'))
admission = importlib.util.module_from_spec(spec)
spec.loader.exec_module(admission)


def prepare(workspace, parallel, output, version):
    output.mkdir(parents=True, exist_ok=True)

    def freeze(path, target):
        destination = output / target
        destination.parent.mkdir(parents=True, exist_ok=True)
        data = path.read_bytes()
        if destination.exists():
            admission.require(destination.read_bytes() == data, 'Refusing to overwrite frozen artifact: ' + target)
        else:
            destination.write_bytes(data)
        return {'path': target, 'sha256': admission.digest(data)}

    def write_json(target, data):
        path = output / target
        path.parent.mkdir(parents=True, exist_ok=True)
        encoded = (json.dumps(data, indent=2) + '\n').encode()
        if path.exists():
            admission.require(path.read_bytes() == encoded, 'Use a new candidate version for changed inputs')
        else:
            path.write_bytes(encoded)
        return {'path': target, 'sha256': admission.digest(encoded)}

    candidates, cells = [], []
    sdk = workspace / 'architecture/evidence/extension-dx/owner-return-20261017'
    sdk_receipt = sdk / 'sdk-resources-receipt.json'
    admission.require(admission.digest(sdk_receipt.read_bytes()) ==
                      '69cabe850aac11b070c657e14bb1e66861e100a2473626fa8832a477f483faf5', 'Unrequested SDK receipt')
    authoring = parallel / 'architecture/evidence/extension-dx/documentation-20261018'
    authoring_receipt = authoring / 'receipt.json'
    admission.require(admission.digest(authoring_receipt.read_bytes()) ==
                      'f2cab41d7a56c1a86e2e2c9d2d6ab45d1048e52f9963a406cd38f520574aae9a', 'Unrequested EXT receipt')
    for ident, receipt_path, commit in [
        ('sdk-framework-v1', sdk_receipt, 'aa5b7d21064bd6d694ba243ffe528f58288b8a92'),
        ('extension-authoring-v1', authoring_receipt, '16a0a28048fd10e45284dce4b07331e3d0a15e6a'),
    ]:
        receipt = json.loads(receipt_path.read_bytes())
        candidate = {'id': ident, 'sourceCommit': commit, 'packages': [], 'runtime': [], 'proofs': [],
                     'artifacts': [freeze(receipt_path, ident + '/owner-receipt.json')]}
        if ident == 'sdk-framework-v1':
            packages = [{**p, 'path': str(sdk / 'sdk/consolidated' / p['file'])} for p in receipt['packages']]
            pins = [p for p in json.loads((sdk / 'sdk/source-pins.json').read_bytes()) if p['repository'] == 'core']
            proofs = [('framework', sdk / 'sdk/packed-final/harness.json', 'npm-integrity'),
                      ('production', sdk / 'sdk/consolidated/production/chromium/receipt.json', 'packs-sha256'),
                      ('recovery', sdk / 'sdk/consolidated/same-page/chromium/receipt.json', 'packs-sha256')]
            for name in ['final-packed-astro.log', 'packed-final/compiled-consumers.tgz']:
                candidate['artifacts'].append(freeze(sdk / 'sdk' / name, ident + '/' + name))
        else:
            packages = [{**p, 'name': '@edit-ac/' + p['name']} for p in receipt['testedPackages']]
            pins = receipt['sourcePins']
            proofs = [('authoring', authoring / 'checks/documentation-final/browser/receipt.json', 'testedPackages-sha256')]
        candidate['sources'] = write_json(ident + '/source-pins.json', pins)
        for package in packages:
            path = Path(package['path'])
            admission.require(admission.digest(path.read_bytes()) == package['sha256'], 'Owner package changed')
            pin = freeze(path, ident + '/packages/' + path.name)
            members = admission.archive_members(path)
            candidate['packages'].append({**pin, 'name': package['name'], 'version': package['version'],
                                          'bytes': path.stat().st_size, 'published': False,
                                          'members': {n: admission.digest(b) for n, b in sorted(members.items())}})
            for name, data in sorted(members.items()):
                if '/dist/wasm/' in name or name == 'package/dist/engine.js':
                    candidate['runtime'].append({'package': package['name'], 'member': name,
                                                 'sha256': admission.digest(data)})
        for proof_id, path, binding in proofs:
            data = json.loads(path.read_bytes())
            tested = data['packs'] if binding != 'testedPackages-sha256' else data['testedPackages']
            candidate['proofs'].append({**freeze(path, ident + '/' + proof_id + '.json'),
                                        'id': proof_id, 'kind': 'retained-production-consumer',
                                        'packages': [p['name'] if p['name'].startswith('@') else '@edit-ac/' + p['name'] for p in tested],
                                        'binding': binding, 'requiredCases': [c['name'] for c in data['cases']]})
        if version == 'v3':
            fresh = output / 'checks/installed-2' / ident / 'runtime.json'
            data = json.loads(fresh.read_bytes())
            candidate['proofs'].append({**freeze(fresh, ident + '/installed.json'),
                'id': 'installed', 'kind': 'retained-production-consumer', 'binding': 'packs-sha256',
                'packages': [p['name'] for p in candidate['packages']],
                'requiredCases': [c['name'] for c in data['cases']]})
        candidates.append(candidate)
    def supported(ident, candidate, proof, cases):
        owned = next(c for c in candidates if c['id'] == candidate)
        package_names = next(p['packages'] for p in owned['proofs'] if p['id'] == proof)
        cells.append({'id': ident, 'state': 'supported', 'candidate': candidate, 'proof': proof,
                      'cases': cases, 'packages': package_names})
    for family in ['native', 'react', 'astro-static', 'astro-ssr']:
        supported(family, 'sdk-framework-v1', 'framework', [e + '-' + family for e in ['chromium', 'firefox', 'webkit']])
    supported('ssr', 'sdk-framework-v1', 'production', ['SHR-04-ssr'])
    supported('navigation', 'sdk-framework-v1', 'production', ['SHR-05-client-task-document-back',
              'SHR-06-cold-full-navigation', 'SHR-06-warm-full-navigation', 'SHR-06-cache-disabled-full-navigation'])
    supported('lifecycle-recovery', 'sdk-framework-v1', 'recovery', ['SHR-03-disposed-waiter',
              'SHR-03-failure-retry', 'SHR-03-remount', 'SHR-03-pending-save', 'SHR-03-optional-retry'])
    authoring_cases = candidates[1]['proofs'][0]['requiredCases']
    supported('authoring-mark-atom-behavior', 'extension-authoring-v1', 'authoring', authoring_cases)
    if version == 'v3':
        supported('markdown-interchange', 'sdk-framework-v1', 'installed',
                  ['markdown-independent-format-roundtrip', 'markdown-disabled-unknown-source-retains-recovery'])
        supported('installed-production-engine', 'extension-authoring-v1', 'installed',
                  ['production-engine-invalid-asset-retry-and-current-wasm', 'production-checkpoint-reopen-and-disposal'])
    for ident, reason in [
        ('structural-callout', 'LCR-1.2: mark/atom and heading/bold codecs do not prove an original structural block.'),
        ('configured-react-astro', 'SDK framework receipts cover sdk-framework-v1 only, not newer facade combinations.'),
        ('optional-loading', 'PARALLEL LDR-1.1 owns changed-input absence-graph repair; not admitted here.'),
        ('native-hosts', 'Native/device/OS runtime proof is outside local authorization.'),
        ('cloud-service', 'No actual durable service/deployment consumer admitted.'),
        ('registry-release', 'No publication, registry or full EQL/roadmap10 release qualification authorized.'),
    ]:
        cells.append({'id': ident, 'state': 'pending', 'reason': reason})
    if version != 'v3':
        cells.append({'id': 'markdown-interchange', 'state': 'pending',
                      'reason': 'Requires independent admitted format outcomes; package presence is not semantic proof.'})
    manifest = {'schemaVersion': 1, 'scope': 'local-only', 'published': False, 'releaseQualified': False,
                'registryIdentity': None, 'candidates': candidates, 'cells': cells,
                'requiredCells': [c['id'] for c in cells if c['state'] == 'supported'],
                'composition': 'Separate immutable candidate families. Never mix their same-version packages or infer shared-main integration.',
                'docsConsumerCommit': '14a38259f73df08513cb2e36cea72acb5530d690'}
    if version == 'v3':
        mappings = []
        coordination = workspace.parent / 'edit-ac/.roadmap-coordination'
        for task in ['1.1', '1.2', '1.3', '1.4', '1.31', '1.32', '1.33', '1.34', '1.35-source']:
            request_path = coordination / 'requests' / ('local-docs-dwf-' + task + '-20261018.json')
            if not request_path.exists():
                request_path = coordination / ('local-docs-dwf-' + task + '-20261018/delivery.json')
            request = json.loads(request_path.read_bytes())
            path = Path(request['receipt']) if request.get('receipt') else Path(request['evidenceDirectory']) / 'receipt.json'
            raw = path.read_bytes()
            if request.get('receiptSha256'):
                admission.require(admission.digest(raw) == request['receiptSha256'], 'Docs receipt changed')
            receipt = json.loads(raw)
            commit = request.get('docsCommit', request.get('commit', receipt.get('docsCommit', receipt.get('commit'))))
            mappings.append({'task': request.get('task', request.get('gate', 'DWF-' + task)),
                             'docsCommit': commit, 'scope': 'source-prerequisite-only' if task == '1.35-source' else 'original-completed-prerequisite',
                             'delivery': freeze(request_path, 'docs-prerequisites/' + task + '-delivery.json'),
                             'receipt': freeze(path, 'docs-prerequisites/' + task + '-receipt.json')})
        manifest['docsPrerequisites'] = mappings
    return write_json('local-candidates-' + version + '.json', manifest)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--parallel-workspace', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--version', default='v2', choices=['v2', 'v3'])
    args = parser.parse_args()
    print(json.dumps(prepare(args.workspace.resolve(), args.parallel_workspace.resolve(), args.output.resolve(), args.version)))
