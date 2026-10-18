#!/usr/bin/env python3
"""Install admitted packages offline in isolated consumers and exercise public imports/WASM."""
import argparse
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile

spec = importlib.util.spec_from_file_location('admission', Path(__file__).with_name('admit-local-candidates.py'))
admission = importlib.util.module_from_spec(spec)
spec.loader.exec_module(admission)


def run(manifest_path, core, expected, output):
    admission.admit(manifest_path, core, expected)
    output.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(manifest_path.read_bytes())
    results = []
    for candidate in manifest['candidates']:
        ident = candidate['id']
        target = output / ident
        admission.require(not target.exists(), 'Use fresh output; preserve failed evidence')
        target.mkdir()
        packs = [str((manifest_path.parent / p['path']).resolve()) for p in candidate['packages']]
        with tempfile.TemporaryDirectory(prefix='lcr-installed-', dir=output) as temporary:
            root = Path(temporary)
            (root / 'package.json').write_text('{"private":true,"type":"module"}')
            (root / 'consumer.mjs').write_bytes((Path(__file__).parents[1] / 'tests/local-candidate-installed-consumer.mjs').read_bytes())
            dependencies = ['react@19.3.0', 'react-dom@19.3.0', 'astro@7.3.8'] if ident == 'sdk-framework-v1' else []
            commands = [(['npm', 'install', '--offline', '--ignore-scripts', '--no-audit', '--no-fund', *packs, *dependencies], 'install.log'),
                        (['node', 'consumer.mjs', ident, str((target / 'runtime.json').resolve())], 'runtime.log')]
            for command, log in commands:
                with (target / log).open('wb') as stream:
                    result = subprocess.run(command, cwd=root, stdout=stream, stderr=subprocess.STDOUT, timeout=120)
                if result.returncode:
                    results.append({'candidate': ident, 'failedCommand': command[0:3], 'exit': result.returncode})
                    break
            else:
                receipt = json.loads((target / 'runtime.json').read_bytes())
                for package in candidate['packages']:
                    installed = root / 'node_modules' / package['name']
                    actual = {str(p.relative_to(installed)): admission.digest(p.read_bytes()) for p in installed.rglob('*') if p.is_file()}
                    expected_members = {n.removeprefix('package/'): h for n, h in package['members'].items()}
                    admission.require(actual == expected_members, 'Installed package differs from authenticated tarball')
                receipt['packs'] = [{'name': p['name'], 'sha256': p['sha256']} for p in candidate['packages']]
                receipt['cleanup']['temporaryConsumerRemoved'] = True
                receipt['installedMembersMatch'] = True
                (target / 'runtime.json').write_text(json.dumps(receipt, indent=2) + '\n')
                results.append({'candidate': ident, 'counts': receipt['counts']})
    (output / 'summary.json').write_text(json.dumps(results, indent=2) + '\n')
    admission.require(all('counts' in r and r['counts']['failed'] == 0 for r in results), 'Installed consumer failed; see retained output')
    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    parser.add_argument('--core', type=Path, required=True)
    parser.add_argument('--expected-sha256', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.manifest.resolve(), args.core.resolve(), args.expected_sha256, args.output.resolve())))
