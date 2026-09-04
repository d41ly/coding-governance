# Acceptance ledger — TOOL-dSealedTally-1

**Serves:** journal TOOL-dSealedTally-1

Tier-2 · node d · 2026-09-04

## What changed

Two `set_fact` calls moved. `phase LANDED` was written at `tools/unattended/unattended.sh:2357`,
above the lander-marker gate that can refuse and above every other fact write;
`landed-anchor` was written at 2405, also above two later writes that can fail. Both now sit
immediately before `stage_or_fail`, in that order:

```
  witness · unpushed-at-landing · units-at-landing · landed-anchor · phase LANDED · stage_or_fail
```

**Anchor before phase, deliberately.** If the anchor write fails the record keeps a non-terminal
phase and stays repairable; the reverse order would reproduce the wedge the unit removes. Every
`fail 34` refusal in the marker gate — 2377, 2389, 2396 — now precedes all five writes.

## The probe, and why it is not arms in the suite

`tools/unattended/`'s self-test suites are under a standing owner instruction not to be run
(2026-08-23). The probe at
`memory/builds/dSealedTally/build/2026-09-04-build-TOOL-dSealedTally-1-1-landed-ordering-probe.sh`
is the remedy that instruction names: it EXTRACTS lines 1-362 of `unattended.test.sh` at run time,
repoints `HERE` and `SCRIPT`, and appends its own arms. There is no second copy of the fixture, so
nothing can drift.

It carries a liveness assertion on itself, because `hit` and `same` are silent on success and a
green run would otherwise be indistinguishable from one whose arms never executed. It reports
`8 of them this unit's` and reds if that count falls.

## The criteria

**Evidences:** TOOL-dSealedTally-1

- AC1 — MET, OBSERVED — `bash …-landed-ordering-probe.sh` exits 0: after a refused `--landed` the
  run-state file is byte-identical by `git hash-object`, the phase still reads `LANDING`, no
  terminal phase was written, and no `landed-anchor` was written either.
- AC2 — MET, OBSERVED BY STAGED BREAK — `PROBE_REV=HEAD bash …-landed-ordering-probe.sh` exits 1
  with exactly four arms red: byte-identity, phase-still-LANDING, no-terminal-phase (got `LANDED`),
  and anchor-written-on-the-accepting-path (got none). The marker-refusal arm PASSES in both
  directions, so the scenario is identical and only the outcome differs. That is the wedge itself,
  reproduced: `phase: LANDED` with no anchor, which reds check 15 forever while check 26 refuses
  every repair verb.
- AC3 — MET, OBSERVED — the same `…-landed-ordering-probe.sh` run asserts the accepting path still
  reaches `LANDED` and writes `landed-anchor` in the same run, so the fix is not "never write
  anything", which AC1 alone could not distinguish.
- AC4 — NOT OBSERVED — the arm exists in `…-landed-ordering-probe.sh` and SKIPS in both
  directions, announcing itself: the malformed-roster lever did not make a
  later fact write refuse, so it exercised nothing. It is printed as a SKIP rather than counted as a
  pass, because a skip that looks like a pass is indistinguishable from coverage. See the residue.
- AC5 — NOT MET AS WRITTEN — `bash tools/unattended/run-unattended-gates.sh --checks` exits 1,
  and the reason is a BUDGET verdict rather than a failing check: all four checks report `ok`,
  while `kit gate` takes 160s against a 120s ceiling declared "measured 28 s" and
  `pass-order history` takes 134s against 90s declared "measured 12 s over 85 build folders".
  Reproduced twice (160/161s, 136/134s), so it is not variance. It is not this unit: moving
  two `set_fact` calls cannot cost 130s, and `pass-order history` never reads
  `tools/unattended/unattended.sh` at all yet breaches by the same shape. Filed as
  `TOOL-dSealedTally-2`.
- AC6 — MET — `bash tools/run-gates/run-gates.sh` keeps the `unattended kit gate` leg green.
- AC7 — NOT OBSERVED — forcing `stage_or_fail` to fail was not attempted, so the one
  residual this ordering keeps is asserted by reading rather than by an arm: a staging
  failure leaves a COMPLETE terminal record that is unstaged. The reasoning stands — that
  state is repairable with `git add`, where the state this unit removes was repairable by
  nothing — but it is reasoning, not an observation. Same residue as AC4 and the same
  missing lever: a `set_fact` or a staging call that fails on demand.

## What the staged break cost, and the class it belongs to

The first attempt at AC2 pointed `PROBE_DRIVER` at an `unattended.sh` extracted into a scratch
directory. It went red, and the red was worthless: the driver resolves its kit library RELATIVE TO
ITSELF, so it refused with *the kit library is missing beside this script* and never reached a
single arm. Four arms "failed" for a reason that had nothing to do with write ordering.

That is the grading-a-copy-that-never-ran class, and the only thing that caught it was reading the
`GOT:` line instead of accepting rc=1 as proof. The probe now copies the whole kit and swaps one
file, and `PROBE_REV` makes the break re-runnable by anyone.

## Residue

AC4 is unobserved. A refusal from `witness`, `unpushed-at-landing` or `units-at-landing` — the three
writes between the marker gate and the terminal pair — is exactly what H13 said this ordering must
survive, and nothing in this build demonstrates it. The lever needed is a `set_fact` that fails on
demand; filesystem permissions do not behave consistently enough under MSYS to be that lever.
Recorded here and carried to the build residue rather than closed silently.
