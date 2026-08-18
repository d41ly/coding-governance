# aBranchedMandate — three things this run measured that have no row yet

Written because `memory/backlog/TOOL.md` is 2 bytes under its 20480 cap and a row would breach it,
and because the alternative was leaving these in a transcript. Each is MEASURED, not suspected.
Whoever rotates the backlog next should lift them into rows.

## 1. `build-complete` is unsatisfiable for a build README that predates the roster markers

The DoD item's first term is `region <README> <!-- roster:units --> <!-- /roster:units -->`. This
build's README carried its authored Units table as a plain `##` heading, so `--close` blocked with
`build-complete` unmet and no indication that a marker pair was what it wanted. Every build folder in
this tree that predates the item is in the same state.

Adding the pair mid-run was safe here ONLY because the roster comparison in `check_authorization` is
gated on the marker's PRESENCE AT BASE — verified: `git show 401416f:…/README.md | grep -c roster:units`
returns 0, so the across-BASE comparison is skipped rather than firing on a mismatch. A build whose
BASE *does* carry the markers could not be repaired this way mid-run.

**Fix shape:** either seed the markers in `MANIFEST`/README scaffolding, or have the item name the
missing region in its refusal instead of reporting a bare "unmet".

## 2. `--close` discards the merge bar's output

`unattended.sh` runs `$GATE_CMD >/dev/null 2>&1` in `dod_met`. So a blocked close reports *that*
`gates-green` failed and never *which leg*. This run paid for it three separate times, each costing a
full extra bar run (~15-30 min under load) to recover the leg name.

It is the SAME defect `TOOL-aBranchedMandate-2`'s S4 fixed one function away for `WIRING_CHECK`, and
that unit fixed the one call site its spec named without grepping for siblings. The fix is the same
shape: capture, and surface indented under the refusal.

## 3. RETRACTED — `gate-logs/` is NOT shared across worktrees

**This finding was wrong and is kept, struck, rather than deleted.** It claimed both paths resolve
through `git rev-parse --git-common-dir` and are therefore shared by every worktree of the repo.

`tools/run-gates.sh:34` uses `git rev-parse --git-dir`, which in a linked worktree resolves to
`.git/worktrees/<name>` — per-worktree, exactly as it should be. Measured here: `--git-dir` gives
`…/.git/worktrees/unattended-abranched-mandate-62b947` holding 70 leg logs of this worktree's own,
while `--git-common-dir` gives `…/.git` holding 71 that belong to the PRIMARY tree. `AGENTS.md`'s
claim that `gate-last-failure.txt` is overwritten "only by the next RED run" is correct.

**How the mistake happened, because that is the reusable part.** Both times I inspected the logs I
typed `--git-common-dir` myself and then read what I found there as the writer's output. The
ten-hour-old leg logs and the `unattended adopter e2e` failure record were the primary tree's, and
both were accurate records of ITS runs. I diagnosed the tool from a directory the tool never writes
to, and then reported the tool as defective — twice, in two separate turns, without once checking
which path the source actually composes.
