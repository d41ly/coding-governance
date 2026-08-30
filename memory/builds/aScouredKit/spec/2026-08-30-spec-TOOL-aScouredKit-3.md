# TOOL-aScouredKit-3 — one predicate decides a gate leg's hold, and the pin file sees both fields

**Status:** OPEN · rev-1 · 2026-08-30 · node a · Tier-1 · base 093730e4 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md) | diff-review | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 |

<!-- /gen:spec-records -->

## 1. Goal

Make `govkit selfcheck` report the held-leg count the runner actually holds, and make the subject
pin file grade the SECOND field that decides a hold, so a leg cannot leave every bar without the
move appearing in a diff.

## 2. Scope (IN)

- S1. `tools/govkit/govkit.py` computes held as `subject == 'kit' or chunk == 'selftests'`, matching
  `tools/run-gates/run-gates.sh:947`, which is the code that decides.
- S2. `tools/govkit/subject-pins.tsv` gains a `chunk` column, compared with the same
  regenerate-in-the-same-commit failure text the subject column already carries.
- S3. That file's generated header stops stating that `repo` legs run on every bar, which is false
  for six of its own rows.
- S4. The failing case is OBSERVED before the change lands: a leg flipped to `chunk: selftests`
  must red the pin comparison. Recorded in §9.

## 3. Non-goals (OUT)

- Re-chunking any leg. All 43 `chunk: selftests` legs are intended holds today; this unit changes
  what is REPORTED and what is PINNED, never which legs run.
- The `GATE_SELFTESTS` policy or the owner ruling of 2026-08-23 behind it.

## 4. Design

Two fields decide whether a leg runs on an automatic bar, and only one of them is pinned.

### Inventory

Measured independently at `093730e4` from `tools/gate-legs.json`:

| measure | value |
|---|---|
| legs in the manifest | 86 |
| `subject == kit` | 40 |
| `chunk == selftests` | 43 |
| held under the runner's real predicate | 46 |
| printed by `govkit selfcheck` | 40 |

The six in the gap are `branch-guard self-test`, `pre-push self-test`, `push-main self-test`,
`recall floor arms`, `run-gates canary` and `run-gates gov canary`. The last two are what
`tools/run-gates/run-gates.sh:939-944` calls the bar's own liveness assertion — the arms that catch
a guard naming an untracked path, which would otherwise skip forever and silently. So the instrument
under-reports the hold on exactly the legs whose holding costs the most.

### Alternatives rejected

Changing `run-gates.sh` to match govkit. The runner is the code that decides; an instrument that
disagrees with it is the instrument that is wrong.

## 5. Production-readiness checklist

- security — N/A, a count and a generated column.
- perf / scale — N/A.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — a leg with no `chunk` key pins the empty value, not a default.
- observability — this IS the observability fix.
- risks — regenerating the pin file rewrites every row; the diff must be read, and S4's staged break
  is what proves the new column can actually red.
- testing + left-shift gates — `python tools/govkit/govkit.py selfcheck` and the govkit selftest.
- migration / rollback — the pin file is generated; `selfcheck --write` regenerates it.
- user docs — the generated header is the doc, and S3 corrects it.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs on this tree, its `subject pins`
  note reports `46 held`, not 40.
- **AC2** — When a leg in `tools/gate-legs.json` is staged with `chunk` flipped to `selftests`,
  `python tools/govkit/govkit.py selfcheck` FAILS naming that leg — the failing case, observed and
  recorded in §9 before the fix landed.
- **AC3** — When `tools/govkit/subject-pins.tsv` is read, no line claims that `repo` legs run on
  every bar.
- **AC4** — When `python tools/govkit/selftest.py` runs, it is green.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit acceptance matrix` · the full bar at the push
boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, authored by the run under the standing mandate.

## 10. Reuse audit

The seam is the existing pin machinery in `tools/govkit/govkit.py` — the subject column already has
a reader, a writer, a comparison and a failure message, and this unit adds a second column through
all four rather than building a parallel mechanism. No new file, no new verb. The build's reuse
probe is recorded in `TOOL-aScouredKit-1` §10 and is not re-composed.
