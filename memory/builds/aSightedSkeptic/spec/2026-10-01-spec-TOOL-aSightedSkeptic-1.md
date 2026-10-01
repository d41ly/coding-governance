# TOOL-aSightedSkeptic-1 — the skeptic is briefed with the repo, the range, the context and the by-design list

**Status:** CLOSED · rev-1 · 2026-10-01 · node a · Tier-2 · base ef1dcdb6 · streams tooling · order 2 · ratified 2026-10-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-build-TOOL-aSightedSkeptic-1-1-acceptance-ledger.md](../build/2026-10-01-build-TOOL-aSightedSkeptic-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-01-build-TOOL-aSightedSkeptic-1-runlog-54774e91.md](../build/2026-10-01-build-TOOL-aSightedSkeptic-1-runlog-54774e91.md) | journal | TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 TOOL-aSightedSkeptic-10 |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-1-0-run-mandate.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-1-0-run-mandate.md) | journal | — |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md) | journal | TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-1-2-build-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-1-2-build-brief.md) | journal | — |
| [2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md](../reviews/2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md) | diff-review | TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 |

<!-- /gen:spec-records -->

## 1. Goal

The skeptic prompt of `tools/workflows/tier2-review.template.js` names no repository, no range, no
context and no by-design list, so a skeptic reads whatever checkout its working directory is, cannot
tell a defect the diff introduced from one that was already there, and is told that "by-design"
refutes without being shown what is. This unit moves the context lines the finder prompt already
carries into one function, `renderBrief(role)`, opens both the finder and the skeptic prompt with it,
and tells the skeptic of a diff review to refute a pre-existing defect and anything the by-design
list covers.

## 2. Scope (IN)

- **S1** — One function, `renderBrief(role)`, with `role` `'finder'` or `'skeptic'`, returns the
  context block both prompts open with: the `REPO:` line, the subject (the diff command for a diff
  review, every subject path at its pinned blob for a spec audit), `CONTEXT:`, `REVIEW ROUND:` with
  its fold sentence, `BY DESIGN`, and the prior round's findings. It is declared after `diffCmd` and
  before `phase('Find')`, and reads the resolved shas at call time. Observed by AC2, AC6.
- **S2** — The finder prompt opens with `renderBrief('finder')`. The lines it carried itself for
  context, round, by-design and prior findings now come from the brief alone, and its lens-specific
  text follows: the role sentence, the spec kind's blob comparison, `LENS:`, the emission rule, the
  durability instruction and the return shape, each as today. Observed by AC2, AC5.
- **S3** — The skeptic prompt opens with `renderBrief('skeptic')`, ahead of its role sentence and
  the findings to judge. Observed by AC1, AC4, AC5.
- **S4** — Wording differs by role on two lines only. `BY DESIGN` reads "do NOT re-report these" for
  a finder and "refute any finding one of these covers" for a skeptic. The prior-findings block
  reads "judge the FIX, and do not re-raise the original" for a finder, and for a skeptic says a
  finding that re-raises one of those originals, rather than a defect in its fix, is refuted as a
  duplicate. Observed by AC3, AC5.
- **S5** — For a diff review only, the skeptic brief carries a `SCOPE:` line: a finding is in scope
  only if the diff introduced its defect or made it reachable, and a defect present unchanged at
  the base is PRE-EXISTING and refuted. It names how to check, `git -C <repo> show <base sha>:<path>`,
  over the resolved base. The spec kind carries no such line. Observed by AC3.
- **S6** — The review key does not change. This unit's prompt change rides the build's one
  `REVIEW_SHAPE` bump, made by `TOOL-aSightedSkeptic-5`. Observed by AC7.
- **S7** — The render `tools/workflows/tier2-review.js` is regenerated from the template by the
  parity gate's render mode and lands in the same commit; the harness version is not moved again.
  Observed by AC8.
- **S8** — The arms of §7 are added to the tier2-review self-test, and its `FLOOR_ASSERTIONS` is
  raised by exactly the assertions they add. Observed by AC9.

## 3. Non-goals (OUT)

- `TOOL-aProbedUnit-16`, no scratch root handed to review agents. It is ADJACENT: it would add one
  more line to the same brief, and it is a different defect with its own filed ask. Not in scope.
- The intent block and `args.specs`. That unit extends `renderBrief(role)`; this one leaves it
  holding what the finder prompt carries at BASE and the `SCOPE:` line.
- The skeptic's judgement of a proposed fix, its severity grade and the `uncertain` verdict. Those
  units edit the skeptic's role sentence, its per-finding lines and its return shape, all of which
  sit after the brief.
