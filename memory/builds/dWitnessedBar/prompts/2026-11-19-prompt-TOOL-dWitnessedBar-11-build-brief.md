**Serves:** journal TOOL-dWitnessedBar-11

# Build brief — TOOL-dWitnessedBar-11

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 8.
- Built so far: units 26, 27, 48, 49, 50, 13, 15, 61 and 47, and three units that moved this unit's files after its
  spec was re-grounded: unit 12 (`9dbb7bc44`: a `tag` on every leg, the `leg`, `pack` and `check` namespaces, run-gates
  1.51, govkit's `LEG_KEY_FLOORS`), unit 22 (`44eb041c6`: `tests` and `enforces` on leg rows and descriptors, selfcheck
  7h comparing both, selftest run g, canary floor 458) and unit 19 (`7c5a3989a`: a `purpose` on every leg, run-gates
  1.52, selfcheck 7h's purpose arms, selftest runs h and i, canary floor 459). Read those files as they stand.
- The spec is rev-6, re-grounded before units 12, 22 and 19 landed; where their landed code differs from what the spec
  assumed (a key set, a floor, a version, a selftest run letter, a descriptor's row shape), hand it back as a
  divergence rather than building around it.
- Unit 22's leg-row edge site marks a three-part `practice.<p>.<rule>` enforces target unarmed until the tag index
  learns the member form; any respelling of those values this spec owns lands on the rows as unit 22 left them.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-11`, its trailer block carrying `Pass: TOOL-dWitnessedBar-11`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-11-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
