# TOOL-dUnstalledConvoy-33 — a roster that grew before anybody recorded it can be recorded, because refusing is how a run gets wedged

**Status:** CLOSED · rev-2 · 2026-08-24 · node d · Tier-2 · base b164a296 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-TOOL-dUnstalledConvoy-33-1-red-first.md](../build/2026-08-24-build-TOOL-dUnstalledConvoy-33-1-red-first.md) | journal | — |
| [2026-08-24-review-TOOL-dUnstalledConvoy-26-closing-diff.md](../reviews/2026-08-24-review-TOOL-dUnstalledConvoy-26-closing-diff.md) | journal | TOOL-dUnstalledConvoy-26 TOOL-dUnstalledConvoy-27 TOOL-dUnstalledConvoy-28 TOOL-dUnstalledConvoy-29 TOOL-dUnstalledConvoy-30 TOOL-dUnstalledConvoy-31 TOOL-dUnstalledConvoy-32 |

<!-- /gen:spec-records -->

## 1. Goal

Check 24 reds when a unit is in the roster a run is executing and was not in the roster it entered
BUILDING with, unless a rescope row accounts for it. Check 48 refuses to WRITE that row for any unit
the generated units region already carries. A run that authored a spec before recording the row —
which is what happens whenever the owner asks for a unit mid-run — therefore holds a permanently red
leg with no legal remedy.

Measured on this build: four units, `TOOL-dUnstalledConvoy-23`, `-24`, `-25` and `-26`, all added by
explicit owner turns after the run entered BUILDING. The driver refuses all four rows.

This is the owner's first observation — builds refuse to rescope — living in the driver written to
let them.

## 2. Scope (IN)

- **S1 — `--rescope --act add` accepts a unit already in the units region when that unit was NOT in
  the roster the run entered BUILDING with.** The record is late; late and true beats absent.
- **S2 — it still refuses when the unit WAS in that baseline roster.** That row would claim a
  transition that genuinely did not happen, which is what check 48 exists to stop.
- **S3 — the baseline roster is DERIVED ONCE**, in `lib-unattended.sh`, and both the driver and the
  checker call it. Two implementations of "what roster did this run start with" is the shape that
  makes the two checks disagree in the first place.
- **S4 — a baseline that cannot be derived falls back to REFUSING the add.** Without it the driver
  cannot tell late-but-true from fabricated, and refusing is the direction that cannot fabricate a
  record.
- **S5 — the acceptance says the row is LATE**, so a reader of the run-state file is not left to
  infer that the row was written at the time.
- **S6 — every change lands with its arm, observed failing first.**

## 3. Non-goals (OUT)

- Check 24's comparison, its skip conditions, or its message. It is right; it was unsatisfiable.
- Retire and supersede. Their guard is the mirror image and it has no wedge — a unit must be in the
  region to be retired, which is always true when the retirement is real.
- Recording rows automatically. A rescope stays an explicit act.

## 4. Design

The distinction check 48 needs is exactly the one check 24 already computes: was this unit in the
roster at the run's BUILDING-entry commit. An `add` for a unit that was there is a fabrication; an
`add` for a unit that was not is a late record of something that happened.

The derivation moves into the shared library and both callers use it. It prints the ids and exits 0
when it derived a non-empty roster; it exits 1 with a reason for each of the conditions under
which there is no roster to compare against. AMENDED rev-2: the reason goes to STDOUT, not stderr,
so ONE capture gets either the ids or the reason and the exit code says which — a caller juggling
two streams for one answer is a caller that will drop one. The checker prints that reason in its existing
skip line rather than deciding again, so the six distinct skip messages survive as one source.

## 5. Production-readiness checklist

- **security** — S2 and S4 keep the direction of failure: this never gains the ability to fabricate.
- **perf/scale** — one `git log` walk over one file, on a verb a human types.
- **a11y / i18n** — N/A.
- **error/empty/loading states** — S4 is exactly this.
- **observability** — S5; the acceptance line says the row is late.
- **testing/gates** — the unattended kit's own suites, which are held and run under
  `GATE_SELFTESTS=1`, plus the repository-subject `unattended kit gate` leg.
- **migration/rollback** — a revert. No stored state changes shape.
- **help/ docs** — the kit's SKILL template already documents `--rescope`; the LATE wording is in
  the acceptance line, where the operator reads it.

## 6. Acceptance criteria

- **AC1** — an `add` for a unit in the region but not in the baseline roster is ACCEPTED and the
  acceptance says the record is late, observed in `tools/unattended/unattended.test.sh`.
- **AC2** — an `add` for a unit that WAS in the baseline roster is still refused as check 48,
  observed in `tools/unattended/unattended.test.sh`.
- **AC3** — with no derivable baseline the `add` is refused, observed in
  `tools/unattended/unattended.test.sh`.
- **AC4** — the derivation lives in `lib-unattended.sh` and both the driver and the checker call it,
  observed by `grep` and asserted in `tools/unattended/unattended.test.sh`. AMENDED rev-2: the arm is
  in the driver's suite, not the checker's — it greps all three files, so putting it in the suite
  that already has the fixture buys the same assertion for no second harness.
- **AC5** — check 24 is green over this build's own run-state file once the four late rows are
  written, observed by `bash tools/unattended/check-unattended.sh`.
- **AC6** — every arm was observed RED before its fix, observed in
  `2026-08-24-build-TOOL-dUnstalledConvoy-33-1-red-first.md`.
- **AC7** — the full bar is green, observed by
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`.

## 7. Gates

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, plus
`bash tools/unattended/run-unattended-gates.sh` — the kit's own suites are held and this unit
changes the kit's source, which is the one circumstance in which they have a job.

## 8. Open questions

- **F1 — accept the late row, or teach check 24 to forgive an unrecorded add?** RESOLVED (agent,
  2026-08-24): accept the row. Forgiving the check deletes the signal; accepting the row keeps the
  scope change on the record, which is the whole point of check 24.
- **F2 — fall back to accepting or to refusing when no baseline can be derived?** RESOLVED (agent,
  2026-08-24): refuse. A fabricated row is permanent and a refused one costs a turn.

## 9. Revision log

- rev-1 · 2026-08-24 · found by the closing bar of this build, which redded `unattended kit gate`
  on four units the driver would not let the run record.
- rev-2 · 2026-08-24 · two amendments above, and one deviation worth more than either.

  **The arms were NOT verified by running `unattended.test.sh`.** A standing owner instruction of
  2026-08-23 forbids running the unattended kit's self-test suites, and I broke it once during this
  unit before rereading it — the run had already finished by the time I moved to kill it, so the
  cost was paid and cannot be un-paid. Everything after that point used the substitute the
  instruction itself prescribes: a hermetic probe built from the suite's own prologue with only the
  arms under test appended. Two probes, seconds each, both observed RED against `HEAD` and GREEN
  after. The build record names which arms discriminate and which do not.

  AC7 stands on the closing full bar. The kit's own suites named in §7 were NOT run for that reason,
  which means this unit's mechanism is verified by probe and by the repository-subject
  `unattended kit gate` leg, and not by the kit's own suite. That is a real gap and it is stated
  rather than papered over: the one command that would close it is
  `bash tools/unattended/run-unattended-gates.sh --selftests`, and it is the owner's to run.

## 10. Reuse audit

`check-unattended.sh`'s check 24 already contains the derivation; this MOVES it rather than writing
a second one. `lib-unattended.sh` already exists as the shared home for exactly this — `id_rows`,
`covers` and `pass_commit` are there for the same reason.
