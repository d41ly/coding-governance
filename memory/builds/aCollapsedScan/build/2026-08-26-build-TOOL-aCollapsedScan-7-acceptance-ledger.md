# Acceptance ledger — the aCollapsedScan follow-up units

**Serves:** journal TOOL-aCollapsedScan-4 TOOL-aCollapsedScan-6 TOOL-aCollapsedScan-7

Node `a` · branch `branch/acollapsedscan-followups` · base `3c37a1fb`. One line per numbered
criterion, each naming the observation that answered it rather than asserting the criterion was met.

**Evidences:** TOOL-aCollapsedScan-7

- AC1 — `tools/memory-recall/selftest.py` — MET, and observed BOTH ways. The linked-worktree arm
  failed against the pre-fix function with `repo_root() returned '.../mrecall-xpurzyne-wt/memory-recall';
  want the worktree root '.../mrecall-xpurzyne-wt'`, and passes after. The suite is 37/37 with 34
  scratch trees swept, up from 32 once the arm's own `try/finally` landed.
- AC2 — `grep -n "def repo_root" tools/memory-recall/*.py` — MET. One definition remains in the kit,
  at `recall_conf.py`. `query.py`'s bare-`rev-parse` second resolver is gone and its one caller uses
  the survivor.
- AC3 — `bash tools/memory-tree/merge-rows.test.sh` — MET, and the new arm observed RED first. With
  `recall_conf.py` restored to its pre-fix bytes the suite exits 1 on `FAIL worktree: git merge did
  not auto-resolve in a linked worktree`, carrying the `ConfError` text; with the fix it is
  `PASS — merge-rows: 49 groups / 40 run cases held`.
- AC4 — `tools/memory-tree/merge-rows.sh` — MET in THIS linked worktree, under git's own
  environment. A three-way input driven through the shipped wrapper with `GIT_DIR` inherited and
  `GIT_WORK_TREE` unset: `driver exit=0 · ConfError: 0 · markers: 0 · ids: 3`, both sides' rows kept.
  This is the same tree and the same wiring that produced two hand-reconciled conflicts earlier in
  the same session.
- AC5 — `python tools/memory-recall/selftest.py` and `python tools/memory-recall/check-recall.py` —
  MET. 37/37 and exit 0 respectively.
- AC6 — `bash tools/run-gates/run-gates.sh` — MET. Recorded in the landing report with its leg
  counts; the run preceding this ledger failed on `memory hygiene` for the absence of this very
  record, which is check 23 doing its job.

**Evidences:** TOOL-aCollapsedScan-4

- AC1 — `bash tools/unattended/run-unattended-gates.sh --checks` — MET. `ok kit gate 187s` against
  the re-declared 240 s ceiling, no `OVER BUDGET` line, exit 0 on an idle box.
- AC2 — `BUDGET_kit_gate` — MET. The comment beside it names node `a`, 2026-08-26 and the 187 s
  reading, in the idiom the seven sibling declarations use, and adds the 362 s under-load reading
  and the rule for reading a breach.
- AC3 — `--checks` — MET. With `BUDGET_skill_wiring` zeroed in a scratch copy the runner printed
  `OVER BUDGET skill wiring took 2s against a declared 0s ceiling` and exited 1, so the mechanism is
  observed armed AFTER the raise rather than assumed from the breaches that preceded it.
- AC4 — `bash tools/unattended/run-unattended-gates.sh --selftests` — NOT MET, and not run. The
  owner instructed mid-build that only the driver suite be run and the gate selftest be skipped, and
  the other three selftest suites went with it. This is the Definition of Done the edited file
  declares in its own header, so the gap is real and is stated here rather than implied away. The
  compensating evidence is narrower: the two suites whose subjects this build actually changed —
  `memory-recall/selftest.py` and `memory-tree/merge-rows.test.sh` — were both run to green, and the
  unattended kit's own three record/wiring checks pass under `--checks`.
- AC5 — `memory/builds/aCollapsedScan/README.md` — MET. The parked entry records the deferral
  resolving as a refusal on 2026-08-26 with the measurement, so no two documents disagree about it.
- AC6 — `bash tools/run-gates/run-gates.sh` — MET, as AC6 above.

**Evidences:** TOOL-aCollapsedScan-6

- AC1 — `python tools/memory-tree/row_grammar.py --check` — MET, both directions. Staged break:
  `check 20: 4 id(s) appear more than once within one row document (pin 3, shrink-only)` naming the
  file, the id and both line numbers. Reverted: `row-grammar: clean (412 row(s), 3 pinned
  duplicate(s))`.
- AC2 — `memory/backlog/TOOL.md` — MET. Row `TOOL-aCollapsedScan-6` reads `WONTDO` and names check
  20 as what already covers it.
- AC3 — `memory/DECISIONS.md` — MET. `TOOL-aCollapsedScan-10` records the correction and names the
  three retired claims.
- AC4 — `bash tools/run-gates/run-gates.sh` — MET, as AC6 above.
