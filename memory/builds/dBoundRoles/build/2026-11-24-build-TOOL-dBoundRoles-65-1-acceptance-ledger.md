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
- AC4 — `git worktree list --porcelain -z` — AMENDED by `TOOL-dBoundRoles-67`, its text restated in `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-67-deviation-672.md`: both operands of S5 print nothing over that list. Recorded before any take-away: the signature sha is `7dae6faf2537917a56de07ad1c44b261bdae19e2`, the parent of `bfccd9126`; S1's comparison against S2's root `dbr63obs` selected no entry; the signature selection selected no entry, the list's detached entries being at other heads (DERIVED at `d5467686f`), so nothing was taken away, left in place or parked. As this unit's pass read it: S1's comparison over it against S2's root printed nothing on the built tree (DERIVED at `421ae3894`), and printed entries against the bare temp folder.
- AC5 — `**Evidences:**` — AMENDED by the main loop's decision, items 3 and 4: one line of unit 64's block answers AC13 and one line of unit 63's answers AC11, each reading AMENDED and naming `TOOL-dBoundRoles-65` and record 652 in place of the revision `LEDGER` would match.

## The positive control's criterion, AC6, added on top by TOOL-dBoundRoles-68

`TOOL-dBoundRoles-68` S4 gives this unit the signature selection's positive control, and its deviation record
`memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-68-deviation-682.md` holds the text, with the S7 that
says what AC4 does not see. This unit's spec is CLOSED and frozen and numbers no AC6, and the acceptance-ledger check
refuses a label its spec does not number, so the answer stands under this heading rather than in the block above.

OBSERVED, over the `git worktree list --porcelain -z` of the scratch repository `C:\Temp\dbr68c\r`, at `cf4f54abd`:

- The signature selection printed `C:/Temp/dbr68c/o/1` alone, a detached worktree outside any `dbr63obs` root; it left
  out `o/2`, detached at the other commit, and `o/3`, on a branch at the signature.
- S1's comparison against the empty `C:\Temp\dbr68c\dbr63obs` printed nothing over the same list.
- After `git worktree remove --force` took `o/1` away the selection printed nothing.
- With the token `dbr68none` the selection exited 1 naming the empty signature and printed no entry.
