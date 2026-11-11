# Build brief — TOOL-dFairHearing-25, pass (b): the placement wording and the clones

**Serves:** research TOOL-dFairHearing-25

Build pass (b) of this unit from `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-25.md`, its latest rev (rev-6), as its §4 "The passes and the orchestrating commit" states pass (b). Pass (a) is `d3c98d523`. The first two calls, on `fhr1a` and `fhr2a`, were denied by the opt-in pack before any agent ran; rev-6's §8 F3 moves the subject under this build and S10 starts the attempts at `b`.

## This pass

- Commit the remaining `tools/workflows/README.md` changes: S8's placement wording for the two placed paths, the replay-1 paragraph, and §8 F4's rewording of the two switch sentences. Observe AC8 and AC5's README half.
- The spec stays INPROGRESS: pass (c) flips it.
- After the commit, make `fhr1b` and `fhr2b` by the committed procedure and observe AC1 over both, and AC2's pack probe (the placed subject admitted, the dClosedLoop subject path denied).
- Stage each call's Workflow arguments as JSON in the run's scratch root, `fhr1b-args.json` and `fhr2b-args.json`, as S2 states them: the placed subject path and its `id`, `reviewDir`, the sibling `specs`, run 1 or run 2, the clone's own checklist, `preset: 'design-audit'`, and a per-run `scratch` subfolder. The context sentence naming where to write the report names `reviewDir`, not run B's dClosedLoop path; the main loop changed it in pass (a)'s staged files, and pass (c) records it as a departure. Return both paths.
- Leave `fhr1a` and `fhr2a` on disk.

## Standing rules

- Before you commit, run `python tools/lexicon/lexicon.py --check` (your role's one gate) and read its `verb offenders <n> over pin <m>` line: your commit must not raise `<n>` above what it read at your pass's start.
- Route the session card to this unit with `manifest-check.sh --card --append` BEFORE the first write; never copy a drafted file into the tree with `cp` or any other shell write to get past the write gate.
- Run no gate leg, no suite and no bar.
- Declare with `--dispatch` every path the commit will carry, one `--writes` flag per path, the generated renders a hook forces into it included. Never declare the run-state file `RUN.md`.
- Writes stay inside the spec's files touched and this build's folder. Clones and fixtures go under `%TEMP%/<short-name>`; other temp files go in the run's scratch root.
- A spec criterion a correct build cannot pass is a `DIVERGENCE:` naming the criterion, never a build around it.
