**Serves:** spec-audit PLAY-dClosedLoop-1

# Tier-2 review, run A: the runtime layer's design record for dClosedLoop

Provenance: a Tier-2 spec audit with five lenses (finders gov-spec-reviewer), five skeptic batches (gov-skeptic) and synthesis (gov-synthesizer). It was run on 2026-10-15 as run A of the two independent rounds the owner asked for. ROUND 1.

Reviewed: memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md@767187aa4073f6e64cb2b2ef6b798f0a538347fd

## Verdict: CLEAN WITH FIXES

No finding is a blocker. Six confirmed findings are high, in five items. The highs cover four problems: recovery after a relaunch, how unit worktrees are merged back, double ownership of units across the build chain, and a fixture that cannot fail. A fifth high is take-over without fencing. Fix all of them before the record is settled.

Review shape: intensity full, raw 60, confirmed 56, refuted 4, unverified 0 (0 uncertain), precision 0.93.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 14 | 13 | 1 | 0 | 0 | 0.93 |
| grounding | yes | 10 | 10 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 13 | 13 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 10 | 8 | 2 | 0 | 0 | 0.80 |
| failure-envelope | yes | 13 | 12 | 1 | 0 | 0 | 0.92 |

Adjudicated tally by item: 43 items, of which 0 are blockers, 5 high, 33 medium and 5 low.

Adjudicated tally by raw confirmed finding: 56 findings, of which 0 are blockers, 6 high, 45 medium and 5 low.

Every confirmed finding keeps its binding grade. Items merge only findings that share a grade. Where one defect was confirmed at two grades, it appears as two items that point at each other: ids 1 and 15, ids 17/52 and 7, and ids 4 and 32/44.

Run integrity:

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Verdict hygiene: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 55 judged sound, 1 judged UNSOUND (id 20, whose corrected fix is the one written below), 0 none proposed, 0 not judged.
- Severity: 0 confirmed findings were left ungraded by the skeptic, and 15 were re-graded.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: 7 spec documents were supplied as `specs`, as sibling context.
- Checklist: 11 items, each assigned to exactly one lens (coherence 3, grounding 2, reuse 2, blast-radius 2, failure-envelope 2).
- By design: the caller's byDesign.
- Move check: no checked subject moved.

The run is complete on these counts.

## High

### H1. A fresh relaunch cannot replay the dead driver's Workflow run (id 1)

- **Where:** [supervise] Relaunch, [spawn] first bullet, [tests] fixture 3.
- **What is wrong:** [supervise] relaunches a driver "fresh, never resumed". [spawn] relies on Workflow journal replay (`resumeFromRunId`) so that no completed agent is paid for twice, and names "the run journal" as the fallback if SubagentStop does not fire. The spawn research return says replay works only in the same session or after `claude --resume`, and that a fresh session has nothing to resume.
- **Consequence:** A relaunched driver re-spawns, and pays again for, every agent the dead run had completed. Fixture 3 cannot pass on a correct build. Recovery rests on SubagentStop persistence, which fixture 6 has not verified.
- **Fix (skeptic judged SOUND):** Pick one recovery path and state it in [supervise] and [spawn]. Either relaunch with `--resume <session-id>` while a Workflow run is in flight and keep `fresh` for between items only, or make per-agent persisted returns the only replay source and drop `resumeFromRunId` from [spawn]. Restate fixture 3 against the chosen path, for example by comparing the journal's totalTokens before and after the kill.
- **Gate:** a design-lint check that every recovery mechanism the record cites names its precondition from the research return. Fixture 3 run against a fresh relaunch specifically.
- **See also:** M1 (id 15) is the same defect confirmed at medium by the grounding lens.

### H2. No step carries a unit worktree's commits back onto the build branch (id 3)

- **Where:** [isolate].
- **What is wrong:** Each unit gets its own worktree, branched from the build branch tip, and release "reclaims all of it". Nothing merges a unit branch back, and nothing orders integration between parallel units. Two sibling records say the opposite: flow-steps `build.unit-pass` ("commits queued by the executor") and v2's dScopedBuild row (one shared worktree).
- **Consequence:** Releasing a unit can discard committed work that never reached the build branch. Two records answer one question.
- **Fix (skeptic judged SOUND):**
  - Add to [isolate] an integration step owned by the supervisor. It fast-forwards or merges each unit branch into the build branch in declared order, before release.
  - Refuse release while the unit branch has commits the build branch lacks, and name the witness for that.
  - Reconcile the step with flow-steps `build.unit-pass` and v2's dScopedBuild row.
  - Extend fixture 8 so that after release the build branch contains every unit's commits.
- **Gate:** a release precondition (`git merge-base --is-ancestor unit build`) that refuses, seen red on a unit holding an unmerged commit.

### H3. dWellOiledMachine takes deliverables v2 still assigns to other chain builds (id 4)

- **Where:** [build] units and gap tables, [gaps-proposed] "Already registered ... Their owners stand".
- **What is wrong:** v2's dDeclaredLoop row already owns:
  - the `next` verb;
  - the owner's pause, resume, withdraw and supersede;
  - the executor launched where `run.host` says;
  - gap-flow-10.

  dBoundRoles owns schema-forced returns (gap-roles-04), and dShippedRelease owns lander hardening (gap-deploy-07). [build] lists the `next` CLI, the client verbs, durable returns and signal traps as its own units, while saying those gap owners "stand". RT-3 moves only four gaps.
- **Further mismatches:** [decide]'s client verbs drop `supersede`. dWellOiledMachine is a child of dDeclaredLoop, yet the parent's row already includes the executor launch the child would supply.
- **Consequence:** Two builds each build one deliverable, and the build order between parent and child breaks.
- **Fix (skeptic judged SOUND):**
  - In [build], list each v2 deliverable that moves to dWellOiledMachine and each that stays, quoting the v2 row text it removes.
  - Move gap-flow-10, gap-roles-04 and gap-deploy-07 (or the parts that move) with their units, or drop those units.
  - Add `supersede` to the client verbs, or record why it is gone.
  - Put the moves to the owner as part of RT-3.
- **Gate:** a chain-roster check that every deliverable phrase and gap id is owned by exactly one chain build across v2 and the layer records.
- **See also:** M18 (ids 32 and 44) is the same overlap confirmed at medium.

### H4. Fixture 2 replays `driver.log`, which cannot contain the acts it is meant to catch (ids 17, 52)

- **Where:** [tests] fixture 2, [act] act-binding rule.
- **What is wrong:** `driver.log` records only unattended.sh verb calls. On a re-probe, `grep -ci workflow` over its 1,964 lines printed 0. The 17 inline Workflow calls and 25+ ad-hoc scripts that the research names as the likely failures live in session transcripts, not in that log. The log is also untracked and per-node, so on another node the population is empty.
- **Consequence:** The fixture is green before act binding exists and cannot fail on the class it exists to catch. It certifies what it does not check. It still catches out-of-order verb transitions, which is why it is graded high rather than blocker.
- **Fix (skeptic judged SOUND):**
  - Draw the replay population from the session transcripts: every main-thread Workflow, Agent and Bash act, plus Bash invocations of scripts outside the declared commands. State that population in the fixture.
  - Require the population to be non-empty.
  - Before trusting the fixture, see it red: count the inline `Workflow{script}` calls in session b710e9c3 and confirm the fixture reports them as outside a declared item.
- **Gate:** a population-non-empty assertion plus a seen-red run on a known-bad transcript.
- **See also:** M5 (id 7) is the same defect confirmed at medium.

### H5. Take-over does not fence the old node's driver (id 50)

- **Where:** [supervise] take-over, [act] act-binding rule.
- **What is wrong:** When a supervisor dies and another node takes the run lease, the old node's detached driver and its Workflow agents keep running. The new supervisor launches a second driver for the same act. Act binding checks only that `next` named the act, not which lease epoch the driver serves. The record has no epoch, token or fencing anywhere.
- **Consequence:** Two drivers can perform the same act. That means duplicate spawns, concurrent commits on one worktree (the E4 index-lock failure) and agents paid for twice, on the take-over path.
- **Fix (skeptic judged SOUND):**
  - Bind each driver to a lease epoch or token issued by the supervisor.
  - Have act binding refuse an act from a driver whose epoch is no longer current.
  - State that an old driver that sees a lost lease stops at its next tool call.
  - Add a fixture: take over the lease while a driver is mid-act, and the old driver's next spawn is refused.
- **Gate:** that fixture, seen red before fencing exists.

## Medium

### M1. Fresh relaunch versus journal replay, on the fallback path (id 15)

- **Where:** [supervise] Relaunch, [spawn] replay, [policies] runtime.relaunch, [tests] 3.
- **What is wrong:** This is the defect in H1, confirmed at medium by the grounding lens. On the main path, returns persisted by SubagentStop witness completed items. On the fallback path, a fresh session cannot replay the journal, so returns are lost (breaking invariant 4) and fixture 3 fails.
- **Fix (skeptic judged SOUND):**
  - Either default `runtime.relaunch` to `resume` for a driver that died with a Workflow run in flight, keeping `fresh` for clean act boundaries.
  - Or make item completion depend only on the SubagentStop-persisted return, and make fixture 6 a precondition of the whole design.
  - Restate the [spawn] fallback so it claims no cross-session durability. Run fixture 3 against a fresh relaunch.
- **Gate:** as H1.

### M2. The default `build` driver lifetime conflicts with per-item schemas and per-unit worktrees (ids 2, 20)

- **Where:** [supervise] launch flags, [act] Lifetime, [isolate], [policies] runtime.driver-lifetime.
- **What is wrong:** Drivers are launched as `claude -p --json-schema <item schema>`. A `-p` run returns one `structured_output` against one schema, and its working directory is fixed at launch. The default lifetime `build` has one driver serve many items and many unit worktrees.
- **Consequence:** A build-lifetime driver either loses the per-item schema fallback or is relaunched per item, which makes the default `item` in practice. Its role agents for later units run outside their own worktree. That brings back the shared-index hazard and defeats fixture 8.
- **Fix:**
  - For id 2 (skeptic judged SOUND): either make `item` the default and say that `--json-schema` binds a single item, or keep `build` and state how per-item returns are schema-forced inside one session, dropping the session-level fallback for that lifetime. Add a fixture that runs two items through one driver and checks each return against its own schema.
  - For id 20 the finder's fix was judged UNSOUND. The skeptic's corrected fix: default `runtime.driver-lifetime` to `item` (per unit lease), as the sessions research picked (S2), so each driver is launched with its cwd set to that unit's worktree. Keep `build` as an opt-in value valid only with `runtime.isolation=shared`. State that a role agent inherits its driver's worktree.
