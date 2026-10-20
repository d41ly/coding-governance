# Research: Cloud coordination: the agentless head

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 150's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-25-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-cloud-and-scale.md`.

---

**THE AGENTLESS HEAD: research return (PLAY-dClosedLoop-1, researcher 25)**

## Recommendation

**Yes, build the head without an LLM, in one form only: it proposes and never assigns.** It should be a pure function computed from remote refs, held under a cadence-style lease, with units still claiming through their own leases. A head outage then falls back to the headless shape on its own.

The design already has two model-free deciders: Flow's position function behind `next`, and the supervisor. Runtime's `no-model-context` invariant reads "Neither the decider nor the supervisor holds model context … by construction: both are programs" (`layer-runtime` `[invariants]`, line 899). The head is a third such function, at fleet scope.

Two things the measurements show:
- **What wins on throughput is a commitment ledger, not the head.** It wins only in one case: several nodes drawing on one plan with a tight window. A shared reservation ledger keyed by plan wins there, and every node could run that same rule without any head.
- **Cutting streams mechanically buys almost nothing inside one build.** The measured median parallelism per build is 1.00. Placement pays off across builds.

## Candidates

All outside sources were read on 2026-10-19.

**C1. Central push placement, filter then score (Kubernetes, Nomad, Borg).** Losing test: H1. Result: **REJECTED** as the assign form; its filter and score survive inside C2.
- **Mechanism:**
  - The Kubernetes scheduler removes nodes that cannot run the work ("filter out nodes that cannot run the Pod"), then ranks the rest by weighted plugin scores. "Scheduling cycles are run serially, while binding cycles may run concurrently." A failed cycle returns the work to the queue (kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/).
  - Nomad's schedulers run "in parallel without locking or reservations", and the leader's plan queue can "do partial or complete rejections of a plan". Ranking there is bin packing plus anti-affinity (developer.hashicorp.com/nomad/docs/concepts/scheduling/how-scheduling-works).
  - Borg names "admission control, efficient task-packing, over-commitment" (research.google/pubs/large-scale-cluster-management-at-google-with-borg/). I could read only the abstract; the claim that tasks keep running while the Borgmaster is down is unverified.
- **Inputs:** capacity per node, constraints, affinity, priority.
- **Guarantee:** no over-commit, as far as the reports are accurate; one serial decision at a time.
- **Failure modes:** stale reports; a head outage stops all placement.
- **Losing test (written before running):** with the head down for 240 minutes, push should do worse than propose-and-claim on makespan.
- **Result (simulation, 20 seeds):**
  - Baseline makespan median: 726 minutes for every mechanism.
  - With the 240-minute outage, push rose to 936 minutes (+29%) and wasted 17,185 idle node-minutes. Propose-and-claim stayed at 726.
  - With one plan shared, a tight window and a 30-minute report lag, push dispatched onto a drained plan 289,128 times. Pull and propose-and-claim were each about 9,570.
- **Fit:** assigning makes the head a single point of failure. It also contradicts P5 (concurrency by lease) and P22 (position derived), since the head's word would replace a lease the unit holds.

**C2. Matchmaking that proposes, then the unit claims (HTCondor, with a time limit as on GitHub).** Losing test: H2. Result: **SURVIVES — recommended.**
- **Mechanism:**
  - The HTCondor negotiator "gives allocated slots to the schedds, and the schedd makes the final choice of which jobs run on which slots". "The condor_schedd can re-use a match the negotiator has given it to run multiple jobs in succession" (htcondor.readthedocs.io/en/latest/admin-manual/cm-configuration.html). The direct claim protocol between the schedd and the machine came only from old slides and search summaries; I could not decode the 2017 PDF, so that part is ambiguous.
  - GitHub runners work the same way with an expiry: "If the runner doesn't pick up the assigned job within 60 seconds, the job is re-queued so that a new runner can accept it" (docs.github.com/en/actions/reference/runners/self-hosted-runners).
