"""Deterministic adversarial controls; fixture receipts never claim real runtime proof."""
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tarfile
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('admission', Path(__file__).parents[1] / 'scripts/admit-local-candidates.py')
admission = importlib.util.module_from_spec(spec)
spec.loader.exec_module(admission)


class AdmissionControls(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='lcr-admission-control-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / 'core'
        self.repo.mkdir()
        def git(*args):
            return subprocess.check_output(['git', '-C', str(self.repo), *args], stderr=subprocess.DEVNULL).strip()
        git('init', '-q')
        (self.repo / 'engine.rs').write_text('// deterministic control\n')
        git('add', 'engine.rs')
        git('-c', 'user.name=Control', '-c', 'user.email=control@example.invalid', 'commit', '-qm', 'Add fixture')
        self.commit = git('rev-parse', 'HEAD').decode()
        self.members = {'package/package.json': json.dumps({'name': '@edit-ac/core', 'version': '0.0.0'}).encode(),
                        'package/dist/wasm/engine.wasm': b'deterministic control bytes, not a runtime'}
        with tarfile.open(self.root / 'core.tgz', 'w:gz') as archive:
            for name, data in self.members.items():
                info = tarfile.TarInfo(name)
                info.size = len(data)
                archive.addfile(info, io.BytesIO(data))
        pack = self.file('core.tgz')
        pack.update(name='@edit-ac/core', version='0.0.0', published=False,
                    bytes=(self.root / 'core.tgz').stat().st_size,
                    members={p: admission.digest(b) for p, b in self.members.items()})
        sources = self.json_file('sources.json', [{'path': 'engine.rs', 'sha256': admission.digest((self.repo / 'engine.rs').read_bytes())}])
        proof = self.json_file('proof.json', {'cases': [{'name': 'fixture-control', 'passed': True}],
                                             'packs': [{'name': '@edit-ac/core', 'sha256': pack['sha256']}],
                                             'counts': {'executed': 1, 'passed': 1, 'failed': 0, 'skipped': 0}})
        proof.update(id='fixture', kind='retained-production-consumer', binding='packs-sha256',
                     packages=['@edit-ac/core'], requiredCases=['fixture-control'])
        self.manifest = {'schemaVersion': 1, 'scope': 'local-only', 'published': False,
                         'releaseQualified': False, 'registryIdentity': None,
                         'candidates': [{'id': 'control', 'sourceCommit': self.commit, 'sources': sources,
                                         'packages': [pack], 'runtime': [{'package': '@edit-ac/core',
                                         'member': 'package/dist/wasm/engine.wasm',
                                         'sha256': admission.digest(self.members['package/dist/wasm/engine.wasm'])}], 'proofs': [proof]}],
                         'requiredCells': ['control'], 'cells': [{'id': 'control', 'state': 'supported',
                         'candidate': 'control', 'proof': 'fixture', 'packages': ['@edit-ac/core'], 'cases': ['fixture-control']}]}

    def test_unproved_package_combination(self):
        self.manifest['cells'][0]['packages'].append('@edit-ac/react')
        with self.assertRaisesRegex(ValueError, 'Cell packages lack'): self.run_admission()

    def file(self, name):
        return {'path': name, 'sha256': admission.digest((self.root / name).read_bytes())}

    def json_file(self, name, value):
        (self.root / name).write_text(json.dumps(value))
        return self.file(name)

    def run_admission(self, expected=None):
        pin = self.json_file('manifest.json', self.manifest)
        return admission.admit(self.root / 'manifest.json', self.repo, expected or pin['sha256'])

    def proof_change(self, change):
        path = self.root / 'proof.json'
        value = json.loads(path.read_text())
        change(value)
        self.manifest['candidates'][0]['proofs'][0].update(self.json_file('proof.json', value))

    def test_valid_control(self):
        self.assertEqual(self.run_admission()['sourceBlobs'], 1)

    def test_missing_package(self):
        (self.root / 'core.tgz').unlink()
        with self.assertRaises(FileNotFoundError): self.run_admission()

    def test_tampered_package(self):
        with (self.root / 'core.tgz').open('ab') as f: f.write(b'tampered')
        with self.assertRaisesRegex(ValueError, 'Artifact changed'): self.run_admission()

    def test_stale_manifest(self):
        with self.assertRaisesRegex(ValueError, 'Stale/unrequested'): self.run_admission('0' * 64)

    def test_fake_published_identity(self):
        self.manifest['published'] = True
        with self.assertRaisesRegex(ValueError, 'Fake published'): self.run_admission()

    def test_fake_registry_identity(self):
        self.manifest['registryIdentity'] = 'registry:fake'
        with self.assertRaisesRegex(ValueError, 'Fake published'): self.run_admission()

    def test_stale_source(self):
        self.manifest['candidates'][0]['sources'] = self.json_file('sources.json', [{'path': 'engine.rs', 'sha256': '0' * 64}])
        with self.assertRaisesRegex(ValueError, 'Source does not match'): self.run_admission()

    def test_member_inventory(self):
        self.manifest['candidates'][0]['packages'][0]['members'].pop('package/dist/wasm/engine.wasm')
        with self.assertRaisesRegex(ValueError, 'member inventory'): self.run_admission()

    def test_fake_version(self):
        self.manifest['candidates'][0]['packages'][0]['version'] = '1.0.0'
        with self.assertRaisesRegex(ValueError, 'name/version'): self.run_admission()

    def test_unrelated_runtime_receipt(self):
        self.proof_change(lambda p: p['packs'][0].update(sha256='0' * 64))
        with self.assertRaisesRegex(ValueError, 'different package bytes'): self.run_admission()

    def test_skipped_runtime(self):
        self.proof_change(lambda p: p['counts'].update(skipped=1))
        with self.assertRaisesRegex(ValueError, 'Incomplete runtime counts'): self.run_admission()

    def test_empty_runtime(self):
        self.proof_change(lambda p: p.update(cases=[]))
        with self.assertRaisesRegex(ValueError, 'Missing/failed runtime'): self.run_admission()

    def test_prepared_proof(self):
        self.manifest['candidates'][0]['proofs'][0]['kind'] = 'prepared-only'
        with self.assertRaisesRegex(ValueError, 'Prepared proof'): self.run_admission()

    def test_missing_required_cell(self):
        self.manifest['requiredCells'].append('missing-browser')
        with self.assertRaisesRegex(ValueError, 'Required support cell omitted'): self.run_admission()

    def test_unsupported_cell_cannot_qualify(self):
        self.manifest['cells'][0].update(state='pending', reason='No proof')
        with self.assertRaisesRegex(ValueError, 'not qualified'): self.run_admission()

    def test_path_traversal(self):
        self.manifest['candidates'][0]['packages'][0]['path'] = '../foreign.tgz'
        with self.assertRaisesRegex(ValueError, 'Unsafe artifact path'): self.run_admission()


if __name__ == '__main__':
    unittest.main(verbosity=2)
