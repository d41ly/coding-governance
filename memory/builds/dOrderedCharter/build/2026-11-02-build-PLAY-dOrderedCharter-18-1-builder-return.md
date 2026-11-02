# dOrderedCharter — unit 18's builder return

**Serves:** journal PLAY-dOrderedCharter-18

Run wf_dbafc3a3-915, summarized from its return.

- Built at rev-3 as pass commit `2d03321ab` (35 files) and follow-up `ea949af20`, which renames the new verdict-epoch arm's fixture locals after the bug-class checklist flagged a reused name. Both carry `Pass: PLAY-dOrderedCharter-18`.
- `tools/memory-tree/id_grammar.py` holds the grammar, the conf layer, check 27's four record readers and its four index names; memory-recall's `extract.py`, `recall_conf.py` and `bench.py` re-export them. `Conf.digest` folds the SHA-1 of `id_grammar.py`.
- Deviation 184 (`report`): S3 says each recall file already carries a `resolve_kit_dir` copy; `recall_conf.py` and `bench.py` did not, so a copy was added to each.
- The dClosedLoop as-built view is committed outside the declared write set: `gen_build_index.py --write` rewrote it when deviation 184 raised its record count.
- Observed by probe: AC2, AC4, AC5, AC6, AC7, AC8, AC9. The naming lexicon exits 0.
- Owed: AC1 and AC3 at PLAY-dOrderedCharter-49's pass, per spec 18's §3 Edges; AC10 (`check-kit-versions.sh` on a planted mismatch) at the close.
- Owed at the close, RED then GREEN: check-verdict-epoch.test.sh 5f (two arms); manifest-check.test.sh F1 and KQ R0; merge-rows.test.sh fixture and absent-grammar arms; corpus_ids `nowhere` and `oldkit`; row_grammar check 27's refusal arms; check-wiring dead-grammar and no-id_grammar arms; transition-audit AC15 and AC10; the recall selftest's digest arm. Also every §7 gate and changed suite: check-memory-hygiene, check-unattended, straggler-guard, the drift-audit selftest.
- Skipped by the builder: `packet.py --check dOrderedCharter` at its 300 s bound.
