# Research: pointing at any part of the flow and telling what happened

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 110's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-13-researcher.md`, and its use is in `build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md`.

---

## 1. Verdict

No, not as designed. Every chain build writes its own record kind, but none of them carries a key that joins it to the others. P33's twelve edge types relate memory and code only. No `gov trace` or `gov why` verb exists in any design record. The journal and the transcripts never leave their node and are pruned after 60 days. Committed cost covers only review acts' output tokens.

Three additions make the answer yes for everything committed:
- a causal-parent key on every record kind, with its inverse derived (candidate D);
- act records carrying the act session's own usage and duration;
- a core `gov trace <key>` / `gov why <key>` verb in dWellOiledMachine.

Detail that lives only on one node would render as `not-local` or `pruned`, never as empty.

## 2. Reconstruction

**Measurements (all read-only; probes under `…/scratchpad/away/d110/`):**
```text
$ python -I keys.py <session tree> abcd975adc93473a6        # dispatch 51's transcript
meta keys: agentType description effort requestNonInteractive requestShape spawnDepth toolUseId
records 199 · sessionIds 1 agentIds 1 · first 13:40:46Z last 13:49:13Z · out 37759
usage keys: cache_creation_input_tokens cache_read_input_tokens input_tokens output_tokens …
$ (journal join over .git/runlog)
lander pushes ended rc=0 on this node: 20   first-parent commits on origin/main in window: 341
bars: 80   bars a push names via gate_run: 21
driver start lines with a session: 983 of 983   lines with unit=: 368
gates lines with slug/sess/unit: 0
$ find .git -name 'stall.*.log'        → (none)
$ runlog.py model dClosedLoop          → "no run-state file that was ever committed", rc=2
$ runlog.py model dSweptBranches       → rc=0, usage per split only, 0 agent ids
```

