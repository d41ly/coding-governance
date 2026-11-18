**Serves:** journal TOOL-dDeclaredLoop-27

# Build brief — TOOL-dDeclaredLoop-27

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dDeclaredLoop's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. Orders 21 to 23 are built: units 81, 78, 85, 25 (splice.py, the stage kind), 29 (upstream.py) and 26 (composition.py: the composition transition field, read_composed_items(rev), position read at the pin) are committed. 27 rev-4 was re-grounded on 26's spec, not 26 as built.
- The spec's base is older than the run's: verify each claim about current code against source before building on it, and
  hand a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dDeclaredLoop-27`, its trailer block carrying `Pass: TOOL-dDeclaredLoop-27` beside
  the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dDeclaredLoop/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed. Run
  `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger `memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-27-1-acceptance-ledger.md`
  in the pass commit: one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, the ledger and every generated file included. A
  file on the kickoff manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map
  needs the map generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are `report`
  and `author-recorded`.
