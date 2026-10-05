**Serves:** diff-review TOOL-aBatchedMinors-1 TOOL-aBatchedMinors-2 TOOL-aBatchedMinors-3 TOOL-aBatchedMinors-4

# Tier-2 closing diff review — aBatchedMinors, ROUND 1

*The closing review of build aBatchedMinors, over the cumulative diff at the integration boundary.
The build implements the owner ruling of 2026-10-04 (TOOL-aBatchedMinors-5 in the decision log): every
finding the CLOSING diff review confirms is promoted to a build unit. That means one unit per BLOCKER
and per HIGH, and the MEDIUMs and LOWs batched into ONE unit, or two only across disjoint write sets.
None of them is folded into a spec. Spec-audit subjects keep folding mediums and lows. Unit 1 (a
`minors` return key in `tier2-review.js`) was retired WONTDO, because minors equals confirmed minus
blockers minus highs whenever both are non-null. Node `a`, 2026-10-04.*

Reviewed range: `5ba0fc4fcdab79eeeb7f75a97a48102bb10bfefa...092bbf2df0760bcdb2b22f933a43fb2b77b59e1d` · ROUND 1

## Verdict: CLEAN WITH FIXES

No blocker and no high survived. Three mediums and eleven lows were confirmed, all with effects
contained to operator procedure, prose carriers, or suite coverage of correct code. Under the rule
this build ships, all fourteen are owed promotion at the closing exit. That is zero units for blockers
and highs and one batched unit for the minors (`highs 0 · minors 14`). The minors' write sets overlap
on `unattended.sh`, the Skill and VERBS carriers, and the two suites, so a second batch unit is not
warranted.

## Review shape

- Intensity full. Raw 16, confirmed 14, refuted 2, unverified 0 (0 uncertain). Precision 0.88.
- Adjudicated tally by raw confirmed finding: BLOCKER 0, HIGH 0, MEDIUM 3 (ids 2, 8, 13), LOW 11
  (ids 1, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16).
- Adjudicated tally by item: BLOCKER 0, HIGH 0, MEDIUM 2 (M1, M2), LOW 7 (L1 to L7). Duplicate pairs
  were merged into one item each (2+13, 1+5, 6+14), and the four suite-coverage lows into one.
- Every binding grade was kept. Finding 9 carries the skeptic's re-grade (medium to low), which is
  its binding grade.
- Intent: 5 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 55 items, each assigned to exactly one of 5 lenses (security 11, correctness 11, seams
  11, verification 11, intent 11).

## Run integrity

- Lenses 5/5 returned, 0 DIED. Skeptic batches 4/4 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 13 judged sound, 1 judged UNSOUND (finding 13, whose corrected fix is
  given below), 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 1 RE-GRADED by the skeptic (finding 9).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief. The zero-blocker and
  zero-high result is therefore evidence from generic-brief lenses only. No lens died, so the set is
  complete for those briefs.

## BLOCKER

None.

## HIGH

None.

## MEDIUM

### M1 — the fold between closing rounds is not restricted to blockers, so the summed counts over-count (ids 2, 13)

- **Where:** `tools/unattended/SKILL.template.md:855` (the derivation) and `:799` (the CONVERGING
  bullet). Also `tools/memory-tree/BUILD-METHOD.template.md` M4, and M8 at `:245` and `:252`.
- **Defect:** The new derivation sums every round's highs and minors "because the fixes between rounds
  close blockers and nothing else". Nothing states that as a rule. CONVERGING still says "Fold and go
  again", and M8 has round N>1 read the fold and pass round N-1's whole confirmed set as
  `priorFindings`, which `tier2-review.js:744-745` tells lenses was "RAISED AND FIXED". The documented
  practice therefore fixes every confirmed finding between rounds.
- **Impact:** An operator who fixes a round-1 high or minor in the fold, then sums as instructed,
  records `--highs`/`--minors` that count already-fixed findings. Check 2 then demands phantom units.
  If the operator leaves them out instead, the gate cannot tell which happened, and those mediums and
  lows were disposed on the spot, which is what the ruling retires.
- **Fix (skeptic's corrected fix; the finder's proposal for 13 was judged UNSOUND, and 2's fix was
  judged SOUND and is subsumed here):** Amend the CONVERGING bullet, its render, and BUILD-METHOD
  M4/M8 so a non-terminal build-slug round fixes its BLOCKERS only and carries its highs, mediums and
  lows to the exit. Also amend M8's invocation (template `:245` and `:252`, plus the render) so that on
  the closing review `priorFindings` carries only the blockers the fold fixed, not "round N-1's
  confirmed set". Then point the `:855` derivation at that rule instead of asserting it.
