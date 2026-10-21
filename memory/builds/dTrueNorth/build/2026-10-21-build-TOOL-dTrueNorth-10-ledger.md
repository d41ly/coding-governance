# TOOL-dTrueNorth-10 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-10

No merge bar, no self-test suite and no gate leg ran in this pass. The two records were written from
the spec's section 4 text by a scratch script that cut each fenced block out of the spec, added its
closing newline and graded it with `deviation_join.read_record` before writing it: both read with no
malformed field. Every criterion below was then observed by the CLIs the spec names over the working
tree on `d9def1b07` with this pass's files in it, after one `python3 tools/memory-tree/gen_build_index.py --write`.
The probes stand in for the `memory hygiene` and `spec tokens (a spec's own names resolve)` legs, which
the close runs; this unit lands no suite arm, so no `New arm:` line is owed.

**Evidences:** TOOL-dTrueNorth-10
- AC1 — `git ls-files 'memory/builds/dTrueNorth/build/*-deviation-*.md'` — with both records staged,
  it listed deviation-1 and deviation-4 of `TOOL-dTrueNorth-4`, `2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md`
  and `2026-10-21-build-TOOL-dTrueNorth-2-deviation-3.md`, among the eighteen records 1 to 20 of the tree.
- AC2 — `python3 "tools/memory-tree/deviation_join.py" --approval by-risk` — exit 0, its head "records
  18 (0 malformed) · refused 1", and no line naming `2026-10-21-build-TOOL-dTrueNorth-7-deviation-2`
  or `2026-10-21-build-TOOL-dTrueNorth-2-deviation-3`; the one `refused:` line names
  `2026-10-21-build-TOOL-dTrueNorth-20-deviation-20`, an author approver below the owner its risk
  loosening requires, which `TOOL-dTrueNorth-20` owns. `python3 tools/memory-tree/gen_build_index.py --print-bindings`
  exit 0, 3210 lines, no `A` row in the population, and one `S` row each: kind `deviation` serving
  `TOOL-dTrueNorth-7` and `TOOL-dTrueNorth-2`.
- AC3 — `grep -n 'cl-dClosedLoop-0002' memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`
  — line 10, its last cell deviation `2026-10-21-build-TOOL-dTrueNorth-2-deviation-3`, the head counting
  18 deviation records, up from 16. `python3 "tools/memory-tree/asbuilt_view.py" --check` — exit 0,
  "findings 0 · view at 59ff8f2ac". The red side, read in memory: the view as `HEAD` holds it, its row
  citing `baseline`, against the render over the tree's records gave one finding, "the file differs
  from its render from line 5 (a hand edit)".
- AC4 — `python3 "tools/memory-tree/design_lib.py" --design --build dTrueNorth` — exit 0, printing
  `cl-dClosedLoop-0002` at `6acd9ea9` with its since cell deviation `2026-10-21-build-TOOL-dTrueNorth-2-deviation-3`.
  `design_lib.derive_clause_hash` gave `6acd9ea9` for both the baseline clause and the record's
  `**After:**`, and `076b7d58` for that `**After:**` with its last byte changed, the drift the
  criterion's red case names.
