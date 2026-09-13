# TOOL-aReplayedCard-5 — `orient-counterfactual.js` measures one stage-2 arm per call

**Status:** SPECCED · rev-1 · 2026-09-13 · node a · Tier-1 · base c4f02308 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 |

<!-- /gen:spec-records -->

## 1. Goal

Stage 2 of the orientation design, the `orient` subagent, is deferred behind a measurement nobody
has run: whether main-context occupancy is worth a slot, a child load and the loss of the ask. The
owner widened that measurement to a matrix — agent type {custom `orient`, Explore-typed} by probe
set {memory-recall in or out, reuse-lookup in or out} — each arm measured as tokens and wall to
READY over two matched kickoffs. Ship the harness that runs ONE arm per call and records it, so
the next session can run the matrix rather than design it.

## 2. Scope (IN)

- **S1** `tools/workflows/orient-counterfactual.js`, a Workflow script taking `args`
  `{repo, task, arm: {agent, recall, reuse}, runs}`. It spawns `runs` kickoff agents of the arm's
  type from a two-element array literal, sequentially, each told to run the kickoff engine's Steps
  0–4 for `task`, to run or skip the recall probe and the reuse probe per the arm, and to return
  the READY line, the card bytes it would append, and its own start and end epoch milliseconds read
  with `date`. It records `budget.spent()` before and after each spawn as the arm's token figure.
  Observed by AC1 and AC2.
- **S2** The script RETURNS the record — the arm, each run's token delta and wall, and the READY
  lines — because a workflow script has no filesystem access. The caller writes it under
  `memory/builds/<slug>/build/` in the ledger grammar, and the README says so in one line. Observed
  by AC1 and AC2.
- **S3** `tools/workflows/orient.agent.template.md`, the custom agent definition the design
  record's section 2.8 specifies — tools Read, Grep, Glob and Bash, no Write, no Edit, no Agent, no
  worktree isolation — shipped as a template. The harness's README states the install: copy it to
  `.claude/agents/orient.md` for the run and remove it after; nothing in this build wires it.
  Observed by AC3.
- **S4** An arm whose agent type cannot be spawned is a named refusal in the record, never a zero:
  the script catches the throw and returns `arm unavailable: <reason>`. Observed by AC3.
- **S5** The script passes `tools/hooks/agent-cap.js` unmarked: its only fan is a two-element
  literal and it calls no raw primitive. Observed by AC4.

## 3. Non-goals (OUT)

- No wired `orient` agent, no `SubagentStop` hook, no engine Step 0 clause. Owner decision 1.
- No run of the matrix in this build. The build leaves the harness; the measurement is the next
  session's, and its result decides stage 2.
- No token figure for the MAIN loop's occupancy. `budget.spent()` counts output tokens across the
  workflow; the record says so, and the main-context bytes are the design record's table 2.9.

### Edges

- **consumes-from** `KICK-aReplayedCard-1` — the card the Explore arm reads at Step 1, once wired;
  without it every arm runs the batch and the comparison is still valid, only slower.
- **hands-off** external — the matrix run and the stage-2 decision.

## 4. Design

One Workflow call per arm; eight calls for the matrix. `Date.now()` is unavailable inside a
workflow script, so wall is measured by the agent with `date +%s%N` at its first and last Bash call
and returned in the schema; the harness never stamps time itself. Tokens are `budget.spent()`
deltas, which count the workflow's own output tokens and are the only per-agent figure a script can
read.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/workflows/orient-counterfactual.js` | new |
| `tools/workflows/orient.agent.template.md` | new |
| `tools/workflows/README.md` | one section: the matrix, the install, the record |
| `memory/map/features/review-harnesses.md` | claims the new keys |

## 5. Production-readiness checklist

- security — the agent definition grants no write tool.
- perf / scale — one arm is two kickoffs; the matrix is sixteen.
- error / empty / loading states — S4.
- observability — the record per call.
- risks — the agent definition's discovery time is UNVERIFIED (design record §7 decision 2); AC3
  settles whether a definition copied in mid-session is spawnable.
- testing — `check-workflow-syntax.js` on the script; AC1 runs one arm.
- migration — none.
- user docs — the workflows README.

## 6. Acceptance criteria

- **AC1** — When the harness is invoked once with `arm: {agent: "Explore", recall: true, reuse:
  true}` and `runs: 2` on this repository, its return holds two runs, each with a non-zero token
  delta and a wall figure, and that return is written to this build's `build/` folder.
  Red when: a run returns null and the record reports zero for it.
  cost: two Explore-typed kickoffs, minutes.
- **AC2** — When that written record is read, it names the arm's four fields and states that the
  token figure is the `budget.spent()` output-token delta.
  Red when: the figure is presented as the subagent's total context.
- **AC3** — When the harness is invoked with `arm.agent: "orient"` and no definition named
  `orient` exists under `.claude/agents/`, the record reads `arm unavailable` naming the type;
  when `orient.agent.template.md` is copied there and the harness is invoked again, either the arm
  runs or the record names the refusal the harness saw. Either outcome is recorded; a silent zero is the red.
  Red when: an unspawnable arm reports a measurement.
- **AC4** — When `node tools/workflows/check-workflow-syntax.js` and
  `bash tools/workflows/check-verifier-fanout.sh` run at the landing commit, the new script passes
  both.
  Red when: the fan is read as unbounded or the file does not parse as an async function body.

## 7. Gates

`workflow script syntax` · `verifier fan-out` · `review-join ban (no ref-keyed join)` · `codebase-map coverage + freshness` · `memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

The seam is `tools/workflows/tier2-review.js` — its `args` parse and refusal at lines 47–76, its
inlined bounded helpers, and the `{path, summary}` return shape the charter's §8 asks for. The
reuse probe returned no workflow seam by name; the shape was read from that file and from
`unattended-unit.js`, which is the one-unit-per-call precedent this harness copies as
one-arm-per-call.

Recall terms used: `counterfactual orient subagent Explore agent type probe set recall reuse matrix tokens wall READY workflow harness budget spent`
