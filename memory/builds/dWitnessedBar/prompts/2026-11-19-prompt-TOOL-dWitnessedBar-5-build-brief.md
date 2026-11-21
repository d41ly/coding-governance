**Serves:** journal TOOL-dWitnessedBar-5

# Build brief — TOOL-dWitnessedBar-5

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 21.
- Built so far through order 20: every unit up to and including 4, 25, 40, 23, 42 and 3 (`930a5289d`, its pass-leg
  fix `e37158660`: `verdict.blocks`, `lib-verdict.sh`, `verdict_flow.py` with `route` and `judge`, and the upgrade step
  `tools/govkit/steps/inherited_red.py`). This spec was re-grounded over unit 3 as landed at `e95e88c85`.
- Units 44 and 5 build at order 21 IN PARALLEL in this one working tree. Their Files touched are disjoint: stage
  explicit paths only, never `git add -A`, and never stage, edit or revert a path the other unit's spec names. The
  session card routes both units, so each builder may flip its own spec's status.
- The pass legs carry one known red: install-prefix on the `conf-scalar-pins` seed argv in
  `tools/memory-tree/kit.toml`, held until unit 51. The full `memory hygiene` leg is red at base on checks 13 and 15
  from other records; the main loop owns those at the close. Any other red is this unit's to fix.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-5`, its trailer block carrying `Pass: TOOL-dWitnessedBar-5`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-5-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.

## A resumed pass

- The first builder of this unit (`wf_f155de9c-57a`) built the whole unit but could not commit. Its pre-commit
  refused the pass for the kickoff manifest's re-stamp, and `--dispatch` then refused to declare that file over a
  stale packet. Its return is `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-5-1-builder-return.md`.
- The packet is re-pinned at `bf873d18c`, and this unit is re-dispatched there with
  `memory/guides/SESSION-KICKOFF.md`, `tools/playbook/kit.toml` and
  `memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-5-deviation-52.md` and `-53.md` declared.
- That builder's work is still in this working tree, unstaged, with its acceptance ledger written. Verify it against
  the spec rather than rebuilding it: re-run its probes, write the deviation record its return owes, re-stamp the
  manifest, and commit the pass through the hooks. Its drafted commit message is
  `C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/msg5.txt`;
  its trailer must read `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
