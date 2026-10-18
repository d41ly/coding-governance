# NP-24 priced: a split of dDeclaredLoop, and a lighter dCalibratedLens

**Serves:** research PLAY-dClosedLoop-1

The owner's answer to NP-24, 2026-10-18, was "Price it now (Recommended)"
(`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md` `[answers]`). This record prices both changes against the
chain at `1d32760f3`, the commit that folded the answers, and parks the choice as SP-1 and SP-2. At that commit the
critical path is 214 units, `1d32760f3`'s v2 `[chain]` read by the script below.

## [method] How a split is priced

- **Units.** A build's units are its planned-units clauses, split on "; " as the design map and the critical-path
  script count them. A build starts when every parent has landed.
- **A split** replaces dDeclaredLoop by two or three parts, each holding a set of its clauses. A later build waits for
  every part that holds a clause it needs.
- **What a later build needs** joins two readings:
  - the reconciliation gate's mechanical one: backticked cites, stage items, keys read, and routes into the breakpoint
    program (`node_users.py`, kept in the night-pass instruments record);
  - a reading of the structural needs the gate cannot see, because they are spelled in plain words, stated clause by
    clause in `[classification]`.
- **The losing test.** A split loses if dWitnessedBar, the spine's successor on the critical path, waits for a moved
  part.
- **What it does not price.** A new build's fixed cost, which no unit counts: its kickoff, README and roster, its specs
  and their audit, a closing review and a landing.

## [classification] dDeclaredLoop's 47 clauses, by who needs them

Clause numbers are those `chain_clauses.py` prints for dDeclaredLoop's row at `1d32760f3`.

- **The spine's core (19): clauses 1, 5, 6, 7, 8, 10, 15, 17, 20, 23, 30, 31, 32, 33, 34, 35, 36, 37 and 42.** Every later build rests on these: the loop kit, the
  guard and floor, transitions, stage claims and coverage, the witness-class rule, the factories, the position engine,
  claims, item declarations, the transition tables, the failure route, terminal states, the disposition set, computed
  witnesses and the tag namespaces. The follow-up rounds join them, since `review.dispose`, a core item, reads
  `review.follow-up`.
- **What dWitnessedBar's stage needs (3): clauses 40, 41 and 43.** These are the breakpoint mechanism.
  `test.recommend` and `test.reason` are Test's stage items, by the gate's stage rule, and they run through the
  breakpoints and the program's items.
- **Needed by dTotalRecall or dBoundRoles (7).** Both builds start as dWitnessedBar lands.

