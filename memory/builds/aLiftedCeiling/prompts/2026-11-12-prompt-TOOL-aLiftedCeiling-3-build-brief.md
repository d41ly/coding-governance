**Serves:** journal TOOL-aLiftedCeiling-3

# Build brief — TOOL-aLiftedCeiling-3

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- Units 1 and 2 are CLOSED: the instruction-edits leg's ceiling is 420 s and its evidence row stands at 110 s. The close's bar
  red `install-prefix (shipped surface)` on that row's source text, which spells the playbook kit's path; this unit rewrites it.
- The row is rewritten by the kit's `--reset` and `--observed` in one call, inside a fresh scratch clone taken at HEAD outside the
  repository, and the generated file is copied back; never run `--write` in this worktree. The value stays 110.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-aLiftedCeiling-3`, its trailer block carrying `Pass: TOOL-aLiftedCeiling-3` beside the
  attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/aLiftedCeiling/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before your first product write and commit it only as `CLOSED`. Run `gen_build_index.py
  --write` after staging and commit every file it rewrites.
- Your acceptance ledger is `memory/builds/aLiftedCeiling/build/2026-11-12-build-TOOL-aLiftedCeiling-3-ledger.md`; each line leads
  with a backticked token its criterion carries.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, run in the background.
- Run no gate leg, no suite, no bar. AC1 and AC4 are gate checks the main loop observes after your return; name them in it.
