# TOOL-aWokenSentinel-16 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-16

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite, per the build README's rule three. The pass verified with the direct checks the spec's
section 7 names for it: the lander-marker block of `tools/unattended/unattended.test.sh` run ALONE
over the suite's sourced prologue and the shard-two epoch, from a runner assembled under the
session scratchpad with `HERE` pointed at the kit under test and the fixture clone under
`%TEMP%/ws16`, once against the working tree's driver and once against a frozen copy of the driver
and its lib at the status header's base `12513c25`; and the greps of AC4 over the working tree and
over `git show 12513c25:tools/unattended/unattended.sh`. `bash -n` over both edited files, and
`check-arms.py --report` read over the tip, which keys seven `fail 34` branches of the driver, the
first three armed as before, the fifth and sixth armed by this unit's arms, the fourth and seventh
unarmed until unit 22 lands. Those stand in for the `unattended kit gate` and `harness arms` legs,
which run once at the close after unit 22.

**Evidences:** TOOL-aWokenSentinel-16
- AC1 — the block alone against the working tree's driver printed `BLOCK n=15 st=0` with zero `FAIL` lines: the `--no-ff` arm's `hit "$out" "phase LANDED"` held and the record's `witness:` equalled the run branch's HEAD, a commit the fixture asserted distinct from the pushed merge. The same block against the driver at `12513c25` printed `BLOCK n=15 st=1` with four `FAIL` lines, the arm's GOT reading `the lander marker names a different commit` and its `same` reading the stale preflight witness. OBSERVED.
- AC2 — in the same two runs: at the tip the parent-commit marker printed `does not contain the witness` and `wanted <HEAD sha>` and the all-zero marker printed `a commit this clone does not hold`, each read by its own `hit`; at `12513c25` both arms failed with GOT `names a different commit`, one sentence for both. OBSERVED.
- AC3 — in the tip run the existing accepting arm printed `phase LANDED`: its three `miss` lines and its `same` over `grep -c '^phase: LANDED' memory/builds/tRun/RUN.md` held at `1`, so the fast-forward landing passes both ancestry reads reflexively. OBSERVED.
- AC4 — `grep -c` over `tools/unattended/unattended.sh` at the working tree printed `1` for `dUnstalledConvoy-38`, `1` for `aUnblockedFleet-7`, `1` for `does not prove`, `1` for `is-ancestor "\$wit"` and `1` for `is-ancestor "\$msha"`; over `git show 12513c25:tools/unattended/unattended.sh` every one printed `0`. OBSERVED.

## What this ledger does not evidence

No kit gate, hygiene leg, spec-token leg, lexicon leg, install-prefix leg or `*.test.sh` suite ran
inside this pass; every one is `--close`'s and each row above says so. The `harness arms` leg is
RED between this commit and unit 22's, by design: spec 16 S2 arms two of the four new sentences
here and hands the other two to unit 22, ordered after it, and the leg runs once after both. The
suite's `FLOOR_ASSERTIONS` rose 898 to 904 and `FLOOR_SHARD_2` 702 to 708, the six arms the block
run alone counted (n 9 to 15), which the whole suite observes at the close and this pass did not.
The `--no-ff` arm restores the fixture `origin main` to `BASE` after it lands, where the block used
to leave it at its last pushed fixture commit; the suite's resting state elsewhere is `BASE`, and
unit 2's `--liveness` AC3 fixture asserts that reading downstream, so a whole-suite run is what
tells the two apart. No identifier was minted, so no lexicon query was owed; `msha` and `_lm_line`
are locals of `verb_landed`. `TOOL-dUnstalledConvoy-38` and `TOOL-aUnblockedFleet-7` are cited from
the driver's comment and their backlog rows are untouched: -38 closes at the close with this unit
cited, -7 stays OPEN with the tolerated ordering recorded against it there. The build README's
authored roster row for this unit moved `PLANNED` to `CLOSED` beside the spec header.
