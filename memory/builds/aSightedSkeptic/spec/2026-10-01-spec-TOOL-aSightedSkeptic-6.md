# TOOL-aSightedSkeptic-6 — one severity rubric, a skeptic's binding grade, and an uncertain verdict

**Status:** CLOSED · rev-1 · 2026-10-01 · node a · Tier-2 · base ef1dcdb6 · streams tooling · order 6 · ratified 2026-10-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-build-TOOL-aSightedSkeptic-6-1-acceptance-ledger.md](../build/2026-10-01-build-TOOL-aSightedSkeptic-6-1-acceptance-ledger.md) | journal | — |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md) | journal | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-6-2-build-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-6-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Severity drives the most expensive disposal this repo has, a BLOCKER or HIGH being promoted to a unit
of its own (`TOOL-aProbedUnit-9`), yet no prompt in the review harness defines a grade, finders choose
one freely, and a skeptic can only confirm or refute. This unit writes ONE consequence-shaped rubric
into every finder, skeptic and synthesis prompt, has the skeptic grade each confirmed finding against
it, binds the synthesis to that grade, and adds an `uncertain` verdict so a skeptic that cannot decide
a costly finding stops refuting it by default.

## 2. Scope (IN)

- **S1** — `const SEVERITY_RUBRIC` in `tools/workflows/tier2-review.template.js`, one string opening
  with the words `SEVERITY RUBRIC`, that grades by CONSEQUENCE:
  `blocker` — on a reachable path it ships a wrong result, a security hole or data loss, or a check
  that certifies what it does not check; `high` — the same consequence on a narrow or unlikely path,
  or a defect that will mislead the next change; `medium` — a real defect whose effect is contained;
  `low` — cosmetic, or a comment, with no effect on behaviour. For the spec kind each grade reads "the
  design, built as written, would ...". It closes with the rule that a grade follows the consequence,
  never the confidence or how alarming the defect looks. Observed by AC1.
- **S2** — The rubric is interpolated, byte-identical, into three prompts and nowhere restated: every
  finder prompt beside its emit instruction, every verify prompt, and the synthesis prompt. Both kinds.
  Observed by AC1.
- **S3** — `VERDICT_SCHEMA`'s item: `verdict` gains a third member, `uncertain`, and an OPTIONAL
  `severity`, enum `blocker`, `high`, `medium` and `low`, is added. `required` is unchanged. Observed
  by AC2.
- **S4** — The verify prompt, both kinds, asks the skeptic to return `severity` for each CONFIRMED
  finding, graded by the rubric against what it read, independent of the finder's bracketed grade. Its
  default rule becomes the one §8 F3 picks: a finding the FINDER graded `medium` or `low` is refuted
  when the skeptic cannot establish it, and one graded `blocker` or `high` is answered `uncertain`,
  with the reason saying what could not be established. The return line names both, and keeps the
  substring `(<n> verdicts, ids <list>)` the self-test's stub reads. Observed by AC2, AC7.
- **S5** — The BINDING grade, by a new `deriveBindingSeverity(f)`: the skeptic's `severity` on a
  confirmed verdict when it is in the closed set, else the finder's. A confirmed finding with no legal
  skeptic grade is counted UNGRADED and logged in a `WARNING:` line naming its ids; one whose two
  grades differ is counted RE-GRADED and logged in a `note:` line. Both counts join the RUN INTEGRITY
  block. The finding's own `severity` field keeps the finder's grade. Observed by AC3, AC4.
- **S6** — The synthesis prompt's CONFIRMED line shows the binding grade in the bracket, lowercase,
  keeping the `id=<n> [` opening the self-test's stub reads, followed by both grades when they
  differ. The prompt says the bracketed grade binds: each confirmed id goes in an item whose severity
  is its binding grade, an item merges findings of one binding grade only, and a different grade
  needs its reason written in the report. Observed by AC3.
- **S7** — `blockers` and `highs` stay derived from the synthesis's `items` over raw confirmed ids,
  by the existing loop, unchanged (`TOOL-dMergedTally-1`). After it, the harness compares each placed
  id's item severity with its binding grade, logs any id placed elsewhere in a `WARNING:` line, and
  returns those ids as `regraded`, an array that is empty when none moved and absent on every path
  where no synthesis ran. §8 F2. Observed by AC6.
- **S8** — `uncertain` is counted UNVERIFIED: never confirmed, never refuted, and outside precision's
  denominator. A verdict answering `uncertain` is held in the existing join, so the duplicate and
  conflict rules apply to it as to the other two members. The unverified set is every finding with
  neither a confirmed nor a refuted verdict, logged in two lines, those answered uncertain and those
  with no usable verdict. Each return carrying `unverified` carries `uncertain`, its integer subset.
  The synthesis prompt's UNVERIFIED lines say which of the two each finding is, carrying the
  skeptic's reason for an uncertain one. The success note and the RUN INTEGRITY block name the
  uncertain count apart from the no-verdict count, so a run whose skeptics all answered never reads as
  one where no skeptic returned. Observed by AC5.
