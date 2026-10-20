# Stall and loop prevention: every loop ends, every wait expires

**Serves:** research PLAY-dClosedLoop-1

The owner asked for the last major part of the design not yet reviewed: whether anything keeps work from stalling or
looping without end, and which layer it lives in. Five researchers each took one question, and their returns are saved
verbatim beside this record. This record answers the owner's two questions, recommends one system that bounds every
loop and every wait, places each part on the layer and build that owns it, and puts the choices it cannot make itself
to the owner.

## [words] The owner's request, 2026-10-19

> Let's review one of the last major parts of the design we haven't reviewed before prior to finalizing the design:
> stall prevention and infinite loop detection. Is there a system to prevent work from being infinitely
> stalled/delayed due to any reason? What layer of the system does it implement through? One example case: tier2
> reviews, spec reviews could previously run infinitely due to non-converge, that's why in the current Gov
> implementation spec reviews were moved to opt-in only while closing diff reviews run ones and promote their
> findings to build units. The main objective, in the end, is to produce features in reasonable time - not waste
> resources on running an infinite non-convergent loop. With the new architecture, I can see several potential loops
> cycling, wasting resources, and stalling work - testers handing work back to design, design still not converging,
> hooks stalling work while agents are unable to comply with the hooks' instructions - a lot of refusal steps have
> been decided on in this design, which will inevitable cause stalls. Since custom scenarios and flow steps are
> possible, this will lead to unforeseen chains which can potentially stall. Research an extensive set of infinite
> loop/stall scenarios in the newly designed architecture and account for a reasonable stall and loop prevention
> system.

## [questions] Five researchers, one question each

| Dispatch | Question | Return |
|---|---|---|
| 143 | Every cycle, retry, wait and hold the converged design plans: its bound, what happens at the bound, who sees it. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-stall-census.md` |
| 144 | Every refusal the design plans or today's tree enforces, and whether its target can act on it. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-stall-refusals.md` |
| 145 | Concrete scenarios in which the design stalls or loops, the repository's own compositions included. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-stall-scenarios.md` |
| 146 | The stalls and loops gov has actually suffered, and what stopped each. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-stall-history.md` |
| 147 | How other systems keep work from stalling or looping, and which mechanisms fit gov. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-stall-prior-art.md` |

## [answer] The owner's questions, answered

- **Is there a system?** No. The converged design has eleven separate bounds, and no single place guarantees that a
  build ends. Each bound is keyed to something the loop itself can reset or renew:
  - `flow.route-backs` counts per item, and a loop that mints new units starts fresh counters. A probe drove a red
    route back that always makes a new unit: a per-item counter never escalated in 1,000 events, while a per-build
    counter escalated at 10 (dispatch 147, P1).
  - Past the count, the loop becomes an owner item that the default `run.on-owner-question: best-effort-recorded`
    answers by the supervisor's own choice, and nothing stops that choice from resuming the loop (dispatch 145,
    SC-flow-1).
  - Today's resume cap resets on any transcript entry, so an act that writes and never finishes relaunches without end
    (dispatch 145, P1; `tools/unattended/resume-tick.sh:70-74`).
  - A refused item stays on the frontier: "`next` returns the frontier", and "an unwitnessed one can always be
    dispatched again". No refusal is counted anywhere, today or in the design (dispatches 143, C28, and 144).
  - The census found 54 cycles and waits, 19 kinds of them unbounded. Under the defaults one chain allows 384 return
    attempts before any owner item, and a closing review whose findings keep minting units allows about 1,440
    act-hours before Test's exit (dispatch 143).
- **Which layer?** The core, because a stall is a failure of the one loop itself (P1), never of an expansion. One
  contract, split by responsibility:
  - **Flow** owns the contract: one budget per build, the outcome when it runs out, the convergence rule, and a static
    check that every composition can finish (dDeclaredLoop).
  - **Runtime** enforces it: progress counted from witnesses, never from activity; deadlines on every wait; the
    refusal breaker; the queue without hold-and-wait; the wait graph across builds (dWellOiledMachine).
  - **Roles** makes a refusal something its target can act on: a typed refusal naming its rule, its remedy and the
    remedy's actor (dBoundRoles).
  - **Review** computes whether a round converged (dFairHearing).
  - **Observability** trends stalls and loops and re-derives the defaults from evidence, never deciding a position
    (dCalibratedLens).

