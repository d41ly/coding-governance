# Acceptance ledger — DEPL-dRemeasuredRender-4

**Serves:** journal DEPL-dRemeasuredRender-4

Built on `57a98c4f`. The touched blocks of `check_update_safety` — the rollback fixture, `[aHI-1]`,
and this build's two — ran through the scratch runner against this tree's `govkit.py`, where every
assertion held, and against `bac1a4fb`'s, the tip the closing review read. There the behaviour arm,
`[dRR-4 AC1]`, failed: the hole was reported discharged and then its render was rolled back.

The coverage arms test guards that already worked at `bac1a4fb`, so each was proved able to fail on
a mutant of this tree's `govkit.py` with four edits: the rolled-back guard and the not-run guard
disabled, the absent-file branch deleted and the `version` re-stamp deleted. All four arms of AC3
and AC4 failed on it. AC5's arm guards a placement that was already right; AC6's repointed arm
fails if the early line goes, as the dRR-2 LIVENESS arms do.

The review's two proposed meta-gates were not built; the class is recorded as
`memory/gotchas/verdict-printed-before-the-step-that-reverts-it.md`.

**Evidences:** DEPL-dRemeasuredRender-4
- AC1 — `is undischarged` — over the `hb` fixture, whose render discharges the hole and whose `[check]` then reds, the run printed ROLLED BACK and `is undischarged (probe exit 1) after the rollback restored the pre-render bytes`, and no `is discharged after the render` line; red at bac1a4fb
- AC2 — `render_hole_verdict` — called in-process with `undischarged`, `discharged` and `no-launch`, it returned three distinct lines, `neither verdict is confirmed` for the third, and named the rollback when asked
- AC3 — `KEPT` — the rollback fixture printed `its kit was rolled back`, a `GOVKIT_RERENDER=0` run printed `its render did not run this time`, and a render that deleted its file printed `its file is absent after the render` with `rendered receipts: 0 re-measured · 1 kept`; each row equalled its pre-update record; each arm red on the guard-dropping mutant
- AC4 — `version` — the re-measured row's version read `DEMO_VERSION=1.1` where the install's read `DEMO_VERSION=1.0`; red on the mutant without the re-stamp
- AC5 — `exited 5` — over the `hr` fixture the run printed the refusal and then the hole's `is undischarged (probe exit 3)` after its early line
- AC6 — `probes undischarged before the render (probe exit 3)` — the `[aHI-1 S3]` arm found that line before the `ran` line
