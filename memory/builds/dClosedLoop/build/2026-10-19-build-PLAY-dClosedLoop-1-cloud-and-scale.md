# Cloud features, scalability and load balancing: every unit claims its own work, a head only offers

**Serves:** research PLAY-dClosedLoop-1

The owner opened a part of the design never touched before: gov working in the cloud, scheduling and balancing work
across several node units of one project in real time. Nothing is built now. The question is what the architecture
must carry so that the feature can be designed and added later without a redesign. Five researchers each took one
question, and their returns are saved verbatim beside this record. This record answers the owner's three questions,
reports the defects the probes reproduced in the leases the chain already plans, recommends a shape and the seams the
core carries now, and puts the choices it cannot make itself to the owner. The review debt the owner's first sentence
parks is recorded in the build README's parked decisions (`a7e85f424`).

## [words] The owner's request, 2026-10-19

> Record the review debt (and any previous ones still owed) for now and let's review another piece we have not
> previously touched: cloud features, scalability, load balancing. What layer should these features belong to?
> Currently, Gov is a self-contained, offline governance project that installs over a target repo and acts as a
> single independent unit. Running jobs over several concurrent nodes simply runs independent copies and no
> real-time coordination happens (yet), everything happens only after an origin merge and repull onto the target
> node. However, this project is eventually expected to work in the cloud environment, scheduling and distributing
> work concurrently over several nodes working on the same project and build. This feature is NOT to be built yet
> (it's to be designed at a later time) but the architecture itself is to be planned for these capabilities.
>
> Projected use case: each Gov's application to its target repo becomes that Adopter's 'node unit', coordinating
> work with with the other available units in real time. The shape of this feature is to be researched - should it
> be headless, where each unit coordinates through a endpoint, independently claiming their work and relaying
> memories and decisions? Should there be an agentless governing head (without the use of an llm), which is a
> template-driven mechanism that receives information from available units per governed project, monitors each
> individual node's hardware load and plan limit utilization, creates and breaks down work streams by build
> mechanically to ensure efficient resource use, relays owner's query as a prompt directly to the available 'node
> units'? Or should it be an agent-driven head, which uses another llm subscription (say claude) or an api key to
> monitor units and plan their workload through the same conventions we're building (runtime/flow/role for the head
> piece)?
>
> This architecture should be designed ready to accommodate for this plan.

## [questions] Five researchers, one question each

| Dispatch | Question | Return |
|---|---|---|
| 148 | Where the design and today's tree assume one node, where they are ready for units coordinating in real time, and which layer cloud coordination belongs to. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-cloud-census.md` |
| 149 | Whether units should coordinate headless, claiming work and relaying memories and decisions through a shared endpoint. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-cloud-headless.md` |
| 150 | Whether a governing head with no LLM should place work by load and plan limits, and in what form. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-cloud-mechanical-head.md` |
| 151 | Whether the head should be an agent on another subscription or key, governed by gov's own runtime, flow and roles. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-cloud-agent-head.md` |
| 152 | What Anthropic's limits, terms, cloud runtimes and security allow and require of units and a head. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-cloud-platform.md` |

## [answer] The owner's questions, answered

- **Which layer?** A new expansion, named `fleet` once the adopters' register gives that word back (CL-1). By the
  design's own test it belongs nowhere else: one node already carries a build from request to landing alone, so
  scheduling across nodes is never core (v2 `[layers]`, P28). Integrations holds adapters only, with no programs,
  policies or records of its own, and observability may read but never decide (dispatch 148, section 3). What the
  fleet coordinates stays core and safe offline:
  - flow's leases, mailbox, registers and change feed, written to git by compare-and-swap, git staying the store of
    record as the owner's NT-14 settled;
  - runtime's per-node supervisor, admission queue and commit queue;
  - every verdict, computed on the node (P3).
  The fleet attaches only at points the core declares, and the core lacks seven of them today ([design-today]).
