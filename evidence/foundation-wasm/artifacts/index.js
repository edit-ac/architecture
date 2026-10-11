let loading;
/**
 * Load the compiled fixture runtime explicitly. Import alone performs no I/O,
 * touches no browser globals and creates no document. One URL per module instance;
 * concurrent calls share initialization and failed initialization can be retried.
 */
export function init(assetUrl) {
    if (typeof assetUrl !== "string" || assetUrl.trim() === "") {
        return Promise.reject(new TypeError("A nonempty WASM asset URL is required"));
    }
    if (loading) {
        if (loading.assetUrl !== assetUrl) {
            return Promise.reject(new Error("The runtime is already initializing or initialized with another asset URL"));
        }
        return loading.promise;
    }
    const gluePath = "./wasm/editac_wasm.js";
    const promise = (async () => {
        const bindings = await import(gluePath);
        await bindings.default({ module_or_path: assetUrl });
        return Object.freeze({
            createFixture: () => new bindings.Fixture(),
            createdDocumentCount: () => bindings.created_document_count(),
        });
    })();
    loading = { assetUrl, promise };
    void promise.catch(() => { if (loading?.promise === promise)
        loading = undefined; });
    return promise;
}