- The synthesis prompt. It already names the range and the context, and the pinned interface says
  the brief opens finder and skeptic prompts only.
- The drift-audit siblings. Their `COMMON` block is a separate pipeline with its own inputs.
- Governance carriers. BUILD-METHOD M8 and the review protocol describe the skeptic stage without
  saying what it is briefed with, and stay correct after this change, so nothing is parked.

### Edges

- **consumes-from** `TOOL-aSightedSkeptic-5` — the build's one `REVIEW_SHAPE` bump, which keeps a lens or verify file written by the old prompts from being reused under these.
- **hands-off** `TOOL-aSightedSkeptic-3` — the INTENT block joins `renderBrief(role)`, reaching finders and skeptics through the one function.
- **hands-off** external — `TOOL-aProbedUnit-16`, the scratch-root sentence, left to that build's own unit.

## 4. Design

### Evidence

Read at `ef1dcdb6` on 2026-10-01, PINNED to that date. Unit 5 lands first and moves the line numbers,
not these facts.

- The finder prompt is built at lines 489-518 of the template. Its context lines are 499-508:
  `CONTEXT:`, `REVIEW ROUND:` with a per-kind fold sentence, `BY DESIGN (do NOT re-report these):`,
  and either the prior findings with the "Judge the FIX" instruction or the first-round line.
- The skeptic prompt is built at lines 607-619. It opens "You are an adversarial skeptic", then the
  findings and the durability and return instructions. It interpolates none of `repo`, `diffCmd`,
  `context`, `byDesign`, `round` or `priorFindings`, and it tells the skeptic to refute "by-design"
  findings without naming any.
- `diffCmd` is line 461, built from `baseSha` and `headSha` after the resume probe. Both thunks run
  after it, so a function that reads it at call time sees the resolved values.
- The self-test's stub skeptic finds its batch ids with the first match of `/ids ([0-9, ]+)\)/` in
  the prompt. Nothing the brief renders from the suite's fixtures matches that pattern; the build
  pass keeps it that way.

### Data model

`renderBrief(role)` returns one string; the diff kind, as a finder sees it at round 1:

```
REPO: <repo> — run every git command as `git -C <repo> …`; every path below is relative to it.
SUBJECT: the diff `git -C <repo> diff <base sha>...<head sha>`.
CONTEXT: <context>
REVIEW ROUND: 1
BY DESIGN (do NOT re-report these): <byDesign>
PRIOR ROUND'S FINDINGS: none - this is a first-round review of the whole diff.
```

The spec kind's `SUBJECT:` line lists each subject as `  - <path>  blob <blob>`. The skeptic's
version swaps the two role-worded lines S4 names and, for the diff kind only, adds:

```
SCOPE: a finding is in scope only if this diff introduced its defect or made it reachable. A defect
present unchanged at the base is PRE-EXISTING: refute it. Check with `git -C <repo> show <base sha>:<path>`.
```

The fold sentence of `REVIEW ROUND:` is today's per-kind text, shared by both roles because it
states a fact about the subject and not an instruction.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `renderBrief` | function | `js.function`, camel; `python tools/lexicon/lexicon.py --suggest renderBrief --as js.function` answered OK on 2026-10-01: it leads with `render`, "turn structure into text" |

### Rollout

The pass edits the template, adds the arms, then regenerates the render with the parity gate's
render mode, `bash tools/workflows/check-protocol-parity.test.sh --render`. Both land in one commit.

### Files touched (estimate)

`tools/workflows/tier2-review.template.js` · `tools/workflows/tier2-review.js` ·
`tools/workflows/tier2-review.test.sh`

### Alternatives rejected

- **A `COMMON` string constant, the drift-audit siblings' shape.** Read at
  `tools/workflows/drift-audit-code.template.js:91`: it is evaluated once from inputs known at the
  top of the script. Here the subject line needs the probe's resolved shas and the wording differs
  by role, so a constant would need two copies and a late declaration. A function is one copy.
- **Copying the finder's context lines into the skeptic prompt.** Two spellings of one block is the
  drift the pinned interface exists to prevent, and a third unit is about to extend it.
- **The refute rules in the skeptic's role sentence.** Rejected in §8 F1.

## 5. Production-readiness checklist

- security — no new input: every value the brief renders is already interpolated into a finder
  prompt at BASE. The skeptic now reads a named repository instead of its working directory, which
  narrows what it can confuse for the subject.
