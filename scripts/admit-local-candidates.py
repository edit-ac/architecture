#!/usr/bin/env python3
"""Verify immutable local packages and scoped retained consumer proof, never releases."""
import argparse
import base64
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import tarfile


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def local_path(root, name):
    p = PurePosixPath(name)
    require(not p.is_absolute() and '..' not in p.parts and '\\' not in name,
            'Unsafe artifact path: ' + name)
    resolved = (root / name).resolve()
    require(root.resolve() in resolved.parents, 'Artifact escapes manifest directory')
    return resolved


def archive_members(path):
    result = {}
    with tarfile.open(path, 'r:gz') as archive:
        for member in archive.getmembers():
            name = member.name
            p = PurePosixPath(name)
            require(p.parts and p.parts[0] == 'package' and '..' not in p.parts
                    and not p.is_absolute() and '\\' not in name,
                    'Unsafe package member: ' + name)
            require(member.isfile() or member.isdir(), 'Nonregular package member: ' + name)
            if member.isfile():
                require(name not in result, 'Duplicate package member: ' + name)
                result[name] = archive.extractfile(member).read()
    return result


def verify_file(root, pin):
    path = local_path(root, pin['path'])
    data = path.read_bytes()
    require(digest(data) == pin['sha256'], 'Artifact changed: ' + pin['path'])
    return data


