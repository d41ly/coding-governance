# TOOL-dTotalRecall-73 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-73
**Caused-by:** TOOL-dTotalRecall-73

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-3 over base
`aec378661` and ran each probe below on node a, 2026-11-24; a fixture is built under the system temp directory
and removed. §7's legs and its `New arm:` RED-first observation are owed to the close.

**Evidences:** TOOL-dTotalRecall-73
- AC1 — `tree_lib.resolve_kept_home('../..')` — the probe printed `memory/project/census-kept-paths.txt` twice (DERIVED 2026-11-24, this probe).
- AC2 — `python record_causes.py --fixture --plant kept-home-rooted` — exited 1 with one `record causes: RED ` line naming `docs/memory/project/census-kept-paths.txt` and `memory/project/census-kept-paths.txt`; the `read at` line named the first, the `registered at` line the second. With `check_kept_home`'s reds dropped in a probe process the plant exited 0 (DERIVED 2026-11-24, both runs).
- AC3 — `inspect.getsource(tree_lib.read_kept_rows)` — printed `False True` and the behaviour probe `None` at the base, and `True False` and `probe row` at the tip (DERIVED 2026-11-24, both probes).
- AC4 — `python record_causes.py --cause-writers` — exited 0 with §4's two lines last and no red; the 126 other lines equal the base's once each literal's own line number is masked, since this unit's lines in `record_causes.py` and `tree_lib.py` move the literals below them. `python record_causes.py --fixture --plant adopter-no-registry` printed `PASS` and the line ending `registered nowhere` (DERIVED 2026-11-24, these runs).