- **S9** — The CONFIRMED log lines on the deferred and synthesis-death paths print the binding
  grade. Observed by AC3.
- **S10** — Seven assertions are written in `tools/workflows/tier2-review.test.sh` and not run in the
  pass, named in §7, and its assertion floor rises by seven over the value the previous unit left.
  Observed by AC8.

## 3. Non-goals (OUT)

- The finder schemas' `severity` enum. It stays the finder's grade, and the ledger reports both.
- A severity for REFUTED or UNVERIFIED findings from the skeptic. A refuted finding is not disposed,
  and an unverified one is disposed at the finder's grade by the build harness, as today.
- Counting `blockers` and `highs` from the binding grades instead of the items. §8 F2.
- Changing how `tools/workflows/unattended-build.template.js` disposes by severity. It reads
  `blockers`, `highs`, `confirmed` and `unverified`, whose meanings this unit keeps.
- The fix verdict. TOOL-aSightedSkeptic-2 owns it.
- `REVIEW_SHAPE`, the review key and the harness version. Unit 5 moves each once for the build, and
  this unit adds no input field.
- A governance carrier. The review protocol states no rubric, and none is edited (invariant 8).

### Edges

- **consumes-from** `TOOL-aSightedSkeptic-2` — `VERDICT_SCHEMA`'s item and the verify prompt as that unit leaves them, with its fix fields optional; this unit extends the same item and prompt.
- **hands-off** `TOOL-aSightedSkeptic-8` — the `ledger` row's `skepticSeverity`, which is the verdict's own grade as this unit reads it, and the verdict value it carries, uncertain among them.

## 4. Design

### Evidence

Read at `ef1dcdb6` on 2026-10-01, PINNED to that sha. Line numbers move as units 5, 1, 3, 4 and 2
land before this one; the identifiers do not.

- Both finder schemas carry `severity` as a free enum (`tools/workflows/tier2-review.template.js:253`,
  `:309`); the emit instructions (`:511-512`) list the four words and define none.
- The verify prompt (`:608-609`) ends each kind's instruction with "Default to refuted when
  uncertain", and `VERDICT_SCHEMA` (`:284`) closes `verdict` at `confirmed` and `refuted`.
- The join (`:646-654`) keeps the first verdict per id, counts agreeing repeats, and demotes
  disagreeing ones to UNVERIFIED; `unverified` (`:658`) is every finding the join holds nothing for.
- The tally (`:860-898`) counts each raw confirmed id at its synthesis item's severity, and returns
  `blockers` and `highs` null when the items do not place every confirmed id exactly once.
- The build harness disposes every confirmed and unverified finding by severity
  (`tools/workflows/unattended-build.template.js:9`), and the owner's ruling `TOOL-aProbedUnit-9`
  promotes blockers and highs to units.
- `TOOL-dMergedTally-1`'s record measured a synthesis that adjudicated 13 confirmed findings at
  blockers 1 and highs 5 against the finders' raw split of 3 and 6, so the finders' grade is not the
  one adjudication lands on.

### Data model

```
VERDICT_SCHEMA.properties.verdicts.items.properties
  id          integer                                 required (unchanged)
  verdict     'confirmed' | 'refuted' | 'uncertain'   required, NEW third member
  reason      string                                  required (unchanged)
  fixVerdict  'sound' | 'unsound' | 'none'            optional (TOOL-aSightedSkeptic-2)
  fixNote     string                                  optional (TOOL-aSightedSkeptic-2)
  severity    'blocker' | 'high' | 'medium' | 'low'   optional, NEW, read on confirmed only
```

The harness tests set membership itself, as it already does for the synthesis's severities, because
a reused file and the self-test's stubs reach it without the platform's validation.

### Return

Every return that carries `unverified` gains `uncertain`, an integer at most `unverified`. The success
return gains `regraded`, the ids the synthesis placed at a grade other than their binding one, empty
when none moved. The deferred and early returns, where no synthesis ran, carry no `regraded`, as they
carry no adjudicated count.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `SEVERITY_RUBRIC` | const string | not graded: the lexicon grades function names |
| `deriveBindingSeverity` | function, verb `derive` | `js.function` |

`deriveBindingSeverity` was asked of `python tools/lexicon/lexicon.py --suggest deriveBindingSeverity
--as js.function`, which read OK on 2026-10-01. It reads `verdictById` at call time, so it is declared
as a function and called only after the join.

