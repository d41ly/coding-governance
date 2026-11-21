**Serves:** journal TOOL-dWitnessedBar-27

# Build brief — TOOL-dWitnessedBar-27

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 2.
- Built so far: unit 26 (`7526c98fa`) rewrote the `resolve_bash_py` block in `tools/lib/resolve_bash.py` to
  `scan_bash(script, host)` returning `(found, tried, refusal)` with `BASH_NAMES`, added the twin `scanBash` in
  `tools/lib/resolve_bash.js`, inlined both into every site behind adapters that keep their names, made govkit's
  `resolve_shell_argv` raise `Refusal`, and widened `test_no_bare_bash_argv` through `scan_bare_bash`.
- The spec is rev-5, re-grounded at the main loop over the first builder's divergence
  (`build/2026-11-19-build-TOOL-dWitnessedBar-27-1-builder-return.md`): the new test section is `2n`, the population
  is re-derived and re-pinned (PINNED in the spec), `tools/govkit/govkit.py` is off the resolver copies, the library
  rule is §8 F3 (b) — `tools/lib/resolve-python.sh` carries neither block nor call, each sourcer sources
  `refuse-wrong-shell.sh` beside it — and the help page is §8 F4 (b), a section in `help/python-floor.md`.
- Unit 26's builder left one bug-class minor for the close review: `scan_bare_bash` hides the rest of a file whose
  `resolve_bash_py` / `resolve_bash_js` block never closes. Do not widen that scanner here.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-27`, its trailer block carrying `Pass: TOOL-dWitnessedBar-27`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-27-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
