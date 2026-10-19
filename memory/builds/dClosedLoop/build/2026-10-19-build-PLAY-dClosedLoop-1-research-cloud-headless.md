# Research: Cloud coordination: the headless shape

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 149's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-24-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-cloud-and-scale.md`.

---

I recommend the headless shape for multi-node coordination, and the design is already mostly headless. Git refs on the shared remote stay the store of record and the fence, and any cloud endpoint is added later as an optional adapter. Four of the eight families below lose to a test in gov's setting. The gaps are in fencing, lease lifecycle, message ordering and capacity, and each becomes a seam to carry now.

Scope: design records at `7e0322a5c`, all read 2026-10-19; outside sources read 2026-10-19. I modified nothing in the tree. All probes ran against local bare repos (`file://`) in `.../scratchpad/d149/`, which I deleted afterwards. Docker was not running, so I could not run any endpoint service (etcd, Consul, Postgres, NATS). Their losing tests below are tests a build must run, predicted from each system's own documentation.

## What the design and code hold today

- **Leases and mailbox.** Coordination `[design]` units 1–8 define CAS lease refs with an epoch and per-session append-only mail refs. The epoch is bumped at every take-over (layer-runtime `[supervise]` lines 406–425).
- **The fencing check is check-then-act.** Layer-runtime lines 411 and 419–420 say the commit queue and the lander "re-read the epoch from the remote before they commit or push". Probe P2(a) shows a stale write landing through exactly that gap.
- **Today's run claim.** It is a parentless commit written by `git push --porcelain --force-with-lease=<ref>:<sha>` (`tools/unattended/unattended.sh:2077-2080`, `:2419-2423`). Its node is the user name (`:2410`).
- **Today's liveness check reads two clocks.** A claim's age is the reader's `date` minus the holder's own `beat-utc` stamp (`unattended.sh:2152`, `:2165`, `:2174-2185`).
- **Change feed and mirror.** The change feed is node-local and "ordered per ref". The mirror is "never read by a verdict" (memory-plan `[pockets]` rows at lines 95–96).
- **Terminal leases get pruned.** The supervisor "expires leases … and prunes terminal run claims" (layer-runtime:454). The flow-items research proposes deleting lease refs at release (research-flow-items-b:63). Probe P3 case 3 shows this lets a queued offline claim win a finished unit.
- **No capacity is published.** `runtime.agents-in-flight` counts agents in one session (v2 `[policies]` :1022). No node publishes capacity. The nearest headless behaviour: once a limit hold passes `runtime.hold-ceiling`, the build lease is released "so a node with quota takes the build over" (layer-runtime:402–404).
- **"Fleet register" is not node membership.** It is distribution's register of adopters, grown from `adopters.toml` (layer-expansions:116, :436–437). It carries no liveness. Node identity is `tools/playbook/fleet.toml` and its `--claim-node` verb (`render_playbook.py:1731`).

## Candidates, one per mechanism family

