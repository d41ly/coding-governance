**Serves:** journal TOOL-dWitnessedBar-1

# Build brief — TOOL-dWitnessedBar-1

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 23.
- Built so far through order 22: every unit up to and including 4, 25, 40, 23, 42, 3, 44, 5, 41, 55 and 8
  (`dd90f8abb`: flake quarantine and the `flake` record kind). This spec was re-grounded over them at `965b98c9c`.
- Units 1 and 59 build at order 23 IN PARALLEL in this one working tree. Their Files touched are disjoint: stage
  explicit paths only, never `git add -A`, and never stage, edit or revert a path the other unit's spec names. The
  session card routes both units, so each builder may flip its own spec's status.
- COMMIT THROUGH A CLEAN CLONE. The other sibling's uncommitted files make the pre-commit hook's build-index and
  codebase-map checks read stale in this tree. Commit as units 44 and 41 did: clone this branch to a short path under
  `%TEMP%`, apply only your own paths there, regenerate the index and the map there, commit through the hooks in a
  linked worktree of that clone, then move this branch forward with a compare-and-swap `git update-ref` from the base
  you started at and align only your own paths in this tree. Never `--no-verify`. If the branch moved under you,
  rebase your commit in the clone onto the new tip and retry.
- The pass legs carry one known red: install-prefix on the `conf-scalar-pins` seed argv in
  `tools/memory-tree/kit.toml`, held until unit 51. The full `memory hygiene` leg is red at base on checks 13 and 15
  from other records; the main loop owns those at the close. Any other red is this unit's to fix.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-1`, its trailer block carrying `Pass: TOOL-dWitnessedBar-1`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-1-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