def admit(manifest_path, core_repository, expected_identity):
    root = manifest_path.resolve().parent
    raw = manifest_path.read_bytes()
    require(digest(raw) == expected_identity, 'Stale/unrequested candidate manifest')
    manifest = json.loads(raw)
    require(manifest['schemaVersion'] == 1 and manifest['scope'] == 'local-only',
            'Only explicit local candidate manifests are admitted')
    require(manifest['published'] is False and manifest['releaseQualified'] is False
            and manifest['registryIdentity'] is None, 'Fake published/release identity')
    require(manifest['candidates'] and manifest['cells'], 'Empty candidate set')
    candidates, proof_counts = {}, {}
    source_count = member_count = 0
    for candidate in manifest['candidates']:
        ident = candidate['id']
        require(ident not in candidates, 'Duplicate candidate')
        require(re.fullmatch(r'[a-f0-9]{40}', candidate['sourceCommit']), 'Unpinned source commit')
        pins = json.loads(verify_file(root, candidate['sources']))
        require(pins and len({p['path'] for p in pins}) == len(pins), 'Empty/duplicate source pins')
        for pin in pins:
            path = PurePosixPath(pin['path'])
            require(not path.is_absolute() and '..' not in path.parts, 'Unsafe source path')
            blob = subprocess.run(['git', '-C', str(core_repository), 'show',
                                   candidate['sourceCommit'] + ':' + pin['path']],
                                  capture_output=True, check=True).stdout
            require(digest(blob) == pin['sha256'], 'Source does not match pinned commit: ' + pin['path'])
            source_count += 1
        packages, hashes, integrities = {}, {}, {}
        require(candidate['packages'], 'Empty packages')
        for pack in candidate['packages']:
            name = pack['name']
            require(name not in packages, 'Duplicate package')
            require(pack['published'] is False, 'Fake published package')
            data = verify_file(root, pack)
            require(len(data) == pack['bytes'], 'Package size changed')
            members = archive_members(local_path(root, pack['path']))
            require({n: digest(b) for n, b in members.items()} == pack['members'],
                    'Package member inventory changed: ' + name)
            metadata = json.loads(members['package/package.json'])
            require(metadata['name'] == name and metadata['version'] == pack['version'],
                    'Package name/version changed')
            packages[name] = members
            hashes[name] = digest(data)
            integrities[name] = 'sha512-' + base64.b64encode(hashlib.sha512(data).digest()).decode()
            member_count += len(members)
        require(candidate['runtime'], 'Missing generated engine/WASM identity')
        for runtime in candidate['runtime']:
            require(digest(packages[runtime['package']][runtime['member']]) == runtime['sha256'],
                    'Generated engine/WASM identity changed')
        proofs = {}
        for proof in candidate['proofs']:
            data = json.loads(verify_file(root, proof))
            proof_id = proof['id']
            require(proof_id not in proofs, 'Duplicate proof')
            require(proof['kind'] == 'retained-production-consumer', 'Prepared proof cannot qualify runtime')
            cases = data['cases']
            require(cases and all(c.get('passed') is True for c in cases), 'Missing/failed runtime cases')
            names = [c['name'] for c in cases]
            require(len(names) == len(set(names)), 'Duplicate runtime case names')
            require(all(n in names for n in proof['requiredCases']), 'Missing required consumer case')
            if proof['binding'] == 'npm-integrity':
                require(all(c['exit'] == 0 for c in data['commands']), 'Failed consumer command')
                bindings = {p['name']: p['integrity'] for p in data['packs']}
                expected = integrities
            else:
                require(proof['binding'] in ['packs-sha256', 'testedPackages-sha256'], 'Unknown binding')
                entries = data['packs' if proof['binding'] == 'packs-sha256' else 'testedPackages']
                bindings = {(p['name'] if p['name'].startswith('@') else '@edit-ac/' + p['name']):
                            p['sha256'] for p in entries}
                expected = hashes
            names_bound = proof['packages']
            require(names_bound and len(set(names_bound)) == len(names_bound)
                    and set(names_bound).issubset(expected), 'Invalid proof package subset')
            require(bindings == {name: expected[name] for name in names_bound},
                    'Consumer tested different package bytes')
            counts = data.get('counts')
            if counts:
                require(counts['executed'] == counts['passed'] and counts['passed'] >= len(cases)
                        and all(counts.get(k, 0) == 0 for k in ['failed', 'skipped', 'cancelled', 'todo']),
                        'Incomplete runtime counts')
            proofs[proof_id] = {'cases': set(names), 'packages': set(names_bound)}
            proof_counts[ident + '/' + proof_id] = len(cases)
        require(proofs, 'No independent runtime proof')
        for recipe in candidate.get('recipes', []):
            require(recipe['proof'] in proofs and recipe['cases']
                    and set(recipe['cases']).issubset(proofs[recipe['proof']]['cases']),
                    'Recipe lacks exact runtime proof')
            content = verify_file(root, recipe['source'])
            blob = subprocess.run(['git', '-C', str(core_repository), 'show',
                                   candidate['sourceCommit'] + ':' + recipe['gitPath']],
                                  capture_output=True, check=True).stdout
            require(content == blob, 'Recipe source differs from pinned Git commit')
            require(recipe['ownerRanges'], 'Recipe has no owning source references')
            for owner in recipe['ownerRanges']:
                path = PurePosixPath(owner['path'])
                require(not path.is_absolute() and '..' not in path.parts,
                        'Unsafe recipe owner path')
                source = subprocess.run(['git', '-C', str(core_repository), 'show',
                                         candidate['sourceCommit'] + ':' + owner['path']],
                                        capture_output=True, check=True).stdout.splitlines(keepends=True)
                require(1 <= owner['start'] <= owner['end'] <= len(source), 'Invalid owner range')
                require(digest(b''.join(source[owner['start'] - 1:owner['end']])) == owner['sha256'],
                        'Recipe owner range differs from pinned source')
        for artifact in candidate.get('artifacts', []):
            verify_file(root, artifact)
        candidates[ident] = proofs
    cell_ids = set()
    for cell in manifest['cells']:
        require(cell['id'] not in cell_ids, 'Duplicate support cell')
        cell_ids.add(cell['id'])
        require(cell['state'] in ['supported', 'pending', 'unsupported'], 'Unknown support state')
        if cell['state'] == 'supported':
            require(cell['cases'], 'Supported cell has zero runtime cases')
            proof = candidates[cell['candidate']][cell['proof']]
            require(all(name in proof['cases'] for name in cell['cases']), 'Cell lacks exact runtime outcomes')
            require(cell['packages'] and set(cell['packages']).issubset(proof['packages']),
                    'Cell packages lack applicable runtime proof')
        else:
            require(bool(cell['reason']), 'Unqualified cell needs an explicit reason')
    require(set(manifest['requiredCells']).issubset(cell_ids), 'Required support cell omitted')
    require(all(c['state'] == 'supported' for c in manifest['cells']
                if c['id'] in manifest['requiredCells']), 'Required local support cell is not qualified')
    for mapping in manifest.get('docsPrerequisites', []):
        require(re.fullmatch(r'[a-f0-9]{40}', mapping['docsCommit']), 'Unpinned docs consumer commit')
        subprocess.run(['git', '-C', str(core_repository.parent / 'docs'), 'cat-file', '-e',
                        mapping['docsCommit'] + '^{commit}'], capture_output=True, check=True)
        verify_file(root, mapping['delivery'])
        verify_file(root, mapping['receipt'])
    return {'manifestSha256': digest(raw), 'candidateCount': len(candidates),
            'sourceBlobs': source_count, 'packageMembers': member_count,
            'reusedRuntimeCases': proof_counts,
            'supportedCells': [c['id'] for c in manifest['cells'] if c['state'] == 'supported'],
            'unqualifiedCells': [c['id'] for c in manifest['cells'] if c['state'] != 'supported'],
            'published': False, 'releaseQualified': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    parser.add_argument('--core', required=True, type=Path)
    parser.add_argument('--expected-sha256', required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(admit(args.manifest, args.core, args.expected_sha256), indent=2))
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError, tarfile.TarError) as error:
        parser.exit(1, 'Local candidate rejected: ' + str(error) + '\n')
