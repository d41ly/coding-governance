# TOOL-aSightedSkeptic-2 — the skeptic judges each finding's proposed fix as well as its claim

**Status:** CLOSED · rev-1 · 2026-10-01 · node a · Tier-2 · base ef1dcdb6 · streams tooling · order 5 · ratified 2026-10-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-build-TOOL-aSightedSkeptic-2-1-acceptance-ledger.md](../build/2026-10-01-build-TOOL-aSightedSkeptic-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md) | journal | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-2-2-build-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-2-2-build-brief.md) | journal | — |
| [2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md](../reviews/2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md) | diff-review | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 |

<!-- /gen:spec-records -->

## 1. Goal

A finder's proposed `fix` reaches the synthesis and the fold with no agent ever judging it, and in the
sampled fold rounds about half the confirmed findings were defects the previous round's fix
introduced. This unit has the skeptic return a `fixVerdict` and a `fixNote` beside each verdict, so the
report carries a corrected fix wherever the finder's would introduce a defect, and so a fix nobody
judged is counted and announced rather than passed on as if it had been.

## 2. Scope (IN)

- **S1** — `VERDICT_SCHEMA`'s item in `tools/workflows/tier2-review.template.js` gains two OPTIONAL
  properties: `fixVerdict`, a string enum of `sound`, `unsound` and `none`, and `fixNote`, a string.
  Neither joins `required`, so a skeptic that omits them degrades to "unjudged" and never fails its
  batch into regeneration. `id` stays the only join key. Observed by AC2, AC7.
- **S2** — The verify prompt, both kinds, shows each finding's `fix` on its line, after its impact, and
  tells the skeptic to judge the fix as a second, separate question: `sound` when applying it cures
  the defect and introduces none the skeptic can see in the code or spec it touches; `unsound` when it
  does not cure the defect, breaks a caller, an invariant or a sibling path, or introduces a defect
  of its own; `none` when no fix was proposed. For `unsound` the `fixNote` says why and gives the
  corrected fix when the skeptic has one. The prompt states that the fix verdict never changes the
  claim's verdict. The return line names both fields, and keeps the substring
  `(<n> verdicts, ids <list>)` the self-test's stub reads ids from. Observed by AC1.
- **S3** — Disposition is unchanged by a fix verdict (§8 F1). A confirmed finding with an `unsound`
  fix stays CONFIRMED at its grade. The synthesis prompt's CONFIRMED line carries the fix through a new
  `renderFixLine(f)`: for `sound` the finder's fix marked judged sound; for `unsound` the finder's fix
  marked REJECTED with the skeptic's `fixNote` as the corrected fix; for `none` that no fix was
  proposed; and, absent a legal `fixVerdict`, the finder's fix marked NOT JUDGED. The synthesis is
  told to write the corrected fix, never the rejected one, into the report, and where an unsound
  fix's note gives no correction, to say the fix is still to be designed. Observed by AC3, AC4.
- **S4** — A confirmed finding whose verdict carries no `fixVerdict` in the closed set is counted
  UNJUDGED. The count is logged as a `WARNING:` line naming the ids, and the synthesis prompt's RUN
  INTEGRITY block gains one clause stating how many confirmed fixes were judged sound, judged
  unsound, had none proposed, and went unjudged, with the sentence that an unjudged fix is the
  finder's proposal and nothing more. Observed by AC5.
- **S5** — The skeptic batch's reuse print, `batchPrints`, is taken over each finding's id, claim AND
  fix, so a verify file judged against one fix is never reused for a finding carrying another under
  the same claim. Observed by AC6.
- **S6** — The synthesis-death log lines, which print each CONFIRMED finding's fix today, print it
  through `renderFixLine` too, so the log a re-run reads does not hand on a rejected fix as the fix.
  Observed by AC3.
- **S7** — Six assertions are written in `tools/workflows/tier2-review.test.sh` and not run in the
  pass, named in §7, and its assertion floor rises by six over the value the previous unit left.
  Observed by AC8.

## 3. Non-goals (OUT)

