**Serves:** journal TOOL-dTotalRecall-57
**Caused-by:** TOOL-dTotalRecall-57

# TOOL-dTotalRecall-57 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `c736ff00f` from [2026-11-23-prompt-TOOL-dTotalRecall-57-build-brief](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-57-build-brief.md), recorded whole; the pass tip is `5ff76c2e2`.

## Why

I built TOOL-dTotalRecall-57 from spec rev-6 and checked its claims against the code. Both retired constants are gone. CENSUS_KEPT_PATHS holds nine rows, all under build folders. read_kept_rows was the table's one reader. check_cause_writers and run_check already took kept. check_alias_compares had a local counter named kept and no kept argument. Nothing in the spec failed to hold, so there was no divergence. One gap: the spec's section 7 New arm line names tools/memory-tree/check-memory-hygiene.test.sh, but Files touched leaves it out. I declared it with its own --dispatch, which was admitted, and recorded that in a Decided trailer.

## Summary

Commit 5ff76c2e2 on branch/unattended-dtotalrecall-ae256e builds TOOL-dTotalRecall-57 and sets its spec header to CLOSED, dated 2026-11-23. The commit ends with `Pass: TOOL-dTotalRecall-57` and `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. The harness asked for "Opus 5.5", but the commit-msg hook's check 49 refused that against the charter's trailer, so I recommitted with the charter's line.

What changed:
- C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/memory-tree/tree_lib.py: imports fnmatch and adds `KEPT_PATH_DOMAIN = "memory/builds/*/build/*"`. read_kept_rows now raises ValueError for any row in the whole table outside that domain. The message names the row and the fix: mark the kept line `# census: kept <census> <reason>`.
- C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/memory-tree/record_causes.py: check_cause_writers checks the table once before its build-folder walk. If the check fails, it adds a red and walks on with an empty table, so --check exits 1, not 2. The fixture gains the plant `kept-row-editable`: one check_cause_writers row naming `<tool_rel>/planted/editable.py`, passed to run_check as kept. The module and function docstrings are updated.
- C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/memory-tree/record_kinds.py: check_alias_compares takes `kept=None`, which it reads as tree_lib.CENSUS_KEPT_PATHS. I used None because this module imports tree_lib only inside its functions; this is recorded in a Decided trailer. Its local counter is renamed n_kept. It checks the table once before its build-folder walk, catches the refusal as a red, and passes kept to read_kept_path. Docstrings are updated.
- C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/memory-tree/check-memory-hygiene.test.sh: a new arm runs the kept-row-editable plant. It expects exit 1, the line `RED cause-writer CENSUS_KEPT_PATHS row `, and exactly one RED line naming /editable.py and `census: kept`.
- The acceptance ledger is at C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/memory/builds/dTotalRecall/build/2026-11-23-build-TOOL-dTotalRecall-57-1-acceptance-ledger.md.
- Also committed: RUN.md with its dispatch and brief rows, and what gen_build_index.py --write rewrote (memory/LIVE.md, memory/backlog/TOOL.md, the build README, and the records region of this spec). gen_map.py --write changed no tracked file. No new function was named, so the naming lexicon was not needed.

What ran (probes only; no gate, suite or bar):
- AC1: `python record_causes.py --fixture --plant kept-row-editable` exited 1 with exactly one RED line naming tools/planted/editable.py and `census: kept`. This stands in for the arm in the memory-hygiene self-test.
- Staged break for that arm: rebinding tree_lib.KEPT_PATH_DOMAIN to '*' in a python -c probe of run_fixture made the plant exit 0 and print `record causes: green`.
- AC2: `git grep -nE "ALIAS_COMPARE_KEPT|CAUSE_WRITER_KEPT" -- tools` printed nothing, and the spelled fnmatch probe printed [] and exited 0.
- AC3: the spelled python -c probe printed 1. These stand in for the record-kinds and record-causes legs.
- With the default table, both censuses report 0 red. The alias census reads 54 scripts with 1 kept. The cause census reads 104 code files with 8 kept and 1 pinned.

Still owed at the close, which the main loop runs:
- The legs on the spec's gates section: memory hygiene, memory-hygiene self-test, record-kinds, record causes (causes and orphans over the legacy population), lexicon naming predicates, recall floor and recall floor arms.
- The New arm's RED-first observation in check-memory-hygiene.test.sh, covering AC1 with the plant kept-row-editable, staged by skipping the domain match.

Bug-class checklist: `gotchas.py --for-diff HEAD~1..HEAD` exited 0 and selected 39 classes. I went through them: the fixture does trigger the rule, the staged break skips the match rather than swapping in a fake value, the refusal becomes a red instead of being swallowed, an empty table fails AC2's probe, and the docs next to the changed fields are updated. None needed a further change.

Nothing was skipped. The --dispatch for the suite path ran past its 120 s bound (PINNED, the Bash tool's default timeout) and moved to the background on its own. I waited for its completion notice; it exited 0 and was admitted before I staged the suite.
