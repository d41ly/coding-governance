**Serves:** journal TOOL-dTotalRecall-49
**Caused-by:** TOOL-dTotalRecall-49

# TOOL-dTotalRecall-49 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `22c3f2cc2` from [2026-11-22-prompt-TOOL-dTotalRecall-49-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-49-build-brief.md), recorded whole; the pass tip is `60424d69e`.

## Why

TOOL-dTotalRecall-49 is built as its rev-3 spec states and committed as one pass commit, 60424d69e. The commit ends with a `Pass: TOOL-dTotalRecall-49` trailer and closes the spec's status header (CLOSED, 2026-11-23).

## Summary

**Built (one commit, 60424d69e, on base 22c3f2cc2):**
- **S1:** `VIEW_HEAD` and the module docstring in `tools/memory-tree/asbuilt_view.py` are back to their bytes from before unit 36. The file now matches its blob at `7ffe749aa^` exactly. `gen_build_index.py --write` re-rendered `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`, and the only change was removing the `**Caused-by:** PLAY-dClosedLoop-1` line. The docstring clause naming this unit went too, because AC2 counts every `Caused-by` in the module; that choice is recorded in a `Decided:` trailer.
- **S2:** `tools/memory-tree/record_causes.py` has two new constants, `KEPT_INSTRUMENT` (S2's reason) and `KEPT_INSTRUMENT_KEY` (the path spelled in parts). The file is keyed in `CAUSE_WRITER_KEPT`.
- **S3:** inside `check_cause_writers` (no new function), a file kept for that reason is red, with its reason printed, in three cases:
  - `design_lib.read_design_keys` over `read_design_conf` returns the off state;
  - it refuses (`DesignRefusal`);
  - `DESIGN_VIEW` has no `-` row, read through `read_legacy_paths`, which goes through `legacy_ledger` `read_registrations` and `read_ledger`.
- **Plant:** the new plant `kept-instrument-not-legacy` in `write_fixture` seeds a fixture view in the legacy tree, cuts its `-` row, sets the four design keys and plants `tools/memory-tree/asbuilt_view.py`.
- **Arm:** added to `tools/memory-tree/check-memory-hygiene.test.sh`, beside unit 36's census arm.
- **Also in the commit:** the acceptance ledger `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-49-1-acceptance-ledger.md`, `RUN.md`, and what `gen_build_index.py --write` re-rendered (`memory/LIVE.md`, `memory/backlog/TOOL.md`, the dTotalRecall README, the spec's records block). `gen_map.py --write` changed nothing.

**Checks that ran (fixtures and probes of this unit's own code only; no gate, suite or bar):**
- **AC1:** `asbuilt_view.py --check` and the instrument's `--check` each printed findings 0 and exited 0 on the worktree after the re-render. This stands in for the `memory hygiene` check 30 parity, which the pre-commit hook also reported as "as-built clean".
- **AC2:** `grep -c Caused-by` over `asbuilt_view.py` printed 0.
- **AC3:**
  - `record_causes.py --check`, run from `tools/memory-tree/`, printed one `cause-writer` line keeping `asbuilt_view.py` with S2's reason, then `8 census file(s) · 8 kept · 0 red`, green, exit 0. This stands in for the `record causes` leg.
  - `--fixture --plant kept-instrument-not-legacy` exited 1, naming the planted instrument red. The arm's two `hit` strings were grep-checked against that output, and the writer-without-cause and legacy arms' count lines were unchanged. This stands in for the memory-hygiene self-test arm.
  - A scratch probe (`C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/probe49.py`) over the same fixture showed the rule can go both ways: with the row restored the file reads kept and exits 0; with the design keys removed it reads off and exits 1; with one key blank it reads refuse and exits 1.
- **Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` exited 0. Acted on it: the "fixture passes by finding nothing" class is answered by that restored-row control, and the "grep for a word" class on AC2 is backed by AC1's two checks.

**Owed to the close:**
- AC1 and AC3 re-run at the pass tip.
- The legs in spec §7: `memory hygiene`, `kit/dogfood doc parity`, `recall floor`, `recall floor arms`, `lexicon naming predicates`, `chain-packet self-test`, `policy fixtures`, `memory-hygiene self-test`, `install-prefix (shipped surface)`, and the `record causes` leg.
- The RED-first observation of the new arm (`check-memory-hygiene.test.sh`, TOOL-dTotalRecall-49 AC3 block), staged by skipping S3's legacy-row test for the reason.
- The view's blob moved, so both chain packets that pin it need re-rendering by the main loop, as they were after unit 48.

**Observed for the close:** in a repo where the design keys are off and the census runs, the shipped `asbuilt_view.py` reads red, as S3 specifies. In this tree the fixture never got that far: `run_check` returns unarmed before the census when the legacy population is absent.

Nothing was skipped. The `--brief` verb reported the brief already recorded and unchanged.
