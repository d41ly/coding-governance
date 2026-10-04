**Serves:** spec-audit TOOL-aGraftedHelix-25

# aGraftedHelix — Tier-2 spec audit of unit 25, ROUND 1

*Node `a`, 2026-10-05, ROUND 1 for this subject. Unit 25 promotes the HIGH of the round-1 audit of
unit 24 (that round's H1, finding 11). It states the failure rule for the `prior-session` add that
unit 24 placed ahead of `write_lease`: a non-zero return from the add's `set_fact` returns the
holder row 1 before `write_lease` runs. Four lenses ran: underspecification, contradiction,
unstated assumption and prior art. Every finding in the body survived a skeptic prompted to REFUTE
it. The four findings the skeptics refuted appear only in the appendix. The author of this report
confirmed that the pinned blob below is the blob at HEAD (`afb5be6b7`), by `git rev-parse
HEAD:<path>` against `git hash-object <path>`. That blob is the spec's rev-2, last touched by
`f507db363`. Five base lines were spot-checked at `5266d22e`. The dispatcher's bare
`--resume) verb_resume "$SLUG" "$KID" ;;` is line 10561. The script's last statement,
`RUNLOG_CLEAN=1; exit "$status"`, is line 10576; id 5 cites 10577, which is one line off and changes
nothing. `fail()` at line 637 is the function that sets `status=1`. `set_fact`'s
`tmp=$(mktemp) || return 2` is line 5528. `set_fact`'s own `fail 17 "cannot record a run fact …"`
refusal is line 5525. The other rows carry the skeptics' verified text and were not re-derived
here.*

**Reviewed at ROUND 1, the subject pinned at its blob:** `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-25.md`@`68d903485eb74f1f53ead028b2cb04a07e375b54`.

## Verdict: CLEAN WITH FIXES

No confirmed finding is graded BLOCKER. The verdict is not CLEAN, because seven confirmed findings
stand and three of them are HIGH, forming two HIGH items.

- H1 (ids 5 and 8): the row's `return 1` never reaches the process exit. The driver exits with
  `$status`, and only `fail` sets it, so `--resume` exits 0 on a build made exactly as S1 writes
  it. AC1's "exits non-zero" therefore reds a correct build, and S1's Readers line states an
  exit-status contract that does not exist. A build pass cannot turn AC1 green without departing
  from the spec, so this must be settled before the pass, not during it.
- H2 (id 6): the add has two triggers, and AC1 drives only the CAS-incomplete one. A build that
  guards only that path's add passes AC1 and the §7 arm, and on an unreachable remote with a failed
  add it forces a claim-lost abort.

H2 and M1 (ids 1 and 10) are one defect carrying two binding grades. The skeptics graded it high
under id 6 and medium under ids 1 and 10. Findings of different binding grades are not merged, so
the report keeps them as two items, and the reason is written at H2. Two findings are LOW, and both
are prose: an exit-status assertion weaker than its scope item, and an Edges line naming a shim the
unit does not use.

Three fixes were judged UNSOUND, ids 1, 6 and 10, and all three address the H2/M1 defect. The
report carries each skeptic's corrected fix. The three corrections disagree on how the unreachable
leg's `mktemp` shim is keyed, and "Reconciling the three corrected fixes" under M1 says which one
the fold should take.

Disposition, per `memory/guides/BUILD-METHOD.md`: every CONFIRMED finding is disposed by severity.
Both HIGHs are promoted to a unit whose mechanism closes them, audited as a SPEC. Each MEDIUM and
LOW is folded into this spec as a rev bump with a §9 line. Unit 25 is itself a promotion of unit
24's H1, and unit 24 promoted unit 23's HIGHs, so promoting H1 and H2 extends the chain once more.
The method ends a chain at a promoting round whose stated precision falls below the review
protocol's floor (`memory/guides/REVIEW-PROTOCOL.md`). This round's precision, stated for that rule
to read, is 0.64.

## Review shape

Intensity full. Raw 11, confirmed 7, refuted 4 (ids 2, 4, 9 and 11), unverified 0 (0 uncertain),
precision 0.64.

The adjudicated tally, counted both ways:

| severity | items | raw confirmed findings |
|---|---|---|
| BLOCKER | 0 | 0 |
| HIGH | 2 | 3 |
| MEDIUM | 1 | 2 |
| LOW | 2 | 2 |
| **total** | **5** | **7** |

Two merges were made, each within one binding grade. Ids 5 and 8 (both high) are one defect: the
verb's return never reaches the process exit. Ids 1 and 10 (both medium) are one defect: the
unreadable-claim trigger is never driven. No binding grade was changed. The skeptic re-graded id 1
from high to medium, and this report keeps that grade.

By lens, raw then confirmed: underspecification 4 and 2, contradiction 3 and 3, unstated
assumption 2 and 1, prior art 2 and 1.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 4 of 4 returned, 0 DIED.
- 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and 0
  duplicates were found.
- Fixes on confirmed findings: 4 judged sound (ids 3, 5, 7 and 8), 3 judged UNSOUND (ids 1, 6 and
  10), 0 with no fix proposed, and 0 NOT JUDGED. An unjudged fix would be the finder's proposal and
  nothing more; none occurs here.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, so none is bound at the finder's grade
  by default. 1 was RE-GRADED by the skeptic: id 1, from high to medium.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, and 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.

This report does not call the run complete. Every lens and every skeptic batch returned, but three
fixes were judged UNSOUND, one grade was re-graded, no checklist was swept, no intent was supplied,
and every lens ran on the generic brief.

**Intent:** NEITHER `specs` nor `context` was supplied to this review. The lenses graded the spec
against itself, against the units it consumes from or amends (units 1, 20, 23 and 24) and against
the tree at base `5266d22e`, not against a stated intent for the build.

**Checklist:** NONE swept — absent. The count of recurring-bug-class findings in this report is
therefore not evidence that the project's recurring classes are absent from this spec. The spec's
own §9 records a checklist run over the promoting commit, which selected
`two-answers-to-one-question`, but that run was the fold's, not this review's. A caller of the next
round should pass the output of `python tools/memory-tree/gotchas.py --for-paths` over the spec's
Files-touched paths.

## How the findings cluster

A fold that repairs a class repairs every row in it, so the classes are named here before the rows.

| class | ids | where the gate belongs |
|---|---|---|
| A criterion asserts an exit status the driver never produces, because a verb's return is not the process exit | 5, 8, 3 | AC1 asserting the exact exit and the `fail` line in `tools/unattended/unattended.test.sh`, observed red with the `fail` removed and the return kept; a new `memory/gotchas/` class beside `status-set-in-a-subshell` |
| A scope item with two triggers whose criterion drives one | 6, 1, 10 | an unreachable-remote AC1 leg, observed red under its own staged break; the §10 entry unit 24's audit asked for |
| Edges prose naming a dependency the criteria replace | 7 | a §10 checklist entry |

The second class recurs. The round-1 audit of unit 24 confirmed the same gap for the add's PLACE
(its M1, id 2) and proposed a §10 checklist entry: "a scope item with more than one trigger names a
criterion leg per trigger." A grep of `memory/gotchas/` and `memory/guides/` for that rule finds
nothing, so the entry was never recorded, and the gap returns one unit later for the add's FAILURE
rule. The nearest recorded class is `memory/gotchas/observed-by-claim-no-arm-discharges.md`, which
covers S1's `Observed by AC1` label claiming a trigger the arm never drives.

# HIGH

## H1 · id=5, id=8 — the row's `return 1` never reaches `--resume`'s exit, so AC1's "exits non-zero" reds a correct build

- **Address:** TOOL-aGraftedHelix-25 §2 S1 (its Readers line, by value), §3 "A new message for the
  failed add", §4 Evidence and Inventory, and §6 AC1.
- **Defect:** the design's only change is the add's `|| return 1` (§4 Inventory). S1 says every
  caller of `--resume` reads the row's exit status and that a failed add now gives it 1. But the
  dispatcher runs `verb_resume "$SLUG" "$KID"` bare (`tools/unattended/unattended.sh:10561`) and
  the script ends with `exit "$status"` (`:10576`). The script sets only `set -u` (`:48`).
  `status` is set to 1 by `fail()` (`:637`) and by one unrelated site (`:5217`). `set_fact`'s
  `mktemp` branch returns 2 without calling `fail` (`:5528`), and so does its trailing `mv`. Unit
  1's holder row "announce, continue" calls no `fail` either, and unit 23's AC2 asserts that a
  holder call whose push exits 124 exits 0. Nothing in AC1's scenario sets `status`. The skeptic on
  id 8 confirmed it with a minimal bash model: a function returning 1, then `exit "$status"` under
  an EXIT trap, exited 0.
- **Impact:** AC1's "exits non-zero" reds on a build that implements S1 exactly. Its exit assertion
  also cannot tell the correct build from §7's staged break, because both exit 0. A builder must
  either weaken AC1 or add a `fail`, which §4 Inventory ("no new check") and §3 ("no new message")
  rule out. If AC1 is weakened, a failed add is invisible to every caller: exit 0, no stdout line,
  no `RUNLOG_CHECKS` entry. The tick, the idle-wake and the session all read a successful resume
  while the record still names `s1`. S1's statement that the row "already returns 1 when
  `write_lease` fails (`:6599`)" is a false interface statement too: a `mktemp` failure inside
  `write_lease` also exits 0. It will mislead the next change about what callers of `--resume`
  observe.
- **Fix — both skeptics judged their fixes SOUND.** Id 5's fix names two options, and id 8's fix is
  id 5's option (b) made concrete:
  - Option (a), from id 5: remove "exits non-zero" from AC1 and remove S1's exit-status reader
    claim. The record reading `session: s1`, the empty set and the unmoved `lease-utc` stand as the
    witness, and §3's rationale is corrected to say the failure reaches callers only on stderr.
  - Option (b), from id 8: in S1, write the add as
    `|| { fail 17 "cannot record a run fact: prior-session in $rel"; return 1; }`. Check 17 is
    `set_fact`'s own "cannot record a run fact" refusal (`:5525`), so no check number is minted.
    Add a §4 Evidence bullet citing `:637`, `:10561` and `:10576`: the process exits with
    `$status`, and only `fail` sets it. Amend §3's "A new message for the failed add" non-goal and
    S1's Readers line to match. AC1 asserts `UNATTENDED check 17 FAILED` beside the exit.
- **Which to take:** option (b). Option (a) leaves a failed add invisible to every caller of
  `--resume`, and S1's whole purpose is that the failure stops the run's progress visibly. Two
  notes for the fold. First, `set_fact`'s three earlier refusals (`:5512`, `:5516`, `:5525`) already
  call `fail 17` before returning 1, so on those paths option (b) prints a second check-17 line.
  That is harmless, but AC1 should assert that the line is present, never how many there are.
  Second, with option (b) the process exits exactly 1, which also settles L1 (id 3).
- **Beyond this subject:** unit 24's AC1 carries the same premise. Its first leg (unit 24 spec line
  217) says the call "exits non-zero" when the `mktemp` shim fails `write_lease`, and the `|| return
  1` at `:6599` yields a process exit of 0 there too. The promoting unit should correct unit 24's
  AC1 in the same change, or unit 24's build hits the same red.
