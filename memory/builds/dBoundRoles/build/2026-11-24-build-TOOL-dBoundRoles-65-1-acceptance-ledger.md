**Serves:** journal TOOL-dBoundRoles-65

# TOOL-dBoundRoles-65 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit on its worktree before the pass commit at base
`421ae3894`. Specs 63 and 64 are CLOSED, so the restated text is the After field of
`memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-65-deviation-652.md`, and a criterion that greps a
frozen spec is answered AMENDED, by
`memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-58-1-main-loop-decision.md`, item 4. No gate, suite
or bar ran in the pass: this unit adds no arm, and the legs its gate line lists are owed to the main loop at the close.

## The control's readings, S4, and the built tree, S5

`<TEMP>` read `C:\Temp` by `tempfile.gettempdir()` and by `cygpath -m "$TEMP"` alike. The scratch repository stood at
`dbr65c` under it, with a detached worktree at `1-1` under its `root` folder.

- The comparison, given `C:\Temp\dbr65c\root` as `cygpath -w` printed it, reported `C:/Temp/dbr65c/root/1-1` alone.
- A raw `startswith` over the same parsed porcelain reported nothing.
- After `git worktree remove --force` the comparison reported nothing, and the scratch directory was cleared.
- Beyond S4: the root in upper case reported the same entry, a sibling named `root-x` and the entry itself taken as the
  root reported nothing, and the `derive_key` equality of S1 picked that entry as the run's own.
- S5: over this repository's list, against `dbr63obs` under `C:\Temp` and under the profile's `AppData\Local\Temp`, the
  comparison reported nothing, and neither directory stands; nothing was taken away. Against the bare `C:\Temp` it
  reported another build's detached checkouts, the liveness of the reading.

**Evidences:** TOOL-dBoundRoles-65
- AC1 — `parse_worktrees` — AMENDED by the main loop's decision, item 4: a `python` probe cut record 652's S12 text for `TOOL-dBoundRoles-63@rev-6`, whitespace collapsed; it names that token, `check_under`, `os.path.realpath` and `dbr63obs`, refuses `os.path.commonpath`, and holds no short temp path phrase. Over the frozen S12 the probe failed every one of those readings.
- AC2 — `check_under` — AMENDED by the main loop's decision, item 4: the probe cut record 652's text for spec 64's S18 and AC13 and spec 63's AC11; each names the token and `dbr63obs`, none holds the retired prefix spelling, AC13 names `dbr65c`, and the record counts itself as each spec's revision-log line naming `TOOL-dBoundRoles-65`. Over the frozen S18, AC13 and AC11 the probe failed each.
- AC3 — `startswith` — the three readings of the section above: one path, nothing, and nothing after `git worktree remove --force`. The raw test's empty reading over the standing leftover is the failing case the comparison replaces.
- AC4 — `git worktree list --porcelain -z` — S1's comparison over it against S2's root printed nothing on the built tree (DERIVED at `421ae3894`), and printed entries against the bare temp folder.
- AC5 — `**Evidences:**` — AMENDED by the main loop's decision, items 3 and 4: one line of unit 64's block answers AC13 and one line of unit 63's answers AC11, each reading AMENDED and naming `TOOL-dBoundRoles-65` and record 652 in place of the revision `LEDGER` would match.