### Rollout

Edit the template, regenerate the render with the parity script's `--render` mode, and commit both
together (invariant 1). The pass's direct checks are the syntax, fan-out and review-join checkers over
the render, and the greps of AC7; the seven arms are written and run once by the main loop at
VERIFYING, beside their reading against the BASE render.

### Files touched (estimate)

`tools/workflows/tier2-review.template.js` · `tools/workflows/tier2-review.js` · `tools/workflows/tier2-review.test.sh`

### Alternatives rejected

The candidates for §8 F1 and F2, and what discriminated them. Each probe READ existing records and
built no arm.

- **F1 (a), the finder's grade binds.** It loses on the `TOOL-dMergedTally-1` measurement: the one
  synthesis on record that adjudicated grades moved two of three finder blockers down, so the finders'
  grade is the one adjudication rejects, and it is the only grade never checked against the code.
- **F1 (c), the higher of the two binds.** It loses on the same measurement, and on cost: every
  disagreement promotes, so the more alarmist grader decides every promotion.
- **F2 (b), a placement off the binding grade is a tally fault.** `unattended-build.template.js`
  refuses a null `blockers`, so one re-grade the synthesis can justify halts the run's disposal.
- **F2 (c), count from the binding grades.** The report's table and the returned counts then disagree
  whenever the synthesis re-grades, which is the defect `TOOL-dMergedTally-1` closed.

## 5. Production-readiness checklist

- security — N/A: the rubric is a constant, and the new verdict fields are agent output read through
  closed sets, as the existing ones are.
- perf / scale — a rubric of a few lines added to each prompt; the agent count is untouched.
- error / empty / loading states — an absent or out-of-set skeptic grade falls back to the finder's
  and is counted; an `uncertain` verdict is outstanding and counted apart from a missing one.
- observability — the UNGRADED, RE-GRADED, uncertain and placement lines, and their RUN INTEGRITY
  clauses.
- risks — more `uncertain` answers raise `unverified`, which the build harness disposes. F3 confines
  the uncertain path to findings the finder graded blocker or high, where a wrong refutation costs a
  lost defect.
- testing — the seven arms of S10 over stub agents.
- migration — none: the new fields are optional, and a verify file written before this unit reads as
  ungraded and certain.
- user docs — N/A: no `args` field is added.

## 6. Acceptance criteria

- **AC1** — Arm `severity: one rubric reaches every finder, skeptic and synthesis prompt` passes over
  a diff-kind and a spec-kind run: each `find:` prompt, each `verify:` prompt and the `synth` prompt
  carries the text opening `SEVERITY RUBRIC`, the same bytes in all of them, naming all four grades.
  Red when: any prompt lacks it, or two prompts carry different rubric text.
- **AC2** — Arm `severity: the verdict schema carries uncertain and an optional severity` passes.
  Red when: `uncertain` is not a member of `verdict`, `severity` is absent or not the four grades, or
  `severity` joins `required`.
- **AC3** — Arm `severity: the skeptic's grade binds the synthesis line` passes: a finder grading
  `high` and a skeptic confirming at `blocker` puts `[blocker]` on that id's CONFIRMED line and names
  both grades, and a `note:` log line counts one re-graded finding.
  Red when: the bracket carries the finder's grade, or the difference is silent.
- **AC4** — Arm `severity: a confirmed verdict with no grade falls back to the finder's, counted and announced`
  passes, with the existing stub verdicts, which carry no grade: every CONFIRMED line carries the
  finder's grade, and a `WARNING:` line and the RUN INTEGRITY block both name the ungraded count.
  Red when: an ungraded finding is silent, or reaches the synthesis without a grade.
- **AC5** — Arm `severity: an uncertain verdict is counted unverified, never refuted or confirmed`
  passes: with one batch answering `uncertain`, the return's `uncertain` and `unverified` both count
  it, `confirmed` and `refuted` do not, precision excludes it, and the synthesis prompt lists it under
  UNVERIFIED with the skeptic's reason.
  Red when: an uncertain finding is scored refuted, confirmed or as no verdict at all.
- **AC6** — Arm `severity: a synthesis placing an id off its binding grade is returned in regraded`
  passes: skeptics confirming at `blocker` and the stub synthesis placing every id in one HIGH item
  return those ids in `regraded`, with `highs` counted from the items as before.
  Red when: `regraded` is empty, or `blockers` and `highs` stop being counted from the items.
