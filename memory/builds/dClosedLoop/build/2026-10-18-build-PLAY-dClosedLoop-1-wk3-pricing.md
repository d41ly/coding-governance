# WK-3 priced: a split of dTotalRecall, and of dBoundRoles with it

**Serves:** research PLAY-dClosedLoop-1

The owner took WK-3's recommendation on 2026-10-18, pricing a split of dTotalRecall before wave 3
(`build/2026-10-18-build-PLAY-dClosedLoop-1-walk.md` `[wave-2-answers]`). This record prices it against the chain at
`44c8c8435`, the commit that folded wave 2's answers. At that commit the critical path is 190 units.

## [method] How the split is priced

- **Units and paths** are counted as NP-24's pricing counts them (`build/2026-10-18-build-PLAY-dClosedLoop-1-np24-pricing.md`
  `[method]`).
- **The successor that matters** is dWellOiledMachine, the build after dTotalRecall on the critical path. A split
  loses if dWellOiledMachine waits for a moved part.
- **What dWellOiledMachine needs** joins two readings:
  - the gate's mechanical one: `node_users.py` finds no backticked dependency of dWellOiledMachine on either build;
  - a reading of its 31 clauses, stated unit by unit in `[classification]`.
- **The bound.** dWellOiledMachine waits for dBoundRoles too, so a dTotalRecall split saves no more than dBoundRoles'
  landing allows. dBoundRoles lands only six units before dTotalRecall.

## [classification] The units dWellOiledMachine needs

Clause numbers are those `chain_clauses.py` prints at `44c8c8435`.

**dTotalRecall: 16 of its 40 units stay.** The code record, clause 11, stays as
well in T2 and C2, since dRankedPlan's intent fields and dCalibratedLens cite the `code` kind.