- **Left-shift:** A carrier-parity check over the closing-review rule: assert the Skill's CONVERGING
  bullet and M4/M8 both contain the blockers-only fold sentence, the same way the existing render
  byte-compare holds the rendered guides to their templates.

### M2 — "omits either count" is certified by an arm that omits both (id 8)

- **Where:** `tools/unattended/unattended.test.sh:5719`, against the guard at
  `tools/unattended/unattended.sh:9097`.
- **Defect:** Spec TOOL-aBatchedMinors-2 AC3 refuses a terminal slug round that omits EITHER count.
  The only arm omits both, so a regression of the guard to an AND test passes every arm.
- **Impact:** Such a regression would write `... highs 2 · minors  · disposition promote`. Check 2's
  `/ · minors [0-9]+/` would not match it, the floor would drop to 1, and two promoted highs would owe
  one unit, with the suite green. The code is correct today.
- **Fix (judged SOUND by the skeptic):** Add two arms on a converged slug round, one with `--highs 1`
  alone and one with `--minors 1` alone. Each must hit the "requires --highs and --minors" refusal and
  be followed by the `same ... 'review · item tRun · reason' ... 0` row count.
- **Left-shift:** This is the arm itself. The class is an AC with an "either" clause whose arm covers
  only the joint case; add it to the project's bug-class checklist as an AC-to-arm cardinality check.

## LOW

### L1 — counts evaluated as bash arithmetic read leading zeros as octal and wrap long strings (ids 1, 5)

- **Where:** `tools/unattended/unattended.sh:9105`, with validation at `:8990-8995`.
- **Defect:** `owe=$(( blockers + highs + (minors > 0 ? 1 : 0) ))` runs over strings screened only by
  `*[!0-9]*`. `--highs 08` aborts the driver with "value too great for base" instead of a fail 37.
  `--highs 010` is read as 8 while check 2's awk reads 10. `18446744073709551616` wraps to 0, so the
  driver refuses `promote` and writes a CONVERGED row with no disposition onto the append-only RUN.md,
  which check 2 then reds permanently.
- **Fix (judged SOUND by the skeptic, both findings):** Refuse a leading zero on a multi-digit value
  and cap the digit count in the `--blockers`/`--highs`/`--minors` validation (refuse `0[0-9]*` and
  `????????*`), or normalise with `$((10#$x))` after a length cap. Either way the driver and the gate
  then read the same integer.
- **Left-shift:** Arms for `--highs 08`, `--highs 010` and an overlong value, each expecting a named
  fail 37 and no row written.

### L2 — the VERBS contract still says promote is "never required" on CONVERGED (ids 6, 14)

- **Where:** `tools/unattended/VERBS.template.md:186-190`, and the rendered
  `memory/guides/UNATTENDED-VERBS.md:190`.
- **Defect:** The sentence saying fold is the reading of a CONVERGED record with nothing above MEDIUM
  and that promote is "ACCEPTED, never required" was left unqualified. The paragraph below it now
  requires promote and refuses fold on the closing review. The Skill qualified the same sentence with
  "on a SPEC subject"; VERBS did not.
- **Fix (judged SOUND by the skeptic, both findings):** Qualify it as "On CONVERGED on a SPEC subject
  an optional --disposition promote is ACCEPTED, never required; the closing diff review's converged
  round is stated below", then re-render the guide.
- **Left-shift:** The same carrier-parity check as M1, extended to the CONVERGED disposition sentence.

### L3 — the state gate's fold message is false for the closing review (id 15)

- **Where:** `tools/unattended/unattended.sh:9079` (comment) and the message at `:9062`.
- **Defect:** A NON-CONVERGENT or CEILING closing round given `--disposition fold` hits the
  pre-existing state gate first, which says fold "is legal only at CONVERGED". The new block refuses
  fold on the closing review at every exit. The comment's "ACCEPTED there and never required" is also
  now false for that subject. The refusal itself is correct.
- **Fix (judged SOUND by the skeptic):** Branch the message on `subj` equal to `slug` and emit the new
  block's "the closing diff review folds nothing" sentence there. Add "on a spec subject" to the
  comment.
- **Left-shift:** An arm giving `fold` on a NON-CONVERGENT slug round that asserts the
  closing-review wording, not the CONVERGED-legal one.

