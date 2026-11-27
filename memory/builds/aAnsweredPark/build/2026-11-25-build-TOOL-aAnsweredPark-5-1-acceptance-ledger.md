# TOOL-aAnsweredPark-5 — acceptance ledger

**Serves:** journal TOOL-aAnsweredPark-5

One builder pass over base `c6ffe744e`. No merge bar, no self-test suite and no gate leg ran in it; each
line below is a direct CLI call over the changed code or a probe of a changed document.

**Evidences:** TOOL-aAnsweredPark-5
- AC1 — `python tools/loop/position.py --fixture --plant parked-decisions` printed `other-build` and `malformed` awaiting with the tag, the seven variants that stood as before, and `held`.
- AC2 — the same `parked-decisions` run printed `tenth` and `later-date` awaiting with the tag.
- AC3 — `python tools/loop/position.py --fixture --plant parked-kinds` printed `hold-specced` and `hold-no-phase` act with none, and `held`.
- AC4 — the probe of section 4 printed `1 1` after each of `tools/loop/position.py`, `help/loop.md` and `tools/loop/README.md`.
- AC5 — `python tools/memory-tree/seen_red.py --build aAnsweredPark --base 3d6c1702` named `loop position fixtures` with `ace7f1ee` and the first ledger, and the `grep -c` of the old paragraph printed 0.
- AC6 — `grep -n "seven variants" tools/loop/position.py` printed nothing, the `grep -c` over `tools/run-gates/selftest-budgets.txt` printed 1, and the fixture bullet of `help/loop.md` names the six new variants.
- seen-red — `loop position fixtures` — red `3ca2cdb02` — green `3ca2cdb02` — `parked-decisions`: the build filter dropped reds `other-build`; the malformed filter dropped reds `malformed`; the newest key replaced by last-read, and by a lexical compare of `id`, reds `tenth`; the date dropped from the key reds `later-date`
- seen-red — `loop position fixtures` — red `3ca2cdb02` — green `3ca2cdb02` — `parked-kinds`: the phase test replaced by `!= "BUILDING"` reds `hold-specced` and `hold-no-phase`

## Owed to the close

Every leg section 6 of the spec names. The arms `parked-decisions` and `parked-kinds` were not observed in this
pass; the main loop saw each red and then green afterwards, at `3ca2cdb02`, and the seen-red lines above record it.
