**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-13-researcher.md role-sha=51b61c49e522 task-sha=6e76afc87356 -->

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
build's design. Now away again, the owner has handed six more points to work into the design. Yours is point 5, in
the owner's words:

> 5. Observability - will it be possible to analyze any part of the flow effortlessly when the full rearchitecture
> is complete? Without evidence, fixes and improvements are impossible. It should be possible to point at any part
> of the flow, worker, task, or issue and be able to tell what was happening.

**Handed facts.** These are settled. Act on them as given, and do not re-derive them.
- **Records.** The design records are under `memory/builds/dClosedLoop/build/`, each named
  `<date>-build-PLAY-dClosedLoop-1-<name>.md`. A record cites its sections as `[tag]`. v2 is
  `2026-10-14-...-architecture-v2.md`.
- **The observability layer** is an expansion: signals about the loop and the runtime, read and filed but never
  deciding a position, and the cadence programs that act on them, Maintain and the Loop Review (v2 `[layers]`;
  `2026-10-16-...-layer-expansions.md` designs it). dTendedCadence owns Maintain and run records; dCalibratedLens
  owns the Loop Review and the value ledger.
- **The core's evidence, as designed:** a transition record per state change (dDeclaredLoop); typed returns between
  roles (P26, dBoundRoles work orders); acts, session bindings and the journal (dWellOiledMachine); per-SHA verdicts
  and seen-red records (dWitnessedBar); landing and release records (dShippedRelease); the card rendered from memory
  (dPlacedRequest, dKeptSession); one relational syntax joining every part by typed edges (P33).
- **Evidence today:** each build's session log, the agent and returned lines `tools/roles/handoff.py agents`
  derives from transcripts, the runlog kit's line grammar, the unattended kit's run records, the drift-audit
  report, the process monitor, the stall-recorder hook, gate output and git history.

**Read:** v2 `[layers]`, `[principles]` (P2, P9, P22, P24, P26, P33) and `[chain]`; `2026-10-16-...-layer-expansions.md`
`[design]` (observability's part) and `[gaps-proposed]`; `2026-10-15-...-layer-runtime.md` `[design]` (the journal,
acts, returns, the supervisor's checklist and the owner's controls); the `tools/runlog/`, `tools/drift-audit/` and
`tools/process-monitor/` kits; the build session log `2026-10-14-...-session-log.md`.

**Measure and test, by reconstruction:**
- pick at least four real past events of different kinds, for example one researcher dispatch in this build's
  session log, one unattended run the runlog or run records hold, one red gate run, and one hook stall or process
  reap. For each, try to tell what was happening using only today's evidence: who acted, on what, under which
  instruction, with which inputs, what it cost in time and tokens, what it produced, and what came next. Count the
  lookups, the sources you had to open, and the questions you could not answer;
- for the same four events, say what the design as specified would record, and which questions would still be
  unanswerable once every chain build lands. Name the record kind and owner for each answer, or the gap;
- the keys: which identifiers today's evidence carries (session ids, agent ids, run ids, SHAs, unit and build ids,
  item tags) and whether each source carries enough of them to join it to the others.

**Answer:**
- will it be possible, once the chain lands, to point at any part of the flow, any worker, any task or any issue and
  tell what was happening, and what is missing for that;
- candidates that differ in mechanism, for example one correlation envelope on every record (build, item, unit,
  role, session, agent, SHA) and a trace resolver that walks P33's edges; one append-only event journal with spans,
  in the shape of OpenTelemetry, from which every view is derived; or an index over today's pockets left where they
  are. For each: what it records, its cost per event, its retention, what reads it (a `gov trace <key>` or
  `gov why <key>` verb, the atlas, the Loop Review), how it stays complete when a worker dies, and the smallest test
  that would make it lose, with that test's result;
- what "effortless" requires of the read side: one query from any key to a timeline, the timeline's shape, and its
  bound;
- the chain: units to add or move, with the owning build; gaps to register; and the owner's forks with options and
  a recommendation. A behaviour the owner may switch is a policy key with a default and its allowed values.

**How to work:**
- Read only. Write no file in the repository, and run no generator in write mode, no bar, no gate leg and no
  self-test suite. A probe lives only under
  `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/away/d110/`,
  spelled literally, since `$TMPDIR` is unset in the Bash tool.
- Read transcripts only to measure their shape and keys. Quote nothing private from them beyond a field name or a
  count.
- A record is evidence. Verify against the code any claim your answer depends on, and say where a record and the
  code disagree.
- Cite file:line for every claim. Show each measuring command with its output.
- Return at most 3,000 words, in the sections below. Prefer tables.

**Return these sections:**
1. **Verdict:** at most 120 words.
2. **Reconstruction:** the four events, today and as designed: lookups, sources, unanswered questions.
3. **Keys:** the identifiers each source carries, and the joins that fail.
4. **Candidates:** what each records, cost, retention, reader, completeness, losing test and result.
5. **The read side:** the query, the timeline and its bound.
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
