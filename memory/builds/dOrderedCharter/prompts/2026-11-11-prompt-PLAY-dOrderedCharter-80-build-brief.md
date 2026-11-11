**Serves:** journal PLAY-dOrderedCharter-80

# Build brief — PLAY-dOrderedCharter-80

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dOrderedCharter's close. Every roster unit through PLAY-dOrderedCharter-55 is CLOSED. The close's bar over `daf84987f`
  failed eight legs; the main loop fixed its own record reds at `80a2a55af`, and a read-only attribution traced the product reds to
  units 31, 78 and 55 (`memory/builds/dOrderedCharter/prompts/2026-11-11-prompt-PLAY-dOrderedCharter-1-close-bar-attribution-researcher.md`).
  This unit carries every remaining fix under `tools/`.
- The policy check's five `review.*` findings are inherited from the merge base and out of scope; gov's install receipt is the
  lander's to rewrite.
- The main loop kept the acceptance matrix's shape-5 scratch install from its probe and re-ran the render self-test there; the four
  failing arm names in spec 80 come from that run.
- Where a fixed shape hits a later refusal from another kit in the default selection, hand it back rather than widen the fix.

## What the main loop needs from your commit

- One pass commit, its subject naming `PLAY-dOrderedCharter-80`, its trailer block carrying `Pass: PLAY-dOrderedCharter-80` beside the
  attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dOrderedCharter/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before your first product write and commit it only as `CLOSED`. Run `gen_build_index.py
  --write` after staging and commit every file it rewrites, the dClosedLoop as-built view and `memory/backlog/PLAY.md` among them.
- Your acceptance ledger is `memory/builds/dOrderedCharter/build/2026-11-11-build-PLAY-dOrderedCharter-80-ledger.md`. A departure
  from the spec is a `deviation` record.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, run in the background: the machine is shared and the verb
  has taken up to an hour. A file on the kickoff manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale
  codebase map needs the map generator's output; declare both.
- Gov's guarded `.governance/` files other than `policy.toml` refuse an agent's commit; do not stage them.
- Run no gate leg, no suite, no bar. The legs your criteria name are the main loop's to observe after your pass.
