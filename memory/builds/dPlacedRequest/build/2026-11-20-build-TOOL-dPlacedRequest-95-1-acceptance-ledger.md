# TOOL-dPlacedRequest-95 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-95

The unit was built from its spec at rev-2 on base `cd30d3d2c`. Built: S1, the resolver
`tools/hooks/scratch-guard.js#resolveKickoffChecker` cut to the two rungs it reads from the hook's
own install, the kit resolver from `__dirname` and the one tracked `manifest-check.sh` of the hook's
own toplevel, its `cwd` parameter and the walk over `[__dirname, cwd]` gone, its one call in
`tools/hooks/scratch-guard.js#readCard` passing nothing, and its header comment naming the two rungs
and that the target's tree is never one. The arm is the TOOL-dPlacedRequest-95 block of
`tools/hooks/scratch-guard.test.sh`, its floor raised over the value the file held. The class lands as
the section `## It bit again in the PreToolUse hook` of
`memory/gotchas/foreign-code-runs-on-the-ambient-credential.md`, the index rendered by
`gotchas.py --write`. No gate, suite or bar ran in this pass.

THE AC1 PROBE, the reading the lines below cite as "the probe": a scratch script under the run's
scratch directory builds the three fixtures of the spec's design section, the target a scratch
repository tracking one `manifest-check.sh` that writes a marker and prints nothing, and drives them
through copies of a directory of the hook's scripts by `node -e` calling `readCard` with no checker
argument for fixtures one and two, and by the copy fed a main-loop Bash payload of
`git -C <target> commit -m x` on stdin for fixture three.

THE BLOCK PROBE: the TOOL-dPlacedRequest-95 block of the suite file, cut from its heading to the
count line and run alone over the suite's own `run_card` and `check_stderr` with the suite's fixture
home and temp, never the suite, against the fixed hook.

**Evidences:** TOOL-dPlacedRequest-95
- AC1 — `readCard` — the probe over the hook at this pass: fixtures one and two each printed `null · (no card: no kickoff checker manifest-check.sh resolves to answer --card --path)`, and fixture three exited 0 with the one witness line `orientation card absent — (no card: no kickoff checker …)`; no marker file existed after any fixture, the target tracking its checker. (DERIVED)
- AC1 — `foreign-code-runs-on-the-ambient-credential` — `python tools/memory-tree/gotchas.py --for-paths tools/hooks/scratch-guard.js` printed it as a path-selected class. (DERIVED)
- AC1 — `grep -c 'TOOL-dPlacedRequest-95' tools/hooks/scratch-guard.test.sh` — printed 8. (DERIVED)
- AC1 — `grep '^FLOOR_ASSERTIONS=' tools/hooks/scratch-guard.test.sh` — printed `FLOOR_ASSERTIONS=400`, above 396, and the comment line three lines above it names TOOL-dPlacedRequest-95 and its rows. (DERIVED)
- AC1 — `grep -c "cwd..s repository tracks" tools/hooks/scratch-guard.js` — printed 0. (DERIVED)
- AC1 — `95c3103ad` — the RED reading: the same probe through copies of the hook's scripts at that base wrote the marker in each fixture, fixtures one and two reading `(no card: the kickoff checker's --card --path did not answer: exit 0: nothing printed)` and fixture three exiting 0 with the same text on its witness line. (DERIVED)
- AC1 — `TOOL-dPlacedRequest-95` — the block probe printed four `ok` rows and no `FAIL` against the fixed hook; its RED-first reading against the hook at `95c3103ad` is owed to the close, below. (DERIVED)

## Readings beside the criteria

- The real hook at its own path, given the fixture target's common dir, still read through gov's one tracked checker under `skills/session-kickoff/`, answering the card path in the target, and wrote no marker: the hook's own toplevel rung is the one every existing card row reaches. (DERIVED)
- The `scratch-guard self-test` budget row was re-priced as a proxy: the row's prior reading plus the probe's wall time, x1.5, rounded up: (DERIVED)
- the prior reading, from node a on 2026-11-13: 187 s (PINNED)
- the probe's wall time over the three fixtures, read by `time` on the run's node: 0.8 s (PINNED)
- the row as written: 282 s, below the 290 s the row held before, since the prior row's figure sat above 187 s x1.5 (DERIVED)
- The leg's `ceiling` in `tools/gate-legs.json` reads 490 s, far above the proxy, so no ceiling move is routed. (PINNED)
- The hooks kit's version carrier was not moved by hand: `tools/govkit/govkit.py#cmd_epoch` states the lander mints the bump at the push boundary and a branch owes none, and this build's earlier hook moves, units 2, 34 and 43, carry no hand bump either. (DERIVED)
- MSYS rewrites a quoted `"/"` inside a native program's argument to Git's install root, so the arm spells its forward slash through `path.posix.sep`; the first draft's marker path was mangled that way and the first probe read was discarded. (DERIVED)

## Items diverged

None.

## Owed at the close

- `New arm:` `tools/hooks/scratch-guard.test.sh`, the TOOL-dPlacedRequest-95 block, four rows, `FLOOR_ASSERTIONS` raised to 400; its RED-first observation against the hook at `95c3103ad` and its GREEN reading inside the suite are the close's. (DERIVED)
- The `scratch-guard self-test` budget row's re-price from the main loop's first reading of the leg alone.
- The legs the spec's Gates section names, run once by the main loop.