- **Left-shift gate:** AC1 asserting exit 1 and `UNATTENDED check 17 FAILED` in
  `tools/unattended/unattended.test.sh`, observed RED with the `fail 17` removed and the
  `return 1` kept. That staged break is the class's own: a return with no `fail`. Record the class
  in `memory/gotchas/` beside `status-set-in-a-subshell` ("reporting a failure and failing are two
  different things"): in this driver a verb's return is not the process exit, so a criterion that
  asserts an exit status names the `fail` that sets it. A line-scan gate is not cheap here. A
  scan for `return [1-9]` with no `fail` on its line over `verb_resume` at base (lines 6447 to 6704)
  hits ten lines, and most are callees that call `fail` themselves (`check_slug ... || return 1`).
  So the predicate needs callee knowledge, and §7 requires running it over the tree before wiring
  it.

## H2 · id=6 — the add has two triggers, and AC1 drives only the CAS-incomplete one

- **Address:** TOOL-aGraftedHelix-25 §2 S1 ("Observed by AC1"), §4 "What a failed add leaves",
  §6 AC1 and §7 New arm, against unit 24 S1 and AC1.
- **Defect:** unit 24 S1 gives the add two triggers: a CAS that did not complete, and a claim that
  could not be read. Unit 24 AC1 drives one leg per trigger, and its §7 arm stages "the
  unreadable-claim path's add alone moved back", so a conforming build may reach the add through a
  separate path for each trigger. This sub-spec covers only the first trigger. Its §4 table is
  headed "on an `s2` call whose CAS did not complete". AC1 drives only the claim push exiting 124,
  and its `mktemp` shim is keyed on a marker the `git` shim creates only when it makes that push
  exit 124; an unreachable remote never produces the marker. S1 still says "Observed by AC1" and
  labels only the `mv` half NOT OBSERVED, so the unreadable trigger is neither observed nor
  labelled.
- **Impact:** a build that writes `|| return 1` on the CAS path's add and leaves it off the
  unreadable path's add passes AC1 and the §7 arm. On an unreachable remote with a failed add, that
  row runs `write_lease` anyway. The record moves to `s2`, the claim stays at `s1` and the set holds
  no `s1`. The next `s2` call answers check 90, or check 89 at the restart row, and the run is
  forced to `--abort --code claim-lost`. That is finding 11's own consequence, on a narrow path.
- **Grade:** binding HIGH, and kept. The same defect is graded MEDIUM under ids 1 and 10 (M1). The
  rubric reading supports HIGH: a forced claim-lost abort is a wrong verdict, and it is reached on
  a narrow path. MEDIUM rests on unit 24's precedent, whose M1 graded the identical gap for the
  add's place as medium. This report judges HIGH the better reading. Disposition follows the
  higher grade in practice: the promoting unit that closes H2 also closes M1, and M1's fold should
  not design a separate leg that the promotion would then redesign.
- **Fix — REJECTED by the skeptic, whose corrected fix is:** take option 2 of the proposal alone.
  Have S1 require both triggers to reach the add through one call site, a single `set_fact` line
  written `|| return 1`. AC1's 124 leg then observes the one return both triggers take. Label the
  unreadable trigger NOT OBSERVED, with the reason that it shares that line. Widen the §4 table
  header to "or whose claim was unreadable". If an unreachable leg is still wanted, give it a
  witness that the row passed the claim-outcome handling before the shim fired, as the 124 leg's
  announce line does. Key its shim to the last pre-add step that path takes, never to the failed
  claim read.
- **Left-shift gate:** see "Reconciling the three corrected fixes" under M1. One design closes H2
  and M1 together.

# MEDIUM

## M1 · id=1, id=10 — S1's failure rule binds both triggers, but AC1 and the §7 arm drive only the 124 trigger

- **Address:** TOOL-aGraftedHelix-25 §2 S1 (its "Observed by AC1" label), §4 table heading, §6 AC1
  and the fixture preamble, and §7 New arm.
- **Defect:** the rule itself covers both triggers. S1 binds the return to "the add's `set_fact`",
  and §4 "The add row's failure rule" attaches it to unit 24 §4's add row, which carries both
  triggers ("the CAS did not complete or the claim was unreadable"). The observation covers one.
  AC1 and the §7 arm drive only the 124 trigger, and the `mktemp` shim is keyed on the `git`
  shim's 124 marker, which an unreachable-remote call never sets. S1 labels only the `mv` half NOT
  OBSERVED. That argument holds for `mv`, which shares the one return, but it does not reach a
  second add site. The chain has already ruled on this: the round-1 audit of unit 24 confirmed its
  M1 (id 2, medium, fix sound) because a build can reach the add from the unreadable branch on its
  own, and unit 24 rev-3 folded that ruling as an unreachable leg plus a separately staged
  unreadable-path break. Unit 20's AC2 likewise drives both triggers. Unit 25 does not apply that
  ruling.
- **Impact:** a build that guards only the CAS path's add passes AC1 and the §7 arm. On an
  unreachable remote with a failed add, it runs `write_lease` and leaves the record at `s2`, the
  claim at `s1` and an empty set. The next not-due `s2` call answers check 90, or check 89 at the
  restart row, and forces claim-lost. The skeptic on id 1 graded it medium because the consequence
  needs a build that splits the add per trigger AND a `mktemp` or `mv` failure during an outage.
  Id 10's skeptic flagged one subsidiary claim as unestablished: "on the unreachable path no push
  runs". Unit 24 rev-4 records that no source states whether a CAS is attempted on an unreadable
  claim. The core claim does not depend on it.
- **Fix, id 1 — REJECTED by the skeptic, whose corrected fix is:** name both triggers in S1, and
  widen the §4 table heading to "whose CAS did not complete or whose claim was unreadable". Give
  AC1 a second leg over a fresh fixture copy with the remote unreachable. In that leg the `git` shim
  creates the marker after the LAST claim git command the row runs before the add on that path:
  the failed claim push if the row attempts a CAS there, otherwise the failed claim fetch. The spec
  must pin which one. Use the same once-only `mktemp` shim. Assert unit 1's announce line, exit 1,
  `session: s1`, `fact` printing nothing for `prior-session`, and `lease-utc` unmoved. Then run a
  call with the remote restored and no shim, and assert exit 0, no `UNATTENDED check 90 FAILED`,
  and a claim naming `session: s2`. In §7, stage the dropped return on the unreadable path's add
  alone, observed red through that leg.
- **Fix, id 10 — REJECTED by the skeptic, whose corrected fix is:** add a second AC1 leg over a
  fresh copy of unit 24 AC1's fixture, with the remote unreachable (unit 23's definition: the bare
  repository renamed away). Make the `git` shim create the marker when the driver's claim read
  exits non-zero. That read is the bounded glob fetch `observe_remote` runs,
  `git fetch ... '+refs/gov/runs/*:refs/gov/remote/runs/*'` (unit 1 S2 and §4 "Reading"). The
  `mktemp` shim stays as AC1's, firing once after the marker exists. Assert the same outcome as the
  first leg, keeping unit 1's announce line as a witness, since unit 20 §4 announces on the
  unreadable trigger too. The leg then exits non-zero and leaves `session: s1`, `fact` printing
  nothing for `prior-session`, and `lease-utc` unmoved. A following `s2` call with the remote
  restored and no shim exits 0 with no `UNATTENDED check 90 FAILED`. Make S1's "Observed by" label
  name both legs. In §7, stage the unreadable path's add return dropped alone, observed red through
  that leg, as unit 24 rev-3's first arm does.