| Clause | The unit | Why dWellOiledMachine needs it |
|---|---|---|
| 1 | the memory contract: the record-kind registry (per kind: tag, layer, home, id rule, … | the record-kind registry, where dWellOiledMachine registers its journal, act, return and binding kinds |
| 2 | the one `record` write command, which mints ids under the build's claim or lease, is … | the `record` command, through which the supervisor alone writes shared records |
| 3 | for every filer outside a build, ids minted under an ask family's counter ref advanced … | ids minted outside a build, for intake that reaches no owner session and for cadence filers |
| 4 | the build README's declared front-matter schema, with unknown keys refused, `node`, … | the work order as each agent's root, where every act session starts |
| 5 | the slug and id grammar exported once and read by every slug and id reader … | the slug and id grammar every reader reads |
| 6 | typed relations (`depends-on`, `patches`, `amends`, `supersedes`, `implements`), … | typed relations, the dependency graph waits and landings read |
| 7 | the ask kind's acceptance at filing (`asks.acceptance`), extending backlog.py's V14 | the ask kind's acceptance at filing, kept so Plan's triage reads asks from the spine's memory alone |
| 16 | the `section`, `record`, `feature` and `class` extractors, `record find`, its last … | record find and show, the read budget, and the default load's memory share the session-start hook loads |
| 23 | derived anchors suffixed for a repeated heading | derived anchors, part of the extractors |
| 24 | the shape-run kind | the shape-run kind, whose rows dWellOiledMachine writes for each act |
| 25 | the acceptance re-measure counted over every read channel | the acceptance re-measure over every read channel, the runtime's among them |
| 26 | the shared extraction primitive in `tools/lib` (LX-2), reading the working tree, the … | the shared extraction primitive the map calls |
| 28 | the level-0 project map (PM-1, PM-2): its renderer and `gov map`, derived from the one … | the level-0 map the session-start hook loads |
| 29 | the three-way completeness check and the `map` leg pack | the map's completeness check and leg pack |
| 31 | the record-kind registry's purpose field, today's kinds, and the namespaces and chain … | the purposes the map renders at level 0 |
| 32 | the replay with the map and without at its first unit, so a losing map is never built, … | the replay that decides whether the map is built, and so whether dWellOiledMachine loads it |

The units that move: 8, decisions split by kind: reuse entries as level-3 instruction units beside their …; 9, the reuse scout's house index in M1c's shape (a digest of symbols, callers, dossiers …; 10, `reuse_lookup.py` retired with its readers rewritten, and memory-recall narrowed to a …; 12, the `gov:note` grammar and `gov:feature` anchors checked both ways with reuse entries, …; 13, gotchas handed by write set; 14, the generated views: README routing, the relation graph, the decisions' holds-now view …; 15, the research view, over the research-return kind; 17, the `annotations` leg, the marker query with the map's index rows where the map is …; 18, retrofit's `baseline` and `census` record kinds, the `origin` field, and the `adopt` …; 19, the origin check, re-derived from history, `origin` among the fields every slice …; 20, the progress cell; 21, the annotation resolve check's legacy and the untouched long blocks registered as …; 22, the `marker` namespace over the existing `gov:` words; 27, and the dated backfill of `kind: research-return` over the existing returns, 72 at …; 30, the atlas re-rendered from the same node table; 33, `gov map code` and `gov code show`, `callers`, `tests` and `where`, `git grep` the …; 34, the enrichment workflow: purposes derived first from docstrings and headers, an …; 35, the replay's losing test extended to code: a unit's files read and its lookups …; 36, extractors emitting typed edges from annotations, front matter, dossiers and decision …; 37, the region-parser factory in `tools/lib`, today's five region parsers re-pointed to it …; 38, the dossier's header becoming the feature node and its prose moving into units and …; 39, the `feature` namespace armed as an instruction selector when it registers, as NP-13 …; 40, the ctags extractor pack, opted into by `memory.code-languages: builtin+ctags` or …. Their users are dCalibratedLens, dConvergedCharter, dIndexedDesign, dMindYourWords, dScopedBuild, dShippedRelease and dTendedCadence, each
starting after dWellOiledMachine or, for dIndexedDesign, after dTotalRecall.

**dBoundRoles: 16 of its 34 units stay.**

| Clause | The unit | Why dWellOiledMachine needs it |
|---|---|---|
| 1 | the roster sorted by layer: twelve core roles (orientation scout, prompt writer, … | the roster, whose roles the act sessions run |
| 2 | each role's static instructions as structured fields, every limit paired with its … | each role's structured instructions and ceilings, loaded into its act session |
| 3 | the work order rendered per item (the item, its inputs as record fields at their SHAs, … | the work order bound to its act by task-sha, which act binding checks |
| 4 | the prompt writer composing every role's task from the driver's details | the prompt writer, which composes every act's task |
| 6 | returns through a schema-forced channel, residual failures retried by `roles.retries` | returns through a schema-forced channel, which the persisted-return store keeps |
| 7 | the role index and agent files beyond every worker's reach, a tree with no index … | the role index and `role-sha` compared at spawn |
| 8 | shell writes held to the allowance | shell writes held to the allowance inside an act session |
| 9 | the role-gate arm's field escape explained and closed | the role-gate arm's field escape closed, kept while folding C2: allowances leak until it is, and keeping it costs nothing, since dBoundRoles' first part still lands before dTotalRecall's |
| 10 | the `none` and `review` write classes enforced | the write classes enforced inside an act session |
| 11 | `driver.reads`, `prompts.author` and `roles.no-spawn` | `driver.reads`, `prompts.author` and `roles.no-spawn`, which the supervisor reads as the driver |
| 12 | every fork resolved by the role that meets it and recorded, or held as … | forks held as `run.on-owner-question` says, which the driver applies |
| 16 | the orientation scout's return carrying the placement disposition and its reason, the … | the driver recording the placement disposition, which dWellOiledMachine re-points to the intake record |
| 17 | the trust mechanism (P29): inputs handed as content, each fact keyed and classed by … | the trust mechanism, re-cut fresh at act launch |
| 24 | the `role` and `field` tag namespaces | the `role` and `field` namespaces the structured fields use |
| 25 | the role static block carried once per spawn | the static block carried once per spawn |
| 26 | the shapes, extending each `tools/roles/workflows.toml` entry with its kind (`single`, … | the shapes, whose digest act binding checks, and the experiment shape's acts |

The units that move: 5, the orientation scout composing the card in a sidechain at session start; 13, prompt-writer calls batched by `prompts.batch`; 14, a return's harness notices persisted with it, by `notices.record`; 15, work-order fields an optional component or an expansion fills (the map's dossiers) …; 18, each role's trust profile and context temperature declared and rendered …; 19, the answered-call hook (`roles.answered-calls`); 20, repairs recorded in returns and filed as asks against the producer's record …; 21, the role files' re-verification orders and protocol pointers replaced by rendered slices; 22, the role-by-step matrix derived from the item declarations and joined both ways; 23, role metrics per role and item into the value ledger, answered calls from the hook's …; 27, the work order's memory slices, code-notes slot and legacy slot, each under its own …; 28, the work order's `map` slot for the roles `memory.project-map` names, with the unfolds …; 29, the orientation scout composing the card's map cell; 30, the answered-call hook's range matching, the excerpt keys and a repair's carry, …; 31, the tester agent, re-founded from dWitnessedBar's minimal one (WK-1), with its …; 32, owner questions asked live while the build is attended, best effort recorded once the …; 33, the `code` slot rendered per item from its declared seed: the seed's definitions with …; 34, the work order selecting instruction units by `feature.*` once dTotalRecall arms that …. Their users are dCalibratedLens, dConvergedCharter, dMindYourWords, dScopedBuild, dShippedRelease and dTendedCadence, each starting after
dWellOiledMachine.

## [results] The candidates, at `44c8c8435`

**As asked.** The owner was asked from the first run, as captured:

```text
baseline: 190 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
dWellOiledMachine starts when its last parent lands: dTotalRecall 120, dBoundRoles 114, dKeptSession 82
T1, dTotalRecall alone: what dWellOiledMachine does not need leaves, the code record with it: dTotalRecall 16 and dTotalRecall-B 24 · 184 units (-6), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dBoundRoles > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
  lands: dTotalRecall 96, dBoundRoles 114, dTotalRecall-B 120, dIndexedDesign 132, dRankedPlan 133, dWellOiledMachine 145
T2, dTotalRecall alone, the code record kept: dTotalRecall 17 and dTotalRecall-B 23 · 184 units (-6), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dBoundRoles > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
  lands: dTotalRecall 97, dBoundRoles 114, dTotalRecall-B 120, dRankedPlan 127, dIndexedDesign 132, dWellOiledMachine 145
C1, both: each build's parts dWellOiledMachine does not need leave, the code record with them: dTotalRecall 16 and dTotalRecall-B 24; dBoundRoles 15 and dBoundRoles-B 19 · 172 units (-18), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dTotalRecall-B > dRankedPlan > dTendedCadence > dCalibratedLens > dConvergedCharter
  lands: dBoundRoles 95, dTotalRecall 96, dBoundRoles-B 114, dTotalRecall-B 120, dWellOiledMachine 127, dIndexedDesign 132, dRankedPlan 133
C2, both, the code record kept: dTotalRecall 17 and dTotalRecall-B 23; dBoundRoles 15 and dBoundRoles-B 19 · 171 units (-19), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dTotalRecall-B > dIndexedDesign > dTendedCadence > dCalibratedLens > dConvergedCharter
  lands: dBoundRoles 95, dTotalRecall 97, dRankedPlan 110, dBoundRoles-B 114, dTotalRecall-B 120, dWellOiledMachine 128, dIndexedDesign 132
```

**As folded.** Folding C2 kept one more of dBoundRoles' units in its first part: clause 9, the role-gate arm's field
escape. Allowances leak until it is closed, and keeping it costs nothing, since dBoundRoles' first part still lands
before dTotalRecall's. The run after it, as captured:

```text
baseline: 190 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
dWellOiledMachine starts when its last parent lands: dTotalRecall 120, dBoundRoles 114, dKeptSession 82
T1, dTotalRecall alone: what dWellOiledMachine does not need leaves, the code record with it: dTotalRecall 16 and dTotalRecall-B 24 · 184 units (-6), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dBoundRoles > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
  lands: dTotalRecall 96, dBoundRoles 114, dTotalRecall-B 120, dIndexedDesign 132, dRankedPlan 133, dWellOiledMachine 145
T2, dTotalRecall alone, the code record kept: dTotalRecall 17 and dTotalRecall-B 23 · 184 units (-6), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dBoundRoles > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
  lands: dTotalRecall 97, dBoundRoles 114, dTotalRecall-B 120, dRankedPlan 127, dIndexedDesign 132, dWellOiledMachine 145
C1, both: each build's parts dWellOiledMachine does not need leave, the code record with them: dTotalRecall 16 and dTotalRecall-B 24; dBoundRoles 16 and dBoundRoles-B 18 · 172 units (-18), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dTotalRecall-B > dRankedPlan > dTendedCadence > dCalibratedLens > dConvergedCharter
  lands: dBoundRoles 96, dTotalRecall 96, dBoundRoles-B 114, dTotalRecall-B 120, dWellOiledMachine 127, dIndexedDesign 132, dRankedPlan 133
C2, both, the code record kept: dTotalRecall 17 and dTotalRecall-B 23; dBoundRoles 16 and dBoundRoles-B 18 · 171 units (-19), dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dTotalRecall-B > dIndexedDesign > dTendedCadence > dCalibratedLens > dConvergedCharter
  lands: dBoundRoles 96, dTotalRecall 97, dRankedPlan 110, dBoundRoles-B 114, dTotalRecall-B 120, dWellOiledMachine 128, dIndexedDesign 132
```

| Candidate | Parts, in units | New builds | Path, in units | Saved |
|---|---|---|---|---|
| T1, dTotalRecall alone | dTotalRecall 16 and 24 | 1 | 184 | 6 |
| T2, dTotalRecall alone, the code record kept | dTotalRecall 17 and 23 | 1 | 184 | 6 |
| C1, both | dTotalRecall 16 and 24; dBoundRoles 16 and 18 | 2 | 172 | 18 |
| C2, both, the code record kept | dTotalRecall 17 and 23; dBoundRoles 16 and 18 | 2 | 171 | 19 |

- **dTotalRecall alone saves six units, however much moves.** dBoundRoles then decides when dWellOiledMachine starts,
  and the path runs through it.
- **Both together save eighteen or nineteen.** dWellOiledMachine then starts once both builds' first parts land. The
  path's new long arm is dTotalRecall's moved part, through dIndexedDesign or dRankedPlan, which need what it holds.
- **Keeping the code record (C2) beats moving it (C1) by one unit.** dRankedPlan, which cites it, then leaves the long
  arm.
- **What the pricing cannot settle.** dIndexedDesign's needs from the moved part are a reading, not a gate's. If
  spec time finds it needs only the reuse index and the typed edges, those two units can stay too, and the path
  shortens by about two more.

## [costs] What the split costs

- **Two more builds.** Each brings the fixed cost NP-24's `[method]` names, which no unit counts.
- **While the moved parts land beside dWellOiledMachine:**
  - no annotation index, research view or generated views;
  - no retrofit kinds or `adopt` program;
  - the `code` record's queries, enrichment and ctags pack absent;
  - each role's trust profile, metrics and slots beyond the map, code and memory slices absent, the work order
    carrying its core fields.
- **The re-cut it owes:** the new rows, rosters and gaps, the moved nodes' owners, the later builds' after cells, and
  the reconciliation gate re-run, as NP-24's split owed.

## [forks] Parked for the owner

| Fork | Question | Options, the recommendation first | What the answer sets |
|---|---|---|---|
| WK-4 | Split dTotalRecall, and dBoundRoles with it? | C2, both split and the code record kept in dTotalRecall's first part: two new builds; T2, dTotalRecall alone: one new build; keep both whole | a structural decision about the chain |

C2 is recommended. dTotalRecall alone cannot save more than six units, and only splitting both lets dWellOiledMachine
start earlier (`[results]`).

## [answers] The owner's answers, 2026-10-18

Asked through AskUserQuestion from the run `[results]` keeps as asked, each answer quoted as the tool returned it, the
critical path's quoted length pinned to the commit it was read at:
- WK-4, asked at `44c8c8435` as "WK-4: Split dTotalRecall, and dBoundRoles with it? (a structural decision about the chain; critical path 190 today)": "C2, both split (Recommended)"

The two new builds' names, asked after:
- asked as "Name for dTotalRecall's split-off build (23 units: decisions and reuse, annotations, the views, the retrofit's memory kinds, the code record's queries, enrichment and ctags pack, and the typed edges)?": "dLinkedLibrary (Recommended)"
- asked as "Name for dBoundRoles' split-off build (19 units: the work order's slots, trust profiles, the answered-call hook, repairs, role metrics, the tester re-founded, owner questions live)?": "dFurnishedOrders (Recommended)"

The fold kept the role-gate escape's fix in dBoundRoles' first part (`[results]`, "As folded"), so dFurnishedOrders
holds 18 units, not the 19 asked.

## [folded] What the answers changed

- **v2's chain** (its revision note dated 2026-10-18, WK-4):
  - dTotalRecall keeps 17 units, and dLinkedLibrary, stage Library, after dTotalRecall, takes 23;
  - dBoundRoles keeps 16, and dFurnishedOrders, stage Orders, after dBoundRoles, takes 18;
  - dIndexedDesign gains dLinkedLibrary as a parent, and dScopedBuild and dTendedCadence gain dFurnishedOrders;
  - dShippedRelease and dMindYourWords gain both;
  - the two builds' gaps split fifteen and nineteen, and fifteen and ten.
- **The owners:**
  - v2's catalogue: 11 keys to dLinkedLibrary and 14 to dFurnishedOrders;
  - flow-steps: the four `adopt.*` items to dLinkedLibrary;
  - layer-memory: eight kinds to dLinkedLibrary;
  - the systems record: the annotations system to dLinkedLibrary;
  - the ownership record's amendment lists every moved node.
- **The re-cut's class rows:** the two whose citing units moved now name dFurnishedOrders, and `decisions.major`'s now
  names dLinkedLibrary as the key's owner. The gate was red on all three until they did.
- **The fates record:** thirteen destinations moved with their functions, and a row whose function split names both
  builds.
- **The chain:** the critical path drops by nineteen units, as C2 priced, and now runs through dLinkedLibrary and
  dIndexedDesign. The instruments record's `[final]` holds the run.
