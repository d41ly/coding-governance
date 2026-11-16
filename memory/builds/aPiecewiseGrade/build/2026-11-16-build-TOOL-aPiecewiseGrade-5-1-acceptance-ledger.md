# TOOL-aPiecewiseGrade-5 — acceptance ledger

**Serves:** journal TOOL-aPiecewiseGrade-5

No merge bar, no self-test suite and no gate ran in this pass. The criteria were observed by the
spec's pass probe, `pg5.sh` in the run's scratch, removed after the pass, run over the built checker
and the worktree's memory-tree kit, with its fixture repositories at `%TEMP%/pg5`. The base copy was
the checker blob at the pass's starting commit `74267c8aa`, `93a5d813`, the blob the spec cites. The
`cache` row also ran a `control` variant, the warm entry unedited, which printed `miss 0 same 1`, so
the three edited variants' `miss 1` is the edit's doing.

**Evidences:** TOOL-aPiecewiseGrade-5
- AC1 — `real plain 1 cold 1 warm 1` — printed as written; the warm run re-graded no spec.
- AC2 — `pg1 steps 11 plain 11 cached 11` — printed as written.
- AC3 — `mut readback rc 1 loud 1 summary 0`, `mut increment rc 1 loud 1 summary 0`,
  `mut tuple rc 1 loud 1 summary 0` and `mut extra rc 1 loud 1 summary 0` — all four printed as
  written; the `extra` traceback ends in the spec's path and `counter names ['extra'] are not SPEC_COUNTERS`.
- AC4 — `cache renamed miss 1 same 1`, `cache extra miss 1 same 1` and `cache dropped miss 1 same 1`
  — all three printed as written.
- AC5 — `nonzero skipped 1 so_bare 1 ao_graded 1 ao_bad 1` — printed as written, and each of the
  four arms' rc and substring held over its fixture.
- AC6 — `grep -cw collections tools/check-spec-tokens.py` printed 0, and
  `grep -c '^SPEC_COUNTERS = (' tools/check-spec-tokens.py` printed 1.
- AC7 — `grep -c 'read back by typed names elsewhere is' memory/gotchas/two-answers-to-one-question.md`
  printed 1.

Owed to the main loop at the close. These were written and not run:
- New arm, the four `PG5 AC5` arms in `tools/check-spec-tokens.test.sh` beside the skip, ac-order
  and bare-source arms, covering AC5: RED on misspelling each counter's name in `main`'s read-back
  and then in `scan_live_spec`'s increment, and on restoring the Counter with one name misspelled,
  which reds that counter's arm alone; GREEN once each is restored.
- `FLOOR_ASSERTIONS` raised by reading by the four `arm` calls (TOOL-aPiecewiseGrade-5); the close
  confirms the executed count.
- The legs section 7 names.
