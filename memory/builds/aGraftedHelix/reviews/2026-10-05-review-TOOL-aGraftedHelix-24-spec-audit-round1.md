**Serves:** spec-audit TOOL-aGraftedHelix-24

# aGraftedHelix — Tier-2 spec audit of unit 24, ROUND 1

*Node `a`, 2026-10-05, ROUND 1 for this subject. Unit 24 promotes the HIGHs of the round-1 audit of
unit 23 (that round's H1, H2 and H3). It moves the `prior-session` add ahead of `write_lease`, names
a session on every criterion call of unit 23 that is not `--resume`, and starts AC5's sequence-d
restart short of d's closing call. Four lenses ran: underspecification, contradiction, unstated
assumption and prior art. Every finding in the body survived a skeptic prompted to REFUTE it. The
three findings the skeptics refuted appear only in the appendix. The author of this report confirmed
that the pinned blob below is the blob at HEAD (`e8f4724a5`), by `git rev-parse HEAD:<path>` against
`git hash-object <path>`. That blob is the spec's rev-2, last touched by `cf911132b`. Five rows were
spot-checked in the tree. For H1, `set_fact` returns 2 on a failed `mktemp` at
`tools/unattended/unattended.sh:5528`, and `write_lease` (lines 5559 to 5569) ends every `set_fact`
with `|| return 1`. For M2, the holder row's only `stage_or_fail` sits inside the `write_lease`-due
branch (lines 6597 to 6600), under the comment at 6592 saying the row writes NOTHING otherwise. For
L2, S1 reads "the next claim write that lands empties them" (spec lines 41 to 42). For L6, unit 23's
AC5 reads "When sequence d of §4 runs" (unit 23 line 275), while unit 24 S3 quotes "when sequence d
of section 4 runs" (spec line 57). For L9, the fourth §7 New arm's floor field reads "none, the arm
is unit 23's and is rewritten". The other rows carry the skeptics' verified text and were not
re-derived here.*

**Reviewed at ROUND 1, the subject pinned at its blob:** `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md`@`9b15b9389adf2e16ad443d31c93d21256440ba25`.

## Verdict: CLEAN WITH FIXES

No confirmed finding is graded BLOCKER, so the spec is buildable as written. The verdict is not
CLEAN, because thirteen confirmed findings stand and one of them is HIGH.

- H1 (id 11): S1 moves the add ahead of `write_lease` but states no rule for the add's own failure.
  A build that lets the row continue past a failed add into `write_lease` reopens the window this
  unit exists to close, and AC1 cannot tell that build from a correct one.

Two findings are MEDIUM. Both sit on the unreachable-remote path, which AC1 never drives. Ten are
LOW, and every one of them is prose: a label, a rationale, a quoted anchor, a restated table or a
floor field. Adjudicated, the thirteen confirmed findings form twelve items. One merge was made,
within one binding grade: ids 1 and 3 (both low) are one defect, an `Observed by AC1` label on S1
that covers two clauses no criterion observes. No binding grade was changed. The skeptic re-graded
id 1 from high to low, and this report keeps that grade.

The one fix judged UNSOUND is id 1's. The finder proposed a new AC1 leg. The skeptic showed that the
leg's stated red cannot occur and that its shim never fires under a correct build. The report
carries the skeptic's corrected fix, which is a label and a rationale correction, not a leg.

Several fixes add legs to AC1, and they should be folded as one design. H1 adds a leg in which the
add's own `set_fact` fails. M1 adds a leg in which the first `s2` call's remote is unreachable. M2
adds a leg in which a later `s2` call is still unreachable. M1's and M2's legs can share one fixture:
an unreachable interrupted call, a still-unreachable call, then a call with the remote restored.

Disposition, per `memory/guides/BUILD-METHOD.md`: every CONFIRMED finding is disposed by severity.
The HIGH is promoted to a unit whose mechanism closes it, audited as a SPEC. Each MEDIUM and LOW is
folded into this spec as a rev bump with a §9 line. Unit 24 is itself a promotion of unit 23's
HIGHs, so promoting H1 extends the chain by one more link. The method ends a chain at a promoting
round whose stated precision falls below the review protocol's floor. This round's precision,
stated for that rule to read, is 0.81.

## Review shape

Intensity full. Raw 16, confirmed 13, refuted 3 (ids 9, 12 and 16), unverified 0 (0 uncertain),
precision 0.81.

The adjudicated tally, counted both ways:

| severity | items | raw confirmed findings |
|---|---|---|
| BLOCKER | 0 | 0 |
| HIGH | 1 | 1 |
| MEDIUM | 2 | 2 |
| LOW | 9 | 10 |
| **total** | **12** | **13** |

By lens, raw then confirmed: underspecification 3 and 3, contradiction 5 and 5, unstated
assumption 2 and 1, prior art 6 and 4.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 4 of 4 returned, 0 DIED.
- 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and 0
  duplicates were found.
- Fixes on confirmed findings: 12 judged sound, 1 judged UNSOUND (id 1), 0 with no fix proposed,
  and 0 NOT JUDGED. An unjudged fix would be the finder's proposal and nothing more; none occurs
  here.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, so none is bound at the finder's grade
  by default. 1 was RE-GRADED by the skeptic: id 1, from high to low.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, and 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.

This report does not call the run complete. Every lens and every skeptic batch returned, but one fix
was judged UNSOUND, one grade was re-graded, no checklist was swept, no intent was supplied, and
every lens ran on the generic brief.

**Intent:** NEITHER `specs` nor `context` was supplied to this review. The lenses graded the spec
against itself, against the units it supersedes or consumes from (units 1, 20 and 23) and against
the tree, not against a stated intent for the build.

**Checklist:** NONE swept — absent. The count of recurring-bug-class findings in this report is
therefore not evidence that the project's recurring classes are absent from this spec. The spec's
own §9 records a checklist run over the promoting commit, but that run was the fold's, not this
review's. A caller of the next round should pass the output of
`python tools/memory-tree/gotchas.py --for-paths` over the spec's Files-touched paths.

## How the findings cluster

A fold that repairs a class repairs every row in it, so the classes are named here before the rows.

| class | ids | where the gate belongs |
|---|---|---|
| The add's failure and trigger paths that no criterion drives | 11, 2, 10 | one AC1 leg per path in `tools/unattended/unattended.test.sh`: the add's own write failing, the unreachable-remote trigger, and an outage that continues past the interrupted call |
| An `Observed by` label covering clauses no criterion observes | 1, 3 | a §10 checklist entry, and the spec lint the round-1 audit of units 20 to 22 asked for |
| Rationale prose that contradicts the spec's own criteria, tables or a sibling unit | 4, 5, 6, 7, 13 | a §10 checklist entry |
| A restatement of a sibling's text that drifts from its source | 8, 14 | a §10 checklist entry: quote the superseded text verbatim, and restate only the moved row |
| A New-arm floor field that does not count the assertions the rewrite adds | 15 | a §10 checklist entry |

The second class recurs. The round-1 audit of units 20 to 22 named an `Observed by` label that no
criterion reads as a recurring class and asked for a spec lint. The round-1 audit of unit 23 noted
that the lint had not been built. It still has not, and the class appears here again.

# HIGH

## H1 · id=11 — S1 states no rule for the add's own failure, so a build that continues into `write_lease` after a failed add reopens the window

- **Address:** TOOL-aGraftedHelix-24 §2 S1 (no rule for the add's own failure), with §6 AC1, §4
  Evidence and §4 "What an interruption leaves".
- **Defect:** S1 orders the add before `write_lease`'s first `set_fact`, but no sentence says the
  row stops when the add's own write fails. §4 Evidence states the failure rule for `write_lease`
  only (`:6599` returns when `write_lease` fails). The interruption table starts from "stopped after
  the add" and never covers an add that failed while the row went on. `set_fact` returns 2 without
  writing when `mktemp` fails (`:5528`), and it returns `mv`'s status unchecked. The `|| return 1`
  suffix is a convention, not a gate: base already has `set_fact` calls chained without it, for
  example at `:7662`. The class rule H1 of unit 23 was promoted for says a protecting fact is
  written before the first write that can move the field it protects, and that rule only holds if
  the protecting write's failure stops the row.
- **Impact:** take a build that writes the add without a return and hits a one-off failure of the
  add's `set_fact`, such as a transient `mktemp` failure or an `mv` failure under a Windows file
  lock. The row continues into `write_lease`, which succeeds. That leaves the record at `s2`, the
  claim at `s1` and no `s1` in the set. The next `s2` call is not due under an unchanged pid, reads
  the claim as foreign and answers check 90, or check 89 at the restart row. That is the claim-lost
  abort unit 23's H1 was promoted to prevent, on a path just as narrow. AC1's shim fires only once
  the record reads `s2`, which is after the add, so AC1 cannot tell the two builds apart. No §7 arm
  stages the missing return.
- **Fix — the skeptic judged it SOUND:** in S1, require the holder row to return non-zero, before
  `write_lease`, whenever the add's `set_fact` fails. Add a third AC1 leg whose `mktemp` shim fails
  the FIRST call made while the claim push exits 124, which is the add's own `set_fact`. That leg
  asserts that the call exits non-zero, the record still reads `session: s1`, and a following `s2`
  call prints no `UNATTENDED check 90 FAILED`. Stage a break that drops the add's `|| return 1`.
- **Left-shift gate:** that leg in `tools/unattended/unattended.test.sh`, observed RED with the
  add's `|| return 1` removed. Add a §10 checklist entry: "a protecting write placed ahead of the
  write it protects carries its own failure rule, and a criterion fails the protecting write
  itself, not only the write after it." A cheaper structural gate is also worth weighing: a
  shell-hygiene scan that flags a `set_fact` in the holder row with no `|| return` on the same line.

# MEDIUM

## M1 · id=2 — S1 moves the add for two triggers, but AC1 drives only the CAS-failed one

- **Address:** TOOL-aGraftedHelix-24 §2 S1 and §6 AC1, against §4 "The order" (the add row).
- **Defect:** §4's add row moves the add for two triggers: the CAS did not complete, or the claim
  was unreadable. AC1 interrupts only the first, through the claim push exiting 124, yet S1 says
  AC1 observes the whole item. An unreachable remote makes the claim unreadable, and a build can
  reach the add from that branch separately.
- **Impact:** a build that moves only the CAS-failed path's add, leaving the unreadable-claim path's
  add after `write_lease`, passes AC1 and every §7 arm. On that path, an interruption after
  `write_lease`'s `session` line leaves the record at `s2`, the claim at `s1` and an empty set. The
  next `s2` call has `write_lease` not due, so it reaches the claim through `mine` alone. Neither
  `mine` nor same session matches, and the call answers check 90. The consequence is contained to
  the unreachable-remote path combined with an interruption.
- **Fix — the skeptic judged it SOUND:** give AC1 a second leg on the same fixture. Make the first
  `s2` call's remote unreachable (unit 23's definition: the bare repo renamed away) instead of the
  124 shim. Keep the same `mktemp` shim and make the same assertions: `session` reads `s2`,
  `prior-session` reads `s1`, and `lease-utc` is unmoved. Then run a second `s2` call with the
  remote restored, which exits 0 with no check 90. Add the leg to §7's first New arm, staging the
  unreadable-path add moved back after `write_lease`.
- **Left-shift gate:** that leg, observed RED under its staged break. Add a §10 checklist entry:
  "a scope item with more than one trigger names a criterion leg per trigger, and its `Observed by`
  label is checked against each."

## M2 · id=10 — §4 assumes the next call's claim write lands, so a continuing outage leaves the interrupted record unstaged

- **Address:** TOOL-aGraftedHelix-24 §4 "What an interruption leaves", the paragraph under the table
  ("The next call stages it ...").
- **Defect:** the paragraph says the next call stages the interrupted record "through the
  `write_lease`-due branch or through unit 23 S3's clear". That holds only when the next call's
  `write_lease` is due or its claim write lands. On a not-due call, unit 23 S2 adds nothing, and unit
  23's set table reads "write_lease not due, and no claim write lands: unchanged, and nothing is
  written". S3's clear, and its `stage_or_fail`, run only after a landed claim write. The only other
  staging point is the `stage_or_fail` inside the due branch (`:6597-6600`). The rest of the not-due
  path stages nothing (`run_orphan_reap`, `verb_status`, `print_resume_orientation`). The stated
  reason is also false for row 1: there the record and the claim both read `s1`, and staging comes
  from the due branch because the environment's session differs from the record's.
- **Impact:** after rows 2 and 3 under the fixture's unchanged pid, or after row 3 or a stop past
  `pid` in a real new session, every call during a continuing outage leaves the record's `s2` and
  `prior-session` lines unstaged. That outage is the condition that left the CAS incomplete in the
  first place. `stage_or_fail`'s own header (`:2620-2628`) says an unstaged run is invisible to every
  check the gate leg has, because that leg's per-run population is the index. No criterion drives an
  interrupted call followed by a still-incomplete one, and AC1's second call runs with no shim, so
  its claim lands. The effect is contained: it heals when a claim lands or another writer stages the
  file. The skeptic corrected one part of the finder's impact: `--hold`'s `check_clean`
  (`:1975-1984`) counts staged paths as well as unstaged ones, so staging alone would not clear
  check 2.
- **Fix — the skeptic judged it SOUND:** either have the holder row run `stage_or_fail` whenever the
  run-state file differs from the index, whether or not `write_lease` is due and whether or not the
  claim lands, and add an AC1 leg in which, after the interrupted call, a second `s2` call with the
  remote unreachable leaves `git diff --name-only` naming no run-state file. Or narrow the sentence
  to "the next call whose claim write lands" and state the outage gap. In either case, give row 1's
  reason as the `write_lease`-due branch: the environment's session differs from the record's.
- **Left-shift gate:** under the first option, that leg, observed RED with the new `stage_or_fail`
  removed. Under the second, a §10 checklist entry: "a sentence that says the next call heals a
  partial write names the condition under which that call writes, and a criterion drives the call
  that does not." This fold shares a paragraph with L3's.

# LOW

## L1 · id=1, id=3 — S1's `Observed by AC1` covers two clauses no criterion observes: the clear's place and the comment

- **Address:** TOOL-aGraftedHelix-24 §2 S1 (the "clear keeps its place" clause and the "comment at
  the row" clause) and §6 AC1, with §3 Non-goals "Moving the clear ahead of `write_lease`".
- **Defect:** S1 says "The clear keeps its place after `write_lease`" and "The comment at the row
  names this order", and tags the whole item "Observed by AC1". AC1's first call never lands a CAS,
  so it never runs the clear. Its second call has `write_lease` not due, so it cannot order the
  clear against `write_lease`. AC1 observes only run-state facts, the claim and exit codes, so it
  cannot observe a comment either. The sibling convention, unit 23 S6 and unit 20 S7, labels a prose
  or comment clause NOT OBSERVED with a reason. §3's rationale for keeping the clear in place is also
  wrong: it says moving the clear ahead would leave a claim under the new session and a record under
  the old one, but no verdict depends on that state.
- **Impact:** for id 1 the finder graded HIGH, on the claim that moving the clear reopens a check-90
  window. The skeptic re-graded it low, and this report keeps that grade. After a landed CAS the
  claim carries the caller's own session, and unit 1 §4's same-session holder row answers the next
  call under that session whatever the set holds. A caller under any other session gets the same
  verdict in both orders, because the set never holds the session a landed CAS just wrote. So no
  verdict depends on where the clear sits. For id 3, the comment can be left stating unit 20's
  add-after-`write_lease` order with every criterion green. That misleads a later reader, which §5's
  risks name as the hazard, but it does not change behaviour.
- **Fix — id 1's fix was judged UNSOUND by the skeptic; this is the skeptic's corrected fix:** label
  S1's clause about the clear's place NOT OBSERVED by a criterion here, with this reason: after a
  landed CAS the claim carries the caller's own session, and unit 1's same-session holder row answers
  it whatever the set holds, so no verdict depends on that place. Correct §3's "Moving the clear
  ahead of `write_lease`" rationale to match. The finder's proposal, an extra AC1 leg, is not
  reproduced here. Its stated red cannot occur because of the same-session row, and under a correct
  build its shim never fires, so the leg would pass by finding nothing.
- **Fix for id 3 — the skeptic judged it SOUND:** label the comment clause NOT OBSERVED by a
  criterion here, with the reason, as unit 23 S6 does for its prose. Keep "Observed by AC1" for the
  add's place only. Both fixes edit the same label, so fold them as one edit.
- **Left-shift gate:** this is the recurring class, so the gate is the spec lint the round-1 audit
  of units 20 to 22 asked for: a check that every S-line tagged `Observed by ACn` names a clause
  that ACn's Red-when can reach. Until it exists, a §10 checklist entry: "an `Observed by` label is
  read clause by clause, and a clause no criterion reaches is split off and labelled NOT OBSERVED
  with a reason."

## L2 · id=4 — S1 says any landed claim write empties the set; unit 23 S3 and AC2 say only a `--resume` holder-row write does

- **Address:** TOOL-aGraftedHelix-24 §2 S1 (the clear sentence), against §6 AC2 and unit 23 S3.
- **Defect:** S1 says "the next claim write that lands empties them". Unit 23 S3, unit 23's §3
  non-goal and its title make the next `--resume` holder-row claim write that lands the only writer
  that empties the set. Unit 24's own AC2 asserts that the set still reads `s1` after a landed
  `--beat` or `--dispatch`.
- **Impact:** a comment or build that follows S1's wording would empty the set on any landed claim
  write, so a tick `--beat` would write the run-state file. Unit 23 §3 rejects that design, and AC2
  here and unit 23 AC1 both go red on it. Unit 23 S3 governs the build, so behaviour is unchanged.
  The cost is a misleading rationale that a comment could copy.
- **Fix — the skeptic judged it SOUND:** change the clause to "and the next `--resume` holder-row
  claim write that lands (unit 23 S3) empties them".
- **Left-shift gate:** a §10 checklist entry: "rationale prose that names a writer is checked
  against the S-line that owns that writer, and against every criterion that asserts the opposite."

## L3 · id=5 — §4's closing paragraph gives one reason for all three rows, and it is false for row 1

- **Address:** TOOL-aGraftedHelix-24 §4 "What an interruption leaves", the closing paragraph,
  against the same table's row 1.
- **Defect:** the paragraph justifies the next call's staging "because in every row the claim it
  reads differs from the record's session". Row 1 ("stopped after the add") has record `session`
  `s1` and claim `s1`, so they do not differ. That row stages through the `write_lease`-due branch
  because the record's session differs from the CALL's session.
- **Impact:** a reader reasoning from the paragraph would conclude that row 1's next call has no
  claim write due and stages nothing. The table rows are right, so a builder working from them
  builds correct behaviour.
- **Fix — the skeptic judged it SOUND:** split the reason. In rows 2 and 3 the claim (`s1`) differs
  from the record's session (`s2`), so the renewal is due and unit 23 S3's clear stages the record.
  In row 1 the record's session (`s1`) differs from the call's (`s2`), so `write_lease` is due and
  its branch's `stage_or_fail` stages the record. M2 rewrites the same paragraph, so fold the two
  together.
- **Left-shift gate:** a §10 checklist entry: "a sentence that quantifies over a table's rows
  ('in every row') is checked against each row."

## L4 · id=6 — S1's by-value inventory says no reader sees a different value, which is the opposite of the unit's purpose

- **Address:** TOOL-aGraftedHelix-24 §2 S1 Readers (by value), against §1 (Finding 11) and the §4
  interruption table.
- **Defect:** S1 says "by value: NO VALUE READERS, because the add writes the same members at an
  earlier point in the row, so no reader of the fact sees a different value". §1 and §4 row 2 say
  otherwise. After an interruption past `write_lease`'s `session` line, the set now holds `s1` where
  the old order left it without one. `check_claim_writable` and the restart row's membership test
  (unit 23 S4, S5) therefore read a different value on that path.
- **Impact:** the retirement inventory claims no reader observes a change, while the design exists
  so that the readers observe one. The next change could use this line to skip re-checking the set's
  readers on the interrupted path. No code is affected, because those readers already read the set
  and none of them changes.
- **Fix — the skeptic judged it SOUND:** change the line to "by value: `check_claim_writable`'s
  holder and status-write read and the restart row's membership test read `s1` after an interrupted
  `write_lease`, where they read nothing before. Neither changes, because each already reads the set
  (unit 23 S4, S5)."
- **Left-shift gate:** a §10 checklist entry: "a `NO VALUE READERS` claim is checked against the
  unit's own goal; a unit that exists to change what a reader sees has value readers."

## L5 · id=7 — §3 says this unit corrects only the sequence-d restart leg, but S2 and §7 also rewrite the sequence-c leg

- **Address:** TOOL-aGraftedHelix-24 §3 Non-goals (the restart legs), against §2 S2 and §7's second
  New arm.
- **Defect:** §3 says that of unit 23 AC5's restart legs "this unit corrects the sequence-d leg
  only". §7's second arm rewrites unit 23's sequence-c restart arm so its `--beat` runs with
  `CLAUDE_CODE_SESSION_ID` unset. That arm is unit 23 AC5's sequence-c leg. S2's supersession names
  unit 23 AC1 and AC4 and does not name AC5.
- **Impact:** the skeptic found the finder's impact overstated. S2's "wherever they run" already
  reaches the `--beat` inside AC5's sequence-c leg, and §7 names that arm, so a builder would not
  leave it under `s1`. Unit 23 AC5's own text names no session for that `--beat`, so no criterion
  text is contradicted. What remains is an overbroad "only" and an incomplete supersession list.
- **Fix — the skeptic judged it SOUND:** change §3 to "this unit corrects the sequence-d leg's
  starting point only; S2's session rule also reaches the `--beat` inside the sequence-c leg". Make
  S2 supersede "unit 23 AC1, AC4 and AC5's sequence-c leg for those calls".
- **Left-shift gate:** a §10 checklist entry: "a supersession list is checked against every §7 arm
  the unit rewrites; an arm rewritten under a criterion the list does not name is a missing entry."

## L6 · id=8 — S3 quotes a supersession anchor that does not exist in unit 23

- **Address:** TOOL-aGraftedHelix-24 §2 S3, the quoted supersession anchor.
- **Defect:** S3 supersedes unit 23 AC5's "when sequence d of section 4 runs". Unit 23 at HEAD is
  rev-4, and its AC5 (line 275) reads "When sequence d of §4 runs". The quoted string appears
  nowhere in unit 23; it appears only in the round-1 review prose.
- **Impact:** anyone tracing the superseded text by grep or by eye will not find it. The supersession
  is still identifiable, because AC5 has only one sequence-d clause and S3 also anchors on the §7
  arm's "after sequence d". The effect is cosmetic.
- **Fix — the skeptic judged it SOUND:** quote the text as written: "When sequence d of §4 runs".
- **Left-shift gate:** a check is cheap here: a spec lint that greps each quoted supersession
  anchor ("This supersedes unit N … \"…\"") against unit N's spec at the same tree and reds on a
  miss. Until then, a §10 checklist entry: "quote superseded text from the spec, never from a
  review's paraphrase of it."

## L7 · id=13 — S2's rationale misstates unit 1's row order and is false as the reason for keeping `--beat` off `s1`

- **Address:** TOOL-aGraftedHelix-24 §2 S2 (the sentence "None runs under `s1`, whose claim unit 1
  §4's same-session row answers before the widening is reached").
- **Defect:** unit 1 §4 "Who may write a claim" lists `mine`, where the widening lives, before
  `same session`, and unit 1 §4's renewal only works if `mine` wins. So "the same-session row answers
  before the widening is reached" misstates the order. It is also false as the reason for keeping
  `--beat` off `s1`. Unit 1 §4 "The two verbs" lets `--beat` write only through the `none` and
  `mine` rows, so a same-session claim prints `skipped`. That makes `--beat` under `s1`
  discriminating, as the skeptic's correction recorded in unit 23's round-1 H3 says. For
  `--dispatch` (take) and `--hold` (write), the same-session row also writes, so `s1` would mask a
  missing widening, which is the true reason.
- **Impact:** the behaviour S2 prescribes is correct, so behaviour is unaffected. The sentence
  contradicts the recorded correction. It could lead a builder of `check_claim_writable` to test
  same session before `mine`, which would defeat unit 1's renewal throttle. That function is unit
  1's to build, earlier in the order, so this unit's builder is unlikely to be the one misled.
- **Fix — the skeptic judged it SOUND:** rewrite the clause. `--dispatch` and `--hold` under `s1`
  reach the same-session row whenever the widening is absent, and that row writes, so they cannot
  red. `--beat` runs with the session unset because the OS-scheduled tick runs that way. Cite unit
  1 §4's row order, `mine` before `same session`.
- **Left-shift gate:** a §10 checklist entry: "a rationale that cites another unit's row order is
  checked against that unit's table and against any skeptic correction recorded on the same point."

## L8 · id=14 — §4 "The order" restates the whole table but drops two qualifiers from unit 20's rows

- **Address:** TOOL-aGraftedHelix-24 §4 "The order" (the clear row and the `stage_or_fail` row).
- **Defect:** §4 restates every step, but S1 supersedes only unit 20 §4's `prior-session` row. Unit
  20's `stage_or_fail` row reads "the index, when write_lease ran or the fact was written", and unit
  20 §4 and unit 23 S3 give a clear on a call with no `write_lease` due its own `stage_or_fail`. Unit
  24's table drops both: its `stage_or_fail` row is unconditional, and its clear row has no stage of
  its own. Unit 24 §5's risks call this table "the one place" the order is stated.
- **Impact:** there are now two answers to one order. A builder who follows the newer table can
  stage on every holder call, which spends a git spawn on every idle-wake tick against the row's
  documented "writes NOTHING unless" contract (`:6592`). Or the builder can leave a not-due clear
  unstaged. The defect is contained: S1 itself places the `stage_or_fail` inside the due branch, and
  the inventory confines the build to moving the add.
- **Fix — the skeptic judged it SOUND:** restore unit 20's qualifier on the `stage_or_fail` row
  ("when `write_lease` ran or `prior-session` was written"), and add "then its own `stage_or_fail`
  when `write_lease` was not due" to the clear row. Alternatively, show only the moved row and point
  at unit 20 §4 for the rest. If H1's promotion adds the add's failure rule, the add row is where it
  belongs.
- **Left-shift gate:** a §10 checklist entry: "a unit that supersedes one row of a sibling's table
  restates only that row and points at the sibling for the rest."

## L9 · id=15 — the rewritten sequence-d arm adds two executed assertions but its floor field says `none`

- **Address:** TOOL-aGraftedHelix-24 §7, the fourth New arm (the sequence-d restart arm), its floor
  field.
- **Defect:** the rewritten arm adds at least two assertions unit 23's arm never made: the set reads
  `s1 s2` and the claim names `s1` before the restart. TEMPLATE-SPEC defines the New-arm third field
  as "<assertion floor to move, or none>". TOOL-dDerivedDocket-61 §7, the `FLOOR_ASSERTIONS` and
  `FLOOR_SHARD_2` history in `unattended.test.sh`, and aGraftedHelix units 5 and 7 all raise the
  floor by exactly the assertions a unit adds, with a retargeted assertion moving none. Unit 23 AC5
  asserts only the restart's outcome, so cutting d's closing call most likely removes nothing from
  that arm.
- **Impact:** the shrink-only executed-assertion pin carries two more assertions of slack. If the
  new precondition assertions were later stranded or dropped, the floor would not register the loss.
  Nothing outside the suite's floor changes.
- **Fix — the skeptic judged it SOUND:** set the arm's floor field to `FLOOR_ASSERTIONS`, plus
  `FLOOR_SHARD_2` if the arm sits in region two, each raised by the assertions the rewrite adds,
  counted off the block. Keep `none` for the second and third arms, which only retarget sessions.
- **Left-shift gate:** a §10 checklist entry: "a New arm that rewrites a sibling's arm counts the
  assertions it adds, and its floor field is `none` only when it adds none."

## What a fold should do first

1. Promote H1. Its unit states the add's failure rule in S1, adds the failing-add leg to AC1 and
   stages the dropped `|| return 1`. Design M1's and M2's AC1 legs beside it, because the three legs
   share AC1's fixture and its `mktemp` shim.
2. Fold M1 and M2 in one rev with H1's promotion in view. One unreachable-remote fixture can carry
   both: an interrupted unreachable call, a still-unreachable call, then a call with the remote
   restored. Decide M2's option first, since the first option changes code and the second only text.
3. Fold L3 with M2: both rewrite §4's closing paragraph and both correct row 1's reason.
4. Fold L1, L2 and L4 in one rev: all three edit S1's text, its label and its readers line.
5. Fold L5 and L7 in one rev: both edit S2 or §3's account of which sessions the criteria use.
6. Fold L6, L8 and L9 last. Each is a one-line edit to an anchor, a table row or a floor field.

A review of the promotion spec should run with a checklist swept and an intent supplied. This round
had neither.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 2 S1 / section 6 AC1 | high | low | confirmed | The labelling defect is real. S1 says 'The clear keeps its place after write_lease' and tags the whole item 'Observed by AC1'. AC1's first call never lands a CAS, so it never runs the clear. Its second call has write_lease not due, so it cannot order the clear against write_lease. The claimed HIGH consequence does not hold, so the grade drops to low. Take an s3 call whose CAS lands and which is interrupted before write_lease's session line. It leaves the claim at s3 and the record at s2. With the clear after write_lease the set still holds s1, and with it moved ahead the set is empty. s3 is a member of neither, so the set decides nothing. Unit 1 section 4's holder column answers the next s3 call through its 'same session' row: the claim's session equals CLAUDE_CODE_SESSION_ID, so the call takes the claim and does not answer check 90. Unit 24 S2 relies on that same row answering before the widening. A caller under any other session gets the same verdict in both orders, because the set never holds the session a landed CAS just wrote. So no verdict depends on where the clear sits, and the only defect is an Observed-by label that no criterion discharges. Section 3's rationale for keeping the clear in place is also wrong for the same reason. The fix is unsound for two reasons. First, its stated red ('a following s3 call answers check 90') does not occur, because of the same-session row. Second, under a correct build its shim never fires, because the session line already reads s3 when the clear runs. The leg would therefore pass by finding nothing, and only the exit status would separate the two builds. | unsound |
| 2 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 2 S1 / section 6 AC1 | medium | medium | confirmed | S1 moves the add for both triggers in section 4's add row: the CAS did not complete, or the claim was unreadable. AC1 drives only the first, through the claim push exiting 124, but S1 claims AC1 observes the whole item. An unreachable remote makes the claim unreadable, and a build can reach the add from that branch separately. A build that leaves only that path's add after write_lease passes AC1 and every section 7 arm. On that path, an interruption after write_lease's session line leaves the record at s2, the claim at s1 and an empty set. The next s2 call has write_lease not due, so it reaches the claim through mine alone. Neither mine nor same session matches, and the call answers check 90. The consequence is contained to the unreachable-remote path combined with an interruption, so it is graded medium. The fix is sound. The mktemp shim's trigger works the same on that path: the add and write_lease's first two set_facts run while the session line still reads s1, and the pid line's mktemp fires the shim. The unreadable-path add records the pre-call session s1, so the asserted set and the unmoved lease-utc hold under a correct build, and the restored-remote call reads the claim as mine through the set. | sound |
| 3 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 2 S1 | low | low | confirmed | S1 contains 'The comment at the row names this order' and closes with 'Observed by AC1'. AC1 observes only run-state facts, the claim and exit codes, so no criterion can observe a comment. The sibling convention, unit 23 S6 and unit 20 S7, labels a prose or comment clause NOT OBSERVED with a reason. That is also the observed-by-claim-no-arm-discharges class the checklist selected for unit 23. The consequence is a comment that can go stale with every criterion still green, which has no effect on behaviour. | sound |
| 4 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 2 S1 (the clear sentence) against section 6 AC2 | low | low | confirmed | S1 says 'the next claim write that lands empties them'. Unit 23 S3, unit 23's section 3 non-goal and its title make the next --resume holder-row claim write that lands the only writer that empties the set. Unit 24's own AC2 asserts that the set still reads s1 after a landed --beat or --dispatch. So the clause is literally false for every writer except one. It sits in S1's rationale, and unit 23 S3 governs the build, so behaviour is unaffected. The cost is a misleading rationale that a comment could copy. | sound |
| 5 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 4 'What an interruption leaves', closing paragraph, against the same table's row 1 | low | low | confirmed | Section 4's interruption table, row 1 ('the add'), gives record session s1 and claim s1. The closing paragraph says 'in every row the claim it reads differs from the record's session'. That is false for row 1, and the same table says the row stages through 'write_lease due'. Its next s2 call stages because the record's session s1 differs from the call's s2. In rows 2 and 3 the stated reason does hold: the claim is s1 and the record is s2, so the renewal is due and unit 23 S3's clear stages the record. The defect is a false justification in prose. The table rows are right, so a builder working from them builds correct behaviour. | sound |
| 6 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 2 S1 Readers (by value) against section 1 Finding 11 and the section 4 interruption table | low | low | confirmed | S1's by-value line says 'no reader of the fact sees a different value'. Section 1 (Finding 11) and section 4 row 2 contradict it. The unit exists so that after an interruption past write_lease's session line, the set holds s1 where the old order left it without s1. check_claim_writable and the restart row's membership test (unit 23 S4, S5) therefore read a different value on that path. The statement is literally false. No code is affected, because those readers already read the set and none of them changes, so the consequence is confined to the inventory prose. | sound |
| 7 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 3 Non-goals (restart legs) against section 2 S2 and the second New arm in section 7 | low | low | confirmed | Section 3 says 'this unit corrects the sequence-d leg only'. Section 7's second arm rewrites unit 23's sequence-c restart arm so its --beat runs with CLAUDE_CODE_SESSION_ID unset. That arm is unit 23 AC5's sequence-c leg, whose sequence c contains the --beat. So the 'only' is contradicted. S2's supersession names AC1 and AC4 and does not name AC5. The finding overstates the impact. S2's 'wherever they run' already reaches the --beat inside AC5's sequence-c leg, and section 7 names that arm explicitly, so a builder would not leave it under s1. Unit 23 AC5's own text names no session for that --beat, so no criterion text is contradicted. What remains is an overbroad 'only' and an incomplete supersession list. | sound |
| 8 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 2 S3, the quoted supersession anchor | low | low | confirmed | Unit 23 at HEAD is rev-4, and its AC5 at line 275 reads 'When sequence d of §4 runs'. Unit 24 S3 at the pinned blob quotes 'when sequence d of section 4 runs', a string that appears nowhere in unit 23. It appears only in the round-1 review prose. Unit 24 uses '§4' freely elsewhere, so no gate forces the paraphrase. The supersession is still identifiable, because AC5 has only one sequence-d clause and S3 also anchors on the section 7 arm's 'after sequence d'. The effect is cosmetic. | sound |
| 9 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 4 Evidence (bullet 4) and 'What an interruption leaves' row 2 | medium | - | refuted | Both premises are true at base, but neither makes unit 24 wrong. (1) The due test at unattended.sh:6597 does compare only lease-utc presence, session and pid. A real s2 call whose CLAUDE_PID differs from the recorded pid therefore finds write_lease DUE after a stop between the session and pid lines. That is a harmless deviation from row 2: the due branch runs the mine test first against the record's pre-call facts with the set included (unit 20 S1, unit 24 section 4 The order). It reads the s1 claim as mine through the set, and then rewrites the whole lease and stages it. So the table's claim and next-call outcome are unchanged. (2) A partial lease left after write_lease's pid, host or pid-image line, with stale host, pid-image and lease-utc, comes from write_lease's own line order (:5557-5570). Base already has it with no claims at all, and the finding concedes the window exists at base. Unit 24 does not touch write_lease. Its scope is where the prior-session add sits relative to it. Its interruption table is scoped to an s2 call whose CAS did not complete, and its columns are record session, set, claim and next call. For those columns, a stop after pid, host or pid-image is identical to row 2 or row 3, so the table is not incomplete on what it claims to analyse. The lease-integrity defect (check_pid_alive reading a live holder as no under a stale lease-utc, lib-unattended.sh:413) is real, but it is a pre-existing write_lease defect for its own unit, not something this design introduces or certifies. Graded medium and not established against this spec, so refuted. | sound |
| 10 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 4 'What an interruption leaves', the paragraph under the table ('The next call stages it ...') | medium | medium | confirmed | The section 4 paragraph says the next call stages the interrupted record 'through the write_lease-due branch or through unit 23 S3's clear'. That holds only when the next call's write_lease is due or its claim write lands. On a not-due call, unit 23 S2 adds nothing, and unit 23's set table reads 'write_lease not due, and no claim write lands: unchanged, and nothing is written'. S3's clear, and its stage_or_fail, run only after a landed claim write. The only other staging point is the stage_or_fail inside the due branch (:6597-6600). The rest of the not-due path stages nothing (run_orphan_reap, verb_status, print_resume_orientation). After rows 2 and 3 under the fixture's unchanged pid, or after row 3 or a stop past pid in a real new session, every call during a continuing outage leaves the record's s2 and prior-session lines unstaged. That outage is the condition that left the CAS incomplete in the first place. stage_or_fail's own header (:2620-2628) says an unstaged run is invisible to every check the gate leg has, because that leg's per-run population is the index. The stated reason is also false for row 1: there the record and the claim both read s1, and staging comes from the due branch because the environment's session differs from the record's. No criterion drives an interrupted call followed by a still-incomplete one, and AC1's second call runs with no shim, so the claim lands. The effect is contained: it heals when a claim lands or another writer stages the file. Correction to the finding's impact: --hold's check_clean (:1975-1984) counts staged paths as well as unstaged ones, so staging alone would not clear check 2. | sound |
| 11 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 2 S1 (no rule for the add's own failure); section 6 AC1 | high | high | confirmed | S1 orders the add before write_lease's first set_fact, but no sentence says the row must stop when the add's own write fails. Section 4 Evidence states the failure rule for write_lease only (':6599 ... returns when write_lease fails'), and the interruption table starts from 'stopped after the add'. It never covers an add that failed while the row went on. set_fact returns 2 without writing when mktemp fails (:5528), and it returns mv's status unchecked. The `\|\| return 1` suffix is a convention, not a gate: base has set_fact calls chained without it, for example :7662. Take a build that writes the add without a return, after a one-off failure of the add's set_fact (a transient mktemp failure, or an mv failure under a Windows file lock). It continues into write_lease, which succeeds, and leaves the record at s2, the claim at s1 and no s1 in the set. The next s2 call is not due under an unchanged pid, reads the claim as foreign and answers check 90, or check 89 at the restart row. That is the claim-lost abort H1 was promoted to prevent. AC1's shim fires only once the record reads s2, which is after the add, so it cannot tell the two builds apart, and no section 7 arm stages the missing return. The consequence is a wrong verdict that forces the run's abort on a narrow path, which is high. | sound |
| 12 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 2 (no scope item); section 4 Files touched | medium | - | refuted | The claim that no memory/gotchas class names H1's exact rule is accurate: destructive-step-before-its-precondition.md is adjacent but distinct. But the missing record does not make unit 24 unbuildable or wrong. BUILD-METHOD (memory/guides/BUILD-METHOD.md:263-264) states the obligation as 'a regression gate, OR a memory/gotchas/ class when the class cannot be gated'. Unit 24's section 7 first new arm is that gate: it interrupts write_lease after its session line, and it is observed red with the add moved back after write_lease. The audit's extra section 10 entry is a build-level left-shift, not a design element. This repo routinely records such classes in separate records(...) commits outside any unit spec (for example 26b48c68c and 211d184df), so a spec without a scope item for it does not mean the class will go unrecorded. The design's behaviour is the same with or without the record, so even if the finding were confirmed its consequence would be documentation only, which is low. Graded medium and not established as a spec defect, so refuted. | sound |
| 13 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 2 S2 (the sentence 'None runs under s1, whose claim unit 1 §4's same-session row answers before the widening is reached') | low | low | confirmed | Real. Unit 1 §4 'Who may write a claim' lists mine (where the widening lives) before same session, and unit 1 §4 Renewal only works if mine wins. A holder's claim, record and env sessions are normally all equal, so 'renew when due' requires mine to take precedence over same session's 'take'. So S2's 'same-session row answers before the widening is reached' misstates the order. It is also false as the reason for keeping --beat off s1. In sequence a after the incomplete s2 call, the claim is s1, the record s2 and the set s1. A widened build reads that claim as mine and renews. A build with no widening reads it as same session, and unit 1 §4 'The two verbs' makes --beat skip there. So --beat under s1 discriminates, which is the skeptic's correction recorded in the unit 23 round-1 review H3. For --dispatch (take) and --hold (write), the same-session row also writes, so s1 would mask a missing widening. That is the true reason. The behaviour S2 prescribes, --beat unset and --dispatch and --hold under s2, is correct. Only the rationale sentence is wrong, and check_claim_writable is unit 1's to build, earlier in the order. Graded low. | sound |
| 14 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 4 'The order' (the clear row and the stage_or_fail row) | low | low | confirmed | Real. Unit 24 §4 'The order' restates every step. Its stage_or_fail row carries no condition, while every sibling conditional row says 'when due'. Unit 20 §4's row reads 'the index, when write_lease ran or the fact was written'. The base comment at unattended.sh:6592 says the row 'writes NOTHING unless' write_lease is due. Unit 24 §5 risks calls this table 'the one place' the order is stated. S1 supersedes only the prior-session row, so the dropped qualifier is an unflagged divergence. The defect is contained. S1 itself says the stage_or_fail sits 'inside the write_lease-due branch', and §4's prose names the staging 'through unit 23 S3's clear'. Inventory confines the build to moving the add, so a unit-24 builder is unlikely to restructure staging. The literal table is still a second, lossy answer to unit 20's order. Low. | sound |
| 15 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 7, the fourth New arm (the sequence-d restart arm), its floor field 'none' | low | low | confirmed | Real. TEMPLATE-SPEC defines the New-arm third field as '<assertion floor to move, or none>'. TOOL-dDerivedDocket-61 §7 (lines 1044-1051), the FLOOR_ASSERTIONS and FLOOR_SHARD_2 history in unattended.test.sh (12308-12470), and aGraftedHelix units 5 and 7 all follow one practice: raise the floor by exactly the assertions a unit adds, with a retargeted assertion moving none. Unit 24's fourth arm adds two precondition assertions unit 23's restart arm never made, the set reading s1 s2 and the claim s1. Unit 23 AC5 asserts only the restart's outcome, not sequence d's closing call, so cutting the closing call most likely removes nothing from that arm. Yet the floor field says 'none'. The second and third arms do only retarget sessions. The effect is that the shrink-only pin carries two more assertions of slack. Nothing outside the suite's floor changes, so low. | sound |
| 16 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-24.md:section 6 fixture preamble and AC1 (the interrupted first call) | low | - | refuted | Not established. Unit 24's §6 preamble restates unit 23's fixture paragraph component by component and leaves out unit 23's closing sentence, 'After every call, git diff --name-only names no run-state file'. That sentence is a criterion-wide assertion of unit 23's criteria, not part of the setup that 'The fixture is unit 23's' imports. Unit 20 likewise carries its per-call diff assertion inside AC2, not in its fixture. Unit 24 also states what the finding says is missing. §4 says 'Each interrupted call leaves the record unstaged. The next call stages it', and AC1 places the git diff --name-only assertion on the second call only. Unit 20 §4's 'a call that writes it leaves no unstaged record' describes a completed call. Under unit 20's own order, an interrupted write_lease also returns before stage_or_fail, so that sentence never covered interruption and needs no supersession. The builder-reuses-a-helper hazard is speculative. Any red it caused would be observed and resolved by §4's own text. The finder graded it low, so it is refuted. | sound |
