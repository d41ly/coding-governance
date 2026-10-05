**Serves:** spec-audit TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-13 TOOL-aEvidencedLens-14

# aEvidencedLens — spec audit of the three promoted units, round 1

*Node `a`, 2026-10-05. A Tier-2 adversarial pass over the three specs promoted from the first
audit's findings: five finder lenses, a skeptic stage prompted to refute each finding, and one
synthesis. Findings are graded by consequence under the run's severity rubric.*

**Round: 1.** Range reviewed: the three subjects below, each pinned at the blob it was read at, plus the tree they cite.

- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md@4da93f761ffc422c8bb752fb6a91593994fba25c`
- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-12.md@ff3688d87ffc61905e8d395ea995f409cc7e17e5`
- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-14.md@4f1c9467aa5b0e3fe16867377f6762e40cd12345`

## Verdict: CLEAN WITH FIXES

No blocker was confirmed. One high defect was confirmed, found independently by three lenses. Unit
13's masked comparison cannot pass on a correct build, because the diff-kind `resume:probe` prompt
carries `inputPrint` and not the full review key, so masking `result.key` leaves the REVIEW_SHAPE
move standing. That is the same class as the first audit's finding 25, which this unit was promoted
to close. Below it sit thirteen mediums in seven items and one low.

Three more defects were each found three times. Unit 13 says no later unit edits the review harness,
yet unit 12 does, at order 7. Unit 12's AC3 and unit 14's AC3 each describe a fixture that the code
they test cannot produce. Every fix below is a spec edit; none needs a design change.

## Review shape

- Intensity full. Raw 18, confirmed 17, refuted 1, unverified 0 (0 uncertain). Precision 0.94.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 4 | 3 | 1 | 0 | 0 | 0.75 |
| failure-envelope | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |

- Adjudicated tally by item: 0 BLOCKER, 1 HIGH, 7 MEDIUM, 1 LOW, which is 9 items.
- Adjudicated tally by raw confirmed finding: 0 blockers, 3 highs, 13 mediums, 1 low, which is 17.
- Refuted and dropped: id 10, a duplicate of id 9. Its reason is in the appendix.

## Run integrity

- Lenses 5/5 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to
  unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 16 judged sound, 1 judged UNSOUND (id 3), 0 none proposed, 0 NOT
  JUDGED. For the unsound fix this report carries the skeptic's corrected fix only.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 2 RE-GRADED by the skeptic (id 13,
  medium to low; id 15, high to medium). The bracketed grade is binding and is the grade used below.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: 12 spec documents were supplied as `specs`, as sibling context.
- Checklist: 32 items, each assigned to exactly one of the 5 lenses (coherence 7, grounding 7,
  reuse 6, blast-radius 6, failure-envelope 6).
- Move check: no checked subject moved.

Every counter that this run must report as zero is zero, so the run is complete in the sense the
harness defines.

The run's duplicate count of 0 counts only what the harness merged. Four defects were each found by
three lenses: ids 1, 5 and 14; ids 4, 6 and 9; ids 2, 7 and 15; and ids 3, 8 and 16. Each set
shares one binding grade and sits in one item below, and one fix discharges it.

## HIGH

### H1 — unit 13's mask leaves `inputPrint` standing in `resume:probe` (ids 1, 5, 14)

- Where: `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md`, section 2
  S2 and S3, section 4 "The masked comparison", section 6 AC1 and AC2.
- Defect: the diff-kind `resume:probe` prompt never contains `result.key`. It spells the key as a
  template, `<the first 12 hex of the base sha>-<the first 12 hex of the head sha>-${inputPrint}`
  (`tools/workflows/tier2-review.template.js:719-720` at HEAD, line 634 at BASE). `inputPrint`
  hashes REVIEW_SHAPE, which is `lenses5-r1` at BASE and `lenses5-r2` at HEAD. So
  `text.split(result.key).join('<KEY>')` masks nothing in that prompt, and the probe differs between
  BASE and HEAD outside every `<KEY>`. AC1 is red on a correct build, and AC2's "every differing
  byte range lies where the masked run wrote `<KEY>`" is false. Section 4's claim that this mask is
  unit 1 AC5's mask does not hold either: unit 1 AC5 compares only `find:`, `verify:` and `synth`.
- Consequence: the only way to turn the red green is to make `inputPrint` equal again, which means
  reverting unit 1's REVIEW_SHAPE move. That is the hazard this unit exists to remove.
- Fix (judged sound, all three): mask the CLASS, meaning every value derived from REVIEW_SHAPE.
  Replace each run's `result.key` and its `inputPrint`, the key's last `-`-separated field, with
  `<KEY>`, replacing the full key first. State in S2, S3 and the section 4 pseudocode that the
  diff-kind `resume:probe` carries `inputPrint` and not the full key. Restate AC2 as "every
  difference lies where a masked key or print token sat", and have a red the mask leaves standing
  name its label and value. The alternative, judged sound for id 1, is to drop `resume:probe` from
  the BASE comparison and say why; it loses the probe half of the invariant, so prefer the mask.
- Left-shift: a spec-audit checklist item for every masked comparison: list each prompt label
  compared, and for each one show the masked value appears in it verbatim. A mask justified by one
  label's shape is the could-not-pass class.

## MEDIUM

### M1 — unit 13's last non-goal is false: unit 12 edits the harness after it (ids 4, 6, 9)

- Where: `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md`, section 3
  Non-goals last bullet, section 3 Edges, section 1 ("the tree after unit 6"), section 2 S2.
- Defect: unit 13 is order 6 and says of later units "None of them edits the review harness". Unit
  12 is order 7 (README gen:build-order step 7), and its Files touched name
  `tools/workflows/tier2-review.template.js`, `tier2-review.js` and `tier2-review.test.sh`. Unit
  13's own section 3 names unit 12 as moving prompts. Unit 12's order moved from 4 to 7 in its rev-2,
  which made this sentence false.
- Consequence: the one cumulative BASE observation stops one harness unit short of the shipped tree.
  Unit 12's AC2 still compares its own diff-kind prompts against its pass-start render, so the
  residual gap is a move made by a fold commit or merge after step 6. Unit 13's own Alternatives
  names exactly that gap.
- Fix (judged sound): order unit 13 after unit 12 (order 8), add a consumes-from edge to
  TOOL-aEvidencedLens-12, and observe through the last harness unit, updating the title and the S2
  "after TOOL-aEvidencedLens-6" wording. The alternative is to keep order 6, replace the false
  sentence with one naming unit 12 as a later harness edit covered only by its own AC2, and rerun
  AC1 to AC3 at the close. Either way, delete "None of them edits the review harness" and name in S2
  and AC1 the last harness-editing unit the observation covers.
- Left-shift: a build-order lint that, for any spec claiming "no unit ordered after this one edits
  X", greps the Files touched of every later-ordered spec for X and reds on a hit. Reorders are what
  falsify such claims, so the check belongs where `gen:build-order` is rendered.

### M2 — unit 12 AC3 plants its pipe in a column the appendix does not render (ids 2, 7, 15)

- Where: `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-12.md`, section 6
  AC3, with S1 and S3 "Observed by AC3", and the section 3 sentence about "a claim" forging a row.
- Defect: AC3 expects the synth appendix row to carry the confirmed finding's `claim` `a | b` as
  `a \| b`. `renderAppendix`'s columns are id, lens, ref, severity, skepticSeverity, verdict, reason
  and fixVerdict (template :1280), and the comment at :1279 says `claim` rides the ledger only. No
  claim bytes reach any row.
- Consequence: AC3 is red or vacuous on a correct build, so the criterion meant to prove the pipe
  escape survives the renderCell refactor observes nothing. A builder chasing it may add a claim
  column, which moves the frozen appendix bytes and breaks the eight-column table
  `review_replay.py` parses. The effect is contained: the existing suite arm at
  `tools/workflows/tier2-review.test.sh:1191-1202` plants a pipe in the skeptic reason, so a dropped
  escape is still caught at VERIFYING.
- Fix (judged sound): carry `a | b` and a line break in a field the appendix renders through
  renderCell, the stub skeptic's `reason` (for example `a | b\nc`). Expect that cell to read
  `a \| b c` on one line, byte-identical to the row under `pre-u12.js`. Stage one break, a
  renderCell that skips the pipe escape, and observe AC3 red on it. Correct section 3's "a claim" to
  the rendered field.
- Left-shift: a spec-audit checklist item: every AC that plants a value in a rendered table names a
  column that renderer emits, checked against the renderer's column list.

### M3 — unit 14 AC3's "excluded merge commit" is not something the walk produces (ids 3, 8, 16)

- Where: `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-14.md`, section 6
  AC3 and the third section 7 New arm line.
- Defect: `read_run_exclusions` prints the non-run PARENT at each two-parent commit and walks on
  through the merge (`tools/unattended/lib-unattended.sh:1334-1373`). `read_run_commits` runs
  `rev-list end ^base ^tip` (:1038-1048), so the merge commit itself always stays in the run's list.
  AC3's "the run commit raising the bound is one read_run_exclusions removes, a merge of the default
  branch into the run" describes a commit the walk cannot remove.
- Consequence: built with the raise in the merge commit, an evil merge differing from both parents,
  the correct leg names it and AC3 reds a correct build. Built with the raise on the excluded side,
  it is AC1's owner-commit fixture again and adds no class. A builder who makes the literal arm pass
  by dropping merge commits from the walk lets a run hide a REVIEW_ROUNDS raise in its own merge,
  which is the owner-held bound unit 9 exists to protect.
- Fix: the finder's fix for id 3 was judged UNSOUND, so only the skeptic's correction is written
  here. Drop AC3 and the third `round walk:` arm, and say that AC1 covers a raise on a merge's
  excluded side; lower AC5's count to at least 2. If an evil-merge keep case is wanted, add it as an
  arm whose red is a staged break, a walk that excludes the merge commit itself. Then amend the
  section 6 preamble and the section 5 testing line so that this arm alone is not required to be red
  against the pass-start leg, because a kept evil merge is named by the pass-start leg too.
  The fixes for ids 8 and 16 were judged sound and agree with this. Id 8 adds the same keep arm (an
  evil run merge must still fail check 19 after the walk), and the preamble amendment above is what
  makes it buildable. Id 16 offers, as an alternative to dropping the arm, a raise on a second,
  distinct default-branch merge in one range, and asks the spec to state that a merge commit's own
  write, settled against every parent, is a run write the walk keeps.
- Left-shift: a spec-audit checklist item for any fixture phrased in a helper's vocabulary ("an
  excluded X"): quote the helper's output contract beside it and confirm X is a member of what it
  emits.

### M4 — unit 13 never requires the two renders' label sets to be equal (id 17)

- Where: `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md`, section 4
  "The masked comparison" and section 6 AC1.
- Defect: the pseudocode maps prompts to `{label: text}` and compares "over labels". AC1 asks only
  for byte identity of "every" prompt and a floor of five `find:` labels per arg set. A driver that
  iterates one side's labels passes when the other adds or drops a `verify:` batch or the
  `resume:probe`.
- Consequence: a diff-kind prompt that appears or disappears between BASE and the observed tree is a
  move under shared invariant 2, and the comparison would certify no such move happened. The miss
  needs a one-sided driver, and the effect is confined to this unit's observation.
- Fix (judged sound): in section 4 and AC1, require the label sets of the two runs to be equal per
  arg set, report a label present on one side only red by name, and print both label counts.
- Left-shift: a reusable comparison helper in the harness's test kit that refuses unequal key sets
  before comparing values, so no hand-written driver can iterate one side.

### M5 — unit 12's `-` envelope misses blank evidence (id 18)

- Where: `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-12.md`, section 2
  S1 and section 5 error / empty / loading states.
- Defect: `renderPromptLine` maps only absent, null and `''` to `-`. Evidence of `'\n'` renders as a
  space and `'  '` renders unchanged. The schema allows both (`evidence: { type: 'string' }`, no
  minLength, template :478), and unit 3's skeptic rule at :1078 keys on the literal `-`.
- Consequence: for a finding whose finder returned blank evidence, the skeptic gets no signal that
  evidence is missing and may confirm on the finder's word, the case unit 3's rule exists to stop.
- Fix (judged sound): make `renderPromptLine` return `-` when the folded value, trimmed, is empty,
  and add a one-line evidence case (`'\n'`) to the S4 arm that must read `| evidence: -`. Because
  renderCell composes the same function, a whitespace-only appendix cell moves from blank to `-`.
  Record that as a deliberate change: amend section 4's "renderCell's output is unchanged for every
  input" and note or exclude the case in AC3. `review_replay.py` strips cells (:105, :150), so it
  will read `-` where it read an empty string.
- Left-shift: an arm in `tier2-review.test.sh` that feeds every rendered evidence or cell function
  the whitespace-only class (`' '`, `'\n'`, `'\r\n'`) and asserts `-`.

### M6 — unit 12 omits the symbols.json regen and the map leg (id 11)

- Where: `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-12.md`, section 4
  Files touched and section 7.
- Defect: adding `renderPromptLine` to `tier2-review.template.js` and `tier2-review.js` adds two
  entries to `memory/map/generated/symbols.json`, which the unguarded `codebase-map coverage +
  freshness` leg byte-compares. Section 4 omits the file and section 7 omits the leg. Unit 6 hit the
  same omission and needed a second dispatch for it.
- Consequence: a pass staging only the declared paths reds the map leg, or costs a second dispatch.
  No wrong result ships.
- Fix (judged sound): add `memory/map/generated/symbols.json` to section 4 Files touched as a regen
  in the same commit, add `codebase-map coverage + freshness` to section 7, and add an AC that
  `grep -c '"renderPromptLine"' memory/map/generated/symbols.json` prints 2.
- Left-shift: a spec lint that reds a spec whose Files touched names a file inventoried in
  `symbols.json` and whose section 4 introduces a new function, unless `symbols.json` is also listed.

### M7 — unit 13's acceptance ledger has no path check 23 reads (id 12)

- Where: `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md`, section 2
  S4, section 4 Files touched, section 6 AC4.
- Defect: the ledger is placed only "in the build folder" and "in memory/builds/aEvidencedLens/".
  Check 23 reads only `builds/*/build/*.md` and `reviews/*.md`
  (`tools/memory-tree/check-memory-hygiene.sh:2607`), and check 4 admits a loose recording-named
  file at a build root, so a root-level ledger passes check 4 and is invisible to check 23. Section 4
  also says the pass writes the ledger "and nothing else", but a new record serving this unit moves
  the README's gen:build-index Records line and this spec's gen:spec-records table.
- Consequence: this Tier-2 unit's criteria read as unevidenced at close, or the dispatch check reds
  on undeclared generated writes. Either costs a cycle; no wrong result ships.
- Fix (judged sound): in S4 and AC4, name the path
  `memory/builds/aEvidencedLens/build/<date>-build-TOOL-aEvidencedLens-13-<seq>-acceptance-ledger.md`,
  carrying `**Serves:** journal TOOL-aEvidencedLens-13` and an `**Evidences:** TOOL-aEvidencedLens-13`
  block. Change section 4 to list that file plus the regenerated `README.md` and this spec's
  gen:spec-records region as the dispatch write set.
- Left-shift: make check 4 refuse a recording-named file at a build root whose name carries
  `acceptance-ledger`, pointing at the `build/` folder, so the invisible case becomes a red.

## LOW

### L1 — unit 13 S1 rebinds "the pass's base" in every brief (id 13)

- Where: `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md`, section 2
  S1, the sentence "The pass's base means the pass-start render wherever a build brief of this build
  spells it".
- Defect: all 14 briefs use "against the pass's base" in their refusal-observation line, which is
  about the checker or driver under change. Only briefs 1, 2, 3, 4 and 6 use "a render taken at the
  pass's base". S1's unscoped sentence rebinds the phrase in briefs 7 to 11 and 14 to a `git show` of
  `tier2-review.js`, a fixture unrelated to their subjects.
- Grade: the finder graded medium; the skeptic re-graded it low and that grade binds. A builder will
  most likely read past the ambiguity, so the effect is wording only.
- Fix (judged sound): scope the sentence to the render-comparison phrase only: "a render taken at
  the pass's base", in the briefs of units 1, 2, 3, 4 and 6, means the pass-start render. Add that
  "against the pass's base" in a brief's refusal-observation line keeps meaning the pass-start HEAD
  of the file under change.
- Left-shift: a spec-audit checklist item: a sentence that defines a term "wherever" it appears must
  name the carriers, checked by grepping the phrase across the build's briefs and specs.

## Left-shift summary

The highest-value class here is a comparison or fixture whose shape was reasoned from one instance
and never checked against the code it observes: a mask taken from three labels and applied to a
fourth (H1), a planted value in a column that is not rendered (M2), a fixture in a helper's
vocabulary the helper never emits (M3). One checklist item covers all three: for every AC fixture,
quote the line of code that produces or consumes the planted value, at the cited sha. The second
class is a claim about other units that a reorder falsified (M1), which a build-order lint can gate
mechanically. The two dispatch-set omissions (M6, M7) are the repeat of a class the build already
hit at unit 6; a spec lint joining Files touched against the generated artifacts they move would
retire it.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md:section 2 S2, section 4 The masked comparison, section 6 AC1 and AC2 | high | high | confirmed | Re-probed tools/workflows/tier2-review.template.js at HEAD 14850417e. :697-698 deriveReviewKey returns `${kind}-r${round}-${pair}-${inputPrint}`. The diff-kind probe at :719-720 spells `${kind}-r${round}-<the first 12 hex of the base sha>-<the first 12 hex of the head sha>-${inputPrint}`, so result.key never appears in the resume:probe prompt and splitting on it masks nothing there. HEAD :687 is REVIEW_SHAPE = 'lenses5-r2'; `git show 028b5cac:...template.js` prints 609:REVIEW_SHAPE = 'lenses5-r1', and its inputPrint at :614 hashes shape. The HEAD print adds probeRules and prevBlobs only on the spec kind or when a prevBlob exists, so for the diff args the two prints differ only by shape, yet they do differ. resume:probe therefore differs between BASE and HEAD outside every <KEY>. Spec 13 S2 and AC1 include resume:probe, and AC2 requires every difference to lie under <KEY>. Both are red on a correct build, and the only way to turn them green is to undo unit 1's shape move. | sound |
| 2 | coherence | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-12.md:section 6 AC3 | medium | medium | confirmed | Re-read template :1280. renderAppendix cols = ['id','lens','ref','severity','skepticSeverity','verdict','reason','fixVerdict'], and the comment at :1279 says `claim` rides the ledger only. The ledger at :1247-1260 carries claim, and renderAppendix never reads it. The synth prompt embeds only that appendix text (:1509-1512). A claim of `a \| b` therefore never reaches an appendix row, so AC3 of spec 12 cannot observe `a \\| b` there: it is either red or vacuous on a correct build. Adding a claim column to satisfy it would move the appendix bytes that S3 freezes and change the 8-column table review_replay.py parses. | sound |
| 3 | coherence | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-14.md:section 6 AC3, section 7 third New arm | medium | medium | confirmed | Re-read tools/unattended/lib-unattended.sh:1334-1373. At a two-parent commit read_run_exclusions prints the non-run parent and descends the run side, and read_run_commits (:1038-1048) runs `rev-list end ^base ^tip`. That keeps the merge commit itself, which is not reachable from the excluded parent. No merge commit is ever removed. Unit 9 spec :36 and :102 say a merge taking one side's value wrote nothing. A raise 'in an excluded merge commit', as the third arm puts it, is one of two things. As an evil merge it stays in the walked list and is correctly named, so AC3 reds a correct build. As a raise on the excluded default-branch side it is AC1's fixture again. AC3's own wording ('the run commit raising the bound is one read_run_exclusions removes') describes a run commit the walk cannot remove. The fix's first option is unsound because a kept evil merge is named by the pass-start leg too, unwalked. Its arm therefore cannot be observed RED against the pass-start leg, as the section 6 preamble and section 5 testing line require. | unsound |
| 4 | coherence | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md:section 3 last bullet (Comparing renders of units ordered after this one) | medium | medium | confirmed | The status headers put unit 13 at order 6 and unit 12 at order 7. README gen:build-order step 7 lists TOOL-aEvidencedLens-12. Spec 12 S1, S5 and its Files touched edit tools/workflows/tier2-review.template.js and its render. Spec 13 section 3 says of units ordered after it 'None of them edits the review harness', and is false for unit 12. The effect is contained: unit 12's own AC2 compares every diff-kind prompt against pre-u12.js. A move made by a fold commit or a merge after step 6 still goes unobserved by any BASE comparison, which is the gap spec 13's own Alternatives names. | sound |
| 5 | grounding | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md:section 2 S2 and S3, section 4 'The masked comparison', section 6 AC1 and AC2 | high | high | confirmed | Re-probed. tools/workflows/tier2-review.template.js:718-720 (HEAD) builds the diff-kind probe's step 3 as the literal `${kind}-r${round}-<the first 12 hex of the base sha>-<the first 12 hex of the head sha>-${inputPrint}`, and the same is true at BASE (git show 028b5cac:...template.js line 634). That literal is not result.key, so text.split(key) cannot mask it. inputPrint hashes REVIEW_SHAPE: BASE has 'lenses5-r1' (git show 028b5cac:tools/workflows/tier2-review.js line 609) and HEAD has 'lenses5-r2' (both files, line 687). The probe line therefore differs. I diffed the probe-prompt source between BASE (620-645) and HEAD (700-729). On the diff branch the only changes are spec-branch text and that inputPrint-bearing literal, so the masked resume:probe compare is red on a correct build. Unit 1's AC5 (spec -1.md:240-243) names find:, verify: and synth only, never resume:probe. So the section 4 claim that 'this unit's mask is that AC5's' does not cover the probe. AC2's 'only where <KEY> sat' is false for the same reason. Graded high: the AC reds on a correct tree, and that pushes a builder toward reverting the REVIEW_SHAPE move. | sound |
| 6 | grounding | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md:section 3 Non-goals, last bullet; section 1 ('the tree after unit 6'); section 3 Edges | medium | medium | confirmed | Re-probed. Unit 12's status line reads 'order 7', and unit 13's reads 'order 6'. The README gen:build-order puts TOOL-aEvidencedLens-12 at step 7, after step 6, which holds TOOL-aEvidencedLens-13. Unit 12's Files touched (-12.md:101) names tools/workflows/tier2-review.template.js, tier2-review.js and tier2-review.test.sh. So the non-goal 'None of them edits the review harness' (-13.md:56) is false, and the BASE observation stops short of the shipped harness. Graded medium rather than high, because unit 12's own AC2 (-12.md:141-147) compares every diff-kind resume:probe, find:, verify: and synth prompt against its pass-start render. Only a move made between passes falls outside both checks, and that gap is contained. | sound |
| 7 | grounding | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-12.md:section 6 AC3 (and S1/S3 'Observed by AC3') | medium | medium | confirmed | Re-probed. tools/workflows/tier2-review.template.js:1279-1282 at HEAD carries the comment '`claim` rides the ledger only (spec F4)'. Its cols are ['id','lens','ref','severity','skepticSeverity','verdict','reason','fixVerdict'] with no claim column. The appendix is the only table in the synth prompt (lines 1506-1512). Unit 12's AC3 (-12.md:148-151) expects the synth appendix row to carry a confirmed finding's claim as `a \| b` with its pipe backslash-escaped. No claim bytes reach any row, so AC3 can never observe the pipe escape it guards. The fix moves the payload into `reason`, which renderCell renders, and adds a staged break. That cures the defect without adding a column that review_replay.py's eight-column parse would choke on. | sound |
| 8 | grounding | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-14.md:section 6 AC3, section 7 third New arm line | medium | medium | confirmed | Re-probed. In tools/unattended/lib-unattended.sh:1366-1374, read_run_exclusions prints a PARENT (_re_p2 or _re_p1) at each two-parent commit and walks on through the merge, never printing the merge itself. read_run_commits (:1038-1048) is rev-list end ^base ^tips, which keeps the merge commit in the run's list. The unit-14 arm (-14.md:150) says 'a run raise in an excluded merge commit', and AC3 (-14.md:132-134) speaks of a run commit that 'read_run_exclusions removes, a merge of the default branch into the run'. Neither describes anything the walk does. A commit the walk really removes sits on the non-run parent's side, which is AC1's owner-commit case. The proposed counter-arm is valid: unit 9's round scan settles a merge as a write when its value differs from EVERY parent (-9.md:34-36, 192-194), matching scan_grant_writes' --cc settle (check-unattended.sh:1635-1656). So an evil run merge must still red. Graded medium: the effect is a fixture that cannot be built as worded, and it is contained. | sound |
| 9 | reuse | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md:section 3 Non-goals, last bullet (with section 2 S2 and the section 1 Goal) | medium | medium | confirmed | git show 4da93f76 (spec 13): line 3 'order 6', line 53 'Units 1 to 4 and 12 move the spec kind's prompts by design', line 56 'Comparing renders of units ordered after this one. None of them edits the review harness.' git show ff3688d8 (spec 12): line 3 'order 7'; S1/S5 and section 4 Files touched edit tools/workflows/tier2-review.template.js and tier2-review.js; rev-2 log says the order moved from 4 to 7, which is what made unit 13's sentence false. README gen:build-order puts unit 13 at step 6 and unit 12 at step 7. A grep for tier2-review across the order-7 and order-8 specs printed 0 for unit 14 and 2 or 3 mentions for units 8 and 11, which are out-of-scope or doc mentions. So the one BASE comparison stops before a harness edit the build ships. That edit has only a per-pass, predecessor-anchored AC2 (12 AC2's fixture line says 'not to BASE'). Unit 13's own Alternatives rejected names this as the gap: a move made between passes, by a fold commit or a merge, is missed. Graded medium: unit 12 AC2 still covers its own diff-kind prompts, so the residual exposure is post-step-6 fold or merge moves plus a false non-goal that misleads the reader. Durability note: the Write to C:/projects/coding-governance/.git/review-lenses/... was refused by the harness as outside the session worktree, so this copy is in the scratchpad. | sound |
| 10 | blast-radius | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md:section 3, last non-goal; section 3 Edges; section 1 | high | - | refuted | duplicate of id=9. It makes the same claim on the same lines: spec 13 :56's non-goal is false because unit 12, at order 7, edits tier2-review.template.js and its render. It names the same consequence, unit 12 and later fold commits escaping the cumulative BASE comparison. I re-observed it: README build-order has step 6 for unit 13 and step 7 for unit 12, and spec 12's section 4 lists the tier2-review files. Its extra point, that the Edges rationale is untrue for the post-unit-6 render, is the same defect. The proposed fix of reordering after unit 12, or adding a final masked BASE comparison at VERIFYING, would cure it. | sound |
| 11 | blast-radius | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-12.md:section 4 Files touched; section 7 | medium | medium | confirmed | grep of memory/map/generated/symbols.json printed renderCell at :6481 for tier2-review.js and at :6486 for tier2-review.template.js. Function symbols of both files are therefore inventoried, and a new renderPromptLine adds two entries. tools/codebase-map/test_codebase_map.py:237 declares ('symbol', 'all_symbols', 'symbols.json', 'render_symbols_json') for the freshness byte-compare. gate-legs.json carries 'codebase-map coverage + freshness' with subject repo and no guard. git show --stat eb3980f2e (unit 6) lists memory/map/generated/symbols.json +30. Its trailer reads 'Decided: declare memory/map/generated/symbols.json at a second dispatch — the map gate requires the regen of the three new function symbols in this commit'. Spec 12's section 4 Files touched names only the three tier2-review files, and section 7 omits the codebase-map leg, so a pass staging only the declared paths reds that leg or needs a second dispatch. The effect is contained: a red bar or an extra dispatch, with no wrong result shipped. | sound |
| 12 | blast-radius | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md:section 2 S4; section 4 Files touched; section 6 AC4 | medium | medium | confirmed | Spec 13 at blob 4da93f76 places the ledger only 'in the build folder' at :44 and :94, and 'in memory/builds/aEvidencedLens/' at :140. It never names the build/ subfolder. tools/memory-tree/check-memory-hygiene.sh:2607 reads only git ls-files "$M/builds/*/build/*.md" "$M/builds/*/reviews/*.md". memory/HYGIENE.md:178-180 admits a 'loose recording-named .md' at a build root, so a root-level ledger passes check 4 and is invisible to check 23. ls memory/builds/aEvidencedLens/ printed README.md RUN.md prompts reviews spec, so build/ does not exist yet. Prior ledgers follow the build/<date>-build-<id>-<seq>-acceptance-ledger.md shape, for example memory/builds/*/build/2026-09-13-build-TOOL-aBatchedArm-3-1-acceptance-ledger.md. Section 4 says the pass writes the ledger 'and nothing else'. Yet README.md:96 'Records: 17 bound to this build, across 3 record folder(s)' and spec 13's gen:spec-records table at :5-11 are generated from the record set, and both move when a record serving unit 13 lands. The build brief says to stage only --dispatch paths. The consequence is contained: check 23 or the dispatch check reds and costs a cycle. It does not ship a wrong result. | sound |
| 13 | blast-radius | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md:section 2 S1, the sentence 'The pass's base means the pass-start render wherever a build brief of this build spells it' | medium | low | confirmed | Re-probed: grep -c "against the pass's base" prompts/*.md prints 1 for all 14 build briefs (units 1-14). grep -l "render taken at the pass's base" matches only briefs 1, 2, 3, 4 and 6. Brief 14 line 19 reads 'Observe every new refusal or gate clause RED on a staged break against the pass's base'. Spec 7 line 187 reads 'observed against the driver at the pass's base'. Spec 13 S1's sentence '"The pass's base" means the pass-start render wherever a build brief of this build spells it' is unscoped, and 'pass-start render' is defined two lines earlier as the git show of tools/workflows/tier2-review.js. Read literally, it rebinds the refusal-observation phrase in briefs 7-11 and 14 to a fixture unrelated to their subject. The consequence is a wording ambiguity a builder will most likely read past, so it is graded low. | sound |
| 14 | failure-envelope | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md:section 2 S2, section 4 The masked comparison, section 6 AC1 and AC2 | high | high | confirmed | Re-read tools/workflows/tier2-review.template.js:719-720. On the diff kind, the resume:probe prompt spells the directory as `${kind}-r${round}-<the first 12 hex of the base sha>-<the first 12 hex of the head sha>-${inputPrint}`, so it never contains result.key. git show 028b5cac:tools/workflows/tier2-review.js shows REVIEW_SHAPE = 'lenses5-r1' with the same template at :634. HEAD has 'lenses5-r2' at :687 and the template at :720. inputPrint hashes REVIEW_SHAPE (:696), so it differs between BASE and HEAD and survives text.split(key).join('<KEY>'). Built as written, spec 13 S2 and AC1 compare resume:probe and go red on a correct build. AC2's 'every differing byte range lies where the masked run wrote <KEY>' fails for the same reason. That is the finding-25 defect this unit exists to close, and a builder chasing the red may revert unit 1's shape move. | sound |
| 15 | failure-envelope | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-12.md:section 6 AC3 (and S3) | high | medium | confirmed | Re-read tools/workflows/tier2-review.template.js:1277-1282. The appendix columns are id, lens, ref, severity, skepticSeverity, verdict, reason and fixVerdict, and the comment there says `claim` rides the ledger only. At BASE renderCell is called only from renderAppendix, so a pipe in a confirmed finding's claim never reaches renderCell. Spec 12 AC3 is therefore vacuous: the row it compares carries no pipe and would match pre-u12.js even with the escape dropped. Spec 12 section 3 also wrongly says the escape keeps 'a claim' from forging a row. The impact is contained. The existing suite arm at tools/workflows/tier2-review.test.sh:1191-1202 plants 'x \| y\r\nz' in the skeptic reason and asserts 'x \\\| y z' plus 9 unescaped pipes per row, and spec 12 section 7 names the 'tier2-review self-test' gate. So a dropped escape is still caught at VERIFYING, just not by AC3. | sound |
| 16 | failure-envelope | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-14.md:section 6 AC3 and the third section 7 New arm line | medium | medium | confirmed | Re-read tools/unattended/lib-unattended.sh:1038-1048. read_run_commits runs `rev-list end ^base ^tip...`, with each exclusion as a parent tip. At :1306-1312, read_run_exclusions prints the non-run PARENT of each two-parent commit and walks down the run side. A merge commit is never excluded and always stays in the run's list. Unit 9 spec lines 34-36 and 102 settle a merge against every parent, so a merge that keeps one side's value writes nothing, and a resolution that differs from both is a run write. Spec 14 AC3 asks for 'the run commit raising the bound [to be] one read_run_exclusions removes, a merge of the default branch into the run', and its section 7 arm says 'a run raise in an excluded merge commit'. That is self-contradictory. A raise in the merge itself is kept and correctly named. A raise on the excluded side is a default-branch commit, which AC1 already covers. A literal build reds a correct leg, or turns the arm into a duplicate of AC1. | sound |
| 17 | failure-envelope | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md:section 4 The masked comparison and section 6 AC1 | medium | medium | confirmed | Read spec 13 blob 4da93f76 at section 4 'The masked comparison' and section 6 AC1. The pseudocode builds prompts{label: text} per render and says 'compare BASE vs HEAD over labels resume:probe, find:*, verify:*'. AC1 requires that 'every' such prompt be byte-identical, and the only count it asks for is 'the number of labels compared, at least the five find: labels of each arg set'. Nothing states that the two renders' label SETS must be equal, or that a label present on one side only must red. A driver that iterates one side's keys satisfies AC1 as written while a verify batch or resume:probe added or dropped on the other side goes unseen. The finder's probe output, labelsA 11 and labelsB 11, was not re-run here because it writes scratch renders. It shows only that equality holds today and does not refute the gap. Severity medium: the miss needs a driver that iterates one side, and the effect is confined to this unit's observation. | sound |
| 18 | failure-envelope | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-12.md:section 2 S1 and section 5 error / empty / loading states | medium | medium | confirmed | Spec 12 blob ff3688d8, S1 (lines 27-29) and the section 4 fold (lines 82-84), maps only null, undefined and '' to '-'. Any other value is String(v) with line-break runs folded to one space, so evidence of '\n' renders as ' ' and evidence of '  ' renders unchanged, never as '-'. The schema at tools/workflows/tier2-review.template.js:478 is `evidence: { type: 'string' }`, with no minLength and no trim. The skeptic rule at :1078 keys on the literal '-' ('Evidence that reads `-` was not recorded'). Section 5's claim that 'absent evidence still reads `-`' therefore misses blank evidence. The same envelope exists in renderCell at :1274-1275 today, and spec 12 re-specifies it for the new prompt path without closing the gap. Severity medium: a narrow input, but the effect is real, since the skeptic gets no signal that evidence is missing. The fix is sound if the build records the deliberate appendix change. Because renderCell composes renderPromptLine, a whitespace-only appendix cell moves from blank to '-'. That falsifies the section 4 sentence 'renderCell's output is unchanged for every input', which must be amended. review_replay.py:105 and :150 strip cells, so it would read '-' where it read ''. The fix already says to note or exclude this in AC3. | sound |
