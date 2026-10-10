**Serves:** diff-review TOOL-aQuotedBrief-1 TOOL-aQuotedBrief-2 TOOL-aQuotedBrief-3

# Tier-2 closing diff review — aQuotedBrief, ROUND 2

*Round 2 of the closing review of build aQuotedBrief. It covers the round-1 fold landing on `main`
at the integration boundary. The fold clears the `skip` sentinel on its way out of the record loop in
`check_prompt_brief` (round-1 B1), adds a regression arm and raises the two assertion floors that arm
moves. Three finder lenses, one skeptic batch, one synthesis pass. Node `a`, 2026-10-09.*

Reviewed range: `cc627830097f2e88cab5e196fc301fbf1d6f1a40...5e21873863dc8d2f43a275b7a73526239d8e3eef` · ROUND 2

## Verdict: CLEAN WITH FIXES

One confirmed finding, graded low. It is a missing regression assertion and does not change
behaviour: the shipped fix in `tools/unattended/unattended.sh:3209` (`why=""; continue`) is correct
by inspection, and nothing at blocker, high or medium survived. The fix the skeptic judged sound is
a test-only edit that adds no new behaviour.

## Review shape

Intensity light, raw 1, confirmed 1, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| correctness | yes | 0 | 0 | 0 | 0 | 0 | - |
| seams | yes | 0 | 0 | 0 | 0 | 0 | - |
| verification | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |

Adjudicated tally, counted two ways. By item: 0 blocker, 0 high, 0 medium, 1 low. By raw confirmed
finding: 0 blocker, 0 high, 0 medium, 1 low (id 1). The two counts are the same because the one item
holds one finding.

### Run integrity

- Lenses: 3/3 returned, 0 died. Skeptic batches: 1/1 returned, 0 died.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 1 judged sound, 0 judged unsound, 0 with no fix proposed, 0 not judged.
- Severity on confirmed findings: 0 left ungraded by the skeptic, 1 re-graded by the skeptic (medium to low).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Intensity is **light**. The security and intent lenses were NOT run, so their bug classes were
  covered only by the checklist items shared out to the lenses that did run. This is not a full review.
- Intent: 2 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 4 items, each assigned to exactly one of 3 lenses: correctness 2, seams 1, verification 1.
- By design: none supplied, with no caller byDesign and no block.

No lens or batch died, so the counts above are complete for the lenses that ran. The zero counts
for correctness and seams are evidence only within those lenses' scope. Because security and intent
did not run, they say nothing about those two classes.

## Findings

### LOW

#### 1. The B1 regression arm cannot show rule 3 still runs when a skip record sorts last — `tools/unattended/unattended.test.sh:4275`

*Lens: verification. The finder graded it medium. The skeptic re-graded it low, and low is the
binding grade.*

**Defect.** The arm added by the fold builds its README with `readme tBr` and never calls
`roster tBr`. The `readme` fixture writes no `<!-- roster:units -->` pair, so in
`check_prompt_brief` (`tools/unattended/unattended.sh:3229-3234`) the authored roster is empty and
the rule-3 loop `for id in $roster` has nothing to iterate. The arm does reach the trailing-skip
path: `2026-10-09-prompt-tBr-1-1-build-brief.md` sorts after `2026-10-09-prompt-mandate.md`. However,
it asserts only the symptom, `preflight OK` and no check-115 text. Round-1 B1 named two halves: a
false refusal with reason `skip`, and rule 3 never running. The arm guards only the first.

**Impact.** No behaviour is affected today. Suppose a later edit handles the trailing sentinel by
returning before rule 3, for example `[ "$why" = skip ] && return 0` after the loop. This arm would
still pass. A real build whose roster unit no item plans would then be admitted whenever a build
brief sorts after its mandate, which is the most common prompt-mode layout. The existing
TOOL-aQuotedBrief-3 arm 3 tests rule 3, but with no trailing skip record, so that combination has no
regression guard.

**Fix (the skeptic judged it SOUND).** Add the trailing record to the TOOL-aQuotedBrief-3 join loop
(`for _bq_arm in 1 2 3 4 ok`, `tools/unattended/unattended.test.sh:4370`). That loop already sets
`roster tBr "1. ARCH-tBr-1 — the unit"`. After `write_brief_record`, add:

```sh
printf '# ARCH-tBr-1 — build brief\n\n- Build the widget.\n' > memory/builds/tBr/prompts/2026-10-09-prompt-tBr-1-1-build-brief.md
```

Arm 3 then proves rule 3 still fires (`rule 3, a roster unit no planned item names: ARCH-tBr-1`)
with a skip record sorting last, and arm `ok` proves a non-empty roster is still admitted. The
alternative is one new arm with `roster tBr`, a stale-only mandate and the trailing build brief,
expecting the rule-3 refusal. Either way, raise `FLOOR_ASSERTIONS` and `FLOOR_SHARD_3` by the
assertions added.

**Left-shift gate.** The class is `fold-text-is-unreviewed-surface`: a regression arm written in a
fold asserts that the reported symptom is gone, not that the behaviour the defect suppressed is back.
A predicate cannot tell which half of a finding an arm covers, so this goes in as a documented §10
check. When a fold's finding is a leaked or shared variable, its arm must exercise every consumer
of that variable with a non-empty population, and must assert at least one positive refusal from
the consumer the defect disabled, not only the absence of the false one. A partial mechanical aid
is a stage-the-break step at fold time: revert the fix to an early `return 0` past the guarded rule,
then confirm the new arm goes RED (§7, "a new gate is not landed until its failing case has been
observed").

review-shape kind=diff-review round=2 intensity=light at=synth raw=1 confirmed=1 refuted=0 unverified=0 blocker=0 high=0 medium=0 low=1 agents=5 out-tokens=18543

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | verification | tools/unattended/unattended.test.sh:4275 | medium | low | confirmed | The finding holds. The B1 arm (unattended.test.sh, about line 4272) builds its README with `readme tBr`, and that fixture writes no `<!-- roster:units -->` pair. No `roster tBr` call follows. In check_prompt_brief the roster therefore reads as empty, and the rule-3 loop `for id in $roster` never runs. The build brief `2026-10-09-prompt-tBr-1-1-build-brief.md` does sort after `2026-10-09-prompt-mandate.md` ('t' > 'm'), so the arm does exercise the trailing-skip path. However, its only assertions are `preflight OK` and no check-115 text. Suppose a later change replaced `{ why=""; continue; }` with code that skips rule 3 when the last record was a skip, for example `[ "$why" = skip ] && return 0` after the loop. The arm would still pass. The existing TOOL-aQuotedBrief-3 arm 3 tests rule 3, but with no trailing skip record. So the combination named by the prior finding, rule 3 never running, is unguarded. The shipped fix in unattended.sh:3209 is correct by inspection, so this is a missing regression assertion with no behaviour effect today. I grade it low rather than medium. | sound | fold-text-is-unreviewed-surface |
