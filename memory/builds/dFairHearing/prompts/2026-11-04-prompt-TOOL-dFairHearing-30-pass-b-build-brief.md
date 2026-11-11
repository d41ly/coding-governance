# Build brief — TOOL-dFairHearing-30, pass (b): the verdict record

**Serves:** research TOOL-dFairHearing-30

Build pass (b), the last pass, of this unit from `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-30.md`, its latest rev, after the main loop has run the eight calls. This brief is committed before the runs so that nothing is committed between them and this pass's commit, which S8 and AC6 require. The facts of the runs (the orchestrating commit and the three S7 blobs, every attempt's clone, status, Workflow run id, result file and transcripts) are in the run-facts file the main loop writes in the run's scratch root, `u30-run-facts.md`, which your dispatch's ground names; read it first.

## This pass

- Apply spec 1's void rule to every completed attempt with unit 25's transcript probes, and record each outcome and void cause in S9's attempt rows. If an attempt is void or failed and its record and arm has no eligible attempt left under unit 35 S1's rule, stop and return what the main loop must re-run; commit nothing.
- Write the S5 verdict record and the manifest (unit 23 S4's terms; scoring and the decision are `TOOL-dFairHearing-35`'s), with every departure named, and observe AC1, AC2's record half, AC4, AC6 and AC7.
- Commit them in one commit, setting the spec to CLOSED, touching none of S8's three files and no product file of spec 15 S6.

## Standing rules

- Before you commit, run `python tools/lexicon/lexicon.py --check` (your role's one gate) and read its `verb offenders <n> over pin <m>` line: your commit must not raise `<n>` above what it read at your pass's start.
- Route the session card to this unit with `manifest-check.sh --card --append` BEFORE the first write; never copy a drafted file into the tree with `cp` or any other shell write to get past the write gate.
- Run no gate leg, no suite and no bar.
- Declare with `--dispatch` every path the commit will carry, one `--writes` flag per path, the generated renders a hook forces into it included. Never declare the run-state file `RUN.md`.
- Writes stay inside the spec's files touched and this build's folder.
- A spec criterion a correct build cannot pass is a `DIVERGENCE:` naming the criterion, never a build around it.
