# Research: per-node task distribution, for the chain's execution

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 217's return, verbatim, except that a title line would be demoted to keep one H1 per record.
Its question is in `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-54-researcher.md`.

---

## Per-node distribution for the dClosedLoop chain: research return (PLAY-dClosedLoop-1, question 54)

**Answer.** Use just-in-time spec phases: a build is specced once its grandparents have landed and its parents' specs have closed, and built once its parents have landed. Split the spec and build phases across nodes, and re-run the schedule at every landing rather than following a fixed table. This finishes the chain in **262 units** against 509 run serially on one node. That beats building whole builds node by node (322) and matches the shortest schedule found (262), while leaving specs exposed to about a third as much tool churn. Node b adds little at Pro-plan speed (272 units with a and d only), so it takes spec phases of builds with spare time, never a critical-path build.

All work was read-only; probes ran only in the scratch folder. `git status` was the same before and after; the staged entries in it belong to the parent session.

### Facts the answer rests on

- **The chain.** It has 22 builds and 509 clauses (`architecture-v2.md:1764-1785`). Splitting each build's units cell on "; " gives the same count as its `cl-` ids for every build; the script asserts this. The baseline is `59ff8f2ac` (`architecture-v2.md:1809`).
- **Critical path: 276 units**, the same as `critical-path.py`'s output.
  - The script prints only one path, through dBoundRoles. dTotalRecall is equally critical (both finish at 157, slack 0), and the printed path hides it.
- **dTrueNorth must land before any other chain spec.** The coverage and deviation gates "must stand before the first chain spec" (`final-questions.md:276-278`), and the sequence is "the bootstrap build first" (`final-questions.md:302`).
  - The bootstrap instruments check chain specs until then (`carries.py:3-5`).
- **v2's own dependency model already allows designing ahead.** `deps.early-build` takes `confirmed-interfaces`, `design-only` or `anything-coordinated` (`architecture-v2.md:1166`), and `deps.landing` defaults to `hold-until-parent-lands` (`architecture-v2.md:1232`). Dependents wait on a parent's interfaces confirmed at its Design exit (`coordination.md:130-137`). Today's gov has none of this mailbox; dKeptSession builds it.
- **A spec revised before its unit's first `Pass:` commit is not a deviation.** The population counts only revisions after that commit (`deviations.py:23`, `:150-158`).
  - Probe: `deviations.py --fixture` gave 0 findings, and its pre-pass rev-2 row is not a member. `--plant pass-revision` gave 1 finding.
- **A spec-only run cannot close normally today.** `build-complete` refuses a roster with unfinished units (`UNATTENDED-PROTOCOL.md:351`), unless every one meets the five carry-forward conditions (`UNATTENDED-STOPS.md:698-712`):
  - the spec's status is `DEFERRED`;
  - the run's starting roster carries the unit;
  - there is a `rescope · item defer` row for it;
  - its spec closes or advances an ask in this build's own backlog, and `ASKS_CMD` is set (`.unattended.conf:216`);
  - no closed unit's spec declares a `consumes-from` edge onto it.
  - `closing-review-recorded` also needs a diff-review record in the run's range (`UNATTENDED-PROTOCOL.md:352`).
- **One driver per build slug.** `RUN_CLAIMS="on"` (`.unattended.conf:162`) makes `refs/gov/runs/<slug>` refuse a second driver of the same build (`unattended.sh:2070-2087`). A finished claim is taken over by the slug's next run (`UNATTENDED-STOPS.md:186-196`), so spec on one node and build on another is allowed one after the other.
  - Concurrent runs of different builds are permitted (`UNATTENDED-PROTOCOL.md:333`).
- **Every node may land.** `LANDING_NODES` is absent from `.unattended.conf`, which means every node may land (`UNATTENDED-PROTOCOL.md:528`).
  - `LANDER_MODE="in-place"` (`.unattended.conf:23`) grades the merge onto the advertised tip under `GATE_FULL=1` (`UNATTENDED-PROTOCOL.md:430-432`). So a build still in progress meets every gate that landed before it, at its own landing.
- **Records-only landings are cheap.** Self-test legs in `tools/gate-legs.json` (for example `:291`, `:381`) are guarded by paths, so a records-only spec landing skips most of them.
- **Parent links are recorded but not enforced.** `parents:` exists in build front matter today. It is rendered (`gen_build_index.py:1570-1587`) and refused only when it names a folder that does not exist (`:2341-2344`). Nothing holds a build until its parents land.
  - **Record vs code:** gap-plan-01 says "No … dependency record across builds" (`gap-register.md:341`). The record does exist; it is only not enforced.