### Reconciling the three corrected fixes

The corrected fixes for ids 6, 1 and 10 address one defect, and they disagree on one point: where
the unreachable leg's marker is keyed.

- Id 10's correction keys the marker on the failed claim fetch. Id 1's skeptic showed why that is
  unsafe whenever the row attempts a CAS after that fetch. Unit 25 §4 Alternatives says the CAS
  takes temporary files, so the once-only shim would fail the CAS's temporary file instead of the
  add's. The incomplete CAS is "announce, continue", the add then runs and writes `s1`, and a leg
  asserting an empty `prior-session` reds on a correct build.
- Id 1's correction keys the marker after the LAST claim git command before the add on that path,
  and requires the spec to pin which command that is. When no CAS runs on the unreadable path, it
  reduces to id 10's keying. It therefore subsumes id 10's.
- Id 6's correction makes the rule structural, with one add call site for both triggers, and
  labels the unreadable trigger NOT OBSERVED. Any unreachable leg it allows is keyed as id 1's is.

Recommended for the promoting unit:

1. First, pin whether a CAS is attempted on the unreadable path. Unit 24 rev-4 records that no
   source states it, and both id 1's keying and id 6's "last pre-add step" depend on the answer.
2. Take id 6's single call site, since it makes a per-trigger split impossible rather than merely
   detected.
