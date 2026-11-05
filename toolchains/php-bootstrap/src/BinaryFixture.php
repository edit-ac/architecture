<?php
declare(strict_types=1);

namespace EditAc\Toolchain;

// Deterministic toolchain input only; this is not an editor document or SDK store.
final class BinaryFixture
{
    /** @return array<string, string> */
    public static function cases(): array
    {
        return [
            'binary' => "\x00\xff\x80\x01\r\n\x00",
            'unicode' => 'Árvíztűrő tükörfúrógép 📝',
            'empty' => '',
        ];
    }
}
