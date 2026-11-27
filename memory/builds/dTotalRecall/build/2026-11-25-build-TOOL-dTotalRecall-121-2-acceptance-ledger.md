# TOOL-dTotalRecall-121 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-121
**Caused-by:** TOOL-dTotalRecall-121

No merge bar, no self-test suite and no gate leg in this pass. The builder built spec rev-3 over base
`5daf07165fd8c427667ee0f3e020c2a030fd55e8`, 2026-11-25 local, in one commit, from the first pass's draft with rev-3's
edits on it. §7's legs, `record_kinds.py --selftest`, and the RED-first observation of every `New arm:` line are owed
to the close.

**Evidences:** TOOL-dTotalRecall-121
- AC1 — `field-name-newline` — `python build_records.py --fixture --plant door-header` refused it and `field-name-twice`, exit 2 each, and printed PASS with 24 cases; `write_record` raised ValueError for both (DERIVED 2026-11-25, that run and a probe).
- AC2 — `read_mint_authority` — stubbed, both absent answered the announced line and `owner`, the holder named and the caller absent raised naming `s-other`, the holder absent and the caller named answered the line (DERIVED 2026-11-25, the probe).
- AC3 — `index-lock` — `door-header` and `ask-door` each exited 2 on it naming git's refusal, with the record gone and `BACKLOG.md` as it was, and the same call with the lock gone wrote; `ask-door` printed PASS with 17 cases (DERIVED 2026-11-25, the two runs).
- AC4 — `bash gov-claim.sh slug d2026-10-26ClosedLoop --claimant <key>` — exited 0 and the `ask` verb minted `TOOL-d2026-10-26ClosedLoop-1`, over a scratch clone and bare remote whose landed policy reads `in-slug`; `slug -x` and `slug 9x` exited 2 (DERIVED 2026-11-25, the probe). The `test_slug_claims` arms are owed to the close.
- AC5 — `python record_find.py --fixture --plant section-outside` — printed `names no section of`, `exit 2` for the first id and the section for the file's stem; `unheld-blob` exited 0 and `missing-section` 2 as they stand (DERIVED 2026-11-25).
- AC6 — `grep -c 'record_kinds.py" --selftest' tools/memory-tree/check-memory-hygiene.test.sh` — printed 1, and the table-only stub's `run_selftest` named the planted member and nothing on today's tuple (DERIVED 2026-11-25). The selftest itself is owed to the close.
- AC7 — `python shape_run.py --fixture --plant <case>` — each of the 8 plants exited and printed as its row says, and with its branch cut in an in-memory copy each red plant exited 0, `malformed` among them (DERIVED 2026-11-25).
- AC8 — `python record_causes.py --fixture --plant <case>` — the 3 census plants printed PASS, and the suite's join was green whole and named each plant whose arm was cut (DERIVED 2026-11-25).
- AC9 — `grep -n 'by TOOL-dTotalRecall-121' tools/memory-tree/check-memory-hygiene.test.sh` — printed one raise line, 842 to 879, its 37 assertions counted by reading (DERIVED 2026-11-25). The close's half, the count of a whole run with its `n_skip` and comment line, is owed there.
- AC10 — `measure_bytes_before_act` — read 1461 with the pipe and 500 with `sed -n 1,5p a.py>b.py`; `check_read_call` answered False for the 3 glued writes and True for the 3 reads; `derive_map_verdict` answered `("win", [])` armed and `("unarmed", ["bytes"])` unarmed (DERIVED 2026-11-25, the probes).
- AC11 — `grep -cE '^(cardinality-refused|prose-pass)[|]' tools/playbook/adopt-playbook.sh` — printed 2, both plants exited 0 with their line, and the join named each cut row (DERIVED 2026-11-25).
- AC12 — `python tools/gate-lint/sh_hygiene.py --shell-role --measure . ':!memory/'` — read 3801 for the suite, 445 for `adopt-playbook.sh` and 819 for `gov-claim.sh`, as their rows hold; the first two widened by `2026-11-25-build-TOOL-dTotalRecall-121-widen-32` and set to the measure by hand, the third unmoved (DERIVED 2026-11-25).
- AC13 — `grep -c 'newest one' tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md` — printed 0 for each; the `--feed` entry names `duplicate` twice and `walk git refuses` once, section 7 names `duplicate`, and each guide is its template's bytes (DERIVED 2026-11-25).
- AC14 — `python tools/memory-tree/record_causes.py --cause-writers` — printed `0 red`, the literal's grep printed 0, and `door-header` printed its replay as `exists` inside its PASS (DERIVED 2026-11-25).
- AC15 — `grep -c 'two builds holding a' tools/memory-tree/README.md` — printed 0, and the other 3 greps printed at least one line each (DERIVED 2026-11-25).