- **Inputs:** C1's inputs, plus each unit's live claim.
- **Guarantee:** the lease's compare-and-swap commit gives no over-commit. Progress continues through a head outage, because a proposal that expires turns into a free claim.
- **Failure modes:** a proposal that goes stale costs one TTL of latency. A node that ignores proposals turns into plain pull.
- **Losing test (written before running):** with no outage, propose-and-claim's makespan should not be more than 10% worse than push.
- **Result:** equal (726 against 726), at 1.00 compare-and-swap attempts per unit. During the outage it lost nothing.
- **Fit:** units already claim by lease, with epochs and fencing (`layer-runtime` `[supervise]`, "Fencing"). A proposal is only an ordering hint on top of the claim, so P23 (claims trusted by key and source) and P26 (typed records) still hold.

**C2b. A replicated head with shared state and optimistic concurrency (Omega).** Losing test: H3, not run. Result: **folded into C2.**
- **Mechanism:** every node computes the placement function from the same refs and commits only its own claim. Omega describes "parallelism, shared state, and lock-free optimistic concurrency control" (research.google/pubs/omega-flexible-scalable-schedulers-for-large-compute-clusters/; abstract only).
- **Failure mode:** nodes reading different ref snapshots make conflicting commits, and compare-and-swap resolves them.
- **Losing test (not run):** conflict rate above hashed pull's. Within my model it is the same code as C2 run on every node, so the test could not discriminate.
- **Fit:** this is what C2 becomes once the head is a pure function, which is why the two are folded together.

**C3. Pull or self-claim from queues (Temporal, Buildkite, GitHub runners): the headless baseline the head must beat.** Losing test: H4. Result: **SURVIVES as the core floor**, with a hashed preference to avoid herding.
- **Mechanism:**
  - Temporal: "A Worker Process polls for a message only when it has spare capacity." Tasks persist in the queue until some worker polls (docs.temporal.io/task-queue).
  - Buildkite: jobs go to the first available agent in the queue, ordered by "how recently an agent within that queue successfully completed a job" (buildkite.com/docs/agent/v3/queues).
  - I did not read GitLab's runner documentation; no claim is made about it.
- **Inputs:** only the node's own capacity and its own live quota.
- **Guarantee:** no over-commit through compare-and-swap; no head at all.
- **Failure modes:** herding; and the node is blind to other nodes' in-flight use of a plan they share.
- **Losing test:** more than 1 compare-and-swap attempt per unit, or a worse makespan than a head.
- **Result:**
  - First-ready pull took 1.86 attempts per unit against 1.00 with a hashed preference, at a makespan of 726 against 734.
  - Herding is real in gov: one mailbox ref per build "took 4.5 times the ideal attempts at eight writers" (`coordination` `[design]` unit 6). Each attempt is a network round trip.
  - Pull failed the shared-plan quota test (H8).
- **Fit:** this is the shape the core already designs (leases, `runtime.hold-ceiling` → "a node with quota takes the build over", v2:1017).

**C4. Priority with fair share, reservation and backfill (Slurm; Airflow pools).** Losing test: H5. Result: **REJECTED for backfill.** Fair-share priority survives as a scoring term inside C2.
- **Mechanism:**
  - Slurm backfill starts a lower-priority job only if it "does not delay the expected start time of any higher priority jobs", and warns that "Backfill scheduling is difficult without reasonable time limit estimates" (slurm.schedmd.com/sched_config.html).
  - Slurm's fair share weighs usage decayed by `PriorityDecayHalfLife` (slurm.schedmd.com/priority_multifactor.html).
  - Airflow: "Once capacity is reached, runnable tasks get queued", then start by priority weight (airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/pools.html).
- **Inputs:** runtime estimates, past use, priority.
- **Guarantee:** reservations are not delayed, provided the estimates hold.
- **Failure mode:** heavy-tailed durations break the reservation.
- **Losing test (written before running):** the measured pass durations' coefficient of variation is above 1, or more than 20% of passes run past twice the median.
- **Result (probe M2):** p10 3, p50 14, p90 86, p99 471 minutes; 31% past twice the median, 16% past four times; coefficient of variation 2.04.
- **Fit:** gov has no per-item estimates yet (`build.spend-cap: measured`, v2:1095). Only `runtime.act-ceiling` (1.5 hours) bounds an act, so a reservation would rest on a ceiling, not an estimate.

