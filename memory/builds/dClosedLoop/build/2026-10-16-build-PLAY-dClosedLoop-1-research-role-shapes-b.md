# Research: role workflow shapes, run B

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 80's return, verbatim, except that its title line is demoted to keep one H1 per
record. Its question is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-25-researcher.md`, which dispatch 79 runs
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`.

---

**Role workflow shapes: researcher return (PLAY-dClosedLoop-1)**

## 1. Verdict

Every role item names one shape from a registry, a `shapes.toml` in the roles kit. A shape is one of four registered harness kinds: `single`, `scout-judge`, `panel` or `twin`. It fills in five fields: stages (role, fan and effort per stage), checklist, orientation template, merge, and a cap on agents.

The work order hashes the resolved shape into a `shape-sha`. Act binding refuses a Workflow call whose roles, efforts or fan differ from that shape. The supervisor checks the journal against the shape afterwards.

Twin runs are used only on design records, set by `review.twin`. One synthesizer merges them over candidate pairs grouped by the address each finding cites.

Shapes are ranked on recall first, then on grade-weighted verified results per 100k tokens. The Loop Review prices each shape in the value ledger and proposes changing one only when the gap is wider than the measured noise between twin runs.

## 2. Today

| Part | What it does | Measured | Where |
|---|---|---|---|
| `workflows.toml` | 10 workflows, each with roles and a stage-to-role table | 3 harnessed workflows declare stages | `tools/roles/workflows.toml:13-105` |
| `house/policy.toml` | effort per role and per workflow stage | 7 roles named; researcher and scout fall to `medium` | `tools/roles/house/policy.toml:5-23` |
| `handoff.py harness-args` / `stage-efforts` | print the declared roles and efforts as JSON | `tier2-review` → `{"diffFinder":"gov-diff-reviewer",…}`; `closing-review` → all `high` | `tools/roles/handoff.py:453-490` |
| `tier2-review.js` | the review panel: up to 5 finder lenses, then up to 5 skeptic batches, then 1 synthesizer | 148,301 B; lens sets in code at `:705-773`; `MAX_VERIFIERS` at `:1283` | |
| Spawn guard (`agent-cap.js`) | Workflow calls: is the harness declared, and is each `args.roles` value an agent-true role | fan cap 5 (`:492-504`) | `tools/hooks/agent-cap.js:2160-2187` |
| `review-shape` line | raw, confirmed, agents and out-tokens per run | 43 runs emitted; nothing in `tools/` reads them | `tier2-review.js:79` |
| Lens-yield table | per-lens raw, confirmed and precision | present in 70 reports | same harness |
| Bug-class checklist | `gotchas.py` over `memory/gotchas/` | 134 files; INDEX is 35,500 B | `tools/memory-tree/gotchas.py` |
| Orientation template | declared nowhere. The reuse scout's body (648 B) defers to `reuse-lookup.agent.md`, which calls `reuse_lookup.py` | that lookup alone (arm M0) solved 0 of 24 | `tools/roles/agents/gov-reuse-scout.agent.md:17-20` |
| Shape-trial seams | `orient-counterfactual.js` runs matched arms; `review_replay.py` scores recall against a known set | | `tools/workflows/orient-counterfactual.js:1-30`, `tools/workflows/review_replay.py:2` |
| Read-path baseline | orientation reads are 16.9% of role input bytes; median 42 calls per agent | | `layer-roles` `[current]` |

**Cost and yield per shape**, from all 43 `review-shape` lines:

```
grep -rho "^review-shape .*" memory/builds/*/reviews/ | awk …
kind/intensity    n   raw  conf agents  outTok   hi+bl
diff-review/light 10  198  159    83   1245285    21
spec-audit/full   12  660  577   132   2691510    45
diff-review/full  21  478  419   228   4614647    64
```

- **Confirmed per 100k out-tokens:** spec/full 21.4, diff/light 12.8, diff/full 9.1.
- **Agents per run:** 11 for full, 9 for light.

**What twin runs found that one run missed:**
- Five core layers: one round covers 74% or 75% of 265 defects. 6 of 29 high defects were found by one round only.
- The expansion round: 66% and 87% of 38 defects; 2 of 8 highs found by one round only.
- The first round yields 16.4 defects per 100k out-tokens. The second round adds 5.9 per 100k (70 defects for 1,193.9k).

**Shape probe.** The spawn guard admits a review shape that is not declared:

```
… "roles":{"diffFinder":"gov-builder","skeptic":"gov-builder","synthesis":"gov-builder"},"efforts":{"diffFinder":"low","skeptic":"low"} … | node tools/hooks/agent-cap.js
exit=0
```

`workflows.toml:68` lists this guard as the enforcer of the closing review's shape. In fact it admits a builder verifying its own work (an R3-C breach) at efforts below policy.

**Where records and code disagree:**
- The handed facts say Runtime declares nine extension points. `layer-runtime` `[extend]` lists ten (cadence items were added), and `[contract]` (`:824`) says "the ten".
- The owner's quote says one xhigh agent matched two scouts and a judge at medium. The benchmark's matched comparison ran both shapes at `medium` (12 of 23 each), and `high` was never measured (benchmark, Limits).

## 3. Across the layers

| Layer | Needs from it | Gives it |
|---|---|---|
| instruction | the checklist and orientation template as units in the static block, under `BODY_CEILINGS` | one checklist and one template unit per shape, tagged `role.*` |
| flow | each role item names a shape in the loop definition; `review.trigger` and `review.cost` | shape-sha as part of each role item's witness; the `review.twin-merge` item |
| roles | the roster, the cycle and P29's handed content | the shape registry and each role's shape, closing gap-roles-18 |
| memory | the return-record kind; a derived house index; the bug-class catalogue | a `shape-run` record kind (shape, shape-sha, agents, tokens, verified results, grades) |
| runtime | role-harness registration with spawn sites and fan; act binding; journal reconcile; the five-agent cap | four harness kinds, each registered once; a digest to bind against |
| observability | `loop.gather`, `loop.price` and `loop.propose` | ledger rows of kind `shape` |
| integrations | none | none |
| distribution | install of `shapes.toml` as an adopter seed beside `policy.toml` | none |

| System | Needs | Gives |
|---|---|---|
| tags | stable tags for items, roles and shapes (`shape.<name>`, `role.<name>`, `<step>.<name>`) | a join of item → shape → role that a check reads |
| annotations | anchors the house index and handed excerpts cut at | demand: which anchors an orientation template asks for |
| instruction writing | a template grammar for checklist and orientation units | two unit kinds with fixed fields |
| memory structure | the house index derived on read; a byte budget for it | the `shape-run` record kind and its reader |

## 4. Candidates

| | A. Shape keyed by workflow | B. Shape is the harness code | **C. Shape registry per item (pick)** | D. Adaptive selection from the ledger |
|---|---|---|---|---|
| **Mechanism** | Add fan, lenses, checklist, orientation and merge columns to each `workflows.toml` entry | An item names a harness script, and the script holds the lenses and fan | Items name a shape row of a registered kind; the work order is hashed with its shape-sha; the call and the journal are bound to it | A ranker picks each item's shape per run from ledger metrics |
| **Efficiency** | 0 agent reads; one row per workflow | 0 agent reads, but a reader must parse 148 KB of JS to name a shape | 0 agent reads; about 14 rows (~6 KB) read by the harness and guard in milliseconds | Needs about 11 runs per arm per item kind (below) |
| **Smallest losing test** | Does one workflow run two shapes it cannot declare apart? | Can a settled per-run lens choice live in code? | Can every shape in use today be written as a row, and does the guard refuse a mismatch? | Is run-to-run noise smaller than the effects being ranked? |
| **Result** | **Loses.** The `closing-review` workflow ran light (9 agents) and full (11 agents) in this build; intensity is a per-call argument found in no data file. 8 of the 19 role items in `[matrix]` (planner 3, architect 3, tester 2) have no workflow entry. | **Loses.** R-1 settled `review.opt-in`, a policy key that picks lenses per run, but lenses are constants at `tier2-review.js:705-773`, and `MAX_LENSES` is a second copy of that fact at `agent-cap.js:497`. | **Passes on paper.** single (builder), panel full and light, M1c scout and twin each write as a row; the skeptic fan writes as `batches(findings,by=address,max=cap)`. The fixture is owed (§5). | **Loses.** Per-run sd is 0.083, so a 10% shift needs 10.8 runs per arm, about 2.4M out-tokens per arm per item kind. 16 of the 19 role items have no samples at all. |

D's noise figures come from the seven twin pairs:

```
python -I -c "…twin pairs (56,57),(44,36),(60,45),(37,43),(52,51),(37,46),(47,49)…"
rel diff per twin [0.018, 0.2, 0.286, 0.15, 0.019, 0.217, 0.042] mean 0.133
per-run sd 0.083
runs/arm to see 0.1 …: 10.8
```

