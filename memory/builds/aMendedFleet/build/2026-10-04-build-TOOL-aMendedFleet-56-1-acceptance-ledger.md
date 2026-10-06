# TOOL-aMendedFleet-56 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-56

**Evidences:** TOOL-aMendedFleet-56
- AC1 — `python tools/drift-audit/drift_report.py --json` — on the unit's working tree: signal 2 carried `baseline` 2, `stale` [] and `new` holding only the two ids earlier units of this build brought in (a forward citation of unit 65 in `tools/push-main.sh`, and the spec high-water registry), at value 4; signal 6 carried `baseline` 1, value 1, `new` and `stale` empty; `--offenders` printed those two `new` rows and no line naming a listed id. Criterion as amended rev-3; the old pin reads 4 against 2 on the same tree, so the bar's `drift-audit records` red predates this unit
- AC2 — `python tools/drift-audit/drift_report.py --check` — with `TOOL-aBatchedLintel-1` respelled out of `tools/memory-tree/check-memory-hygiene.sh` and a comment naming a SPECCED sibling appended to `drift_report.py`: value stayed 4, exit 1, stderr listed the sibling as `new` and `TOOL-aBatchedLintel-1` as `stale`, and `--offenders` carried a row for the sibling and `{"stale": "TOOL-aBatchedLintel-1"}`; both edits reverted
- AC3 — `python tools/drift-audit/drift_report.py --check` — with only that deletion: exit 1 and stderr `stale TOOL-aBatchedLintel-1`, the layer still spelling the id. RED first: with S10's exclusion stubbed out the same tree reported no stale id and `cited_in` named `tools/drift-audit/drift_signals.py`. With the id also deleted from `BASELINES`, `--offenders` printed no line naming it. Restored
- AC4 — `python tools/drift-audit/drift_report.py --check` — with a third id appended to signal 2's list: exit 1 and `RATCHET WEAKENED — tools/drift-audit/drift_signals.py: BASELINES['non_terminal_specs_cited_by_product_source'] is seeded with 3 ids where the base pins it at 2 in PINS`; `--offenders` printed the matching `ratchet` line. The base does not list the signal yet, so the seed rule fired; the gained-id rule is the arm's. Restored
- AC5 — `python tools/drift-audit/drift_report.py` — with signal 6 restored to `PINS`: exit 2, stdout empty, one stderr line naming it and both declarations; with `source_cited_ids_resolving_to_no_record` added to `BASELINES`: exit 2, stdout empty, refused as declared in both, since it keeps its pin. The second refusal, a key naming no gateable signal, was observed with `live_builds_without_activity` under `--check`: exit 2, stdout empty, so no history row was appended
- AC6 — `grep -c "BASELINES" tools/drift-audit/README.md tools/drift-audit/drift_signals.template.py` — printed 5 and 2, from 0 and 0 before the edit, and the old pin's grep in `tools/drift-audit/drift_signals.py` printed 0

## The arm

`test_baselines` in `tools/drift-audit/selftest.py`, eight checks over a `make_repo` fixture with
the layer inside its evidence globs: the seeded fixture green with the fields, an equal-count swap
red with its keys, a drain red as stale while the layer spells the id, a set gaining an id against
its committed base red, a first seed above the base pin red and one at it green, and a signal in both
declarations refused with exit 2. Run ALONE through a scratchpad slice calling it, fixture under
`%TEMP%/dab56`: eight `ok`. `CHECK_FLOOR` 357 -> 365. The suite did not run.

## Owed at the close

- `drift-audit selftest`, `drift-audit records`, `drift-audit wiring`, `codebase-map coverage +
  freshness`, `recall floor`, `recall floor arms`, `lexicon naming predicates` and `spec tokens`.
- `drift-audit records` stays red on this branch until the two `new` ids above drain: unit 65's
  close removes the first, and the second needs the high-water registry's spec path kept out of
  signal 2's evidence or that spec closed. Neither is this unit's write set.
- The drift-audit kit version bump, per the brief; `kit epoch` is the close's.
