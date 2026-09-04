# TOOL-aWeldedTribunal-6 — `govkit update` reports a source gov started shipping instead of missing it

**Status:** CLOSED · rev-4 · 2026-09-04 · node a · Tier-2 · base 9b5ae688 · streams tooling · order 6 · ratified 2026-09-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md) | spec-audit | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-round2.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-round2.md) | spec-audit | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |

<!-- /gen:spec-records -->

## 1. Goal

`govkit update`'s classification loop iterates the RECEIPT, so a file gov newly ships for a kit the
target already claims is not in the iteration space at all. The verb reports the install clean and
the adopter finds out at the next `ImportError`. Measured on a live adopter: the lexicon kit's
`canon.py` was claimed by that kit's `include = "**"`, present in gov at the exact sha the adopter
pulled, reported as a GAP by `plan --coverage`, and still left out by `update --write`. Every entry
point of that kit died for six days under a green bar.

## 2. Scope (IN)

- **S1** — `update` computes the GAP set for the kits in scope, using `coverage_rows`, which is the
  existing read-only join that answers exactly this question and needs no receipt.
- **S1b** — **The gap set is GRADED through `decline_findings` before anything is printed**, the way
  both existing call sites do it. `coverage_rows` does NOT honour the decline registry — §4 shows
  its body — so an ungraded call reports every deliberately-declined file as a gap. It needs
  `commit_now` from `git rev-parse HEAD`, and it grades staleness as well as presence.
  **It is NOT a pure grader**: it calls `r.fail(...)` on twelve arms between `govkit.py:2489` and
  `:2609`, `Report.emit` returns 1 whenever `problems` is non-empty (`:964-972`), and `_cmd_update`
  returns `r.emit()` on every exit path. So passing `update`'s own Report would make a malformed or
  stale `[[decline]]` row FAIL a write verb operators run constantly, for a defect that has nothing
  to do with the update. §8 resolves which Report is passed.
- **S2** — Each UNDECLINED gap is REPORTED as its own counted line, naming the kit, the destination
  and the gov source, in the same shape the other classification verdicts print. A DECLINED row
  prints too, as a declined row, because a gap that disappears from a report without saying why is
  the exclusion-list shape the decline contract exists to avoid becoming.
- **S3** — An UNDECLINED gap makes the verb's summary say the install is INCOMPLETE. A fully
  declined gap set summarises COMPLETE. The defect is not that a file was left out; it is that
  leaving it out read as clean, and a summary that reads INCOMPLETE forever for a target with a
  decline registry is the same defect with the sign flipped.
- **S4** — `--kits` scoping binds the gap set exactly as it binds `rows_all`. A gap in a kit the
  caller did not name is not this invocation's business.
- **S4b** — The THREE call-site enumerations in the source are renumbered in the same commit:
  `govkit.py:2438` reads "ONE PREDICATE, TWO CALL SITES — `cmd_check` and `plan --coverage`" inside
  `decline_findings`'s own docstring, `:2674` reads "call site one of two" and `:2859` "call site two
  of two". S1b makes `update` the third. Those three sentences are the record of the decision S1b
  reuses, and leaving them to become wrong on landing is the same class sibling unit 7 spends four
  scope items on for two other carriers — in the file this unit edits.
- **S5** — An arm proving a gap is DETECTED and one proving a clean install reports ZERO gaps, and
  the zero is PRINTED. A clean run that prints nothing is indistinguishable from a coverage report
  that failed to run, which is a rule `plan --coverage` already follows in this same file.

## 3. Non-goals (OUT)

- **WRITING the gap.** This unit reports; it does not land bytes. Landing a source that has no
  receipt row means inventing a row — deciding its role, its `commit`, its `gov_oid`, whether the
  target ever declined it — and every one of those is a decision `update` has no evidence for. The
  row this closes says "there is no verb that lands new kit bytes without adopting", and a REPORT
  is what makes that fact visible at the right moment. The landing verb is a follow-up and needs its
  own owner decision about the role a synthesised row carries.
- **Making `update` run the kit's `[adopt]`.** That is `apply`, and for an adopter holding a kit
  deliberately inert it is a posture flip. The row names this explicitly as not the workaround.
