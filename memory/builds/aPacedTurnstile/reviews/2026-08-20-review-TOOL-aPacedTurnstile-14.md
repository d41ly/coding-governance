# M4 spec audit — TOOL-aPacedTurnstile-14

**Serves:** spec-audit TOOL-aPacedTurnstile-14@rev-2

**Verdict:** BLOCKED at rev-2 · folded at rev-3 · node a · base 43a6c13e · 2026-08-20

Shape: four primed document lenses, batched skeptics defaulting to REFUTE, one synthesis, run as a
`Workflow` under the fan-out and concurrency caps. Ten agents. Thirty-five findings raised, twenty
verdicts surviving refutation, seven unique after de-duplication, precision 0.57. Every confirmed
finding was re-verified against source before folding; none was taken on a skeptic's word.

## Confirmed and folded

| # | Sev | Lens | The finding | Folded into |
|---|---|---|---|---|
| 1 | high | prior-art | S8 performs a remedy that `TOOL-aBoundedVerdict-11` names as SUPERSEDED, in a CLOSED ratified record that also declares this row closed. The spec cited that record for support and never named the reversal | §4, a recorded reversal plus the checkable fact retiring the objection |
| 2 | high | prior-art | S3 presented a RESTORED branch as a new one. `TOOL-cBriefedPilot-6` S4 built this refusal for the authored pair and its S7 shipped the arms and the floor raise; `TOOL-aBoundedVerdict-11` S8 repointed that one branch | S3, and §10's prior-art paragraph |
| 3 | high | prior-art | The misnaming S6 corrects has four carriers and S6 reached two | S6 enumerates all four; AC5 became a scoped grep |
| 4 | medium | prior-art | A LIVE parked owner decision leaves open whether `build-complete`'s missing-units term survives at all — the term S2 and S4 serve | §3, as a non-goal naming the park and the revert path |
| 5 | medium | prior-art | The published protocol already promises the malformed-roster refusal, so this restores a contract rather than extending one | §4, and the reason no protocol file is under Files touched |
| 6 | medium | prior-art | S9 corrected one stale map claim; three exist across two dossiers | S9, and `unattended.md` joined Files touched |
| 7 | low | prior-art | `gen_build_index.py`'s `PLAN_OPEN` comment still calls the roster pair RETIRED | §4's closing line, and S9's carrier set |

A criterion for closing the backlog row was absent and nothing observes it — hygiene check 8 grades
that a row carries one status token, never whether the token is true. This exact row is the proof:
another unit already declared it closed and it is still open. Folded as S10 and AC11.

## What the audit did not establish

Three lenses returned findings; the count above is after de-duplication across them, so a finding
raised by two lenses is one row here. The refuted fifteen are in the run's own transcript and are
not re-litigated. Precision at 0.57 sits just above the level at which the charter says to tighten
scope before adding agents, so the shape is retained as-is for the next document audit.

The audit read the spec, the format, the build method, the charter and the driver source. It did NOT
execute the build, because none of it is built — every finding is about the document and the records
it binds, which is what a pre-code pass is for.
