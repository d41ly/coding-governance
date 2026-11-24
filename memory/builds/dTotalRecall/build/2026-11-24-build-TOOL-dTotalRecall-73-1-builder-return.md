**Serves:** journal TOOL-dTotalRecall-73
**Caused-by:** TOOL-dTotalRecall-73

# TOOL-dTotalRecall-73 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `aec378661` from [2026-11-24-prompt-TOOL-dTotalRecall-73-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-73-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `6d0627dd6`.

## Why

TOOL-dTotalRecall-73 is built as spec rev-3 states. Its claims about current code held at base aec378661, units 66 and 70 included. AC1 to AC4 were observed by probe; AC4 holds with line numbers masked (see summary). The spec is CLOSED in this commit. (DERIVED 2026-11-24, the pass)

## Summary

Built:
- `tree_lib.py#resolve_kept_home` is the keep registry's one path. `read_kept_rows` opens it, and its row domain is that home's second parent.
- `record_causes.py#check_kept_home` is wired at the end of `check_cause_writers`. It prints the `read at` and `registered at` (or `registered nowhere`) lines, reds a registration that names another file, and refuses registrations that do not read.
- The plant `kept-home-rooted`, its arm in `check-memory-hygiene.test.sh`, and the re-rendered symbols.json.
- The acceptance ledger and the spec's CLOSED header.

Observed (DERIVED 2026-11-24, node a). These probes stand in for the `record causes` leg and the hygiene suite's arm:
- AC1: the probe printed `memory/project/census-kept-paths.txt` twice.
- AC2: the plant exited 1 with one red naming both homes, each line naming its own. With the reds dropped in a probe process it exited 0. (DERIVED 2026-11-24, the pass)
- AC3: `False True` and `None` at the base; `True False` and `probe row` at the tip.
- AC4: `--cause-writers` exited 0 with the two lines added and no red. `adopter-no-registry` printed PASS and `registered nowhere`. (DERIVED 2026-11-24, the pass)
- A planted ValueError re-raised with `read_legacy_paths`' text. §4's table read as stated for the blank, slash-only, trailing-slash, leading-slash and doubled-segment values and for a `.` segment. The backslash and `..` values were not probed.
- Eight sibling plants (kept-row-docs-root, -traversal, -arity, -duplicate, departures-pinned, unmarked-writer, reason-on-other-file, legacy) gave their expected exits and reds.
- `lexicon.py --suggest` answered OK for both names, and `--measure` left VERB_OFFENDER_PIN at 1435.
- `bash -n` parsed the suite. The pre-commit hook was green.

Owed to the close: §7's legs, and the RED-first observation of the new `kept-home-rooted` arm in tools/memory-tree/check-memory-hygiene.test.sh, staged by skipping the comparison in `check_kept_home`. No gate, suite or `--selftest` ran here.

To note:
- AC4's "every other line as at the pass base" holds only with line numbers masked, because this unit's own edits move the kept literals below them. The other 126 lines (DERIVED 2026-11-24) then match, and the ledger says so.
- §4's "the one join of a memory root to the registry's filename" is true of the engine path. Two other joins stand and are untouched: the remedy text in `id_grammar.py#check_marker_domain`, derived from the walked path, and the fixture writer `record_kinds.py#write_kept_fixture`. Unit 76's spec names both functions; for the first it says it is handed no root.
- The bug-class checklist over HEAD~1..HEAD selected 41 classes (DERIVED 2026-11-24) and led to no further change.
- The index generator now renders the build's status as DEFERRED in LIVE.md, the build README and backlog/TOOL.md, because no unit is INPROGRESS until the next one is flipped.
- No timeout was hit and no command was skipped. The specs of units 78 and 79 and the untracked reground prompts in the tree are the spec writer's, and I left them alone. (DERIVED 2026-11-24, the pass)
