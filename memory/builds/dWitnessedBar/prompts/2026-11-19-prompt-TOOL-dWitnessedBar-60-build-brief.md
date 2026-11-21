**Serves:** journal TOOL-dWitnessedBar-60

# Build brief — TOOL-dWitnessedBar-60

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 33.
- Built so far through order 33's first unit: every unit up to and including 4, 25, 40, 23, 42, 3, 44, 5, 41, 55, 8,
  1, 59, 30, 29, 7, 21, 6, 2, 43, 51, 56, 57 and 58 (`75914afa1`: the evidence suite's floor is 310, and
  `memory/project/shell-role.txt` rows for both hook and evidence suites were widened in widen-3). Unit 28 (order 30) is
  deferred against asks TOOL-dWitnessedBar-101 to -103 and is not built. This spec, rev-4, was re-grounded at `c9d20a65b`.
- Nothing else is in flight in this working tree: commit directly here.
- The full `memory hygiene` leg is red at base on checks 13 and 15 from other records, and whole-tree spec tokens on one
  aMendedLedger spec; the main loop owns those at the close. Any other red is this unit's to fix.
- A suite that grows past its `memory/project/shell-role.txt` row is widened in this pass with `ratchet.py widen
  shell-role`, its record filed under this unit, as unit 58 did.
- Name every new function with a verb from `.lexicon.conf`'s VERBS table, nested helpers included. Cite code lines in
  every record you write as `path#symbol` or blob-pinned, never a bare `path:line`, fixture text included.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-60`, its trailer block carrying `Pass: TOOL-dWitnessedBar-60`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-60-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
