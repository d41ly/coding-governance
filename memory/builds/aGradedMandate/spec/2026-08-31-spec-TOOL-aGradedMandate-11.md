# TOOL-aGradedMandate-11 — the closing-loop census is MEASURED and recorded, never pinned from memory

**Status:** SPECCED · rev-2 · 2026-08-31 · node a · Tier-1 · base 396cd9db · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-review-TOOL-aGradedMandate-10-promotion-audit.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-10-promotion-audit.md) | spec-audit | TOOL-aGradedMandate-10 |

<!-- /gen:spec-records -->

## 1. Goal

PROMOTED, not authored: round 2 of this build's spec audit exited `NON-CONVERGENT`, and its blocker
R2 became this unit. `TOOL-aGradedMandate-1`'s AC7 invoked the charter's rule — run a candidate gate
predicate over the real tree before wiring it — and then answered it from memory, pinning three
expected hits where the executed predicate returns twenty-one. This unit produces the measurement as
a committed record and rewrites AC7 to read that record instead of a number nobody re-ran.

## 2. Scope (IN)

- **S1** — Write a journal record under `memory/builds/aGradedMandate/build/` carrying the executed
  output of `TOOL-aGradedMandate-1` S1's predicate over EVERY tracked `RUN.md`: per record, whether
  it passes, and if not, which arm refuses it — the no-row arm or the no-terminal-token arm.
- **S2** — Replace `TOOL-aGradedMandate-1` AC7 with one that reads that record: the predicate's
  verdict for every tracked `RUN.md` matches the recorded set, and any record at a NON-TERMINAL
  phase that refuses is a finding. The failure condition is a DIVERGENCE from a measured set, never
  a count typed into a spec.
- **S3** — State in the record WHY a refusal on a terminal record costs nothing: the
  slug-subject closing-review convention postdates most tracked records, `--close` is the only
  reader, and no verb re-closes a terminal record. That is the argument `TOOL-aGradedMandate-1` §4
  is actually making, and the record is its evidence.
- **S4** — The record carries its own liveness assertion: it names the count of records examined and
  the count that refuse, so a future run of the same probe over an empty selection is
  distinguishable from a clean corpus.

## 3. Non-goals (OUT)

- **No gate.** The population legitimately freezes at authoring time and a leg over it would red
  honest landings — `TOOL-aGradedMandate-1` §3 already rules that out and this unit does not
  reopen it.
- **No change to S1's predicate.** The census measures the predicate as specced; it does not tune it
  to make the number smaller.
- **No retrofit of the refusing records.** Twenty-one tracked records refuse, and **two of them are
  NON-TERMINAL**: `memory/builds/aGradedMandate/RUN.md` at `FOLDING`, which is this build's own, and
  `memory/builds/aThawedCorpus/RUN.md` at `LANDING`, which is not — `PHASES_TERMINAL` is
  `LANDED ABORTED` at `unattended.sh:333`. So the census DOES fire the finding S2 and AC4 define, and
  it is owed an answer rather than pre-declared harmless. What is owed per record: this build's own is
  answered by `TOOL-aGradedMandate-1` AC8, which requires the closing round to take the bare slug;
  `aThawedCorpus` has already had `--close` run and nothing re-evaluates it, which the census records
  as its disposition. The nineteen terminal refusers are not rewritten, because rewriting a finished
  record is what the protocol forbids.

## 4. Design

The record is an ordinary journal-kind record with a `**Serves:**` binding line naming
`TOOL-aGradedMandate-1` and this unit. Its body is the probe's output, unedited, above a short
reading of it. The probe is a shell loop over `GIT ls-files 'memory/builds/*/RUN.md'` applying S1's
three clauses; it is written in the record itself so a later reader can re-run the same bytes rather
than reconstruct them from prose.

### Files touched (estimate)

| File | Why |
|---|---|
| `memory/builds/aGradedMandate/build/<date>-build-TOOL-aGradedMandate-11-closing-loop-census.md` | S1, S3, S4 |
| `memory/builds/aGradedMandate/spec/2026-08-31-spec-TOOL-aGradedMandate-1.md` | S2, as a rev bump |

