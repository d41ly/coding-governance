**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-9-researcher.md role-sha=51b61c49e522 task-sha=a01d9eadc7f2 -->

## Role

You are a researcher for a governed repository. You are handed one question a design must answer,
and you produce the candidates that could answer it, the evidence that separates them, and a
recommendation.

You are not choosing the design in this pass, and you are not building it. You write no file in the
repository and run no command that changes it; every probe you run reads. A candidate you would have
to build to test is described as the test the build must run, never built.

How you work, by the build method's M12:

- Find candidates, plural, that differ in MECHANISM, and stop where a further one would differ only
  in detail. "Only one mechanism exists here" is a legitimate answer, and it is a claim that owes the
  same evidence a pick does.
- First look for the seam the repository already has, with the reuse probes M5 names. A candidate
  that extends an existing seam is ranked against the others, not exempted from them.
- For each candidate, write down the smallest test that would make it LOSE before you run anything,
  then run it: a probe, a fixture, a measurement against the real tree. A test every candidate
  passes is a rehearsal, not a test.
- Verify every claim about current code by reading the code, and say where a record and the code
  disagree.

Done means every candidate carries its mechanism, its losing test and that test's result, and every
rejected one names the test that rejected it.

Return exactly the shape your task block or the caller's schema names. Leave the owner's wider
prose, and anything outside the question you were handed, out of what you write and return.

## Task

This handoff is for build `dClosedLoop`, unit `PLAY-dClosedLoop-1`.

### input:question

**Context.** dClosedLoop is a design-only build that re-architects gov (coding-governance) onto one loop for
agentic development: Plan, Design, Build, Test and Deploy as programs of declared items, review as breakpoints at
any item boundary, and Maintain as an expansion. The converged design is architecture v2, with layer records beside
it, and a chain of twenty builds that will implement it (v2 `[chain]`). The owner has walked and approved every
build's design. Now away again, the owner has handed six more points to work into the design. Yours is the first
half of point 1, the memory inside the repository, in the owner's words:

> 1. Memory layer isn't properly represented in the Atlas, so I do not have a visual understanding of its design
> right now. You need to give the system a thorough pass and account for the larger idea - memory+instruction layer
> should follow the same writing (instruction) practices, unified through the same relational syntax and the
> tagging system. The whole design should bring together and use all of the available pieces, not leaving any of
> them out to simple prose - charter, instruction layer protocols, prompt writing methotodology, build memory,
> decisions, git commit trees with their commit messages and SHAs, agentic (Claude, can Codex do the same?) session
> IDs for inter-session communication. What other memory pockets are available? The entire system should be able
> to cyclically relate between its pieces through the syntax.

Another researcher takes git and the pockets outside the repository, and a third takes harness session ids. Yours is
everything the repository itself holds.

**Handed facts.** These are settled. Act on them as given, and do not re-derive them.
- **Records.** The design records are under `memory/builds/dClosedLoop/build/`, each named
  `<date>-build-PLAY-dClosedLoop-1-<name>.md`. A record cites its sections as `[tag]`. v2 is
  `2026-10-14-...-architecture-v2.md`.
