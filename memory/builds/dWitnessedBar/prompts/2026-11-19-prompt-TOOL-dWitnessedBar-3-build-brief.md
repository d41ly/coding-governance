**Serves:** journal TOOL-dWitnessedBar-3

# Build brief — TOOL-dWitnessedBar-3

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 20.
- Built so far through order 19: every unit up to and including 4 (the runner's per-tree verdict record, the pre-push
  hook adopting only the pushed tree's GREEN record), 25 (the verdict's `run_id` and `cause`, failing-leg tails kept by
  hash), 40 (the per-tree verdict's declines and reuse pair), 23 (`66ad2ab39`: the `gov-tester` role) and 42
  (`22f207038`: the tail sweep across worktrees). Spec rev-8 was re-grounded over all of them at `d9b5251da`.
- §8 F6's ask is filed in this build's own backlog as TOOL-dWitnessedBar-100 (`70acc009c`), not under the
  TOOL-dDeclaredLoop-12 id the spec names, which dDeclaredLoop already holds for a closed unit. Cite the filed id where
  your code or records name the ask; the spec's wording is fixed at the close.
- This unit builds alone at order 20; units 44, 5 and 8 consume from it and wait for its pass.
- The pass legs carry one known red: install-prefix on the `conf-scalar-pins` seed argv in
  `tools/memory-tree/kit.toml`, held until unit 51. The full `memory hygiene` leg is red at base on checks 13 and 15
  from other records; the main loop owns those at the close. Any other red is this unit's to fix.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-3`, its trailer block carrying `Pass: TOOL-dWitnessedBar-3`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-3-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