- **Headless, an agentless head, or an agent-driven head?** All three have a place, and they are not equals:
  - **Headless is the floor.** Every unit claims its own work by lease, and goes on doing so when everything above it
    is down. Eight nodes racing for one lease produced exactly one winner in 10 of 10 rounds (dispatch 149, P1).
  - **An agentless head may be added, and it only offers.** A model-free function reads every node's beat and every
    build's ready set and offers units to nodes; each unit still claims through its own lease. Simulated over 20
    seeds, a head that assigns lost 29% of makespan during a four-hour outage, 936 minutes against 726, while one that
    offers matched it with the head up and lost nothing with it down (dispatch 150, C1 and C2).
  - **An LLM serves as a judge role only,** for a record no rule can type, choosing within a closed set of routes the
    program computed, on another subscription or key if the owner sets one. This keeps the owner's third option where
    judgment is needed: the head's LLM part is a role run through the same runtime, flow and roles as any act. What
    it drops is letting that role drive. In 11 identical runs an LLM head made the same safe choices as a program but
    placed them two different ways, at about $0.10 and 15 s per decision against 38 ms, and a standing model session
    breaks Runtime's no-model-context invariant, P25 and P26 (dispatch 151, F1 and F5).
- **Is the architecture ready for it?** Half of it is. The shared truth is already multi-node and works offline. The
  deciding half is missing: no node publishes its presence, capacity or plan; nothing finds work another node released;
  nothing above a node can offer it work; nothing addresses a node or the whole project; and the plan limit, which is
  per account, is seen only after it is hit (dispatch 148, section 1; dispatch 152, section 1). The probes also
  reproduced two defects in the leases the chain already plans ([defects]).

## [today] What gov does today, measured

- **Four nodes, one remote, no live coordination.** Landing merges by node since 2026-09-15: a 47, d 13, b 1, c 1
  (dispatch 148, section 2).
- **Claims are the only shared state on the remote, and they are stale.** `git ls-remote origin 'refs/gov/*'` returns
  17 run claims and nothing else. Every claim is a parentless commit, so the remote keeps no history, and each names a
  user rather than a fleet tag. Of the 9 not marked landed, 8 belong to builds already closed, their beats 145 to 301
  hours old (dispatches 148 and 150; `gap-conc-02` and `gap-conc-06` already record both).
- **Coordination happens at the merge.** Main carries 21 reconcile-related subjects since 2026-09-15, two of them
  across nodes; 8 merges in 30 days conflicted, each in a shared generated or guide file; `memory/LIVE.md` took 331
  commits in 30 days, 163 of them naming a reconcile or a conflict (dispatch 148, section 2).
- **A plan limit is seen only after it is hit.** This node's transcripts hold 650 quota readings in 208 files, every
  one a rejection, none carrying the headroom left (dispatch 152, section 1).
- **Builds are narrow.** Over 163 builds with specs, the median parallelism inside a build is 1.00, and 46% of the
  parallel groups touch the same files (dispatch 150, M1).
- **Pass durations are heavy-tailed.** The median pass takes 14 minutes, p90 86 and p99 471, a coefficient of
  variation of 2.04 (dispatch 150, M2).

## [design-today] What the converged design already has, and what it lacks

It has the shared truth (dispatch 148, section 1):
- leases for builds, units and cadence runs, each with an epoch and compare-and-swap, an offline queue that yields on
  conflict (`leases.offline`), and overlap checks;
- a mailbox per build, one append-only ref per writing session, and create-only decision and problem registers;
- a node-local change feed, and Runtime's memory-mirror point, which the owner's NT-14 opened for a cloud database;
- hosts as registered names (`run.host`, `kits.host`, `maintain.host`, `cloud-routine` among them), notification
  channels, and the integrations point for cloud hosts and remote CI;
- `build.push: every-pass`, so another node reads a build's witnesses at its next fetch.

