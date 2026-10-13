import type { AnchorResolution, Bias, EngineHandle, StableRange } from "@edit-ac/core";
import type { DOMRenderer } from "./render.js";
export interface ModelPoint {
    node: string;
    offset: number;
    bias: Bias;
}
export interface DOMPoint {
    node: Node;
    offset: number;
}
export interface CapturedSelection {
    range: StableRange;
    anchorBias: Bias;
    focusBias: Bias;
}
/** Independently owned async target, released explicitly or on bridge disposal. */
export interface RetainedSelection extends CapturedSelection {
    readonly active: boolean;
    dispose(): void;
}
export type CaptureResult = {
    type: "captured";
    selection: CapturedSelection;
} | {
    type: "outside" | "unsupported";
    reason: string;
};
export type RestoreResult = {
    type: "restored";
} | {
    type: "outside" | "empty";
} | {
    type: "stale";
    anchor: AnchorResolution;
    focus: AnchorResolution;
} | {
    type: "unsupported";
    reason: string;
};
/** Internal bridge. Capture synchronously before preparing a command; native
 * selectionchange also captures user navigation. Tokens belong to this bridge
 * until the next capture/clear/dispose. No absolute target survives a patch.
 */
export declare class DOMSelection {
    readonly renderer: DOMRenderer;
    private readonly engine;
    private captured;
    private readonly retained;
    private readonly subscription;
    private disposed;
    lastResult: RestoreResult;
    private readonly changed;
    constructor(renderer: DOMRenderer, engine: EngineHandle);
    get current(): CapturedSelection | undefined;
    private native;
    private inside;
    /** Map only renderer-owned text/BR positions. Noneditable atoms are excluded. */
    toModel(node: Node, offset: number, bias?: Bias): ModelPoint | undefined;
    toDOM(point: ModelPoint): DOMPoint | undefined;
    private boundary;
    capture(affinity?: {
        anchor: Bias;
        focus: Bias;
    }): CaptureResult;
    /** Capture an independently owned range before crossing an async boundary.
     * Later navigation and patch restoration cannot release or redirect it.
     */
    retain(): RetainedSelection | undefined;
    restore(): RestoreResult;
    clear(): void;
    dispose(): void;
}
