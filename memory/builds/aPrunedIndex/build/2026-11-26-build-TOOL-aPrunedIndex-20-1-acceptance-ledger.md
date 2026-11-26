# TOOL-aPrunedIndex-20 — acceptance ledger

**Serves:** journal TOOL-aPrunedIndex-20

No merge bar, no self-test suite and no gate leg ran in this pass. Every reading is node a's, 2026-11-26,
from base `5b44ad17b` at spec rev-2, by one probe script under the run's scratch that puts
`tools/playbook` on `sys.path`, imports `tag_bundle` and replaces `subprocess.run` with a fake, and by
`python -c` calls of `tag_bundle.run_plant_process`. The parent module is `git show 5b44ad17b:tools/playbook/tag_bundle.py`
written to the scratch and loaded with `importlib.util`.

**Evidences:** TOOL-aPrunedIndex-20
- AC1 — the fake sleeping `0.05 * (13 - i)` s for the plant at index `i` and counting fakes running at once printed `calls=13 distinct=13 peak=4`, `distinct` derived from `tag_bundle.SELFTEST_ROWS`.
- AC2 — under one fake returning each row's wanted exit and line, the built and parent modules' `run_selftest` captures were equal and both returned 0; under a fake returning exit 1 and the lines `first line` and `second line` for `named-probe`, the captures were equal, both returned 1, and both held `arm FAIL  tag plant named-probe — wanted rc=0 + within a tenth under every pad, got rc=1` with the two lines indented under it, then `FAIL — 1 of 14 tag plant rows failed`.
- AC3 — under a fake raising `OSError("probe")` for `released-rows` only, `run_selftest` returned 1 and printed `arm FAIL  tag plant released-rows — wanted rc=0 + only replaced edits left, and nothing lost, got rc=None`, then `      OSError: probe`, then `FAIL — 1 of 14 tag plant rows failed`; the other 13 rows printed `arm ok`. A `python -c` call of `run_plant_process("dead-versions")` with the real `subprocess.run` returned exit 0 and the plant's `reads cost their own version's rows` line; with `subprocess.run` raising `OSError("x")` it returned `None`, `''` and `'OSError: x'`.
- AC4 — `git grep -c "max_workers" -- tools/playbook/tag_bundle.py` printed `tools/playbook/tag_bundle.py:1`; the AC2 probe printed `rows same: True`. The build commit's `git diff --name-only` is owed a read at the close against the cut-line list.
- AC5 — owed at the close: the main loop's six timed `python tools/playbook/tag_bundle.py --selftest` readings with their gauges, three with this unit's build commit reverted and three at the tip, and on green the row writes by unit 17's AC8.
