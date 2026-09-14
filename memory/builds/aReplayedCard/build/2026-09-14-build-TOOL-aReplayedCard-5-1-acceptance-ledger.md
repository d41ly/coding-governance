# Acceptance ledger — TOOL-aReplayedCard-5, the stage-2 counterfactual harness

**Serves:** journal TOOL-aReplayedCard-5

Every figure here was observed by the pass at its dispatch tree (`d62c9092`, the branch tip the
unit was dispatched from) and re-checked at the staged landing tree. Two criteria are NOT this pass's
to observe: a sidechain agent holds neither the `Agent` nor the `Workflow` tool, so AC1 and AC3 name
the invocation the orchestrator makes after this unit lands, and the orchestrator appends its
observation beneath each. Until it does, those two lines are a debt this record states, not a claim.

## What shipped

- `tools/workflows/orient-counterfactual.js` — 219 lines; parses under `check-workflow-syntax.js`
  as an async function body; the one loop is `for (const i of RUNS) { // gov:sequential-agents(2)`
  over `const RUNS = [0, 1] // gov:fixed-verifiers`, with `await agent(` inline; the fallback is one
  `await agent(` after the loop under no loop at all. Three definitions, every one leading with a
  declared verb: `renderPrompt`, `buildOpts`, `measureRun`.
- `tools/workflows/orient.agent.template.md` — the `orient` definition, frontmatter `tools: Read,
  Grep, Glob, Bash`, `model: inherit`, `maxTurns: 60`; nothing installs it.
- `tools/workflows/README.md` — one section: the matrix, the call, the install, the record.
- `memory/map/features/review-harnesses.md` — claims `orient-counterfactual.js` under
  `workflow-scripts`; the template yields no inventory key, measured by `gen_map.py --check` before
  the claim, which named the script alone.

## The predicate, probed both ways

The fan-out check prints a count on admission and nothing per loop, so "the check names the loop
it admitted" cannot be read off a green run. It was read off a RED one instead: three copies of the
script under `mktemp`, each fed to `check-verifier-fanout.sh` by explicit path.

| copy | change | verdict |
|---|---|---|
| unmarked | `// gov:sequential-agents(2)` deleted from the header | RED — `L168: r = await agent(renderPrompt(i), buildOpts(i, arm.agent))` · `agent() inside a loop body` |
| arrow | an arrow inside the call's argument list, after `agent(` | clean — the arrow is not between the header and the call, so it defers nothing |
| three | `RUNS = [0, 1, 2]` under a marker still naming 2 | clean — the receiver is a three-element literal, still under the file constant |

The unmarked RED is the observation AC4 (rev-3) asks for: remove the marker and the loop is refused
as the unbounded shape, so the marker is what admits it and the loop is the one it admits.

## Gates at the staged tree

- `node tools/workflows/check-workflow-syntax.js` — `6 workflow script(s) parsed clean`, exit 0
- `bash tools/workflows/check-verifier-fanout.sh` — `6 workflow script(s) obey the ≤5-verifier rule`, exit 0
- `bash tools/workflows/check-review-join.sh` — clean, exit 0
- `python tools/lexicon/lexicon.py --check` — `lexicon OK — 1953 tracked file(s)`, exit 0; the
  verb-offender pin did not move, so the three new definitions are all inside the table
- `bash tools/check-install-prefix.sh` — `carried-prefix clean — 135 recorded file(s), 35
  hand-justified, none rising`, exit 0; the README section spells the new files by bare name and the
  call by `{kit}/`, so `tools/workflows/README.md` stays at its four carried literals
- `python tools/codebase-map/test_codebase_map.py` — 6 ok, exit 0, after `gen_map.py --write`

**Evidences:** TOOL-aReplayedCard-5

- AC1 — `Workflow { scriptPath: 'tools/workflows/orient-counterfactual.js', args: { repo: '<this worktree>', task: '<a task>', arm: { agent: 'Explore', recall: true, reuse: true }, engine: 'skills/session-kickoff/SKILL.md' } }` — OWED TO THE ORCHESTRATOR: this pass holds no `Workflow` tool. The orchestrator makes that call once, writes the return under this build's `build/` folder, and appends beneath this line: each run's `outcome`, `tokens` and `wallMs`, the record's `sequential` value, and the `fallback` entry if any. Red as written: a run whose `outcome` is not `spawned` and whose line carries no `reason`, or `sequential: false`.
  Observed by the orchestrator, 2026-09-14, run `wf_237795b3-22b`, record `2026-09-14-build-TOOL-aReplayedCard-5-2-counterfactual-explore-arm.md`: `sequential: true`; run 1 Explore `spawned`, tokens 19665, wallMs 299315; run 2 Explore `refused-step` — reason: the agent would not run `git fetch` under its own no-mutation rule and substituted `--dry-run` — tokens 19172, wallMs 266116; `fallback` for run 2 under the default type `spawned`, tokens 28546, wallMs 472483. Both runs' cards carry the recall ids and the reuse verdict, so Explore holds Bash and the two probes; the UNVERIFIED in the spec's §5 is settled that far.
- AC2 — `budget.spent()` — the record's `tokensNote` field states, verbatim, that each `tokens` is the `budget.spent()` delta around that spawn, the workflow's OUTPUT tokens while the agent ran, and not the subagent's total context; `arm` carries `agent`, `recall`, `reuse` and the record's top level carries `repo` and `task`. Observed in the script's return literal at the staged tree; the written copy inherits it because the caller writes the return.
- AC3 — `arm.agent: "orient"` — OWED TO THE ORCHESTRATOR, two calls: first with no `orient` definition under `.claude/agents/`, expecting `verdict` to read `arm unavailable: orient — …` with each run's `reason` carrying the spawn's own refusal; then with `orient.agent.template.md` copied to `.claude/agents/orient.md`, expecting either a `spawned` run or a `threw`/`null`/`refused-step` outcome naming what the harness saw. The orchestrator appends both verdicts beneath this line. What this pass observed: the script derives `verdict` from the spawned count and never emits a measurement for a run whose outcome is not `spawned` — `tokens` is the delta read, `wallMs` is null.
  Observed by the orchestrator, 2026-09-14, runs `wf_fb1eaab5-04d` and `wf_adb06a03-7e0`: with no definition, `verdict` reads `arm unavailable: orient — run 1 threw: agent({agentType}): agent type 'orient' not found …; run 2 threw: …`, tokens 0, wallMs null, `fallback: null` — a named refusal, never a zero. With `orient.agent.template.md` copied into this worktree's agents directory as `orient.md` and the harness invoked again in the same session, the verdict is byte-identical: the harness's agent registry is read at session start, so a definition copied in mid-session is NOT spawnable, and the matrix run must start its session with the definition already present. The definition was removed after the call.
- AC4 — amended rev-3 — `bash tools/workflows/check-verifier-fanout.sh` and `node tools/workflows/check-workflow-syntax.js` both exit 0 at the staged tree with the new script in their population; the same check over an unmarked copy REDS naming `L168` and the loop's `agent(` call, as the table above records. The amendment: the criterion asked the check to NAME the loop it admitted, which no output of the gate or the hook does; rev-3 asks for the RED on the unmarked copy instead, and its §9 line logs it.
