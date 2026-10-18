# Walk: the converged design, build by build

**Serves:** research PLAY-dClosedLoop-1

Step 4 of the owner's convergence order ran end to end: the declared whole-design audit, its fold, the fold's
closing review, and that review's fold. Asked what next, the owner chose to walk the converged design build by
build, before a follow-up review or the build's exit. This record holds the walk as presented, wave by wave, and
the owner's word on each.

## [words] The owner's choice, 2026-10-18

- Asked "Step 4 has run: audit, fold, the fold's review, and its fold. What next?", the owner chose, verbatim: "Walk the design first", whose text read: "I lay out the converged v2 and the chain for you to walk, build by build, before either."

- Asked to resume after the night pass, the owner's answers and the spine's split, the owner said, verbatim:
  "re-derive the walk and present wave 1" (2026-10-18). The glance and wave 1 are derived again in `[chain-2]` and
  `[wave-1-2]`.
- The owner's word on wave 1, 2026-10-18, verbatim: "approve wave 1, present wave 2".
- The owner's word on wave 2 and its forks, 2026-10-18, verbatim: "approve wave 2, take the recommendations".
- The owner's request for wave 3, 2026-10-18, verbatim: "present wave 3".

## [chain] The chain at a glance

As presented, at `beda01950`. The night pass has since grown the chain to 330 units.
At `15cec9200` the critical path is 211 units (the night-pass record's `[chain-impact]`). This glance and wave 1 are
derived again when the walk resumes.

- **Sixteen builds,** ordered by when each can finish, in planned units, a unit being one clause of a row's
  planned units: dGroundRules 8; dFairHearing 19; dOrderedCharter 30; dDeclaredLoop 73; dWitnessedBar 93; dBoundRoles
  123; dTotalRecall 125; dIndexedDesign 134; dRankedPlan 136; dWellOiledMachine 149; dScopedBuild 158; dTendedCadence
  159; dMindYourWords 165; dCalibratedLens 167; dShippedRelease 169; dConvergedCharter 181.
- **The critical path, 181 units at `beda01950`:** dGroundRules, dOrderedCharter, dDeclaredLoop, dWitnessedBar,
  dTotalRecall, dWellOiledMachine, dShippedRelease and dConvergedCharter.
- **The waves:**
  1. the foundation: dGroundRules, dOrderedCharter, dFairHearing and dDeclaredLoop;
  2. dWitnessedBar, dBoundRoles, dTotalRecall, dIndexedDesign and dRankedPlan;
  3. dWellOiledMachine, dScopedBuild, dTendedCadence and dMindYourWords;
  4. dCalibratedLens, dShippedRelease and dConvergedCharter.

## [wave-1] The foundation, as presented

### dGroundRules: Policy

First of all, 8 units, finishing at 8 of 181. It owns `policy.on-invalid` and closes gap-spine-06 (HIGH, the
policy sprawl).
- **The policy file:** `.governance/policy.toml`, its schema, its one reader and its JSON mirror, moved here so both
  roots read policy from a build ahead of them (RC-1).
- **How a key resolves:** an override in the file, then the named preset once dDeclaredLoop adds presets, then the
  catalogue default. An absent file reads defaults. A malformed file or an out-of-set value reads the last valid
  landed revision, or refuses (AF-2). The reader and every mirror consumer read the landed revision, never the
  working tree (FM1).
- **A minimal guard:** owner-only writes to the policy file, its mirror and the instruction manifest, until
  dDeclaredLoop's full guard lands.
- **The legacy policy homes** (kit confs, `gate-env.sh`, the roles' house policy) on a shrink-only list derived from
  the files, and an arm red when a landed build's key has no reader.
- **To look at:** it is pure plumbing. Its value shows when dOrderedCharter reads its first key.

### dOrderedCharter: Foundation, the instruction layer

After dGroundRules, 22 units, finishing at 30. It owns 12 keys, the `exception` and `override` kinds, the tags and
instruction-writing systems and 9 tag namespaces, and closes 21 gaps, 12 of them HIGH.
- **The charter re-founded as the loop's front door:** its level-0 envelope (the precedence and override rule, the
  instruction map, one line per practice, the hand-off to the loop, the project block) and the drive section from
  kit descriptors. It is held inside 32 KiB against today's size rows (DA-L6), and re-injected on compact and
  resume.
- **The instruction system:**
  - the instruction-unit registry, schema and grammar;
  - one renderer, absorbing the playbook, roles and agent-instructions wiring;
  - the ladder renumbered, levels 0 to 7, and load sets budgeted per reader and harness;
  - the guarded instruction manifest;
  - memory instructing nothing;
  - practices rendered per step into work orders.
- **The core that cannot be built around (P16):** the principle registry and meta-check, the kinds register, the
  conformance-gate contract, the exception register and `core.*` policies, and the factories and gates for units,
  practices, Skills and layers.
- **The tag system:** namespaced tags, seven namespaces of its own, with the grammar, the derived tag index and one
  resolver.
- **Layers and P28:**
  - the layer register and contract;
  - the check that the core never depends on an expansion or optional part, over every edge kind, each seen red
    (DA-H3, DA-M7);
  - today's edges each made an optional slot or moved into the core;
  - the moved grammar's and `map_lib`'s consumers re-pointed (DA-H4, DA-M9).
- **The build's card** delivered at level 1, through a per-worktree file the charter imports.
- **To look at:** 12 of its 21 gaps are HIGH, because the instruction layer is where gov's sprawl lives. It sits on
  the critical path right after policy.

### dFairHearing: the review harness

After dGroundRules and beside dOrderedCharter, 11 units, finishing at 19. It owns the harness's four items
(`review.pin`, `review.lens`, `review.refute`, `review.report`), `review.opt-in`, `review.unclassed` and `review.twin`,
and the `review` kind, and closes 9 gaps.
- **The owed replays first,** the design-audit preset run blind on a frozen history. Then the preset itself, five
  lenses for design and architecture records: coherence, grounding, reuse to precedent, the failure envelope to
  trust boundaries, and alternatives and cost.
- **Opt-in lenses** (security, alternatives, cost, portability, adopter migration, topology), each swapped in for a
  named default lens.
- **The panel:**
  - skeptic batches sorted by address;
  - duplicates counted as merged confirmations;
  - grades per id;
  - refuted claims and twins flagged to the synthesizer;
  - fix verdicts by class;
  - every confirmed finding given one disposition: `class:`, `new:`, `gate:` or `none`.
- **The review records** realigned with the code, and the twin merge when the owner opts in (RS-1).
- **To look at:** AF-1 has dDeclaredLoop call this harness at every review breakpoint, so the harness must land
  first. It does: it finishes at 19, before dOrderedCharter's 30.
- **Fixed during this walk:** its unit count. A parenthesis listed the preset's lenses with semicolons, so the count
  split one clause into five: 15 read, 11 meant. `paren_semis.py` now scans every row for a split inside a clause,
  and was seen red on this one.

### dDeclaredLoop: Spine, the loop

After dOrderedCharter and dFairHearing, 43 units, finishing at 73. Five builds wait on it: dWitnessedBar,
dBoundRoles, dTotalRecall, dRankedPlan and dIndexedDesign. It owns 17 items, 43 keys, 7 kinds and 4 tag namespaces,
and closes 19 gaps, 12 of them HIGH.
- **The loop:**
  - the loop kit, keyed by stage tags, with each step a program of declared items;
  - one transition table per level (build, feature, unit), and an engine that refuses any transition it lacks;
  - terminal states and a default failure route;
  - witnesses computed, never typed;
  - stage claims and the coverage gate;
  - the `step`, `item`, `policy` and `command` namespaces.
- **Policy machinery:**
  - the named presets and their completeness check;
  - the preset step in dGroundRules's reader, and the charter's preset section;
  - the guard, the TTY CLI and the default floor;
  - the factories and conformance gates for commands, keys, presets, stages, hooks, roles and workflows.
- **Coordination:**
  - one lease grammar with epochs and take-over;
  - the mailbox per build, read at every item boundary;
  - dependency coordination through the parent's lease;
  - offline behaviour as `leases.offline` defines it (FL1).
- **Position and orientation:**
  - the position engine: step, next item and interrupts, all derived from witnesses;
  - the build's card at level 1, a ref on the remote, cached, snapshotted and re-keyed on resume;
  - the card's pointers;
  - what a session does as its window fills;
  - compaction summaries read as leads, never as sources.
- **Entry (PM-9, RC-8):** the entry step's items, the placement predicate and its check, and claims keyed and
  trusted.
- **Review control flow (AF-1):**
  - breakpoints at any item boundary, with reviews and owner gates as one mechanism;
  - the owner gate, held for the owner's disposition;
  - the breakpoint program's trigger, disposal, fold and cost;
  - the follow-up and design-audit rounds, with `REVIEW_ROUNDS` retired;
  - the stage-exit recommendation for every step.
- **Three small units:** `actions.free`, backward transitions recorded, and progress reported through
  `notify.owner`.
- **To look at:** this is the build to scrutinise.
  - It is 43 of the 181 critical-path units, the largest by far, and five builds wait for all of it.
  - AF-1 has just added the review control flow.
  - A split is worth pricing, such as coordination or review control flow as a build of its own beside
    dWitnessedBar. It shortens the path only if the children do not need those parts.

## [chain-2] The chain at a glance, derived again

Derived at `b3866c4ad`, after the night pass, the owner's answers and the spine's three-way split
(`build/2026-10-18-build-PLAY-dClosedLoop-1-np24-pricing.md`). The facts are the runs `[walk-instrument-2]` holds.

- **Eighteen builds,** ordered by when each can finish, in planned units: dGroundRules 8; dFairHearing 20;
  dOrderedCharter 35; dDeclaredLoop 57; dPlacedRequest 64; dWitnessedBar 79; dKeptSession 82; dBoundRoles 113;
  dTotalRecall 119; dIndexedDesign 131; dRankedPlan 132; dWellOiledMachine 150; dScopedBuild 161; dTendedCadence 164;
  dMindYourWords 167; dShippedRelease 171; dCalibratedLens 175; dConvergedCharter 189.
- **The critical path, 189 units at `b3866c4ad`:** dGroundRules, dOrderedCharter, dDeclaredLoop, dWitnessedBar,
  dTotalRecall, dWellOiledMachine, dTendedCadence, dCalibratedLens and dConvergedCharter. Its tail now runs through
  Maintain and Review, not dShippedRelease, since the night pass and the owner's answers grew both.
- **Since the first glance:** the chain grew from 285 units to 334, with the night pass and the owner's answers. Its
  critical path went from 181 at `beda01950` to 214 at `1d32760f3`, and then fell to 189 at `b3866c4ad` with the
  split.
- **The waves,** grouped as first presented, the two new builds joining wave 1, where their units were:
  1. the foundation and the spine: dGroundRules, dOrderedCharter, dFairHearing, dDeclaredLoop, dPlacedRequest and
     dKeptSession;
  2. dWitnessedBar, dBoundRoles, dTotalRecall, dIndexedDesign and dRankedPlan;
  3. dWellOiledMachine, dScopedBuild, dTendedCadence and dMindYourWords;
  4. dCalibratedLens, dShippedRelease and dConvergedCharter.

## [wave-1-2] The foundation and the spine, presented again

### dGroundRules: Policy

First of all, 8 units, finishing at 8 of 189. It owns `policy.on-invalid` and closes gap-spine-06 (HIGH, the
policy sprawl).
- **The policy file:** `.governance/policy.toml`, its schema, its one reader and its JSON mirror, here so that both
  roots read policy from a build ahead of them (RC-1).
- **How a key resolves:** an override in the file, then the named preset once dKeptSession adds presets, then the
  catalogue default. An absent file reads defaults. A malformed file or an out-of-set value reads the last valid
  landed revision, or refuses (AF-2). Every consumer reads the landed revision, never the working tree (FM1).
- **A minimal guard:** owner-only writes to the policy file, its mirror and the instruction manifest, until
  dDeclaredLoop's full guard lands.
- **The legacy homes:** kit confs, `gate-env.sh` and the roles' house policy, on a shrink-only list derived from the
  files, and an arm red when a landed build's key has no reader.
- **Since first presented:** one word. Presets now come from dKeptSession, so until it lands at 82 a key resolves
  from the file straight to the catalogue default.
- **To look at:** it is still pure plumbing.

### dOrderedCharter: Foundation, the instruction layer

After dGroundRules, 27 units, finishing at 35. It owns 14 keys, the `exception` and `override` kinds, the tags and
instruction-writing systems and 9 tag namespaces, and closes 24 gaps, 12 of them HIGH.
- **The charter as the loop's front door:** its level-0 envelope (precedence and override, the instruction map, one
  line per practice, the hand-off to the loop, the project block) and the drive section from kit descriptors. It is
  held inside 32 KiB and re-injected on compact and resume.
- **The instruction system:**
  - the unit registry, schema and grammar;
  - one renderer, absorbing the playbook, roles and agent-instructions wiring;
  - the ladder renumbered 0 to 7, and load sets budgeted per reader and harness;
  - the guarded instruction manifest;
  - memory instructing nothing;
  - practices rendered per step into work orders.
- **The core that cannot be built around (P16):** the principle registry and meta-check, the kinds register, the
  conformance-gate contract, the exception register and `core.*` policies, and the factories for units, practices,
  Skills and layers.
- **The tag system and the relational syntax (P33):**
  - namespaced tags, a derived index and one resolver;
  - the closed edge registry, twelve types declared and `cites` derived;
  - `gov tag bundle`, a manifest of ranges or, by flag, the content inlined (NP-14);
  - new text citing `path#symbol` or a blob-pinned line, not file:line (NP-17).
