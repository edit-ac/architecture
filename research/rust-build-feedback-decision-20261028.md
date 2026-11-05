# Retain full development debug information

Keep the current development and test profiles. Do not adopt `debug = 1` as a
workspace default. This closes RAQ-3.3 with measured non-adoption, rather than a
build-speed or runtime-qualification claim.

The bounded comparison used the current Rust graph, including the vendored Yrs
dependency, optional source-edit capability and shared fixture crate. Both lanes
used Rust 1.97.1, the `aarch64-apple-darwin` target, default features, two jobs,
incremental compilation and separate initially empty target directories. The only
configuration difference was development/test debug information: full (`2`)
against limited (`1`). Production browser and release settings were unchanged.

The representative workflow was:

```sh
cargo check -p editac-core --lib --locked --offline --jobs 2 \
  --target aarch64-apple-darwin --timings --message-format=json
cargo test -p editac-core --test table_cells --no-run --locked --offline \
  --jobs 2 --target aarch64-apple-darwin --timings --message-format=json
```

For reproduction, use an isolated copy of current source and a distinct
`CARGO_TARGET_DIR` per lane. Set `CARGO_INCREMENTAL=1` and both
`CARGO_PROFILE_DEV_DEBUG` and `CARGO_PROFILE_TEST_DEBUG` to the lane's value.
Run the workflow once cold, once unchanged, then after the same private constant
edit to `editac-core/src/lib.rs` in both lanes. The cold integration build follows
the library check and can reuse its prerequisites; it is not an independently
cold integration build. Warm runs must report fresh artifacts. Finish by running
the same integration selector without `--no-run`.

Both builds and all three existing integration cases passed in each lane. Limited
debug information reduced observed output size and some build times in this
single comparison. Concurrent compilation elsewhere on the Mac and fixed cold-run
order prevent a general speedup claim. No repeat was needed after the debugger
comparison established a concrete reason to reject the candidate.

With the resulting integration executables, LLDB's
`image lookup -t table_cells::Fixture` found the type and its fields in the full
debug build, but returned no match in the limited debug build. Losing type
inspection is an unacceptable default tradeoff for this development workflow.
This matches [Cargo's documented debug levels](https://doc.rust-lang.org/cargo/reference/profiles.html#debug):
limited debug information omits type and variable information.

The experiment changed only task-owned copies and environment settings. No
configuration is retained, no selectors or assertions changed, and no FFI
packaging redesign or shared-cache policy was attempted. Separate targets avoided
cache lock contention and interference with another worker's cache; their combined
space cost is a reason to remove the experiment outputs after measurement.

The exact source pins, elapsed times, output sizes, command statuses, test counts,
debugger result and cleanup receipt are recorded in the workspace's RAQ-3.3
progress and ignored task evidence. Broader topology/build-feedback verification
remains RAQ-4.4; future performance decisions remain with existing architecture
fitness ownership in roadmap 30. Neither ownership grants another optimization
allocation. Hard caps and native qualification deferrals remain in force.