**How twin results merge.** Two mechanisms were tested on the five core layers' hand-made maps:
- **A deterministic union by cited address:** **loses.**
- **A synthesizer judging candidate pairs grouped by address:** kept.

```
python -I scratchpad/addrmerge.py
ALL {'both': 150, 'tagjoin': 148, 'pairs': 5557, 'falsepairs': 5149}
```

Grouping by the cited `[tag]` recovers 148 of 150 twin pairs. But 5,149 of the 5,557 pairs that share an address (92.7%) are different defects. So the address only makes candidates, and a synthesizer must judge them.

**Single scout or more agents (reuse), from the benchmark:**

| Shape | Agents | Solved | Out-tokens per solved |
|---|---|---|---|
| M3 + judge @medium | 3 | 12/23 | 2.05k |
| M1b @medium | 1 | 13/24 | 1.23k |
| M1c @medium | 1 | 16/24, both runs | 1.75k |
| M1c twin union | 2 | primaries 18 against 17 and 18 alone; items 41 against 39 | about 3.5k |

A second scout run adds no primary, so twins do not pay for scouts.

## 5. The pick, specified

**Grammar** (roles kit; the adopter's copy is seeded like `policy.toml`):

```toml
[shape.review-panel]            # tag shape.review-panel
kind = "panel"                  # one of the registered role harnesses: single | scout-judge | panel | twin
agents-max = 11
checklist = ["lens-brief", "bug-classes"]   # instruction units, by tag
orientation = "cold-artifact"   # orientation template unit, by tag
merge = "synthesized"           # none | union | synthesized | twin-synth
[[shape.review-panel.stage]]
key = "find";   role = "reviewer";    fan = "lenses(review.opt-in)"
[[shape.review-panel.stage]]
key = "refute"; role = "skeptic";     fan = "batches(findings,by=address,max=cap)"
[[shape.review-panel.stage]]
key = "report"; role = "synthesizer"; fan = 1
```

- Effort stays in `policy.toml`, rekeyed `[effort.stages.<shape>]`.
- A twin is `kind = "twin"` with `of = "<shape>"`, `runs = 2` and `merge = "twin-synth"`.

**Per role:**

| Role | Shape (kind, agents) | Effort per stage | Checklist | Orientation template | Merge | Evidence |
|---|---|---|---|---|---|---|
| orientation scout | single, 1 | xhigh until a trial says otherwise | kickoff manifest | session tree, leases, card | none | scouts hold recall at medium (benchmark); the trial runs on `orient-counterfactual.js` |
| prompt writer | single, 1 | medium | work-order fields | resolved work order | none | R3-E: 64.5% of task bytes are retyped |
| planner | single, 1 | high | plan-record fields | intake, triage, card | none | unmeasured; the default is today's spec-writer level |
| researcher | single, 1; twin for design records | medium | M12: candidates, losing tests | the question, plus a house-index slice | twin-synth, marking each claim `corroborated` or `single-run` | three expansion defects rested on one run's claim |
| reuse scout | single (M1c), 1; a design pass is optional | medium | M1b steps, sketch, census | house index handed first | union with the design pass | 16/24 against 13; a fifth of `extra`'s cost |
| architect | single, 1 | high | decompose fields | plan record and seams | none | unmeasured |
| spec writer | single per unit | high | spec template and bug classes | unit row, interfaces, seams | none | policy today |
| builder | single per unit | xhigh | acceptance and `gotchas.py` | spec at its SHA, write set | none (the executor re-runs acceptance) | diff-time depth (arm D1 fell 7→4 at medium) |
| tester | single, 1 | medium | attribution labels | verdict and labels | none | commands do the most |
| reviewer, skeptic, synthesizer | panel, up to 11 (light 9) | diff high; spec and design-audit medium | lens brief and bug classes | cold artifact | synthesized | §2 yields |
| deployer, maintainer | single | medium | registered by their expansion | registered by their expansion | none | P28 |

**Owners:**
- the registry and each role's shape: **dBoundRoles** (roles layer);
- call binding and journal reconcile: **dWellOiledMachine**;
- `twin-synth` in the review harness: **dFairHearing**;
- the `shape` ledger rows and the Loop Review's use of them: **dCalibratedLens**.

**Checks**, each with the case that turns it red:

| Check | Red case |
|---|---|
| `shape-join` (a new `check_roles` rule) | an item with no shape; a stage naming an undeclared role; `kind` not registered; an effort that is not a level |
| `shape-bind` (act-binding pack) | the §2 probe: `diffFinder=gov-builder` with efforts `low` must exit 2 (it exits 0 today) |
| `shape-reconcile` (supervisor) | a planted journal with a 12th agent, or a stage spawned as the wrong agent type → the witness is voided |
| `separation` | a verifier stage whose role authored the pinned artifact |
| `twin-placed` (command) | a finding id of either run left unplaced, or placed twice |
| `shape-run-coverage` | a role act with no `shape-run` record |
| Interpreter fixture (owed) | re-running the runtime twin's args must reproduce 11 and 9 spawn labels exactly |

**Read-path cost:**
- Agents read no shape data.
- Checklist and orientation units sit inside the static block, under `BODY_CEILINGS`. Bodies today are 648 to 2,377 B against ceilings of 1,536 to 4,096 B.
- The house index is handed in the task block, capped at 8 KB. gov's generated `MAP.md` plus `CARDS.md` is 41.7 KB.
- The target is the locate and method calls (4.0% and 6.2% of calls today), which the handed index should answer.

**Metric:**
1. Keep the shapes whose recall (against the union of known defects, or a `review_replay.py` known set) is within 2 sd (0.17 relative) of the best.
2. Among those, rank by grade-weighted (3, 2, 1) verified results per 100k tokens.

Out-tokens are the only cost logged today. Cache-read tokens join once runlog keys them by task-sha; they dominated the benchmark's cost.

## 6. Items and policies

| Item | Actor | Needs | Does | Witness | Routes |
|---|---|---|---|---|---|
| every role item (filled) | its role | resolved shape | runs within the shape | return record carries shape-sha; reconcile is clean | as declared |
| `review.twin-merge` (new) | synthesizer | both reports, plus candidate pairs grouped by address | defect map | the `twin-placed` join | `review.dispose` |
| `review.cost` (filled) | command | harness log | writes `shape-run` | the record | done |
| `loop.gather` and `loop.price` (filled) | command | `shape-run` records | ledger rows of kind `shape` | ledger blob | `loop.propose` |
| `loop.shape-trial` (new, observability) | executor | two shapes, one population | matched arms (orient-counterfactual pattern) | runlog-derived costs; replay recall | `loop.propose` |

| Key | Allowed | Default | Why |
|---|---|---|---|
| `roles.shape.<item>` | registered shape names with a compatible return | the item's declared shape | selects an extension, so it is validated against the registry |
| `roles.shape-enforce` | refuse, record | refuse | today's guard admits mismatches |
| `review.twin` | never, design-records, design-and-landing, always | design-records | 21–25% of highs escape a single round; design escapes spread down the chain |
| `review.twin-merge` | synthesized, manual | synthesized | address alone is 7.3% precise |
| `roles.orientation.house-index` | handed, pointer, off | handed | +3 of 24 solved at 2× the scout's cost |
| `review.loop.shape-trial` | owner-asked, each-window, never | owner-asked | a trial costs about 2.4M out-tokens per arm |

## 7. Gaps

- **Closes:** `gap-roles-18`. Partly closes `gap-roles-16` (a verifier stage's packet becomes declared) and `gap-roles-07` (the reuse scout's body gains the M1c checklist).
- **New, proposed:**
  - **Spawn guard does not enforce the shape.** It admits any agent-true role in any stage, at any effort (probe, §2).
  - **Nothing reads the `review-shape` line.** It is emitted by 43 runs with no reader.
  - **Twin runs have no harness and no merge.** In this build the defect maps were placed by hand in the comparison records.
  - **Four core roles have no definition and no workflow entry:** planner, architect, tester and prompt writer. Check against `gap-roles-14` before registering this one.

## 8. Forks

1. **Reviewer depth:** one run at `high`, or a twin at `medium`, for design records? Never measured.
   - **Recommend:** keep twins, and owe a matched trial on blob `767187aa` with `review_replay.py`.
2. **When twins run:** `design-records` (recommended), `design-and-landing`, or `always`.
3. **Orientation scout effort:** stay at `xhigh` until a counterfactual trial shows `medium` holds (recommended), or move to `medium` now on the scout evidence.
4. **Shape changes:** the Loop Review proposes and the owner ratifies (recommended), or changes apply automatically inside the noise band.

The twin-merge probe script is in the session scratchpad at `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\addrmerge.py`; nothing was written to the repository.