- **Layers and P28:** the layer register and contract, and the check that the core never depends on an expansion or
  an optional part, over every edge kind. Today's edges are each made a declared slot or moved into the core.
- **The build's card** delivered at level 1, through a per-worktree file the charter imports.
- **Since first presented:** five units, all from the night pass.
  - The drive section says a build runs unattended by default from its request, and the `[land]` rule reads
    through the request's mandate (point 1).
  - The edge registry, `gov tag bundle` and the citation rule (point 4).
  - Each role's load set budgets the `code` slot (point 3).

  Three gaps came with them, gap-found-24 to gap-found-26.
- **To look at:**
  - It sits right after policy on the critical path. Half its gaps are HIGH, since the instruction layer is where
    gov's sprawl lives.
  - Its units are uneven. The core-independence check (clause 16) and the tag system (clause 19) each read like
    several units of work, so its count understates it. Spec time is the place to cut them.

### dFairHearing: the review harness

After dGroundRules and beside dOrderedCharter, 12 units, finishing at 20. It owns the harness's four items
(`review.pin`, `review.lens`, `review.refute`, `review.report`), `review.opt-in`, `review.unclassed` and
`review.twin`, and the `review` kind, and closes 10 gaps.
- **The owed replays first:** the design-audit preset run blind on a frozen history, scored against 59 known defects.
- **The preset:** five lenses for design records. They are coherence, grounding, reuse held to precedent, the failure
  envelope extended to trust boundaries, and alternatives and cost.
- **Opt-in lenses** (security, alternatives, cost, portability, adopter migration, topology), each swapped for a named
  default lens.
- **The panel:**
  - skeptic batches sorted by address;
  - duplicates counted as merged confirmations;
  - grades per id;
  - refuted claims and twins flagged to the synthesizer;
  - fix verdicts by class;
  - one disposition per confirmed finding.
- **The review records** realigned with the code, and the twin merge when the owner opts in (RS-1).
- **Since first presented:** one unit, the scorer factory (night pass, point 2). It is one deterministic scorer that
  re-derives every figure from raw outputs, extracted from `review_replay.py` with aScoutedSeam's grader as its second
  instance. gap-test-18 came with it.
- **To look at:**
  - It must land before dDeclaredLoop, whose breakpoints call it (AF-1), and does, at 20 against 35.
  - Its security lens now has a second caller, Maintain's weekly security review (NP-19).

### dDeclaredLoop: Spine, the loop

After dOrderedCharter and dFairHearing, 22 units, finishing at 57. Seven builds wait on it: dPlacedRequest,
dKeptSession, dWitnessedBar, dBoundRoles, dTotalRecall, dRankedPlan and dIndexedDesign. It owns 12 items, 19 keys,
4 kinds and 4 tag namespaces, and closes 10 gaps, 6 of them HIGH.
- **The loop:**
  - the loop kit, keyed by stage tags;
  - each step a program of declared items, named by semantic tags;
  - one transition table per level, backward transitions recorded, and an engine refusing any transition it lacks;
  - terminal states, a default failure route and one closed disposition set;
  - stage claims and the coverage gate;
  - the `step`, `item`, `policy` and `command` namespaces.
- **Witnesses and position:**
  - witnesses computed, never typed, a probe's commands among them, re-run at its pinned SHA;
  - the position engine, deriving step, next item and interrupts from witnesses;
  - claims keyed and trusted by key and source.
- **Policy machinery:** the guard, the TTY CLI and the default floor, and the factories and conformance gates for
  commands, keys, presets, stages, hooks, roles and workflows.
- **Review control flow (AF-1):**
  - breakpoints at any item boundary, with reviews and owner gates one mechanism;
  - the breakpoint program's trigger, disposal, fold and cost;
  - the follow-up and design-audit rounds, with `REVIEW_ROUNDS` retired;
  - the stage-exit recommendation for every step.
- **Since first presented:** split three ways (SP-1, S3).
  - It keeps the loop's core and the review control flow. Test's stage items run through that control flow, and
    `review.dispose` reads the follow-up rounds' key.
  - Twenty-one of its first 43 units moved to dPlacedRequest and dKeptSession, and so did the night pass's four
    additions.
- **To look at:**
  - It finishes at 57, not 73. Of the seven builds that wait on it, dWitnessedBar is the one on the critical path.
  - The review control flow is now its heaviest part: four units carrying twelve keys.

### dPlacedRequest: Entry, new

After dDeclaredLoop, 7 units, finishing at 64. dKeptSession, dBoundRoles and dTotalRecall wait on it. It owns the
five entry items and the probe program's seven, 17 keys, and the `card`, `lease` and `probe` kinds. It closes 8 gaps,
6 of them HIGH.
- **Leases:**
  - one lease grammar for builds, units and cadence runs, with epochs bumped at every take-over;
  - run claims migrated onto it, and overlap warned or refused;
  - fleet identity checked against the remote, and offline behaviour as `leases.offline` defines.
- **The card:** at level 1, a ref per build on the remote, cached in the clone, snapshotted and re-keyed on resume,
  with `resume.context` and `resume.partial`.
- **Entry:** the entry step's items (orientation, the three placing items and the claim), and the placement predicate
  and its check. An unattended prompt is placed the same way.
- **What each item carries:** its `map` slot declarations and its code seed (point 3).
- **The probe program:** seven items and the `probe` kind, placed at any boundary or raised by any role, with
  stand-ins until the tester and the experiment shape land (point 2).
- **To look at:**
  - Six HIGH gaps rest on seven units. Orientation and concurrency are where today's sessions lose most, so the
    leases and the card each carry several units of work.
  - It has slack. It lands at 64, and dBoundRoles and dTotalRecall cannot start before dWitnessedBar lands at 79. It
    can grow by 15 units at spec time without moving the path.

### dKeptSession: Session, new

After dDeclaredLoop and dPlacedRequest, 18 units, finishing at 82. dWellOiledMachine and dIndexedDesign wait on it.
It owns 12 keys and the `mailbox message` kind, and closes 3 gaps, 2 of them HIGH.
- **Presets:** the named presets and their completeness check, the preset step in dGroundRules's reader, the
  charter's preset section, and policy at govkit intake.
- **Coordination:** the mailbox per build, read at every item boundary; live delivery where the harness has it; and
  dependency coordination through the parent's lease.
- **Sessions:**
  - orientation cost recorded per stage;
  - progress reported through `notify.owner`;
  - a fresh session recommended until the card-import fixture passes;
  - the card's pointers;
  - what a session does as its window fills;
  - compaction summaries read as leads.
- **Attendance and `repeat`** (point 1): the attendance rule, which never selects an actor, the driver or a binding,
  and the `repeat` disposition onto a playbook.
- **Two small units:** `actions.free` at the tool call, and the policy namespaces' purposes reviewed.
- **To look at:**
  - It is grouped by when its parts are needed, not by theme. That is the split's price.
  - Until it lands at 82, only the `standard` preset works, no mailbox carries notices, and attendance is not yet a
    key.
  - It has the most slack in the wave. Nothing that waits on it starts before 119.

**The owner's word:** approved, 2026-10-18 (`[words]`).

## [wave-2] The stage and memory builds, as presented

Derived at `9b4386707`, whose chain is `b3866c4ad`'s. Each build's "since the walk opened" reads its row against
`beda01950`, the commit the walk opened at.

### dWitnessedBar: Test

After dDeclaredLoop, 22 units, finishing at 79. Six builds wait on it: dBoundRoles, dTotalRecall, dMindYourWords,
dScopedBuild, dShippedRelease and dTendedCadence. It owns 9 items, 15 keys, 6 kinds, the retrofit system and 3 tag
namespaces, and closes 20 gaps, 6 of them HIGH.
- **The verdict:**
  - gate health measured against a reliability bar;
  - bypasses recorded;
  - attribution deciding what blocks;
  - the runner-written verdict the pre-push hook reads;
  - held legs by policy, and the peer-node verifier;
  - seen-red records and flake quarantine.
- **Tests as a product contract:** runner adapters, a derived pre-commit list, and multi-node cost evidence.
- **Legs:**
  - the gate-leg factory and its conformance gate, each leg declaring the principles it enforces;
  - the `leg`, `check` and `pack` namespaces;
  - each leg's purpose, today's 140 reviewed;
  - `tests=` and `enforces=` edges on legs.
- **The retrofit's ledger:** the baseline ledger factory (shrink-only debt, append-only history, declared set or
  ceiling), the `ratchet` pack and `test.seed` at registration. Gov's own 27 registries, pins and legacy lists move
  onto it.
- **A fix pass keeps its check** (night pass, point 6). A fix pass may not edit the red leg's own tests or gate
  script. A change there routes through the tester's wrong-spec judgment to Design as a new unit.
- **Since the walk opened:** two units from the night pass, the fix-pass rule and the leg edges, and gap-test-19.
- **To look at:**
  - It is the one stage build that lands before dBoundRoles binds the roles, and its stage names the tester three
    times: `test.attribute`, `test.reason` and the fix pass's judgment. No agent plays the tester today, and none
    until dBoundRoles lands at 113. The probe program declares a stand-in for the same gap, and Test declares none.
    That is WK-1.
  - The reliability bar is what lets `strict` and `guarded` refuse hook bypass without stalling (R5.1).

### dBoundRoles: Roles

After dDeclaredLoop, dWitnessedBar and dPlacedRequest, 34 units, finishing at 113. dWellOiledMachine and
dShippedRelease wait on it. It owns 20 keys, the `work order` kind, the role-shapes system and 2 tag namespaces, and
closes 25 gaps, 11 of them HIGH.
- **The roster:** twelve core roles, the tester among them, and the deployer and maintainer as expansion roles,
  defined by dShippedRelease and dTendedCadence.
- **The work order:**
  - rendered per item, hashed into the spawn marker and bound to its act;
  - memory slices, code-notes and legacy slots, each under its own budget;
  - the `map` slot, the `code` slot from each item's seed, and instruction units selected by `feature.*`, each
    "not installed" until dTotalRecall lands.
- **Roles as enforced fields:**
  - static instructions as fields, every limit paired with its enforcer;
  - returns through a schema-forced channel;
  - the role index beyond workers' reach;
  - shell writes held to the allowance;
  - write classes enforced.
- **Trust and repairs (P29):** inputs handed as content, each fact keyed and classed by the executor, trust profiles,
  the answered-call hook, and repairs filed as asks against the producer's record.
- **Who composes what:** the prompt writer composes every role's task, and the orientation scout composes the card
  and its map cell.
- **Shapes:** `single`, `per-unit`, `panel`, `twin` and `experiment`, each with its fan, checklist, merge and an agent
  cap.
- **Since the walk opened:** four units from the night pass, with the `experiment` shape, and gap-roles-21 and
  gap-roles-22:
  - the tester agent and the `probe` outcome on every return;
  - owner questions asked live while attended;
  - the `code` slot;
  - the `feature` selector and the code-notes slot from a tag's bundle.
- **To look at:**
  - Three of its slots render "not installed" until dTotalRecall lands, six units after it.
  - It binds the planner and the architect, whose items run dRankedPlan's and dIndexedDesign's stages, yet neither
    build follows it. That is WK-2.
  - 11 of its 25 gaps are HIGH. The roles layer is where P25, role work only in role agents, is enforced.

### dTotalRecall: Memory

After dDeclaredLoop, dWitnessedBar and dPlacedRequest, 40 units, finishing at 119. Four builds wait on it:
dWellOiledMachine, dRankedPlan, dIndexedDesign and dShippedRelease. It owns 4 items, 25 keys, 16 kinds, 3 systems and
5 tag namespaces, and closes 34 gaps, 9 of them HIGH.
- **The memory contract:** the record-kind registry, each kind with its tag, layer, home, id rule, schema, writer,
  readers, lifecycle and check. Templates and checks are generated from it, and one `record` command writes, minting
  ids under the build's claim or lease.
- **Builds and relations:** the README's front-matter schema, the slug and id grammar exported once, typed relations
  checked both ways, and the ask kind's acceptance at filing.
- **Decisions and reuse:**
  - decisions split by kind, reuse entries as level-3 units and a major-decision log;
  - the reuse scout's house index;
  - `reuse_lookup.py` retired, and memory-recall narrowed to a record finder.
- **Finding records:** the extractors, `record find` and `record show` over the one index, the read budget per role
  item, and the default load's memory share.
- **The project map:** the level-0 map, `gov map`, its completeness check, and the atlas from the same node table.
  The map is built only if it wins its replay.
- **Code depth** (P32, night pass):
  - the core `code` record, replacing symbols and callers;
  - `gov code show`, `callers`, `tests` and `where`;
  - enrichment keyed by body hash;
  - the replay extended to code;
  - the ctags pack (NP-10).
- **The relational syntax's memory half** (P33):
  - typed edges from annotations, front matter, dossiers and decision rows;
  - the region-parser factory;
  - the dossier's header becoming the feature node;
  - the `feature` selector armed.
- **The retrofit's memory half:** the `baseline` and `census` kinds, the `origin` field, the `adopt` program, the
  annotations leg and the marker namespace.
- **Since the walk opened:** nine units from the night pass and the owner's answers. The caller map gave way to the
  `code` record, and gap-mem-28 to gap-mem-34 came with them.
- **To look at:**
  - It is the largest build in the chain, 40 units, and all of them sit on the critical path.
  - The nine new units, code depth and the relational syntax's memory half, may not be needed by dWellOiledMachine,
    its successor on the path. If they are not, a split prices as dDeclaredLoop's did. That is WK-3.

