# Fix brief — TOOL-dFairHearing-37: AC1 against the built records, and two New-arm breaks unit 32 already fixed

**Serves:** research TOOL-dFairHearing-37

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Revise `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-37.md` so a correct build of it passes on today's tree. Its builder returned a DIVERGENCE before any write; read `memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-37-1-builder-return.md` first. Commit nothing; the main loop commits.

### Items
1. AC1's first half says every path `git show --name-only --format= <c30>` lists sits under `memory/builds/dFairHearing/` or is `tools/workflows/README.md`. Unit 30's verdict commit db0f99c71 also lists `memory/LIVE.md` and `memory/backlog/TOOL.md`, the generated renders the build-index hook forces into every pass commit. Restate the predicate so it holds on a correct build and still reds on the defect it names (for example: no path under `tools/` other than `tools/workflows/README.md`, or an explicit allow-list of the generated renders).
2. AC1's second half names "the commit that adds unit 35's manifest". Unit 35 (a4fbcbf33) adds no manifest; it modifies unit 30's. Give the half a referent that exists.
3. §7's `New arm:` lines for AC5 and AC14 name staged breaks against unit 32's code (`replay_scorer.py`'s ls-files spelling and `check_ungated`'s closer class), but unit 32 (fb755fa80) already fixed both, so each arm stays green on its declared break. Name a staged break that fails on today's code for each (the builder suggests S31's spelling after the verb, and the closer class narrowed to one character). Correct S5's and S15's sentences that describe code already holding.
4. Check each remaining criterion against the built records of units 25, 30, 32, 35 and 36, as the return's probe list reports them, and §6's backticked words against `tools/check-spec-tokens.py`'s `BAR` pattern (:419-424).
5. Rev bump and one §9 line per change, naming this brief. Leave the status header's state as it is.

### Acceptance
Every criterion a correct build can pass on today's tree; every `New arm:` line names a break that reds on today's code.

### Gates
None you run.

### Non-goals
No other spec, no code.
