# TOOL-aFrugalTurnstile-6 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-6

No merge bar and no self-test suite ran in this pass. AC1 to AC10 ran as ONE scratch fixture: the
block between the `post-merge arms` markers in `run-gates.evidence.test.sh`, extracted into a harness
outside the kit dir that defines the suite's `ROOT`, `PFX`, `KIT`, `ok` and `nope`, with
`GATE_TURNSTILE_DIR` and `GATE_MEMPAUSE=0` set as the suite sets them, under the default `mktemp -d`
root. RED first: at base `bef97330` the script does not exist (`git show` of it exits 128), so a red
landing publishes no ref and writes no record, which is the red-when of AC1 to AC7 and AC9. The first
fixture run went 6 of 20, and its reds were real, which shows the arms can fail: global
`core.autocrlf=true` checked the scratch worktree out CRLF, so every bar went red on a `\r`, AC2 and
AC5 read RED where a green was due, and the refs those reds left made AC3, AC6, AC7 and AC9 red too.
The fixture now sets `core.autocrlf false` and clears the ref before AC6, AC7 and AC9; the second run
went 20 of 20 in 6 min 17 s of wall clock. AC11 and AC12 ran as the greps and the map check they name.
Also run on the new file, each clean: the substitution-fed-loop and location-probe scans, the
remote-literal ban and the install-prefix ban. The lexicon checker's run named nothing in
`post-merge.sh`. The close still owes the §7 legs, the evidence suite whole among them, whose
ceiling and budget row may need raising for the six to seven minutes these arms add on node a.

**Evidences:** TOOL-aFrugalTurnstile-6
- AC1 — `verdict RED` — `post-merge.sh <c2>` exited 1, `git ls-remote <bare> refs/gov/bar-red` printed c2, the record read `published pushed`, and `gate-run/<run_id>/` held the leg's `red` line after `git worktree list` named no scratch tree.
- AC2 — `kind full` — `post-merge.sh <c3>` exited 0, `git ls-remote --exit-code` exited 2, and `gate-bar-green.shared` carried exactly `sha tree bar bar_paths kind base selftests run_id by stamped` with `by post-merge` and the default bar string; `gate-full-green.shared` was present and no `gate-pm.` tree was left.
- AC3 — `published kept` — with the ref staged at c2, `post-merge.sh <c1>` exited 0 and the ref still named c2.
- AC4 — `published kept` — with the ref staged at c3, `post-merge.sh <c2>` exited 1 and the ref still named c3.
- AC5 — `GATE_FULL` — under `GOV_GATE_CMD="bash bar.sh"` and a caller's `GATE_REUSE=lineage`, the probe read `GATE_FULL=1`, a non-empty `GATE_TURNSTILE_HOLDER`, no `GATE_REUSE`, HEAD at the sha and a cwd ending in `gate-pm.<pid>`; the record's `bar` read `bash bar.sh`.
- AC6 — `post-merge: publish FAILED` — with a `pre-receive` hook rejecting `refs/gov/*`, a red exited 1, the line named the rejection, and the record read `published failed` with a non-empty `why`.
- AC7 — `post-merge: REFUSING` — a commit only on a local feature branch exited 2, no probe file was written and the remote held no ref.
- AC8 — `export GOV_GATE_CMD="bash bar.sh"` — exited 2 naming the line with no probe written; the single-quote, trailing-comment, CRLF and later-assignment forms each exited 0 with the record's `bar` reading `bash bar.sh` (the double-quote form is AC5's).
- AC9 — `GOV_REMOTE` — two remotes and a detached HEAD exited 2 naming it; `--remote <second>` published c2 on the second remote and `git ls-remote` of the first showed none.
- AC10 — `post-merge: usage:` — no argument, and a sha naming no commit, each exited 2 with the usage line and no `gate queue` line, so no bar ran.
- AC11 — `WHAT THIS DOES NOT CHECK` — the grep in the kit directory printed one line, and `^## The post-merge bar` in `README.md` printed one line.
- AC12 — `python tools/codebase-map/gen_map.py --check` — exited 0 after the regeneration, and `grep -c post-merge.sh memory/map/generated/symbols.json` printed a non-zero count.
