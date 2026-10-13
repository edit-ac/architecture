import { spawnSync } from 'node:child_process';
import { join } from 'node:path';

// Explicit named suites: an unknown name must fail instead of matching zero tests.
const [suite, ...options] = process.argv.slice(2);
const suites = { recovery: ['tests/browser/entry.spec.ts', 'tests/browser/recovery.spec.ts'], render: ['tests/browser/render.spec.ts'], selection: ['tests/browser/selection.spec.ts'] };
if (!suites[suite]) throw new Error('Expected browser suite: recovery, render or selection');
const engines = suite === 'render' || suite === 'selection' ? ['chromium', 'firefox', 'webkit'] : [null];
for (const engine of engines) {
  const env = { ...process.env };
  if (engine) {
    env[`EDITAC_${suite.toUpperCase()}_BROWSER`] = engine;
    const outputKey = `EDITAC_${suite.toUpperCase()}_OUTPUT`;
    if (env[outputKey]) env[outputKey] = join(env[outputKey], engine);
    console.log(`${suite} browser: ${engine}`);
  }
  const result = spawnSync(process.execPath, ['--test', ...options, ...suites[suite]], { stdio: 'inherit', env });
  if (result.error) throw result.error;
  if (result.status !== 0) process.exitCode = result.status ?? 1;
}
