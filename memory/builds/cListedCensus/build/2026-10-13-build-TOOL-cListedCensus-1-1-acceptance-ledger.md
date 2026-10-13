# TOOL-cListedCensus-1 — acceptance ledger

**Serves:** journal TOOL-cListedCensus-1

Observed on node c (git 2.55.0.windows.1, Python 3.14) against the scanner at the rev-2 fold
`a2e2e31ec`. Every staged break was a scratch copy of the scanner under the session scratchpad,
run whole with `--selftest`; the tracked file was never edited to stage one. nc's tree was read only.
No leg runs this scanner, so the bar observes none of these criteria.

**Evidences:** TOOL-cListedCensus-1
- AC1 — `python tools/gate-lint/ps-hygiene.py --selftest` — exit 0 and the pass line, with the five population arms run. Ten staged breaks each exited 1 on the arm that guards them: the walk and the BASE recount red the empty and untracked arms; no zero refusal and the count above the on-disk skip red the empty arm; no returncode check and a dead listing reported as empty red the not-a-repo arm; a `.claude` prune reds the control; the `-- '*.ps1'` pathspec, a case-sensitive suffix and no `-z` red the sub/ü.PS1 arm.
- AC2 — `.claude/worktrees/` — in nc's primary tree the BASE scanner exited 1 on 6 findings across 19 files, every one under `.claude/worktrees/`, and the new one exited 0 on `OK — 1 tracked .ps1 file(s)`, also with `GIT_DIR` exported; re-observed after the rev-2 fold.
- AC3 — `python tools/gate-lint/ps-hygiene.py .` — in gov it exited 2 and its stderr said the run graded NOTHING; the BASE scanner printed `OK — 0 .ps1 file(s) clean` and exited 0 on the same tree.
- AC4 — `a-gate-that-walks-the-repo-root-reads-other-worktrees` — `gotchas.py --for-paths tools/gate-lint/ps-hygiene.py` listed it as a path-anchored class, and `gotchas.py --check` exited 0.
- AC5 — `git grep -nE 'ps-hygiene|gate-lint/|\.ps1'` — over the four docs every population claim says tracked and every empty-population verdict says exit 2; the only `0 .ps1 file(s) clean` hit is the dossier's past-tense account of the August 2026 landing, and no hit promises `0 files clean`.
