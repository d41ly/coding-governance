# DEPL-aBenchedProbe-3 — acceptance ledger

**Serves:** journal DEPL-aBenchedProbe-3

Built inline by the main loop on 2026-10-10, after two delegated passes died with their sessions; the
second left the edits uncommitted, and this pass read them against the spec and ran every check
itself. No merge bar and no self-test suite ran. The five slices of section 4 were run by a slice
runner kept in the run's scratch (never committed), each with a temporary root under `%TEMP%`. Three
staged breaks of `tools/govkit/govkit.py` were each restored from a byte copy, with `__pycache__`
cleared before and after. The close still owes `govkit selftest` whole and the section 7 legs.

**Evidences:** DEPL-aBenchedProbe-3
- AC1 — `main()` — after the edit, slices A, B, C, D and E of `main()` each printed `FAILURES 0`,
  including the arms S4, S5 and S6 add. The before-run is the spec author's measurement at 54ba9c0e
  recorded in section 4 (nineteen arms); this pass re-observed slice B's twelve liveness reds by
  restoring the unconditional red (break 2 below), not by re-running the BASE file.
- AC2 — `held self-test legs:` — `python tools/govkit/govkit.py selfcheck` on the real tree exited 0
  and printed `59 graded, 22 self-test-shaped`, the three exempt legs and population 61 in chunk
  selftests, with no stand-down clause.
- AC3 — `7j4: entry 'demo' gate leg 'demo'` — slice B's AC5 `--write` arm passed on exit 1 with that
  line and the pin row; with 7j4's subject test replaced by `if False:` (break 1) the arm printed FAIL;
  restored, it passed.
- AC4 — `tools/govkit/govkit.py` — with the population forced to zero in `tools/govkit/govkit.py`
  (break 1, `r.fail if 0 else r.note`), both S5 liveness arms printed FAIL; restored, both passed.
- AC5 — `the zero-population reds stand down` — slice B's clean fixture printed that clause and slice
  E's `[-6]` arm saw exit 0 and the absent-manifest note; with `_j4_live = r.fail` unconditionally
  (break 2) slice B printed twelve FAILs, the scratch-gov fixture GREEN arm among them; restored, zero.
- AC6 — `tools/gate-legs.json` — in a copy with all 61 `selftests` chunks of `tools/gate-legs.json`
  moved to `declarations`, `selfcheck` printed no 7j4 refusal, its note ended with the stand-down
  clause, and 7h2 redded each moved chunk pin (exit 1). The header above 7j4 names both stand-downs
  and 7h2 as the cover.