## [today] What gov does today, measured

From gov's own records and this node's logs (dispatches 144 and 146):
- **Reviews do not converge on findings.** Confirmed findings stay flat at 14 to 23 per round. In 33 of 79 subjects
  round 2 found as many as round 1 or more. Blockers fall, then plateau at 1 to 3.
- **The fold causes the next round.** A round's own fold caused 68% to 97% of the next round's findings in the four
  records that counted them.
- **What stopped review loops:**
  - the strict-decrease rule (`tools/unattended/unattended.sh:12473-12481`): 156 CONVERGED, 51 NON-CONVERGENT and 10
    BOUNDED exits, no subject past 5 driver rounds;
  - one spec audit by default, then owner-only opt-in (spec subjects with two or more rounds fell from 48% to none
    outside this build);
  - promoting findings to units instead of folding them.
- **What never fired:**
  - `RUNAWAY_CEILING` (8), whose halt code appears nowhere under `memory/`;
  - `RESUME_ATTEMPTS` (6): all 23 recorded resumes were manual;
  - the promotion chain's precision floor, which `unattended.sh` never reads.
- **Loops a person had to stop:**
  - a promotion cascade of four audit generations, about 12M tokens, stopped by the run's own override;
  - a nine-round closing review, stopped by the owner's word;
  - a weekly-limit wake loop, 115 wakes over 4.8 days, ended by the quota reset and a manual resume.
- **Waits that outlived their work:** 16 owner-decision hand-offs; 8 run records still read HELD after their work
  landed.
- **Refusals:** no hook refusal is counted, and a builder was refused 10 times in a row by one rule before it returned
  a divergence. No refusal alone ended a run unresolved in the transcript corpus: each streak ended in an admitted call
  or a typed divergence, which `--plan` then re-offered.

## [design-today] What the converged design already has

From dispatch 143's census of 54 cycles and waits:
- **Bounded with an ending:** role retries (`roles.retries` 3), one spec-audit round by default, the act ceiling
  (1.5 h), the experiment fan, Stop-hook caps, the mail fetch timeout.
- **Bounded, then a wait nothing bounds:** every route back (`flow.route-backs` 3, then an owner item), the session-limit
  hold (6 h, then an owner item that "keeps holding"), the stale remote (24 h, then a park), the release hold (72 h,
  restarting on every "keep waiting").
- **Unbounded:**
  - re-dispatch after a refusal, a voided witness or a crashed SubagentStop;
  - patch-build chains, each new build starting at zero;
  - closing-review follow-up rounds, if a follow-up is not counted;
  - loops before `entry.claim`, research and probe round trips;
  - supervisor restarts, and `invalid-input`, which only journals;
  - every wait with no ceiling: dependency holds, mailbox disposal, the admission queue, quarantine, scenario
    conflicts, owner gates under `strict`;
  - `flow.adapt` changes, and cycles of repository routes over an acyclic `needs` graph;
  - release retries.
- **Records disagree:** whether a resume cap counts relaunches of one act or consecutive fruitless launches; whether a
  waiting build's lease is renewed; and the closing review lost today's `RUNAWAY_CEILING` backstop.

## [scenarios] Where it stalls

Dispatch 145 built 68 scenarios across every layer. The top ten by likelihood times cost under the defaults:

| Scenario | The loop or wait |
|---|---|
| SC-flow-3 | A deterministically refused item stays on the frontier and is dispatched again, forever. |
| SC-flow-2 | The owed closing review finds a HIGH, its findings become units, the follow-up review finds more, and so on. |
| SC-flow-1 | Past `flow.route-backs`, the owner item is answered by the supervisor's best effort, and the loop resumes. |
| SC-rt-1 | An act that writes before it dies never fills the consecutive resume cap. |
| SC-rt-6 | An act reaped at the 1.5 h ceiling relaunches from zero and is reaped again. |
| SC-flow-4 | Another build lands first, the verdict is stale, Test re-verifies, and a low-priority build starves. |
| SC-x-4 | Concurrent builds on a hot file re-conflict at the prepared merge after every landing. |
| SC-rt-3 | A weekly session limit holds launches while the lease keeps renewing, so no node with quota takes over. |
| SC-rt-4 | A killed agent's slot is never released, and a live session's admission queue waits forever. |
| SC-own-5 | Nothing pushes an owner item, so every wait on the owner lasts until the owner opens a session. |

The composition scenarios are the owner's "unforeseen chains": a repository stage routing back into itself, two
scenarios handing a build back and forth, additive `flow.adapt` changes with no cap, a repository role whose return
the driver can never accept, an item whose witness nobody writes, and a repository lens that always finds something.

## [outside] What other systems teach

Dispatch 147 surveyed workflow engines, CI, Kubernetes, distributed systems, agent frameworks, stuck detectors,
review stopping rules, termination proofs and workflow-net soundness, and probed each against gov's setting:
- **Three properties need three mechanisms:** bounded loops (a counter that only falls), bounded waits (a deadline with
  a declared outcome) and bounded thrash (a breaker that classifies retries).
- **Key the counter by build.** Per-item and per-edge counters never escalated when a loop minted new keys; per-build
  did (P1). A race or contention must not count, as Kubernetes ignores disruptions.
- **The strict-decrease rule held.** Today's `review_state` survived every adversarial sequence (P2); every `until-`
  and `while-` rule should exit on a non-decrease.
- **Activity is not progress.** A heartbeat or a transcript write proves liveness only; progress must come from
  witnesses.
- **Soundness alone is not enough.** A planted repository stage with an exit passed the soundness check while an
  uncounted self-loop survived (P5); every cycle must also pass a counted edge.
- **Hold-and-wait deadlocks the queue.** Six acts each making a nested fan of two wedged all six slots at saturation,
  while reserving the whole tree up front finished at tick 18 (P3).
- **A breaker must key on the refusing rule.** Keyed on the action and its observation, a rephrased refused write never
  tripped; keyed on the rule, it tripped at event 4 (P4).
- **Owner waits need a deadline too.** GitHub fails an unapproved deployment after 30 days, and escalation alone ends
  in a silent assignment.

## [design] The recommendation: a budget, a convergence rule, deadlines, actionable refusals, a watchdog, a static check

A new principle carries it: **P39 Every loop ends and every wait expires.** Every way work can repeat draws on one
budget per build that only the owner can raise; every wait carries a deadline and a declared outcome; every refusal
names a remedy its target can perform, or goes at once to an actor who can; and a build that stops making witnessed
progress is stopped by a detector, never by a person noticing.

1. **One rework budget per build.** Every repetition draws on it:
   - a route back to an earlier item or step, and a fix pass;
   - a review round after the first, a follow-up round included;
   - a re-dispatch of an unwitnessed item instance after a refusal, a voided witness or a lost SubagentStop;
   - a research or probe round trip;
   - a patch build raised by the build's own landing, which shares the originating build's budget, so a chain of
     patch builds draws on one budget.
   The budget is keyed to the build, never to an item instance, so units a loop mints cannot reset it. Until
   Design's exit freezes the per-unit shares, the budget is the base alone, as it is for a build with no units (the
   parked debt's review). Before `entry.claim`, loops draw on a budget keyed to the intake's content key.
   `flow.route-backs` stays as the per-item early limit. The remaining budget is on the card.
2. **Contention is queued, never counted.** A verdict staled by another build's landing, a prepared merge that
   conflicts after another landing, and a wait for an admission slot are contention. They wait in order in the landing
   queue (`gap-flow-08`) or the admission queue and draw nothing from the budget, so a busy main never turns a healthy
   build into an owner item.
