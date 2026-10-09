# Acceptance ledger — TOOL-dHomedResolver-3

**Serves:** journal TOOL-dHomedResolver-3

Built on `88437f6c`. Both records follow the catalogue's section shape, each names the gate its
instance carries and says the class itself has none, and both are claimed in the memory-tree
hygiene dossier's `gotcha-classes`.

**Evidences:** TOOL-dHomedResolver-3
- AC1 — `python tools/memory-tree/gotchas.py --check` — exits 0 with both records parsed and `INDEX.md` re-rendered at 105 records; check 18 was red until each named its gate
- AC2 — `python tools/memory-tree/gotchas.py --for-paths` — over gen_build_index.py and check-memory-hygiene.sh it lists both new classes at path tier
