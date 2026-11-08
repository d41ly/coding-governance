# Build brief — TOOL-dFairHearing-30, pass (a): the per-arm step, the clones and the eight calls staged

**Serves:** research TOOL-dFairHearing-30

Build pass (a) of this unit from `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-30.md`, its latest rev. The unit splits in two passes, as `TOOL-dFairHearing-25` did: its eight runs are `tier2-review.js` Workflows a builder cannot start, so the main loop runs them between your pass and pass (b). S8 binds the verdict record's commit to the orchestrating commit as its first parent, so pass (b)'s commit follows the runs with nothing committed between. Scoring and the decision are superseded by `TOOL-dFairHearing-35` (this spec's hands-off edge); this unit records the attempts and keeps the evidence.

Read unit 25's pass (b) and (c) returns first (`memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-25-2-builder-return.md` and `2026-11-04-build-TOOL-dFairHearing-25-3-builder-return.md`) and its verdict record (`2026-11-04-build-TOOL-dFairHearing-25-replay-verdicts.md`): the same procedure, its scripts in the run's scratch root, the opt-in pack's subject rule, and the void rule's transcript probe all carry over.

## This pass

- S7: add the per-arm step of §4 to the replay section of `tools/workflows/README.md`, and observe AC5 and AC2's dirty-clone and stale-name halves on their fixtures.
- Commit that change as this pass. The spec stays INPROGRESS: pass (b) flips it.
- After the commit, make the eight first-attempt clones `f1s1` to `f4u1` by the committed procedure at each record's range head (spec 15 §4's corpus), and observe S2's clean status for each.
- Stage each of the eight calls' Workflow arguments as JSON in the run's scratch root, `f<r><a>1-args.json`, from spec 15 S5's arms and instrument: the clone as `repo`, the diff kind's subject, each arm's checklist as spec 15 states it, and a per-call `scratch` subfolder. Check each payload against the live opt-in pack and agent-cap rules with a stdin probe of `tools/hooks/agent-cap.js`, so no call is refused at the tool boundary. Return the eight paths and anything a call needs that the spec leaves open.
- Return the per-arm block, ready to run per clone, with `SCRATCH` and `ORCH` set, so the main loop writes `run.log` as S7 states.

## Standing rules

- Before you commit, run `python tools/lexicon/lexicon.py --check` (your role's one gate) and read its `verb offenders <n> over pin <m>` line: your commit must not raise `<n>` above what it read at your pass's start.
- Route the session card to this unit with `manifest-check.sh --card --append` BEFORE the first write; never copy a drafted file into the tree with `cp` or any other shell write to get past the write gate.
- Run no gate leg, no suite and no bar.
- Declare with `--dispatch` every path the commit will carry, one `--writes` flag per path, the generated renders a hook forces into it included. Never declare the run-state file `RUN.md`.
- Writes stay inside the spec's files touched and this build's folder. Clones and fixtures go under `%TEMP%/<short-name>`; other temp files go in the run's scratch root.
- A spec criterion a correct build cannot pass is a `DIVERGENCE:` naming the criterion, never a build around it.
