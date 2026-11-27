# TOOL-dTotalRecall-87 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-87
**Caused-by:** TOOL-dTotalRecall-87

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-3 over base
`02e6a8172` and ran each probe below on node a, 2026-11-24; a fixture is built under the system temp directory
and removed. §7's legs and its `New arm:` RED-first observation are owed to the close.

**Evidences:** TOOL-dTotalRecall-87
- AC1 — `tree_lib.resolve_memory_root(c)` — the probe printed the four roots the criterion states, and each of the four refused values raised `ValueError` opening `MEMORY_ROOT=`, as did `/`, a blank of one dot and an inner `..` (DERIVED 2026-11-24, this probe).
- AC2 — `python record_causes.py --fixture --plant kept-home-trailing-root` — exited 0 with no `record causes: RED ` line, its `read at` and `registered at` lines both naming `docs/memory/project/census-kept-paths.txt`. With the conf's raw value joined in a probe process the `read at` line named `docs/memory//project` (DERIVED 2026-11-24, both runs).
- AC3 — `python record_causes.py --fixture --plant kept-root-blank` — exited 1 with one `record causes: RED ` line, opening `cause-writer MEMORY_ROOT=`, one `read nowhere` line and no `read at` line. With the blank refusal skipped and the kit default returned in a probe process the plant exited 0 (DERIVED 2026-11-24, both runs).
- AC4 — `tree_lib.resolve_kept_home(d)` — the probe printed the registry's path under `docs/memory` three times and `MEMORY_ROOT` twice; over the base's engines it printed the second and third as spelled and a home for the last two. `python record_causes.py --cause-writers` exited 0, its 128 lines equal to the base's once each literal's own line number is masked, since this unit's lines in `record_causes.py` and `tree_lib.py` move the literals below them (DERIVED 2026-11-24, these runs).
