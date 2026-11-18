# TOOL-aPiecewiseGrade-2 — acceptance ledger

**Serves:** journal TOOL-aPiecewiseGrade-2

No merge bar, no self-test suite and no gate ran in this pass. The criteria were observed by the
spec's pass probe, `pg2.sh` in the run's scratch, removed after the pass, run once over the built
driver with the fixture repository at `%TEMP%/pg2`, then over the base driver from `bf9ebc91c`
held under `%TEMP%/pg2b`.

Two places where the probe is narrower than section 4 describes, neither moving a criterion:
- The base run's fixture sits at `%TEMP%/pg2`, the built run's own path, and only the base driver
  sits under `%TEMP%/pg2b`. The checker's input record holds ABSOLUTE paths, so a fixture at a
  second path moves the whole key and with it the skip line's `(key …)` prefix, which is the
  fixture's placement and not the driver.
- The `lines same` comparison normalises the one wall-clock field, the `in <n>s` the check-49
  refusal and the admit note carry; unnormalised, the refused step's reading differed by a second
  between the two runs. Every other byte compared equal.

**Evidences:** TOOL-aPiecewiseGrade-2
- AC1 — `first graded 3 live 3 gens 1 named 1` — printed as written.
- AC2 — `same skipped 1` and `onespec graded 1 gens 1 newname 1` — both printed as written.
- AC3 — `moved said 1 kept 1 gens 2` and `refused kept 1 gens 2` — both printed as written.
- AC4 — `lines same 1` — printed as written, from the base driver at `bf9ebc91c` against the built one.
- AC5 — `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` printed nothing,
  and `grep -c 're-grades the rest and runs every cross-build join whole' memory/guides/UNATTENDED-VERBS.md`
  printed 1.
- AC7 — `lint fixed 2 admitted 6 unfollowed 0` — printed as written, `scan_temp_file` imported over
  the built driver's text.
- AC8 — `planted spared 1 graded 3 gens 1 named 1` — printed as written.

Owed to the main loop at the close. These were written and not run:
- AC6 — `bash "$SCRATCH/pg2-time.sh"`, the timed base-against-built `run_spec_token_check` on node
  `a`; it runs the whole-tree checker, which only the main loop may run. Not written in this pass.
- New arm, the `TOOL-aPiecewiseGrade-2 AC1 AC2 AC3 AC8` assertions after the `TOOL-aLightenedLoop-6
  AC12` step in `tools/unattended/unattended.test.sh`: RED on naming the generation on every
  branch, which reds the moved and refused `kept` assertions; RED on dropping the shape check,
  which reds `a planted malformed spec-token name spares its target`; RED on a sweep that does not
  spare the live generation, which reds `a refusal keeps the live spec-token generation and its
  name`; GREEN once each is restored.
- The driver suite's assertion count rises by the arm's assertions, twelve `same` and one `hit`
  (DERIVED from the arm's text); the close confirms the executed count.
- The legs section 7 names.
