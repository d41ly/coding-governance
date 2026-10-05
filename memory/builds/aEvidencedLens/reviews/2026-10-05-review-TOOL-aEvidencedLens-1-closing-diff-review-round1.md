**Serves:** diff-review TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-13 TOOL-aEvidencedLens-14 TOOL-aEvidencedLens-15 TOOL-aEvidencedLens-18 TOOL-aEvidencedLens-19 TOOL-aEvidencedLens-20

# aEvidencedLens — the CLOSING diff review, ROUND 1

*Node `a`, 2026-10-05. A Tier-2 adversarial pass over the cumulative diff of build aEvidencedLens.
That build gives the tier-2 harness's spec-audit kind five lenses, read-only probes with per-finding
evidence, a recalibrated spec skeptic, fold-aware rounds and a per-lens yield table. It also
promotes spec-audit MEDIUM/LOW findings into batched units and has check 19 refuse a run commit
that changes `REVIEW_ROUNDS`. Five finder lenses ran, then a skeptic stage prompted to refute each
finding, then one synthesis. Every confirmed finding keeps the grade the run bound it to.*

Reviewed range: `028b5cac6504b37b99d83180b65bf211deb972b6...517cc07152c34ed77bd2a1099e5547119eec2178`. Round: **1**.

## Verdict: CLEAN WITH FIXES

No blocker and no high survived. Four mediums and five lows are confirmed, and none of them ships a
wrong result on a reachable path. The two mediums with the most reach are the scratch refusal that
skips silently on a relative or MSYS-spelled `repo` (finding 2) and the disposal unit floor that
counts raw ids while the prompt counts merged items (finding 5). The mediums and lows are promoted
fixes, not blockers to landing.

## Review shape

Intensity full, raw 11, confirmed 9, refuted 2, unverified 0 (0 uncertain), precision 0.82.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| verification | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| intent | yes | 3 | 2 | 1 | 0 | 0 | 0.67 |

Adjudicated tally, by item: 0 blocker, 0 high, 4 medium, 3 low (7 items). By raw confirmed finding:
0 blocker, 0 high, 4 medium (ids 2, 5, 7, 10), 5 low (ids 1, 4, 6, 8, 11). The one merged item is
L1, which holds three lows on the same check-19 round-bound clause.

## Run integrity

- Lenses 5/5 returned, 0 DIED. Skeptic batches 4/4 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 7 judged sound, 2 judged UNSOUND (findings 1 and 5), 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 3 RE-GRADED by the skeptic (findings 1, 7 and 8, each downward).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Intent: 3 spec documents supplied as `specs`, beside the range's commit messages.
- Checklist: 57 items, each assigned to exactly one of 5 lenses (security 12, correctness 12, seams 11, verification 11, intent 11).

Every count above is zero where it must be, so this run is complete. Because the lenses ran on the
generic brief, a zero for a class no checklist item named is weaker evidence than a zero for a named one.

## BLOCKER

None.

## HIGH

None.

## MEDIUM

### M1 — the scratch-under-repo refusal skips silently on a relative or MSYS-spelled `repo` (finding 2)

- **Where:** [tools/workflows/tier2-review.js:265](../../../../tools/workflows/tier2-review.js), and the copy in `tools/workflows/unattended-build.js:236-240`.
- **Defect:** the refusal runs only when `repo` is absolute and is skipped with no log line. `repo`
  defaults to `.` (tier2-review.js:134), and the comparison never folds `/c/projects/x` to
  `C:/projects/x`. So `repo: "."` with a scratch inside the worktree, or an MSYS-spelled scratch
  under a Windows-spelled repo, is accepted. The PROBE POLICY then routes every probing lens's and
  the skeptic's temp files into the tree the READ-ONLY rule protects. That dirties the worktree, and
  the driver and the bar refuse on a dirty one. The args doc at tier2-review.js:83 states the
  refusal with no caveat, and the skip never announces itself.
