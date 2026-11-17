**Serves:** journal TOOL-dDeclaredLoop-80

# Build brief — TOOL-dDeclaredLoop-80

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dDeclaredLoop's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. Every unit through build order 37 is built, and unit 67 of order 38 (6bc52aca7, the round-2 audit's kept minors) is built with red-fixes 73a62e8d6 and 59d8c5773. Unit 76's no-own-conf-read plant reds the budget and breakpoint fixture legs until this unit lands; greening them is this unit's job. The spec is rev-6, re-grounded with unit 67 dispatched first; it renames write_pre_placement_tree to its _plant spelling and carries edits of units 86, 88 and 90 early.
- The spec's base is older than the run's: verify each claim about current code against source before building on it, and
  hand a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dDeclaredLoop-80`, its trailer block carrying `Pass: TOOL-dDeclaredLoop-80` beside
  the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dDeclaredLoop/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed. Run
  `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger `memory/builds/dDeclaredLoop/build/2026-11-17-build-TOOL-dDeclaredLoop-80-1-acceptance-ledger.md`
  in the pass commit: one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, the ledger and every generated file included. A
  file on the kickoff manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map
  needs the map generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are `report`
  and `author-recorded`.
