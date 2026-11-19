# TOOL-dSweptScratch-1 — every selftest and fixture removes the scratch it made, read-only git objects included

**Status:** OPEN · rev-1 · 2026-11-19 · node d · Tier-1 · base 389c0c86 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Selftests and planted fixtures stop leaving their scratch in the system temp dir on Windows. Node `d`
held ~1M leftover dirs there on 2026-11-19, and a measured share came from this repo's suites run
directly (the bar's trapped `TMPDIR` hides it).

## 2. Scope (IN)

- **S1** — Every scratch tree that holds a git repository is removed with a chmod-and-retry hook
  instead of `shutil.rmtree(..., ignore_errors=True)`, reusing `deviation_join.remove_tree`,
  `step_gate.remove_scratch_tree` or `loop_witness.remove_tree` where the call site already reaches
  that kit, else a local hook of memory-recall's `_set_writable` shape. Observed by AC1.
  **Readers:** by name: none, since the replaced call is a private cleanup line in each suite and no
  other file spells it there · by value: NO VALUE READERS, a removal returns nothing any caller reads.
- **S2** — Every scratch dir a suite made and never removed is either removed or made under a parent
  the suite already removes: `mkdtemp(dir=<the enclosing TemporaryDirectory>)`, a dir under the
  trapped `$TMP` or `$wt`, a parent kept in a variable, a trap that no longer replaces another.
  Observed by AC1.
- **S3** — The cleanup never fails a run: removal errors are caught, as they were under
  `ignore_errors`. Observed by AC2.

## 3. Non-goals (OUT)

- Leaks from a run killed from outside (a wall breach, a terminated tree): no in-suite code runs then.
- The vendored copies in adopters: they take this through `govkit` re-adoption, not a hand edit.
- Any change to what a suite asserts.

### Edges

none

## 4. Design

Git writes `.git/objects` read-only, and on Windows `os.unlink` of a read-only file raises, which
`ignore_errors=True` swallows, so the tree survives and the caller believes it was removed: the
mechanism TOOL-aBranchedMandate-6 measured and fixed in the memory-recall selftest alone. The hook
clears the bit and retries (`onexc` on 3.12+, `onerror` below), the whole removal wrapped so it can
never raise. The remaining sites are plain bookkeeping: a dir with no removal, a `$(…)` subshell that
lost its `SCRATCH+=`, a reassigned variable, an EXIT trap replaced by a later one.

### Files touched (estimate)

- `.githooks/pre-push.test.sh`
- `.githooks/pre_push_bar_selftest.py`
- `tools/branch-reconcile/selftest.py`
- `tools/govkit/fixtures/retired_edits.py`
- `tools/govkit/fixtures/stale_edges.py`
- `tools/govkit/selftest.py`
- `tools/govkit/shims.py`
- `tools/lexicon/selftest.py`
- `tools/loop/review_bounds.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/merge-rows.test.sh`
- `tools/memory-tree/migrate_backlog.py`
- `tools/memory-tree/routed_commits.py`
- `tools/playbook/core.py`
- `tools/playbook/fixtures/composition.py`
- `tools/playbook/fixtures/row_kind.py`
- `tools/playbook/instruction_units.py`
- `tools/playbook/overlay.py`
- `tools/playbook/pins.py`
- `tools/process-monitor/selftest.py`
- `tools/run-gates/check-receipt.py`
- `tools/run-gates/run-selftests.sh`
- `tools/runlog/selftest.py`
- `tools/unattended/unattended.test.sh`
- `tools/workflows/check-verifier-fanout.test.sh`
- `memory/map/generated/symbols.json`
- `memory/guides/SESSION-KICKOFF.md`

## 5. Acceptance criteria

- **AC1** — When each touched suite runs with `TMPDIR`, `TEMP` and `TMP` pointed at a fresh empty
  dir, the dir is empty after it exits. Red when: the unchanged suite runs the same way, which left
  91 (runlog), 25 (branch-reconcile), 232 (lexicon), 60 (run-selftests), 43 (instruction units), 26
  (overlay), 14 (review bounds), 12 (pins), 12 (core), 8 (build index), 5 (merge-rows), 2 (pre-push
  bar), 2 (pre-push), 2 (process-monitor), 1 (check-receipt), 1 (migrate-backlog), 1 (routed
  commits), 1 (verifier fan-out), measured on node `d`.
- **AC2** — When `python tools/runlog/selftest.py` and each other touched suite runs, its verdict is
  the one the unchanged suite gives. Red when: a removal error reaches a suite
  that passed, or a new import fails where a fixture is planted alone.

## 6. Gates

`routed commits name a specced unit` · `runlog selftest` · `branch-reconcile selftest` · `lexicon selftest` · `pre-push bar self-test` · `pre-push self-test` · `run-selftests self-test` · `verifier fan-out self-test` · `instruction units selftest` · `build-index selftest` · `govkit selftest` · `codebase-map kit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `playbook render selftest` · `policy fixtures` · `pre-push run-log line` · `process-monitor census selftest` · `recall floor` · `recall floor arms` · `review-join self-test` · `run-gates run-log line` · `tier2-review self-test` · `unattended-build self-test`

The long suites (`govkit selftest`, `tools/unattended/unattended.test.sh`) were read and `bash -n`
checked rather than run in full; the full bar runs at the push boundary.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-19 · initial draft.
