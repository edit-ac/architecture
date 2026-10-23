"""Shared queue locations for the existing readiness collectors."""

import json
import hashlib
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = ROOT / "architecture/runner-queues/emulator-web-readiness-20261022/manifest.json"


def arguments(parser):
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--runtime-root", type=Path,
                        help="current runtime state; defaults to manifest.runtimeRoot")


class Locations:
    def __init__(self, manifest=DEFAULT_MANIFEST, runtime_root=None):
        self.manifest = Path(manifest).resolve()
        self.data = json.loads(self.manifest.read_text())
        if self.data["workspace"] != str(ROOT):
            raise ValueError("Manifest belongs to another workspace")
        self.queue = self.manifest.parent
        self.state = Path(runtime_root or self.data.get("runtimeRoot") or
                          ROOT / ".roadmap-runner" / self.queue.name).resolve()
        if not self.state.is_relative_to(ROOT / ".roadmap-runner"):
            raise ValueError("Runtime root must belong to this workspace")
        self.store = ROOT / "architecture/.artifacts" / self.state.relative_to(ROOT / ".roadmap-runner")
        self.successor = self.data.get("mode") == "single-workspace-main-feature-first"

    def preserved_inputs(self, load):
        baseline = load(ROOT / '.roadmap-runner/emulator-web-readiness-20261022/pre-schema-policy-dirty-inputs.json')
        extra = self.state / 'additional-preserved-inputs.json'
        if extra.is_file():
            for row in load(extra)['paths']:
                repo, path = row['repo'], Path(row['path'])
                if repo not in baseline or path.is_absolute() or '..' in path.parts:
                    raise ValueError('Invalid additional preserved input')
                if any(old['path'] == str(path) for old in baseline[repo]):
                    raise ValueError('Additional input cannot replace original provenance')
                baseline[repo].append({k: v for k, v in row.items() if k != 'repo'})
        revisions = self.state / 'preserved-source-revisions.json'
        if revisions.is_file():
            for revision in load(revisions)['paths']:
                matches = [r for r in baseline.get(revision['repo'], []) if r['path'] == revision['path']]
                if len(matches) != 1 or matches[0]['sha256'] != revision['originalSha256']:
                    raise ValueError('Preserved revision must match original provenance')
                copy = Path(revision['preservedCopy']).resolve()
                if not copy.is_relative_to(self.state / 'preserved-sources'):
                    raise ValueError('Preserved copy must stay in current preservation storage')
                matches[0].update({k: revision[k] for k in ['preservedCopy', 'evolvedOwner', 'deliveryOwner', 'reconstruction']})
        return baseline

    def preserved_path(self, row, live):
        for path in [live, Path(row['preservedCopy']) if row.get('preservedCopy') else None]:
            if path and path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == row['sha256']:
                return path
        raise ValueError('Preserved input changed without authenticated original bytes: ' + str(live))

    def link(self, path, target):
        path, target = Path(path), Path(target)
        if path.is_symlink() and path.resolve() != target:
            raise ValueError("Refuse to replace another owner's link")
        if path.exists() and not path.is_symlink():
            raise ValueError("Refuse to replace existing regular inventory")
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.is_symlink():
            path.symlink_to(os.path.relpath(target, path.parent))
