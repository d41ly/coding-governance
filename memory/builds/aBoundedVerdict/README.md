---
slug: aBoundedVerdict
node: a
opened: 2026-08-16
streams: tooling
roster: TOOL
ids: TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-6 TOOL-aBoundedVerdict-7 TOOL-aBoundedVerdict-8 TOOL-aBoundedVerdict-9 TOOL-aBoundedVerdict-10 TOOL-aBoundedVerdict-11 TOOL-aBoundedVerdict-12 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-14 TOOL-aBoundedVerdict-15 TOOL-aBoundedVerdict-16 TOOL-aBoundedVerdict-17 TOOL-aBoundedVerdict-18 TOOL-aBoundedVerdict-19 TOOL-aBoundedVerdict-20 TOOL-aBoundedVerdict-21 TOOL-aBoundedVerdict-22 TOOL-aBoundedVerdict-23 TOOL-aBoundedVerdict-24 TOOL-aBoundedVerdict-25 TOOL-aBoundedVerdict-26 TOOL-aBoundedVerdict-27 TOOL-aBoundedVerdict-28 TOOL-aBoundedVerdict-29 TOOL-aBoundedVerdict-30
---

# aBoundedVerdict — an unattended run stops reviewing, stops stalling, and says why it stopped

Node `a` · opened 2026-08-16 · streams tooling.

The owner reported three faults in the unattended-build flow: a tier-2 review cycle that can run
indefinitely on a unit whose verdict keeps coming back BLOCKED; a run that pauses for owner input
nobody will supply; and a single `ABORTED` terminal that says nothing about why.

All three faults are real. Two of the three remedies the owner proposed were aimed at levers the
evidence does not support, and the owner chose the evidence-backed alternative for both after being
shown the measurements. This build specs what was chosen. It builds nothing — it is a design pass,
and implementation is a follow-on.

The research behind it is committed at
[`build/2026-08-16-build-TOOL-aBoundedVerdict-1-flow-research.md`](build/2026-08-16-build-TOOL-aBoundedVerdict-1-flow-research.md),
with every measurement, every reproduction and every refuted claim enumerated.

## What the measurements said

Each row was reproduced against this tree, not inferred.

| Finding | Measurement |
|---|---|
| **The review loop is real, and it happened AGAIN during this build** | `memory/builds/dClosedLexicon/` holds EIGHT review records in one day. Rounds 2–7 are all BLOCKED — six consecutive, blocker counts 1, 1, 2, 1, 2, not converging — round 8 returns "PASS WITH FINDINGS", and the run then reached ABORTED with a witness and no readable reason. All three reported faults in one record, from a run following the method faithfully. It landed on `main` while these specs were open |
| The second-worst case, and the one the specs were first written against | `memory/builds/aSiftedPlaybook/reviews/` holds five consecutive spec-audit rounds over one 7-unit set plus a sixth closing round, all on one day. Verdicts: CLEAN WITH FIXES, BLOCKED, BLOCKED, BLOCKED, CLEAN WITH FIXES, BLOCKED. Final spec revs reached rev-12. That one landed; the eight-round case did not |
| Nothing counts reviews | A repo-wide grep for any numeric review bound returns nothing. The review filename carries the build slug and a per-build record counter, so the unit is not recoverable from the name — the driver refuses that join in its own source, having measured it wrong on 7 of 7 multi-unit builds |
| The loop's engine is a rule, not a missing number | The build method has NO stated disposition for a BLOCKED verdict, and its own rule that a rev-moved spec is unreviewed means folding a CLEAN-WITH-FIXES round re-arms the loop |
| Testing forks would serve 7% of them | Of 46 resolved forks read in full across 10 specs, 3 were decidable by a mechanical test alone. About 67% are not testable at all. In one, resolving on the measurement would have picked the answer this repo names as its own vacuous-selector class |
| The fork rule is already non-asking | 30 corpus resolutions already read as agent-delegated. The residual owner turns are the method's vetoes 2 and 3, which are authority questions no test settles |
| A halt phase would have no reader | Nothing outside the unattended kit reads the phase. All in-kit readers branch on the terminal/non-terminal binary; resume behaves identically for the landed and aborted terminals. The record already carries the reason twice and nothing parses either |
| A new terminal phase is unwritable as such | Added to the core set, it is refused by the driver's own guard and the refusal names two verbs that cannot write it. The BINDING protocol's phase list is joined to the driver by no gate, so it drifts silently — reproduced twice |
| A halt reason code costs nothing to carry | Appending one to a real tracked run-state file left both the unattended leg and the hygiene gate green, while a control appending the banned bypass flag reds — so the leg reads the file and is genuinely blind to the code |

