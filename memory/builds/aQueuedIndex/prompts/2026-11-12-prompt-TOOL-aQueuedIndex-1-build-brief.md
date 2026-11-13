**Serves:** journal TOOL-aQueuedIndex-1

# Build brief — TOOL-aQueuedIndex-1

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is aQueuedIndex's one unit, on the owner's 2026-11-12 prompt "fix the tag index contention so bars don't flake" and
  the brief they accepted (`memory/builds/aQueuedIndex/prompts/2026-11-12-prompt-TOOL-aQueuedIndex-1-brief.md`).
- The spec's fork F1, the busy timeout, is resolved on its recommendation, 600 s, the one value measured green. The spec
  writer prototyped the design in a scratch clone and one race passed with the waiter reusing the other writer's tree.
- The index is shared by every worktree of this node: any probe that writes an index runs in a scratch repository of its own.
  Another session may hold the node's index; a `database is locked` from a probe against it is contention, retried once.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-aQueuedIndex-1`, its trailer block carrying `Pass: TOOL-aQueuedIndex-1` beside the
  attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/aQueuedIndex/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before your first product write and commit it only as `CLOSED`. Run `gen_build_index.py
  --write` after staging and commit every file it rewrites.
- Your acceptance ledger is `memory/builds/aQueuedIndex/build/2026-11-12-build-TOOL-aQueuedIndex-1-ledger.md`; each line leads
  with a backticked token its criterion carries.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, run in the background. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map generator's
  output; declare both.
- Run no gate leg, no suite, no bar. The five scratch-clone races are the main loop's to run after your pass.