3. Also add id 1's unreachable leg, keyed as id 1 says. Unit 24's audit asked for "a criterion leg
   per trigger", and a single call site written today is still one edit away from two. Under a
   single call site the "unreadable path's add alone" break cannot be staged, so stage instead the
   unreadable path rerouted to a second, unguarded add, observed red through the unreachable leg.
4. The leg's exit assertion follows H1's decision. Under H1 option (b) it is exit 1 plus
   `UNATTENDED check 17 FAILED`. At base it would be exit 0.

- **Left-shift gate:** the unreachable leg in `tools/unattended/unattended.test.sh`, observed RED
  under its staged break. Record the §10 entry unit 24's audit proposed and nobody recorded: "a
  scope item with more than one trigger names a criterion leg per trigger, and its `Observed by`
  label is checked against each." Cite it from
  `memory/gotchas/observed-by-claim-no-arm-discharges.md`, the recorded class it is an instance of.

# LOW

## L1 · id=3 — AC1 asserts "exits non-zero" where S1 promises 1

- **Address:** TOOL-aGraftedHelix-25 §6 AC1, against §2 S1.
- **Defect:** S1 says the row returns 1 and that the add "is written `|| return 1`", but AC1
  asserts only "exits non-zero". The criterion is weaker than the scope item it observes.
