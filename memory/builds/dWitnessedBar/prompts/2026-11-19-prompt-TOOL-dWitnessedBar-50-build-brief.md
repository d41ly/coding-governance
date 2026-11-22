**Serves:** journal TOOL-dWitnessedBar-50

# Build brief — TOOL-dWitnessedBar-50

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 3.
- Built so far: units 26, 27, 48 and 49 — the `resolve_bash_py` block and its twin, `tools/lib/refuse-wrong-shell.sh`
  with the refusal call in all 88 members of unit 27's population (82 inline members, six sourcers), the coverage arm
  `scan_rws_coverage` and section `2n` of `tools/lib/resolve-python.test.sh`, and `scan_bare_bash` with shapes 1 to 4.
  Read `scan_rws_coverage` as unit 27 left it: this unit widens its assertion 2 (§8 F4).
- The spec is rev-4, re-grounded at `fed701a30`: the population is PINNED at 89 (unit 27's 88 plus
  `.githooks/pre-commit`), `pass-tree.sh` and `pass-tree.test.sh` are named exclusions (§8 F3), and the pre-commit hook
  carries the refusal inline after `set -u` (§8 F4).
- Unit 13 (`9cdebebc4`, red-fixes `a96cb1dec`, `15710a90a`) is built: `tools/lib/legacy_ledger.py`, section `2o`. Its spec wrote
  `tools/lib/resolve-python.test.sh` too; touch only what this spec names in that file.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-50`, its trailer block carrying `Pass: TOOL-dWitnessedBar-50`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-50-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
