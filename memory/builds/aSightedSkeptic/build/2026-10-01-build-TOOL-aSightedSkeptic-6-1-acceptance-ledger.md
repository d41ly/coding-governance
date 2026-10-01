# TOOL-aSightedSkeptic-6 — acceptance ledger

**Serves:** journal TOOL-aSightedSkeptic-6

One `SEVERITY_RUBRIC` now reaches every finder, skeptic and synthesis prompt. A skeptic's grade
binds the synthesis line, an ungraded confirmation falls back to the finder's grade and is counted,
and `uncertain` is a verdict that counts as unverified. The arm readings come from the main loop's
one VERIFYING run of the tier2-review self-test at 149e89d6 (165 passed, 0 failed) and from the same
test file run against the BASE render at 9fdd0c18 in a frozen clone (56 passed, 109 failed). The
greps and the direct checks were re-run on the build's tip, whose `tools/` is byte-identical to
149e89d6.

**Evidences:** TOOL-aSightedSkeptic-6
- AC1 — `severity: one rubric reaches every finder, skeptic and synthesis prompt` — `ok` at
  VERIFYING, `FAIL` against the BASE render.
- AC2 — `severity: the verdict schema carries uncertain and an optional severity` — `ok` at
  VERIFYING, `FAIL` against the BASE render.
- AC3 — `severity: the skeptic's grade binds the synthesis line` — `ok` at VERIFYING, `FAIL` against
  the BASE render.
- AC4 — `severity: a confirmed verdict with no grade falls back to the finder's, counted and announced`
  — `ok` at VERIFYING, `FAIL` against the BASE render.
- AC5 — `severity: an uncertain verdict is counted unverified, never refuted or confirmed` — `ok` at
  VERIFYING, `FAIL` against the BASE render.
- AC6 — `severity: a synthesis placing an id off its binding grade is returned in regraded` — `ok`
  at VERIFYING, `FAIL` against the BASE render.
- AC7 — `SEVERITY_RUBRIC` — `grep -c` printed 4 over the template and 4 over the render, and 0 over
  `git show 9fdd0c18:` of the template. `check-workflow-syntax.js` over the render exited 0 with "1
  workflow script(s) parsed clean", and `check-verifier-fanout.sh` and `check-review-join.sh` each
  exited 0. The arm `severity: the uncertain rule follows the finder's grade` printed `ok` at
  VERIFYING and `FAIL` against the BASE render.
- AC8 — `grep -c "severity:" tools/workflows/tier2-review.test.sh` — printed 9 at this unit's commit
  278c694f and 2 at 9fdd0c18, seven more; at the build's tip it prints 11. `FLOOR_ASSERTIONS` read
  123 at 4ce58141, the unit built just before this one, and 130 at 278c694f, seven above. The arms of
  AC1 to AC7 were read from the main loop's runs above, the green one and the RED one.
