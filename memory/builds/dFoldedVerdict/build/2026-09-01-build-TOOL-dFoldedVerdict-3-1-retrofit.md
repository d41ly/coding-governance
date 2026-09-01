# TOOL-dFoldedVerdict-3 — four exit rows say which disposition they took, and the bar goes green

**Serves:** journal TOOL-dFoldedVerdict-3

*Node `d`, 2026-09-01, owner-present build under `memory/guides/BUILD-METHOD.md`.*

## What binds now

`bash tools/unattended/check-unattended.sh` is **GREEN over the whole tracked corpus**. It was RED on
`origin/main` for `memory/builds/dMispairedQuote/RUN.md` before this build opened, and red on
`dBriefedPass` as well from the moment `TOOL-dFoldedVerdict-2` landed the cutoff at order 3.

FOUR exit rows across TWO landed records now carry a disposition, per the owner's ruling of
2026-09-01 that the cutoff is `2026-09-01` and therefore admits both. Each record also carries a
`disposition-source:` block in its authored half stating why no verb could write those values, what
independently verifies each, and what is deliberately not reconstructed.

| record | subject | recorded | derived from |
|---|---|---|---|
| `dMispairedQuote` | `TOOL-dMispairedQuote-1` | `promote` | its spec's rev-3 log: blockers 1, 8 and 17 PROMOTED to `-3`, blocker 24 FOLDED |
| `dMispairedQuote` | `TOOL-dMispairedQuote-3` | `fold` | its spec's rev-4 log: both blockers disposed as FOLDS |
| `dBriefedPass` | `dBriefedPass-spec-set` | `fold` | three spec rev-4 logs: all three FOLD, none promoted |
| `dBriefedPass` | `dBriefedPass` | `fold` | commit `c7e9bca1`: "all four are defects in code the review was reading, so all four FOLD" |

Seven blockers across the four exits, every one accounted for. Nothing was invented to clear a gate,
which is the one outcome this unit was forbidden to produce.

## The mixed subject, and the rule that decides it

`TOOL-dMispairedQuote-1` took BOTH dispositions: three of its four standing blockers were promoted to
a new unit and one was folded into the spec. The field holds one value per subject.

It records `promote`, and the rule is now written down in
`memory/gotchas/one-value-field-records-a-mixed-outcome.md` rather than discovered again per record.
The two values are not symmetric: `promote` DEMANDS a unit id that check 2 looks for, `fold` demands
nothing. Recording the demanding value over-asks, which is visible and arguable. Recording the other
would have retired the whole exit's obligation on the strength of one blocker in four, and three real
promotions would have gone unobserved by the gate written to observe exactly them.

That class record states its own gap: **nothing gates it.** No check can see that an outcome was
mixed, because the mixedness lives in prose the field summarises. What is gated is the ABSENCE and
the illegal VALUE; neither can tell a correct one-value answer from an incorrect one.

## Grading my own predecessor

One of the two records is `dBriefedPass`, this build's immediate predecessor and my own prior run.
Its dispositions were re-derived from that build's spec revision logs and from commit `c7e9bca1`,
NOT from the `TOOL-dBriefedPass-9` backlog row that asserts both loops folded. That row says the
right thing; it is a summary of the thing being graded, and a criterion satisfied by a summary of its
own subject is the vacuity this whole build exists to remove, reproduced one level up.

## Evidence

**Evidences:** TOOL-dFoldedVerdict-3

- **AC1** — the red was reproduced at this unit's PRE-IMAGE and not at `adc0543c`, in the
  absent-disposition shape `TOOL-dFoldedVerdict-2` ships rather than the BASE shortfall message: both
  records named, four exited subjects named, no shortfall counts in the sentence. That is the
  criterion's class-and-names test, and its being unit 2's wording rather than BASE's is what proves
  order 3 had landed.
- **AC2** — all six of `dMispairedQuote`'s blockers have a recorded disposition in that build's own
  spec revision logs, corroborated at both ends: `-1`'s rev-3 names 1, 8 and 17 as promoted and 24 as
  folded, and `-3`'s rev-1 independently records being promoted from that exit carrying exactly 1, 8
  and 17.
- **AC2a** — `dBriefedPass`'s blockers likewise. The spec-set exit's three are disposed in three
  rev-4 logs, one of which states "both blockers here are document defects and FOLD rather than
  promote"; the build exit's four are disposed individually in `c7e9bca1`, whose subject line reads
  "all four blockers disposed". The backlog row was treated as corroboration and not as evidence.
