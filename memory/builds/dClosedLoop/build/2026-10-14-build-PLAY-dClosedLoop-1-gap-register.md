# Gap register — every distance between today's gov and a closed lifecycle loop, with its evidence and its owner

**Serves:** research PLAY-dClosedLoop-1

Derived by the main loop from the six stage-research records in this folder, deduplicated so that
each gap appears once, under the stage whose contract must close it. Severity is the researcher's
unless the row says `(main loop)`. Evidence points at the record and section holding the
measurement; the records hold the file:line citations. The `Owner build` column stays `—` until
the chain opens; the build's acceptance (c) joins that column against the chain READMEs, so every
key below must end up owned by exactly one chain build.

Record shorthand: `plan`, `design`, `build`, `test`, `deploy`, `maintain` name
`build/2026-10-14-build-PLAY-dClosedLoop-1-research-<stage>.md`.

## How the parts interact today: the implicit loop

```text
owner prompt ──► /session-kickoff (card, brief) ──► build README + roster ─────────────► [no plan, no order]
                        │                                                                      ▲
                        ▼                                                                      │ asks, unlabelled,
   reuse probes ──► gov-spec-writer ──► spec (status header) ──► spec audit (opt-in, 3/173)    │ never triaged
                                              │ INPROGRESS, self-set                           │
                                              ▼                                                │
   route on card ──► write gate ──► gov-builder passes ──► closing review (enforced only       │
                                              │              under a mandate)                  │
                                              ▼                                                │
   pre-commit (hand-named legs) ──► pre-push bar (local, bypassable; 70 held legs skipped)     │
                                              │                                                │
                                              ▼                                                │
   push-main lander ──► main ──► remote CI (after the fact, blocks nothing) ──► post-merge     │
                                              │                                (declared in 0/3)
                                              ▼                                                │
   govkit (pull-only) ──► adopters (no CI emitted, no product release contract, 990 behind)   │
                                              │                                                │
                                              ▼                                                │
   SessionStart detectors (drift, procmon, wiring) ──► report only ──────────────────────────────┘
```

The middle of the loop, one unit's Design, Build and Test, is deep: a spec format, a twelve-part
method, role agents, a write gate and a 140-leg bar. The ends are thin or absent: nothing plans
across builds, nothing deploys or verifies a governed product, nothing maintains on a cadence, and
nothing feeds Maintain's findings back into a plan. `tools/roles/workflows.toml` already orders
the middle as stages 0 to 7 (`orient` to `bookkeeping`), and that is the seam a loop definition
extends.

## Cross-cutting themes

- **T1. Deep middle, missing ends.** Plan, Deploy and Maintain carry most of the HIGH gaps.
- **T2. Guards read state the actor writes.** The write gate reads a route and a status the agent
  writes; the build entry trusts a self-set INPROGRESS; review and receipt records are hand-writable.
  The charter's `[class]` rule forbids exactly this, and four of six researchers hit it.
- **T3. The binding verdict is local.** One node's pre-push hook decides; `--no-verify` skips it;
  half the legs never run before a landing; remote CI blocks nothing; the default branch is red today.
- **T4. Two contracts, one loop.** Unattended runs close on a 13-item definition of done; attended
  builds owe the same things in prose.
- **T5. Concurrency is advisory.** The overlap probe always returns 0, claims cover unattended runs
  only and never expire, and 41 live spec pairs from different builds share a path unseen.
- **T6. The loop corrects itself only by adding.** Every confirmed finding becomes a gate or a bug
  class; nothing retires one; the surface grew from 17 to 140 legs in ten weeks.
- **T7. Review lives at two stages.** Design (opt-in) and Build (closing review); none at Plan, Test,
  Deploy or Maintain, and none of the loop itself.
- **T8. The product and gov's own governance are one body.** Adopters get partial contracts: no
  product-test shape, no release contract, no emitted CI, no currency watch.

## Register

