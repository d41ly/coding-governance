# Research: stall and loop scenarios in the converged design

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 145's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-20-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-stall-and-loop.md`.

---

**THE SCENARIOS: where the converged design stalls or loops without end (research return, PLAY-dClosedLoop-1)**

Nothing in the repository was written. Two probes ran on copies in the session scratchpad, and both copies are deleted. No gate leg or test suite was run.

**Record keys used in the citations below.** All files are under `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\`:
- `v2` = `2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
- `steps` = `2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`
- `rt` = `2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`
- `roles` = `2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md`
- `instr` = `2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md`
- `mem` = `2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`
- `exp` = `2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`
- `adopt` = `2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md`
- `np2` = `2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`
- `fi` = `2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md`
- `coord` = `2026-10-14-build-PLAY-dClosedLoop-1-coordination.md`
- `fr` = `2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md`
- `rl` = `2026-10-14-build-PLAY-dClosedLoop-1-roles.md`

## Probes, as measured

**P1. The resume attempt cap resets on any move.** I copied `derive_attempts` from `tools/unattended/resume-tick.sh:228` into a scratch fixture. The sidecar held 10 attempts, one every 10 minutes:
```
A last-move 300s ago:  lifetime=10 consecutive=0 (cap 6 -> exhausted? no)
B last-move 7200s ago: lifetime=10 consecutive=10 (cap 6 -> exhausted? yes)
```
This matches the code's own comment, "THE ATTEMPT CAP IS CONSECUTIVE, NOT LIFETIME… a transcript-only move resets the count too" (`resume-tick.sh:70-74`), and `RESUME_ATTEMPTS_DEFAULT=6` (`:121`). `rt [supervise]` says the supervisor "keeps what that seam already proves: the attempt cap". So an act that writes anything at all never exhausts the cap.

**P2. A census of the routes in `steps`' item tables.** The script found `items=89 items-with-loop-or-wait-route=23 with-bound-in-cell=6 without=17`.
- 13 of the 17 rely on `steps [rules]`'s general `flow.route-backs` clause: `build.acceptance`, `build.core`, `design.input`, `design.ready`, `design.research`, `entry.place`, `plan.dedupe`, `review.fold`, `test.attribute`, `test.merge`, `test.route`, `test.seen-red`, and `deploy.current`/`test.verdict` on staleness.
- The other 4 are waits that clause does not cover:
  - `deploy.parents` "holds";
  - `build.ratify` "until";
  - `adopt.practices` "until".
- The census is a regex match, so it is approximate.

**Tree measurements.**
- `tools/unattended/unattended.sh` is 14,346 lines and 995,424 bytes.
- `tools/gate-legs.json` was touched by 60 commits since 2026-09-19.
- `main` took 353 first-parent commits since 2026-09-19.

## Ambiguities in the sources that decide whether a guard binds

- **A1. "Route back" is never defined.** `steps [rules]` counts route backs "in the build's transition record" and trips when one "returns to the same item". `rt [decide]` lists four kinds: a failed check back to `entry.place`, a fix pass, a review's next round, and a backward transition. Undefined:
  - whether a stale verdict or a merge conflict counts;
  - whether a new unit, which is a new item instance, counts;
  - whether a route back before the claim counts, when no build record exists yet.
- **A2. What happens once the route-back count is passed.** The loop becomes an owner item "resolved as [breakpoint]'s owner gate is". Under the default `best-effort-recorded`, that gate is the supervisor's own recorded choice (`steps [breakpoint]`). Nothing declares the owner item's outcome set, or whether the count resets after it is resolved.
- **A3. `flow.adapt`'s "stricter values" is undefined for loop-bound keys** (`np2 [p1-scenarios]` 4). `adopt [design]` 10 declares a widening order for row fields only, not for policy values.
- **A4. Whether `runtime.act-ceiling` bounds command items** run by the supervisor, such as `test.verdict` on a remote backend.
- **A5. Composition refusal versus the admission clamp.** A policy write that lowers `runtime.agents-in-flight` below a shape's stage cap could be refused at composition (`adopt [design]` 9) or clamped at admission (`np2 [answers-reviewed]`). The records do not say which applies.
- **Records versus code.**
  - `steps [open]` S-1 names four driver loop states. The code also exits `CEILING` (`unattended.sh:11723`, `check-unattended.sh:844`).
  - v2's `RUNAWAY_CEILING` matches `unattended.sh:774` (`"8"`), with the refusal at `:783`.
  - The handed bounds (route-backs 3, retries 3, act ceiling 1.5 h, hold ceiling 6 h, leases 24 h, release ceiling 72 h) match `v2 [policies]`.
  - `roles.retries` covers only a value that fails to resolve, never a refusal (`rl` RL-7).