Two further defects surfaced that the owner's report did not name, and both are in scope because
each is a place an unattended run stalls or silently proceeds wrongly:

- **A unit awaiting owner scope approval has no rule anywhere.** The playbook's Definition of Ready
  requires scope approval before building. The words "scope approval" and the SPECCED token appear
  zero times across all five carriers an unattended run reads, and the driver's planning verb prints
  `READY - build it` for such a unit.
- **Both readers of a spec's open-questions section are blind in the same way.** Each tests for the
  resolution marker with an unanchored substring and reads only the section's first non-blank line.
  A section whose first line reads that the fork is not resolved therefore classifies as ready, and
  a later unresolved bullet is invisible. Reproduced against both readers with live controls.

## The owner's three decisions

Put in one turn on 2026-08-16, with the measurements above, and answered.

| Question | Decision |
|---|---|
| Fork rule — general testing, or a narrow probe rule plus the real stall fixes? | **Narrow probe rule plus the stall fixes.** Testing is specced only for a declared fact-question subclass; the budget goes to the dispositions and plumbing that actually unblock a run |
| Halt status — new terminal phases, or a validated reason code? | **A validated halt code** on the abort verb, against a kit-owned shrink-only set, with real readers. No phase-vocabulary change |
| Review cap — bind attended runs too, or unattended only? | **Unattended runs only.** The cap is a driver refusal; no corpus-wide retrofit of the 53 existing review records |

The third decision is what keeps this build small. A cap binding every run would have needed a new
required field on every review record, a date-cutoff ratchet, and a waiver pass over a corpus where
24 of 53 records name no unit id at all.

The table below is GENERATED from the status header of every spec in this folder — do not hand-edit
it.


## Units — the authored roster

One mechanism per unit. The `ids:` key above is a reservation range, not this roster.

