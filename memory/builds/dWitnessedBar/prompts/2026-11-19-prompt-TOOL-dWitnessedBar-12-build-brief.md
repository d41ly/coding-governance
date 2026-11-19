**Serves:** journal TOOL-dWitnessedBar-12

# Build brief — TOOL-dWitnessedBar-12

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 5.
- Built so far: units 26, 27, 48, 49 and 50 (the `resolve_bash_py` block, `tools/lib/refuse-wrong-shell.sh` with its
  `--coverage` population, `scan_bare_bash`), unit 13 (`tools/lib/legacy_ledger.py`, section `2o` of
  `tools/lib/resolve-python.test.sh`) and unit 15 (`test.seed` at every check's registration; read what its pass
  committed before building on it).
- The spec is rev-6, re-grounded at `98e33d71c`: 198 manifest rows, 70 `[[gate_leg]]` rows in 27 descriptors, `LEG_KEYS`
  the landed keys plus `tag`, `owed_rows.py` reading `LEG_KEYS`, and `derive_kit_rows` shared by `extract_check` and
  `extract_command`. §8 F6 points each namespace row at a plain path, F7 puts `leg` and `pack` in `layer.flow` and
  `check` in `layer.distribution`, F8 names the rows `[[numbered_check]]`, and F9 spells the policy kit's owner
  segment `policy-kit`. Its ask TOOL-dWitnessedBar-34 closes with this pass.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-12`, its trailer block carrying `Pass: TOOL-dWitnessedBar-12`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-12-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
