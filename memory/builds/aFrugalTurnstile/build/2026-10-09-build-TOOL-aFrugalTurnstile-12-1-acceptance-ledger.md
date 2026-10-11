# TOOL-aFrugalTurnstile-12 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-12

No merge bar, no runner and no self-test suite ran for this ledger. The TOOL-aFrugalTurnstile-9
fixture script was copied to a short temp root and extended: its stub bar also writes `GATE_LEGS`,
`GATE_REUSE` and `GATE_DOCS_BASE` to a file outside the repo, and three cases export them before
`--close tRun` (in-place with a `full stale` decision, twice, and once under `LANDER_MODE=primary`).
Each case ran once per driver, extracted with `git archive` at the previous commit `d4e5927f` and
again with the edited `unattended.sh`. At the previous commit the stub saw every exported knob and
a `kind full` gate-bar-green was recorded over a `GATE_LEGS` subset, so AC1 and AC2 were RED; with
the edit the stub saw all three unset, the decline line was printed, and the primary arm was
scrubbed too. AC3 ran as a slice of the new parity arm, cut out of the suite into a scratch script:
RED against the previous driver, which names no scrub list, GREEN against the edit, and the staged
copy with `GATE_REUSE` dropped was named. The close still owes the two new arm blocks in
`tools/unattended/unattended.test.sh` inside the suite, which were not run, and every §7 leg.

**Evidences:** TOOL-aFrugalTurnstile-12
- AC1 — `GATE_LEGS` — at the edit the stub's file read `GATE_LEGS=<unset>` and the output carried `not honoured from the environment by this bar: GATE_LEGS`, in-place and primary alike; at `d4e5927f` the stub read `GATE_LEGS=one-leg.json` and a `kind full` record was written.
- AC2 — `GATE_DOCS_BASE` — with `GATE_REUSE=1` and `GATE_DOCS_BASE=deadbeef` exported, the stub read both unset at the edit and the line named `GATE_REUSE GATE_DOCS_BASE`; at `d4e5927f` it read `GATE_REUSE=1` and `GATE_DOCS_BASE=deadbeef`.
- AC3 — `BAR_SCRUBBED_KNOBS` — every hook name was found in the edited driver's scrub (2 assertions, 0 failures); the copy with `GATE_REUSE` dropped was named ` GATE_REUSE`; against `d4e5927f` both assertions failed, naming all five hook knobs.
