**Serves:** journal TOOL-dWitnessedBar-47

# Build brief — TOOL-dWitnessedBar-47

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 6.
- Built so far: units 26, 27, 48, 49, 50, 13, 15, 12 and 61. This unit edits the ledger factory as units 13, 15 and 61
  left it: read `tools/lib/legacy_ledger.py` whole as it stands, including unit 15's `check_home_admitted` and unit
  61's `read_head_sha` and `NULL_SHA`, before building on any claim the spec makes about it.
- The spec is rev-6, re-grounded before units 15 and 61 landed; where their landed code differs from what the spec
  assumed, hand it back as a divergence.
- Unit 15's builder noted that a fresh adopt prints `unarmed` for the untracked `memory/map` until this unit lands, and
  that arm 6 of `tools/codebase-map/adopt-codebase-map.test.sh` may read that.
- Unit 22 builds after this unit at the same order; its spec is being revised and touches none of these files.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-47`, its trailer block carrying `Pass: TOOL-dWitnessedBar-47`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-47-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
