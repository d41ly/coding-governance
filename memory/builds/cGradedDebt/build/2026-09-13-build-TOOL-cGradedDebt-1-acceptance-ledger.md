**Serves:** journal TOOL-cGradedDebt-1 TOOL-cGradedDebt-2

# cGradedDebt — acceptance ledger

Every line below was observed on node `c` on 2026-09-13, against the tree that carries the round-1
review fold. Figures are derived from the run named in each line, not copied from the spec.

**Evidences:** TOOL-cGradedDebt-1

- AC1 — `tools/memory-tree/check-memory-hygiene.test.sh` — PASS, 380 assertions, exit 0. The arm
  lists a compliant tracked index-set member in the fixture's `curation-debt.txt` and the gate names
  it under the stale-entry branch. Observed twice more outside the suite: the fixture dump printed
  `memory/builds/tRunOk/README.md` under that branch while `memory/builds/tRunBig/RUN.md` stayed out
  of it, and a staged break on this repo listing `memory/guides/SESSION-KICKOFF.md` made the gate
  exit 1 naming that path alone. The arm carried a PREFIX of the fail signature at rev-1 and was
  therefore unarmed; `check-arms.py --report` now reads 31 branches and 31 armed.
- AC2 — `bash tools/memory-tree/check-memory-hygiene.sh` — exit 0 over this repo, with no stale row
  and all four registry rows reporting. The four earn, in order, checks `6 7`, `6`, `7` and `6 7`.
- AC3 — `bash tools/memory-tree/check-memory-hygiene.sh` — four `memory-hygiene: curation-debt.txt`
  lines, one per listed path. `memory/builds/cBriefedPilot/README.md` reads `earns check(s) 6 of the
  6 7` and `memory/builds/aUnmannedHelm/README.md` reads `earns check(s) 7 of the 6 7`, each naming
  fewer checks than it is waived from. The denominator is DERIVED from the three selections: at
  rev-1 it was the literal `6 7 8`, which reported a build README as two checks over-wide when a
  build README cannot be in check 8's population at all, and reported `aBoundedVerdict/README.md` as
  over-wide when its waiver is exactly as wide as its fault.
- AC4 — `bash tools/memory-tree/check-memory-hygiene.sh` — `memory-hygiene: check 8 graded 500
  backlog row(s) across 4 shard(s)`. It graded 61 before this unit. The figure is DERIVED and moved
  from 499 to 500 inside this build, because the build filed a backlog row of its own — which is
  why the criterion no longer pins it.
- AC5 — `python tools/memory-tree/check-arms.py --check` — exit 0 with this gate's `ARMS_FLOORS`
  entry at `27:27`, and `memory/project/unarmed-branches.txt` still empty. `--report` reads 31
  branches and 31 armed against a measured 30 before this unit.

**Evidences:** TOOL-cGradedDebt-2

- AC1 — `bash tools/memory-tree/check-memory-hygiene.sh` — check 8 names no row in
  `memory/backlog/TOOL.md`, and the report line for that file reads `earns check(s) 6 7 of the
  6 7 8`, so its check-8 waiver is now idle and says so. Measured unwaived before the fix: 6
  findings over 438 graded rows in that file, 0 over the other three shards.
- AC2 — `memory/project/curation-debt.txt` — the note for that row no longer claims check 8 reds on
  one named line; it records that the faults were six, names both shapes, and says they are fixed.
  The row itself is still listed, because the file remains 5.8x over `INDEX_CAP_BYTES` and its
  remedy is the open owner call `TOOL-aWeighedCompass-3`.

## What this ledger does not evidence

The round-1 review's B4 is cleared by CLOSING these two specs rather than by an observation here; the
drift signal it names is measured on the landing commit. The project-keys fixture defect found while
settling B4 has no acceptance criterion of its own: it was not in either spec's scope, it was fixed
in the same pass, and the evidence is the suite going from `FAIL project keys: the fixture is not
clean unset (rc=1) — every arm below is meaningless` to `ok   project keys: the fixture is clean with
no key set` plus thirteen sibling arms that had been grading nothing.
