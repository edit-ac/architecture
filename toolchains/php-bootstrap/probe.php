<?php
declare(strict_types=1);

use EditAc\Toolchain\BinaryFixture;
use Psr\Log\NullLogger;

$passed = 0;
function check(bool $condition, string $message): void
{
    global $passed;
    if (!$condition) {
        throw new RuntimeException($message);
    }
    $passed++;
}

try {
    require __DIR__ . '/vendor/autoload.php';
    check(class_exists(BinaryFixture::class) && class_exists(NullLogger::class), 'Composer PSR-4/dependency autoload');
    (new NullLogger())->info('Local deterministic bootstrap');
    check(in_array('sqlite', PDO::getAvailableDrivers(), true), 'PDO SQLite unavailable');
    foreach (Composer\InstalledVersions::getInstalledPackages() as $package) {
        check(!preg_match('/^(laravel|illuminate|filament|livewire)\//', $package), 'Unexpected framework dependency');
    }
    [$script, $mode, $path] = $argv;
    if (!in_array($mode, ['write', 'reopen'], true)) {
        throw new RuntimeException('Expected write or reopen');
    }
    if ($mode === 'write' && file_exists($path)) {
        throw new RuntimeException('Refusing to overwrite existing SQLite file');
    }
    if ($mode === 'reopen' && !is_file($path)) {
        throw new RuntimeException('SQLite file missing before reopen');
    }
    $db = new PDO('sqlite:' . $path, null, null, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
    $sqliteVersion = $db->query('SELECT sqlite_version()')->fetchColumn();
    if ($mode === 'write') {
        $db->exec('CREATE TABLE fixture (id TEXT PRIMARY KEY, payload BLOB NOT NULL)');
        $db->beginTransaction();
        $insert = $db->prepare('INSERT INTO fixture VALUES (:id, :payload)');
        foreach (BinaryFixture::cases() as $id => $bytes) {
            $insert->bindValue(':id', $id, PDO::PARAM_STR);
            $insert->bindValue(':payload', $bytes, PDO::PARAM_LOB);
            $insert->execute();
        }
        $db->commit();
        check((int) $db->query('SELECT count(*) FROM fixture')->fetchColumn() === 3, 'Expected three committed rows');
    } else {
        $rows = $db->query('SELECT id, payload, typeof(payload) AS storage_type FROM fixture')->fetchAll(PDO::FETCH_ASSOC);
        check(count($rows) === 3, 'Expected three rows after process restart');
        $expected = BinaryFixture::cases();
        foreach ($rows as $row) {
            check(array_key_exists($row['id'], $expected) && $row['payload'] === $expected[$row['id']] && $row['storage_type'] === 'blob', 'Binary BLOB reopen mismatch: ' . $row['id']);
        }
        check($db->query('PRAGMA integrity_check')->fetchColumn() === 'ok', 'SQLite integrity check');
    }
    $db = null;
    echo json_encode(['mode' => $mode, 'sqliteVersion' => $sqliteVersion, 'executed' => $passed, 'passed' => $passed, 'failed' => 0, 'skipped' => 0], JSON_THROW_ON_ERROR), PHP_EOL;
} catch (Throwable $error) {
    fwrite(STDERR, json_encode(['executed' => $passed + 1, 'passed' => $passed, 'failed' => 1, 'skipped' => 0, 'error' => $error->getMessage()]) . PHP_EOL);
    exit(1);
}