### dIndexedDesign: Design

After dDeclaredLoop, dTotalRecall and dKeptSession, 12 units, finishing at 131. dScopedBuild and dTendedCadence wait on
it. It owns 10 items, 4 keys and 10 kinds, and closes 10 gaps, 4 of them HIGH.
- **The hand-off and the index:** the derived-READY hand-off and the design index.
- **Design review by policy,** with its opt-in, effort and audit guard.
- **Evidence:** reuse and alternatives backed by recorded probes, and the research harness on the `experiment` shape.
- **The spec as a contract:**
  - measured, and redesigned as a structured, tagged contract;
  - agreement and tier checks, and sections named by tag;
  - the feature level, each feature's interfaces declared, with two-level re-entry and fork resolution by policy;
  - `implements=` and `decides=` edges, and `design.seams` reading a tag's bundle.
- **Playbooks** (night pass, point 1): the playbook record kind, which is dScriptedRepeat's canon with its pieces and
  sets by hash and `check-playbook` as Design's pack. With it come the playbook set and its set check, registered at
  Test's leg-pack point.
- **Since the walk opened:** three units from the night pass, the playbook kinds and the structured spec's edges. The
  research harness was re-based on the `experiment` shape, and gap-flow-17 came with them.
- **To look at:** its stage's items are the architect's, and its research harness waits on dBoundRoles' `experiment`
  shape. dBoundRoles is not its ancestor (WK-2).

### dRankedPlan: Plan

After dDeclaredLoop and dTotalRecall, 13 units, finishing at 132. dTendedCadence waits on it. It owns 9 items, 6 keys
and 3 kinds, and closes 10 gaps, 5 of them HIGH.
- **Priority and triage:** priority beside `parents:` and the generated plan view, rule-based triage, dormancy
  disposal, and the live-build mapping carried out.
- **The planner's stage:**
  - the planner and triager role and the Plan workflow;
  - Plan Review;
  - kickoff offering the next item, with attended briefs gated;
  - the full kickoff only where `kickoff.runs` says.
- **Ratification:** the session's intake log is read as the request's ratification. Until dWellOiledMachine's hook
  writes it, `plan.exit` falls back to the owner gate.
- **What Plan hands on:**
  - each role item's memory read set, sized at Plan;
  - the probes owed before Design (night pass, point 2);
  - the intent fields: affected systems derived from the `code` record, and open questions as fork tags (point 6).
- **Since the walk opened:** two units from the night pass, and gap-plan-08.
- **To look at:**
  - Until dWellOiledMachine lands, eighteen units after it, every Plan exit waits for the owner. Under unattended by
    default, that is the one owner gate the chain keeps for a while.
  - Its stage's items are the planner's, and dBoundRoles is not its ancestor (WK-2).

## [wave-2-forks] Wave 2's forks, parked for the owner

| Fork | Question | Options, the recommendation first | What the answer sets |
|---|---|---|---|
| WK-1 | Who plays the tester before dBoundRoles lands? | a minimal tester agent ships with dWitnessedBar in today's roles kit and dBoundRoles re-founds it with the other roles, one more unit in dWitnessedBar; an owner item stands in, as the probe program's does, so every own or mixed red and every Test exit waits for the owner until dBoundRoles lands; the skeptic stands in, a role doing another's work against P25 | a structural decision |
| WK-2 | Should dIndexedDesign and dRankedPlan follow dBoundRoles? | yes, both: dBoundRoles lands at 113, before either can start at 119, so the edges cost nothing and their stages' roles are bound first; keep them as they are, the stages' roles unplayed until dBoundRoles happens to land | a structural decision about the chain |
| WK-3 | Price a split of dTotalRecall? | price it before wave 3, as the spine's split was; keep it whole | a structural decision about the chain |

## [wave-2-answers] Wave 2's forks, answered

The owner approved wave 2 and took each fork's recommendation, 2026-10-18 (`[words]`):
- **WK-1:** a minimal tester agent ships with dWitnessedBar in today's roles kit, and plays `test.attribute`,
  `test.reason` and the fix pass's judgment. dBoundRoles re-founds it with the other roles. dWitnessedBar gains a
  unit, and the critical path with it.
- **WK-2:** dIndexedDesign and dRankedPlan follow dBoundRoles, so their stages' roles are bound before they start.
  The research harness builds on the `experiment` shape outright, and its stand-in is gone.
- **WK-3:** a split of dTotalRecall is priced before wave 3, in
  `build/2026-10-18-build-PLAY-dClosedLoop-1-wk3-pricing.md`.
