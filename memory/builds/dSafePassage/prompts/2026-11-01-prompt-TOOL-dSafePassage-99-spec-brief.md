**Serves:** research TOOL-dSafePassage-99

# Brief: one engine for every govkit_module() caller, after a staged copy loads in process

## The prompt

> The close's arm observation at 390033278 (researcher a41ba284319099c09, batch f) found, and the main loop reproduced in a clone at 390033278, that `check_upgrade_steps` in `tools/govkit/selftest.py` crashes before its later arms: `python -c "...; s.check_upgrade_steps(tmp)"` exits 1 with `upgrade_steps.Refusal: the resolved destination '..\\E.txt' leaves the target repository` raised from `<tmp>/dsp87-quote-widened/govkit/govkit.py` line 1245, through `read_refusal` (selftest.py:3097) at the `[dSP-72]` `leaked72` comprehension (selftest.py:3199). The `govkit selftest` leg of `tools/gate-legs.json` runs that suite, guarded on `{prefix}/govkit/`, so the bar reds on it. Adopted under UNATTENDED-PROTOCOL §11: a measured red, nothing this repo measures gets worse.

## The brief

### Goal
Author the spec of TOOL-dSafePassage-99, closing the mechanism: TOOL-dSafePassage-87 AC6 loads a staged `upgrade_steps.py` in process (selftest.py:3179-3182, `us87`); its `read_steps` reaches that copy's own `load_govkit()` (upgrade_steps.py:2675), whose identity test compares `sys.modules["govkit"].__file__` with the COPY's `HERE / "govkit.py"`, misses, and overwrites `sys.modules["govkit"]` with the copy's engine (upgrade_steps.py:2690). `govkit_module()` (selftest.py:150) answers with `import govkit`, which returns that cached copy, so every later caller (here `gk72`, selftest.py:3198) gets an engine whose `Refusal` is not the class `read_refusal` catches. Other in-process staged loads (selftest.py:4208, 4235, 4296, 4496) are the same class. Fix it once, in the shared function every caller routes through: `govkit_module()` returns the engine at `GOVKIT` (the real `HERE / "govkit.py"`), re-binding `sys.modules["govkit"]` to it when the cached module is not that file. Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 17`, node `a`, `**Derived:** TOOL-dSafePassage-87` with this brief's finding in §9, §6 criteria each with a Red-when, §7 gates with a `New arm:` line, §10 reuse, §8 `none`. Add its row to the README `roster:units` table. Verify every cited line at the current HEAD before citing it.

### Items
- **Id 1 (high):** a whole `check_upgrade_steps` run crashes at `[dSP-72]` after 87 AC6's staged load, so the `govkit selftest` bar leg reds at HEAD. AC: the function runs to completion with `FAILURES` empty in a fresh process at the build commit. Red-when: `govkit_module()` given back its `import govkit` body.
- **Id 2 (regression arm):** a check in `tools/govkit/selftest.py` that loads a staged copy in process, drives it through a path reaching its `load_govkit()`, then asserts `govkit_module().__file__` resolves to `GOVKIT`. It is the `New arm:` line, red under the same break.

### Non-goals
No change to `upgrade_steps.load_govkit` (the copy's own engine is correct for the copy); no edit to a CLOSED spec; no product code; no commit, no stage into the real index, no RUN.md row.

### Acceptance
Both items are carried in 99's text. The spec is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in §6 is tracked by git; no backticked §6 token is a bare suite path (write `tools/govkit/selftest.py` only inside prose, never as a backticked command) or a code fragment that embeds a repository path; and no AC's diff or grep is already non-empty at the spec's own commit because a generated records block moved.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
