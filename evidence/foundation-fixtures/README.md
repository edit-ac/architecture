# FND-1.2 reproducible semantic fixtures

Implemented and locally verified 2026-10-11; no deployment or engine qualification.
Source snapshot SHA-256/revision: `38b5b9d96921dc419471bdce3a85537df40e7bc3255ebbdc4a20c0ace71d0897`.
Core base `f3d4d35182ee4a96ec99bc5b30832cee22c9bb14`; implementation is uncommitted.
[Receipt](receipt.json) identifies exact working-tree hashes, runtime and commands.

`core/fixtures/generate.mjs`, `manifest.json`, `README.md` and
`tests/fixtures.test.mjs` provide fixed-seed schema-neutral recipes and compact
expected semantic shapes. `package.json` adds `check:fixtures` to the existing
workspace check. Existing dependency pins and unrelated edits are preserved.

Task: 20 blocks / 10,240 UTF-8 text bytes; Long: 2,000 / 1,048,576;
Large: 10,000 / 5,242,880. Aged references Long plus 100,000 seeded
insert/delete operations. A separate string oracle verifies valid targets,
UTF-16 deletion lengths and unchanged final content. It is not an applied engine
state. Adversarial cases cover a 250 KiB paragraph, 1,024 fragmented marks,
8 Unicode families, invalid surrogate-interior positions, depths 31/32/33 and
4-by-128 table cells. Multi-editor inputs declare 50 static previews and
separate 1/10 active-editor scenarios. Neither the nesting boundary nor these
scenarios establish supported engine/runtime limits.

Manifest text hashes/bytes exclude JSON recipes; serialized CRDT bytes/hashes
and engine anchor results remain null. Corpus JSON hashes pin text, attributes,
structure and operation recipes without adopting a schema.

| Check | Result | Evidence |
| --- | --- | --- |
| `node --test tests/fixtures.test.mjs` | exit 0; 9 executed / 9 passed / 0 failed / 0 skipped / 0 cancelled | [log](logs/fixtures-initial.log) |
| `node --test tests/protocol-toolchain.test.mjs` | exit 0; 3 executed / 3 passed / 0 failed / 0 skipped / 0 cancelled | [log](logs/js-integration.log) |
| `node fixtures/generate.mjs TEMP/a`, then `TEMP/b` | both exit 0; 10 files byte-identical, committed manifest matches; zero mismatches | [hash receipt](reproducibility.json), [a](logs/cli-a.log), [b](logs/cli-b.log) |
| `git diff --check -- package.json fixtures tests/fixtures.test.mjs` | exit 0 | [log](logs/diff-check.log) |

Commands used `/Users/bpstr/.nvm/versions/node/v24.19.0/bin` because the host's
other Node symlink has a different version. No network/provider calls, secret
loading, Rust rebuild, publication or second roadmap parent was involved.

Test temporary directories were removed in finally; independent CLI cleanup
removed 43,345,932 bytes of temporary files (exact path in hash receipt).
[Cleanup receipt](cleanup.json) reports no remaining task process candidates,
no servers/browsers started, and 17.44 GiB data-volume free. Free space remains
low; this iteration created no persistent build/cache output, and unrelated
artifacts/processes were preserved. No broader cleanup was attempted.

Next dependency-ready parent: FND-1.3, bidirectional real Yrs/Yjs v1 update and
state-vector exchange over a tiny XML/text fixture. FND-1.2 closes input recipe
acceptance only; structural identity, engine anchors and applied Aged CRDT
measurements belong to subsequent probes.
