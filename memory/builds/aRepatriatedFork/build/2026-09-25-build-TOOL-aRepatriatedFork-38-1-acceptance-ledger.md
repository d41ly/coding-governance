# TOOL-aRepatriatedFork-38 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-38

Written by the unit pass on node a. The probe was a scratch script outside the tree, feeding each
reader a temp conf. The arms ran as slices or direct calls: the memory-recall prologue through its
bash-parity arm, `test_conf_grammar` and the new process-monitor arm called directly, the
spec-tokens prologue plus its two new arms, `render_playbook.py --selftest` whole, and the lexicon
prologue plus its `--scaffold` block. Temp slice files were removed. The old-bytes run swapped in
`HEAD`'s seven readers and restored them, byte-compared.

**Evidences:** TOOL-aRepatriatedFork-38
- AC1 — `lexicon_conf.load_conf` — the probe on old bytes printed seven `BAD` rows, among them `BAD  lexicon_conf.load_conf: A='"2026-09-10 node a"   # a trailing note'`, `BAD  map_lib.load_conf: A='"2026-09-10'` and `BAD  check-spec-tokens read_conf_key: A=''`, beside `ok   bash source (the reference): A='2026-09-10 node a' B='plain'`; after the fix every row prints `ok`
- AC2 — `tools/memory-recall/selftest.py` — every arm passes on the built tree. With the old readers: `FAIL conf parser == bash … NOTED: python '"a' != bash 'a quoted value'`; codebase-map `FAIL "a`; `FAIL test_read_roots_drops_a_trailing_comment (got (['/c/a/one', '/c/b/two"', '#', 'note'], …))`; `arm FAIL  a quoted cutoff with a trailing comment still arms the join — expected rc 1, got 0`; `arm FAIL a conf value keeps no trailing comment — got ('mem ory"   # note', 'TOOL   # note')`; and the two lexicon arms in `FAILURES`. `bash tools/check-spec-tokens.test.sh` exits 0 whole
- AC3 — `bash tools/check-kit-versions.sh` — exits 0 with codebase-map 1.11, lexicon 1.9, memory-recall 1.15, playbook-render 1.8 and process-monitor 0.6; `bash tools/lexicon/adopt-lexicon.sh --check` and `bash tools/memory-recall/adopt-memory-recall.sh --check` exit 0
