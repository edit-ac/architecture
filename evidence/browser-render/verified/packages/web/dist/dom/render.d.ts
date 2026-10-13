import type { EngineHandle } from "@edit-ac/core";
export interface DOMPosition {
    node: Node;
    start: number;
    length: number;
}
/** Internal projection adapter. It renders engine state, never imports DOM state.
 * Input/selection readiness is a separate lifecycle gate. No DOM access at import.
 */
export declare class DOMRenderer {
    readonly root: HTMLElement;
    private readonly entries;
    private readonly owners;
    private readonly subscription;
    private disposed;
    private revision;
    constructor(root: HTMLElement, engine: EngineHandle, options?: {
        readOnly?: boolean;
    });
    getBlock(id: string): HTMLElement | undefined;
    getNodeId(node: Node): string | undefined;
    /** UTF-16 text and hard-break map; empty-block placeholder has length zero. */
    positions(id: string): readonly DOMPosition[];
    setReadOnly(value: boolean): void;
    dispose(): void;
    private apply;
    private update;
    private arrange;
    private markKey;
    private safeHref;
    private createRun;
    private patchRuns;
}
