**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-15-researcher.md role-sha=51b61c49e522 task-sha=0e79df104b39 -->

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
it, and a chain of twenty builds, 367 planned units, that will implement it (v2 `[chain]`). The owner is answering
the away pass's forks. Two answers on point 4, one practice across platforms, ask for more work, in the owner's
words:

> AP-17 (which platforms gov promises): gitbash + linux at start, but add a potential future plan for macos and pwsh-launch.

> AP-19 (which Python gov requires): 3.11 but let's plan this ahead, do we need a newer python version for any reason? Now is the time to price it in.

Today is 2026-10-18.

**Handed facts.** These are settled. Act on them as given, and do not re-derive them.
- **Records.** The design records are under `memory/builds/dClosedLoop/build/`, each named
  `<date>-build-PLAY-dClosedLoop-1-<name>.md`. A record cites its sections as `[tag]`. v2 is
  `2026-10-14-...-architecture-v2.md`. The away pass's record is `2026-10-18-...-away-pass.md`, and point 4's
  research return is `2026-10-18-...-research-compatibility.md`: read its sections on platforms and the
  interpreter before anything else.
- **Point 4 as designed (P37):** a role per language, Python for logic, shell as thin shims, JavaScript on the
  harness's surfaces, new and rebuilt code moving to Python by a shrink-only ratchet. A declared platform matrix:
  Windows with Git-Bash and Linux (WSL2 or native) at tier 1, macOS unsupported until a node runs it. Keys
  `platforms.supported` (any subset of windows-gitbash, linux, macos, pwsh-launch; default windows-gitbash, linux;
  never set by a preset) and `platforms.verify` (held until the Linux half is green, then ci). Both keys are owned
  by dShippedRelease; the portability leg pack is dWitnessedBar's.
- **Measured in the away pass:** under WSL Ubuntu 22.04, Python resolves to 3.10 and `tomllib` fails, node is
  absent, and a worktree's gitdir pointer holds a Windows path WSL's git cannot open. `tools/lib/resolve-python.sh`
  accepts a Python below the floor and prefers the Microsoft Store alias, which spawns about four times slower than
  the direct executable on this node. PowerShell as the launch shell passed its fixture, but there `bash` resolves
  to WSL's.
- **Supersession (P38):** a change an adopter can see ships as a release-chained upgrade step with up and down
  steps, so raising the interpreter floor later is itself an upgrade step every adopter walks.

**The question.** Two parts.
1. **The Python floor.** Does gov need a Python newer than 3.11, now or within the chain's horizon? Price each
   candidate floor, 3.11, 3.12, 3.13 and 3.14, by:
   - what gov's tracked Python uses today, as a census of version-bound features and modules (the feature, the
     version that introduced or removed it, and the count of uses with a file:line sample), including modules
     removed by PEP 594 in 3.13;
   - what the chain's designed units would want: the supervisor, the trace verbs, the conformance fixture, the
     gates' parallel runs, typed returns and TOML reading and writing;
   - each version's end of life, verified from python.org, against the chain's likely horizon;
   - availability and provisioning on each promised and planned platform: Windows (python.org installer, the Store,
     the Python install manager), Ubuntu 22.04 and 24.04, Debian 12, macOS, and any provisioning tool you would
     recommend;
   - the cost of raising the floor later, as an upgrade step under P38, against raising it now.
2. **The future plan for macOS and pwsh-launch.** What each needs before gov could promise it. Measure the blockers
   on today's tree: bash 4+ features against macOS's bash 3.2, GNU-only tool flags against BSD tools, timeout and
   coreutils gaps, case-insensitive filesystems, Python and node provisioning, and for pwsh-launch which entry
   points a PowerShell launch reaches and how `bash` resolves there. Name the runner each would use, the trigger
   that would start the work, and price the plan as units and gaps on the chain build that owns each part. The plan
   is planned, not promised: `platforms.supported` keeps its default.

**How to work:**
- Read only. Write no file in the repository, and run no generator in write mode, no bar, no gate leg and no
  self-test suite. Install nothing, on Windows or in WSL, and change no interpreter, package or PATH; a version that
  is not present is priced from its documentation. A probe or a throwaway copy lives only under
  `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/away/d113/`,
  spelled literally, since `$TMPDIR` is unset in the Bash tool.
- A record is evidence. Verify against the code any claim your answer depends on, and say where a record and the
  code disagree.
- Cite file:line for every claim, and a URL for every external fact. Show each measuring command with its output.
- Return at most 2,500 words, in the sections below. Prefer tables.

**Return these sections:**
1. **Verdict:** at most 150 words: the floor, and the plan for each platform, one line each.
2. **The floor:** the census, the units' wants, end of life, availability, the cost of a later bump, and each
   candidate with its losing test and result.
3. **macOS:** the blockers measured, the runner, the trigger, units and gaps.
4. **pwsh-launch:** the same.
5. **Chain, gaps and forks:** units by build, gaps with their owning build, keys, and the owner's forks with options
   and a recommendation. A behaviour the owner may switch is a policy key with a default and its allowed values.

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
