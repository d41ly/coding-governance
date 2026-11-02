**Serves:** journal TOOL-dSafePassage-67

# TOOL-dSafePassage-67 — acceptance ledger

The unit as built, at spec rev-1. `tools/govkit/fixture_target.py`: `build_scratch_gov` inits with
`--template=` and its config loop pins `commit.gpgsign false` and `core.hooksPath .git/hooks` beside
`core.autocrlf false`, the `core.autocrlf` comment moved up to the loop; `run_git` raises `OSError`
naming the argv, the directory and git's stderr on a non-zero exit; `check_inherited_config` is the
`--selftest` flag. `tools/govkit/selftest.py` gains `check_fixture_target`, called beside
`check_step_gate_fixture`.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass, and the role hook refuses
the `--selftest` flag form to a builder, so `check_inherited_config` (the function the flag calls)
was run through `python -I -c` on node d (Windows, git 2.54.0.windows.1). The red cases ran the
same function on four scratch copies of the file, each with one break, loaded by path.

**Evidences:** TOOL-dSafePassage-67
- AC1 — `python -I -c "...; import fixture_target as f; print('rc', f.check_inherited_config())"` exit 0: four `liveness:` lines first (the control's init copied the template's pre-commit; its commit refused, exit 128; the `hooks-path` canary written; with `commit.gpgsign=false`, exit 0), then `build_target holds base at HEAD (subject 'base')`, `no canary written ... ([])`, `no .git/hooks/pre-commit copied`, `run_git raised OSError on the refused signed commit: git -c commit.gpgsign=true commit --allow-empty -qm signed in .../target exited 128: error: gpg failed to sign the data`, and `fixture-target: PASS · 8 of 8 observations hold`, rc 0. Red, each rc 1: `commit.gpgsign` dropped, `build_target holds base at HEAD: it raised git commit -qm base ... exited 128`; `core.hooksPath` dropped, `no canary written ... (['hooks-path'])`; `--template=` dropped, `(['template'])` and `no .git/hooks/pre-commit copied` missed; `run_git` returning on a non-zero exit, `run_git raised OSError on the refused signed commit: it returned`. Owed at the close: the `fixture_target.py --selftest` command itself and the new arm `check_fixture_target`, red on its staged break (the loop drops `commit.gpgsign`) and green restored, plus the §7 gates over every factory caller.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (`check_fixture_target`, run whole), the break was `fixture_target.py`'s config loop dropping `commit.gpgsign`: `FAIL [dSP-67] fixture_target.py --selftest exits 0 and prints its PASS line`, where the fixture prints `fixture-target: MISS build_target holds base at HEAD: it raised git commit -qm base … error: gpg failed to sign the data`. Restored, GREEN: 1 of 1 `ok`.
