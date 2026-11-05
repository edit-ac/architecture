#!/usr/bin/env python3
"""Install or check EWP-1.1 only; never loads the caller's Composer credentials."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).resolve().parent
PROFILE = ROOT / "toolchains/php-development.json"
ARTIFACTS = ROOT / ".artifacts/ewp-1.1"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["install", "check"])
    args = parser.parse_args()
    if args.operation == "check":
        print("TAP version 13", flush=True)
    profile = json.loads(PROFILE.read_text())
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    # An isolated HOME/config/cache and an allowlist prevent ambient auth/plugin use.
    home = ARTIFACTS / "home"
    home.mkdir(exist_ok=True)
    env = {
        "PATH": "/usr/bin:/bin:/usr/sbin:/sbin",
        "HOME": str(home),
        "COMPOSER_HOME": str(home / "composer"),
        "COMPOSER_CACHE_DIR": str(ARTIFACTS / "composer-cache"),
        "COMPOSER_NO_INTERACTION": "1",
    }
    php = profile["php"]["executable"]
    composer = profile["composer"]["executable"]
    passed = 0

    def require(condition, message):
        nonlocal passed
        if not condition:
            raise RuntimeError(message)
        passed += 1
        if args.operation == "check":
            print(f"ok {passed} - {message}", flush=True)

    def run(argv):
        return subprocess.check_output(argv, cwd=SOURCE, env=env, text=True, stderr=subprocess.STDOUT).strip()

    require(platform.system() == "Darwin" and platform.machine() == "arm64", "Profile requires macOS ARM64")
    for name in ["php", "composer"]:
        entry = profile[name]
        require(hashlib.sha256(Path(entry["executable"]).read_bytes()).hexdigest() == entry["sha256"], f"{name} executable differs from pin; explicitly review/update the profile")
    php_version = run([php, "-r", "echo PHP_VERSION;"])
    composer_version = run([php, composer, "--version", "--no-ansi"])
    require(php_version == profile["php"]["version"], "PHP version differs from pin")
    require(composer_version.startswith("Composer version " + profile["composer"]["version"] + " "), "Composer version differs from pin")
    print("# " + json.dumps({"php": php_version, "composer": composer_version, "provenanceChecks": passed}), flush=True)
    if args.operation == "install":
        if not (SOURCE / "composer.lock").is_file():
            raise RuntimeError("Missing composer.lock; dependency resolution is an explicit maintainer operation")
        print(run([php, composer, "install", "--no-dev", "--no-plugins", "--no-scripts", "--prefer-dist", "--no-progress", "--no-interaction"]), flush=True)
        return
    # Separate PHP processes establish an actual closed-file reopen. No network command runs here.
    with tempfile.TemporaryDirectory(prefix="sqlite-", dir=ARTIFACTS) as tmp:
        database = str(Path(tmp) / "fixture.sqlite")
        for mode in ["write", "reopen"]:
            result = json.loads(run([php, str(SOURCE / "probe.php"), mode, database]))
            require(result["executed"] > 0 and result["failed"] == 0 and result["skipped"] == 0, f"Invalid {mode} runtime counts")
            require(result["sqliteVersion"] == profile["php"]["sqliteVersion"], "SQLite runtime differs from pin")
            for assertion in range(result["passed"]):
                passed += 1
                print(f"ok {passed} - {mode} PHP/PDO assertion {assertion + 1}", flush=True)
            print("# " + json.dumps(result), flush=True)
    print(f"1..{passed}\n# tests {passed}\n# pass {passed}\n# fail 0\n# skipped 0", flush=True)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as error:
        print(json.dumps({"failed": 1, "error": str(error), "output": getattr(error, "output", None)}), flush=True)
        raise SystemExit(1)
