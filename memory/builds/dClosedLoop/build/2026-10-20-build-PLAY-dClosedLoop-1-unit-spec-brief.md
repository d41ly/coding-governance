# Unit spec brief: what the writer of PLAY-dClosedLoop-1's spec reads, writes and settles

**Serves:** research PLAY-dClosedLoop-1

The unit spec writer's `input:spec`. Its handoff brief is
`build/2026-10-20-build-PLAY-dClosedLoop-1-unit-spec-handoff-brief.md`.

## [write]

One new file and nothing else: `memory/builds/dClosedLoop/spec/2026-10-20-spec-PLAY-dClosedLoop-1.md`.
- **H1:** `# PLAY-dClosedLoop-1: ` followed by the unit's title.
- **Status header:** `**Status:** INPROGRESS · rev-1 · 2026-10-20 · node d · Tier-2 · base 742957fc · streams
  playbook+kickoff+tooling+deployer`. These are the build README's streams and the kickoff's base, and the unit is in
  progress because Phase 0 remains.

Your scratch folder is `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/exec/d232/`.
Probes and drafts go there and nowhere else. Make no model or network call, and run none of the bar's legs.

An id no build has minted is written `missing:<id>`. Another build's id never leads a table cell, a heading or a list
item: put a word first.

## [read]

- The build README, `memory/builds/dClosedLoop/README.md`: its problem, improvements, rules and front matter.
- The kickoff record, `memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md`: the owner's
  prompt verbatim, the brief and the route. It holds the unit's goal, IN and OUT scope, to-do and acceptance check.
- The design: v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`, its
  `[clause-ids]` with its `Baseline:` line, and `[chain]`; the gap register,
  `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md`.
- The audit: `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, its `[baseline]`.
- The execution: `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md` and the plan
  `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md`, whose `[phase-0]` is the
  unit's remaining work.
- The session log's Events, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md`, for
  the unit's history.
- `memory/TEMPLATE-SPEC.md` whole, the canon you write to; `tools/gate-legs.json` for leg names; `memory/HYGIENE.md`
  for record and id rules.

## [settle]

- **What the unit is.** A design-only unit. It researched, designed, audited and froze gov's re-architecture (v2 at
  baseline `59ff8f2ac`). It planned the chain's execution, and its Phase 0 opens the chain. Its product is records
  under `memory/`, never product code.
- **§4 Design points, never restates.** Name each record that holds the design: v2, the gap register, the audit, the
  execution plan, and their sections. Restating them would make two answers to one question.
- **§6 Acceptance** carries:
  - the kickoff's acceptance check, (a) to (d);
  - the baseline taken;
  - Phase 0's acceptance as the plan states it.

  Mark each criterion done or open, citing the record that shows it.
- **§7 Gates** lists the legs the kickoff named, as `tools/gate-legs.json` names them, and the full bar before any
  landing.
- **§8** holds as open F-items:
  - Phase 0 itself;
  - the atlas, at 16.4 MB with the execution records and past its 16 MB limit;
  - any other question the records leave open.
- **§9:** one rev-1 line saying the spec was written at the landing, 2026-10-20, because check 21 binds a record only
  to a spec H1, and the unit's design had lived in its build records.
- **§10:** the reuse facts as the template requires, citing what the unit reused: the map, the gate-legs manifest,
  the drift audit, the build method, the build index generator, the roles kit's handoffs and the tier-2 harness.

## [return]

Your final message gives:
- the spec's path and size;
- each acceptance criterion, done or open, with its citation;
- every leg §7 names;
- anything the canon required that the records could not supply, as a question.
