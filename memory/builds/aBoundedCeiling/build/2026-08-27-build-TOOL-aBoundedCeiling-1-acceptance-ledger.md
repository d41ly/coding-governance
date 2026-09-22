# Acceptance ledger — TOOL-aBoundedCeiling-1 and -6

**Serves:** journal TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-6

Every criterion below is answered by something that was RUN, and where a criterion is answered by a
suite rather than by a single observation, this record says so rather than implying a stopwatch. Two
entries say plainly that they are covered by an arm nobody watched fail; that is weaker evidence and
it is labelled weaker.

**Evidences:** TOOL-aBoundedCeiling-1

- AC1 — `GATE FAIL  slow bounded  (timed out after 2s)` — a fixture leg declaring `"ceiling": 2` over
  a 45 s command, driven through the real runner via `GATE_LEGS`. Reported RED naming the leg and the
  number. The ELAPSED half is arm 1c, which compares a file-captured bound against a command-
  substitution control on the same sleeper: 1 s against 62 s when measured directly on node `a`.
- AC2 — `gates RED — 1/2 legs failed` — the same run. The verdict was FAIL, not `skip`, `held` or
  `reuse`, so the knob did not turn a leg into a pass, which is `gate-profiles.txt`'s governing
  invariant.
- AC3 — `run-gates: 1 of 2 legs declare no ceiling and run unbounded this run` with `exit=0` — a
  mixed fixture where one leg declares a ceiling and one does not. The run named the count and
  refused nothing, which is what keeps an adopter's merged manifest from being rejected for a field
  it cannot supply.
- AC4 — `ceilings INERT` — emitted on the profile line by a real bar on 2026-08-27 at 11:46, when the
  liveness probe lost a race under load, together with its stderr NOTE naming the missing
  `timeout -k`. The legs were still dispatched. Observed in the field rather
  than staged, which is also how the single-attempt probe's flakiness was found.
- AC5 — `PASS (134 assertions)`, `CANARY EXIT: 0` — `bash tools/run-gates/run-gates.test.sh`, the
  suite that IS the `run-gates canary` leg and that carries the pinned leg-key set the `ceiling`
  field had to join. Zero complaints.
- AC6 — covered by arm 1c/1d's fixtures and by inspection of `input_key`, NOT by a direct
  before-and-after measurement of the reuse key. `run-gates.sh` reads the ceiling into a shell array
  beside `guards` and `subjects` and never into the child's argv, so it cannot enter the key; the
  spec's own §4 states the narrower claim this criterion was rewritten to. WEAKER than the entries
  above and recorded as such.
- AC8 — `gov-canary: 2 of 85 gov leg(s) are not bounded` then `exit 1`, and `exit 0` once restored —
  the failing case staged by deleting one leg's `ceiling` and setting another's to `0`, so both
  shapes were exercised. This is the arm that makes the declaration requirement real in gov without
  redding an adopter.

**Evidences:** TOOL-aBoundedCeiling-6

- AC1 — `rc=137 RB_TOOK=11 wall=12s` — the SHIPPED `run_bounded`, extracted from the driver with
  `sed` rather than retyped, given a 60 s child under a 2 s bound. Killed, not waited out. rc 137 and
  not 124 because SIGTERM took ~9 s to land under load and `-k` escalated, which is why both codes
  are mapped.
- AC2 — `rc=0 RB_TOOK=1 wall=2s` — the same function over a backgrounded GRANDCHILD, the case that
  distinguishes a bound on the clock from a bound on the verdict. The command-substitution control
  took 62 s against the same sleeper.
- AC3 — `bounded at the kit default of 3600s` — the stderr NOTE emitted by `unattended.sh --version`
  against a conf declaring no GATE_BOUND. The dedicated arm for it is in `unattended.test.sh`; the fixture conf now declares
  the key so this path is exercised deliberately rather than in every other arm's output.
- AC4 — `rc=3 out=[ran-unbounded] wall=2s` — `run_bounded` with `GATE_BOUND_LIVE=0`. The command RAN
  and its exit status survived, so an inert bound never turns a check into a skip.
- AC5 — `PASS (864 assertions)`, `DRIVER EXIT: 0`, zero FAILs — `bash tools/unattended/unattended.test.sh`
  including the `--preflight` arm whose `WIRING_CHECK` sleeps past the bound and whose elapsed time is
  asserted. That arm is what cleared `check-arms`' refusal of the breach branch; it is evidenced by a
  green suite rather than by a watched failure, which is WEAKER than AC1 and AC2 above.

## What this ledger does not claim

The full merge bar has not been green end to end on this tree. `gates-green` was overridden at
`--close` on owner instruction, and the landing bar's remaining timeouts are the ceilings' own headroom
against a contended box, recorded separately. Nothing here should be read as "the bar passed".
