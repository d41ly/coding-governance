# Execution brief: what the plan's writer reads, writes and settles

**Serves:** research PLAY-dClosedLoop-1

The plan writer's `input:spec`. Its handoff brief is `build/2026-10-20-build-PLAY-dClosedLoop-1-execution-handoff-brief.md`.

## [write]

Two new files, and nothing else in the repository:

- `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md`, the plan. It opens with
  one H1, then `**Serves:** research PLAY-dClosedLoop-1`. Its sections are named by bracketed tags, as the build's
  other records are, never by number.
- `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`, the schedule script. It parses
  v2's `[chain]` itself, asserts 22 builds and 509 clauses, and prints the plan's schedule table, each node's load and
  the first wave. Its docstring names its inputs, its model and what it does not model.

Your scratch folder is `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/exec/d219/`.
Probes and drafts go there and nowhere else, and nothing in any other scratch folder is yours to change. Make no
model call and no network call. Run none of the bar's legs.

A unit id that no build has minted is written `missing:<id>`, never bare, so the build index does not join it into a
roster (the memory tree's own marker). A prior id never leads a table cell, a heading or a list item: put a word first
(`| id TOOL-x-3 | …`), or hygiene reads it as defined here.

## [read]

- The owner's question, the outline the owner was shown, the four answers and the main loop's readings of them:
  `build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md` `[question]`, `[presented]`, `[answers]`, `[readings]`.
- The five returns, each with its facts cited: `build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-driver.md`,
  `-coordination.md`, `-handoffs.md`, `-schedule.md` and `-deviation.md`.
- Their probe scripts and the main loop's two checks: `-research-exec-instruments.md`, whose `[verified]` holds the
  checks. The schedule researcher's `planj.py`, `heft.py`, `stale.py` and `schedule.py` are there to reuse.
- The design: v2 `build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`, its `[chain]`, `[clause-ids]`,
  `[policies]`, `[presets]` and `[owed]`; `build/2026-10-19-build-PLAY-dClosedLoop-1-final-questions.md`, its
  bootstrap list and `[deviation]`; the bootstrap instruments `build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py`,
  `-deviations.py` and `-asbuilt.py`; the gap register `build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md`.
- Today's machinery, wherever a step rests on it: `memory/guides/UNATTENDED-PROTOCOL.md`, `UNATTENDED-VERBS.md`,
  `UNATTENDED-STOPS.md`, `memory/guides/BUILD-METHOD.md`, `memory/TEMPLATE-SPEC.md`, `memory/HYGIENE.md`,
  `tools/unattended/unattended.sh`, `tools/workflows/unattended-build.js`, `tools/push-main.sh`, `.unattended.conf`,
  `tools/roles/handoff.py`, `skills/session-kickoff/`.

Re-verify any fact a return states before a step rests on it. Recalled or handed facts are background.

## [sections]

The plan carries these sections, in this order.

- `[answer]`: the plan in brief, with its bad news first.
- `[constraints]`: what today's gov forces on the plan, each fact cited.
- `[phase-0]`: dClosedLoop's remaining work before any node starts, each item with its acceptance and the red test
  that proves it. At least these items:
  - The three instruments hardened against every escape and false red the deviation and handoffs returns found, each
    fix seen red on its plant.
  - The packet instrument: its fields, its byte re-render check and its completeness arms.
  - The schedule script, run again at every landing.
  - The opening of the chain in one landing. It covers each README's front matter, stage, `parents:`, the roster
    mapped to clause ids, `spec-audit:`, and the `may:` grant derived from the paths of the nodes the build owns,
    saying exactly how that derivation runs. It also covers the packet, the `readme-contract.txt` rows, the README
    slot contract, and the backlog ask each build's spec-run close needs.
  - Two opening hazards: the existing citations of not-yet-minted dTrueNorth unit ids in the build's records and
    instruments, which `gen_build_index.py --write` joins into dTrueNorth's README once its folder exists; and which
    session may mint ids in a chain build's backlog.
  - The opening's gates and its one landing on the owner's ask.
  - The policies the owner's answers ratify, as decision rows.
  - Each node's preparation, node b's onboarding to gov included.
- `[phase-1]`: dTrueNorth on node a as the pilot. Its steps, what it proves, and how its product controls take over
  from the instruments without a gap: the cutoff date, how long both run together, and the clauses that retire each
  instrument.
- `[phase-2]`: the chain itself. The spec run (its close through carry-forward, as the owner ratified) and the build
  run, step by step. How a fork is resolved when nothing may park. What the owner sees at each spec landing.
- `[handoffs]`: the packet and the per-pass brief. What a cold session on any node reads, in order. How a packet is
  kept current as parents land.
- `[coordination]`: the node loop, the claim rules, landing, conflicts, shared records, asks across builds, and what a
  node does when it finds another node's work in its way.
- `[schedule]`: the table, pasted with its command line. The dispatch rule. The first wave. Makespan and load per
  node.
- `[sync-points]`: each landing that changes what nodes load, and what each in-flight build does then. This includes
  the driver's successor after dWellOiledMachine.
- `[deviations]`: the owner's rule applied (`[readings]`). What is recorded where, the end-of-build departures report
  (generated: from what, listing what), the as-built roll-up, what still detects strictly, and what nothing catches.
- `[per-node]`: a runbook for each of nodes a, b and d. Its setup, its first assignment, its loop, its actions at
  sync points, and what it does when blocked.
- `[owner]`: the owner's own steps: land the opening, start each run, read each spec landing's coverage, read each
  build's departures report, rule on what the plan leaves open.
- `[cannot]`: what today's gov cannot do for this plan, the union of the five returns' lists, each with its smallest
  change and that change's kind.
- `[defaults]`: the decisions the plan carries as recommended defaults for the owner's walk, each with its options.
  At least these:
  - the builds that rewrite their own driver (dDeclaredLoop, dPlacedRequest, dWellOiledMachine), reconciled with the
    owner's "the build must go through to completion";
  - dPlacedRequest's claim migration: a test that a live claim on another node survives it, or a drain;
  - how dTrueNorth's comparison replaces the instruments: bootstrap legs first, or the product absorbing the plant
    suite as its acceptance;
  - who starts each run;
  - the two deviation keys' values after the chain.
- `[disagreements]`: where the returns disagree, which the plan follows, and why.

## [settle]

Points the returns leave open, which the plan must answer from the records:

- **Forks when nothing may park.** Today a fork with no delegated resolver parks, and a parked decision turns the
  run's landing into an owner hand-off (`UNATTENDED-VERBS.md`, `BUILD-METHOD.md`). State what lets a run resolve every
  fork itself and record it for the end report, using only today's driver and the owner's grants. If nothing does,
  name the smallest change.
- **The spec-run close, end to end.** Give the exact verbs and records a spec run uses to close through carry-forward
  and land: every unit `DEFERRED`, a rescope row each, the backlog ask, `ASKS_CMD`, and the closing review over the
  spec commits. Then say how the later build run on another node picks the deferred specs up. Cite each step.
- **Node b's slice.** Model b as eligible for both phases at its lower pace. Sweep the pace from 0.25 to 0.5 of a or
  d. Prefer phases with slack over the critical path. Report the makespan and each node's load for each pace, and
  what the owner's "smaller slice, preferably non-critical" assigns b.
- **What the owner starts.** The owner's act starts every run. Count the runs the plan asks the owner to start, and
  say when, from what the schedule script prints.

## [return]

Your final message: the two paths and their sizes; the schedule script's command line, output and exit code; every
reading of the owner's answers you found wrong or incomplete, as a question; each `[defaults]` item with its
recommended option; and anything you could not settle, with what would settle it.