Each cell is a label. The unit's own Goal section owns the full statement and this table
deliberately does not restate it.

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aBoundedVerdict-11` | 2 | the units region: generated, mandatory, read by name |
| 2 | `TOOL-aBoundedVerdict-12` | 2 | a blocked close names its cause |
| 3 | `TOOL-aBoundedVerdict-13` | 2 | every remote observation is bounded |
| 4 | `TOOL-aBoundedVerdict-4` | 2 | the open-questions predicate, in both readers |
| 5 | `TOOL-aBoundedVerdict-5` | 2 | a park verb |
| 6 | `TOOL-aBoundedVerdict-2` | 2 | the halt code and verdict vocabularies |
| 7 | `TOOL-aBoundedVerdict-1` | 2 | the review loop's convergence rule and the promotion disposition |
| 8 | `TOOL-aBoundedVerdict-14` | 2 | fold-scoped review rounds |
| 9 | `TOOL-aBoundedVerdict-3` | 2 | the stall dispositions |
| 10 | `TOOL-aBoundedVerdict-15` | 1 | close-path writes are staged and guarded — **and see the ordering note below: `-5` and `-3` both depend on its `--attest`, so it moves ahead of both at build time** |
| 11 | `TOOL-aBoundedVerdict-16` | 2 | the closing-review join: a diff-review, in range |
| 12 | `TOOL-aBoundedVerdict-17` | 2 | authorization survives a split fetch/push URL |
| 13 | `TOOL-aBoundedVerdict-18` | 1 | the two vacuous checks get subjects |
| 14 | `TOOL-aBoundedVerdict-19` | 1 | the protocol pair says what the code does |
| 15 | `TOOL-aBoundedVerdict-21` | 2 | the landing push is bounded too |

*An id appears here only once a conforming spec defines it — hygiene check 14 refuses a cited
id nothing defines, which is the mechanical form of the method's "never build a MISSING unit".*

**Ordering correction, 2026-08-19 (spec audit).** The numbers above are a dependency order and two of
them are wrong: `-5` S6 names `-15`'s `--attest --value` as the writer it needs, and `-3`'s halt path
reaches `--abort`, which requires the two agent keys `--attest` writes. `-15` declares no dependency
of its own, so it moves ahead of both. Both dependencies are SOFT — the keys are hand-editable, so the
cost of the old order is a hand-edit rather than a block — which is why this is recorded as a
correction here rather than a re-numbering of a table two other documents cite.

**The order is a dependency order, not a preference.** Unit 4 hardens the predicate that decides
whether a fork is resolved; until it does, every rule the later units write about forks is
unenforceable, because a section declaring itself unresolved reads as resolved. Unit 5 supplies the
verb that parking needs — parking is today an unstructured hand-edit of a file the kit calls
generated. Unit 2 supplies the halt vocabulary that units 1 and 3 both dispose into. Unit 1 spends
that vocabulary on the review cap, and unit 3 spends it on the stall sites. Units 1 and 3 both
depend on unit 2 and neither depends on the other, so they are the only pair that could run
concurrently — and their write sets intersect in the protocol document, so they must not.

## Cross-unit rules

- **The cap is a file constant, never an environment or conf value.** This repo already argued that
  case for the agent fan-out bound and recorded the reason: a ceiling raisable from the environment
  leaves no diff behind. Unit 1 reuses that decision rather than re-litigating it, and the gate leg
  reads the constant from the driver the same way it already reads the core phase and DoD sets.
- **No unit adds a phase-vocabulary member.** The measured cost of doing so is in the research
  record, and the owner's second decision rules it out. A unit that finds itself wanting one has
  found a fork, not a licence.
- **Every new refusal branch is armed in the same unit that adds it** — armed in that gate's sibling
  test, or pinned in `memory/project/unarmed-branches.txt` with the reason it cannot be. That
  pin-or-arm refusal is the mechanism, not the floors: `ARMS_FLOORS` is a one-sided MINIMUM that reds
  only when a measured count falls BELOW it, so raising it is never what makes an arm mandatory and
  raising it without a real branch reds the bar. The floors move only where the report mode shows the
  measured counts actually grew. Measured: adding one refusal to the driver reds the meta-gate
  immediately, naming the unarmed branch — and only one of the two unattended gates is fully armed,
  the driver carrying a standing pin for one branch.
- **The authored region's fact pin moves exactly once, and only for a singleton.** The binding
  protocol pins that region at a closed, enumerated set of facts, and the pin has moved twice before
  leaving a stale reader each time — the driver's own resume comment still says five. This build
  therefore splits by SHAPE, not by convenience: `TOOL-aBoundedVerdict-2`'s halt code is a per-run
  singleton three readers read by key, so it becomes the eighth fact and that unit moves the pin in
  all four places it is spelled. `TOOL-aBoundedVerdict-1`'s review rounds are append-only history, so
  they become lines under a new park KIND and move nothing — which is what a tracked sibling spec
  chose for the identical question, by name.
- **Any unit touching a path on the kickoff manifest's watch list re-audits the claims derived from
  it and re-stamps the manifest in the same commit.** Every unit in this build touches at least one:
  the hygiene engine and `.memory-tree.conf`, `.unattended.conf`, the kickoff engine, and the build
  method are all watched, and the manifest ratchet is a merge-bar leg that reds on a watched file
  changed with no re-stamp at or after the change. `memory/guides/SESSION-KICKOFF.md` is in all five
  units' Files-touched lists for that reason — it was in three when this rule was written, which is
  the rule asserting its own compliance rather than having it.
- **The charter read-path budget is shared, and the spender set is stated HERE and nowhere else.**
  **Re-measured 2026-08-19 at this build's declared base**, because the figures this bullet carried
  were against a RETIRED ceiling and a builder trusting them believed in headroom that did not exist:
  `python tools/memory-tree/corpus_ids.py --report` gives **91997 bytes against a ceiling of 112987**
  (`.memory-tree.conf`), so **20990 bytes of headroom**, with `UNATTENDED-PROTOCOL.md` at 27582 and
  `BUILD-METHOD.md` at 17460. The old 70262-against-86476 and the 72122-against-86476 in
  `TOOL-aBoundedVerdict-3` were both against 86476, which is no longer the ceiling.
  The spender set is now SEVEN units, not four: `-1`, `-3` and `-14` grow the build method; `-2`,
  `-3`, `-5`, `-11` and `-19` grow the unattended protocol. Two specs previously each named the total
  and named only each other as the other spender, which is how a shared budget gets spent twice. No
  spec carries the figure as authority: the builder re-measures with the corpus reporter.
- **Two units move the unattended leg's own check count**, which is stated in the leg's header and
  again in the charter's gate-suite bullet and observed by no gate. They state their moves one apart
  rather than both writing the same number.
- **No spec id in this build may be cited from product source while its status is non-terminal.**
  The drift signal that counts such citations sits at its pin with zero tolerance, and the files
  these units edit are product source.

## The reground, 2026-08-17

The default branch moved **94 commits** while this build was open, and the spec set was regrounded
onto it at `febba16` before landing. Seventeen claims had gone stale; one was a blocker. What the
reground changed, recorded because a set that silently re-based is a set nobody can audit:

- **The blocker.** `TOOL-aBoundedVerdict-2`'s migration said the population of codeless ABORTED
  run-state records was zero. At the new base it is ONE — `memory/builds/dClosedLexicon/RUN.md` — so
  that unit's own leg check would have redded the merge bar on the day it landed. It is now a stated
  one-record retrofit.
- **The pin moved under the spec.** The authored region went from seven facts to eight while this
  build was open, so the halt code is the NINTH, not the eighth. That is the third move, and the
  third to leave stale readers behind — which is the argument `TOOL-aBoundedVerdict-2` S7 was already
  making, now demonstrated rather than asserted.
- **A completeness grep that would have failed exactly as designed.** The two-value alternation
  would have returned nothing while two carriers still said `eight`. It is now number-agnostic.
- **Two arguments that had come to argue the opposite.** "The most recent closed build" no longer
  supports the continuation-line convention, and the kickoff size leg no longer takes the positional
  the spec cited.

Every measured figure in this build is now a snapshot with the command beside it, not an allowance.
That rule was written into these specs before the reground and the reground is what proved it.

## Out of scope for this build

Named here so the cut-line is one place rather than five.

- No implementation. This build lands a README, five specs and their review records.
- No change to the phase vocabulary, the core phase or Definition-of-Done floors, or the terminal
  set.
- No cap binding attended runs, and no new required field on a review record.
- No change to the governance template. The Definition of Ready stays generic there; the unattended
  disposition for a unit awaiting scope approval belongs to the unattended protocol, which is where
  unit 3 puts it. If the template needs a pointer, that is a playbook unit and a backlog row.
- None of the seven adjacent open backlog rows this build reads and does not fix — the anchor
  forgery class, the leg's recomputed base, the unbound executing kit code, the missing
  cross-component fixture, the planning verb's first-line blindness as a separate row, the
  unpaired shipped protocol version, and the never-landed silent-exit refusals. Unit 4 closes the
  planning verb's blindness as a side effect and says so in its own record.


## The 2026-08-19 re-decomposition

The owner reopened this build with three reports and one reversal. The reversal is the round cap:
`TOOL-aBoundedVerdict-1`'s two-round design is **withdrawn**, not re-tuned. Its replacement, the
measurement that forced it, and the disposition the owner ratified for a residual blocker are in
`build/2026-08-18-build-TOOL-aBoundedVerdict-1-review-loop-design.md`. A five-lens adversarial audit
of the close path ran behind that design and confirmed 32 defects, 3 of them blockers;
`build/2026-08-18-build-TOOL-aBoundedVerdict-1-close-path-audit.md` is the findings table and is the
source every new unit below derives from.

**The reversal in one line.** The cap bound the wrong variable. Over 90 tracked review records the
only exit the method states — a literal clean verdict — occurs **zero** times, while `BLOCKED` is 36
and has no disposition anywhere. A count does not give a loop an exit; it moves the stall earlier.

**Why the build grew from five units to fourteen.** The owner's second report — closing "faces
multiple issues, and often stalls" — was scoped to a full close-path audit rather than to the two
named symptoms, and the audit found that the headline symptom is a dated cross-kit regression rather
than a design flaw: `TOOL-aTetheredRecord-5` began rendering a Records table inside the region the
driver selects unit rows out of by row shape, which makes `build-complete` and
`closing-review-recorded` mutually unsatisfiable on 49 of 49 builds. Nine new units carry that and
the rest of the confirmed set.

### Classification, per the build method's four states

| Unit | State | What it needs |
|---|---|---|
| `-11` `-12` `-13` `-14` `-15` `-16` `-17` `-18` `-19` `-21` | **SPECCED** | all authored this session; `-21` was created by the owner's resolution of `-13` F3 |
| `-1` | **THIN by reversal** | its design is withdrawn; rev-6 replaces the cap with the convergence rule and deletes the S8 the audit found vacuous |
| `-5` | **THIN** | its S1 spells a three-field `--park` and its S5 a decision-only count; the verb that shipped under `TOOL-cSettledDocket-1` has two fields and counts four kinds, so the spec and the code disagree |
| `-2` | **READY, widening** | gains the verdict-token half — the vocabulary a machine can read is the same problem one document over |
| `-3` | **READY** | unchanged in scope. Its rev-6 adds two cross-references only: its halt path reaches `--abort`, whose agent keys `-15`'s `--attest` writes, and the review-side analogue of its park rule is `-1` S9. `--attest` is `-15`'s and the non-overridable sentence is `-19`'s — an earlier draft of this row gave both to `-3`, which would have put two units on one mechanism |
| `-4` | **READY** | unchanged by any of this |

### What the audit changed about the dependency order

`-11` moves to the front. It is the owner's ratified mechanism — the units region becomes generated
and mandatory — and three other things wait on it: `build-complete` cannot pass until it lands, the
promotion disposition `-1` now carries needs a units region a run may legally extend, and `--status`
cannot name a real next unit without it. `-12` and `-13` are independent blockers on the same verb
and neither waits for anything.

### The trap the ratified resolution must not fall into

The frozen scope cannot move into the run-state file. That file is written by the run, and a scope
frozen where its subject can write it is `memory/gotchas/inputs-inside-the-subjects-reach.md`. The
authority stays the BASE blob, re-derived through git by both the driver and the leg.

## The unattended run, 2026-08-19 — what it built and what it cost

Phase BUILDING, blocked short of landing. `RUN.md` holds the phase, the witness and three parked
decisions; this section is the derivation an owner reads first.

**Built and green:** `TOOL-aBoundedVerdict-11`, all eight scope items. Driver suite 333 assertions
(315 before), leg sibling 182, `check-arms` clean. Status INPROGRESS rather than CLOSED, deliberately:
CLOSED means built AND landed, and marking it otherwise would make `build-complete` pass on a claim
the tree does not support — the class the unit exists to remove.

**Not started:** the other fourteen units. One consumed the run, and beginning a second while the
first cannot land would accumulate rather than finish.

### Why it stopped

`gates-green` is unreachable, and not because of this diff. Leg check 7 — at most one live run — reds
on two non-terminal records: this one and `aPacedTurnstile`'s, which arrived with the merge from main
at `6f598a1`. That run overrode `build-complete`, could not land because the primary tree's main was
ahead by three commits of a different mid-flight build, and stopped at phase LANDING. `LANDING` is not
in `PHASES_TERMINAL`, so the record is live forever and check 7 counts it against every later run: one
stuck run is a fleet-wide block. `TOOL-aBoundedVerdict-24`.

Every exit is outside this mandate. `--override gates-green` is refused on this repo's own record —
`aBranchedMandate`'s commit says spending it means spending the one machine check between an
unattended run and an unverified landing, and that someone else's red is a reason to escalate rather
than to spend it. Writing `--landed` or `--abort` onto another node's record is not this run's to do.
So it is parked and escalated, which is what a gate-red-out-of-scope halt names. Two prior runs in
this corpus met the same class and both parked; this is the third.

### The four parked decisions — the owner's turn this run did not take

Each was parked through the verb, so `RUN.md` carries the question, the options seen and the
reason. Enumerated here because the wrap-up derives from this file, and a parked entry the
owner never reads is the "forgotten" the method says a bare park is indistinguishable from.

| # | The question | What the run did instead |
|---|---|---|
| 1 | **The closing review's base**, now that the run has merged `origin/main`. M8 pins it to the run's BASE, and that pin now predates 25 commits this run did not write. | Took the merge-base and recorded the deviation rather than silently reinterpreting a binding rule. |
| 2 | **`-11` S8 retired the authored roster wholesale**, which made `build-complete`'s missing-units term a tautology — the generated region is a subset of the specs by construction. | SPLIT the two questions instead of retiring: authorization, presence and terminality read the generated region; the planned-but-unspecced question keeps the authored pair, the only thing that can express it. Dropping the term outright remains the owner's to prefer. |
| 3 | **`gates-green` is unreachable**, because another node's run is live at `LANDING` and is not this run's record to write. | Escalated rather than overriding. Two prior runs in this corpus met the same class and both parked; this is the third. |
| 4 | **`drift-audit`'s non-terminal-spec-citation signal is unsatisfiable** for any multi-unit build that cites its ids in code: CLOSED needs landing, landing needs green, green needs CLOSED. | Filed as `TOOL-aBoundedVerdict-30` with three options named, none of them this run's to pick. |

One OWNER FORK also remains open in the spec set: `TOOL-aBoundedVerdict-21` F3 — whether a
bounded-out push whose outcome is unknown should wake someone immediately rather than wait for
the resume path. It would add an owner-notification mechanism this kit does not have.

### Recommendations, in the order that unblocks the most

Put to the owner in the run's own turn and recorded here, because a recommendation
that lives only in a transcript is one nobody reads again.

1. **Clear `aPacedTurnstile` first.** One command, and it unblocks the FLEET rather than
   this run: its record sits at `LANDING`, which is not terminal, so check 7 counts it
   against every later run. `--landed` if that push landed, `--abort` if it did not. Then
   make `TOOL-aBoundedVerdict-24` a real unit — one stuck run becoming a fleet-wide bar
   outage will recur, and it is not a subtle failure.

2. **Land this branch before building the remaining ten units.** Five are built, armed and
   green, and they fix owner issues 2 and 3 outright. Landing makes the rest CHEAPER,
   because `build-complete`, the message channel and the review scoping start working.
   The unlanded diff is already ~67 commits, and the closing review over it is exactly the
   over-large review this build exists to prevent.

3. **Fix `TOOL-aBoundedVerdict-30` before the next unattended run.** Recommended shape: add
   a signal state for "cited by the diff that implements it". Do NOT stop citing unit ids in
   shipped code — that provenance is what made half this run's findings traceable — and do
   not touch a pin whose shrink-only direction is deliberate.

4. **Take the four parked decisions and the one open owner fork** (`-21` F3, whether an
   unknown-outcome push should wake someone). All carry their options and reasoning.

5. **Two method changes, weighted highest.** The two adversarial audits produced 118
   findings and caught NONE of the defects execution found, including three that would have
   bricked the run at close after all fifteen units were built.
   - **A completion sweep per unit.** Three times this run a unit was called done while its
     own Files-touched list named carriers nobody had opened — four documentation halves,
     two kit versions, a status flip; 1-of-5 at the low point. Mechanical, and gateable:
     every id whose spec reads INPROGRESS must have its named carriers touched in the same
     range.
   - **Treat "green at an unchanged assertion count" as a failure.** It happened twice — six
     scope items and an entire contract change, both unmeasured and both nearly read as
     confirmation.

**Not recommended:** building further units before landing, and spending
`--override gates-green` for a red that belongs to another run. Two prior runs in this
corpus refused that override on exactly these grounds, and the precedent is worth more than
this run finishing.

### The twelve defects the run found by EXECUTING

None was reachable by reading. Two adversarial audits over this same material — 33 findings on the
close path, 85 on the spec set — caught none of them.

| where | what |
|---|---|
| `-11` design | the cutoff was missing, so the unit was unlandable by ANY run |
| | the cutoff lived in a conf the driver cannot read |
| | the cutoff comparison was INVERTED — it would have refused this run at close |
| | S8 retired the authored roster wholesale, making a DoD term a tautology |
| S4 | refused every BRAND-NEW build: `unit_rows` returns 1 on a well-formed but empty region |
| test arms | a branch unreachable from any arm, because the fixture conf never declared the key |
| | two arms that masked the branch under test by tripping an earlier refusal |
| | a cutoff moved by export rather than through the conf the driver SOURCES |
| fixtures | two fixture READMEs that could not exercise the check written for them |
| tooling | a text-mode read destroyed three raw CR bytes and broke an unrelated check |
| | `&&` put a `mkdir` inside a background job, so its sibling raced it |
| naming | a loop variable called `rm` tripped the leg's own read-only guard, correctly |

Three of the first four would have surfaced **at close, after all fifteen units were built**.

### What the run corrected in its own specs

`-11` moved rev-2 → rev-6 while being built: the id-set comparison replacing a byte compare that
would have refused every run that built anything; the cutoff and its home; S8 narrowed from *retired*
to *split*, because the authored roster is the only carrier of a planned-but-unspecced unit and the
generated region is a subset of the specs by construction. Each rev names what was wrong and how it
was found.

<!-- gen:build-index -->
**Build status:** SPECCED · 15 unit(s) · node a · opened 2026-08-16 · streams tooling
ids TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-6 TOOL-aBoundedVerdict-7 TOOL-aBoundedVerdict-8 TOOL-aBoundedVerdict-9 TOOL-aBoundedVerdict-10 TOOL-aBoundedVerdict-11 TOOL-aBoundedVerdict-12
ids TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-14 TOOL-aBoundedVerdict-15 TOOL-aBoundedVerdict-16 TOOL-aBoundedVerdict-17 TOOL-aBoundedVerdict-18 TOOL-aBoundedVerdict-19 TOOL-aBoundedVerdict-20 TOOL-aBoundedVerdict-21 TOOL-aBoundedVerdict-22 TOOL-aBoundedVerdict-23 TOOL-aBoundedVerdict-24
ids TOOL-aBoundedVerdict-25 TOOL-aBoundedVerdict-26 TOOL-aBoundedVerdict-27 TOOL-aBoundedVerdict-28 TOOL-aBoundedVerdict-29 TOOL-aBoundedVerdict-30

<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aBoundedVerdict-1 — the review loop converges or promotes, and no round is refused by a counter](spec/2026-08-16-spec-TOOL-aBoundedVerdict-1.md) | SPECCED | rev-8 | 2026-08-19 |
| [TOOL-aBoundedVerdict-2 — a halted run records WHY, in a vocabulary something reads](spec/2026-08-16-spec-TOOL-aBoundedVerdict-2.md) | SPECCED | rev-6 | 2026-08-19 |
| [TOOL-aBoundedVerdict-3 — every remaining place a run would wait for the owner gets a disposition](spec/2026-08-16-spec-TOOL-aBoundedVerdict-3.md) | SPECCED | rev-6 | 2026-08-19 |
| [TOOL-aBoundedVerdict-4 — a fork that says it is unresolved stops reading as resolved](spec/2026-08-16-spec-TOOL-aBoundedVerdict-4.md) | SPECCED | rev-5 | 2026-08-17 |
| [TOOL-aBoundedVerdict-5 — parking becomes a verb instead of a hand-edit](spec/2026-08-16-spec-TOOL-aBoundedVerdict-5.md) | SPECCED | rev-7 | 2026-08-19 |
| [TOOL-aBoundedVerdict-11 — the units region becomes generated, mandatory, and read by name](spec/2026-08-19-spec-TOOL-aBoundedVerdict-11.md) | CLOSED | rev-8 | 2026-08-19 |
| [TOOL-aBoundedVerdict-12 — a blocked close names its cause, not just the item it blocked on](spec/2026-08-19-spec-TOOL-aBoundedVerdict-12.md) | CLOSED | rev-3 | 2026-08-19 |
| [TOOL-aBoundedVerdict-13 — every remote observation is bounded, and pays its cost last](spec/2026-08-19-spec-TOOL-aBoundedVerdict-13.md) | SPECCED | rev-2 | 2026-08-19 |
| [TOOL-aBoundedVerdict-14 — an adversarial round after the first reviews the fold, not the build](spec/2026-08-19-spec-TOOL-aBoundedVerdict-14.md) | CLOSED | rev-4 | 2026-08-19 |
| [TOOL-aBoundedVerdict-15 — every close-path write is staged, guarded, and reachable by a verb](spec/2026-08-19-spec-TOOL-aBoundedVerdict-15.md) | CLOSED | rev-3 | 2026-08-19 |
| [TOOL-aBoundedVerdict-16 — `closing-review-recorded` joins a diff-review, in range](spec/2026-08-19-spec-TOOL-aBoundedVerdict-16.md) | CLOSED | rev-2 | 2026-08-19 |
| [TOOL-aBoundedVerdict-17 — a split fetch/push URL stops being an unsatisfiable authorization](spec/2026-08-19-spec-TOOL-aBoundedVerdict-17.md) | SPECCED | rev-1 | 2026-08-19 |
| [TOOL-aBoundedVerdict-18 — the two checks that cannot fail get subjects](spec/2026-08-19-spec-TOOL-aBoundedVerdict-18.md) | SPECCED | rev-2 | 2026-08-19 |
| [TOOL-aBoundedVerdict-19 — the protocol pair says what the code does, and one closed AC is settled](spec/2026-08-19-spec-TOOL-aBoundedVerdict-19.md) | SPECCED | rev-1 | 2026-08-19 |
| [TOOL-aBoundedVerdict-21 — the landing push is bounded too](spec/2026-08-19-spec-TOOL-aBoundedVerdict-21.md) | SPECCED | rev-1 | 2026-08-19 |
<!-- /gen:build-units -->

Records live under `spec/`, `build/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-16-build-TOOL-aBoundedVerdict-1-flow-research.md](build/2026-08-16-build-TOOL-aBoundedVerdict-1-flow-research.md) | — | *none — an adversarial research pass run BEHIND this build; it precedes the spec set and is what warranted it* |
| [2026-08-18-build-TOOL-aBoundedVerdict-1-close-path-audit.md](build/2026-08-18-build-TOOL-aBoundedVerdict-1-close-path-audit.md) | research | TOOL-aBoundedVerdict-1 |
| [2026-08-18-build-TOOL-aBoundedVerdict-1-review-loop-design.md](build/2026-08-18-build-TOOL-aBoundedVerdict-1-review-loop-design.md) | research | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 |
| [2026-08-16-review-TOOL-aBoundedVerdict-1-2.md](reviews/2026-08-16-review-TOOL-aBoundedVerdict-1-2.md) | spec-audit | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 |
| [2026-08-16-review-TOOL-aBoundedVerdict-1.md](reviews/2026-08-16-review-TOOL-aBoundedVerdict-1.md) | spec-audit | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 |
| [2026-08-19-review-TOOL-aBoundedVerdict-1-2.md](reviews/2026-08-19-review-TOOL-aBoundedVerdict-1-2.md) | spec-audit | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-11 TOOL-aBoundedVerdict-12 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-14 TOOL-aBoundedVerdict-15 TOOL-aBoundedVerdict-16 TOOL-aBoundedVerdict-17 TOOL-aBoundedVerdict-18 TOOL-aBoundedVerdict-19 |

