**Serves:** journal TOOL-dFramedEntrypoint-5

# Acceptance ledger — TOOL-dFramedEntrypoint-5

*Node d, 2026-08-25. One commit, as the spec requires: splitting the tuple change from the corpus
surgery was measured at 750 slot-contract violation lines.*

**Evidences:** TOOL-dFramedEntrypoint-5

- AC1 — `git ls-files 'memory/builds/*/README.md' | xargs grep -lF -- '<!-- gen:build-docs -->' | wc -l`
  returns 0, from 62 before the write. Scoped to the graded class and terminated, because a repo-wide
  grep cannot return zero: ten tracked non-README files carry the string, this build's own specs
  among them.
- AC2 — the same probe over `| Record | Kind | Serves |` returns 0 across the class.
- AC3 — `render_region` — a build with an unnamed unit id renders the line naming it.
- AC4 — `render_region` — a build with no spec-audit record for a unit renders the second join.
- AC5 — `a fully-covered build STILL renders both joins, saying none` — the arm. Both joins are now
  UNCONDITIONAL: each used to hide behind its own non-empty test, so a build with FULL coverage
  rendered nothing and was indistinguishable from one whose joins were never computed. Full coverage
  is the common case, not the rare one.
- AC6 — `python tools/memory-tree/gen_build_index.py --selftest` — PASS, and it completes without the
  `IndexError` that the round-2 audit predicted and that fired on the first run of this unit: an arm
  iterating `for _i in (3, 2, 1)` over `GEN_REGIONS`. Every region-addressing arm now names its
  region. No grep for the marker string could have found that arm.
- AC7 — `python tools/memory-tree/gen_build_index.py --check-format` exits 0 on the post-surgery tree.
- AC8 — `bash tools/memory-tree/check-memory-hygiene.sh`, `bash tools/check-kit-versions.sh`,
  `python3 tools/codebase-map/test_codebase_map.py`, `bash tools/memory-tree/marker-contract.test.sh`,
  `bash tools/check-dead-paths.sh`, `python tools/govkit/govkit.py selfcheck` — all green. Corpus
  measured at 473,203 B across 62 build READMEs.

## What drained, measured rather than claimed

The registry was EMPTIED and the gate re-run, so the surviving rows are the ones that still red rather
than the ones that look like they might. Five of eight drained: `aPacedTurnstile`, `aDrainedSluice`,
`dUnstalledConvoy`, `aRuledFrontispiece` and this build's own row. Every one was renderer-shaped and
said so in its own text.

`TOOL-dUnstalledConvoy-13` closes with them. Its row said a build's spec-audit record cannot fit the
generated bindings row past about eleven units, because the row must spell every id it serves. There
is no bindings row.

Three README rows remain and all three are AUTHORED prose over an authored cap, which is what the
registry was for: `aBoundedVerdict` at 38,261 B (down from 44,872), `cBriefedPilot` at 27,895 (down
from 32,023), and `aUnmannedHelm` for a single 419-character line.

## Found while draining, and written into the registry

`memory/backlog/TOOL.md`'s row silences checks 6, 7 AND 8. With the registry emptied, check 8 reds on
line 34 — so that row is currently hiding a real status-token fault as well as the width it was
opened for. Recorded in the row rather than fixed here: the file belongs to no single build and
rotating it is its own work.

## The three selftest classes, and which one hurt

Class (a), the tuple-index arms, raised `IndexError` and stopped the harness — loud, immediate,
predicted. Class (b), the records-table arm, failed by name. Class (c) was the expensive one: eighteen
arms testing `strip_records_sentence`, whose subject this unit retires. The sentence they asserted on
was the record selector's LIVENESS assertion — nine arms detected a mis-segmented selector by noticing
it had gone missing — so what replaces it is a counted `Records: <n> bound to this build` line and a
positive arm over a fixture that holds a record. A build holding one record and reporting zero is the
same mis-segmentation, said out loud instead of inferred from an absence.
