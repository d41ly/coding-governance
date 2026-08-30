# TOOL-aScouredKit-11 — the gate-leg manifest is withheld only by problems the LEGS step raised

**Status:** OPEN · rev-1 · 2026-08-30 · node a · Tier-2 · base 093730e4 · streams tooling+deployer

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md) | diff-review | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 |

<!-- /gen:spec-records -->

## 1. Goal

Stop `govkit apply` from withholding a target's entire gate-leg manifest because of a problem raised
eight steps earlier, and stop the receipt from recording legs that were never written.

## 2. Scope (IN)

- S1. The write-back at `tools/govkit/govkit.py` guards on the problem count raised SINCE the LEGS
  step began, not on the whole run's accumulated `r.problems`.
- S2. A withheld manifest is announced on stdout, naming how many problems withheld it and how many
  legs were built and discarded.
- S3. When the manifest is withheld, `emitted` in the receipt is EMPTY. A receipt claiming legs that
  no file carries is a record of coverage that does not exist.

## 3. Non-goals (OUT)

- Changing which problems any earlier step raises, or making any of them non-fatal.
- The `else:` outbox branch for a target with no promoted runner. Its behaviour is unchanged.
- Retrofitting existing adopter receipts. A re-run writes a correct one.

## 4. Design

`apply` runs nine steps and accumulates findings in one `Report`. The LEGS step's write-back read
`if not r.problems:`, which is the whole run's total — so any earlier problem, including one that is
by design and reported as such, suppressed the manifest for every kit in the run.

The comment already sitting above that loop shows the class was found once and half-fixed: findings
raised INSIDE the leg loop were deferred until after the write-back, because calling `r.fail` there
"suppressed the manifest write for EVERY leg, so one defective leg silently took the healthy ones
with it". The deferral fixed the loop's own findings and left the guard reading the global counter.

### Data model

One integer, `_legs_problems_before`, captured immediately after `step(STEP_LEGS, …)`. The guard
becomes an equality against it. That makes the predicate mean *did THIS step fail*, which is what
the surviving comment already assumes it means.

### Files touched (estimate)

| Area | Files | Note |
|---|---|---|
| Engine | `tools/govkit/govkit.py` | the snapshot, the guard, the withheld branch |

### Alternatives rejected

Writing the manifest unconditionally and letting the caller decide. A manifest built from legs whose
token resolution failed would install argv fragments carrying unresolved `{prefix}` placeholders,
which is a worse failure than withholding — the target would run a bar made of broken commands.

## 5. Production-readiness checklist

- security — none. The change narrows when a file is written; it adds no path and no input.
- perf / scale — N/A, one integer comparison.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — the withheld case is the state this unit adds, and it prints.
- observability — the new stdout line is the fix's own observable.
- risks — the guard now admits a run that had earlier problems, so a manifest can land in a target
  whose install reported other failures. That is correct and is the point: the legs are valid or
  they are not, independently of whether an unrelated kit had a hole. The receipt still records the
  problems.
- testing + left-shift gates — `python tools/govkit/selftest.py`, which drives real `apply` runs in
  throwaway repos.
- migration / rollback — no artifact format changes. An existing receipt with a stale `emitted` is
  corrected by the next `apply`.
- user docs — the stdout line is the operator-facing text; `WIRE-INTO-PROJECT.md` needs no change
  because it never promised the old behaviour.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py apply` runs against a target whose earlier steps
  raise a problem and whose legs all resolve, the gate-leg manifest IS written — verified by reading
  the target's `gate_runner.file` after the run.
- **AC2** — When a leg's own token resolution fails, the manifest is withheld and stdout carries a
  line beginning `govkit apply — gate legs: WITHHELD`, naming the problem count and the leg count.
- **AC3** — When the manifest is withheld, the receipt's `gate_runner.emitted` is an empty list, so
  no reader can infer coverage that no file carries.
- **AC4** — When `python tools/govkit/selftest.py` runs, it is green.
- **AC5** — When `python tools/govkit/govkit.py selfcheck` runs on this tree, it exits 0.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit acceptance matrix` · `govkit refusal join` · the
full bar at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, authored by the run under the standing mandate.

## 10. Reuse audit

The seam is the existing `Report` object, which already counts problems and already has a
step-scoped vocabulary in `STEP_*`. Nothing new is introduced: the fix is to read the counter the
class already maintains at the boundary the step already declares. No existing helper computes a
per-step delta, and one is not extracted for a single call site. The build's reuse probe is recorded
in `TOOL-aScouredKit-1` §10 and is not re-composed.
