**Serves:** journal TOOL-dFramedEntrypoint-1

# Acceptance ledger — TOOL-dFramedEntrypoint-1

*Node d, 2026-08-24. Every line carries the command that made the observation. The canon's failing
case was staged and observed RED against the live tree before the predicate was wired, which is this
repo's rule for a new gate and the reason AC3 exists.*

**Evidences:** TOOL-dFramedEntrypoint-1

- AC1 — `python tools/memory-tree/gen_build_index.py --check-format` — observed by writing
  `memory/project/readme-contract.txt` naming this build's own README, running the verb, and reading
  exit 1 with rows naming the file and each offending line; then deleting the registry and reading
  exit 0 again. The staged break is in this record because a gate seen only passing asserts nothing.
- AC2 — same run. `canonical slot out of order: <heading>` is emitted, exercised by the selftest arm
  `canonical slots out of order are named` over a fixture whose slots are rotated.
- AC3 — `slot_violations("...no marker pair...")` now returns
  `no generated region pair, so every slot trigger would pass vacuously`. This is the arm that FAILED
  before the unit: the function returned `[]` unconditionally when it found no pair. Armed twice, once
  with `canon=True` and once with `canon=False`, because the hole was in the shared prefix.
- AC4 — arm `prose above the first canonical heading is named`, and observed live on this build's own
  README during the staged break at lines 12 and 14 through 18.
- AC5 — `python tools/memory-tree/gen_build_index.py --check-format` exits 0 AND prints
  `NOTE the heading canon is bound on ZERO build READMEs`, so the green line cannot be read as
  coverage. The population is empty by design until unit 3 writes the registry and unit 7 seeds it.
- AC6 — `python tools/memory-tree/gen_build_index.py --selftest` reports `PASS`, and the count of
  `arm ok` lines rose from 71 to 84. Thirteen arms, counted by
  `--selftest | grep -c '^arm ok'`. The harness prints no summary total, which is why the observation
  is the line count.
- AC7 — `bash tools/run-gates/run-gates.sh` legs run individually for this pass:
  `build README slot contract` green, `build-index selftest` green, `memory hygiene` green,
  `kit/dogfood doc parity` green over 3 pairs, `check-kit-versions.sh` green, `check-arms.py` green.
  The blind-spot paragraph is in `do_check_format`'s docstring and in the module docstring, NOT in
  `tools/gate-legs.json` — that manifest's key set is closed and canary-enforced, and JSON carries no
  comments, so the criterion as first written could never have passed.
- AC8 — `python tools/memory-tree/gen_build_index.py --survey` over all 62 tracked build READMEs:
  `62 would fail the canon, 0 conform; 0 are BOUND today`. Hits and near-misses both printed, unbound
  files included, exit 0. The survey is a VERB rather than a flag because `main()` returns 2 on an
  unknown mode but ignores a trailing argument, so the `--check-format --dry-run` spelling this
  criterion first carried would have printed the ordinary clean line and passed by doing nothing.
- AC9 — `memory/guides/BUILD-METHOD.md` M2 now routes the unit classification to the build-level rules
  slot, M3 names the description slot as the goal bound a run may not amend, and M4 routes the
  runaway-ceiling promotion notice to the same slot. Edited in
  `tools/memory-tree/BUILD-METHOD.template.md` FIRST and re-rendered with
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, which is the direction the parity
  harness requires.
- AC10 — `python tools/memory-tree/corpus_ids.py --report`: 133,195 B before the method edit and
  133,243 B after, so the charge is +48 B. `READ_PATH_CEILING` moved 133,138 to 133,396. Unit 8 raised
  the same ceiling for its own charge and said in its own comment that it would not cover this one;
  both units price their own growth, which is what the round-2 audit asked for.

## Staged breaks observed, and what they proved

The canon walk was disabled in place and the selftest re-run: five arms failed by name, then the file
was restored and all 84 held again. That is the difference between an arm and a decoration, and it is
recorded because the arms were written by the same session that wrote the predicate.

## What was found rather than built

`memory/guides/BUILD-METHOD.md` measured 313 lines at this build's BASE against the 310-line cap M1
declares for itself, and no gate enforces that pair. This unit's edits took it to 312, a net reduction
of one line. The remaining two are PARKED rather than trimmed: M1's budget is a governance carrier's
own stated constraint, and M3's veto 2 does not delegate a change to one. The parked entry carries the
three options and the measurement.