- Changing a finding's verdict, severity or disposition because its fix is unsound. §8 F1.
- A return field for fix counts. The per-finding fix verdict reaches a caller through unit 8's
  ledger; this unit returns nothing new.
- The skeptic's own severity grade and the `uncertain` verdict. Both are TOOL-aSightedSkeptic-6.
- Judging the fixes of REFUTED findings. The skeptic may return a fix verdict for one; the harness
  reads it for confirmed findings only, since a refuted finding's fix is never applied.
- `REVIEW_SHAPE` and the review key. Invariant 5 of the shared brief: unit 5 bumps the shape once for
  the build, and this unit adds no input field, so `inputPrint` is untouched.
- The harness version. Unit 5 moves it once for the build.
- BUILD-METHOD M8's invocation block and the review protocol, which do not describe the verdict
  schema; no governance carrier is edited (invariant 8).
- The kit README. This unit adds no `args` field, which is what that README documents.

### Edges

- **consumes-from** `TOOL-aSightedSkeptic-5` — the build's one `REVIEW_SHAPE` bump, which is what keeps a verify file written by the old prompts from being reused under these.
- **hands-off** `TOOL-aSightedSkeptic-6` — the same `VERDICT_SCHEMA` item and verify prompt, extended next with the skeptic's grade and the `uncertain` verdict; both units' fields stay optional.
- **hands-off** `TOOL-aSightedSkeptic-8` — carrying `fixVerdict` per finding in the `ledger`, and, where a confirmed finding's fix was judged unsound, the skeptic's corrected fix as the fix that `confirmedFindings` hands the next round.

## 4. Design

### Evidence

Read at `ef1dcdb6` on 2026-10-01, PINNED to that sha. Line numbers move as units 5, 1, 3 and 4 land
before this one; the identifiers do not.

- `VERDICT_SCHEMA` (`tools/workflows/tier2-review.template.js:270`) holds `id`, `verdict` and
  `reason`, all required, and nothing about a fix.
- The verify prompt (`:607-619`) renders each finding as
  `id=<n> [<severity>] <ref> — <claim> | impact: <impact>`. The `fix` is not shown.
- The synthesis prompt's CONFIRMED lines (`:729-736`) print `fix: ${f.fix}` with no judgement, and
  the synthesis-death log (`:908-909`) prints the same field.
- `batchPrints` (`:589`) fingerprints `[id, claim]` per finding.
- The self-test's `buildVerdicts` stub reads ids from the prompt with `/ids ([0-9, ]+)\)/` and
  returns `{id, verdict, reason}` only; `buildSynth` splits the prompt on `UNVERIFIED findings` and
  reads `id=(\d+) \[`. S2 and S3 keep both spellings.
- The motivating measure is in the run mandate: 23 of 45 sampled later-round findings were defects
  introduced by a previous round's fix. The dHonouredPark round-3 record says five of its seven
  defects were introduced by round 2's fold.

### Data model

```
VERDICT_SCHEMA.properties.verdicts.items.properties
  id          integer                          required (unchanged)
  verdict     'confirmed' | 'refuted'          required (unit 6 adds a third member)
  reason      string                           required (unchanged)
  fixVerdict  'sound' | 'unsound' | 'none'     optional, NEW
  fixNote     string                           optional, NEW
```

A verdict whose `fixVerdict` is absent or outside the set is read as unjudged. The schema's enum
refuses an out-of-set value from a live agent; the harness tests membership again because a reused
file and the self-test's stubs reach it without the platform's validation.

### Counting

Over `confirmed` only, after the existing join, four counts: sound, unsound, none, unjudged. They sum
to `confirmed.length`. Unjudged above zero logs
`WARNING: <n> confirmed finding(s) carry a fix no skeptic judged — ids <list>`. The RUN INTEGRITY
clause reads `fixes on confirmed findings: <s> judged sound, <u> judged UNSOUND, <x> none proposed,
<j> NOT JUDGED`, followed by the sentence that an unjudged fix is the finder's proposal only.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `renderFixLine` | function, verb `render` | `js.function` |

