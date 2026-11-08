# Build brief — TOOL-dFairHearing-25, pass (a): the procedure and the clones

**Serves:** research TOOL-dFairHearing-25

Build pass (a) of this unit from `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-25.md`, its latest rev. The unit splits in two passes because its replay-1 runs are `tier2-review.js` Workflows, which a builder cannot start: the main loop runs them between your pass and pass (b), as it did for `TOOL-dFairHearing-1`. Unit 15's half of the spec (S4, AC4, AC6 and the unit-15 lines of S5 to S7) is superseded by `TOOL-dFairHearing-30` and is not built here.

## This pass

- S8 and S9: add the placement step to the replay section of `tools/workflows/README.md`, with its one EXIT trap, and observe AC8, including its forced-bundle-failure fixture under `%TEMP%/fpl`.
- Commit that change as this pass. The spec stays INPROGRESS: pass (b) flips it.
- After the commit, make replay 1's two first-attempt clones by that procedure, `%TEMP%/fhr1a` and `%TEMP%/fhr2a`, from the S2 placement commit, and observe AC1 over both, including the refused second run into `fhr1a` and the empty `git for-each-ref refs/replay/`.
- Stage each run's Workflow arguments as a JSON file in the run's scratch root, `fhr1a-args.json` and `fhr2a-args.json`: spec 1 §4 "The isolation"'s arguments (run B's from its comparison record, `repo` the clone, `scratch` the session scratchpad, `preset: 'design-audit'`) plus S2's `reviewDir`. Return both paths, and the command that prints `gotchas.py --for-paths` in each clone, as run.
- Name in your return the orchestrating-commit rule of S7: the main loop reads `HEAD` before the first run, and commits nothing between the runs and pass (b)'s commit.

## Standing rules

- Before you commit, run `python tools/lexicon/lexicon.py --check` (your role's one gate) and read its `verb offenders <n> over pin <m>` line: your commit must not raise `<n>` above what it read at your pass's start.
- Route the session card to this unit with `manifest-check.sh --card --append` BEFORE the first write; never copy a drafted file into the tree with `cp` or any other shell write to get past the write gate.
- Run no gate leg, no suite and no bar.
- Declare with `--dispatch` every path the commit will carry, one `--writes` flag per path, the generated renders a hook forces into it included. Never declare the run-state file `RUN.md`.
- Writes stay inside the spec's files touched and this build's folder. Clones and fixtures go under `%TEMP%/<short-name>`; other temp files go in the run's scratch root.
- A spec criterion a correct build cannot pass is a `DIVERGENCE:` naming the criterion, never a build around it.
