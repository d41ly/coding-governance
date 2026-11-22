**Serves:** journal TOOL-dWitnessedBar-46

# Build brief — TOOL-dWitnessedBar-46

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 10.
- Built so far: units 26, 27, 48, 49, 13, 50, 15, 12, 61, 22, 47, 19, 11 (the gate-leg factory), 14 (`25a3d2970`: the
  `ratchet` pack, the `conf-scalar-pins` registration and its `keys-not-scalar --measure` seed), 45 and 54, and unit
  16 (`3a7a51471`, `450f7b322`: gov's registries converted onto the ledger, `tools/memory-tree/convert_registry.py`,
  the step program `tools/govkit/steps/registry_to_ledger.py`, and the four lists that sat under `tools/` moved to
  `memory/project/`).
- The spec is rev-6, re-grounded before unit 16 landed; read the memory-tree kit's descriptor, its exempt rows and its
  adopter as they stand now, and hand back any claim unit 16's landed shape breaks as a divergence.
- Unit 17's rev-6 later re-points this unit's scaffold arm at one planted pin (its F7); build the arm as this spec
  says.
- The pass legs carry one known red: install-prefix on the `conf-scalar-pins` seed argv in
  `tools/memory-tree/kit.toml`, held until unit 51. Any other red is this unit's to fix.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-46`, its trailer block carrying `Pass: TOOL-dWitnessedBar-46`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-46-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
