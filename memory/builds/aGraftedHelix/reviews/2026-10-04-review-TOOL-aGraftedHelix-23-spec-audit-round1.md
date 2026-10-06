**Serves:** spec-audit TOOL-aGraftedHelix-23

# aGraftedHelix — Tier-2 spec audit of unit 23, ROUND 1

*Node `a`, 2026-10-04, ROUND 1 for this subject. Unit 23 promotes the HIGHs of the round-1 audit of
units 20 to 22 (that round's findings 1, 2, 6, 7 and 12). It makes unit 20's `prior-session` fact a
set, moves its read into `check_claim_writable`, and drives the sequences that audit named. Four
lenses ran: underspecification, contradiction, unstated assumption and prior art. Every finding in
the body survived a skeptic prompted to REFUTE it. The four findings the skeptics refuted appear
only in the appendix. The author of this report confirmed that the pinned blob below is the blob at
HEAD (`ec4d17e92`), by `git rev-parse HEAD:<path>` against `git hash-object <path>`. That blob is
the spec's rev-2. Four rows were spot-checked in the tree. For H1, `write_lease` writes `session` at
`tools/unattended/unattended.sh:5563`, between `keepalive` and four more `set_fact` calls, each
ending `|| return 1`. For M1, the holder row's only `stage_or_fail` sits inside the
`write_lease`-due branch (lines 6597 to 6600), under a comment at 6592 saying the row writes NOTHING
otherwise. For M4, `run_hold` calls `check_clean` with no argument at line 4918, and
`scan_dirty_paths` counts `git diff --cached` at line 1966. For H2, the spec's §7 restart arm reads
"after sequence d" (spec line 258). The other rows carry the skeptics' verified text and were not
re-derived here.*

**Reviewed at ROUND 1, the subject pinned at its blob:** `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md`@`d560a89d2014ba58d16569b4523024fe7dce3c51`.

## Verdict: CLEAN WITH FIXES

No confirmed finding is graded BLOCKER, so the spec is buildable as written. The verdict is not
CLEAN, because twelve confirmed findings stand and three of them are HIGH. Two of the HIGHs are
criteria that cannot reach the path they certify. The third is a crash window in the order S2
inherits, and it ends in the outcome this unit exists to prevent: a live run reading its own claim
as foreign and being forced to `--abort --code claim-lost`.

- H1 (id 11): S2 adds to the set after `write_lease` has already moved the record's `session`, so a
  failure or kill between the two leaves a claim no member names, and the next call answers check
  90 or 89.
- H2 (id 6): AC5's restart runs after sequence d's closing call, which empties the set, so the
  restart is a plain same-session match and S5's membership test is never reached.
- H3 (id 1): AC4's `--hold` names no session, so run under the fixture's s1 it writes through the
  same-session row and never exercises the widening it is the only criterion for.

Seven findings are MEDIUM and two are LOW. Adjudicated, the twelve confirmed findings form nine
items. Two merges were made, each within one binding grade. Ids 2, 7 and 12 (all medium) are one
defect in S2: the add has no `write_lease`-due scope and no `stage_or_fail`, so an offline renewal
dirties the record. Ids 3 and 16 (both medium) are one defect at the restart row: S1's supersession
leaves unit 20 S8's "when that is not `absent`" guard standing, and AC5 never reaches a member other
than the first. No binding grade was changed. The skeptic re-graded id 9 from medium to low, and
this report keeps that grade.

Two fixes interact and should be folded as one. H1's fix moves the add BEFORE `write_lease`, and
M1's fix confines the add to calls whose `write_lease` is due. Together they put the add inside the
due branch, ahead of `write_lease`, where the branch's existing `stage_or_fail` stages it. H3's fix
and M4's fix also touch the same AC4 leg: run `--hold` under s2, after committing and pushing the
staged record.

Disposition, per `memory/guides/BUILD-METHOD.md`: every CONFIRMED finding is disposed by severity.
Each HIGH is promoted to a unit whose mechanism closes it, audited as a SPEC. Each MEDIUM and LOW is
folded into this spec as a rev bump with a §9 line. Unit 23 is itself a promotion, so promoting H1
to H3 extends the chain by one more link. The method ends a chain at a promoting round whose stated
precision falls below the review protocol's floor. This round's precision, stated for that rule to
read, is 0.75.

## Review shape

Intensity full. Raw 16, confirmed 12, refuted 4 (ids 4, 5, 8 and 13), unverified 0 (0 uncertain),
precision 0.75.

The adjudicated tally, counted both ways:

| severity | items | raw confirmed findings |
|---|---|---|
| BLOCKER | 0 | 0 |
| HIGH | 3 | 3 |
| MEDIUM | 4 | 7 |
| LOW | 2 | 2 |
| **total** | **9** | **12** |

By lens, raw then confirmed: underspecification 5 and 3, contradiction 5 and 4, unstated
assumption 4 and 3, prior art 2 and 2.

The prior-art lens went from six findings refuted of six in the round-1 audit of units 20 to 22 to
two confirmed of two here. Both of its findings cite a recorded decision or a sibling unit's clause
that this spec leaves standing.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 4 of 4 returned, 0 DIED.
- 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and 0
  duplicates were found.
- Fixes on confirmed findings: 12 judged sound, 0 judged UNSOUND, 0 with no fix proposed, and 0
  NOT JUDGED. An unjudged fix would be the finder's proposal and nothing more; none occurs here.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, so none is bound at the finder's grade
  by default. 1 was RE-GRADED by the skeptic: id 9, from medium to low.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, and 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.

This report does not call the run complete. Every lens and every skeptic batch returned, but no
checklist was swept, no intent was supplied, and every lens ran on the generic brief.

**Intent:** NEITHER `specs` nor `context` was supplied to this review. The lenses graded the spec
against itself, against the units it consumes from (units 1 and 20) and against the tree, not
against a stated intent for the build.

**Checklist:** NONE swept — absent. The count of recurring-bug-class findings in this report is
therefore not evidence that the project's recurring classes are absent from this spec. This is the
fourth consecutive round of this build with no checklist. A caller of the next round should pass the
output of `python tools/memory-tree/gotchas.py --for-paths` over the spec's Files-touched paths.

## How the findings cluster

A fold that repairs a class repairs every row in it, so the classes are named here before the rows.

| class | ids | where the gate belongs |
|---|---|---|
| S2's add has no position and no scope: where it runs relative to `write_lease`, which calls it runs on, what it stages, what it does with an empty value | 11, 2, 7, 12, 14 | one arm in `tools/unattended/unattended.test.sh` per call shape: interrupted inside `write_lease`, offline renewal-only, empty pre-call session |
| A criterion or staged break that cannot reach the path it certifies | 6, 1, 3, 16, 10 | the staged break observed RED at VERIFYING, plus a §10 checklist entry |
| A leg that cannot go green on a correct build, because a recorded decision refuses its precondition | 15 | a §10 checklist entry |
| Descriptive prose stating a looser rule than the S-line it summarises | 9 | a §10 checklist entry |

The second class is the one this build keeps paying for. The round-1 audit of units 20 to 22 named
an `Observed by` label that no criterion reads, and a staged break that cannot red its arm, as two
recurring classes and asked for a spec lint. That lint has not been built. Here the class holds two
of the three HIGHs.

Ids appear in more than one class where the defect has two faces. Each id still sits in exactly one
graded item below.

# HIGH

## H1 · id=11 — S2 adds to the set after `write_lease` has moved the record's `session`, so an interruption between them leaves the claim under a session no member names

- **Address:** TOOL-aGraftedHelix-23 §2 S2 (the "before its `stage_or_fail`" clause), with §3 Edges
  and unit 20 §4 "The order".
- **Defect:** unit 20's order runs the CAS, then `write_lease`, then the prior-session write, then
  `stage_or_fail`. S2 pins the add only "before its `stage_or_fail`", so the add follows
  `write_lease`. That assumes nothing stops the row between the two. But `write_lease`
  (`tools/unattended/unattended.sh:5559-5570`) is six sequential `set_fact` calls, each ending
  `|| return 1`. It writes `session` at line 5563 with four more after it, and `set_fact` returns 2
  when `mktemp` fails. The holder row returns when `write_lease` fails (line 6599), and the kit
  already names an in-call crash window at line 6576.
- **Impact:** a holder call whose push did not complete then fails or is killed after
  `write_lease`'s `session` line and before the add. The record reads `session: s2`, the claim `s1`,
  and the set holds no `s1`. The same-keepalive retry reads its own claim as foreign `live` and
  answers check 90. A relaunch at the restart row fails S5's membership test and answers check 89.
  Either way the live run is forced to `--abort --code claim-lost`, the outcome this unit and unit 20
  exist to prevent. The path is narrow, and made likelier because a push that exits 124 has already
  spent the call's time. No criterion or arm interrupts the row.
- **Fix — the skeptic judged it SOUND:** in S2, require the add (its `set_fact`) to run after the
  CAS outcome and the claim read, both known before `write_lease` under unit 20's order, and BEFORE
  `write_lease`. Restate that row in §4. Add an arm with a `set_fact` or `mktemp` shim that fails
  `write_lease` after its `session` line, asserting that the next holder call is not check 90.
  Fold this with M1's fix, as the Verdict section says.
- **Left-shift gate:** that arm in `tools/unattended/unattended.test.sh`, observed RED with the add
  placed after `write_lease`. Add a §10 checklist entry: "a fact that protects a record field from a
  partial write is written before the first write that can move that field, not after the batch."

## H2 · id=6 — AC5's restart runs after sequence d's closing call, which empties the set, so S5's membership test is never reached

- **Address:** TOOL-aGraftedHelix-23 §6 AC5 and §7 (the restart arm), against §4 The sequences.
- **Defect:** §4 defines every sequence as ending in a closing `--resume` call that lands, and AC1
  reads "sequences … run" to include that call. Read the same way, AC5's "when sequence d of
  section 4 runs and the next call is under s3" and the §7 arm's "after sequence d" put the restart
  after the closing s3 call. By S3 that call empties the set and leaves the claim at s3. The restart's
  claim session then equals `CLAUDE_CODE_SESSION_ID` s3, which is unit 1's plain same-session row.
  AC5's own "the remote restored" only makes sense right after d's second unreachable call, so the
  text contradicts the state it intends.
- **Impact:** built as written, the AC5 arm passes with or without S5. Its staged break ("the
  restart widening comparing the whole value") runs over an empty set, finds the claim already
  same-session, and stays green, so the arm certifies S5 without reaching it. The red-first rule in
  §5 would most likely stall the pass on a reinterpretation rather than let a vacuous arm land, which
  is why the grade is HIGH and not BLOCKER.
- **Fix — the skeptic judged it SOUND:** have AC5 and the §7 arm read "sequence d up to, but not
  including, its closing call", and assert that the set reads `s1 s2` and the claim names
  `session: s1` immediately before the restart call.
- **Left-shift gate:** the corrected arm, observed RED under its whole-value staged break. Add a §10
  checklist entry: "a criterion that runs after a named sequence states whether the sequence's
  closing call has run, and asserts the state it needs before the stimulus."

## H3 · id=1 — AC4's `--hold` names no session, so under the fixture's s1 it never exercises the widening it is the only criterion for

- **Address:** TOOL-aGraftedHelix-23 §6 AC4 (the `--hold` leg), and AC1 sequences a and b (the
  `--beat` and `--dispatch` legs).
- **Defect:** AC4 names s2 for its `--dispatch` ("a `--dispatch` follows under s2") but no session
  for its `--hold`, and the fixture defines a session only for holder calls. `--hold` has no
  lease-session binding (`run_hold`, `unattended.sh:4837`, never calls `check_keepalive_reaped`).
  Under s1 the claim's session equals the environment's, so unit 1 §4's same-session row (status
  write: write) writes `held` with no prior-session widening at all.
- **Impact:** AC4's `--hold` is the only criterion S4 says drives a status-write site. The §7 arm's
  staged break (the set supplied from the `--resume` row only) reds through the s2 `--dispatch` leg,
  so an s1 `--hold` never has to red. A build that reads the set in `check_claim_writable` for
  holder mode only then passes. In that build `--hold`, `--landed`, `--abort` and the LANDING
  re-bind announce instead of writing after an incomplete holder push, and the published claim stays
  live under the old session while the run is held, landed or aborted. The path is narrow, not
  certain: the suite's global default is `CLAUDE_CODE_SESSION_ID=fixture-session`
  (`unattended.test.sh:483`), which would not be vacuous.
- **Skeptic's correction to the finding, kept here:** `--beat` under s1 is not vacuous. Unit 1 §4
  "The two verbs" makes `--beat` write only through the `none` and `mine` rows, so a same-session
  claim prints `skipped`, and AC1 already requires `renewed`. AC1 b's `--dispatch` under s1 would
  take through the same-session row, but AC4's s2 `--dispatch` covers holder mode.
- **Fix — the skeptic judged it SOUND:** name the session on every call that is not `--resume`. Run
  `--hold` and AC1 b's `--dispatch` under s2, and run AC1 a's `tick --beat` with
  `CLAUDE_CODE_SESSION_ID` unset or s2, never s1. Add to AC1's "Red when": "`--beat` prints a
  skipped line". Fold with M4, which changes the same `--hold` leg's setup.
- **Left-shift gate:** a staged break in the §7 arm that supplies the set in holder mode only,
  observed RED through the `--hold` leg on its own. Add a §10 checklist entry: "every criterion call
  names its session; a call that inherits the fixture's session is checked against the same-session
  row before it is trusted to exercise a widening."

# MEDIUM

## M1 · id=2, id=7, id=12 — S2 adds to the set on calls with no `write_lease` due and no `stage_or_fail`, so an offline renewal dirties the record

- **Address:** TOOL-aGraftedHelix-23 §2 S2; §2 S3; §4 "The set across one `--resume` holder-row
  call"; the §6 fixture preamble.
- **Defect:** S2 adds to the set on any `--resume` holder-row call whose CAS did not complete or
  whose claim could not be read, with no `write_lease`-due scope, and places the add "before its
  `stage_or_fail`". The row's only `stage_or_fail` sits inside the `write_lease`-due branch
  (`unattended.sh:6597-6600`), under a comment at line 6592 saying the row writes NOTHING otherwise.
  S3 gives the clear a `stage_or_fail` of its own; S2 gives the add none. Unit 1's Renewal reads the
  claim on every holder call, including the idle-wake tick, and renews it when the beat is a quarter
  of the bound old with nothing else due. §4's table also answers that call twice: "the claim
  unreadable" adds, "no claim write due" leaves the set unchanged, and no precedence is stated.
- **Impact:** the first offline tick of an outage, or a renewal whose push exits 124, under the
  recorded session and pid, adds `prior-session: <the current session>`. That member does nothing,
  because `mine` already accepts the record's own session. The run-state file is left modified and
  unstaged, which falsifies §6's "after every call, `git diff --name-only` names no run-state file"
  and breaks the holder row's write-nothing contract in unit 20 §4. When the network returns, the
  next landed renewal clears the set and stages a record change, so every network blip now restages
  the record. None of sequences a to f drives this path: sequence e changes `CLAUDE_PID`, which makes
  `write_lease` due. Unit 20's "The order" stages "when `write_lease` ran or the fact was written",
  which partly mitigates the unstaged outcome for a builder who reads it, but the S2/S3 asymmetry
  and the table overlap remain.
- **Caveat on one citation (id 12):** unit 1 AC13 removes the `SKILL.template.md:38` sentence that
  finding cites, so that citation is stale. The write-nothing contract still stands in unit 20 §4 and
  in the code comment.
- **Fix — the skeptics judged all three SOUND; merged:** confine S2's add to calls whose
  `write_lease` is due, and say so in §4's table: on any other call the pre-call session is the
  current one, and a claim that passed `mine` carries that session or an existing member, so there
  is nothing to add. Make the "claim unreadable" row conditional on that. (The alternative two
  skeptics also accepted, giving the add its own `stage_or_fail` as S3 does, keeps the useless
  member and the restage per outage; prefer the confinement, which also composes with H1's fix.) Add
  a criterion: an unchanged-session, unchanged-pid `--resume` with an aged beat and a claim push
  that exits 124 exits 0, leaves `git status --porcelain` empty, and writes no `prior-session` line.
- **Left-shift gate:** that criterion as an arm, observed RED under S2 as written. Add a §10
  checklist entry: "an S-line that adds a write to a row names the row's existing staging point, or
  states its own."

## M2 · id=3, id=16 — S1 leaves unit 20 S8's "when that is not `absent`" guard standing, and AC5 never reaches a member other than the first

- **Address:** TOOL-aGraftedHelix-23 §2 S1 (the supersession sentence) and S5; §6 AC5.
- **Defect:** unit 20 S8 (rev-4) widens the restart row with the record's prior-session fact "when
  that is not `absent`". S1 supersedes unit 20's reading of `absent` for S2 and S3 only, and S5 says
  only that S8 "tests membership". A builder converting S8 to membership can keep the guard on the
  fact's value. AC5 drives the restart only from sequence d, where the claim is s1, the set's FIRST
  member, and the set never holds `absent`. So a build that keeps S8's guard, or one that compares
  only the first member, passes AC1 to AC6. Unit 20 is built first (order 4), so its build already
  carries the guard.
- **Impact:** a run leased with `CLAUDE_CODE_SESSION_ID` unset reads (k1, `absent`) in record and
  claim. An s2 holder call whose push exits 124 leaves the record at s2 and the set `{absent}`. A
  relaunch as s2 under a new pid and keepalive sets `restart=1` (`unattended.sh:6612-6615`), reads
  the fresh claim as foreign live, and the take-over column answers check 89. The run is locked out
  until the beat ages past `RESUME_STALE_BOUND`, and the take is then logged as a foreign stale one.
  A relaunch after sequence a, b or c, where the claim is the set's second member, fails the same way
  under a first-member compare. The path is narrow and heals after the bound.
- **Fix — the skeptics judged both SOUND; merged:** extend S1's supersession sentence to name unit
  20 S8's "when that is not `absent`" clause, and have S5 state that an `absent` member counts at the
  restart row. Add legs to AC5, each with a §7 arm: after sequence c, an s3 restart under a new
  keepalive and `CLAUDE_PID` takes over with no check 89; and, with the fixture leased under
  `CLAUDE_CODE_SESSION_ID` unset, an s2 holder call whose claim push exits 124, then an s2 call with
  `CLAUDE_PID` changed and a new `--keepalive-id`, takes the run over, prints no
  `UNATTENDED check 89 FAILED`, and leaves a claim naming the new keepalive and session s2. Stage
  the restart widening skipping an `absent` member, and comparing the first member only.
- **Left-shift gate:** those arms, each observed RED under its staged break. Add a §10 checklist
  entry: "a supersession sentence lists every clause of the superseded unit that reads the value
  being redefined, found by grep for the value, not by memory of the S-lines."

## M3 · id=10 — two Red-when clauses have no staged break in §7, so the S3 "only when non-empty" guard is never observed red

- **Address:** TOOL-aGraftedHelix-23 §7 New arms, against §6 AC1 and AC2 Red-when, and §2 S3.
- **Defect:** §7's six arms stage the absent-only rule, the claim-only set, the unconditional
  pre-call write, absent-as-no-fact, the `--resume`-only reader and the whole-value restart compare.
  None stages S3's "only when non-empty" guard, so AC2's `git status --porcelain` assertion
  ("a landed holder write over a record without the fact writes it") is never observed red. Rev-2
  says AC2 observes that guard, which is an observed-by claim no arm discharges. The finder
  overstated the AC1 half: a build that empties the set on a landed `--beat` or `--dispatch` leaves
  it reading s2, not `s1 s2`, before the closing call, and that assertion is observed red under the
  a/b/c arm's absent-only break. Only an ADDING variant at `--beat` or `--dispatch` escapes an
  observed assertion there.
- **Impact:** §5 requires every arm to be observed RED on its staged break first, yet the assertion
  guarding S3's non-empty rule never is, and could pass vacuously. The guarded defect is contained: a
  record restaged on every landed `--resume` renewal.
- **Fix — the skeptic judged it SOUND:** add a staged break to the a/b/c arm, "`--beat` (and
  `--dispatch`) empties the set when its claim write lands", with the assertion that the set reads
  s1 after it observed red. Add a staged break to the e/f arm, or a new arm, "the clear written
  whether or not the set is non-empty", with AC2's `git status --porcelain` assertion observed red.
- **Left-shift gate:** those staged breaks, each observed RED at VERIFYING. This is the
  observed-by-claim class the round-1 audit of units 20 to 22 asked a spec lint for: every Red-when
  clause maps to a §7 staged break that reds it.

## M4 · id=15 — AC4's second `--hold` leg runs over a staged record, which `--hold` refuses by a recorded decision, so a correct build can never pass it

- **Address:** TOOL-aGraftedHelix-23 §6 AC4 (the second fixture copy's `--hold` leg); §7 New arm 5.
- **Defect:** unit 20 S2 has the incomplete holder call run `write_lease` and the prior-session
  write, then `stage_or_fail`, leaving the run-state file in the index. AC4 runs `--hold` straight
  after it. `run_hold` calls `check_clean` with no argument (`unattended.sh:4918`) before any write,
  and `scan_dirty_paths` counts `git diff --cached` (line 1966). The `check_clean` header (lines 1969
  to 1973, TOOL-dDerivedDocket-61 S8) records that `--hold` and `--preflight` pass nothing, so both
  refuse even a lease-only difference. `VERBS.template.md` lists a dirty tree among `--hold`'s
  pre-write refusals, and `unattended.test.sh:2826-2830` commits a record before every hold for this
  reason.
- **Impact:** on a correct build the leg ends in `UNATTENDED check 2 FAILED` and the claim still
  reads `live`, so it can never go green. Its Red-when misdiagnoses the failure ("announces instead
  of writing"), and the obvious repair, passing the run-state file to `--hold`'s `check_clean`,
  reverses a recorded decision. `--dispatch` does not call `check_clean`, so AC4's first leg and
  AC1's sequence b are unaffected. The effect stays inside one acceptance leg and its arm.
- **Fix — the skeptic judged it SOUND:** in AC4's second copy, after the incomplete s2 call, commit
  the staged run-state file and push the run branch with no shim. That push does not touch
  `refs/gov/runs/<slug>`, so the claim still names s1 and the set still reads s1; assert both. Then
  run `--hold`, under s2 per H3. Say in AC4 that the commit and push are there to satisfy `--hold`'s
  clean-tree and published-tip refusals, citing TOOL-dDerivedDocket-61 S8, so nobody exempts the
  record instead. Mirror this setup in §7's fifth arm, using the suite's `build_hold_fixture` shape
  (`unattended.test.sh:2826-2830`).
- **Left-shift gate:** the leg observed GREEN on the base plus the fix before its staged break is
  observed RED. Add a §10 checklist entry: "a criterion that invokes a verb satisfies that verb's
  documented pre-write refusals in its setup, and says which decision each setup step answers."

# LOW

## L1 · id=9 — the title, §3 and §5 say any landed holder write empties the set; S3 says only a `--resume` holder-row claim write does

- **Address:** TOOL-aGraftedHelix-23 title, §3 "Bounding the set", §5 perf/scale and §5 migration,
  against §2 S3 and §4 sequences a and b.
- **Defect:** four places say the set is emptied by "the next/first holder write that lands": the
  title, §3 ("the first holder write that lands empties the set, so it grows only across one
  outage"), §5 perf, and §5 migration. S3 confines emptying to the next `--resume` holder-row claim
  write that lands. S4 and unit 1's call-site table count `--beat`, `--dispatch` and `--close` as
  holder sites, and AC1 requires a landed `--beat` or `--dispatch` to leave the set unchanged, so
  sequence a grows the set across two incomplete pushes with a landed `--beat` between them. The
  non-goal that waives a bound rests on a premise the spec's own sequence a disproves.
- **Grade:** the finder graded medium; the skeptic re-graded it low, and this report keeps low. S3,
  AC1 and the adjacent "Emptying the fact from other writers" non-goal state the rule consistently.
  S6 makes the shipped comments and stops guide name the `--resume` row as the one writer, and AC1's
  "set reads `s1 s2` before the closing call" reds a build that empties on `--beat`. Built as
  written, behaviour is unaffected; the defect stays in the spec's descriptive prose.
- **Fix — the skeptic judged it SOUND:** reword the title, §3 "Bounding the set", §5 perf/scale and
  §5 migration to "the next `--resume` holder-row claim write that lands". Restate the bound: at
  most two members per incomplete `--resume` call, deduplicated by session, kept until a `--resume`
  claim write lands, whatever other holder writes land in between.
- **Left-shift gate:** a §10 checklist entry: "a title or non-goal that summarises an S-line is
  re-read against the S-line on every fold that touches either."

## L2 · id=14 — S2 states no rule for an empty pre-call session or a `none` claim read

- **Address:** TOOL-aGraftedHelix-23 §2 S2; §4 Evidence.
- **Defect:** S2 adds "the record's session fact as it stood before the call" and, "when the claim
  read succeeded", "the claim's session field", with no rule for an empty value. A claim read that
  finds no claim succeeds (unit 1's `none` row, which creates) and has no session field. The holder
  row's write branch also runs on a pre-lease record with no `lease-utc` (`unattended.sh:6597`),
  whose session it prints as `${os:-none}` (line 6601), so the pre-call session can be empty. §4
  Evidence's "a recorded session is never empty" covers only what `write_lease` wrote.
- **Impact:** a literal join stores `s1 ` or a doubled or leading space. `fact` strips only leading
  spaces (line 1129), so the stored bytes differ from S1's one-space form. Membership and every
  verdict are unaffected, and a `none` claim is created again on the next call whatever the set
  holds. The consequence is cosmetic.
- **Fix — the skeptic judged it SOUND:** state in S2 that an empty pre-call session and a `none`
  claim read add nothing to the set.
- **Left-shift gate:** fold an assertion into H1's or M1's arm that the stored `prior-session` line
  matches S1's one-space form exactly. No separate arm is worth its cost.

## What a fold should do first

1. Promote H1 to H3 together. One promotion unit can close all three, because each is about where
   the set is written or which call exercises it. It moves the add ahead of `write_lease` with an
   interrupting arm (H1), runs AC5's restart before sequence d's closing call (H2), and names a
   session on every non-`--resume` criterion call, running `--hold` under s2 (H3).
2. Fold M1 and L2 in one rev with H1's promotion in view, since all three redefine S2's add. M1's
   confinement to `write_lease`-due calls and H1's placement before `write_lease` are one rule.
3. Fold M2 and M3 in one rev: both add §7 arms and staged breaks, M2 at the restart row and M3 for
   S3's non-empty guard and the `--beat` and `--dispatch` writers.
4. Fold M4 with H3's promotion in view, since both rewrite the same AC4 `--hold` leg.
5. Fold L1 last, in whichever rev touches S3, so the title and §3 and §5 are re-read against the
   final S3.

A review of the promotion spec should run with a checklist swept and an intent supplied. None of
the last four rounds of this build had either.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:section 6 AC4 (the --hold leg), and AC1 sequences a and b (the --beat and --dispatch legs) | high | high | confirmed | AC4 names s2 for the --dispatch ('a --dispatch follows under s2') but names no session for the --hold, and the fixture defines a session only for holder calls ('A holder call is ... under the session named'). --hold has no lease-session binding (run_hold, unattended.sh:4837, never calls check_keepalive_reaped). Unit 1 section 4 gives the status-write column 'same session -> write', so a --hold run with CLAUDE_CODE_SESSION_ID=s1 writes held over the s1 claim without the prior-session widening. AC4's --hold is the only criterion S4 says drives a status-write site, and the section 7 arm's staged break (the set supplied from the --resume row only) reds through the s2 --dispatch leg, so an s1 --hold never has to red. A build that reads the set only in holder mode then passes, which is a check certifying a widening it never exercised, on the narrow path where the arm runs --hold under s1. The suite's global default is CLAUDE_CODE_SESSION_ID=fixture-session (unattended.test.sh:483), which would not be vacuous, so the path is narrow, not certain. One part of the finding is wrong: --beat under s1 is not vacuous. Unit 1 section 4 'The two verbs' says --beat writes only through the none and mine rows and every other row is skipped, so a same-session claim makes --beat print skipped, and AC1 already requires 'renewed'. AC1 b's --dispatch under s1 would take through the same-session row, but AC4's s2 --dispatch covers holder mode. | sound |
| 2 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:section 2 S2; section 4 'The set across one --resume holder-row call' | medium | medium | confirmed | S2 adds to the set on any --resume holder-row call whose CAS did not complete or whose claim could not be read, with no write_lease-due scope. Unit 20 S2 was scoped to that branch ('the row still runs write_lease'). The row's stage_or_fail sits inside the write_lease-due branch (unattended.sh:6597-6600, whose comment says the holder 'writes NOTHING unless' a lease field changed). S3 gives the clear its own stage_or_fail, and S2 does not. Section 4's table has rows 'the claim unreadable -> add' and 'no claim write due -> unchanged', and both apply to an offline call with nothing due, with no precedence stated. Unit 20's 'The order' table does stage 'when write_lease ran or the fact was written', which partly mitigates the unstaged outcome for a builder who reads it, but the S2/S3 asymmetry and the table overlap remain. No AC drives an incomplete or offline renewal: AC2's renewal leg lands. The effect is contained. The added value is the current session, which no verdict needs, and the run-state file stays dirty or is written on calls the row's contract says write nothing. | sound |
| 3 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:section 6 AC5; section 2 S5 and S1 | medium | medium | confirmed | AC5 drives the restart only after sequence d, where the set is 's1 s2' and the claim is s1, the first member, and the set never holds absent. Its red-when catches only a whole-value compare. S5 says 'any member' and S1 says absent is a legal member, but S1's supersession names only unit 20 S2 and S3. Unit 20 S8 still reads 'equals the record's prior-session fact, when that is not absent', and unit 20 is built first (order 4). A builder converting S8 to membership can keep that guard and pass AC5. That guard is reachable. After AC3's incomplete s2 call, the record is s2, the claim is (k, absent) and the set is 'absent'. An s2 relaunch under a new keepalive reaches the restart row and reads the live claim as foreign, so it gets check 89 until the beat goes stale. A first-member-only compare is less plausible but also passes. The path is narrow and the lockout lasts only until the claim reads stale, so the effect is contained. | sound |
| 4 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:section 2 S6 | medium | - | refuted | S6 states the requirement plainly: comments and the stops guide must say the fact is a set, that the empty value is the cleared state, and that the --resume row is its one writer. It carries the marker NOT OBSERVED with a reason, which memory/TEMPLATE-SPEC.md section 2 sanctions. The project's own class record for this defect (memory/gotchas/a-folded-field-leaves-its-row-shape-docs-behind.md) says prose of this kind is not gated and is a documented review check. Unit 20 S7's predicate cited lines that exist at base. The lines S6 governs do not exist until unit 20 is built, and they carry the distinctive token prior-session, so finding them is a trivial grep, not missing design. The criterion the finding proposes is a manual judgment over grep hits, not a mechanical check. A build following S6 ships no stale prose. The only consequence is to comments and docs with no behavioural effect, so it would be low even if confirmed, and asking for a predicate is a preference. | sound |
| 5 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:section 2 S2 (the clause 'when the claim read succeeded, the claim's session field'); section 4 set table | low | - | refuted | The redundancy is real but has no effect on behaviour. Under unit 20 S1 the holder row decides mine against the pre-call record facts, and unit 11 makes every renewer copy its session from the record. So a CAS that runs on a mine verdict has a claim session equal to the pre-call record session or an existing member. On a same-session verdict it equals the environment session, which write_lease records as the record's session. The clause therefore never adds a value a reader needs. Built as written, it is a defensive no-op, and the set still holds the right values. S2's 'Observed by AC1 and AC2' is true of every behaviour S2 produces. Section 7 asks for no arm for this clause, so the arm that cannot go red is one the spec never asks for. This is a clarity preference, not a defect that makes the spec unbuildable or wrong. | sound |
| 6 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:section 6 AC5 and section 7 (the restart arm) against section 4 The sequences | high | high | confirmed | Section 4 defines a sequence as ending in its closing --resume call ('A sequence ends with a closing --resume call under its last session and no shim'), and AC1 uses 'sequences ... run' to include that call. Read the same way, AC5's 'When sequence d of section 4 runs and the next call is under s3' and the section 7 arm's 'after sequence d' put the restart after the closing s3 call. That call lands, empties the set per S3, and leaves the claim at s3, so the restart's claim session equals CLAUDE_CODE_SESSION_ID s3. That is unit 1's plain same-session row, and S5's membership test is never reached. The staged break ('the restart widening comparing the whole value') runs over an empty set and stays green. AC5's 'the remote restored' only makes sense right after d's second unreachable call, so the intended state is the one before the closing call, and the text contradicts it. The red-first rule in section 5 would most likely stall the pass rather than let a vacuous arm land. That makes this a misleading defect on a narrow path, not a shipped false certification: high. | sound |
| 7 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:section 2 S2 against section 2 S3 and the section 6 fixture preamble | medium | medium | confirmed | Unit 1 section 4 'Renewal' has the holder --resume read its claim on every call and renew it when the beat is a quarter of the bound old, with no write_lease due. Unit 20 AC3 drives exactly that renewal-only call. Unit 23 S2 adds to the set on any --resume holder-row call whose CAS did not complete or whose claim could not be read, 'before its stage_or_fail'. Its section 4 table has the 'claim unreadable' row with no write_lease condition. At base 5266d22e, unattended.sh:6597-6600 shows the row's only stage_or_fail inside the write_lease-due branch. Unit 20 S2 records that fact, which is why S3 gives the clear its own stage_or_fail, and S2 gets none. An offline idle-wake tick, or a renewal whose push exits 124, therefore turns an empty set into {s1} and leaves the run-state file unstaged. That contradicts section 6's 'After every call, git diff --name-only names no run-state file', and no criterion drives the path. The effect is contained: a dirty record until the next landed holder write empties the set and stages it. Medium. | sound |
| 8 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:section 2 S4 against section 2 S5 | medium | - | refuted | S4 says check_claim_writable reads the set 'whenever its mode is holder or status write'. That is a sufficient condition, not an 'only', and 'no caller passes the fact in' is consistent with reading it inside the function in take-over mode too. S5, with unit 20 S8, defines the restart condition and the keepalive comparison from the record's facts before the call. check_claim_writable can read those itself, because run_takeover CASes before write_lease. So a build that reads the set in-function at the restart row satisfies both lines, and the claim that 'a builder must break one of the two lines' is false. Either placement also yields the same verdict, and AC5 (plus unit 20 AC6's presumed-stopped leg) observes it. At most S4's mode list is incomplete. That does not make the spec unbuildable or wrong. | sound |
| 9 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:title, section 3 'Bounding the set', and section 5 perf/scale and migration, against section 2 S3 and section 4 sequences a and b | medium | low | confirmed | Real. The title says 'emptied by the next holder write that lands', the 'Bounding the set' non-goal in section 3 says 'the first holder write that lands empties the set, so it grows only across one outage', section 5 perf says 'empties on the first landed holder write', and section 5 migration says 'the next holder write that lands empties it'. But S3 confines the emptying to 'the next --resume holder-row claim write that lands'. S4 and unit 1's call-site table use 'holder' for --resume, --dispatch, --close and --beat. AC1 requires a landed --beat or --dispatch to leave the set reading s1, and sequence a shows the set growing across two incomplete pushes with a landed --beat between them. So the bound premise is false as written. Graded low, not medium. S3, AC1 and the adjacent 'Emptying the fact from other writers' non-goal state the rule consistently, S6 makes the shipped comments and stops guide name the --resume row as the one writer, and AC1's 'set reads s1 s2 before the closing call' assertion reds a build that empties on --beat. Built as written, behaviour is unaffected, and the defect stays in the spec's own descriptive prose. | sound |
| 10 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:section 7 New arms against section 6 AC1 and AC2 Red-when, and section 2 S3 | medium | medium | confirmed | Real for AC2, and partly for AC1. Section 7's six arms stage the absent-only rule, the claim-only set, the unconditional pre-call write, absent-as-no-fact, the --resume-only reader and the whole-value restart compare. None stages the S3 'only when non-empty' guard, so AC2's git status --porcelain assertion is never observed red. Unit 20's arm for the same AC3 clause stages a different break too. Rev-2 claims AC2 observes that guard, which is the observed-by-claim-no-arm-discharges class this repo documents: stage the scope item's own break and watch the arm red. The finder overstates the AC1 half. A build that empties the set on a landed --beat or --dispatch leaves the set reading s2, not s1 s2, before the closing call, and AC1's 's1 s2' assertion is observed red under the a/b/c arm's absent-only break. So only an adding variant escapes an observed assertion there. The consequence is an unobserved assertion guarding a contained defect, a record restaged on every landed renewal. | sound |
| 11 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:section 2 S2 (with section 3 Edges, unit 20 section 4 'The order') | high | high | confirmed | Real. Unit 23 consumes unit 20's section 4 'The order', which runs the CAS, then write_lease, then the prior-session write, then stage_or_fail. Unit 23's S2 pins the add only 'before its stage_or_fail', so the add follows write_lease. write_lease (unattended.sh:5559-5570) writes keepalive, then session at :5563, then four more set_fact calls, each '\|\| return 1', and set_fact returns 2 when mktemp fails (:5528). The holder row returns on a write_lease failure (:6599), and the kit already names an in-call crash window at :6576. A failure or kill after the session line and before the add leaves the record at s2, the claim at s1 and no s1 in the set. The same-keepalive retry then reads the claim as foreign live (check 90), and the relaunch at the restart row fails S5's membership test (check 89). Both force the claim-lost abort this unit exists to prevent. This is a narrow path, made likelier because a push that exits 124 has already spent the call's time. | sound |
| 12 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:section 2 S2; section 4 'The set across one --resume holder-row call' | medium | medium | confirmed | Real. S2 adds on any --resume holder-row call 'whose claim could not be read', with no write_lease-due qualifier. Unit 20 S2 implicitly had one ('the row still runs write_lease'). Unit 1 S7 and its Renewal section make the holder row read its claim on every call, including the idle-wake tick, and unit 1 keeps that path working offline. So the first offline tick under the recorded session and pid adds the current session, which mine already accepts, so the member is useless. At base that path has no stage_or_fail (unattended.sh:6597-6600; the :6592 comment says it 'writes NOTHING unless'). Unit 20 section 4 keeps 'a renewal ... still writes nothing'. The section 4 table also answers this call twice, 'the claim unreadable' (add) and 'no claim write due' (unchanged), and due-ness cannot be read off an unreadable claim. One caveat: unit 1 AC13 removes the SKILL.template.md:38 sentence, so that citation is stale, but the local write-nothing contract stands in unit 20 and the code comment. The effect is contained: one record write per outage, left unstaged or restaged, then a staged clear on recovery. None of sequences a to f drives this path. | sound |
| 13 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:section 2 S5 (with S4) | low | - | refuted | The detail the finding asks for belongs to unit 20, not unit 23. Unit 23 S5 takes unit 20 S8's restart widening as it is and changes only its comparison, from equality to membership. Unit 20 S8 already says how the restart row is identified ('it holds exactly when CLAUDE_CODE_SESSION_ID equals the record's session fact before the call'), and it has to read prior-session in take-over mode itself, because unit 20 is built first. Unit 20's hands-off gives unit 23 only 'the read inside check_claim_writable for every holder and status-write site', which is exactly S4's scope. So S4's 'no caller passes the fact in' applies to those modes and does not forbid either take-over mechanism. The claimed impact is also not clearly a defect. The over-match is a presumed-stopped take-over by the recorded session itself. That row is reached only when CLAUDE_PID equals the recorded pid (unattended.sh:6612-6615); with a different pid, restart=1 and the call goes to :6680 instead. There, reading a claim under the record's own keepalive and a prior-session member as 'same session' is the reading S8 gives the restart row. TOOL-aGraftedHelix-8's 'claim taken over' line is for a foreign stale take, and unit 20 AC6 asserts it only for a different session, s3. If unit 20 S8's 'exactly' is imprecise, that is a finding against unit 20. The finder graded this low. | unsound |
| 14 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:section 2 S2; section 4 Evidence | low | low | confirmed | S2 adds 'the record's session fact as it stood before the call' and, 'when the claim read succeeded', 'the claim's session field', and states no rule for an empty value. Two paths reach one. First, a claim read that finds no claim succeeds (unit 1's 'none' row, which creates), so S2 asks for a session field that does not exist; when that create's push exits 124, a literal build adds the empty string beside the record's session. Second, the holder row's write branch runs on a record with no lease-utc (unattended.sh:6597) and prints its session as ${os:-none} (:6601), so the pre-call session can be empty. Section 4 Evidence's 'a recorded session is never empty' covers only what write_lease wrote. A literal join then stores 's1 ' or a doubled or leading space. fact strips only leading spaces (:1129), so the stored bytes differ from S1's one-space form. Membership and every verdict are unaffected, and a 'none' claim is created again on the next call whatever the set holds. The consequence is cosmetic. | sound |
| 15 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:section 6 AC4 (the second fixture copy's --hold leg); section 7 New arm 5 | medium | medium | confirmed | Unit 20 S2 has the incomplete holder call run write_lease and the prior-session write, then stage_or_fail. Unit 23's §6 preamble asserts only that 'git diff --name-only names no run-state file', which confirms the record is left STAGED, not committed. run_hold calls check_clean with no argument (unattended.sh:4918) after argument parsing and before any write. check_clean counts scan_dirty_paths, which includes 'git diff --cached --name-only' (:1966). The header at :1969-1973 records that --hold deliberately passes nothing (TOOL-dDerivedDocket-61 S8). VERBS.template.md lists 'a dirty tree' among --hold's pre-write refusals, and unattended.test.sh:2826-2830 commits a record before every hold for exactly this reason. So on a correct build, AC4's second-copy leg ends in 'UNATTENDED check 2 FAILED' and the claim never reads held. The leg can never go green, its 'Red when' misdiagnoses the failure, and the obvious repair, passing the run-state file to --hold's check_clean, reverses a recorded decision. --dispatch does not call check_clean, so AC4's first leg and AC1's sequence b are not affected. The effect stays inside one acceptance leg and its arm. | sound |
| 16 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-23.md:section 2 S1 (the supersession sentence) and S5; section 6 AC5 | medium | medium | confirmed | Unit 20 S8 (rev-4) widens the restart row with the record's prior-session fact 'when that is not absent'. Unit 23 S1's supersession names only 'unit 20 S2's and S3's reading', and the Goal states finding 7 against S3 alone. S5 says S8 'tests membership'. A reader can take that as changing only the comparison and keeping S8's guard on the fact's value, which reads 'absent' for the set {absent}. S5's 'any member' points the other way, so the spec is at best ambiguous, and no criterion settles it. AC3 drives the absent member only at the holder column, and AC5 starts from sequence d, whose members are s1 and s2. The path is reachable. A lease with CLAUDE_CODE_SESSION_ID unset leaves record and claim at (k1, absent). An s2 holder call (ls_sid absent != s2, so write_lease is due) whose push exits 124 leaves record s2 and the set {absent}. A relaunch as s2 with a new pid and keepalive then sets restart=1 at :6612-6615, because ls_sid is s2 and not absent. With the guard kept, the fresh claim reads foreign live, the take-over column answers check 89, and the run waits until the beat passes RESUME_STALE_BOUND, when the take is logged as a foreign stale one. That is a wrong verdict on the run's own claim, on a narrow path, and it heals itself after the bound. | sound |
