# TOOL-dWitnessedBar-42 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-42

This pass ran no merge bar, no gate leg and no suite. Every criterion below was checked on node d on
2026-11-20 by a probe script driving the changed runner over a scratch clone under `%TEMP%/p42` with a
linked worktree `p42.wt`, one red leg `fx/varied.sh` whose output varies with `FX_N`; the same probe
over the base runner (`git show HEAD:tools/run-gates/run-gates.sh` at `367eac1e4`) read red on AC1's
named tail, AC2 and AC3. The close owes every leg of section 7 and the RED-first observation of the
`New arm:` line: the evidence suite's AC1-AC3 arms, staged red by restricting the sweep to `RUNROOT`,
by dropping the grace and by dropping the `touch -c`, and unit 25's AC5 case with its tails aged.

**Evidences:** TOOL-dWitnessedBar-42
- AC1 — `GATE_RUN_KEEP` — B's red run named tail `7b91910c…`, aged eight days; three red runs in A at
  `GATE_RUN_KEEP=1` left one run dir in A, B's tail on disk, and the aged unnamed `deadbeef` removed.
  The base runner removed B's tail. Owed: the evidence arm's run and its RED-first observation, and
  unit 25's AC5 case passing with its tails aged.
- AC2 — `TAIL_GRACE_S` — the one-minute-old unnamed `cafe01` survived the same sweeps (the base runner
  removed it); `grep -c 'TAIL_GRACE_S' run-gates.sh` printed 4. Owed: the evidence arm's RED-first
  observation.
- AC3 — `tail.*` — A's newest tail aged eight days, then a red run hashing it again: its age after the
  run read 0 s, and `gate-tails/` held no `tail.*` name (the base runner left it at 691202 s). Owed: (DERIVED from the builder's probe)
  the evidence arm's RED-first observation.
