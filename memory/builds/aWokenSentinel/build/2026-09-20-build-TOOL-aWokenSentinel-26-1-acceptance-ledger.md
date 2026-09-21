# TOOL-aWokenSentinel-26 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-26

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite. The pass verified with the direct checks the spec's section 7 names for it: the
lander-marker block of `tools/unattended/unattended.test.sh` run ALONE over the suite's sourced
prologue, from a runner assembled under the session scratchpad (`r26/runner.sh`, the prologue's
`SCRIPT=` line pointed at a `DRIVER` variable, the fixture clone under `%TEMP%/ws26` through
`TMPDIR`), against the working tree's driver, which this unit does not touch — once as a copy of
the block at the tip of unit 22's pass with a probe segment spliced in after the pushed control's
restoration line, evaluating the three `same` lines under each staged state and the restored one
(`r26/block.probe.sh`); once as the tip's block with the guard committed in place
(`r26/block.tip.sh`); and the greps of AC1, AC3 and AC4 over the working tree, over `git show
830c46e8:…` and over `git show 077788ec:…`, the commit whose subject carries
`TOOL-aWokenSentinel-22`. Those stand in for the `unattended kit gate`, `harness arms (fail
branches armed or pinned)`, `memory hygiene`, `spec tokens` and `install-prefix` legs, which run
once at the close. One spec fold was owed and taken as rev-2: the bare `sed` to `LANDED` that §4
named for the first staged state reds two properties, and the folded state reds one. The executed
count the guard adds is three.

**Evidences:** TOOL-aWokenSentinel-26
- AC1 — `grep -c 'accepting arm enters' tools/unattended/unattended.test.sh` printed `3` at the tip, `0` over `git show 830c46e8:tools/unattended/unattended.test.sh` and `0` over `git show 077788ec:…`. `grep -n` at the tip placed the three `same` lines at 4836, 4837 and 4838, the accepting arm's `printf 'landed main at %s by push-main` at 4839 directly below them, and spec 22's pushed control `git push -q -f origin tscratch:main` at 4816 above them. OBSERVED.
- AC2 — the probe copy of the block, run alone over the sourced prologue against the working tree's driver, printed under `state=A0` (the bare `sed` to `LANDED`, §4's rev-1 spelling) two lines, `FAIL accepting arm enters at a committed LANDING record: expected [1], got [0]` and `FAIL accepting arm enters with a clean tree: expected [0], got [1]`, the reading rev-2 folds; under `state=A` (the record `sed` to `LANDED`, `fixture`, `git push -q -f origin HEAD:main`) the record line alone, `FAIL accepting arm enters at a committed LANDING record: expected [1], got [0]`; under `state=B` (`: > stray`) the clean-tree line alone, `FAIL accepting arm enters with a clean tree: expected [0], got [1]`; under `state=C` (one `--allow-empty` commit on `tscratch26` off HEAD, pushed by `git push -q -f origin tscratch26:main`) the advertised line alone, `FAIL accepting arm enters with HEAD advertised as origin main: expected [d0bf24dd…], got [80bb69f2…]`, the probe's own echo reading `scratch=d0bf24dd… head=80bb69f2… advertised=d0bf24dd…`; and under `state=R` (`sed` to `LANDING`, `rm -f stray`, `fixture`, `git push -q -f origin HEAD:main`) no `FAIL` line, the probe ending `n=49 st=1` with the block's remaining arms, the accepting arm included, adding no `FAIL` (`BLOCK n=59 block=39 st=1`, 39 being the block's 24 plus five evaluations of three). AMENDED at rev-2 for the first state's spelling, then OBSERVED.
- AC3 — `grep -c 'TOOL-aWokenSentinel-22' tools/unattended/unattended.test.sh` printed `5` at the tip; the hit at line 4831 is the guard's own comment, `(TOOL-aWokenSentinel-22) landed the record and moved origin main above this line`. OBSERVED.
- AC4 — `sed -n 's/^FLOOR_ASSERTIONS=//p' tools/unattended/unattended.test.sh | tail -1` printed `973` at the tip and `970` over `git show 077788ec:…`; `grep -n '^FLOOR_SHARD_'` printed `FLOOR_SHARD_1=208 FLOOR_SHARD_2=777` at the tip and `FLOOR_SHARD_1=208 FLOOR_SHARD_2=774` at `077788ec`, the accepting arm sitting in region two. The tip's block run alone printed `BLOCK n=47 block=27 st=0` against unit 22's recorded `block=24`, the three the floors moved by. OBSERVED; the whole-suite reading of the raised floors is observed at --close.
- checkers — `bash -n tools/unattended/unattended.test.sh` exited 0 and the file carries no CR byte (`grep -c $'\r'` printed `0`). OBSERVED; the legs are observed at --close.

## What this ledger does not evidence

No kit gate, hygiene leg, spec-token leg, lexicon leg, install-prefix leg or `*.test.sh` suite ran
inside this pass; every one is `--close`'s and each row above says so. The `harness arms` leg's
verdict on the driver's branches does not move here: the guard arms nothing and reads the suite's
own fixture state. The whole-suite reading of `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` is the
close's; this pass measured the block alone. The `tscratch26` branch the probe copy makes lives in
the probe's own fixture clone under `%TEMP%/ws26`, not in the suite, whose tip block makes no
branch of its own. No identifier was minted, so no lexicon query was owed; the three labels are
`same` arguments. The build README's authored roster row for this unit moved `PLANNED` to
`CLOSED` beside the spec header; this pass touched no sibling's row.