- **Gate:** a policy-validation rule that refuses `driver-lifetime=build` unless `isolation=shared`.

### M3. The actor kinds omit "the executor", and hook items have no route (id 5)

- **Where:** [extend] actor kinds, [supervise] Each tick, [act].
- **What is wrong:** Runtime's actor kinds are command, role, hook and owner. The roles layer's are role, command, hook, executor and owner. The tick routes only command items and role or owner items. The executor's duties have no component: resolve inputs, key and class facts, recompute them at the spawn, and wrap the work order.
- **Consequence:**
  - `build.acceptance`, `build.unit-pass` and hook items have no handler.
  - A Workflow harness has no filesystem access, so it cannot do the executor's duties.
  - A model driver doing them would break P29.
  - A new actor kind would need dispatch code.
- **Fix (skeptic judged SOUND):**
  - State that "the executor" is the supervisor, or rename it in one place.
  - Add `executor` (or its mapping) to the actor kinds, and say how hook items are dispatched or witnessed.
  - Assign work-order assembly and fact keying to the supervisor before the driver's act, passed as Workflow args.
  - Make dispatch by actor kind a registered adapter.
- **Gate:** a cross-layer check that every actor named in the roles matrix maps to a Runtime dispatch route.

### M4. Two keys govern driver renewal, and the prose contradicts one of them (ids 6, 37)

- **Where:** [policies] runtime.relaunch and runtime.driver-refresh, [supervise] Relaunch, [sessions].
- **What is wrong:** `runtime.relaunch` (fresh, resume) and `runtime.driver-refresh` (fresh, compact-with-card) both set how a driver at `context.threshold` is renewed. [supervise] says "never resumed", although `resume` is an allowed value. Nothing in the record reads `runtime.relaunch`.
- **Consequence:** With non-default values the record gives two verdicts, and the builder has to guess which key wins.
- **Fix (skeptic judged SOUND):**
  - Either merge them into one key, for example `runtime.driver-renewal` with values fresh, resume and compact-with-card.
  - Or split them by trigger: death or a limit goes to `runtime.relaunch`, the threshold goes to `runtime.driver-refresh`. Name the split in both [supervise] and [policies].
  - Reword "never resumed" as "resumed only under runtime.relaunch=resume".
- **Gate:** a policy-catalogue check that each key has at least one reader in the record and that no two keys name the same trigger.

### M5. Fixture 2 passes by finding nothing (id 7)

- **Where:** [tests] fixture 2.
- **What is wrong:** This is the defect in H4, confirmed at medium by the coherence lens. Every logged act is a driver verb that maps to a transition, so the out-of-declaration rate is about 0% whatever the design.
- **Fix (skeptic judged SOUND):** Replay the main-session transcripts (Workflow and Bash tool calls), not `driver.log`. As a seen-red check, first run the fixture on a session known to contain the improvised workflows.
- **Gate:** as H4.

### M6. Invariant 2 claims refusal of spawns that hooks cannot see (ids 8, 16)

- **Where:** [invariants] 2, [act] act-binding rule, [supervise] agents in flight, [tests] 5.
- **What is wrong:** Workflow `agent()` calls and nested `workflow()` calls are not tool calls, so no hook sees them (agent-cap.js:18-27). Invariant 2 still says a spawn that `next` did not name is refused, and the in-flight count runs "across every Workflow call". Fixture 5 assumes a queue, but a PreToolUse hook can only refuse. No fixture asserts that an unnamed spawn is refused.
- **Consequence:** Inside an admitted script, extra agents and nested workflows run unrefused and uncounted. The invariant certifies more than the hook surface can check.
- **Fix (skeptic judged SOUND):**
  - Restate invariant 2 and `runtime.fanout` at the Workflow-call granularity: the call, its declared script by sha, and a static bound on the script's `agent()` sites (as agent-cap rules 1-3 do today).
  - Name what stays unchecked: the runtime `agent()` count and nested `workflow()`.
  - Change fixture 5 to assert a refusal plus a supervisor-side queue.
  - Add fixtures for an unnamed spawn or Workflow call being refused, and for an admitted script calling `agent()` once more than declared.
- **Gate:** those fixtures.

### M7. Fixtures 6 and 12 cannot fail (id 9)

- **Where:** [tests] fixtures 6 and 12.
- **What is wrong:** Fixture 6 ("SubagentStop fires ... If not, the stated fallback") passes on either branch. Fixture 12 ("the cost ... measured") has no bound.
- **Consequence:** Return durability and per-start cost go ungated.
- **Fix (skeptic judged SOUND):**
  - Split fixture 6 into two. First, SubagentStop fires for a role-typed sidechain and its return file exists, keyed by agent_id. Second, with the hook removed, the journal plus `--json-schema` still yields a persisted, schema-valid return, and a staged invalid return is held.
  - Give fixture 12 a bound derived from [current], for example a headless start under N seconds or under 84k tokens.
- **Gate:** a [tests] lint that every fixture states a failing condition.

### M8. Invariant 7 is false under allowed policy values and for the binding events (ids 10, 23)

- **Where:** [invariants] 7, [enforce] Failing closed, [policies] runtime.hook-failure and runtime.below-floor, [sessions] binding.
- **What is wrong:** Invariant 7 is unconditional, yet `runtime.hook-failure=open` and `runtime.below-floor=degrade` are allowed values. SessionStart, which binds a session to its build and delivers the card, cannot block. SubagentStart cannot block either. Neither is in the witness list, which names only Stop, SubagentStop and git hooks.
- **Consequence:** A crashed SessionStart dispatcher leaves a session unbound, with nothing recorded. Resume already misses the card 7 of 14 times. Whether act binding then refuses everything or nothing is unstated, so binding may fail open.
- **Fix (skeptic judged SOUND):**
  - Qualify invariant 7 with "under `runtime.hook-failure=closed` on a node at or above `runtime.cli-floor`".
  - Add SessionStart and SubagentStart to the witness-backed events. The hook writes a binding record, and the PreToolUse act-binding rule requires it, so a missing binding refuses the first tool call.
  - Add a fixture with a crashed SessionStart dispatcher, and add that case to fixture 9.
- **Gate:** that fixture.
- **See also:** the hook-failure half of id 60 (M13) is answered by this fix.

### M9. Extension points are selected by closed enums (id 11)

- **Where:** [extend], [policies] runtime.harnesses, runtime.scheduler, runtime.journal.
- **What is wrong:** [extend] says a new harness, scheduler backend or journal sink is "a filled contract. Runtime gains no code". The keys that select them are closed enums of today's adapters. `runtime.scheduler` is single-valued, while [schedule] runs a node task, CI and a routine at once.
- **Consequence:** A newly registered adapter cannot be selected without changing the key schema.
- **Fix (skeptic judged SOUND):** Make these keys take lists of registered adapter names, validated against the registry. For example: `runtime.harnesses = [claude-code, codex]`, `runtime.scheduler = {cadence item -> backend}`, `runtime.journal = [runlog, observability]`.
- **Gate:** a schema check that every extension-point key validates against its registry, not a literal enum.

### M10. The CLI floor does not say which binary it checks, and it re-opens a rejected decision (ids 18, 29)

- **Where:** [enforce] CLI floor, [harness] node registry, [supervise] headless launch, [policies] runtime.cli-floor.
- **What is wrong:** This node runs the desktop session at 2.1.295 and the PATH `claude` at 2.1.292. The supervisor would launch the PATH binary for every headless driver. The record never says which binary is checked or launched. It also authors a version floor, which TOOL-aMendedFleet-61's review rejected in favour of the session's own version (read_cli_version, the `cli-version` fact). unattended.sh:8790-8795 explains why `claude --version` is the wrong source.
- **Consequence:** The floor grades the wrong binary. Every headless driver on this node runs below the floor and may fail open.
- **Fix (skeptic judged SOUND):**
  - Read the running session's own version through read_cli_version and the `cli-version` fact, never PATH.
  - Have the supervisor resolve and pin the absolute `claude` it launches, and check that binary against `runtime.cli-floor` before any launch.
  - Record both versions per node.
  - Cite TOOL-aMendedFleet-61 and state why a fail-closed feature floor differs from the launch-version pin it rejected.
- **Gate:** a fixture with a stub PATH `claude` below the floor, where the launch is refused.

### M11. Nothing hosts the supervisor, and resume-tick already is one (ids 19, 27)

- **Where:** [supervise] Where it runs, [schedule] node-task backend, [build] "the supervisor" unit, [invariants] 5.
- **What is wrong:** The supervisor is a per-node process with no model. Nothing launches it, keeps it alive or restarts it after a reboot. The desktop scheduled task named as a carrier wakes a model session, which only an agent can register. resume-tick.sh is already that process: OS-scheduled every 10 minutes as gov-resume-tick, it treats `--liveness` as its only stale verdict, kills stale trees and launches detached `claude -p`. The record cites it only for the permissions flag.
- **Consequence:**
  - After a reboot no tick runs, or the supervisor ends up hosted in a model session, which breaks invariant 5.
  - A second out-of-session actor with its own "stalls" predicate competes with `--liveness`.
- **Fix (skeptic judged SOUND):**
  - State that the supervisor is resume-tick.sh grown. It keeps `--liveness` as the only stale or terminal verdict, `--beat`, the attempt cap and run_detached, and replaces only the `--resume --dangerously-skip-permissions` launch.
  - Make the node-task backend the existing gov-resume-tick registration (README lines 202-218), extended to wake cadence items. That gives an OS-level carrier with a restart policy and a liveness beat under the run lease.
  - Say that a desktop-app task, if kept, wakes a model session and is therefore an act, not the supervisor.
- **Gate:** a single-stale-predicate check (one definition of stale across unattended and supervisor), plus a reboot fixture.

### M12. Codex's hook events do not "match one for one" (id 22)

- **Where:** [harness] One guard core, [policies] runtime.harnesses.
- **What is wrong:** The research lists only PreToolUse, SubagentStart, SubagentStop, PreCompact and SessionEnd for Codex, and Codex has no Workflow tool (unverified). The dispatcher needs SessionStart, PostToolUse, Stop and PostCompact. Codex's own docs call its hooks "not a complete enforcement boundary".
- **Consequence:** Under `claude-code-and-codex`, a Codex driver gets no binding, card or Stop witness, and no role harness. Invariant 7 does not hold there.
- **Fix (skeptic judged SOUND):** Replace the claim with the measured event map, list the missing events and the missing Workflow capability, and state the degraded guarantees. Alternatively, restrict Codex to role-agent or instructions-plus-guards use until a spawn backend is declared.
- **Gate:** a per-harness capability table checked against the dispatcher's required events.

