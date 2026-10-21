# TOOL-dTrueNorth-6 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-6

No merge bar, no self-test suite and no gate leg ran in this pass; the naming lexicon answered the
names the pass mints (`--suggest`, one identifier each). Every criterion below was observed by a probe
of the changed code over the working tree on `b1526808a`: the generator's own CLI on the tree, the
two CLIs in a scratch clone of the tree under the user temp directory, short-named, with this pass's
two modules copied in, and the host's verbs in-process over a throwaway fixture tree mirroring the
self-test's host case. The probes stand in for the `build-index selftest`, `memory hygiene` and
`spec tokens (a spec's own names resolve)` legs; those, and the `New arm:` line's RED-first
observation over `gen_build_index.py`'s self-test, are owed to the close.

**Evidences:** TOOL-dTrueNorth-6
- AC1 — `python3 "tools/memory-tree/asbuilt_view.py" --fixture --plant hand-edit` — exit 1, one
  finding: "the file differs from its render from line 15 (a hand edit)", line 15 being the
  `cl-dClosedLoop-0007` row whose text the plant edited; with no plant the same CLI exited 0 with
  findings 0.
- AC2 — `python3 "tools/memory-tree/asbuilt_view.py" --fixture --plant no-row` — exit 1, one finding:
  "fixture-deviation-3: departs from cl-dClosedLoop-0009 and carries no amends or supersedes row", the
  record whose `**Follow-through:**` is `gap gap-build-08`.
- AC3 — `python3 "tools/memory-tree/asbuilt_view.py" --fixture --plant no-citation` — exit 1, two
  findings: the hand edit at line 15, and "cl-dClosedLoop-0007: its text differs from the baseline's
  and cites no record", read from the edited body's row citing `baseline`.
- AC4 — `python3 "tools/memory-tree/asbuilt_view.py" --fixture --plant baseline` — exit 1, one
  finding: the design record's `Baseline:` line moved from 59ff8f2ac to b1526808a, the view rendering
  from the pin; the plant's note printed "cl-dClosedLoop-0119 renders the pin's text, not the working
  tree's loosened one", the rendered row equal to the pin's clause and the loosened text differing.
- AC5 — `python3 "tools/memory-tree/asbuilt_view.py" --fixture --plant pin-mismatch` — exit 1, one
  finding: "fixture-deviation-5: pins cl-dClosedLoop-0011@00000000, and the baseline's clause hashes
  8312590d", naming the record, the pinned hash and the baseline's.
- AC6 — `cmp <scratch>/product.md <scratch>/instrument.md` — exit 0 over the tree's 16 records, both
  files 237354 bytes, each written by its `--write --out` into the run's scratchpad, the head
  counting 16 deviation records and the `cl-dClosedLoop-0004` row citing deviation-4.
- AC7 — `cmp` — exit 0 in the scratch clone under `%TEMP%` carrying one more record whose
  `**Follow-through:**` is `supersedes cl-dClosedLoop-0020@42c7d579 by cl-dClosedLoop-0777`: both
  renders counted 17 records, `cl-dClosedLoop-0020` appeared in no row, and the dSafePassage row read
  `cl-dClosedLoop-0777`, the record's `**After:**` and deviation `2026-10-21-build-TOOL-dTrueNorth-6-deviation-99`.
- AC8 — `python3 tools/memory-tree/gen_build_index.py --check` — in that clone, after `--write`,
  exit 0; with the `cl-dClosedLoop-0300` row's text edited by hand, exit 1 listing the view's path
  twice under `build-index DRIFT`, at line 312 and as the clause citing no record; after one
  `python3 tools/memory-tree/gen_build_index.py --write` the same `--check` exited 0. With a record
  departing from `cl-dClosedLoop-0300` through `gap gap-mem-47`, `--check` exited 1 with an
  `as-built VERDICT` line naming `2026-10-21-build-TOOL-dTrueNorth-6-deviation-98`, and `--write`
  exited 0, wrote 1581 artifacts, `memory/LIVE.md` among them, and the view, printing the verdict.
  A hand-edited row whose clause a chain spec carries took two `--write` runs, the coverage region
  rendering from the view before the view is written, which `TOOL-dTrueNorth-16` S20 moves.
- AC9 — `python3 "tools/memory-tree/asbuilt_view.py" --fixture --plant amends-reader` — exit 0,
  printing that `read_design_view` reads hash 7e717036 for `cl-dClosedLoop-0007` and the since cell
  `deviation fixture-deviation-1`, and that `derive_clause_hash` of the record's `**After:**` is 7e717036.
- AC10 — `python3 "tools/memory-tree/asbuilt_view.py" --check` — in the clone with `DESIGN_VIEW` blank
  in `.memory-tree.conf`, it printed "as-built view: off — DESIGN_VIEW is blank in .memory-tree.conf,
  so nothing is read and no view is rendered" and exited 0. `python3 tools/memory-tree/gen_build_index.py --check`
  there, with `SPEC_CARRIES_CUTOFF` blank too since the coverage join refuses a blank `DESIGN_VIEW`
  first, printed the same off line, and its output diffed against the generator at `b1526808a` over the
  same tree differed in that line and in `memory/LIVE.md`'s Landed-unclosed count, which reads the
  product source the pass changed.
- AC11 — `python3 "tools/memory-tree/asbuilt_view.py" --check` — exit 0 with findings 0 over the tree's
  `DESIGN_VIEW` after this pass's `gen_build_index.py --write`, and `python3 memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py --check`
  exit 0 with findings 0 against the same file.
- AC12 — `git grep -n "asbuilt_view.py" -- tools/memory-tree/README.md` — printed the "What's here" row
  naming the generator, its host `gen_build_index.py` and its `as-built view: off` state.
