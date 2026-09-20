# TOOL-aWokenSentinel-22 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-22

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite. The pass verified with the direct checks the spec's section 7 names for it: the
lander-marker block of `tools/unattended/unattended.test.sh` run ALONE over the suite's sourced
prologue, from a runner assembled under the session scratchpad (`r22/runner.sh`, the prologue's
`SCRIPT=` line pointed at a `DRIVER` variable, the fixture clone under `%TEMP%/ws22` through
`TMPDIR`), once against the working tree's driver and once against a frozen copy of the driver
and its lib read out of history at `12513c25` by `git show`; a scratch copy of that block with one
`echo` probe after the restoration line, for AC2's after-state; `check-arms.py --report` over the
tip and over a short-path `git clone --local --no-checkout` of the repository checked out at
`6bb7ac75`, the commit whose subject carries `TOOL-aWokenSentinel-16`; and the `-F` greps of AC4
over the working tree and over `git show 830c46e8:tools/unattended/unattended.test.sh`. Those stand
in for the `unattended kit gate`, `harness arms (fail branches armed or pinned)`, `memory hygiene`,
`spec tokens` and `install-prefix` legs, which run once at the close. One spec fold was owed and
taken as rev-3, AC3's vacuous grep, named by the checklist on the pass commit; the design's code
ran as written on both drivers, and the executed count it adds is nine.

**Evidences:** TOOL-aWokenSentinel-22
- AC1 — the block alone against the working tree's driver printed `BLOCK n=44 block=24 st=0` with zero `FAIL` lines: the no-sha marker's two `hit` lines held on `the lander marker carries no commit sha, so it is a touched file and not evidence; fix what the lander writes. marker holds` and `marker holds: landed main at nothing by push-main`, and the `same` over `grep -c '^phase: LANDING' memory/builds/tRun/RUN.md` held at `1`. Against the driver at `12513c25` the same block printed `BLOCK n=44 block=24 st=1`, the no-sha arm's first `hit` failing with GOT `UNATTENDED check 34 FAILED — the lander marker names a different commit`, and the `same` on `phase: LANDING` still holding, because the equality refusal writes nothing either. OBSERVED.
- AC2 — in the tip run the unpushed marker's `hit` lines held on `the lander marker names a commit the remote default branch does not reach, so the landing it records is not the one` and `marker <sha> against refs/heads/main`, the `same` on `phase: LANDING` held at `1`, the `same` on the scratch commit read `distinct`, and after `git push -q -f origin tscratch:main` the `miss` on `does not reach` and the `same` over `grep -c '^phase: LANDED'` at `1` both held. The probe copy printed `PROBE22 landing=1 porcelain=[] head=ce9f09e4… advertised=ce9f09e4…` after the three restoration lines, the two shas equal in full, and the accepting arm below then printed its own `phase LANDED` count of `1`. Against `12513c25` the two `hit` lines failed with GOT `names a different commit` (the sha tail `marker 99b2482a… against refs/heads/main` among them) and the pushed control's `same` read `expected [1], got [0]`. OBSERVED.
- AC3 — `python3 tools/memory-tree/check-arms.py --report` at the tip printed `ARMED` on all seven `check 34` rows of `tools/unattended/unattended.sh` (branches 4 and 7 at driver lines 2569 and 2581 newly so), and `grep -c $'^tools/unattended/unattended.sh\t34\t' memory/project/unarmed-branches.txt` printed `0` where the same grep keyed `\t9\t` printed `1` and keyed on the file alone printed `7`, the file being tab-keyed by file, check and branch; rev-2's `grep -c 'check 34'` also printed `0`, and prints 0 on every tree because the file never spells those words, which the bug-class checklist on the pass commit named (`fixture-passes-by-finding-nothing`) and the spec's rev-3 folds. The same report over the clone at `6bb7ac75` printed seven `check 34` rows with branches 4 (`carries no commit sha`, line 2532) and 7 (`does not reach`, line 2544) blank in the ARMED column and the other five armed. OBSERVED; the `harness arms` leg is observed at --close.
- AC4 — `grep -cF` over `tools/unattended/unattended.test.sh` printed `1` for the 123-character literal and `1` for the 115-character one at the tip, and `0` for each over `git show 830c46e8:tools/unattended/unattended.test.sh`; both literals were re-derived at the pass by calling `check-arms.py`'s `signature()` over the driver's two `fail 34` messages, which returned 123 and 115 characters equal to the spec's. OBSERVED.
- checkers — `bash -n tools/unattended/unattended.test.sh` exited 0 and the file carries no CR byte (`grep -c $'\r'` printed `0`). `FLOOR_ASSERTIONS` rose 961 to 970 and `FLOOR_SHARD_2` 765 to 774, the nine arms the block run alone counted (n 15 to 24), which the whole suite observes at the close and this pass did not. OBSERVED; the legs are observed at --close.

## What this ledger does not evidence

No kit gate, hygiene leg, spec-token leg, lexicon leg, install-prefix leg or `*.test.sh` suite ran
inside this pass; every one is `--close`'s and each row above says so. The `harness arms` leg was
RED between unit 16's commit and this one by design, and is green on the check-34 branches at this
tip by the report above; the whole-suite reading of the raised floors is the close's. The
`tscratch` branch the second arm makes stays in the fixture clone until the suite's `TMP` is
removed, and nothing downstream enumerates fixture branches. No identifier was minted, so no
lexicon query was owed; `_unpushed` is a shell local of the suite. `TOOL-aUnblockedFleet-7` and
`TOOL-dScaffoldedMirror-22` are cited from the arms' comments and their records are untouched. The
build README's authored roster row for this unit moved `PLANNED` to `CLOSED` beside the spec
header; siblings 17, 19 and 21 left theirs at `PLANNED` and this pass did not touch those rows.
