# TOOL-aWindowedPass-2 — acceptance ledger

**Serves:** journal TOOL-aWindowedPass-2

`pass_commit` and `build_commit` attribute per commit: a `Pass:` trailer decides alone, and a commit
with none falls back to its subject. The arm observations are the main loop's, on a slice of
`check-unattended.test.sh` holding its prologue and the trailer arms: four arms green, then red with
the trailer branch staged out of the library, and the library restored before commit 55213dd2. The
grep readings were re-taken at the close of the build. What the break run printed per arm was not
kept beyond its verdict, so the red halves below say only that.

**Evidences:** TOOL-aWindowedPass-2
- AC1 — `pass_commit` — the arm with a `Pass: none` records commit and then a `Pass: ARCH-tRun-1`
  commit passed, with no check 23 FAILED; the slice was red with the trailer branch staged out.
- AC2 — `pass_commit` — the no-trailer arm graded the subject-named commit, as at base.
- AC3 — `build_commit` — the arm comparing its answer to the trailered commit printed `same`, and the
  slice was red under the same break.
- AC4 — `Pass: <unit-id>` — the grep over `tools/workflows/unattended-unit.js` printed 1, and the
  same grep over the rendered `.claude/skills/unattended/SKILL.md` printed 1.
