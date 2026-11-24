**Serves:** journal TOOL-dTotalRecall-58
**Caused-by:** TOOL-dTotalRecall-58

# TOOL-dTotalRecall-58 build pass 2 — the builder's return

The gov-builder return for the pass dispatched at `12d219431` from [2026-11-24-prompt-TOOL-dTotalRecall-58-build-2-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-58-build-2-brief.md), recorded whole; the pass tip is `7fd3f8e38`.

## Why

Built to spec rev-4 with no divergence. `id_grammar.py#check_marker_domain` is called in the build-folder walks of `check_cause_writers` and `check_alias_compares`, before any skip or keep. AC1 to AC4 are observed by probe. The §7 legs and both New arms' RED-first observations are owed to the close.

## Summary

No gate, suite or bar ran, beyond the lexicon's `--suggest` (OK for `check_marker_domain`) and the pre-commit hook (green).

Observed per criterion:
- **AC1:** `record_causes.py --fixture --plant marker-in-build-script` printed PASS, exit 0: its check exits 1 with one red, at the pinned instrument's line 13. This stands in for the record-causes plant arm.
- **AC2, first half:** the spelled git log, re-read at the pass tip, lists no dTotalRecall subject.
- **AC2, second half:** observed through `python tools/chain-packet.py --check dTotalRecall`, as the brief directs: exit 0, byte compare green, pin arm 7 instruments and 0 findings. It ran over the worktree early in the pass, before the commit; the commit touches no build-folder code file. `packet.py --check` itself was not run.
- **AC3:** `record_kinds.py --fixture --plant marker-in-kept-script` printed PASS, exit 0: its check exits 1 with one red, at line 14 of the kept deviations path. This stands in for the record-kinds selftest arm.
- **AC4:** no build-folder code file carries the marker. The callers of `read_kept_reason` are the definition, the three S4 names and `check_marker_domain`.
- **Real tree:** both censuses print 0 reds (104 code files; 54 scripts).
- **Staged break:** in a scratch probe with `check_marker_domain` returning no finding, both plants print FAIL and exit 1.
- **Neighbouring plants, unchanged:** departures-pinned and pinned-writer-drained PASS; kept-row-drained ended RED and unkept-build-alias printed its one red, as each must; the green record-kinds fixture is green.

Owed to the close:
- §7's legs: memory hygiene, lexicon naming predicates, recall floor, recall floor arms.
- RED-first of New arm `marker-in-build-script` (`record_causes.py`).
- RED-first of New arm `marker-in-kept-script` (`record_kinds.py --selftest`, in `shows`, because AC3 has the fixture exit 0).

Coverage gap you may want to close: no suite runs `marker-in-build-script`. `check-memory-hygiene.test.sh` was in the dispatch, but neither the spec's Files touched nor §7 names it, so I left it alone, as the unit-53 census plants are left.

`gotchas.py --for-diff HEAD~1..HEAD` ran and nothing it names needed a further change. Every command finished within its bound.

Worktree left to the main loop:
- Specs 60 and 65 and their untracked prompts are another writer's and are unstaged.
- `58-1-builder-return.md` carries a 'DERIVED' edit I did not make; it is unstaged.
- The dTotalRecall README's unstaged diff is only the re-rendered rows for units 60 and 65; the commit carries my own rows only.

`--brief` answered already recorded, unchanged, and no extra `--dispatch` was needed. No deviation record was owed.

Files committed, under C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e:
- tools/memory-tree/id_grammar.py
- tools/memory-tree/record_causes.py
- tools/memory-tree/record_kinds.py
- memory/map/generated/symbols.json
- memory/LIVE.md
- memory/backlog/TOOL.md
- memory/builds/dTotalRecall/README.md
- memory/builds/dTotalRecall/RUN.md
- memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-58.md (header CLOSED; the index generator also added its spec-records row)
- memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-58-2-acceptance-ledger.md
