**Serves:** journal TOOL-dWitnessedBar-51

# Build brief — TOOL-dWitnessedBar-51

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 31.
- Built so far through order 29: every unit up to and including 4, 25, 40, 23, 42, 3, 44, 5, 41, 55, 8, 1, 59, 30, 29,
  7, 21, 6, 2 and 43 (`5308f3c08`). Unit 28 (order 30) is deferred against asks TOOL-dWitnessedBar-101 to -103 and is
  not built; this spec, rev-6, was re-grounded at `510f79a69` without its edge onto unit 28.
- This unit builds alone; nothing else is in flight in this working tree, so commit directly here.
- The driver sits at its refusal-site ceiling (343 sites, 339 armed, DERIVED from unit 21's builder probe).
- Every earlier pass carried one red, install-prefix on `tools/memory-tree/kit.toml`'s `conf-scalar-pins` seed argv;
  this unit's S51 fixes it. The full `memory hygiene` leg is red at base on checks 13 and 15 from other records; the
  main loop owns those at the close. Any other red is this unit's to fix.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-51`, its trailer block carrying `Pass: TOOL-dWitnessedBar-51`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-51-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
