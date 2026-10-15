#!/usr/bin/env python3
"""Assemble SEC-1.10 evidence offline; fail closed on missing or changed proof."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tarfile

ARCH = Path(__file__).resolve().parents[1]
ROOT = ARCH.parent
SUITES = {'envelopes', 'key_lifecycle', 'protected_store', 'encrypted_sync',
          'rotation', 'assets', 'capabilities', 'profile_conformance'}
GATES = ['security-profiles/sec-1.1', 'crypto-selection/sec-1.2',
         'envelope-admission/sec-1.3', 'key-lifecycle/sec-1.4',
         'protected-store/sec-1.5', 'encrypted-sync/sec-1.6',
         'membership/sec-1.7', 'assets/sec-1.8', 'capabilities/sec-1.9']


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def pin(path):
    return {'path': str(path.relative_to(ROOT)), 'bytes': path.stat().st_size, 'sha256': sha(path)}


def read_log(path):
    if path.exists():
        return path.read_text()
    return gzip.decompress(path.with_suffix(path.suffix + '.gz').read_bytes()).decode()


def assemble(evidence):
    manifest = json.loads((ARCH / 'tests/security-conformance.json').read_text())
    original = json.loads((ARCH / 'tests/security-profiles.json').read_text())['fixtures']
    rows = manifest['fixtures']
    require(manifest['productionQualified'] is False, 'Production qualification forbidden')
    require(len(rows) == len(original) and {r['id'] for r in rows} == {r['id'] for r in original},
            'Missing, duplicate or unknown fixture mapping')
    log = read_log(evidence / 'canonical.log')
    statuses = json.loads((evidence / 'check-status.json').read_text())
    require(statuses and all(c['exit'] == 0 for c in statuses), 'Required check failed')
    require(any(c['command'] == 'cargo test -p editac-security --locked' for c in statuses),
            'Canonical command missing')
    executions = {}
    suite = None
    summaries = []
    for line in log.splitlines():
        match = re.search(r'Running tests/(\w+)\.rs', line)
        if match:
            suite = match[1]
            require(suite not in executions, 'Duplicate suite ' + suite)
            executions[suite] = set()
        match = re.fullmatch(r'test (\w+) \.\.\. ok', line)
        if match and suite:
            executions[suite].add(match[1])
        match = re.fullmatch(r'test result: ok\. (\d+) passed; (\d+) failed; (\d+) ignored; (\d+) measured; (\d+) filtered out;.*', line)
        if match:
            counts = list(map(int, match.groups()))
            require(not any(counts[1:]), 'Failed/ignored/measured/filtered result')
            summaries.append(counts[0])
    require(set(executions) == SUITES, 'Missing/unknown suites: ' + str(set(executions) ^ SUITES))
    for name, tests in executions.items():
        source = (ROOT / f'core/crates/editac-security/tests/{name}.rs').read_text()
        declared = set(re.findall(r'#\[test\]\s*fn (\w+)', source))
        require(tests == declared and tests, 'Incomplete executed tests: ' + name)
    require(sum(summaries) == sum(map(len, executions.values())), 'Unaccounted test summary')
    original_by_id = {r['id']: r for r in original}
    for row in rows:
        for field in ['parent', 'invariant', 'asset', 'attacker', 'expected']:
            require(row[field] == original_by_id[row['id']][field], 'Fixture drift: ' + row['id'])
        require(row['test'] in executions[row['suite']], 'Unexecuted fixture: ' + row['id'])
    historical = []
    for gate in GATES:
        receipt = ARCH / 'evidence' / (gate + '-20261015/receipt.json')
        data = json.loads(receipt.read_text())
        artifacts = next(data[k] for k in ['artifactHashes', 'artifacts', 'artifacts_sha256'] if k in data)
        entries = artifacts if isinstance(artifacts, list) else [
            {'path': k, 'sha256': v['sha256'] if isinstance(v, dict) else v} for k, v in artifacts.items()]
        for entry in entries:
            path = ROOT / entry['path'] if entry['path'].startswith(('architecture/', 'core/')) else receipt.parent / entry['path']
            require(sha(path) == entry['sha256'], 'Changed historical artifact: ' + str(path))
        historical.append({**pin(receipt), 'verified_artifacts': len(entries),
                           'scope': 'historical gate evidence; not current platform or review qualification'})
    entry = json.loads((ARCH / 'evidence/security-profiles/sec-1.1-20261015/receipt.json').read_text())
    for path, expected in entry['entryReceiptHashes'].items():
        require(sha(ARCH / path) == expected, 'Changed upstream entry receipt: ' + path)
    # Cargo's generated lock has single-line JSON-compatible quoted identity
    # fields. Inventory only these fields; do not interpret dependency syntax.
    lock_text = (ROOT / 'core/Cargo.lock').read_text()
    packages = []
    for block in lock_text.split('[[package]]')[1:]:
        fields = re.findall(r'^(name|version|source|checksum) = ("[^\n]*")$', block, re.MULTILINE)
        package = {k: json.loads(v) for k, v in fields}
        require(len(package) == len(fields) and {'name', 'version'} <= package.keys(), 'Malformed lock identity')
        require(not package.get('source', '').startswith('registry+') or 'checksum' in package, 'Missing registry checksum')
        packages.append(package)
    require(packages, 'Empty lock inventory')
    for name, version in [('openmls', '0.9.1'), ('openmls_rust_crypto', '0.6.0'), ('age', '0.11.4')]:
        require(any(p['name'] == name and p['version'] == version for p in packages), 'Protocol dependency drift: ' + name)
    inventory = {'lock': pin(ROOT / 'core/Cargo.lock'), 'scope': 'entire locked graph; not active-target advisory clearance', 'packages': packages}
    (evidence / 'dependencies.json').write_text(json.dumps(inventory, indent=2) + '\n')
    (evidence / 'coverage.json').write_text(json.dumps({'fixtures': rows, 'executed': {k: sorted(v) for k, v in executions.items()}, 'productionQualified': False}, indent=2) + '\n')
    # Scan exact disposable markers and raw key bytes, not source fixtures.
    patterns = [b'SEC15_PRIVATE_SEEDED_CONTENT_983421', b' protected offline tail',
                b'SEC16_CONFIDENTIAL_INITIAL_20261015', b'SEC16_OFFLINE_ALPHA', b'SEC16_OFFLINE_BRAVO',
                b'SEC18_ATTACHMENT_CONTENT_PRIVATE_20261015', b'SEC18_THUMBNAIL_PRIVATE_20261015',
                b'SEC18_PREVIEW_PRIVATE_20261015', b'SEC18_PRIVATE_TITLE_20261015',
                b'SEC18_PRIVATE_ALT', b'SEC18_PRIVATE_NAME']
    patterns += [bytes([n]) * 32 for n in [1, 2, 3, 9, 0x53, 0x61, 0x72]]
    allowed = {'explicit-plaintext.json', 'explicit-recovery.json',
               'explicit-old-recovery.json', 'explicit-unjournaled.json'}
    scanned, exports = [], []
    def scan(name, data):
        info = {'path': name, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
        if Path(name).name in allowed:
            require(b'PLAINTEXT RECOVERY EXPORT' in data, 'Unlabeled export: ' + name)
            exports.append(info)
        else:
            require(not any(pattern in data for pattern in patterns), 'Seed/key leakage: ' + name)
            scanned.append(info)
    if not (evidence / 'runtime.tar.gz').exists():
        require((evidence / 'runtime').is_dir(), 'Missing runtime evidence')
        with tarfile.open(evidence / 'runtime.tar.gz', 'w:gz') as archive:
            archive.add(evidence / 'runtime', arcname='runtime')
    with tarfile.open(evidence / 'runtime.tar.gz', 'r:gz') as archive:
        for member in archive.getmembers():
            if member.isfile():
                scan(member.name, archive.extractfile(member).read())
    for path in sorted(evidence.glob('*.log*')):
        data = gzip.decompress(path.read_bytes()) if path.suffix == '.gz' else path.read_bytes()
        scan(path.name, data)
    require(scanned and exports, 'Missing runtime sinks or explicit-export proof')
    scan_result = {'patterns': len(patterns), 'matches': 0, 'unauthorized_sinks': scanned,
                   'authorized_plaintext_exports': exports, 'limits': 'Only exact prepared seeds/key bytes; does not prove absence of every leak'}
    (evidence / 'runtime-manifest.json').write_text(json.dumps(scan_result, indent=2) + '\n')
    controls = json.loads((evidence / 'evidence-controls.json').read_text())
    require(controls['executed'] == controls['passed'] == 7 and controls['failed'] == controls['skipped'] == 0,
            'Evidence rejection controls incomplete')
    sources = sorted((ROOT / 'core/crates/editac-security').rglob('*.rs'))
    sources += [ROOT / 'core/Cargo.lock', ROOT / 'core/crates/editac-security/Cargo.toml',
                ROOT / 'core/crates/editac-security/README.md', ARCH / 'evidence/encryption.md',
                ARCH / 'tests/security-conformance.json', ARCH / 'tests/security-profiles.json', Path(__file__).resolve()]
    sources += sorted((ROOT / 'core/crates/editac-security/tests/fixtures').glob('*.json'))
    prior = json.loads((ARCH / 'evidence/capabilities/sec-1.9-20261015/receipt.json').read_text())
    sources += [ROOT / p['path'] for p in prior['source_pins'] if (ROOT / p['path']).exists()]
    sources = sorted(set(sources))
    receipt = {'task': 'SEC-1.10', 'scope': 'prepared native mechanics and review handoff; no production/platform/deployment/review qualification',
               'source_revision': '96a85fbfe5d7eecf51fcb41d461acce218c64fb83c42500ef74fbcee92baec3d',
               'loaded_prompt_revision': '2e18a98412c7',
               'base_revisions': {repo: subprocess.check_output(['git', '-C', str(ROOT / repo), 'rev-parse', 'HEAD'], text=True).strip() for repo in ['core', 'architecture']},
               'checks': statuses, 'evidence_controls': controls, 'toolchain': {'rust': '1.97.1', 'node': '24.19.0', 'python': '3.9.6'}, 'canonical': {'executed': sum(map(len, executions.values())), 'passed': sum(summaries), 'failed': 0, 'ignored': 0, 'skipped': 0, 'filtered': 0, 'suites': {k: len(v) for k,v in executions.items()}},
               'fixture_count': len(rows), 'historical_receipts': historical,
               'nested_controls': {'expected_native_crash_exits_79': 3, 'key_compiler_controls': 5, 'top_level_subprocess_helper_tests': 1},
               'retained_failures': [{'log': 'canonical-initial-compile-failure.log.gz', 'exit': 101, 'reason': 'New conformance trait import and unsupported receipt assertion; repaired without production changes'}, {'log': 'canonical-trait-name-failure.log.gz', 'exit': 101, 'reason': 'Incorrect transport trait name; corrected to CiphertextTransport'}],
               'scan': {'files': len(scanned), 'patterns': len(patterns), 'matches': 0, 'authorized_exports': len(exports)},
               'source_pins': [pin(p) for p in sources],
               'limits': ['Roadmap24 independent review and actual platform evidence required', 'No assigned reviewer or resolved independent findings', 'RUSTSEC-2026-0173 retained; no current advisory clearance', 'Restored MLS senders retired; durable transactional resume/rejoin/freshness unqualified', 'No paid inference, credentials, production writes, deployment or publication'],
               'artifacts': [pin(p) for p in sorted(evidence.rglob('*')) if p.is_file() and p.name != 'receipt.json' and 'runtime' not in p.relative_to(evidence).parts]}
    (evidence / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({'fixtures': len(rows), 'passed': sum(summaries), 'historical_artifacts': sum(r['verified_artifacts'] for r in historical), 'source_pins': len(sources)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--evidence', required=True, type=Path)
    args = parser.parse_args()
    assemble(args.evidence.resolve())
