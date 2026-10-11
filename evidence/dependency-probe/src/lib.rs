//! Compile-only probe for the proposed edit.ac dependency pins.
//!
//! These re-exports require the public dependency types to resolve. They do not
//! implement an editor, exchange Yjs updates, generate native SDKs, or establish
//! schema, wire compatibility, performance, size, or release qualification.

pub use pulldown_cmark::Parser;
pub use wasm_bindgen::JsValue;
pub use yrs::Doc;

#[cfg(feature = "native-probe")]
pub use uniffi::RustBuffer;
