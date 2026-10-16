# Research: role workflow shapes, run A

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 79's return, verbatim. Its question is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-25-researcher.md`, which dispatch 80 runs
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`.

---

I'm returning the eight sections for the **role workflow shapes** research. Nothing was written to the repository. Every probe was read-only, and the `agent-cap` probe used a `Workflow` payload, which writes nothing (agent-cap.js:1683-1709 writes only on `Agent` payloads).

## 1. Verdict

A shape is declared data: one extended entry per role item in the existing `tools/roles/workflows.toml`. Each entry names one of four shape kinds, and each kind is a role harness registered at Runtime's role-harness point. The entry also names its stages and their fan, its checklist source, its orientation template, its merge and its twin rule. Efforts stay in `house/policy.toml`. The guard compares each harness call's roles and efforts with the declared shape and refuses a mismatch. Today it admits one (probe below, exit 0). Shapes are ranked by confirmed results per 100k output tokens. Recall is measured against a twin union only on calibration pairs. Twins earn their cost on design reviews, where single-run coverage is 66–87%, and never on the reuse scout, where two runs agreed 24 of 24.

## 2. Today

| Part | What it does | Measured | Where |
|---|---|---|---|
| Workflow table | 10 workflows: driver, harness, roles, `stages` map | 3 workflow-driven harnesses; 6 stage keys | `tools/roles/workflows.toml:13-105` |
| Effort policy | effort per role, and per stage for two workflows | 7 role entries, 2 stage tables | `tools/roles/house/policy.toml:5-23` |
| Effort and role readers | `harness-args` / `stage-efforts` | output below | `tools/roles/handoff.py:453-488` |
| Static checks | R6–R9 cover the table's keys, roles and stage map | no fan, no merge, no template | `tools/roles/check_roles.py:29-35` |
| Spawn guard, rule 6 | checks only that the harness is declared and each `args.roles` value is an agent-true role | lets through a wrong stage-to-role map and any effort (probe below) | `tools/hooks/agent-cap.js:2157-2187` |
| Lens sets, fan, batches | hard-coded in one 1,998-line script, plus a byte copy in the template | 5 / 5 / 3 lenses, `MAX_VERIFIERS = 5` | `tools/workflows/tier2-review.js:705-773,1283-1284` |
| Resume probe | an untyped agent that runs `git rev-parse` and reads files | not in the shape line's agent count (11, against 12 in the ledger) | `tier2-review.js:926-927,935` |
| Shape line | per-run raw, confirmed, agents, out-tokens | 43 lines; no effort, shape id or role-sha | `tier2-review.js:929-933` |
| Checklist | `gotchas.py --for-diff/--for-paths` | 130 classes; 3,605 B for two paths | `tools/memory-tree/gotchas.py:1-30` |
| Agent files | static blocks | 9 files, 45,213 B; efforts rendered into front matter | `.claude/agents/*.md` |
| Orientation template, merge | none declared (`gap-roles-18`) | twin merges were placed by hand in 3 comparison records | layer-roles `[owner-notes]` |

```
$ python tools/roles/handoff.py stage-efforts closing-review   -> {"diffFinder":"high","skeptic":"high","synthesis":"high"}
$ python tools/roles/handoff.py harness-args tier2-review      -> {"diffFinder":"gov-diff-reviewer","skeptic":"gov-skeptic","specFinder":"gov-spec-reviewer","synthesis":"gov-synthesizer"}
```

**Cost and yield per shape**, aggregated from every `review-shape` line under `memory/builds/*/reviews/`:

| Shape | Runs | Raw | Confirmed | Precision | Agents | Out-tokens | Confirmed per 100k out | Confirmed per agent |
|---|---|---|---|---|---|---|---|---|
| spec-audit, 5 lenses, medium | 12 | 660 | 577 | 0.87 | 132 | 2.69M | 21.4 | 4.37 |
| diff, full, 5 lenses | 21 | 478 | 419 | 0.88 | 228 | 4.61M | 9.1 | 1.84 |
| diff, light, 3 lenses | 10 | 198 | 159 | 0.80 | 83 | 1.25M | 12.8 | 1.92 |

**Twin runs**:
- **Five core layers** (layers-reviews-compared `[summary]`): either round alone covers 74% or 75% of 265 defects. The second round added 70 defects for 1,194k tokens, 5.9 per 100k, against the first round's 16.4. It caught 6 of the 29 high defects.
- **Expansion round:** 66% and 87% coverage. It caught 2 of 8 highs, both security.
- **Runtime layer:** 46 or 45 of 59 defects.

**aScoutedSeam benchmark** (`git show b0fe68f30:…-1-2-benchmark.md`):
- **Agent set:** M1b checklist scout solved 12 of 23 against M3 (two scouts and a judge) at 12 of 23, on a third of the agents (lines 169-171).
- **Pilot rejected:** M2, five lenses with skeptics, cost 1.6–1.9M tokens per case, and its skeptics refuted 0 of 49 (94-97).
- **Orientation template:** M1c, with a house index, a sketch and a census, solved 16 of 24 against 13 (`…-1-7-m1c-trial.md:56-63`). Its two runs agreed on 24 of 24 positives, and the union added no primary (81-82).

**Where the records and the code disagree:**
1. **Owner's paraphrase vs benchmark:** the owner speaks of xhigh against medium. The benchmark compared M1b and M3 both at medium. The effort finding (extra to medium held recall at a fifth to a seventh of the cost) is a separate result.
2. **Runtime extension points:** the handed facts say nine. layer-runtime `[extend]` (line 746 onward) now lists ten; the expansion round added cadence items.
3. **Agent count:** the comparison records count 12 agents per run, but the shape line says `agents=11`. The difference is the untyped probe.

## 3. Across the layers

| Layer | Needs from it | Gives it |
|---|---|---|
| instruction | orientation templates as tagged units `orient.<name>`; checklist slices rendered into the task block | which units each stage's role loads; zero shape bytes in any agent's context |
| flow | each role item names its `shape`; `review.<stage>.effort` (v2:696) | the merge outcome as the item's witness; the twin item |
| roles (owner) | roster, `[matrix]`, `roles.verifier-context` | per-item shape; the join that every role item has a shape |
| memory | a `shape-run` record kind through `record`; bug classes from the library; the house index as a map component | the yield series; the defect map as a record |
| runtime | role-harness registration with spawn sites and fan; act binding; journal reconciliation | four shape kinds, each one registered harness |
| observability | the Loop Review as a journal reader | the ranking metric and calibration pairs |
| integrations | nothing | nothing (a twin needs no outside service) |
| distribution | `shapes` installed as an adopter-owned seed beside `policy.toml` | per-harness install targets |

| Other system | Needs from it | Gives it |
|---|---|---|
| Tags | the `shape.*`, `orient.*` and `role.*` namespaces; join checks | the shape tag on every return and shape-run record |
| Code annotations | canonical-copy markers (`# >>> name`) and anchors that the house index reads | the house index as the annotations' main consumer |
| Instruction writing | a template grammar for orientation units; the statement types of P11 | the rule that shapes are data and never load |
| Memory structure | a record kind, house-index freshness, and the read-path budget for the index (2–33 KB measured) | the yield metric as the case for what the read path should carry |

