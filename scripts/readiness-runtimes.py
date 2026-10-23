#!/usr/bin/env python3
"""RRD-1.2: inventory local runtimes without booting or qualifying them.

Supply --manifest and optional --runtime-root for a successor queue.
Run from the workspace: python3 architecture/scripts/readiness-runtimes.py
Then use --check to validate the saved inventory without repeating probes.
Only explicit read-only commands below are executed. No package installation,
remote connections, application tests, provider calls or credential loading.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import plistlib
import pwd
import re
import shutil
import subprocess
from readiness_config import Locations, arguments


ROOT = Path(__file__).resolve().parents[2]
HOME = Path.home()
STORE = ROOT / 'architecture/.artifacts/emulator-web-readiness-20261022'
OUT = STORE / 'runtimes.json'
LINK = ROOT / '.roadmap-runner/emulator-web-readiness-20261022/runtimes.json'
LOGS = STORE / 'runtime-inventory'
SDK = HOME / 'Library/Android/sdk'
JAVA = Path('/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home')
DEVELOPER = '/Applications/Xcode.app/Contents/Developer'
PINS = {}
SAVED_PROBES = {}
CONFIG = Locations()


def configure(manifest, runtime_root=None):
    global CONFIG, STORE, OUT, LINK, LOGS
    CONFIG = Locations(manifest, runtime_root)
    STORE = CONFIG.store
    OUT, LINK = STORE / 'runtimes.json', CONFIG.state / 'runtimes.json'
    LOGS = STORE / 'runtime-inventory'


def scoped_proof():
    """Authenticate supplied proof metadata; never replay runtime probes/suites."""
    PINS.clear()
    path = CONFIG.state / 'initial-current-format-proof.json'
    proof = json.loads(Path(pin(path)).read_text())
    source_rows, binary_rows = [], []
    for key, base, rows in [('inputs', ROOT, source_rows), ('executedBinaries', ROOT / 'core', binary_rows)]:
        for name, expected in proof.get(key, {}).items():
            source = base / name
            actual = hashlib.sha256(source.read_bytes()).hexdigest() if source.is_file() else None
            if source.is_file():
                pin(source)
            rows.append({'path': str(source), 'expectedSha256': expected, 'currentSha256': actual,
                         'state': 'matched' if actual == expected else 'changed' if actual else 'absent-historical-input'})
    for path in [__file__, CONFIG.manifest, Path(__file__).with_name('readiness_config.py'),
                 ROOT / 'core/package.json', ROOT / 'core/rust-toolchain.toml']:
        pin(path)
    package = json.loads((ROOT / 'core/package.json').read_text())
    node = HOME / '.nvm/versions/node' / ('v' + package['engines']['node']) / 'bin/node'
    pin(node)
    return {'schemaVersion': 1, 'parent': 'SFC-1.1', 'mode': 'scoped-proof-metadata',
            'proof': proof, 'proofRef': str(CONFIG.state / 'initial-current-format-proof.json'),
            'sourceAuthentication': source_rows, 'binaryAuthentication': binary_rows,
            'toolchains': {'node': fact(node), 'nodeRequired': package['engines']['node'],
                'shared': {'scope': 'Initial 59-case proof only; full cutover/runtime suites remain open'},
                'terminal': {'scope': 'No terminal runtime qualification'}},
            'targets': {}, 'probes': [], 'sourcePins': dict(PINS),
            'runtimeQualification': 'Historical bounded proof only; no current-format cutover/full target qualification',
            'prohibitedActionsExecuted': {'boot': 0, 'tests': 0, 'providers': 0, 'network': 0, 'provisioning': 0}}


def pin(path):
    path = Path(path)
    if not path.is_absolute():
        path = ROOT / path
    if path.is_file():
        PINS[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
    return str(path)


def fact(path):
    path = Path(path)
    return {'path': str(path), 'exists': path.exists()}


def properties(path):
    path = Path(path)
    if not path.is_file():
        return {}
    pin(path)
    return dict(tuple(part.strip() for part in line.split('=', 1))
                for line in path.read_text().splitlines()
                if '=' in line and not line.lstrip().startswith('#'))


def probe(name, argv, env=None):
    """Retain full bounded-command output locally; never invoke a shell."""
    argv = list(map(str, argv))
    log = LOGS / (name + '.log')
    command_env = dict(os.environ, DEVELOPER_DIR=DEVELOPER)
    command_env.update(env or {})
    prior = SAVED_PROBES.get(name)
    if prior and prior['argv'] == argv and prior['environment'] == dict(env or {}, DEVELOPER_DIR=DEVELOPER):
        old_log = Path(prior['log'])
        if old_log.is_file() and hashlib.sha256(old_log.read_bytes()).hexdigest() == prior['sha256']:
            return dict(prior, reused=True)
    try:
        with log.open('w') as stream:
            result = subprocess.run(argv, cwd=ROOT / 'core', env=command_env,
                                    stdout=stream, stderr=subprocess.STDOUT, timeout=45)
        code = result.returncode
    except (OSError, subprocess.TimeoutExpired) as error:
        log.write_text(str(error) + '\n')
        code = 124 if isinstance(error, subprocess.TimeoutExpired) else 127
    return {'id': name, 'argv': argv, 'cwd': str(ROOT / 'core'), 'exit': code,
            'reused': False, 'collectedUtc': datetime.now(timezone.utc).isoformat(),
            'environment': dict(env or {}, DEVELOPER_DIR=DEVELOPER),
            'log': str(log), 'sha256': hashlib.sha256(log.read_bytes()).hexdigest()}


def text(probes, name):
    return Path(next(p['log'] for p in probes if p['id'] == name)).read_text()


def read_json(probes, name):
    try:
        return json.loads(text(probes, name))
    except (ValueError, StopIteration):
        return {}


def route(owner, command, inputs, scope, unavailable=()):
    return {'owner': owner, 'cwd': str(ROOT / 'core'), 'command': command,
            'inputs': [fact(ROOT / p) for p in inputs], 'scope': scope,
            'unavailablePrerequisites': list(unavailable), 'executed': False}


def access_search():
    """Search authored runtime/setup documentation, never SSH keys/config."""
    roots = [ROOT / 'architecture/operations', ROOT / 'core/native', ROOT / 'docs/content']
    files = [ROOT / 'architecture/WORKSPACE_SETUP.md', ROOT / 'architecture/specs/verification.md']
    for root in roots:
        files.extend(sorted(root.rglob('*.md')))
    pattern = re.compile(r'parallels|utm(?:ctl|app| virtual)|vmware|virtualbox|qemu|multipass|'
                         r'\bssh\s+\S+|(?:windows|linux).{0,60}(?:host|runtime|\bvm\b)', re.I)
    matches = []
    for path in files:
        if not path.is_file():
            continue
        pin(path)
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if pattern.search(line):
                matches.append({'path': str(path), 'line': number, 'text': line})
    return {'searchedDocuments': len(set(files)), 'matches': matches,
            'conclusion': 'No executable Windows/Linux remote endpoint or VM access route '
                          'is configured by these authored documents. Generic policy/task references '
                          'are requirements, not runtime access. No network connection attempted.'}


def collect():
    if CONFIG.successor:
        return scoped_proof()
    LOGS.mkdir(parents=True, exist_ok=True)
    upstream = json.loads((STORE / 'readiness.json').read_text())
    if upstream['prerequisites']['RRD-1.1']['state'] != 'source-inventory-verified':
        raise ValueError('RRD-1.1 source inventory is required')
    probes = []
    package = json.loads((ROOT / 'core/package.json').read_text())
    node_bin = HOME / '.nvm/versions/node' / ('v' + package['engines']['node']) / 'bin'
    commands = [
        ('host', ['/usr/bin/sw_vers']), ('xcode', ['/usr/bin/xcodebuild', '-version']),
        ('swift', ['/usr/bin/xcrun', 'swiftc', '--version']),
        ('ios-sdk-path', ['/usr/bin/xcrun', '--sdk', 'iphonesimulator', '--show-sdk-path']),
        ('ios-sdk-version', ['/usr/bin/xcrun', '--sdk', 'iphonesimulator', '--show-sdk-version']),
        ('macos-sdk-path', ['/usr/bin/xcrun', '--sdk', 'macosx', '--show-sdk-path']),
        ('macos-sdk-version', ['/usr/bin/xcrun', '--sdk', 'macosx', '--show-sdk-version']),
        ('macos-sdk-build', ['/usr/bin/xcrun', '--sdk', 'macosx', '--show-sdk-build-version']),
        ('sim-runtimes', ['/usr/bin/xcrun', 'simctl', 'list', 'runtimes', '-j']),
        ('sim-devices', ['/usr/bin/xcrun', 'simctl', 'list', 'devices', 'available', '-j']),
        ('avds', [SDK / 'emulator/emulator', '-list-avds']),
        ('emulator', [SDK / 'emulator/emulator', '-version']),
        ('adb', [SDK / 'platform-tools/adb', 'version']),
        ('java17', [JAVA / 'bin/java', '-version']),
        ('node', [shutil.which('node') or 'node', '--version']),
        ('npm', [shutil.which('npm') or 'npm', '--version']),
        ('node-pinned', [node_bin / 'node', '--version']),
        ('rust-toolchains', [HOME / '.cargo/bin/rustup', 'toolchain', 'list']),
    ]
    for name, command in commands:
        probes.append(probe(name, command))
    probes.append(probe('npm-pinned', [node_bin / 'npm', '--version'],
                        {'PATH': str(node_bin) + ':' + os.environ.get('PATH', '')}))
    rust_pin = re.search(r'channel\s*=\s*"([^"]+)"', (ROOT / 'core/rust-toolchain.toml').read_text())[1]
    rust = HOME / '.rustup/toolchains' / (rust_pin + '-aarch64-apple-darwin')
    # Direct installed binaries cannot trigger rustup downloads.
    for tool in ['rustc', 'cargo']:
        probes.append(probe(tool, [rust / 'bin' / tool, '--version']))
    probes.append(probe('rust-targets', [HOME / '.cargo/bin/rustup', 'target', 'list',
                                       '--installed', '--toolchain', rust.name]))
    gradle = ROOT / 'core/target/native-tooling/gradle-8.14/bin/gradle'
    probes.append(probe('gradle814', [gradle, '--offline', '--no-daemon', '--version'],
                        {'JAVA_HOME': str(JAVA)}))
    cached_gradles = sorted((HOME / '.gradle/wrapper/dists').glob('*/**/bin/gradle'))
    # Available alternatives are inventory facts, never silently substituted for 8.14.
    for index, candidate in enumerate(cached_gradles):
        probes.append(probe('cached-gradle-' + str(index),
            [candidate, '--offline', '--no-daemon', '--version'], {'JAVA_HOME': str(JAVA)}))
    runtimes = read_json(probes, 'sim-runtimes').get('runtimes', [])
    devices = read_json(probes, 'sim-devices').get('devices', {})
    avds = []
    for name in text(probes, 'avds').splitlines():
        config = HOME / '.android/avd' / (name + '.avd/config.ini')
        if not config.is_file():
            continue
        pairs = dict(line.split('=', 1) for line in config.read_text().splitlines() if '=' in line)
        image = SDK / pairs.get('image.sysdir.1', '__missing__')
        avds.append({'name': name, 'config': pin(config), 'abi': pairs.get('abi.type'),
                     'image': fact(image), 'properties': fact(image / 'source.properties'),
                     'systemImageMetadata': properties(image / 'source.properties'),
                     'systemImage': fact(image / 'system.img')})
    browsers = []
    for app in ['Safari', 'Google Chrome']:
        path = Path('/Applications') / (app + '.app/Contents/Info.plist')
        info = plistlib.loads(path.read_bytes()) if path.is_file() else {}
        browsers.append({'application': app, 'plist': fact(path),
                         'version': info.get('CFBundleShortVersionString'),
                         'build': info.get('CFBundleVersion')})
    lock = ROOT / 'core/node_modules/playwright-core/browsers.json'
    browser_spec = json.loads(lock.read_text()) if lock.is_file() else {}
    playwright = {'lock': pin(lock), 'required': browser_spec.get('browsers', []),
                  'cache': str(HOME / 'Library/Caches/ms-playwright'),
                  'installed': []}
    cache = Path(playwright['cache'])
    if cache.is_dir():
        playwright['installed'] = sorted(p.name for p in cache.iterdir() if p.is_dir() and not p.name.startswith('.'))
    playwright['executables'] = []
    patterns = {'chromium': '*/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing',
        'chromium-headless-shell': '*/chrome-headless-shell',
        'firefox': 'firefox/*.app/Contents/MacOS/firefox', 'webkit': 'pw_run.sh', 'ffmpeg': 'ffmpeg-mac'}
    for browser in playwright['required']:
        if browser['name'] not in patterns:
            continue
        folder = cache / (browser['name'].replace('-', '_') + '-' + browser['revision'])
        candidates = list(folder.glob(patterns[browser['name']]))
        playwright['executables'].append({'name': browser['name'], 'revision': browser['revision'],
            'folder': fact(folder), 'executables': [fact(p) for p in candidates],
            'available': bool(candidates) and all(os.access(p, os.X_OK) for p in candidates)})
    vm_tools = {name: shutil.which(name) for name in ['prlctl', 'utmctl', 'VBoxManage',
        'qemu-system-aarch64', 'qemu-system-x86_64', 'multipass', 'docker', 'podman', 'colima', 'limactl', 'pwsh']}
    vm_paths = [Path('/Applications') / name for name in ['UTM.app', 'Parallels Desktop.app',
                'VMware Fusion.app', 'VirtualBox.app', 'Docker.app']]
    vm_paths += [HOME / p for p in ['Virtual Machines.localized', 'VirtualBox VMs',
        'Documents/Virtual Machines.localized', 'Library/Containers/com.utmapp.UTM/Data/Documents',
        '.lima', '.colima', '.local/share/containers/podman/machine']]
    # Existing preparation drivers retain deleted historical receipt dependencies.
    ios_receipts = ['architecture/evidence/engine-completion-review/receipt.json',
        'architecture/evidence/native-preparation/nat-1.3-20261013/receipt.json',
        'architecture/progress/.roadmap-runner/09-native-preparation-9c393cca2aad/source-d18a82d0de7a.md']
    android_receipts = ['architecture/evidence/native-preparation/nat-1.4-20261013/receipt.json']
    owners = {row['profile']: row for row in upstream['suites']}
    ios_route = route(owners['ios']['implementationOwner'], 'bash tests/native/ios-control.sh --output "$TASK_OUTPUT"',
        ['core/tests/native/ios-control.sh', 'core/tests/native/ios-control.py'] + ios_receipts,
        'Existing NAT-1.5 target UIKit preparation only; not full SDK qualification.',
        [p for p in ios_receipts if not (ROOT / p).exists()])
    android_route = route(owners['android']['implementationOwner'], 'bash tests/native/android-control.sh --output "$TASK_OUTPUT"',
        ['core/tests/native/android-control.sh', 'core/tests/native/android-control.py'] + android_receipts,
        'Existing NAT-1.6 target EditText preparation only; not full SDK qualification.',
        [p for p in android_receipts if not (ROOT / p).exists()])
    targets = {
        'web': {'runtime': 'macOS OS host; Safari/Chrome and pinned Playwright desktop browsers',
            'owner': owners['web']['implementationOwner'], 'browsers': browsers, 'playwright': playwright,
            'packageRoute': route('QWB-1.1', 'npm run build:wasm && npm run build && npm run test:browser',
                ['core/package.json', 'core/scripts/test-browser.mjs'],
                'Desktop web only. Mobile web still requires named mobile target runtime.'),
            'unavailablePrerequisites': []},
        'ios': {'runtime': 'iOS Simulator; never macOS Swift host XCTest', 'owner': owners['ios']['implementationOwner'],
            'runtimes': runtimes, 'devices': devices, 'packageRoute': ios_route,
            'buildRoute': 'cargo +1.97.1 build --offline --locked -p editac-ffi --lib --target aarch64-apple-ios-sim; '
                          'xcrun --sdk iphonesimulator swiftc -target arm64-apple-ios26.5-simulator (native UIKit host)',
            'unavailablePrerequisites': ios_route['unavailablePrerequisites']},
        'android': {'runtime': 'Android Emulator arm64-v8a; never JVM/JNA host tests',
            'owner': owners['android']['implementationOwner'], 'avds': avds, 'packageRoute': android_route,
            'buildInputs': [fact(SDK / p) for p in ['platforms/android-36', 'build-tools/36.0.0',
                'ndk/27.1.12297006', 'ndk/27.1.12297006/toolchains/llvm/prebuilt/darwin-x86_64/bin/aarch64-linux-android35-clang']],
            'packageProject': pin('core/native/android/probe/control/build.gradle.kts'),
            'unavailablePrerequisites': android_route['unavailablePrerequisites']},
        'macos': {'runtime': 'current macOS arm64 OS host, native AppKit', 'owner': owners['macos']['implementationOwner'],
            'packageRoute': route(owners['macos']['implementationOwner'], 'bash native/macos/scripts/check.sh bootstrap',
                ['core/native/macos/Package.swift', 'core/native/macos/scripts/check.sh',
                 'core/native/macos/scripts/check.py'], 'Existing AppKit bootstrap, not full platform proof.'),
            'unavailablePrerequisites': []},
    }
    for target, owner in [('windows', 'RWI-1.1'), ('linux', 'RLN-1.1')]:
        targets[target] = {'runtime': 'unavailable: no documented accessible OS host/VM located',
            'owner': owner, 'implementation': fact(ROOT / 'core/native' / target),
            'packageRoute': {'owner': owner, 'command': None, 'executed': False,
                'scope': 'No existing SDK/package/dispatcher; do not represent a planned command as executable.'},
            'unavailablePrerequisites': ['Accessible ' + target + ' OS host/VM with native desktop session',
                'Native SDK implementation, toolkit/package toolchain and dispatcher'],
            'unblock': owner + ' must locate an authorized local/available VM or test host, record OS/toolkit '
                       'versions and provide the missing SDK/package/dispatcher. No cloud or paid provisioning authorized.',
            'retry': 'Documented host/VM access or native implementation inputs change; no unchanged retries.'}
    for target, row in targets.items():
        row['implementationOwner'] = owners[target]['implementationOwner']
        row['testingOwners'] = owners[target]['requiredTestingOwners']
        row['runtimeQualification'] = 'not executed'
        row['unblockOwner'] = row['owner']
        if target in ['ios', 'android']:
            row['unblock'] = 'Owner replaces obsolete receipt-bound preparation with current-source target harness; '
            row['unblock'] += 'retain original case IDs, real controls/engine and complete final qualification ownership.'
    native_env = {'DEVELOPER_DIR': DEVELOPER, 'PATH': str(node_bin) + ':' + str(HOME / '.cargo/bin') + ':' + os.environ.get('PATH', '')}
    for target in ['web', 'ios', 'macos']:
        targets[target]['packageRoute']['environment'] = native_env
    targets['android']['packageRoute']['environment'] = dict(native_env, JAVA_HOME=str(JAVA),
        ANDROID_HOME=str(SDK), ANDROID_SDK_ROOT=str(SDK))
    targets['android']['unavailablePrerequisites'].extend([
        'Pinned Gradle 8.14 distribution and checksum-verified archive are absent; cached 9.3.1 is not the pinned route'
    ] if not gradle.exists() else [])
    if not (ROOT / 'core/target/native-tooling/gradle-8.14-bin.zip').is_file():
        targets['android']['unavailablePrerequisites'].append('Checksum-pinned Gradle 8.14 archive required by existing target driver')
    targets['ios']['runtimePaths'] = [fact(r['bundlePath']) for r in runtimes if r.get('bundlePath')]
    for target in ['ios', 'android']:
        targets[target]['unavailablePrerequisites'].append(
            'Current-source packaged SDK target harness; existing driver proves preparation controls only')
    for target, required_target in [('ios', 'aarch64-apple-ios-sim'), ('android', 'aarch64-linux-android'),
                                    ('web', 'wasm32-unknown-unknown')]:
        if required_target not in text(probes, 'rust-targets').splitlines():
            targets[target]['unavailablePrerequisites'].append('Rust target ' + required_target)
    if not any(r.get('isAvailable') and r.get('identifier') == 'com.apple.CoreSimulator.SimRuntime.iOS-26-5' for r in runtimes):
        targets['ios']['unavailablePrerequisites'].append('iOS 26.5 Simulator runtime required by existing target driver')
    if not avds or not all(a['image']['exists'] and a['systemImage']['exists'] for a in avds):
        targets['android']['unavailablePrerequisites'].append('Named Android AVD and complete system image')
    for item in targets['android']['buildInputs']:
        if not item['exists']:
            targets['android']['unavailablePrerequisites'].append(item['path'])
    if text(probes, 'node-pinned').strip() != 'v' + package['engines']['node']:
        targets['web']['unavailablePrerequisites'].append('Pinned Node ' + package['engines']['node'])
    if text(probes, 'npm-pinned').strip() != package['engines']['npm']:
        targets['web']['unavailablePrerequisites'].append('Pinned npm ' + package['engines']['npm'])
    if not playwright['required'] or not all(p['available'] for p in playwright['executables']):
        targets['web']['unavailablePrerequisites'].append('Pinned Playwright browser specification and executable cache')
    mac_pin = json.loads((ROOT / 'core/native/macos/toolchain.json').read_text())
    mac_actual = {'xcode': text(probes, 'xcode').strip(), 'swift': text(probes, 'swift').strip(),
        'sdkVersion': text(probes, 'macos-sdk-version').strip(), 'sdkBuild': text(probes, 'macos-sdk-build').strip()}
    targets['macos']['toolchainPin'] = {'expected': mac_pin, 'observed': mac_actual}
    for key in ['sdkVersion', 'sdkBuild']:
        if mac_actual[key] != mac_pin[key]:
            targets['macos']['unavailablePrerequisites'].append('macOS ' + key + ' pin mismatch')
    console_owner = pwd.getpwuid(Path('/dev/console').stat().st_uid).pw_name
    targets['macos']['consoleOwner'] = console_owner
    if console_owner in ['root', 'loginwindow']:
        targets['macos']['unavailablePrerequisites'].append('Logged-in native GUI desktop session')
    for path in ['architecture/specs/verification.md', 'core/package.json', 'core/package-lock.json',
                 'core/rust-toolchain.toml', 'cli/rust-toolchain.toml', 'core/native/ios/Package.swift',
                 'core/native/macos/Package.swift', 'core/native/macos/toolchain.json', 'core/tests/native/ios-control.py',
                 'core/tests/native/android-control.py', 'core/tests/native/kotlin-fixture.py', __file__]:
        pin(path)
    access = access_search()
    return {'schemaVersion': 1, 'parent': 'RRD-1.2', 'collectedUtc': datetime.now(timezone.utc).isoformat(),
        'prerequisites': {'RRD-1.2': {'state': 'availability-inventoried', 'nextOwner': 'RRD-1.3',
            'runtimeQualification': 'none; missing harness/runtime inputs remain explicit'}},
        'host': {'system': platform.system(), 'machine': platform.machine(), 'os': platform.mac_ver()[0]},
        'targets': targets, 'toolchains': {'rustInstalled': str(rust), 'rustTargets': text(probes, 'rust-targets').splitlines(),
            'nodePinnedBin': str(node_bin), 'packageEngines': package['engines'],
            'javaHome': str(JAVA), 'gradle814': fact(gradle), 'androidSdk': str(SDK),
            'cachedGradles': [str(p) for p in cached_gradles],
            'androidPackages': {p: properties(SDK / p / 'source.properties') for p in [
                'platforms/android-36', 'build-tools/36.0.0', 'ndk/27.1.12297006']},
            'terminal': {'cwd': str(ROOT / 'cli'), 'command': 'cargo +1.97.1 test --offline --locked',
                         'scope': 'Existing terminal source suite, not executed'},
            'shared': {'cwd': str(ROOT / 'core'), 'command': 'cargo +1.97.1 test --offline --locked --workspace',
                       'scope': 'Existing shared source suite, not executed'}},
        'runtimeAccess': {'tools': vm_tools, 'localPaths': [fact(p) for p in vm_paths], 'documentation': access,
                         'limitation': 'Local discovery only; no remote availability claim or network probe.'},
        'probes': probes, 'sourcePins': dict(PINS),
        'prohibitedActionsExecuted': {'boot': 0, 'tests': 0, 'providers': 0, 'network': 0, 'provisioning': 0}}


def validate(data):
    if data.get('mode') == 'scoped-proof-metadata':
        if data != scoped_proof():
            raise ValueError('Saved scoped proof differs from authoritative metadata/current inputs')
        proof = data['proof']
        predicates = [data['parent'] == 'SFC-1.1', bool(data['sourceAuthentication']),
                      sum(proof['suites'].values()) == proof['rustDistinctPassed'] == 59,
                      proof['rustFailed'] == proof['rustRequiredSkipped'] == 0,
                      len(proof['setupFailures']) == 2, bool(proof.get('commands')),
                      not data['probes'], all(v == 0 for v in data['prohibitedActionsExecuted'].values())]
        predicates += [Path(p).is_file() and hashlib.sha256(Path(p).read_bytes()).hexdigest() == sha
                       for p, sha in data['sourcePins'].items()]
        if not all(predicates):
            raise ValueError('Scoped proof metadata or current pins changed')
        return {'inventoryChecks': {'executed': len(predicates), 'passed': len(predicates), 'failed': 0, 'skipped': 0},
                'availabilityProbes': {'executed': 0, 'passed': 0, 'failed': 0, 'skipped': 0},
                'collectionNewProbes': 0, 'collectionReusedProbes': 0, 'runtimeTestsExecuted': 0,
                'output': str(OUT)}
    checks = []
    def require(ok, name):
        checks.append(name)
        if not ok:
            raise ValueError(name)
    require(set(data['targets']) == {'web', 'ios', 'android', 'macos', 'windows', 'linux'}, 'six target profiles')
    require(data['parent'] == 'RRD-1.2', 'original parent')
    require(all(v == 0 for v in data['prohibitedActionsExecuted'].values()), 'no runtime/application/provider execution')
    for target, row in data['targets'].items():
        require(bool(row['owner']) and row['owner'] == row['unblockOwner'], target + ' owner')
        require(row['runtimeQualification'] == 'not executed', target + ' no qualification claim')
        require(bool(row['packageRoute'].get('command') or row['unavailablePrerequisites']), target + ' route or explicit absence')
        require(row['packageRoute']['executed'] is False, target + ' command not executed')
        for item in row['packageRoute'].get('inputs', []):
            require(item['exists'] == Path(item['path']).exists(), target + ' route input ' + item['path'])
            require(item['exists'] or item['path'].replace(str(ROOT) + '/', '') in row['unavailablePrerequisites'],
                    target + ' missing route input has explicit disposition')
    for row in data['targets']['ios']['runtimePaths'] + data['targets']['android']['buildInputs']:
        require(row['exists'] == Path(row['path']).exists(), 'target runtime/build path ' + row['path'])
    for avd in data['targets']['android']['avds']:
        for key in ['image', 'properties', 'systemImage']:
            item = avd[key]
            require(item['exists'] == Path(item['path']).exists(), 'AVD input ' + item['path'])
    for browser in data['targets']['web']['playwright']['executables']:
        require(browser['available'] or bool(data['targets']['web']['unavailablePrerequisites']),
                'browser available or explicit prerequisite ' + browser['name'])
    require({'terminal', 'shared'} <= data['toolchains'].keys(), 'terminal/shared suite routes retained')
    for path, sha in data['sourcePins'].items():
        require(Path(path).is_file() and hashlib.sha256(Path(path).read_bytes()).hexdigest() == sha, 'source pin ' + path)
    for p in data['probes']:
        log = Path(p['log'])
        require(log.is_file() and hashlib.sha256(log.read_bytes()).hexdigest() == p['sha256'], 'probe log ' + p['id'])
    ignored = subprocess.run(['git', '-C', str(ROOT / 'architecture'), 'check-ignore', '-q', str(OUT)], check=False)
    require(ignored.returncode == 0, 'ignored runtime artifact')
    counts = {'executed': len(checks), 'passed': len(checks), 'failed': 0, 'skipped': 0}
    probe_counts = {'executed': len(data['probes']), 'passed': sum(p['exit'] == 0 for p in data['probes']),
                    'failed': sum(p['exit'] != 0 for p in data['probes']), 'skipped': 0}
    return {'inventoryChecks': counts, 'availabilityProbes': probe_counts,
            'collectionNewProbes': sum(not p.get('reused', False) for p in data['probes']),
            'collectionReusedProbes': sum(p.get('reused', False) for p in data['probes']),
            'unavailableProbes': [p['id'] for p in data['probes'] if p['exit'] != 0],
            'runtimeTestsExecuted': 0, 'output': str(OUT)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='check saved pins/logs; no runtime probes')
    parser.add_argument('--reuse-probes', action='store_true',
                        help='reuse unchanged command/log receipts during this inventory session')
    arguments(parser)
    args = parser.parse_args()
    configure(args.manifest, args.runtime_root)
    if args.reuse_probes:
        SAVED_PROBES.update({p['id']: p for p in json.loads(OUT.read_text())['probes']})
    data = json.loads(OUT.read_text()) if args.check else collect()
    result = validate(data)
    result['probesExecutedThisInvocation'] = 0 if args.check else result['collectionNewProbes']
    if not args.check:
        if LINK.exists() and not LINK.is_symlink():
            raise ValueError('Refuse to replace regular runtime inventory')
        if LINK.is_symlink() and LINK.resolve() != OUT:
            raise ValueError('Refuse to replace another runtime inventory link')
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(data, indent=2) + '\n')
        LINK.parent.mkdir(parents=True, exist_ok=True)
        if not LINK.is_symlink():
            CONFIG.link(LINK, OUT)
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