### L4 — M4 cites an exception M2 does not carry (id 16)

- **Where:** `tools/memory-tree/BUILD-METHOD.template.md:141` (M4) against `:34` (M2).
- **Defect:** M4 says the minors batch "is the one unit M2's one-mechanism rule admits". M2 still says
  "one mechanism per spec" with no exception.
- **Fix (judged SOUND by the skeptic):** Add "except the closing diff review's minors batch (M4)" to
  M2's decompose sentence, and re-render `memory/guides/BUILD-METHOD.md` within its byte cap.
- **Left-shift:** None proportionate; a §10 checklist entry, "a cross-reference to a rule's exception
  must land in the rule too".

### L5 — the build README still promises the retired harness key (id 7)

- **Where:** `memory/builds/aBatchedMinors/README.md:25`.
- **Defect:** "The review harness returns the minor count the record needs" describes unit 1, which
  is WONTDO (README `:39`, `:65`). What shipped derives minors from the harness's
  blockers/highs/confirmed tally.
- **Fix (judged SOUND by the skeptic):** Reword it to what shipped, for example "The closing exit
  records highs and minors derived from the harness's own blockers/highs/confirmed tally, with no
  parser over review prose", or drop it.
- **Left-shift:** None proportionate; a §10 checklist entry to re-read "Expected improvements" when a
  unit is retired.

### L6 — suite coverage gaps on correct code (ids 9, 10, 11)

- **id 9 — `tools/unattended/check-unattended.sh:759`.** The per-RUN-file summation `nneed += owe`
  has no arm with two promoting subjects; a regression to `nneed = owe` or a per-subject max passes.
  Skeptic re-graded this medium to low (binding). **Fix (judged SOUND):** Add an mkdisp arm with
  `item S1 ... blockers 2 · NON-CONVERGENT · disposition promote` and
  `item tDisp ... blockers 0 · CONVERGED · highs 1 · minors 1 · disposition promote`. Two new ids must
  hit "against a floor of 3", and three must not reach "check 2 FAILED".
- **id 10 — `tools/unattended/unattended.test.sh:5723`.** AC2's "no row is written" for the
  spec-subject refusal is unasserted; the zero-row check greps `item tRun` only. **Fix (judged
  SOUND):** After `:5717`, assert `grep -c 'review · item S9 · reason' memory/builds/tRun/RUN.md` is 0.
- **id 11 — `tools/unattended/check-unattended.sh:781`.** The graded promote messages now print
  `nsubj`, not `nneed`. No arm tells them apart, and the graded "cannot be read" branch has no arm.
  **Fix (judged SOUND):** Extend the arm at `check-unattended.test.sh:1270` to match "1 subject(s)
  EXITED recording disposition promote and the generated units region gained only 1". Optionally add
  a graded arm with an unreadable BASE and a counted row.
- **Left-shift:** These are the arms. The class (an AC clause or a changed accumulator with no
  distinguishing arm) belongs in the checklist beside M2.

### L7 — a suite comment claims a post-cutoff arm that does not exist (id 12)

- **Where:** `tools/unattended/check-unattended.test.sh:1303`.
- **Defect:** The comment says "at the fold cutoff and after it", but the one arm commits at
  `DISPDATE 2026-09-15`, which equals `FOLD_CUTOFF`.
- **Fix (judged SOUND by the skeptic):** Add an arm with `DISPDATE` after the cutoff (for example
  2026-10-04T00:00:00 +0000), or reword the comment to "at the fold cutoff".
- **Left-shift:** The added arm.

## Refuted

- **id 3** — a duplicate of id 1 (same line, same octal defect).
- **id 4** — pre-existing and in line with intent. Promotion has always been scoped to CONFIRMED
  findings, and skeptic-UNCERTAIN findings were counted by no flag at the base either.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | security | tools/unattended/unattended.sh:9105 | low | low | confirmed | unattended.sh:9105 is new in this diff: owe=$(( blockers + highs + (minors > 0 ? 1 : 0) )) over values validated only by `*[!0-9]*` (lines ~8990-8993), so leading zeros and overlong strings pass. Reproduced: `h=08; $(( h ))` aborts bash with 'value too great for base' (rc 1, nothing after it runs); `010` evaluates to 8; 18446744073709551616 wraps to 0. check-unattended.sh's awk reads the same field as decimal (`hi += 0`), so the driver's owe and check 2's floor can disagree, and the overflow case lets the driver accept a no-disposition CONVERGED row that check 2 then reds as a no-disposition exit on an append-only record. Base used blockers only in [ -ge ]/[ = ] comparisons, so the arithmetic path is new. Contained: the input is operator-supplied, and the gate reds the miscount instead of passing it. Low. | sound |