## 4. Candidates

| | A: shapes stay in harness code (today, extended) | B: shape as data, one interpreter harness | C: escalate on the first run's output | D: one high-effort agent per role item |
|---|---|---|---|---|
| Mechanism | lens sets and fan in each `.js`; `workflows.toml` maps roles; static marker scan | each workflow entry is a shape; kinds are registered harnesses; the guard compares the call's args with the entry | run single; twin or widen when the run's own output signals (e.g. `review.follow-up=after-high`) | collapse fans: one agent with every brief, plus the checklist |
| Efficiency | a shape change edits about 2,000 lines plus a byte copy; the caller makes 2 lookups and types the args (6 of 11 failed runs were refusals of caller-composed args, research-roles-interactions:59) | caller lookups 2 to 0; agents read 0 shape bytes; −1 agent per review (the probe moves to a command) | estimate: saves at most what the trigger skips | estimate: about a third of the tokens if recall held |
| Test that makes it lose | does the guard admit a harness call in an undeclared shape? | can one kind's merge be declared without losing review's judgment? (tag-key merge vs the hand map) | how often does the trigger fire? | does any lens hold defects no other lens found? |
| Result | **loses**: exit 0 (probe 1) | **survives**: needs a placing agent; a key alone is not enough (probe 2) | **loses**: fires on 37 of 43 runs (probe 3) | **not refuted by the tree; owed**: every runtime lens held 2–5 unique defects, and D1's recall fell at medium. The test rides on dFairHearing's owed replay |