3. **When the budget runs out, the build ends.** The outcome is declared (`flow.on-exhausted`), and no outcome loops
   again. Under the default the driver takes the ending its evidence supports, and records it for the owner:
   - land what is witnessed green, every open finding filed as an ask with its evidence;
   - or, where only some units fail, descope them to asks and land the rest;
   - or, where nothing can land, close the build incomplete, its branch and records kept, every open item filed.
   This keeps the owner's FR-4 and FR-12, "Builds DO NOT get parked on the unresolved fork pretext": best effort still
   decides, but it may choose only among endings. Raising the budget is the owner's alone.
4. **Every iterative rule stops when it stops converging.** Today's strict-decrease rule applies to every `until-*`
   and `while-*` value, spec audits, closing-review follow-ups and fix passes against one acceptance red:
   - dFairHearing's report computes each round's state against the round before, CONVERGED, NON-CONVERGENT, BOUNDED
     or CEILING, from its blocker and high count;
   - a NON-CONVERGENT round's findings are promoted, to units while budget remains and to asks after, never folded
     into another round;
   - `RUNAWAY_CEILING` becomes the policy key `review.max-rounds` and bounds every review loop, the closing review
     included.
5. **Progress is a witness, never activity.** Runtime's supervisor keeps a progress ledger per item instance: each
   act records whether it produced a new witness, a new commit on its unit, a changed findings digest, or a refusal and
   its rule. Then:
   - **no progress:** `runtime.no-progress` acts on one instance with no new witness make the item stuck; it draws on
     the budget and routes to its producer;
   - **repeat:** a repeat of the act before's verdict digest or refusal rule on one instance is no new witness, so
     it counts toward `runtime.no-progress`, and the loop detector journals it; a wait that declares its own
     deadline is exempt, so a poll is no loop. Revised by the parked debt's review: it fired at a fixed two, with no
     outcome;
   - **relaunch:** the cap counts lifetime relaunches of one instance, reset only by a new witness, never by a
     transcript entry; an instance reaped twice at the act ceiling with no new witness routes to its producer to split;
   - **lease:** a build's lease renews on witnessed progress at item boundaries and on declared waits inside their
     deadline, never on activity alone, so a looping holder's lease expires. The supervisor's beat is liveness and
     renews nothing, and until the ledger lands the transition record's item boundaries stand in for it (the parked
     debt's review).
