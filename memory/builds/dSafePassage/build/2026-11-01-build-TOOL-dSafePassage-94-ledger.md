**Serves:** journal TOOL-dSafePassage-94

# TOOL-dSafePassage-94 — acceptance ledger

The unit as built, at spec rev-1. Product write: `tools/govkit/selftest.py`, added lines only, inside
`check_floor_bash`. S1's `read_fallback_argv` and S2's `steps94` sit before the `[dSP-91 L2]` comment,
the two reads inside that block's `with`, and the two checks after `[dSP-91 L2]`. S3's cache removal
and pinned mtime are in `read_stub_tail`, and S4's probe follows the `[dSP-92]` loop, each as the
spec's §4 fenced text writes it. `tools/govkit/upgrade_steps.py` and
`tools/govkit/steps/python_floor.py` are not edited.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Every criterion was observed
on node a (Windows 11) from this worktree's root. AC1 is the spec's command, with the `tmp` directory
in the run's scratchpad rather than `tempfile.mkdtemp`. AC2's breaks were staged in a scratch tree
under `%TEMP%`, the short-path exception for fixture repositories: `git archive HEAD tools` with
this pass's `selftest.py` copied over it, committed, and each break committed in turn by a probe
script `ac2.py` in the run's scratchpad, which ran AC1's command there and printed the FAIL lines.

Owed at the close: the RED-first observation of §7's three `New arm:` lines inside the suite, and
the §7 legs at the bar. AC2's rows below are probes of `check_floor_bash` alone, not of the suite.

**Evidences:** TOOL-dSafePassage-94
- AC1 — printed `ok   [dSP-87 AC5]`, `ok   [dSP-91 L2]`, two `ok   [dSP-94]` lines, seven `ok   [dSP-92]` lines, one `ok   [dSP-94]` line, then `[]`.
- AC2 — each break printed 11 `ok` lines and one FAIL. `check_runs` narrowed to `except ValueError:`: the first `[dSP-94]` failed with `OSError(22, "This version of %1 is not compatible ...")`, `[dSP-91 L2]` `ok`. `steps._BASH = None` cut: the first failed with `['C:\\Program Files\\Git\\usr\\bin\\bash.exe', 'x']`. S2's replacement given back `except OSError:`: the second failed with `['bash', 'x']`. The `shutil.rmtree` line cut: the third failed in 3 of 3 runs.
- AC3 — `git diff --numstat c86d51fa5 -- tools` printed one line, `38	0	tools/govkit/selftest.py`; the `git grep` for the `rmtree` line printed one line, `:4521`, inside `read_stub_tail` (`def` at `:4519`).

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in a scratch clone of `390033278` (batch g, `2026-11-01-prompt-TOOL-dSafePassage-91-1-researcher.md`), each break staged alone and restored. tools/govkit/selftest.py `check_floor_bash`. First `[dSP-94]`: check_runs narrowed to ValueError at upgrade_steps.py:399: `FAIL [dSP-94] resolve_shell_argv on that PATH, GOV_BASH unset and no bash cached, hands back bare bash — OSError(22, …)` (the second `[dSP-94]` and the return-path `[dSP-95]` also FAIL; `[dSP-91 L2]` reads ok); `steps._BASH = None` cut: `FAIL [dSP-94] … — ['C:\\Program Files\\Git\\usr\\bin\\bash.exe', 'x']`. Second `[dSP-94]`: the copy's replacement given back `except OSError:`: `FAIL [dSP-94] the same read, check_runs narrowed to catch ValueError, reads the spawn's OSError — anchor count 1; ['bash', 'x']`. Third `[dSP-94]`: the shutil.rmtree line cut from read_stub_tail, 6 runs, RED 6 of 6: `FAIL [dSP-94] a stand-in the size of the one before it runs its own source, not that one's bytecode — pyc True; mtime_ns 0`. GREEN restored after each: `FAILURES []`.