Probe 1, on the guard. Payload: `tier2-review.js`, `kind: diff-review`, with the declared shape, then with `gov-builder` in every stage at `low`, then with `gov-session` as finder:
```
--- declared shape                                   exit 0
--- undeclared: builder as finder+skeptic, effort low exit 0
--- control: agent:false role  BLOCKED by agent-cap: rule 6 … not an agent-true role   exit 2
```

Probe 2, the merge key. The runtime appendices were joined to the hand map in runtime-reviews-compared `[map]`:
```
appendix rows A,B: 60 61 map defects: 61
defects in both: 33 joined by a shared section tag: 33
cross-defect A/B pairs: 2175 that a tag key would wrongly merge: 860
```
A section-tag key finds every true join but wrongly merges 40% of cross-defect pairs. The key can only block candidate pairs; an agent places them.

Probe 3, escalation:
```
spec-audit full runs 12 runs with >=1 high/blocker: 11
diff-review full runs 21 … 18
diff-review light runs 10 … 8
```

D's owed test: one high-effort agent with all five design-audit briefs on blob `767187aa`. It loses unless it reaches at least 74% of 59 defects and at least 7 of 8 highs, at no more than a third of 212k output tokens.

## 5. The pick, specified

**Pick: B.** It is owned by dBoundRoles, with the kind harnesses registered through dWellOiledMachine and the review kind's internals in dFairHearing. The seam it extends is `workflows.toml` plus `check_roles` R9 plus rule 6.

The shape grammar extends the existing entry. Efforts stay in `policy.toml`, so each fact lives in one place:
```toml
[[workflow]]
name = "review.design"                  # tag shape.review.design; items name it
kind = "find-verify-synth"              # single | per-unit | scout-pass | find-verify-synth
stages = { find = {role="reviewer", fan="preset:design-audit", cap=5},
           verify = {role="skeptic", fan="batches-by-address", cap=5},
           synth = {role="synthesizer", fan=1} }
orient = "orient.verifier-cold"         # an instruction unit tag
checklist = "library:for-paths"         # none | library:for-diff | library:for-paths
merge = "synth"                         # none | concat | synth | defect-map
twins = "review.twins"                  # a policy key, or "never"
```

**Per role:**

| Role | Kind, agent set | Effort per stage | Checklist | Orientation | Merge | Evidence |
|---|---|---|---|---|---|---|
| orientation scout | single | xhigh as declared; calibration owed | none | the card | none | no measurement; nothing changes without one |
| prompt writer | single | medium | none | the resolved work order | none | writes framing only (R3-E) |
| planner, architect | single | high | library:for-paths | `orient.producer` | none | judgment roles; no shape data |
| researcher | single; twins on owner-opened forks | medium | none | handed question and packet | defect-map over candidates | this round runs twins; first data point |
| reuse scout | scout-pass: one M1c scout plus a deterministic design pass | medium | library:for-paths | `orient.house-index`, sketch, census | concat, deduped by path and symbol | 16 vs 13 of 24; judge added 0; 24 of 24 agreement, so never twins |
| spec writer, builder | per-unit, parallel up to the bound | high / xhigh as declared | library:for-paths | `orient.producer` | none | per unit by design |
| tester | single | medium | library:for-diff | `orient.verifier-cold` | none | attribution is mostly command work |
| reviewer, skeptic, synthesizer | find-verify-synth, 5+≤5+1 | design or spec medium; diff high; light diff 3 lenses | library | `orient.verifier-cold` | synth; twins → defect-map | 21.4 per 100k at medium; D1 fell at medium (7 to 4 of 23) |
| deployer, maintainer | single (expansion-registered) | medium | none | `orient.producer` | none | P28 |