- **Impact, corrected by this report:** the finding argues that a build writing a bare `|| return`
  exits 2, because `set_fact` returns 2 on a failed `mktemp` (`:5528`), and so passes AC1. H1 shows
  that mechanism does not hold. The dispatcher discards `verb_resume`'s return (`:10561`) and exits
  `$status` (`:10576`), so the verb's return value never reaches the process exit. At base the
  process exits 0 either way. What survives is the textual gap: AC1's exit assertion must name the
  exact status the chosen fix for H1 produces. No caller of `--resume` is shown to branch on 1
  versus 2, so the grade stays LOW.
- **Fix — the skeptic judged it SOUND:** change AC1's first-call assertion from "exits non-zero" to
  "exits 1", and add to Red when: the row propagates `set_fact`'s own status. Fold this into H1's
  promotion. Under H1 option (b), `fail` sets `status=1` and "exits 1" is the right assertion.
  Under option (a) the exit assertion is removed and this finding is moot.
- **Left-shift gate:** none of its own; H1's gate covers it.

## L2 · id=7 — §3 Edges says the unit consumes unit 24 AC1's `mktemp` shim, which cannot fail the add

- **Address:** TOOL-aGraftedHelix-25 §3 Edges (consumes-from TOOL-aGraftedHelix-24).
- **Defect:** the edge says this unit consumes unit 24's "AC1's fixture and its `mktemp` shim".
  Unit 24 AC1's shim forwards until the run-state `session:` line reads `s2`, then fails once. With
  the add ahead of `write_lease`, that line reads `s2` only after the add, so that shim cannot fail
  the add. §6 and §4 Alternatives define a different shim, keyed on the `git` shim's 124 marker.