- perf / scale — each skeptic prompt grows by the brief, a few hundred bytes plus the prior-findings
  list; a fold round with many prior findings pays that list once per batch, at most five batches.
- error / empty / loading states — an absent `byDesign` renders today's `none supplied`; no prior
  findings renders the first-round line, as the finder sees it today.
- observability — none added; the change is in what agents read, which the self-test's stubs record.
- risks — a skeptic that now refutes PRE-EXISTING defects lowers the confirmed count of a fold round.
  That is the intended effect: those defects were not introduced by the fold. A defect the diff made
  reachable without editing its line stays in scope by S5's wording.
- testing — the arms of §7, run once at VERIFYING; the direct checks of §6 in the pass.
- migration — none; no argument is added and the key is unchanged.
- user docs — N/A: no argument is added, and the kit README documents arguments.

## 6. Acceptance criteria

- **AC1** — When the tier2-review self-test runs at VERIFYING, its arm
  `a skeptic prompt carries the repo, the range, the context and the by-design list` passes: a diff
  run with `context: 'CTX-MARK'` and `byDesign: 'BD-MARK'` produces `verify:` prompts that each
  carry `REPO: /tmp/r`, the diff command over the resolved shas, `CTX-MARK` and `BD-MARK`.
  Red when: the arm runs against the BASE render, whose skeptic prompt carries none of the four.
  permission: the suite runs once, at VERIFYING, by the main loop; the RED-first observation is the
  main loop's, running the final suite in a frozen clone at this unit's parent commit.
- **AC2** — When the self-test runs at VERIFYING, its arm
  `every finder and skeptic prompt opens with the shared brief` passes: on a diff run and on a spec
  run, every `find:` and every `verify:` prompt begins with `REPO: /tmp/r`, and the `CONTEXT:` line
  is byte-identical across all of them within a run.
  Red when: either prompt kind is assembled without `renderBrief`, which is the skeptic at BASE.
  permission: as AC1.
- **AC3** — When the self-test runs at VERIFYING, its arm
  `a diff skeptic is told to refute a pre-existing defect and a by-design one` passes: every diff
  `verify:` prompt carries `PRE-EXISTING` and `refute any finding one of these covers`, while no
  `find:` prompt and no spec-audit `verify:` prompt carries `PRE-EXISTING`.
  Red when: the rule is missing, which is BASE, or it leaks into a finder or the spec kind.
  permission: as AC1.
- **AC4** — When the self-test runs at VERIFYING, its arm
  `a spec-audit skeptic prompt names the repo and every subject at its blob` passes: each spec-run
  `verify:` prompt carries `/tmp/r`, `s.md` and `abc1234`.
  Red when: the spec skeptic is not briefed, which is BASE.
  permission: as AC1.
- **AC5** — When the self-test runs at VERIFYING, its arm
  `a fold-round skeptic is shown the prior round's findings` passes: a round-2 diff run with
  `priorFindings: [{ ref: 'p.js:9', claim: 'PRIOR-MARK' }]` produces `verify:` prompts that carry
  `PRIOR-MARK` and the word `duplicate`, and `find:` prompts that carry `PRIOR-MARK` and
  `Judge the FIX`.
  Red when: the skeptic is not shown the prior findings, which is BASE, or a finder loses them.
  permission: as AC1.
- **AC6** — When `grep -c "^function renderBrief(role)" tools/workflows/tier2-review.template.js`
  runs it prints 1, and `grep -c "renderBrief('finder')"` and `grep -c "renderBrief('skeptic')"`
  over the same file each print at least 1, where BASE prints 0 for all three.
  Red when: the block is spelled twice instead of called, or a prompt kind does not call it.
- **AC7** — When `git diff HEAD~1 -U0 -- tools/workflows/tier2-review.template.js | grep -cE "inputPrint|deriveReviewKey|REVIEW_SHAPE"`
  runs on this unit's build commit it prints 0, and at VERIFYING the self-test's existing arms
  beginning `AC3` pass unchanged.
  Red when: this unit touched the key derivation, which invariant 5 of the shared spec brief
  reserves to `TOOL-aSightedSkeptic-5`.
- **AC8** — When `bash tools/workflows/check-verifier-fanout.sh`,
  `bash tools/workflows/check-review-join.sh` and `node tools/workflows/check-workflow-syntax.js`
  each exit 0, and
  `sed "s/{{FANOUT_CAP}}/5/g" tools/workflows/tier2-review.template.js | diff - tools/workflows/tier2-review.js`
  prints nothing.
  Red when: the brief reshaped a fan receiver, broke the parse, or the render was not regenerated.
  figure: 5 is DERIVED, the value `bash tools/workflows/check-verifier-fanout.sh --print-cap` prints
  in this repository; re-read it before the observation.
