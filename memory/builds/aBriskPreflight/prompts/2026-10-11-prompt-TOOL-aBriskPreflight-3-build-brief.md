# Build brief — TOOL-aBriskPreflight-3: which wiring arms preflight needs, decided by measurement

**Serves:** research TOOL-aBriskPreflight-3

Build the unit its spec, `spec/2026-10-11-spec-TOOL-aBriskPreflight-3.md`, describes: a per-arm
window instrument and a measurement record under this build's `build/` folder, and the two asks in
this build's `BACKLOG.md`. Its S4 is binding: no commit of this unit edits a file under `tools/`,
`.githooks/` or `.unattended.conf`. This run sequences its passes one at a time, inline.

## The tree you start from

- Units 1 and 2 are CLOSED (`4421bf650`, `4f0f655e9`), so the tree to measure is HEAD. Unit 2's
  result record carries the latest whole-check count (180 forks, 121 execs); your one trace of
  `--check` is taken on HEAD with the build's instrument, `build/…-1-run-traced.sh` and
  `…-1-trace-spawns.py`, in a throwaway clone under `%TEMP%/<short>` (the `skill` arm reds in a
  clone because this machine's installed kickoff engine follows the primary checkout: say so, and
  it is the same for every candidate). Record the host's spawn cost beside it
  (`build/…-1-host-state.sh`).
- Units 4, 5 and 6 are CLOSED too; they do not touch the wiring check.

## How to work in this tree

- **Declare before you write**, with `--dispatch`: your records, `memory/builds/aBriskPreflight/BACKLOG.md`,
  `memory/builds/aBriskPreflight/README.md`, `memory/LIVE.md`, `memory/ledger/2026-10.md`,
  `memory/map/generated/symbols.json` (the instrument is a `.py` and its functions enter the map),
  and `memory/backlog/TOOL.md` if the generator renders it.
- **Stage your declared paths AND `memory/builds/aBriskPreflight/RUN.md`** in the pass commit.
- **A records-only `.py` is graded by the lexicon leg**: every `def` leads with a declared verb; ask
  `python tools/lexicon/lexicon.py --suggest <name> --as py.function` first.
- **A new ask carries its `SEV` row in the same commit**; read `memory/guides/UNATTENDED-ASKS.md` §5
  for the filing shape, and render with `python tools/memory-tree/gen_build_index.py --write`.
- No suite, no bar. Never kill a process you did not start.
