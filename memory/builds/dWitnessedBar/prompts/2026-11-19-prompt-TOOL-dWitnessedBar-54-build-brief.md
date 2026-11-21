**Serves:** journal TOOL-dWitnessedBar-54

# Build brief — TOOL-dWitnessedBar-54

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 10.
- Built so far: units 26, 27, 48, 49, 13, 50, 15, 12, 61, 22, 47, 19, 11 (the gate-leg factory), 14 (the `ratchet`
  pack) and unit 45 (`383e7b739`: `regen.check_when` admits `exists:<path>`, the factory's `[[generated]]` row in
  `tools/run-gates/kit.toml` carries `when = "exists:{prefix}/govkit/govkit.py"`, and a row whose `when` fails is
  reported skipped). This unit lands in the same merge as unit 45: govkit selfcheck refuses the `exists:` form until
  this unit's S2 admits it, so the pass legs run once over both.
- The spec is rev-5, re-grounded at `4e5497fb7`; read unit 45's row as it landed and hand back any claim it breaks as a
  divergence.
- The pass legs carry one known red: install-prefix on the `conf-scalar-pins` seed argv in
  `tools/memory-tree/kit.toml`, held until unit 51. Any other red is this unit's or unit 45's to fix.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-54`, its trailer block carrying `Pass: TOOL-dWitnessedBar-54`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-54-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
