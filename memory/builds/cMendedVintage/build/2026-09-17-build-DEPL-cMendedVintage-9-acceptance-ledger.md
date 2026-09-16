# cMendedVintage — the acceptance ledger for unit 9

**Serves:** journal DEPL-cMendedVintage-9

*Node `c`, 2026-09-17, written by the pass that built the unit. Every line below was taken against
the real files in the unit's own worktree. No merge bar and no `*.test.sh` suite ran in this pass;
each criterion was answered by replaying its own command at the shell, stated per criterion below.*

## The one thing worth reading twice

**The refusal was observed RED twice, and the second observation is the one that matters.** A
fixture proves a mechanism only for the fixture's own values, so after the scratch tree refused, the
predicate as committed was run over the SHIPPED descriptors — a detached worktree at `3ca2f144^`,
the last revision that still held a live instance, with this tip's engine copied in. It exited 1
naming `entry 'gate-lint' plans a file at 'memory/project/substitution-fed-loops.txt'`, and its note
read `276 planned destination(s) graded … 1 under it`. That is the real rule, refused by the gate
that now forbids its class. At this tip the same command reads `274 … 0 under it` and exits 0.

**The population is counted on the RED runs too.** After `TOOL-cMendedVintage-2` the hit count is
zero by design, so a zero with no population beside it would be indistinguishable from a predicate
that ran over nothing. The note prints both numbers on every run, clean and dirty, and the arms
assert both.

**Evidences:** DEPL-cMendedVintage-9

- AC1 — `python tools/govkit/govkit.py selfcheck` in a scratch gov tree whose one descriptor
  declares `role = "seed"` with `to = "{memory_root}/project/demo-registry.txt"`, built under this
  run's scratchpad by the same recipe the committed arm uses. Exit 1. The finding names the entry,
  the resolved destination and the reason: `entry 'demo' plans a file at
  'memory/project/demo-registry.txt', under the reserved 'memory/project/' prefix`, followed by
  `check 3 of their `check-memory-hygiene.sh`` and `PROJECT_REGISTRY_EXTRA`. Its note read
  `3 planned destination(s) graded against the reserved `{memory_root}/project/` prefix, 1 under
  it`. The break was staged in the scratch tree and never in the worktree.
- AC2 — `python tools/govkit/govkit.py selfcheck` over the same fixture with
  `to = "memory/project/demo-registry.txt"`, a bare literal in place of `{memory_root}`. Exit 1,
  byte-identical finding, identical note. This is the criterion that decides the implementation: the
  predicate grades the RESOLVED destination, so the two spellings are one fact, where a matcher over
  the descriptor's source text would catch the token form and miss this one.
- AC3 — `python tools/govkit/govkit.py selfcheck` over this tree, unmodified. Exit 0, and the
  gate-legs note reads `274 planned destination(s) graded against the reserved
  `{memory_root}/project/` prefix, 0 under it`. 274 is greater than zero, which is the whole of what
  this criterion asks. figure: DERIVED at this tip. The CONTROL for it is a third fixture whose
  destination sits one segment ABOVE the reserved prefix, `{memory_root}/demo-registry.txt`: exit 0,
  note `3 … 0 under it`, so the refusal is not a ban on `{memory_root}` or on `seed` rows.
- AC4 — `python tools/govkit/refusal_join.py`. Exit 0, printing `251 branch(es) across 4
  module(s)`. Both shrink-only pins moved in this commit: `BRANCH_PIN` 217 -> 251 and `FILE_PIN`
  1 -> 4, each carrying the measurement beside it in the source. MEASURED both sides with the
  file's own matcher: 250 branches over the four modules at base `3ca2f144`, 251 at this tip, so
  this unit's delta is exactly the one new branch. The anchor-set half of this criterion was
  WITHDRAWN at rev-2 and the reason is in the spec: the file enumerates no anchor set, and its
  membership join runs only against a reached-set passed on argv that nothing in this tree passes.
- AC5 — `git grep -n 'report-reseed' -- WIRE-INTO-PROJECT.md`. One hit, inside the new
  `## Maintenance` subsection, which names the override and its `missing`/`renamed` exemption set,
  names inCMS core and NicoCares as the two trees holding an installed copy, and gives the four
  manual steps. The runbook PRESCRIBES install paths, so the subsection was also graded by
  `bash tools/check-install-prefix.sh`: clean, 268 shipped files, no undeclared root-install
  spelling.

## What did not run, and why

The permanent arms — three plus a control in the deployer's own suite — were written and are not
what any criterion above answers. No suite ran in this pass, by the pass's own mandate; the arms
replay exactly the four fixture runs recorded under AC1, AC2 and AC3, and the bar the run owes
covers them once every unit is terminal.

`bash tools/memory-tree/check-memory-hygiene.sh` exits 1 over this tree on check 23, and it did so
before this unit wrote a line: every closed DEPL unit in this build from `-1` through `-8`, plus
`-16` and `TOOL-cMendedVintage-1`, numbers acceptance criteria that no journal record evidences.
This record discharges unit 9's own five rows. The rest are this build's to back-fill and are named
here so the red is attributed rather than inherited silently.
