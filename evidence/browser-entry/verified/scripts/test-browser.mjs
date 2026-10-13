import { spawnSync } from 'node:child_process';

// Explicit named suites: an unknown name must fail instead of matching zero tests.
const [suite, ...options] = process.argv.slice(2);
if (suite !== 'recovery') throw new Error('Expected browser suite: recovery');
const result = spawnSync(process.execPath, ['--test', ...options, 'tests/browser/entry.spec.ts', 'tests/browser/recovery.spec.ts'], {
  stdio: 'inherit', env: process.env,
});
if (result.error) throw result.error;
process.exitCode = result.status ?? 1;
