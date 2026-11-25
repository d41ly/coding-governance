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

## Owed to the close

Every leg section 6 of the spec names, and the RED-first observation of the arms `parked-decisions` and
`parked-kinds` on the staged breaks its two `New arm:` lines name, not observed in this pass.
