"""Deterministic regressions for successor metadata; no runtime/provider calls."""

import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import readiness_config as config


def module(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


inventory = module('readiness-inventory')
runtimes = module('readiness-runtimes')
handoff = module('readiness-handoff')


class CollectorTests(unittest.TestCase):
    def setUp(self):
        scratch = SCRIPTS.parent / '.artifacts/readiness-tests'
        scratch.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.manifest = self.root / 'architecture/queue/manifest.json'
        self.manifest.parent.mkdir(parents=True)
        self.state = self.root / '.roadmap-runner/successor'
        self.data = {'workspace': str(self.root), 'runtimeRoot': str(self.state),
                     'mode': 'single-workspace-main-feature-first'}
        self.manifest.write_text(json.dumps(self.data))

    def locations(self, state=None):
        with patch.object(config, 'ROOT', self.root):
            return config.Locations(self.manifest, state)

    def test_manifest_selects_successor_without_old_generated_receipts(self):
        location = self.locations()
        self.assertEqual(location.state, self.state)
        self.assertEqual(location.store, self.root / 'architecture/.artifacts/successor')
        self.assertTrue(location.successor)

    def test_explicit_runtime_root_controls_output(self):
        state = self.root / '.roadmap-runner/isolated/run'
        self.assertEqual(self.locations(state).store, self.root / 'architecture/.artifacts/isolated/run')

    def test_foreign_workspace_rejected(self):
        self.data['workspace'] = '/foreign'
        self.manifest.write_text(json.dumps(self.data))
        with self.assertRaisesRegex(ValueError, 'another workspace'):
            self.locations()

    def test_runtime_root_cannot_escape_workspace(self):
        with self.assertRaisesRegex(ValueError, 'Runtime root'):
            self.locations(self.root / 'outside')

    def test_relative_link_and_repeated_same_owner(self):
        location = self.locations()
        target = location.store / 'readiness.json'
        target.parent.mkdir(parents=True)
        target.write_text('{}')
        link = location.state / target.name
        location.link(link, target)
        location.link(link, target)
        self.assertEqual(link.resolve(), target)

    def test_regular_file_preserved(self):
        location = self.locations()
        path = self.root / 'existing'
        path.write_text('preserve')
        with self.assertRaisesRegex(ValueError, 'regular'):
            location.link(path, self.root / 'target')
        self.assertEqual(path.read_text(), 'preserve')

    def test_foreign_dangling_link_preserved(self):
        location = self.locations()
        path = self.root / 'link'
        path.symlink_to('absent')
        with self.assertRaisesRegex(ValueError, 'another owner'):
            location.link(path, self.root / 'new')
        self.assertEqual(path.readlink(), Path('absent'))

    def test_additional_provenance_cannot_relabel_original(self):
        location = self.locations()
        location.state.mkdir(parents=True)
        extra = location.state / 'additional-preserved-inputs.json'
        extra.write_text(json.dumps({'paths': [{'repo': 'core', 'path': 'original', 'sha256': 'new'}]}))
        def load(path):
            return json.loads(path.read_text()) if path == extra else {'core': [{'path': 'original', 'sha256': 'old'}]}
        with self.assertRaisesRegex(ValueError, 'original provenance'):
            location.preserved_inputs(load)

    def test_additional_external_edit_retains_separate_ownership(self):
        location = self.locations()
        location.state.mkdir(parents=True)
        extra = location.state / 'additional-preserved-inputs.json'
        extra.write_text(json.dumps({'paths': [{'repo': 'core', 'path': 'additional', 'sha256': 'new', 'externalOwner': 'external-unvalidated'}]}))
        def load(path):
            return json.loads(path.read_text()) if path == extra else {'core': [{'path': 'original', 'sha256': 'old'}]}
        rows = location.preserved_inputs(load)['core']
        self.assertEqual(rows[0], {'path': 'original', 'sha256': 'old'})
        self.assertEqual(rows[1]['externalOwner'], 'external-unvalidated')

    def test_evolved_source_requires_exact_original_copy(self):
        location = self.locations()
        live = self.root / 'live'
        live.write_bytes(b'evolved')
        original = location.state / 'preserved-sources/original'
        original.parent.mkdir(parents=True)
        original.write_bytes(b'original\r\n')
        row = {'sha256': inventory.digest(b'original\r\n'), 'preservedCopy': str(original)}
        self.assertEqual(location.preserved_path(row, live), original)
        self.assertEqual(live.read_bytes(), b'evolved')
        original.write_bytes(b'corrupted')
        with self.assertRaisesRegex(ValueError, 'original bytes'):
            location.preserved_path(row, live)

    def test_preserved_revision_cannot_change_original_hash(self):
        location = self.locations()
        location.state.mkdir(parents=True)
        revisions = location.state / 'preserved-source-revisions.json'
        revisions.write_text(json.dumps({'paths': [{'repo': 'core', 'path': 'original', 'originalSha256': 'wrong'}]}))
        def load(path):
            return json.loads(path.read_text()) if path == revisions else {'core': [{'path': 'original', 'sha256': 'old'}]}
        with self.assertRaisesRegex(ValueError, 'original provenance'):
            location.preserved_inputs(load)

    def test_hash_authentication_distinguishes_changed_and_absent(self):
        (self.root / 'same').write_bytes(b'same')
        (self.root / 'changed').write_bytes(b'current')
        with patch.object(inventory, 'ROOT', self.root), patch.object(inventory, 'PINS', {}):
            rows = inventory.authenticate_pins({
                'same': inventory.digest(b'same'), 'changed': inventory.digest(b'old'),
                'absent': inventory.digest(b'old')}, self.root)
        self.assertEqual({r['path']: r['state'] for r in rows}, {
            'same': 'matched', 'changed': 'changed', 'absent': 'absent-historical-input'})

    def test_source_state_is_not_acceptance_drift(self):
        original = 'Status: IN_PROGRESS\n\n- [ ] SFC-1.1 task\nAcceptance: preserve data.\n'
        updated = original.replace('[ ]', '[x]') + 'Current delivery: verified.\n'
        self.assertEqual(handoff.stable_source(original), handoff.stable_source(updated))
        self.assertNotEqual(handoff.stable_source(original), handoff.stable_source(original.replace('preserve', 'discard')))

    def test_unvalidated_observations_do_not_invalidate_accepted_source_pins(self):
        saved = {'workspace': {'repositories': {'core': {'head': 'same', 'preservedDirtyPaths': ['original'],
                  'ownedDirtyPaths': [], 'externalInputs': [{'path': 'external', 'currentSha256': 'before'}]}}},
                 'sourcePins': {'accepted': 'exact'}}
        current = json.loads(json.dumps(saved))
        current['workspace']['repositories']['core']['externalInputs'][0]['currentSha256'] = 'after'
        self.assertEqual(handoff.acceptance_checkpoint(saved), handoff.acceptance_checkpoint(current))
        current['sourcePins']['accepted'] = 'changed'
        self.assertNotEqual(handoff.acceptance_checkpoint(saved), handoff.acceptance_checkpoint(current))

    def test_preserved_ownership_still_part_of_checkpoint(self):
        saved = {'workspace': {'repositories': {'core': {'preservedDirtyPaths': ['original']}}}}
        current = {'workspace': {'repositories': {'core': {'preservedDirtyPaths': []}}}}
        self.assertNotEqual(handoff.acceptance_checkpoint(saved), handoff.acceptance_checkpoint(current))

    def proof(self):
        return {'mode': 'scoped-proof-metadata', 'parent': 'SFC-1.1',
                'proof': {'suites': {'current': 59}, 'rustDistinctPassed': 59,
                          'rustFailed': 0, 'rustRequiredSkipped': 0,
                          'setupFailures': ['wrong-node', 'missing-exchange-env'], 'commands': ['prepared']},
                'sourceAuthentication': [{'state': 'matched'}], 'sourcePins': {},
                'probes': [], 'prohibitedActionsExecuted': {'tests': 0, 'providers': 0}}

    def test_scoped_metadata_does_not_probe(self):
        proof = self.proof()
        with patch.object(runtimes, 'probe', side_effect=AssertionError('unexpected probe')), \
             patch.object(runtimes, 'scoped_proof', return_value=proof):
            result = runtimes.validate(proof)
        self.assertEqual(result['inventoryChecks']['failed'], 0)
        self.assertEqual(result['runtimeTestsExecuted'], 0)
        self.assertEqual(result['availabilityProbes']['executed'], 0)

    def test_required_skip_rejects_accepted_proof(self):
        proof = self.proof()
        proof['proof']['rustRequiredSkipped'] = 1
        with patch.object(runtimes, 'scoped_proof', return_value=proof), self.assertRaises(ValueError):
            runtimes.validate(proof)

    def test_changed_saved_pin_rejects_check(self):
        proof = self.proof()
        source = self.root / 'source'
        source.write_bytes(b'changed')
        proof['sourcePins'][str(source)] = inventory.digest(b'original')
        with patch.object(runtimes, 'scoped_proof', return_value=proof), self.assertRaises(ValueError):
            runtimes.validate(proof)

    def test_saved_proof_cannot_invent_runtime_or_qualification(self):
        proof = self.proof()
        saved = dict(proof, runtimeQualification='passed')
        with patch.object(runtimes, 'scoped_proof', return_value=proof), self.assertRaisesRegex(ValueError, 'authoritative'):
            runtimes.validate(saved)

    def preserved_fixture(self, mutate=False, external=False):
        baseline = {'core': []}
        for index in range(44):
            path = self.root / 'core' / f'preserved-{index}'
            path.parent.mkdir(exist_ok=True)
            path.write_bytes(b'preserved')
            baseline['core'].append({'path': path.name, 'status': ' M', 'sha256': inventory.digest(path.read_bytes())})
        if mutate:
            path.write_bytes(b'changed')
        if external:
            path = self.root / 'core' / 'external'
            path.write_bytes(b'current')
            baseline['core'].append({'path': path.name, 'status': ' M', 'sha256': inventory.digest(b'observed'),
                                     'externalOwner': 'external active task', 'deliveryOwner': 'SFC-3.3'})
        tasks = ['RWP-1.1-I1', 'RWP-1.1-I2', 'RWP-1.1-I3', 'RWP-1.2-I1-G1']
        tasks += [f'RWP-1.2-I1-S1-G{n}' for n in range(2, 8)]
        manifest = {'entries': [{}, {'progressFile': str(self.root / 'progress.md')}]}
        with patch.object(inventory, 'ROOT', self.root), patch.object(inventory, 'PINS', {}), \
             patch.object(inventory, 'load', side_effect=[baseline, manifest]), \
             patch.object(inventory, 'read', return_value='\n'.join(tasks)), \
             patch.object(inventory, 'git', return_value='a' * 40), \
             patch.object(inventory.subprocess, 'run'):
            return inventory.preserved_work()

    def test_removed_generated_receipts_do_not_block_preserved_source(self):
        result = self.preserved_fixture()
        self.assertEqual(len(result['paths']), 44)
        self.assertEqual(len(result['accepted']), 10)
        self.assertTrue(all(r['receiptSha256'] is None for r in result['accepted']))
        self.assertEqual(result['interrupted']['state'], 'interrupted-unvalidated')
        self.assertEqual(result['interrupted']['owner'], 'SFC-2.3')

    def test_preserved_source_mutation_rejects_handoff(self):
        with self.assertRaisesRegex(ValueError, 'Preserved input changed'):
            self.preserved_fixture(mutate=True)

    def test_external_evolution_is_recorded_without_claiming_preserved_or_verified(self):
        result = self.preserved_fixture(external=True)
        external = result['paths'][-1]
        self.assertFalse(external['preserved'])
        self.assertEqual(external['currentSha256'], inventory.digest(b'current'))
        self.assertEqual(external['sha256'], inventory.digest(b'observed'))
        self.assertIn('excluded', external['state'])
        self.assertTrue(all(r['preserved'] for r in result['paths'][:-1]))


if __name__ == '__main__':
    unittest.main()
