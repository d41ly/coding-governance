# Phase 0 brief: the unit spec's criteria marked as Phase 0 met them

**Serves:** research PLAY-dClosedLoop-1

The handoff for dispatch 245 renders from this brief record through `handoff.py render --role gov-spec-writer`. Phase 0
ran on node d from 2026-10-20 to 2026-10-21, and the opening is committed on `branch/unruffled-aryabhata-d89ede`.
The handoff asks that each of AC6 to AC12 be marked done in the unit spec as it is met, by the spec-writer role.

## The prompt

Revise `spec/2026-10-20-spec-PLAY-dClosedLoop-1.md` so its §6 states, for each criterion Phase 0 reached, DONE or
OPEN with the record that shows it, its §8 states F2 as settled by the owner's answer, and its H1 takes the form the
roles kit and the driver's plan reader read.

## The brief

### Goal

The unit spec reflects Phase 0 as the records show it, so the owner's opening read and the agent ledger read one
current spec: AC1, AC2 and AC6 to AC12 each marked from its record, F2 settled, and the H1 written as
`# PLAY-dClosedLoop-1 — <title>` with an em dash, which `tools/roles/handoff.py:763` (`^# ([A-Z]+)-<build>-([0-9]+) — `)
and `tools/unattended/unattended.sh --plan` require (today both read the spec as no unit: "no spec … defines a unit
id on its first line" and "NOT A UNIT (no status header)").

### Items

1. **H1:** the colon after the id becomes ` — `; the title words are unchanged. Re-check with `python
   tools/roles/handoff.py agents --handoff memory/builds/dClosedLoop/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-61-builder.md`
   that the ledger note no longer says no spec defines a unit id, and with `bash tools/unattended/unattended.sh --plan
   dClosedLoop --paths` that the spec is read as a unit; report both outputs. If the second still says NOT A UNIT, find
   why from the reader's source and fix the header form only if the template allows it; otherwise report it.
2. **§6, each criterion, from its record** (read each before writing it; cite the record by path and section):
   - AC1: the nine execution rows `PLAY-dClosedLoop-2` to `-10` in `memory/DECISIONS.md`, each in full in
     `build/2026-10-21-build-PLAY-dClosedLoop-1-phase0-decisions.md`; still OPEN on F3, the design rounds' answers.
   - AC2: `memory/LIVE.md` lists all 22 chain builds, and each chain README carries its stage H1 and `parents:` line
     (the main loop measured 22 of 22 at `ff5fbaf43`).
   - AC6: `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-deviations-instruments.md` (`## P0.1 and P0.2`) and
     `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-carries-instruments.md`, against P0.1 as revised.
   - AC7: the same deviations record, P0.2's plants.
   - AC8: `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-packet-instruments.md` and
     `build/2026-10-21-build-PLAY-dClosedLoop-1-phase0-checks.md` `[ac8]`.
   - AC9: `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-schedule-redtests.md`, row 9 fixed by its `## Finding 15`.
   - AC10: `build/2026-10-21-build-PLAY-dClosedLoop-1-phase0-checks.md` `[checks]` and `[red-tests]`.
   - AC11: the decisions record, each row quoting its answer.
   - AC12: `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-nodes.md`: on node d three of the four observations
     hold and the resume tick is not registered, the owner's act; nodes a and b are OPEN.
   Where a criterion's wording no longer matches the revised plan (P0.1, P0.2 and P0.7 were revised on 2026-10-20 at
   the owner's answers, `build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md` `[phase0-answers]`), say so in the
   criterion rather than rewording it silently.
3. **§8:** F2 settled by the owner's answer 4 in `[phase0-answers]`, quoted verbatim. F1 stays as it is until the
   landing. F3, F4 and F5 stay open.
4. **§9:** a revision entry, and the header's `rev-N` moved only if `memory/TEMPLATE-SPEC.md` counts these edits as
   material.

### Acceptance

- Every §6 status cites a record you read for this pass; no status is asserted without one.
- `memory/TEMPLATE-SPEC.md`'s Tier-2 canon still holds, and no line begins with an AC label outside the criteria list.
- No unit id that no build has minted appears bare.

### Gates

None of the bar's legs. The main loop runs the spec-tokens leg and memory hygiene on the staged spec.

### Non-goals

- Your tree is the main loop's worktree. Edit only the unit spec; never commit, the main loop does.
- No edit to the execution plan, v2, any record, instrument or decision row. No new decision: an open question stays
  an F-item.
- Probes go under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unruffled-aryabhata-d89ede/1cef2554-91c7-4cd1-9950-7f33d1289103/scratchpad/d245/`
  only, as files, never through a heredoc; never delete anything outside it.