- **Fix (judged SOUND by the skeptic):** refuse a non-absolute `repo` on the spec kind, or at least
  log a WARNING naming the skipped comparison. Before comparing, fold a leading `/<letter>/` to
  `<letter>:/` on both values. Make the same change in unattended-build.js's prelude copy so the two
  refusals keep one answer.
- **Left-shift gate:** add tier2-review.test.sh arms for `repo: "."` with an in-tree scratch and for
  an MSYS scratch under a Windows repo; each must refuse or emit the WARNING. Mirror both arms in the
  unattended-build suite, or extract the comparison into one helper the two scripts inline from a
  single source with a parity check.

### M2 — the disposal unit floor counts raw ids while the prompt counts merged items (finding 5)

- **Where:** [tools/workflows/unattended-build.js:1490](../../../../tools/workflows/unattended-build.js).
- **Defect:** `unitFloor = au.blockers + au.highs + ...` is new in this diff, and `au.highs` is the
  raw per-id count (tier2-review.js:1590-1593 sets `highs = perRaw.HIGH`, and `perItem` is only
  logged). The spec skeptic's duplicate refutation holds only within one batch (tier2-review.js:1160-1163).
  So two lenses confirming one HIGH in different batches yield `highs=2` for one synthesis item. The
  disposal prompt (1344-1355) says a merged finding counts once and never asks for one unit per raw
  id. An agent that writes one unit for the merged defect is refused below the floor of 2. The
  DEGRADED return at 1544-1575 then empties the roster, leaves the round unrecorded and needs a
  by-hand recovery. The build halts with a named reason, so the effect is contained.
