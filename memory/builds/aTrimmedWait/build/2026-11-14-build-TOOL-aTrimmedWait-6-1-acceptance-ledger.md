# TOOL-aTrimmedWait-6 acceptance ledger

**Serves:** journal TOOL-aTrimmedWait-6

No merge bar, no self-test suite and no `*.test.sh` ran in this pass. Every observation below was
made on node a, one command at a time with nothing else running, over the spec at rev-2. The pass
probe is the spec's §4 block, saved as `p6.sh` in the run's scratch directory with `SCRATCH` set
inside it and one addition: a `HOOKJS` variable, defaulting to `tools/hooks/scratch-guard.js`, names
the hook module both halves of the block load, so the same block ran over the base module
(`git show 846d51d3:tools/hooks/scratch-guard.js`, saved as `base6/scratch-guard.js` in the scratch
directory) and over the built one. The corpus probe is the spec's §4 `p6c.js`, byte for byte. The
changed code is `tools/hooks/scratch-guard.js#checkPollWait`,
`tools/hooks/scratch-guard.js#scanLauncherOptions`, `tools/hooks/scratch-guard.js#scanCommandHeads`
and `tools/hooks/scratch-guard.js#checkRoleGate`. The suite arm's rows in
`tools/hooks/scratch-guard.test.sh#run_role_bash` and their RED-first observation are owed to the
main loop at the close.

**Evidences:** TOOL-aTrimmedWait-6
- AC1 — `bash "$SCRATCH/p6.sh"` over the built hook printed the `head` line `kit/a.test.sh` for
  `bash -eo pipefail`, `bash -euxo pipefail`, `bash -co pipefail` and `bash -o pipefail`, and
  `(none)` for `bash -no pipefail`. Over the base module the first three read `pipefail`, as the
  spec recorded at `a25c84fc0`.
- AC2 — `bash "$SCRATCH/p6.sh"` over the built hook: R1 to R7 each printed `exit 2`; R1 named
  `row G3 suite`, R2 and R3 `row P1` (`row P1 tail follow`), R4 `row P2` (`row P2 sleep in a loop`),
  and R5, R6 and R7 `row P3` (`row P3 sleep at or over 5 s`). Over the base module every R row printed `exit 0`. <!-- DERIVED from POLL_SLEEP_FLOOR_S -->
- AC3 — the same run printed `exit 0` with nothing after it for N1 to N6, and `exit 2` naming
  `row G2 runner` for N7, identical to the base module's N rows.
- AC4 — `node "$SCRATCH/p6c.js"` over the base and built modules and the §4 transcript directory
  printed `commands 9301 · same 9140 · poll 161 · cluster 0 · other 0` in 19.8 s. <!-- PINNED 2026-11-14 -->
  So `other 0` holds: no gate verdict moved outside the two intended classes. The `poll` count is
  161 and the `cluster` count 0. <!-- PINNED 2026-11-14 -->
- AC5 — `grep -c 'P1 tail follow' tools/hooks/scratch-guard.js tools/hooks/README.md` printed 1 for
  each file and `grep -c 'polling wait' help/roles.md` printed 1;
  `grep -n 'eo pipefail. among them' tools/hooks/scratch-guard.js` and
  `grep -n 'such as the .o. inside' tools/hooks/README.md` printed nothing.
- AC6 — the R5 payload of `"$SCRATCH/p6.sh"` (`sleep 240; cat /c/x.out` as `gov-builder`) piped
  into `node "$SCRATCH/base6/scratch-guard.js"` three times, then into
  `node tools/hooks/scratch-guard.js` three times, one at a time on node a:
  base 136, 107 and 111 ms, each exit 0; built 121, 132 and 155 ms, each exit 2. <!-- PINNED 2026-11-14 -->
  The hook's own cost stays near a tenth of a second, and the 240 s wait it refuses is the <!-- DERIVED from the AC6 payload's own duration -->
  payload's own duration. <!-- DERIVED from the AC6 payload's own duration -->
- Verdict parity — on the pass probe's fixture the base and built hook gave identical exits for N1
  to N7, so every admit and the one gate refusal stand; the R rows are the intended new refusals.
  The corpus probe's `same` and `other 0` carry the same reading over the measured session.
- Owed to the close: the new arm's 14 `run_role_bash` rows (7 for AC2, 7 for AC3) and `FLOOR_ASSERTIONS` at 375, <!-- DERIVED from 361 plus the 14 new rows -->
  observed RED on the spec's staged break and GREEN once restored, and the gate legs listed in §7.
