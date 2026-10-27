**Serves:** journal TOOL-dSafePassage-36

# TOOL-dSafePassage-36 — acceptance ledger

The unit as built, at spec rev-4. `tools/govkit/upgrade_steps.py`: `read_target_repositories` walks
`<git dir>/modules/` of the git directory `rev-parse --absolute-git-dir` prints for the target, and
no longer reads `--git-common-dir`; a submodule's own walk was already rooted at its own git dir.
`fixture isolation` gains `submodule-unpopulated-worktree`, its `-stub` twin and
`submodule-main-only`, each over a linked worktree `wt` of the scratch target, stepped by a new
fixture step program `update.py` (`git submodule update --init`, then `git status --porcelain`).
`tools/govkit/selftest.py` carries their needles and a walk copy rooted at the common dir.
`help/upgrade-steps.md`'s "What a step can reach" names the worktree's own git directory.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed by the
unit's own CLI (`python tools/govkit/upgrade_steps.py fixture isolation --plant ...`) over its
scratch fixture under `%TEMP%` on node d (Windows, Git Bash), and by the same CLI over a scratch copy
whose walk line was replaced by the common-dir root. They stand in for the `govkit selftest` leg's
`check_step_isolation` rows for this unit only.

Owed at the close: `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`,
`govkit selfcheck`, `recall floor arms`, `encoding posture`, `lexicon naming predicates`,
`policy fixtures`, `spec tokens`; and the new arm's RED-first observation (§7): the `-stub` twin and
the walk copy rooted at the common dir must red the `[dSP-36]` rows.

**Evidences:** TOOL-dSafePassage-36
- AC1 — `--plant submodule-unpopulated-worktree` exited 1 printing `fixture/update · refused · ... filter.canary.clean in C:/Users/daily-agent/AppData/Local/Temp/gk-iso-d1mjwa55/t/.git/worktrees/wt/modules/sub/config (submodule sub), so nothing was spawned` and `unpopulated-worktree canary: absent`, no `FAILED`; `--plant submodule-unpopulated-worktree-stub` exited 1 printing `fixture/update · up · ok` and `unpopulated-worktree canary: present · filter-clean`. Red: the common-rooted copy under the same plant printed `fixture/update · up · ok`, `canary: present · filter-clean` and `isolation: FAILED · the step was not refused naming filter.canary.clean in .../t/.git/worktrees/wt/modules/sub/config (submodule sub)`, exit 1.
- AC2 — `--plant submodule-main-only` exited 0 printing `fixture/update · up · ok` and `main-only canary: absent`. Red: the common-rooted copy refused it naming `filter.canary.clean in .../t/.git/modules/sub/config (submodule sub)` and printed `isolation: FAILED · the main worktree's submodule config refused the linked worktree's step, or its filter ran`, exit 1.
- AC3 — `git grep -n -i -e "worktree" -e "submodule" -- help/upgrade-steps.md` printed lines 53-58: the check reads the submodules of the target's own worktree, `.git/worktrees/<name>/modules/` in a linked worktree, never the main worktree's `.git/modules/`.
- No regression in the main-worktree population: `submodule-filter`, `-nested`, `-unpopulated` and their `-stub` twins and `local-filter` each exited 1 with no `isolation: FAILED`, the refusals naming `.git/modules/...` as before.
