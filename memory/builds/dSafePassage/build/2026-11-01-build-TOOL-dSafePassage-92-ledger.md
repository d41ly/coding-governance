**Serves:** journal TOOL-dSafePassage-92

# TOOL-dSafePassage-92 — acceptance ledger

The unit as built, at spec rev-2. Product write: `tools/govkit/selftest.py`, inside
`check_floor_bash`: S1's nested `test_floor_fallback`, which `[dSP-91 L2]` now calls in place of its
inline needle, with the check's comment and the function's docstring naming it; S2's seven
`[dSP-92]` checks, five of them real runs of a copy of `steps/python_floor.py` taken through
`run_step_isolated` by the nested `read_stub_tail`. The S1 and S2 text is the spec's §4 fenced text
as written. `memory/map/generated/symbols.json` does not index nested functions and did not change.
No `Refusal` site is added or removed. `tools/govkit/steps/python_floor.py` is not edited.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Every criterion was observed
on node a (Windows 11, Python 3.15) from this worktree's root, or from a scratch tree at
`%TEMP%/s92` made by `git archive HEAD tools` with the working-copy `selftest.py` laid over it and
committed (the short-path exception for fixture repositories), each break then staged and committed
in turn. AC1's `tempfile.mkdtemp()` was given the run's scratchpad as its `dir`, the run's scratch
rule. `test_floor_fallback` and `read_stub_tail` each read `OK` from `lexicon.py --suggest --as py.function`.

Owed at the close: the RED-first observation of §7's two `New arm:` lines inside the suite (the
seven `[dSP-92]` checks, and `[dSP-91 L2]` under its two stub breaks), and the §7 legs at the bar.
The red observations below were probes of AC1's command, not the suite: they do not discharge the
arms' staged-break observations at the close. The two stub breaks of the second `New arm:` line
were not staged in this pass.

**Evidences:** TOOL-dSafePassage-92
- AC1 — `python -c "import pathlib, sys, tempfile; sys.path.insert(0, 'tools/govkit'); import selftest as s; s.check_floor_bash(pathlib.Path(tempfile.mkdtemp(dir=<scratchpad>))); print(s.FAILURES)"` printed `ok   [dSP-87 AC5] ...`, `ok   [dSP-91 L2] ...`, seven `ok   [dSP-92] ...` lines and `[]`, in about 2.3 s.
- AC2 — in the scratch tree, AC1's command under each break: 91's `("bash" in tail or "python-floor.sh" in tail) and` given back to the return printed `FAIL [dSP-92]` for the UTF-16, empty, no-program and text-file shapes; `crashed = False` for the raise on `:36`, the deep raise and the no-module shape; the frame marker cut for the deep raise only; `'subprocess.py"' in tail and` cut from `spawn_failed` for the no-module shape only; `(*OSError.__subclasses__(),)` for the text-file shape only. Every other line read `ok`, and restored, all nine read `ok` and the last line `[]`.
- AC3 — `git grep -n -F "test_floor_fallback("` printed three lines inside `check_floor_bash`: the `def` `:4458`, the `[dSP-91 L2]` call `:4477`, the `[dSP-92]` call `:4517`; `git grep -n -F '"bash" in tail'` printed nothing; `git grep -n -E "by .test_floor_fallback."` printed two lines, the docstring `:4433` and the `[dSP-91 L2]` comment `:4473`; `git grep -n -F "it names bash or the floor script"` printed nothing.