- **Nodes.**
  - a, b, c and d are all registered (`AGENTS.md:102-108`).
  - The owner's own description of the fleet: d has 16 cores / 32 GB and one Max plan serving five projects; a has 16c/32GB and one Max plan serving three projects; b has 4c/8GB and a Pro plan and works "for inCMS, NicoCares only" (`cloud-and-scale.md:434-436`). So b is registered for gov but does not currently serve it.
- **Two premises that don't match the records.**
  - "One stream per node" is not in the build method. The rule is one stream per work-unit (`AGENTS.md:29`, `:172`). The only node-level exclusivity is the per-slug claim.
  - The driver's verbs live in `tools/unattended/unattended.sh`; `lib-unattended.sh` is its library.
- **Nothing finds or offers work to a node.** Nodes cannot find work they do not hold (gap-conc-16, `gap-register.md:337`), and no one can offer them work (gap-conc-19, `:340`). So distribution today is assignment.

### The model, and what I had to assume

Each build is split into a spec phase of `s·U` and a build phase of `(1−s)·U`, where U is its clause count, measured in units of the fastest node's work.

- **Spec share `s`.** Assumed 0.33 and swept over 0.2 to 0.5. History cannot measure it: `Pass:` trailers do not separate spec passes from build passes.
- **Node speeds.** a = d = 1, b = 0.25, with 0.5 also tried. d at 0.75 and 0.6 was also tried, because d serves more projects.
- **Units are not a calendar.** No unit wall time is recorded (gap-rt-26).
- **One phase at a time per node.** Phases are placed by list scheduling: the most-downstream-work task first, on the node that would finish it soonest.

### Candidates, each with the test it could lose

Results below are at s = 0.33 and b = 0.25 unless stated.

| Candidate | How it works | Test that could make it lose | Result |
|---|---|---|---|
| **A. Whole build per node** | Spec and build back to back, after the parents land | Makespan more than 5% over the best schedule found | **Loses.** 309–322 against 262–275 across every s and b; node b is idle (0%) |
| **B. Spec ahead at the baseline** | Spec any build once dTrueNorth lands | Staleness no worse than other schedules at the same makespan | **Loses.** Makespan 267, staleness 163 (worst build 15) |
| **C. Spec after parents' specs close** | v2's `design-only` model | Same staleness test | **Loses.** Makespan 262 with staleness 61 (worst 6); J does the same makespan at 19 |
| **J. Just-in-time spec** | Spec after dTrueNorth lands, the parents' specs close and the grandparents land; build after the parents land | (1) Makespan more than 5% over C; (2) a spec revised when a parent lands becomes a deviation; (3) a spec-only run cannot close | (1) **Passes:** 262–275, against C's 259–275 at b = 0.25. (2) **Passes:** the fixture above. (3) **Partial:** it works today only through the carry-forward route (see below) |
| **Split spec and build across nodes** | The build may run on another node than its spec | Splitting saves less than 5% over keeping both on one node | **Wins.** 262 against 287 for one node per build |
| **D. Split one build's units across nodes** | Two nodes drive one slug | A second driver's `--preflight` is refused | **Rejected by reading the code, not run** (running it needs a remote write): `UNATTENDED-STOPS.md:186-196`, `.unattended.conf:162` |
| **Static table vs re-dispatch at each landing** | Follow the table as fixed, or re-run the scheduler as phases finish | Durations vary ±60%; 300 draws | **The static table loses.** Median 306 / p90 326, against 290 / 309 re-dispatching (re-dispatch was given the actual durations, so this is its best case) |
| **Node b's role** | b may build, or b specs only | b-full beats spec-only by more than 5% | **No meaningful difference.** 263 against 268. b adds about 9 units at Pro speed (272 with a and d only), or about 33 if b runs at half speed. With d at 0.6, J still beats A: 319 against 365 |

Staleness counts how many other builds land between a build's spec closing and its build starting, among builds whose clauses change a surface the nodes themselves run on. The regex for that (in `stale.py`) catches 21 of the 22 builds, so treat it as a relative measure only.

### Recommendation: the schedule, derived by `planj.py` (J, s = 0.33, b = 0.25)

