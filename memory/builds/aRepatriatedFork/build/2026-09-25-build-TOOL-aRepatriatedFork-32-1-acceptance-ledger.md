# TOOL-aRepatriatedFork-32 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-32

Written by the unit pass on node a. The new arms ran as a SLICE of the hygiene self-test: its
prologue, the helpers, and the fixture tree from the check-16 block through this unit's block, in a
temp script inside the kit dir, removed afterwards. No whole suite ran. The old-bytes run swapped in
`HEAD`'s engine and generator and restored both, byte-compared.

**Evidences:** TOOL-aRepatriatedFork-32
- AC1 — `RECORD_SERVES_CUTOFF` — the slice exits 0 at `SLICE n=35 st=0`; the control prints `ok   check 21 control: with no cutoff the id, filename and pin branches all grade the pre-cutoff records`, and the id, filename and both pin arms print `ok`
- AC2 — `RECORD_SERVES_CUTOFF` — over the old engine and generator the slice exits 1: `FAIL RECORD_SERVES_CUTOFF: the id branch still grades a record dated before the cutoff`, the same for the filename branch, and `FAIL RECORD_SERVES_CUTOFF: the pin still counts the unbound record dated before the cutoff`; the control arm still printed `ok`
- AC3 — `gen_build_index.py` — with the `U` print deleted from a kit copy, the slice prints `ok   check 21: a generator printing N and no U row reds instead of leaving the pin ungraded`
- AC4 — `bash tools/memory-tree/check-memory-hygiene.sh` — exits 0 on gov's tree
- AC5 — `bash tools/check-kit-versions.sh` — exits 0 with memory-tree 2.97; `python tools/govkit/govkit.py epoch` reports no FAILED entry
