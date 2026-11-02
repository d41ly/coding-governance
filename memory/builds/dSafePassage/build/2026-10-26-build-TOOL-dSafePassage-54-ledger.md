**Serves:** journal TOOL-dSafePassage-54

# TOOL-dSafePassage-54 — acceptance ledger

The unit as built, at spec rev-2. The `isolation` family gains the plant `submodule-sound-no-nested`:
a scratch repository with one commit, added into the scratch superproject by `git -c
protocol.file.allow=always submodule add`, no key set. It shares the `ref-named-config` plant's
sound arm: `read_target_repositories` must list exactly the target's `.git` and `.git/modules/sub`,
its liveness that git wrote `.git/modules/sub/HEAD` and no `.git/modules/sub/modules`, and the
status step must run unrefused; both exit 0. `help/upgrade-steps.md`, "What a step can reach",
states that a `modules/` git never created is an empty listing.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node d
(Windows, Python 3.14, git 2.54.0.windows.1, bash under Git for Windows) over this worktree, by the
fixture CLI and by a probe script in the run's scratchpad (`probe54.py`), which also ran each AC1 and
AC2 observation over a scratch copy of `tools/govkit/` with TOOL-dSafePassage-53's
`FileNotFoundError` handler deleted, TOOL-dSafePassage-51's single `except OSError`.

Owed at the close: the `New arm:` line of §7 (tools/govkit/selftest.py, covers AC1 AC2), the
`[dSP-54]` checks, observed RED on the staged copy with the single `except OSError` and GREEN over the
module; and the §7 legs `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`, `govkit
selfcheck`, `recall floor arms`, `encoding posture (text IO names its encoding)`, `lexicon naming
predicates`, `policy fixtures` and `spec tokens (a spec's own names resolve)` at the close's bar. Not
covered, as §7 states: a submodule layout another git version writes, and a git-built nested submodule.

**Evidences:** TOOL-dSafePassage-54
- AC1 — `isolation: population · .../t/.git/modules/sub · reached by sub` — `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-sound-no-nested` exited 0, printing the target's `.git` row, the `.git/modules/sub` row, `fixture/status · up · ok` and no refusal, `Traceback` or `isolation: FAILED`; over the copy it exited 1, refused naming `.git/modules/sub/modules does not list (FileNotFoundError: ...)`, with `isolation: FAILED`.
- AC2 — `read_target_repositories` — imported by path and called on this worktree's root, it returned one row, `C:/projects/coding-governance/.git/worktrees/unattended-dsafepassage-567339` with `reached_by` empty, equal to `git rev-parse --absolute-git-dir`, which holds no `modules`; over the copy it returned the refusal `.../unattended-dsafepassage-567339/modules does not list (FileNotFoundError: ...)`.
- AC3 — `passes with no refusal` — TOOL-dSafePassage-51's §4 section-probe awk line over `help/upgrade-steps.md` printed 120 lines, its 37th `a target with no submodules, or whose submodules have none nested, passes with no refusal. A submodule`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (`check_step_isolation`, the dSP-54 rows), the break was the walk's handler cut back to TOOL-dSafePassage-51's single `except OSError`: `FAIL [dSP-54] AC1 the module: fixture isolation submodule-sound-no-nested exits 0 …`, refused, and `FAIL [dSP-54] AC2 the module: read_target_repositories over gov's own tree … — …/b54/.git/modules does not list (FileNotFoundError` (2 of 4). Restored, GREEN: 4 of 4 `ok`.