- **Impact:** the edge names a dependency the unit does not use. A builder who reuses unit 24's
  shim as the edge states never fails the add, and AC1's own witness then reds because the add
  writes `s1`. §6's criterion text is explicit, so the effect stays in the record's prose.
- **Fix — the skeptic judged it SOUND:** reword the edge as "AC1's fixture and the interruption arm;
  the `mktemp` shim is re-keyed here on the `git` shim's 124 marker (§6)".
- **Left-shift gate:** a §10 checklist entry: "an Edges line names exactly what the criteria
  consume; a fixture element the unit re-keys is named as re-keyed."

## What a fold should do first

1. Promote H1 and H2 into one unit. Decide H1's option first, because the exit assertion of every
   leg follows it; this report recommends option (b), `fail 17` plus `return 1`. In the same
   change, correct unit 24's AC1 first-leg "exits non-zero", which carries the same premise.
2. In that unit, pin whether a CAS is attempted on the unreadable path before designing the
   unreachable leg. Then take id 6's single call site and id 1's leg, keyed as id 1 says.
3. Fold M1 as a rev bump with a §9 line that points at the promoting unit as the mechanism that
   closes it, rather than designing a second leg here.
4. Fold L1 with H1's promotion, since its assertion is whatever H1 decides.
5. Fold L2 last. It is a one-line rewording of the Edges entry.

