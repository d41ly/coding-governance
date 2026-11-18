# TOOL-dDeclaredLoop-50 deviation 503 — the sweep's driver ceiling read over TOOL-dDeclaredLoop-22

**Serves:** deviation TOOL-dDeclaredLoop-50

- **Departs from:** `TOOL-dDeclaredLoop-50@rev-4` [§5]
- **Hand-off:** spec-to-code
- **Before:** §5's sweep names the driver's refusal ceiling as 335 PINNED, set by TOOL-dDeclaredLoop-31's decision row.
- **After:** the ceiling reads 340 PINNED at the base of this pass, set by TOOL-dDeclaredLoop-22's decision row; this pass edits no `*.sh` file, so the census and the ceiling stay where that unit left them, and no code of this pass moves for the figure.
- **Cause:** builder discovery
- **Reason:** TOOL-dDeclaredLoop-22 raised the ceiling after rev-4 was written, and the sweep re-run at the base of this pass found that figure alone stale.
- **Evidence:** the `REFUSAL_CEILINGS` line of `.memory-tree.conf` at the base of this pass, and `memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-22-deviation-223.md`.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** TOOL-dDeclaredLoop-22