- **Auditing the twelve of fourteen kits.** The row states that how many of those are real gaps
  versus sanctioned divergence needs per-kit judgement and was not measured. Reporting them is what
  makes that judgement possible; making it is not this unit's.
- **`TOOL-aScouredKit-25`.** Not a separate unit. It is the same defect independently re-confirmed
  and says in its own text to close it against `TOOL-aFlaggedScaffold-3` rather than work it twice.
  It closes with this unit.

## 4. Design

### Where the gap set comes from

`coverage_rows(root, target, deploy, descs, selection, r, rows)` at
`tools/govkit/govkit.py:2263` is the existing predicate, built by `DEPL-dCarriedReceipt-4`, with two
call sites already: `plan --coverage` and `cmd_check`. It is a read-only join that needs no receipt.
This unit is call site three and adds no predicate.

**It does NOT honour the decline registry, and rev-1 said it did.** Its whole body is:

```python
return [{"kit": row["kit"], "dest": row["dest"], "src": row["src"]}
        for row in rows
        if row["kind"] == "write" and not row["missing"] and row["dest"] not in have]
```

No decline lookup anywhere. **Both existing call sites grade it themselves**: `:2673` computes gaps,
calls `decline_findings` at `:2679`, and prints `GAP` only where the lookup returns `None`; `:2869`
does the same for `check`. The comment beside the first says why the map comes back from the GRADER
rather than being read off the descriptor — filtering on presence alone makes it an exclusion list
again, which is the thing `DEPL-dCarriedReceipt-5` exists to prevent.

Built on rev-1's false premise, `update` would print every deliberately-declined file as a gap and
pin its summary to INCOMPLETE permanently for any target with a decline registry. That is the
crying-wolf failure the decline contract's own header names, applied to the verb operators run most.
So the grading step is S1b and it is not optional.

That single-predicate property is the whole reason this is small. The row's measurement — that
`plan --coverage` REPORTS the gap while `update --write` leaves it out — is the evidence that the
question is already answered correctly somewhere in this file and simply is not asked here.

### Where it runs

**AFTER every refusal this verb already makes**, immediately before the unclaimed-sources report and
the three summary exits. Rev-3 said "after `--kits` scoping and before the classification loop", and
that was MEASURED WRONG: `coverage_rows` calls `planned_writes`, which RAISES on an out-of-tree
prefix, so the `-11` escape fixture's GRADED refusal became a hard abort and its self-test arm went
from pass to fail. `index_read`'s own header in this same file records that class for out-of-tree
paths — raising on one turns a graded refusal into an abort and changes the verb's exit code.

**A report may never pre-empt a refusal.** The whole pass is additionally wrapped so it cannot raise
at all: an exception prints `coverage: UNAVAILABLE` naming the type and message, which is a different
fact from zero gaps and says so. The exit code is never touched — a coverage report is not a merge
verdict.

The `--kits` scope still binds: `_gap_selection` is the receipt's claimed entries intersected with
the descriptors, narrowed by `--kits` when given.

### The summary

`update`'s closing line gains a gap count, and a non-zero count changes the verb's own verdict
sentence from clean to incomplete. `plan --coverage` already prints `gap 0` deliberately, for the
reason its own comment gives — a clean run that printed nothing is indistinguishable from a
coverage join that did not run. This unit inherits that rule rather than restating it.

### Files touched (estimate)

- `tools/govkit/govkit.py` — one call, one print loop, one summary field, and the three call-site
  enumerations of S4b at `:2438`, `:2674` and `:2859`.
- `tools/govkit/selftest.py` or the govkit suite — the arms of S5.

### Alternatives rejected

- **Iterate the descriptor sources instead of the receipt.** Rejected: the receipt is the record of
  what the target TOOK, and iterating sources would reclassify every declined and every
  deliberately-inert file as a row to move. That is a much larger behaviour change than the defect
  warrants, and it is the shape that would need the per-kit judgement §3 declines to make.
- **Have `update` write the gap with a synthesised row.** Rejected per §3: no evidence for the
  fields.
- **Point the operator at `plan --coverage` in the refusal.** Rejected as the WHOLE fix: it is good
  advice and is worth including in the report line, but a verb that requires the operator to
  already suspect the problem is the same silence one message further away.

## 5. Production-readiness checklist

- security — no new write path; this unit strictly reads and prints. The verb writes into a
  repository gov does not own, which is why the non-goal against writing is load-bearing.