| Event | Today: sources and lookups | Answered today | Unanswered today |
|---|---|---|---|
| **E1.** Researcher dispatch 51 (session-log:115) | 6 sources, about 9 lookups: dispatch row, agent-line block (session-log:654-657), prompt marker, main transcript plus agent jsonl/meta, `git log` (6107daeee dispatched it, 50ebfc4de filed it), the research record | who: gov-researcher, medium effort. On what: the build and unit, from the `gov:handoff` marker (handoff.py:420). Cost: 8m26s and 37.8k output tokens. Produced: research-observability-a. Next: layer-expansions | **The tree SHA the agent read:** the transcript carries only `gitBranch` and `cwd`. **Which agent line is dispatch 51:** the row holds no agent id, so the only join is matching 8m26s and 37.8k. **Input and cache tokens:** only in node d's transcript. **The agent ledger:** never written, because handoff.py:769-771 skips a build with no spec. |
| **E2.** Unattended run dSweptBranches, run 1 | 6 sources, about 8 lookups: the committed record, RUN.md, README, driver.log, the run model (which needs node d's transcripts), git | window, usage per split (main 551,764 out; workflow 407,128 out), 21 units, brief and dispatch times | **Cost per unit or per agent:** the model holds usage per split only. **Which agent did each dispatch:** no agent id anywhere. **Terminal state:** the record says `LANDING · terminal: no`, the README says CLOSED, RUN.md says `phase: LANDING`. |
| **E3.** Red bar on `30466e129`, run `push-…-1733` | 6 sources, about 8 lookups: gates.log, pushes.log (`gate_run` join), the worktree's `gate-run/<run>/*.out`, `git show`, git ancestry, the transcript directory found by worktree name | SHA, 3 failed legs, the push refused (rc=1), the build from the merge subject (dRedressedBar), next unit TOOL-dRedressedBar-28 (from subject prose) | **Which session, unit or item ran the bar:** 0 of 80 gates lines carry one. **Leg output:** survives only in `.git/worktrees/<wt>/gate-run`, so a worktree prune deletes it. |
| **E4.** Reap `tree-killed target 8008`, 2026-10-13T21:50:50Z | 6 sources, about 9 lookups: health.log, gates.log by time, `.procs` files, a transcript search, reap's callers in code, the worktree's gate-run directory | It was the 6-hour wall-breach kill (`wall_breach=21600`) of bar `20261013T155028Z-1620` (16 legs red), joined **only by the matching second**. The session was found by worktree directory plus timestamp. | **What pid 8008 was, and which leg hung.** health.log's four fields carry no run, session or build key (reap.py:35-41). No stall line was ever recorded on this node. |

**As designed, once every chain build lands:**

| Event | The answering record (kind, owner) | Still unanswerable |
|---|---|---|
| E1 | work order with inputs at SHAs and `task-sha` (dBoundRoles); act record (launch, epoch, outcome) with `--session-id` beside the epoch (dWellOiledMachine, layer-runtime:376,894); return keyed by item instance, `task-sha` and spawn site (layer-runtime:533-536); research-return (dLinkedLibrary); the next item from transitions (dDeclaredLoop) | **Cost:** the act record declares no tokens or wall time. Shape-run rows carry output tokens for review acts only (flow-steps:477; systems:426-432). **Transcript detail:** never leaves its node (layer-runtime:854). |
| E2 | transitions per unit (dDeclaredLoop); landing record (dShippedRelease), which closes the terminal ambiguity; run record (dTendedCadence, layer-expansions:248-250) | **Per-act cost**, as in E1. **A run on a node that dies before its journal reader writes the run record:** no designed detector catches it. |
| E3 | runner-written verdict keyed by SHA, seen-red and routing records, catch history (`gap-test-10`, dWitnessedBar) | **Who ran a bar outside an act:** no record names an attended session's run. **Leg output:** no designed home. |
| E4 | a journal line, under the invariant that every runtime event is journaled (layer-runtime:883, dWellOiledMachine) | **The line's keys:** the journal grammar declares no act, epoch or bar-run field. **The health log and stall log:** no designed record kind names either. **Retention:** 60 days, node-local (layer-runtime:919). |

**Where the records and the code disagree:**
1. **dSweptBranches.** The committed record is stale: the model re-derived today ends its window at 13:29:51Z with 565,263 main output tokens, while the record says 12:01:30Z and 551,764.
2. **The agent ledger.** session-log:62 says agent lines "go to this build's agent ledger", but the code writes none for this build (handoff.py:769-771).
3. **The stall recorder.** The design's limit signal is stall-recorder's StopFailure record (layer-runtime:396). The hook calls that payload field "UNVERIFIED" (stall-recorder.js:26-30), and it has never fired on this node.
4. **Session ids.** The rule "no session ids" in committed records (dLoggedFlight README:39-41) is enforced only on the runlog record. 133 memory files carry a UUID, and 31 RUN.md `session:` facts are committed.

## 3. Keys

| Source | build | unit | item | role | session | agent | run | SHA | Where it lives |
|---|---|---|---|---|---|---|---|---|---|
| session-log dispatch row | file | implicit | – | ✓ | 8-char prefix | – | – | – | committed |
| agent lines | ✓ | ✓/label | – | ✓ | – | ✓ | wf/direct | – | committed |
| `gov:handoff` marker | ✓ | ✓ | – | ✓ | – | – | – | role-sha, task-sha only | committed |
| agent transcript | – | – | – | agentType | ✓ | ✓ | – | – (branch only) | node, 365 days |
| driver.log | slug | 368 of 1,964 lines | – | – | 983 of 983 starts | – | nonce | – | node |
| gates.log | – | – | – | – | – | – | ✓ | head | node |
| pushes.log | – | – | – | – | – | – | `gate_run` 21 of 80 | ref SHAs | node |
| runlog record | ✓ | ✓ | – | – | refused | – | start SHA | ✓ | committed |
| health.log | – | – | – | – | – | – | – | – | node |
| commits | subject | subject | – | – | – | – | – | ✓ | committed |

**Joins that fail:**
- dispatch row to agent: no shared key;
- agent to the tree it read: no key;
- bar to session or build: 0 of 80 bars;
- reap to bar: time only;
- run record to agent: no key;
- a node's journals to the loop: 20 of 341 landings seen here.

The design adds `task-sha`, item instance and epoch. It never puts one key on every kind, though, and no edge joins them.

## 4. Candidates

The M5 seam is runlog's `build_run_model` (`tools/runlog/model.py`). It already joins 7 sources, so candidate C extends it, and C is ranked against the others like any candidate.

| | A: correlation envelope plus a resolver over P33 edges | B: one append-only span journal (OTel shape), every view derived | C: an index over today's pockets, left where they are (runlog model grown) | D: a causal-parent key per record, with its inverse derived (pick) |
|---|---|---|---|---|
| **Records** | 7 keys on every record: build, item instance, unit, role, session, agent or act, SHA | every event as a span: id, parent, start, end, attributes | nothing new; it joins what exists | each record's own id plus its cause: act→item instance; return→act (`task-sha`, spawn site); verdict→SHA and act-or-binding; journal line→act or epoch; reading→lease; ask→reading or finding. The envelope is derived by walking up. |
| **Cost per event** | about 220 B on every record | about 225 B a line (driver.log: 441,333 B / 1,964 lines) | 0 on write; 0.57 s per run model on read | one field, 40-70 B |
| **Retention** | the record's own | `runtime.journal`, 60 days, node-local | each pocket's own | the record's own; node-local leaves render `not-local` or `pruned` |
| **Reader** | grep, the trace verb | a span viewer | the runlog Skill | `gov trace`, `gov why`, the atlas, the Loop Review |
| **When a worker dies** | the writer stamps; a dead worker writes nothing | a span never closes | heuristic | the act record exists before launch, so a launch with no outcome or child is a visible open leaf |
| **Losing test** | (1) A walk over P33's edges reaches a runtime record. (2) The owner's session-id rule admits the envelope. | Does one node's journal see the loop? Can a committed span carry its times? | Answer the four events with key joins only. | Every designed kind knows its parent's id at write time. |
| **Result** | (1) **Loses:** 0 of the 12 edge types relate act, return, session or verdict (night-pass:255-257). (2) Collides with dLoggedFlight README:39-41. Survives only as a rendered view. | **Loses:** this node saw 20 of 341 landings, and committing journal times breaks the owner's rule (runlog README:402). It survives as Runtime's node journal. | **Loses:** dClosedLoop returns rc=2, E3 and E4 have no run, and 5 joins are by time or prose. It survives as the pre-chain backfill reader. | **Passes** for every designed kind, with the session-binding record as the root of unbound work. The health and stall logs (0 keys) must fold into the journal grammar. |

Cost in D is the act session's own JSON output: `session_id`, `total_cost_usd`, `usage` and `duration_api_ms`, measured at research-runtime-floor-probes:313. The supervisor writes it into the act record with no transcript read.

## 5. The read side

- **The query.** `gov trace <key>` takes any id: a tag, an ask, a SHA, a run, an act, a session or a path. It resolves the key in dOrderedCharter's one tag index, then walks the parent links down. `gov why <key>` walks up only: item, then work order and role-sha, then the instruction units at that SHA, then the request or intake record.
- **The timeline's shape.** One row per record, ordered by its own write time:
  `time · kind · actor (role|command|owner|hook) · item instance · outcome · cost (in/out/cache, wall) · record or journal ref`
- **Three states per row.** Filled; `not-local: node <x>`; or `pruned past runtime.journal`. Never empty, which is the optional-slot rule of v2 `[layers]`.
- **The bound.** E2 alone has 259 model events. So the timeline holds `trace.rows` rows (60 by default) and folds by kind past that, as `tags.bundle-rows` does. Committed rows need one index read and no transcript parse.

## 6. Chain, gaps and forks

**Units by build:**

| Build | Unit |
|---|---|
| dOrderedCharter | the `caused-by` edge, if OB-3 says so, and the `act` and `session` namespaces |
| dTotalRecall | a required `parent` field per record kind, with root kinds declared (intake, session binding, cadence lease). `record` refuses a missing parent. The check runs both ways and is seen red on a planted orphan. |
| dWellOiledMachine | act records gain usage and duration from the act session's JSON; journal lines require `act`/`epoch` or `session`; the health and stall logs fold into the journal grammar; `gov trace` and `gov why` with their fixture: the four events above, replayed as planted records, each answered in one query |
| dWitnessedBar | the verdict record names its bar run and its parent; leg-output tails kept by hash, as OB-4 says |
| dTendedCadence | a reading for acts launched with no outcome past `runtime.act-ceiling`, owned by Runtime |
| dCalibratedLens | the Loop Review prices cost per item kind from trace rows, not only from shape-run rows |

**Gaps to register:**

| Proposed id | What is missing | Evidence |
|---|---|---|
| `gap-rt-25` | no record carries a join key to its cause | §3 |
| `gap-rt-26` | act records carry no cost | layer-runtime:894 |
| `gap-rt-27` | the health and stall logs carry no keys | reap.py:35-41 |
| `gap-mem-35` | P33 relates no runtime kinds | night-pass:255 |
| `gap-test-20` | leg output dies with its worktree | `gate-run/` under `.git/worktrees/` |
| `gap-maint-14` | a dead node's unrecorded run goes undetected | layer-expansions:248 |

**The owner's forks:**

| Fork | Options | Recommendation |
|---|---|---|
| **OB-1** `trace.identity`: what committed records may name | `act-only` (session and agent ids reached through the node's act record), `session`, `salted` | **`act-only`**, which keeps the 2026-09-13 rule |
| **OB-2** `trace.cost`: what committed act records carry | `tokens+wall`, `tokens`, `none` | **`tokens+wall`**. Durations come from process output, not journal times of day; the owner to confirm against the 2026-09-16 rule. |
| **OB-3** the causal parent: an edge or a field | `caused-by` as P33's 13th declared edge (amends NP-15), or a record field outside the edge set | **the edge** |
| **OB-4** `trace.leg-output`: where failing legs' output lives | `tail-by-hash` (committed), `node-local` | **`tail-by-hash`** |
| **OB-5** `trace.rows`: the timeline's bound | 60, 120, `all` | **60** |

I wrote no file in the repository. `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md` showed up untracked during my run, and I did not create it.

**Files read or measured:**
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/runlog/README.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles/handoff.py`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/unattended/stall-recorder.js`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/process-monitor/reap.py`
- `C:/projects/coding-governance/.git/runlog/`
- `C:/projects/coding-governance/.git/health.log`
