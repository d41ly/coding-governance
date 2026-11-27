**Serves:** journal TOOL-dTotalRecall-65
**Caused-by:** TOOL-dTotalRecall-65

# TOOL-dTotalRecall-65 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `cb72756eb` from [2026-11-24-prompt-TOOL-dTotalRecall-65-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-65-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `f1e11ac49`.

## Why

Spec rev-5 is built as written, with two recorded departures (deviation 1012). (1) The kickoff manifest's `last-audit` is re-stamped in this commit, because the pre-commit hook refuses a staged `.memory-tree.conf` without it and the brief asks for it. (2) The plants `reason-on-other-file` (unit 60) and `marker-in-kept-script` (unit 58), both added after rev-5, now write a row into their fixture's own registry.

## Summary

The nine keep rows moved one for one from `CENSUS_KEPT_PATHS` into `memory/project/census-kept-paths.txt`, named in `PROJECT_REGISTRY_EXTRA`. `tree_lib.py#read_kept_rows(census, root)` and `read_kept_path(census, path, root)` read it under the conf's memory root. The `kept` arguments and the engine table are gone. The plant `adopter-no-registry` and its suite arm are new. Spec CLOSED; ledger and deviation 1012 committed. (DERIVED 2026-11-24, the pass)

OBSERVED by probe, DERIVED 2026-11-24:
- AC1: both greps print nothing, and the conf grep prints 1. Stands in for nothing further.
- AC2: the build-folder lines of `record_causes.py --cause-writers` equal the base's byte for byte (8 kept, 1 pinned, 0 red, exit 0). `record_kinds.py --check` prints the base's lines byte for byte; its only reds are the host's stray common-dir entries (history-verdicts, recovery-manifests, theirs.tmp). The registry holds 9 rows. Stands in for `record causes` and `record-kinds`. (DERIVED 2026-11-24, the pass)
- AC3: `adopter-no-registry` prints PASS, exit 0. With an engine-held row injected in the probe process it exits 1.
- AC4: `kept-row-drained` and `kept-row-editable` each exit 1 with one RED naming the registry and the path. With the registry unread, or the domain widened, each exits 0. These plants stand in for the `memory-hygiene self-test` arms. (DERIVED 2026-11-24, the pass)
- AC5: ValueError naming `census-kept-paths.txt` and `line 2`.
- Also run: `reason-on-other-file` exits 1 with two reds. `marker-in-kept-script` prints PASS. A CRLF registry, a reason holding a TAB and a non-default MEMORY_ROOT all read correctly. `bash -n` on the suite file is clean. (DERIVED 2026-11-24, the pass)
- The pre-commit hook passed at the commit, including the map freshness and kickoff-manifest checks. `gen_map.py --write` changed nothing under memory/map.

OWED TO THE CLOSE: every leg of section 7, and the RED-first observation of its `New arm:` lines in `tools/memory-tree/check-memory-hygiene.test.sh`: `adopter-no-registry`, and the moved arms of `kept-row-drained` and `kept-row-editable`. Also owed there: the re-pointed `reason-on-other-file` hit, and `marker-in-kept-script` in `record_kinds.py`'s selftest. (DERIVED 2026-11-24, the pass)

OTHER POINTS:
- The commit also carries the regenerated dClosedLoop as-built view (2365 deviation records), declared by `--dispatch`. The first `--dispatch`, for deviation 1012, ran past its 300 s bound, went to the background and exited 0. (DERIVED 2026-11-24, the pass)
- The committed build README carries only this unit's rows. The working README still holds the full render, with the uncommitted rows of units 66, 68 and 69, whose specs and prompts I left unstaged. (DERIVED 2026-11-24, the pass)
- With unit 65 CLOSED the index derives the build as DEFERRED in LIVE.md and the backlog until another unit is INPROGRESS.
- TOOL-dTotalRecall-69 will find the stamp already in place, the first outcome of its uncommitted rev-3.
- `gotchas.py --for-diff HEAD~1..HEAD` ran over the commit; no class it listed needed a change. One last post-commit re-run of five plants was refused by the worktree guard and skipped. The last code edit after the plant runs was a docstring re-wrap in `record_causes.py`, after which `adopter-no-registry` ran PASS.