**C5. Quota-aware routing with cooldowns (LiteLLM's router).** Losing test: H6. Result: **REJECTED as a local counter.** It survives as a reservation ledger keyed by plan, with a fresh account reading.
- **Mechanism:** the router filters out deployments over their TPM or RPM limits and picks the least used, or the least busy. After `allowed_fails` it applies a cooldown, then falls back to other deployments. Usage is shared across instances only through Redis, and "The cap is counted in process" (docs.litellm.ai/docs/routing).
- **Inputs:** its own count of requests and tokens per deployment.
- **Guarantee:** none against use the router never sees.
- **Failure mode:** in gov, the owner's attended session and every act on a node share one plan, so a local count undercounts.
- **Losing test (written before running):** with one plan shared, a tight window and a 30-minute stale report, the work fails to finish.
- **Result (simulation, 400 unit-minutes per 5-hour window, acts capped at 90 minutes):**

  | Admission rule | Estimate p50 | Estimate p90 |
  |---|---|---|
  | Plain pull | 48% done | 48% done |
  | Node-local hold (live reading, own in-flight acts only) | 48% | 54% |
  | Fleet-wide hold, report 30 min stale | 48% | 63% |
  | Fleet-wide hold, report 5 min old | not run | 100% (makespan 1,953, 12 kills over 20 seeds) |
  | Fleet-wide hold, live reading | 49% | 100% (makespan 1,976, 3 kills) |

  With ample quota (2,400 per window), every mechanism tied at 433 with 0 kills.
- **Fit:** the useful input exists, but only inside a session. The Claude Code status line receives `rate_limits.five_hour` and `rate_limits.seven_day` (`used_percentage`, `resets_at`). It "appears only for claude.ai Pro and Max subscribers … and only after the first API response in the session" (code.claude.com/docs/en/statusline). The reading covers the whole account, not one node. Today gov sees a limit only after the fact, through `StopFailure`, and that payload shape is unverified: "ONE FIELD IS ASSUMED, AND IT IS UNVERIFIED" (`tools/unattended/stall-recorder.js:26`).

**C6. DAG list scheduling (critical path, HEFT).** Losing test: H7. Result: **REJECTED** as a reason to cut builds across nodes. The critical-path rank survives only as an ordering term across builds.
- **Mechanism:** HEFT ranks tasks by upward rank over estimated costs and places each on the processor with the earliest finish time (Topcuoglu, Hariri and Wu, IEEE TPDS 2002, via en.wikipedia.org/wiki/Heterogeneous_earliest_finish_time and experts.arizona.edu/en/publications/performance-effective-and-low-complexity-task-scheduling-for-hete/; I did not read the full text).
- **Inputs:** the work graph and cost estimates.
- **Guarantee:** a good makespan when the graph is wide and the estimates are sound.
- **Failure mode:** a graph that cannot be cut.
- **Losing test (written before running):** median ideal parallelism per build ≤ 1.2.
- **Result (probe M1):**
  - 163 builds with specs hold 1,301 units; 90 builds declare `order`, covering 985 units.
  - Order-group widths: {1: 679, 2: 64, 3: 21, 4: 11, 5: 4, 6: 3, 7: 2, 9: 1, 10: 1}.
  - Of the 107 groups with more than one unit, 49 (46%) overlap in `Files touched`. The most shared paths are `tools/unattended/unattended.sh` (19), its test (17) and `run-gates.sh` (11).
  - Ideal parallelism per build: median 1.00, mean 1.32, max 4.00. After serializing the overlapping units: median 1.00, mean 1.17, max 3.00.
- **Fit:** Ray makes the same choice. It ranks nodes by locality, then low utilization, and picks at random among the top k (docs.ray.io/en/latest/ray-core/scheduling/index.html). In gov the locality to rank on is the build's own node.

**Where judgment stays, and the head does not reach:**
- A request that is not yet a build: placement and Plan's planner.
- Cutting a build into features and units with write sets: `design.decompose`, which is the architect's job (`flow-steps:185`).
- Whether an overlap inside a parallel group is benign. That is 46% of the measured groups, and `leases.overlap` only warns.

What the head decides mechanically: which READY unit goes to which node, and when to hold a launch on a plan near its window.

**Today's head inputs are absent or stale (probe M3, read-only `git cat-file` of `refs/gov/remote/runs/*`, which match `git ls-remote`):**
- There are 17 claims. 9 are non-terminal: 8 `held` and 1 `live` (aFrugalTurnstile, last beat 2026-10-11T01:28Z). The handed fact listed eight held and missed that `live` one.
- The newest non-terminal beat is 2026-10-13T13:58Z. At 2026-10-19T15:00Z, every non-terminal claim is 6.0 to 12.5 days stale.
- The `node:` field holds user names (`daily-agent`, `d41ly`), not fleet tags.
- No claim carries capacity, load or quota. `tools/playbook/fleet.toml` carries identity only: tag, user, host, `projects_root` and `variances`.
- No key anywhere bounds acts per node or per plan. `runtime.agents-in-flight` counts "agents in flight in one session" (v2:1022).

**Losing tests, as written before running:**
- H1: push loses if a head outage adds makespan that propose-and-claim does not.
- H2: propose-and-claim loses if its makespan is more than 10% worse than push with no outage.
- H3: replicated head loses if its conflicts exceed hashed pull's.
- H4: pull loses on more than 1 compare-and-swap attempt per unit, or a worse makespan than a head.
- H5: backfill loses if the pass durations' coefficient of variation is above 1, or more than 20% of passes run past twice the median.
- H6: a local counter loses if work fails to finish on a shared plan with a stale report.
- H7: cross-node cutting loses if median per-build parallelism is ≤ 1.2.
- H8: node-local admission loses on a shared, tight plan against a fleet-wide ledger.

## Seams the architecture must carry now

| # | Seam | Owning layer | Cost while gov stays offline |
|---|---|---|---|
| S1 | A capacity row per node in the node registry (acts and builds in flight per node), beside the "runtime facts" `[harness]` already adds; the supervisor enforces it locally | Runtime | One row per node; it bounds the supervisor on a single node too |
| S2 | A plan label per node: which subscription or key its acts draw on, never the credential, consistent with `runtime.act-auth` | Runtime | One label; nothing reads it until two nodes share it |
| S3 | A per-node report record: free slots, load (the core and memory detection `run-gates.sh` already does, e.g. lines 493–505 and `mempause`), the quota reading and its `resets_at` or the `StopFailure` reset, and the read time, so staleness is computed under P23 | Runtime writes; Memory declares the kind | Written locally at each supervisor beat; pushed only when leases or `build.push` push |
| S4 | A reservation ledger keyed by plan: admission charges a p90 estimate, by compare-and-swap, before launch. This is the piece that won H8 | Runtime (admission) | On one node it is the in-flight ledger the admission queue already plans |
| S5 | `place(frontiers, leases, reports, reservations, policy) → proposals`, a pure function that consumes `next`'s answers unchanged | Runtime | The one-node case is today's supervisor; declare the signature now |
| S6 | Lease acquisition takes an optional `proposed-for` and a TTL; past the TTL anyone may claim. This makes the proposal a wait with a deadline, as P39 requires | Flow (the coordination feature) | None: with no proposal, claim order is unchanged |
| S7 | A placement-backend registry at a core point; the built-in default is self-claim, and the head registers as an expansion. Its host is a lease-held cadence item, `refs/gov/leases/run/head/<period>`, so P28 holds | Runtime (`[extend]`; a sibling of verdict backends) | An empty registry with the default built in |
| S8 | Requests addressable before they are builds: a project-level request ref, claimable by lease, so an owner's prompt can be relayed to an available node. Today mailbox recipients are only "a build, or one of its units" (`coordination` unit 6), and `intake` is an amendment to a running build (`flow-roles` FR-8) | Flow (entry, dPlacedRequest) | The requesting node claims its own request at once, as it does today |
| S9 | A per-item-kind duration estimate with a core fallback (`runtime.act-ceiling` as the worst case), fed by `trace.cost` rows when they exist | Runtime fallback; Observability enriches | Already planned under `build.spend-cap: measured` |

## Records that disagree, and other researchers' questions

**Records that disagree:**
- The coordination record's `[design]` says dDeclaredLoop builds the coordination feature; v2's chain row (v2:1545) and the `leases.*` rows give it to dPlacedRequest.
- "Fleet register" means adopters (`layer-expansions:116`), while `fleet.toml` lists nodes. The overload needs one name each.

**Belongs to other researchers (one line each):**
- Platform: whether a headless `claude -p` act exposes `rate_limits`, and whether several nodes may share one subscription under the terms.
- Census: which layer cloud features belong to.
- Headless shape: C3 is that shape's baseline.

## Probes and how they were run

Everything was read-only. The scratch folder `.../scratchpad/d150/` was created, used, and deleted; `git status` shows only the five prompt files that were already untracked.
- **M1:** a Python parse of `memory/builds/*/spec/*.md` headers and `Files touched` sections.
- **M2:** `git log --since=2026-07-19 --format=%ct\t%s origin/main`, measuring gaps between commits of the same build's unit ids, kept between 2 minutes and 12 hours. This is a proxy: a gap can include idle time.
- **M3:** `git cat-file -p` over `refs/gov/remote/runs/*`.
- **Simulation:** a model, not the tree. It assumed 4 nodes with 2 slots each, 12 chained builds, and lognormal durations fitted to M2. Whether gov's nodes share a plan is recorded nowhere.

**Main records read**, all under `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\`:
- `2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
- `2026-10-14-build-PLAY-dClosedLoop-1-coordination.md`
- `2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`
- `2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`

**Code read**, under `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\`:
- `unattended\unattended.sh:2077-2087`
- `unattended\stall-recorder.js:11-30`
- `run-gates\run-gates.sh:470-473`
- `playbook\fleet.toml`

**Sources** (all read 2026-10-19):
- [Kubernetes scheduling framework](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/)
- [Nomad: how scheduling works](https://developer.hashicorp.com/nomad/docs/concepts/scheduling/how-scheduling-works)
- [Slurm scheduling configuration (backfill)](https://slurm.schedmd.com/sched_config.html)
- [Slurm multifactor priority](https://slurm.schedmd.com/priority_multifactor.html)
- [HTCondor central manager configuration](https://htcondor.readthedocs.io/en/latest/admin-manual/cm-configuration.html)
- [HTCondor Week 2017 admin tutorial (PDF, could not be decoded)](https://research.cs.wisc.edu/htcondor/HTCondorWeek2017/presentations/TueThain_AdminTut.pdf)
- [Omega (abstract)](https://research.google/pubs/omega-flexible-scalable-schedulers-for-large-compute-clusters/)
- [Borg (abstract)](https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/)
- [Buildkite queues](https://buildkite.com/docs/agent/v3/queues)
- [GitHub self-hosted runners reference](https://docs.github.com/en/actions/reference/runners/self-hosted-runners)
- [Temporal task queues](https://docs.temporal.io/task-queue)
- [Airflow pools](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/pools.html)
- [Ray scheduling](https://docs.ray.io/en/latest/ray-core/scheduling/index.html)
- [LiteLLM routing](https://docs.litellm.ai/docs/routing)
- [HEFT (Wikipedia)](https://en.wikipedia.org/wiki/Heterogeneous_earliest_finish_time)
- [Topcuoglu, Hariri and Wu, 2002 (record only)](https://experts.arizona.edu/en/publications/performance-effective-and-low-complexity-task-scheduling-for-hete/)
- [Claude Code status line](https://code.claude.com/docs/en/statusline)
