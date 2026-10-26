**Serves:** research TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8

# Close observation brief — batch A, the policy-check New arm: lines

## The prompt

> Every roster unit of dGroundRules is terminal (TOOL-dGroundRules-67 at 4f76c4b39 closed the guard sweep). BUILD-METHOD M8 owes each `New arm:` line a RED-first observation at the close, recorded in the unit's ledger.

## The brief

### Goal
For each of TOOL-dGroundRules-1, TOOL-dGroundRules-2, TOOL-dGroundRules-3, TOOL-dGroundRules-4, TOOL-dGroundRules-5, TOOL-dGroundRules-6, TOOL-dGroundRules-7, TOOL-dGroundRules-8: read its CLOSED spec's `New arm:` lines that name `tools/policy/check_policy.py` (a `--fixture <case>` set or an `ARMS` arm; skip lines naming any other suite, which the main loop observes itself), and observe each one at the close as BUILD-METHOD M8 asks: RED on the line's staged break, then GREEN once restored. Work only in a `git clone --shared` of this worktree at HEAD under `%TEMP%/<short-name>` (one clone per break, removed afterwards); write nothing in the worktree. Run each case singly (`python tools/policy/check_policy.py --fixture <case>`) or the arm the line names; never the whole `--fixture` suite, which is the close's leg. Take the break the line states; where it says the case plants its own break, RED is the case run against the unit's product change rolled back (`git show <unit's commit>^:<product file>` over the clone's copy, the unit's commit found with `git log --grep 'Pass: <unit id>'`), and say which. A line counts observed when its break reds at least one of the assertions it covers; say how many. Return, per unit, ONE paragraph ready to append to that unit's acceptance ledger under `memory/builds/dGroundRules/build/`: `The New arm: line(s) of this unit on tools/policy/check_policy.py were observed at the close, in a scratch clone of <HEAD sha>:` then, per line, the break, the RED output line(s) quoted and the GREEN result, each backticked token on one line. Report plainly any line you could NOT observe red, with the reason; never invent an output.

### Non-goals
Any write to a tracked file; any commit; the whole `--fixture` run; any other suite.

### Acceptance
One ledger paragraph per unit, or the reason a line could not be observed.

### Gates
No gate runs in this pass.

### Limitations
Other close runs share the machine; a slow case is load, not a red.

### Reuse
Each unit's own acceptance ledger records how its builder staged the break in its pass.
