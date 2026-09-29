# TOOL-aRepatriatedFork-39 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-39

Written by the unit pass on node a, 2026-09-28. The old-engine runs loaded `corpus_ids.py` as
`869209ed` holds it from a temp copy inside the kit dir and called its `_scratch`, `walk`, `checks`
and `_measure_lines` over the new arms' fixtures; the copy was removed after. The hygiene suite ran
as a slice, its prologue plus the (d2) rotation block, in a temp file inside the kit dir, removed
after.

**Evidences:** TOOL-aRepatriatedFork-39
- AC1 — `corpus_ids.py --selftest` — `arm ok    check 14 grades present-tense citations only, as check 15 does` on the built tree; the 869209ed engine reports `check 14: id ARCH-tPast-7 is cited but never defined` and the same for `ARCH-tPast-8` over that fixture. The present-tense control reports `check 14: id ARCH-tGhost-9 is cited but never defined` on both engines
- AC2 — `corpus_ids.py --selftest` — `arm ok    a waiver row no present-tense file cites is stale`, whose finding reads `waives ARCH-tPast-7, which no present-tense file cites — stale row`; the 869209ed engine reports no stale row there, only `ARCH-tPast-8` as an unwaived orphan
- AC3 — `corpus_ids.py --selftest` — `arm ok    --measure's pin equals check 14's orphan count` (`1 == 1`) and `arm ok    ...and the pin --measure prints is the count check 14 grades` (`ORPHAN_ID_PIN="0"`); the 869209ed engine gives `ORPHAN_ID_PIN="2"` over the past-tense fixture, and `ORPHAN_ID_PIN="2"` with 2 graded orphans over the mixed one
- AC4 — `bash tools/memory-tree/check-memory-hygiene.sh` — exits 0 on gov's tree; `python tools/memory-tree/corpus_ids.py --measure` prints `ORPHAN_ID_PIN="0"`, the pin gov declares, before and after. The rotation slice prints `slice: st=0 n=7`; with the fixture's pre-unit `memory/README.md` it prints `FAIL check 14 did NOT flag a rotated id whose archive is present-but-unstaged` and `st=1`. `bash tools/check-kit-versions.sh` exits 0 at memory-tree 2.100, and `python tools/govkit/govkit.py epoch --base f8fdd873` reports no FAILED entry