A review of the promotion spec should run with a checklist swept and an intent supplied. This round
had neither.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-25.md:section 2 S1 / section 6 AC1 / section 7 arm | high | medium | confirmed | The rule itself does cover both triggers. S1 binds the return to 'the add's set_fact', and section 4 'The add row's failure rule' attaches it to unit 24 section 4's add row, which carries both triggers ('the CAS did not complete or the claim was unreadable'). The observation, however, covers one trigger only. AC1 and the section 7 arm drive only the 124 trigger, and the mktemp shim is keyed on the git shim's 124 marker, which an unreachable-remote call never sets. S1 labels only the mv half NOT OBSERVED, so nothing announces that the unreadable trigger goes unobserved. Unit 24's own section 7 arm stages 'the unreadable-claim path's add alone moved back', so the spec set already treats a per-trigger split of the add as a real break. Unit 24's round-1 audit also graded the identical gap for the add's place (its finding 2) MEDIUM. The section 4 table heading names only the CAS-incomplete call. Graded medium rather than high: the consequence needs a build that splits the add per trigger and also a mktemp or mv failure during an outage, so the effect is contained. The fix is unsound for two reasons. First, keying the marker on the claim read failing can spend the once-only mktemp shim on the CAS's temporary file instead of the add's: unit 25 section 4 Alternatives states that the CAS takes temporary files, and unit 24 rev-4 records that no source states whether a CAS is attempted on the unreadable path. In that case the incomplete CAS is 'announce, continue', the add runs and writes s1, and the leg asserting an empty prior-session reds on a correct build. Second, the fix drops the announce-line witness that AC1 relies on to prove the shim fired after the CAS outcome. | unsound |
| 2 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-25.md:section 2 S1 / section 6 AC1 | medium | - | refuted | S1 binds the return to 'a non-zero return from the add's set_fact', and that rule is correct for a conditional add. The hypothesized '[ -n "$new" ] && set_fact ... \|\| return 1' returns on the test's status, not on set_fact's. It therefore violates S1 as written rather than following it. Base's own idiom for a conditional fact write with a return is 'if [ -n ... ]; then set_fact ... \|\| return 1; fi' (tools/unattended/unattended.sh:6368-6369). That is the hold-unpushed precedent unit 23 S3 says it reuses. So the premise that S1 prescribes a shape that is wrong for a conditional add is false. What remains is a missing negative test against a mis-implementation the spec does not invite. The factual part is accurate: no criterion in units 23 to 25 drives a triggered add whose members are all present. Graded medium and not established as a spec defect, so it is refuted. Judged on its own, the fix is sound: the record s1, set s1, claim s1 state is unit 24 section 4's 'stopped after the add' row, and the set still reading s1 doubles as the witness that the CAS did not land. | sound |
| 3 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-25.md:section 6 AC1 | low | low | confirmed | Established from the spec and from base. S1 says the row returns 1 and that the add 'is written \|\| return 1', but AC1 asserts only 'exits non-zero'. set_fact returns 2 when mktemp fails (tools/unattended/unattended.sh:5528), and the dispatcher ends with 'exit "$status"' after verb_resume. A build that writes a bare '\|\| return' therefore exits 2 and passes AC1 and the arm. The criterion is weaker than the scope item it observes. No caller of --resume is shown to branch on 1 versus 2, so the effect is cosmetic: low. | sound |
| 4 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-25.md:section 6 AC1, the witness sentence | low | - | refuted | The precondition is already stated in the spec. S1 says 'The add's place is unit 24's', the Edges entry consumes from TOOL-aGraftedHelix-24 'the add's place ahead of write_lease', and the AC fixture is unit 24 AC1's. The witness sentence lists where the shim can fire relative to the add under the order this unit consumes, and that order is a precondition, not something AC1 has to detect. Unit 24 AC1 owns the order regression. Restating the dependency inside the sentence is a style preference and changes no behaviour. | sound |
| 5 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-25.md:section 2 S1 (Readers, by value); section 3 'A new message for the failed add'; section 4 Inventory; section 6 AC1 | high | high | confirmed | At base 5266d22e the dispatcher runs '--resume) verb_resume "$SLUG" "$KID" ;;' (:10561), ignores the return and ends with 'exit "$status"' (:10577). The script sets only 'set -u' (:48). Only fail() sets status=1 (:637); the one other assignment, at :5217, is in an unrelated check. The EXIT trap (write_runlog_end) records rc and calls no exit. verb_resume's one caller is that dispatcher line. set_fact's mktemp branch is 'tmp=$(mktemp) \|\| return 2' (:5528) and calls no fail. Unit 1's 'announce, continue' holder row prints and goes on, and unit 23 AC2 asserts that the 124 holder call exits 0. So an add written '\|\| return 1', as S1 and the section 4 Inventory specify, gives verb_resume 1 and the process 0. AC1's 'exits non-zero' therefore reds a correct build. S1's by-value claim that callers of --resume read the row's exit status, and that the row 'already returns 1' to them when write_lease fails, is false for the mktemp and mv branches. That false interface statement will mislead the next change. AC1's other assertions still discriminate the staged break, so this is high rather than blocker. | sound |
| 6 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-25.md:section 2 S1 ('Observed by AC1'); section 4 'What a failed add leaves'; section 6 AC1; section 7 New arm (against unit 24 S1 and AC1) | high | high | confirmed | Unit 24 S1 gives the add two triggers, an incomplete CAS and an unreadable claim, and unit 24's section 7 arm separately stages 'the unreadable-claim path's add alone moved back'. A conforming build may therefore reach the add through a separate path for each trigger. Unit 25's AC1 drives only the claim push exiting 124. Its mktemp shim waits on a marker that the git shim creates only at that 124, and an unreachable remote never produces it. The section 4 table is headed for the incomplete-CAS call only. S1 says 'Observed by AC1' and labels only the mv half NOT OBSERVED. A build that puts '\|\| return 1' only on the CAS path's add passes AC1 and the section 7 arm. If the add then fails while the remote is unreachable, write_lease still runs: the record moves to s2, the claim stays at s1 and no s1 is in the set. The next call then answers check 90 (or check 89 at the restart row) and forces claim-lost. The path is narrow and the consequence is a wrong verdict. | unsound |
| 7 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-25.md:section 3 Edges (consumes-from TOOL-aGraftedHelix-24) | low | low | confirmed | Unit 24 AC1's mktemp shim forwards until the run-state session line reads s2, then fails once. With the add placed ahead of write_lease, the session line does not read s2 until after the add, so that shim cannot fail the add. Unit 25 section 6 defines a different shim keyed on a marker the git shim creates at its 124, and section 4 Alternatives says the shim is keyed on the git shim's 124. The edge's claim that this unit consumes unit 24 AC1's mktemp shim is therefore inaccurate. The criterion text in section 6 is explicit, so a builder following AC1 is not misled. The defect is in prose only, which makes it low. | sound |
| 8 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-25.md:section 2 S1 (its Readers line) and section 6 AC1, unchecked by section 4 Evidence | high | high | confirmed | At base 5266d22e, verb_resume is dispatched bare at tools/unattended/unattended.sh:10561, and the script ends with `exit "$status"` at :10576. `status` is set to 1 only by fail() at :637 and by one unrelated site at :5217. In set_fact, the `tmp=$(mktemp) \|\| return 2` at :5528 and the trailing mv call no fail. Elsewhere in verb_resume every `return 1` is paired with a fail call. Unit 1 section 4 gives the holder row's not-completed CAS 'announce, continue', and unit 1 says the verb goes on. Unit 1 AC18 shows an announcing holder call exiting 0. So nothing in AC1's scenario sets status. A minimal bash model (a function returning 1, then exit "$status" under an EXIT trap) exited 0. An add written `\|\| return 1`, as S1 specifies, makes --resume exit 0, so AC1's 'exits non-zero' reds on a build that follows S1 exactly. S1's Readers claim that 'a failed add now gives it 1' is false, and so is the precedent it cites at :6599. As a result the pass cannot go green without departing from the spec. It also points the next change at a false exit-status contract. | sound |
| 9 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-25.md:section 4 'What a failed add leaves' and section 2 S1 ('the one return covers a failed mv as well as a failed mktemp') | medium | - | refuted | The code fact is true: set_fact at :5529-5534 does not check awk's status before `mv "$tmp" "$f"`. But the spec's statement holds for the population it defines. S1 defines a failed add as a non-zero return from the add's set_fact. A mktemp failure returns 2 before anything is written, and a failed rename leaves the destination untouched, so 'a failed add writes nothing' is accurate. The awk-failure path is a different case: an add that reports success while corrupting the record. That defect lives inside set_fact, predates this unit, and applies equally to write_lease's six facts and to every other caller. This unit does not touch set_fact and does not worsen the defect. Building it as written ships nothing new, and no verdict in section 4's table depends on the defect. Asking the unit to document or fix set_fact's internal atomicity is scope that section 3's 'Every other set_fact caller' non-goal leaves out. It belongs in a separate backlog row against set_fact. | sound |
| 10 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-25.md:section 2 S1 (its 'Observed by AC1' label), section 6 AC1 and the fixture preamble, section 7 New arm | medium | medium | confirmed | Unit 25 S1's rule covers 'the add's set_fact'. That is unit 24's add, which unit 24 S1 and its section 4 'The order' row run on two triggers: a CAS that did not complete, and a claim that could not be read. Unit 25's section 4 table is titled for the CAS trigger only. AC1 has a single leg, with the claim push exiting 124, and its mktemp shim arms only on a marker the git shim creates when it makes that push exit 124. No leg runs with the remote unreachable, and the S1 label gives no NOT OBSERVED reason for that trigger. It gives one only for the mv half, which really does share the one return; that argument does not reach a second add site. The chain already confirmed this exact gap for unit 24: the round-1 audit's M1 (id 2, medium, fix sound) holds that a build can reach the add from the unreadable branch separately, and it ruled that a scope item with more than one trigger names a criterion leg per trigger. Unit 24 rev-3 folded that ruling as an unreachable leg plus a separately staged unreadable-path break. A build that guards only the CAS path's add passes unit 25's AC1 and its section 7 arm. On an unreachable remote with a failed add, that build runs write_lease and leaves the record at s2, the claim at s1 and an empty set. The next not-due s2 call then answers check 90, or check 89 at the restart row. One subsidiary claim is not established: 'on the unreachable path no push runs'. Unit 24 rev-4 records that no source states whether a CAS is attempted on an unreadable claim. The core claim does not depend on it, because unit 25 defines no unreachable leg at all. The consequence is contained to an unreachable remote combined with a failed add on a build that has two differently guarded add sites, so the grade is medium, matching M1's. | unsound |
| 11 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-25.md:section 4 Alternatives rejected (the shell-hygiene scan bullet), section 4 Inventory, section 10 Reuse audit | low | - | refuted | The facts check out, but none of them makes unit 25 wrong. TOOL-dSealedTally-1 is CLOSED, and unattended.sh:4630-4651 at base 5266d22e does carry the ANCHOR-BEFORE-PHASE comment and set_fact landed-anchor ... \|\| return 1 ahead of set_fact phase LANDED. Unit 25 does not cite it. Unit 25's reuse audit already names the identical seam, write_lease's set_fact ... \|\| return 1 and the holder row's return at :6599, and reuses it. Citing a second instance of the same shape changes no design element. The add's place is already commented at the row by unit 24 S1 ('The comment at the row names this order'), and write_lease's own load-bearing \|\| return 1 lines carry no per-line comment either. So the missing comment is a preference, and the dropped-return break the finder fears is exactly what section 7's arm is staged red on. The gotchas-class part was refuted for unit 24 in the same round (that audit's id 12). BUILD-METHOD.md:263-264 asks for 'a regression gate, OR a memory/gotchas/ class when the class cannot be gated'. Section 7's arm is that regression gate for this finding, and this repo records class entries in separate records commits outside unit specs. The Alternatives sentence says 'this class's regression gate here'; the 'here' scopes it to this instance, so it does not claim class-wide coverage. By the finder's own account the consequence is documentation only, and it was graded low. | sound |