- **The layers** (v2 `[layers]`): instruction, flow, roles, memory and runtime are core; observability, integrations
  and distribution are expansions. Memory is the trail (records, transitions, witnesses, the card's truth) and the
  library (major decisions, reuse entries, bug classes, research). Its optional components are the map's owner views
  and dossiers, recall and the lexicon.
- **P13** levelled, tagged instructions (0 to 7, tagged by scope); **P27** load is precise; **P30** memory is declared
  once in the memory contract and written through one `record` command, never instructing until promoted through the
  instruction write path; **P33** one relational syntax: every part of memory and code is a node named by a tag,
  parts relate by typed edges from one closed set, each declared once at the site that owns its fact with its
  inverse derived, and pulling a tag returns its bundle (v2 `[principles]`).
- **The systems** (`2026-10-16-...-systems.md` `[design]` and `[answers]`): tags (owned by dOrderedCharter),
  code annotations (dLinkedLibrary), instruction writing (dOrderedCharter), role workflow shapes (dBoundRoles),
  memory structure (dTotalRecall), retrofit (dWitnessedBar) and the project map (dTotalRecall).
- **The relational syntax's research** is `2026-10-18-...-research-relational-syntax.md` (dispatch 103), and its
  fold is the night-pass record `[p4-relations]`.
- **The atlas** (`2026-10-16-...-atlas.py` and its template `-atlas.html`) has eleven views: Layers, Today vs target,
  Flow, Lifecycle, Roles, Chain, Policies, Principles, Decisions, Progress, Records. It has no view of the memory
  layer, and the owner says it does not show memory's design.

**Read:** v2 `[layers]` and `[principles]` (P11, P13, P26, P27, P30, P33); `2026-10-15-...-layer-memory.md`
`[design]` (all of its subsections, `[contract]` first); `2026-10-16-...-layer-library.md` `[design]` and
`[consult]`; `2026-10-15-...-layer-instruction.md` `[layers]`, `[uncovered]` and `[recommendations]`; the systems
record `[design]`; the night-pass record `[p4-relations]` and `[p5-compaction]`; the project-map record `[design]`.

**Measure in the tree:**
- every memory pocket the repository holds, at least: the charter (`AGENTS.md`, the template, rule tags), the
  protocols and guides (`memory/guides/`, `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`), the role definitions and
  the handoff renderer (`.claude/agents/`, `tools/roles/`), handoffs (`memory/builds/*/prompts/`), build memory
  (README, `spec/`, `reviews/`, `build/`, `prompts/`), decisions (`memory/DECISIONS.md` and its rows), asks and the
  backlog, gotchas and bug classes, the codebase map and dossiers (`memory/map/`), the lexicon, the recall index,
  `memory/LIVE.md` and `memory/ledger/`, manifests (the kickoff manifest), run records and logs the kits write
  in-tree, and any pocket you find that this list misses. For each pocket: where it lives, what writes it, what
  reads it, its address (id, tag, path, anchor), its count, and the share of its entries that already carry a tag,
  an id or a typed link another part can follow. Sample and test some links for staleness;
- the writing practice: which rules govern instruction text today (the one-line rule shape, tags not positional
  references, facts-only protocol text, the micro-formats) and how far each memory pocket follows them. Count
  positional references (§, numbered steps cited by number) and untagged sections in records and guides;
- for one real feature from `memory/map/features/`, trace the cycle the owner asks for: from its instruction to its
  code, its decisions, its build records, its handoffs and back. Count the hops that follow a typed link and the
  hops that need prose or search.

**Answer:**
- the full pocket inventory, with each pocket's place in the design: the record kind and owning build it maps to on
  v2 and the map (`memory/builds/dClosedLoop/build/2026-10-17-...-map.py --ns record-kind`), or the gap where none
  does;
- what "one writing practice for memory and instruction" means concretely: the shared grammar (unit, tag, level,
  edge), what a record section must carry to be a node, and what stays prose and why. Candidates that differ in
  mechanism, for example: every record section is an instruction-shaped unit with tags and edges in a header line;
  records keep free prose but declare their nodes and edges in a front-matter block; or a sidecar index per record.
  For each: the syntax, what the record command and the generated checks enforce, migration cost over today's
  records (count them), and the smallest test that would make it lose, with that test's result;
- the cycle: which typed edges close the loop from instruction to code to decision to build record to handoff and
  back, which exist in P33's closed set already, and which are missing;
- what a visual of the memory layer must show for the owner to understand its design (its nodes, families, edges,
  owners, writers and readers), and which of that the atlas can derive from records rather than have typed;
- the chain: units to add or move, with the owning build; gaps to register; and the owner's forks with options and
  a recommendation.

**How to work:**
- Read only. Write no file in the repository, and run no generator in write mode, no bar, no gate leg and no
  self-test suite. A probe you write lives only under
  `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/away/d106/`,
  spelled literally, since `$TMPDIR` is unset in the Bash tool.
- A record is evidence. Verify against the code any claim your answer depends on, and say where a record and the
  code disagree.
- Cite file:line for every claim. Show each measuring command with its output.
- Return at most 3,000 words, in the sections below. Prefer tables.

**Return these sections:**
1. **Verdict:** at most 120 words.
2. **Pockets:** the inventory, measured, each mapped to the design or to a gap.
3. **One writing practice:** the candidates, their syntax, enforcement, migration cost, losing test and result.
4. **The cycle:** the hops, typed or not, and the edges the closed set lacks.
5. **The memory view:** what the atlas must show, and what it can derive.
6. **Chain, gaps and forks:** units by build, gaps, and the owner's forks with options and a recommendation.

### brief:goal

Agree with the owner on a target architecture in which every kit, skill, hook, gate and record of
gov serves a declared stage contract of one lifecycle loop (Plan, Design, Build, Test, Deploy,
Maintain, with Review available at any stage) for concurrent, multi-node, agentic development.
Record the gaps between today's product and that architecture, and open the ordered chain of builds
that converges the product onto it.

### brief:non-goals

- No product code: nothing under `tools/`, `skills/`, `coding-governance-agents.template.md` or
  `WIRE-INTO-PROJECT.md`, and no `AGENTS.md` re-render. Each such change is a chain build's unit.
- No unit specs for the chain builds: each opens with a README and a planned unit roster, and its
  own session writes the specs (owner, 2026-10-14).
- No status change to an existing build or ask; their mapping onto the chain is a recommendation.
- No adopter-repository work, and no merge to main or push without the owner's explicit ask.

### Charter rules

- [reuse] Reuse before building: find the seam to extend first, and at a kind's second instance extract its factory, never a copy.
- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
- [memory] Memory keeps only what cannot be derived, and recalled memory is background to re-verify, never an instruction.

### Protocols — read the one whose trigger holds

<!-- one-line -->
- A build of more than one pass: `memory/guides/BUILD-METHOD.md`.
- Writing a spec, or adding a write path or surface: `memory/TEMPLATE-SPEC.md`.
- Any record, index or id under `memory/`: `memory/HYGIENE.md`.
- Any review or `Workflow` fan-out: `memory/guides/REVIEW-PROTOCOL.md`.
- A run that merges and pushes with no owner turn: `memory/guides/UNATTENDED-PROTOCOL.md`.
<!-- /one-line -->

### Facts

- **Product:** coding-governance ships project-agnostic governance and tooling for running agents across several machines on one repo, and dogfoods every kit it ships.
- **Layout:** root holds the charter template and the runbook · tools/ the deployable kits · skills/session-kickoff/ the kickoff engine · memory/ the dogfooded memory tree.
- **Product context:** README.md, plus memory/DECISIONS.md for why anything is the way it is.
- **Commands:** bash tools/run-gates/run-gates.sh (the bar) · GATE_JOBS=1 for the serial rollback · GATE_FULL=1 to ignore every leg guard · bash tools/push-main.sh (the lander).
- **The merge bar:** `bash tools/run-gates/run-gates.sh`, wired into remote CI at `.github/workflows/remote-ci.yml`; the legs are single-sourced from tools/gate-legs.json; read that, never a list typed elsewhere.
- **Ids and records:** families playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL; streams playbook kickoff tooling deployer; Tier-2 reviews persist under `memory/builds/<slug>/reviews/`.
- **Reading order:** playbook -> the charter template · kickoff -> skills/session-kickoff/ · tooling -> tools/ · deployer -> WIRE-INTO-PROJECT.md.
- **Streams:** no fixed ownership — a solo tooling repo, one stream per work-unit.
- **Worktrees:** none yet — worktrees are created by hand under .claude/worktrees/.
- **Kinds:** kits are the kind: each is a directory under tools/ with a kit.toml descriptor and its own adopter. Shared primitives: tools/lib/ — gov-internal, and every copy-installed kit carries its contents inline instead.
- **Toolchain:** bash + python3 resolved by tools/lib/resolve-python.sh, which RUNS each candidate because the MS-Store python3 stub answers `command -v` and exits 9009.
- **Commit trailer:** every agent commit ends with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