It lacks the deciding half, seven points the core must declare (dispatch 148, section 3):
1. a way for a node to find leases it does not hold, released or expired;
2. a recipient that names a node or the whole project;
3. a doorbell point for live delivery, the wait `gap-conc-05` already records;
4. a source that can offer a node work, whose offer the node's own claim re-checks;
5. a record of a node's presence and capacity;
6. a reading of plan usage per account, for admission;
7. a path for the owner's request to reach another node with its provenance intact.

## [defects] Defects in the leases the chain already plans

The headless researcher ran the design's lease protocol against local bare repositories (dispatch 149, the probe
table):
- **Fencing is check-then-act.** The commit queue and the lander re-read the epoch from the remote, then push
  (layer-runtime `[supervise]`). A holder replaced between that read and its push still landed its stale work (P2(a)).
  The same work pushed together with a new lease beat commit, in one `git push --atomic` under `--force-with-lease`,
  was refused at the remote, and the branch stayed unchanged (P2(b)). Re-pushing an unchanged lease ref checks
  nothing, since the server never sees it (P2(c′)), so the fence must be a new beat.
- **A pruned lease restarts its epoch.** The supervisor prunes terminal claims, and a later proposal deletes lease
  refs at release. A claim queued offline then wins on reconnection, holding a unit another node already landed, at
  epoch 1 (P3, case 3). Kept as a terminal tombstone instead, the queued claim was refused (P3, cases 1 and 2).
- **Separate pushes leave orphans.** A landing whose release and `landed` notice went as separate pushes left main
  landed and the lease live when the remote dropped between them; one atomic push wrote all three or none (P5).

Smaller ones, each found by reading:
- expiry is judged by the reader's clock against the holder's own stamp (`tools/unattended/unattended.sh:2152-2185`);
- messages carry no order across one build's session refs, so a relayed `changed` can arrive before the `confirmed`
  it supersedes (dispatch 149, family 5, a test the build must run);
- the cadence lease grammar lists its kinds literally, against Runtime's rule that a registered name never meets a
  literal list (dispatch 151, seam 4);
- P39's rework budget is keyed to builds and intake content only, so a cadence run's loop has no bound (dispatch 151,
  seam 5);
- `--bare` is set to become `-p`'s default, and bare mode reads neither the OAuth login nor the setup token that
  `runtime.act-auth` lists first (dispatch 152, section 3).

## [shapes] The three shapes, measured

| Shape | Measured | Verdict |
|---|---|---|
| Headless: each unit claims through git leases | one winner in 10 of 10 races of eight nodes; a spread start cut the herd from 36 claim attempts to 12 (dispatch 149, P1 and P6) | the floor, and already the design's shape |
| Headless through a lease service (etcd, Consul, Postgres locks) | a service's lock cannot fence a write it never sees, and a node offline for a day can neither renew nor queue (dispatch 149, families 2 and 3) | rejected as the store; a lease-store adapter only if it passes the fence fixture |
| An agentless head that assigns | +29% makespan during a four-hour outage; with a 30-minute stale report it dispatched onto a drained plan 289,128 times (dispatch 150, C1) | rejected |
| An agentless head that offers, units claiming | equal makespan with the head up, nothing lost with it down, 1.00 claim attempts per unit (dispatch 150, C2) | recommended |
| Admission by a ledger keyed by plan | on a shared, tight plan, plain pull and node-local admission finished 48 to 54% of the work, and a ledger with a live reading finished all of it (dispatch 150, C5) | the real balancing gain, which every node can run with no head |
| Cutting builds into streams | median parallelism inside a build 1.00 (dispatch 150, C6) | rejected; offers pay across builds |
| An agent head that drives | 11 identical runs: no hard rule broken, no injection followed, two different placements; $0.064 to $0.113 and 12.5 to 20.9 s per decision (dispatch 151, F1) | rejected as a driver |
| A model-free head calling an LLM judge role | 6 runs, the same route every time; $0.080 to $0.090 per call, and no call at all on a fully typed fixture (dispatch 151, F5) | recommended where a record has no type |

## [scale] What grows with the number of units

