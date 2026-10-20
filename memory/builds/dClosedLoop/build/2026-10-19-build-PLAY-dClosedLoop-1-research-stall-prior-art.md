# Research: how other systems stop stalls and endless loops

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 147's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-22-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-stall-and-loop.md`.

---

## Prior art: how other systems stop stalls and endless loops, and which mechanisms fit gov

**Answer.** No single mechanism is enough, and that claim is backed by the tests below. Three properties come from outside systems, and each needs its own mechanism:
- **Bounded loops.** A counter that some quantity forces down.
- **Bounded waits.** A deadline on every wait, with a declared outcome when it passes.
- **Bounded thrash.** A breaker that classifies retries and stops the ones that cannot succeed.

Gov already has some of each: `review_state`'s strict-decrease rule, `RUNAWAY_CEILING`, the stop-guard's block cap, `flow.route-backs`, `runtime.act-ceiling` and `runtime.hold-ceiling`. In each case, though, the bound is keyed to something the loop can renew or reset. The tests below show where that breaks.

I wrote nothing in the repository. The five probes (P1–P5) ran in my session scratchpad, which is the system temp root, and are deleted. All sources were read on 2026-10-19.

### Corrections to the handed facts
- The stall recorder, the stop guard and the gate guard are in `tools/unattended/`, not `tools/hooks/`. `tools/hooks/` holds agent-cap, format-guard and scratch-guard.
- `RUNAWAY_CEILING="8"` is a file constant at `tools/unattended/unattended.sh:774`. Line 783 refuses `REVIEW_ROUNDS` at or above it. The kit defaults `RESUME_ATTEMPTS=6` and `RESUME_TURNS=40` are at `tools/unattended/resume-tick.sh:121-122`.

### Candidates, one per mechanism family

