**Serves:** journal TOOL-dTotalRecall-50
**Caused-by:** TOOL-dTotalRecall-50

# TOOL-dTotalRecall-50 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `4c50b60eb` from [2026-11-22-prompt-TOOL-dTotalRecall-50-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-50-build-brief.md), recorded whole; the pass tip is `7f51d13dd`.

## Why

TOOL-dTotalRecall-50 is built as the spec states, and it is committed with the spec header set to CLOSED · rev-4 · 2026-11-23. I checked the spec against the tree before writing anything. Every cited symbol is there: record_kinds.py#read_tracked and #read_memory_root, backlog.py#parse_file and #build_grammar, id_grammar.py#parse_id_parts, gov_record.py#write_new_ask, tree_lib.py#BIND_HEAD_LINES and #read_bindings, deviations.py#derive_report_path and #render_report, and packet.py's INSTRUMENTS and read_asks. The deviations.py blob at HEAD is still 30a1f15b. The build folders track 104 code files, and the 9 census hits are exactly the ones in the spec's §4 table. Nothing diverged.

## Summary

Committed 7f51d13dd on branch/unattended-dtotalrecall-ae256e (base 4c50b60eb). The pass works: the shipped row reads as filed on the real tree, and both new plants PASS. No gate, suite or bar ran.

**What changed**
- `tools/memory-tree/record_causes.py`:
  - S1: the writer census now also reads every tracked `*.py`, `*.sh` and `*.js` file under `<memory root>/builds/*/build/` (new `read_build_code_paths`). Both tests read past the 12-line binding window, so a file's own binding line is never a hit.
  - `CAUSE_WRITER_KEPT` gains 8 entries keyed by repository path:
    - reason `pinned instrument`: dClosedLoop's asbuilt.py and packet.py.
    - reason `outside the write set`: dClosedLoop's walk.py, fold-inventory.py and walk-seed.py; aMendedFleet's harness.py and ab.py; dDerivedDocket's signer.py.
  - S2: new `CAUSE_WRITER_PINNED` holds one row: dClosedLoop's deviations.py, the departures glob, and the ask PLAY-dClosedLoop-1002. The row is red when its instrument is not tracked, when it spells Caused-by past its binding window, or when its ask is not filed (new `check_ask_filed`).
  - S3: while that row stands, a new departures record with no Caused-by line counts as caused by its first Serves id, in both the causes check and the orphan check (`read_pinned_records`, `derive_record_cause`).
  - Two new plants, `pinned-writer-drained` and `departures-pinned` (`render_pinned_instrument`, `check_pinned_plant`).
  - `run_check`, `read_grading` and `check_cause_writers` take a `pinned` argument. The fixture plants pass their own row, and every other plant passes none.
- The arm for AC2 and AC3 is added to `tools/memory-tree/check-memory-hygiene.test.sh`.
- S4: the ask was filed through `gov_record.py new ask --build dClosedLoop --family PLAY --sev LOW`. The door's counter handed out PLAY-dClosedLoop-1002, not 39, so that is the id the row names.
- Also in the commit:
  - the acceptance ledger `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-50-1-acceptance-ledger.md`
  - `memory/map/generated/symbols.json` (rebuilt with `gen_map.py --write`)
  - the files `gen_build_index.py --write` rewrote: `memory/LIVE.md`, `memory/backlog/PLAY.md`, `memory/backlog/TOOL.md`, and the dClosedLoop and dTotalRecall READMEs
  - `RUN.md`
- I declared the four undeclared generator outputs with a second `--dispatch`, which succeeded.

**Checks that ran, and the gate each stands in for**
- AC1, standing in for the `record causes` leg: `python record_causes.py --check` from `tools/memory-tree/` exited 0 (green).
  - It printed the pinned row for deviations.py as `ask PLAY-dClosedLoop-1002 · filed`, with its glob reading 27 records (DERIVED, that check).
  - The instrument's census line sits at its line 39, each other §4 file shows as kept with its reason, and no line points at a binding head.
  - The build-folder count line reads `104 code files · 9 census file(s) · 8 kept · 1 pinned · 0 red`.
  - `gen_build_index.py --asks --build dClosedLoop --json` lists the id at line 30. Its row names no build slug except dClosedLoop inside its own id.
- AC2 and AC3, standing in for the `memory-hygiene self-test` arm:
  - `--fixture --plant pinned-writer-drained` PASS: the first check exits 1 naming the row as drained; the second, with the ask row deleted, exits 1 naming TOOL-fRoot-2 as not filed.
  - `--fixture --plant departures-pinned` PASS: green while the row stands; with the row cut it exits 1 naming the record.
  - I re-ran eight existing plants (legacy, causeless, writer-without-cause, kept-instrument-not-legacy, bulleted-cause, script-causeless, backfill-selection, backfill-refusals); each gave its exit code from before the pass.
- I checked the arm's expected strings with `grep -F` against the saved plant output, without running the suite.
- Naming lexicon: OK for all five new helpers.

**Owed to the close**
- The spec's legs on the spec's gates section and the `record causes` leg.
- The `New arm:` RED-first observation of the TOOL-dTotalRecall-50 block in `check-memory-hygiene.test.sh`, staged two ways: by skipping the row's drain and filed-ask tests, and by skipping S3's interim read.

**Bug-class checklist** (`gotchas.py --for-diff HEAD~1..HEAD`) ran and I went through it. Three things it surfaced that the close should know:
- The fixture plants use their own row, so the shipped row's PLAY id and dClosedLoop backlog are only checked by AC1 on the real tree.
- The `pinned instrument` entries repeat membership of the packet's INSTRUMENTS list, and the departures glob repeats the name `deviations.py#derive_report_path` gives. Both are copies the spec asks for.
- If no build-folder file is found, the census prints a count of zero rather than failing.

**Skipped and inherited**
- Nothing was skipped. The second `--dispatch` ran past its 120 s bound (DERIVED, the builder's command limit) and I let it finish in the background before committing.
- That dispatch printed one existing problem in another build: dWitnessedBar's packet `--check` shows 1 finding on its instrument-pin check.