- **Claim attempts.** Claiming the lowest free unit first costs n(n+1)/2 attempts for n nodes, 36 at eight; starting
  from a spread unit cost 12 (dispatch 149, P6).
- **Model capacity grows with pools, not nodes.** Every node signed into one account draws on one five-hour window
  and one weekly limit, so a node added on the same plan adds hardware but no model capacity. Capacity scales with
  accounts, seats or API workspaces, and a ledger keyed by plan keeps the nodes sharing one from draining it (dispatch
  152, section 1; dispatch 150, C5).
- **Writers on one ref.** One mailbox ref per build took 4.5 times the ideal attempts at eight writers, which one ref
  per session already fixes (`gap-conc-04`).
- **News.** A fetch takes 0.6 s, but news waits for the reader's read points (`gap-conc-05`); the doorbell point is
  where a faster transport attaches.
- **Landings.** One landing at a time, a median 334 s per full bar under the lander's lock (`gap-conc-07`).
- **Refs.** Leases kept as tombstones grow with units, so they are pruned once no queued claim can still arrive.

## [platform] What the platform allows and requires

All from dispatch 152:
- **The limit unit is the plan, not the node.** Pro and Max limits are a five-hour window and a weekly limit per
  account; Team and Enterprise limits are per seat; API limits are per organization and model class. Admission and
  any head therefore count pools: the account, seat or workspace a node's acts draw on.
- **Usage is barely readable.** The status line carries the account's used share and reset time, documented for Pro
  and Max in interactive sessions only; API keys carry organization-wide headers; the usage API lags about five
  minutes and covers API use only. A reading must carry its source and its age, and a head trusts it only by key and
  source (P23).
- **Hosted cloud sessions cannot write gov's refs.** Anthropic's cloud sessions and routines push branches only, so a
  hosted cloud node cannot acquire a `refs/gov` lease without a transport that falls back to a branch namespace; a
  self-hosted or Actions host can.
- **The terms leave an owner's own unattended fleet on one subscription ambiguous.** The plan limits assume ordinary,
  individual use; setup tokens are offered for scripts and CI; products built for others should use API keys.
  Anthropic's legal page sends such questions to its sales team, so this is an owner action, not a design fork
  ([owed]).
- **Security.** No credential crosses a coordination record. A relayed prompt is data with provenance, never consent.
  An endpoint is a new copy of an adopter's records, under its own retention. A head serving several adopters must
  isolate each one's configuration, working directory and egress.

## [design] The recommendation: P40, a `fleet` expansion, and the seams the core carries now

A new principle carries it: **P40 A unit claims its own work; anything above it only offers.** Each node unit carries
a build from request to landing alone and offline. Across units, the one grant is a lease the unit acquires itself,
fenced in the same atomic push as the work it covers. A head, an endpoint or a scheduler may offer, relay and measure,
but it never assigns, never decides a position or a verdict, and never holds the only copy of anything, so losing it
costs latency and never correctness.

1. **The truth stays core, in git.** Leases, mail, registers, the change feed, bindings and the card stay git refs
   written by compare-and-swap. Git stays the store of record, as the owner's NT-14 settled, and every verdict is
   computed on the node (P3). An endpoint is an adapter that carries the same records faster.
2. **The fence travels with the effect.** Every effect push, a pass push, the lander's push to main, a release with
   its `landed` notice, carries the holder's new lease beat in one `git push --atomic` under
   `--force-with-lease=<lease>:<tip seen>`. This replaces re-reading the epoch before the push, and merges two pushes
   into one.
3. **A lease is never deleted.** A release writes a terminal tombstone, and the epoch rises monotonically for the
   lease's whole life. A claim queued offline longer than `leases.queued-claim-days` is refused on reconnection, and a
   tombstone may be pruned only after that age.
4. **Expiry is judged by a declared clock:** the holder's stamp corrected by the clock offset the node registry
   records, or an observer seeing the tip unchanged for `leases.expiry-hours`, never the reader's raw clock against
   the writer's stamp.
