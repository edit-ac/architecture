import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';

// Design-plan checks only. No encryption implementation is exercised here.
const plan = JSON.parse(readFileSync(new URL('./security-profiles.json', import.meta.url)));
const decision = readFileSync(new URL('../decisions/003-encryption-profiles.md', import.meta.url), 'utf8');
const review = readFileSync(new URL('../evidence/security-threat-model.md', import.meta.url), 'utf8');
const fixture = name => {
  const found = plan.fixtures.find(item => item.id === `SEC-F-${name}`);
  assert.ok(found, `Missing acceptance fixture: ${name}`);
  return found;
};
const outcome = (name, expected, parent) => {
  const item = fixture(name);
  assert.equal(item.expected, expected);
  assert.equal(item.parent, parent);
};

test('SEC-1.1 profiles distinguish local storage, relay protection and TLS', () => {
  assert.deepEqual(Object.keys(plan.profiles).sort(), ['baseline', 'e2ee', 'local-at-rest']);
  assert.equal(plan.profiles.baseline.protectBeforePersist, false);
  assert.equal(plan.profiles.baseline.protectBeforeRelay, false);
  assert.equal(plan.profiles['local-at-rest'].protectBeforePersist, true);
  assert.equal(plan.profiles['local-at-rest'].protectBeforeRelay, false);
  assert.equal(plan.profiles.e2ee.protectBeforePersist, true);
  assert.equal(plan.profiles.e2ee.protectBeforeRelay, true);
  for (const profile of Object.values(plan.profiles)) assert.equal(profile.tlsIsE2ee, false);
  assert.deepEqual(plan.profiles.e2ee.plaintextEndpoints,
    ['authorized-client', 'explicitly-authorized-decrypting-endpoint']);
  assert.ok(plan.profiles['local-at-rest'].plaintextEndpoints.includes('configured-plaintext-sync'));
});

test('SEC-1.1 creation and failure never authorize plaintext fallback', () => {
  outcome('create-first', 'no-plaintext-first-write', 'SEC-1.5');
  outcome('create-failure', 'abort-without-plaintext', 'SEC-1.5');
  outcome('commit-crash', 'recover-acknowledged-protected-state', 'SEC-1.5');
});

test('SEC-1.1 authentication, writer authority and freshness have distinct obligations', () => {
  for (const name of ['wrong-key', 'tamper', 'cross-document', 'cross-epoch', 'cross-schema', 'cross-key-epoch']) {
    outcome(name, 'reject-before-apply', 'SEC-1.3');
  }
  outcome('replay', 'no-second-application', 'SEC-1.3');
  outcome('counter-restore', 'safe-protocol-recovery-or-locked', 'SEC-1.3');
  outcome('oversized', 'reject-before-unbounded-allocation', 'SEC-1.3');
  outcome('readonly-forgery', 'reject-authenticated-reader-write', 'SEC-1.3');
  outcome('host-auth-no-key', 'locked-no-key-delegation', 'SEC-1.4');
});

test('SEC-1.1 lost keys and scoped use have honest recovery and disclosure limits', () => {
  outcome('lost-key', 'unavailable-without-authorized-recovery', 'SEC-1.4');
  outcome('key-cleanup', 'scoped-use-no-key-in-locator-log-tool', 'SEC-1.4');
});

test('SEC-1.1 offline revocation preserves knowledge limits and protected pending work', () => {
  outcome('offline-revoked', 'no-new-epoch-access-old-plaintext-not-erased', 'SEC-1.7');
  outcome('old-pending', 'quarantine-retain-no-silent-admission-or-loss', 'SEC-1.7');
});

test('SEC-1.1 relay receipts and incompatible peers cannot imply plaintext acceptance', () => {
  outcome('opaque-receipt', 'ciphertext-storage-only-receipt', 'SEC-1.6');
  outcome('incompatible-peer', 'visible-incompatible-no-plaintext', 'SEC-1.6');
});

test('SEC-1.1 history, attachments, backups and exports retain the full protection boundary', () => {
  outcome('history-key-missing', 'unavailable-history-no-approximation', 'SEC-1.8');
  outcome('attachment-binding', 'reject-cross-document-attachment', 'SEC-1.8');
  outcome('backup-cache-leak', 'seed-absent-from-unauthorized-artifacts-logs', 'SEC-1.8');
  outcome('implicit-export', 'deny-without-explicit-plaintext-authorization', 'SEC-1.8');
});

test('SEC-1.1 agents require an authorized plaintext endpoint and ordinary edit policy', () => {
  outcome('opaque-agent', 'deny-plaintext-tools-on-relay', 'SEC-1.9');
  outcome('local-agent-readonly', 'local-authorized-readonly-cannot-edit', 'SEC-1.9');
  outcome('metadata-observer', 'declare-identifiers-size-timing-participants-not-content', 'SEC-1.1');
});

test('SEC-1.1 every declared asset and attacker maps to a reviewed invariant and named planned check', () => {
  assert.ok(plan.fixtures.length >= 27);
  assert.equal(new Set(plan.fixtures.map(item => item.id)).size, plan.fixtures.length);
  assert.deepEqual([...new Set(plan.fixtures.map(item => item.asset))].sort(), plan.assets);
  assert.deepEqual([...new Set(plan.fixtures.map(item => item.attacker))].sort(), plan.attackers);
  const checks = new Map([
    ['SEC-1.1', 'node --test tests/security-profiles.test.mjs'],
    ['SEC-1.3', 'envelopes'], ['SEC-1.4', 'key_lifecycle'], ['SEC-1.5', 'protected_store'],
    ['SEC-1.6', 'encrypted_sync'], ['SEC-1.7', 'rotation'], ['SEC-1.8', 'assets'],
    ['SEC-1.9', 'capabilities'],
  ]);
  for (const item of plan.fixtures) {
    assert.match(item.invariant, /^SEC-INV-[a-z-]+$/);
    assert.ok(decision.includes(`\n## ${item.decisionSection}\n`), item.id);
    for (const field of ['id', 'asset', 'attacker', 'invariant', 'parent', 'expected']) {
      assert.ok(review.includes(item[field]), `${item.id}: missing review ${field}`);
    }
    assert.ok(checks.has(item.parent));
    const target = checks.get(item.parent);
    assert.equal(item.plannedCheck, item.parent === 'SEC-1.1' ? target
      : `cargo test -p editac-security --test ${target} --locked`);
    assert.equal(item.state, item.parent === 'SEC-1.1' ? 'design-contract' : 'planned-behavior');
  }
});

test('SEC-1.1 design review leaves cryptography and independent review unqualified', () => {
  assert.equal(plan.schema, 1);
  assert.equal(plan.gate, 'SEC-1.1');
  assert.equal(plan.qualification, 'design-only');
  assert.equal(plan.protocolSelected, false);
  assert.equal(plan.productionReady, false);
  assert.deepEqual(plan.exclusions, [
    'compromised-unlocked-endpoint', 'malicious-authorized-writer',
    'authorized-reader-copy-or-collusion', 'traffic-analysis-or-denial-of-service',
    'global-rollback-without-trusted-freshness', 'historical-plaintext-copies',
  ]);
  assert.ok(decision.includes('## Resolved and open decisions'));
  assert.ok(decision.includes('roadmap 24'));
});
