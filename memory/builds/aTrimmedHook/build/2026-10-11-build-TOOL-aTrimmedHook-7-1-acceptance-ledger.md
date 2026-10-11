# TOOL-aTrimmedHook-7 — acceptance ledger

**Serves:** journal TOOL-aTrimmedHook-7

No merge bar and no self-test suite ran in this pass. AC1 to AC3 were observed by running
`test_staged_render` alone through a slice: every arm held in 8.6 s. With the three mechanisms
inverted in a scratch copy, all three arms printed FAIL, which is each observed RED. AC4 was observed
through a slice of the manifest-check self-test's helpers and the new arm, run against this pass's
checker and against the pre-unit one; the arms 1 to 21 range and both new blocks were re-run against
this pass's checker as well. The close owes the whole `build-index selftest` and
`manifest-check self-test` legs.

**Evidences:** TOOL-aTrimmedHook-7
- AC1 — `gen_build_index.py --selftest` — with `os.path.relpath` made to raise `ValueError`,
  `check_staged_render` answered a skip instead of raising; with the guard removed it raised.
- AC2 — `gen_build_index.py --selftest` — a path holding a lone surrogate round-tripped through
  `build_blob_request` to its original byte; with the strict encode it raised.
- AC3 — `gen_build_index.py --selftest` — a file staged under a kit directory inside the fixture root,
  reached through `here`, saw a render owed; with `here` ignored it saw a skip.
- AC4 — `manifest-check.sh` — on a fixture whose watch directory holds 100 ASCII files and one
  non-ASCII file it printed the WARN naming `matches 101 tracked files`; the pre-unit checker printed
  no such line, observed RED.