5. **Messages are causal and keyed.** Each carries its session's sequence number, a take-over names its predecessor's
   last message, and `confirmed` and `changed` carry the interface's content key. A dependent acts on the recomputed
   key, never on arrival order.
6. **Each node beats its presence and capacity.** The supervisor's beat, already pushed with each pass, carries the
   node's fleet tag, its free agent slots against `runtime.agents-in-flight`, any limit hold with its reset time, its
   hardware load read with the standard library (about 1 ms on Windows, never a PowerShell CIM call per item), its
   plan allowance with the reading's source and age, and its pool label: the name of the account, seat or workspace
   its acts draw on, never the credential. Membership is derived from live beats.
7. **Admission counts pools.** The admission queue charges a reservation against the pool's ledger, by
   compare-and-swap, before a launch, sized by an estimate per item kind that falls back to `runtime.act-ceiling`
   until `trace.cost` rows give a p90 (`runtime.admission-scope: pool`). On a node alone in its pool, the ledger is
   the in-flight ledger the admission queue already plans.
8. **A node finds and picks its own work.** One read gives the claimable ready set across builds: ready, unleased
   units whose dependencies are confirmed, and released or expired leases. A pure, replaceable pick function chooses
   what this node claims next, by plan priority and then the oldest released, from a spread start (dispatch 149, P6).
9. **Work can be offered, never assigned.** Lease acquisition takes an optional offer naming the node it was made for
   and its deadline, `leases.offer-seconds`; past the deadline anyone may claim the unit, so an offer is a wait with a
   deadline, as P39 requires. An offer source registers at a core point, and the built-in source is the node's own
   pick. An offer is evidence; only the acquisition is the witness, and compare-and-swap with the epoch refuses a
   stale one.
10. **A request can travel beyond its node.** A request that is not yet a build is written as a project-level record
    any node may claim by lease, and a mailbox recipient may name a node or the project. The owner's words are written
    verbatim where the owner types them, and a head relays only the record's id (the owner's FR-1). A relayed request
    is data with provenance, never consent, and only the owner's own session confirms a breakpoint.
11. **Coordination has transport points.** Runtime's `[extend]` gains a lease-store point, git refs its only adapter,
    with a conformance fixture holding the probes above, and a doorbell point, `deps.messaging` taking registered
    names. Each host declares whether it can write custom refs and which auth class it needs; a host that cannot
    write refs uses a branch-namespaced fallback or acquires nothing. Every adapter row declares its tenancy, its
    retention and its region.
12. **Harness and credential resolve per role.** `runtime.act-harness` and `runtime.act-auth` resolve per role
    through Roles' resolver, as effort and model do, so a judge role or a head can run on another subscription or key
    without drawing on the workers' plan; `api-key` stays last and only the owner adds it. A harness row records how
    its adapter reads the credential, and the act launch is pinned out of bare mode.
13. **New publishing boundaries are scanned.** The secret scan covers lease, mail, beat and mirror payloads and every
    adapter's publishing boundary, and the record door refuses a token shape in a coordination record.
14. **Every lease holder has a budget.** A cadence run, Maintain's, the Loop Review's or a registered program's, draws
    on a rework budget of its own, keyed to its period lease, and ends as `flow.on-exhausted` says.
15. **Cadence lease kinds are names, never a list,** so a cadence item an expansion registers, a head's cycle among
    them, can hold a lease.
16. **"Fleet" means nodes.** The register of adopters becomes the adopter register, leaving the word to the fleet
    tag, `fleet.toml` and the new expansion.
17. **What no head may do:** write a lease, a position or a verdict on a node's behalf, or hold a standing model
    context. Runtime's no-model-context and pure-position invariants stand unchanged.

The keys the fold would add, each with its preset row:
- `leases.queued-claim-days`, in days, default 7, dPlacedRequest;
- `leases.offer-seconds`, in seconds, default 300, dPlacedRequest;
- `runtime.admission-scope`: session, node or pool, default pool, dWellOiledMachine;
- `roles.harness.<role>` and `roles.auth.<role>`, each defaulting to the runtime key it overrides, dWellOiledMachine.

