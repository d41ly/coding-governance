**Serves:** journal TOOL-dWitnessedBar-16

# Build brief — TOOL-dWitnessedBar-16, pass 2

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 10.
- THIS IS PASS 2 of the two-pass unit. Pass 1 landed as `87bc9f615` and `6c989def1`, and the main loop committed the
  converted `memory/project/readme-contract.txt` in `1f4ce2c30`. The spec is now rev-13: build S12 (delete the
  transitional read, observe AC14), S14 (move the four lists under the tool root to `memory/project/` with every
  name of them) and S15 (pass 1's remaining pass-leg reds), and move the spec's status to `CLOSED` in this pass's
  commit.
- Pass 1's pass-leg output is the untracked log
  `C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/unit16-pass1-pass-legs.log`;
  S15 lists what of it this pass owns. The one install-prefix line that stays is unit 14's `conf-scalar-pins` seed
  argv, carried until unit 51.
- Run `python tools/playbook/writing_practice.py check pinned-facts` and `python tools/playbook/positional.py` over
  your own records before committing; they read only tracked files.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-16`, its trailer block carrying `Pass: TOOL-dWitnessedBar-16`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-16-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
