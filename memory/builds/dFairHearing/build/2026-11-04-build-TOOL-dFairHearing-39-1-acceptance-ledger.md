# Acceptance ledger — TOOL-dFairHearing-39

**Serves:** journal TOOL-dFairHearing-39

Built against spec rev-3 at the pass's parent `2e4e82b2f`. Each criterion was run from the repository
root on the working tree that this unit's commit carries, after `gotchas.py --write` regenerated the
index. Before the edit, the four record greps and the index grep each printed 0. No suite, gate or
bar ran in the pass. The spec's Gates section declares no new arm, and its legs are owed to the close.

**Evidences:** TOOL-dFairHearing-39
- AC1 — `gotchas.py --for-paths` over unit 37's spec — it listed `criterion-asserts-what-its-own-command-cannot-show (directory)` before the edit and after it. The record's harvested anchors are still `memory/builds/`, `tools/check-spec-tokens.py` and `tools/check-testsuite-counts.sh`
- AC2 — the four greps over the record — `unrecognized arguments` printed 2, `TOOL-dFairHearing-37` 1, `the line of that tool that emits it` 1 and `Eight ways` 1. `gotchas.py --for-paths tools/memory-tree/gotchas.py` printed no line naming the class, so the prose naming of the bug-class tool derives no anchor on it
- AC3 — `gotchas.py --check` — it exited 0, and its one line was the existing unselected-anchor advisory. `grep -c "an error text its tool never emits" memory/gotchas/INDEX.md` printed 1. The class's row shows 3 anchors, the same as the parent's row read with `git show` at `2e4e82b2f`