### 1. Git refs on the shared remote as the medium (the existing seam, extended): **recommended**
- **Mechanism:** create-only and compare-and-swap ref writes for leases; one append-only ref per session for mail; `next` derives the ready set from witnesses (P22); epochs fence.
- **Guarantee:** exclusive claims per ref, and all-or-nothing writes across several refs with `git push --atomic`. ["Either all refs are updated, or on error, no refs are updated. If the server does not support atomic pushes the push will fail"](https://git-scm.com/docs/git-push). Order holds within one ref only. Runs fully offline (P3).
- **Failure modes:** check-then-act fencing; deleting a ref resets it; a herd of nodes picking the same unit; the reader's clock judging the holder's stamp.
- **Probes run:**

| Probe | Result |
|---|---|
| P1: 8 nodes race to create one unit lease, 10 rounds | `rounds with winners!=1: 0 of 10`. Exclusive. |
| P2(a): holder A re-reads its lease, B takes over, A pushes its branch normally (the design as worded) | `remote build-b tip: A stale work 2`. **The stale write lands.** |
| P2(b): A pushes its branch together with a lease beat commit in one `--atomic` push, expecting the lease tip it saw | `[rejected] (stale info)` / `[rejected] (atomic push failed)`; branch unchanged. **Fenced at the remote.** |
| P2(c′): same, re-pushing the lease ref unchanged | `[up to date]`; `lease ref in the packet commands sent: 0`. An unchanged lease ref is never checked by the server, so the fence must be a new beat commit. |
| P3: node A offline queues a claim; B claims (case 1) or releases with a terminal commit (case 2) | both `[rejected] (stale info)`. A yields. |
| P3 case 3: B's released ref is pruned, then A reconnects | `[new reference]`, `remote now: holder A epoch 1 (queued offline)`. **ABA:** A now holds a lease on a unit B already landed, and its epoch has restarted at 1. |
| P5: endpoint down after the main push, with release and `landed` as separate pushes | main says "land b", lease still "live", no mail. Separate pushes leave orphans. |
| P5: one `--atomic` push of main + lease release + `landed` mail | down: nothing written; up: all three written. Down was simulated before the push, not mid-transfer. |
| P6: 8 nodes, 8 ready units, lowest-free-unit-first claiming | `total push attempts: 36` (= 8+7+…+1), all 3 runs. |
| P6: same, random starting unit | `12` attempts, all 3 runs; 8 distinct holders every time. The identical counts suggest bash's `RANDOM` seeding repeats in subshells, so treat 12 as one sample. |

- **Fit:** this is the headless shape. It needs seams S1–S4 and S7 below. Whether GitHub accepts `--atomic` today is unconfirmed: the only evidence is the [2015 Git 2.4 blog post](https://github.blog/2015-04-30-git-2-4-atomic-pushes-push-to-deploy-and-more/) and a [2019 git-list report](https://public-inbox.org/git/xmqq1s2b7b64.fsf@gitster-ct.c.googlers.com/T/). This belongs to the platform researcher.

### 2. Lease and lock services with fencing (etcd, Consul, ZooKeeper, Chubby): rejected as the store of record; allowed later as a lease-store adapter only if it fences the git write
- **Mechanism:** the server holds a TTL lease plus a monotonic token. etcd says ["fencing token is revision number"](https://etcd.io/docs/v3.5/learning/why/). Consul's sequencer is "(Key, LockIndex, Session)", and it adds a lock-delay of 0–60 s, default 15 s, which it calls "not a bulletproof method" ([Consul sessions](https://developer.hashicorp.com/consul/docs/automate/session)). ZooKeeper locks use ephemeral sequential znodes, with each waiter watching only its predecessor to avoid the herd ([ZooKeeper recipes](https://zookeeper.apache.org/doc/current/recipes.html)).
- **Guarantee:** exclusivity for the service's own keys, with TTL measured by the server.
- **Failure modes:**
  - etcd: ["The lock feature of etcd itself cannot be used for protecting external resources"](https://etcd.io/docs/v3.5/learning/why/). The store being written must check the token itself ([Kleppmann, fencing tokens](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html)).
  - Consul gossip can produce a false failure and release a lock whose owner is still alive.
  - A node offline for a day cannot acquire or renew at all.
- **Losing test (not run):** take the lease in the service and push the effect to git, with a take-over between the two. Same shape as P2(a), so a stale holder lands unless the git push carries S1's fence. A second test: `leases.offline: warn` queues a claim and pushes it on reconnection, and the service-held lease would have to merge with it. This fails unless the service is only a mirror of the git ref.
- **Fit:** a transport swap behind a lease-store adapter, and only if that adapter passes S1's fence fixture. Its one gain over git is a server-side clock for expiry (S4). Chubby's published sequencers and lock-delay are cited through etcd's page. I could not extract text from the [Chubby PDF](https://storage.googleapis.com/gweb-research2023-media/pubtools/4444.pdf), so that citation is second-hand.

### 3. SQL row claims (Postgres advisory locks, `FOR UPDATE SKIP LOCKED`): rejected
- **Mechanism:**
  - Session-level advisory locks are held "until explicitly released or the session ends" ([Postgres explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html)).
  - `SKIP LOCKED` "provides an inconsistent view … can be used to avoid lock contention with multiple consumers accessing a queue-like table" ([Postgres SELECT](https://www.postgresql.org/docs/current/sql-select.html)).
- **Guarantee:** exclusive only while a connection or transaction stays open.
- **Failure mode:** a dropped connection releases the lock while the agent keeps working, so there are two holders. Postgres's docs do not state the dropped-connection case directly; it is implied by "session ends".
- **Losing test (not run):** a laptop node holds a unit for the 24 h `leases.expiry-hours`, and its Wi-Fi drops once. Any lease measured in hours loses, and an offline node can neither read nor claim.
- **Fit:** the durable alternative is a status-plus-epoch row with compare-and-swap, which is family 1's contract on another store.

### 4. Pull-based job queues (Temporal, Celery, Sidekiq, Buildkite, GitHub Actions runners): rejected as headless; its pattern is adopted
- **Mechanism:** workers poll outbound and claim jobs.
  - Temporal workers poll "only when it has spare capacity", with no inbound ports ([Temporal task queues](https://docs.temporal.io/task-queue)).
  - Buildkite agents poll over HTTPS, with no port forwarding; an agent is marked lost after 3 minutes without heartbeats ([Buildkite agent](https://buildkite.com/docs/agent/v3), [lifecycle](https://buildkite.com/docs/agent/v3/lifecycle)).
  - GitHub Actions re-queues a job its runner has not picked up within 60 s and fails it after 24 h queued ([self-hosted runners](https://docs.github.com/en/actions/reference/runners/self-hosted-runners)).
- **Guarantee:** at-least-once delivery.
  - Temporal rejects a late completion or heartbeat with NOT_FOUND, which acts as a task-token fence ([Temporal request failures](https://docs.temporal.io/troubleshooting/request-failures); [community thread](https://community.temporal.io/t/activity-timeout-and-temporal-server-connectivity-issue/8869)). The [Temporal timeouts page](https://docs.temporal.io/encyclopedia/detecting-activity-failures) itself does not say this, so it is ambiguous.
  - Sidekiq's basic fetch loses a job forever if the process crashes mid-job ([Sidekiq reliability](https://github.com/sidekiq/sidekiq/wiki/Reliability)).
  - Celery's `acks_late` is safe only "if your task is idempotent" ([Celery FAQ](https://docs.celeryq.dev/en/stable/faq.html)).
- **Losing test (reasoned, not run):** someone must enqueue the job, so the queue implies a producer. With no head, the only producer is the ready set derived from witnesses. That turns the queue back into family 1, whose herd cost is P6's 36 attempts versus 12.
- **Fit:** adopt the pattern, not the service: outbound-only polling, a node claiming only while it has headroom (S7), and idempotent or reconciling items. The design's `once-per-instance` invariant already requires the last (layer-runtime `[invariants]` :897). Who enqueues is the agentless-head question.

### 5. Replicated logs and change feeds (Kafka, NATS JetStream, Postgres logical replication): rejected as the store; a transport swap for the doorbell and the mirror
- **Guarantee:**
  - Kafka's transactional producers fence "zombies" by an epoch bumped per `transactional.id` ([Confluent on Kafka transactions](https://www.confluent.io/blog/transactions-apache-kafka/); I did not reach Apache's own design page, the fetch returned a redirect stub). Order holds per partition; that is general knowledge, not confirmed in a source this pass.
  - NATS dedupes on `Nats-Msg-Id` within a window of 2 minutes by default. That is "exactly-once publish" only, and end-to-end needs idempotent consumers ([Synadia](https://www.synadia.com/blog/jetstream-reliable-delivery-dlq-replay), [NATS model](https://docs.nats.io/jetstream/model_deep_dive)). AckWait and MaxDeliver details come from secondary sources.
  - Postgres logical replication stops on a unique-key conflict until fixed by hand, and on an origin conflict the incoming change "is always applied" ([Postgres replication conflicts](https://www.postgresql.org/docs/current/logical-replication-conflicts.html)).
- **Failure modes:** no order across partitions or subjects; replay beyond the dedupe window; a second writer silently winning.
- **Losing test (not run; the build must run it):** a memory relayed out of order. A parent's session s1 posts `confirmed` with interface v1; after a take-over, session s2 posts a breaking `changed` with v2; the relay delivers `changed` first. A dependent that applies messages in arrival order ends on v1. The design gives no rule for ordering across two session refs (coordination `[design]` 6–8).
- **Fit:** a transport swap behind the existing notification and memory-mirror points (layer-runtime `[extend]` :843, :846), provided S5 and S6 hold. It is never a verdict input.

### 6. CRDT sync (Automerge, ElectricSQL): rejected for decisions and claims
- **Guarantee:**
  - Automerge converges every replica to the same winner, chosen by internal operation id and not wall clock; losers are kept in `getConflicts` ([Automerge conflicts](https://automerge.org/docs/reference/documents/conflicts/)).
  - ElectricSQL syncs reads out of Postgres only; it "doesn't provide (or prescribe) a built-in solution for getting data back into Postgres" ([Electric writes](https://electric.ax/docs/guides/writes)).
- **Losing test (already run by the night pass two, 2026-10-19, point 4):** two sessions decide one question differently. An append-only chain kept both; a create-only ref keyed by a derived key refused the second. A CRDT converges on one winner without refusing either, which is the outcome P23 and NT-18 forbid.
- **Fit:** presence and notice data only.

### 7. Gossip membership (SWIM, Serf): rejected
- **Guarantee:** eventual membership with a suspicion phase. It runs peer to peer over UDP plus periodic TCP full syncs, and false positives are possible ([Serf gossip internals](https://github.com/hashicorp/serf/blob/master/docs/internals/gossip.html.markdown)).
- **Losing test (reasoned):** gov's nodes are workstations that sleep and sit behind NAT. Membership needs peers to reach each other directly, and membership confers no exclusivity.
- **Fit:** derive liveness from lease beats on the shared medium instead (S7).

### 8. Coding-agent fleets that claim tasks: confirms family 1, nothing to adopt
- Claude Code agent teams: "Task claiming uses file locking"; the task list lives under `~/.claude/tasks/{team-name}/`; "One team per session"; "Lead is fixed". It is a single machine, with no fencing or offline story documented ([agent teams](https://code.claude.com/docs/en/agent-teams)).
- beads: a git-backed JSONL issue tracker, which moved to hash IDs because sequential IDs collided across agents and branches. Its claim semantics are unverified; the sources are third-party ([pkg.go.dev](https://pkg.go.dev/github.com/steveyegge/beads@v0.49.1), [B4mad guide](https://brenner-axiom.codeberg.page/beads-technical-guide/)).

## Fit, in the three classes the question asks for

- **Transport swap behind an adapter:** the doorbell (`deps.messaging`, notification adapters); the memory mirror (`memory.mirror`, exists); the notice read (`mailbox.notice`, `mailbox.fetch-seconds`); and a lease store, once S3 exists.
- **Needs a new contract:** S1 fence-in-the-effect; S2 lease tombstones and monotonic epochs; S3 the lease-store point and its conformance fixture; S4 whose clock judges expiry; S5 message causality and keyed interfaces; S6 replay-safe event keys; S7 a capacity and liveness beat.
- **Must stay true offline (P3):** every verdict is computed locally; git remains the only store an effect is fenced against; an endpoint outage costs only latency.

## Seams to carry now

| Seam | Owning layer | What it is | Cost while gov stays offline |
|---|---|---|---|
| **S1 Fence in the effect** | flow (lease grammar, dPlacedRequest); runtime (commit queue, lander) | Every effect push (pass push, the lander's main push, release with `landed`) carries the holder's lease beat commit in one `--atomic` push with `--force-with-lease=<lease>:<tip seen>`. This replaces the re-read-then-push in layer-runtime:411–420, which P2(a) beat. | None. The beat already rides each pass (`leases.renewal` progress), so this merges two pushes into one. P5 also gets all-or-nothing landings. |
| **S2 Leases are never deleted** | flow; memory (lifecycle in the memory contract) | Release writes a terminal tombstone commit, and the epoch is monotonic per (slug, unit) forever. Prune only past the queued-claim age limit, and refuse queued claims older than that limit. | One ref per unit, kept. It contradicts layer-runtime:454's pruning of terminal claims once run claims migrate onto leases, and research-flow-items-b:63's proposed delete. |
| **S3 A lease-store point** | runtime `[extend]` | Today's eleven points (:834–846) have none for leases. The point declares acquire, renew, release, take over and read, the epoch rule, and a conformance fixture containing P1, P2(b), P3 cases 1–3 and P5. Git refs are the only implementation. | An interface plus a fixture; nothing runs. |
| **S4 Expiry by a declared clock** | flow | "Expired" is judged by the store's TTL where the store has a clock. On git, it is the holder's stamp corrected by the recorded clock offset (layer-runtime:828), or the observer seeing the tip unchanged for `leases.expiry-hours`. Today the reader's clock judges the writer's stamp (`unattended.sh:2152-2185`). | A field. |
| **S5 Causal and keyed messages** | flow (mailbox schema in the loop kit) | Each message carries a per-session sequence number. A `takeover` names the predecessor's last message id. `confirmed` and `changed` carry the interface's content key. The dependent acts on the recomputed key (P23), never on arrival order. The build must run family 5's reorder test. | Three fields. |
| **S6 Content-derived event keys** | memory and runtime (change feed) | The feed's event key (memory-plan:95) is content-derived, so any relay is replay-safe beyond a dedupe window (NATS's default is 2 minutes). | None. |
| **S7 A capacity and liveness beat** | runtime (supervisor beat), written through flow's lease record | Each beat records agents in flight versus the cap, any limit hold with its reset time, and the node tag. A headless node self-claims only with headroom and no hold, starting from a spread unit (P6: 36 → 12 attempts). Membership is derived from live beats, not gossip. | A few fields per beat; no extra push. |
| **S8 A claimable ready set** | flow (`next`) | One cross-build read of ready, unleased units whose dependencies are confirmed. In the headless shape this is the queue. An owner request becomes an `intake` message (NT-21) claimed by whichever node takes the lease. | Read-only. |

## Recommendation and limits

The headless shape answers "claim your own work, relay memories and decisions" with no new store: family 1 plus S1–S8. A cloud endpoint is then an optional set of adapters at the doorbell, mirror and lease-store points, never what a verdict reads.

What headless cannot do is place work across nodes by measured hardware load and plan-limit utilisation as a global optimum. It only does local self-selection with headroom. That belongs to the agentless-head researcher, and S7's beat is the input any head would read.

GitHub's acceptance of `--atomic` and its fetch and push rate limits belong to the platform researcher.

The design files I drew on, all in `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/`:
- `2026-10-14-build-PLAY-dClosedLoop-1-coordination.md`
- `2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
- `2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`
- `2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md`
- `2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`

Code cited:
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/unattended/unattended.sh`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/playbook/fleet.toml`
