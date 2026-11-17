# TOOL-dDeclaredLoop-117 deviation 1175 — two figures the unit's sweep pins read otherwise at the pass's base

**Serves:** deviation TOOL-dDeclaredLoop-117

- **Departs from:** `TOOL-dDeclaredLoop-117@rev-1` [AC5, the sweep's symbol-tier and deviation-population rows]
- **Hand-off:** spec-to-code
- **Before:** the sweep reads no `write_conf_plant` row in the symbol tier before the pass, so the AC5 grep of that id prints 1 after it, and it reads the build's highest deviation number as 1002, PINNED 2026-11-17.
- **After:** the symbol tier already holds a `write_conf_plant` row for the step gate's plant writer, at the spec's base as at this pass's, so the AC5 grep prints 2 after the regeneration and the criterion is observed as the one added row, whose file is `tools/loop/loop_lib.py`; the build's highest deviation number is 1174 at the pass's base and 1171 to 1173 are unused, so the records keep the numbers the spec gives them, PINNED 2026-11-17.
- **Cause:** builder discovery
- **Reason:** the sweep re-run at the pass's base read both figures otherwise; each is a count and no design claim, since the regeneration adds the one row the spec names and the three record numbers it assigns stay free.
- **Evidence:** the acceptance ledger `2026-11-17-build-TOOL-dDeclaredLoop-117-1-acceptance-ledger.md`, its AC5 and AC6 lines; `tools/govkit/step_gate.py#write_conf_plant`.
- **Risk:** editorial
- **Approver:** author, the builder pass of TOOL-dDeclaredLoop-117, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-17-build-TOOL-dDeclaredLoop-117-1-acceptance-ledger
