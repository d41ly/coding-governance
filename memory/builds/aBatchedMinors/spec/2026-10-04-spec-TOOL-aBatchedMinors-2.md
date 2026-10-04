# TOOL-aBatchedMinors-2 — the closing review's exit records its standing findings and promotes them all

**Status:** CLOSED · rev-3 · 2026-10-04 · node a · Tier-2 · base 5ba0fc4f · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aBatchedMinors-2-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aBatchedMinors-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-build-TOOL-aBatchedMinors-2-runlog-dc0cf1f9.md](../build/2026-10-04-build-TOOL-aBatchedMinors-2-runlog-dc0cf1f9.md) | journal | TOOL-aBatchedMinors-3 TOOL-aBatchedMinors-4 TOOL-aBatchedMinors-6 |
| [2026-10-04-prompt-TOOL-aBatchedMinors-2-1-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aBatchedMinors-2-1-build-brief.md) | journal | — |
| [2026-10-04-review-TOOL-aBatchedMinors-2-closing-diff-round1.md](../reviews/2026-10-04-review-TOOL-aBatchedMinors-2-closing-diff-round1.md) | diff-review | TOOL-aBatchedMinors-1 TOOL-aBatchedMinors-3 TOOL-aBatchedMinors-4 |

<!-- /gen:spec-records -->

## 1. Goal

The owner ruled on 2026-10-04 that EVERY confirmed finding of the closing diff review is promoted to a
unit: one per BLOCKER and HIGH, and the MEDIUMs and LOWs batched into one unit, or two. Today
`--review` cannot tell that rule from the old one. Its row records the blocker count and nothing about
the findings below it, so a closing exit at zero blockers may record no disposition at all and the
mediums and lows it stood on vanish into a fold nothing reads. This unit makes the closing review's
terminal round SAY what stood, and refuses one that stood on anything without promoting it.

## 2. Scope (IN)

- **S1** — `--review` takes `--highs <n>` and `--minors <n>`: the CONFIRMED HIGH findings and the
  confirmed MEDIUM-plus-LOW findings standing at the exit. Each, when given, is a plain integer or
  the verb refuses (check 37). Observed by AC1.
- **S2** — The two counts are the CLOSING review's: on a subject that is not the build slug they are
  refused, naming that a spec audit's minors are folded into the spec under review. On the slug
  subject they are refused on a round that is not a terminal exit, exactly as `--disposition` is, and
  REQUIRED on one that is (`CONVERGED`, `NON-CONVERGENT`, `CEILING`). Observed by AC2 and AC3.
- **S3** — At a terminal round of the slug subject, `standing = blockers + highs + minors`. A
  non-zero `standing` requires `--disposition promote`; `fold` is refused there whatever the counts,
  because the closing review folds nothing. A zero `standing` refuses `promote`, because a promotion
  of nothing writes a row the gate would read as owing a unit. Observed by AC4 and AC5.
- **S4** — The row carries the counts after the exit token and before the disposition, so the field
  the gate reads as LAST stays the disposition:
  `verdict <v> · blockers <b> · <EXIT> · highs <h> · minors <m>[ · disposition promote]`. The echo
  names the unit floor the exit owes: one per blocker and high, plus one for the minors when any
  stood. Observed by AC6.
- **S6** — The driver's usage header names both flags on the `--review` line, because check 26 reds a
  parsed flag no header line documents. Observed by AC8.
- **S5** — The spec-audit path is byte-for-byte unchanged: a non-slug subject's rows, refusals and
  echoes do not move. Observed by AC7.

## 3. Non-goals (OUT)

- The spec audit's disposition. A spec subject's mediums and lows are folded into the spec under
  review, which IS their fix; the owner's ruling names the closing review.
- How the minors are split between one unit and two. The verb records the count; the split is the
  method's rule, stated by `TOOL-aBatchedMinors-4`.
- The gate's reading of the new fields, which is `TOOL-aBatchedMinors-3`.
- A cutoff. Old rows carry no counts and the verb is the only writer of new ones.

### Edges

- **hands-off** `TOOL-aBatchedMinors-6` — the closing review's batched minors harden this unit.
- **hands-off** `TOOL-aBatchedMinors-3` — the row grammar S4 writes is the one check 2 reads.

## 4. Design

### Evidence

Read at base `5ba0fc4f`. `verb_review` in `tools/unattended/unattended.sh` computes the state from the
blocker counts, keys its disposition gate on that state, and writes one row through `park()`. Check 2
of `tools/unattended/check-unattended.sh` reads the disposition as the LAST ` · ` field of the reason
and the blocker count by `match(rs, /blockers [0-9]+/)`, so two new fields placed between the exit
token and the disposition change neither read. The closing review's subject is the build slug, the
equality `verb_review` already makes to choose the round bound.

