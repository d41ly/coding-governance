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
| gap-flow-04 | Flow | MED | A critical planning issue has no path: no recorded plan revision and no re-design inventory of completed work, though none has occurred in 173 builds. Raised by the owner. | flow FL-P6 and its measurement | — |
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