### M13. `runtime.fanout` duplicates agent-cap's bound with an unbounded range (ids 25, 40, 60)

- **Where:** [policies] runtime.fanout, runtime.hook-failure, [supervise] agents in flight, [invariants] 7.
- **What is wrong:** `runtime.fanout` ("an agent count", default 5, no range) is a second carrier beside agent-cap's MAX_VERIFIERS and EFFECTIVE_CAP, `.agent-cap.conf` FANOUT_CAP (which can only lower the cap), the FANOUT_CAP placeholder in four workflow templates, and the agent-cap-restatement leg. It also changes the semantics: agent-cap counts a per-prompt total, "never the concurrency bound". TOOL-aRepatriatedFork-7 decided the cap is never raisable, and TOOL-aUnmannedHelm-1 measured that a hook counter is racy. A value of 0 deadlocks, and values above the platform's 16 or 20 cannot be enforced. `runtime.hook-failure=open` falsifies invariant 7 (see M8).
- **Consequence:** Two enforcers answer one question with different semantics. A value above 5 does nothing or revives the override that was removed on purpose.
- **Fix (skeptic judged SOUND):**
  - Name one carrier. Either `runtime.fanout` replaces `.agent-cap.conf` and is read by agent-cap.js through the policy mirror, or it is an alias of FANOUT_CAP limited to 1..5 that can only lower the cap.
  - Have the in-flight count read min(FANOUT_CAP, 5), and do not make the supervisor's counter a per-hook read.
  - Validate the range at intake, 1 to min(16, 20).
  - Either drop `open` from runtime.hook-failure or qualify invariant 7 with it, and have the class check report the policy value.
  - List the consumers to change: agent-cap.js, the FANOUT_CAP templates, check-agent-cap-restatement.sh and its leg, and the agent-cap self-test leg.
  - Cite TOOL-aRepatriatedFork-7 and TOOL-aUnmannedHelm-1.
  - Add a fixture: with `runtime.fanout=3`, both the hook and the supervisor refuse the 4th agent.
- **Gate:** that fixture, plus the existing restatement leg extended to `runtime.fanout`.

### M14. `runtime.reap` re-declares PROCMON_REAP_MODE with a mismatched value set (id 26)

- **Where:** [policies] runtime.reap, [supervise] "reaps orphans and stalls", [gaps-proposed] 7.
- **What is wrong:** `runtime.reap` has the values orphans, orphans-and-idle and report. PROCMON_REAP_MODE has report, reap-orphans and reap-all, and reap.py refuses anything outside that set. The record never names `reap.py --sweep` as the reaper.
- **Consequence:** A second reap policy, and possibly a second reaper, that bypasses process-monitor's safety fences (TOOL-aReapedSpinner-8..10).
- **Fix (skeptic judged SOUND):** Have the supervisor run `reap.py --sweep` under PROCMON_REAP_MODE. Retire `runtime.reap`, or make it name that closed set exactly. Reword gap 7 to: the existing sweep is never scheduled.
- **Gate:** the policy-catalogue check from M4 extended to flag keys that shadow an existing kit config key.

### M15. Per-worktree `core.hooksPath` reverses a decided position, and its readers are unnamed (ids 28, 42)

- **Where:** [enforce] "core.hooksPath becomes per-worktree", [isolate] "the worktree's own hooks path".
- **What is wrong:**
  - WIRE-INTO-PROJECT.md:855-858 and check-wiring.sh:615-630 (TOOL-aWeldedTribunal-7) chose an out-of-tree path so a branch cannot make the guard inert. Running each worktree's own hooks lets a unit branch weaken its own gate.
  - The change also touches readers the record does not name:
    - check-wiring Check H (:740-773) sets the path only when it is unset, and reports "ok" on today's absolute value.
    - run-gates KF3 (:4928-4931) blanks an absolute hooksPath.
    - govkit/matrix.py:143 sets the path.
    - The check-wiring self-test leg depends on all of this.
- **Consequence:** A guard bypass on a narrow path. The fix never reaches existing clones, and fixture 8 passes only on fresh worktrees.
- **Fix (skeptic judged SOUND):**
  - Cite the decided position.
  - Either keep one trusted out-of-tree copy per worktree, written by the supervisor from the build branch tip at allocation, or require the hook to refuse a `.githooks` that differs from the trusted copy.
  - Name the mechanism (a relative `.githooks`, or `config.worktree` with extensions.worktreeConfig).
  - List the consumers above. Make Check H refuse an absolute value, reusing its arm.
  - Extend fixture 8 two ways: an edited `.githooks` in a worktree must not run, and an existing clone with an absolute hooksPath must report UNWIRED.
- **Gate:** that fixture.

### M16. The permission allowlist ignores the owner ruling on auto mode (id 30)

- **Where:** [supervise] driver launch "an explicit permission allowlist", [invariants] 8.
- **What is wrong:** DECISIONS TOOL-aMendedFleet-116 (owner, 2026-10-07) moves unattended runs to `--permission-mode auto` once node CLIs reach 2.1.281, and TOOL-aMendedFleet-117 is the open build. The record neither cites nor reconciles either.
- **Consequence:** Two permission models get built for the same launches.
- **Fix (skeptic judged SOUND):** Cite both. Either adopt auto mode with the allowlist as its floor, or raise the conflict as an RT question to the owner. Do not settle it by default.
- **Gate:** a design-record check that cites open DECISIONS asks touching the same surface.

### M17. Parallel units are treated as unproven, and the condition that cleared them is dropped (id 31)

- **Where:** [current] "No parallel units", [isolate], [tests] 8.
- **What is wrong:** The record repeats "parallelism route: none" (TOOL-cBriefedPilot-21). That was superseded by TOOL-aHoistedPass-10 after TOOL-dUnstalledConvoy-7 cleared R2 with R5. The clearance depends on E3 condition 2 (passes stay off shared mutable records), which [isolate] omits. Fixture 8 re-tests only the index lock, which is already known, and skips E4 conditions 5-7 (merging without markers or loss).
- **Consequence:** Merge conflicts or lost writes on RUN.md, the decision log, backlog shards and generated indexes.
- **Fix (skeptic judged SOUND):** Cite TOOL-dUnstalledConvoy-7 and TOOL-aHoistedPass-10. Add to [isolate] that the supervisor alone writes shared records and merges unit branches through the row-keyed merge driver. Restate fixture 8 as E4 conditions 5-7 over a run that touches shared records.
- **Gate:** that fixture, plus a stale-carrier check (TOOL-aHoistedPass-32 class) over design records.

### M18. `next`, the client verbs, signal traps and isolation are planned twice across the chain (ids 32, 44)

- **Where:** [build] units and "Gaps that stay where they are", [decide] client verbs, [gaps-proposed] "Already registered".
- **What is wrong:** This is the overlap in H3, at medium. v2:704 (dDeclaredLoop) still holds the `next` verb, the position engine, the owner's verbs, the executor launch, the resume-card fix, the compact hook and gap-flow-10. v2:711 (dScopedBuild) still plans parallel commits in a shared worktree, which [isolate] abolishes. Line :263 claims to settle where `next` lives but marks nothing in v2 for amendment. The client verbs are not mapped onto unattended's --hold, --park, --abort and --resume. The v2 chain header "thirteen builds" goes stale.
- **Fix (skeptic judged SOUND):**
  - Add a "[chain] edits" or "units it takes from dDeclaredLoop" list to [build], quoting each v2:704 and v2:711 phrase that moves, and mark v2's rows for amendment.
  - Move gap-deploy-07 and gap-flow-10 to dWellOiledMachine, or drop the signal traps and the owner verbs from its units.
  - Map each client verb onto the unattended verb it extends (pause to --hold, withdraw to --abort, resume to --resume, ask/answer to --park/--propose), or say which are new.
  - Note that the chain grows from thirteen to fourteen builds.
- **Gate:** as H3.

### M19. Subagent-stop return validation and act binding each have two owners (id 33)

- **Where:** [build] "the role harness's durable returns", [enforce] roles pack "act binding", [settled] row 3.
- **What is wrong:** [settled] gives "return validation at subagent stop" to dBoundRoles, and v2 gives it gap-roles-04. [build] lists the same hook as a dWellOiledMachine unit. Act binding sits in the roles pack but is built as a Runtime unit.
- **Consequence:** Two SubagentStop rules that disagree, or each build assuming the other built it.
- **Fix (skeptic judged SOUND):** Choose one owner for each. Either Runtime only wires dBoundRoles' check into the dispatcher, or move the item out of the [settled] row and mark v2's dBoundRoles units for amendment.
- **Gate:** as H3.

### M20. The core sweep rebuilds branch-reconcile, which the core may not depend on (id 34)

- **Where:** [isolate] "a sweep reaps orphans: today, 8 merged worktrees", [contract] engine kits.
- **What is wrong:** branch_reconcile.py already classifies worktrees as MERGED, EQUIVALENT or SUPERSEDED and removes them under `--write` with a recovery manifest (TOOL-dSweptBranches-1..4). [contract] keeps branch-reconcile an expansion, and "the core never depends on an expansion".
- **Consequence:** A second classifier and remover, and two removers that disagree.
- **Fix (skeptic judged SOUND):** Either promote branch-reconcile's verdicts and removal into the core engine kit, or limit the core sweep to workspaces the supervisor leased and leave merged-branch housekeeping to branch-reconcile. State the choice in [isolate] and [contract].
- **Gate:** a core-versus-expansion dependency check over the contract's engine kits.

### M21. The journal and run record are claimed without runlog, and new producers need code (id 35)

- **Where:** [contract] record kinds and engine kits, [extend] journal sinks, [policies] runtime.journal.
- **What is wrong:** runlog already owns the journal grammar, the journals and the committed run record (record.py). PRODUCER_FILES is closed to driver, gates and pushes. runlog.py:499 takes `--producer` choices from it, and selftest.py:1009 pins it.
- **Consequence:** Possibly a second journal format. The claim "Runtime gains no code" fails at the first new producer.
- **Fix (skeptic judged SOUND):** Name runlog as the engine kit for the journal and the run record, and make `runtime.journal`'s summary record.py's committed record. List adding the supervisor and dispatcher producers as a runlog unit in [build], or make the producer set declarable.
- **Gate:** a selftest that every journal producer the record names exists in PRODUCER_FILES.

