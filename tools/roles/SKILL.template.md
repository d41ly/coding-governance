---
name: build
description: Drive an ATTENDED code build through the harness pipeline an unattended run uses - spec writers, the spec audit where the owner declared one, one builder per unit, the closing review and one bar - with every agent spawned as its rendered role. Use after /session-kickoff's READY card and the owner's go, for a build that writes product code. Do NOT use for a run that merges and pushes with no owner turn, which is /unattended, or for a change that writes no product code.
---
<!-- gov:kit roles@1.3 -->

# Attended builds

This Skill is a ROUTER. The procedure is `{{MEMORY_ROOT}}/guides/BUILD-METHOD.md`: read it WHOLE
before stage 3, and it wins any difference. The stages below are the workflows of
`{{KIT_DIR}}/workflows.toml`, in its stage order. Every `handoff.py` here is
`python {{KIT_DIR}}/handoff.py`, and every `unattended.sh` is `bash {{TOOL_ROOT}}unattended/unattended.sh`.

## Before stage 3

- The orientation card carries a READY line and a `## task` whose eight fields are filled, the brief
  sits under `{{MEMORY_ROOT}}/builds/<slug>/prompts/`, and the owner's go is quoted under its
  `## Owner confirmation`. Any of the three missing: stop, and run `/session-kickoff`.
- No run-state file exists, so this run is ATTENDED: the one driver verb used is
  `unattended.sh --plan <slug> --paths`. Merge and push each wait for the owner's explicit ask.
- A fork goes to the owner through `AskUserQuestion`, never to a park: no mandate delegates it (M3).
- You write no freeform agent prompt. A direct spawn is an `Agent` call whose `subagent_type` is the
  role and whose `prompt` is the output of this line, unchanged:
  `python {{KIT_DIR}}/handoff.py render --role <role> --build <slug> --unit <id> --input <key>=<value> --part task`
  Every harness call carries `roles`, the JSON `handoff.py harness-args <harness>` prints, and
  `efforts`, the JSON `handoff.py stage-efforts <workflow>` prints for the workflow that call runs.
- Every agent the session dispatches or receives is reported by pasting, unchanged, what
  `handoff.py agents --handoff <path>` prints for a direct spawn, or `handoff.py agents --run <run-id>`
  for a harness call. Run it once the call returns and again when its notification arrives; the
  same run adds each complete line to the build's agent ledger.

## Stage 1 — orient

`/session-kickoff` ran it; nothing runs here.

## Stage 2 — reuse

A card carrying a `## reuse` section had its scout run at kickoff, and the spec writers read it.
Otherwise they read the card's `**Reuse:**` field. This Skill spawns no scout.

## Stage 3 — spec-write

Read `unattended.sh --plan <slug> --paths`, then call `{{TOOL_ROOT}}workflows/unattended-build.js` by
`scriptPath` as the verbs guide's "Drive the build as ONE program" bullet composes it
(`{{MEMORY_ROOT}}/guides/UNATTENDED-VERBS.md`), with these differences: `mode: 'attended'`; every
`units[]` entry carries its `planState` from that read; no `runStateExists`; `base` is the READY
line's; `roles` from `handoff.py harness-args unattended-build`; `efforts` from
`handoff.py stage-efforts spec-write`; `specAudit` only where the build
README declares `spec-audit:`. Act on its `nextAction`.

## Stage 4 — spec-review

Stage 3's harness runs it as its AUDIT stage, and only where `specAudit` was passed (M4).

## Stage 5 — build

Until `--plan --paths` prints `next: none - every tracked spec is terminal`, for the next READY unit:

1. set its spec's status to INPROGRESS and its date to today, an edit touching nothing else: the
   owner's go is the approval INPROGRESS records;
2. append a `## route` naming the unit, as the brief skeleton's route lines say, through the kickoff
   check script's `--card --append`;
3. call the hand-out's `dispatch.scriptPath` with `dispatch.args` plus `unitId`, `specPath`,
   `briefPath`, `roles` from `handoff.py harness-args unattended-unit` and `efforts` from
   `handoff.py stage-efforts build`, on every dispatch;
4. on `diverged: true`, write a revision record under the build's `prompts/` holding `## The brief`
   and no `## The prompt`, its Goal the builder's `why` verbatim and its other four sub-heads copied
   from the build's brief; spawn `gov-spec-writer` on it with `--input spec=<path> --input
   prompt=<that record>`; then dispatch the unit again. On any other `committed: false`, stop and bring
   the `why` to the owner.

## Stage 6 — closing-review

Call `{{TOOL_ROOT}}workflows/tier2-review.js` as M8 composes it, adding `roles` from
`handoff.py harness-args tier2-review` and `efforts` from `handoff.py stage-efforts closing-review`.
Each blocker's fix is a pass of the unit it lands in: write
the finding into a fix record under `prompts/`, set that unit back to INPROGRESS by the same
status-only edit, and dispatch it with that record as `briefPath`. Then re-review the fix (M8).

## Stage 7 — gate-bar

`bash {{TOOL_ROOT}}run-gates/run-gates.sh`, once, after the last unit is terminal; the governing
doc's merge-bar section decides its flags.

## Wrap-up

M9's derivation. Then ask before any merge or push.

## Shared with /unattended

| Stage | Shared carrier | Here, and why |
|---|---|---|
| orient | `/session-kickoff` | it ran before this Skill; a mandated run runs it after preflight |
| spec-write, spec-review | the build harness, M4 | `mode: 'attended'`, because no run-state file exists |
| build | the unit harness, M6 | no recording verbs; the main loop flips INPROGRESS and routes each unit |
| closing-review | M8 | identical, roles included |
| gate-bar | the merge bar | the main loop runs it; under a mandate the run's close does |
| wrap-up | M9 | identical |
| landing | the charter's `[land]` rule | the owner's ask; a mandate lands by its protocol |
