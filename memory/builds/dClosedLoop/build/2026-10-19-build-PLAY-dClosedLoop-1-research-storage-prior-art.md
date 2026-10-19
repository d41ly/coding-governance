# Research: storage and coordination, prior art outside gov

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 131's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-12-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`.

---

## Point 3, outside prior art: storage and coordination for a typed record graph shared by several nodes

**Short answer:** keep plain files in git, with one derived SQLite index per tree as the relational engine. Move coordination onto per-sender git refs. Add an optional ids-only "doorbell" for real-time, and offer MCP as an optional read surface. A database (Dolt, cloud Postgres, synced SQLite) or a bus (NATS) belongs only behind an optional slot.

I wrote nothing in the repository. Every probe ran on a copy under the session scratchpad, which I deleted afterwards (`removed`). One untracked file, `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-research-scenarios-design.md`, appeared while I worked. It is not mine. Every source below was read on 2026-10-19.

### What gov already has (read from the code)

- **A derived SQLite index.** memory-recall builds two FTS5 indexes from the markdown tree, standard library only, offline (`tools/memory-recall/README.md:5-7`). It uses `import sqlite3` (`tools/memory-recall/query.py:77`), opens read-only (`query.py:785`), and keeps its cache under the common git dir (`query.py:21`).
- **A compare-and-swap ref record.** `CLAIM_NS="refs/gov/runs"` (`tools/unattended/unattended.sh:2087`) is pushed with `--force-with-lease` (`unattended.sh:2423`). `git ls-remote` against origin returned 17 `refs/gov/runs` refs.
- **The design.** It already fixes: one graph with typed edges whose inverses are derived, and doors as the only writers (`memory-plan [frame]`, `[doors]`); refs that move by compare-and-swap, and a mailbox at `refs/gov/mail/<slug>` (`memory-plan [families]`, `coordination [design]` item 6); live delivery written to the mailbox first (`coordination [design]` item 7); and P2, P3, P33 and P35 (`architecture-v2 [principles]`).

### Probes run (measured on this node: Windows, git 2.54.0, Python 3.14.5, SQLite 3.50.4 with `ENABLE_FTS5`)

| # | Probe | Output |
|---|---|---|
| A | SQLite edge index over the real `memory/` (Serves, Evidences, Caused-by, Supersedes, Amends lines), corpus repeated 1×, 10×, 50× | `files=4257 edges=6218 … build=0.256s inverse-query=1.0ms db=2.1MB`; `files=42570 … build=2.686s inverse-query=5.0ms db=21.1MB`; `files=212850 edges=310900 … build=14.958s inverse-query=24.2ms db=106.8MB` |
| A' | Incremental input: memory files changed over the last 1, 20, 200 commits | 3, 83, 296 files (296 is 7% of 4,257) |
| A'' | The same inverse answered by grep | `grep -rl … 'Serves:.*PLAY-dClosedLoop-1'`: 263 files, 23,625 bytes, 304 ms. The index answers 258 in 1 ms. The two differ because my extractor keeps only ID-shaped targets, which is why an index needs an agree-with-grep check. |
| B | Two nodes each append 20 messages to one mailbox ref (`refs/gov/mail/x`) by compare-and-swap, against a local bare remote | `node a appended=20 cas-retries=6`, `node b appended=20 cas-retries=20`, chain length 40, about 14.6 s. A rerun gave 8/20 retries, still no message lost. |
| B' | The same, with one ref per sender (`refs/gov/mail/x/<node>`) | `cas-retries=0` on both nodes, 20 and 20 commits, 6.48 s. |
| B'' | Network floor | `git ls-remote origin 'refs/gov/runs/*'` took 0.604 s. I did not measure a real push, because pushing would modify the shared remote. |
| C | A SQLite file committed to git, changed on two branches, then merged | `m.db \| Bin 8192 -> 8192 bytes`, then `CONFLICT (content): Merge conflict in m.db` |
| C' | An append-only JSONL file with `merge=union` | Both appended lines kept, no conflict |
| C'' | Two nodes write git notes on one commit, merged with `-s cat_sort_uniq` | Both lines kept: `n1: verdict green` / `n2: verdict red` |
| D | Two nodes each add a record with `**Supersedes:** DEC-x-1` on separate branches | `git: both merged clean`. The index query finds `[('DEC-x-1', 'd2.md,d3.md')]`. |
| E | Reading witnesses from history | Trailers over all 6,318 log lines: 179 ms. `git for-each-ref refs/gov`: 34 ms. |

