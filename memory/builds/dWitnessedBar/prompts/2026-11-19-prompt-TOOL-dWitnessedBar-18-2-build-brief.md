**Serves:** journal TOOL-dWitnessedBar-18

# Build brief — TOOL-dWitnessedBar-18, second builder

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 12.
- Built so far through order 11: units 26, 27, 48, 49, 13, 50, 15, 12, 61, 22, 47, 19, 11, 14, 45, 54, 16, 46, 17
  (`dbbd8caba`: keyed record and row populations, `{prefix}` resolved in every seed argv by the factory, a fresh
  scaffold writing neither waiver home), 52 (`fd73e0bbb`: `ratchet.py#read_root_confs`) and 53 (`b4d0b0f50`).
- The first builder stopped before writing code; its return is
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-18-1-builder-return.md`. The spec is now
  rev-7: `landed-steps` is seeded by `upgrade_steps.py list --ids`, every step id the graded tree declares and no
  ref (§8 F6, F8), and `tools/memory-tree/ratchet.py` carries the `append-removed` plant. Read the rev-7 spec whole;
  hand back any claim the landed code breaks as a divergence.
- A ledger home or step program sits outside any `tools/<kit>/` path or behind `{prefix}`, which the factory now
  resolves in seed argvs: `install-prefix (shipped surface)` takes no waiver.
- The pass legs carry one known red: install-prefix on the `conf-scalar-pins` seed argv in
  `tools/memory-tree/kit.toml`, held until unit 51. The full `memory hygiene` leg is red at base on checks 13 and 15
  from other records; the main loop owns those at the close. Any other red is this unit's to fix.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-18`, its trailer block carrying `Pass: TOOL-dWitnessedBar-18`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-18-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
