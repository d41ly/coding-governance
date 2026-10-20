# Execution: the chain built under today's gov, across nodes a, b and d

**Serves:** research PLAY-dClosedLoop-1

After the baseline, the owner asked how the chain is executed. This record holds the owner's words, the research
that answers them, and, once the owner has walked it, the plan. Nothing here opens the chain or starts a node's
work: the baseline's stop holds until the owner approves a plan (`whole-audit.md` `[baseline]`).

## [question]

The owner, 2026-10-20, verbatim:

> Our plan: this entire design is going to be built under the current GOV, by the current /unattended driver. Since
> the build is very large, I want to distribute both the speccing and building across nodes a, b and d. And specs
> still need to be strictly compared against any deviations from the design. I need fully-oriented handoffs,
> coordination and per-node task distribution steps. How do we execute this?

## [research]

Five researchers took one facet each, at the owner's medium effort, read-only, each with its own scratch folder and
no model or network calls. Each return is saved verbatim beside this record as it lands.

| Facet | Dispatch | Handoff | Return |
|---|---|---|---|
| The unattended driver, end to end | 214 | `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-51-researcher.md` | `build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-driver.md` |
| Coordination across nodes a, b and d | 215 | `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-52-researcher.md` | `build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-coordination.md` |
| Fully oriented handoffs | 216 | `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-53-researcher.md` | `build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-handoffs.md` |
| Per-node task distribution | 217 | `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-54-researcher.md` | `build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-schedule.md` |
| Specs held to the design, strictly | 218 | `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-55-researcher.md` | `build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-deviation.md` |

Every probe script the five left in their scratch folders is kept verbatim in
`build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-instruments.md`, so each table can be re-run. That record's
`[verified]` holds the main loop's two checks of claims the returns left open. First, a spec whose design pin is
stale passes today's spec-tokens leg, seen red on a control first, while the bootstrap `carries.py` reds it. Second,
a README the owner landed on main resolves at the default-branch anchor, where a `slug` run reads `spec-audit:` and
`may:`; that was read in the driver, not run.

## [presented]

The main loop's synthesis as shown to the owner before the four questions, 2026-10-20. It is an outline; the plan
record elaborates it.

- **The bad news first.** Nothing in today's merge bar compares a spec with the design: a spec whose design pin is
  stale passes the bar on every node, and only the bootstrap `carries.py`, which nothing runs, catches it. The
  deviation researcher's plants found several departures those instruments miss.
- **What today's gov forces.** A whole chain build is the smallest piece two nodes can split, carried by one
  `/unattended` run in one fresh worktree; units inside a run go one at a time. The owner starts every run with
  `/unattended <slug>` on the node. A build's audit opt-in and `may:` grants count only from a README the owner landed
  on main; no run has used that path yet. Nothing holds a build until its parents land. The current driver carries the
  chain only until dWellOiledMachine lands, which dissolves it; dDeclaredLoop and dPlacedRequest change it mid-chain.
