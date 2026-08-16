---
slug: aBoundedVerdict
node: a
opened: 2026-08-16
streams: tooling
roster: TOOL
ids: TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5
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
| The review loop is real and recent | `memory/builds/aSiftedPlaybook/reviews/` holds five consecutive spec-audit rounds over one 7-unit set plus a sixth closing round, all on one day. Verdicts: CLEAN WITH FIXES, BLOCKED, BLOCKED, BLOCKED, CLEAN WITH FIXES, BLOCKED. Final spec revs reached rev-12 |
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
**Build status:** OPEN · 5 unit(s) · node a · opened 2026-08-16 · streams tooling · ids TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aBoundedVerdict-1 — two review rounds, then the unit stops being reviewed](spec/2026-08-16-spec-TOOL-aBoundedVerdict-1.md) | OPEN | rev-1 | 2026-08-16 |
| [TOOL-aBoundedVerdict-2 — a halted run records WHY, in a vocabulary something reads](spec/2026-08-16-spec-TOOL-aBoundedVerdict-2.md) | OPEN | rev-1 | 2026-08-16 |
| [TOOL-aBoundedVerdict-3 — every remaining place a run would wait for the owner gets a disposition](spec/2026-08-16-spec-TOOL-aBoundedVerdict-3.md) | OPEN | rev-1 | 2026-08-16 |
| [TOOL-aBoundedVerdict-4 — a fork that says it is unresolved stops reading as resolved](spec/2026-08-16-spec-TOOL-aBoundedVerdict-4.md) | OPEN | rev-1 | 2026-08-16 |
| [TOOL-aBoundedVerdict-5 — parking becomes a verb instead of a hand-edit](spec/2026-08-16-spec-TOOL-aBoundedVerdict-5.md) | OPEN | rev-1 | 2026-08-16 |

Records live under `spec/` and `build/`.
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
- **Every new refusal branch is armed in the same unit that adds it.** Adding one refusal to the
  driver was measured to red the harness meta-gate immediately, naming the unarmed branch. Both
  unattended gates sit at fully-armed floors, so the arm is not optional and its floor entry moves
  in the same commit.
- **No spec id in this build may be cited from product source while its status is non-terminal.**
  The drift signal that counts such citations sits at its pin with zero tolerance, and the files
  these units edit are product source.

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