`deps.messaging` takes registered doorbell names beside its three values; it stays dKeptSession's, and
dWellOiledMachine arms it with the doorbell point.

## [layers] Which layer owns what

| Layer | Build | What it owns |
|---|---|---|
| flow (core) | dPlacedRequest | the fenced effect push, tombstoned leases and monotonic epochs, the declared expiry clock, offers with a deadline, cadence lease kinds as names, project-level requests |
| flow (core) | dKeptSession | causal, keyed messages, and recipients that name a node or the project |
| runtime (core) | dWellOiledMachine | the node beat, admission by pool, discovery and the pick, the lease-store, doorbell and offer points, host capabilities and adapter tenancy, harness and credential per role, the scanned boundaries and the record door, a budget for every cadence run, and the fenced push in the commit queue and the lander |
| distribution (expansion) | dShippedRelease | the adopter register, renamed |
| observability (expansion) | dCalibratedLens | the beats and the pools' ledgers trended, and the reservation estimate re-derived |
| integrations (expansion) | planned | endpoint and cloud-host adapters at the core points |
| `fleet` (new expansion) | planned | the head, its judge role, the dispatch record and the request relay |

## [planned] The fleet itself, planned and not scheduled

Proposed for v2 `[planned]`, counting in no build's planned units:
- **The fleet: node units coordinating in real time.** Trigger: the owner's word that work must be scheduled across
  nodes as it happens. Layer: `fleet`, an expansion (P28, P40). Units:
  - the head, a model-free function from every node's beat, the pools' ledgers and the claimable ready set to offers,
    hosted as a lease-held cadence item that any node may run;
  - the judge role it calls for a record no rule types, registered by the expansion, choosing within a closed set of
    routes the program computed;
  - endpoint adapters at the lease-store, doorbell and memory-mirror points, each passing the core's conformance
    fixture and declaring its tenancy;
  - cloud-host adapters, each declaring its auth class and whether it writes refs;
  - a dispatch record of each offer's inputs, proposer and validation, replayed by re-running the program and
    re-validating the judge's choice;
  - the owner's request relayed by reference.

  Its test: a four-hour head outage costs no throughput, an offer reaches a node only through that node's own lease,
  and a replay reproduces the program's offers byte for byte.

## [chain] Where it lands

Each clause sits on the build that registers its kind, or on a descendant of every build whose schema it reads:
- **dPlacedRequest:**
  - the fenced effect push, seen red on a stale holder's push after a take-over;
  - leases never deleted, epochs monotonic, and queued claims past their age refused, seen red on a pruned lease
    and on a stale queued claim;
  - expiry judged by a declared clock;
  - cadence lease kinds as names;
  - a project-level request record any node claims by lease;
  - an offer with a deadline on lease acquisition, an expired offer a free claim.
- **dKeptSession:** messages carrying a session sequence number, a take-over's predecessor and the interface's content
  key, seen red on the reorder test; recipients that name a node or the project.
- **dWellOiledMachine:**
  - the node beat;
  - admission by pool through a reservation ledger;
  - discovery of released and expired leases, and the pure pick function;
  - the lease-store, doorbell and offer points, the lease store's conformance fixture, and `deps.messaging` armed;
  - host capabilities and adapter tenancy;
  - harness and credential per role, and the act launch pinned out of bare mode;
  - the scan of coordination payloads and adapter boundaries, and the record door;
  - a budget for every cadence run;
  - the commit queue and the lander pushing through the fenced push.

  Each is seen red on a planted case: two nodes sharing one pool, a hosted host refused a ref push, a token in a
  lease payload, a cadence run that never converges.
- **dShippedRelease:** the adopter register, renamed.
- **dCalibratedLens:** the beats and the pools' ledgers trended, and the reservation estimate re-derived from
  `trace.cost`.

