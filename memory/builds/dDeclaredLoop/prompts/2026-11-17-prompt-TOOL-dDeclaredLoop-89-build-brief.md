**Serves:** journal TOOL-dDeclaredLoop-89

# Build brief — TOOL-dDeclaredLoop-89

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dDeclaredLoop's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. Every unit through build order 43 is built: unit 87 (82087c644) made derive_conf_constants in loop_lib.py match by class (every module-level binding whose value's syntax subtree holds a conf name, descending into if, try, with, for and while but never into a function or class; assignments, augmented and annotated assignments, tuple targets), and added joined-path, os-path-join, multi-argument-path, aliased-from-import and a non-conf negative row to the conf-read-forms plant. This unit builds before unit 88 at order 44. The spec is rev-5, re-grounded on the branch at 759298f0f.
- The spec's base is older than the run's: verify each claim about current code against source before building on it, and
  hand a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dDeclaredLoop-89`, its trailer block carrying `Pass: TOOL-dDeclaredLoop-89` beside
  the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dDeclaredLoop/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed. Run
  `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger `memory/builds/dDeclaredLoop/build/2026-11-17-build-TOOL-dDeclaredLoop-89-1-acceptance-ledger.md`
  in the pass commit: one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, the ledger and every generated file included. A
  file on the kickoff manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map
  needs the map generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are `report`
  and `author-recorded`.