**Rejected shapes:**
- scout plus judge: no gain on three times the agents (M3).
- lenses plus skeptics for scouting: about 1.7M tokens per case, 0 refuted (M2).

**Checks, each with its red case:**
1. **R9+:** every entry's kind names a registered harness whose declared spawn sites equal the entry's stages. Red on today's tree: tier2-review's probe at :935 has no stage.
2. **Rule 6+:** `args.roles` and `args.efforts` must equal the entry's resolved map. Red on probe 1's second payload.
3. **Act reconciliation:** journaled SubagentStart types per stage stay within the declared fan. Red on a planted extra `agent()`.
4. **Join:** every role item in the matrix names a shape, and every shape is named. Red when an item's `shape` is struck in a planted copy.

**Read-path cost:** shapes never load into an agent, so role agents gain 0 bytes and the caller makes 0 lookups (against 2 today). The only added load is `orient.house-index` in the reuse scout's task block, 2–33 KB as measured, held to the packet budget.

## 6. Items and policies

| Tag | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `design.house-index` | command | generates the house index before `design.seams` | index digest keyed into the work order | to `design.seams` |
| `review.twin` | command | dispatches a second run, identical args except the run label | two reports at one pinned blob | to `review.merge` |
| `review.merge` | synthesizer (merge stage) | places both runs' findings on defects; the command blocks candidate pairs by address first | defect-map record; the instrument refuses an unplaced id | confirmed defects go to `review.findings` |
| `review.cost` (fills) | command | the shape line gains `shape`, `efforts` and `role-sha` | the shape-run record | to the Loop Review |
| `loop.shape-rank` | command (observability) | ranks shapes per item by confirmed per 100k out, with recall vs the union on calibration pairs | rank table derived from shape-run records | a proposal to Plan |

| Key | Values | Default | Why |
|---|---|---|---|
| `review.twins` | never, design-owed, every-owed | design-owed (fork F1) | the second run adds 15–52% more defects and caught 8 of 37 highs, at 4.7–6.0 defects per 100k |
| `roles.shape-binding` | refuse, warn, record | refuse | matches `roles.answered-calls` |
| `roles.shape-calibration` | off, on-change, periodic | on-change | a twin pair when a shape or role-sha changes keeps the recall series alive at minimum cost |

## 7. Gaps

**Closes:** `gap-roles-18` (gap-register:134). Contributes to `gap-review-03`: the probe leaves review, and light and twin depth are declared.

**New gaps exposed:**

| Proposed id | Severity | Gap | Evidence |
|---|---|---|---|
| gap-roles-19 | HIGH | rule 6 admits any agent-true role at any effort in any stage, so a builder can review its own diff (breaks R3-C) | probe 1, exit 0; agent-cap.js:2182-2186 |
| gap-roles-20 | LOW | tier2-review spawns an untyped agent for command work, and no stage declares it | tier2-review.js:935; 11 vs 12 agents |
| gap-review-11 | MED | the shape line has no effort, shape or role-sha, so yield cannot be tied to effort | all 43 lines; tier2-review.js:931 |
| gap-review-12 | MED | twin merges have no item, record kind or check; three were placed by hand | comparison `[map]` sections; probe 2 |

## 8. Forks

| Fork | Options | Recommendation |
|---|---|---|
| F1: when twins run by default | never; design-owed; every-owed | design-owed: that is the owner's practice so far, and the marginal yield sits at the 6.3-per-100k bar |
| F2: effort for roles with no measurement (orienter and builder, xhigh) | keep; lower after a replay; lower now | keep, and run a calibration replay before any change |
| F3: run candidate D's single-agent review arm on dFairHearing's replay | add it (+1 agent, about 70k tokens); skip | add it: it is the one test that can retire the 11-agent fan |

Files read:
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\roles\workflows.toml`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\roles\house\policy.toml`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\roles\handoff.py`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\roles\check_roles.py`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\hooks\agent-cap.js`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\workflows\tier2-review.js`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\.claude\roles.json`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\` (the records named above)