- **WK-4,** asked once that pricing was written: the owner chose C2 (that record's `[answers]`). dTotalRecall and
  dBoundRoles each split, and dLinkedLibrary and dFurnishedOrders join wave 2, where their units were.

## [wave-3] The runtime and the builds it opens, as presented

Derived at `7788ac269`. Each build's "since the walk opened" reads its row against `beda01950`.

### dWellOiledMachine: Runtime

After dBoundRoles, dTotalRecall and dKeptSession, 31 units, finishing at 128. Four builds wait on it: dMindYourWords,
dScopedBuild, dShippedRelease and dTendedCadence. It owns 7 items, 10 extension points, 18 keys, 7 kinds and 2 tag
namespaces, and closes 35 gaps, 13 of them HIGH, the most of any build.
- **The platform spike first:** a role-typed Workflow agent run inside a headless act session, with the headless
  backend measured beside it.
- **The driver:**
  - the supervisor, the only driver in every mode, the owner's session its client;
  - `next` over the loop kit's position function, and the `next —` micro-format;
  - the owner's pause, resume, withdraw and supersede, and attend and unattend;
  - the `step —` announcement before each act while attended.
- **Intake:** the prompt-submit hook writing each owner prompt to the session's intake log, Plan's ratification and the
  placement dispositions re-pointed to it, and intake for a prompt that reaches no owner session.
- **Acts:**
  - one act session per role act, with act binding and the epoch check at every spawn;
  - binding against the resolved shape's digest, each act writing its shape-run row;
  - the persisted-return store, and agent slots reserved under the cap.
- **The enforcement surface:** one dispatcher entry per event, the kits' fragments as packs, ask rules only the
  dispatcher answers, and each pack's refusal naming its rule and remedy; grants on every adapter row, and the secret
  value scan.
- **Sessions:** bound on every source; the compact hook re-injecting the build's card; the session-start hook loading
  the default set, card and map, and ending with `next`'s line; each compaction journaled.
- **Hosts and adapters:** scheduler hosts, harness adapters with capability tables, a measured `browser` row among them,
  the node registry, and the `visual.capture` command adapter.
- **The rest:** workspaces and the commit queue, event waits, the journal grammar, and the unattended kit dissolved
  into the loop kit and this one.
- **Since the walk opened:** seven units from the night pass:
  - the one-driver statement;
  - the announcement;
  - intake beyond the owner's session;
  - the unattended kit's dissolution;
  - the browser row and visual capture;
  - experiments' acts;
  - refusal text.

  Three units were reworded, and gap-orient-16 to gap-orient-18 and gap-rt-22 to gap-rt-24 came with them.
- **To look at:**
  - It left the critical path with WK-4. It lands four units before dTendedCadence can start, so it can grow by four
    at spec time before it returns to the path.
  - Its first unit, the platform spike, decides the runtime's shape. If it fails, the owner's session keeps hosting
    the driver under its owner binding, as the night pass's hosting rule says.
  - It carries the most gaps of any build.

### dScopedBuild: Build

After dIndexedDesign, dWitnessedBar, dWellOiledMachine and dFurnishedOrders, 11 units, finishing at 143.
dConvergedCharter waits on it. It owns 9 items, 6 keys and 2 kinds, and closes 7 gaps, 3 of them HIGH.
- **The exit contract:** one contract with a history-derived base, refusing a build's exit while a core red its own
  commits introduced stands, and the core checks run by the executor at Build's exit.
- **Scope and specs:**
  - built specs frozen;
  - every closing-review finding disposed as new units;
  - scope checked at the push by the touch join over the unit's own commits.
- **The record:** the closing review recorded, a write gate reading derived state, and the checklist witnessed.
- **The retrofit's drain:** each unit drains the legacy it touches, in hunks under `retrofit.drain-cap`, and claims
  the baselined map keys its write set holds.
- **Since the walk opened:** two units from the night pass. A bug-report patch build gets a red-first `reproduction`
  probe before its fix, and a playbook's pieces are built as units.
- **To look at:** it has 14 units of slack before dConvergedCharter can start. Its builders' code and map slots come
  from dFurnishedOrders, its parent since WK-4.

### dTendedCadence: Maintain

After dWitnessedBar, dRankedPlan, dWellOiledMachine, dIndexedDesign and dFurnishedOrders, 14 units, finishing at 146.
dCalibratedLens waits on it. It owns 7 items, 15 keys and 2 kinds, and closes 12 gaps, 2 of them HIGH.
- **The Maintain run:** its step checklist on the flow's executor, never a recipe-mode playbook, the cadence on
  Runtime's hosts, the safe-fix set and the maintenance record.
- **Detectors:**
  - detectors with owners, and map freshness;
  - the memory's dead pointers, absorbing `check-dead-paths.sh` with its merge-bar leg;
  - bundle members whose code changed while their head line did not.
- **Delivery:** Maintain and the Loop Review as cadence steps of the observability expansion, patch intakes rendered
  from keyed readings, `maintain.retrofit-heat`'s sweeps filed as patch builds, and the maintainer's definition.
- **Since the walk opened:** four units from the night pass and the owner's answers, and gap-maint-12 and
  gap-maint-13:
  - a cyclic playbook's cadence item, filing `repeat` intakes;
  - the bundle detector;
  - the weekly security review;
  - readings tiered by their deviation.
- **To look at:**
  - It is on the critical path again, now after dIndexedDesign.
  - Its four new units sit on the path. A split could save at most eight units, since dConvergedCharter also waits for
    dShippedRelease, and moving only the four new units would save four. That is WK-6.

### dMindYourWords: Lexicon

After dWellOiledMachine, dWitnessedBar, dLinkedLibrary and dFurnishedOrders, 17 units, finishing at 145. No build waits
on it. It owns 5 keys and the lexicon-declaration kind, and closes 10 gaps, 3 of them HIGH.
- **Definition classes:** conforming, forced, out of scope, not a name, and debt. Only debt counts against the
  shrink-only pin, held as a keyed ledger population.
- **Forced names:** recognised by what forces them, from packs generated per host kit, and gov's own contract-forced
  names in a table the instruction write path owns. The first wave of packs covers Python's stdlib bases, its test
  frameworks, `ast`, `logging` and the shell hosts. Django, Flask, Starlette, FastAPI and React follow after an
  adopter census.
- **Enforcement:**
  - the work order's vocabulary slice;
  - staged definitions checked at commit;
  - the branch's offenders compared with its base's at the bar;
  - drift beyond verbs, one verb per declared family per object, and a frozen noun canon.
- **The vocabulary** changes only through the instruction write path, and the two drift signals are the lexicon's own
  leg pack.
- **Since the walk opened:** one unit, the overloaded terms settled: attended, playbook and baseline (gap-lex-09).
- **To look at:**
  - No build waits on it, not even dConvergedCharter, whose exit check joins the fates table, and four fates rows go
    to it. That is WK-5.
  - Its packs unit, clause 7, reads like several units of work: two waves of generated packs.

## [wave-3-forks] Wave 3's forks, parked for the owner

| Fork | Question | Options, the recommendation first | What the answer sets |
|---|---|---|---|
| WK-5 | Should dConvergedCharter wait for dMindYourWords? | yes: dMindYourWords lands at 145, before dConvergedCharter can start at 157, so the edge costs nothing, and convergence's fates join covers the lexicon's four rows; no, the lexicon lands on its own and convergence's join leaves its rows unchecked | a structural decision about the chain |
| WK-6 | Split dTendedCadence? | keep it whole: no split saves more than eight units, bounded by dShippedRelease, and only its four new units could plausibly move, saving four; price a split, as WK-3 was | a structural decision about the chain |

## [walk-instrument] The walk's facts, and the clause scan

Each build's facts are derived, never typed: its stage, parents, children, finish, units, gaps by grade and owned
nodes by kind.

```python
"""Derive each chain build's walk facts from the records: stage, parents, children, earliest finish in units, its
planned units (each clause's head), the gaps it owns by area, and the nodes it owns by kind.

Usage: python -X utf8 walk_facts.py [<build> ...]   (from the worktree root; no build prints them all)
"""
import collections
import importlib.util
import re
import sys

B = "memory/builds/dClosedLoop/build/"
spec = importlib.util.spec_from_file_location("projectmap", B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py")
mp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mp)
A, ns = mp.derive()
owned = collections.defaultdict(lambda: collections.Counter())
for kind in ("item", "policy-key", "point", "record-kind", "tag-namespace", "system"):
    for n in ns[kind]:
        for k, vs in n["rels"]:
            if k == "owner":
                for v in vs:
                    owned[v][kind] += 1
v2 = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
chain = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
rows = {}
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| ([^|]+) \| ([^|]+) \| (.+) \| ([^|]+) \|$", ln)
    if m:
        rows[m.group(1)] = {"stage": m.group(2).strip(), "parents": [p.strip() for p in m.group(3).split(",")],
                            "units": [u.strip() for u in m.group(4).split("; ") if u.strip()],
                            "gaps": [g.strip() for g in m.group(5).split(",")]}
names = list(rows)
for b in names:
    rows[b]["parents"] = [p for p in rows[b]["parents"] if p in rows]
children = {b: [c for c in names if b in rows[c]["parents"]] for b in names}
finish = {}


def f(b):
    if b not in finish:
        finish[b] = max((f(p) for p in rows[b]["parents"]), default=0) + len(rows[b]["units"])
    return finish[b]


for b in names:
    f(b)
reg = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md", encoding="utf-8").read()
sev = dict(re.findall(r"(?m)^\| (gap-[a-z]+-\d\d) \| [^|]+ \| (HIGH|MED|LOW) \|", reg))
want = sys.argv[1:] or sorted(names, key=lambda b: finish[b])
for b in want:
    r = rows[b]
    gaps = []
    for g in r["gaps"]:
        m = re.match(r"(gap-[a-z]+)-(\d\d) to gap-[a-z]+-(\d\d)", g)
        gaps += [f"{m.group(1)}-{i:02d}" for i in range(int(m.group(2)), int(m.group(3)) + 1)] if m else [g]
    by_sev = collections.Counter(sev.get(g, "?") for g in gaps)
    print(f"=== {b} · {r['stage']} · after {', '.join(r['parents']) or 'dClosedLoop'} · before "
          f"{', '.join(children[b]) or 'none'} · finishes at {finish[b]} of {max(finish.values())} · units "
          f"{len(r['units'])} · gaps {len(gaps)} ({', '.join(f'{k} {v}' for k, v in sorted(by_sev.items()))}) · owns "
          + ", ".join(f"{v} {k}s" for k, v in sorted(owned[b].items())))
    for i, u in enumerate(r["units"], 1):
        print(f"  {i:2d}. {u[:150]}{'…' if len(u) > 150 else ''}")
```

```text
$ python walk_facts.py dGroundRules dOrderedCharter dFairHearing dDeclaredLoop
=== dGroundRules · Policy · after dClosedLoop · before dOrderedCharter, dFairHearing · finishes at 8 of 181 · units 8 · gaps 1 (HIGH 1) · owns 1 policy-keys
   1. `.governance/policy.toml`, its schema, its one reader and its JSON mirror, moved from dDeclaredLoop so that both roots read policy from a build ahead …
   2. the reader extending `read_policy_key`'s contract, read at the landed revision, never from the working tree, parsed and never sourced (M7)
   3. each key resolved in one order: an override in the file, then the named preset's value once dDeclaredLoop adds presets to this reader, then the catalo…
   4. a malformed file or an out-of-set value read as `policy.on-invalid` says, by default the last valid landed revision with the reason recorded and, with…
   5. the JSON mirror regenerated at each landing and pinned to the landed revision, every consumer reading the mirror from the landed revision's blob, or c…
   6. the minimal guard, enforcing the defaults of `policy.guard` and `policy.proof`, owner-only and the TTY proof, without reading either key, and refusing…
   7. the legacy homes on a shrink-only list derived by query from the files they guard, never typed, red on a planted row and green on today's files: every…
   8. an arm red when a key whose Owner build has landed has no reader, its population the catalogue's Owner column joined to the builds landed on the defau…
=== dOrderedCharter · Foundation · after dGroundRules · before dDeclaredLoop · finishes at 30 of 181 · units 22 · gaps 21 (HIGH 12, MED 9) · owns 12 policy-keys, 2 record-kinds, 2 systems, 9 tag-namespaces
   1. the practice catalogue and `charter.practices`
   2. the charter re-founded in its level-0 envelope (front door, precedence and override rule with `charter.override` and its record, instruction map, acti…
   3. envelopes rendered for every registered document and the gate over them
   4. the instruction map re-injected on compact and resume
   5. ranked envelopes in every subagent handoff
   6. the drive section composed from a drive table in each adopted kit's descriptor, checked both ways, each subagent's role line repeated in its handoff, …
   7. the core: the principle registry, the meta-check, the kinds register with each kind's owning build, the conformance-gate contract, the exception regis…
   8. the build's card delivered at level 1 through an ignored per-worktree card file the charter's entry file imports, re-rendered by every session-start h…
   9. the instruction-unit registry (per unit: tag, level, statement type, scope tags, trigger, budget class, source, owning kit), documents rendered from u…
  10. the namespaced tag system (reader, level, layer, step, item, role, policy, practice, principle, kind, record, kit), of which it registers reader, leve…
  11. load sets derived per reader and item, budgeted per load point and per harness, extending `template-size-limits.txt`, refused at render when over budg…
  12. the statement grammar and its check, render provenance in a sidecar lock
  13. the ladder renumbered, the platform above it and the charter at level 0
  14. memory instructing nothing, a standing directive promoted into a unit
  15. the instruction manifest and its guarded write command (`instructions.edit`, `instructions.proof`), each `instructions.edit` value given its arm, witn…
  16. the layer register, the layer contract, the layer kind's factory and conformance gate, and the check that the core never depends on an expansion or an…
  17. the edges that check finds today each made a declared optional slot with a named fallback, or moved into the core, in its own unit: `gen_build_index.p…
  18. the moved grammar's by-path consumers re-pointed in the move's own unit, from an inventory of every reader of `extract.py` and `recall_conf.py` by pat…
  19. the tag grammar, its namespace registry and the derived tag index, one JSON file per tree at `<git-common-dir>/gov/index/<tree>.json` written atomical…
  20. the instruction unit's schema and grammar, the one renderer with the charter and work-order templates and the write command, absorbing playbook parity…
  21. each practice's reach per step rendered as step-scoped units handed in work orders, the charter keeping one line per practice (IW-2)
  22. the namespace row's `purpose-source` and `owner` fields and the chain registry's purpose field, their existing entries reviewed by dTotalRecall's PM-5…
=== dFairHearing · Review harness · after dGroundRules · before dDeclaredLoop, dCalibratedLens · finishes at 19 of 181 · units 11 · gaps 9 (HIGH 1, LOW 3, MED 5) · owns 4 items, 3 policy-keys, 1 record-kinds
   1. the owed replays first: the design-audit preset run blind at blob 767187aa, from a bundle of the history to 6cfd21619 cloned outside the repository, s…
   2. the design-audit preset of the spec-audit kind for design and architecture records, chosen by a `preset` argument that Design's breakpoint passes when…
   3. opt-in lenses (security, alternatives, cost, portability, adopter migration, topology), each swapped for a named default lens of its preset in the fiv…
   4. skeptic batches sorted by cited address
   5. duplicates counted as merged confirmations, with the orphan check on both kinds
   6. items carrying a grade per id, ranked by the highest
   7. refuted claims and same-address twins handed to the synthesizer to flag
   8. fix verdicts judged by class, and every confirmed finding given one disposition from `review.report`'s grammar (`class:`, `new:`, `gate:`, or `none` u…
   9. portability, topology and adopter migration as bug-class checklist entries anchored to their paths, never universal, and lens notes passed by the call…
  10. the review records brought back in line with the code at their sources (`tools/workflows/REVIEW-PROTOCOL.template.md`'s lens list, lens count and skep…
  11. the panel's internals, and the twin merge a review step runs when the owner's `review.twin` opts it in (RS-1)
=== dDeclaredLoop · Spine · after dOrderedCharter, dFairHearing · before dBoundRoles, dTotalRecall, dWitnessedBar, dRankedPlan, dIndexedDesign · finishes at 73 of 181 · units 43 · gaps 19 (HIGH 12, LOW 1, MED 6) · owns 17 items, 43 policy-keys, 7 record-kinds, 4 tag-namespaces
   1. the loop kit and definition keyed by the stage tags, the roles kit's stage table moved and its seven readers re-pointed in the same unit, never waitin…
   2. the named presets and their completeness check, with its pair rules, and each shipped preset loaded with only the core installed, refused only for a v…
   3. the preset step added to dGroundRules's reader, so a key the file does not override reads the named preset's value, seen red when a strict-named file …
   4. the charter's preset section, the preset's name and the keys that differ from it, rendered through dOrderedCharter's renderer and seen red on a plante…
   5. the guard, the TTY CLI and the default floor
   6. the transition record three ways
   7. stage claims and the coverage gate
   8. the witness-class rule
   9. policy at govkit intake
  10. the factories and conformance gates for commands, policy keys, presets, stages, hooks, roles and workflows
  11. the coordination feature: one lease grammar for builds, units and cadence runs, each lease carrying an epoch bumped at every take-over, with run claim…
  12. the mailbox per build, its closed set of message kinds checked on write, read and disposed at every transition, shown on the card and kept in the buil…
  13. live delivery where the harness has it
  14. dependency coordination by the parent's lease, interfaces confirmed at Design's exit, change and landing notices
  15. the position engine: deriving each unit's step, the build's step, the next item and its interrupts from witnesses, items idempotent by witness and key…
  16. the build's orientation card at level 1, below the charter, kept as a ref per build on the remote (the truth), cached in the clone by build and object…
  17. claims keyed and trusted by key and source
  18. the entry step's items: the card's orientation, the three placing items and the claim (PM-9)
  19. the placement predicate and its check, moved from dRankedPlan (RC-8): a disposition for every request, made by `placement` and recorded with its reaso…
  20. each step's items declared with actor, inputs, allowance, return schema and witness
  21. `actions.free` at the tool call
  22. orientation cost recorded per stage
  23. backward transitions recorded like forward ones
  24. the mailbox read at every item boundary by `mailbox.reads`, with the `intake` message kind
  25. progress reported by `notify.owner`
  26. a fresh session in the build's worktree recommended until the card-import fixture passes
  27. the card's pointers updated as the build progresses, by `card.pointers`: the latest records by tag, the open forks and the item in flight, so a compac…
  28. what a session does as its window fills, by `context.on-full` and `context.threshold`
  29. a compaction's summary read as a lead, never a source
  30. every checklist item named by a semantic tag, its number only display order
  31. each step a program of items with declared dependencies, every item declared with its tag, actor, inputs by layer, instruction scope, allowance, retur…
  32. one transition table per level (build, feature, unit), the engine refusing any transition it lacks
  33. a default failure route (the refusal recorded, `next` returning the frontier: the unwitnessed items whose needs are witnessed)
  34. the terminal states flow-steps' `[transitions]` declares, and `deps.on-parent-withdrawn`
  35. one closed disposition set
  36. witnesses computed rather than typed by the acting agent (acceptance re-run by the executor, red attribution joined to the verdict)
  37. the `step`, `item`, `policy` and `command` tag namespaces, with their extractors
  38. the items' declarations of the `map` slot and their unfolds
  39. the policy namespaces' purposes, reviewed
  40. breakpoints placeable at any item boundary (`review.breakpoints`), reviews and owner gates one mechanism with `review.<stage>` and `autonomy` its defa…
  41. the breakpoint program's own items, `review.trigger`, `review.dispose`, `review.fold` and `review.cost`, with `review.blocks`, `review.unverified`, `r…
  42. follow-up closing-review rounds by `review.follow-up`, and the design audit's rounds by `review.design.rounds` and `review.design.round-count`, `REVIE…
  43. the stage-exit recommendation: every step's recommend and reason items, the score computed and the reasoning returned by the step's producing role, as…
$ python critical_path.py
critical path: 181 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dShippedRelease > dConvergedCharter
each build's earliest finish, in units: dGroundRules 8, dFairHearing 19, dOrderedCharter 30, dDeclaredLoop 73, dWitnessedBar 93, dBoundRoles 123, dTotalRecall 125, dIndexedDesign 134, dRankedPlan 136, dWellOiledMachine 149, dScopedBuild 158, dTendedCadence 159, dMindYourWords 165, dCalibratedLens 167, dShippedRelease 169, dConvergedCharter 181
```

The clause scan, red on dFairHearing's preset clause before the fix and green after it:

```python
"""Find every [chain] row whose planned-units cell holds "; " inside parentheses or backticks, where the unit count's
split on "; " cuts one clause into several.

Usage: python -X utf8 paren_semis.py   (from the worktree root); exit 1 when any is found
"""
import re
import sys

v2 = open("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
chain = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
found = 0
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| [^|]+ \| (.+) \| [^|]+ \|$", ln)
    if not m:
        continue
    depth, tick, at = 0, False, []
    cell = m.group(2)
    for i, ch in enumerate(cell):
        if ch == "`":
            tick = not tick
        elif not tick and ch == "(":
            depth += 1
        elif not tick and ch == ")":
            depth = max(0, depth - 1)
        elif cell.startswith("; ", i) and (depth or tick):
            at.append(i)
    for i in at:
        found += 1
        print(f"{m.group(1)}: ...{cell[max(0, i - 70):i + 50]}...")
print(f"splits inside a clause: {found}")
sys.exit(1 if found else 0)
```

```text
$ python paren_semis.py   (before the fix: 4 splits, all in dFairHearing's preset clause, rc 1)
$ python paren_semis.py   (after it)
splits inside a clause: 0
```

## [walk-instrument-2] The walk derived again, at `b3866c4ad`

`walk_facts.py` and `critical_path.py` as above, the latter's build count raised to 18 by the split. What changed
since the first presentation is `since.py`'s:

```python
"""What changed in a build's chain row since a commit: clauses added, dropped, or reworded, and gaps added or dropped.
A build that did not exist then reads as all new; a clause matched by its first 60 characters reads as reworded.

Usage: python -X utf8 since.py <commit> <build> [<build> ...]   (from the worktree root)
"""
import re
import subprocess
import sys

V = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"


def rows(text):
    chain = text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
    out = {}
    for ln in chain.split("\n"):
        m = re.match(r"^\| (d[A-Z]\w+) \| ([^|]+) \| ([^|]+) \| (.+) \| ([^|]+) \|$", ln)
        if m:
            out[m.group(1)] = ([u.strip() for u in m.group(4).split("; ") if u.strip()],
                               [g.strip() for g in m.group(5).split(",")])
    return out


then = rows(subprocess.run(["git", "show", f"{sys.argv[1]}:{V}"], capture_output=True, text=True,
                           encoding="utf-8").stdout)
now = rows(open(V, encoding="utf-8").read())
for b in sys.argv[2:]:
    old_u, old_g = then.get(b, ([], []))
    new_u, new_g = now[b]
    print(f"=== {b}: units {len(old_u)} -> {len(new_u)}, gaps {len(old_g)} -> {len(new_g)}")
    old_heads = {u[:60]: u for u in old_u}
    for u in new_u:
        if u in old_u:
            continue
        if u[:60] in old_heads:
            print(f"  reworded: {u[:200]}")
        else:
            print(f"  added: {u[:200]}")
    new_heads = {u[:60] for u in new_u}
    for u in old_u:
        if u not in new_u and u[:60] not in new_heads:
            print(f"  left: {u[:160]}")
    for g in sorted(set(new_g) - set(old_g)):
        print(f"  gap added: {g}")
    for g in sorted(set(old_g) - set(new_g)):
        print(f"  gap left: {g}")
```

```text
$ python walk_facts.py dGroundRules dOrderedCharter dFairHearing dDeclaredLoop dPlacedRequest dKeptSession
=== dGroundRules · Policy · after dClosedLoop · before dOrderedCharter, dFairHearing · finishes at 8 of 189 · units 8 · gaps 1 (HIGH 1) · owns 1 policy-keys
   1. `.governance/policy.toml`, its schema, its one reader and its JSON mirror, moved from dDeclaredLoop so that both roots read policy from a build ahead …
   2. the reader extending `read_policy_key`'s contract, read at the landed revision, never from the working tree, parsed and never sourced (M7)
   3. each key resolved in one order: an override in the file, then the named preset's value once dKeptSession adds presets to this reader, then the catalog…
   4. a malformed file or an out-of-set value read as `policy.on-invalid` says, by default the last valid landed revision with the reason recorded and, with…
   5. the JSON mirror regenerated at each landing and pinned to the landed revision, every consumer reading the mirror from the landed revision's blob, or c…
   6. the minimal guard, enforcing the defaults of `policy.guard` and `policy.proof`, owner-only and the TTY proof, without reading either key, and refusing…
   7. the legacy homes on a shrink-only list derived by query from the files they guard, never typed, red on a planted row and green on today's files: every…
   8. an arm red when a key whose Owner build has landed has no reader, its population the catalogue's Owner column joined to the builds landed on the defau…
=== dOrderedCharter · Foundation · after dGroundRules · before dDeclaredLoop · finishes at 35 of 189 · units 27 · gaps 24 (HIGH 12, MED 12) · owns 14 policy-keys, 2 record-kinds, 2 systems, 9 tag-namespaces
   1. the practice catalogue and `charter.practices`
   2. the charter re-founded in its level-0 envelope (front door, precedence and override rule with `charter.override` and its record, instruction map, acti…
   3. envelopes rendered for every registered document and the gate over them
   4. the instruction map re-injected on compact and resume
   5. ranked envelopes in every subagent handoff
   6. the drive section composed from a drive table in each adopted kit's descriptor, checked both ways, each subagent's role line repeated in its handoff, …
   7. the core: the principle registry, the meta-check, the kinds register with each kind's owning build, the conformance-gate contract, the exception regis…
   8. the build's card delivered at level 1 through an ignored per-worktree card file the charter's entry file imports, re-rendered by every session-start h…
   9. the instruction-unit registry (per unit: tag, level, statement type, scope tags, trigger, budget class, source, owning kit), documents rendered from u…
  10. the namespaced tag system (reader, level, layer, step, item, role, policy, practice, principle, kind, record, kit), of which it registers reader, leve…
  11. load sets derived per reader and item, budgeted per load point and per harness, extending `template-size-limits.txt`, refused at render when over budg…
  12. the statement grammar and its check, render provenance in a sidecar lock
  13. the ladder renumbered, the platform above it and the charter at level 0
  14. memory instructing nothing, a standing directive promoted into a unit
  15. the instruction manifest and its guarded write command (`instructions.edit`, `instructions.proof`), each `instructions.edit` value given its arm, witn…
  16. the layer register, the layer contract, the layer kind's factory and conformance gate, and the check that the core never depends on an expansion or an…
  17. the edges that check finds today each made a declared optional slot with a named fallback, or moved into the core, in its own unit: `gen_build_index.p…
  18. the moved grammar's by-path consumers re-pointed in the move's own unit, from an inventory of every reader of `extract.py` and `recall_conf.py` by pat…
  19. the tag grammar, its namespace registry and the derived tag index, one JSON file per tree at `<git-common-dir>/gov/index/<tree>.json` written atomical…
  20. the instruction unit's schema and grammar, the one renderer with the charter and work-order templates and the write command, absorbing playbook parity…
  21. each practice's reach per step rendered as step-scoped units handed in work orders, the charter keeping one line per practice (IW-2)
  22. the namespace row's `purpose-source` and `owner` fields and the chain registry's purpose field, their existing entries reviewed by dTotalRecall's PM-5…
  23. a build run unattended by default from its request, said in the drive section, and the charter's `[land]` rule read through the request's mandate (nig…
  24. the edge-type registry and the `edge` grammar: one closed set of typed edges, each declared once at the site that owns its fact and its inverse derive…
  25. `gov tag bundle`, returning a tag's members, regions and instructions as a manifest of ranges under `tags.bundle-rows`, folded past it, or with their …
  26. file:line citations joined to the positional population `tags.positional` holds, new text citing `path#symbol` or a blob-pinned line, as NP-17 settles…
  27. each role's load set budgeting the `code` slot (night pass, point 3)
=== dFairHearing · Review harness · after dGroundRules · before dDeclaredLoop, dCalibratedLens · finishes at 20 of 189 · units 12 · gaps 10 (HIGH 1, LOW 3, MED 6) · owns 4 items, 3 policy-keys, 1 record-kinds
   1. the owed replays first: the design-audit preset run blind at blob 767187aa, from a bundle of the history to 6cfd21619 cloned outside the repository, s…
   2. the design-audit preset of the spec-audit kind for design and architecture records, chosen by a `preset` argument that Design's breakpoint passes when…
   3. opt-in lenses (security, alternatives, cost, portability, adopter migration, topology), each swapped for a named default lens of its preset in the fiv…
   4. skeptic batches sorted by cited address
   5. duplicates counted as merged confirmations, with the orphan check on both kinds
   6. items carrying a grade per id, ranked by the highest
   7. refuted claims and same-address twins handed to the synthesizer to flag
   8. fix verdicts judged by class, and every confirmed finding given one disposition from `review.report`'s grammar (`class:`, `new:`, `gate:`, or `none` u…
   9. portability, topology and adopter migration as bug-class checklist entries anchored to their paths, never universal, and lens notes passed by the call…
  10. the review records brought back in line with the code at their sources (`tools/workflows/REVIEW-PROTOCOL.template.md`'s lens list, lens count and skep…
  11. the panel's internals, and the twin merge a review step runs when the owner's `review.twin` opts it in (RS-1)
  12. the scorer factory: one deterministic scorer that re-derives every figure from committed raw outputs, pairs the cases every variant answered and refus…
=== dDeclaredLoop · Spine · after dOrderedCharter, dFairHearing · before dPlacedRequest, dKeptSession, dBoundRoles, dTotalRecall, dWitnessedBar, dRankedPlan, dIndexedDesign · finishes at 57 of 189 · units 22 · gaps 10 (HIGH 6, LOW 1, MED 3) · owns 12 items, 19 policy-keys, 4 record-kinds, 4 tag-namespaces
   1. the loop kit and definition keyed by the stage tags, the roles kit's stage table moved and its seven readers re-pointed in the same unit, never waitin…
   2. the guard, the TTY CLI and the default floor
   3. the transition record three ways
   4. stage claims and the coverage gate
   5. the witness-class rule
   6. the factories and conformance gates for commands, policy keys, presets, stages, hooks, roles and workflows
   7. the position engine: deriving each unit's step, the build's step, the next item and its interrupts from witnesses, items idempotent by witness and key…
   8. claims keyed and trusted by key and source
   9. each step's items declared with actor, inputs, allowance, return schema and witness
  10. backward transitions recorded like forward ones
  11. every checklist item named by a semantic tag, its number only display order
  12. each step a program of items with declared dependencies, every item declared with its tag, actor, inputs by layer, instruction scope, allowance, retur…
  13. one transition table per level (build, feature, unit), the engine refusing any transition it lacks
  14. a default failure route (the refusal recorded, `next` returning the frontier: the unwitnessed items whose needs are witnessed)
  15. the terminal states flow-steps' `[transitions]` declares, and `deps.on-parent-withdrawn`
  16. one closed disposition set
  17. witnesses computed rather than typed by the acting agent (acceptance re-run by the executor, a probe's commands re-run at its pinned SHA, red attribut…
  18. the `step`, `item`, `policy` and `command` tag namespaces, with their extractors
  19. breakpoints placeable at any item boundary (`review.breakpoints`), reviews and owner gates one mechanism with `review.<stage>` and `autonomy` its defa…
  20. the breakpoint program's own items, `review.trigger`, `review.dispose`, `review.fold` and `review.cost`, with `review.blocks`, `review.unverified`, `r…
  21. follow-up closing-review rounds by `review.follow-up`, and the design audit's rounds by `review.design.rounds` and `review.design.round-count`, `REVIE…
  22. the stage-exit recommendation: every step's recommend and reason items, the score computed and the reasoning returned by the step's producing role, as…
=== dPlacedRequest · Entry · after dDeclaredLoop · before dKeptSession, dBoundRoles, dTotalRecall · finishes at 64 of 189 · units 7 · gaps 8 (HIGH 6, MED 2) · owns 12 items, 17 policy-keys, 3 record-kinds
   1. the coordination feature: one lease grammar for builds, units and cadence runs, each lease carrying an epoch bumped at every take-over, with run claim…
   2. the build's orientation card at level 1, below the charter, kept as a ref per build on the remote (the truth), cached in the clone by build and object…
   3. the entry step's items: the card's orientation, the three placing items and the claim (PM-9)
   4. the placement predicate and its check, moved from dRankedPlan (RC-8): a disposition for every request, made by `placement` and recorded with its reaso…
   5. the items' declarations of the `map` slot and their unfolds
   6. the probe program (`probe.trigger`, `probe.pin`, `probe.design`, `probe.experiment`, `probe.run`, `probe.judge`, `probe.return`) and the `probe` recor…
   7. each item's declared code seed: its write set, its scope paths or its question's paths (night pass, point 3)
=== dKeptSession · Session · after dDeclaredLoop, dPlacedRequest · before dWellOiledMachine, dIndexedDesign · finishes at 82 of 189 · units 18 · gaps 3 (HIGH 2, MED 1) · owns 12 policy-keys, 1 record-kinds
   1. the named presets and their completeness check, with its pair rules, and each shipped preset loaded with only the core installed, refused only for a v…
   2. the preset step added to dGroundRules's reader, so a key the file does not override reads the named preset's value, seen red when a strict-named file …
   3. the charter's preset section, the preset's name and the keys that differ from it, rendered through dOrderedCharter's renderer and seen red on a plante…
   4. policy at govkit intake
   5. the mailbox per build, its closed set of message kinds checked on write, read and disposed at every transition, shown on the card and kept in the buil…
   6. live delivery where the harness has it
   7. dependency coordination by the parent's lease, interfaces confirmed at Design's exit, change and landing notices
   8. `actions.free` at the tool call
   9. orientation cost recorded per stage
  10. the mailbox read at every item boundary by `mailbox.reads`, with the `intake` message kind
  11. progress reported by `notify.owner`
  12. a fresh session in the build's worktree recommended until the card-import fixture passes
  13. the card's pointers updated as the build progresses, by `card.pointers`: the latest records by tag, the open forks and the item in flight, so a compac…
  14. what a session does as its window fills, by `context.on-full` and `context.threshold`
  15. a compaction's summary read as a lead, never a source
  16. the policy namespaces' purposes, reviewed
  17. the attendance rule: `attendance` places owner breakpoints and has owner questions asked live, and never selects an item's actor, the driver or a bind…
  18. the `repeat` disposition in the placement set and its `none` row in the transition table, routing a request onto a `playbook`, filed as an ask until d…
$ python critical_path.py
critical path: 189 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
each build's earliest finish, in units: dGroundRules 8, dFairHearing 20, dOrderedCharter 35, dDeclaredLoop 57, dPlacedRequest 64, dWitnessedBar 79, dKeptSession 82, dBoundRoles 113, dTotalRecall 119, dIndexedDesign 131, dRankedPlan 132, dWellOiledMachine 150, dScopedBuild 161, dTendedCadence 164, dMindYourWords 167, dShippedRelease 171, dCalibratedLens 175, dConvergedCharter 189
$ python since.py beda01950 dGroundRules dOrderedCharter dFairHearing dDeclaredLoop
=== dGroundRules: units 8 -> 8, gaps 1 -> 1
  reworded: each key resolved in one order: an override in the file, then the named preset's value once dKeptSession adds presets to this reader, then the catalogue default with the reason recorded, which is all 
=== dOrderedCharter: units 22 -> 27, gaps 21 -> 24
  added: a build run unattended by default from its request, said in the drive section, and the charter's `[land]` rule read through the request's mandate (night pass, point 1)
  added: the edge-type registry and the `edge` grammar: one closed set of typed edges, each declared once at the site that owns its fact and its inverse derived, and the instruction selectors open to a namespa
  added: `gov tag bundle`, returning a tag's members, regions and instructions as a manifest of ranges under `tags.bundle-rows`, folded past it, or with their content inlined under the byte budget the call nam
  added: file:line citations joined to the positional population `tags.positional` holds, new text citing `path#symbol` or a blob-pinned line, as NP-17 settles (night pass, point 4)
  added: each role's load set budgeting the `code` slot (night pass, point 3)
  gap added: gap-found-24
  gap added: gap-found-25
  gap added: gap-found-26
=== dFairHearing: units 11 -> 12, gaps 3 -> 4
  added: the scorer factory: one deterministic scorer that re-derives every figure from committed raw outputs, pairs the cases every variant answered and refuses a partial population, extracted from `review_re
  gap added: gap-test-18
=== dDeclaredLoop: units 43 -> 22, gaps 19 -> 10
  reworded: witnesses computed rather than typed by the acting agent (acceptance re-run by the executor, a probe's commands re-run at its pinned SHA, red attribution joined to the verdict)
  left: the named presets and their completeness check, with its pair rules, and each shipped preset loaded with only the core installed, refused only for a value on a 
  left: the preset step added to dGroundRules's reader, so a key the file does not override reads the named preset's value, seen red when a strict-named file with no ov
  left: the charter's preset section, the preset's name and the keys that differ from it, rendered through dOrderedCharter's renderer and seen red on a planted override
  left: policy at govkit intake
  left: the coordination feature: one lease grammar for builds, units and cadence runs, each lease carrying an epoch bumped at every take-over, with run claims migrated
  left: the mailbox per build, its closed set of message kinds checked on write, read and disposed at every transition, shown on the card and kept in the build's transi
  left: live delivery where the harness has it
  left: dependency coordination by the parent's lease, interfaces confirmed at Design's exit, change and landing notices
  left: the build's orientation card at level 1, below the charter, kept as a ref per build on the remote (the truth), cached in the clone by build and object id and sn
  left: the entry step's items: the card's orientation, the three placing items and the claim (PM-9)
  left: the placement predicate and its check, moved from dRankedPlan (RC-8): a disposition for every request, made by `placement` and recorded with its reason, its fac
  left: `actions.free` at the tool call
  left: orientation cost recorded per stage
  left: the mailbox read at every item boundary by `mailbox.reads`, with the `intake` message kind
  left: progress reported by `notify.owner`
  left: a fresh session in the build's worktree recommended until the card-import fixture passes
  left: the card's pointers updated as the build progresses, by `card.pointers`: the latest records by tag, the open forks and the item in flight, so a compacted or fre
  left: what a session does as its window fills, by `context.on-full` and `context.threshold`
  left: a compaction's summary read as a lead, never a source
  left: the items' declarations of the `map` slot and their unfolds
  left: the policy namespaces' purposes, reviewed
  gap left: gap-conc-01
  gap left: gap-conc-02
  gap left: gap-flow-06
  gap left: gap-flow-07
  gap left: gap-orient-01
  gap left: gap-orient-02
  gap left: gap-orient-04
  gap left: gap-orient-06
  gap left: gap-orient-11
```

## [walk-instrument-3] Wave 2's facts, at `9b4386707`

`walk_facts.py` and `since.py` as above. `stage_actors.py` finds the stage items acted by a role no agent plays today:

```python
"""Each stage item whose actor no agent plays today, with the stage's build and whether dBoundRoles, which binds the roles,
is an ancestor of it. An item listed with "no" acts through a role nothing provides before that build starts, unless
its records declare a stand-in.

Usage: python -X utf8 stage_actors.py   (from the worktree root)
It reads flow-steps' item rows (actor, owner), v2's [chain] (stages, parents) and tools/roles/agents/ (today's agents).
It does not read stand-ins; the probe program's are declared in flow-steps' [probe], and the walk names the others.
"""
import pathlib
import re

B = "memory/builds/dClosedLoop/build/"
fs = open(B + "2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md", encoding="utf-8").read()
v2 = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
chain = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
parents, stage_build = {}, {}
names = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| ([^|]+) \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        parents[m.group(1)] = [p.strip() for p in m.group(3).split(",") if p.strip() in names]
        stage_build[m.group(2).strip().lower()] = m.group(1)


def ancestors(b, acc=None):
    acc = set() if acc is None else acc
    for p in parents[b]:
        if p not in acc:
            acc.add(p)
            ancestors(p, acc)
    return acc


today = {re.sub(r"^gov-|\.agent\.md$", "", p.name).replace("-", " ")
         for p in pathlib.Path("tools/roles/agents").glob("*.agent.md")}
ROLE_AGENT = {"spec writer": "spec writer", "builder": "builder", "researcher": "researcher", "reuse scout": "reuse scout",
              "orientation scout": "orienter", "reviewer": "diff reviewer", "skeptic": "skeptic",
              "synthesizer": "synthesizer"}
print(f"today's agents: {', '.join(sorted(today))}")
rows = 0
for m in re.finditer(r"^## \[([a-z-]+)\][^\n]*\n(.*?)(?=^## |\Z)", fs, flags=re.M | re.S):
    step = m.group(1)
    if step not in stage_build:
        continue
    for ln in m.group(2).split("\n"):
        c = [x.strip() for x in ln.strip().strip("|").split(" | ")]
        if not ln.startswith("| `") or len(c) != 7:
            continue
        actor = re.split(r"[,:]", c[1])[0].strip()   # the role, its qualifiers ("one per unit", "under ...") dropped
        if actor in ("command", "executor", "owner", "hook") or ROLE_AGENT.get(actor) in today:
            continue
        sb = stage_build[step]
        bound = "yes" if "dBoundRoles" in ancestors(sb) or sb == "dBoundRoles" else "no"
        rows += 1
        print(f"{step:7} {c[0]:22} actor {actor:12} owner {c[6]:15} stage build {sb:15} after dBoundRoles: {bound}")
print(f"stage items acted by a role no agent plays today: {rows}")
```

Its first run compared whole actor cells, qualifiers included ("builder, one per unit"), and listed 23 items. Matching
each actor's role name before its qualifiers gives the run below.

```text
$ python walk_facts.py dWitnessedBar dBoundRoles dTotalRecall dIndexedDesign dRankedPlan
=== dWitnessedBar · Test · after dDeclaredLoop · before dBoundRoles, dTotalRecall, dMindYourWords, dScopedBuild, dShippedRelease, dTendedCadence · finishes at 79 of 189 · units 22 · gaps 20 (HIGH 6, LOW 3, MED 11) · owns 9 items, 15 policy-keys, 6 record-kinds, 1 systems, 3 tag-namespaces
   1. gate health measured and the reliability bar
   2. bypasses recorded
   3. attribution deciding what blocks
   4. the runner-written verdict the pre-push hook reads
   5. held legs by policy
   6. the peer-node verifier
   7. seen-red records
   8. flake quarantine
   9. the product-test contract with runner adapters
  10. derived pre-commit list and multi-node cost evidence
  11. the gate-leg factory and its conformance gate, every leg declaring the principles it enforces
  12. the `leg`, `check` and `pack` tag namespaces, each leg given a `tag` field beside its free-text name, which stays the join key
  13. retrofit's baseline ledger factory in `tools/lib`, one file per population, each registration declaring its direction (shrink-only debt, append-only h…
  14. the `ratchet` leg pack, with its `populated`, `seed laundering`, rename and merge rows
  15. `test.seed` at every check's registration, seeding only an absent population and recording a failed or dead-probe seed unarmed
  16. gov's own 27 registries converted in place onto the ledger (RF-5), 17 shrink-only debt, 2 append-only histories, 7 declared sets and 1 ceiling, with t…
  17. the seven record and row pins as keyed populations, and the date cutoffs registered as cutoffs
  18. the positional references and IW-1's legacy list registered from dOrderedCharter's keyed lists
  19. the leg's purpose field in `gate-legs.json`, today's 140 legs reviewed: each purpose derived from what the leg carries, or put to the owner (PM-5)
  20. the legacy-homes list dGroundRules declares, converted into a ledger population keyed by conf and key when its factory lands (M4)
  21. a fix pass that keeps its check: its allowance excluding the red leg's own test files and gate script, a change to them routed through the tester's wr…
  22. the `tests=` and `enforces=` edge fields on legs (night pass, point 4)
=== dBoundRoles · Roles · after dDeclaredLoop, dWitnessedBar, dPlacedRequest · before dWellOiledMachine, dShippedRelease · finishes at 113 of 189 · units 34 · gaps 25 (HIGH 11, LOW 4, MED 10) · owns 20 policy-keys, 1 record-kinds, 1 systems, 2 tag-namespaces
   1. the roster sorted by layer: twelve core roles (orientation scout, prompt writer, planner, researcher, reuse scout, architect, spec writer, builder, te…
   2. each role's static instructions as structured fields, every limit paired with its enforcer, a ceiling of tools, write classes and gate legs, and a typ…
   3. the work order rendered per item (the item, its inputs as record fields at their SHAs, its allowance, its return template, its witness), hashed into t…
   4. the prompt writer composing every role's task from the driver's details
   5. the orientation scout composing the card in a sidechain at session start
   6. returns through a schema-forced channel, residual failures retried by `roles.retries`
   7. the role index and agent files beyond every worker's reach, a tree with no index refused, `role-sha` compared at spawn
   8. shell writes held to the allowance
   9. the role-gate arm's field escape explained and closed
  10. the `none` and `review` write classes enforced
  11. `driver.reads`, `prompts.author` and `roles.no-spawn`
  12. every fork resolved by the role that meets it and recorded, or held as `run.on-owner-question` says (LR-3)
  13. prompt-writer calls batched by `prompts.batch`
  14. a return's harness notices persisted with it, by `notices.record`
  15. work-order fields an optional component or an expansion fills (the map's dossiers) declared as optional slots in their three states, and bug classes r…
  16. the orientation scout's return carrying the placement disposition and its reason, the driver recording it and running `placement.check`
  17. the trust mechanism (P29): inputs handed as content, each fact keyed and classed by the executor and re-cut fresh at act launch
  18. each role's trust profile and context temperature declared and rendered (`roles.trust`, `roles.verifier-context`)
  19. the answered-call hook (`roles.answered-calls`)
  20. repairs recorded in returns and filed as asks against the producer's record (`roles.on-contradiction`)
  21. the role files' re-verification orders and protocol pointers replaced by rendered slices
  22. the role-by-step matrix derived from the item declarations and joined both ways
  23. role metrics per role and item into the value ledger, answered calls from the hook's records and the other classes from runlog's extractor, accepted a…
  24. the `role` and `field` tag namespaces
  25. the role static block carried once per spawn
  26. the shapes, extending each `tools/roles/workflows.toml` entry with its kind (`single`, `per-unit`, `panel`, `twin`, and `experiment`, whose cases, var…
  27. the work order's memory slices, code-notes slot and legacy slot, each under its own budget and its own answer (systems `[cross]`), the legacy slot in …
  28. the work order's `map` slot for the roles `memory.project-map` names, with the unfolds each item declares (PM-6), rendering "not installed" until dTot…
  29. the orientation scout composing the card's map cell
  30. the answered-call hook's range matching, the excerpt keys and a repair's carry, designed in its own unit specs (RC-7)
  31. the tester agent, absent today, with its allowance (scratch, and the browser where the harness has it), and the `probe` outcome on every role's return…
  32. owner questions asked live while the build is attended, best effort recorded once the wait passes (night pass, point 1)
  33. the `code` slot rendered per item from its declared seed: the seed's definitions with their ranges, their callers, callees and tests and their kit's s…
  34. the work order selecting instruction units by `feature.*` once dTotalRecall arms that selector, and the code-notes slot filled from the tag's bundle (…
=== dTotalRecall · Memory · after dDeclaredLoop, dWitnessedBar, dPlacedRequest · before dWellOiledMachine, dRankedPlan, dIndexedDesign, dShippedRelease · finishes at 119 of 189 · units 40 · gaps 34 (HIGH 9, LOW 8, MED 17) · owns 4 items, 25 policy-keys, 16 record-kinds, 3 systems, 5 tag-namespaces
   1. the memory contract: the record-kind registry (per kind: tag, layer, home, id rule, schema, writer, readers, lifecycle, check), templates and checks g…
   2. the one `record` write command, which mints ids under the build's claim or lease, is idempotent and content-addressed, renders templates and refuses i…
   3. for every filer outside a build, ids minted under an ask family's counter ref advanced by a `--force-with-lease` push, the claimant key on every claim…
   4. the build README's declared front-matter schema, with unknown keys refused, `node`, `roster` and `streams` derived, a generated routing region by purp…
   5. the slug and id grammar exported once and read by every slug and id reader (`builds.slug-words`, `builds.slug-style`, `builds.slug-date`), proven by f…
   6. typed relations (`depends-on`, `patches`, `amends`, `supersedes`, `implements`), inverted, checked both ways and rendered as the relation graph
   7. the ask kind's acceptance at filing (`asks.acceptance`), extending backlog.py's V14
   8. decisions split by kind: reuse entries as level-3 instruction units beside their dossiers and under `memory/map/conventions/`, proposed with their bui…
   9. the reuse scout's house index in M1c's shape (a digest of symbols, callers, dossiers and reuse entries, with the sketch and census steps), delivered t…
  10. `reuse_lookup.py` retired with its readers rewritten, and memory-recall narrowed to a record finder
  11. the core `code` record (night pass, point 3), replacing the optional symbols and callers: files, definitions with their ranges and body hashes, import…
  12. the `gov:note` grammar and `gov:feature` anchors checked both ways with reuse entries, the generated annotation index and its resolve check (`annotati…
  13. gotchas handed by write set
  14. the generated views: README routing, the relation graph, the decisions' holds-now view and the reuse view
  15. the research view, over the research-return kind
  16. the `section`, `record`, `feature` and `class` extractors, `record find`, its last line naming the total past 40 rows, and `record show` over the one …
  17. the `annotations` leg, the marker query with the map's index rows where the map is installed (AN-1), and the read hook on shell reads too (AN-2)
  18. retrofit's `baseline` and `census` record kinds, the `origin` field, and the `adopt` program the core's own command runs where distribution is absent:…
  19. the origin check, re-derived from history, `origin` among the fields every slice renders, and the reuse digest's ranking
  20. the progress cell
  21. the annotation resolve check's legacy and the untouched long blocks registered as ledger populations
  22. the `marker` namespace over the existing `gov:` words
  23. derived anchors suffixed for a repeated heading
  24. the shape-run kind
  25. the acceptance re-measure counted over every read channel
  26. the shared extraction primitive in `tools/lib` (LX-2), reading the working tree, the index or a revision, with the shell and JavaScript tokenizers mov…
  27. and the dated backfill of `kind: research-return` over the existing returns, 72 at `1b759b620`
  28. the level-0 project map (PM-1, PM-2): its renderer and `gov map`, derived from the one index and cached beside it, at most `memory.map-budget` and deg…
  29. the three-way completeness check and the `map` leg pack
  30. the atlas re-rendered from the same node table
  31. the record-kind registry's purpose field, today's kinds, and the namespaces and chain builds whose fields dOrderedCharter adds, reviewed as `memory.ma…
  32. the replay with the map and without at its first unit, so a losing map is never built, and a loss routed: the slot's "not installed" made terminal, dW…
  33. `gov map code` and `gov code show`, `callers`, `tests` and `where`, `git grep` the engine of `where` and the floor for a language with no extractor, t…
  34. the enrichment workflow: purposes derived first from docstrings and headers, an agent's pass for the rest as `memory.code-enrich` says, each keyed to …
  35. the replay's losing test extended to code: a unit's files read and its lookups counted, with the `code` slot and without it (night pass, point 3)
  36. extractors emitting typed edges from annotations, front matter, dossiers and decision rows, `decides` written on decision rows, and the span rule: a d…
  37. the region-parser factory in `tools/lib`, today's five region parsers re-pointed to it (night pass, point 4)
  38. the dossier's header becoming the feature node and its prose moving into units and records, as NP-16 settles (night pass, point 4)
  39. the `feature` namespace armed as an instruction selector when it registers, as NP-13 settles (night pass, point 4)
  40. the ctags extractor pack, opted into by `memory.code-languages: builtin+ctags` or `ctags`: definitions and their ranges for every language the built-i…
=== dIndexedDesign · Design · after dDeclaredLoop, dTotalRecall, dKeptSession · before dScopedBuild, dTendedCadence · finishes at 131 of 189 · units 12 · gaps 10 (HIGH 4, LOW 2, MED 4) · owns 10 items, 4 policy-keys, 10 record-kinds
   1. the derived-READY hand-off
   2. the design index
   3. design review by policy, its opt-in, effort and audit guard, the stage-exit recommendation being dDeclaredLoop's (AF-1)
   4. reuse and alternatives backed by recorded probes
   5. the research harness, built on the `experiment` shape once dBoundRoles registers it, and run as today until then (night pass, point 2)
   6. agreement and tier checks
   7. the spec measured, recommendations emitted, and the spec redesigned as a structured, tagged contract
   8. the feature level (build, features, units) with each feature's interfaces declared structurally, two-level re-entry by `design.reentry`, additive-vers…
   9. spec sections named by tag across tiers
  10. the playbook record kind: dScriptedRepeat's canon, its declaration block, pieces and sets identified by hash, amendment by proposal, and `check-playbo…
  11. the playbook set record and its set check, registered at Test's leg-pack point (night pass, point 1)
  12. the structured spec declaring `implements=` and `decides=` edges, and `design.seams` reading a tag's bundle (night pass, point 4)
=== dRankedPlan · Plan · after dDeclaredLoop, dTotalRecall · before dTendedCadence · finishes at 132 of 189 · units 13 · gaps 10 (HIGH 5, LOW 1, MED 4) · owns 9 items, 6 policy-keys, 3 record-kinds
   1. priority beside `parents:` and the generated plan view
   2. the planner and triager role and Plan workflow
   3. rule-based triage
   4. dormancy disposal
   5. the live-build mapping carried out
   6. Plan Review
   7. kickoff offering the next item and attended briefs gated
   8. the full kickoff only where `kickoff.runs` says
   9. the session's intake log, which `entry.intake`'s prompt-submit hook writes (dWellOiledMachine's, PM-9), read as the request's ratification by `plan.ra…
  10. until that hook and the intake kind land, `plan.exit` under `plan.ratification: request` falls back to dDeclaredLoop's owner gate, held for the owner'…
  11. each role item's memory read set sized at Plan, as `id#tag` keys
  12. `plan.record` declaring the probes owed before Design (night pass, point 2)
  13. the plan record's intent fields: the affected systems derived from the `code` record and checked, and the open questions as fork tags (night pass, poi…
$ python since.py beda01950 dWitnessedBar dBoundRoles dTotalRecall dIndexedDesign dRankedPlan
=== dWitnessedBar: units 20 -> 22, gaps 19 -> 20
  added: a fix pass that keeps its check: its allowance excluding the red leg's own test files and gate script, a change to them routed through the tester's wrong-spec judgment to Design as a new unit, its arm
  added: the `tests=` and `enforces=` edge fields on legs (night pass, point 4)
  gap added: gap-test-19
=== dBoundRoles: units 30 -> 34, gaps 23 -> 25
  reworded: the shapes, extending each `tools/roles/workflows.toml` entry with its kind (`single`, `per-unit`, `panel`, `twin`, and `experiment`, whose cases, variants, bounded fan, scorer or blind judge and re-r
  added: the tester agent, absent today, with its allowance (scratch, and the browser where the harness has it), and the `probe` outcome on every role's return template (night pass, point 2)
  added: owner questions asked live while the build is attended, best effort recorded once the wait passes (night pass, point 1)
  added: the `code` slot rendered per item from its declared seed: the seed's definitions with their ranges, their callers, callees and tests and their kit's siblings, as ranges under `memory.code-budget`, for
  added: the work order selecting instruction units by `feature.*` once dTotalRecall arms that selector, and the code-notes slot filled from the tag's bundle (night pass, point 4)
  gap added: gap-roles-21
  gap added: gap-roles-22
=== dTotalRecall: units 32 -> 40, gaps 27 -> 34
  added: the core `code` record (night pass, point 3), replacing the optional symbols and callers: files, definitions with their ranges and body hashes, imports, every Python definition with import-aware calls
  added: `gov map code` and `gov code show`, `callers`, `tests` and `where`, `git grep` the engine of `where` and the floor for a language with no extractor, the map's level 0 holding one counted `code` line (
  added: the enrichment workflow: purposes derived first from docstrings and headers, an agent's pass for the rest as `memory.code-enrich` says, each keyed to its definition's body hash and stale when the hash
  added: the replay's losing test extended to code: a unit's files read and its lookups counted, with the `code` slot and without it (night pass, point 3)
  added: extractors emitting typed edges from annotations, front matter, dossiers and decision rows, `decides` written on decision rows, and the span rule: a definition's extent where one derives, `gov:end <ta
  added: the region-parser factory in `tools/lib`, today's five region parsers re-pointed to it (night pass, point 4)
  added: the dossier's header becoming the feature node and its prose moving into units and records, as NP-16 settles (night pass, point 4)
  added: the `feature` namespace armed as an instruction selector when it registers, as NP-13 settles (night pass, point 4)
  added: the ctags extractor pack, opted into by `memory.code-languages: builtin+ctags` or `ctags`: definitions and their ranges for every language the built-in extractors do not read, the record naming its ex
  left: the caller map: every Python definition, import-aware calls, shell and JavaScript edges under the ambiguity test, cross-language invocation edges, freshness-che
  gap added: gap-mem-28
  gap added: gap-mem-29
  gap added: gap-mem-30
  gap added: gap-mem-31
  gap added: gap-mem-32
  gap added: gap-mem-33
  gap added: gap-mem-34
=== dIndexedDesign: units 9 -> 12, gaps 9 -> 10
  added: the research harness, built on the `experiment` shape once dBoundRoles registers it, and run as today until then (night pass, point 2)
  added: the playbook record kind: dScriptedRepeat's canon, its declaration block, pieces and sets identified by hash, amendment by proposal, and `check-playbook` as Design's pack (night pass, point 1)
  added: the playbook set record and its set check, registered at Test's leg-pack point (night pass, point 1)
  added: the structured spec declaring `implements=` and `decides=` edges, and `design.seams` reading a tag's bundle (night pass, point 4)
  left: the research harness
  gap added: gap-flow-17
=== dRankedPlan: units 11 -> 13, gaps 9 -> 10
  added: `plan.record` declaring the probes owed before Design (night pass, point 2)
  added: the plan record's intent fields: the affected systems derived from the `code` record and checked, and the open questions as fork tags (night pass, point 6)
  gap added: gap-plan-08
$ python stage_actors.py
today's agents: builder, diff reviewer, orienter, researcher, reuse scout, session, skeptic, spec reviewer, spec writer, synthesizer
plan    `plan.triage-judge`    actor planner      owner dRankedPlan     stage build dRankedPlan     after dBoundRoles: no
plan    `plan.record`          actor planner      owner dRankedPlan     stage build dRankedPlan     after dBoundRoles: no
plan    `plan.reason`          actor planner      owner dDeclaredLoop   stage build dRankedPlan     after dBoundRoles: no
design  `design.inventory`     actor architect    owner dIndexedDesign  stage build dIndexedDesign  after dBoundRoles: no
design  `design.decompose`     actor architect    owner dIndexedDesign  stage build dIndexedDesign  after dBoundRoles: no
design  `design.reason`        actor architect    owner dDeclaredLoop   stage build dIndexedDesign  after dBoundRoles: no
test    `test.attribute`       actor tester       owner dWitnessedBar   stage build dWitnessedBar   after dBoundRoles: no
test    `test.reason`          actor tester       owner dDeclaredLoop   stage build dWitnessedBar   after dBoundRoles: no
stage items acted by a role no agent plays today: 8
```

## [walk-instrument-4] Wave 3's facts, at `7788ac269`

`walk_facts.py`, `since.py` and `critical_path.py` as above, the last now counting twenty builds. `leaves.py` finds the
builds no build waits on, and the fates rows each one owns:

```python
"""The chain builds no build waits on, and the fates table's destinations each one owns. A leaf other than the
convergence build lands outside convergence's exit check, which joins the fates table.

Usage: python -X utf8 leaves.py   (from the worktree root)
"""
import re

B = "memory/builds/dClosedLoop/build/"
v2 = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
fates = open(B + "2026-10-18-build-PLAY-dClosedLoop-1-fates.md", encoding="utf-8").read()
chain = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
names = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
parents = {}
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| ([^|]+) \| .+ \| [^|]+ \|$", ln)
    if m:
        parents[m.group(1)] = [p.strip() for p in m.group(2).split(",") if p.strip() in names]
children = {b: [c for c in parents if b in parents[c]] for b in parents}
table = fates.split("## [table]", 1)[1].split("\n## ", 1)[0]
for b in sorted(b for b, cs in children.items() if not cs):
    rows = [ln for ln in table.split("\n") if ln.startswith("| ") and re.search(rf"\b{b}\b", ln.split(" | ")[4] if
                                                                                   ln.count(" | ") >= 5 else "")]
    print(f"leaf {b}: {len(rows)} fates rows go to it")
    for ln in rows:
        c = [x.strip() for x in ln.strip().strip("|").split(" | ")]
        print(f"  {c[0]} · {c[1][:50]} · {c[3]} · {c[4][:110]}")
print(f"builds no build waits on: {sum(1 for cs in children.values() if not cs)} of {len(children)}")
```

```text
$ python walk_facts.py dWellOiledMachine dScopedBuild dTendedCadence dMindYourWords
=== dWellOiledMachine · Runtime · after dBoundRoles, dTotalRecall, dKeptSession · before dMindYourWords, dScopedBuild, dShippedRelease, dTendedCadence · finishes at 128 of 171 · units 31 · gaps 35 (HIGH 13, LOW 5, MED 17) · owns 7 items, 10 points, 18 policy-keys, 7 record-kinds, 2 tag-namespaces
   1. the platform spike first: a role-typed Workflow agent run inside a headless act session, with the headless backend measured beside it
   2. the `next` verb over the loop kit's position function, the `next —` micro-format, and the check that every declared command ends with one or declares …
   3. the owner's pause, resume, withdraw and supersede through the guarded command, mapped onto unattended's verbs, and attend and unattend, each writing a…
   4. the prompt-submit hook writing each owner prompt verbatim to the session's intake log, its secrets redacted and its size capped (`entry.intake`, PM-9)
   5. Plan's ratification and the placement dispositions re-pointed to the intake record, RC-9's fallback drained per harness, only where an adapter's capab…
   6. the supervisor: `resume-tick.sh` grown, started and restarted by the node tick, the executor launched where `run.host` says, its liveness its build le…
   7. act binding and the epoch check at the Workflow, Agent and shell call, decided in the dispatcher's PermissionRequest entry, with in-script spawns decl…
   8. the persisted-return store, keyed per spawn site, and the shared deferral block
   9. agent slots reserved under agent-cap's cap
  10. the one enforcement surface: the kits' fragments as packs, one dispatcher entry per event, ask rules on gated tools that only the dispatcher's Permiss…
  11. workspaces by `build.worktree`, the commit queue, integration before release and the sweep
  12. sessions bound on every source, a resume that delivers no card diagnosed and closed, the compact hook re-injecting the build's current card, never the…
  13. the scheduler's host adapters and per-period cadence witnesses
  14. harness adapters with capability tables
  15. the node registry's runtime facts
  16. the journal grammar moved into the core, and its retention by `runtime.journal`
  17. the grant enforced on every adapter row, and the secret value scan at every boundary that publishes
  18. event waits woken by their record, keyed by the record's id and the build, an owner request on an unleased build woken the same way, and the sweep tha…
  19. act binding against the resolved shape's digest, and the journal reconciled against it, writing each non-review act's shape-run row
  20. the `hook` and `point` tag namespaces
  21. the hook-message and harness-prompt templates
  22. hook and point purposes, reviewed
  23. the session-start hook loading the set `memory.default-load` names, the card and the map by default in the owner's session, at startup, at resume and …
  24. the journal's count of map reads outside a slice
  25. the supervisor the only driver in every mode, the owner's session its client, which hosts the driver only before this build lands or if its platform s…
  26. the `step —` announcement before each act while attended, and once when attendance begins, rendered from `next` and the item's declaration, never type…
  27. intake for a prompt that reaches no owner session, through the mailbox's `intake` message or a cadence filer (night pass, point 1)
  28. the unattended kit dissolved into the loop kit and the runtime's own kit: its hooks repacked, its supervisor seam taken, `/unattended` a client of `ru…
  29. a measured `browser` row in each harness adapter's capability table, and the `visual.capture` command adapter: the pinned tree served, the cache buste…
  30. act binding and shape-run rows for an experiment's acts (night pass, point 2)
  31. a hook pack's refusal text, naming its rule and its remedy, declared in the pack's contract and checked at registration (night pass, point 6)
=== dScopedBuild · Build · after dIndexedDesign, dWitnessedBar, dWellOiledMachine, dFurnishedOrders · before dConvergedCharter · finishes at 143 of 171 · units 11 · gaps 7 (HIGH 3, LOW 1, MED 3) · owns 9 items, 6 policy-keys, 2 record-kinds
   1. one exit contract with a history-derived base, refusing a build's exit while a core red its own commits introduced stands
   2. built specs frozen, every closing-review finding disposed as new units by `review.findings`
   3. scope at the push
   4. the closing review recorded
   5. a write gate reading derived state
   6. the checklist witnessed
   7. the core checks run by the executor at Build's exit
   8. `build.unit-pass` and `build.scope` draining the legacy a unit touches, in hunks under `retrofit.drain-cap`, and claiming the baselined map keys its w…
   9. the touch join as `build.scope`'s one check, graded by its value, over the union of `git diff-tree -U0 --no-merges -M` across the unit's own commits, …
  10. a red-first reproduction, a `reproduction` probe, before a patch build's fix when the build comes from a bug report (night pass, point 2)
  11. a playbook's pieces built as units with piece records joined by hash, and a proposal to amend the playbook filed as an ask (night pass, point 1)
=== dTendedCadence · Maintain · after dWitnessedBar, dRankedPlan, dWellOiledMachine, dIndexedDesign, dFurnishedOrders · before dCalibratedLens · finishes at 146 of 171 · units 14 · gaps 12 (HIGH 2, LOW 4, MED 6) · owns 7 items, 15 policy-keys, 2 record-kinds
   1. the Maintain run as its step checklist on the flow's executor, never a recipe-mode playbook
   2. the cadence, on Runtime's hosts
   3. the safe-fix set
   4. detectors with owners
   5. map freshness
   6. the maintenance record
   7. a detector for the memory's dead pointers, owned by Maintain, absorbing `check-dead-paths.sh` and keeping its merge-bar leg at Test's leg-pack point (…
   8. Maintain and the Loop Review delivered as cadence steps of the observability expansion, detectors registered by layer, patch intakes rendered from key…
   9. `maintain.retrofit-heat`, filing each period's sweep as a patch build under `retrofit.cadence: hot-first`'s standing ask and sweep asks only under `of…
  10. the maintainer's definition, Maintain's filings, registered through dBoundRoles's layer contract
  11. a cyclic playbook's cadence item, filing `repeat` intakes (night pass, point 1)
  12. a detector for bundle members whose code changed while their head line did not (night pass, point 4)
  13. the recurring security review, a cadence item running dFairHearing's security lens over the landed tree as `maintain.security-review` says, weekly by …
  14. readings tiered by their deviation from their pins under `maintain.tiers: bands`, to log, to diagnose read-only or to act within `maintain.fixes` (NP-…
=== dMindYourWords · Lexicon · after dWellOiledMachine, dWitnessedBar, dLinkedLibrary, dFurnishedOrders · before none · finishes at 145 of 171 · units 17 · gaps 10 (HIGH 3, LOW 3, MED 4) · owns 5 policy-keys, 1 record-kinds
   1. the definition classes (conforming, forced, out of scope, not a name, debt), with only debt counted against the shrink-only pin (`lexicon.pin`), held …
   2. forced names recognised by what forces them (`lexicon.forced`): packs keyed by base member, base prefix and host namespace, applied only where the sit…
   3. gov's own contract-forced names declared in a table the instruction write path owns, the code carrying at most a pointer a check resolves (LX-3), with…
   4. override markers verified against the packs
   5. a reasoned site suppression as the owner's counted fallback
   6. `--suggest` made forced-aware
   7. the packs, generated per host kit (`inspect` per Python minor, wheel AST, pluggy hookspecs, `.d.ts`), shell hosts curated, each with its kit, version …
   8. packs detected from the import census and manifests and declared by the owner, custom packs included (`lexicon.packs`)
   9. enforcement: the work order's vocabulary slice and forced-aware answers, staged definitions checked at commit (`lexicon.at-commit`), and the branch's …
  10. drift beyond verbs (`lexicon.drift`): one verb per declared family per object, the families declared by the packs the stack census selects for the kit…
  11. the vocabulary changed only through the instruction write path, with `ratified` replaced by its record and the `init` row re-justified
  12. one extraction primitive in `tools/lib`, which dTotalRecall builds and the map and the lexicon each call over the working tree, the index or a revisio…
  13. the tag-name vocabulary check, registered at the instruction layer's name-check point that dOrderedCharter builds
  14. the kit's defects fixed: repeated block headers refused, IIFE values and properties ungraded, the dead modes, and the Skill, conf and README reconcile…
  15. records kept out by the path selector
  16. the two lexicon drift signals as the lexicon's own leg pack, registered at Test's leg-pack point
  17. the overloaded terms settled: attended as a session kind and as a mode, playbook as the charter renderer and as playbook mode, and baseline as retrofi…
$ python since.py beda01950 dWellOiledMachine dScopedBuild dTendedCadence dMindYourWords
=== dWellOiledMachine: units 24 -> 31, gaps 9 -> 15
  reworded: the owner's pause, resume, withdraw and supersede through the guarded command, mapped onto unattended's verbs, and attend and unattend, each writing an `attendance override` record scoped by `attendan
  reworded: sessions bound on every source, a resume that delivers no card diagnosed and closed, the compact hook re-injecting the build's current card, never the kickoff's, the PreCompact flush and the keep-list
  reworded: the session-start hook loading the set `memory.default-load` names, the card and the map by default in the owner's session, at startup, at resume and at a compaction, ending with `next`'s line compute
  added: the supervisor the only driver in every mode, the owner's session its client, which hosts the driver only before this build lands or if its platform spike fails, under its owner binding, each role act
  added: the `step —` announcement before each act while attended, and once when attendance begins, rendered from `next` and the item's declaration, never typed by a model (night pass, point 1)
  added: intake for a prompt that reaches no owner session, through the mailbox's `intake` message or a cadence filer (night pass, point 1)
  added: the unattended kit dissolved into the loop kit and the runtime's own kit: its hooks repacked, its supervisor seam taken, `/unattended` a client of `run` until dConvergedCharter retires it (night pass,
  added: a measured `browser` row in each harness adapter's capability table, and the `visual.capture` command adapter: the pinned tree served, the cache busted, the declared viewports taken, screenshots kept 
  added: act binding and shape-run rows for an experiment's acts (night pass, point 2)
  added: a hook pack's refusal text, naming its rule and its remedy, declared in the pack's contract and checked at registration (night pass, point 6)
  gap added: gap-orient-16
  gap added: gap-orient-17
  gap added: gap-orient-18
  gap added: gap-rt-22
  gap added: gap-rt-23
  gap added: gap-rt-24
=== dScopedBuild: units 9 -> 11, gaps 7 -> 7
  added: a red-first reproduction, a `reproduction` probe, before a patch build's fix when the build comes from a bug report (night pass, point 2)
  added: a playbook's pieces built as units with piece records joined by hash, and a proposal to amend the playbook filed as an ask (night pass, point 1)
=== dTendedCadence: units 10 -> 14, gaps 10 -> 12
  reworded: a detector for the memory's dead pointers, owned by Maintain, absorbing `check-dead-paths.sh` and keeping its merge-bar leg at Test's leg-pack point (NP-22)
  added: a cyclic playbook's cadence item, filing `repeat` intakes (night pass, point 1)
  added: a detector for bundle members whose code changed while their head line did not (night pass, point 4)
  added: the recurring security review, a cadence item running dFairHearing's security lens over the landed tree as `maintain.security-review` says, weekly by default (NP-19)
  added: readings tiered by their deviation from their pins under `maintain.tiers: bands`, to log, to diagnose read-only or to act within `maintain.fixes` (NP-21)
  gap added: gap-maint-12
  gap added: gap-maint-13
=== dMindYourWords: units 16 -> 17, gaps 9 -> 10
  added: the overloaded terms settled: attended as a session kind and as a mode, playbook as the charter renderer and as playbook mode, and baseline as retrofit's debt and as a measured reference (night pass, 
  gap added: gap-lex-09
$ python critical_path.py
critical path: 171 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dLinkedLibrary > dIndexedDesign > dTendedCadence > dCalibratedLens > dConvergedCharter
each build's earliest finish, in units: dGroundRules 8, dFairHearing 20, dOrderedCharter 35, dDeclaredLoop 57, dPlacedRequest 64, dWitnessedBar 80, dKeptSession 82, dBoundRoles 96, dTotalRecall 97, dRankedPlan 110, dFurnishedOrders 114, dLinkedLibrary 120, dWellOiledMachine 128, dIndexedDesign 132, dScopedBuild 143, dMindYourWords 145, dTendedCadence 146, dShippedRelease 149, dCalibratedLens 157, dConvergedCharter 171
$ python leaves.py
leaf dConvergedCharter: 15 fates rows go to it
  roles · `check_roles.py` · RESHAPED · role-by-step matrix joined both ways (dFurnishedOrders); policy reader re-pointed (dConvergedCharter)
  roles · `house/policy.toml` · MERGED · into `.governance/policy.toml` (dConvergedCharter); on dGroundRules's legacy list until then
  workflows · `REVIEW-PROTOCOL.template.md` · RESHAPED · corrected by dFairHearing, then a rendered view (dConvergedCharter)
  memory-tree · `transition_audit.py` · STAYS · an append-only history population; `read_modes` re-pointed (dConvergedCharter)
  memory-tree · method, spec and annotation templates · RESHAPED · spec as a tagged contract (dIndexedDesign); guides as views (dConvergedCharter)
  unattended · `check-unattended` · RETIRED · none: it gates the unattended kit itself, which dissolves at convergence (dConvergedCharter)
  unattended · `check-arms-groups` · RETIRED · none: it lints the kit's own self-test file, which dissolves with the kit (dConvergedCharter)
  unattended · drift and runlog calls, `read_policy_key` · RESHAPED · optional slots (dOrderedCharter); re-pointed (dConvergedCharter)
  unattended · guide templates (PROTOCOL, VERBS, STOPS, ASKS) · RESHAPED · rendered views of the loop's checklists (dConvergedCharter)
  unattended · the `/unattended` Skill · RETIRED · a client of `run` until dConvergedCharter retires it, unattended being the default state (NP-4)
  run-gates · held halves, WSL, selftests, profile, ceilings · STAYS · `held_halves` re-pointed (dConvergedCharter)
  skills · rendered Skills, six of seven, `/unattended` apart · RESHAPED · thin level-4 entries; `/build` becomes a client of `next` and `run` (dConvergedCharter, with dWellOiledMachine
  .githooks · pre-push · RESHAPED · reads the runner verdict; trusted copy; policy re-point (dWitnessedBar, dWellOiledMachine, dConvergedCharter)
  .githooks · `gate-env.sh` · RESHAPED · owner keys folded (dConvergedCharter); mechanics stay
  guides · hand-written guides · RETIRED · rendered views; rationale moves to `help` fields (dConvergedCharter)
leaf dMindYourWords: 4 fates rows go to it
  lexicon · `lexicon.py` gate and pin · RESHAPED · definition classes, keyed debt ledger, forced packs (dMindYourWords)
  lexicon · `canon`, `scaffold_lexicon` · RESHAPED · noun canon seeded and frozen; packs chosen by census (dMindYourWords)
  lexicon · its two drift signals · MERGED · the lexicon's leg pack (dMindYourWords)
  drift-audit · seven gateable signals · RESHAPED · five core legs and two lexicon legs (dTendedCadence gap-maint-09; dMindYourWords)
builds no build waits on: 2 of 20
```
