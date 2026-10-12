export class EngineError extends Error {
    code;
    operation;
    constructor(code, operation, message) {
        super(message);
        this.code = code;
        this.operation = operation;
        this.name = "EngineError";
    }
}
function invoke(operation, action) {
    try {
        return action();
    }
    catch (error) {
        if (error instanceof EngineError)
            throw error;
        if (typeof error === "string") {
            try {
                const e = JSON.parse(error);
                if (e && typeof e === "object" && "code" in e && "operation" in e && "message" in e && typeof e.code === "string" && typeof e.operation === "string" && typeof e.message === "string") {
                    throw new EngineError(e.code, e.operation, e.message);
                }
            }
            catch (parsed) {
                if (parsed instanceof EngineError)
                    throw parsed;
            }
        }
        throw new EngineError("InvalidInput", operation, error instanceof Error ? error.message : String(error));
    }
}
/** Avoid JSON.stringify's coercion of NaN, bigint, undefined, custom toJSON and sparse arrays. */
function encode(value, operation) {
    let count = 0;
    const seen = new Set();
    const visit = (v, depth) => {
        if (++count > 100_000 || depth > 32)
            throw new EngineError("ResourceLimit", operation, "request exceeds structure limit");
        if (v === null || typeof v === "string" || typeof v === "boolean")
            return;
        if (typeof v === "number" && Number.isSafeInteger(v))
            return;
        if (typeof v !== "object" || seen.has(v))
            throw new EngineError("InvalidInput", operation, "request must contain plain JSON values");
        const proto = Object.getPrototypeOf(v);
        if ((Array.isArray(v) && proto !== Array.prototype) || (!Array.isArray(v) && proto !== Object.prototype && proto !== null))
            throw new EngineError("InvalidInput", operation, "request must contain plain objects");
        seen.add(v);
        if (Array.isArray(v)) {
            if (v.length > 100_000 || Object.keys(v).length !== v.length)
                throw new EngineError("InvalidInput", operation, "sparse or decorated array");
            for (let i = 0; i < v.length; i++) {
                const d = Object.getOwnPropertyDescriptor(v, String(i));
                if (!d || !("value" in d))
                    throw new EngineError("InvalidInput", operation, "accessor input");
                visit(d.value, depth + 1);
            }
        }
        else {
            for (const key of Reflect.ownKeys(v)) {
                const d = Object.getOwnPropertyDescriptor(v, key);
                if (typeof key !== "string" || !("value" in d) || !d.enumerable)
                    throw new EngineError("InvalidInput", operation, "accessor or hidden input");
                visit(d.value, depth + 1);
            }
        }
        seen.delete(v);
    };
    visit(value, 0);
    return JSON.stringify(value);
}
function token(value, operation) {
    if (typeof value !== "string" || value.length > 128)
        throw new EngineError("InvalidInput", operation, "invalid opaque token");
    return value;
}
export function createHandle(construct, options) {
    let raw = invoke("create", () => construct(encode(options, "create")));
    const use = (operation, action) => invoke(operation, () => {
        if (!raw)
            throw new EngineError("Disposed", operation, "engine has been disposed");
        return action(raw);
    });
    const prepare = (request) => use("prepare", e => JSON.parse(e.prepare(encode(request, "prepare"))).token);
    const releasePlan = (plan) => use("releasePlan", e => e.release_plan(token(plan, "releasePlan")));
    return Object.freeze({
        read: () => use("read", e => JSON.parse(e.read())),
        anchor: (node, offset, bias) => use("anchor", e => JSON.parse(e.anchor(encode({ node, offset, bias }, "anchor"))).token),
        resolve: (anchor) => use("resolve", e => JSON.parse(e.resolve(token(anchor, "resolve")))),
        releaseAnchor: (anchor) => use("releaseAnchor", e => e.release_anchor(token(anchor, "releaseAnchor"))),
        prepare,
        can: (request) => {
            try {
                const p = prepare(request);
                releasePlan(p);
                return true;
            }
            catch (e) {
                if (e instanceof EngineError && ["EngineRejected", "InvalidInput", "InvalidHandle", "ResourceLimit"].includes(e.code))
                    return false;
                throw e;
            }
        },
        commit: (plan) => use("commit", e => JSON.parse(e.commit(token(plan, "commit")))),
        releasePlan,
        history: (request) => use("history", e => JSON.parse(e.history(encode(request, "history")))),
        dispose: () => { if (raw) {
            const allocation = raw;
            raw = undefined;
            try {
                allocation.dispose();
            }
            finally {
                allocation.free();
            }
        } },
    });
}
