---
slug: aBoundedVerdict
node: a
opened: 2026-08-16
streams: tooling
roster: TOOL
ids: TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-6 TOOL-aBoundedVerdict-7 TOOL-aBoundedVerdict-8 TOOL-aBoundedVerdict-9 TOOL-aBoundedVerdict-10
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

<!-- gen:build-index -->
**Build status:** SPECCED · 5 unit(s) · node a · opened 2026-08-16 · streams tooling · ids TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-6 TOOL-aBoundedVerdict-7 TOOL-aBoundedVerdict-8 TOOL-aBoundedVerdict-9 TOOL-aBoundedVerdict-10

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aBoundedVerdict-1 — two review rounds, then the unit stops being reviewed](spec/2026-08-16-spec-TOOL-aBoundedVerdict-1.md) | SPECCED | rev-5 | 2026-08-17 |
| [TOOL-aBoundedVerdict-2 — a halted run records WHY, in a vocabulary something reads](spec/2026-08-16-spec-TOOL-aBoundedVerdict-2.md) | SPECCED | rev-4 | 2026-08-17 |
| [TOOL-aBoundedVerdict-3 — every remaining place a run would wait for the owner gets a disposition](spec/2026-08-16-spec-TOOL-aBoundedVerdict-3.md) | SPECCED | rev-5 | 2026-08-17 |
| [TOOL-aBoundedVerdict-4 — a fork that says it is unresolved stops reading as resolved](spec/2026-08-16-spec-TOOL-aBoundedVerdict-4.md) | SPECCED | rev-5 | 2026-08-17 |
| [TOOL-aBoundedVerdict-5 — parking becomes a verb instead of a hand-edit](spec/2026-08-16-spec-TOOL-aBoundedVerdict-5.md) | SPECCED | rev-5 | 2026-08-17 |

Records live under `spec/`, `build/` and `reviews/`.
<!-- /gen:build-index -->

## Units — the authored roster

One mechanism per unit. The `ids:` key above is a reservation range, not this roster.

Each cell is a label. The unit's own Goal section owns the full statement and this table
deliberately does not restate it.

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aBoundedVerdict-4` | 2 | the open-questions predicate, in both readers |
| 2 | `TOOL-aBoundedVerdict-5` | 2 | a park verb |
| 3 | `TOOL-aBoundedVerdict-2` | 2 | the halt code vocabulary |
| 4 | `TOOL-aBoundedVerdict-1` | 2 | the review round cap |
| 5 | `TOOL-aBoundedVerdict-3` | 2 | the stall dispositions |

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
- **The charter read-path budget is shared by four of the five units, and the spender set is stated
  HERE and nowhere else.** Measured at base: 70262 bytes against a ceiling of 86476, so 16214 bytes
  of headroom. `TOOL-aBoundedVerdict-1` and `TOOL-aBoundedVerdict-3` grow the build method;
  `TOOL-aBoundedVerdict-2`, `TOOL-aBoundedVerdict-3` and `TOOL-aBoundedVerdict-5` grow the unattended
  protocol, which is itself a read-path member at 18214 bytes. Two specs previously each named the
  total and named only each other as the other spender, which is how a shared budget gets spent
  twice. No spec carries the figure as authority: the builder re-measures with the corpus reporter.
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