Asked of `python tools/lexicon/lexicon.py --suggest renderFixLine --as js.function`, which read OK on
2026-10-01. It reads `verdictById` at call time, so it is declared as a function and called only after
the join.

### Rollout

Edit the template, regenerate the render with the parity script's `--render` mode, and commit both
together (invariant 1). The pass's direct checks are the syntax, fan-out and review-join checkers over
the render, and the greps of AC7; the six arms are written and run once by the main loop at
VERIFYING, beside their reading against the BASE render.

### Files touched (estimate)

`tools/workflows/tier2-review.template.js` · `tools/workflows/tier2-review.js` · `tools/workflows/tier2-review.test.sh`

### Alternatives rejected

The candidates for §8 F1, and the probe that discriminated them. A probe READS: it measured existing
review records and built no arm.

- **(b) An unsound fix demotes the finding to UNVERIFIED.** What would make it lose: a record where a
  finding whose fix later introduced a defect was itself a real defect. The dHonouredPark round-3
  record is one. Round 2's findings there were fixed, and the fixes introduced five of round 3's seven
  defects. Under (b) every one of those real round-2 defects leaves the confirmed set and its run
  reads PARTIAL. Rejected: it trades a bad fix for a lost defect.
- **(c) An unsound fix is raised as a finding of its own.** It needs a second id space for findings the
  skeptic raises, which the orchestrator-assigned integer join (`TOOL-aFoldedQuarry-2`) has no slot
  for, and it double-counts one defect in `blockers` and `highs`. Rejected under veto 1: it fails the
  shared brief's rule that `id` stays the only join key.

## 5. Production-readiness checklist

- security — the fix text is untrusted output of another agent, already interpolated into the
  synthesis prompt today; this unit adds the skeptic's note beside it and nothing that executes it.
- perf / scale — one more short field per finding in each skeptic prompt and return; the verifier
  count is untouched.
- error / empty / loading states — an absent or out-of-set fix verdict is unjudged, counted and
  announced; an unsound verdict with an empty note says the fix is still to be designed.
- observability — the `WARNING:` line and the RUN INTEGRITY clause of S4.
- risks — a skeptic may judge a correct fix unsound. The finder's fix stays in the report, marked
  rejected, beside the correction, so the folder sees both.
- testing — the six arms of S7 over stub agents.
- migration — none: both fields are optional, and a verify file written before this unit reads as
  unjudged.
- user docs — N/A: no `args` field is added, and the verdict schema is documented in the harness's own
  comments.

## 6. Acceptance criteria

- **AC1** — Arm `fix verdict: every verify prompt shows each finding's fix and asks for fixVerdict` passes,
  over one diff-kind and one spec-kind run. Red when: either kind's verify prompt lacks a finding's
  fix text, or names neither `sound` nor `unsound`.
- **AC2** — Arm `fix verdict: the verdict schema carries fixVerdict and fixNote, neither required` passes.
  Red when: either property is absent, the enum is not exactly sound, unsound and none, or either
  joins `required`.
- **AC3** — Arm `fix verdict: an unsound fix reaches the synthesis as the correction, the finding still confirmed`
  passes: with skeptics returning `confirmed` and `unsound` with a note, the synthesis prompt carries
  the note and the word REJECTED on that finding's line inside the CONFIRMED section, and the return's
  `confirmed` count equals the BASE run's.
  Red when: the note is missing, the finder's fix is presented unmarked, or the finding left the
  confirmed set.
- **AC4** — Arm `fix verdict: an unsound fix with no correction is still to be designed` passes.
  Red when: an empty `fixNote` renders the finder's fix as the fix.
- **AC5** — Arm `fix verdict: an unjudged fix is counted, logged and named in RUN INTEGRITY` passes:
  with the existing stub verdicts, which carry no fix verdict, a log line opens `WARNING:` and names
  the unjudged ids, and the synthesis prompt carries `NOT JUDGED` in its RUN INTEGRITY block.
  Red when: an unjudged fix is silent in either place.