Probe D shows that git merges the semantic conflict silently and only the derived index catches it. The gate list in `memory-plan [gates]` checks edges per source ("a second edge line of one type") but has no check per target, such as one `supersedes` per target. This is my observation only; whether two supersessions are illegal is the design's call.

---

## The families

### F1. Plain files in git, plus a derived index
**Mechanism:** the canonical records are text files in the tree. A rebuildable index (SQLite or similar) is derived from them, and git history is the audit log.

**Real systems:**
- Fossil keeps derived metadata that "can be recomputed from the canonical artifacts" with `fossil rebuild`; only the artifacts sync ([fossil tech overview](https://fossil-scm.org/home/doc/trunk/www/tech_overview.wiki)).
- Letta MemFS stores agent memory as markdown files in a git repo, found with ordinary file tools, with no default vector index ([docs.letta.com/letta-code/memfs](https://docs.letta.com/letta-code/memfs)). That summary came from a search result; the concepts page I fetched only says memory is "git-tracked" ([docs.letta.com/concepts/memgpt](https://docs.letta.com/concepts/memgpt)).
- beads_rust (`br`) keeps "SQLite plus JSONL as the operating contract" ([gascity.com/guide/beads-vs-br](https://gascity.com/guide/beads-vs-br/)).
- MCP Agent Mail is "backed by Git (for human-auditable artifacts) and SQLite (for indexing and queries)" ([github.com/Dicklesworthstone/mcp_agent_mail](https://github.com/Dicklesworthstone/mcp_agent_mail)).

**Point 2:**
- *Consistency:* not kept by git. The index plus a gate detects broken relations after merge (probe D).
- *Offline:* full.
- *Latency:* push/fetch, seconds at best, no push notification.
- *Conflicts:* text merge. Separate files avoid conflicts but hide semantic ones (probe D).
- *Agent-friendliness:* best of all families. cat, grep and git suffice, the agent reads only the rows it needs, and the index cuts inverse lookups from 304 ms and 23 KB of paths to 1 ms (A'').
- *Audit:* line diffs in every PR.
- *Service and credentials:* the git remote only.
- *Cost:* none.

**Point 3:**
- *Two nodes deciding at once:* both merge. The conflict is caught only by an index gate (D).
- *A node offline for a day:* fine.
- *A large adopter's history:* the index is built from the tree, not history, and scales linearly (15 s at 213k files). The 7% incremental input in A' implies roughly 1 s per 20k changed files, extrapolated, not measured. Witnesses read from history grow with commits (E).
- *An agent verifying a fact without a service:* yes.
- *An adopter with no database:* fine.

**Known failure:** beads' SQLite+JSONL era. Its changelog, as summarised by the company behind Beads (biased), records "stale-database overwrites, deleted-issue resurrection … split-brain", from "two representations that had to stay aligned" ([gascity.com/guide/beads-vs-br](https://gascity.com/guide/beads-vs-br/)). The difference that matters: beads let the database be written too. Under gov's door rule the index is never written, only rebuilt.

### F2. Git-backed databases (versioned SQL or graph)
**Mechanism:** a database engine whose storage is a Merkle DAG with branch, merge, push and pull, and merges cell by cell.

**Real systems:**
- Dolt:
  - Conflicts land in `dolt_conflicts_<table>`, and foreign-key violations block the commit ([dolthub.com/docs/concepts/dolt/git/conflicts](https://www.dolthub.com/docs/concepts/dolt/git/conflicts)).
  - Since v1.81.10 it uses git remotes, storing data under `refs/dolt/data`; Bitbucket is unsupported ([announcement](https://dolthub.com/blog/2026-02-13-announcing-git-remote-support-in-dolt), [follow-up](https://www.dolthub.com/blog/2026-02-19-supporting-git-remotes-as-dolt-remotes)).
- Beads on Dolt: embedded mode "is single-writer (enforced via file lock)", and concurrent writers need a `dolt sql-server` ([beads.gascity.com/architecture/dolt](https://beads.gascity.com/architecture/dolt)). A "beads classic" restore exists because the server "added friction for solo Beads users" ([dolthub blog 2026-04-02](https://www.dolthub.com/blog/2026-04-02-restoring-beads-classic/), a vendor source).
- TerminusDB, "a knowledge graph database with built-in version control" with push and pull, server-shaped ([terminusdb.com/docs](https://terminusdb.com/docs/)).
- Fossil, the whole repository as one SQLite file ([fossil tech overview](https://fossil-scm.org/home/doc/trunk/www/tech_overview.wiki)).

**Point 2:**
- *Consistency:* the strongest of any family. Schema, foreign-key checks at merge, and cell-level merge.
- *Offline:* full with an embedded engine.
- *Latency:* push/pull, the same as git.
- *Conflicts:* rows and cells.
- *Agent-friendliness:* needs the `dolt` binary and SQL; plain git tools cannot read `refs/dolt/data`.
- *Audit:* invisible in a code-review diff, since the data is not in the tree.
- *Service:* a binary on every node, and a server for more than one writer.
- *Cost:* open source.

**Point 3:**
- *Two nodes deciding at once:* the best result. A cell conflict or constraint violation surfaces at merge.
- *A node offline for a day:* fine.
- *A large history:* fine.
- *An agent verifying a fact without a service:* only with the binary installed.
- *An adopter with no database:* loses, because it requires a new binary and two stores (code in git, records in Dolt). The same mistake as committing a binary database (probe C) appears if records are mirrored into the tree.

### F3. Embedded databases kept in sync
**Mechanism:** a local SQLite per node, replicated to other nodes.

**Real systems:**
- Litestream: asynchronous WAL shipping, "each database replicates to a single replica destination", and its VFS read replicas are read-only ([litestream.io/how-it-works](https://litestream.io/how-it-works/)).
- LiteFS: one primary chosen by a Consul lease, writes go to the primary ([docs.fly.io/litefs/how-it-works](https://docs.fly.io/litefs/how-it-works)). Last release v0.5.14 on 2025-04-22, last commit the same day (GitHub API).
- cr-sqlite: per-column LWW CRDTs, rows matched by primary key, transport supplied by the user, and the page does not say how foreign keys or unique constraints merge ([github.com/vlcn-io/cr-sqlite](https://github.com/vlcn-io/cr-sqlite)). Last release v0.16.3 on 2024-01-17 (GitHub API).
- libSQL embedded replicas: reads are local, writes go to the remote primary, and offline writes only with `offline: true`; every example passes an `authToken` ([docs.turso.tech](https://docs.turso.tech/features/embedded-replicas/introduction)).
- ElectricSQL: "does not do write-path sync" ([electric.ax/docs/guides/writes](https://electric.ax/docs/guides/writes)).
- PowerSync: writes queue on the client to a developer's `uploadData()` backend, authenticated with a JWT ([docs.powersync.com client architecture](https://docs.powersync.com/architecture/client-architecture)).

**Point 2:**
- *Consistency:* constraints hold locally. Across nodes it is single-writer, or CRDT last-write-wins that loses intent.
- *Offline:* reads always; writes only under CRDT, an offline flag, or a queue.
- *Latency:* seconds or less.
- *Conflicts:* the primary decides, or LWW, or the app's backend.
- *Agent-friendliness:* SQL through a local file.
- *Audit:* no PR diff.
- *Service:* a primary or sync service plus tokens; Litestream and cr-sqlite need none beyond storage or transport.

**Point 3:**
- *Two nodes deciding at once:* LWW silently keeps one decision, which fails P35, since the losing decision's cause disappears.
- *A node offline for a day:* only CRDT or queued designs survive.
- *An agent verifying a fact without a service:* yes with a local copy, but the copy cannot be verified against reviewed history, which fails P2.
- *An adopter with no database:* mostly loses.

### F4. A cloud relational database
**Mechanism:** one shared server holds the truth; clients connect over the network.

**Real systems:**
- Postgres `LISTEN`/`NOTIFY`: the payload must be "shorter than 8000 bytes", delivery goes to sessions "that has previously executed LISTEN", only on commit, and the page says nothing about durability ([postgresql.org/docs/current/sql-notify.html](https://www.postgresql.org/docs/current/sql-notify.html)).
- Supabase Realtime: Postgres Changes "does not guarantee delivery", and a client away for 30 s loses those changes ([supabase blog](https://supabase.com/blog/realtime-or-pipelines-how-to-choose-the-right-tool), [self-hosting realtime](https://supabase.com/docs/reference/self-hosting-realtime/introduction)). Both quotes came through search summaries, not pages I fetched.
- Neon: copy-on-write branches, and instant restore 6 h on Free, 1 day on paid plans ([neon.com/docs/introduction/branching](https://neon.com/docs/introduction/branching)).

**Point 2:**
- *Consistency:* full ACID with foreign keys, the strongest live consistency.
- *Offline:* none.
- *Latency:* milliseconds.
- *Conflicts:* serialised by the server.
- *Agent-friendliness:* SQL, but every read needs a credential and the network.
- *Audit:* none in review.
- *Service:* a hosted database with a connection secret on every node.
- *Cost:* per seat or usage.

**Point 3:**
- *Two nodes deciding at once:* handled, by serialisation.
- *A node offline for a day:* loses. It cannot read or write.
- *An agent verifying a fact without a service:* loses.
- *An adopter with no database:* loses.
- *P3:* the verdict is no longer computed locally.
- *Secrets:* the connection string must live somewhere. That is possible in an OS store, but it is a new credential surface on every node.

### F5. Message buses, event logs and event sourcing
**Mechanism:** an append-only ordered log; consumers keep offsets, and state is replayed from events.

**Real systems:**
- Event sourcing: "capture all changes … as a sequence of events", with complete rebuild and temporal queries ([martinfowler.com](https://martinfowler.com/eaaDev/EventSourcing.html)).
- NATS JetStream KV: a bucket is a stream with compare-and-swap, watchers and per-key history ([docs.nats.io KV](https://docs.nats.io/nats-concepts/jetstream/key-value-store)). Leaf nodes dial out and need their own JetStream domain for a local store; the page does not describe behaviour while disconnected ([docs.nats.io leafnodes](https://docs.nats.io/running-a-nats-service/configuration/leafnodes)).
- Redis Streams: `XADD` and `XREAD BLOCK`; consumer groups keep a pending list until `XACK` ([redis.io streams](https://redis.io/docs/latest/develop/data-types/streams/)).
- Kafka: events "durably stored in topics" on brokers, with per-topic retention ([kafka.apache.org/intro](https://kafka.apache.org/intro)).

**Point 2:**
- *Consistency:* order and offsets only; relations are left to consumers.
- *Offline:* a consumer catches up from its offset within retention.
- *Latency:* milliseconds.
- *Conflicts:* compare-and-swap per key in NATS KV.
- *Agent-friendliness:* needs a client binary.
- *Audit:* none in review.
- *Service:* a broker plus credentials.

**Point 3:**
- *Real-time between online nodes:* wins.
- *A node offline for a day:* fine if retention covers it.
- *An agent verifying a fact without a service:* loses.
- *An adopter with no database:* loses, because a broker is a service.
- *P2/P3:* a witness living in the broker is not committed history.
- *Note:* the git commit chain is itself an event-sourced log. Probes B and C' show both a log on refs and a log in a union-merged file.

### F6. Graph and agent-memory systems
**Mechanism:** an LLM extracts entities and facts into a graph or vector store; retrieval is by search.

**Real systems:**
- Graphiti/Zep: bi-temporal; facts are "invalidated — not deleted"; needs Neo4j, FalkorDB or Neptune (Kuzu deprecated); an LLM is required for ingestion, OpenAI by default; an MCP server exists ([github.com/getzep/graphiti](https://github.com/getzep/graphiti)).
- mem0: defaults to OpenAI `gpt-5-mini` with `OPENAI_API_KEY`, Qdrant, and a SQLite history store; self-hosted needs Postgres with pgvector ([docs.mem0.ai](https://docs.mem0.ai/open-source/overview)).
- Neo4j: Community Edition is "suitable for single-instance deployments", and clustering is Enterprise-only ([neo4j.com operations manual](https://neo4j.com/docs/operations-manual/current/introduction/)).
- Letta: memory blocks on a hosted or self-hosted server, plus MemFS (F1).

**Point 2:**
- *Consistency:* extraction is a model's output, so it is not deterministic.
- *Offline:* only fully local stacks.
- *Agent-friendliness:* high for recall, low for proof.
- *Audit:* none.
- *Service:* a graph database plus an LLM key.

**Point 3:**
- *P2 and P33:* loses. An edge produced by an LLM extraction is not "declared once at the site that owns its fact" (P33), and it is not a witness (P2).
- *An agent verifying a fact without a service:* loses.
- *Worth taking:* the bi-temporal invalidate-not-delete idea, which gov's `supersedes` edge already approximates.

### F7. Agent-native access layers
**Mechanism:** a protocol through which agents reach a store or each other. It is not a store.

**Real systems:**
- MCP: stdio, where "the client launches the MCP server as a subprocess", or Streamable HTTP with optional SSE and `Last-Event-ID` resumption ([modelcontextprotocol.io 2025-11-25 transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)).
- A2A 1.0.0: JSON-RPC, gRPC or REST between opaque agents, with Agent Cards, task states, webhook push notifications and required authentication ([a2a-protocol.org](https://a2a-protocol.org/latest/specification/)). The page says A2A joined the Agentic AI Foundation; I could not confirm a Linux Foundation tie from the fetched part.
- MCP Agent Mail, an HTTP FastMCP server over git plus SQLite, with advisory file reservations; the README does not say how several machines share it ([github](https://github.com/Dicklesworthstone/mcp_agent_mail)).

**Point 2:**
- An MCP server over stdio is local, needs no credential, and costs one tool schema per session.
- A2A needs an HTTP endpoint and authentication on each agent, which means agents that are online at the same time.

**Point 3:**
- A2A loses for an offline node and for an adopter that runs no service.
- Over stdio, MCP inherits the scenarios of whatever store it wraps.
- **Rule:** never a family on its own; only an access layer over another family.

### F8. Git-native coordination on refs and notes
**Mechanism:** state lives in commits on refs outside the branches, moved by compare-and-swap push, merged by ref or notes strategies.

**Real systems:**
- git-bug: operation packs as JSON blobs, commit chains under `refs/<namespace>/<id>`, ordered by Lamport clocks, ties broken by pack id ([data model](https://github.com/git-bug/git-bug/blob/master/doc/design/data-model.md)), pushed and pulled over any git remote ([github.com/git-bug/git-bug](https://github.com/git-bug/git-bug)).
- git-appraise: notes under `refs/notes/devtools/*`, one JSON item per line so "cat_sort_uniq" merges automatically ([github.com/google/git-appraise](https://github.com/google/git-appraise)). Last push 2023-08-12 (GitHub API).
- git notes merge strategies: `union` and `cat_sort_uniq` ([git-scm.com/docs/git-notes](https://git-scm.com/docs/git-notes)). That `refs/notes/*` is outside the default refspecs is not stated on that page; it is from my own knowledge.
- Dolt's `refs/dolt/data` (F2), and gov's own run claims.

**Point 2:**
- *Consistency:* append-only chains plus compare-and-swap. Nothing is lost under a race (B), and per-sender refs remove contention (B').
- *Offline:* append locally, push on reconnect. A per-sender ref never conflicts; a shared chain must re-parent.
- *Latency:* a push plus the reader's poll. The floor is about 0.6 s per `ls-remote` (B''), and there is no notification.
- *Agent-friendliness:* `git log refs/gov/mail/...` returns about 54 bytes for two messages.
- *Audit:* not in PR diffs (refs sit outside branches), but fully in git.
- *Service:* none beyond the remote.

**Point 3:**
- *Two nodes deciding at once:* compare-and-swap serialises a lease (one wins); messages from both survive.
- *A node offline for a day:* fine.
- *A large history:* refs are tiny, and closed refs are pruned per `coordination [design]` item 6.
- *An agent verifying a fact without a service:* yes.
- *An adopter with no database:* fine.
- *Real-time:* loses.

**Only one access-layer mechanism?** No. MCP (host to tool) and A2A (agent to agent) differ, which is why F7 lists both. Beyond these eight families, further candidates differ only in detail. Examples: Oxen and lakeFS are versioned stores like F2; CouchDB and PouchDB are synced stores like F3.

---

## Candidates for gov

| # | Candidate | Smallest scenario that makes it LOSE | Result |
|---|---|---|---|
| K1 | **F1 + F8:** records in the tree; one derived SQLite index per tree, rebuilt and never written; coordination on per-sender refs (`refs/gov/mail/<slug>/<sender>`, leases by compare-and-swap) | (a) Two nodes write conflicting relations on separate branches. (b) A sub-second notice is needed between online nodes. | (a) Probe D: git merges clean; the index query catches it. It loses only if no gate per target is armed, which the plan's gate list lacks today. (b) Loses. The floor is a poll of about 0.6 s plus push time, and no push notification exists. |
| K2 | **K1 + a doorbell:** a live channel carrying only `{ref, message id}` (harness session messaging, as already designed in `coordination [design]` item 7; or an optional NATS, ntfy or Postgres `NOTIFY` slot) | A doorbell is lost, or the node is offline. | Survives by construction: the ref is the record and the doorbell only shortens the poll. A lost ring degrades to K1's latency. It never fails P2 or P3, because the doorbell carries no fact. `NOTIFY` and Supabase drop messages (sources above), which is acceptable only because of this design. |
| K3 | **F2 Dolt** as the record store, through `refs/dolt/data` | An adopter that will not install a binary; a reviewer reading a PR diff. | Loses on both. It also splits the repository into two stores. Beads needed a server for concurrent writers and later restored a serverless mode. |
| K4 | **F4 cloud Postgres** + realtime | A node offline for a day; an agent verifying a fact without a service. | Loses on both, and fails P3. The connection secret is a new credential on every node. |
| K5 | **F3 synced SQLite** (cr-sqlite, libSQL) as the record store | Two nodes decide at once under LWW. | Loses: one decision silently vanishes. It also fails P2, since the replica's state is not committed history. cr-sqlite's last release was 2024-01. |
| K6 | **F5 JetStream** as the bus beside git (truth in the broker) | An adopter that will not run a broker; a node offline past retention. | Loses on the first. Kept in K2 only as an optional doorbell slot. |
| K7 | **F6 Graphiti or mem0** as the memory | An agent verifying an edge offline; P33's declared-edge rule. | Loses on both: the edge is LLM-extracted and an LLM key is needed. |
| K8 | **F7 MCP over stdio** as the read surface over K1's index | A harness without MCP. | Survives as an optional slot: the CLI (`gov tag`, `gov trace`) remains the floor, consistent with P36. |

## My pick

**K2:** K1's records-in-tree, one derived SQLite index and per-sender refs, plus an ids-only doorbell slot, with K8's MCP over stdio as an optional read surface.

The repository's seams already carry it:
- memory-recall's derived SQLite index (`tools/memory-recall/query.py:77`, `:785`);
- the compare-and-swap ref claim (`tools/unattended/unattended.sh:2087`, `:2423`);
- "write the mailbox first, then deliver live" (`coordination [design]` item 7).

Two changes to the designed mechanism follow from the probes:
1. **Per-sender mailbox refs** in place of one chain per build: 0 retries against 26–28 retries for 40 messages (B, B').
2. **An invariant leg on the derived index that runs after merge**, because git merges conflicting decisions clean (D).

The owner's "relational structure that mechanically maintains connections" is this index plus gates. A relational store that is written to directly is what produced beads' split-brain problems.

**Scenario it handles worst:** sub-second, real-time coordination between online nodes whose harness offers no live session messaging and whose adopter enables no doorbell. The floor is then about 0.6 s per `ls-remote` poll plus an unmeasured push round trip, and the poll repeats per node per mailbox. The second-worst is a very large adopter's cold index build: 15 s at 213k files, linear.

## Open caveats
- Push latency to the real remote and git hosts' rate limits on frequent polling are unmeasured.
- The beads migration rationale comes only from Dolt and Gas City sources.
- Letta's MemFS and Supabase's delivery claims came through search summaries, not pages I fetched.
- cr-sqlite and LiteFS release dates come from the GitHub API, not the projects' pages.
