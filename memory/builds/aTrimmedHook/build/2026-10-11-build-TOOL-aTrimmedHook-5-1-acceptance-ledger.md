# TOOL-aTrimmedHook-5 — acceptance ledger

**Serves:** journal TOOL-aTrimmedHook-5

No merge bar and no self-test suite ran in this pass. Both arms were observed by running
`test_staged_render` alone through a slice: every arm held in 7.0 s. With the key read as blank in a
scratch copy, the AC1 arm printed FAIL, which is the arm observed RED.

**Evidences:** TOOL-aTrimmedHook-5
- AC1 — `gen_build_index.py --selftest` — with `LIVE_LANDED_UNCLOSED=1` in the conf passed to
  `check_staged_render`, a product-source file staged beside a no-id memory edit saw a render owed; with
  the key read as blank, the same arm saw a skip.
- AC2 — `gen_build_index.py --selftest` — the same staged pair with the key blank saw a skip, so the
  key still gates the wider read.