### M22. The dispatcher and hook packs ignore the fragments and settings-merge (ids 36, 41)

- **Where:** [enforce] "Rules come in packs", "One dispatcher entry per event", onFailure, [extend] hook packs, [build] the one enforcement surface.
- **What is wrong:**
  - The pack declaration is designed from scratch, beside 12 tracked `*.fragment.json` files and their readers: settings-merge.py, check-wiring.sh, check-hook-destinations.sh and govkit.
  - settings-merge writes entries as `{type, command}` only, and its `--check` compares only the command.
- **Consequence:**
  - A second registration format.
  - Wiring legs that go red or grade fragments the dispatcher no longer reads.
  - Adopters stay fail-open while `--check` reports them wired.
- **Fix (skeptic judged SOUND):**
  - Define a pack as the fragment schema extended with owner, decision class, failure mode, latency budget and policy key.
  - Have settings-merge.py render one dispatcher entry per event, write `onFailure`, and compare it in `--check`.
  - List as files touched by the enforcement-surface unit:
    - every fragment, including the kickoff's orientation-card and orientation-replay;
    - settings-merge.py;
    - each adopt-*.sh;
    - check-hook-destinations.sh and its leg;
    - check-wiring.sh and govkit;
    - the kit version markers.
- **Gate:** probe with the new settings-merge on a scratch settings.json, delete `onFailure`, and `--check` must exit non-zero.

### M23. The resume-tick retirement has no owning unit (id 38)

- **Where:** [supervise] "No session the runtime launches skips permissions", [build] units, [invariants] 8.
- **What is wrong:** The flag at resume-tick.sh:385 is "retired", but no [build] unit retires or rewrites resume-tick. The record names none of its consumers:
  - resume-tick.test.sh:368, whose AC1 asserts the flag;
  - check-unattended.sh:5770, which scans resume-tick.sh;
  - the unattended SKILL's CronCreate keepalive (.claude/skills/unattended/SKILL.md:16, rendered from tools/unattended/SKILL.template.md).
- **Consequence:** An unchanged resumer still launches `--dangerously-skip-permissions`, which breaks invariant 8, or the test goes red with no owner.
- **Fix (skeptic judged SOUND):** Add a [build] unit that retires resume-tick or rewrites it onto the fresh relaunch, naming these consumers. Add a fixture that greps every launch site under tools/ for the flag and returns zero hits.
- **Gate:** that grep fixture.
- **See also:** L2 (id 13).

### M24. `next` replaces --plan and --status without naming their readers (id 39)

- **Where:** [decide] "It replaces today's three derivations".
- **What is wrong:** Three kinds of reader depend on the old verbs:
  - runlog's model.py:120-140 classifies `--status` as heartbeat, read-only and tree-blind;
  - stop-guard.js:167 sends sessions to `--plan`;
  - unattended-build.js calls `--plan` 20 times.

  gen_build_index.py also reads these verbs.
- **Consequence:** runlog misreads liveness on supervised runs, and stop-guard points to a retired derivation.
- **Fix (skeptic judged SOUND):** List these readers for re-pointing in the same unit: model.py and its fixtures, stop-guard.js, unattended-build.js and its template, and gen_build_index.py. State whether `--plan` and `--status` stay as aliases. Add a fixture in which runlog reads a heartbeat from a journal holding only `next` calls.
- **Gate:** that fixture.

### M25. The new `runtime.*` keys duplicate v2 keys and have no preset values (id 43)

- **Where:** [policies] runtime.isolation, runtime.scheduler, runtime.hook-failure, runtime.below-floor.
- **What is wrong:**
  - `runtime.isolation` (default worktree-per-unit) duplicates `build.worktree` (default shared). The defaults are opposite.
  - `runtime.scheduler` overlaps `maintain.host` and `run.host`, which use a different vocabulary.
  - `runtime.hook-failure` sits beside `hooks.bypass`.
  - No `runtime.*` key has preset values, and `runtime.below-floor` has no default.
- **Consequence:** Two keys answer one behaviour, and the record fails v2's completeness rule for presets.
- **Fix (skeptic judged SOUND):**
  - For each pair, retire or fold one key and say which: reconcile the isolation default, and give the scheduler keys one value vocabulary.
  - State how `hooks.bypass` relates to fail-closed.
  - Give every `runtime.*` key a value in each of the four presets, and give `runtime.below-floor` a provisional default until RT-2 is answered.
- **Gate:** v2's preset-completeness check, run over the layer records now.

### M26. Driver relaunch has no attempt cap, backoff or terminal outcome (id 48)

- **Where:** [supervise] Relaunch, [policies].
- **What is wrong:** A dying driver is relaunched without bound. This drops today's RESUME_ATTEMPTS (default 6, "ATTEMPTS EXHAUSTED").
- **Consequence:** An unbounded token sink at 84k tokens per start when an item never completes or the node is exhausted.
- **Fix (skeptic judged SOUND):** Add `runtime.relaunch-attempts` and a backoff. Once attempts are exhausted, park the run and raise an owner item. Add a fixture: a stub CLI that always exits at `--max-turns` ends parked after N attempts.
- **Gate:** that fixture.

### M27. A take-over can re-run a command whose effect landed without its witness (id 49)

- **Where:** [supervise] "The supervisor's own death", [invariants] 3, [extend] command adapters.
- **What is wrong:** A command item whose effect landed before its witness was written is re-dispatched. No command adapter is required to be idempotent or to reconcile.
- **Consequence:** A double push attempt or a duplicate record.
- **Fix (skeptic judged SOUND):** Require each command adapter's witness contract to declare idempotence or a reconcile probe; for the lander, that origin is already at the expected sha. Add a fixture: kill the supervisor after the lander's push and before its witness, and the take-over must not push twice.
- **Gate:** that fixture.

### M28. The orphan sweep has no ownership or clean-and-merged predicate (id 51)

- **Where:** [isolate] "a sweep reaps orphans", [tests] 8.
- **What is wrong:** The sweep targets 497 temp directories whose source the research calls not attributable. Nothing protects a dirty or unmerged worktree; the census has one of each.
- **Consequence:** Deletion of foreign scratch and of uncommitted or unmerged work. Fixture 8's "counts return to baseline" rewards over-deletion.
- **Fix (skeptic judged SOUND):** Reap only what the supervisor allocated: lease-marked directories under a gov-owned scratch root, and worktrees it created. Require a worktree to be clean and merged (or pushed) before removal. Change fixture 8 so a dirty worktree and a foreign tmp dir both survive.
- **Gate:** that fixture.

### M29. Fixtures 4 and 7 never reach the deferral factory or the partial fan (id 53)

- **Where:** [tests] 4 and 7, [spawn] deferral factory.
- **What is wrong:** Fixture 4 replaces `claude` with a stub, so no `agent()` returns null. Fixture 7 invites a synthetic exit-1 guard. Neither covers the measured partial fan (up to 10 of 20 agents died), and [spawn] gives no unit-level outcome for a mixed fan.
- **Consequence:** The deferral path ships unproven, and done returns may be paid for again.
- **Fix (skeptic judged SOUND):** Specify the partial-fan outcome in [spawn]. Add a fixture in which some of k agents return null: the done returns persist, the nulls become deferred-platform, and the relaunch re-pays only the nulls. For fixture 7, require a guard with a missing interpreter path and one killed by a resource limit.
- **Gate:** those fixtures.

### M30. The in-flight counter has no feed and no release for dead agents (id 54)

- **Where:** [spawn] runtime.fanout counting, [supervise] agents in flight.
- **What is wrong:** The record never says what feeds the counter or how a dead agent's slot is released. Agents inside a script are invisible to hooks.
- **Consequence:** Leaked slots fill `runtime.fanout` and every later dispatch queues forever. Or, if hooks alone feed the counter, it under-counts.
- **Fix (skeptic judged SOUND):** Feed the counter from the script's declared concurrency at launch, or from SubagentStart and SubagentStop once fixture 6 proves they fire. Give each slot an expiry or reconcile it against live processes and journal state. Add a fixture: kill a driver holding 5 slots, and the next dispatch is admitted after reconcile.
- **Gate:** that fixture.

### M31. The SubagentStop hold has no bound and no malformed-input handling (id 55)

- **Where:** [spawn] "exit 2 holds an agent whose return fails".
- **What is wrong:**
  - The hold has no retry bound.
  - Empty, unparseable and oversized `last_assistant_message` values are not handled.
  - A crashed SubagentStop hook admits the stop, because onFailure has no effect there.
- **Consequence:** The agent is held indefinitely, or the item stops with nothing persisted and an unclear status.
- **Fix (skeptic judged SOUND):**
  - Bind the hold to `roles.retries` (or the 5 schema retries), then persist a refusal and route the item.
  - Specify handling for empty, unparseable and oversized messages, with a size cap.
  - State that a missing return after a stop means the item is unwitnessed and can be dispatched again.
  - Test it with a SubagentStop hook pointed at a missing path.
- **Gate:** that fixture.

### M32. Cadence items have no per-period witness (id 56)

- **Where:** [schedule] missed fire and lease, [tests] 10, [invariants] 3.
- **What is wrong:** A lease excludes only concurrent runs. A missed-fire catch-up on node B re-runs a period node A has already finished. Invariant 3 is undefined for recurring items.
- **Consequence:** The weekly Loop Review or the nightly bar runs twice per period, or never again.
- **Fix (skeptic judged SOUND):** Key each cadence witness by its period (ISO week or date), and consult it before acquiring the lease. Extend fixture 10: node A runs the period's item, then node B launches late and must skip.
- **Gate:** that fixture.

### M33. `next` has no answers for an empty frontier or bad inputs (id 57)

- **Where:** [decide] One derivation.
- **What is wrong:** Only "one act per frontier item" is defined. There are no answers for an empty frontier, malformed declarations, invalid policy values, corrupt witnesses or an unreachable remote. Two runs already stalled at BUILDING with all work terminal.
- **Consequence:** The supervisor ticks forever on no act, or acts on a guess.
- **Fix (skeptic judged SOUND):** Add a closed answer set: terminal, blocked (with a reason), invalid-input (naming the bad declaration, policy or witness) and stale-remote. Make each a declared supervisor transition. Add fixtures: an empty frontier closes the run, and a corrupt witness answers invalid-input.
- **Gate:** those fixtures.

### M34. Act binding misses Bash scripts and unbound sessions (id 58)