- **AC6** — Arm `fix verdict: a verify file judged over another fix is dispatched` passes: a verify
  file carrying the print a run with the same ids and claims but another fix produced is not reused.
  Red when: `batchPrints` ignores the fix.
- **AC7** — When `grep -c 'fixVerdict' tools/workflows/tier2-review.template.js` and the same grep over
  `tools/workflows/tier2-review.js` run, both print the same count of at least 3, where BASE prints
  0; and `node tools/workflows/check-workflow-syntax.js tools/workflows/tier2-review.js`,
  `bash tools/workflows/check-verifier-fanout.sh` and `bash tools/workflows/check-review-join.sh`
  each exit 0. Red when: the render was not regenerated, or the edit broke the parse, the fan-out
  grammar or the id join.
- **AC8** — When `grep -c "fix verdict:" tools/workflows/tier2-review.test.sh` runs it prints at least
  6, where BASE prints 0, and the file's `FLOOR_ASSERTIONS` value is six above the value the previous
  unit left. Red when: an arm is missing or the floor did not move.
  permission: a pass runs no suite; the arms of AC1 to AC6 are read from the main loop's VERIFYING run,
  which also reads them RED against the BASE render, as the build README's rule requires.

## 7. Gates

`tier2-review self-test` · `workflow script syntax` · `verifier fan-out` · `verifier fan-out self-test` · `review-join ban (no ref-keyed join)` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `unattended-build self-test` · `lexicon naming predicates` · `memory hygiene`

New arm: tools/workflows/tier2-review.test.sh · stub skeptics returning `unsound` with and without a note, stub verdicts with no fix verdict, and a verify file printed over another fix · FLOOR_ASSERTIONS rises by 6

## 8. Open questions

- **F1 — Does an unsound fix change the finding's disposition, or only the fix text?** (a) Fix text
  only: the finding stays confirmed at its grade, and the report carries the skeptic's correction with
  the finder's fix marked rejected. (b) An unsound fix demotes the finding to unverified. (c) An
  unsound fix is raised as a finding of its own. §4 Alternatives rejected records the probe: (b) loses
  real defects, as the dHonouredPark round-2 findings show, and (c) breaks the integer join and
  double-counts. (a) keeps every confirmed defect and stops the rejected fix reaching the fold, which is
  where the measured harm was. Recommendation (a).
  RESOLVED (agent, 2026-10-01, delegated): (a), the most feature-rich survivor after M3's vetoes; (c)
  falls to veto 1 on the shared brief's join rule.
- **F2 — Is the fix judged by the same skeptic in the same batch, or by a second skeptic stage?** (a)
  The same batch, as a second question per finding. (b) A second stage after the verify stage, over
  confirmed findings only. (b) spends up to five more agents per review, against the review protocol's
  verify-stage total, and the cap is a governance constant this build may not move. Recommendation (a).
  RESOLVED (agent, 2026-10-01, delegated): (a); (b) falls to veto 2, since it needs the fan-out total
  raised in a governance carrier.

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft, from the build's shared spec brief, the run mandate's finding 1,
  and the harness template read at `ef1dcdb6`.

## 10. Reuse audit

The probe, run on 2026-10-01:

```
python tools/codebase-map/reuse_lookup.py "a skeptic judges whether a finding's proposed fix is sound"
```

It ranked `tier2-review.js` under the review-harnesses dossier as the one seam naming a skeptic, and
otherwise name-stem neighbours (`ratchet_findings`, `find_block`) that judge nothing. The seam this
unit extends is the harness's own verify stage: `VERDICT_SCHEMA`, the verify prompt, the `verdictById`
join and the synthesis prompt in `tools/workflows/tier2-review.template.js`. No existing seam judges a
proposed fix; the recall probe found no record that decided the question, only review records that
measured fold-introduced defects, which §4 cites.

Recall terms used: skeptic verdict fix fold round tier2-review VERDICT_SCHEMA priorFindings confirmed refuted synthesis introduced defect

The question passed with them: "has any review harness ever judged a proposed fix, or recorded that
fold-round fixes introduce new defects".
