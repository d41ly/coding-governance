**Serves:** journal TOOL-dDeclaredLoop-45

# Build brief — TOOL-dDeclaredLoop-45

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dDeclaredLoop's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. Orders 1 to 17 are complete, and order 18 is under way: repair unit 112 made --plan read each spec's ask verbs once, and unit 14 added the frontier and the refusal route to tools/loop/position.py and the driver's --refused verb. This unit continues order 18 beside unit 69 and arms a built unit's acceptance in position.py.
- The spec's base is older than the run's: verify each claim about current code against source before building on it, and
  hand a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dDeclaredLoop-45`, its trailer block carrying `Pass: TOOL-dDeclaredLoop-45` beside
  the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dDeclaredLoop/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed. Run
  `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger `memory/builds/dDeclaredLoop/build/2026-11-15-build-TOOL-dDeclaredLoop-45-1-acceptance-ledger.md`
  in the pass commit: one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, the ledger and every generated file included. A
  file on the kickoff manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map
  needs the map generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are `report`
  and `author-recorded`.