### Alternatives rejected

Loosening S1's subject join so more records pass. Rejected: it would tune the predicate to flatter
the census, which is the inverse of what a probe is for, and `TOOL-aGradedMandate-1`'s rev-3 fold
already ruled the join stays exact.

## 5. Production-readiness checklist

- security — N/A. Reads tracked records.
- perf / scale — N/A. One pass over 28 files.
- a11y — N/A. No user surface.
- i18n — N/A. No user surface.
- error / empty / loading states — S4's liveness assertion is exactly this: a probe that selects
  nothing says so rather than reporting a clean corpus.
- observability — the record IS the observability, and it is committed rather than left in a
  transcript.
- risks — the census goes stale as records land. Accepted and stated in the record: it is dated
  evidence for a decision taken on that date, not a live query, which is the same status every
  measurement in this repo's build records carries.
- testing + left-shift gates — none owed; §3 states why a gate over this population is refused.
  The left-shift is procedural and is recorded in the build README's build-level rules: a
  grep-shaped or census-shaped criterion is not accepted until its value has been MEASURED and
  written down.
- migration / rollback — deleting the record and reverting AC7.
- user docs — none owed.

## 6. Acceptance criteria

- **AC1** — The record exists, is TRACKED, and carries a `**Serves:** journal` binding line naming
  `TOOL-aGradedMandate-1` and `TOOL-aGradedMandate-11`, verified by
  `python tools/memory-tree/gen_build_index.py --print-bindings`.
- **AC2** — The record's per-record verdicts are reproducible: re-running the probe the record
  carries against `GIT ls-files 'memory/builds/*/RUN.md'` produces the same pass and refuse sets, and
  the record names both counts.
- **AC3** — `TOOL-aGradedMandate-1` AC7 NAMES THIS RECORD BY FILENAME:
  `grep -c 'closing-loop-census' memory/builds/aGradedMandate/spec/2026-08-31-spec-TOOL-aGradedMandate-1.md`
  returns at least 1. **Measured before the edit: 0.** The obvious spelling was rejected as
  unfalsifiable — `grep -c 'a fourth hit'` over that spec already returns 0, because the round-2 fold
  replaced AC7 with a supersession note, so it cannot go red in either direction and S2 would have no
  observer at all.
- **AC4** — The record names every NON-TERMINAL `RUN.md` it examined and its verdict for each,
  which is the arm that would have caught round 2's R7 — this build's own
  `memory/builds/aGradedMandate/RUN.md` included.
- **AC5** — `bash tools/memory-tree/check-memory-hygiene.sh` is green over the new record, which is
  what grades its filename and its binding line.

## 7. Gates

`memory hygiene` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-31 · PROMOTED from round 2 of the spec audit, blocker R2, per the build method's
  M4 exit rule.

- rev-2 · 2026-08-31 · promotion-audit fold of the BLOCKER B1 and of H1. AC3 was unfalsifiable - its grep already returned 0 because the round-2 fold had replaced AC7 with a supersession note - and now names this unit's record by filename, measured at 0 before the edit. Non-goal 3's claim that every refuser is terminal or this build's own is corrected: two are non-terminal and one of those is another build's.

## 10. Reuse audit

The SET-level probes are recorded in `TOOL-aGradedMandate-1` §10.

The seam is the memory tree's own journal-record convention: `memory/HYGIENE.md`'s "Record bindings"
already closes the kind set and `gen_build_index.py --print-bindings` is already both the report and
the gate's predicate, so nothing new is needed to make this record findable or graded.

No existing seam produces the census. `tools/drift-audit/drift_report.py` sweeps records for
staleness rather than applying a candidate predicate, and the unattended leg's own record walk grades
what is there rather than what a proposed check would say. The probe is therefore written here, and
it is written INTO the record so the next reader re-runs bytes rather than prose.
