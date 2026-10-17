# Layer review: the roles layer

**Serves:** research PLAY-dClosedLoop-1

The third round of the owner's layer-by-layer review. It sets the owner's roles layer against the
design the earlier rounds settled:
- the roles round (`build/2026-10-14-build-PLAY-dClosedLoop-1-roles.md`): its roster, item map,
  exchange, guard and trust;
- the orientation round's `[trust]` (`build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md`);
- the item cycle (`build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md`, `[cycle]`);
- the step definitions (`build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`);
- the instruction layer's tags, grammar and views
  (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md`, R-A to R-E).

What role agents receive and do today is measured by the main loop's instruments, recorded in
`[instrument]`. No researcher was dispatched. The four roles researchers and five orientation
researchers of 2026-10-14 cover the field, and their records are cited where used.

## [words] The owner's words, 2026-10-15

> We will revisit Layer 2's relations to other layers later. Let's review the Roles layer next:
> [3. Roles Layer]
>
> * A set of pre-defined roles for agents to assume when executing tasks at Layer 2.
> * Each role comes with a permanent role instructions block from Layer 1 which instructs the role on
>   what it does, its functions and constraints, and a flexible session-oriented prompt block that
>   explains an immediate task to the role.
> * Each role must have a clearly described relation and function to each of the Layer 2 steps.
> * Roles use role-specific tags to be pointed at relevant instructions across other layers.
> * Roles need a 'trust mechanism' between them - a definition where data received by a role-assuming
>   agent is trusted and immediate used instead of re-verified. An issue with the current role
>   implementation - agents using roles re-orient in their tasks, calling multitudes of tools not
>   necessarily relevant to the task at hand, even if the parent session or another agent had
>   previously oriented in the relevant data.
> * What other architectural and structural implementations would improve this layer's function?

## [settled] What the design already fixes

- **The roster** (roles round, RL-1 to RL-8) has fourteen roles:
  - the orientation scout and the prompt writer;
  - the planner, researcher, reuse scout, architect, spec writer and builder;
  - the tester, deployer and maintainer;
  - one reviewer with a lens per step, the skeptic and the synthesizer.

  The main session is the driver and never a worker. The executor drives when no one attends.
- **The two blocks** (`[model]`):
  - A role's static instructions are its system prompt, rendered from the roles kit at level 5 and
    keyed by `role-sha`.
  - A task is a work order rendered from its item at level 6. It is hashed into the spawn marker and
    bound to its act by the act's task-sha and the session's binding record (Runtime), since a
    headless act has no subagent agent id.
- **The item cycle** (flow-roles `[cycle]`):
  1. `next` names the item and its actor.
  2. The driver hands the prompt writer the item's resolved work order: its inputs as keyed content,
     and references only for optional depth (flow-roles `[cycle]`, as the fold amended it).
  3. The executor wraps the prompt in the work order and spawns a fresh agent.
  4. The role returns a filled template through a schema-forced channel.
  5. The driver resolves the witness.

  A role carries nothing from one item to the next.
- **Exchange** (`[exchange]`): workers never message each other. Every exchange is a typed record the
  driver routes.
- **Exclusivity** (`[guard]`) holds by construction, at the tool call, at the return and after the
  fact.
- **Why the driver trusts a worker** (`[trust]`): because it is constrained and checked, not because
  it is believed.
- **Why a session trusts a claim** (orientation `[trust]`): by key and source. A session acts on a
  claim only while its key recomputes equal and its weakest source is not actor-typed.
- **Tags** (layer-instruction R-A, R-B, R-C, R-E):
  - one namespaced tag system, with `role` among its namespaces;
  - a role's static instructions and a work order are each assembled from units by their tags;
  - protocols and templates are views sliced by tag;
  - R-C's render refuses a set over budget, and a set missing a unit it requires.
- **The layers** (P28): the deployer's and the maintainer's items live in the integrations and
  observability expansions, and core Deploy has no role (step definitions).

## [current] What a role agent receives and does, measured 2026-10-15

**What it receives.** The prefix records of four of this session's researcher spawns (the
`.prefix.json` beside each transcript) show:
- a system prompt of 5,872 characters, most of it the rendered agent file;
- a user-context block of 1,852 to 2,168 characters, and a 613-character reminder that is identical in
  all four;
- the task, of 7,478 to 9,868 characters.

No block the size of `AGENTS.md` (16,732 B) or of the auto-memory index (13,187 B) arrives:
- `omitClaudeMd: true` (`tools/roles/render_agents.py:132`) is honoured on CLI 2.1.295;
- this settles what the anatomy research recorded as "STATED only";
- the charter reaches a role only as its file's `## Charter` section;
- this holds for subagents on CLI 2.1.295, the only version measured. Act sessions launch the node's
  resolved binary, 2.1.292 here, where no prefix record of a gov role exists, and an act session
  reads `CLAUDE.md` itself (the instruction layer's `gap-rt-12`).

**What its static block tells it to do.** The nine role files (45,213 B) send agents back to their
sources:
- **Pointers:** 9 of 9 carry `### Protocols — read the one whose trigger holds`, each a pointer to a
  whole document.
- **Re-verification:** four places order it, cited at their sources:
  - `tools/roles/agents/gov-spec-writer.agent.md:30`: "Verify every claim about current code by
    reading that code";
  - `tools/roles/agents/gov-researcher.agent.md:33`: "Verify every claim about current code by
    reading the code";
  - `tools/roles/agents/gov-session.agent.md:18`: a sender's records are "background to re-verify";
  - `memory/TEMPLATE-SPEC.md:106`, rendered from `tools/memory-tree/SPEC-TEMPLATE.template.md:106`:
    "Verify every claim about existing code against source at writing time".
- **Whole reads:** `tools/roles/agents/gov-builder.agent.md:19` says "Read the spec whole before you
  touch code, and the brief your task names".

The skeptic (`gov-skeptic.md:19`) and the diff reviewer (`gov-diff-reviewer.md:20`) also read the
cited source. That is their job, and it stays.

**What it does.** Every agent on this node spawned as a gov role was measured, directly or by a
workflow. That is 171 transcripts, 9,980 calls and 8,771 file reads. A workflow's generic subagents
are left out, because their role cannot be read from their prompts. Calls are classed by the
orientation-cost research's P5 classes:

| role | n | briefed | calls med/p90 | state % | locate % | method % | orient bytes % | prefix med | parent-had % of reads | re-read % of reads | identical re-reads | own-prompt reads |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gov-builder | 29 | 0 | 97 / 232 | 4.9 | 4.8 | 4.3 | 18.5 | 1 | n/a | 64.9 | 1 | 0 |
| gov-diff-reviewer | 5 | 0 | 48 / 89 | 1.5 | 0.4 | 0.4 | 1.5 | 0 | n/a | 59.4 | 0 | 0 |
| gov-researcher | 21 | 21 | 31 / 51 | 1.0 | 12.1 | 19.7 | 30.2 | 1 | 25.8 | 48.1 | 0 | 0 |
| gov-skeptic | 24 | 0 | 16 / 25 | 0.5 | 3.8 | 4.5 | 5.7 | 0 | n/a | 52.6 | 0 | 0 |
| gov-spec-reviewer | 20 | 0 | 55.5 / 111 | 0.2 | 4.5 | 3.1 | 7.2 | 1 | n/a | 58.7 | 0 | 0 |
| gov-spec-writer | 67 | 40 | 45 / 138 | 2.0 | 2.3 | 6.7 | 20.2 | 0 | 46.8 | 63.9 | 4 | 17 |
| gov-synthesizer | 5 | 0 | 5 / 7 | 0.0 | 3.7 | 25.9 | 8.7 | 1 | n/a | 33.3 | 0 | 0 |
| ALL | 171 | 61 | 42 / 119 | 2.5 | 4.0 | 6.2 | 16.9 | 1 | 42.0 | 60.9 | 5 | 17 |
| ALL direct | 61 | 61 | 44 / 126 | 1.6 | 3.9 | 7.6 | 17.3 | 0 | 42.0 | 60.5 | 4 | 17 |
| ALL workflow | 110 | 0 | 41 / 114 | 3.1 | 4.1 | 5.3 | 16.7 | 1 | n/a | 61.2 | 1 | 0 |

- **Orientation:** about one call in eight orients.
  - By class: 2.5% of calls are state, 4.0% locate and 6.2% method.
  - Their results are 16.9% of the bytes role agents take in.
  - Researchers lead, at 32.8% of their calls and 30.2% of their bytes.
- **Timing:** orientation is spread through the work, not front-loaded. The median role agent's first
  content call is its first or second call.
- **Parent's reads:** 42.0% of the files a directly spawned role agent read, its parent had already
  read before the dispatch. That is 46.8% for spec writers and 25.8% for researchers.
- **The parent's reads its agents read again most:**

  | File | Reads |
  |---|---|
  | `tools/govkit/govkit.py` | 320 |
  | `tools/govkit/selftest.py` | 118 |
  | `tools/run-gates/run-gates.sh` | 94 |
  | `tools/memory-tree/check-memory-hygiene.sh` | 82 |
  | `tools/gate-legs.json` | 75 |
  | `memory/TEMPLATE-SPEC.md` | 68 |
- **Method-class reads** go to whole documents: 811 file reads, from about 619 method-class calls
  (6.2% of 9,980), as `ro_top.py` counts them:

  | Document | Calls |
  |---|---|
  | `memory/TEMPLATE-SPEC.md` | 131 |
  | `memory/guides/BUILD-METHOD.md` | 130 |
  | `memory/guides/SESSION-KICKOFF.md` | 59 |
  | `memory/HYGIENE.md` | 43 |
  | `AGENTS.md` | 17 |
- **Own prompt:** spec writers read their own handoff prompt file 17 times.
- **Repeats inside one agent:** re-reading within one agent is not the cost. Only 5 reads repeat an
  identical path and range, or an identical command. The 60.9% re-read share counts files an agent
  came back to, mostly read in chunks or after a grep.

**Caveats:**
- A call's class comes from the paths and commands it names, never from why it was made.
- A method-class call can be the task's subject, as when a researcher audits the guides.
- Parent-had counts a file once the parent read any part of it. It is an upper bound on the reads a
  handed packet could have saved.
- Parent-had covers direct spawns only. A workflow's role agents have no parent transcript to compare.
- Bash reads are found by regex: `cat`, `head`, `tail`, `sed`, `wc`, `grep` or `awk` naming a file.

**What earlier research found.** The orientation-cost research
(`build/2026-10-14-build-PLAY-dClosedLoop-1-research-orientation-cost.md`) found two things:
- A briefed role agent spends 15.1% of its calls on method documents and 14.9% on locating (n=34).
- Pushing the card into the context did not stop re-derivation while the kickoff's first step still
  ordered it. Its candidate A lost: sessions with the card made 8 state calls, sessions without it 3.

**The lesson for this layer.** An agent uses handed content only when two things hold:
- no instruction orders the content re-derived;
- nothing lets the re-derivation through.

## [fit] The owner's layer against the design

| The owner's point | Where the design has it | What this round adds |
|---|---|---|
| Pre-defined roles for the flow's tasks | the settled roster | the roster sorted into core and expansion roles (`[roster]`) |
| A permanent role block from Layer 1, and a flexible session-oriented task block | `[model]`: the static block at level 5, the work order at level 6 | the static block holds only what holds for all of the role's items; the task block carries the session's orientation for the item as handed content (`[trust]`, `[tags]`) |
| Each role's relation to each step | the roles round's item map, superseded by the step definitions' Actor cells | the matrix, derived from the item declarations and checked both ways (`[matrix]`) |
| Role tags pointing at instructions across layers | R-B's `role` namespace; R-A assembles both blocks by tag | a trigger the item already decides is resolved at render and its slice carried; only a trigger that depends on what the role finds stays a pointer, to a slice (`[tags]`) |
| Trust between roles | the driver trusts workers (`[trust]`); sessions trust keyed claims (orientation `[trust]`) | the missing half: what a worker trusts in what it is handed, and the mechanism that stops it re-deriving (`[trust]`) |
| Other improvements | — | R3-A to R3-H (`[more]`) |

## [trust] The trust mechanism, as proposed

The settled design trusts in one direction: the driver trusts a worker's return because it is checked.
The owner's point is the other direction: a worker must trust what it is handed, or it re-derives it.

Today three things stand in the way:
- nothing says what a worker may act on;
- two role files order re-verification;
- work orders hand references, not content.

The proposal makes trust a property of the handed fact, assigned by the dispatch. Verification
becomes a property of a role's job.

**The rule, proposed as P29: a role acts on what its work order hands it, and verifies only what its
job is to verify.**

1. **Handed, not referenced.** Before the spawn, the executor resolves every input of the work order
   into content:
   - record fields;
   - code and document excerpts, cut at their anchors;
   - the card's slice for the item;
   - the method slices whose triggers the item decides.

   A reference stays only for depth the role may not need, and is marked optional. This amends the
   spawn in `[cycle]`, where the executor wraps the prompt in the work order, and dBoundRoles'
   "inputs as record fields at their SHAs".

   It extends `tools/roles/handoff.py render`, which already resolves each role's declared `reads`
   (`task:`, `card:`, `brief:`, `input:`) into the task block verbatim, and hashes the Role and Task
   sections into the spawn marker. The card's slice is handed today. New are the excerpts cut at their
   anchors, the method slices, and every fact's key and class.

   Two failures have routes:
   - **Over budget:** the render demotes the optional inputs to references first. Still over, the item
     routes back to the item that produced its largest input, as a divergence: a unit too big for its
     builder's packet returns to the architect for a split. The route counts against
     `flow.route-backs`.
   - **A vanished anchor:** a fact whose file was renamed, deleted or rewritten is found again by its
     key's blob in history. Not found, it is handed as missing, and the role works without it on
     record.
2. **Every handed fact carries its key and its class.** The key names what the fact was derived from:
   - a blob SHA and a line range;
   - a record id at its SHA;
   - or a command and the digest of its output.

   The class is one of three:
   - `witnessed`: cut or computed by a command or a hook;
   - `decided`: the owner's words, a ratified record or the policy file;
   - `claimed`: an upstream role's judgment, such as a seam's fit, a statement in a spec, or a
     finding.

   The executor writes keys and classes, and no agent types one. This is the witness rule, applied to
   inputs.
3. **Fresh at act launch, by construction.** The supervisor recomputes every key when it cuts the
   work order at act launch, and re-cuts any fact whose key moved. Attended, the driver cuts it
   through the same renderer. A role never checks freshness. This moves the orientation `[trust]`
   check from the agent to the dispatch.
   - **After the cut.** Inside the act the harness spawns without a shell, so a fact can move between
     the cut and the spawn: the commit queue in a shared worktree, or a fan's later stage. The
     answered-call hook compares each read's blob SHA with the handed key at the call (10), so a moved
     fact is read fresh, never refused. A staged fan's later stage is cut from the earlier stage's
     keyed returns.
   - **A claimed fact** is keyed by the sources it was judged from. When one of them moves, the fact is
     not re-cut, since no command can recompute a judgment. It is handed as evidence, marked stale,
     with the source that moved, and its producer re-judges it only when an item routes it back.
4. **Acting on it is the default.** A producing role uses each handed fact as given:
   - it cites a handed excerpt by its key, as verified;
   - it reads beyond its packet only for what its own work produces from: the code it changes, or the
     question it researches.

   The rule replaces "Verify every claim about current code by reading that code". A claim about code
   counts as verified when this item read the code, or was handed it with its key.

   `roles.trust` sets which facts a role acts on. F3-1 settled it as `keyed`: every keyed fact.
   `witnessed-only` makes every role re-check an upstream role's claim.

   **A claimed fact guides; it never decides** (the owner's LR-2). A role works from a `claimed`
   fact, but nothing that changes state rests on one without P23's re-derivation: a verdict, a
   position, a landing or a gate. P23 governs decisions, and P29 governs inputs.
5. **Verification is a job, not a habit.** Only verifying roles re-check what they are handed, and
   only their subject:
   - the reviewer checks the pinned artifact through its lens;
   - the skeptic checks each finding against its cited source;
   - the tester attributes each red of the verdict.

   The executor's re-run of the acceptance commands is the same idea, done by a command. Each role's
   definition declares the input classes it verifies, its trust profile, and the render puts the
   profile in its static block.
6. **Verifiers start cold.** A verifier's packet holds the artifact, the criterion and the claim. It
   never holds the author's reasoning, because a verifier's independence is what it produces. This is
   `roles.verifier-context`, settled by F3-3 as `cold`. F3-3 named the reviewer and the skeptic; the
   key covers every verifier of item 5, so the tester starts cold too.
7. **A false handed fact is repaired and recorded.** A producing role that finds a handed fact false
   works from the corrected fact and finishes:
   - its return records the repair: the fact as handed, the fact as found, and the key of what it
     read;
   - the driver files the repair as an ask against the producer's record;
   - until that record is fixed, work orders hand the repaired fact, keyed to the repairing return.

   The boundaries:
   - **Mandate:** a repair stays inside the role's mandate. A false fact whose repair would change
     what the role was asked to produce is a divergence. It routes back as a builder's `diverged`
     does today.
   - **Records:** a repair changes no record but the role's own return. A built spec stays frozen
     (P19).
   - **Where the repair lives:** in its repair ask, keyed by the sources the repairing role read,
     never by its immutable return. So it goes stale like any claimed fact when those sources move
     (3). While the ask is open, the cut hands the repaired fact in place of the original.
   - **When it ends:** when the producer's record is fixed. For a frozen built spec that is a new unit
     (P19), and the repair holds until that unit is built and its spec supersedes the fact.
   - **Two repairs of one fact:** the first filed holds. A second that differs is a contradiction
     between roles, and routes to the producer as a divergence, its ask carrying both.

   This is `roles.on-contradiction`. F3-4 settled it as `repair-and-record`. The other values:
   - `return` stops with `contradicted` instead;
   - `ask` parks the item for the owner.
8. **Orientation happens once.** The orientation scout re-verifies recall at entry, once: memory, prior
   records and the card. It keys what it finds, and everything after it trusts the keys. The charter's
   `[memory]` rule holds: recall is re-verified, at one boundary instead of by every role.
9. **Returns hand forward.** A return carries the keys of what its role relied on and what it
   established, such as files read at their SHAs and probes with their digests. The next work order
   hands them on, so trust compounds along the chain instead of each role re-deriving.
10. **Enforced at the call.** A PreToolUse hook compares each call with the work order. It finds the
    work order through the act's task-sha and the session's binding record, or, for an in-session
    spawn, the handoff's marker. An answered call is one whose answer the work order already holds:
    - a read of a handed range at the same blob SHA. A read is any call that returns a file's content:
      Read, Grep returning content, and the shell readers the hook parses. A read that only partly
      overlaps a handed range is not answered, and runs;
    - a state or locate call whose answer is handed and still holds: HEAD, the branch, the base, the
      build's position. The hook recomputes the handed value at the call, so once the role's own commit
      or a parallel pass moves it, the call runs;
    - a whole method document whose slice is handed.

    Below CLI 2.1.295, a rule on an ungated tool, Read among them, stays open when its hook fails
    (Runtime `[enforce]`, RT-2). There the rule holds while its hook runs, and a failure is recorded.

    `roles.answered-calls` decides what happens to one: refuse it and name the anchor of the handed
    answer, warn, or record. F3-2 settled it as `refuse`. A verifier's read of its subject is never an
    answered call, and neither is a read the packet does not cover.
11. **Measured.** Every role agent's calls are classed, per role and item, into the value ledger, beside
    the orientation cost `orient.budget` already records. The answered calls come from the hook's own
    records, and the other classes from runlog's extractor (R3-F). The Loop Review reads the trend,
    and `[current]` is the baseline.

**Why trust holds.** A worker trusts a handed fact because the dispatch keyed it and checked the key
at the spawn, not because another agent said it. The design keeps three boundaries:
- one where recall is re-verified: the orientation scout;
- one where handed facts are made fresh: the dispatch;
- one class of roles whose job is to doubt: the verifiers.

## [tags] Role tags and the two blocks

- **One tag per role**, `role.<name>`, in R-B's `role` namespace. Every instruction unit names the
  roles it binds. A unit that names none binds the driver alone.
- **The binding extends a seam.** Today a role's front-matter `rules:` key names the charter rule tags
  it binds, rendered by `roles_lib.render_charter_blocks` and checked by `check_rule_tags` (R4). R-B's
  join widens it both ways: a unit's `role.*` scope tags and each role's `rules:` key must agree.
- **The static block** holds the units tagged for the role that hold for every item it acts in:
  - its job, and its never-list, each line paired with its enforcer;
  - its allowance ceiling;
  - its trust profile;
  - its return template, with its closed outcome set;
  - the practices it binds, by their reach;
  - the method slices every one of its items needs.

  The block is the same at every spawn. Within one act session and the platform's cache window, the
  cached prefix serves every spawn of the role after the first. Across act sessions, with another
  worktree's working directory or hours apart, the prefix is built again. R3-F measures it as
  cache-read tokens per spawn.
- **The task block** is the work order: the units tagged with the item, the handed facts, and the
  prompt writer's framing. The owner's "session-oriented" block is this one: the session's
  orientation, cut to the item and keyed.
- **Tags select; the renderer renders.**
  - A trigger the item already decides is resolved at render, and its slice is carried.
  - A trigger that depends on what the role finds stays a pointer, and it points at a slice, never a
    whole document.

  This applies R-E's "an agent reads its slice" to role agents. It answers the 811 method-class reads.
- **The pointers' source.** The whole-document pointers come from the charter's `## Protocols`
  section, which `roles_lib.CARRIED_SECTIONS` carries whole into every agent type and handoff. The
  unit that slices them re-points that machinery in the same unit: `CARRIED_SECTIONS`, `check_roles.py`
  R0 (a charter with no Protocols section), R5 and R10 (a body or overlay naming a protocol file), and
  `render_agents.py`'s self-test arm 4, which asserts the carried text.
- **Budgets both ways.** R-C's render refusals apply per role and per item. A block over its budget is
  refused, and so is a block missing a unit its items require. The static block's budget is
  `check_roles.py`'s `BODY_CEILINGS` (1,536 to 4,096 bytes per role, rule R5), one carrier. The
  block's growth raises a ceiling only by an owner-approved change to it.
- **Joins:**
  - every `role.*` tag names a declared role;
  - every declared role's static block resolves;
  - no unit reaches a role untagged.

## [matrix] Each role's relation to the steps

The relation is derived from the item declarations, never typed. Today the step definitions are the
declarations. Each Actor cell opens with one actor's kind: `command`, `executor`, `hook`, `owner`, or a
role's name, which ends at the first comma, colon or parenthesis. `role_matrix.py` (`[instrument]`,
revised 2026-10-16) reads only that opening, so prose in the cell never adds an actor, and derives the
matrix from the step definitions as folded:

| Actor | entry | plan | design | build | test | deploy | breakpoint | lifecycle |
|---|---|---|---|---|---|---|---|---|
| orientation scout | `entry.orient`, `entry.place` | — | — | — | — | — | — | — |
| planner | — | `plan.triage-judge`, `plan.record`, `plan.reason` | — | — | — | — | — | — |
| researcher | — | `plan.research` | `design.research` | — | — | — | — | — |
| reuse scout | — | — | `design.seams` | — | — | — | — | — |
| architect | — | — | `design.inventory`, `design.decompose`, `design.reason` | — | — | — | — | — |
| spec writer | — | — | `design.unit-spec` | — | — | — | `review.fold` | — |
| builder | — | — | — | `build.unit-pass` | — | — | — | — |
| tester | — | — | — | — | `test.attribute`, `test.reason` | — | — | — |
| reviewer | — | — | — | — | — | — | `review.lens` | — |
| skeptic | — | — | — | — | — | — | `review.refute` | — |
| synthesizer | — | — | — | — | — | — | `review.report` | — |
| command | `entry.place-check`, `entry.claim` | `plan.input`, `plan.dedupe`, `plan.triage-rule`, `plan.place`, `plan.lease`, `plan.recommend`, `plan.exit` | `design.input`, `design.reentry`, `design.overlaps`, `design.recommend`, `design.ready`, `design.exit` | `build.base`, `build.unit-lease`, `build.scope`, `build.recommend`, `build.distill`, `build.exit` | `test.merge`, `test.select`, `test.verdict`, `test.route`, `test.flakes`, `test.seen-red`, `test.recommend`, `test.exit` | `deploy.current`, `deploy.mandate`, `deploy.parents`, `deploy.land`, `deploy.core`, `deploy.record`, `deploy.distill`, `deploy.recommend`, `deploy.notify`, `deploy.released`, `deploy.snapshot`, `deploy.unlease`, `deploy.close` | `review.trigger`, `review.pin`, `review.dispose`, `review.cost` | `life.notify`, `life.snapshot`, `life.unlease`, `life.close` |
| executor | — | — | — | `build.acceptance`, `build.core` | — | — | — | `life.quiesce` |
| hook | `entry.intake` | — | — | — | — | — | — | — |
| owner | `entry.place-owner` | — | — | — | — | — | — | `life.request` |

- **Counts:** 75 items, each with one actor; 15 actors; 19 items with a role.
- **The prompt writer and the driver** act in no item. The prompt writer is a cycle role: it acts in
  every role item's cycle, framing each work order (`[roster]`, flow-roles `[cycle]`). The driver
  routes and never works.
- **The check has four arms**, each a finding:
  - every body row under a step's heading is an item row the pattern reads, every item row sits
    under a step's heading, and every step holds an item, since a parser that skips what it cannot
    place reports a clean run (arm 0, added after the fold's closing review and widened after its
    follow-up round);
  - every item's actor is a command, the executor, a hook, the owner, or a declared item role;
  - every core item role acts in at least one core item;
  - no core item names an expansion role (P28).
- **Seen red:** each arm on a planted copy of the step definitions, one line changed: a misspelled
  role, a core role left with no item, an expansion role in a core item, a cycle role in an item, and
  a step's heading renamed. On the records as written it exits 0.
- **Each role's static block renders only its own row**: the items it acts in, each with its inputs and
  its return. A builder never loads the loop.
- **Built from data.** Once dDeclaredLoop's loop definition declares the items as data, the matrix is
  derived from that definition, not from this record's tables.

## [roster] Core and expansion roles

P28 sorts the settled roster. Which items each role acts in is `[matrix]`'s, derived, so the roster
names only each role's layer and how it acts:

| Role | Layer | Acts as |
|---|---|---|
| orientation scout | core | item role |
| prompt writer | core | cycle role: every role item's cycle, and no item |
| planner | core | item role |
| researcher | core | item role |
| reuse scout | core | item role |
| architect | core | item role |
| spec writer | core | item role, folds included |
| builder | core | item role |
| tester | core | item role |
| reviewer | core | item role; the maintenance-run and loop lenses arrive with observability |
| skeptic | core | item role |
| synthesizer | core | item role |
| deployer | distribution, integrations | item role: release notes, and verify judgment |
| maintainer | observability | item role: Maintain's filings |

Twelve roles are core and two belong to expansions. An expansion registers its roles and lenses
through its layer contract, and the core roster never names them. The deployer acts for two
expansions: release notes for distribution, and verify judgment for integrations.

## [more] What else would improve the layer

**R3-A. One role definition, rendered everywhere.**
- Each role is declared once, in the roles kit, with these fields:
  - its tag and its layer;
  - its job, and its never-list with each line's enforcer;
  - its allowance ceiling;
  - its model;
  - its trust profile;
  - its return template;
  - its packet budget, beside its static block's ceiling in `BODY_CEILINGS`.
- Its effort stays in the adopter-owned `tools/roles/house/policy.toml`, per role and per workflow
  stage, read by `handoff.py stage-efforts` (TOOL-aOrientedCast-10).
- Each role composes with the adopter-owned seeds the kit never rewrites: its house overlay,
  `tools/roles/house/<role>.md`, rendered as `## House rules`, and that effort policy.
- The agent files, the charter's role index, the matrix, the spawn guard's table and the return
  validator are all rendered from it.
- This extends dBoundRoles' "static instructions as structured fields" with the layer, the trust
  profile, the budget and the tags.

**R3-B. Static blocks cached, task blocks bounded.** The static block holds only what holds for all of
the role's items, so every spawn of a role within one act session and the cache window reuses the
cached prefix (`[tags]`). Anything item-specific goes in the task.

**R3-C. Separation of duties, checked.** The author of an artifact never verifies it:
- a builder never reviews its own diff;
- a spec writer never audits its own spec;
- a skeptic never sees the reviewer's reasoning, under `roles.verifier-context: cold`;
- each review round's reviewers are fresh agents.

Every item spawns a fresh agent, so an agent-id check could never fail. The breach that can happen is
in the packet: the spawn guard checks each verifier's work order against `roles.verifier-context`,
and under `cold` refuses one that carries the author's packet or reasoning. Under `warm`, the
`velocity` preset's value, the owner has chosen the faster, anchored review.

**R3-D. Fresh agents stay cheap because packets are complete.**
- The platform can continue an earlier agent with its context.
- The settled cycle instead spawns a fresh agent per item, and a role carries nothing between items.
- Continuing would make an item depend on an agent's memory, and would step around the key check at
  the spawn.
- The complete packet is what makes the fresh agent cheap. Continuing agents is not recommended.

**R3-E. The prompt writer works from a packet too.**
- It receives the driver's details and the resolved work order.
- It writes only the framing.
- It points at handed facts by anchor instead of retyping them. Today 64.5% of a task's bytes are
  retyped (gap-roles-05).

Without that packet, the prompt writer re-orients on every worker's behalf.

**R3-F. Role metrics in observability.**
- **What is measured**, per role and item:
  - calls by class, and answered calls;
  - tokens;
  - outcomes, retries and contradictions returned;
  - each lens's refutation rate.
- **Who reads it:** the Loop Review.
- **Acceptance:** two measures, over every role act, whether a subagent, a workflow agent or a
  headless session, keyed by its task-sha:
  - answered calls, from the answered-call hook's own records: each one it refused, warned or
    recorded. Under `refuse`, an attempt is counted as refused, not as zero;
  - method and locate calls below this round's baseline, classed by runlog's extractor
    (`tools/runlog/extract.py`, `derive_tool_class`), which already reads every subagent and workflow
    agent's transcript with its agent type.

  `role_orientation.py` stays this round's baseline instrument only.
- **Measured since.** The memory round's five briefed researchers show why the measure must be
  the answered call, not the path class. Their subject was memory itself, so locate and method
  reads were their content (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`,
  `[research]`). Their brief's one explicit instruction, to leave the design records alone, held:
  0 reads, against 24 before.

**R3-G. A role's version travels with its work.**
- The `role-sha` each item ran under is kept with its return. The Loop Review can then tie a change in
  a role's metrics to a change in its definition.
- Role definitions stay outside every worker's reach.
- They change only as instructions do, under `instructions.edit`.

**R3-H. The platform's own role fields.** Agent files accept `skills` and agent-scoped `hooks` (roles
anatomy research, inventory).
- The level-4 Skills a role's tags select are handed in its static block as thin entries. An agent
  file's `skills` field serves the subagent backend only, since a headless act has no agent file.
- The answered-call rule is a pack in Runtime's one dispatcher entry per event, never an agent-scoped
  hook. A guard beside the dispatcher fails open, and the anatomy research measured agent-scoped hooks
  failing open (Runtime `[enforce]`).

The rest belongs to the lower-level design.

## [gaps] Registered, 2026-10-15

Eight gaps joined the register then, all owned by dBoundRoles. `[owner-notes]` later added `gap-roles-18`.

| Gap | Severity | What it is |
|---|---|---|
| `gap-roles-10` | HIGH | role files order re-verification and declare no trust |
| `gap-roles-11` | HIGH | work orders hand references, not content |
| `gap-roles-12` | MED | role files point at whole protocol documents |
| `gap-roles-13` | MED | nothing sees or bounds an answered call |
| `gap-roles-14` | MED | the roster is not sorted by layer |
| `gap-roles-15` | MED | the role-to-step relation is typed, never derived or joined |
| `gap-roles-16` | LOW | nothing declares what a verifier receives |
| `gap-roles-17` | LOW | a false handed fact has no repair record and no route |

## [forks] Asked, 2026-10-15

**F3-1. "A role acts on what its work order hands it, keyed and checked fresh at the spawn. Which
handed facts does it act on without re-checking?"**
- Offered:
  - Every keyed fact (Recommended): command outputs, the owner's decisions and upstream roles'
    claims, such as a seam or a statement in a spec. Only the reviewer, the skeptic and the tester
    re-check, and only their subject.
  - Witnessed and decided only: command outputs and decisions are trusted, and every role re-checks
    an upstream role's claim before using it.

**F3-2. "A role agent makes a call its work order already answers. It might re-read a handed excerpt
at the same commit, ask git for the HEAD it was handed, or open a whole guide whose slice it carries.
What happens by default?"**
- Offered:
  - Refuse, naming the anchor (Recommended): the hook refuses the call and says where the answer sits
    in the task. Reads the task does not cover, and verifiers' reads of their subject, are never
    refused.
  - Warn and allow: the call runs, with a notice naming the anchor.
  - Record only: the call is counted per role in the value ledger, as orientation cost is today.

**F3-3. "What do the verifying roles, the reviewer and the skeptic, receive by default?"**
- Offered:
  - Cold: the artifact, the criterion and the claim (Recommended). Never the author's reasoning or
    packet, because a verifier's independence is what it produces.
  - Warm: they also get the author's packet and reasoning. That is faster, but anchored on the
    author's view.

**F3-4. "A role finds that a fact it was handed is false. What does it do by default?"**
- Offered:
  - Return it as its outcome (Recommended): the role stops with `contradicted` and the evidence, and
    the driver routes it to the fact's producer, as a builder's divergence goes back to Design.
  - Repair, record and continue: the role works from the corrected fact and records the repair in
    its return, and the producer's record is fixed afterwards.
  - Ask the owner: the item parks for the owner. Unattended runs follow `run.on-owner-question`.

### Settled after F3-1 to F3-4, 2026-10-15

- **F3-1:** Every keyed fact (Recommended).
  - The key is `roles.trust`. Its default is `keyed`, and `witnessed-only` is allowed.
- **F3-2:** Refuse, naming the anchor (Recommended).
  - The key is `roles.answered-calls`. Its default is `refuse`, and `warn` and `record` are allowed.
- **F3-3:** Cold (Recommended).
  - The key is `roles.verifier-context`. Its default is `cold`, and `warm` is allowed.
- **F3-4:** Repair, record, continue. This is the owner's answer, over the recommended return.
  - The key is `roles.on-contradiction`. Its default is `repair-and-record`, and `return` and `ask`
    are allowed.
  - `[trust]` is amended in place: the repair is recorded in the return and filed as an ask against
    the producer's record. Until the record is fixed, the repaired fact is handed onward, keyed to
    the repairing return.
  - A repair stays inside the role's mandate. A false fact whose repair would change what the role
    was asked to produce is still a divergence, and a built spec stays frozen (P19).

**What changed elsewhere:**
- **v2:**
  - P29 is added.
  - The four keys join the catalogue and every preset.
  - dBoundRoles' roster is sorted into twelve core roles and two expansion roles. Its units gain
    the trust mechanism, the derived matrix and role metrics.
  - `[owed]` gains the roles layer's lower-level design and, at the re-cut, the expansion roles'
    home.
- **The presets** follow each stance:
  - `velocity` warns on answered calls, sends verifiers warm, and repairs;
  - `strict` trusts only witnessed and decided facts, and returns a contradiction;
  - `guarded` returns a contradiction.
- **The register:** `gap-roles-17` now names the missing repair record and route.

## [owner-notes] Raised when round four opened, 2026-10-15

> So far, Layer 3 doesn't describe the actual MECHANICAL SHAPE of the role execution - workflows,
> agent sets, agent orientation templates. Origin branch 'deterministic-reuse-workflows-f70c33' and its
> build 'aScoutedSeam' ran an extensive reuse agent workflow test to find one important point -
> agent/workflow shape matters for improved result. Individual agents at xhigh effort produce about
> the same quality results as 2 scouts + 1 adjudicator at medium effort for fraction of the cost. How
> the actual work is shaped matters, we will revisit this point later.

**The evidence**, from aScoutedSeam's benchmark (`origin/branch/deterministic-reuse-workflows-f70c33` at `b0fe68f30`, `memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md`). Its higher effort is named `extra`.
- **Effort.** The three scout arms held their recall at `medium` for a fifth to a seventh of the cost:
  about ten minutes and 4M cache-read tokens per scout, against two hours and 28M at `extra`. The
  diff-time reviewer was the exception: its recall fell from 7 to 4 of 23.
- **Agent set.** At `medium`, a code scout and a design scout followed by a judge solved 12 of 23
  positives. One checklist scout solved the same 12, hit more items (22 against 20), and used a
  third of the agents. A five-lens fan-out with skeptics was ruled out on cost after three pilots.
- **Orientation template.** A checklist scout that first reads a generated house index, sketches the
  implementation and takes a convention census solved 16 of 24 in each of two runs, where the plain
  checklist scout solved 13.

**What it means for this layer.** Shape moved recall more than agent count did:
- the checklist and the orientation template;
- the effort per role.

Each role item therefore owes a declared execution shape: its agent set, effort, checklist,
orientation template and merge. The owner set this for a later revisit. It is recorded as
`gap-roles-18` and in v2's `[owed]`.

Three of the five parts are declared data today, and the revisit extends them:
- the agent set per workflow, with a `stages` table mapping each harness stage to a role
  (`tools/roles/workflows.toml`);
- the effort per role and per workflow stage (`tools/roles/house/policy.toml`), both served to the
  harnesses by `handoff.py harness-args` and `stage-efforts`;
- the bug-class checklist per diff (`tools/memory-tree/gotchas.py`).

The orientation template and the merge are declared nowhere. aScoutedSeam is evidence only: its branch is unmerged and no
chain build counts on its code.

## [instrument] The instruments, as run 2026-10-15

### `role_orientation.py`

It classes every role agent's calls and measures the reads its parent already had:

```python
"""Measure how much of a role agent's work re-orients, over the direct role spawns on this node.

Population: every subagent transcript under ~/.claude/projects/C--projects-coding-governance*/ whose
.meta.json agentType starts with "gov-": direct spawns under <session>/subagents/, and the role agents
a workflow spawned under <session>/subagents/workflows/<run>/. Generic workflow subagents are left out:
their prompts are free text, so their role cannot be read from them. The parent of a direct spawn is
its session transcript; a workflow's role agent has no parent transcript to read, so parent-had is
computed over direct spawns only.

Each tool call is put in one class, in this order (the classes of the orientation-cost research, P5):
- state:   a Bash git status|log|branch|worktree|rev-parse|fetch|remote|show-ref|merge-base|describe.
- locate:  a call naming LIVE.md, memory/builds/*/README.md, memory/ledger, memory/plan, BACKLOG, ASKS,
           gen_build_index, or `ls memory/builds`.
- method:  a call naming an instruction document: memory/guides/, TEMPLATE-SPEC, HYGIENE, AGENTS.md,
           CLAUDE.md, the charter template, a SKILL file, DECISIONS.md, .claude/rules/, .claude/agents/.
- content: everything else.

Flags, counted over Read calls and over files named by a Bash cat/head/tail/sed/wc/grep:
- parent-had: the parent session had read that file before it dispatched this agent.
- re-read:    this agent had already read that file (any range; reading a file in chunks counts).
- identical:  this agent had already made the identical read: the same Read path, offset and limit, or
              the same Bash command.
- own-prompt: the file is the agent's own handoff prompt (the marker's path=).

The orientation prefix is the number of calls before the agent's first content call.
Bytes are the lengths of the tool results, by the call's class.
Usage: python role_orientation.py [--session <session-id>] [--first <agent-id> ...]
"""
import collections
import glob
import json
import os
import re
import statistics
import sys

ROOT = os.path.expanduser("~/.claude/projects")
STATE = re.compile(r"^\s*(?:cd [^;&]+(?:&&|;)\s*)?git\s+(?:-C\s+\S+\s+)?(status|log|branch|worktree|rev-parse|fetch|remote|show-ref|merge-base|describe)\b")
LOCATE = re.compile(r"LIVE\.md|memory/builds/[^/\s]+/README\.md|memory/ledger|memory/plan|BACKLOG|ASKS|gen_build_index|ls\s+\S*memory/builds/?(\s|$)")
METHOD = re.compile(r"memory/guides/|TEMPLATE-SPEC|HYGIENE|AGENTS\.md|CLAUDE\.md|agents\.template\.md|SKILL(\.template)?\.md|DECISIONS\.md|\.claude/rules/|\.claude/agents/")
FILEISH = re.compile(r"[\w./\\:-]+\.(?:md|py|sh|js|toml|json|txt|conf|yml|yaml)\b")
READERS = re.compile(r"^\s*(?:cd [^;&]+(?:&&|;)\s*)?(cat|head|tail|sed|wc|grep|awk)\b")


def norm(p):
    p = p.replace("\\", "/")
    m = re.search(r"coding-governance/(?:\.claude/worktrees/[^/]+/)?(.*)$", p, re.I)
    return (m.group(1) if m else p).lstrip("./")


def text_of(content):
    if isinstance(content, str):
        return content
    out = []
    for b in content or []:
        if isinstance(b, dict):
            t = b.get("text") if b.get("type") == "text" else b.get("content")
            out.append(t if isinstance(t, str) else text_of(t) if isinstance(t, list) else "")
    return "".join(out)


def calls_of(path):
    """Ordered tool calls of one transcript: (id, name, input, result_len), plus the first user text."""
    calls, results, first = [], {}, None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            try:
                o = json.loads(line)
            except ValueError:
                continue
            msg = o.get("message") or {}
            content = msg.get("content")
            if o.get("type") == "user" and first is None:
                first = text_of(content)
            if isinstance(content, list):
                for b in content:
                    if not isinstance(b, dict):
                        continue
                    if b.get("type") == "tool_use":
                        calls.append([b.get("id"), b.get("name"), b.get("input") or {}, 0])
                    elif b.get("type") == "tool_result":
                        results[b.get("tool_use_id")] = len(text_of(b.get("content")))
    for c in calls:
        c[3] = results.get(c[0], 0)
    return calls, first or ""


def files_read(name, inp):
    if name == "Read":
        return [norm(inp.get("file_path", ""))]
    if name == "Bash" and READERS.search(inp.get("command", "")):
        return [norm(t) for t in FILEISH.findall(inp.get("command", ""))]
    return []


def klass(name, inp):
    s = json.dumps(inp).replace("\\\\", "/")
    if name == "Bash" and STATE.search(inp.get("command", "")):
        return "state"
    if LOCATE.search(s):
        return "locate"
    if METHOD.search(s):
        return "method"
    return "content"


_parents = {}


def parent_reads(session_jsonl, tool_use_id):
    """Files the parent read before the tool_use that spawned the agent; None if not found."""
    if session_jsonl not in _parents:
        seq = []
        if os.path.exists(session_jsonl):
            calls, _ = calls_of(session_jsonl)
            seq = [(c[0], c[1], c[2]) for c in calls]
        _parents[session_jsonl] = seq
    seen = set()
    for cid, name, inp in _parents[session_jsonl]:
        if cid == tool_use_id:
            return seen
        seen.update(files_read(name, inp))
    return None


def pct(a, b):
    return 100.0 * a / b if b else 0.0


def main(argv):
    only_session = argv[argv.index("--session") + 1] if "--session" in argv else None
    show = argv[argv.index("--first") + 1:] if "--first" in argv else []
    rows = []
    for meta in glob.glob(ROOT + "/C--projects-coding-governance*/*/subagents/**/agent-*.meta.json", recursive=True):
        m = json.load(open(meta, encoding="utf-8"))
        role = m.get("agentType", "")
        if not role.startswith("gov-"):
            continue
        session_dir = meta.replace(chr(92), "/").split("/subagents/")[0]
        spawn = "workflow" if "/subagents/workflows/" in meta.replace(chr(92), "/") else "direct"
        sid = os.path.basename(session_dir)
        if only_session and sid != only_session:
            continue
        aid = os.path.basename(meta)[len("agent-"):-len(".meta.json")]
        calls, first = calls_of(meta[:-len(".meta.json")] + ".jsonl")
        if not calls:
            continue
        pm = re.search(r"gov:handoff[^>]*?path=(\S+)", first)
        own = norm(pm.group(1)) if pm else None
        had = parent_reads(session_dir + ".jsonl", m.get("toolUseId")) if spawn == "direct" else None
        cls = collections.Counter()
        byt = collections.Counter()
        reads = parent_hits = rereads = own_reads = identical = 0
        mine = set()
        exact = set()
        prefix = None
        for i, (_, name, inp, rlen) in enumerate(calls):
            k = klass(name, inp)
            cls[k] += 1
            byt[k] += rlen
            if k == "content" and prefix is None:
                prefix = i
            key = json.dumps([name, inp.get("file_path"), inp.get("offset"), inp.get("limit"), inp.get("command")])
            if files_read(name, inp):
                if key in exact:
                    identical += 1
                exact.add(key)
            for f in files_read(name, inp):
                reads += 1
                if had is not None and f in had:
                    parent_hits += 1
                if f in mine:
                    rereads += 1
                if own and f == own:
                    own_reads += 1
                mine.add(f)
        rows.append(dict(role=role, spawn=spawn, aid=aid, sid=sid, n=len(calls), cls=cls, byt=byt, reads=reads,
                         parent=parent_hits, parent_known=had is not None, rereads=rereads, identical=identical,
                         own=own_reads, prefix=len(calls) if prefix is None else prefix,
                         brief=bool(pm), calls=calls))
        if aid in show:
            print(f"--- first calls of {role} {aid}")
            for _, name, inp, rlen in calls[:14]:
                arg = inp.get("file_path") or inp.get("command") or inp.get("pattern") or inp.get("url") or ""
                print(f"  {klass(name, inp):7} {name:9} {rlen:7} {norm(str(arg))[:110]}")
    if not rows:
        sys.exit("no role transcripts found")
    print("| role | n | briefed | calls med/p90 | state % | locate % | method % | orient bytes % | prefix med | parent-had % of reads | re-read % of reads | identical re-reads | own-prompt reads |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    groups = collections.defaultdict(list)
    for r in rows:
        groups[r["role"]].append(r)
        groups["ALL " + r["spawn"]].append(r)
    groups["ALL"] = rows
    for role in sorted(groups, key=lambda k: (k.startswith("ALL"), k)):
        g = groups[role]
        n = [r["n"] for r in g]
        tot = sum(n)
        c = collections.Counter()
        b = collections.Counter()
        for r in g:
            c.update(r["cls"])
            b.update(r["byt"])
        reads = sum(r["reads"] for r in g)
        known_reads = sum(r["reads"] for r in g if r["parent_known"])
        p90 = sorted(n)[max(0, -(-len(n) * 9 // 10) - 1)]
        print(f"| {role} | {len(g)} | {sum(r['brief'] for r in g)} | {statistics.median(n):g} / {p90} | "
              f"{pct(c['state'], tot):.1f} | {pct(c['locate'], tot):.1f} | {pct(c['method'], tot):.1f} | "
              f"{pct(b['state'] + b['locate'] + b['method'], sum(b.values())):.1f} | "
              f"{statistics.median(r['prefix'] for r in g):g} | "
              f"{(f"{pct(sum(r['parent'] for r in g), known_reads):.1f}" if known_reads else "n/a")} | {pct(sum(r['rereads'] for r in g), reads):.1f} | "
              f"{sum(r['identical'] for r in g)} | {sum(r['own'] for r in g)} |")
    known = sum(r["parent_known"] for r in rows)
    print(f"\nagents {len(rows)}; parent transcript found for {known}; calls {sum(r['n'] for r in rows)}; "
          f"file reads {sum(r['reads'] for r in rows)}")


if __name__ == "__main__":
    main(sys.argv[1:])
```

Run as `python role_orientation.py`, it printed:

```text
| role | n | briefed | calls med/p90 | state % | locate % | method % | orient bytes % | prefix med | parent-had % of reads | re-read % of reads | identical re-reads | own-prompt reads |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gov-builder | 29 | 0 | 97 / 232 | 4.9 | 4.8 | 4.3 | 18.5 | 1 | n/a | 64.9 | 1 | 0 |
| gov-diff-reviewer | 5 | 0 | 48 / 89 | 1.5 | 0.4 | 0.4 | 1.5 | 0 | n/a | 59.4 | 0 | 0 |
| gov-researcher | 21 | 21 | 31 / 51 | 1.0 | 12.1 | 19.7 | 30.2 | 1 | 25.8 | 48.1 | 0 | 0 |
| gov-skeptic | 24 | 0 | 16 / 25 | 0.5 | 3.8 | 4.5 | 5.7 | 0 | n/a | 52.6 | 0 | 0 |
| gov-spec-reviewer | 20 | 0 | 55.5 / 111 | 0.2 | 4.5 | 3.1 | 7.2 | 1 | n/a | 58.7 | 0 | 0 |
| gov-spec-writer | 67 | 40 | 45 / 138 | 2.0 | 2.3 | 6.7 | 20.2 | 0 | 46.8 | 63.9 | 4 | 17 |
| gov-synthesizer | 5 | 0 | 5 / 7 | 0.0 | 3.7 | 25.9 | 8.7 | 1 | n/a | 33.3 | 0 | 0 |
| ALL | 171 | 61 | 42 / 119 | 2.5 | 4.0 | 6.2 | 16.9 | 1 | 42.0 | 60.9 | 5 | 17 |
| ALL direct | 61 | 61 | 44 / 126 | 1.6 | 3.9 | 7.6 | 17.3 | 0 | 42.0 | 60.5 | 4 | 17 |
| ALL workflow | 110 | 0 | 41 / 114 | 3.1 | 4.1 | 5.3 | 16.7 | 1 | n/a | 61.2 | 1 | 0 |

agents 171; parent transcript found for 61; calls 9980; file reads 8771
```

### `ro_top.py`

It names the files behind each class, reusing `role_orientation.py`'s functions:

```python
"""Top paths behind role_orientation.py's classes: what the parent had, and what method and locate calls read."""
import collections, glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import role_orientation as ro

had_c, meth_c, loc_c, state_c = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
for meta in glob.glob(ro.ROOT + "/C--projects-coding-governance*/*/subagents/**/agent-*.meta.json", recursive=True):
    m = json.load(open(meta, encoding="utf-8"))
    if not m.get("agentType", "").startswith("gov-"):
        continue
    fwd = meta.replace(chr(92), "/")
    calls, first = ro.calls_of(meta[:-len(".meta.json")] + ".jsonl")
    had = None
    if "/subagents/workflows/" not in fwd:
        had = ro.parent_reads(fwd.split("/subagents/")[0] + ".jsonl", m.get("toolUseId"))
    for _, name, inp, _ in calls:
        k = ro.klass(name, inp)
        fs = ro.files_read(name, inp)
        for f in fs:
            if had is not None and f in had:
                had_c[f.split("/build/")[-1] if "/build/" in f else f] += 1
            if k == "method":
                meth_c[f] += 1
            if k == "locate":
                loc_c[f] += 1
        if k == "state":
            state_c[" ".join(inp.get("command", "").split()[:3])[:40]] += 1
for title, c in (("parent-had", had_c), ("method", meth_c), ("locate", loc_c), ("state", state_c)):
    print(f"## {title}: {sum(c.values())}")
    for k, n in c.most_common(10):
        print(f"  {n:4} {k[:100]}")
```

Run as `python ro_top.py`, it printed:

```text
## parent-had: 1459
   320 tools/govkit/govkit.py
   118 tools/govkit/selftest.py
    94 tools/run-gates/run-gates.sh
    82 tools/memory-tree/check-memory-hygiene.sh
    75 tools/gate-legs.json
    68 memory/TEMPLATE-SPEC.md
    56 tools/run-gates/run-gates.test.sh
    44 memory/guides/BUILD-METHOD.md
    44 memory/builds/dRedressedBar/README.md
    37 skills/session-kickoff/manifest-check.sh
## method: 811
   131 memory/TEMPLATE-SPEC.md
   130 memory/guides/BUILD-METHOD.md
    59 memory/guides/SESSION-KICKOFF.md
    43 memory/HYGIENE.md
    21 skills/session-kickoff/SKILL.md
    17 skills/session-kickoff/manifest-check.sh
    17 AGENTS.md
    16 memory/guides/REVIEW-PROTOCOL.md
    14 coding-governance-agents.template.md
    14 WIRE-INTO-PROJECT.md
## locate: 300
    87 memory/builds/dRedressedBar/README.md
    40 tools/memory-tree/gen_build_index.py
    13 memory/LIVE.md
    12 README.md
     7 skills/session-kickoff/manifest-check.sh
     5 memory/HYGIENE.md
     5 memory/guides/UNATTENDED-ASKS.md
     4 tools/memory-tree/backlog.py
     4 tools/memory-tree/check-memory-hygiene.sh
     4 memory/DECISIONS.md
## state: 250
   162 cd C:/projects/coding-governance/.claude
    17 git log --oneline
    12 git status --short
     9 git -C C:/projects/coding-governance/.cl
     5 git rev-parse HEAD
     4 git rev-parse --git-path
     4 cd "C:/projects/coding-governance/.claud
     4 cd C:/Users/d41ly/AppData/Local/Temp/r20
     3 cd /c/projects/coding-governance/.claude
     3 git log --format='%h
```

### `role_matrix.py`

It derives the actor-by-step matrix from the step definitions, and fails on an item whose actor it
cannot name:

```python
"""Derive the role-by-step matrix from the step-definitions record: every item row's Actor cell, read
for the actors it names. Prints each actor's items by step, and every item whose Actor cell names no
known actor (exit 1 if any).

Usage: python role_matrix.py <flow-steps record> [--plant]
--plant replaces the first item's actor with "nobody", to see the unmatched-item check fail.
"""
import collections
import re
import sys

ACTORS = [  # (actor, pattern over the Actor cell); order matters only for display
    ("orientation scout", r"\bscout\b(?! *\()(?<!reuse scout)"),
    ("reuse scout", r"reuse scout"),
    ("planner", r"\bplanner"),
    ("researcher", r"\bresearcher"),
    ("architect", r"\barchitect"),
    ("spec writer", r"spec writer"),
    ("builder", r"\bbuilder"),
    ("tester", r"\btester"),
    ("reviewer", r"\breviewer|\blens\b"),
    ("skeptic", r"\bskeptic"),
    ("synthesizer", r"\bsynthesizer"),
    ("deployer", r"\bdeployer"),
    ("maintainer", r"\bmaintainer"),
    ("owner", r"\bowner"),
    ("executor", r"\bexecutor"),
    ("hook", r"\bhook"),
    ("command", r"\bcommand"),
    ("driver", r"\bdriver|main session"),
]


def main(argv):
    text = open(argv[0], encoding="utf-8").read()
    if "--plant" in argv:
        text = re.sub(r"(\n\| `[a-z]+\.[a-z-]+` \| )[^|]+", r"\1nobody ", text, count=1)
    step = None
    matrix = collections.defaultdict(lambda: collections.defaultdict(list))
    unmatched = []
    for line in text.splitlines():
        h = re.match(r"^## \[([a-z]+)\]", line)
        if h:
            step = h.group(1)
            continue
        row = re.match(r"^\| `([a-z]+\.[a-z0-9-]+)[^`]*` \| ([^|]+) \|", line)
        if not row or step is None:
            continue
        item, actor = row.group(1), row.group(2).lower()
        hits = [name for name, pat in ACTORS if re.search(pat, actor)]
        if "reuse scout" in hits and "orientation scout" in hits and actor.count("scout") == 1:
            hits.remove("orientation scout")
        if not hits:
            unmatched.append(f"{step}: {item}: {actor.strip()}")
        for name in hits:
            matrix[name][step].append(item)
    steps = ["entry", "plan", "design", "build", "test", "deploy", "breakpoint"]
    print("| Actor | " + " | ".join(steps) + " |")
    print("|---|" + "---|" * len(steps))
    for name, _ in ACTORS:
        if name in matrix:
            cells = [", ".join(f"`{i}`" for i in matrix[name].get(s, [])) or "—" for s in steps]
            print(f"| {name} | " + " | ".join(cells) + " |")
    total = sum(len(v) for m in matrix.values() for v in m.values())
    print(f"\nactor-item pairs {total}; actors {len(matrix)}; unmatched items {len(unmatched)}")
    for u in unmatched:
        print("UNMATCHED", u)
    return 1 if unmatched else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

Run on `build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`, it exited 0 and printed:

```text
| Actor | entry | plan | design | build | test | deploy | breakpoint |
|---|---|---|---|---|---|---|---|
| orientation scout | `entry.orient`, `entry.place` | — | — | — | — | — | — |
| reuse scout | — | — | `design.seams` | — | — | — | — |
| planner | — | `plan.triage-judge`, `plan.record` | — | — | — | — | — |
| researcher | — | `plan.research` | `design.research` | — | — | — | — |
| architect | — | — | `design.inventory`, `design.decompose` | — | — | — | — |
| spec writer | — | — | `design.unit-spec` | — | — | — | — |
| builder | — | — | — | `build.unit-pass` | — | — | — |
| tester | — | — | — | — | `test.attribute` | — | — |
| reviewer | — | — | — | — | — | — | `review.lens` |
| skeptic | — | — | — | — | — | — | `review.refute` |
| synthesizer | — | — | — | — | — | — | `review.report` |
| executor | — | — | — | `build.unit-pass`, `build.acceptance`, `build.core` | — | — | — |
| hook | `entry.intake` | — | — | — | `test.verdict` | — | — |
| command | `entry.intake` | `plan.input`, `plan.dedupe`, `plan.triage-rule`, `plan.place`, `plan.lease`, `plan.recommend`, `plan.exit` | `design.input`, `design.reentry`, `design.overlaps`, `design.recommend`, `design.ready`, `design.exit` | `build.base`, `build.unit-lease`, `build.acceptance`, `build.scope`, `build.recommend`, `build.core`, `build.exit` | `test.merge`, `test.select`, `test.verdict`, `test.flakes`, `test.seen-red`, `test.recommend`, `test.exit` | `deploy.current`, `deploy.mandate`, `deploy.parents`, `deploy.land`, `deploy.core`, `deploy.record`, `deploy.recommend`, `deploy.close` | `review.trigger`, `review.pin`, `review.dispose`, `review.cost` |

actor-item pairs 60; actors 14; unmatched items 0
```

Run with `--plant`, it exited 1. The last lines of its output:

```text

actor-item pairs 58; actors 14; unmatched items 1
UNMATCHED entry: entry.intake: nobody
```

### `role_matrix.py`, revised 2026-10-16

The fold's revision reads each Actor cell's opening only, takes the roster from `[roster]`, and
implements all three arms. After the fold's closing review (M16), arm 0 refuses an item row under a
heading that names no step, and a step with no item. Before it, a renamed heading dropped its items
and the run still printed `findings 0`. After the follow-up round (M10), arm 0 also reads every table
body row under a step's heading as an item row, and refuses one its pattern cannot read. Before that,
the revised instrument run over a copy with `test.reason`'s tag uppercased printed
`items 71; … findings 0` and exited 0:

```python
"""Derive the role-by-step matrix from the step definitions, and check it against the roster both ways.

An Actor cell opens with its kind: `command`, `executor`, `hook`, `owner`, or a role's name, which ends
at the first comma, colon or parenthesis. Nothing after that is read, so prose never adds an actor.
The roster is the roles record's `[roster]` table: each role's layer, and whether it acts as an item
role or as a cycle role, which acts in every role item's cycle and in no item.

Four arms, each a finding (exit 1 if any):
  0. every table body row under a step's heading is an item row the item pattern reads, every item
     row sits under a step's heading, and every step holds at least one item, since a parser that
     skips what it cannot place reports a clean run;
  1. every item's actor is a command, the executor, a hook, the owner, or a declared item role;
  2. every core item role acts in at least one core item;
  3. no core item names an expansion role (P28).

Usage: python role_matrix.py <flow-steps record> <roles record>
"""
import collections
import re
import sys

KINDS = ("command", "executor", "hook", "owner")
STEPS = ["entry", "plan", "design", "build", "test", "deploy", "breakpoint", "lifecycle"]
ITEM = re.compile(r"^\| `([a-z]+\.[a-z0-9-]+)` \| ([^|]+) \|")
SEPARATOR = re.compile(r"^\|(\s*:?-+:?\s*\|)+\s*$")


def roster(text):
    block = text.split("\n## [roster]", 1)[1].split("\n## ", 1)[0]
    roles = {}
    for line in block.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 3 and cells[0] not in ("Role", "---") and not cells[0].startswith("-"):
            roles[cells[0]] = {"layer": cells[1], "cycle": cells[2].startswith("cycle role")}
    if not roles:
        sys.exit("no [roster] rows")
    return roles


def actor_of(cell):
    head = re.split(r"[,:(]", cell.strip(), maxsplit=1)[0].strip().lower()
    return head


def main(argv):
    lines = open(argv[0], encoding="utf-8").read().splitlines()
    roles = roster(open(argv[1], encoding="utf-8").read())
    step = None
    matrix = collections.defaultdict(lambda: collections.defaultdict(list))
    findings = []
    items = body = 0
    per_step = collections.Counter()
    for n, line in enumerate(lines):
        h = re.match(r"^## \[([a-z-]+)\]", line)
        if h:
            step = h.group(1)
            continue
        if step is None or not line.startswith("|"):
            continue
        header = n + 1 < len(lines) and SEPARATOR.match(lines[n + 1])
        if header or SEPARATOR.match(line):
            continue
        row = ITEM.match(line)
        if step not in STEPS:
            if row:
                findings.append(f"arm 0: {row.group(1)} sits under [{step}], which is no step the matrix reads")
            continue
        body += 1
        if not row:
            findings.append(f"arm 0: a row under [{step}] that the item pattern cannot read: {line[:48]}")
            continue
        items += 1
        per_step[step] += 1
        item, actor = row.group(1), actor_of(row.group(2))
        if actor in KINDS:
            matrix[actor][step].append(item)
            continue
        if actor not in roles:
            findings.append(f"arm 1: {item}: actor '{actor}' is no kind and no declared role")
            continue
        if roles[actor]["cycle"]:
            findings.append(f"arm 1: {item}: '{actor}' is a cycle role, and acts in no item")
            continue
        if roles[actor]["layer"] != "core":
            findings.append(f"arm 3: {item}: core item names the expansion role '{actor}' ({roles[actor]['layer']})")
        matrix[actor][step].append(item)
    for s in STEPS:
        if per_step[s] == 0:
            findings.append(f"arm 0: step [{s}] holds no item")
    for name, r in roles.items():
        if r["layer"] == "core" and not r["cycle"] and name not in matrix:
            findings.append(f"arm 2: core role '{name}' acts in no core item")
    order = [n for n in roles if n in matrix] + [k for k in KINDS if k in matrix]
    print("| Actor | " + " | ".join(STEPS) + " |")
    print("|---|" + "---|" * len(STEPS))
    for name in order:
        cells = [", ".join(f"`{i}`" for i in matrix[name].get(s, [])) or "—" for s in STEPS]
        print(f"| {name} | " + " | ".join(cells) + " |")
    pairs = sum(len(v) for m in matrix.values() for v in m.values())
    role_items = sum(len(v) for n, m in matrix.items() if n not in KINDS for v in m.values())
    print(f"\nitems {items} of {body} body rows; actor-item pairs {pairs}; actors {len(matrix)}; "
          f"items with a role {role_items}; cycle roles {sum(r['cycle'] for r in roles.values())}; findings {len(findings)}")
    for f in findings:
        print("FINDING", f)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

Run as `python role_matrix.py <the step definitions> <this record>`, it exited 0 and printed the table
in `[matrix]`, then:

```text
items 72 of 72 body rows; actor-item pairs 72; actors 15; items with a role 19; cycle roles 1; findings 0
```

Each arm was seen red on a planted copy of the step definitions, one line changed each, the four
malformed rows added after the follow-up round. Each run exited 1:

```text
$ planted: `plan.reason`'s actor misspelled `plannr` (1 line changed)
items 72 of 72 body rows; actor-item pairs 71; actors 15; items with a role 18; cycle roles 1; findings 1
FINDING arm 1: plan.reason: actor 'plannr' is no kind and no declared role
exit 1

$ planted: `design.seams`'s actor changed to `command`, so the reuse scout acts in no item (1 line changed)
items 72 of 72 body rows; actor-item pairs 72; actors 14; items with a role 18; cycle roles 1; findings 1
FINDING arm 2: core role 'reuse scout' acts in no core item
exit 1

$ planted: `test.reason`'s actor changed to the expansion role `deployer` (1 line changed)
items 72 of 72 body rows; actor-item pairs 72; actors 16; items with a role 19; cycle roles 1; findings 1
FINDING arm 3: test.reason: core item names the expansion role 'deployer' (distribution, integrations)
exit 1

$ planted: `plan.reason`'s actor changed to the cycle role `prompt writer` (1 line changed)
items 72 of 72 body rows; actor-item pairs 71; actors 15; items with a role 18; cycle roles 1; findings 1
FINDING arm 1: plan.reason: 'prompt writer' is a cycle role, and acts in no item
exit 1

$ planted: the [lifecycle] heading renamed [controls] (1 line changed)
items 66 of 66 body rows; actor-item pairs 66; actors 15; items with a role 19; cycle roles 1; findings 7
FINDING arm 0: life.request sits under [controls], which is no step the matrix reads
FINDING arm 0: life.quiesce sits under [controls], which is no step the matrix reads
FINDING arm 0: life.notify sits under [controls], which is no step the matrix reads
FINDING arm 0: life.snapshot sits under [controls], which is no step the matrix reads
FINDING arm 0: life.release sits under [controls], which is no step the matrix reads
FINDING arm 0: life.close sits under [controls], which is no step the matrix reads
FINDING arm 0: step [lifecycle] holds no item
exit 1

$ planted: `test.reason`'s tag uppercased to `test.Reason` (1 line changed)
items 71 of 72 body rows; actor-item pairs 71; actors 15; items with a role 18; cycle roles 1; findings 1
FINDING arm 0: a row under [test] that the item pattern cannot read: | `test.Reason` | tester | `test.recommend` | an
exit 1

$ planted: `test.attribute`'s tag given a second dot, `test.attribute.own` (1 line changed)
items 71 of 72 body rows; actor-item pairs 71; actors 15; items with a role 18; cycle roles 1; findings 1
FINDING arm 0: a row under [test] that the item pattern cannot read: | `test.attribute.own` | tester | the OWN and MI
exit 1

$ planted: `deploy.notify`'s row with its backticks dropped (1 line changed)
items 71 of 72 body rows; actor-item pairs 71; actors 15; items with a role 19; cycle roles 1; findings 1
FINDING arm 0: a row under [deploy] that the item pattern cannot read: | deploy.notify | command, idempotent | `deploy.
exit 1

$ planted: a double space after `test.attribute`'s tag (1 line changed)
items 71 of 72 body rows; actor-item pairs 71; actors 15; items with a role 18; cycle roles 1; findings 1
FINDING arm 0: a row under [test] that the item pattern cannot read: | `test.attribute`  | tester | the OWN and MIXED
exit 1
```

### `role_matrix.py`, revised 2026-10-17

The debt round's two reviews of the follow-up fold (`reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-round3-a.md`
and `-b.md`) found arm 0 still reading a row by its first character. A row indented one space, or with its
leading pipe dropped, still renders as a table row, and the instrument skipped both. Arm 0 now reads tables
by the renderer's grammar: a header row and its separator open one, and it runs to the first blank line or
block start. Only arm 0's reader changed:

```diff
--- role_matrix.py, 2026-10-16
+++ role_matrix.py, 2026-10-17
@@ -8,7 +8,10 @@
 Four arms, each a finding (exit 1 if any):
   0. every table body row under a step's heading is an item row the item pattern reads, every item
      row sits under a step's heading, and every step holds at least one item, since a parser that
-     skips what it cannot place reports a clean run;
+     skips what it cannot place reports a clean run. A table is read by the renderer's grammar, not by
+     a line's first character: a header row and its separator open it, either indented up to three
+     spaces and with its edge pipes optional, and it runs to the first blank line or block start, so
+     an indented or pipe-less body row is a row to grade, and a finding when the pattern cannot read it;
   1. every item's actor is a command, the executor, a hook, the owner, or a declared item role;
   2. every core item role acts in at least one core item;
   3. no core item names an expansion role (P28).
@@ -22,7 +25,9 @@
 KINDS = ("command", "executor", "hook", "owner")
 STEPS = ["entry", "plan", "design", "build", "test", "deploy", "breakpoint", "lifecycle"]
 ITEM = re.compile(r"^\| `([a-z]+\.[a-z0-9-]+)` \| ([^|]+) \|")
-SEPARATOR = re.compile(r"^\|(\s*:?-+:?\s*\|)+\s*$")
+SEPARATOR = re.compile(r"^\|?(\s*:?-+:?\s*\|)+(\s*:?-+:?\s*)?$")
+INDENT = re.compile(r"^ {1,3}")
+BLOCK = re.compile(r"^ {0,3}(#|`{3}|~{3}|>|[-*+] |\d+[.)] )")
 
 
 def roster(text):
@@ -50,15 +55,21 @@
     findings = []
     items = body = 0
     per_step = collections.Counter()
+    in_table = False
     for n, line in enumerate(lines):
         h = re.match(r"^## \[([a-z-]+)\]", line)
         if h:
-            step = h.group(1)
+            step, in_table = h.group(1), False
             continue
-        if step is None or not line.startswith("|"):
+        flat = INDENT.sub("", line)
+        if not in_table:
+            nxt = INDENT.sub("", lines[n + 1]) if n + 1 < len(lines) else ""
+            in_table = step is not None and "|" in flat and bool(SEPARATOR.match(nxt))
             continue
-        header = n + 1 < len(lines) and SEPARATOR.match(lines[n + 1])
-        if header or SEPARATOR.match(line):
+        if not line.strip() or BLOCK.match(line):
+            in_table = False
+            continue
+        if SEPARATOR.match(flat):
             continue
         row = ITEM.match(line)
         if step not in STEPS:
```

Run with its planting script, `plant_roles.py` below, over the step definitions at this fold: eleven
plants, the two new ones last.
The clean run prints what the 2026-10-16 instrument prints there, and the table in `[matrix]` is unchanged:

```text
$ clean
items 75 of 75 body rows; actor-item pairs 75; actors 15; items with a role 19; cycle roles 1; findings 0
exit 0

$ planted: `plan.reason`'s actor misspelled `plannr` (1 line changed)
items 75 of 75 body rows; actor-item pairs 74; actors 15; items with a role 18; cycle roles 1; findings 1
FINDING arm 1: plan.reason: actor 'plannr' is no kind and no declared role
exit 1

$ planted: `design.seams`'s actor changed to `command`, so the reuse scout acts in no item (1 line changed)
items 75 of 75 body rows; actor-item pairs 75; actors 14; items with a role 18; cycle roles 1; findings 1
FINDING arm 2: core role 'reuse scout' acts in no core item
exit 1

$ planted: `test.reason`'s actor changed to the expansion role `deployer` (1 line changed)
items 75 of 75 body rows; actor-item pairs 75; actors 16; items with a role 19; cycle roles 1; findings 1
FINDING arm 3: test.reason: core item names the expansion role 'deployer' (distribution, integrations)
exit 1

$ planted: `plan.reason`'s actor changed to the cycle role `prompt writer` (1 line changed)
items 75 of 75 body rows; actor-item pairs 74; actors 15; items with a role 18; cycle roles 1; findings 1
FINDING arm 1: plan.reason: 'prompt writer' is a cycle role, and acts in no item
exit 1

$ planted: the [lifecycle] heading renamed [controls] (1 line changed)
items 69 of 69 body rows; actor-item pairs 69; actors 15; items with a role 19; cycle roles 1; findings 7
FINDING arm 0: life.request sits under [controls], which is no step the matrix reads
FINDING arm 0: life.quiesce sits under [controls], which is no step the matrix reads
FINDING arm 0: life.notify sits under [controls], which is no step the matrix reads
FINDING arm 0: life.snapshot sits under [controls], which is no step the matrix reads
FINDING arm 0: life.unlease sits under [controls], which is no step the matrix reads
FINDING arm 0: life.close sits under [controls], which is no step the matrix reads
FINDING arm 0: step [lifecycle] holds no item
exit 1

$ planted: `test.reason`'s tag uppercased to `test.Reason` (1 line changed)
items 74 of 75 body rows; actor-item pairs 74; actors 15; items with a role 18; cycle roles 1; findings 1
FINDING arm 0: a row under [test] that the item pattern cannot read: | `test.Reason` | tester | `test.recommend` | an
exit 1

$ planted: `test.attribute`'s tag given a second dot, `test.attribute.own` (1 line changed)
items 74 of 75 body rows; actor-item pairs 74; actors 15; items with a role 18; cycle roles 1; findings 1
FINDING arm 0: a row under [test] that the item pattern cannot read: | `test.attribute.own` | tester | the OWN and MI
exit 1

$ planted: `deploy.notify`'s row with its backticks dropped (1 line changed)
items 74 of 75 body rows; actor-item pairs 74; actors 15; items with a role 19; cycle roles 1; findings 1
FINDING arm 0: a row under [deploy] that the item pattern cannot read: | deploy.notify | command, idempotent | `deploy.
exit 1

$ planted: a double space after `test.attribute`'s tag (1 line changed)
items 74 of 75 body rows; actor-item pairs 74; actors 15; items with a role 18; cycle roles 1; findings 1
FINDING arm 0: a row under [test] that the item pattern cannot read: | `test.attribute`  | tester | the OWN and MIXED
exit 1

$ planted: `test.reason`'s row indented one space (1 line changed)
items 74 of 75 body rows; actor-item pairs 74; actors 15; items with a role 18; cycle roles 1; findings 1
FINDING arm 0: a row under [test] that the item pattern cannot read:  | `test.reason` | tester | `test.recommend` | a
exit 1

$ planted: `deploy.notify`'s row with its leading pipe dropped (1 line changed)
items 74 of 75 body rows; actor-item pairs 74; actors 15; items with a role 19; cycle roles 1; findings 1
FINDING arm 0: a row under [deploy] that the item pattern cannot read: `deploy.notify` | command, idempotent | `deploy.
exit 1
```

The planting script, run as `python plant_roles.py role_matrix.py <the step definitions> <this record>
<scratch dir>`:

```python
"""Run the matrix instrument clean, then on planted copies of the step definitions, one line changed each.

Usage: python plant_roles.py <role_matrix.py> <flow-steps record> <roles record> <scratch dir>
Prints each run as the roles record's [instrument] keeps it: the summary and FINDING lines, then the exit.
"""
import re
import subprocess
import sys

tool, steps, roles, scratch = sys.argv[1:5]
text = open(steps, encoding="utf-8", newline="").read()

PLANTS = [
    ("`plan.reason`'s actor misspelled `plannr`",
     r"(\| `plan\.reason` \| )planner", r"\1plannr"),
    ("`design.seams`'s actor changed to `command`, so the reuse scout acts in no item",
     r"(\| `design\.seams` \| )reuse scout", r"\1command"),
    ("`test.reason`'s actor changed to the expansion role `deployer`",
     r"(\| `test\.reason` \| )tester", r"\1deployer"),
    ("`plan.reason`'s actor changed to the cycle role `prompt writer`",
     r"(\| `plan\.reason` \| )planner", r"\1prompt writer"),
    ("the [lifecycle] heading renamed [controls]",
     r"(?m)^## \[lifecycle\]", "## [controls]"),
    ("`test.reason`'s tag uppercased to `test.Reason`",
     r"\| `test\.reason` \|", "| `test.Reason` |"),
    ("`test.attribute`'s tag given a second dot, `test.attribute.own`",
     r"\| `test\.attribute` \|", "| `test.attribute.own` |"),
    ("`deploy.notify`'s row with its backticks dropped",
     r"\| `deploy\.notify` \|", "| deploy.notify |"),
    ("a double space after `test.attribute`'s tag",
     r"\| `test\.attribute` \|", "| `test.attribute`  |"),
    ("`test.reason`'s row indented one space",
     r"(?m)^(\| `test\.reason` \|)", r" \1"),
    ("`deploy.notify`'s row with its leading pipe dropped",
     r"(?m)^\| (`deploy\.notify` \|)", r"\1"),
]


def run(path):
    p = subprocess.run([sys.executable, tool, path, roles], capture_output=True, text=True, encoding="utf-8")
    keep = [ln for ln in p.stdout.splitlines() if ln.startswith(("items ", "FINDING"))]
    return "\n".join(keep), p.returncode


out, rc = run(steps)
print("$ clean")
print(out)
print(f"exit {rc}")
for desc, pat, rep in PLANTS:
    planted, n = re.subn(pat, rep, text, count=1)
    if n != 1:
        sys.exit(f"plant did not apply: {desc}")
    changed = sum(a != b for a, b in zip(text.split("\n"), planted.split("\n")))
    path = f"{scratch}/planted-steps.md"
    open(path, "w", encoding="utf-8", newline="").write(planted)
    out, rc = run(path)
    print(f"\n$ planted: {desc} ({changed} line changed)")
    print(out)
    print(f"exit {rc}")
```

The 2026-10-16 instrument missed both new plants:

```text
$ planted: `test.reason`'s row indented one space (1 line changed)
items 74 of 74 body rows; actor-item pairs 74; actors 15; items with a role 18; cycle roles 1; findings 0
exit 0

$ planted: `deploy.notify`'s row with its leading pipe dropped (1 line changed)
items 74 of 74 body rows; actor-item pairs 74; actors 15; items with a role 19; cycle roles 1; findings 0
exit 0
```

## [revised] Revised 2026-10-16: the two Tier-2 rounds, folded

Two Tier-2 rounds reviewed this record at blob `081ef3c1`. The comparison record places their findings
on 39 defects (`build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md`, `[map-roles]`),
and its map's `disposition` cells point here. Each defect's fix sits in place, in the sections named.
The owner holds a revisit of the layer's mechanical shape, and the defects on execution shape are
folded as facts and handed to it:
- **amend:** this record, or a sibling record, now states the fix;
- **fork:** the owner answered it, in the comparison record's `[answers]`;
- **none:** every finding on it was refuted.

| Defect | Disposition | Where the fix sits |
|---|---|---|
| `matrix-keyword-derivation` | amend | `[matrix]`: the Actor cell's opening names its one actor; `role_matrix.py` revised |
| `matrix-prompt-writer` | amend | `[roster]`: the prompt writer is a cycle role; `[matrix]`'s second arm covers item roles |
| `matrix-arms-unseen` | amend | `role_matrix.py` implements all three arms, each seen red (`[instrument]`) |
| `sod-agent-id-check` | amend | R3-C: the spawn guard checks each verifier's packet against `roles.verifier-context` |
| `acceptance-unmeasurable` | amend | R3-F: answered calls from the hook's records, other classes from runlog's extractor, keyed by task-sha |
| `agent-file-hook` | amend | R3-H: the answered-call rule is a pack in Runtime's one dispatcher entry |
| `agent-id-binding` | amend | `[settled]` and `[trust]` 10: the act's task-sha and the session's binding record |
| `cut-at-launch` | amend | `[trust]` 3: fresh at act launch, and the window after it guarded; v2's P29 |
| `method-call-figures` | amend | `[current]`: 811 method-class reads, from about 619 calls; `gap-roles-12` |
| `recall-once-per-session` | none | refuted |
| `gaps-count-stale` | amend | `[gaps]` notes `gap-roles-18` |
| `answered-state-calls` | amend | `[trust]` 10: a state call is answered only while its handed value holds |
| `answered-call-fail-open` | amend | `[trust]` 10: open below CLI 2.1.295 on ungated tools |
| `settled-rule-attribution` | amend | `[settled]`: the render refusal is R-C's |
| `effort-carrier` | amend | R3-A: effort stays in `house/policy.toml`; handed to the mechanical-shape revisit |
| `execution-shape-seams` | amend | `[owner-notes]` and `gap-roles-18`: three of the five parts are declared; handed to the revisit |
| `metrics-extractor-seam` | none | refuted; R3-F names runlog's extractor anyway |
| `role-step-join-exists` | none | refuted |
| `rules-key-binding` | amend | `[tags]`: the binding extends each role's `rules:` key, joined both ways |
| `handoff-seam` | amend | `[trust]` 1: it extends `handoff.py render` |
| `cycle-amendment` | amend | flow-roles `[cycle]` and `[records]`, under a dated `Revised:` line |
| `protocol-pointer-machinery` | amend | `[tags]`: the slicing unit re-points the carry machinery; `gap-roles-12` |
| `body-ceiling` | amend | R3-A: the packet and block budgets extend `BODY_CEILINGS` |
| `keys-agent-typed` | none | refuted |
| `reverify-order-sources` | amend | `[current]` cites the kit sources, `gov-session` and the spec template; `gap-roles-10` |
| `claimed-fact-staleness` | amend | `[trust]` 3: a claimed fact whose source moved is handed as stale evidence |
| `read-class-undefined` | amend | `[trust]` 10: a read is any call that returns a file's content; a partial overlap runs |
| `over-budget-route` | amend | `[trust]` 1: optional inputs demote first, then the item routes back; a vanished anchor |
| `repair-lifecycle` | amend | `[trust]` 7: when a repair ends, and concurrent repairs |
| `repair-staleness` | amend | `[trust]` 7: the repair is keyed by its sources and preferred over the original |
| `p29-vs-p23` | fork, amend | LR-2; `[trust]` 4; v2's P29 |
| `flow-roles-steps-stale` | amend | flow-roles `[steps]` is marked superseded by `[matrix]` |
| `dboundroles-order` | none | refuted |
| `verifier-set-spelling` | amend | `[trust]` 6: `roles.verifier-context` covers the reviewer, the skeptic and the tester |
| `cached-prefix-claim` | amend | `[tags]` and R3-B: the cached prefix holds within an act and the cache window |
| `blob-sha-crlf` | none | refuted |
| `cli-version-measurement` | amend | `[current]`: measured on 2.1.295 only |
| `roster-fold-item` | amend | `[roster]`; the step definitions' `review.fold` |
| `adopter-role-overlays` | amend | R3-A: the house overlays and the effort policy compose each role |
