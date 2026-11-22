**Serves:** journal TOOL-dWitnessedBar-48

# Build brief — TOOL-dWitnessedBar-48

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 2.
- Built so far: unit 26 (`7526c98fa`) — the `resolve_bash_py` block is `scan_bash(script, host)` with `BASH_NAMES`, its
  twin `scanBash`, name-keeping adapters at every site, and `scan_bare_bash` in `tools/run-gates/measure_legs.py`
  behind `test_no_bare_bash_argv`. Unit 27 (`8b3aa5783`) — `tools/lib/refuse-wrong-shell.sh`, the refusal call in
  every `resolve_python` member, `wrong_shell_at` / `wrongShellAt` added to both resolver blocks (every copy
  byte-identical), and section `2n` of `tools/lib/resolve-python.test.sh`.
- The spec is rev-4, re-grounded at `fed701a30`; each new inline copy of the `resolve_bash_py` block is the canonical
  at this pass's tip, unit 27's `wrong_shell_at` included, and the parity row finds it by its marker.
- Unit 26's builder left one bug-class minor for the close review: `scan_bare_bash` hides the rest of a file whose
  block never closes. This unit widens shape 2 of that scanner; widen only what the spec states.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-48`, its trailer block carrying `Pass: TOOL-dWitnessedBar-48`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-48-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
