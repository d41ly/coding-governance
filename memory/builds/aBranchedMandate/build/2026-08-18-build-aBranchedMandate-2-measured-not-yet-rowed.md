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

## 3. `gate-logs/` and `gate-last-failure.txt` are shared across every worktree of the repo

Both resolve through `git rev-parse --git-common-dir`, so concurrent bars from different worktrees of
the same repo write the same per-leg logs and the same failure file. `AGENTS.md` states that
`gate-last-failure.txt` is overwritten "only by the next RED run", which holds only on a
single-worktree machine.

Measured twice on node `a`, and it misled this run both times: leg logs timestamped ten hours earlier
were read as evidence of the current run's progress, and `gate-last-failure.txt` named
`unattended adopter e2e` — a leg this run's diff never touched — while the real failure was elsewhere.

**Fix shape:** key the log dir on the worktree (`git rev-parse --git-dir`), or stamp each run and
have readers match the stamp.
