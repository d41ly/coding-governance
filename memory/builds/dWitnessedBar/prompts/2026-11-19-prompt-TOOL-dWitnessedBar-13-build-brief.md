**Serves:** journal TOOL-dWitnessedBar-13

# Build brief — TOOL-dWitnessedBar-13

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 3.
- Built so far: units 26, 27, 48 and 49 — the `resolve_bash_py` block (`scan_bash`, `BASH_NAMES`, `wrong_shell_at`)
  and its JavaScript twin with name-keeping adapters, `tools/lib/refuse-wrong-shell.sh` in every `resolve_python`
  member, and `scan_bare_bash` in `tools/run-gates/measure_legs.py` with shapes 1 to 4. Sections `2j` and `2n` of
  `tools/lib/resolve-python.test.sh` are theirs; this unit's section is `2o`.
- The spec is rev-4, revised over the first builder's divergence
  (`build/2026-11-19-build-TOOL-dWitnessedBar-13-1-builder-return.md`): `compare` reads measured rows from
  `--measured <path>` (§8 F6), `read_registrations` reads every tracked `kit.toml` and `govkit/registry.toml` at any
  depth (§8 F7), `read_renames` re-keys base rows before `compare_to_base` judges, `carry` writes only a tracked home,
  and the merge class passes its row plane to every postcondition. The new "The CLI" sub-section gives each verb.
- Unit 50 is flipped INPROGRESS and waits on this pass, because both write `tools/lib/resolve-python.test.sh`.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-13`, its trailer block carrying `Pass: TOOL-dWitnessedBar-13`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-13-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
