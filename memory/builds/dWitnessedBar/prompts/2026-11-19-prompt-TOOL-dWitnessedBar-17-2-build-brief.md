**Serves:** journal TOOL-dWitnessedBar-17

# Build brief — TOOL-dWitnessedBar-17, second builder

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 11.
- Built so far through order 10: units 26, 27, 48, 49, 13, 50, 15, 12, 61, 22, 47, 19, 11, 14 (the `ratchet` pack,
  `conf-scalar-pins`), 45, 54, 16 (`87bc9f615`, `3ce285ad7`: gov's registries on the ledger,
  `tools/memory-tree/convert_registry.py`, the four lists once under `tools/` now in `memory/project/`) and 46
  (`028b97364`: the adopter's `seed_scalar_pins` and `--seed-pins`, `keys-not-scalar` red when unarmed, the seven
  gov-only legs as exempt rows).
- The first builder stopped at a divergence, its return
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-17-1-builder-return.md`, committing nothing.
  The spec is now rev-7 (`da9345429`): this unit converts and registers `corpus-path-unresolved.txt` itself, with its
  reader change in `corpus_ids.py`; it arms checks 13 to 15 on a home that exists rather than on a read-back seed;
  and S9 resolves `{prefix}` in a seed argv inside the factory. Read the rev-7 spec whole; the earlier return is
  background, not the contract.
- The pass legs carry one known red: install-prefix on the `conf-scalar-pins` seed argv in
  `tools/memory-tree/kit.toml`, held until unit 51. Any other red is this unit's to fix.
- Units 52 and 53 (re-grounded at rev-5 over this spec) build after this unit at the same order.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-17`, its trailer block carrying `Pass: TOOL-dWitnessedBar-17`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-17-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
