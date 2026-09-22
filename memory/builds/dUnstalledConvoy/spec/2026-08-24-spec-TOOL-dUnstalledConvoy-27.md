# TOOL-dUnstalledConvoy-27 — the push boundary READS the stamp's switch field, or the field is a byte nobody consults

**Status:** CLOSED · rev-1 · 2026-08-24 · node d · Tier-2 · base b164a296 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-TOOL-dUnstalledConvoy-26-2-acceptance-ledger.md](../build/2026-08-24-build-TOOL-dUnstalledConvoy-26-2-acceptance-ledger.md) | journal | TOOL-dUnstalledConvoy-26 TOOL-dUnstalledConvoy-28 TOOL-dUnstalledConvoy-29 TOOL-dUnstalledConvoy-30 TOOL-dUnstalledConvoy-31 TOOL-dUnstalledConvoy-32 |
| [2026-08-24-build-TOOL-dUnstalledConvoy-27-1-red-first.md](../build/2026-08-24-build-TOOL-dUnstalledConvoy-27-1-red-first.md) | journal | — |
| [2026-08-24-review-TOOL-dUnstalledConvoy-26-closing-diff.md](../reviews/2026-08-24-review-TOOL-dUnstalledConvoy-26-closing-diff.md) | journal | TOOL-dUnstalledConvoy-26 TOOL-dUnstalledConvoy-28 TOOL-dUnstalledConvoy-29 TOOL-dUnstalledConvoy-30 TOOL-dUnstalledConvoy-31 TOOL-dUnstalledConvoy-32 TOOL-dUnstalledConvoy-33 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dUnstalledConvoy-26` records the self-test switch in the `gate-full-green` stamp so a green can
say what it covered. Nothing reads it. `.githooks/pre-push` parses exactly `sha`, `fingerprint` and
`manifest_blob`, and its predicates consult nothing else — so the field is written and inert, and the
push boundary accepts a record earned over a partial bar as proof for a push that needs a whole one.

## 2. Scope (IN)

- **S1 — the hook's parser learns the key.** It reads the recorded switch state alongside the three
  fields it already takes.
- **S2 — one more predicate: the record must COVER the run it is offered for.** A green earned with
  self-tests OFF does not satisfy a push that would run them; a green earned with them ON satisfies
  either. Coverage, not equality — a record that covered MORE is still proof.
- **S3 — an absent key reads as OFF.** Every stamp written before this unit lacks it, and defaulting
  the missing case to "covered everything" would make every pre-existing record certify legs it never
  ran.
- **S4 — the forcing reason NAMES the switch** when that is why a full run is owed, in the same shape
  the hook's other reasons take. A run forced for an unstated reason is a run whose operator learns
  nothing.
- **S5 — every change lands with its arm, observed failing first.**

## 3. Non-goals (OUT)

- Changing what the stamp WRITES. `TOOL-dUnstalledConvoy-26` owns that; this unit reads it.
- Changing the other seven predicates, the lag bound, or the fingerprint check.
- Deciding where this repo SETS the switch — `TOOL-dUnstalledConvoy-28`.

## 4. Design

The hook already decides whether a full run is owed and already has a vocabulary of reasons for
saying so. This adds one reason and one field to a parser that takes three.

S2's direction is the whole of the correctness. The tempting predicate is equality — record and run
agree — and it is wrong in the cheap direction: a record earned with self-tests ON is strictly
stronger evidence than a switch-off push needs, and forcing a full run there would cost every adopter
the saving the parent unit exists to give. Coverage is the relation; equality is a stricter relation
that happens to look like one.

S3 is the migration. There is no stamp in the wild carrying this key, and the safe reading of its
absence is the weaker one.

## 5. Production-readiness checklist

- **security** — this is the security half of the parent unit. Without it the push boundary trusts a
  green it cannot interpret.
- **perf/scale** — one more line parsed, one more comparison, on a path that already reads the file.
- **a11y / i18n** — N/A.
- **error/empty/loading states** — S3 is exactly this: a record without the key.
- **observability** — S4; the forcing reason is the operator's only window into this decision.
- **testing/gates** — the pre-push self-test, plus the full bar.
- **migration/rollback** — S3 makes old records safe by construction. Rollback is a revert.
- **help/ docs** — `AGENTS.md`'s merge-bar section describes what the hook decides and on what.

## 6. Acceptance criteria

- **AC1** — the hook parses the switch key from a stamp, observed in `.githooks/pre-push.test.sh`.
- **AC2** — a record earned switch-OFF does not satisfy a switch-ON push; a full run is forced,
  observed in `.githooks/pre-push.test.sh`.
- **AC3** — a record earned switch-ON satisfies a switch-OFF push; no full run is forced, observed in
  `.githooks/pre-push.test.sh`.
- **AC4** — a record with NO switch key reads as OFF, observed in `.githooks/pre-push.test.sh`.
- **AC5** — the forcing reason names the switch when that is the cause, observed in
  `.githooks/pre-push.test.sh`.
- **AC6** — every arm was observed failing against the pre-fix hook, observed in
  `2026-08-24-build-TOOL-dUnstalledConvoy-27-1-red-first.md`.
- **AC7** — the full bar is green, observed by `bash tools/run-gates/run-gates.sh`.

## 7. Gates

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **F1 — coverage or equality?** RESOLVED (agent, 2026-08-24): coverage. Equality forces a full run
  whenever a stronger record is offered for a weaker push, which is every adopter's ordinary case and
  would delete the parent unit's saving at the boundary it was measured for.

## 9. Revision log

- rev-1 · 2026-08-24 · promoted from round 2's NON-CONVERGENT spec audit of
  `TOOL-dUnstalledConvoy-26`, which found the stamp field written and never read.

## 10. Reuse audit

The hook already parses the stamp and already carries a reasons vocabulary; this adds a key and a
predicate to both rather than a second reader. No new file.
