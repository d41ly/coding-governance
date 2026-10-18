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
