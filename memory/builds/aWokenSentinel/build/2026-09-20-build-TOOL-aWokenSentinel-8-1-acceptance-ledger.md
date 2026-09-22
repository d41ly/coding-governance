# TOOL-aWokenSentinel-8 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-8

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite, per the build README's rule three. The pass verified with the direct check the spec's
section 6 names: the `landing-unstamped` block of `tools/unattended/stop-guard.test.sh` run ALONE
over the suite's sourced prologue, from a runner assembled under the session scratchpad with `HERE`
pointed at the kit under test, once against the working tree's hook and once against a frozen copy
of the hook and `run-lease.js` at this pass's base `6bb7ac75` — the spec's status-header base
`12b3701d` predates unit 3's commit of the hook, so the RED reading is against the hook as unit 3
left it. `node --check` over the hook, `bash -n` over the suite, and the greps of AC4 and AC5 over
the working tree and over `git show 6bb7ac75:tools/unattended/stop-guard.js`. Those stand in for
the `unattended kit gate`, `lexicon naming predicates`, `install-prefix`, `hook destinations`,
`memory hygiene` and `spec tokens` legs, which run once at the close.

**Evidences:** TOOL-aWokenSentinel-8
- AC1 — the block alone against the working tree's hook printed `BLOCK n=24 pass=24 fail=0`: the `FINISHED-UNSTAMPED` payload with `session_crons` set read `decision` `block`, a reason carrying `finished and unstamped`, `unattended.sh --landed fx`, `block 1/6` and `phase LANDING`, no `--plan` and no `--abort`; the sidecar's last line read `decision` `block`, `reason` `landing-unstamped`, `phase` `LANDING`, `verdict` `FINISHED-UNSTAMPED` and `session_crons` deep-equal to the payload's, parsed by python. The same block against the hook at `6bb7ac75` printed `BLOCK n=24 pass=14 fail=10`, the first `FAIL` reading `the stop is blocked: expected [block], got []` and the line's reason reading `finished-unstamped`. OBSERVED.
- AC2 — in the same two runs: at the tip, two seeded `landing-unstamped` lines against `STOP_GUARD_BLOCKS="2"` allowed with empty stdout and a line reason of `blocks-exhausted`, and one seeded line blocked with `block 2/2`; at the base both readings failed, the line reason reading `finished-unstamped` and the `block 2/2` missing. OBSERVED.
- AC3 — in the same two runs: at the tip a one-element `background_tasks` at this verdict allowed with a line reason of `background-tasks`; at the base the line reason read `finished-unstamped`. OBSERVED.
- AC4 — `grep -c 'landing-unstamped' tools/unattended/stop-guard.js` printed `5` at the working tree and `0` over `git show 6bb7ac75:tools/unattended/stop-guard.js`; the leading comment block, cut with `awk '/^#!/ {next} !/^(\/\*\*| \*)/ {exit} {print}'`, printed `2` at the tip and `0` at the base; `grep -c 'finished-unstamped'` printed `0` at the tip. `node --check` printed nothing and exited 0. OBSERVED.
- AC5 — in the same two runs the record at `LANDING` with `session: absent` printed `rc=0`, empty stdout and no sidecar at both the tip and the base. `grep -L '^session: ' memory/builds/*/RUN.md` at the working tree listed all 55 run-state records — none in this tree carries the fact, this run's included — of which four sit at `LANDING` (`aCollapsedScan`, `dRatifiedSeam`, `dRetiredFork`, `dSealedTally`) and three at `BUILDING`; that is the population the row never reaches, derived at observation. OBSERVED.

## What this ledger does not evidence

No kit gate, hygiene leg, spec-token leg, lexicon leg, install-prefix leg, hook-destinations leg
or `*.test.sh` suite ran inside this pass; every one is `--close`'s and each row above says so.
The suite's `FLOOR_ASSERTIONS` rose 80 to 104, the 24 assertions the block run alone counted,
which the whole suite observes at the close and this pass did not. The integration arm that drives
unit 7's `--landed` refusal, the stop, this block and the re-run to `LANDED` through the real
driver is unit 7's S8 and is not built here. No identifier was minted: `renderBlock` gained a
leading `reason` parameter and `checkStop` a branch, so `memory/map/generated/symbols.json` is
unmoved and no lexicon query was owed. `VERDICTS_ALLOW` is gone — with `TERMINAL` its only entry,
the map was one compare. The build README's authored roster row for this unit moved `PLANNED` to
`CLOSED` beside the spec header.
