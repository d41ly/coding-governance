**Serves:** journal TOOL-dFramedEntrypoint-2

# Acceptance ledger — TOOL-dFramedEntrypoint-2

*Node d, 2026-08-24. Every line carries the command that made the observation.*

**Evidences:** TOOL-dFramedEntrypoint-2

- AC1 — `budget_findings` — a slot body over its declared ceiling produces a hard finding naming the
  slot, the file, the measured bytes and the ceiling, and `--check-format` returns it in the same
  list as a slot-contract violation so one red reports both classes.
- AC2 — `budget_findings` — a slot over its recorded high-water and under its ceiling produces an
  ADVISORY finding, printed before the verdict and never added to the exit-code path.
- AC3 — `python tools/memory-tree/gen_build_index.py --check-format` — the advisory prints on stdout,
  which the runner persists per leg under the git common dir. The advisory is UNOBSERVABLE through
  the runner's own summary on a green leg, which is why AC4's verb exists and why this line does not
  claim the runner surfaces it.
- AC4 — `python tools/memory-tree/gen_build_index.py --report` — prints every canonical slot with its
  ceiling, and with an empty bound population says so explicitly rather than printing an empty table.
- AC5 — `python tools/memory-tree/gen_build_index.py --bump` — rewrites
  `build-readme-slot-highwater.txt` only; `build-readme-slot-limits.txt` is never opened for writing
  by that verb.
- AC6 — `_assert_slot_table` — an absent limits file raises, naming the expected path, rather than
  skipping. Asserted on EVERY run of `--check-format`, not only while grading a bound file.
- AC7 — `a limits row for an unknown slot is a refusal` — the arm. A ceiling outliving its slot
  silently widens what it was written to bound, which is the second direction of the
  declared-population rule.
- AC8 — `bash tools/run-gates/run-gates.sh` legs run individually: hygiene, slot contract,
  build-index selftest, check-arms, check-wiring, govkit selfcheck, dead-path carriers, marker
  contracts, codebase-map coverage + freshness — all green. The bar's green over the slot budget is
  VACUOUS today and this line says so: the bound population is empty until unit 3 writes the registry
  and unit 7 seeds it, which is why unit 7 owns the one real seeding event.
- AC9 — `a limits table missing a canonical slot is a refusal` — the arm, watched failing against the
  staged break below before it was written.
- AC10 — `git diff --stat` after `--bump` shows only the high-water file modified.
- AC11 — `python tools/memory-tree/gen_build_index.py --selftest` — PASS, 102 `arm ok` lines against
  95 before this unit. The bare bar HOLDS that leg, so this unit's Definition of Done is
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` and the leg was run standalone.
- AC12 — `unarmed_slots` — a row present with no value is the ANNOUNCED unarmed state: the leg names
  how many slots ship unarmed on every run, and it is distinguishable from a missing row, which
  refuses.
- AC13 — `build-readme-slot-highwater.txt` — absent, it is legal and read as no recorded baseline,
  while an absent `build-readme-slot-limits.txt` refuses. The two files are declared separately and
  fail differently, which is the whole reason rev-2 split them.

## The defect this unit shipped for one commit, and what caught it

`_read_slot_table` skipped any line starting with `#`. Every canonical slot heading starts with `#`,
so the table parsed to EMPTY and the leg reported five slots as deliberately UNARMED — a plausible,
green, entirely wrong state. Found by running `--report` and reading five `UNARMED` lines where five
numbers were declared.

The repair is two things, not one. The comment predicate became "a line with no tab". And
`_assert_slot_table` now runs on EVERY `--check-format`, not only while grading a bound file — because
with an empty population nothing ever validated the declaration, and a data file's integrity cannot
depend on whether anything happens to be using it.

Staged break, observed: restoring the `#` predicate makes two arms fail AND makes the leg exit 1
naming the first missing row. Before the always-on assertion, the same break exited 0.

## Adopter

`kit.toml` gains the `slot-budget-ceilings` hole with a discharge probe, and
`adopt-memory-tree.sh` strips the VALUES from the limits file at scaffold while keeping the ROWS —
because a row with no value is legal and announced, and a missing row is a refusal. Verified by
running the strip's awk over a fixture: rows survive with an empty value field, comments pass
through. `role = "seed"`, after `role = "data"` was refused by govkit selfcheck as not a declared kind.
