**Serves:** journal TOOL-dTotalRecall-2

# TOOL-dTotalRecall-2 build pass 2 — the builder's return

The gov-builder return for the pass dispatched at `9e0dfdb00` from [2026-11-22-prompt-TOOL-dTotalRecall-2-build-brief-2](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-2-build-brief-2.md), recorded whole; the pass tip is `d91388c2f`.

## Why

TOOL-dTotalRecall-2 is built and committed as d91388c2f with a `Pass: TOOL-dTotalRecall-2` trailer, and its spec status is now CLOSED. Rev-13's fix to §8 F6's mark let the pre-commit hook accept the CLOSED status, which was the only reason pass 1 diverged. Nothing else in the spec diverged from the code.

## Summary

TOOL-dTotalRecall-2 is built and committed as d91388c2f5cad72e9210e620b90910740f7c2dee on base 9e0dfdb009f5d58b9521fdb9ae47daaaef3b1ed0. The pre-commit hook passed and the spec moved to CLOSED. Every criterion AC1 to AC10 was observed by probe. The suite arms, the RED-first observation and the legs on the spec's gates section are owed to the close.

**What this pass did**
- `--brief` reported the brief already recorded, unchanged, so it wrote nothing.
- Re-applied pass 1's patch with the brief's excludes. It applied clean at this base.
- Renamed the ledger to `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-2-2-acceptance-ledger.md` and rewrote it for pass 2.
- Re-read the code against rev-13. Rev-13 changes only §8 F6's mark, and nothing in the code diverges from the spec.
- Set the spec status to CLOSED. That is the only spec edit; the generator rewrote its records region.
- Ran `gen_build_index.py --write` and committed what it rewrote: `memory/builds/dTotalRecall/README.md`, `memory/LIVE.md`, `memory/backlog/TOOL.md` and the dClosedLoop as-built view, whose deviation count went to 2354.
- Re-ran `gen_map.py --write` and `record_kinds.py --write`. Neither changed anything, and the gen:record-kinds region reads the same in `tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md`.

**Deviation 26, added this pass**
Pass 1 left a gap: the names and rules the spec does not state (the `Decided:` lines) had no deviation record. I added `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-2-deviation-26.md`, declared first with `--dispatch` (refused nothing). It records `read_kind_row`, `DOOR_WRITER`, `SEQ_RULE`, the `check` hook on `write_record`, `run_claim_cli`, how the content key is built, where the ask family comes from, the absent-session rule, the `unarmed — no loop kit` line, the refused placeholders and the minimal-seed fixtures. `build_records.py read` exits 0 on it.
- I wrote it by hand as deviation 26, in this unit's block after 21 to 25. The door would have minted it as 1002, past the build's per-unit numbering; the commit's `Decided:` trailer says so.

**Checks that ran (no gate, suite or bar ran)**
- Probe `C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/tdr2_pass2_probe.py`: `gov_record.py new` calls in a seed repo and its clones under `%TEMP%/gr2p`, over a bare remote. 24 of 24 checks OK:
  - AC1, both halves, including the planted `writer = "runlog"` row.
  - AC2, AC3, AC8 and AC10.
  - AC4: the next `<n>` is written.
  - AC5, all five cases; this node's fleet tag resolved to `d`.
  - AC6, with a remote and without.
  - AC7's twin specs, byte-equal.
  - AC9: the `tomllib` check of the registry, plus `new exception` refused.
- AC7's `build-readme dLoop` half, run with pass 1's `ac7_readme.py` in the same scratch directory: exit 0, the README has its `slug-grammar:` line, and the remote holds `refs/gov/claims/dLoop`.
- AC4's second half, on a clone of the pass tree with no `refs/gov/` and this pass's code copied in: `new spec TOOL-dTotalRecall-2 --tier 2` exited 2 naming the existing spec.
- These probes stand in for the `memory-hygiene self-test`, `record-kinds`, `build-index selftest` and `policy fixtures` legs.
- `lexicon.py --suggest` printed OK for every new Python function and every shell helper. `lexicon.py --measure` left `VERB_OFFENDER_PIN` at 1448. These stand in for the naming leg.
- `bash -n` passes on `tools/memory-tree/check-memory-hygiene.test.sh`.

**Owed to the close**
- The `New arm:` RED-first observation in `tools/memory-tree/check-memory-hygiene.test.sh`, covering AC1 to AC10. Its three staged breaks are dropping the key comparison, the authority read, and the `--name` grammar test, each in turn.
- The `memory-hygiene self-test` leg that runs those 31 new assertions, with the floor raised 797 to 828.
  - 8 of the assertions need the unattended kit and skip aloud without it.
- Every other leg in §7.

**Checklist after the commit**
`gotchas.py --for-diff HEAD~1..HEAD` exited 0 and listed 44 classes. I went through the ones that apply:
- The arm captures carry `:-NONE` fallbacks, so a capture that is empty fails its assertion.
- No source was written through a heredoc.
- `gov_record.py` sets `dont_write_bytecode`, so a staged break cannot run stale bytecode.
- Writes use LF and UTF-8, and the gov-claim call goes through `resolve_bash`.
- The ledger rename was staged on both sides.
- The one `|` in the README is in a code block, not a table cell.

Nothing needed fixing. No command hit its timeout, and the scratch fixture repos under `%TEMP%` are removed.