## [gaps] Gaps this adds to the register

| Key | Stage | Sev | Gap | Owner |
|---|---|---|---|---|
| `gap-conc-12` | Spine | HIGH | Fencing is check-then-act: the commit queue and the lander re-read a lease's epoch and then push, so a holder replaced between the read and the push still lands its write; one atomic push carrying the lease beat was refused at the remote instead. | dPlacedRequest |
| `gap-conc-13` | Spine | HIGH | A released lease that is pruned restarts its epoch: a claim queued offline then wins a unit another node has already landed, at epoch 1. | dPlacedRequest |
| `gap-conc-14` | Spine | LOW | A lease's expiry is judged by the reader's clock against the holder's own stamp, so clock skew moves every expiry. | dPlacedRequest |
| `gap-conc-15` | Spine | MED | Messages carry no order across one build's session refs: a take-over's `changed` relayed ahead of its predecessor's `confirmed` leaves a dependent on the older interface. | dKeptSession |
| `gap-conc-16` | Spine | MED | No node can find work it does not hold: nothing reads released or expired leases across builds, a node "with quota takes the build over" with no way to find it, and today's resume tick skips every lease another node hosts. | dWellOiledMachine |
| `gap-conc-17` | Spine | MED | An owner's request reaches only the node it was typed on: intake is bound to the owner's session, mailbox recipients are a build or its units, and no request record exists that another node can claim. | dPlacedRequest |
| `gap-conc-18` | Spine | LOW | The cadence lease grammar lists its kinds literally, `maintain` and `review`, against Runtime's rule that a registered name never meets a literal list, so a cadence item an expansion registers cannot hold a lease. | dPlacedRequest |
| `gap-conc-19` | Spine | MED | Nothing outside a node can offer it work: no lease takes an offer with a deadline and no point registers an offer source, so any head would have to assign, which lost 29% of makespan in a simulated head outage. | dPlacedRequest |
| `gap-rt-40` | Runtime | HIGH | No node publishes its presence, capacity or plan: admission counts one session's agents, a plan limit is per account and shared by every node signed into it, and a limit is seen only after it is hit; on a shared, tight plan, node-local admission finished 48 to 54% of the work where a ledger keyed by plan finished all of it. | dWellOiledMachine |
| `gap-rt-41` | Runtime | MED | Coordination has no transport point: leases and mail are written to `refs/gov/*` directly, which Anthropic's hosted cloud sessions and routines cannot push, and no host declares whether it can. | dWellOiledMachine |
| `gap-rt-42` | Runtime | MED | The harness and its credential are set once for the repository, so a head or a judge role cannot run on another subscription or key without drawing on the workers' plan. | dWellOiledMachine |
| `gap-rt-43` | Runtime | MED | Headless acts lose the subscription login once `--bare` becomes `-p`'s default, since bare mode reads neither the OAuth login nor the setup token, and no harness row records how an adapter reads its credential. | dWellOiledMachine |
| `gap-rt-44` | Runtime | MED | New publishing boundaries go unscanned: lease, mail and mirror payloads sit outside the secret scan's population, and no door refuses a token shape in a coordination record. | dWellOiledMachine |
| `gap-rt-45` | Runtime | MED | P39's rework budget is keyed to builds and intake content only, so a cadence run's loop, Maintain's, the Loop Review's or any head's re-planning, has no bound. | dWellOiledMachine |
| `gap-deploy-29` | Deploy | LOW | "Fleet" names two things: the fleet register lists adopters while a fleet tag names a node. | dShippedRelease |

## [forks] For the owner, 2026-10-19

