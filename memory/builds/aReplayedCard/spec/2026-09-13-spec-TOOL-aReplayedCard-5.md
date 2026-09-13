# TOOL-aReplayedCard-5 — `orient-counterfactual.js` measures one stage-2 arm per call

**Status:** SPECCED · rev-2 · 2026-09-13 · node a · Tier-1 · base c4f02308 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 |
| [2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md](../reviews/2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 |
| [2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 |

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
  `{repo, task, arm: {agent, recall, reuse}}`. The run count is FIXED at two by a marked constant
  literal, `const RUNS = [0, 1]` carrying `gov:fixed-verifiers`, iterated by a `for (const i of
  RUNS)` header carrying `gov:sequential-agents(2)`, so the two kickoffs run one after the other
  and never share the repository's wall clock. Each agent is spawned with the arm's type, told to
  run the kickoff engine's Steps 0–4 for `task`, to run or skip the recall probe and the reuse
  probe per the arm, and to return the READY line, the card bytes it would append, and its own
  start and end epoch milliseconds read with `date`. The script records `budget.spent()` before
  and after each spawn as the run's token figure. Observed by AC1 and AC2.
- **S2** The script RETURNS the record — the arm, each run's token delta and wall, and the READY
  lines — because a workflow script has no filesystem access. The caller writes it under
  `memory/builds/<slug>/build/` in the ledger grammar, and the README says so in one line. Observed
  by AC1 and AC2.
- **S3** `tools/workflows/orient.agent.template.md`, the custom agent definition the design
  record's section 2.8 specifies — tools Read, Grep, Glob and Bash, no Write, no Edit, no Agent, no
  worktree isolation — shipped as a template. The harness's README states the install: copy it to
  `.claude/agents/orient.md` for the run and remove it after; nothing in this build wires it.
  Observed by AC3.
- **S4** Every run carries a closed `outcome` field — `spawned`, `null`, `threw` or
  `refused-step` — so a dead arm is a named value the caller can grep, never a zero: a spawn that
  throws is caught and recorded as `threw` with the message; a null return, which is the harness's
  documented dead-agent shape, is `null`; an agent that spawned but reports it could not execute
  a step, an Explore-typed one refused Bash say, is `refused-step` with the step named, and the
  script then re-runs that arm once with the default workflow agent type, recording which type
  ran. Observed by AC1 and AC3.
- **S5** The script passes `tools/hooks/agent-cap.js` WITH the sequential marker: the one loop is
  the marked `for (const i of RUNS)` over the marked literal, and it calls no raw primitive.
  Observed by AC4.

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
read. Functions the script defines are graded by the js probe cell of `.lexicon.conf`, so they
lead with table verbs: `runArm`, `measureRun`, `renderRecord`.

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
- risks — the design record's §7 decision 2 records as UNVERIFIED whether an Explore-typed agent
  can run Bash and the Skill tool, which bears on the Explore half of the matrix; S4's
  `refused-step` outcome and fallback record the answer rather than a zero. Whether a definition
  copied to `.claude/agents/` mid-session is spawnable is a second unknown the record does not
  state; AC3 settles it.
- testing — `check-workflow-syntax.js` on the script; AC1 runs one arm.
- migration — none.
- user docs — the workflows README.

## 6. Acceptance criteria

- **AC1** — When the harness is invoked once with `arm: {agent: "Explore", recall: true, reuse:
  true}` on this repository, its return holds two runs, each with an `outcome` field, a token
  delta and a wall figure, the second run's start is after the first run's end, and that return is
  written to this build's `build/` folder; a run whose outcome is not `spawned` names the type that
  ran in its place or the reason none did.
  Red when: a run returns null and the record reports zero for it, or the two runs overlap.
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
  both, and the fan-out check names the marked sequential loop as the one loop it admitted.
  Red when: the loop is unmarked and read as an unbounded fan, or the file does not parse as an
  async function body.

## 7. Gates

`workflow script syntax` · `verifier fan-out` · `review-join ban (no ref-keyed join)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · §4 · §5 · §7 · S1 · S4 · S5 · AC1 · AC4 · folded the round-1 spec audit.
  The run count is a marked two-element literal iterated by a `gov:sequential-agents(2)` loop, so
  the kickoffs never overlap and the hook admits the shape (M6); every run carries a closed
  `outcome` and an Explore arm that cannot run a step falls back to the default type, recorded
  (M7); the design record's decision 2 is cited for what it says (M7); the lexicon and
  install-prefix legs join §7 and the functions lead with table verbs (L3).

## 10. Reuse audit

The seam is `tools/workflows/tier2-review.js` — its `args` parse and refusal at lines 47–76, its
inlined bounded helpers, and the `{path, summary}` return shape the charter's §8 asks for. The
reuse probe returned no workflow seam by name; the shape was read from that file and from
`unattended-unit.js`, which is the one-unit-per-call precedent this harness copies as
one-arm-per-call.

Recall terms used: `counterfactual orient subagent Explore agent type probe set recall reuse matrix tokens wall READY workflow harness budget spent`
