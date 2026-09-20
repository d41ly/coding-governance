# Brief — TOOL-aReplayedCard-5, the stage-2 counterfactual harness

**Serves:** journal TOOL-aReplayedCard-5

What this pass is handed: the unit's spec at rev-2 (Tier-1, CLEAN WITH FIXES at round 1, folded),
the build README, `tools/workflows/tier2-review.js` as the shape to copy for its `args` parse and
refusals, `tools/workflows/unattended-unit.js` as the one-unit-per-call precedent, and
`tools/hooks/README.md` for the fan-out grammar the hook enforces.

What it builds: `tools/workflows/orient-counterfactual.js`, one arm per Workflow call over the
matrix {agent type: custom `orient` or Explore} × {memory-recall in/out} × {reuse-lookup in/out},
two sequential kickoffs per call, and `tools/workflows/orient.agent.template.md`, the custom agent
definition the harness's README tells a runner to copy to `.claude/agents/orient.md` for a run and
remove after. Nothing here wires the agent; owner decision 1.

What is not obvious:

- **You cannot run the harness.** A sidechain agent holds neither the `Agent` nor the `Workflow`
  tool, so AC1 and AC3 are the ORCHESTRATOR's to observe after you return. Write the acceptance
  ledger with AC1 and AC3 in the OBSERVED form naming the harness invocation the orchestrator will
  make, and say in your return value that they are owed to the parent; the parent appends the
  observation to your ledger record. Your own observations are AC2 (the record's fields), AC4 (the
  two checks below), and that the script parses.
- **The fan-out hook reads the script at the `Workflow` call, and its grammar is strict**
  (`tools/hooks/README.md`, "What the hook DENIES"): the run count is `const RUNS = [0, 1]` on a
  line carrying `// gov:fixed-verifiers`, iterated by exactly one `for (const i of RUNS) {` header
  carrying `// gov:sequential-agents(2)` as a line comment, with `await agent(` directly inside,
  no enclosing loop, no arrow between the header and the call, and no raw `parallel(` or
  `pipeline(` anywhere. Verify with `bash tools/workflows/check-verifier-fanout.sh` and
  `node tools/workflows/check-workflow-syntax.js`; both are bar legs.
- **No `Date.now()`, `Math.random()` or `new Date()` in a workflow script** — they throw. Wall is
  the agent's own `date +%s%N` at its first and last Bash call, returned in the schema; tokens are
  `budget.spent()` deltas around each spawn, which count the workflow's output tokens and the
  record says so.
- **Every run carries a closed `outcome`** — `spawned`, `null`, `threw`, `refused-step` — and an
  Explore arm that reports it could not run a step is re-run once with the default agent type,
  recording which type ran. `agent()` returns null for a dead agent and throws on a terminal
  error; catch both.
- **The script returns the record; it cannot write a file.** The README says the caller writes the
  return under `memory/builds/<slug>/build/` in the ledger grammar.
- **A kit file names nothing outside itself by literal**: the repo path, the task and the arm
  arrive in `args`; the script spells no `memory/` or `skills/` path and no sibling kit path.
  `install-prefix (shipped surface)` grades every tracked `tools/*` and `*.template.*` file.
- **Functions lead with a table verb** — the js probe cell of `.lexicon.conf` grades
  `orient-counterfactual.js`; the spec names `runArm`, `measureRun`, `renderRecord`. `main`, `cmd`
  and `test` are reserved.
- **The kit descriptor**: `tools/workflows/kit.toml`'s `**` rule ships the script; the dossier
  `memory/map/features/review-harnesses.md` claims workflow-script keys — add both new files to
  the claims the coverage inventory enumerates (`python tools/codebase-map/gen_map.py --check`
  names what is unclaimed). Add one section to `tools/workflows/README.md`: the matrix, the
  install of the agent template, the record and the caller's write.
- **The acceptance ledger** is `2026-09-14-build-TOOL-aReplayedCard-5-1-acceptance-ledger.md`
  under `build/`, `**Serves:** journal TOOL-aReplayedCard-5`, one `**Evidences:**` block; keep
  every backticked token of an answer on the bullet's first physical line.
- **Author with the Write tool, LF; finish with the records**: spec status CLOSED with today's
  date, `gen_build_index.py --write`, `git add -A`, the hygiene gate (minutes, never through
  `tail`), `python tools/check-spec-tokens.py`, the two workflow checks above, and commit with the
  unit id in the subject. No push, no merge.