- **AC9** — When the self-test runs at VERIFYING, its summary line reports at least its raised
  `FLOOR_ASSERTIONS`, and `grep -c "FLOOR_ASSERTIONS=" tools/workflows/tier2-review.test.sh` prints 1.
  Red when: an added arm is stranded past an early exit, so the count falls under the floor.
  figure: the new floor is DERIVED by the pass, counted off the arms it adds, and stated in the
  commit's `Decided:` trailer.
  permission: as AC1.

## 7. Gates

`tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `unattended-build self-test` · `verifier fan-out` · `review-protocol parity (kit vs dogfood)` · `review-join ban (no ref-keyed join)` · `workflow script syntax` · `lexicon naming predicates`

New arm: tools/workflows/tier2-review.test.sh · `a skeptic prompt carries the repo, the range, the context and the by-design list`, staged by the BASE render · FLOOR_ASSERTIONS raised by the count added
New arm: tools/workflows/tier2-review.test.sh · `every finder and skeptic prompt opens with the shared brief` · as above
New arm: tools/workflows/tier2-review.test.sh · `a diff skeptic is told to refute a pre-existing defect and a by-design one` · as above
New arm: tools/workflows/tier2-review.test.sh · `a spec-audit skeptic prompt names the repo and every subject at its blob` · as above
New arm: tools/workflows/tier2-review.test.sh · `a fold-round skeptic is shown the prior round's findings` · as above

## 8. Open questions

- **F1 — Where do the skeptic's refute rules live?** (a) Inside `renderBrief('skeptic')`, as the
  role-worded `BY DESIGN` and prior-findings lines and the `SCOPE:` line. (b) In the skeptic's own
  role sentence after the brief. Two later units of this build rewrite that role sentence and its
  return lines, so (b) puts the rules where the next edit lands, and it separates each rule from the
  context it refers to. Recommendation (a). RESOLVED (agent, 2026-10-01, delegated): (a), the
  option that leaves fewer follow-ups for the units ordered after this one, M3's rule.
- **F2 — Does a spec-audit skeptic get the pre-existing rule?** (a) No: a spec audit has no range,
  its subject is the whole document at a pinned blob, and nothing marks a line as older than the
  review. (b) Yes, read against the previous rev. (b) needs a base the spec kind does not carry and
  `args` does not supply, which is a new input this unit was not asked for. Recommendation (a).
  RESOLVED (agent, 2026-10-01, delegated): (a); (b) needs a new `args` field, a public surface
  this unit was not priced for, which is M3's veto 2.
- **F3 — Is the synthesis prompt opened with the brief too?** (a) No, finder and skeptic only, as the
  pinned interface states. (b) Yes, for uniformity. The synthesis already names the range and the
  context, and (b) would put a by-design list in front of the one agent told to read every
  outstanding finding itself. Recommendation (a). RESOLVED (agent, 2026-10-01, delegated): (a), the
  pinned interface; (b) fails it.

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft, from the owner's mandate, the shared spec brief, and the
  template and its self-test read at `ef1dcdb6`.

## 10. Reuse audit

The probe, run on 2026-10-01:

```
python tools/codebase-map/reuse_lookup.py "a shared context block prepended to every reviewer and skeptic prompt"
```

It ranked `target_context` in `tools/govkit/govkit.py`, two runlog review derivations and the
review protocol guide, and reported `.sh` as an unscanned layer. None renders a prompt, so outside
the edited file no existing seam fits; the `reuse_lookup.py` result is that answer, recorded. The seam
extended is the finder prompt's own context lines in `tools/workflows/tier2-review.template.js`,
lifted into a function rather than copied. The nearest prior art is the `COMMON` block of
`tools/workflows/drift-audit-code.template.js`, one string prepended to every lens brief, which
TOOL-aScouredKit-36 extended and which recorded that this harness composes its briefs differently;
§4 says why its constant form does not fit here. The recall hits confirm the gap is recorded only in
this build's own mandate, and no decision record chose a blind skeptic.

Recall terms used: tier2-review skeptic verify prompt repo range context byDesign priorFindings pre-existing refute COMMON brief

The question passed with them: "why does the tier2 review skeptic prompt carry no repo, range,
context or by-design list, and how is a pre-existing defect told from one the diff introduced".
