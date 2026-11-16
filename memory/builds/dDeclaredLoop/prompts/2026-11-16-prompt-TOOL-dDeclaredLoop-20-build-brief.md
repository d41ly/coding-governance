**Serves:** journal TOOL-dDeclaredLoop-20

# Build brief — TOOL-dDeclaredLoop-20

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dDeclaredLoop's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. Units through order 30 are built: 21 (review bounds), 30/48/49/61/60/62 (the rework budget and its homes), 32 (convergence routing, --fix-pass, budget.py target) and 31 (6a3174eb0, --exhausted, the ending rows, census 335). 20 rev-5 was grounded at 02524cadf while 31 built: read 31's code as shipped. Its decision row (ceiling 335 -> 338, Skill row 10848 -> 10922) has landed. Unit 50 (order 32) writes the review [[item]] rows; you write none.
- The spec's base is older than the run's: verify each claim about current code against source before building on it, and
  hand a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dDeclaredLoop-20`, its trailer block carrying `Pass: TOOL-dDeclaredLoop-20` beside
  the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dDeclaredLoop/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed. Run
  `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger `memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-20-1-acceptance-ledger.md`
  in the pass commit: one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, the ledger and every generated file included. A
  file on the kickoff manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map
  needs the map generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are `report`
  and `author-recorded`.
