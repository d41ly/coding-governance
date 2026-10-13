**Serves:** journal TOOL-aSweptBar-3

# Fix brief — TOOL-aSweptBar-3's two arms still red when its suites ran alone

The main loop ran both suites alone, serially, from a detached worktree at `e0088cb2e` (this unit's
commit, before units 4 to 6). Seven of the evidence suite's eight reds and five of the pre-push suite's
six are green. Two stay red, so the unit is reopened for them. The spec, rev-2, stands; each fix is
the root cause of an arm its §2 already scopes (S4/S5 for AC6, S7 for 25b). Diverge only through
`diverged: true`.

## The brief

### Goal
Turn the two surviving reds green at their root, at this unit's spec.

### Items
1. **pre-push 25b**, `.githooks/pre-push.test.sh`. The push now prints a decision, but scopes:
   `scoped gate on main push (fbe909db) — full bar green 988988bf from this git dir's gate-bar-green
   is 2 first-parent landing(s) back, within 10; reuse offered to remote and history legs … — bar:
   bash tracked-bar.sh`. The candidate is `gate-bar-green`, which arm 25's own push wrote, NOT the
   runner stamp the arm plants. TOOL-aFrugalTurnstile-1 AC4 says a bar that is not this kit's runner
   adopts no reuse and forces FULL naming why; TOOL-aSparedSpawn-32/33 added the `gate-bar-green`
   lineage source. Find whether that source bypasses the non-runner check in `.githooks/pre-push`
   (a product regression: fix the hook so every candidate source passes through the check), or
   whether a non-runner `gate-bar-green` is a sanctioned candidate (then the arm's expectation is
   stale: fix the arm, citing the record that sanctions it). Decide from the records, not taste.
2. **run-gates evidence AC6**, `tools/run-gates/run-gates.evidence.test.sh` (the arm after
   `rm -f "$RU_GD/gate-full-green"` / `ru_run` / `ru_run GATE_REUSE=1`): "the opt-in run did not
   reuse pa, or it stamped a full green". Read the two runs' `GATE` lines and the ledger to see
   which half fails, and fix its root: the earning bar's key, the opt-in key, or the stamp.

### Acceptance
Each arm passes when its suite runs alone; observe each red on the parent first. The main loop
re-runs both suites alone after the commit.

### Gates
`pre-push self-test` · `run-gates evidence`

### Non-goals
No other arm moves. No pin, ceiling or registry raise.

### Limitations
No suite or bar runs in the pass; extract the arm into a fixture under the scratchpad (or a short
`%TEMP%` path for a repository) and drive the hook or runner directly.

### Reuse
The suite's own helpers (`stamp`, `ru_run`, `read_lin_stamp`) and the hook's existing non-runner
refusal text.