| Key | Stage | Sev | Gap | Evidence | Owner build |
|---|---|---|---|---|---|
| gap-found-01 | Foundation | HIGH | No instruction hierarchy: about 25 load-bearing documents (about 551 KB) reach agents by six routes at different times, carry no identity or rank, and state precedence only for kickoff; nothing restores their order after a context reset. Raised by the owner. | foundations step 1, current state | — |
| gap-found-02 | Foundation | HIGH | The charter's practices are one-line rules without reach: no stage contract, role or review lens reads them, and an adopter's methodology has no home but free prose. Raised by the owner. | foundations step 1, current state | — |
| gap-found-03 | Foundation | HIGH | Subagents load no charter (`omitClaudeMd: true`) and receive unranked charter fragments, with nothing ordering charter, role and task. Raised by the owner. | foundations step 1, current state | — |
| gap-found-04 | Foundation | MED | No rule and no record governs a live instruction that conflicts with the charter. Raised by the owner. | foundations step 1, F1-1 | — |
| gap-found-05 | Foundation | HIGH | The charter does not teach an agent how to drive gov for its role: its generated tool lines say what each tool answers, so every agent re-derives how to start and advance the loop from many files. Raised by the owner. | foundations step 1 continued, current state | — |
| gap-found-07 | Foundation | HIGH | No principle declares its enforcement: 22 of the charter's 36 practices are cited by no code file, no leg names the principle it enforces (0 of 140), and nothing stops a principle existing only as prose. Raised by the owner. | foundations core, current state and instrument | — |
| gap-found-08 | Foundation | HIGH | Extensions are hand-made: factories exist for 3 of 13 extension kinds (kit adoption, builds, micro-specs), so a new kit, command, document, policy key, leg, role, workflow, hook or Skill conforms only if its author remembers every rule. Raised by the owner. | foundations core, current state | — |
| gap-found-06 | Foundation | HIGH | No tool names the next step: six adopt scripts print install hints and nothing else ends with the caller's next command, so the loop advances only by agents re-deriving it. Raised by the owner. | foundations step 1 continued, current state | — |
| gap-flow-01 | Flow | HIGH | No feature level between build and unit: the interfaces between a feature's units have no record, so a change that breaks a feature cannot be told from one that touches a unit, and re-design has no granularity but the unit. Raised by the owner. | flow FL-D2, FL-D4, FL-D5 | — |
| gap-flow-02 | Flow | HIGH | The decision principles that resolve unattended forks (the most feature-rich option, then the most expandable, fully recorded) are stated nowhere; M3 names feature-rich only, and nothing ranks them above the charter's adjustable practices. Raised by the owner. | flow FL-D3, FL-D6; `memory/guides/BUILD-METHOD.md` M3 | — |
| gap-flow-03 | Flow | MED | The plan is written up to three times (README, brief, card) and the levels of card, plan and brief are declared nowhere. Raised by the owner. | flow Plan, current state; FL-P2, FL-P5 | — |
| gap-flow-05 | Flow | MED | Built specs are revised retroactively: a closing review's blockers can be folded into an already-built unit as a spec revision (dSweptBranches, "the blockers folded into unit 3 rev-3"), so the trail of what was built against which spec breaks. Raised by the owner. | flow FL-B3; `memory/builds/dSweptBranches/README.md` | — |
| gap-flow-06 | Flow | HIGH | No cross-build coordination: a build cannot reach the session working on a build it depends on, no message survives a session, and a dependency gates nothing. Raised by the owner. | flow interactions FI-2, FI-5, FI-6 | — |
| gap-flow-07 | Flow | MED | A build whose units sit in different steps has no defined step, and a session's card does not follow its build across transitions. Raised by the owner. | flow interactions FI-1, FI-8 | — |
| gap-flow-08 | Flow | MED | Landing order among builds verified at once is undefined; the first landing silently stales the others' verdicts. Raised by the owner. | flow interactions FI-7 | — |
| gap-flow-09 | Flow | MED | A merge conflict between a build and the default branch's tip has no route. Raised by the owner. | flow interactions FI-3 | — |
| gap-flow-04 | Flow | MED | A critical planning issue has no path: no recorded plan revision and no re-design inventory of completed work, though none has occurred in 173 builds. Raised by the owner. | flow FL-P6 and its measurement | — |
| gap-orient-01 | Orient | HIGH | Placement is unaided and unrecorded: kickoff tells the agent to derive a request's scope itself, an unattended run handed a prompt always opens a new build, and only 6 of 131 recent builds name a predecessor, so a mis-placement cannot be audited; path overlap cannot decide placement (the named predecessor ranked first 0 of 5 times). Raised by the owner. | orientation research, routing; `skills/session-kickoff/SKILL.md:126-131`; `tools/unattended/SKILL.template.md:28-32` | — |
| gap-orient-02 | Orient | HIGH | Nothing binds a session to its build: the route check verifies existence and pairing only, so a route to a terminal build or to another session's build lands, and a resumed route is never re-checked. Raised by the owner. | orientation research, routing; `skills/session-kickoff/manifest-check.sh:995-1001` | — |
| gap-orient-03 | Orient | HIGH | A build's position is read from typed state: a unit's step and pass come from status headers and RUN.md's phase, all 10 INPROGRESS units sat idle 8 days or more, no resolver says which pass is due, and `LIVE.md` inherits 7 of 30 stale non-terminal headers. Raised by the owner. | orientation research, routing (c) and trust | — |
| gap-orient-04 | Orient | HIGH | Orientation is exploratory: a new session spends a median 35 tool calls and 146k fresh input tokens before its first productive write, 20% of them locating the work or re-reading git state; kickoff's Step 1 orders re-deriving what the card printed (median 6 calls), and READY reaches the card in 19 of 64 sessions. Raised by the owner. | orientation research, cost; `skills/session-kickoff/SKILL.md:49-56` | — |
| gap-orient-05 | Orient | HIGH | Claims carry no freshness keys: the card's cells go stale unmarked, the replay's `now —` line read the primary tree instead of the session's worktree, and 4 of 17 run claims disagree with their RUN.md, so a session cannot tell a fresh claim from a stale one without re-deriving it. Raised by the owner. | orientation research, trust; `skills/session-kickoff/manifest-check.sh:499`; this session's compact hook output | — |
| gap-orient-06 | Orient | MED | Resuming costs more than starting: a resume caches the whole context again (median 467k fresh input tokens, against 146k for a new session), and a compaction spends a median 15 calls re-reading content. Raised by the owner. | orientation research, cost | — |
| gap-orient-07 | Orient | MED | Briefs carry pointers, not facts: briefed agents spend 15% of their calls on method documents and 15% locating, agents read their own prompt file 10 times, and `role-sha` is never compared with the role it was rendered from. Raised by the owner. | orientation research, cost P4 and P6; `tools/hooks/agent-cap.js:55-60` | — |
| gap-orient-08 | Orient | HIGH | Work is bound to no checklist item: about 63% of main-loop tool calls follow no protocol step, typed role agents are 4.1% of subagents, a harness branches on free text, and researcher returns are unchecked (5 of 10 ended without a final turn). Raised by the owner. | orientation research, determinism; `tools/workflows/unattended-unit.js:348` | — |
| gap-orient-09 | Orient | HIGH | Allowances escape in the field: the role-gate arm let 34 typed gate runs through though a replay of the same commands is refused, cause unknown, and the `none` and `review` write classes are declared but read by nothing. Raised by the owner. | orientation research, determinism probes 2 and 3; `tools/hooks/scratch-guard.js:101-104` | — |
| gap-orient-10 | Orient | MED | Memory loads unchecked: 12 of the 98 paths the auto-memory names no longer exist, and the dangling-pointer signal only reports. Raised by the owner. | orientation research, trust; `tools/drift-audit/drift_signals.py:470` | — |
| gap-orient-11 | Orient | HIGH | A build's card cannot be found by its build: cards are keyed by session id in the clone's git directory, so a new session, a dead process or another node never finds the card of the build it picks up, and no card exists on the remote. Raised by the owner. | orientation research, preserve; `skills/session-kickoff/manifest-check.sh:311-316` | — |
| gap-orient-12 | Orient | HIGH | A resume delivered no card: in this session the resume hooks printed only the process and wiring checks, though the replay is wired for resume; the cause is unknown. Raised by the owner. | orientation research, preserve (this session's transcript, the resume at 16:21:01Z) | — |
| gap-orient-13 | Orient | MED | The card never reaches the charter's instruction slot: hook output lands as a reminder at the hook point, subagents (`omitClaudeMd: true`) get only the route, and another harness gets nothing. Raised by the owner. | orientation research, preserve; `tools/roles/render_agents.py:132`; https://code.claude.com/docs/en/hooks | — |
| gap-roles-01 | Roles | HIGH | Most checklist items have no role: of 70 items across the steps, 11 are performed by a role, 18 by the main session, 9 by a command and 32 by nobody; no role exists for planning, feature design, testing, deployment, maintenance or the Plan, Test, Deploy and Loop reviews. Raised by the owner. | roles research, coverage | — |
| gap-roles-02 | Roles | HIGH | The main session performs role functions: in 60 days it wrote or edited specs 605 times, product code 565 times, folded review findings 367 times, and wrote plans 336 times and task briefs 74 times. Raised by the owner. | roles research, coverage P2 and P5 | — |
| gap-roles-03 | Roles | HIGH | Role limits are prose: 58 of the 59 prohibitions in role bodies name no enforcer, `writes` is a class rather than an allowance, and shell writes escape every role gate (85 from the main session and 66 from typed roles since the role arm landed). Raised by the owner. | roles research, anatomy probe 3, coverage P4 | — |
| gap-roles-04 | Roles | HIGH | Returns between roles are uncontracted on the direct route: 48 of 48 direct-spawn returns are free text, `returns` is prose no code reads, and no subagent-stop check exists. Raised by the owner. | roles research, prior art probe C, anatomy | — |
| gap-roles-05 | Roles | HIGH | Exchanges between roles are retyped by the main session: 64.5% of a rendered task's bytes are typed input, 71 of 126 direct spawns carried free-text prompts, and 844 of 901 spec fold commits came from no unit. Raised by the owner. | roles research, interactions probes 3, 4 and 7 | — |
| gap-roles-06 | Roles | HIGH | The guard shares state with what it guards: the role index and agent files sit outside every role gate, so a role holding Write could edit them, and a tree with no role index is unarmed. Raised by the owner. | roles research, anatomy; `tools/hooks/scratch-guard.js:99-101` | — |
| gap-roles-07 | Roles | MED | Roles go unused or double up: the orienter, reuse scout and diff reviewer had no spawn in 60 days, the reuse scout's body adds nothing, the spec writer also holds disposal, and the session-handoff template has no agent. Raised by the owner. | roles research, coverage P6 | — |
| gap-roles-08 | Roles | MED | The work order names no checklist item, allowance or witness key, and a builder's divergence returns to "the caller" with no route back. Raised by the owner. | roles research, anatomy; `tools/workflows/unattended-unit.js:269` | — |
| gap-spine-01 | Spine | HIGH | No stage model: no kit, leg, dossier, role or hook declares the stage it serves, and the loop exists only implicitly. | design §4.1 (0 of 31 dossiers carry a stage); `tools/roles/workflows.toml` covers stages 0–7 only | — |
| gap-spine-02 | Spine | HIGH | Guards read agent-written state across stages, against `[class]`. | build §4 (write gate), design §4.4 (INPROGRESS), test §5 C (pusher-written receipt), deploy §5 C | — |
| gap-spine-03 | Spine | HIGH | Attended and unattended builds run different exit contracts. | build §3, §4 (DoD needs RUN.md) | — |
| gap-spine-04 | Spine | MED | gov's own governance and the shipped product are one body; adopters receive partial stage contracts. (main loop) | test §4, deploy §4; `.claude/rules/product.md` | — |
| gap-spine-05 | Spine | MED | Protocol volume: guides 301 KB, runbook 163 KB, unattended guides about 216 KB. (main loop) | maintain instrument 2; `wc -c` of `memory/guides/` | — |
| gap-spine-06 | Spine | HIGH | No single answer to "what is this repo's policy": per-repo configuration spans at least eight surfaces holding about 160 keys, owner choices mixed with kit mechanics. Added after round 4. (main loop) | design-rounds R4; five dotfile confs hold 138 keys | — |
| gap-conc-01 | Spine | HIGH | Cross-build and cross-node overlap is advisory: the probe always returns 0 and sees only pushed refs; no unit or path claim exists. | build §4, design §4.2 (41 pairs across 22 build pairs) | — |
| gap-conc-02 | Spine | MED | Claims never age, name a user rather than a fleet tag, and cover unattended runs only; slug uniqueness is checked against local history only. | plan §4 (8 of 17 held, 17 of 17 user names) | — |
| gap-conc-03 | Spine | MED | `[isolate]` has no mechanism: harness passes share one worktree and meet git's index lock. | build §4 | — |
| gap-plan-01 | Plan | HIGH | No priority, order or dependency record across builds and asks. | plan §4 (absent; TOOL-aBoundedVerdict-7 DEFERRED) | — |
| gap-plan-02 | Plan | HIGH | Triage is never drained: 435 of 521 live asks unlabelled; 297 deferred onto one owner-triage ask open since 2026-10-05; no role owns triage. | plan §4 | — |
| gap-plan-03 | Plan | HIGH | The asks pipeline is not the real intake: 165 of 167 builds came from prompts, and a prompt yields a one-build brief, never a plan. | plan §2, §4 | — |
| gap-plan-04 | Plan | HIGH | Nothing reviews a plan, a backlog or a priority order. | plan §4 | — |
| gap-plan-05 | Plan | HIGH | Dormant work is labelled, never disposed: 21 of 25 live builds dormant. | plan §4; maintain instrument 1 | — |
| gap-plan-06 | Plan | MED | Most OPEN asks are not ready to build: 94 of 218 grade `no`, 132 lack an acceptance. | plan §4 | — |
| gap-plan-07 | Plan | MED | The brief is gated only for units a run built; attended briefs are stated. | plan §4 | — |
| gap-design-01 | Design | HIGH | No record holds an architecture above one unit; the map is an inventory. | design §4.1 | — |
| gap-design-02 | Design | HIGH | Design conflicts between builds are invisible: 25 non-registry shared paths between live specs, 21 with an INPROGRESS side. | design §4.2 | — |
| gap-design-03 | Design | HIGH | Design review is off by default: 3 of 173 builds declare an audit; 503 of 989 Tier-2 specs unaudited. | design §4.3 | — |
| gap-design-04 | Design | HIGH | The hand-off to Build ignores design state: a FORKED unit at INPROGRESS is admitted. | design §4.4 (TOOL-dNarrowedAnchor-1) | — |
| gap-design-05 | Design | MED | Nothing checks that a spec's reuse audit is true; 142 of 978 cite no probe. | design §4.5 | — |
| gap-design-06 | Design | MED | Rejected design candidates are unchecked; 95 of 978 Tier-2 specs record none. | design §4.6 | — |
| gap-design-07 | Design | MED | The reuse stage is neither enforced nor recorded, and research has no harness (7 research records in 173 builds). | design §4.7, §4.8 | — |
| gap-design-08 | Design | MED | Audits never come back clean: 0 of 254, 170 BLOCKED; nothing measures whether specs reach review short of their bar or the bar moves. (main loop) | design §4.3 | — |
| gap-design-09 | Design | LOW | Sub-spec agreement, tier assignment and unpushed specs are prose or invisible. | design §4.9–4.12 | — |
| gap-build-01 | Build | HIGH | Scope is not bound to the unit: 120 of 584 unit-attributed product commits touched files outside their unit (42 of 582 at kit granularity). | build §4 | — |
| gap-build-02 | Build | HIGH | The attended closing review is unenforced: 29 of 59 attended builds with a CLOSED unit carry one, against 86 of 89 unattended. | build §4 | — |
| gap-build-03 | Build | MED | Bash and PowerShell product writes escape the write gate. | build §4 | — |
| gap-build-04 | Build | LOW | The per-pass bug-class checklist is unverified, and agents a harness spawns are uncounted. | build §4 | — |
| gap-test-01 | Test | HIGH | Kit self-tests, 70 of 140 legs and 23,494 s of 28,066 s summed maxima, are on no pre-landing path. | test §4 | — |
| gap-test-02 | Test | HIGH | The binding verdict is one node's bypassable hook; remote CI blocks nothing; the default branch reds memory hygiene today. | test §4; maintain instrument 4 | — |
| gap-test-03 | Test | HIGH | Adopters get no product-test contract: no test levels, selection, or flake policy; their manifest starts empty. | test §4 | — |
| gap-test-04 | Test | MED | Flakes: one timeout retry only, no quarantine or flake record. | test §4 | — |
| gap-test-05 | Test | MED | A green is not shared across nodes: the stamp is local and no green ref exists. | test §4 | — |
| gap-test-06 | Test | MED | "A gate never seen red is not a gate" has no recorder. | test §4 | — |
| gap-test-07 | Test | MED | The pre-commit leg list is hand-named. | test §4 | — |
| gap-test-08 | Test | MED | Cost evidence is thin: 21 legs have no ceiling evidence, all from one node, and no whole-bar wall time is recorded (records claim 4–7 h). | test §4 | — |
| gap-test-09 | Test | LOW | A stale README example, 8 unguarded held legs, and a PowerShell scan on no leg. | test §4 | — |
| gap-deploy-01 | Deploy | HIGH | An adopter's own release, environments, rollout, rollback and post-deploy verification are not addressed; one adopter built all of it outside gov. | deploy §4 | — |
| gap-deploy-02 | Deploy | HIGH | The post-landing verdict is inert: `GATE_POST_MERGE` declared in 0 of 3 trees, `refs/gov/bar-red` absent, CI cannot publish. | deploy §4 | — |
| gap-deploy-03 | Deploy | HIGH | No CI job is emitted into adopters; one adopter's six workflows never call the bar. | deploy §4 | — |
| gap-deploy-04 | Deploy | HIGH | Adopter currency is unwatched: receipts 990 commits behind after six days; `update` is pull-only; no fleet register. | deploy §4 | — |
| gap-deploy-05 | Deploy | MED | Outbox orders are graded by nothing (one adopter holds 16, five of them rollbacks). | deploy §4 | — |
| gap-deploy-06 | Deploy | MED | Landing and release have no review, no role and no changelog. | deploy §4 | — |
| gap-deploy-07 | Deploy | MED | A killed hook on Windows still lands an ungated push; hooks-path drift is only a note; the lander kit is unversioned with an undeclared dependency. | deploy §4 | — |
| gap-deploy-08 | Deploy | LOW | The runbook is 163 KB of narrative under an existence-only parity check; `[isolate]` ports and the `up —` line are stated only. | deploy §4 | — |
| gap-maint-01 | Maintain | HIGH | No cadence: nothing runs on a schedule except an unattended run's own keepalive. | maintain §4 | — |
| gap-maint-02 | Maintain | HIGH | Detectors without owners: 15 of 27 drift signals nonzero, most report-only, 2 dead probes. | maintain §4, instrument 1 | — |
| gap-maint-03 | Maintain | HIGH | The governing surface only grows, and nothing prices or retires a leg, rule or bug class. | maintain §4, instrument 2 | — |
| gap-maint-04 | Maintain | HIGH | Records dominate the work: 1,598 of 2,827 commits in 30 days touched only `memory/`. (main loop) | maintain instrument 3 | — |
| gap-maint-05 | Maintain | MED | Run records and dormant builds never close: 89 live `RUN.md`, 10 non-terminal for merged work. | maintain §4 | — |
| gap-maint-06 | Maintain | MED | The map goes stale: 28 of 31 dossiers older than their paths. | maintain §4 | — |
| gap-maint-07 | Maintain | MED | Ratchets that should shrink do not (3 of 5), timeouts are retried and forgotten, and reaping is manual. | maintain §4 | — |
| gap-maint-08 | Maintain | LOW | Naming offense rate and dangling ledger pointers are report-only. | maintain §4 | — |
| gap-review-01 | Review | HIGH | Review exists at two stages only; Plan, Test, Deploy and Maintain have none. | every record §3 | — |
| gap-review-02 | Review | HIGH | No review of the loop itself: no retrospective reads the loop's metrics and changes a stage contract. | maintain §3, §4 | — |
| gap-review-03 | Review | MED | Review cost is high, about 9 agents and 0.81 M tokens per spec audit, and is why audits are off by default. | design §5 C3 | — |

The counts are derived, never typed: a first draft typed 59 rows here over a table holding 56. The
instrument, run against this file, and its output when the register was written:

```bash
grep '^| gap-' <this file> | awk -F'|' '{gsub(/ /,"",$3); gsub(/ /,"",$4); s[$3]++; v[$4]++} END {for (k in s) printf "%s=%d ", k, s[k]; print ""; for (k in v) printf "%s=%d ", k, v[k]; print ""}'
```

```text
Deploy=8 Plan=7 Spine=8 Test=9 Review=3 Build=4 Maintain=8 Design=9
LOW=5 MED=23 HIGH=28
```

Re-measured after round 4 added `gap-spine-06`, same instrument:

```text
Deploy=8 Plan=7 Spine=9 Test=9 Review=3 Build=4 Maintain=8 Design=9
LOW=5 MED=23 HIGH=29
```

Re-measured after the foundations revisit's step 1 added the four owner-raised `gap-found-*` rows,
same instrument:

```text
Deploy=8 Plan=7 Spine=9 Test=9 Review=3 Foundation=4 Build=4 Maintain=8 Design=9
LOW=5 MED=24 HIGH=32
```

Re-measured after step 1's continuation added `gap-found-05` and `gap-found-06`, same instrument. The
Stage column groups the owner's foundations; `gap-found-06` is owned by the Spine, which builds the
`next` verb:

```text
Deploy=8 Plan=7 Spine=9 Test=9 Review=3 Foundation=6 Build=4 Maintain=8 Design=9
LOW=5 MED=24 HIGH=34
```

Re-measured after the core consistency step added `gap-found-07` and `gap-found-08`, same instrument:

```text
Deploy=8 Plan=7 Spine=9 Test=9 Review=3 Foundation=8 Build=4 Maintain=8 Design=9
LOW=5 MED=24 HIGH=36
```

Re-measured after the flow walk's Plan and Design stages added four `gap-flow-*` rows, same
instrument:

```text
Deploy=8 Plan=7 Flow=4 Spine=9 Test=9 Review=3 Foundation=8 Build=4 Maintain=8 Design=9
LOW=5 MED=26 HIGH=38
```

Re-measured after the flow walk's Build stage and the flow-interactions round added `gap-flow-05`
to `gap-flow-09`, same instrument:

```text
Deploy=8 Plan=7 Spine=9 Test=9 Review=3 Foundation=8 Build=4 Flow=9 Maintain=8 Design=9
LOW=5 MED=30 HIGH=39
```

Re-measured after the orientation round added `gap-orient-01` to `gap-orient-10`, measured by the four
orientation researchers and the main loop, same instrument:

```text
Deploy=8 Plan=7 Spine=9 Orient=10 Test=9 Review=3 Foundation=8 Build=4 Flow=9 Maintain=8 Design=9
LOW=5 MED=33 HIGH=46
```

Re-measured after the adopted preservation research added `gap-orient-11` to `gap-orient-13`, same
instrument:

```text
Deploy=8 Plan=7 Spine=9 Orient=13 Test=9 Review=3 Foundation=8 Build=4 Flow=9 Maintain=8 Design=9
LOW=5 MED=34 HIGH=48
```

Re-measured after the roles round added `gap-roles-01` to `gap-roles-08`, measured by the four roles
researchers, same instrument:

```text
Roles=8 Deploy=8 Plan=7 Spine=9 Orient=13 Test=9 Review=3 Foundation=8 Build=4 Flow=9 Maintain=8 Design=9
LOW=5 MED=36 HIGH=54
```
