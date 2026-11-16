**Serves:** journal TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-2 TOOL-aPiecewiseGrade-3 TOOL-aPiecewiseGrade-4 TOOL-aPiecewiseGrade-5 TOOL-aPiecewiseGrade-6 TOOL-aPiecewiseGrade-7 TOOL-aPiecewiseGrade-8

# The new arms observed at the close: each red on its staged break, green restored

The main loop observed these at the close, after every unit was terminal, on `8aedf65a2`, as BUILD-METHOD
M8 owes (`doc.build-method#m8-closing-the-build`). The owner chose the scope at the close: "Fast suites
only (Recommended)". So every `New arm:` line in `tools/check-spec-tokens.test.sh` was observed, and the
lines in `tools/unattended/unattended.test.sh` are owed, listed below.

**Method.** A frozen clone of `8aedf65a2` was copied once per break. Each break replaced exactly one site
of `tools/check-spec-tokens.py`, and the instrument refused if the site was not unique. Each copy ran the
whole suite, `bash tools/check-spec-tokens.test.sh`, four copies at a time, and its FAIL lines were read
against the green run. GREEN is the unbroken copy's run at the same head: `PASS (291 assertions)` (DERIVED,
its last line), above the suite's floor of 284 (TOOL-aPiecewiseGrade-8). The instruments are `breaks.py`
and `breaks.sh` in the session scratchpad. Under four concurrent copies the green run took 720 s (PINNED
8aedf65a2), against the leg's 330 s ceiling (DERIVED from the leg manifest); the bar measures it alone.

## Observed red, then green

- Unit 3: the `lru_cache` decorator removed from `load_design_lib` reds `TOOL-aPiecewiseGrade-3 AC2` alone.
- Unit 1:
  - A per-spec key that replays no `read` line reds the PG1 steps `retired`, `carries`, `packet`, `isfile` and `cited`, with `PG1 AC4` and `PG1 AC7`.
  - The packet join's answer reused from the previous cached run reds the PG1 steps `packet`, `isfile`, `cited`, `kit`, `cutoff` and `onespec`, with `PG1 AC6`.
- Unit 4:
  - The fixed `.next` directory made again beside the cache reds `PG4 AC1` and `PG1 AC6`.
  - The mode run on `SPEC_TOKENS_CACHE` alone, its next directory made beside the cache, reds `PG4 AC3` alone.
  - The trace skipping the fixed `.next` name instead of the named directory reds `PG1 AC7` alone.
- Unit 5: `main` reading through a `collections.Counter` with one name misspelled reds that counter's arm alone, each in its own run: `skipped`, `so_bare`, `ao_graded` and `ao_bad`.
- Unit 8:
  - The cache guard's two lines deleted from `read_spec_cache` red `PG8 AC1` alone.
  - The `KeyError` guard's two lines deleted from `main` red `PG8 AC2` alone.

## Owed: not observed, by the owner's call

Every `New arm:` line in `tools/unattended/unattended.test.sh`, the driver suite that runs for hours:

- Unit 2: the name-file arm covering AC1, AC2, AC3 and AC8, with its three staged breaks.
- Unit 6: the overlap and busy arm (AC1 to AC4), the pid-record arm (AC10 to AC14) and the GH37 block on the factory's names (AC6).
- Unit 7: the `foreign` kind in the AC13 loop.

The driver suite's executed counts against its floors did not run either, `FLOOR_SHARD_3` among them, which unit 7's spec writer found unraised by unit 6.
