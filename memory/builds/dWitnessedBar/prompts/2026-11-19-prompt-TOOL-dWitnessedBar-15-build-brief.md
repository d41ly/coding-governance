**Serves:** journal TOOL-dWitnessedBar-15

# Build brief — TOOL-dWitnessedBar-15

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 4.
- Built so far: units 26, 27, 48, 49 (the `resolve_bash_py` block, `tools/lib/refuse-wrong-shell.sh`, `scan_bare_bash`),
  unit 13 (`9cdebebc4`, red-fixes `a96cb1dec` and `15710a90a`: `tools/lib/legacy_ledger.py` with `read_rows`,
  `read_registrations` over every tracked file named exactly `kit.toml` and the `DEPLOYER_HOME` registry, the CLI
  `read|compare|carry` with `compare --measured <path>`, copies in memory-tree and gate-lint, section `2o` of
  `tools/lib/resolve-python.test.sh`) and unit 50 (`091488ac9`: `--coverage` in `tools/lib/refuse-wrong-shell.sh`).
  Read the factory as unit 13 left it.
- Unit 13 rev-4 §8 F6 makes `compare` read measured rows from `--measured <path>` through `read_rows(path, arity,
  tail=())`; this unit's seed run prints those rows, so its output grammar is what `read_rows` parses. Name `read_rows`
  as the parser of the seed's stdout rather than a second parser.
- The spec's §8 F4 and F5 each owe an ask in `memory/builds/dDeclaredLoop/BACKLOG.md`; neither is filed at HEAD. File
  both as ask rows there in this pass (an ask row in another build's BACKLOG is the one write outside this build the
  README admits), declaring that path with `--dispatch` first, each with its `SEV` row.
- The first builder of this unit (run `wf_c651adcf-b6c`) built and probed it, then rolled back uncommitted, because it
  read `--dispatch`'s refusal of `memory/map/generated/symbols.json` as a bar on staging that file. It is not one:
  `symbols.json` is an effective generated output (its generator `gen_map.py` is in this unit's write set), so it must
  NOT be declared, and `--check-commit` admits it undeclared. Its full staged diff is saved at
  `C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/TOOL-dWitnessedBar-15-pass.patch`
  and its drafted message at
  `C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/TOOL-dWitnessedBar-15-commit-msg.txt`.
  Apply the patch (`git apply --index`), re-verify it against the spec and the tree at HEAD, run
  `python tools/codebase-map/gen_map.py --write` and stage `memory/map/generated/symbols.json` undeclared, run
  `python tools/memory-tree/gen_build_index.py --write`, and commit with that message (its `Pass:` trailer intact).
  The worktree is clean of other passes' edits now. Its three spec gaps are settled as its deviation record states:
  memory-tree's copy gains a seed-only CLI, a failed `--widen` seed writes nothing and exits 1, a failed seed exits 1.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-15`, its trailer block carrying `Pass: TOOL-dWitnessedBar-15`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-15-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
