# TOOL-aBatchedMinors-6 — the closing review's batched minors, round 1

**Status:** CLOSED · rev-1 · 2026-10-04 · node a · Tier-2 · base 5ba0fc4f · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aBatchedMinors-2-runlog-dc0cf1f9.md](../build/2026-10-04-build-TOOL-aBatchedMinors-2-runlog-dc0cf1f9.md) | journal | TOOL-aBatchedMinors-2 TOOL-aBatchedMinors-3 TOOL-aBatchedMinors-4 |
| [2026-10-04-build-TOOL-aBatchedMinors-6-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aBatchedMinors-6-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-aBatchedMinors-6-1-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aBatchedMinors-6-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build confirmed fourteen findings at round 1: three MEDIUM and
eleven LOW, no blocker and no high. Under the rule this build ships, all fourteen are promoted, and
because nothing above MEDIUM stood they form ONE batched unit. This is that unit. It is the batch the
build method's M4 admits as the one exception to M2's one-mechanism rule, so its scope is the list of
findings it closes rather than one mechanism. One unit, not two: the build is driven inline, so a
second unit across a disjoint write set would buy no concurrency.

Closes the round-1 items of `reviews/2026-10-04-review-TOOL-aBatchedMinors-2-closing-diff-round1.md`:
M1 (ids 2, 13), M2 (id 8), L1 (ids 1, 5), L2 (ids 6, 14), L3 (id 15), L4 (id 16), L5 (id 7), L6 (ids
9, 10, 11) and L7 (id 12).

## 2. Scope (IN)

- **S1 — M1.** On the closing diff review, a non-terminal round's fold fixes its BLOCKERS only, and
  its highs, mediums and lows carry to the exit, where they are counted and promoted. The Skill's
  CONVERGING bullet, the build method's M4 and M8 say so, and M8's invocation passes, on the closing
  review, only the blockers the fold fixed as `priorFindings`. The Skill's derivation of `--highs`
  and `--minors` points at that rule instead of asserting it. Observed by AC1.
- **S2 — M2.** Two arms on a converged closing round: `--highs 1` alone, and `--minors 1` alone, each
  refused naming both flags and writing no row. Observed by AC2.
- **S3 — L1.** `--blockers`, `--highs` and `--minors` refuse a multi-digit value with a leading zero
  and a value longer than nine digits, so bash arithmetic and check 2's awk read one integer. Three
  arms: `08`, `010`, and a ten-digit value. Observed by AC3.
- **S4 — L2.** The verbs entry's CONVERGED sentence is qualified to a spec subject. Observed by AC4.
- **S5 — L3.** The state gate's fold refusal on the build-slug subject says the closing review folds
  nothing, and its comment is qualified to a spec subject. One arm on a NON-CONVERGENT closing round.
  Observed by AC5.
- **S6 — L4.** M2's decompose sentence names the closing review's minors batch as its exception.
  Observed by AC1.
- **S7 — L5.** The build README's improvement bullet describes what shipped. Observed by AC6.
- **S8 — L6.** A graded check-2 arm with two promoting subjects; the S9 refusal's zero-row assertion;
  and the leading-count arm extended to read the subject count. Observed by AC7.
- **S9 — L7.** A post-cutoff fold arm, so the comment's claim holds. Observed by AC7.

## 3. Non-goals (OUT)

- A gate grepping carriers for the blockers-only sentence. The class is the universal
  two-answers-to-one-question entry the checklist already selects on every closing round.
- Unverified findings. Promotion stays scoped to CONFIRMED findings, as the refuted id 4 records.

### Edges

- **consumes-from** `TOOL-aBatchedMinors-2` — the driver it hardens.
- **consumes-from** `TOOL-aBatchedMinors-3` — the leg whose arms it adds.

## 4. Design

### Evidence

The round-1 record names every location; each fix there was judged SOUND by its skeptic, except
id 13's, whose corrected fix S1 takes.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/SKILL.template.md`
- `.claude/skills/unattended/SKILL.md`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/memory-tree/BUILD-METHOD.template.md`
- `memory/guides/BUILD-METHOD.md`

## 5. Production-readiness checklist

- security — the count validation narrows accepted input; nothing widens.
- perf / scale — two more `case` patterns per call.
- observability — each refusal names the flag and the value.
- migration — none: no record is rewritten.
- error / empty / loading states — every new refusal writes no row.
- risks — the method's byte cap; the M8 edit replaces words rather than adding a paragraph.
- testing — each new arm observed red against the round-1 tip.
- user docs — the carriers are the docs.

## 6. Acceptance criteria

- **AC1** — When the rendered Skill, M4, M8 and M2 are read, the closing review's fold fixes blockers
  only, `priorFindings` there carries only fixed blockers, and M2 names the batch exception; the
  `kit/dogfood doc parity` and `unattended skill wiring` legs match renders to templates.
  Red when: a carrier still tells a CONVERGING closing round to fold its highs and minors.
- **AC2** — When a converged closing round gives `--highs 1` alone or `--minors 1` alone, `--review`
  refuses naming both flags and writes no row.
  Red when: the guard is weakened to require both missing.
- **AC3** — When `--highs 08`, `--minors 010` or `--blockers 1234567890` is given, `--review` refuses
  with check 37 naming the flag, and writes no row.
  Red when: the driver aborts on bash arithmetic or computes octal.
- **AC4** — When `memory/guides/UNATTENDED-VERBS.md` is read, its "never required" sentence names a
  spec subject.
  Red when: it stays unqualified.
- **AC5** — When a NON-CONVERGENT closing round gives `--disposition fold`, the refusal says the
  closing diff review folds nothing.
  Red when: it says fold is legal at CONVERGED.
- **AC6** — When the build README is read, no improvement bullet names a harness `minors` key.
  Red when: the retired unit's promise stands.
- **AC7** — When check 2 grades a record with two promoting subjects whose floors are 2 and 1 over two
  new ids, it fails naming a floor of 3, and passes over three; the S9 refusal writes no S9 row; the
  leading count reads `1 subject(s)`; and a fold committed after `FOLD_CUTOFF` reds.
  Red when: the summation regresses to a per-subject maximum.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `kit/dogfood doc parity` · `build-method size` · `method carriers (every pointer declared)` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · the round-1 driver, which aborts on `08` and accepts `--highs 1` alone only if regressed · none
New arm: tools/unattended/check-unattended.test.sh · two promoting subjects over too few ids · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · authored from the round-1 closing review record.

## 10. Reuse audit

Every fix extends a seam the build already touched: `verb_review`'s validation and state gate, check
2's arm block, and the three carriers. `python tools/codebase-map/reuse_lookup.py` cannot see `.sh`
seams; the seams are the ones units 2 to 4 extended. Recall returned the cluster-C record of
aProbedUnit's closing review for the state gate's message.

Recall terms used: closing review disposition promote fold severity BLOCKER HIGH MEDIUM LOW unit rescope CONVERGED
