# TOOL-aPiecewiseGrade-8 — acceptance ledger

**Serves:** journal TOOL-aPiecewiseGrade-8

No merge bar, no self-test suite and no gate ran in this pass. AC1 and AC2 were observed by the
spec's pass probe, `pg8.sh` in the run's scratch, removed after the pass, run against the shipped
`tools/check-spec-tokens.py` at base `4b2379010` over a one-spec fixture repo with the checker copied
into its tool root, beside two mutants cut from that copy by `sed`. AC3 was observed by running the
commands it spells over the built suite. `bash -n` over the suite parsed it clean.

**Evidences:** TOOL-aPiecewiseGrade-8
- AC1 — `drop guard miss 1 same 1` and `drop noguard miss 0 same 0` — printed as written: with S4's
  two lines in `read_spec_cache` deleted, the cached run raised the `KeyError` naming `ao_bad`, wrote
  no `graded.list` and exited 1.
- AC2 — `fresh guard rc 1 loud 1 summary 0` and `fresh noguard rc 0 loud 0 summary 1` — printed as
  written, the second with S3's two lines in `main` deleted.
- AC3 — `grep -c 'PG8 AC[12] ' tools/check-spec-tokens.test.sh` printed 2, and
  `grep -c '^FLOOR_ASSERTIONS=284$' tools/check-spec-tokens.test.sh` printed 1.

Owed to the main loop at the close. These were written and not run:
- New arm `PG8 AC1` in `tools/check-spec-tokens.test.sh`, after the PG4 block: RED on deleting S4's
  two lines (`if got[2].keys() != set(SPEC_COUNTERS):` and its `return None`) from `read_spec_cache`
  in `tools/check-spec-tokens.py`; GREEN once restored.
- New arm `PG8 AC2` beside it: RED on deleting S3's two lines (`if got[2].keys() != totals.keys():`
  and its `raise KeyError`) from `main`; GREEN once restored.
- The suite's executed assertion count reaching the floor 284 (PINNED, TOOL-aPiecewiseGrade-8 S3).
- The legs section 6 names.
