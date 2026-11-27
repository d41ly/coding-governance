# TOOL-dTotalRecall-118 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-118
**Caused-by:** TOOL-dTotalRecall-118

No merge bar, no self-test suite and no gate leg in this pass. The builder built spec rev-1 over base
`ee5987930e2bd2e74a91b80b0cf8a5d935758b9d`, 2026-11-25 local, in one commit. §7's legs and the `New arm:` RED-first
observation of `tools/runlog/selftest.py`'s `test_memory_dtr118_root`, with the first run of the nine restored arms,
are owed to the close.

Before the edit the same probe answered None for all five calls of AC1. With both equalities cut in a scratch copy of
the kit, the four counting plants read zero bytes on both channels over their one agent (DERIVED 2026-11-25, that copy).
The restored arms count more than §4 says: the floor 1711 (DERIVED, its raise line) counts seven of the nine, so it
sits under the suite's count by the checks of `test_memory_dtr43_paths` and `test_memory_dtr53_paths`; the floor of S4 is built as written.

**Evidences:** TOOL-dTotalRecall-118
- AC1 — `memory_measure.derive_read_channel` — answered `read`, `shell`, `read`, `shell` and None in order, and None for `C:/fx/other-tree/memory` (DERIVED 2026-11-25, the probe).
- AC2 — `python tools/runlog/runlog.py memory --fixture --plant <case>` — the pooled rows read 400 on read, 350 on shell, 300 on read, 250 on shell, and zero for `root-sibling`, each over one agent (DERIVED 2026-11-25, the five runs).
- AC3 — `grep -c '^def test_memory_' tools/runlog/selftest.py` — printed 10, and the block from its section line to the end of `test_memory_ac9_privacy` equals `ffa0dcf2d^1`'s byte for byte, nine arms (DERIVED 2026-11-25, the probe's compare).
- AC4 — `grep -nE '^ASSERTION_FLOOR|RAISED 1711' tools/runlog/selftest.py` — printed the raise line and the floor 1724, `parse_floor_raise` read the same pair, and `test_memory_dtr118_root` alone passed its 10 checks with no failure (DERIVED 2026-11-25, the probe).