| 2 | correctness | tools/unattended/SKILL.template.md:855 | medium | medium | confirmed | The new SKILL paragraph sums every round's highs and minors and justifies it with 'the fixes between rounds close blockers and nothing else'. Neither CONVERGING ('Fold and go again') nor M4 ('Folding a round's own fixes does not re-arm the loop') nor M8 restricts the fold to blockers. M8 in fact also says 'Left-shift every confirmed finding - a regression gate' before closing, which invites acting on highs and minors between rounds. A run that fixes a round-1 high or minor in the fold and then follows the summing rule over-counts --highs/--minors. check 2 then demands units for findings that were already fixed. The premise exists only as a rationale clause in one paragraph, so two carriers give two answers. The effect stays inside the run's unit count. Medium. | sound |
| 3 | correctness | tools/unattended/unattended.sh:9105 | low | - | refuted | Duplicate of id 1: same line (unattended.sh:9105), same defect (bash reads zero-padded counts as octal and aborts on 08/09), same impact and same class of fix. Id 1 carries it with the overflow case as well. | sound |
| 4 | seams | tools/unattended/SKILL.template.md:853 | medium | - | refuted | PRE-EXISTING and in line with the stated intent. The owner ruling this build implements, and every spec and doc it touches, scope promotion to findings the closing review CONFIRMS. At base the closing exit's --blockers was already the confirmed-blocker count, and highs were disposed from the confirmed set, so a skeptic-UNCERTAIN finding was already counted by no flag and promoted by nobody. No doc at base or head (SKILL, BUILD-METHOD, PROTOCOL, specs) addresses unverified findings for the closing review. The diff adds two counts drawn from the same confirmed population and does not newly drop a population. The Disposal stage in unattended-build.js is the spec-audit path, which this build leaves unchanged by design. | sound |
| 5 | seams | tools/unattended/unattended.sh:9105 | low | low | confirmed | Reproduced. unattended.sh:8990-8995 validates highs/minors with *[!0-9]*, which admits a leading zero, and :9105 feeds them to $(( )). In bash, `f(){ local h=08; o=$(( h + 1 )); }; f; echo next` prints 'value too great for base' and the script exits rc=1 without reaching 'next', so the driver dies without a fail 37. `010` evaluates as 8, so the exit note at :9136 says 'owes at least' a different number than check 2's awk +0 reads from the row ('highs 010' read as 10). At the base, blockers reached only review_state's [ -ge ] tests, which read decimal, so this path is new. The input is operator-typed and the effect is contained to a mis-stated note or an aborted call that writes no row. | sound |
| 6 | seams | tools/unattended/VERBS.template.md:190 | low | low | confirmed | VERBS.template.md:189-192 (and the rendered memory/guides/UNATTENDED-VERBS.md:190) still say that on CONVERGED an optional --disposition promote is 'ACCEPTED, never required'. The diff made that false for the build-slug subject, where unattended.sh:9106 now requires promote whenever owe>0. The new paragraph directly below does state the closing rule, so a careful reader resolves it. The unqualified sentence is still a contradiction this diff introduced into a binding contract carrier that the Skill carrier did qualify. The effect is documentation only, and the driver refuses the wrong call loudly. | sound |
| 7 | seams | memory/builds/aBatchedMinors/README.md:25 | low | low | confirmed | memory/builds/aBatchedMinors/README.md:25 still lists 'The review harness returns the minor count the record needs' as an expected improvement. Unit 1, which would have delivered it, is WONTDO (README :39 and :65). The same README records the retirement two sections later, so the claim is stale but contradicted in place. It has no behavioural effect, so it is cosmetic. | sound |
| 8 | verification | tools/unattended/unattended.test.sh:5719 | medium | medium | confirmed | Spec TOOL-aBatchedMinors-2 AC3 (line 112) says the slug subject's terminal round is refused when it 'omits either count'. The only arm, unattended.test.sh:5719 (`--blockers 0` with neither flag), omits both. The guard at unattended.sh:9097 (`[ -z "$highs" ] \|\| [ -z "$minors" ]`) is correct today. A regression to an AND test would still pass every arm, and it would write a 'minors ' row that check 2 cannot match, which drops the owe back to the floor. That makes the AC's 'observed' claim broader than what the suite certifies. The current code is correct, so the consequence is contained to future-regression detection. | sound |
| 9 | verification | tools/unattended/check-unattended.sh:759 | medium | low | confirmed | No graded check-2 fixture holds two subjects that both record disposition promote. The only multi-subject arm (check-unattended.test.sh:1175) runs the ungraded path, which still counts nneed++. Every new aBatchedMinors arm (1268-1305) holds the single subject tDisp. The diff replaced the graded nneed++ with the weighted 'nneed += owe' (check-unattended.sh:759). A regression to 'nneed = owe' or to a per-subject max would therefore pass every arm. The current code is correct; the effect is a coverage gap on a stated contract, with no wrong behaviour today. | sound |
| 10 | verification | tools/unattended/unattended.test.sh:5723 | low | low | confirmed | Spec TOOL-aBatchedMinors-2 AC2 says the spec-subject refusal writes no row. The S9 arm at unattended.test.sh:5717 checks only the refusal text, and the zero-row 'same' assertion at 5723 greps 'item tRun' only. Today the refusal (unattended.sh:8995-8998) fails and returns before park(), so no S9 row is written. The 'no row' clause is still unasserted. | sound |
| 11 | verification | tools/unattended/check-unattended.sh:781 | low | low | confirmed | Both graded promote messages now print nsubj (check-unattended.sh:777,779), while the floor is nneed. The only arm that asserts the leading subject count (test.sh:1244) uses an uncounted row, where nsubj and nneed are both 1, so it cannot tell them apart. The new floor arms match only from 'gained only' onward. No arm reaches the graded 'cannot be read' branch. Output is correct today, and a regression would only misword the message. | sound |
| 12 | verification | tools/unattended/check-unattended.test.sh:1303 | low | low | confirmed | The comment at check-unattended.test.sh:1303 claims coverage 'at the fold cutoff and after it'. The single arm commits at DISPDATE 2026-09-15T00:00:00, which equals FOLD_CUTOFF=2026-09-15 (unattended.sh:819). No post-cutoff arm exists. The overclaim is in a comment only. | sound |
| 13 | intent | tools/unattended/SKILL.template.md:799 | medium | medium | confirmed | The premise added at SKILL.template.md:855 ('the fixes between rounds close blockers and nothing else') is contradicted by the method the diff leaves in place, not just left unstated. BUILD-METHOD M8 (template :245, :252) has round N>1 read the FOLD and pass 'round N-1's confirmed set' as priorFindings. tier2-review.js:744-745 tells the lenses that set was 'RAISED AND FIXED'. So the documented practice fixes every confirmed finding between rounds, and the CONVERGING bullet (:799, 'Fold and go again') is unedited. Under that practice the summed --minors/--highs counts findings already fixed in place, so a unit is owed for a fix that has already happened. The alternative is that the operator leaves them out, and the gate cannot tell which one occurred. The effect is limited to the operator procedure and record counts; the driver's refusals stay correct. | unsound |
| 14 | intent | tools/unattended/VERBS.template.md:190 | low | low | confirmed | VERBS.template.md:186-190 still states, unqualified, that fold is the reading of a CONVERGED record with nothing above MEDIUM, that the row needs no field, and that promote on CONVERGED is 'ACCEPTED, never required'. The paragraph that follows in the same entry says the build-slug subject's CONVERGED REQUIRES promote whenever minors stood and refuses fold outright. The diff made the first sentence false for that subject without qualifying it. It is prose only: the driver enforces the new rule. | sound |
| 15 | intent | tools/unattended/unattended.sh:9079 | low | low | confirmed | The state-gate message at unattended.sh:9062 is unchanged from the base (it is the same text there). This diff made it false for the build-slug subject, because the new block at :9101-9103 refuses fold on the closing review at every exit, CONVERGED included. A NON-CONVERGENT or CEILING closing round given fold hits the state gate first, which tells the operator that fold becomes legal at CONVERGED. The comment's 'ACCEPTED there and never required' is likewise now false for that subject. Only operator guidance is affected: the refusal itself is correct. | sound |
| 16 | intent | tools/memory-tree/BUILD-METHOD.template.md:141 | low | low | confirmed | BUILD-METHOD.template.md:141 (M4) now says the minors batch 'is the one unit M2's one-mechanism rule admits'. M2 at :34 is unedited and states 'one mechanism per spec' with no exception, so the cross-reference names an exception that its target does not carry. Only prose is affected. | sound |
