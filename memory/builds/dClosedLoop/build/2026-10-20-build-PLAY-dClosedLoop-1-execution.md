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
