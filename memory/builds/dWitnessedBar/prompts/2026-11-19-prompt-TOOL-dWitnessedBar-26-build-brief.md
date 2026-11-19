**Serves:** journal TOOL-dWitnessedBar-26

# Build brief — TOOL-dWitnessedBar-26

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This is build order 1, the first unit: nothing of this build is built yet.
- The spec's base is `cdfbd1cf`; the run's is `9e21ac76`. Since then dGroundRules landed `tools/lib/resolve_bash.py`
  with its `resolve_bash_py` block, so S1 is the in-place rewrite §8 F1 names, not a new file. Copies of that block
  also sit in `tools/policy/check_policy.py`, `tools/loop/loop_witness.py` and `tools/playbook/render_playbook.py`,
  and govkit's resolver now lives in `tools/govkit/upgrade_steps.py:369` (TOOL-dSafePassage-35 S24), which the spec
  already names. Re-derive the site list with the S6 query at this base rather than trusting §4's table line numbers.
- Verify each claim about current code against source before building on it, and hand a claim that no longer holds
  back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-26`, its trailer block carrying `Pass: TOOL-dWitnessedBar-26`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-26-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (a copy
  of the block the spec did not list, the ledger, a generated file) needs its own `--dispatch` with `--writes` for it
  before you stage it. A file on the kickoff manifest's `watch:` list needs the manifest re-stamped in the same
  commit, and a stale codebase map needs the map generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
