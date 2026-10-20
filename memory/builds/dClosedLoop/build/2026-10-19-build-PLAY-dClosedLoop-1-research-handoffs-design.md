# Research: handoffs in the converged design

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 132's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-13-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`.

---

**Point 4: is there one handoff system in the converged design, and is it good enough?**

**Short answer.** No. The design has five carriers that pass work between agents, sessions and nodes, and they share keys but not one contract. Inside one item's cycle the handoff is typed and well checked. It falls short in three places:

- **Between items and steps**, an earlier step's commitments are not handed to the next step as rows it must answer. The record vocabulary for such rows appears 0 times in 154 records, and that includes the edge aScoutedSeam measured.
- **Between nodes**, no rule says when a build's branch reaches the remote before landing. Until it does, another node cannot see completed units.
- **For "completed work, decisions, problems"**, the mailbox has no message kind for any of the three.

My pick is one contract: every commitment crosses an edge as a row the receiver must answer, the rows ride the record graph, and the build branch is pushed per witnessed item.

I wrote nothing in the repository. The probes ran on a `git archive e1a54ac67` copy of the build folder under the scratchpad, since deleted. `git status` still shows only other agents' untracked research files.

**Record short names** (all under `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\`):

| Short name | File |
|---|---|
| v2 | `2026-10-14-…-architecture-v2.md` |
| roles | `…-roles.md` |
| layer-roles | `…-layer-roles.md` |
| flow-roles | `…-flow-roles.md` |
| flow-steps | `…-flow-steps.md` |
| layer-runtime | `…-layer-runtime.md` |
| coordination | `…-coordination.md` |
| orientation | `…-orientation.md` |
| flow-interactions | `…-flow-interactions.md` |
| memory-plan | `…-memory-plan.md` |
| systems | `…-systems.md` |
| fates | `…-fates.md` |
| ownership | `…-ownership.md` |
| layer-memory | `…-layer-memory.md` |

## 1. One build's hand-offs, end to end

| # | Hop | Payload | Type | Checker | Record | Latency |
|---|---|---|---|---|---|---|
| 1 | owner → intake | the prompt, verbatim and redacted | hook-written entry keyed by session and content | prompt-submit hook, secret scanner (flow-steps [entry] `entry.intake`) | intake log | immediate |
| 2 | session start → orientation scout → driver | the composed card | card cells keyed, trusted while keys recompute (orientation [trust]) | `placement.check` on the disposition (flow-steps `entry.place`) | card: remote ref is the truth, clone cache, terminal snapshot (orientation [Adopted]) | at session start |
| 3 | driver → prompt writer | the resolved work order: item, acceptance, inputs as keyed content, allowance, return template (flow-roles [cycle] 2) | level-6 work order; each fact keyed and classed `witnessed`, `decided` or `claimed` by the executor (layer-roles [trust] 2) | render budget refusal (v2 [principles] P27); keys recomputed at act launch (P29) | `gov:handoff` marker, planned to gain `item=` (memory-plan [sites]) | same act |
| 4 | prompt writer → executor | the task prompt, "a record of its own" (flow-roles [cycle] 3) | **prose framing**, hashed into the spawn marker | **none named.** R3-E's rule "points at handed facts by anchor" (layer-roles [more]) has no check; grep for "framing" finds no check | the handoff file | same act |
| 5 | executor → role | the framing wrapped in the work order, plus the static block (`role-sha`) | system prompt (level 5) plus work order (level 6) | spawn guard; role-sha comparison; answered-call hook (layer-roles [trust] 10) | spawn marker; act binding (layer-runtime [act]) | same act |
| 6 | role → driver | filled return template, closed outcome set | schema-forced channel (`--json-schema` or `StructuredOutput`) | SubagentStop validation; `roles.retries` (layer-runtime [spawn]) | return record keyed by item, task-sha and spawn site; `answers` edge planned (memory-plan [edges]) | at agent stop |
| 7 | return → witness | the item's witness | computed, never typed (P2; flow-steps [rules]) | executor/command | per item, e.g. acceptance record, scope report | before any dependent item starts (P24) |
| 8 | item → next item | records the next work order hands on; "returns hand forward" their keys (layer-roles [trust] 9) | handed facts, upstream judgments classed `claimed` | **the receiver is never required to dispose of them** (see section 2) | trail records | next item |
| 9 | step → step | transition record, card re-rendered (`card.follows`), mailbox disposed | transition three ways | exit item over the reached witnesses | transition log | at transition |
| 10 | driver ↔ another build or a session without the lease | mailbox message: id, sender, recipient, kind, refs, body, `answers` (coordination [design] 6) | closed set of kinds | schema check on write; a transition is refused while a message is undisposed | `refs/gov/mail/<slug>`, copied into the folder at close | read at each item boundary (`mailbox.reads`, flow-roles FR-8) |
| 11 | node ↔ node | claims, leases (epoch, beat), card ref, binding records, bar-red, class-claims | refs moved by compare-and-swap | lease epoch fencing (layer-runtime [supervise]) | `refs/gov/*` | leases at transitions and pass commits; card at transitions; bindings per act |

How a running act hears news: an act session makes exactly one call (layer-runtime [act]), so a message reaches it only at the next item boundary. The worst-case latency is therefore one item's duration.

## 2. What items and steps commit to, and how the next one receives it

Probe: I parsed the role items in flow-steps' item tables (the `edges.py` script, run on the archive copy). Result: 22 role items. Five of them already answer every upstream item through a computed one-to-one join:

- `review.refute`: "every finding has one verdict" (flow-steps:473)
- `review.report` (:474)
- `review.fold` (:476)
- `test.attribute`: "every such red has one judgment" (:289)
- `design.inventory` (:178)

The command item `build.distill` joins forks to decision-log rows the same way (:234).

The edges that carry commitments but are answered as prose, or not at all:

| Edge | What step N commits to | How N+1 receives it |
|---|---|---|
| `plan.record` → `design.decompose` | acceptance observations, the cut-line, the parents' interfaces | handed as content; the architect's witness is a schema check plus a fork join (:180) |
| `design.seams` → `design.decompose` | seams with their probe digests | handed; no row per seam (flow-roles [steps] Design 2–3) |
| `design.decompose` → `design.unit-spec` | interfaces, seams, overlaps | overlaps are acknowledged (row-like, :183); seams are answered only by the spec's one reuse-audit token, which is prose (gap-register gap-design-05) |
| `design.unit-spec` → `build.unit-pass` | S-items, acceptance criteria, seams, bug classes | criteria are re-run by the executor (`build.acceptance`, computed, which is better than rows); seams only through the reuse line, `proposed <tag>` or `none` with a closed reason (:229); S-items and bug classes get no rows |
| build → `review.lens` (the measured edge) | spec criteria and MUST seams | **the work order carries "the build's range" only** (flow-roles [steps] Build 8; `review.pin` pins "the commit range", :471); the witness joins findings to cited lines, not to commitments (:472) |
| research → asking item | candidates and a recommendation | research record; returns name their handoff in prose in 58 of 88 research records (memory-plan [edges] `answers`) |

Probe: grep for P7's verdict vocabulary over all 154 records at `e1a54ac67`. The only hits for `bypassed` are about `hooks.bypass` (foundations:345, ownership:82). The `{item, used|bypassed|not-applicable, why}` contract appears nowhere in the design.

## 3. Session to session, on one build

- **Resume and compaction.** Every SessionStart source binds the session and re-renders the card file from the remote ref (orientation [Adopted]; layer-runtime [sessions]). A PreCompact hook flushes the item in flight. The keep-list holds the card's pointers, the build, the item and the open asks. The compaction summary is read as a lead, never a source (v2 [chain] dKeptSession). The owner's session starts fresh at an item boundary past 60% (`context.on-full`, `context.threshold`). The `gap-orient-12` resume misses (7 of 14) are owed a diagnosis first (layer-runtime [sessions]).
- **What a fresh session learns:**
  - its position, from `next` over witnesses (P22);
  - "the latest records by tag, the open forks and the item in flight", from `card.pointers` (v2 dKeptSession).
  - Decisions: fork records as they are written. Decision-log rows arrive only at `build.distill`, after Build, and only for major forks (flow-steps :234).
  - Problems: repair asks (layer-roles [trust] 7), route-back counts in the transition record, and owner items. The journal stays on its node (v2:1094: "another node cannot see a node's journal").
- **Two sessions on different units of one build.** The design does not support two drivers. `continue` is refused while another session's lease holds (orientation [placement] "Checked"; OR-6). Units run in parallel inside one driver (`build.unit-pass`; FR-5 commit queue). A second session reaches the build only through an `intake` message, read at the holder's next item boundary (flow-roles FR-8; flow-steps `entry.place`, "amend → … an `intake` message to the session holding the build").
  - **Ambiguous:** unit leases carry host and session fields (coordination [design] 1), which suggests units could have different holders, yet no item lets a session that is not the holder take one.
- **Hand-off to another session (`gov-session`).**
  - Today it writes a one-way prose prompt file. It "returns nothing to the sender", and the receiver must re-verify (`tools/roles/agents/gov-session.agent.md:8-19`).
  - The design folds it into the prompt writer (v2 [chain] dBoundRoles; fates:82). See contradiction 2 below.

## 4. Node to node

**What propagates, and how late:**

- Claims: created once by compare-and-swap (`entry.claim`).
- Leases: renewed at transitions and pass commits, expiring after 24 h (`leases.expiry-hours`). A dead node's build therefore waits up to 24 h before another node may take it over.
- Mailbox: one compare-and-swap append per message, one ref fetch per item boundary (session-model H9).
- Card ref: compare-and-swap at every transition (orientation [Adopted]).
- Act bindings: pushed per act (memory-plan [families]).
- Transcripts and journal: stay on their node and render `not-local` elsewhere (P35).

Today only `refs/gov/runs` exists:
- `git ls-remote origin 'refs/gov/*'` → `17 refs/gov/runs`
- `git grep 'refs/gov/mail\|refs/gov/leases\|refs/gov/cards\|refs/gov/bindings' -- tools skills` → no output.

**Failure modes the records handle:**
- offline work: `leases.offline: warn` queues the write and yields on conflict;
- take-over: epoch fencing, which is safe under clock skew (layer-runtime [supervise]);
- pruning: messages are copied into the folder before the ref is pruned (flow-steps [rules]).

**Failure modes they leave open:** the build-branch push (contradiction 8), and per-item card pointers that may never leave the node (contradiction 10).

## 5. Gaps and contradictions

1. **Stale wording on inputs.** v2 [chain] dBoundRoles says "its inputs as record fields at their SHAs", and roles [model] says the same. layer-roles [trust] 1 explicitly amends that to "Handed, not referenced", and the same v2 row later says "inputs handed as content". The handed facts for this question quote the stale form.
2. **`gov-session` folds into the prompt writer** (v2; fates:82). But the prompt writer "acts in no item" and is a cycle role (layer-roles [matrix]). Its real successors are the `intake` message plus the saved card. No record says so.
3. **The mailbox's closed set is not one list.**
   - coordination [design] 6 declares nine kinds and says "a new kind is a change to the loop kit".
   - `intake` is added at flow-roles:250, and `withdrawn` and `superseded` are posted at flow-steps:571. None of them is in that list, and v2 enumerates no kinds.
   - No kind carries completed work, a decision or a problem.
4. **Unreachability.** flow-interactions FI-6's settlement (:131-134) says "no reply within a bound means unreachable" and that the mailbox is read "at each transition". That contradicts coordination [interpretations] 1 (no timeout: the lease decides), which the owner confirmed (v2 [open], RC-5), and FR-8 (every item). flow-interactions is not marked superseded.
5. **Mailbox owner.** ownership:114 and :507 say dDeclaredLoop. v2's NP-24 revision (:505-507) and layer-memory:435 say dKeptSession.
6. **The verifier's packet.** layer-roles [trust] 6 says it holds "the artifact, the criterion and the claim". flow-roles [steps] Build 8 hands the closing review the range only, with no criterion.
7. **No P7 rows at any edge.** 0 hits, as above. The measured build → review edge is among the edges without them.
8. **Take-over assumes pushed witnesses.** "A take-over on any node reads the same witnesses" (layer-runtime [supervise]). No item or rule pushes the build branch before Test or landing; grep for any branch-push rule finds none. The `fencing` fixture implies act pushes ("its commit and push are each refused", layer-runtime [tests]) but declares no cadence. **Ambiguous.**
9. **The return store's home is unstated** ("writer item not named", layer-memory:437; ownership:508). memory-plan puts research returns in the tracked trail family. Whether other returns are committed and pushed is ambiguous.
10. **Card granularity.** The remote card is written per transition, but `card.pointers` updates every item with no store named. Another node may therefore see a card that is only current to the step.
11. **The prompt writer's prose framing has no checker** (hop 4).
12. **Live delivery cannot reach an act.** It reaches only an owner's Claude session. Codex has no inbox, and "only a model sends to another session's inbox" (memory-plan [sessions]).

## 6. Candidates for one handoff system

| | Mechanism | Smallest losing test | Result against the records |
|---|---|---|---|
| **A. As designed** | Five carriers joined by keys: work order and return, records plus `next`, card plus pointers, mailbox, refs | Does the closing reviewer's work order carry the specs' MUST seams and criteria as rows its return must answer, with the completeness computed? | **Loses.** It carries the range only (flow-roles Build 8; flow-steps :471-472); 0 rows anywhere. It also fails node take-over visibility (contradiction 8). |
| **B. Mailbox as the bus** | Every return, decision and problem posted to `refs/gov/mail/<slug>`; sessions and nodes read it | Does a `done` or `decided` message carry anything a witness does not already hold, without becoming a typed second copy of state? | **Loses.** `next` already derives done-ness from witnesses (P22). Mailbox entries are trusted only by key (orientation [trust]), so a message can only equal its witness or go stale. Its own risk note says mailbox writes "ride transitions and passes only" (coordination [design] Risks), so posting per return breaks its cost bound. One compare-and-swap ref per build would also serialise parallel acts. This matches the owner's "not a long-term solution". |
| **C. Commitment rows on the record graph** | Described below | Four tests, below | **Passes the four tests on the records**; its node clause is a change the records do not hold yet. |
| **D. Shared external store** (relational or cloud database) | All sessions and nodes write rows to one service | Does the core keep working offline and on a git-only adopter? | **Loses as the core contract.** It breaks P3 (local-first) and `leases.offline`, and P28 (the core depends on no expansion). It survives only as a transport adapter in the integrations expansion. Its ranking belongs to point 3's research. |
| **E. Live session inboxes as primary** | `SendMessage` between sessions | Can it reach a headless act, a Codex session or another node? | **Loses.** It is Claude-only and model-sent (memory-plan [sessions]), and an act makes one call (layer-runtime [act]). It stays as `deps.messaging`'s live channel. |

**Candidate C's mechanism.**
- Every role return declares what it establishes: seams, criteria, interfaces, resolved forks, findings and repairs.
- Every downstream work order hands those as `claimed` rows.
- Every downstream return answers each row with `{item, used|bypassed|not-applicable, why}`.
- At SubagentStop the executor computes the one-to-one join. A missing row is a failing value and is retried under `roles.retries`. A `bypassed` row becomes a finding and routes.
- Rows persist in the return record with `answers` and `caused-by` edges.
- The commit queue pushes the build branch, returns included, at each witnessed item.
- The mailbox keeps only traffic that crosses a lease: `confirm-request`, `changed`, `landed`, `intake`, and so on. Its messages take the same row shape.

**Candidate C's four losing tests:**

1. **Is there a seam to extend?** Yes: the five computed joins above, `build.distill`, and P29's `claimed` class with "returns hand forward". **Pass.**
2. **Does it break `roles.verifier-context: cold`?** The cold packet allows "the criterion and the claim" and forbids only the author's reasoning (layer-roles [trust] 6). Commitments are criteria. **Pass,** once flow-roles Build 8 is amended.
3. **Does it break P2?** A row's verdict is agent-typed, so it is held as `claimed`. The witness is the computed join, and state never rests on a `claimed` fact (P29, "guides; never decides"). **Pass.**
4. **Does it fix node visibility?** Only through its push clause, which no record holds yet. The test the build must run: node A commits 3 of 5 units and dies; node B takes over after expiry; B's `next` names unit 4, and B's closing reviewer receives the seam rows of units 1–3.

## 7. Pick, and what it leaves open

**Pick: C.** It extends seams the records already hold rather than building a new one. It turns the measured gain (aScoutedSeam P7, 13 → 20 of 23 on the diff check) into the default at every edge. It gives "completed work, decisions, problems" one shape: rows and records whose cause is named. And it narrows the mailbox to the job only it can do.

It leaves these open, each a fork for the owner:

- **Edges beyond the two measured ones are TRANSFER** (aScoutedSeam §4 and §7). Each needs that record's §5 measurement before it is relied on.
- **Push cadence** (every item, every pass commit, or every transition) trades a network round trip against how late other nodes learn of work.
- **Whether two sessions or nodes may drive different units of one build.** Today it is one lease holder; the unit-lease fields are ambiguous.
- **The row budget** under P27 and `memory.item-budget`.
- **A checker for the prompt writer's framing.**
- **Mid-item interrupts to a running act**, whose latency today is the item's whole duration.
- **Whether a database transport sits behind the rows** is point 3's question.

**Sources:**
- aScoutedSeam's principles: `git show origin/main:memory/builds/aScoutedSeam/build/2026-10-19-build-TOOL-aScoutedSeam-3-3-agent-prompt-principles.md`, P7 and §4.
- Today's handoff marker: `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\roles\handoff.py:420-421`. It carries no `item=` or `answers`.
