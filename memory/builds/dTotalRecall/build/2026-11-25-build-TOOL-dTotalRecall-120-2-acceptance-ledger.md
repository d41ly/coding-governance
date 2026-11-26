# TOOL-dTotalRecall-120 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-120
**Caused-by:** TOOL-dTotalRecall-120

No merge bar, no self-test suite and no gate leg in this pass. The builder built spec rev-2 over base
`3c1a90c1e5504c14af332d8c2b8b8be3343339a3`, 2026-11-25 local, in one commit, from the first pass's draft. The plants
ran over the working tree's `record_causes.py`. §7's legs and the `New arm:` RED-first observation of
`tools/memory-tree/check-memory-hygiene.test.sh`'s `legacy-drained` arm are owed to the close.

With today's reader put back in a probe over the plant, the check printed its one `unarmed` line and exited 0, the
backfill wrote nothing and the plant printed FAIL, exit 1 (DERIVED 2026-11-25, the probe).

**Evidences:** TOOL-dTotalRecall-120
- AC1 — `python record_causes.py --fixture --plant legacy-drained` — printed the new record and the two former legacy ones under `causes`, the `cause-writer ·` count line, 3 `backfilled` lines and `fixture legacy-drained · PASS`, exit 0 (DERIVED 2026-11-25, that run).
- AC2 — `read_legacy_paths` — answered None over a scratch tree with no registration, and the plants `legacy`, `causeless` and `none` printed byte for byte what they print at `acbb74bb`, exits 0, 1 and 0 (DERIVED 2026-11-25, the probe).
- AC3 — `grep -n 'an empty population' tools/memory-tree/record_causes.py` — printed no line (DERIVED 2026-11-25).
- AC4 — `grep -n 'plant legacy-drained' tools/memory-tree/check-memory-hygiene.test.sh` — printed the arm; `FLOOR_ASSERTIONS` went from 837 to 842, its five assertions, and the `shell-role` row from 3751 to 3752, the measured count, widened by `2026-11-25-build-TOOL-dTotalRecall-120-widen-31` (DERIVED 2026-11-25). The floor is counted by reading; the suite's own run is owed to the close.
