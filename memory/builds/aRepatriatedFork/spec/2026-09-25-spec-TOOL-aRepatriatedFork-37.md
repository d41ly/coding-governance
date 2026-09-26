# TOOL-aRepatriatedFork-37 — the unattended suite derives the repair pointer it asserts

**Status:** CLOSED · rev-2 · 2026-09-25 · node a · Tier-1 · base be3bbf21 · streams tooling · order 19

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/unattended/unattended.test.sh` asserted the preflight's repair pointer as the literal
`$TOOL_REL/memory-tree/gen_build_index.py`. The driver derives that path through
`derive_index_repair`, which follows the install receipt, so at inCMS, whose generator sits at
`scripts/gen_build_index.py`, the driver was right and the arm red.

## 2. Scope (IN)

- **S1** — The arm keeps the shape half, `the --write mode of `, and reads the path the message names.
  It asserts that path is a tracked `gen_build_index.py` in the tree the kit runs from, so no kit
  segment is spelled. Observed by AC1, AC2.
- **S2** — The class is graded, not the instance: every `hit` or `miss` in the unattended suites that
  names a sibling kit's file was read. The two others seed the file they then expect, in their own
  fixture, so they hold at any layout. Observed by AC3.
- **S3** — unattended takes its version bump in every carrier. Observed by AC4.

## 3. Non-goals (OUT)

- The driver, whose derivation is already right.
- The `GENERATED_INDEXES` arms at the dispatch verb, which declare the path themselves and compare
  declared data, so any spelling holds.

### Edges

- **hands-off** `DEPL-aRepatriatedFork-20` — the suite leg inCMS runs, which stops redding on its
  own generator's location.

## 4. Design

### Evidence

`lib-unattended.sh` `derive_index_repair` calls `resolve_kit_dir memory-tree gen_build_index.py`,
whose first rung is the receipt row whose `source` ends in `memory-tree/gen_build_index.py`. The
suite's `run` executes the host's own `unattended.sh`, so the resolver reads the HOST install, while
the arm spelled gov's layout.

`grep -nE '^\s*(hit|miss)\b.*(memory-tree|memory-recall|codebase-map|workflows|hooks|run-gates|lexicon|/lib/|drift-audit|runlog)/'`
over `tools/unattended/*.test.sh` found three more lines. `adopt-unattended.test.sh:139` expects
`${TR_T}memory-tree/gotchas.py`, which its `seed` writes at line 51. The two
`check-unattended.test.sh` check-31 lines name `vendor/harness/workflows/`, a prefix the arm itself
lays. `unattended.test.sh:1019` expects a probe-log substring its fixture writes.

### Inventory

No new function. One arm, now two assertions.

### Files touched (estimate)

`tools/unattended/unattended.test.sh` and the unattended version carriers.

### Alternatives rejected

- Calling `derive_index_repair` from the arm. The expectation would then be the function under test.

## 6. Acceptance criteria

- **AC1** — When the suite's prologue plus its S8 roster block runs as a slice in gov, it exits 0 at
  `SLICE n=35 st=0`. Red when: the pointer names no tracked generator.
- **AC2** — When the same slice runs in a scratch install that homes the kit at `scripts/unattended/`
  and its generator at `scripts/gen_build_index.py` through a receipt row, the new arm passes and the
  old bytes' arm fails with `FAIL missing: the --write mode of scripts/memory-tree/gen_build_index.py`.
  Red when: the new arm fails there too.
- **AC3** — The `grep -nE` in §4 Evidence, run over `tools/unattended/*.test.sh`, returns no line that spells a sibling kit's path the fixture did
  not lay. Red when: another arm expects a kit segment the host install resolves.
- **AC4** — `bash tools/check-kit-versions.sh` exits 0 and `python tools/govkit/govkit.py epoch`
  reports no FAILED entry. Red when: an unattended carrier kept 1.39.

## 7. Gates

`kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `harness arms (fail branches armed or pinned)` · `unattended kit gate` · `unattended skill wiring` · `install-prefix (shipped surface)`

New arm: none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-25 · initial draft, from the owner's ruling.
- rev-2 · 2026-09-25 · §4 Evidence · AC3 · the class grep and its three non-instances recorded.
  Built: green in gov's layout and in a foreign one, red on the old bytes there.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "the path a resolver found for a sibling kit's generator"`
ranked `resolve`, `kit_rel` and `resolve_memory_root`, none of them the driver's resolver; it prints
`unscanned layers: .sh`. The seam is `derive_index_repair` in
`tools/unattended/lib-unattended.sh`, found by grepping the message, and the arm now reads its
output rather than restating its layout.

Recall terms used: `derive_index_repair resolve_kit_dir gen_build_index repair pointer receipt kit
prefix TOOL_REL suite arm foreign layout`.