- **AC3** — over the review ROWS, `dMispairedQuote` returns 1 promote and 1 fold and
  `dBriefedPass` returns 0 promote and 2 fold, summing to 2 as rev-4 pinned it — the SUM, never the
  split, so the criterion could not assert the answer AC2a had to derive. Each record carries exactly
  one `disposition-source:` line. **The criterion's bare `grep -c` does not work on these records and
  that is a defect in the criterion, not in the data:** both files carry pre-existing parked
  `decision` rows quoting the flag spelling `--disposition fold|promote`, so an unscoped grep returns
  4 and 3. The counts above are scoped to review rows, which is the population the criterion means.
- **AC4** — `bash tools/unattended/unattended.sh --status dMispairedQuote` reports the same phase,
  witness and halt code it reported before the edit. No fact key's first-match position moved: the
  provenance block's continuation lines are indented, so none of them can be read as a key.
- **AC5** — a throwaway `mktemp -d` clone seeded with a non-terminal record and driven to a
  `NON-CONVERGENT` exit by two real `--review` calls emits
  `review · item TOOL-dMispairedQuote-3 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT ·
  disposition fold`. `diff` against the hand-written tail in the tracked record reports NO
  DIFFERENCE. Byte-shape agreement with `TOOL-dFoldedVerdict-1` observed, not asserted, and against
  the shipped driver rather than the kit self-test suite.
- **AC6** — with both dispositions removed and STAGED, `check-unattended.sh` exits 1 naming
  `memory/builds/dMispairedQuote/RUN.md` under the same absent-disposition refusal. Restored by
  re-applying the two suffixes with a targeted script — NOT with `git stash`, whose stack is shared
  across worktrees, and NOT with `git checkout --`, which restores the whole file. The provenance
  block survived both directions, which the targeted restore is what guarantees.
- **AC7** — `bash tools/unattended/check-unattended.sh` exits 0 over EVERY tracked run-state record.
  This is the criterion the whole unit exists to reach and it is corpus-wide, so a sibling record the
  cutoff newly admitted would fail here rather than hide.
- **AC8** — `memory/builds/aClosedDocket/spec/…-4.md` reads `WONTDO` with
  `superseded by TOOL-dFoldedVerdict-1 TOOL-dFoldedVerdict-2 TOOL-dFoldedVerdict-3` in its tail, the
  id is still present in that build's generated units region, and hygiene is green over the flip.
- **AC9** — both of `check 24`'s arms asserted by name. The RETIRE arm is SATISFIED: exactly one
  `rescope · item retire TOOL-aClosedDocket-4` row, whose reason names `TOOL-dFoldedVerdict-3`, and
  no check-24 failure. The SUPERSESSION arm is NEVER REACHED: `grep -c -- ' -> '` over the rescope
  rows returns 0, so no successor is extracted and none is graded against another build's roster —
  which is the whole reason rev-2 changed the act from `supersede` to `retire`. The `--act supersede`
  observation was NOT made: the row is unremovable once written and the criterion routes it to a
  throwaway clone, which is work this pass did not do. Stated, not implied.
- **AC10** — `gen_build_index.py --check` and `--check-format` both exit 0.
- **AC11** — `wc -c` reports 7269 for `dMispairedQuote` and 11031 for `dBriefedPass`, both far under
  `INDEX_CAP_BYTES` of 61440 and under the 8 KB authored-region budget. The pre-edit figure for the
  second was deliberately not carried in the spec and was measured here instead.
- **AC12** — `grep -n 'records the promote value'` over
  `memory/gotchas/one-value-field-records-a-mixed-outcome.md` returns the rule's own sentence, the
  front matter carries `name` and `description` at column 0, and hygiene is green — which is what
  asserts the class declares its resolution. It declares NONE, in as many words, matching N5.
- **AC13** — `python tools/memory-tree/gotchas.py --for-paths memory/builds/dMispairedQuote/RUN.md`
  lists this class. Anchors are DERIVED from the backticked paths in the body, so this is the arm
  separating a rule written down from a rule written down WHERE THE NEXT DIFF WILL MEET IT. Without
  it a record naming no reachable path is only reported inert and the pass still looks complete.
- **AC14** — `grep -n 'TOOL-dMispairedQuote-7' memory/backlog/TOOL.md` returns ONE row naming all
  three of `TOOL-dFoldedVerdict-1`, `-2` and `-3` as what answers it, with no live successor pointer
  at the id S5 just flipped to WONTDO, and hygiene is green over the edit. Without this the backlog's
  only route from the measured defect to its fix would have named a retired unit, going stale in the
  same commit that fixed it.

## What this pass did NOT do

The `--act supersede` negative arm of AC9 was not observed. It needs a throwaway clone because the
row cannot be removed from an append-only record once written, and this pass did not build one. What
IS observed is that the shipped row reaches the RETIRE arm and never the successor arm — the positive
half of the same question.

`TOOL-dMispairedQuote-7` was repointed here rather than in `TOOL-dFoldedVerdict-2`, whose S13 also
claimed it. Unit 3's S8 claims it explicitly and says so; the explicit claim won.
