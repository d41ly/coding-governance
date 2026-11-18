# TOOL-dDeclaredLoop-51 deviation 512 — the help example's item count read over TOOL-dDeclaredLoop-50

**Serves:** deviation TOOL-dDeclaredLoop-51

- **Departs from:** `TOOL-dDeclaredLoop-51@rev-3` [§2, §4]
- **Hand-off:** spec-to-code
- **Before:** S2 and §4's prototype give the count line as `loop: items · 61 read · 8 pending · 0 unarmed` after S1, PINNED 2026-11-16, measured on an export ahead of TOOL-dDeclaredLoop-50.
- **After:** the definition reads 67 PINNED items at the base of this pass, the six review rows TOOL-dDeclaredLoop-50 added included, so the line the read prints after S1, and the line `help/loop.md` now carries, is `loop: items · 67 read · 8 pending · 0 unarmed`, PINNED; the pending count moves by one as the spec states, and no code of this pass moves for the figure.
- **Cause:** builder discovery
- **Reason:** §5's Dependency names S2's figures DERIVED at the pass, after units 50 and 22 land; the sweep re-run at the base of this pass found the read count alone stale, and the help page still carried the pre-50 count line.
- **Evidence:** `loop_lib.py --fixture --plant witness-actor-listed`, which runs the whole `--check` read over the shipped definition, printed `67 read · 9 pending` before the edit and `67 read · 8 pending` after it.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage — the count line is derived from the read at the pass, as §5 provides
- **Caused-by:** TOOL-dDeclaredLoop-50