## Scenarios

Likelihood is graded 1 to 5 under the defaults: the `standard` preset, unattended, `run.on-owner-question: best-effort-recorded`.

| id | layer | trigger | cycle or wait | guard today | detector signal | cost of one turn | likelihood |
|---|---|---|---|---|---|---|---|
| SC-flow-1 | flow | any loop passes `flow.route-backs` (3) | an owner item is resolved by the supervisor's best-effort choice, the loop resumes, and every extra lap raises another owner item (A2) | `steps [rules]`, `steps [breakpoint]`: a count with no stop | the same (build, item) owner item resolved by the supervisor more than once | one lap of the loop it bounds | 4 |
| SC-flow-2 | flow | the owed closing review keeps finding HIGHs | findings become units (P19), go through Design and Build, then `review.follow-up: after-high` runs again, and so on (the owner's own example) | `steps [rules]` (rounds count), then SC-flow-1 | the HIGH count does not fall across rounds; new findings land only on the new units | a Tier-2 fan plus spec writers and builders. This build's own fold pairs confirmed 19 and 31 defects (`np2 [reviewed]`) | 5 |
| SC-flow-3 | flow | a deterministic refusal of an item: hook, allowance, render, ask filing | "a refusal… `next` returns the frontier" (`steps [rules]`), and the item is still on it. "An unwitnessed one can always be dispatched again" (`rt [invariants]` once-per-instance). Neither `blocked` nor `stuck` fires (`rt [decide]`) | none: retries cover resolve failures only (`rl` RL-7) | the same instance dispatched N times with the same refusal class and no new witness | one act: prompt writer plus role agent, up to `RESUME_TURNS` 40 | 4 |
| SC-flow-4 | flow | another build lands first | `deploy.current` reads stale, the build goes back to Test and re-verifies (`fi`: "each landing makes the others' verdicts stale"). A low-priority build starves. If staleness counts (A1), 3 landings by others raise a false owner item | `gap-flow-08`: no landing queue exists | stale count per build; the verdict tree hash changes while the build's own commits do not | a bar run plus a prepared merge; gov runs about 12 landings a day (measured) | 4 |
| SC-flow-5 | flow | `placement.check: refuse` fails the scout's return | `entry.place` loops on itself before any claim, so there is no transition record to count in (A1) | none before the claim | the same intake content key placed more than N times | one scout act in the owner's session | 2 |
| SC-flow-6 | flow | a cold tester (`roles [trust]` 6) flips between code-miss and spec-wrong | the build oscillates between a fix pass in Build and a new unit through Design, and each new unit is a new instance (A1) | `steps [rules]`, if backward transitions count | the same red leg with alternating `test.attribute` judgments | tester plus builder or spec writer, plus a bar | 3 |
| SC-flow-7 | flow | an `awaiting` item with no ceiling (`build.ratify`, `adopt.practices`, `deploy.parents`) | it holds forever: `awaiting` "raises no owner item itself", and only the release and hold ceilings exist (`rt [decide]`) | none | awaiting age past a deadline with an unchanged witness set | wall time, the lease held, dependents blocked | 3 |
| SC-flow-8 | flow | a different leg flakes on each lap | each `test.flakes` re-entry counts on the build, leading to SC-flow-1 | `steps` `test.flakes` | rising re-entry count with a different leg each time | a bar run | 2 |
| SC-flow-9 | flow | a blocking CONTENDED red (non-default `verdict.blocks`) | "a re-run on a quiet host", and no quiet host ever appears | none in the cell | repeated contended re-runs | a bar run | 1 |
| SC-instr-1 | instruction | a load set missing a `required-by` unit (a gov rename, or a patch held under `instructions.stale`) | "A refusal leaves the spawn undone, and the caller files an ask" (`instr [recommendations]` R-C), then SC-flow-3 | none on repetition | the same (item, missing unit) refusal each beat; the same ask key re-filed | a render plus an ask; the build is blocked | 3 |
| SC-instr-2 | instruction | required units alone exceed the harness's own limit | always refused whatever `budgets.enforce` says (`instr [recommendations]`); demoting inputs does not help | `roles [trust]` 1 covers inputs only | the same over-limit refusal each beat | a render; the build is blocked | 2 |
| SC-instr-3 | instruction | the live charter's `[verify]` ("verify every claim… by reading the code") conflicts with P29 until dConvergedCharter | the agent re-reads handed ranges, which leads to SC-roles-1 | none until the charter is rewritten | answered-call refusals per act above a threshold | turns burnt per act | 4 |
| SC-instr-4 | instruction | the fix needs an instruction change, and agents may only propose one (`instructions.edit`) | the unattended build waits on the owner's command | none | an open proposal while the item is refused | wall time | 3 |
| SC-instr-5 | instruction | `instructions.stale: refuse` (non-default) | a gov update is held until the owner re-pins, and builds needing it wait | `v2 [policies]` (owner) | the update held past N days | wall time | 1 |
| SC-roles-1 | roles | `roles.answered-calls: refuse` and a role that re-verifies by habit | Read refused, then Grep, then shell readers, until max turns; relaunch; the attempt cap resets (P1) | `roles [trust]` 10 names the anchor | the same refusal class repeated within one act | up to 40 turns per act | 4 |
| SC-roles-2 | roles | a return names a commit the stale-epoch queue refused | 3 retries (`rl` RL-7), then the item "parks", with no ceiling on the park | `rl` RL-7 | a parked item's age | 3 role acts, then a wait | 2 |
| SC-roles-3 | roles | two roles disagree on one keyed fact | repair, then contradiction, then a divergence back to the producer, then a repair again (`roles [trust]` 7) | `flow.route-backs` | one fact key's value oscillating | two acts per lap | 2 |
| SC-roles-4 | roles | a unit touching `unattended.sh` (995,424 bytes) | over budget, so it routes back to the architect for a split; a single-file unit cannot split; then SC-flow-1 | `roles [trust]` 1 (counted) | the same unit split again with its packet size unchanged | architect act per lap | 3 |
| SC-roles-5 | roles | the tester says code-miss, but the test is wrong | a fix pass may not edit the test (`steps [test]`: "A fix pass keeps its check"); acceptance fails; fix pass again | `rt [decide]` (fix pass counted) | the same acceptance red after every fix pass | builder plus acceptance re-run | 3 |
| SC-roles-6 | roles | a harness script spawns an unnamed agent | the act's witness is voided (`rt [invariants]` named-acts) and the same script re-runs | none | voided witness on the same act each time | a whole fan | 2 |
| SC-mem-1 | memory | a filer with no mechanical acceptance under `asks.acceptance: refuse` | "An item that cannot file routes as any refusal does: `next` returns its frontier" (`mem [asks]`), then SC-flow-3 | none | the same ask refused each beat | an act plus a refusal | 3 |
| SC-mem-2 | memory | the lexicon installed (gov dogfoods it), `lexicon.at-commit: refuse` plus `drift: refuse-new` | a builder that must coin a term is refused at every commit, so the pass never commits; relaunch; the cap resets (P1) | none | the same lexicon refusal per commit attempt | an act up to 40 turns | 3 |
| SC-mem-3 | memory | `memory.map-purpose: review` on a new node | "derive… or consult with the owner" (`v2 [policies]`), so the unit waits | none | open map-purpose consults | wall time | 2 |
| SC-mem-4 | memory | a frozen spec (P19) cites a tag retired mid-flight under `tags.retired-cites: refuse-new` | the builder cannot comply, diverges, and the spec stays frozen, so a new unit is needed | `flow.route-backs` | a refused cite of a retired tag | builder plus spec writer | 2 |
| SC-mem-5 | memory | many writers on one compare-and-swap ref (class claims, leases) | retry and yield; the mailbox was already fixed: one ref per build took 4.5 times the ideal attempts at eight writers (`np2 [p3-storage]`) | `steps` `review.report` (counted) | the compare-and-swap attempts-per-write ratio | network round trips | 1 |
| SC-rt-1 | runtime | an act that writes or adds transcript before dying | the consecutive cap never fills (P1), so relaunches never stop | `rt [supervise]` relaunch (as inherited) | lifetime attempts far above `RESUME_ATTEMPTS` with no witness | up to 1.5 h and 40 turns per lap | 4 |
| SC-rt-2 | runtime | the dispatcher cannot run, for example after a CLI payload change | under `hook-failure: closed`, every gated call is denied (`rt [invariants]` fail-closed); every act fails and relaunches | preflight only | a denial rate of 100% across acts | every act on the node | 2 |
| SC-rt-3 | runtime | a weekly session limit | the supervisor holds launches and keeps renewing its lease; past 6 h it raises an owner item "and keeps holding" (`rt [supervise]`); no node with quota can take over | `runtime.hold-ceiling` (notification only) | hold age while the lease beats | days of wall time; dependents blocked | 3 |
| SC-rt-4 | runtime | a killed or crashed agent with no SubagentStop or saved result | the reservation leaks in a live session and every spawn queues forever (`rt [supervise]` Agents in flight; `np2 [p7-agent-cap]`: the event is unmeasured) | a sweep for dead sessions only | queue wait past a deadline while ledger slots are older than the act ceiling | the whole session | 3 |
| SC-rt-5 | runtime | the agent limit lowered below a shape's stage cap | composition fails, `invalid-input` "refuses to act, and journals it", and no owner item is raised (`rt [decide]`; A5) | none | `invalid-input` on every beat | a silent stall | 2 |
| SC-rt-6 | runtime | an act longer than 1.5 h (a big closing review) | reaped, relaunched fresh; the unfinished agent restarts from zero and is reaped again | `rt [supervise]`, with the cap reset (P1) | reaps per item with the same partial returns | 1.5 h of tokens per lap | 4 |
| SC-rt-7 | runtime | a bound session legitimately waiting | stop-guard blocks 6 turns per session (`stop-guard.js:94`, `:128-131`); every relaunch is a new session with 6 more | `stop-guard.js` lifetime cap per session | `run-open` blocks per run summed over sessions | 6 model turns per relaunch | 3 |
| SC-rt-8 | runtime | the remote cannot be read | `stale-remote` holds and retries, parking at 24 h (`rt [decide]`) | `leases.expiry-hours` | the age of `stale-remote` | 24 h idle | 2 |
| SC-obs-1 | observability | a reading flaps around its pin (14 of 108 readings varied, `exp`) | ask, patch build, ask closed, breach again, new ask | `exp` `maintain.file` key (dedupes only while the ask is open) | ask (reading, offender) reopened after a close | a whole patch build per flap | 3 |
| SC-obs-2 | observability | main red | an event run per landed SHA, plus a `deploy.core` patch build per landing (`steps` `deploy.core`) | `plan.dedupe`, if it matches | runs or patch intakes per red SHA | event run plus placement per landing | 3 |
| SC-obs-3 | observability | a kept row whose window lapses | proposed again every 60 days per row (`exp [Loop Review]`) | by design | the same (kind, id) proposed after each keep | one owner item per row per window | 4 (cost low) |
| SC-obs-4 | observability | caps re-derived from p90 (`loop.propose`) under `budgets.pinned` refuse | the cap ratchets down, work orders are refused (SC-flow-3), and the next p90 is lower again | none | a cap value falling monotonically | blocked items | 1 |
| SC-obs-5 | observability | `maintain.fixes` regenerates a generated index on clean-base | each period conflicts with open builds' prepared merges, sending them back to resolution passes (`steps` `test.merge`) | `flow.route-backs` per build | conflicts on generated paths after each Maintain landing | resolution pass plus bar per build | 2 |
| SC-int-1 | integrations | promote refused, or verify answers a dead probe | owner item "retry again" or "verify again", picked by best effort each time (`exp [design-integrations]`) | none | the same (SHA, environment) retried more than N times | engine and verify calls | 2 |
| SC-int-2 | integrations | a pinned file differs | "no verdict stands"; only the owner's command re-pins, so every landing waits; under `dispatch-closure` the pin covers `gate-legs.json` (60 commits in 30 days) | `exp [design-integrations]` (owner item) | pin-mismatch age | wall time, all landings | 2 |
| SC-int-3 | integrations | an environment is broken under roll-forward | the ask key includes the SHA, so each landing files a new ask and rolls forward again | `exp` (dedupes per SHA only) | asks per environment across SHAs | ask plus release per landing | 2 |
| SC-int-4 | integrations | remote CI skipped or queued | dead probe, never green; `test.verdict` has no ceiling in its cell (A4) | `deploy.core` has the act ceiling, `test.verdict` none | verdict-wait age | Test blocked | 2 |
| SC-int-5 | integrations | the notification adapter is down | owner items go undelivered, which amplifies every owner wait | terminal fallback (`exp`) | no delivery record for an owner item | wall time | 2 |
| SC-dist-1 | distribution | `currency.on-behind: red` | the update build's own Test reds if the leg reads a stale committed currency record (`exp` currency leg; ambiguous) | none | currency red on the update build | deadlock until the probe runs | 1 |
| SC-dist-2 | distribution | an install step needs the target's code | it "always falls back to attended" (`v2 [policies]` `install.steps`), so an unattended update waits | none | update attended-pending | wall time plus a currency owner item | 3 |
| SC-dist-3 | distribution | weekly semantic row changes | an in-flight build re-pins at each step boundary; held patches, orders, and deviation orders repeat (`adopt [design]` 13, 15) | orders only | composition hash changes on every step of one build | re-composition plus orders | 2 |
| SC-dist-4 | distribution | `install.on-shim-call: refuse` under `verdict.blocks: every-red` | adopter scripts red, and the migration build cannot land | none | shim refusals plus a blocked landing | deadlock | 1 |
| SC-comp-1 | composition | a repository item's route leads back into itself, or a two-item route cycle | the needs graph is acyclic and routes are joined to the table, but route cycles are never checked (`adopt [design]` 11); counting depends on A1 | `steps [rules]` if any re-entry counts | an item re-entered more than N times | that item's act | 3 |
| SC-comp-2 | composition | a repository item in Build needs a Test item | needs are acyclic and resolve, but Build can never exit, so the build is `stuck` | `rt [decide]` `stuck` raises an owner item | `stuck` | build halted | 2 |
| SC-comp-3 | composition | scenario A names B as successor, and B names A | it re-composes at every step exit; a conflict under `refuse` waits for the owner each time (`np2 [p1-scenarios]` 7) | none on switches | scenario id alternating per step | re-composition plus an owner wait | 2 |
| SC-comp-4 | composition | additive `flow.adapt` | roles add items, stages and stricter values at every boundary with no cap (`np2 [p1-scenarios]` 4) | none | composition size and change count rising | grows without limit | 3 |
| SC-comp-5 | composition | a "stricter" `review.design.rounds: until-clean` or `review.follow-up: while-finding` applied unattended, or a scenario preset slot raising route-backs | a loop bound is widened (A3) | rounds still count against route-backs, unless that is raised too | a bound-key change without the owner's proof | as SC-flow-2 | 3 |
| SC-comp-6 | composition | a repository role's return names a kind or version nobody produces | 3 retries, then a park | `rl` RL-7 | a parked item | 3 acts, then a wait | 2 |
| SC-comp-7 | composition | an item witness needs an absent capability or a record nobody writes | never witnessed, the exit is unreachable, then SC-flow-3; the schema refuses only "no witness" (`adopt [scenarios]`) | none | instance dispatched more than N times with no witness | an act per beat | 3 |
| SC-comp-8 | composition | a repository lens that always finds something | it feeds SC-flow-2; a repository lens never owes a replay (`np2 [p1-scenarios]` 9) | `flow.route-backs` | that lens's finding yield never zero | as SC-flow-2 | 3 |
| SC-x-1 | between builds | a parent paused or looping | the dependent holds at `deploy.parents`; the parent's lease renews while paused (`steps [lifecycle]`) or looping (`rt [supervise]`), so it stays "reachable" (`fi`: "No timeout applies") | none | dependent awaiting while the parent's transitions are unchanged | dependent blocked | 3 |
| SC-x-2 | between builds | each build needs the other's confirmed interface | mutual wait; `depends-on` cycles are refused, except through a "pending" target (`mem [relations]`) | `mem [relations]` (partial) | two builds each awaiting the other | both blocked | 2 |
| SC-x-3 | between builds | a `question` the receiver cannot answer, or a stream of `changed` | "every transition… is refused while a message… is neither answered nor acknowledged" (`coord [design]` 6); each `changed` triggers a re-design | none | an unanswered message's age; the `changed` rate | transitions blocked; a re-design per message | 3 |
| SC-x-4 | between builds | concurrent builds on a hot file | prepared-merge conflict, resolution pass, another build lands, conflict again; then SC-flow-1 | `steps [rules]` per build | conflict paths repeating per build | resolution pass plus bar | 3 |
| SC-x-5 | between builds | `leases: refuse` (strict) | the second build waits on the first's release; a stuck holder keeps renewing | expiry only on death | lease-wait age | transitive block | 2 |
| SC-x-6 | between builds | a parent withdrawn | replan, the link moves to a replacement, the replacement is withdrawn, replan again | `flow.route-backs` | replans per build | planner plus architect | 1 |
| SC-x-7 | between builds | an inherited red on main | defaults land (`.githooks/gate-env.sh:103` `INHERITED_RED=land`), but every main push is forced to the full bar until a green descends (`.githooks/pre-push:1909-1971`); under `park` or `every-red`, two reds whose fixes block each other deadlock | gate-env policy | `refs/gov/bar-red` age | full bar per push; deadlock under `park` | 2 |
| SC-x-8 | between builds | under `build.unit-holders: any-session`, a session abandons a unit lease | the driver waits up to the 24 h expiry | `leases.expiry-hours` | unit lease beats stop while it stays held | 24 h | 2 |
| SC-own-1 | owner | ratifications and owner-only writes: `build.ratify`, the remote pin, `policy-file.guard`, `instructions.edit`; or `park-item` under `strict` | the wait has no ceiling and the lease keeps renewing | `blocked` raises once (`rt [decide]`) | owner-item age | wall time; dependents blocked | 3 |
| SC-own-2 | owner | release hold answered "keep waiting" | the ceiling restarts every 72 h (`rt [answers]` revision), indefinitely, and best effort can keep choosing to wait | `build.release-ceiling` | re-opens of the same (build, SHA) item | an owner item every 72 h | 2 |
| SC-own-3 | owner | an attend request (`confirm-steps`) and then the owner leaves | every step-exit gate waits; attendance never times out | none | gate age while attended | wall time | 3 |
| SC-own-4 | owner | `review.unclassed: owner-rules`, or a probe returns claimed or unrunnable | owner item, finding returned, re-disposed `none` or unrunnable again, owner item again | `flow.route-backs` | the same finding or probe returned to the owner more than once | owner turns | 2 |
| SC-own-5 | owner | default `notify.owner: turn-micro-formats`, `notify.channel: terminal` ("Nothing pushes a notification by default", `fr [forks]` settled) | a background supervisor's owner items are seen only when the owner next opens a session | none | owner-item age with no delivery | the wait's whole length | 4 |

## Top ten, ranked by likelihood times cost under the defaults

1. **SC-flow-3.** The design's own rules make an unwitnessed refused item permanently dispatchable: "`next` returns the frontier" plus "an unwitnessed one can always be dispatched again". No counter sits on re-dispatch of one instance.
2. **SC-flow-2.** A fresh review almost always finds something, and the closing review is owed by default with a follow-up after every HIGH. This build's own fold pairs confirmed 19 and 31 defects.
3. **SC-flow-1.** Under the default `best-effort-recorded`, the owner item that is supposed to end a loop is answered by the supervisor itself. Nothing says the count stops or resets.
4. **SC-rt-1.** I measured it: ten lifetime relaunches count as zero once the run has moved in the last five minutes. Any act that writes a transcript entry therefore escapes `RESUME_ATTEMPTS`.
5. **SC-rt-6.** gov's large closing reviews and bars routinely run toward the 1.5 h act ceiling, and a fresh relaunch restarts the unfinished agent from zero under a cap that P1 shows resets.
6. **SC-flow-4.** gov landed 353 first-parent commits in 30 days with no landing queue (`gap-flow-08`), and every landing stales every other build's verdict.
7. **SC-x-4.** `tools/gate-legs.json` alone took 60 commits in 30 days, so concurrent builds keep re-conflicting at the prepared merge.
8. **SC-rt-3.** Session limits already killed four Tier-2 reviews (`stall-recorder.js:12-13`), and the designed hold keeps renewing the lease, so no other node can take the build over.
9. **SC-rt-4.** Whether SubagentStop fires for killed or stalled agents is explicitly unmeasured (`np2 [p7-agent-cap]`). One leaked reservation leaves a live session's admission queue waiting forever.
10. **SC-own-5.** Nothing pushes an owner item by default. Every wait on the owner in the table lasts until the owner happens to open a session.

Next by score: SC-mem-1, SC-instr-1, SC-roles-1, SC-x-1, SC-own-1.

**Findings that belong to other researchers, one line each.**
- To the census: the 17 loop or wait routes with no bound in their own cell (P2).
- To history: the run that ran away under the consecutive cap, `resume-tick.sh:70-74`.
- To prior art: per-instance retry counters with dead-letter queues, as in Temporal and SQS.
