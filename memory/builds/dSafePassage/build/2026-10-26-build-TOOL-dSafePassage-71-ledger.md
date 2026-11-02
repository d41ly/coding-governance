**Serves:** journal TOOL-dSafePassage-71

# TOOL-dSafePassage-71 — acceptance ledger

The unit as built, at spec rev-1. `tools/govkit/selftest.py` gains `build_staged_copy` (the kit
directory copied whole by `shutil.copytree` without `__pycache__`, the staged text written as the
copy's `upgrade_steps.py`), `read_handpicked_copies` (the §4 regex per line, the helper's body
located by `_ast`) and `check_staged_copies`, dispatched after `check_step_walk()` over
`tmp / "dst"` with three `[dSP-71]` checks. The `[dSP-36]`, `[dSP-42] AC5`, `[dSP-7] AC6` and
`[dSP-35] AC4` arms stage through the helper; `[dSP-35]` keeps its own `process-monitor` copy.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows) by a probe of the changed code: a `python -c` import of `selftest.py` as a module,
or a scratch script running each arm's staged copy through the fixture CLI.

Owed at the close: both `New arm:` lines' RED-first observations (the four routed arms red on their
staged breaks through the helper, `[dSP-36]` red at base; `check_staged_copies` red with the
`[dSP-36]` hand-picked copy restored in a working copy) and the §7 legs.

**Evidences:** TOOL-dSafePassage-71
- AC1 — the §6 probe, staged through `build_staged_copy`, printed `submodule-unpopulated-worktree 1 True False` and `submodule-main-only 1 True False`. Red when, observed: the same text in a copy holding only `govkit.py` printed `1 False True` for `submodule-main-only`.
- AC2 — through the helper, `fixture isolation --plant submodule-fsmonitor` exited 1 with `fsmonitor canary: present` and `isolation: FAILED` (anchor count 1); `--plant callers` exited 1 naming `upgrade_steps.py:<n>, in planted_spawn` with `<n>` the planted text's line count; `fixture lock --plant lock-live-slow-census`, with `census.py` copied to the sibling `process-monitor`, printed `lock: taken` and `lock: FAILED` (anchor count 1).
- AC3 — the §6 `python -c` printed `True True`; the copy holds 43 files outside `__pycache__`.
- AC4 — the §6 `python -c` printed `[] True` (inside count 1) and then `True`. Red when, observed: with the helper's `def` renamed in the text, `read_handpicked_copies` returned `([3468], 0)`, the helper's own write named outside and an inside count of 0.
- AC5 — `git grep -n -e "build_staged_copy(" -e "shutil.copy(HERE / " -- tools/govkit/selftest.py` printed six lines: the `def` at 3461, the call in `check_staged_copies` at 3498, and the four arm call sites at 3676, 3699, 3754 and 3956; no `shutil.copy(HERE / ` line.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: Both `New arm:` lines were observed at the close, RED on their staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (`check_staged_copies` run whole, and the `[dSP-36]` common-dir rows), the break was the `[dSP-36]` arm's hand-picked copy restored in a working copy of selftest.py (`shutil.copy` of `govkit.py` only, then a write of `upgrade_steps.py`). Results: `FAIL [dSP-71] AC4 no line of selftest.py outside build_staged_copy stages the engine in a bare local directory … — outside: [3814, 3819]; inside: 1`, `FAIL [dSP-71] AC4 a hand-picked copy appended to selftest.py is named by its line`, and `FAIL [dSP-36] a walk copy rooted at the common dir reds fixture isolation submodule-unpopulated-worktree — … ModuleNotFoundError: No module named 'fixture_target'` (2 of 3 and 2 of 2). This stands in for the line's "RED at base c9baa97c". Restored, GREEN: 3 of 3 and 2 of 2 `ok`.