- **Where:** [act] act-binding rule, [invariants] 2.
- **What is wrong:** The rule covers only spawns, Workflow calls and transitions. The 25+ improvised scripts run through Bash. Behaviour for a session bound to no build, such as owner work or a review fan-out, is unstated.
- **Consequence:** Invariant 2 is false as built. Attended sessions are either refused everything or silently exempt.
- **Fix (skeptic judged SOUND):** Widen the rule to Bash execution of scripts outside the declared commands, or narrow invariant 2 and record the script class as unenforced. State the no-binding behaviour, and add a fixture for each.
- **Gate:** those fixtures.

## Low

### L1. Owed compaction checks have no disposition (id 12)

- **Where:** [sessions], [settled] owed CX-3 checks.
- **What is wrong:** Three owed checks have no disposition: whether a subagent's brief is re-injected after its own compaction, the re-attachment cap (5 files of 5,000 tokens each), and whether PreCompact can flush inside a subagent.
- **Consequence:** A future card over 5,000 tokens would come back as a path only, with no gate. The effect is small because SessionStart re-delivers the card and no subagent has ever compacted.
- **Fix (skeptic judged SOUND):** Dispose of each check in [sessions]: bound the card under 5,000 tokens with a size check in the build's units, and declare subagent compaction out of scope (0 of 2,708 transcripts compacted). Add a fixture that compacts a session and finds the card's content re-attached.
- **Gate:** the card-size check.

### L2. Invariant 8 has no fixture (id 13)

- **Where:** [invariants] 8, [tests].
- **What is wrong:** No fixture gates the permission-skip retirement. The test consumers `resume-tick.test.sh:368,385`, which assert the flag, are not named.
- **Fix (skeptic judged SOUND):** Add a fixture that greps every runtime launcher's argv for `--dangerously-skip-permissions` and fails on any hit, seen red on `resume-tick.sh:385`. Name the test consumers to re-point.
- **See also:** M23 (id 38).

### L3. The "hundreds of acts below 1,000 turns" claim is unmeasured (id 21)

- **Where:** [act] Lifetime.
- **What is wrong:** Calls per act were never measured, and the measured median is about 44 calls per unit. Compaction triggers on tokens (preTokens about 914k to 1M), not turns.
- **Consequence:** More relaunches than the design expects.
- **Fix (skeptic judged SOUND):** Add a fixture that measures calls and tokens per act for a thin driver, choose the lifetime default from it, and restate the trigger as tokens against `context.threshold`.

### L4. The dispatcher's 57 ms latency goal is untimed (id 24)

- **Where:** [enforce] One dispatcher entry per event.
- **What is wrong:** The research puts an in-process dispatcher at about 85 ms. A Bash call loads at least two packs.
- **Fix (skeptic judged SOUND):** Add a fixture that times the dispatcher on a benign Bash payload over 10 runs against the 57 ms baseline, or restate the goal as a measured budget once the dispatcher exists.

### L5. The new Runtime gaps have no key prefix (id 47)

