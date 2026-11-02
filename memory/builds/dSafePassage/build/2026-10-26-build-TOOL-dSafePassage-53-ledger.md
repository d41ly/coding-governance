**Serves:** journal TOOL-dSafePassage-53

# TOOL-dSafePassage-53 — acceptance ledger

The unit as built, at spec rev-2. `read_target_repositories`'s `modules/` walk lists each directory
with `os.scandir` inside one `try` whose handlers are `except FileNotFoundError: continue`, then
`except OSError as e`, a refusal naming the path and `type(e).__name__`. The walk is the worklist
TOOL-dSafePassage-51 built, so §4's `return` from one `walk(d)` is that loop's `continue`
(`2026-10-28-build-TOOL-dSafePassage-53-deviation-1.md`). The `isolation` family gains the plant
`submodule-modules-not-a-directory`: `.git/modules/a` a bare repository from `git init --bare`, its
`modules` a regular file.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node d
(Windows, Python 3.14, bash under Git for Windows) over this worktree, by a probe script in the run's
scratchpad (`probe53.py`: AC1's `ast` read and AC3's import by path) and by the fixture CLI. Each probe
was also run over a scratch copy of `tools/govkit/` with the `FileNotFoundError` handler deleted.

Owed at the close: the `New arm:` line of §7 (tools/govkit/selftest.py, covers AC2 AC3), the
`[dSP-53]` checks, observed RED on its two staged copies (TOOL-dSafePassage-51's single `except
OSError`, and a handler passing every `OSError`) and GREEN over the module; and the §7 legs
`govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`, `govkit selfcheck`, `recall
floor arms`, `encoding posture (text IO names its encoding)`, `lexicon naming predicates`, `policy
fixtures` and `spec tokens (a spec's own names resolve)` at the close's bar. Not covered, as §7 states:
a `PermissionError` listing.

**Evidences:** TOOL-dSafePassage-53
- AC1 — `[('FileNotFoundError', ['Continue']), ('OSError', ['Raise'])]` — the `ast` probe over `tools/govkit/upgrade_steps.py` found one innermost `try` calling `os.scandir` in `read_target_repositories`, its handlers in that order, the second's body raising `Refusal`; over the copy without the first handler it printed `[('OSError', ['Raise'])]` and `AC1 RED`.
- AC2 — `does not list (NotADirectoryError` — `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-modules-not-a-directory` exited 1, refused naming `.git/modules/a/modules does not list (NotADirectoryError: [WinError 267] ...)`, with no `Traceback` and no `isolation: FAILED`; a copy whose `OSError` handler continues printed `fixture/status · up · ok` and `isolation: FAILED`.
- AC3 — `read_target_repositories` — imported by path and called over a `git init` repository under the scratchpad with no `.git/modules`, it returned one row, that repository's `.git` with `reached_by` empty; over the copy with the single `except OSError` it returned the refusal `.git/modules does not list (FileNotFoundError: ...)`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (`check_step_isolation`, the dSP-53 rows), the break was a walk returning on every `OSError`: `FAIL [dSP-53] AC2 fixture isolation submodule-modules-not-a-directory exits 1, refused naming /.git/modules/a/modules does not list (NotADirectoryError`, where the fixture prints `isolation: fixture/status · up · ok` (3 of 4). Restored, GREEN: 4 of 4 `ok`.