**C1. Attempt counters with backoff and retry classes**
- **Seen in:**
  - Temporal retry policy: backoff 2.0, maximum attempts "unlimited" by default, with the docs recommending Schedule-To-Close "to limit the total duration of retries" ([docs](https://docs.temporal.io/encyclopedia/retry-policies)).
  - Kubernetes Job: `backoffLimit` defaults to 6, delays of 10s, 20s, 40s… capped at ten minutes. `podFailurePolicy` can `Ignore` disruption failures or `FailJob` on a bug exit code ([docs](https://kubernetes.io/docs/concepts/workloads/controllers/job/)).
  - Argo `retryStrategy`: an `expression` ANDed with `retryPolicy` ([docs](https://argo-workflows.readthedocs.io/en/latest/retries/)).
  - Airflow per-exception retry policies ([docs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html)).
  - CrewAI `max_retry_limit` 2 ([docs](https://docs.crewai.com/en/concepts/agents)).
- **Guarantee:** a bounded number of retries for one key.
- **Failure mode:** the loop mints a fresh key each time, or a race gets counted like a defect.
- **Gov today:** "past `flow.route-backs` returns to the same item, the loop becomes an owner item" (flow-steps `[rules]`, lines 37-39). Whether "same item" means the item kind or the unit instance is not stated, so that is ambiguous.
- **Losing test (P1):** I parsed flow-steps `[transitions]` (24 rows, 9 stage edges) and drove adversarial traces through it with R=3:
  ```
  always-new-unit red:   K1 per item instance NEVER escalates in 1000 · K2 per edge kind at 10 · K3 per build at 10
  flow.adapt fresh stage: K1 NEVER · K2 NEVER · K3 per build at 11
  landing race:          all three escalate at 7
  ```
  - A counter keyed per item or per edge loses whenever `verdict.red-route: always-new-unit` or `flow.adapt: additive-recorded` (night-pass-two `[point 1]`, lines 109-113) mints new keys.
  - Every keying turns a landing race into an owner item. Kubernetes avoids that by classifying disruptions as `Ignore`.
- **Fit:** a policy bound. Key the counter by build, and add a retry-class table. A race or contention route should go to a queue, not count against the budget.

**C2. Deadlines and timeouts**
- **Seen in:**
  - Temporal: Start-To-Close per attempt, Schedule-To-Close over the whole execution, which defaults to infinity, and one of the two is required ([docs](https://docs.temporal.io/encyclopedia/detecting-activity-failures)).
  - Kubernetes `activeDeadlineSeconds` "takes precedence over its `.spec.backoffLimit`".
  - Argo `activeDeadlineSeconds` per workflow or template ([docs](https://argo-workflows.readthedocs.io/en/latest/walk-through/timeouts/)).
  - GitHub Actions job `timeout-minutes`, default 360 ([docs](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)).
  - An approval wait: "If a job is not approved within 30 days, it will automatically fail" ([GHES 3.5 docs](https://docs.github.com/en/enterprise-server@3.5/actions/managing-workflow-runs/reviewing-deployments)). This is ambiguous: the current github.com page does not state it.
  - An Airflow sensor timeout "fails immediately without retrying".
- **Guarantee:** wall-clock bounds on both an attempt and the whole run.
- **Failure mode:** it kills slow but healthy work, and a per-attempt ceiling multiplied by attempts and route-backs leaves no total bound.
- **Gov today:**
  - `runtime.act-ceiling` 1.5 h is a Start-To-Close.
  - Relaunch is capped by `RESUME_ATTEMPTS` (layer-runtime `[supervise]`, lines 393-394).
  - `resume-tick.sh:70-74` resets that count on any move, "a transcript-only move resets the count too".
  - I found no build-level deadline or spend bound in v2, layer-runtime or layer-flow (searched for spend, cost or wall budgets).
- **Losing test (P5b, a coarse regex over flow-steps item rows):** 14 rows route to a wait, hold, park, block or owner item, and only 3 name a deadline-like bound in the same cell. The 11 without include `deploy.parents` ("a parent unlanded or paused → holds", line 361), `test.flakes`, `review.dispose` and `life.quiesce`.
  - An owner breakpoint is "held until the owner's disposition record" (`[breakpoint]`, lines 448-454), and the owner queue's depth is "read with no bound (NP-18)" (v2 `[chain]`, dCalibratedLens).
- **Fit:** a static check that every wait declares a deadline and an outcome. Add a build-level schedule-to-close (a wall-clock deadline plus a spend budget) as a policy bound.

**C3. Heartbeats, liveness probes and watchdogs**
- **Seen in:**
  - Temporal heartbeat timeout: when it fires, "the Activity Task fails and a retry occurs".
  - Kubernetes liveness probe, which restarts the container.
  - Airflow zombie or undead task detection.
- **Guarantee:** a dead or hung worker is detected.
- **Failure mode:** a live process stuck in a loop keeps beating, so this proves liveness, not progress.
- **Losing test (read from code; running the suite is forbidden):**
  - `unattended.sh:8364` grades STALLED only on how long ago the last write and the last commit happened.
  - `resume-tick.sh:70-74` resets the attempt cap on a transcript entry.
  - So an act that writes on every turn without converging reads PROGRESSING, and its relaunch count never runs out.
  - `leases.renewal: activity` (v2 `[policies]`) has the same shape: an active but stuck holder renews forever.
- **Fit:** a runtime watchdog for death only. Progress must come from witnesses (C9/C10), never from activity.

**C4. Restart intensity, crash-loop backoff and circuit breakers**
- **Seen in:**
  - Erlang supervisor: more than MaxR restarts in MaxT seconds (default 1 in 5) and it stops its children and itself, leaving the decision to its parent ([docs](https://www.erlang.org/doc/system/sup_princ.html)).
  - Kubernetes CrashLoopBackOff: 10s doubling, capped at 300s, reset after 10 minutes of clean running ([docs](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)).
  - Fowler's circuit breaker: closed, open and half-open states, a failure threshold and a reset timeout ([article](https://martinfowler.com/bliki/CircuitBreaker.html)).
- **Guarantee:** thrash stops and escalates one level up.
- **Failure mode:** the reset window can be gamed by flapping.
- **Gov today:** the stop guard caps lifetime blocks at 6, under the harness's 8 consecutive blocks (`tools/unattended/stop-guard.js:53-58,153`). Nothing equivalent covers PreToolUse refusals.
- **Losing test (P4):** an agent rephrasing a write that one hook rule refuses. A detector keyed on the (action, observation) pair "never fires in 10 events". Keyed on the observation, meaning the refusing rule, it "fires at event 4".
- **Fit:** an escalation breaker per (act, hook rule): N refusals of one rule open the breaker and park the item to the remedy's actor. This extends the existing refusal contract, where a hook pack's refusal text names its rule and its remedy (layer-runtime, v2 `[chain]` dWellOiledMachine). A remedy whose actor is not the agent is non-retryable, as `FailJob` is in Kubernetes.

**C5. Deadlock detection and prevention**
- **Seen in:**
  - Wait-for graph: deadlock if and only if there is a cycle, but "not applicable to a resource allocation system with multiple instances of each resource type" ([Wikipedia](https://en.wikipedia.org/wiki/Wait-for_graph)).
  - Postgres runs its deadlock check only after `deadlock_timeout` (default 1s) because "the check for deadlock is relatively expensive" ([docs](https://www.postgresql.org/docs/current/runtime-config-locks.html)).
- **Gov today:**
  - `depends-on` "must form no cycle" (layer-memory, line 542).
  - The composed needs graph is checked acyclic (flow-roles-adoption, line 221).
  - The admission queue is a counted resource: six slots, "never refused" (v2 `runtime.agents-in-flight`). A wait-for graph does not apply to it.
- **Losing test (P3, a simulation of six acts each making a nested fan-2 call):**
  ```
  mode A (nested call queues on the shared counter): STUCK - 0 done, 6 acts waiting holding 6 of 6 slots, nothing changed since tick 3
  mode B (whole tree reserved up front, clamped):    all 6 acts done at tick 18
  mode A with 3 acts:                                 all 3 acts done at tick 9
  ```
  - The hazard only appears at saturation, so a low-load fixture is a rehearsal, not a test.
  - Ambiguous in the records: whether an act session's own Workflow call draws on the act's reservation or queues again.
- **Fit:**
  - A static rule against hold-and-wait: a nested spawn draws only from its parent's reservation.
  - A lazy runtime check in the Postgres style: a queue wait past T with no release → a stall record naming the holders.

**C6. Leases with fencing**
- **Seen in:** Kleppmann: a lease alone is unsafe under process pauses, so the storage side must reject a stale token ([article](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html)).
- **Gov today:** epochs are already designed in (layer-runtime `[supervise]` Fencing, lines 401-415).
- **Guarantee:** safety only.
- **Losing test:** the same as C3's lease case. Under `leases.renewal: activity`, `leases.expiry-hours` (24) never fires for a looping holder.
- **Fit:** keep fencing, and renew only on a witnessed item boundary.

**C7. Turn, recursion and budget caps in agent frameworks**
- **Seen in:**
  - LangGraph `recursion_limit`. Ambiguous source: the docs page states no number, current source has `DEFAULT_RECURSION_LIMIT = ... "10007"` ([source](https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/langgraph/langgraph/_internal/_config.py)), and third parties cite 25 ([forum](https://forum.langchain.com/t/best-practices-for-parallel-nodes-fanouts/1900)).
  - AutoGen termination conditions that combine with `|` and `&`: MaxMessage, TokenUsage, Timeout, Handoff, External… ([docs](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/termination.html)).
  - CrewAI `max_iter` 20 and `max_execution_time`.
  - OpenAI Agents SDK `max_turns` → `MaxTurnsExceeded`, or an `error_handlers` fallback ([docs](https://openai.github.io/openai-agents-python/running_agents/)).
  - Claude Agent SDK `max_turns` and `max_budget_usd` → `error_max_turns` and `error_max_budget_usd`; the budget "counts only the call's own spend; totals restored from a resumed session don't count" ([docs](https://code.claude.com/docs/en/agent-sdk/python)).
  - SWE-agent `per_instance_cost_limit` 3.0 ([docs](https://swe-agent.com/latest/reference/model_config/)).
- **Guarantee:** one run is bounded.
- **Failure mode:** the cap resets on every relaunch or resume.
- **Gov today:** `--max-turns` from `RESUME_TURNS` on each launch (layer-runtime, line 377). That bounds a session, not an item.
- **Losing test:** a relaunch resets the cap, as the SDK itself documents. I did not run it.
- **Fit:**
  - A per-item and per-build spend budget accumulated across relaunches from the `trace.cost` rows the design already writes.
  - AutoGen's OR-of-conditions as the shape for combining terminations.

**C8. Stuck detection by repetition**
- **Seen in:** OpenHands' StuckDetector: 4 identical action-observation pairs, 3 identical action-errors, 3 monologue messages, a 6-step ping-pong ([guide](https://docs.openhands.dev/sdk/guides/agent-stuck-detector)). Issue #762 records the polling false positive and made the thresholds configurable ([issue](https://github.com/OpenHands/software-agent-sdk/issues/762)).
- **Losing tests (P4):**
  - A legitimate `deploy.released` poll: "fires at event 4". That is a false positive.
  - A fix/red ping-pong: fires at 6.
  - Review rounds whose findings differ each round, with the count flat at 3: "never fires in 10 events". That is a miss.
- **Fit:** a runtime watchdog keyed on (item, verdict digest) and on the refusing rule. Exempt waits that declare their own deadline (C2), since that removes the polling false positive.

**C9. Stopping rules for iterative review**
- **Seen in:**
  - Self-Refine: at most 4 iterations; "Early iterations significantly improve output quality" and the paper reports "diminishing returns" ([paper](https://arxiv.org/html/2303.17651v2)). For example, Code Optimization goes 22.0 → 27.0 → 27.9 → 28.8.
  - Huang et al.: without external feedback, "performance even degrades after self-correction" ([paper](https://arxiv.org/abs/2310.01798v2)).
- **Gov today:** `review_state` re-arms only on a strictly smaller blocker count (`unattended.sh:12455-12480`), and v2 carries those states forward (flow-steps `[open]` S-1, line 690).
- **Losing test (P2, the function copied and run):**
  ```
  flat 3,3 -> NON-CONVERGENT at round 2 · oscillating 2,1,2 -> NON-CONVERGENT at 3 ·
  descent 12..1 -> CEILING at round 8 · REVIEW_ROUNDS=1 -> BOUNDED at 1 · fixed-count 2 -> BOUNDED at 2
  ```
  - The rule holds against every adversarial sequence I gave it.
  - The `until-no-blocker`, `until-no-high` and `until-clean` values of `review.design.rounds` and `review.follow-up: while-finding` are bounded only by `flow.route-backs`, not by this rule.
- **Fit:** a policy bound. Every `until-`/`while-` rule should also exit on a non-decrease, which reuses the seam that exists.

**C10. Termination proofs (variant or ranking functions)**
- **Seen in:** a loop variant strictly decreases on a well-founded order, so a loop can make only finitely many passes ([Wikipedia](https://en.wikipedia.org/wiki/Loop_variant)).
- **Fit:** the design rule behind C1 and C9. The variant should be a per-build tuple: (route-back budget remaining, open blockers), ordered lexicographically.
  - P1 shows why a per-item counter is not a variant: new items reset it.
  - `review_state` already is a variant, on its own count.

**C11. Workflow-net soundness and livelock checks**
- **Seen in:** van der Aalst et al., *Soundness of Workflow Nets*:
  - Soundness means three things: the option to complete, proper completion, and no dead transitions. A net is sound if and only if its short-circuited net is live and bounded.
  - It assumes strong fairness: "If we required termination without this assumption, all nets allowing loops … would be called unsound."
  - It is undecidable once reset arcs, meaning cancellation, are added. Gov's withdraw and supersede are cancellation.
  - Source: vdaalst.com/publications/p628.pdf, pages 2-3 and §5-6.
- **Losing test (P5, on the real `[transitions]` table plus a planted repository stage):**
  ```
  table as read: no state without a route to a terminal · uncounted non-owner cycles: none
  planted stage, no exit:   ['repo-check'] cannot complete · uncounted cycle repo-check→repo-check
  planted stage with exit:  completes (sound) · uncounted cycle repo-check→repo-check still present
  ```
  - Soundness passes the third case while an uncounted loop survives. Agents are not fair schedulers, so soundness is necessary but not sufficient.
  - With counters bounding every cycle the state space is finite, and reachability is decidable again.
- **Fit:** a static check at composition (flow-roles-adoption, line 221). It must cover the item-level `Then` routes too, which are prose today. The join gap-flow-15 already owes them; P5 parsed only the build table.

### Static against dynamic

**Checkable on the composed flow before a build runs.** Each check is O(V+E) at the push, on the composer the design already has:
- Every state reaches a terminal (option to complete), and every route is reachable (no dead items).
- Every cycle passes a counted edge. Drop the counted and owner-actor edges, and the rest must be acyclic. This needs no cycle enumeration.
- Every wait declares a deadline and an outcome, and every owner item has a declared default when its deadline passes.
- Every nested spawn draws from its parent's reservation.
- `depends-on` and the needs graph stay acyclic, as already designed.

Limit: these checks cannot see a loop that mints its own keys (P1) or a refusal that an agent cannot satisfy.

**Only checkable at run time:**
- The per-build variant decreases.
- A repeat of (item, verdict digest).
- A breaker per hook rule.
- A queue wait with no release (Postgres-style lazy check).
- A heartbeat as the death check.

Costs: counters and deadlines are close to free. Repeat detection is cheap but produces false positives unless declared waits are exempt (P4). Judging progress with an LLM is costly and unreliable, per Huang et al., so do not use it.

### Recommended combination
1. **One per-build variant: a route-back budget (C1/C10, keyed per build).** It is the only keying that survived P1's minted-key and `flow.adapt` traces. Classify races and contention as `Ignore`-class, so P1's landing race goes to the landing queue instead of the owner.
2. **`review_state`'s strict decrease on every `until-`/`while-` rule (C9).** It is already built and survived all of P2. Self-Refine and Huang support stopping early.
3. **A static check on the composed flow: completion, counted cycles, and a deadline on every wait (C11 + C2).** It catches the uncounted loops and deadline-less waits that repository stages and scenarios bring, which P5 caught and soundness alone missed.
4. **Deadlines with declared outcomes, including the owner (C2).** These close the 11 deadline-less waits and the unbounded owner queue. GitHub fails an approval after 30 days, and PagerDuty shows that escalating alone ends in a silent assignment ([docs](https://support.pagerduty.com/main/docs/escalation-policies)).
5. **A refusal breaker per (act, hook rule) with retry classes (C4).** It is the only mechanism that caught P4's hook-refusal loop. It reuses the refusal contract.
6. **A spawn reservation without hold-and-wait, plus a lazy queue-stall check (C5).** It removes P3's deadlock at saturation.
7. **Heartbeats and fencing kept for death and safety only (C3/C6).** Lease renewal and the relaunch counter should key on witnessed progress. As built, `resume-tick.sh:70-74` resets on activity.

Rejected as the sole mechanism:
- Per-attempt turn caps (C7): reset per run.
- Repeat detection alone (C8): misses changing findings in P4.
- Soundness alone (C11): passed an uncounted loop in P5.
- Per-item counters (C1 K1): never escalate in P1.

One line for the census researcher: `resume-tick.sh:70-74` and `unattended.sh:8364` are a live progress-blind bound in today's code.

Files I read: `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/unattended/unattended.sh`, `.../tools/unattended/resume-tick.sh`, `.../tools/unattended/stop-guard.js`, `.../tools/unattended/stall-recorder.js`, and `.../memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`.