- **Phase 0, dClosedLoop finishes** (node d, records only, then one landing on the owner's ask): harden the three
  deviation instruments, each fix seen red on its plant; build the packet instrument, one generated and byte-checked
  handoff per chain build; commit the schedule instrument; open the chain in one landing, 22 READMEs with stage,
  parents, a roster mapped to clause ids, the owner's audit opt-in and grants, and each packet; prepare the nodes
  (wiring, remote head, the resume tick on each, node b set up for gov).
- **Phase 1, dTrueNorth on node a, the pilot** (6 units): one run specs, audits, builds, reviews and lands it. It
  proves the opt-in from a README landed on main, and it builds the product comparison with the planted tests as its
  acceptance. Nothing else is specced until it lands.
- **Phase 2, the chain rescheduled at every landing.** A build is specced once its parents' specs close and its
  grandparents land, and built once its parents land; its two phases may go to different nodes: 262 units, against
  276 on the critical path and 309 to 322 with one whole build per node. Each node fetches, reads the claims, takes the
  ready unclaimed phase the schedule names, starts its run from a fresh worktree off `origin/main`, pushes after every
  pass and lands in place. Another node's live or held claim means other work, never a run started over it; a stale
  claim is taken over only if its branch is on the remote; a shared file waits for a parent and otherwise reconciles
  at the lander's conflict; a problem in another build is an ask in its `BACKLOG.md`. Eleven landings change what
  running nodes load, and dPlacedRequest is a barrier.
- **Holding specs to the design.** From dTrueNorth's landing every node's bar runs the comparison at pre-push, at
  `--close` and in CI. Every build's spec audit is opted in. The owner reads each build's coverage report when its spec
  phase lands. Approval by risk with no one at the keyboard was proposed: editorial by the run, additive or stricter by
  the spec-writer role with a re-audit, loosening, breaking or an owner ruling parked BLOCKED. The owner's third answer
  replaces that last line.

## [answers]

The four questions as asked, 2026-10-20, each with the options offered, and the owner's answers verbatim.

**1. "How should a build's speccing and building be split across nodes?"**
- "Split phases (Recommended)": each build gets a spec run, then a later build run, possibly on another node: 262
  units. A spec run closes by deferring every unit (a rescope row each, one backlog ask per build), a policy the owner
  ratifies. About 43 runs to start, and the owner sees each build's coverage before its code starts.
- "Whole build per run": one run specs and builds each build: 309 to 322 units, 22 runs to start, no new policy; the
  design exit passes inside the run, with no look from the owner.

The owner: "Split phases (Recommended)".

**2. "What should the 22 READMEs carry when you land the opening?"**
- "Audit + derived grants (Recommended)": `spec-audit:` on all 22, plus a `may:` grant per build naming the paths of
  the nodes it owns, so its governance-carrier forks do not park; the owner sees every grant in the opening diff
  before landing it.
- "Audit, no grants": `spec-audit:` on all 22, no grants; every governance-carrier or public-surface fork parks until
  the owner rules.
- "Audit default line": one `SPEC_AUDIT_DEFAULT` line on main instead of 22 `spec-audit:` lines, and no grants.

The owner: "Audit + derived grants (Recommended)".

**3. "When an unattended run must depart from the design, who approves the departure?"**
- "Park owner-level (Recommended)": editorial by the run; additive or stricter by the spec-writer role with a
  re-audit record; loosening, breaking or needing the owner's ruling parks the unit BLOCKED until the owner rules.
- "Park every deviation": any departure parks for the owner, whatever its risk.
- "Owner-level, pre-approvable": as recommended, plus departures the owner foresees pre-approved by decision ids on a
  build's `may:` line.

The owner: "departures are recorded and explained at the end, nothing is parked or blocked - the build must go
through to completion."

**4. "What should node b do?"**
- "Spec phases only (Recommended)": onboard b to gov; it takes spec phases of builds with slack, never a
  critical-path build, joining around unit 110; without b, a and d finish in 272 units instead of 262.
- "Spec and build": b may also take a build phase when the build's slack covers b's slower pace; no meaningful gain
  measured over spec-only.
- "Leave b out": a and d only, 272 units, no onboarding.

The owner: "Spec and build, but since node b has lower limits, it should be issued a smaller slice, preferably
non-critical."

## [readings]

The main loop's reading of the two answers the owner wrote in their own words. The plan applies these; the owner's
walk of the plan corrects any of them.

- **Answer 3 sets two designed policy keys and changes no clause.** v2's catalogue already offers both values:
  `deviation.gate` takes `refuse`, `warn-and-ask` or `report`, and `deviation.approval` takes `by-risk`, `owner-all`
  or `author-recorded` (`architecture-v2.md` `[policies]`). The `standard` preset sets `refuse` and `by-risk`
  (`[presets]`). The owner's answer is the override `deviation.gate = report` with `deviation.approval =
  author-recorded` for the chain's execution, so no `[chain]` clause changes and no deviation record is owed. Before
  those keys exist as product (dDeclaredLoop owns the approval key, dScopedBuild the gate key), the plan applies the
  same two values to the bootstrap instruments and to every run.
- **"At the end" is read as each build's end.** Each build's landing carries a generated report that explains every
  departure the deviation join computes, whether recorded or not. The as-built view rolls them up across the chain.
  Detection stays strict, because the join computes the population rather than trusting a declaration; only the
  refusal and the wait for the owner go.
- **"Nothing is parked or blocked" reaches past deviations.** A fork the run cannot resolve parks today and turns the
  run's landing into a hand-off to the owner. The plan has to say how every fork is resolved by the run, its
  resolution recorded and explained at the end like a departure, and what in today's driver allows that.
- **Answer 4 makes node b a smaller, slack-first share of both phases.** b takes spec and build phases sized to its
  lower limits, preferring phases with slack over the critical path, once it is onboarded to gov.
- **Answer 1 ratifies the spec-run close.** A spec run closes through the carry-forward route: every unit deferred, a
  rescope row each, one backlog ask per build that every spec advances, and a closing review over the spec commits.
- **Answer 2 puts the grants in the owner's hands at the opening.** Each build's `may:` grant is derived from the
  paths of the nodes it owns, and the owner reads every grant in the opening diff before landing it.

## [plan]

The plan is `build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md`. Its schedule script is
`build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`. Both were written by dispatch 219, whose return is
`build/2026-10-20-build-PLAY-dClosedLoop-1-execution-return-plan.md`. The plan applies none of the readings it found
wrong; it states each as a question in its `[defaults]`.

**Two of `[readings]` were wrong, and the main loop confirmed both.**
- **The grant derivation has no input.** Answer 2's grant is "derived from the paths of the nodes it owns", but a
  build's owned nodes are keys, and a `may:` grant takes only a decision id or a repo-relative path
  (`tools/unattended/lib-unattended.sh`, `parse_grants` and the comment above it).
- **Answer 3 does change a clause.** `cl-dClosedLoop-0004` joins each departure "at the close to a record whose
  approver meets its risk class by the by-risk table", "seen red on … an approver below the risk" (v2 `[chain]`,
  dTrueNorth's row). So setting `deviation.approval = author-recorded` for the chain departs from that clause, and the
  plan carries the departure as a proposed deviation for the owner. The reading "no deviation record is owed" is
  withdrawn.

**One mechanism departs from a written rule, which the plan's D6 needs the owner to know.** The driver admits
`--override build-complete`, since its no-override set is `authorization-reachable` and `pieces-complete` only
(`tools/unattended/unattended.sh`, `DOD_NO_OVERRIDE`). The verbs guide, though, says a unit added during the run
leaves `build-complete` unmet and its build "is a `--handoff` under `owner-decision`, never an override"
(`memory/guides/UNATTENDED-VERBS.md`, rule 9 of the close). D6's recommended option uses the code's admission against
the guide's rule, on an owner ruling. Whether the bar's unattended leg reds that override is unread.

## [answers-2]

The plan's open choices, asked in three sets on 2026-10-20 after the plan landed (`execution-plan.md` `[defaults]`).
Each is given with the options offered and the owner's answer verbatim. One answer came back as a question, and the
main loop's reply is recorded beside it.

**Set 1.**

1. "A build's owned nodes are keys, and a may: grant takes only a decision id or a file path, so grants can't come
   from owned nodes. What should each build's may: grant be?"
   - "One decision row (Recommended)": one decision row, landed with the opening, grants each chain build the
     governance-carrier and public-surface changes its own `[chain]` clauses name; all 22 `may:` lines cite it.
   - "Paths from its clauses": the file paths among each build's own clause text, 49 in all; 9 builds get none.
   - "Paths typed per build": the opening's author types each build's paths, and the owner reviews all 22 lines.

   The owner: "One decision row (Recommended)".
2. "Your deviation answer departs from clause cl-0004, which fixes dTrueNorth's interim deviation check to the
   by-risk table and fails an approver below the risk. Which holds for the chain?"
   - "A deviation, your values (Recommended)": a deviation the owner approves, quoting the answer, so the interim
     check reads `report` and `author-recorded` for the chain.
   - "Build it as written": the check keeps the by-risk table, and a loosening departure fails the bar until the owner
     approves it.

   The owner: "A deviation, your values (Recommended)".
3. "When a spec run's audit or review confirms a finding, the finding becomes a new unit, and the carry-forward close
   refuses new units. How does such a run end?"
   - "Override, your ruling (Recommended)": a standing ruling lets it close with `--override build-complete`.
   - "Hand off to you": the run hands off for the owner's decision.
   - "Spec run builds them": the spec run builds its added units itself.

   The owner: "Why does carry-forward close refuses new units? It should not refuse any new units that come from the
   reviews (either spec or closing diff), that sounds like a bug."

   The main loop's reply, as given:
   - It is not a bug in the code. It is the deliberate edge of M4's severity rule, ruled for diffs on 2026-10-04 and
     for specs on 2026-10-05: every confirmed review finding is promoted to a unit and built, and none is parked or
     waived.
   - The carry-forward term's second condition enforces the rule by refusing to defer a unit the run itself added. Its
     comment cites M4 (`tools/unattended/unattended.sh`, `check_carry_forward`;
     `memory/guides/BUILD-METHOD.md` M4).
   - That rule assumed one run that specs and builds. The split lands the spec run before anything is built, so its
     promoted units hit a rule written for a run that could have built them.
   - Carrying them to the same build's build run keeps M4's intent, as long as the build run must build them and
     cannot defer them again.
   - The fix is one condition: a spec run may carry a review-promoted unit forward to its own build run, once. That is
     product code in the unattended kit, so it needs a home. Question 5 asks where.
4. "At Pro pace the schedule gives node b six spec runs and no build run, though you asked for spec and build. What
   should b get?"
   - "Measure, then assign (Recommended)": the pilot measures b's pace, and b gets whatever build runs its slack
     allows.
   - "Reserve one build now": pin dRankedPlan's build run (slack 33) to b now.
   - "Spec runs only": b takes spec runs only.

   The owner: "Spec runs only".

**Set 2.**

5. "The fix is one condition in the unattended kit: a spec run may carry a review-promoted unit forward to its own
   build run, once. Where does that product code go?"
   - "dTrueNorth's extra unit (Recommended)": dTrueNorth runs as one whole run, spec and build together, and adds the
     fix as one unit, a departure from v2 the owner approves.
   - "dClosedLoop fixes it first": Phase 0 takes one product-code unit, lifting dClosedLoop's no-product-code line
     for it.
   - "Override until fixed": spec runs close with `--override build-complete` under a standing ruling until a chain
     build fixes the condition.

   The owner: "dTrueNorth's extra unit (Recommended)".
6. "Three kinds of fork still park under today's driver: one whose options all widen a security, data or write
   surface, one with no surviving option, and one the build's goal can't survive. Until dOrderedCharter's decision
   principles land, what happens to such a unit?"
   - "Carry it forward (Recommended)": the build lands without that unit, the owner rules, and a later run builds it.
   - "Standing ruling": the run takes the most capable option that fails only the security veto or the goal bound,
     recorded as a departure; nothing waits on the owner, but a security surface may widen unreviewed.

   The owner: "Standing ruling".
7. "dDeclaredLoop, dPlacedRequest and dWellOiledMachine rewrite the driver they run under. How do their build runs
   finish?"
   - "Land through new code (Recommended)": driver-touching units go last, and the build lands through its own new
     code; the owner lands it only if that code refuses.
   - "Always hand off": these three always end with a hand-off for the owner to land.
   - "Run them attended": their build runs are attended sessions.

   The owner: "Land through new code (Recommended)".
8. "The report setting lets a departure land even when the run never wrote a record for it, but you said departures
   are recorded. Which applies?"
   - "Report, as read (Recommended)": the comparison lists every departure it finds, a step before the close gives
     each a record, and the end report shows any left unrecorded.
   - "Refuse until recorded": the close refuses until every departure has a record, which only the run need write.

   The owner: "Report, as read (Recommended)".

**Set 3.**

9. "dPlacedRequest moves run claims onto leases while other nodes have runs live. How is that made safe?"
   - "Test in its spec (Recommended)": its spec carries a test that a live claim on another node survives the
     migration, with a drain as the fallback.
   - "Drain first": no other chain run may be live or held when its build run reaches the migrating unit.

   The owner: "Test in its spec (Recommended)".
10. "Today only your /unattended <slug> starts a run, and the plan needs 44 starts at 38 moments. Who starts each run?"
    - "You type it (Recommended)": the owner types `/unattended <slug>` on the node the schedule names.
    - "Node session, standing ruling": each node's attended session starts the run, under a standing ruling.
    - "Scheduled task": a scheduled task on each node starts the next run; nothing like it exists today.

    The owner: "You type it (Recommended)".

**Not asked, carried as the plan recommends, for the owner's walk:**
- R6: `design.coverage` stays `refuse`, since the run always clears a coverage red itself.
- D3: dTrueNorth's product comparison absorbs the instruments' planted cases as its acceptance.
- D5: after the chain, the two deviation keys return to `standard`'s `refuse` and `by-risk`.
- D8: the opening mints every roster id and carry-forward ask, which the carry-forward rules force.

**What the answers change in the plan.**
- The grants become one decision row that every chain README's `may:` cites.
- The departure from `cl-dClosedLoop-0004` is a deviation the owner approves, quoting answer 3 of `[answers]`.
- dTrueNorth runs as one whole run and carries one more unit: the carry-forward condition for review-promoted units,
  a departure from v2 the owner approved. Every later spec run closes with it.
- Node b takes spec runs only.
- Residual forks follow the standing ruling, each choice recorded as a departure. A choice that widens a security,
  data or write surface is listed first in its build's departures report.
- D1, D2, D4 and R3 stand as recommended.
