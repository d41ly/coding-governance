**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-11-researcher.md role-sha=51b61c49e522 task-sha=300c5319badb -->

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
build's design. Now away again, the owner has handed six more points to work into the design. Yours is point 3,
and the session-id part of point 1, in the owner's words:

> 3. Claude Code CLI. This is already being used in part by the existing processes and their tooling but a larger
> question - is there benefit to integrating more of the CLI instead of relying on Claude Desktop/Codex Desktop
> applications? How to achieve agnosticism from the application the owner would use? This should be
> researched/tested.

> (from point 1) ... agentic (Claude, can Codex do the same?) session IDs for inter-session communication. What
> other memory pockets are available? The entire system should be able to cyclically relate between its pieces
> through the syntax.

**Handed facts.** These are settled. Act on them as given, and do not re-derive them.
- **Records.** The design records are under `memory/builds/dClosedLoop/build/`, each named
  `<date>-build-PLAY-dClosedLoop-1-<name>.md`. A record cites its sections as `[tag]`. v2 is
  `2026-10-14-...-architecture-v2.md`.
- **Runtime's design** (`2026-10-15-...-layer-runtime.md` `[design]`, owned by dWellOiledMachine) declares the
  extension points `harness-adapters` (how a harness loads instructions, spawns, hooks and compacts),
  `spawn-backends` (a way to start a role agent), `host-adapters` (where the supervisor and its sessions run) and
  `notification-adapters`, and a supervisor that runs act sessions. dKeptSession owns the session model, the
  mailbox (`mailbox-message`) and the card's session keys; dWellOiledMachine owns session bindings, acts and the
  journal.
- **How the owner works today.** On this node the owner runs Claude Code inside the Claude desktop app's Code tab
  (the in-app Claude Code is 2.1.295, the `claude` on PATH is 2.1.292). gov's instructions are `AGENTS.md`, which
  `CLAUDE.md` imports; `tools/agent-instructions/` wires other agents' filenames to it. gov ships hooks wired in
  `.claude/settings.json`, role agents in `.claude/agents/`, the kickoff skill through a junction, and `Workflow`
  scripts under `tools/workflows/`. The unattended kit's launcher, `tools/unattended/resume-tick.sh`, names a CLI
  launch line that has never run. Never run that line, and never pass `--dangerously-skip-permissions`.
- **The design's other agents.** v2 counts every harness gov installs into as a target that Runtime's harness
  adapters declare (v2 `[layers]`, distribution).

**Read:** v2 `[layers]`, `[principles]` (P4, P15, P16, P24, P25, P26) and `[chain]`; `2026-10-15-...-layer-runtime.md`
`[current]`, `[design]` and `[build]`; the night-pass record `[p1-unattended]` and `[p5-compaction]`; the
`tools/roles/` kit and `tools/hooks/`; `tools/agent-instructions/`.

**Measure and test:**
- what gov depends on per harness surface today: every place the tree invokes `claude`, reads a Claude Code hook
  payload field, writes `.claude/` settings, ships a `Workflow` script, or depends on a desktop-only feature. Grep
  and count; name the files;
- the CLI as it is on this node: `claude --version`, `claude --help`, and the flags for headless runs, output
  formats, session ids, resume and fork, agents, permission modes, settings sources and MCP. Then run one minimal
  headless session that uses no tools, for example `claude -p "Reply with one word: pong" --output-format json`
  with a turn limit, and read the session id it returns. Resume that session by id headlessly and confirm it
  remembers. Find the transcript the run wrote. If the CLI refuses to start inside this session, record the
  refusal and its message, and do not route around it;
- Codex: whether `codex` is installed here (`codex --version`). If it is, read its help for headless runs, session
  ids and resume, and run nothing that edits. If it is not, take its documented behaviour from its own docs (web
  search), and say that you could not test it;
- inter-session communication: what the Claude harness offers for one session to address another by id (resume,
  fork, message tools a session may have, transcripts as a shared medium), what Codex offers, and what the design's
  mailbox assumes. Say which of these a script can drive, and which only an app can;
- the desktop apps: which of their features gov's flows use or would want (session lists, split views, scheduled
  tasks, artifacts, a browser pane, worktree management), and which of those has a CLI or SDK equivalent.

**Answer:**
- is there a benefit to integrating more of the CLI: what headless runs, session ids, structured output and the SDK
  would give the loop's supervisor, the unattended path and observability, and what they cost (auth, permission
  prompts, nesting, versions drifting between the app and PATH);
- how to make gov agnostic of the application the owner uses: candidates that differ in mechanism, for example the
  desktop app as the runtime with the CLI as a fallback; the CLI (or SDK) as the one runtime with any app as a
  viewer; or harness adapters with a conformance fixture each harness must pass, and the owner's app chosen by a
  policy. For each: what it changes in Runtime's design, which harnesses it covers (Claude Code in the CLI, the
  desktop app and an IDE; Codex in its CLI and app), and the smallest test that would make it lose, with that
  test's result;
- session ids as memory: what a session id gives (resume, transcript, attribution), how it joins the relational
  syntax (journal entries, returns, commits), whether Codex can do the same, and what a harness without ids needs;
- the chain: units to add or move, with the owning build; gaps to register; and the owner's forks with options and
  a recommendation. A behaviour the owner may switch is a policy key with a default and its allowed values.

**How to work:**
- Read only, except the one headless test session and its resume. Write no file in the repository, and run no
  generator in write mode, no bar, no gate leg and no self-test suite. A probe lives only under
  `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/away/d108/`,
  spelled literally, since `$TMPDIR` is unset in the Bash tool.
- A record is evidence. Verify against the code any claim your answer depends on, and say where a record and the
  code disagree. Mark every claim taken from documentation rather than a test as documented, not tested.
- Cite file:line for every claim. Show each command with its output.
- Return at most 3,000 words, in the sections below. Prefer tables.

**Return these sections:**
1. **Verdict:** at most 120 words.
2. **Today:** what gov depends on, per harness surface.
3. **The CLI and Codex, tested:** commands and outputs, and what the apps add.
4. **Agnosticism:** the candidates, losing tests and results.
5. **Session ids as memory:** what they give, how they join the syntax, Codex's parity.
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
