**Serves:** journal TOOL-dSafePassage-56

# TOOL-dSafePassage-56 — acceptance ledger

The unit as built, at spec rev-3. `tools/govkit/upgrade_steps.py` gains `test_path_linked(path)`,
`os.path.islink` or `os.path.isjunction`, both `lstat` reads. `read_target_repositories`' walk calls
it on each path it pops, before `os.scandir`, and refuses a hit naming that path; the child test is a
call of it. The `isolation` family gains `submodule-modules-link-nested` (`.git/modules/a`, a bare
repository, whose `modules` is a junction back to `.git/modules`) and `submodule-modules-link-outside`
(its `modules` a junction to the fixture's scratch `outside/`, holding a bare repository `x` whose
config sets `filter.canary.clean`); on POSIX each is a directory symlink. The TOOL-dSafePassage-51
arm's staged-break anchor now names the child test's call. No user page changes, per §5.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node d
(Windows, Python 3.14, git 2.54.0.windows.1, bash under Git for Windows) over this worktree, by the
fixture CLI and by a probe script in the run's scratchpad (`probe56.py`), which also ran both plants
over a scratch copy of `tools/govkit/` with the walk's entry test replaced by `if False:`, a walk that
tests only listed children.

Owed at the close: the `New arm:` line of §7 (tools/govkit/selftest.py, covers AC1 AC2 AC3), the
`[dSP-56]` checks, observed RED on the children-only copy and GREEN over the module; the
`[dSP-51]` AC3 AC4 checks re-observed over their moved anchor; and the §7 legs `govkit selftest`,
`govkit refusal join`, `govkit acceptance matrix`, `govkit selfcheck`, `recall floor arms`, `encoding
posture (text IO names its encoding)`, `lexicon naming predicates`, `policy fixtures` and `spec tokens
(a spec's own names resolve)` at the close's bar. Not covered, as §7 states: a reparse point that is
neither a symlink nor a junction, and a link a POSIX host makes that Windows cannot.

**Evidences:** TOOL-dSafePassage-56
- AC1 — `[True, False, False]` — `upgrade_steps.py` imported by path, `test_path_linked` over a `mklink /J` junction, a plain directory and an absent path; `os.path.islink` over the same junction read `False`.
- AC2 — `.git/modules/a/modules is a link the walk would enter` — `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-modules-link-nested` exited 1 in 3 seconds, refused naming `.../t/.git/modules/a/modules`, no `Traceback`, no `isolation: FAILED`; over the copy it exited 1 with `isolation: FAILED`, refused naming `.../t/.git/modules/a/modules/a/modules/a/...`, a deeper path.
- AC3 — `.git/modules/a/modules is a link the walk would enter` — the same family with `--plant submodule-modules-link-outside` exited 1 in 4 seconds, refused naming `.../t/.git/modules/a/modules`, no `filter.canary.clean` in the output; over the copy it exited 1 with `isolation: FAILED`, refused naming `filter.canary.clean in .../outside/x/config (submodule a/x, by name)`.
- AC4 — `test_path_linked(cur)` — an `ast` walk of `read_target_repositories` found `test_path_linked(cur)` at line 1525 and `os.scandir(cur)` at line 1529, the same argument, the test first.