- perf / scale — one `coverage_rows` join per invocation. `plan --coverage` already pays it and its
  own comment notes the cost, so the flag is not doubled: it is computed once and used once.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a target with no descriptors yields an empty gap set and prints
  `gap 0`.
- observability — this unit IS the observability fix.
- risks — the honest one: a REPORT does not fix the adopter. An operator who reads `gap 1` and does
  nothing is in the same state as today, six days of ImportError included. What changes is that the
  state is legible at the moment the verb runs rather than at the next crash.
- testing + left-shift gates — S5's arms. The class is the vacuous-selector family: a verb whose
  population excludes the thing it is asked about.
- migration / rollback — none; no receipt schema change, so no adopter migrates.
- user docs — `update`'s help text and any govkit runbook section describing what the verb covers.
  The sentence "there is no verb that lands new kit bytes without adopting" should be written where
  an operator reads it, not only in a backlog row.

## 6. Acceptance criteria

- **AC1** — When `govkit update` runs against a target whose claimed kit has a descriptor source
  with no receipt row, the output names that source and its destination on its own line.
- **AC2** — When that run finishes, its summary line from `govkit update` reports a non-zero gap
  count and does NOT describe the install as clean.
- **AC3** — When `govkit update` runs against a target with no gaps, the output prints `gap 0`
  explicitly rather than printing nothing.
- **AC4** — When `govkit update --kits <one>` runs against a target with a gap in a DIFFERENT kit,
  that gap is not reported. The scope binds.
- **AC5** — When the arm reproducing the row's own measurement runs — a kit claimed by
  `include = "**"` with a source added upstream — `update` reports the gap that
  `plan --coverage` already reports, so the two verbs agree.
- **AC6** — When `govkit update` runs against a fixture target whose ONLY gap is DECLINED, it prints
  no undeclined `GAP` row and its summary says COMPLETE. This is S1b, and it is the criterion that
  catches a build made on rev-1's false premise.
- **AC6b** — When `govkit update` runs against that same fixture, the output PRINTS a `declined` row
  naming the kit and the destination. AC6 takes the absence half of S2, this takes the presence half.
  Without it the cheapest build filters declined rows out of the report entirely, which passes every
  other criterion whole while committing exactly the exclusion-list failure `DEPL-dCarriedReceipt-5`
  exists to prevent — and which the reference call site at `govkit.py:2681-2689` goes out of its way
  to avoid.
- **AC6c** — When `govkit update` runs against a fixture holding one STALE `[[decline]]` row, its
  exit code is whatever §8 F1 resolved, observed rather than assumed. This is the criterion H2 found
  missing: rev-2 wired a grader that fails on twelve arms into a verb whose §5 asserted no new
  failure mode.
- **AC7** — When `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` runs the govkit legs, they
  stay green.

