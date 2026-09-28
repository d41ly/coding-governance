# TOOL-aRepatriatedFork-32 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-32

Written by the unit pass on node a, and extended by the rev-3 fold of the closing diff review of
units 31 to 38 (2026-09-26). At rev-2 the new arms ran as a SLICE of the hygiene self-test in a temp
script inside the kit dir, removed afterwards, and the old-bytes run swapped in `HEAD`'s engine and
generator. At rev-3 the WHOLE suite ran twice on frozen clones: once over the built tree, and once
with the rev-2 engine (`176e1060`'s bytes) swapped in.

**Evidences:** TOOL-aRepatriatedFork-32
- AC1 — `RECORD_SERVES_CUTOFF` — the whole suite exits 0 at `PASS (459 assertions)` over the built tree; the control prints `ok   check 21 control: with no cutoff the id, filename and pin branches all grade the pre-cutoff records`, and the id, filename and both pin arms print `ok`
- AC2 — `RECORD_SERVES_CUTOFF` — at rev-2, over the old engine and generator the slice exited 1: `FAIL RECORD_SERVES_CUTOFF: the id branch still grades a record dated before the cutoff`, the same for the filename branch, and `FAIL RECORD_SERVES_CUTOFF: the pin still counts the unbound record dated before the cutoff`; the control arm still printed `ok`
- AC3 — `gen_build_index.py` — with the `U` print deleted from a kit copy, the suite prints `ok   check 21: a generator printing N and no U row reds instead of leaving the pin ungraded`
- AC4 — `bash tools/memory-tree/check-memory-hygiene.sh` — exits 0 on gov's tree, printing `memory-hygiene: check 21: the unbound pin grades 15 of N 15 unbound record(s), 0 exempt by RECORD_SERVES_CUTOFF or legacy-files.txt, against RECORD_UNBOUND_PIN=15`
- AC5 — `bash tools/check-kit-versions.sh` — exits 0 with memory-tree 2.99; `python tools/govkit/govkit.py epoch --base f8fdd873` reports no FAILED entry, and `bash tools/memory-tree/check-verdict-epoch.sh` is clean with the bump in the same commit as the last engine change
- AC6 — `tools/memory-tree/kit.toml` — the suite prints `ok   check 21: a pin above its graded count reds as slack, naming the value to lower it to` and `ok   check 21: the pin's measurement prints graded, total and exempt counts`; over the rev-2 engine both print FAIL and the suite exits 1 on those two alone. The descriptor's `--print-bindings` clauses hold over gov's own reply and over `N 0`, and fail over a U-less `N 2` reply, which the rev-2 descriptor held