### Data model

```
2026-10-04T12:00:00Z review · item <slug> · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 1 · minors 4 · disposition promote
```

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`

### Alternatives rejected

- **One `--units <n>` flag naming the units promoted.** Nothing could compare it to anything: a run
  that promoted too few would record too few. Counts of what STOOD are facts the review produced.
- **The gate parsing severities out of the review record.** Tested at base: of 141 tracked
  diff-review records, 8 carry a `| <SEVERITY> |` table row; the rest grade in headings whose shape
  varies by author. A parser would read a grammar the records do not share. The harness's tally is
  already integers, and the verb is where integers become a row.
- **`--confirmed` beside `--highs`, minors derived by the verb.** The verb sees one round, and the
  minors standing at the exit are summed over every round's return; the subtraction belongs to the
  operator holding those returns.

## 5. Production-readiness checklist

- perf / scale — two integer tests and one string comparison per round; no new process.
- security — no new write path: the row still goes through `park()` and its guards.
- error / empty / loading states — every malformed count, every count on the wrong subject or round,
  and every disposition the counts contradict is a numbered refusal that writes nothing.
- observability — the echo names the unit floor the exit owes.
- testing — each refusal is observed against the base driver first.
- migration — none: rows written before this carry no counts and nothing re-reads them as owing any.
- user docs — the verbs entry and the Skill, in `TOOL-aBatchedMinors-4`.
- risks — an in-flight closing review recorded before this lands has no counts; it keeps its row.

## 6. Acceptance criteria

- **AC1** — When `--review` runs with `--highs x` or `--minors -1`, it refuses naming the flag as
  not a plain integer, and the run-state file gains no row.
  Red when: the value is written into the row unvalidated.
- **AC2** — When `--review` runs on a spec subject with `--minors 2`, it refuses naming the closing
  review, and no row is written.
  Red when: the spec-audit path accepts a count the gate would then read as owing units.
- **AC3** — When the slug subject's terminal round omits either count, `--review` refuses naming the
  missing flag; when a non-terminal slug round carries one, it refuses as a claim about an exit that
  has not happened.
  Red when: a converged closing round records with no counts, the base behaviour.
- **AC4** — When the slug subject converges with `--highs 0 --minors 3` and no disposition, it
  refuses naming `promote`; with `--disposition fold` it refuses naming that the closing review folds
  nothing; with `--disposition promote` it writes the row.
  Red when: the base driver's "never required at CONVERGED" stands for the closing review.
- **AC5** — When the slug subject converges with `--highs 0 --minors 0 --disposition promote`, it
  refuses as promoting nothing; with no disposition it writes the row.
  Red when: a zero-standing promote row is written.
- **AC6** — When the slug subject converges with `--highs 1 --minors 4 --disposition promote`, the
  row reads `blockers 0 · CONVERGED · highs 1 · minors 4 · disposition promote` and the echo names a
  floor of 2 units.
  Red when: the counts follow the disposition, so the gate's last-field read breaks.
- **AC7** — When the existing `--review` arms that grade spec subjects run unchanged against the
  new driver, they pass.
  Red when: a spec-subject refusal or echo moved.
- **AC8** — When `bash tools/unattended/check-unattended.sh` runs, check 26 names no undocumented flag.
  Red when: the parser takes `--highs` and `--minors` and the header line does not.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · the base driver, which accepts a converged closing round with no counts · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the owner's ruling and `verb_review` at base.
- rev-2 · 2026-10-04 · S6 · AC8 · building found check 26 reds an undocumented flag, so the usage
  header line moves here from `TOOL-aBatchedMinors-4`, which owns the same file's prose no further.
- rev-3 · 2026-10-04 · §3 Edges · the hands-off to `TOOL-aBatchedMinors-6`, which consumes this unit; the
  close's hygiene check 12 found the edge one-sided.

## 10. Reuse audit

The seam extended is `verb_review` itself: its closed-set test, its state gate keyed on the computed
state, its `subj = slug` bound equality and its single `park()` write. No new verb, no new row kind.
`python tools/codebase-map/reuse_lookup.py "closing review disposition promote findings to units by
severity"` printed `unscanned layers: .sh`, so it cannot see this seam; the seam was found by reading
`unattended.sh`. `python tools/memory-recall/query.py` returned `TOOL-aProbedUnit-9`, the severity
ruling this unit supersedes for the closing review, and the cluster-C record that made `promote`
optional at `CONVERGED`.

Recall terms used: closing review disposition promote fold severity BLOCKER HIGH MEDIUM LOW unit rescope CONVERGED
