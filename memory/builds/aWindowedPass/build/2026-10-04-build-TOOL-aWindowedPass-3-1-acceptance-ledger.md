# TOOL-aWindowedPass-3 — acceptance ledger

**Serves:** journal TOOL-aWindowedPass-3

`--check-commit` grades a commit against the declarations of the run this worktree's branch drives,
from the `commit-msg` hook, while `--dispatch` can still widen them. The observations are the main
loop's, on a slice of `unattended.test.sh` holding its prologue and the new block, 30 arms at exit 0,
then two break runs staged in the driver and the driver restored byte-identical. The hook ran for
real on this build's own pass commits from c5582706 on, since `core.hooksPath` is the relative
`.githooks`.

**Evidences:** TOOL-aWindowedPass-3
- AC1 — `--check-commit` — on a branch no run names it exited 0 and printed nothing; with the binding
  staged to take any record it exited 1 with a refusal.
- AC2 — `--writes` — with a stray staged path it exited 1, naming the path and printing the
  `--dispatch` command with a `--writes` for it; with the subset test staged out it exited 0.
- AC3 — `--check-commit` — with only the run-state file and a declared generated output staged it
  exited 0; with the generated subtraction staged out it exited 1.
- AC4 — `Pass: none` — a subject naming the open pass with no trailer exited 1 asking for
  `Pass: ARCH-tRun-1` or `Pass: none`, and `Pass: none` exited 0; with the trailer requirement staged
  out the first exited 0.
- AC5 — `check-commit` — the grep over `.githooks/commit-msg` printed 2 and over
  `tools/unattended/README.md` printed 1.