## 7. Gates

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` for `govkit selftest`, which is
`subject = kit` in `tools/gate-legs.json` and is therefore held as `ondemand` by
`tools/run-gates/run-gates.sh:947` on the plain bar — a leg's GUARD scopes a run, the subject and
chunk decide whether it runs at all. `AGENTS.md` records that no boundary sets `GATE_SELFTESTS`
(owner, 2026-08-27) and that a DoD owes the full pair for KIT work, which this is. The repo-subject
govkit legs still run on the plain bar.


**The FULL PAIR, not half of it.** `AGENTS.md:488` spells the DoD command for KIT work as
`GATE_FULL=1 GATE_SELFTESTS=1`; `GATE_SELFTESTS=1` alone lifts the `ondemand` hold but leaves every
per-leg GUARD in force, so kit legs outside the touched directory stay held with no `skipped` line
saying which. Rev-2 cited the pair and prescribed one half of it.
## 8. Open questions

- **F1 · Which `Report` does `update` pass to `decline_findings`?** The grader writes findings and
  `update` emits whatever Report it is handed, so this decides whether decline-registry hygiene can
  fail a write verb.

  **Option A, `update`'s own Report:** matches both existing call sites exactly. A stale or malformed
  `[[decline]]` row then fails `govkit update`.

  **Option B, a throwaway Report whose problems are PRINTED as informational lines:** `update` gets
  the decline MAP without inheriting decline-hygiene refusals, and nothing is hidden.

  RESOLVED (agent, 2026-09-04, delegated): **Option B**. Option A trips M3's veto 3 — it widens what
  a write verb REFUSES beyond anything this unit's risk tier priced, and §1's whole subject is a
  REPORT. `update` is the verb operators run most, and making it fail on a defect in a different
  registry is how a report stops being run at all. Printing the grader's problems keeps Option A's
  visibility without its blast radius, and AC6c observes the resulting exit code rather than assuming
  it. The reference call sites pass their own Report because `check` and `plan` are read-only verbs
  whose whole job is grading; `update` is not, and that difference is the reason the two diverge.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Confirmed against source that the classification loop is
  `for row in rows_all` over `receipt.get("files", [])` at `tools/govkit/govkit.py:5825`, and that
  `coverage_rows` exists at `:2263` with call sites in `plan --coverage` and `cmd_check` only.
- rev-2 · 2026-09-04 · folded spec-audit round 1 (H1, H7). **H1, high:** rev-1's §4 asserted that
  `coverage_rows` "honours the decline registry". It does not — its body filters on
  `kind == "write"`, `not missing` and `dest not in have`, and BOTH existing call sites grade the
  result themselves through `decline_findings`. The claim was load-bearing, because S1 reused the
  predicate and §4 said the unit "adds no predicate": built faithfully, `update` would have printed
  every declined file as a gap and read INCOMPLETE forever. S1b adds the grading step, S2 and S3 are
  scoped to UNDECLINED gaps, and AC6 is its arm. **H7:** §7 named the plain bar for a
  `subject = kit` leg and reasoned from the leg's guard; corrected to `GATE_SELFTESTS=1`.

- rev-3 · 2026-09-04 · folded spec-audit round 2 (H1, H2, M8, M10). The loop exited NON-CONVERGENT
  at round 2, so this is the disposing fold and there is no round 3. **H1, high:** S2's DECLINED-row
  half was observed by nothing — AC6 checked only the ABSENCE of an undeclined `GAP` row, so the
  cheapest build filters declined rows out entirely and commits the exclusion-list failure S2 names.
  AC6b takes the presence half. This is round 1's dominant pattern recurring on a fold-new scope
  item. **H2, high:** S1b wired `decline_findings` — which `r.fail`s on twelve arms — into a verb
  that returns `r.emit()` on every exit path, while §5 asserted no new failure mode. F1 resolves it
  to a throwaway Report whose problems print, and AC6c observes the exit code. **M8:** S1b makes
  `update` the third call site and three enumerations in the source say two; S4b renumbers them.
  **M10:** §7 prescribed half the pair it cited.

- rev-4 · 2026-09-04 · corrected at BUILD time. Rev-3's stated insertion point put the gap pass
  BEFORE the classification loop, and running the govkit self-test refuted it: `coverage_rows` reaches
  `planned_writes`, which raises on the `-11` escape fixture's out-of-tree prefix, so that fixture's
  graded refusal became a hard abort and its arm failed. Confirmed as MINE rather than pre-existing by
  running the same suite against the stashed-clean tree, where all arms held. The pass now runs after
  every refusal and is wrapped so it cannot raise; §4 records both. This is the same out-of-tree class
  `index_read`'s header already documents in this file, which is worth noting: the file warned about
  it and the first cut walked into it anyway.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "deploy verb reports files gov ships that an adopter does
not hold"` was run and did NOT name the seam — its top candidates were `report` in the drift-audit
selftest and `cmd_report` in `row_grammar.py`, neither of which is this behaviour. That miss is
recorded rather than retried with softer words, because a probe exits 0 on a miss and "nothing
found" is an answer.

The seam is `coverage_rows` at `tools/govkit/govkit.py:2263`, the existing read-only partial-adoption
join built by `DEPL-dCarriedReceipt-4`; this unit is its third call site and introduces no new
predicate. The `gap 0` printing rule is likewise reused from `plan --coverage`'s own comment rather
than re-decided. It was found by grepping `coverage` and `GAP` across `tools/govkit/govkit.py` after
the recall probe surfaced the two backlog rows that measured the defect — which is the documented
fallback when the map probe misses.

Recall terms used: `--terms "agent-cap blankLiterals capFindings fanoutFindings landed phase check34
lander marker unrepairable govkit renormalize memory-tree conf"`
