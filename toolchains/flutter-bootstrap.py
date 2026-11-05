#!/usr/bin/env python3
"""ECM-1.1: install a pinned official SDK and compile an empty Dart consumer."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
import zipfile


PROFILE = Path(__file__).with_name("flutter-development.json")
WORKSPACE = PROFILE.parents[2]


def digest(path):
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def save_json(path, value):
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(path)


def install(profile, destination):
    pin = profile["flutter"]
    storage = profile["storage"]
    marker = destination / "install.json"
    if marker.exists():
        installed = json.loads(marker.read_text())
        if installed["archiveSha256"] != pin["archiveSha256"]:
            raise RuntimeError("Existing SDK installation has a different archive pin")
        if not (destination / "flutter/bin/dart").is_file():
            raise RuntimeError("Existing installation is incomplete; preserve it for diagnosis")
        print("Reusing verified archive installation:", destination)
        return
    if (destination / "flutter").exists():
        raise RuntimeError("Unreceipted SDK exists; refusing to replace it")
    destination.mkdir(parents=True, exist_ok=True)
    if shutil.disk_usage(destination).free < storage["minimumFreeBytes"]:
        raise RuntimeError("Insufficient free disk space for bounded installation")
    archive = destination / "sdk.zip.partial"
    if not archive.exists():
        request = urllib.request.Request(pin["archiveUrl"])
        with urllib.request.urlopen(request, timeout=30) as response, archive.open("xb") as target:
            length = int(response.headers.get("Content-Length", "0"))
            if length != pin["archiveBytes"] or length > storage["maximumArchiveBytes"]:
                raise RuntimeError("Unexpected official archive length")
            total = 0
            while chunk := response.read(1024 * 1024):
                total += len(chunk)
                if total > storage["maximumArchiveBytes"]:
                    raise RuntimeError("Archive exceeded storage bound")
                target.write(chunk)
    if archive.stat().st_size != pin["archiveBytes"] or digest(archive) != pin["archiveSha256"]:
        raise RuntimeError("Archive size/SHA-256 mismatch; preserve failed input, do not extract")
    with zipfile.ZipFile(archive) as bundle:
        size = sum(item.file_size for item in bundle.infolist())
        if size > storage["maximumExtractedBytes"]:
            raise RuntimeError("SDK exceeds extracted storage bound")
        for item in bundle.infolist():
            path = Path(item.filename)
            if path.is_absolute() or ".." in path.parts or path.parts[0] != "flutter":
                raise RuntimeError("Unexpected archive member path")
    # ditto preserves the executable modes and symlinks in the official bundle.
    # No chmod, shell profile changes, elevated installation or package manager.
    with tempfile.TemporaryDirectory(prefix="extract-", dir=destination) as staging:
        subprocess.run(["/usr/bin/ditto", "-x", "-k", str(archive), staging], check=True)
        (Path(staging) / "flutter").rename(destination / "flutter")
    save_json(marker, {
        "archiveUrl": pin["archiveUrl"], "archiveSha256": pin["archiveSha256"],
        "archiveBytes": archive.stat().st_size, "extractedBytes": size,
        "flutterRevision": pin["revision"], "installedAt": time.time(),
    })
    archive.unlink()
    print("Installed verified official SDK:", destination)


def check(profile, destination):
    pin = profile["flutter"]
    marker = json.loads((destination / "install.json").read_text())
    if marker["archiveSha256"] != pin["archiveSha256"]:
        raise RuntimeError("Installed archive receipt does not match profile")
    sdk = destination / "flutter"
    dart = sdk / "bin/cache/dart-sdk/bin/dart"
    flutter = sdk / "bin/flutter"
    output_root = WORKSPACE / "core/.artifacts/dart-toolchain"
    output_root.mkdir(parents=True, exist_ok=True)
    output = Path(tempfile.mkdtemp(prefix="ECM-1.1-", dir=output_root))
    environment = os.environ.copy()
    environment.update({key: os.path.expanduser(value) for key, value in profile["environment"].items()})
    # Use one Android SDK's adb, while keeping CocoaPods available through its
    # own installation path. Do not alter the user's shell or global settings.
    environment["PATH"] = os.pathsep.join(
        os.path.expanduser(value.replace("{flutter}", str(sdk)))
        for value in profile["subprocessPath"]
    )
    environment["PUB_CACHE"] = str(destination / "pub-cache")
    deadline = time.monotonic() + 300
    report = {
        "taskId": "ECM-1.1", "profileSha256": digest(PROFILE),
        "archive": marker, "sdk": str(sdk), "commands": [],
        "capabilities": profile["capabilities"],
        "executed": 0, "passed": 0, "failed": 0, "skipped": 0,
        "nativeRuntimeExecutions": 0,
    }

    def run(name, command):
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise RuntimeError("Five-minute focused bootstrap budget exhausted")
        log = output / (name + ".log")
        with log.open("w") as stream:
            try:
                result = subprocess.run(command, cwd=WORKSPACE / "core", env=environment,
                                        stdout=stream, stderr=subprocess.STDOUT,
                                        timeout=remaining, check=False)
                code = result.returncode
            except subprocess.TimeoutExpired:
                code = 124
        report["commands"].append({"name": name, "argv": command, "exitCode": code, "log": str(log)})
        save_json(output / "report.json", report)
        return code, log.read_text()

    def require(condition, name):
        report["executed"] += 1
        report["passed" if condition else "failed"] += 1
        save_json(output / "report.json", report)
        if not condition:
            raise RuntimeError(name + " failed; see " + str(output / "report.json"))

    try:
        code, version_text = run("flutter-version", [str(flutter), "--suppress-analytics", "--no-version-check", "--version", "--machine"])
        version = json.loads(version_text)
        report["version"] = version
        require(code == 0 and version["frameworkVersion"] == pin["version"]
                and version["frameworkRevision"] == pin["revision"]
                and version["channel"] == pin["channel"], "pinned Flutter provenance")
        code, version_text = run("dart-version", [str(dart), "--version"])
        report["dartVersionOutput"] = version_text.strip()
        require(code == 0 and ("Dart SDK version: " + pin["dartVersion"] + " ") in version_text,
                "pinned Dart compiler")
        # Doctor is host metadata only. Its full diagnostics and exit status are
        # retained separately; missing optional native tooling is never a pass
        # for that target and never launches a target or changes its licenses.
        code, doctor = run("flutter-doctor", [str(flutter), "--suppress-analytics", "--no-version-check", "doctor", "--verbose"])
        report["doctor"] = {"exitCode": code, "diagnostics": doctor}
        report["observedCapabilities"] = {
            "doctorCategories": [re.sub(r"^\[[^\]]*\]\s*", "", line)
                                 for line in doctor.splitlines()
                                 if re.search(r"\[(?:✓|!|✗)\]", line)],
            "androidSdkPath": environment["ANDROID_SDK_ROOT"],
            "developerDirectory": environment["DEVELOPER_DIR"],
            "androidLicenses": "not-accepted" if "licenses not accepted" in doctor
                               else "accepted" if "All Android licenses accepted" in doctor else "unknown",
            "targetQualification": "deferred; doctor/compiler metadata is not native runtime proof",
            "desktopEmbedding": profile["capabilities"]["desktop"],
        }
        require(code == 0, "doctor metadata command")
        consumer = WORKSPACE / "core" / profile["consumer"]
        report["consumerSha256"] = digest(consumer)
        code, _ = run("dart-compile", [str(dart), "compile", "exe", str(consumer), "-o", str(output / "empty-consumer")])
        require(code == 0 and (output / "empty-consumer").is_file(), "empty Dart consumer compilation")
        print(json.dumps({key: report[key] for key in ("executed", "passed", "failed", "skipped", "nativeRuntimeExecutions")}))
        print("Report:", output / "report.json")
    finally:
        save_json(output / "report.json", report)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["install", "check"])
    args = parser.parse_args()
    profile = json.loads(PROFILE.read_text())
    if platform.system() != profile["host"]["os"] or platform.machine() != profile["host"]["architecture"]:
        raise RuntimeError("This pinned profile supports macOS ARM64 only")
    destination = Path(profile["flutter"]["installDirectory"]).expanduser()
    {"install": install, "check": check}[args.operation](profile, destination)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        print("ECM-1.1:", error, file=sys.stderr)
        sys.exit(1)
