# Local PHP bootstrap

EWP-1.1 pins the already installed macOS ARM64 Homebrew runtime in
[`../php-development.json`](../php-development.json). This probe is a plain PHP
Composer consumer; it does not implement the editor SDK or qualify Laravel/Filament.

From the architecture repository:

```sh
python3 toolchains/php-bootstrap/bootstrap.py install
python3 toolchains/php-bootstrap/bootstrap.py check
```

Installation downloads only locked `psr/log` and generates the local Composer
autoload files. It uses an isolated Composer home/cache, disables scripts/plugins
and does not read the caller's credentials. The check runs offline, verifies the
runtime pins and Composer autoload, and uses separate PHP processes to write and
reopen a real SQLite file. Its three BLOB inputs cover NUL/invalid UTF-8 bytes,
Unicode text and empty bytes. Temporary databases are removed on success or failure.
The TAP summary reports actual assertions with no skipped cases.

The profile's framework versions are selected from official package metadata and
the original Laravel/Filament owners. Their full graph installation, lockfiles and
runtime delivery remain with those owners. No framework is required here.

On a different host, provision maintained official PHP/Composer distributions and
explicitly review the paths, versions and executable digests in the profile. A
digest/version mismatch fails rather than upgrading silently. The committed lock
must exist; changing dependencies is an explicit maintainer resolution step.

Generated dependencies stay in ignored `vendor/`; download/cache/log output stays
in ignored `../../.artifacts/ewp-1.1/`.
