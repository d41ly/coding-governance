# TOOL-aSightedSkeptic-10 — acceptance ledger

**Serves:** journal TOOL-aSightedSkeptic-10

Five `observed-by:` arms in the tier2-review self-test now read the surfaces the closing review's H1
and H2 named: the synthesis-death and deferred CONFIRMED log lines, the PARTIAL note, RUN
INTEGRITY's unverified clause, the uncertain `WARNING:` line and the all-uncertain note. The class
is filed as a gotcha. The arm readings come from the main loop's VERIFYING run of the self-test at
fe3c29fc (180 passed, 0 failed) and from the same test file against the BASE render at 9fdd0c18 (56
passed, 124 failed). The pass's own commit, f1f8eda6, records each arm red under its spec §4 staged
break of the harness and green once re-rendered. The greps and the direct checks were run at
fe3c29fc, whose `tools/` matches f1f8eda6's.

**Evidences:** TOOL-aSightedSkeptic-10
- AC1 — `observed-by: a dead synthesis logs every CONFIRMED finding at its binding grade` — `ok` at
  fe3c29fc, `FAIL` against the BASE render, and red under the staged break that logs `f.severity`
  per f1f8eda6's message.
- AC2 — `observed-by: a dead synthesis logs every CONFIRMED finding's fix through renderFixLine` —
  `ok` at fe3c29fc, `FAIL` against the BASE render, and red under the staged break that logs
  `f.fix` per f1f8eda6's message.
- AC3 — `observed-by: a dead skeptic batch logs every CONFIRMED finding at its binding grade` — `ok`
  at fe3c29fc, `FAIL` against the BASE render, and red under the staged break on the deferred-path
  log line per f1f8eda6's message.
- AC4 — `observed-by: one uncertain answer is counted apart from no verdict in the note, RUN INTEGRITY and the log`
  — `ok` at fe3c29fc, `FAIL` against the BASE render, and red under the staged break that
  interpolates `unverified.length` per f1f8eda6's message.
- AC5 — `observed-by: an all-uncertain round never reads as none judged` — `ok` at fe3c29fc, `FAIL`
  against the BASE render, and red under the staged break that deletes the uncertain term per
  f1f8eda6's message.
- AC6 — `grep -c "'observed-by: " tools/workflows/tier2-review.test.sh` — over `git show f1f8eda6:`
  of the test it printed 5, and over its parent 6c84b91f 0. The `FLOOR_ASSERTIONS=` grep read 180
  at f1f8eda6 and 175 at 6c84b91f, five above.
- AC7 — `observed-by-claim-no-arm-discharges` — `--for-paths` over the test file and over spec 6
  each listed the record, and `python tools/memory-tree/gotchas.py --report` listed it as `class`
  with `3 anchor(s)`.
- AC8 — `declares: yes` — `python tools/memory-tree/gotchas.py --check` exited 0, and `--declares`
  fed the new record on stdin, the form its usage line names, printed `declares: yes` and exited 0.
- AC9 — `git diff --stat HEAD~1 HEAD -- tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js`
  — run as `git diff --stat f1f8eda6~1 f1f8eda6` over the same two paths, it printed nothing.