Ids no record names: TOOL-aBoundedVerdict-21.

Ids no `spec-audit` record has ever named: TOOL-aBoundedVerdict-21.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-16-spec-TOOL-aBoundedVerdict-1.md](spec/2026-08-16-spec-TOOL-aBoundedVerdict-1.md)
  - [2026-08-16-spec-TOOL-aBoundedVerdict-2.md](spec/2026-08-16-spec-TOOL-aBoundedVerdict-2.md)
  - [2026-08-16-spec-TOOL-aBoundedVerdict-3.md](spec/2026-08-16-spec-TOOL-aBoundedVerdict-3.md)
  - [2026-08-16-spec-TOOL-aBoundedVerdict-4.md](spec/2026-08-16-spec-TOOL-aBoundedVerdict-4.md)
  - [2026-08-16-spec-TOOL-aBoundedVerdict-5.md](spec/2026-08-16-spec-TOOL-aBoundedVerdict-5.md)
  - [2026-08-19-spec-TOOL-aBoundedVerdict-11.md](spec/2026-08-19-spec-TOOL-aBoundedVerdict-11.md)
  - [2026-08-19-spec-TOOL-aBoundedVerdict-12.md](spec/2026-08-19-spec-TOOL-aBoundedVerdict-12.md)
  - [2026-08-19-spec-TOOL-aBoundedVerdict-13.md](spec/2026-08-19-spec-TOOL-aBoundedVerdict-13.md)
  - [2026-08-19-spec-TOOL-aBoundedVerdict-14.md](spec/2026-08-19-spec-TOOL-aBoundedVerdict-14.md)
  - [2026-08-19-spec-TOOL-aBoundedVerdict-15.md](spec/2026-08-19-spec-TOOL-aBoundedVerdict-15.md)
  - [2026-08-19-spec-TOOL-aBoundedVerdict-16.md](spec/2026-08-19-spec-TOOL-aBoundedVerdict-16.md)
  - [2026-08-19-spec-TOOL-aBoundedVerdict-17.md](spec/2026-08-19-spec-TOOL-aBoundedVerdict-17.md)
  - [2026-08-19-spec-TOOL-aBoundedVerdict-18.md](spec/2026-08-19-spec-TOOL-aBoundedVerdict-18.md)
  - [2026-08-19-spec-TOOL-aBoundedVerdict-19.md](spec/2026-08-19-spec-TOOL-aBoundedVerdict-19.md)
  - [2026-08-19-spec-TOOL-aBoundedVerdict-21.md](spec/2026-08-19-spec-TOOL-aBoundedVerdict-21.md)
- **`build/`**
  - [2026-08-16-build-TOOL-aBoundedVerdict-1-flow-research.md](build/2026-08-16-build-TOOL-aBoundedVerdict-1-flow-research.md)
  - [2026-08-18-build-TOOL-aBoundedVerdict-1-close-path-audit.md](build/2026-08-18-build-TOOL-aBoundedVerdict-1-close-path-audit.md)
  - [2026-08-18-build-TOOL-aBoundedVerdict-1-review-loop-design.md](build/2026-08-18-build-TOOL-aBoundedVerdict-1-review-loop-design.md)
- **`reviews/`**
  - [2026-08-16-review-TOOL-aBoundedVerdict-1-2.md](reviews/2026-08-16-review-TOOL-aBoundedVerdict-1-2.md)
  - [2026-08-16-review-TOOL-aBoundedVerdict-1.md](reviews/2026-08-16-review-TOOL-aBoundedVerdict-1.md)
  - [2026-08-19-review-TOOL-aBoundedVerdict-1-2.md](reviews/2026-08-19-review-TOOL-aBoundedVerdict-1-2.md)
<!-- /gen:build-docs -->
