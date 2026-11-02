**Serves:** research TOOL-dSafePassage-100

# Brief: measure37 calls the resolved launcher, or skips naming what is not covered

## The prompt

> The close's observation of TOOL-dSafePassage-87 AC11 ran the resolver suite in a clean clone at 390033278 twice. Restored, it still exits 1 on one line: `FAIL a python launcher is invoked without being resolved:` naming `tools/push-main.test.sh:1409:  "${_py_arms:-python3}" -c '`. That line came in with TOOL-dSafePassage-82 (5fe2dab8e). The resolver suite is the bar leg at `tools/gate-legs.json:323`, so the bar reds on it. Adopted under UNATTENDED-PROTOCOL §11: a measured red, nothing this repo measures gets worse.

## The brief

### Goal
Author the spec of TOOL-dSafePassage-100: `measure37` (tools/push-main.test.sh:1408) invokes `"$_py_arms"` with no parameter default, and its call site (the `if [ -n "$_mt_rc" ]` block at :1423) also requires `[ -n "$_py_arms" ]`, printing a `skip — 37 ... NOT covered` line when no launcher resolved, in the spelling of its sibling guard at :1452. Today an empty `_py_arms` falls back to an unresolved `python3`, which the parameter-default ban in tools/lib/resolve-python.test.sh (`bare_scan`, the `:-python3}` shape) refuses. Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 17`, node `a`, `**Derived:** TOOL-dSafePassage-82` with this brief's finding in §9, §6 criteria each with a Red-when, §7 gates (the existing ban is the gate that reds; say whether a `New arm:` line is owed and why), §10 reuse, §8 `none`. Add its row to the README `roster:units` table. Verify every cited line at the current HEAD before citing it. TOOL-dSafePassage-99 is being specced concurrently at order 17 with a disjoint write set (tools/govkit/selftest.py); do not touch its files.

### Items
- **Id 1 (high):** the resolver suite's launcher ban names `tools/push-main.test.sh:1409` at HEAD, so its bar leg reds. AC: a `git grep` for the `:-python3}` spelling in that file prints nothing, and the call site's guard names `_py_arms`. Red-when: the default given back.

### Non-goals
No change to the ban or to the resolver block; no other launcher site; no edit to a CLOSED spec; no product code; no commit, no stage into the real index, no RUN.md row.

### Acceptance
The item is carried in 100's text. The spec is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in §6 is tracked by git; no backticked §6 token is a bare suite path (write test-suite paths only inside prose, never as a backticked command) or a code fragment that embeds a repository path; and no AC's diff or grep is already non-empty at the spec's own commit because a generated records block moved.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
