/** Disposable foundation fixture; callers must release its WASM allocation. */
export interface Fixture {
    text(): string;
    utf16_length(): number;
    update_v1(): Uint8Array;
    apply_v1(bytes: Uint8Array): void;
    free(): void;
}
export interface FixtureRuntime {
    createFixture(): Fixture;
    createdDocumentCount(): number;
}
/**
 * Load the compiled fixture runtime explicitly. Import alone performs no I/O,
 * touches no browser globals and creates no document. One URL per module instance;
 * concurrent calls share initialization and failed initialization can be retried.
 */
export declare function init(assetUrl: string): Promise<FixtureRuntime>;
