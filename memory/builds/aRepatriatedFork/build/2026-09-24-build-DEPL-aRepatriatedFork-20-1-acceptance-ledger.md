# DEPL-aRepatriatedFork-20 — acceptance ledger

**Serves:** journal DEPL-aRepatriatedFork-20

This is one unit pass under the mandate, and it ended BLOCKED. It ran no merge bar, no self-test
suite, and no inCMS bar. The run and its findings are recorded in this build's convergence journal,
`2026-09-24-build-DEPL-aRepatriatedFork-20-convergence-journal.md`. This ledger answers only the
criteria the pass actually observed. The unanswered ones are listed below the block, each with the
reason it is unanswered.

**Evidences:** DEPL-aRepatriatedFork-20
- AC6 — `gen_build_index.py --check` — the red-first control. Gov's generator ran over the unmigrated tree at inCMS `bc7e95589`, in the `converge-arf20` worktree before any commit, and it refused. The first refusal was the absent `memory/project/stale-header-waiver.txt`. With only that empty registry created, the next refusal was the first README's roster: "memory/builds/aBoundGazetteer/README.md: roster value '[aBoundGazetteer]' is outside the FAMILIES set". The registry was then removed again.

## Criteria this pass did not observe

- **AC1 — deferred.** It is observed after the owner lands this at inCMS, and landing needs the
  owner's ask, which this run does not carry. Its precondition was observed on the branch. After
  step 01, a read-only `govkit update --kits memory-tree` lists the four programs and
  `check-arms.py` as `stale`, where before they were `unattributed`.
- **AC7 — deferred.** It is the landing's own done condition: a full inCMS bar after the update.
- **AC2 — not observed.** The `memory-hygiene` leg still names `check-docs-hygiene.sh` on the
  branch. The wiring is item 3 of the journal's list of what remains.
- **AC3 — not observed green.** On a scratch clone with step02 applied, `--check` came back clean
  over 971 artifacts, but only after the 150 parked statuses were stubbed as a probe. `--check-format`
  still reds 41 nested READMEs, and the journal records that as a gov finding.
- **AC4 — not observed.** The recall-selftest retirement is item 2 of what remains. The
  `recall-regression` leg is red on the branch until it lands.
- **AC5 — half done.** The journal lists every check with its disposition. None of the eight checks
  kept as an inCMS project leg has been extracted yet, so none of them has been seen failing.