| Build | Stage | Parents | Units | Earliest start–finish | Slack | Spec: node, span | Build: node, span |
|---|---|---|---|---|---|---|---|
| dTrueNorth | Fidelity | dClosedLoop | 6 | 0–6 | 0 | a 0–2 | a 2–6 |
| dGroundRules | Policy | TrueNorth | 11 | 6–17 | 0 | a 6–10 | a 10–17 |
| dSafePassage | Supersession | GroundRules | 13 | 17–30 | 0 | d 10–14 | d 17–26 |
| dOrderedCharter | Foundation | SafePassage | 37 | 30–67 | 0 | a 17–29 | a 29–54 |
| dFairHearing | Review harness | SafePassage | 18 | 30–48 | 19 | d 26–32 | d 32–44 |
| dDeclaredLoop | Spine | OrderedCharter, FairHearing | 34 | 67–101 | 0 | d 44–55 | a 55–78 |
| dWitnessedBar | Test | DeclaredLoop | 30 | 101–131 | 0 | d 55–65 | a 78–98 |
| dPlacedRequest | Entry | DeclaredLoop | 21 | 101–122 | 7 | d 65–72 | d 78–92 |
| dKeptSession | Session | DeclaredLoop, PlacedRequest | 28 | 122–150 | 7 | d 92–101 | a 106–125 |
| dTotalRecall | Memory | DeclaredLoop, WitnessedBar, PlacedRequest | 26 | 131–157 | 0 | a 98–106 | d 110–127 |
| dBoundRoles | Roles | DeclaredLoop, WitnessedBar, PlacedRequest | 26 | 131–157 | 0 | d 101–110 | a 133–151 |
| dLinkedLibrary | Library | TotalRecall | 25 | 157–182 | 20 | a 125–133 | d 147–164 |
| dWellOiledMachine | Runtime | BoundRoles, TotalRecall, KeptSession | 61 | 157–218 | 0 | d 127–147 | a 156–197 |
| dFurnishedOrders | Orders | BoundRoles | 20 | 157–177 | 41 | **b** 110–136 | d 164–177 |
| dRankedPlan | Plan | DeclaredLoop, TotalRecall, BoundRoles | 16 | 157–173 | 45 | **b** 136–157 | d 177–188 |
| dIndexedDesign | Design | DeclaredLoop, TotalRecall, KeptSession, BoundRoles, LinkedLibrary | 16 | 182–198 | 20 | a 151–156 | d 188–199 |
| dShippedRelease | Deploy | WitnessedBar, TotalRecall, BoundRoles, WellOiledMachine, LinkedLibrary, FurnishedOrders | 31 | 218–249 | 4 | **b** 157–198 | d 199–220 |
| dTendedCadence | Maintain | WitnessedBar, RankedPlan, WellOiledMachine, IndexedDesign, FurnishedOrders | 18 | 218–236 | 0 | a 197–203 | a 213–226 |
| dScopedBuild | Build | IndexedDesign, WitnessedBar, WellOiledMachine, FurnishedOrders | 15 | 218–233 | 20 | a 209–213 | a 226–236 |
| dMindYourWords | Lexicon | WellOiledMachine, WitnessedBar, LinkedLibrary, FurnishedOrders | 17 | 218–235 | 18 | a 203–209 | d 225–237 |
| dCalibratedLens | Review | TendedCadence, FairHearing | 17 | 236–253 | 0 | d 220–225 | a 236–247 |
| dConvergedCharter | Convergence | ScopedBuild, ShippedRelease, CalibratedLens, MindYourWords | 23 | 253–276 | 0 | d 237–244 | a 247–262 |

Earliest start–finish and slack assume unlimited nodes and whole builds. The two node columns are J's schedule on a, b and d.

- **Load:** a is busy 100%, d 86%, b 34%. The makespan is 262.
- **The dispatch rule.** The table is the plan at the assumed speeds; the rule below is what to follow, because re-dispatching beats a fixed table (see the noise row above). At each landing:
  - re-run the script;
  - the free node takes the ready phase with the most downstream work;
  - b takes only spec phases, or a build only when its slack covers b's slowdown;
  - no build phase starts until every parent's claim reads `landed`.

**First wave.**
- **Node a:** dTrueNorth, spec then build. It is the only chain work that can start (`final-questions.md:276-278`).
- **Node d:** opens all 22 chain folders, READMEs and rosters in one commit. `parents:` must name folders that already exist (`gen_build_index.py:2341-2344`). Then d takes dSafePassage's spec once dGroundRules' spec closes.
- **Node b:** gets onboarded to gov, because it currently serves only inCMS and NicoCares (`cloud-and-scale.md:434-436`; onboarding steps at `AGENTS.md:114`). It joins at about 110.
- Speccing dGroundRules alongside dTrueNorth would save at most 4 units, judging from the table's own rows, and would break the bootstrap rule. Not recommended.

**Sync points.** A landed change reaches every build still in progress through the in-place merge bar at that build's own landing, so no step is needed for gates. These landings change what running nodes load at session start, so they need action:

| Lands at | Build | What changes for the nodes | In progress then (J) | What the in-progress build does |
|---|---|---|---|---|
| 6 | dTrueNorth | Spec format: `**Carries:**` lines, the carries join, the coverage report, the deviation join, `@rev-N` pins (cl-0001–0005) | nothing | Every later spec is written to the new format |
| 26 | dSafePassage | Upgrade steps that retire `.agent-cap.conf` and `template-size-limits.txt`, and hooks (cl-0018 onward) | spec dOrderedCharter on a | Each node runs the steps on its own machine; the session is rotated at its next pass boundary |
| 54 | dOrderedCharter | The charter re-founded; AGENTS.md re-rendered (cl-0032) | spec dDeclaredLoop on d | Rotate the session; a fresh kickoff loads the new charter (M7 does not re-read the charter) |
| 78 | dDeclaredLoop | The roles kit's stage table moves; its seven readers are re-pointed (cl-0086) | nothing | — |
| 92 | dPlacedRequest | Run claims migrated onto leases (cl-0120) | build dWitnessedBar on a | **A barrier.** The migration must carry a live foreign claim; that test is owed in its spec. Otherwise drain all runs first |
| 98 | dWitnessedBar | The pre-push hook reads a runner-written verdict (cl-0342) | spec dKeptSession on d | Nothing for a spec; its next landing produces a verdict |
| 151 | dBoundRoles | Role definitions are rewritten | build dLinkedLibrary on d, spec dRankedPlan on b | Rotate at the pass boundary |
| 177 | dFurnishedOrders | The per-pass checklist is retired from the build method and the `/unattended` skill (cl-0195) | build dWellOiledMachine on a | Picked up automatically: M7 re-reads BUILD-METHOD at every pass boundary |
| 197 | dWellOiledMachine | The `next` verb, re-pointed `--plan`/`--status`, hooks (cl-0280, 0281) | build dIndexedDesign on d, spec dShippedRelease on b | Rotate; check the driver verbs |
| 199 | dIndexedDesign | Design-to-Build hand-off; the coverage join moves into the product (cl-0383) | spec dTendedCadence on a | Its spec phase finishes through the new Design exit |
| 220 / 236 | dShippedRelease / dScopedBuild | Landing record and lander (cl-0413); built specs frozen (cl-0400) | build dTendedCadence on a; build dMindYourWords on d | Land through the new lander; no edits to a landed unit's spec |

At every landing, any spec written ahead whose parent just landed is re-grounded: its §10 reuse probe is re-run against the landed parent, and it is revised before its first `Pass:` commit. That revision costs no deviation record.

### What today's gov cannot do for this plan, and the smallest change

1. **Closing a spec-only `/unattended` run.**
   - Today the only route is carry-forward: every unit set to `DEFERRED`, a `--rescope --act defer` row per unit, one backlog ask that every spec `advances`, and a diff-review record over the spec commits.
   - **Policy (smallest):** record that route as the spec-run close. The other options are a **manual step** (spec phases run with the owner present and land through `push-main.sh`), or giving up the phase split (287 instead of 262).
   - dIndexedDesign's Design-exit hand-off (cl-0383) lands too late (around 199) to help.
2. **Nothing holds a build until its parents land** (`parents:` is only rendered). **Manual step:** before `--preflight` of a build phase, read every parent's claim as `landed` via `--claims`. The product fix is dRankedPlan (cl-0369) plus dPlacedRequest's leases.
3. **No node finds or is offered work** (gap-conc-16, gap-conc-19). **Manual step:** an assigner (the owner, or node a) re-runs `planj.py` at each landing and records the next assignments.
4. **Running sessions do not reload the charter, roles or hooks, and machine installs are per node.** **Manual step:** rotate sessions and run upgrade steps on each node at the sync points marked above.
5. **dPlacedRequest's claim-to-lease migration while other nodes have runs live.** **A chain build's unit:** its spec must carry the test "a live claim on another node survives the migration". Failing that, a **manual** drain barrier.

### Scripts

All in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/exec/d217/`:
- `schedule.py`: parses v2 `[chain]`, asserts 22 builds / 509 units, prints the earliest start, finish and slack table.
- `heft.py`: the scheduler.
- `stale.py`: policy J and the staleness measure.
- `planj.py`: the table above. Run as `python3 planj.py <dir> <worktree> 0.33 0.25 any full J`.
- `noise.py`: B's staleness and the static-vs-re-dispatch draws.
- `surfaces.py`: maps each build's clauses to the surfaces the nodes run on.
- `compare.py`: the first, earliest-start sweep.