6. **Every wait has a deadline and an outcome.** Every `awaiting`, hold, park, dependency hold, mailbox disposal,
   queue wait, quarantine, release hold and owner item declares both:
   - **owner items:** a deadline (`run.owner-deadline`), then the outcome `run.on-owner-silence` says for an item
     `run.on-owner-question` left open. A ratification or an owner-only write is never decided for the owner, and an
     approval that would loosen a value recommends the decline, so silence never applies a loosening (the parked
     debt's review);
   - **the session-limit hold:** at `runtime.hold-ceiling` the lease is released as a hand-over, so a node with quota
     takes the build over, and the wake tick stops firing into a refused turn;
   - **the admission queue:** a wait past the act ceiling, `runtime.act-ceiling`, with no release writes a stall
     record naming the holders; a slot an act session the supervisor launched holds past it is reclaimed, since
     every act ends by that ceiling, and an attended session's slots only by the liveness sweep (the parked debt's
     review);
   - **dependency and mailbox waits:** past their deadline, the waiter takes its declared default (replan, or the
     asker's default answer);
   - **quarantine:** its threshold gets a default, and a held leg runs at least once each period;
   - **release hold:** each "keep waiting" is counted per build and landed SHA, and the third parks the build;
   - **supervisor restarts:** more than a set number in an hour stop the supervisor and raise an owner item, as an
     Erlang supervisor escalates; `invalid-input` raises an owner item at once instead of only journaling.
7. **Refusals are actionable, or they escalate.** Every refusal is a typed record: its rule, its remedy, and the
   remedy's actor, who is the refused agent, its producer, the driver, the owner or another build:
   - the hook-pack contract v2 already plans ("a hook pack's refusal text, naming its rule and its remedy, declared in
     the pack's contract and checked at registration") also declares the remedy's actor;
   - a remedy the refused actor cannot perform within its grant routes at once to that actor, and the item is never
     re-offered to the refused agent;
   - a breaker per act and rule: the same rule refusing `runtime.refusal-repeats` times in one act ends the act with a
     typed refusal return, and the item draws on the budget and routes to the remedy's actor;
   - registration refuses a remedy another registered guard refuses, which catches the cycles dispatch 144 found
     between guards.
8. **The static termination check.** Every composition, gov's packs with the overlay, the scenarios and a build's
   recorded changes, is checked at the push and at each step boundary a build moves:
   - every state reaches a terminal, and every item is reachable;
   - every cycle in the build and item transition tables passes a counted edge: drop the counted and owner edges, and
     the rest is acyclic;
   - every wait declares a deadline and an outcome;
   - every nested spawn draws from its parent's reservation, never queues again;
   - scenario successor chains are acyclic;
   - raising any loop bound (the budget, a round count, a retry count, a deadline) is a loosening: under `flow.adapt`
     it waits for the owner, and in the overlay it is a widening the update's report names.
9. **Waits across builds are graphed.** When a wait passes half its deadline, the supervisor builds the wait graph
   across builds (parent holds, interface waits, lease waits, open mailbox questions). A cycle raises one owner item
   naming every build in it, and a parent that ends incomplete releases its dependents to `deps.on-parent-withdrawn`.
10. **Owner items reach the owner.** Progress keeps reaching the owner as the owner's FR-3 settled, by the micro-format
    lines at each turn's end. While no owner session is open, owner items alone are also pushed through the
    registered channel, as the owner's SL-6 settled it, and `notify.owner-items` lets the owner change that. A push
    reaches an absent owner only through a channel other than the terminal, so a core-only install reports that it
    has none (the parked debt's review).
11. **Observability trends, never decides.** Runtime journals every stall and loop event with its class: no progress,
    repeat, budget spent, deadline passed, breaker open, cycle across builds. The Loop Review trends them per
    scenario, item and rule, and re-derives the budget, the deadlines and the thresholds from that evidence (P9).

## [layers] Which layer owns what

| Layer | Build | What it owns |
|---|---|---|
| Policy | dGroundRules | the keys' schema and their declared loosening direction |
| Entry | dPlacedRequest | the pre-claim budget keyed by intake content |
| Flow | dDeclaredLoop | the rework budget, contention routed to the queues, the ending when the budget runs out, the convergence routing, `review.max-rounds`, the static termination check |
| Review | dFairHearing | each round's state computed against the round before |
| Session | dKeptSession | the mailbox's question deadlines, and the remaining budget on the card |
| Roles | dBoundRoles | the typed refusal return, and routing to the remedy's actor |
| Test | dWitnessedBar | quarantine's default threshold and its run each period, and what a quiet host is |
| Runtime | dWellOiledMachine | the progress ledger, the no-progress and repeat detectors, the relaunch cap, lease renewal on progress, every wait's deadline and outcome, the refusal breaker, the queue's reservation and stall check, the wait graph across builds, restart intensity, an owner item's deadline and push, and each build's spend |
| Deploy | dShippedRelease | patch-build chains on the originating budget, counted release retries and holds, the landing queue |
| Review loop | dCalibratedLens | trends of every stall and loop class, and defaults re-derived from them |

## [coverage] Every top scenario and unbounded class, and what ends it

| Scenario or class | Ended by |
|---|---|
| SC-flow-3, refusal re-dispatch (census C28) | item 7's breaker and remedy routing; each re-dispatch draws on item 1's budget |
| SC-flow-2, follow-up review chains (C8) | item 4's convergence rule and promotion; each round draws on the budget |
| SC-flow-1, best effort resuming a loop | item 3: past the budget, best effort may choose only an ending |
| SC-rt-1, the resume cap resetting | item 5's lifetime relaunch count, reset only by a witness |
| SC-rt-6, reaped and restarted from zero | item 5: two reaps with no witness route to the producer to split |
| SC-flow-4 and SC-x-4, landing races and re-conflicts | item 2: contention queues, and draws nothing |
| SC-rt-3, the session-limit hold | item 6: the lease released at the hold ceiling |
| SC-rt-4, a leaked admission slot | item 6's stall check and reclaim; item 8's reservation rule |
| SC-own-5, owner items unseen | item 10, as the owner's SL-6 settled it, where a push channel other than the terminal is registered; a core-only install reports `push-when-away` with none |
| Patch-build chains (C48) | item 1: one budget along the chain |
| Waits with no ceiling (C20, C22, C36, C40, C43) | item 6, checked by item 8 |
| Composition chains (SC-comp-1 to 8) | item 8; item 1 for what the check cannot see |
| Builds waiting on each other (SC-x-1, SC-x-2) | item 9 |
| Refusal cycles between guards | item 7's registration check |
| `invalid-input` and supervisor restarts (C33, C34) | item 6 |

## [chain] Where it lands

Each clause sits on the build that registers its kind, or on a descendant of every build whose schema it reads:
- **dGroundRules:** each loop bound and deadline key declares that raising it is a loosening.
- **dPlacedRequest:** the pre-claim budget keyed by intake content, seen red on a planted placement loop.
- **dFairHearing:** each round's state in the review report, computed against the round before, seen red on a planted
  flat and an oscillating sequence, and on falling ones that reach and pass the caller's limit.
- **dDeclaredLoop:**
  - the rework budget in the transition record, the base alone before Design's exit, every repetition kind drawing
    on it, seen red on a planted loop that mints a new unit each lap and on one that spends the base before
    Design's exit;
  - contention routed to the queues and never counted, seen on a planted stale verdict;
  - `flow.on-exhausted`, each ending planted, and a best-effort choice to loop again refused;
  - the convergence routing for every `until-*` and `while-*` value, and `review.max-rounds`, seen red on a falling
    sequence run past it;
  - the static termination check, seen red on a planted repository stage that routes back into itself with an exit,
    a stage with no path to a terminal, an unreachable item, an empty state set, a wait with no deadline, a
    scenario successor cycle, an unattended raise of a loop bound and an approval item recommending a loosening.
- **dKeptSession:** mailbox question deadlines with the asker's default; the remaining budget on the card, seen red
  on a card without it; the pair rule holding `review.design.round-count` at or below `review.max-rounds`.
- **dBoundRoles:** the typed refusal return with its rule, remedy and actor in every role's template, and remedy
  routing in the outcome table.
- **dWitnessedBar:** quarantine's default threshold and a held leg run each period; a quiet host defined.
- **dWellOiledMachine:** the progress ledger; the no-progress and repeat detectors; the lifetime relaunch cap; lease
  renewal on progress; every held wait's deadline and outcome; the refusal breaker and the remedy-actor check at hook
  registration; the reservation rule and the queue stall check; the wait graph across builds; restart intensity and
  `invalid-input` raised; owner items' deadlines, their push and every silence value; the spend record and the cap's
  outcome. Each is seen red on a planted case of its own, v2's row naming every one, the 115-wake limit loop among
  them (the parked debt's review).
- **dShippedRelease:** patch-build chains on the originating build's budget; release retries and "keep waiting"
  counted; the landing queue, already `gap-flow-08`'s.
- **dCalibratedLens:** the stall and loop classes trended, seen red on a class left out of the trend, and the
  budget, deadlines and thresholds re-derived.

## [gaps] Gaps this adds to the register

| Key | Stage | Sev | Gap | Owner |
|---|---|---|---|---|
| `gap-flow-23` | Flow | HIGH | No bound spans a build: the driver bounds each review loop and each unit pass apart, so a build's total rework has no ceiling; a promotion cascade ran four audit generations, about 12M tokens, before a run's own override stopped it. | dDeclaredLoop |
| `gap-flow-24` | Flow | MED | Nothing checks that a flow can finish or that its loops are counted: the run's phases are code, extension vocabularies add steps unchecked, and a per-item counter never escalated once a loop minted new units. | dDeclaredLoop |
| `gap-rt-37` | Runtime | HIGH | The resume cap counts consecutive fruitless launches and resets on any transcript entry, so an act that writes and never finishes relaunches without end; all 23 recorded resumes were manual. | dWellOiledMachine |
| `gap-rt-38` | Runtime | HIGH | Waits have no deadline or outcome: held runs, limit holds and owner hand-offs wait until a person resumes them; one weekly-limit stall woke a session 115 times over 4.8 days, and 8 run records still read HELD after their work landed. | dWellOiledMachine |
| `gap-rt-39` | Runtime | MED | No refusal is counted: every PreToolUse and git hook refuses afresh, a builder was refused 10 times in a row by one rule, and the stop guard's cap resets with each session. | dWellOiledMachine |
| `gap-roles-31` | Roles | MED | A refusal names no actor for its remedy: three of today's guards name remedies their target cannot perform (a spawn, a parent's kickoff, an owner write), and a refused builder's only exit is a free-text divergence. | dBoundRoles |
| `gap-review-21` | Review | MED | Only the unattended driver computes whether a review round converged: attended reviews, promotion chains and follow-up rounds have no rule, the precision floor is never read, and a round's own fold caused 68% to 97% of the next round's findings. | dFairHearing |

## [forks] For the owner, 2026-10-19

| Fork | Question | Options, the recommendation first |
|---|---|---|
| SL-1 | How is a build's repeated work bounded? | one budget per build, 4 plus 2 per unit frozen at Design's exit, every repetition drawing on it; one budget per build, a flat 8; per item only, as the design stands (`flow.route-backs` 3) |
| SL-2 | When a build spends its budget, what ends it? | best effort picks an ending, never another lap: land what is green and file the rest, descope failing units, or close incomplete; park for the owner; close incomplete at once |
| SL-3 | How do closing-review follow-ups stop? | keep your FR-9 (a follow-up after a HIGH), each round ending when its blocker and high count stops falling, its findings promoted; one round only, every finding promoted; follow-ups while anything is found, under the same rule |
| SL-4 | What happens when the owner does not answer an owner item by its deadline? | remind, then park the item's build and release its lease so other work goes on, the item staying open; apply the recommended option unless it is a ratification or an owner-only write; wait, as today |
| SL-5 | How long is an owner item's deadline? | 72 hours; 24 hours; 7 days |
| SL-6 | While no owner session is open, is an owner item pushed? | push owner items only, through the registered channel, progress staying as your FR-3 set it; nothing pushed, as your FR-3 set it; push owner items and every park |
| SL-7 | When does a repeated refusal stop being retried? | a refusal its target cannot act on routes at once to the remedy's actor, and the same rule 3 times in one act ends the act; the same, at 2; the same, at 5 |
| SL-8 | How is spend bounded beyond the rework budget? | record each build's spend and trend it, then set a cap from the evidence, as `memory.item-budget` was measured first; a spend cap per build now; none |

## [answers] The owner's answers, 2026-10-19

Put to the owner in two batches, each question with its recommendation first. The owner's words, verbatim:

| Fork | The owner's answer |
|---|---|
| SL-1 | "Per build, scaled (Recommended)" |
| SL-2 | "Best-effort ending (Recommended)" |
| SL-3 | "FR-9 + convergence (Recommended)" |
| SL-4 | "Apply recommendation" |
| SL-5 | "24 hours" |
| SL-6 | "owner items only by default, changeable by the policy setting" |
| SL-7 | "at once or after 3 by default,  changeable by the policy setting (2 or 5, or any owner-set number up to 10)" |
| SL-8 | "Measure, then set (Recommended)" |

Four took the recommendation as offered: SL-1, SL-2, SL-3 and SL-8. SL-4 chose the second option: past the deadline,
the item's recommended option applies, unless it is a ratification or an owner-only write, which is never decided for
the owner. SL-5 chose 24 hours over the recommended 72. SL-6 and SL-7 took the recommendation in the owner's own words,
each a policy value the owner may change, and SL-7's count may be any the owner sets up to 10.

## [folded] Where the answers went, 2026-10-19

- **v2:** P39 joins the principles. Eleven keys join the catalogue and every preset: `flow.rework-budget`,
  `flow.on-exhausted`, `flow.wait-ceiling`, `review.max-rounds`, `runtime.no-progress`, `runtime.refusal-repeats`,
  `runtime.restarts`, `notify.owner-items`, `run.owner-deadline`, `run.on-owner-silence` and `build.spend-cap`. Eight rows say
  their part: `leases.renewal` gains `progress` as its default, and `flow.route-backs`, `review.design.round-count`,
  `review.follow-up`, `run.on-owner-question`, `notify.owner`, `runtime.hold-ceiling` and `verdict.flakes` follow.
  Ten chain rows gain clauses, each seen red on its planted case: dGroundRules, dPlacedRequest, dFairHearing,
  dDeclaredLoop, dKeptSession, dBoundRoles, dWitnessedBar, dWellOiledMachine, dShippedRelease and dCalibratedLens.
- **This record, where the fold placed a thing differently from [design], [layers] and [chain]:**
  - an owner item's push moves from dKeptSession to dWellOiledMachine, which registers `notify.channel`, since a
    clause sits on a descendant of every build whose schema it reads;
  - the remaining budget goes on the card through dKeptSession, which updates the card's pointers;
  - the admission queue's stall check reads `runtime.act-ceiling` instead of a key of its own: every act ends by that
    ceiling, so a wait that outlasts it with no release can only be a leaked slot;
  - the owner-item keys join the `run` namespace beside `run.on-owner-question`, as `run.owner-deadline` and
    `run.on-owner-silence`, instead of opening an `owner` namespace for two keys;
  - `leases.renewal` keeps its owner, dPlacedRequest, and gains the value `progress`, which dWellOiledMachine's ledger
    arms;
  - `flow.wait-ceiling` is the deadline gov's own waits declare, and the static check still reds a wait declaring
    none;
  - a CONTENDED red's quiet host is one running no other bar, and a re-run that finds none within the wait ceiling
    raises an owner item.
- **flow-steps:** a refused instance's re-dispatch draws on the budget, and the route-back rule ends a loop instead of
  raising an owner item.
- **layer-runtime:** the relaunch cap counts an instance's life, the session-limit hold releases the lease at its
  ceiling, and `invalid-input` raises an owner item at once.
- **coordination:** a mailbox question waits only until `flow.wait-ceiling`.
- **The gap register:** the seven gaps in [gaps], each on its owning build's chain row.
- **The chain:** nineteen clauses join ten rows, and the critical path grows from 239 units at `ad530a80c` to 253,
  its fourteen new units one on dGroundRules, four on dDeclaredLoop, one on dWitnessedBar, one on dBoundRoles, six on
  dWellOiledMachine and one on dCalibratedLens.
- **The parked debt's review, 2026-10-19:** its pair found the route-back rule's two other homes in
  flow-steps, two layer-runtime fixtures and the supervisor's beat still carrying the outcomes P39
  replaced, and several clauses with no check that can fail. All are folded
  (`build/2026-10-19-build-PLAY-dClosedLoop-1-parked-debt-reviews-compared.md`).

## [owed] Owed to later builds

- The rework budget's default re-derived by the Loop Review once 30 builds have run under it (dCalibratedLens).
- Whether SubagentStop fires for a killed, stalled or owner-stopped agent, which the admission queue's release and the
  in-flight ledger already wait on (dWellOiledMachine's platform spike).
- The no-progress and repeat detectors' false positives measured on gov's own run logs before either blocks
  (dWellOiledMachine).
- The item-level transition tables, which the static check reads and `gap-flow-15` already owes (dDeclaredLoop).