| Clause | The unit | Who needs it, and why |
|---|---|---|
| 11 | the coordination feature: one lease grammar for builds, units and cadence runs, each … | dTotalRecall cites `leases.offline` and mints ids under a claim or lease; dRankedPlan and dScopedBuild read lease keys |
| 16 | the build's orientation card at level 1, below the charter, kept as a ref per build on … | the card: `entry.orient` composes it, and dWellOiledMachine's session-start load reads it |
| 18 | the entry step's items: the card's orientation, the three placing items and the claim … | dBoundRoles renders every item's work order, the entry items' included; dRankedPlan follows entry |
| 19 | the placement predicate and its check, moved from dRankedPlan (RC-8): a disposition … | dBoundRoles cites `placement.check` |
| 38 | the items' declarations of the `map` slot and their unfolds | dBoundRoles's work order carries the `map` slot each item declares; dTotalRecall's replay reads it |
| 46 | the probe program (`probe.trigger`, `probe.pin`, `probe.design`, `probe.experiment`, … | dBoundRoles cites the `probe` kind, each role's return gaining the probe outcome; dRankedPlan reads `probe.observations` |
| 47 | each item's declared code seed: its write set, its scope paths or its question's paths … | dBoundRoles computes each item's `code` slot from its declared seed |

- **Needed only by builds that start later (18).** Each later build starts after dTotalRecall or dBoundRoles
  lands.

| Clause | The unit | Who needs it, and why |
|---|---|---|
| 2 | the named presets and their completeness check, with its pair rules, and each shipped … | the named presets: until they land a key reads its catalogue default, so only `standard` works |
| 3 | the preset step added to dGroundRules's reader, so a key the file does not override … | the preset step in the reader, with them |
| 4 | the charter's preset section, the preset's name and the keys that differ from it, … | the charter's preset section, with them |
| 9 | policy at govkit intake | policy at govkit intake: dShippedRelease |
| 12 | the mailbox per build, its closed set of message kinds checked on write, read and … | the mailbox: dWellOiledMachine's live delivery, dScopedBuild and dShippedRelease |
| 13 | live delivery where the harness has it | live delivery: dWellOiledMachine |
| 14 | dependency coordination by the parent's lease, interfaces confirmed at Design's exit, … | dependency coordination: dIndexedDesign, dScopedBuild and dShippedRelease |
| 21 | `actions.free` at the tool call | `actions.free` at the tool call: dWellOiledMachine's hooks |
| 22 | orientation cost recorded per stage | orientation cost per stage: dCalibratedLens |
| 24 | the mailbox read at every item boundary by `mailbox.reads`, with the `intake` message kind | `mailbox.reads`: dWellOiledMachine |
| 25 | progress reported by `notify.owner` | `notify.owner`: dWellOiledMachine's notification adapters |
| 26 | a fresh session in the build's worktree recommended until the card-import fixture passes | the fresh-session recommendation: dWellOiledMachine |
| 27 | the card's pointers updated as the build progresses, by `card.pointers`: the latest … | `card.pointers`: dWellOiledMachine's replay |
| 28 | what a session does as its window fills, by `context.on-full` and `context.threshold` | `context.on-full`: dWellOiledMachine |
| 29 | a compaction's summary read as a lead, never a source | a compaction summary read as a lead: dWellOiledMachine |
| 39 | the policy namespaces' purposes, reviewed | the policy namespaces' purposes, reviewed: no later build |
| 44 | the attendance rule: `attendance` places owner breakpoints and has owner questions … | the attendance rule: dWellOiledMachine's announcement and attendance override |
| 45 | the `repeat` disposition in the placement set and its `none` row in the transition … | `repeat`: dIndexedDesign's seventh input and dTendedCadence's cyclic playbooks |

## [results] The candidates, at `1d32760f3`

**As asked.** The owner was asked from the first run, as captured:

```text
baseline: 214 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
S1, two builds: the late parts leave: dDeclaredLoop 27, dDeclaredLoop-B 20 · 194 units (-20), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
  dDeclaredLoop-B lands at 82, dWitnessedBar at 84
S2, two builds: everything dWitnessedBar does not need leaves: dDeclaredLoop 21, dDeclaredLoop-B 26 · 192 units (-22), dGroundRules > dOrderedCharter > dDeclaredLoop > dDeclaredLoop-B > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
  dDeclaredLoop-B lands at 82, dWitnessedBar at 78
S3, three builds: the early and the late parts each leave: dDeclaredLoop 21, dDeclaredLoop-B 6, dDeclaredLoop-C 20 · 188 units (-26), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
  dDeclaredLoop-B lands at 62, dWitnessedBar at 78
  dDeclaredLoop-C lands at 76, dWitnessedBar at 78
dConvergedCharter's parents land at: dCalibratedLens 200, dShippedRelease 196, dScopedBuild 186
lightening dCalibratedLens by k units saves min(k, 4): the next parent, dShippedRelease, lands only 4 units before dCalibratedLens does
L1, dCalibratedLens split: the Loop Review's 4 after dTendedCadence, the other 7 after dWellOiledMachine · 210 units (-4), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dShippedRelease > dConvergedCharter
S1 with L1: 190 units (-24), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dShippedRelease > dConvergedCharter
```

**As corrected.** Folding the owner's S3 found two clauses placed against the gate's own rules:
  - clause 16 moved from the late parts to the early ones: `entry.orient`, an entry item, composes the card;
  - clause 42 moved from the late parts to the core: `review.dispose`, a core item, reads `review.follow-up`.

The run after both corrections, as captured:

```text
baseline: 214 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
corrected while folding: clause 16 moved from the late parts to the early ones: `entry.orient`, an entry item, composes the card
corrected while folding: clause 42 moved from the late parts to the core: `review.dispose`, a core item, reads `review.follow-up`
S1, two builds: the late parts leave: dDeclaredLoop 29, dDeclaredLoop-B 18 · 196 units (-18), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
  dDeclaredLoop-B lands at 82, dWitnessedBar at 86
S2, two builds: everything dWitnessedBar does not need leaves: dDeclaredLoop 22, dDeclaredLoop-B 25 · 192 units (-22), dGroundRules > dOrderedCharter > dDeclaredLoop > dDeclaredLoop-B > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
  dDeclaredLoop-B lands at 82, dWitnessedBar at 79
S3, three builds: the early and the late parts each leave: dDeclaredLoop 22, dDeclaredLoop-B 7, dDeclaredLoop-C 18 · 189 units (-25), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
  dDeclaredLoop-B lands at 64, dWitnessedBar at 79
  dDeclaredLoop-C lands at 75, dWitnessedBar at 79
dConvergedCharter's parents land at: dCalibratedLens 200, dShippedRelease 196, dScopedBuild 186
lightening dCalibratedLens by k units saves min(k, 4): the next parent, dShippedRelease, lands only 4 units before dCalibratedLens does
L1, dCalibratedLens split: the Loop Review's 4 after dTendedCadence, the other 7 after dWellOiledMachine · 210 units (-4), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dShippedRelease > dConvergedCharter
S1 with L1: 192 units (-22), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dShippedRelease > dConvergedCharter
```

| Candidate | Parts, in units | New builds | Path, in units | Saved |
|---|---|---|---|---|
| S1, two builds: the late parts leave | 29 and 18 | 1 | 196 | 18 |
| S2, two builds: everything dWitnessedBar does not need leaves | 22 and 25 | 1 | 192 | 22 |
| S3, three builds: the early and the late parts each leave | 22, 7 and 18 | 2 | 189 | 25 |
| L1: dCalibratedLens split at the Loop Review | 4 and 7 | 1 | 210 | 4 |
| S1 with L1 |  | 2 | 192 | 22 |

- **S3, the owner's choice, delays nothing.** Its early part lands before dWitnessedBar. Its late part's first user
  starts only after dTotalRecall lands.
- **S2 couples the early parts' users to the late ones.** dTotalRecall and dBoundRoles then wait for one moved part
  that holds both, and it lands after dWitnessedBar.
- **S1 leaves the early parts in the spine.** That keeps one build, but holds the spine's successor longer.
- **No lightening of dCalibratedLens saves more than 4 units.** dShippedRelease lands only 4 units
  before it, and the path then runs through dShippedRelease.

## [costs] What a split costs

- **One more build per new part.** Each new part brings the fixed cost `[method]` names.
- **While the moved parts land beside dWitnessedBar:**
  - only the `standard` preset works, since every key reads its catalogue default;
  - sessions orient on today's kickoff card until the early part lands;
  - no mailbox carries dependency notices;
  - `attendance` is not yet a key, so every run is unattended, which is its default anyway.
- **The re-cut it owes:**
  - the new builds' rows, rosters and gaps;
  - their nodes' owners, moved in the ownership record and flow-steps;
  - the later builds' after cells;
  - the reconciliation gate, re-run;
  - the walk's waves, derived again.

## [forks] Parked for the owner

| Fork | Question | Options, the recommendation first | What the answer sets |
|---|---|---|---|
| SP-1 | Split dDeclaredLoop? | S1, the late parts leave as one new build; S3, the early and the late parts leave as two new builds; keep the chain as it stands | a structural decision about the chain |
| SP-2 | Lighten dCalibratedLens? | keep it whole, since no lightening saves more than the slack before dShippedRelease; split it at the Loop Review, L1 | a structural decision about the chain |

S1 was recommended because one new build buys most of what any split reaches (`[results]`).

## [answers] The owner's answers, 2026-10-18

Asked through AskUserQuestion with the first run's figures (`[results]`, "As asked"), each answer quoted as the tool
returned it, the critical path's quoted length pinned to the commit it was read at:
- SP-1, asked at `1d32760f3` as "SP-1: Split dDeclaredLoop? (a structural decision about the chain; critical path 214 today)": "S3, two new builds"
- SP-2, asked as "SP-2: Lighten dCalibratedLens? (a structural decision about the chain)": "Keep it whole (Recommended)"

The two new builds' names, asked after:
- asked as "Name for the early build (7 units: leases, the card, the entry items and placement, the map slot, the probe program, the code seed), which lands beside dWitnessedBar?": "dPlacedRequest (Recommended)"
- asked as "Name for the late build (19 units: presets, session handling across compaction, the mailbox and dependency notices, follow-up review rounds, attendance, repeat)?": "dKeptSession (Recommended)"

The naming questions already carried the first correction, the card moving to the early build. The second, the
follow-up rounds staying in the spine, was found after them, so dKeptSession holds 18 units, not the 19 asked.

## [folded] What the answers changed

- **v2's chain** (its revision note dated 2026-10-18, SP-1):
  - dDeclaredLoop keeps 22 units, the spine's core and the breakpoint mechanism;
  - dPlacedRequest, stage Entry, after dDeclaredLoop, takes 7;
  - dKeptSession, stage Session, after dDeclaredLoop and dPlacedRequest, takes 18;
  - dBoundRoles and dTotalRecall gain dPlacedRequest as a parent, and dWellOiledMachine and dIndexedDesign gain
    dKeptSession;
  - dDeclaredLoop's 21 gaps split ten, eight and three;
  - dGroundRules's preset step and `[owed]`'s preset section now name dKeptSession.
- **The owners:**
  - v2's catalogue: 17 keys to dPlacedRequest and 12 to dKeptSession;
  - flow-steps: the five entry items and the probe program's seven to dPlacedRequest;
  - layer-memory: the `card`, `lease` and `probe` kinds to dPlacedRequest, and the `mailbox message` kind to
    dKeptSession;
  - the ownership record's amendment lists every moved node.
- **The re-cut's class rows:** `preset`'s row names dKeptSession as the key's owner. The four rows whose citing
  clause moved name it as the citing build. The gate read those four as needing no dependency, and the moved
  citations as unclassed, until they did.
- **The fates record:** five destinations that moved with their clauses.
- **The chain:** the critical path drops by twenty-five units, as the corrected run priced. Both new builds land before
  any build that waits on them starts. The instruments record's `[final]` holds the run.
- **dCalibratedLens** stays whole (SP-2).

**Owed next:** the walk resumes, its `[chain]` glance and wave 1 derived again over eighteen builds.