| Fork | Question | Options, the recommendation first |
|---|---|---|
| CL-1 | Which layer should cloud coordination, scheduling and load balancing belong to? | a new expansion, `fleet`, attaching only at core points, with the adopters' register renamed so the word means nodes; integrations, as adapters plus a head adapter; the core, as a fleet scheduler inside Runtime |
| CL-2 | What shape should coordination across node units take? | headless as the floor, plus a model-free head that only offers and calls an LLM judge role only for a record no rule types; headless only, never a head; an agent-driven head that plans and dispatches as a governed role, on its own subscription or key |
| CL-3 | How should the head break work down? | it offers whole ready units across builds, and Design's unit roster stays the cut; it also cuts each build's units into streams by their declared order and files; an LLM planner role re-cuts builds for it |
| CL-4 | How should an owner's prompt reach another node unit? | written verbatim where the owner types it, as a request record a head offers by reference and a unit claims by lease; the head forwards the prompt's text to the unit it picks; only on the node where it was typed, as today |

## [answers] The owner's answers, 2026-10-19

Put to the owner in one batch, each question with its recommendation first. The owner's words, verbatim:

| Fork | The owner's answer |
|---|---|
| CL-1 | "New fleet expansion (Recommended)" |
| CL-2 | "Headless + offering head (Recommended)" |
| CL-3 | "Whole units, across builds by default, but also a new headless-first 'planner' role by default, with a planning workflow at medium effort, opt-in by default to assist for complex builds (like this one, for example)." |
| CL-4 | "By reference, claimed (Recommended)" |

Three took the recommendation as offered. CL-3 kept it as the default and added a planner: a planning workflow at
medium effort, opt-in by default, to assist complex builds. The design already binds a planner in the Plan stage, so
the fold reads CL-3 as giving that planner a Design item of its own, `design.streams`, and reads "headless-first" as
needing no head. v2 `[open]` holds that reading for the owner to confirm.

## [folded] Where the answers went, 2026-10-19

- **v2:** P40 joins the principles, and `[layers]` names `fleet` as the one planned expansion. Six keys join the
  catalogue: `leases.queued-claim-days`, `leases.offer-seconds`, `runtime.admission-scope` and `design.streams` in
  every preset, and `roles.harness.<role>` and `roles.auth.<role>` beside the never-touch keys they override.
  `leases.expiry-hours`, `deps.messaging`, `runtime.act-harness` and `runtime.act-auth` say their part. Six chain rows
  gain the seams: dPlacedRequest, dKeptSession, dIndexedDesign, dWellOiledMachine, dShippedRelease and dCalibratedLens.
  `[planned]` holds the fleet itself, and `[open]` the reading of CL-3.
- **flow-steps and layer-roles:** the planner's `design.streams` item, after `design.overlaps` and before
  `design.unit-spec`, run only where `design.streams` holds for the build.
- **layer-memory and coordination:** the two stale statements [owed] names are corrected.
- **The gap register:** the sixteen gaps, the fifteen in [gaps] and `gap-design-12` for CL-3's planner, each on its
  owning build's chain row.
- **The chain:** the critical path grows from 253 units at `ace51f4a7` to 262, its nine new units eight on
  dWellOiledMachine and one on dCalibratedLens.

## [owed] Owed

- **The review debt grows.** This record and its fold join the commits the parked closing-review pair must cover.
- **Two records disagreed with v2,** and the fold corrected them: the coordination record's `[design]` title says
  dDeclaredLoop builds the feature, where v2 gives the leases to dPlacedRequest and the mailbox to dKeptSession; and
  layer-memory lists the lease and the mailbox message among Runtime's kinds, where P5 makes them flow's (dispatch 148).
- **Probes the researchers could not run,** owed to the builds that carry the seams: whether GitHub accepts
  `git push --atomic` (dPlacedRequest); whether a hosted cloud session's push of a `refs/gov` ref is refused, and
  whether the status line runs under `-p` (dWellOiledMachine); the message reorder test (dKeptSession); a lease service
  fenced against git (the fleet's own build).
- **The terms, an owner action.** Whether an owner's own unattended fleet on one subscription is the ordinary,
  individual use the plan limits assume is Anthropic's to answer, and its legal page sends such questions to sales.
  Until the owner records an answer, `runtime.act-auth` keeps its default, and `api-key` stays the owner's to add.
