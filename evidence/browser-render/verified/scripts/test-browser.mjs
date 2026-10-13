import { spawnSync } from 'node:child_process';
import { join } from 'node:path';

// Explicit named suites: an unknown name must fail instead of matching zero tests.
const [suite, ...options] = process.argv.slice(2);
const suites = { recovery: ['tests/browser/entry.spec.ts', 'tests/browser/recovery.spec.ts'], render: ['tests/browser/render.spec.ts'] };
if (!suites[suite]) throw new Error('Expected browser suite: recovery or render');
const engines = suite === 'render' ? ['chromium', 'firefox', 'webkit'] : [null];
for (const engine of engines) {
  const env = { ...process.env };
  if (engine) {
    env.EDITAC_RENDER_BROWSER = engine;
    if (env.EDITAC_RENDER_OUTPUT) env.EDITAC_RENDER_OUTPUT = join(env.EDITAC_RENDER_OUTPUT, engine);
    console.log(`Render browser: ${engine}`);
  }
  const result = spawnSync(process.execPath, ['--test', ...options, ...suites[suite]], { stdio: 'inherit', env });
  if (result.error) throw result.error;
  if (result.status !== 0) process.exitCode = result.status ?? 1;
}