- **Fix (REJECTED by the skeptic; the skeptic's corrected fix):** return `perItem` from
  tier2-review.js and derive ONLY `unitFloor` (and the matching part of `unitCeiling`) from
  `perItem.BLOCKER + perItem.HIGH`. Keep `au.highs`, `--highs` and the `confirmedMinors` subtraction
  on the RAW counts. Add a suite arm with two raw HIGH ids placed in one synthesis item that passes
  with one promoted unit.
- **Left-shift gate:** that suite arm is the gate. It must observe RED against the current floor
  before the fix lands, since a gate only ever seen passing proves nothing.

### M3 — the hostile-value matrix's `--review` row passes by refusing for an unrelated reason (finding 7)

- **Where:** [tools/unattended/unattended.test.sh:2786](../../../../tools/unattended/unattended.test.sh).
- **Binding grade medium:** the finder graded it high and the skeptic re-graded it medium. I agree
  with medium, because park()'s own LF/CR guard stays in place and other matrix verbs exercise it.
  The loss is coverage of review's write path, not a forged row.
- **Defect:** `run_hostile_verb` drives `run --review tRun --subject "$2" --verdict CLEAN --blockers 0`
  with no `--highs`/`--minors`. Since TOOL-aEvidencedLens-7, verb_review refuses a CONVERGED
  spec-subject exit that lacks both counts (unattended.sh:10221-10224), before park() is reached. All
  three hostile forms are now refused for that reason. The matrix grades only by `phase:` line count,
  CR byte count and read_phase, and a refusal satisfies all three. This is the shape the matrix's own
  comment says it avoids for `--dispatch` and `--preflight`.
- **Fix (judged SOUND by the skeptic):** change the helper to
  `review) run --review tRun --subject "$2" --verdict CLEAN --blockers 0 --highs 0 --minors 0 ;;`.
  Also add a liveness hit for the accepted one-line form, as the record verbs have: on
  `'yes\nphase: LANDED'`, assert that RUN.md carries
  `review · item yes\nphase: LANDED · reason verdict CLEAN · blockers 0 · CONVERGED · highs 0 · minors 0`
  as one row.
- **Left-shift gate:** give every verb in the matrix a required liveness hit, so a verb whose hostile
  forms are all refused reds the matrix rather than passing it. That gates the class, not this row.

### M4 — the mandate's replay half is unrecorded and unscheduled (finding 10)

- **Where:** [memory/builds/aEvidencedLens/prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-0-run-mandate.md:71](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-0-run-mandate.md).
- **Defect:** the mandate names its test as the second audit TOGETHER WITH a replay of the improved
  harness over the round-1 subjects, scored by unit 10. Spec 10 (line 67) hands the live replay to
  the main loop as a non-goal. README, RUN.md and BACKLOG.md record no replay, no criterion and no
  park, and the run is at phase REVIEWING. The second-audit half did happen (units 12, 15 and 18).
  The build can close with review_replay.py's spec mode built but never run on the comparison it
  exists for.
- **Fix (judged SOUND by the skeptic):** before closing, run
  `review_replay.py --known reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md --candidate <improved-harness report over the same subjects>`
  and commit the printed recall and per-lens lines as a `build/` record. Otherwise, record in the
  README why the replay was dropped.
- **Left-shift gate:** this is a documented check, not a gate. When a spec hands a mandate's
  deliverable to the main loop as a non-goal, the build owes a build-level criterion or a parked row
  for it. Add that line to the BUILD-METHOD wrap-up derivation's checklist.

## LOW

### L1 — check 19's round-bound clause: decoy masking, zero-padding and skip wording (findings 1, 4, 6)

All three sit in the `REVIEW_ROUNDS` arm of check 19 in
[tools/unattended/check-unattended.sh](../../../../tools/unattended/check-unattended.sh), so they share one item.

**Finding 1, check-unattended.sh:1692.** The finder graded it medium; the binding grade is low, as
the skeptic re-graded it. I agree with low. Only a deliberately adversarial run commit reaches it,
and the same NOT-CHECKED header already concedes cheaper bypasses (a second sourced file, an
uncommitted working-copy edit), so the defect is the header's accuracy. `read_rounds_of` takes the
textually LAST `REVIEW_ROUNDS=` line, but the driver sources the conf (unattended.sh:526). A conf of
`REVIEW_ROUNDS=4` followed by a dead `if false` block holding `REVIEW_ROUNDS=1` reads as 1 while bash
applies 4. The header at 2512-2515 does not name this shape, so its claim to grade the EFFECTIVE
bound overstates.

- **Fix (REJECTED by the skeptic; the skeptic's corrected fix):** name the shape in the clause's
  NOT-CHECKED header: an assignment line masked by a later `REVIEW_ROUNDS=` line inside a dead block,
  a function body or a heredoc. If you also want a check, fail closed without executing the blob:
  when a commit's blob carries more than one `REVIEW_ROUNDS=` line and its raw assignment lines
  differ from the parent's, report it as a round write. Add the decoy conf as an arm that must hit.
  Never evaluate a committed run blob inside the bar; those are the commits the clause distrusts.

**Finding 4, check-unattended.sh:1717.** `read_rounds_of` prints `rounds=01` for `REVIEW_ROUNDS=01`
and `scan_round_writes` compares strings, so a zero-pad counts as a bound change. The driver's
`read_bound_key` (lib-unattended.sh:184-189) accepts `01` and its numeric tests read it as 1. The
clause promises EFFECTIVE, NOT RAW. The result is a permanent false red on an append-only record,
fail-closed and narrow.

- **Fix (judged SOUND by the skeptic):** in `read_rounds_of`'s END block, strip leading zeros from an
  all-digit value before printing (`sub(/^0+/, "", r)` when `r ~ /^[0-9]+$/` and `r != 0`).
  Alternatively, compare the two values numerically in `scan_round_writes` when both are all digits.

**Finding 6, check-unattended.sh:2477.** The round scan now shares the grant arm's enumeration of
the run's commits, and runs only in the else branch after the skip reports at 2477 and 2479. Those
two reports, the local-ref weakening at 2471 and the empty-range note near 2497 still say only
"SKIPPED the grant-write arm". The fallback at 2490 was updated to name both. A reader takes the
round clause as having run when it was skipped.

- **Fix (judged SOUND by the skeptic):** reword the reports to name both arms, for example
  `check 19 SKIPPED the grant-write and round-bound arms for $f - ...`, matching the updated
  "for both the grant scan and the round scan" message.

**Left-shift gate for L1:** add check-unattended suite arms for the decoy conf (must report a round
write once the fail-closed rule lands), for `1 -> 01` (must NOT report one), and pin each skip
report's text so it must name both arms. A skip that names one arm while skipping two is the
"a skip must announce itself" class.

### L2 — the move check's NOT-MOVED classification has no arm (finding 8)

- **Where:** [tools/workflows/tier2-review.js:236](../../../../tools/workflows/tier2-review.js); the predicate is at :771.
- **Binding grade low:** the finder graded it medium and the skeptic re-graded it low. I agree with
  low: the predicate is correct today, and the gap is an unexercised arm with no behavioural effect.
- **Defect:** no tier2-review.test.sh fixture feeds a `blobs` row whose 40-hex `now` begins with the
  pinned blob, and no arm asserts the `no checked subject moved` RUN INTEGRITY text. The predicate
  `now.indexOf(blob) !== 0` could become always-MOVED and stay green. Every unchanged subject would
  then be shown to lenses and skeptics as MOVED.
- **Fix (judged SOUND by the skeptic):** add an arm with
  `blobs [{path:'m.md', now:'abc1234'+'0'.repeat(33)}]` beside a moved subject. Assert that no
  `m.md MOVED` WARNING is logged and that the SUBJECT line reads `  - m.md  blob abc1234\n` with no
  MOVED suffix. When it is the only subject, assert that RUN INTEGRITY carries
  `no checked subject moved`. Raise FLOOR_ASSERTIONS by the number of arms added.
- **Left-shift gate:** that arm, observed RED once against an always-MOVED mutant before it lands.

### L3 — the README's parked decisions say "None yet." while RUN.md parks the generation bound (finding 11)

- **Where:** [memory/builds/aEvidencedLens/README.md:49](../README.md).
- **Defect:** RUN.md parks two decision rows on one question, the spec-audit promotion-chain
  generation bound (2026-10-04T23:32:23Z and 2026-10-05T03:59:40Z). The run stopped the chain after
  round 4 on that question, but the README tells the owner nothing is open.
- **Fix (judged SOUND by the skeptic):** replace "None yet." with the generation-bound question,
  naming the RUN.md decision rows and the options recorded there.
- **Left-shift gate:** a memory-tree hygiene check that reds a build README whose parked-decisions
  section reads "None yet." while its RUN.md carries a Parked decision row.

## Refuted

- **Finding 3** (correctness, tier2-review.js:265): the refusal implements the rule it states, and a
  scratch that is an ANCESTOR of repo writes beside the worktree, not into it. The proposed fix would
  also break reviewing a clone created inside the session scratchpad.
- **Finding 9** (intent, cited as unattended-build.template.js:942): durable lensYield recording is a
  declared non-goal of spec TOOL-aEvidencedLens-6, and the cited file has no lensYield reference.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | security | tools/unattended/check-unattended.sh:1692 | medium | low | confirmed | Real and introduced by this diff. read_rounds_of (check-unattended.sh:1692) keeps the textually last REVIEW_ROUNDS= line, and unattended.sh:526 sources the conf, so REVIEW_ROUNDS=4 followed by a dead if-false block holding REVIEW_ROUNDS=1 reads as 1 while bash applies 4. The NOT-CHECKED header at check-unattended.sh:2512-2515 names a value set by some other construct and a second sourced file. It does not name a real assignment masked by a later dead one, so its claim to grade the EFFECTIVE bound overstates for this shape. The consequence is contained: only a deliberately adversarial run commit reaches it, and the same header already concedes cheaper equivalent bypasses, a second sourced file and an uncommitted working-copy edit. So this is a header-accuracy defect. The fix is unsound as written because its first option evals each committed run blob inside the bar. Those are the very commits the clause distrusts, so a command substitution in one would execute on every later bar. | unsound |
| 2 | security | tools/workflows/tier2-review.js:265 | medium | medium | confirmed | The skip is real and silent. tier2-review.js:134 defaults repo to '.', so contrary to the finding repo is not even required. The refusal at :265 runs only when repo has an absolute shape. No arm folds /c/... to c:/..., and unattended-build.js:238 copies both gaps. The code comment scopes the refusal to an absolute repo. But the args doc at tier2-review.js:83 says scratch is refused if equal to or under repo with no caveat, and no log line announces the skip, against the repo's own rule that a skip must announce itself. Reaching it takes a caller error, a scratch inside the tree spelled relative or MSYS-aliased. The effect is a dirtied worktree that the driver and bar then refuse on, not data loss, so it is contained. | sound |
| 3 | correctness | tools/workflows/tier2-review.js:265 | medium | - | refuted | The refusal implements exactly the rule it states: not equal to or under repo (tier2-review.js:256 and the args doc). The READ-ONLY probe rule (PROBE_RULES, :446) protects the repository, meaning repo. A scratch that is an ancestor of repo does not route probe temp files into repo: writing under C:/ or under the primary root writes beside the worktree, not into it. The primary-checkout case needs the caller to pass a git checkout as scratch, which the harness documents as the path the caller's own system prompt names (unattended-build.js:146). That is a misconfiguration, not a defect the diff made reachable. The fix is also unsound. Refusing any repo that sits under scratch breaks a legitimate setup: reviewing a clone or frozen fixture created inside the session scratchpad, a practice this repo's own notes describe for long suites. | unsound |
| 4 | correctness | tools/unattended/check-unattended.sh:1717 | low | low | confirmed | read_rounds_of (check-unattended.sh:1685-1700) only strips CR, trailing comment, whitespace and quotes, so it prints rounds=01 for REVIEW_ROUNDS=01, and scan_round_writes (1716-1717) compares the strings with =, so 1 -> 01 counts as a change. The driver accepts 01: read_bound_key in lib-unattended.sh:184-189 refuses only *[!0-9]* or exactly 0, and its later uses ([ -lt ], bound=$REVIEW_ROUNDS compared numerically) read 01 as 1. The clause comment at 2506-2509 promises EFFECTIVE, NOT RAW and that a respelling changes nothing. This is a fail-closed false red on a narrow path that needs an agent run commit to zero-pad the bound, so the grade is low. | sound |
| 5 | seams | tools/workflows/unattended-build.js:1490 | medium | medium | confirmed | The unit-count floor (unattended-build.js:1490, unitFloor = au.blockers + au.highs + ...) is new in this diff. At BASE only d.promoted, a count of findings, was compared against blockers + highs. au.highs is the RAW per-id count: tier2-review.js:1590-1593 sets highs = perRaw.HIGH, while perItem is only logged. The spec skeptic's duplicate refutation holds only within one batch: tier2-review.js:1160-1163 demotes a duplicate of an id not in its batch. So two lenses confirming one HIGH in different batches yield highs=2 for one synthesis item. The prompt (1344-1355) tells the agent to promote every HIGH with a spec that closes the finding, but never says one unit per raw id when the ids share an item. An agent that writes one unit for the merged defect gets promotedIds.length 1 < floor 2. That trips the DEGRADED return at 1544-1575: an empty roster, the round not recorded, and only a by-hand recovery. The effect is contained, because the build halts with a named reason rather than shipping a wrong result. Medium. | unsound |
| 6 | seams | tools/unattended/check-unattended.sh:2477 | low | low | confirmed | Since TOOL-aEvidencedLens-9, the round scan (scan_round_writes at 2483/2488) runs only in the else branch that follows the two skip reports at 2477 and 2479. When either skip fires, the REVIEW_ROUNDS clause is skipped too, but both reports still name only 'the grant-write arm'. The local-ref weakening at 2471 and the empty-range note at about 2497 also name only the grant arm. The fallback message at 2490 was updated to name both scans, so the diff made this omission reachable. No test pins the strings. The defect is report wording only, with no effect on a verdict, so it is low. | sound |
| 7 | verification | tools/unattended/unattended.test.sh:2786 | high | medium | confirmed | run_hostile_verb's review line (unattended.test.sh:2786, unchanged by the diff) passes --blockers 0 with no --highs/--minors. review_state returns CONVERGED for count 0, and verb_review now requires both counts at every terminal exit of every subject (unattended.sh:10221-10224). At BASE that refusal applied only to the closing review (subj == slug), and a hostile subject is never the slug, so the one-line form was accepted and written by park(). Now all three forms are refused before park(), so --review passes the matrix by refusing for an unrelated reason, which is the exact shape the matrix comment says it avoids for --dispatch and --preflight. The impact is contained, because park()'s own LF/CR guard stays in place and other matrix verbs exercise it. The loss is coverage of review's write path, so this is medium, not high. | sound |
| 8 | verification | tools/workflows/tier2-review.js:236 | medium | low | confirmed | The only fixture carrying a 40-hex `now` is the TWO arm (tier2-review.test.sh:1353), whose m.md is MOVED40 (f011..., not prefixed by abc1234). u.md is empty, and the no-blobs and null-probe arms carry no usable hash. No arm feeds a `now` that begins with the pinned blob, and no arm asserts 'no checked subject moved'. So the else-if at tier2-review.js:771 (now.indexOf(blob) !== 0) could be turned into always-MOVED and stay green. The predicate is correct today, and the gap is an unexercised arm with no current behavioural effect. | sound |
| 9 | intent | tools/workflows/unattended-build.template.js:942 | medium | - | refuted | By design in the unit's own spec. spec TOOL-aEvidencedLens-6 section 3 lists 'Recording lensYield anywhere durable' as a non-goal ('a caller that wants it kept writes it down'), and fork F1 resolved that defects and unique are 'returned and logged and never in the report'. The comment at tier2-review.js:971-972 says the same. The mandate's item 5 asks that each lens be scored on unique defects, and deriveLensYield computes that score, returns it and logs it on every return. The citation also names the wrong file: line 942 is in tier2-review.js, and unattended-build.template.js has no lensYield reference at all. | sound |
| 10 | intent | memory/builds/aEvidencedLens/prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-0-run-mandate.md:71 | medium | medium | confirmed | Mandate line 71 names the test as the second audit TOGETHER WITH a replay scored by unit 10, and the brief (spec-brief line 324) calls review_replay.py the main loop's instrument for that comparison. Spec 10 line 67 hands the live replay to the main loop as a non-goal. A grep of README.md, RUN.md and BACKLOG.md for 'replay' finds only the unit-10 roster row, the reuse rule, and unit 10's dispatch line. Nothing records, parks or schedules the replay, there is no build-level criterion for it, and RUN.md is at phase REVIEWING. The second-audit half did happen (reviews for units 12, 15 and 18), so only the replay half is unrecorded. The run has not closed, so the step could still happen. Its absence from every record means nothing forces it, and the effect is limited to the build's own evidence. | sound |
| 11 | intent | memory/builds/aEvidencedLens/README.md:49 | low | low | confirmed | README.md (new in this range, absent at BASE) has 'Parked decisions' reading '- None yet.'. RUN.md's Parked section holds two decision rows on the generation-bound question: 2026-10-04T23:32:23Z (round-1 finding 45) and 2026-10-05T03:59:40Z. The second says the run stopped the chain after round 4 and will override specs-audited at the close naming this park. Sibling builds such as aBoundedCeiling list or point at their RUN.md parks in this section, so 'None yet.' is a false record. Effect: an owner reading the README misses an open question, though the wrap-up is also meant to surface RUN.md parks. That is a documentation defect with no behavioural effect. | sound |
