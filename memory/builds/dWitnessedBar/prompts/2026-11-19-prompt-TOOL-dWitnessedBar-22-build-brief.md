**Serves:** journal TOOL-dWitnessedBar-22

# Build brief — TOOL-dWitnessedBar-22

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 6.
- Built so far: units 26, 27, 48, 49, 50, 13, 15 and 61, and unit 12 (`6b3f271c6`: a `tag` on every row of
  `tools/gate-legs.json` and every descriptor `[[gate_leg]]` row, `LEG_KEYS` gaining `tag`, the `leg`, `pack` and
  `check` namespaces, run-gates at 1.51 and govkit's `LEG_KEY_FLOORS`). Read those files as they stand: this unit's
  edge fields land on the rows unit 12 tagged, and any new leg key follows the floor pattern unit 12 set.
- The spec is rev-4, re-grounded while unit 12 was still a contract; where unit 12's landed code differs from what the
  spec assumed, hand it back as a divergence.
- Unit 47 builds after this unit at the same order.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-22`, its trailer block carrying `Pass: TOOL-dWitnessedBar-22`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-22-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
