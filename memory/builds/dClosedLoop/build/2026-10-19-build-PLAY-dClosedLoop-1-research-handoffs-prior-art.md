# Research: handoffs, prior art outside gov

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 133's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-14-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`.

---

All sources below were read on 2026-10-19. Records are cited as `<record> [<tag>]` and code as `path:line`. The probes ran in a copy under the system temp root (`handoff-probe.dPmc`), which is now deleted, and I wrote nothing in the tree.

Scenarios used in point 3:
- **S1:** a commitment the next step silently drops.
- **S2:** two sessions on one build each decide the same question differently.
- **S3:** a problem found on one node that another node walks into an hour later.
- **S4:** a session resumed after compaction redoes finished work.

## Families

### F1. Prose transfer: the transcript or a text message goes to the receiver

**Mechanism.** The receiver gets the sender's conversation, or a summary of it, or a plain-text message. Meaning lives in prose.

**Systems:**
- **OpenAI Agents SDK handoffs.** "the new agent takes over the conversation, and gets to see the entire previous conversation history." An `input_filter` rewrites a `HandoffInputData`. `nest_handoff_history` (beta, off by default) "compacts summarizable history into ordered assistant summary segments." `input_type` validates only the handoff call's own arguments and "does not replace the next agent's main input." (https://openai.github.io/openai-agents-python/handoffs/)
  - The SDK's sessions store history items in SQLite, Redis, SQLAlchemy or similar backends. A compaction session summarises them. (https://openai.github.io/openai-agents-python/sessions/)
  - Local context "is not sent to the LLM." (https://openai.github.io/openai-agents-python/context/)
- **AutoGen Swarm.** "all agents share the same message context". The next speaker is chosen from the most recent `HandoffMessage` (https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/swarm.html). A team's `save_state()` is a JSON dict holding the message thread and each agent's model context (https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/state.html).
- **Cognition, "Don't Build Multi-Agents" (dated "06.12.25").** "Share context, and share full agent traces"; "Actions carry implicit decisions, and conflicting decisions carry bad results" (https://cognition.com/blog/dont-build-multi-agents).
- **Claude Code cross-session messaging.** "Plain text only." A held message in a `-p` session is dropped after `dialogExpiry` (5 minutes by default). The receiving session holds at most 100 messages and drops the oldest past that, and queues at most 50 accepted messages. An `offline` remote session gets the message only after its machine reconnects. (https://code.claude.com/docs/en/cross-session-messaging)

**Point 2:**
- **Payload:** untyped prose.
- **What the receiver must answer:** nothing.
- **Persistence:** the session store, which is per backend, or nothing for live messages.
- **Latency:** in-turn.
- **Detecting a lost or bent item:** none built in. A summary may drop an item and no one is told.

**Point 3:**
- **S1:** loses, because nothing enumerates the commitments.
- **S2:** loses. Cognition's Flappy Bird case is exactly this: two sub-agents built a mismatched background and bird.
- **S3:** loses unless the sender happens to address the right live session.
- **S4:** loses, because the resumed state is a summary of the transcript.

### F2. Call and typed return: a prompt goes in and a schema-validated result comes out

**Mechanism.** The parent hands the child a prompt. The child returns a value validated against a JSON Schema, with re-prompts on a mismatch.

**Systems:**
- **Claude Agent SDK subagents.** "The only content you pass from parent to subagent is the Agent tool's prompt string." Only the final message returns. (https://code.claude.com/docs/en/agent-sdk/subagents)
- **Claude Agent SDK structured outputs.** `outputFormat` takes a draft-07 schema. A failed run ends with `error_max_structured_output_retries`, and "A result can also end with subtype `success` but no `structured_output`… Treat that case as a failure" (https://code.claude.com/docs/en/agent-sdk/structured-outputs).
- **CrewAI.** Tasks support `context`, `output_pydantic`/`output_json`, and guardrails that retry up to `guardrail_max_retries` (default 3) (https://docs.crewai.com/en/concepts/tasks). The docs do not say what reaches the next prompt. The source shows that what is handed on is `DIVIDERS.join(output.raw for output in task_outputs)` with `"\n\n----------\n\n"` (https://raw.githubusercontent.com/crewAIInc/crewAI/main/lib/crewai/src/crewai/utilities/formatter.py). **The type is validated on return and then flattened back to raw text at the next edge.**
- **MCP tools.** With an `outputSchema`, "Servers MUST provide structured results that conform… Clients SHOULD validate" (https://modelcontextprotocol.io/specification/2025-11-25/server/tools).

**Point 2:**
- **Payload:** JSON typed by a schema.
- **What the receiver must answer:** the return must parse. Coverage of the inputs is not checked.
- **Persistence:** none of its own. A transcript file exists per subagent and is resumable by agentId within the same session.
- **Latency:** in-call.
- **Detection:** shape only. A row omitted from an array, or a false "used", passes a static schema (Probe 1 below).

**Point 3:**
- **S1:** loses under a static schema. It holds if each work order renders its own schema (Probe 1).
- **S2:** loses, because nothing is shared across calls.
- **S3:** loses, because nothing persists.
- **S4:** partial. A persisted return is a witness only if someone keys and stores it.

### F3. Shared typed state with reducers and checkpoints

**Mechanism.** Every node reads and writes one typed state. A per-key reducer merges writes, and a checkpoint is saved at each super-step.

**System: LangGraph.**
- State is a TypedDict or Pydantic model. Each key has a reducer, and a key without one is overwritten (https://docs.langchain.com/oss/python/langgraph/graph-api).
- Parallel writes to a key with no reducer raise `INVALID_CONCURRENT_GRAPH_UPDATE` (https://docs.langchain.com/oss/python/langgraph/errors/INVALID_CONCURRENT_GRAPH_UPDATE).
- Checkpoints are saved per `thread_id` with `values`, `next` and `tasks`. On resume, "you don't re-run the successful nodes" (pending writes), but nodes after the checkpoint re-execute "LLM calls, API requests". Durability is `exit`, `async` or `sync`. (https://docs.langchain.com/oss/python/langgraph/checkpointers)
- The cross-thread Store is keyed by namespace and key. **Its docs describe no locking or conflict handling for concurrent writers** (https://docs.langchain.com/oss/python/langgraph/stores).

**Point 2:**
- **Payload:** typed channels.
- **What the receiver must answer:** nothing. A node reads whatever it reads.
- **Persistence:** Postgres or SQLite checkpointers, plus the Store.
- **Latency:** one database write per super-step.
- **Detection:** a same-key conflict within one super-step, and nothing else.

**Point 3:**
- **S1:** loses, because a key nobody reads is never flagged.
- **S2:** holds inside one graph run (the concurrent-update error). Across threads and machines it loses, because the Store's semantics are undocumented.
- **S3:** partial, through the Store, but only if a reader knows to look up the key.
- **S4:** holds for completed nodes, and loses for a side effect made after the checkpoint.

### F4. A durable workflow built on an event history, with typed messages

**Mechanism.** The workflow's state is rebuilt by replaying an append-only event history. Senders reach it through typed signals (asynchronous), queries (read-only) and updates (synchronous, with a validator).

**System: Temporal.**
- Replay checks commands against the history (https://docs.temporal.io/workflow-execution).
- Signals are recorded as `WorkflowExecutionSignaled`. The send "returns once the server accepts it, not once the Workflow processes it." Update validators reject before the history. A workflow that finishes with handlers still running logs a warning, and `all_handlers_finished` exists to wait for them. (https://docs.temporal.io/develop/python/message-passing, https://docs.temporal.io/references/events)
- "only one Workflow Execution with a given Workflow Id can be in an Open state at any given time". The default conflict policy is Fail. (https://docs.temporal.io/workflow-execution/workflowid-runid)
- The encyclopedia page (https://docs.temporal.io/encyclopedia/workflow-message-passing) does not say whether signals are recorded. The Python guide does: **the sources differ in coverage.**

**Point 2:**
- **Payload:** typed by the SDK.
- **What the receiver must answer:** an update gets an accept or reject plus a result; a signal gets none.
- **Persistence:** the server's history, across machines.
- **Latency:** one server round trip.
- **Detection:** determinism on replay, the validator, the workflow-id conflict check, and a warning for unfinished handlers.

**Point 3:**
- **S1:** partial. Only typed handlers are checked.
- **S2:** holds when the decision is the workflow id, a derived business key.
- **S3:** loses unless the finding is a signal to a known workflow.
- **S4:** holds, through replay. An activity's side effect still needs idempotency.

### F5. A task-lifecycle protocol: artifacts passed by reference

**Mechanism.** Work is a task with a closed set of states, and outputs are artifacts addressed by id or URI. Receivers fetch what they need instead of receiving prose.

**Systems:**
- **A2A 1.0.0.**
  - A Task carries `id`, `contextId`, `status`, `artifacts` and `history`.
  - States include `INPUT_REQUIRED` and `AUTH_REQUIRED`.
  - A Part holds exactly one of `text`, `raw`, `url` or `data`.
  - A message names earlier tasks through `referenceTaskIds`.
  - A terminal task "cannot restart". A refinement is a new task in the same `contextId`.
  - **The spec requires no acknowledgement of a message and no schema check of `data`.** The only ack is a 2xx to a push notification.
  - (https://a2a-protocol.org/latest/specification/, https://a2a-protocol.org/latest/topics/life-of-a-task/)
- **MCP resources.** Each resource has a URI. The host application decides what enters context ("application-driven"). `resources/subscribe` triggers `notifications/resources/updated`, and annotations carry `priority` and `lastModified` (https://modelcontextprotocol.io/specification/2025-11-25/server/resources).
- **Anthropic's research system (2025-06-13).** Subagents store their work outside and pass back lightweight references. The lead saves its plan to memory before the context passes 200k tokens. Vague task descriptions produced duplicate work. (https://www.anthropic.com/engineering/multi-agent-research-system) The fetch tool paraphrased this post, so treat the wording as a paraphrase.

**Point 2:**
- **Payload:** typed parts and URIs.
- **What the receiver must answer:** a state transition, with no per-item answer.
- **Persistence:** whatever the server keeps.
- **Latency:** an HTTP round trip, or a push.
- **Detection:** state and versioned artifacts. Nothing checks whether a referenced item was read.

**Point 3:**
- **S1:** loses, because a reference not followed is not flagged.
- **S2:** loses, because two tasks in one context may diverge.
- **S3:** partial: a subscription works if the reader subscribes to the right URI.
- **S4:** holds for artifacts. Whether work was finished is held by the server's state, not by the agent.

### F6. Blackboard, or a publish-subscribe pool

**Mechanism.** Agents post to a shared space. A control unit, or the agents themselves, pick who acts from what is on the board, and readers subscribe by interest.

**Systems:**
- **LbMAS (arXiv 2507.01701, 2025-07-02).** Agents see "all the information and others' messages". Who acts is chosen from the board's contents. It reports competitive accuracy with fewer tokens.
- **arXiv 2510.01285 (v2, 2026-01-31).** A central agent posts requests, and sub-agents "volunteer to respond based on their capabilities". It reports 13% to 57% relative gains over master-slave baselines.
- **MetaGPT (arXiv 2308.00352v7, §3.2).** Agents exchange structured documents instead of dialogue, because of the telephone game: "the original information may be quite distorted". A shared message pool uses role-based subscription, and an agent acts only once all its prerequisites have arrived.

**Point 2:**
- **Payload:** a free or document schema.
- **What the receiver must answer:** nothing, beyond prerequisites gating action in MetaGPT.
- **Persistence:** the board's store.
- **Latency:** a read per tick.
- **Detection:** missing prerequisites (MetaGPT). Otherwise none.

**Point 3:**
- **S1:** loses.
- **S2:** loses unless board entries are keyed.
- **S3:** **holds if the subscription is by subject.** This is the family's strength.
- **S4:** partial.

### F7. Work-item tracker as the medium

**Mechanism.** Hand-offs are items with ids, typed status, dependencies and a "ready" query. Agents claim items and leave notes on them.

**Systems:**
- **Beads.**
  - Dolt-backed. Embedded mode has a single writer; concurrent writers need server mode.
  - Hash ids such as `bd-a1b2` avoid merge collisions.
  - Dependency types are `blocks`, `related` and `parent-child`, with links such as `supersedes`.
  - `bd ready` lists items with no open blockers.
  - Machines sync through `refs/dolt/data` on a git remote.
  - Old items "decay" into summaries.
  - (https://github.com/steveyegge/beads)
- **Linear agent sessions.**
  - Activities are typed: `thought`, `elicitation`, `action`, `response`, `error`.
  - The agent must emit an activity "within 10 seconds", or the session is marked unresponsive.
  - States are `pending`, `active`, `awaitingInput`, `complete`, `stale` and `error`.
  - (https://linear.app/developers/agent-interaction)
- **Claude Code agent teams.**
  - A task list with dependencies and file-locked claims.
  - A validated JSON mailbox per agent.
  - The documented limitation: "teammates sometimes fail to mark tasks as completed, which blocks dependent tasks".
  - No resume for in-process teammates.
  - (https://code.claude.com/docs/en/agent-teams)
- **Anthropic's long-running harness (2025-11-26).**
  - A JSON feature list in which only the `passes` field may change.
  - JSON was chosen because models are less likely to overwrite it inappropriately than Markdown.
  - `claude-progress.txt` plus git log give each session its bearings, followed by a smoke test before new work.
  - (https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- **GitHub Copilot coding agent.** One PR and one repository per task, and a 59-minute session cap. The page does not describe how an issue is handed over (https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent).

**Point 2:**
- **Payload:** typed status and dependencies, with prose bodies.
- **What the receiver must answer:** a status, and a timed ack in Linear's case.
- **Persistence:** cross-machine, through Dolt over git or a SaaS service.
- **Latency:** an API or sync round trip.
- **Detection:** blocked dependencies and staleness, but **the status is typed by the agent itself** (the agent-teams limitation above).

**Point 3:**
- **S1:** loses, because item bodies are prose.
- **S2:** partial: hash ids prevent id collisions, not two answers to one question.
- **S3:** holds if the finding is filed and the reader runs a ready or search query.
- **S4:** holds if the status is witnessed. Harness-style, it loses when the agent typed "passes" wrongly.

### F8. Failure research on hand-offs: not a medium

- **MAST** (arXiv 2503.13657v3, 1600+ traces, 7 frameworks) has 14 modes. The hand-off-relevant ones:

  | Mode | Share | Scenario |
  |---|---|---|
  | FM-1.3 step repetition | 15.7% | S4 |
  | FM-2.6 reasoning-action mismatch | 13.2% | |
  | FM-1.5 unaware of termination | 12.4% | |
  | FM-3.3 incorrect verification | 9.1% | |
  | FM-3.2 no or incomplete verification | 8.2% | |
  | FM-2.3 task derailment | 7.4% | |
  | FM-2.2 fail to ask for clarification | 6.8% | |
  | FM-1.4 loss of conversation history | 2.8% | |
  | FM-2.1 conversation reset | 2.2% | |
  | FM-2.5 ignored other agent's input | 1.9% | S1 |
  | FM-2.4 information withholding | 0.85% | S1 |

  - Insight 2: "Solutions focused on context or communication protocols are often insufficient for FC2 failures."
  - Adding a high-level verification step gave ChatDev +15.6%.
  - Our earlier record agrees on the percentages it quotes: `research-roles-priorart.md [6. Pick]`.
- **The telephone game** (arXiv 2407.04503, ICLR 2025). "Small biases, negligible at the single output level, risk being amplified in iterated interactions". Attraction is stronger under open-ended instructions than under constrained ones.
- **Who&When** (arXiv 2505.00212). The best method attributes the failing agent at 53.5% and the decisive step at 14.2%. **Reconstructing cause from transcripts after the fact is unreliable**, which favours recording the cause at write time (P35).
- **Measured at home:** handing the diff check the scout's MUST seams as `{item, used|bypassed|not-applicable, why}` rows took it from 13 to 20 of 23 (`git show origin/main:memory/builds/aScoutedSeam/build/2026-10-19-build-TOOL-aScoutedSeam-3-3-agent-prompt-principles.md` [P7], lines 103-115).

## Candidates for gov

### Probes run, and what the design records say

**Probe 1: does the return channel catch a dropped or invented commitment row?**
- Setup: jsonschema 4.26.0 in a temp venv, Draft7Validator, commitments S1 to S3.
- The per-order schema is rendered per work order: `item: {enum: commitments}`, `maxItems`, and one `contains`/`const` per commitment. All of these exist in draft-07, the SDK's draft.

```
all-answered           static=PASS  per-order=PASS []
S2-dropped             static=PASS  per-order=REJECT ["None of [...
S2-invented-S9         static=PASS  per-order=REJECT ["'S9' is not one of ['S1', 'S2', 'S3']"]
S2-twice-S3-missing    static=PASS  per-order=REJECT ["None of [...
```

**Probe 2: two sessions decide question Q1 of build b differently.**
- Setup: a bare remote and two clones, using `--force-with-lease` compare-and-swap.

```
== shape 1: append-only mailbox refs/gov/mail/b, CAS on the tip
A append: ok
B append at stale tip: exit 1
B re-append on fresh tip: ok
mailbox now holds:
  decided Q1=prose
  decided Q1=rows
== shape 2: keyed decision register refs/gov/decisions/b/Q1, create-only
A decide: ok
B decide: exit 1
register holds: Q1=rows
```

**Probe 3: a session posts, crashes before writing its witness, resumes and posts again.**

```
same body, two attempts: same sha? no
-- append-chain retry:  attempt 2 ok -> 2 messages
-- keyed by derived id b8ef889c075e:  attempt 2 exit 1 -> 1 message(s)
```

**Latency.** `git ls-remote origin 'refs/gov/*'` three times returned 17 refs in 772, 603 and 640 ms.

**What the design records say, checked against the code:**
- **Mailbox.** It is "an append-only chain of commits, one per message, appended by compare-and-swap". A transition is refused while a message is "neither answered nor acknowledged" (`2026-10-14-build-PLAY-dClosedLoop-1-coordination.md` [design], unit 6). That catches an unanswered message, not a contradictory one. Probe 2 shape 1 is exactly this design.
- **Fork ids.** A fork's id is minted by `record`, and the decision log is keyed by (build, fork id) (`2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md` [design] item 2). `record` is "content-addressed" (`architecture-v2.md` [revised] notes, line 246). So two sessions that decide one question differently produce two distinct ids, and both land. **Nothing in the records keys a decision by the question.**
- **Mailbox recipients.** Recipients are a build or its units (coordination [design] 6). **There is no channel addressed by subject.** One existing seam is subject-keyed and fleet-wide: `refs/gov/bar-red`. `post-merge.sh` publishes it by compare-and-swap (`tools/run-gates/post-merge.sh:249-284`). Every node's pre-push reads it and forces a FULL bar on any descendant (`.githooks/pre-push:1927-1971`).
- **Live delivery.** The design writes the mailbox first and delivers live second (coordination [design] 7). The Claude Code limits listed under F1 confirm that it must.

### C1. Typed work order plus a schema rendered per order, with commitment rows (F2 extended by P7, P26 and P29)

- **Smallest losing scenario:** S1, a return that omits commitment S2.
  - Under a static schema it **loses** (Probe 1: PASS).
  - Under the rendered schema it **holds** (REJECT on drop, on an invented id, and on a duplicate standing in for a missing row).
- **Still loses:** a row that says "used" falsely. That is bent information, MAST FM-3.2/3.3 (8.2% and 9.1%), and only a verifier catches it (P29).
- **Out of reach:** it does not touch S2, S3 or S4.

### C2. C1 plus the designed append-only mailbox chain (today's design)

- **Smallest losing scenario:** S2.
- **Result: loses** (Probe 2 shape 1). The compare-and-swap serialises the writers, the correct retry lands both decisions, and only a human-like reader would notice.
- **Also loses S4 duplication** (Probe 3: 2 messages), because a commit's SHA changes with its timestamp.
- **S3** reaches the other node only if the finder addresses its build.

### C3. C1 plus create-only registers on the remote, keyed by derived key (F4's workflow-id uniqueness and F3's same-key conflict, over gov's refs)

**The registers:**
- **Decisions:** `refs/gov/decisions/<build>/<key>`, where the key is derived from the work-order slot that raised the question (item id and declared fork slot), never from its wording.
- **Messages:** the message id is derived from (sender act, item, kind, subject), so a retry is a no-op.
- **Notices:** keyed by subject (a path, definition or tag from P32/P33, or a node fact). The supervisor cuts each work order (P29) and reads the notices that intersect the item's seed. This extends the `bar-red` pattern beyond SHA ancestry.

**Results:**
- **Smallest losing scenario:** two sessions derive different keys for the same question.
- S2 with a declared slot **holds** (Probe 2 shape 2: B exits 1 and must read A's decision).
- An S4 retry **holds** (Probe 3: 1 message).
- S3 **holds** when the problem's subject intersects the later item's seed.
- **Cost:** one round trip of about 0.6 to 0.8 s per lookup, which fits the design's rule that leases and mail "ride transitions and passes only" (coordination [design], Risks).

### C4. A shared typed state store (F3) as the medium across sessions

- **Smallest losing scenario:** two nodes write one key to the cross-thread Store. LangGraph documents no conflict semantics for that.
- **Result:** rejected. Making the store safe across nodes means adding compare-and-swap per key, which collapses it into C3 on a heavier dependency.
- **Not run here:** I did not install LangGraph. The build's test would be two `PostgresStore` clients doing `put` on one key while each is unaware of the other, then asserting that one write is refused.

### C5. A durable workflow engine (F4) as the runtime

- **Smallest losing scenario:** a node offline, or no Temporal server present.
- **Result:** rejected. It contradicts the local-first verdict (P3) and the rule that no harness is the runtime (P36), and gov ships bash and python over a git remote.
- **What C3 keeps from it:** workflow-id uniqueness, update validators, and an event-history witness.

### C6. Tracker as the medium (F7)

- **Smallest losing scenario:** an agent finishes the work but never marks the item done, which is the documented agent-teams limitation. Or an agent marks it done falsely, the harness's "passes" problem.
- **Result:** loses S1 and S4, because the status is agent-typed and violates P2 and P23. Beads adds Dolt for concurrent writers.
- **Ideas folded into C3:** the hash ids, the `ready` query (gov's `next`, P22), and dependency gating.

### C7. Transcript or live-message transfer (F1) as the primary channel

- **Smallest losing scenario:** S4. After `nest_handoff_history` or a compaction summary, a commitment survives only as prose.
- **Also loses:** live text is held and then dropped after 5 minutes in a `-p` session.
- **Result:** rejected as the medium. It stays as the "live second" path of the design.

### C8. A blackboard (F6) written by workers

- **Smallest losing scenario:** a worker that cannot write. "seven of ten roles cannot post" (`2026-10-14-build-PLAY-dClosedLoop-1-research-roles-interactions.md` [5. Candidates], B).
- **Result:** rejected as a channel. A board written by the supervisor alone and keyed by subject is C3's notice register, so further variants of it differ only in detail.

## Pick

**C3:** C1's rendered per-order schema with commitment rows on every role edge, plus create-only registers on the remote for decisions, messages and notices. Each register is keyed by a derived key, written by the supervisor, and read when a work order is cut. The designed mailbox chain stays as the log people read, with each message also keyed by its derived id.

**Worst scenario: S2 for a question no item declared.** Two sessions on one build each meet an architectural fork that no work-order slot names. They phrase it differently, derive different keys, and both decisions land, just as Probe 2's shape 1 landed both.

C3 catches this only downstream:
- when both decisions touch one subject that a notice or lease overlap covers; or
- at review.

The build must run this fixture as its losing test. Two act sessions are handed the same underdetermined unit pair, and the build counts how many contradictory decision records reach the branch with no refusal. The same holds for S3 when the problem's subject is not in the later item's seed, such as a node-level toolchain fault. That case needs notices keyed by node fact, which the design does not yet name.