- **Where:** [gaps-proposed] "New area Runtime: 1. ... 12.".
- **What is wrong:** The twelve gaps have no `gap-<area>-NN` key, so the register's acceptance join has nothing to match.
- **Fix (skeptic judged SOUND):** Name the prefix (for example `gap-rt-01`...`gap-rt-12`) and each gap's owner build. Update the register's re-measured counts.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=60 confirmed=56 refuted=4 unverified=0 blocker=0 high=6 medium=45 low=5 agents=11 out-tokens=170743

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] Relaunch, [spawn] first bullet, [tests] fixture 3 | high | high | confirmed | Read the blob 767187aa. [supervise] :300-302 says a driver is 'relaunched fresh, never resumed'. [spawn] :333-335 relies on a run that 'replays from its journal (`resumeFromRunId`)', and :341-343 makes 'the run journal' the fallback if SubagentStop does not fire. research-runtime-spawn.md [platform] says replay works 'within the same session, or after `claude --resume`' and that a fresh session has 'nothing to resume'. So a freshly relaunched driver cannot replay a dead driver's run. In the fallback case, where SubagentStop does not fire, a completed agent's return is then lost or paid for again, and fixture 3 cannot hold. | sound | - |
| 2 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] driver launch flags vs [act] Lifetime and [policies] runtime.driver-lifetime | high | medium | confirmed | [supervise] :293-294 launches drivers as `claude -p` with `--json-schema` 'set to the item's return schema'. [act] :325 and [policies] :481 make `build` the default lifetime, so one driver serves many items. A `-p` invocation takes one prompt and returns one `structured_output` against one schema (spawn return, `claude -p` row). A build-long `-p` driver would therefore have to be re-invoked for each item, either with `--resume` (which contradicts 'fresh') or fresh (which is in effect `item`). research-runtime-sessions.md:172 picks S2, 'a fresh driver per item'. The builder has to choose between them, so the effect is contained. | sound | - |
| 3 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[isolate] | high | high | confirmed | [isolate] :381-391 gives each unit a worktree branched from the build branch tip and says 'Release reclaims all of it'. No step carries a unit's commits back onto the build branch, and nothing orders integration between parallel units. The siblings say the opposite: flow-steps.md:156 build.unit-pass has 'commits queued by the executor', and the v2 dScopedBuild row has 'parallel units' commits queued by the executor in the shared worktree'. Two records answer one question, and committed unit work has no defined path to the build branch. | sound | - |
| 4 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[build] units and gap tables, [gaps-proposed] 'Already registered ... Their owners stand' | high | high | confirmed | The v2 dDeclaredLoop row (architecture-v2.md ~:704) already lists these deliverables: 'the `next` verb over the loop's state', 'the owner's pause, resume, withdraw and supersede', 'the executor launched where `run.host` says', and gap-flow-10. The dBoundRoles row lists 'returns through a schema-forced channel' and gap-roles-04. The dShippedRelease row lists 'lander hardening' and gap-deploy-07. Yet [build] :499-512 lists the `next` CLI, the client verbs, durable returns, and signal traps with per-worktree hooks for dWellOiledMachine, while :592-598 says 'Their owners stand' for gap-roles-04, gap-flow-10 and gap-deploy-07. RT-3 names only four gap moves. The client verbs at :277-281 omit `supersede`. dWellOiledMachine is a child of dDeclaredLoop, yet the parent's row already includes the executor launch. The BY DESIGN note covers only the position function, leases and the mailbox, not the `next` CLI or the client verbs. | sound | - |
| 5 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[extend] actor kinds, [supervise] Each tick, [act] | medium | medium | confirmed | The [extend] :435 actor kinds are command, role, hook and owner. layer-roles.md:345 lists 'a declared role, a command, a hook, the executor or the owner', and its matrix (:335) gives the executor build.unit-pass, build.acceptance and build.core. The [supervise] tick (:288-292) routes only command items and role or owner items, so hook items have no stated route. 'The executor' is never mapped to the supervisor or the driver. The roles layer's executor duties (:197-220: resolve inputs, key and class facts, recompute them at the spawn, wrap the work order) have no component in the record. The spawn return says Workflow scripts have no filesystem access, so the role harness cannot do these duties. | sound | - |
| 6 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[policies] runtime.relaunch and runtime.driver-refresh; [supervise] Relaunch; [sessions] | medium | medium | confirmed | [policies] :482-483 define both `runtime.driver-refresh` (fresh, compact-with-card) and `runtime.relaunch` (fresh, resume). [supervise] :300 says 'relaunched fresh, never resumed', which is absolute and contradicts the allowed `resume` value. [sessions] :403 cites only `runtime.driver-refresh`. In the record, `runtime.relaunch` appears only in its policy row, and [supervise] names neither key. Two keys answer one question. | sound | two-answers-to-one-question |
| 7 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[tests] fixture 2 | medium | medium | confirmed | Re-ran the probe on C:/projects/coding-governance/.git/runlog/driver.log. Every line is a driver verb event (--liveness 376, --dispatch 362, --check-commit 330, --brief 228, --rescope 142, ...), and `grep -ci workflow` printed 0. research-runtime-executor.md:153 names 'the improvised inline workflows' as the likely failures, and they are not in this log. Fixture 2 (:533-534), replayed over driver.log, therefore cannot see the acts it is meant to catch, and it passes trivially. | sound | fixture-passes-by-finding-nothing |
| 8 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[invariants] 2, [act] act-binding rule, [supervise] agents in flight | medium | medium | confirmed | research-runtime-spawn.md [paths] says Workflow `agent()` calls 'are invisible to every hook (`agent-cap.js:20-27`, `:1495-1497`)', and that a nested `workflow()` 'is not a tool call, so no hook sees it'. Invariant 2 (:451) and [act] :323-324 claim that any spawn `next` did not name is refused, and [supervise] :303-304 counts agents in flight 'across every Workflow call'. Hooks can bind only the Workflow tool call, not the spawns inside a script. [tests] :531-549 has no fixture in which an unnamed spawn or Workflow call is refused. | sound | - |
| 9 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[tests] fixtures 6 and 12 | medium | medium | confirmed | The [tests] heading at :529 promises fixtures 'each able to make the design lose'. Fixture 6 (:540) reads 'SubagentStop fires ... If not, the stated fallback', which passes on either branch and never checks that the fallback persists a valid return. Fixture 12 (:549) reads 'The cost ... measured', with no bound. Neither fixture can fail. | sound | - |
| 10 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[invariants] 7 vs [policies] runtime.hook-failure and runtime.below-floor; [sessions] binding | medium | medium | confirmed | Invariant 7 (:457) is unconditional, but [policies] allows `runtime.hook-failure=open` (:484) and `runtime.below-floor` may be `degrade` (:486). The witness list at :371-373 is Stop, SubagentStop and git hooks. research-runtime-hooks.md:24 records 'Errors exit 2, which SessionStart does not block', and the onFailure switch at :74 converts failures to exit 2. So a SessionStart binding failure neither blocks nor has a witness. [sessions] :395 makes binding depend on SessionStart, and resume misses the card 7 of 14 times. The record never says how act binding treats an unbound session. | sound | - |
| 11 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[extend] vs [policies] runtime.harnesses, runtime.scheduler, runtime.journal | medium | medium | confirmed | [extend] :439-445 says harness adapters, scheduler backends and journal sinks are registered contracts and that 'Runtime gains no code'. The selecting keys at :490-492 are closed enums of today's options: `runtime.harnesses` has the fixed value 'claude-code-and-codex', `runtime.scheduler` is single-valued (node-task, cloud-routine, ci-only), and `runtime.journal` is local-and-summary or local. A newly registered adapter cannot be selected without changing the key schema. [schedule] :414-418 uses a node task together with CI's schedule for read-only verdicts, which a single-valued key cannot express. | sound | - |
| 12 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[sessions] and [settled] owed compaction checks | medium | low | confirmed | [settled] :46-48 lists as owed 'a subagent's brief re-injected after its own compaction' and 're-attachment cap'. v2 ~:752-755 asks for the card file to be sized to come back, and for a check on whether PreCompact can flush in a subagent. [current] :196-198 records the measured facts, but [sessions] :393-404, [build] and [tests] dispose of none of them: no card-size bound, no subagent decision. The effect is small, because [current] :189 says the compact source re-delivers the card every time through SessionStart, and no subagent has ever compacted. So low. | sound | - |
| 13 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[invariants] 8 and [tests] | low | low | confirmed | Read the blob: invariant 8 is at :458, and [tests] 1-12 (:531-549) has no fixture for permission-skipping launches. Running grep for dangerously-skip-permissions over tools/ printed resume-tick.sh:59 (a comment), :385 (the launch), and resume-tick.test.sh:368 and :385, both of which assert the flag. The record names :385 as retired but names neither the test consumers nor a gate. | sound | - |
| 14 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[contract] engine kits | low | - | refuted | Premise false against the sibling records. layer-instruction.md:223-224 places memory-recall in Knowledge and runlog in Observability, both as expansions, and runtime.md:28 says 'The core never depends on an expansion.' The runtime record already covers both the right way: runlog as a registered journal sink in [extend] (:443, 'runlog, observability's store') and in [supervise] (:311), and hook packs come 'from the layers and kits that own them' (:356). Listing either as a Runtime engine kit would contradict the layer model. | unsound | - |
| 15 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] Relaunch, [spawn] replay, [policies] runtime.relaunch, [tests] 3 | high | medium | confirmed | Confirmed. research-runtime-spawn.md:101 says replay works only in the same session or after --resume, and that a fresh session has 'nothing to resume'. The record repeats that fact in its own summary ('Workflow replay needs the same session, or --resume'), yet [supervise] (:300-302) relaunches 'fresh, never resumed', runtime.relaunch defaults to fresh (:483), and [spawn] (:333-335, :341-343) relies on resumeFromRunId replay, naming 'the run journal' as the fallback if SubagentStop does not fire. On the main path, SubagentStop-persisted returns witness completed items, so the next-driven relaunch does not re-pay for them. The inconsistency therefore bites on the fallback path: there the journal cannot be replayed by a fresh session, so returns are lost (contradicting invariant 4) and fixture 3 fails. Graded medium because the path is narrow and the cost is contained (re-run tokens). | sound | - |
| 16 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[act] act-binding rule, [supervise] agents in flight, [invariants] 2, [tests] 5 | high | medium | confirmed | tools/hooks/agent-cap.js:18-27 printed: 'Agents spawned INSIDE a workflow sidechain remain uncounted and always will be — the script's agent() is not a tool call, so no matcher covers it'. research-runtime-spawn.md says nested workflow() 'is not a tool call, so no hook sees it'. Yet [act] (:323-324) claims to refuse 'any spawn ... that next did not name', invariant 2 (:451) says 'a spawn ... it did not name is refused', and [supervise] (:303-304) counts in-flight agents 'across every Workflow call'. A hook can bind only at the outer Workflow call, by its script and args. Inside an admitted harness, agent() calls and nested workflow() calls are neither refusable nor counted by a hook. SubagentStart may observe them but cannot block. The record names none of this residual. It is contained because the harness scripts are declared code, so medium. | sound | - |
| 17 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[tests] 2 | high | high | confirmed | .git/runlog/driver.log has 1964 lines, and grep -c -i workflow printed 0. Every row is a driver verb (counts: --liveness 376, --dispatch 362, --check-commit 330, ...). Fixture 2 (:533-534) replays only driver.log. research-runtime-executor.md:42 found the 17 inline Workflow calls and the 25+ ad-hoc scripts in session transcripts, and :153 calls them 'the likely failures'. None of those can appear in driver.log, so the fixture cannot count the class it exists to catch, and it would pass the act-binding design on an incomplete population. | sound | - |
| 18 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] CLI floor, [harness] node registry runtime facts, [supervise] headless launch | high | medium | confirmed | Re-probed. `claude --version` printed 2.1.292, `which -a claude` printed only /c/Users/d41ly/.local/bin/claude, and this session's transcript tail shows "version":"2.1.295" x7. The record knows about the split (its own summary and gap 2 say 'the PATH CLI is 2.1.292'), but [enforce] (:369-370), [harness] (:428-429) and [supervise] (:293) never say which binary is checked or which `claude` the supervisor launches. Built from PATH, every headless driver on this node is below the floor. Whether that fails open or is refused depends on an unspecified choice of what to read, plus RT-2. Graded medium rather than high because below-floor handling is still an open owner question. | sound | - |
| 19 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] Where it runs, [schedule] node-task backend, [invariants] 5 | high | medium | confirmed | A grep of the blob for launch, restart, reboot, host and systemd finds no mechanism that starts, keeps alive or restarts the supervisor. Only 'one supervisor runs per node' (:285), the host adapter row 'this node' (:440), and 'a take-over on any node' (:312-313) appear, with nothing saying who triggers that take-over. `git show HEAD:.unattended.conf` lines 132-137 describe the desktop scheduled-task pair as 'Named for the AGENT to call ... no script reaches the store', and ~/.claude/scheduled-tasks/ holds per-task prompt directories. So the node-task backend in [schedule] (:414-416) wakes a model session, not a no-model process. The missing host lifecycle is real. Its effect is that the loop stalls after a reboot, which is contained, so medium. | sound | - |
| 20 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[isolate] workspace per unit lease vs [act]/[policies] runtime.driver-lifetime=build | medium | medium | confirmed | In the blob, [isolate] (:381-385) allocates a worktree per unit lease, while [act] (:325) and [policies] (:481) default driver-lifetime to build. research-runtime-sessions.md picks 'S2. A fresh driver per item', and hooks C1 creates the worktree and scratch per unit. The record states no way for a build-lifetime driver's Workflow role agents to work in each unit's worktree. A session's working directory is anchored at launch, and agent threads reset to it, as this very harness notes. Under the defaults, later units would run outside their own worktree, which defeats fixture 8. | unsound | - |
| 21 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[act] Lifetime | medium | low | confirmed | [act] (:326-327) says 'a few calls per act fit hundreds of acts below the 1,000-turn compaction distance'. No return measures calls per act. research-runtime-executor.md gives a median of about 44 main-session calls per unit, with compactions at preTokens 914,072-1,001,711. Sessions research: 0 of 48 sessions under 1,000 turns compacted, and the median before compaction is 969,959 tokens, so the trigger is tokens, not turns. The claim is therefore unmeasured and untested. Its effect is contained: more frequent fresh relaunches (84k each). Low. | sound | - |
| 22 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[\harness] One guard core, [policies] runtime.harnesses | medium | medium | confirmed | [\harness] (:424-425) says Codex's events 'now match one for one'. The record's own platform summary and research-runtime-sessions.md:126 list only PreToolUse, SubagentStart, SubagentStop, PreCompact and SessionEnd for Codex. :133 says 'No Workflow tool ... (unverified)' and quotes Codex's docs: 'not a complete enforcement boundary'. The dispatcher (:352-354) needs SessionStart, PostToolUse, Stop and PostCompact, and the role harness is Workflow agent(). The returns do not bear out the one-for-one claim. Effect is limited to the opt-in claude-code-and-codex value, so medium. | sound | - |
| 23 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] Failing closed, [invariants] 7 | medium | medium | confirmed | [enforce] (:371-373) names only Stop, SubagentStop and git hooks as witnessed. research-runtime-hooks.md shows SessionStart 'Errors exit 2, which SessionStart does not block', and research-runtime-spawn.md says SubagentStart 'cannot block'. [sessions] (:395-396) makes SessionStart the act that binds a session to its build. The record names no witness for that binding and does not say how act binding behaves when the binding is missing, notably for attended sessions, which the supervisor does not launch with a known item. So invariant 7 is not grounded for the binding events. | sound | - |
| 24 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] One dispatcher entry per event | low | low | confirmed | [enforce] (:354-355) claims lazy packs stay 'within the 57 ms that one guard costs today'. research-runtime-hooks.md gives guards at 52-57 ms, node -e 0 at 39 ms, and in-process at about 39+3x15 ≈ 85 ms, 'neutral if lazy', which is untimed. No [tests] item times the dispatcher; fixture 12 times a headless driver start. A Bash call matches at least the write-allowance and gate-guard packs, so lazy loading still plausibly exceeds 57 ms. The stated goal is ungated, with latency-only effect, so low. | sound | - |
| 25 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[policies] runtime.fanout; [supervise] Agents in flight | medium | medium | confirmed | Record blob 767187aa matches. [policies] has `runtime.fanout \| an agent count \| 5` with no upper bound, and [supervise] counts in-flight agents under it. Neither line mentions agent-cap or FANOUT_CAP. tools/hooks/agent-cap.js:61-72 makes 5 a file-constant ceiling that is 'never raisable', which a repo may only lower through FANOUT_CAP in .agent-cap.conf, giving min(n,5) at each site and for the direct-spawn slots (TOOL-aRepatriatedFork-7). DECISIONS.md:44 (TOOL-aUnmannedHelm-1) records that the hook counter is racy. So the design creates a second, unbounded source for a bound already decided. One caveat: the in-flight total is a different quantity from agent-cap's per-site width, so the conflict is real but contained. | sound | - |
| 26 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[policies] runtime.reap; [supervise] 'reaps orphans and stalls'; [gaps-proposed] 7 | medium | medium | confirmed | [policies] gives `runtime.reap` the values orphans, orphans-and-idle and report. .process-monitor.conf:54-70 declares PROCMON_REAP_MODE with the closed set report/reap-orphans/reap-all, and reap.py:367-368 and :439-440 refuse anything outside that set. So `orphans-and-idle` has no counterpart, and the record never names reap.py --sweep. [contract] does list process-monitor as the supervision engine kit, which partly softens this, but the second key with a mismatched value set stands. Gap 7 is defensible as written: the research shows 0 live --sweep runs. The suggested rewording makes it more accurate. | sound | - |
| 27 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise]; [schedule] 'Where it runs'; [build] 'the supervisor' unit | medium | medium | confirmed | resume-tick.sh:1-18 is already an OS-scheduled, out-of-session process that runs every 10 minutes, takes --liveness as its only stale/terminal verdict, kills stale trees and launches detached claude -p. README:211/218 registers it as gov-resume-tick. The record names resume-tick only at :153, :299 and :569, all about the permissions flag. [contract] says 'unattended (becomes the supervisor and client verbs)', which hints at reuse. But [supervise] adds its own 'stalls' reaping and lease expiry without keeping --liveness as the single stale predicate, and [schedule]'s node-task backend never mentions the existing registration. A second stale judge is a plausible result. | sound | - |
| 28 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] 'Git hooks trap signals, and `core.hooksPath` becomes per-worktree'; [isolate] 'the worktree's own hooks path' | high | medium | confirmed | [enforce]:374 says core.hooksPath 'becomes per-worktree', and [isolate] says 'the worktree's own hooks path'. Gap 6 frames the defect as the absolute path running the primary tree's hooks. WIRE-INTO-PROJECT.md:855-858 asks for an out-of-tree copy so that a branch cannot make the guard inert. check-wiring.sh:615-618 (TOOL-aWeldedTribunal-7) documents that the relative .githooks runs each worktree's own hooks. The record cites neither and never says the per-worktree path is a trusted copy, so a unit branch could weaken its own gate. I grade it medium rather than high: the wording is ambiguous, the path is narrow, and the effect is limited to one unit's commits. | sound | - |
| 29 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] 'It needs a declared CLI floor'; [policies] runtime.cli-floor; [harness] node registry 'the CLI version against the floor' | medium | medium | confirmed | [enforce]:369-370 and [policies] declare an authored `runtime.cli-floor` 2.1.295, checked at session start. The aMendedFleet-61 spec:24 says its review 'rejected an authored version floor in favour of the launching session's own version'. unattended.sh:8790-8795 implements read_cli_version from AI_AGENT and explains why `claude --version` is the wrong source. The record cites none of this. | sound | - |
| 30 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] 'Driver sessions are launched headless ... an explicit permission allowlist'; [invariants] 8 | medium | medium | confirmed | [supervise]:296 fixes 'an explicit permission allowlist' for headless drivers. DECISIONS.md:225 (TOOL-aMendedFleet-116, owner 2026-10-07) moves runs to --permission-mode auto once node CLIs reach 2.1.281, with TOOL-aMendedFleet-117 as the build. grep finds no 'permission-mode', 'auto' or 116/117 in the record. The two are not strictly exclusive, since auto mode can honour allow rules, but the record neither reconciles the owner ruling nor raises it as a question. | sound | - |
| 31 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[current] 'No parallel units'; [isolate]; [tests] 8 | medium | medium | confirmed | [current]:166-167 states that the harness ratified 'parallelism route: none'. That route is TOOL-cBriefedPilot-21 (DECISIONS:76), which TOOL-aHoistedPass-10 (DECISIONS:179) superseded after TOOL-dUnstalledConvoy-7 recorded 'parallelism route: cleared'. The record repeats a stale carrier, unattended-build.js, of the kind TOOL-aHoistedPass-32 already lists. The criteria record's E3 condition 2 (shared mutable records) and E4 conditions 5-7 (merge without markers or loss) appear nowhere in [isolate], and fixture 8 tests only the index lock. | sound | - |
| 32 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[build] units 'the `next` CLI ...' and 'the client verbs'; [decide] client verbs; [gaps-proposed] 'Already registered' | medium | medium | confirmed | v2:704 (dDeclaredLoop) still holds 'the `next` verb over the loop's state', 'the owner's pause, resume, withdraw and supersede through the guarded command', and gap-flow-10. The runtime record's [build] lists 'the `next` CLI' and 'the client verbs' as dWellOiledMachine units, its gap move-table holds only gap-tool-03, gap-orient-12, gap-orient-14 and gap-conc-03, and it says of gap-flow-10 'Their owners stand'. :263 claims to settle the placement of `next` but marks nothing in v2 for amendment. So two chain builds claim the same units. | sound | amendment-leaves-its-other-half-standing |
| 33 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[build] unit 'the role harness's durable returns (the subagent-stop hook)'; [enforce] roles pack 'act binding'; [settled] table row 3 | medium | medium | confirmed | [settled]:37 assigns 'return validation at subagent stop' to dBoundRoles, and v2:705 gives dBoundRoles schema-forced returns and gap-roles-04. Yet [build]:504 lists 'the role harness's durable returns (the subagent-stop hook)' as a dWellOiledMachine unit, and [spawn]:336-339 designs that hook to validate against the schema. Act binding is likewise placed in the roles pack at :357 but is a Runtime unit at :501. Ownership is double-assigned. | sound | - |
| 34 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[isolate] 'Release reclaims all of it, and a sweep reaps orphans: today, 8 merged worktrees'; [contract] engine kits | medium | medium | confirmed | [isolate] says 'a sweep reaps orphans: today, 8 merged worktrees', and that is a supervisor duty in the core. branch_reconcile.py:15-17 already removes MERGED, EQUIVALENT and SUPERSEDED worktrees under --write with a recovery manifest. Yet [contract]:467 keeps branch-reconcile as an expansion, and :29 says 'The core never depends on an expansion'. So the core must either rebuild that classifier or break its own rule. | sound | - |
| 35 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[contract] record kinds and engine kits; [extend] journal sinks; [policies] runtime.journal | medium | medium | confirmed | [contract]:468 claims 'the run journal, the run record' as Runtime's record kinds, and :467's engine kits omit runlog. Yet the supervisor 'journals every event to runlog' (:311), and runlog is a journal sink (:443). runlog_lib.py:40 closes PRODUCER_FILES to driver/gates/pushes, runlog.py:499 takes --producer choices from it, selftest.py:1009 pins it, and record.py is 'one run's committed record'. Journaling supervisor events needs a runlog code change, and no [build] unit lists it. | sound | - |
| 36 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] 'Rules come in packs' / 'Each rule declares'; [extend] hook packs; [build] the one enforcement surface | medium | medium | confirmed | [enforce]:352-364 designs the pack declaration (event, matcher, owner, decision class, ...) from scratch. The record mentions fragments only at :157. `git ls-files '*.fragment.json' \| wc -l` printed 12. `git grep -l fragment.json -- tools` lists check-wiring.sh, check-hook-destinations.sh and govkit.py, and settings-merge.py is the documented merger (agent-cap.js wiring note). The enforcement-surface unit names none of these readers, though a single dispatcher entry per event changes what each of them reads. | sound | - |
| 37 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] Relaunch; [sessions] driver sessions; [policies] runtime.relaunch and runtime.driver-refresh | low | medium | confirmed | Read blob 767187aa: [supervise]:300-301 says a driver that dies, hits a limit or reaches context.threshold is 'relaunched fresh, never resumed', yet [policies]:483 gives runtime.relaunch the values fresh and resume. [sessions]:403 and [policies]:482 add runtime.driver-refresh (fresh, compact-with-card) for the same threshold relaunch. So two keys govern one event, and the prose rule contradicts a value the policy allows. Under non-default values the builder cannot tell which key wins. That is a real behavioural ambiguity, but a contained one. | sound | amendment-leaves-its-other-half-standing |
| 38 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] 'No session the runtime launches skips permissions' + [build] units + [invariants] 8 | high | medium | confirmed | Re-probed. resume-tick.sh:385 launches `claude -p --resume %q --dangerously-skip-permissions`. resume-tick.test.sh:368 and :385 assert the flag. check-unattended.sh:5770 scans resume-tick.sh. The unattended SKILL.md:16 has its first act CronCreate a keepalive tick. The record says the flag is 'retired' only in [supervise]:298-299. Its [build] units (:499-512) name no retirement or rewrite of resume-tick, and the record names none of these consumers. Graded medium rather than high: [supervise] does state the retirement, and the test arm would go red visibly if the flag were dropped. The real risk is an unowned change, not a silent unguarded ship. | sound | - |
| 39 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[decide] 'It replaces today's three derivations: --plan, --status and the run phase' | medium | medium | confirmed | [decide]:265-266 says `next` replaces --plan, --status and the run phase. Re-probed: tools/runlog/model.py:120, :126 and :140 classify --status as tree-blind, read-only and HEARTBEAT. stop-guard.js:167 tells the session to run `unattended.sh --plan`. unattended-build.js holds 20 --plan hits. The record names none of these readers and does not say whether the old verbs survive as aliases. A runlog heartbeat model fed only `next` calls would misread liveness. | sound | - |
| 40 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] 'Agents in flight are counted under the lease (runtime.fanout)' + [policies] runtime.fanout default 5 | medium | medium | confirmed | Re-read agent-cap.js:498-503. EFFECTIVE_CAP is min(FANOUT_CAP, MAX_VERIFIERS), set from the tracked .agent-cap.conf, and 'a declared value can only LOWER it'. :1533 says the budget is LIFETIME-PER-PROMPT, 'the TOTAL and never the concurrency bound'. workflows/README.md:22-25 lists FANOUT_CAP for four templates. gate-legs.json:1296 holds 'agent-cap restatement'. The record's runtime.fanout (in-flight, default 5) names none of these. So two enforcers would answer one question with different semantics, and a value above 5 cannot take effect. | sound | - |
| 41 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] 'One dispatcher entry per event' / 'Enforcement entries set onFailure: "block"' | medium | medium | confirmed | `git ls-files '*fragment*.json'` lists 12 files. `grep -rn onFailure tools` finds no wiring hit. settings-merge.py:435-436 builds an entry as {type, command} only, and :457-462 compares and rewrites only the command. [enforce]:352 and :366 collapse wiring to one dispatcher per event with onFailure:block, but neither section nor the enforcement unit at [build]:505 names the fragments, settings-merge, the adopters or the hook-destinations leg. So --check would keep reporting fail-open entries as wired. | sound | - |
| 42 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] '`core.hooksPath` becomes per-worktree' + [isolate] 'the worktree's own hooks path' | medium | medium | confirmed | `git config --get core.hooksPath` printed C:\projects\coding-governance\.githooks, and extensions.worktreeConfig printed true. In run-gates.sh at about :4930-4931, KF3 blanks any absolute or drive-letter hooksPath. check-wiring.sh:747-755 prints 'ok' for any set value that resolves to a pre-commit, and sets the path only in the unset branch. govkit/matrix.py:143 sets .githooks. [enforce]:374 and [isolate]:383 change the hooksPath scheme without naming any of these readers or writers. An existing clone with the absolute value would keep passing Check H. | sound | - |
| 43 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[policies] runtime.isolation, runtime.scheduler, runtime.hook-failure, runtime.below-floor | high | medium | confirmed | In v2: :483 is `build.worktree` (per-unit, parallel-only, shared; default shared), with preset row :637. :490 is `maintain.host` and :449 is `run.host`, both with the os-scheduler/cloud-routine vocabulary. :512 defines a preset as a 'complete assignment'. In the runtime record, [policies]:488 adds runtime.isolation (default worktree-per-unit), :490 adds runtime.scheduler (node-task, cloud-routine, ci-only), and :486 leaves runtime.below-floor with no default. No preset values are given, and [contract]:471 does not mention build.worktree or maintain.host. The isolation pair has opposite defaults. The hooks.bypass pairing is weaker, since it is a different concern (a recorded bypass), but the core claim holds. Graded medium: the completeness check v2 plans would catch the missing preset rows, so the effect is contained. | sound | - |
| 44 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[build] units and 'Gaps that stay where they are' | high | medium | confirmed | v2:699 heads the chain 'thirteen builds'. The v2:704 dDeclaredLoop row plans 'the `next` verb', 'the position engine', 'the executor launched where `run.host` says', the resume card fix, the compact hook and 'the owner's pause, resume, withdraw', and owns gap-flow-10. The v2:711 dScopedBuild row plans 'parallel units' commits queued by the executor in the shared worktree'. The runtime [build] takes gap-tool-03, orient-12, orient-14 and conc-03, yet lists the client verbs (:500) and signal traps (:506) as its own units. It keeps gap-flow-10 and gap-deploy-07 with their owners (:526, :598) and names no roster edits. [isolate] contradicts dScopedBuild's shared-worktree plan. Graded medium: the build is proposed and held as RT-3, so the consequence is double-planned work, not a wrong shipped result. | sound | - |
| 45 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[contract] 'unattended (becomes the supervisor and client verbs)' / [build] | medium | - | refuted | The facts reproduce: wc -c printed 66859 and 10237 against the ceilings 66860 and 10240 at template-size-limits.txt:143 and :151, and both legs exist in gate-legs.json. But the record is design-only, and BY DESIGN unit-level implementation detail belongs to each chain build's own specs. Byte budgets of prose carriers are exactly that kind of detail. The size legs themselves stop any overrun, so nothing defective ships. This is a planning preference, not a graded defect. | unsound | - |
| 46 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[build] 'The build: dWellOiledMachine' | low | - | refuted | memory/HYGIENE.md:175 requires 'a fresh CamelCase adjective-noun, [A-Za-z] only'. 'WellOiled' is the compound adjective 'well-oiled' and 'Machine' is the noun, so dWellOiledMachine fits the adjective-noun shape. v2's own chain already carries the three-word slug dMindYourWords. backlog.py:129 SLUG_RE accepts it. The premise of a broken rule does not hold. | none | - |
| 47 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[gaps-proposed] 'New area Runtime: 1. ... 12.' | low | low | confirmed | [gaps-proposed]:553-590 numbers twelve gaps under area 'Runtime' with no gap-<area>-NN key, while the register keys every row (for example gap-orient-14, gap-roles-17). Its re-measured blocks at :226-297 show that counts are updated on each addition. The impact claim that nothing ties the gaps to an owner is false: [build]:527 says dWellOiledMachine's 'new gaps are in [gaps-proposed]'. The missing key prefix stands, and it is cosmetic until registration. | sound | - |
| 48 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] Relaunch; [policies] | high | medium | confirmed | `grep -i 'attempt\|backoff\|retries\|park'` on the blob found only roles.retries in [contract]:471, and per v2:430 that key governs role-return retries, not driver relaunch. [supervise]:300-302 relaunches a driver that dies or hits a limit with no count, backoff or terminal state. [spawn]:347 covers only the session-limit hold. Today's resume-tick.sh:121 and :326 enforce RESUME_ATTEMPTS_DEFAULT=6 and report ATTEMPTS EXHAUSTED. The design drops that bound, so a repeatedly dying driver relaunches without end. Graded medium: the consequence is cost (84k tokens per start), not a wrong result or data loss. | sound | - |
| 49 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] 'The supervisor's own death'; [invariants] 3; [extend] command adapters | high | medium | confirmed | I read blob 767187aa at :312-313, which says 'loses only the tick in flight. A take-over on any node reads the same witnesses'. Invariant 3 is at :452 and the [extend] command-adapter row at :436 says only 'a command with its witness contract'. Grepping the blob for idempot, fenc and epoch found nothing. Nothing makes a command adapter reconcile an effect that landed without its witness, so a take-over can re-run it. I grade it medium rather than high: a lander re-push of the same sha is largely a no-op at git level, so the real harm is mostly a duplicate record, and that is contained. | sound | - |
| 50 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] take-over; [act] act-binding rule | high | high | confirmed | The take-over clause is at :312-313. Act binding at :323-324 refuses only what `next` 'did not name for this driver'. The blob has no epoch, token or fencing anywhere. research-runtime-spawn.md:23 confirms today's launch is detached through Start-Process or setsid, so a driver outlives its launcher. research-runtime-hooks.md:134 records the E4 index-lock failure. Two drivers serving the same act after a take-over is not excluded, though it only happens on the narrow supervisor-death path. | sound | - |
| 51 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[isolate] 'Release reclaims all of it, and a sweep reaps orphans'; [tests] 8 | high | medium | confirmed | Spec :388-389 says 'a sweep reaps orphans: today, 8 merged worktrees and 497 stale temp directories'. research-runtime-hooks.md:98 says the source of those directories 'is not attributable: mktemp -d is used by unattended, run-gates and others'. The spec defines no ownership predicate for temp directories and no clean-or-merged predicate for worktrees. The 'merged' qualifier appears only in the census, not as a rule. Fixture 8's 'counts return to baseline' does not protect foreign or dirty items. The loss is confined to stale scratch and a narrow worktree path, so I grade it medium. | sound | - |
| 52 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[tests] 2; [act] act-binding rule | high | high | confirmed | I re-ran the probe on the common git dir's runlog/driver.log. The verb histogram held only unattended verbs: --liveness 376, --dispatch 362, --check-commit 330, --brief 228, and so on. grep -c 'Workflow\\|agent(' printed 0, and git ls-files \| grep -c driver.log printed 0. Fixture 2 (:533-534) therefore draws its population with none of the improvised workflows or scripts that [gaps-proposed] 1 cites, so it can pass on the class it claims to test. It can still catch out-of-order verb transitions, which is why I grade it high rather than blocker. | sound | staged-break-substitutes-a-synthetic-value |
| 53 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[tests] 4 and 7; [spawn] deferral factory | medium | medium | confirmed | Fixture 4 (:537-538) follows research-runtime-spawn.md, which puts a stub `claude` ahead of the real one on PATH. That replaces the CLI, so no Workflow `agent()` returns null and the factory at :344-345 is never exercised by it. research-runtime-spawn.md:89 records partial fans of up to 10 of 20. [spawn] gives a per-agent null-to-deferral rule but no unit-level outcome for a mixed fan. The fixture 7 point overlaps the existing missing-path guard clause, but the part about the failure-kind class still holds. | sound | staged-break-substitutes-a-synthetic-value |
| 54 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[spawn] runtime.fanout counting; [supervise] agents in flight | medium | medium | confirmed | Spec :303-304 counts agents in flight 'across every Workflow call and every headless launch' and never says what feeds the counter or how a dead agent's slot is released. research-runtime-spawn.md:22-23 says `agent()` calls and nested `workflow()` calls are invisible to every hook. :126 says today's ledger still relies on a 45-minute expiry. The design states no expiry or reconcile step. | sound | - |
| 55 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[spawn] 'exit 2 holds an agent whose return fails' | medium | medium | confirmed | Spec :336-343 says 'exit 2 holds an agent whose return fails', with no bound and no handling for empty, malformed or oversized messages, nor for the hook itself crashing. research-runtime-hooks.md says onFailure 'has no effect on Stop, SubagentStop', so a crashed hook admits the stop. The 5 schema retries in research-runtime-spawn.md apply to Workflow schemas, not to this hook's hold. | sound | - |
| 56 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[schedule] missed fire and lease; [tests] 10 | medium | medium | confirmed | Spec :413 relies on a lease for 'two nodes never run the same item', and :416 runs a missed fire at the next launch. The blob has no period-keyed witness, which I confirmed by grepping it for 'period'. Invariant 3 at :452 cannot apply to a recurring item without one. research-runtime-sessions.md W2 says the lease handles double fire and that catch-up is untested. That covers concurrent fires, not sequential ones. | sound | - |
| 57 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[decide] One derivation | medium | medium | confirmed | [decide] at :264-275 defines only 'exactly one act per frontier item'. The blob states no answer for an empty frontier, malformed inputs or an unreachable remote. Its own census, at :133 and :558, measures 2 runs 'stalled at BUILDING with all work terminal', and the design does not close that case. | sound | - |
| 58 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[act] act-binding rule; [invariants] 2 | medium | medium | confirmed | The act-binding rule at :323-324 covers only spawns, Workflow calls and transitions. Invariant 2 at :451 says 'Every act was named by next', yet its own clause names only spawns and transitions. [gaps-proposed] 1 at :557 cites 25+ improvised scripts, which run through Bash and are uncovered. 'Attended sessions are drivers too' (:328) leaves a session bound to no build unspecified. | sound | - |
| 59 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] retirement of the resume-tick.sh:385 launch; [build] | medium | - | refuted | BY DESIGN: the build is design-only and each chain build writes its own unit specs, so naming each reader of a retired value is unit-level detail. The facts do reproduce. grep printed resume-tick.sh:59 and :385, and resume-tick.test.sh:368 and :385, which assert the flag. The spec does retire the launch at :298-299 and states invariant 8. Listing the suite's assertions belongs to the chain build's unit spec, not this layer record. | sound | retirement-inventory-misses-readers-by-value |
| 60 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[policies] runtime.fanout and runtime.hook-failure; [invariants] 7 | medium | medium | confirmed | The policy table gives `runtime.hook-failure` the values 'closed, open' (:484) and `runtime.fanout` 'an agent count' with no range (:487). Invariant 7 at :457 says 'Every enforcement rule fails closed'. With `open` allowed, the policy can falsify that invariant, so the record is internally inconsistent. agent-cap.js:1654 confirms that today's FANOUT_CAP rejects anything outside 1 to MAX_VERIFIERS. | sound | - |