- **AC7** — When `grep -c 'SEVERITY_RUBRIC' tools/workflows/tier2-review.template.js` and the same grep
  over `tools/workflows/tier2-review.js` run, both print the same count of at least 4, where BASE
  prints 0, the definition and its three interpolations; and
  `node tools/workflows/check-workflow-syntax.js tools/workflows/tier2-review.js`,
  `bash tools/workflows/check-verifier-fanout.sh` and `bash tools/workflows/check-review-join.sh`
  each exit 0. Arm `severity: the uncertain rule follows the finder's grade` passes: every verify
  prompt names `uncertain` for a finding graded blocker or high and keeps refuted as the default for
  medium or low.
  Red when: the render was not regenerated, the edit broke the parse, the fan-out grammar or the id
  join, or the default rule is unchanged.
- **AC8** — When `grep -c "severity:" tools/workflows/tier2-review.test.sh` runs it prints at least 7
  more than at BASE, and the file's `FLOOR_ASSERTIONS` value is seven above the value the previous
  unit left. Red when: an arm is missing or the floor did not move.
  permission: a pass runs no suite; the arms of AC1 to AC7 are read from the main loop's VERIFYING run,
  which also reads them RED against the BASE render, as the build README's rule requires.

## 7. Gates

`tier2-review self-test` · `workflow script syntax` · `verifier fan-out` · `verifier fan-out self-test` · `review-join ban (no ref-keyed join)` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `unattended-build self-test` · `lexicon naming predicates` · `memory hygiene`

New arm: tools/workflows/tier2-review.test.sh · stub skeptics returning a grade, no grade, a grade off the finder's, and `uncertain`, and a stub synthesis placing ids off their binding grade · FLOOR_ASSERTIONS rises by 7

## 8. Open questions

- **F1 — Which grade binds the synthesis when finder and skeptic disagree?** (a) The finder's, the
  skeptic's shown beside it. (b) The skeptic's, falling back to the finder's when the skeptic gave
  none. (c) The higher of the two. (d) Neither: the synthesis decides with both shown. §4 Alternatives
  rejected records why (a) and (c) lose; (d) is today's unrubricked adjudication with one more number
  beside it. (b) binds the one grade made against the rubric by the agent that read the code to
  confirm the finding. Recommendation (b).
  RESOLVED (agent, 2026-10-01, delegated): (b), the most feature-rich survivor after M3's vetoes.
- **F2 — How do `blockers` and `highs` stay derived over raw confirmed ids once a grade binds?** (a)
  From the items as today, with the binding grade instructed, each placement checked against it, and
  an id placed elsewhere logged and returned in `regraded`. (b) A placement off the binding grade is a
  tally fault, both counts null. (c) Counted from the binding grades, the items' severities ignored.
  §4 Alternatives rejected records why (b) and (c) lose. Recommendation (a).
  RESOLVED (agent, 2026-10-01, delegated): (a); (c) falls to veto 1 on `TOOL-dMergedTally-1`'s rule
  that the report's table and the returned counts agree.
- **F3 — Does "default to refuted when uncertain" stay, and for which findings?** (a) It goes:
  `uncertain` for every finding a skeptic cannot decide. (b) It stays for findings the finder graded
  medium or low, and one graded blocker or high is answered `uncertain`. (c) It stays for every
  finding, and `uncertain` is only for a skeptic that could not read the code. Under (a), the noise of
  a low-precision run, measured at 0.13 to 0.40 on small or hardened diffs, becomes outstanding
  findings the build harness must dispose. Under (c), an unsure skeptic still refutes a real blocker,
  which is the loss this verdict exists to stop. Recommendation (b).
  RESOLVED (agent, 2026-10-01, delegated): (b), the survivor meeting both the shared brief's
  `uncertain` row and the precision floor the review protocol states.

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft, from the build's shared spec brief, the run mandate's finding 6,
  and the harness template read at `ef1dcdb6`.

## 10. Reuse audit

The probe, run on 2026-10-01:

```
python tools/codebase-map/reuse_lookup.py "one shared definition of finding severity blocker high medium low"
```

It ranked name-stem neighbours only (`find_block`, `ratchet_findings`, `build_lang_mode_findings`) and
the run-gates and backlog seams, none of which grades a finding. No existing seam fits: the harness
spells the four grades in its finder schemas, its synthesis schema and its tally, and defines none of
them. The seam this unit extends is the harness's own verify stage and tally in
`tools/workflows/tier2-review.template.js`: `VERDICT_SCHEMA`, the `verdictById` join, the synthesis
prompt, and the `TOOL-dMergedTally-1` loop it leaves unchanged. The recall probe found the owner's
disposal ruling `TOOL-aProbedUnit-9` and the `TOOL-dMergedTally-1` measurement, both cited in §4; no
record had defined a grade.

Recall terms used: severity BLOCKER HIGH MEDIUM LOW rubric skeptic synthesis items blockers highs promoted folded disposal tier2-review

The question passed with them: "what defines blocker high medium low severity for a review finding,
and which grade drives promotion".
