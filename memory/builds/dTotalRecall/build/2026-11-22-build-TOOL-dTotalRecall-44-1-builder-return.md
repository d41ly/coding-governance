**Serves:** journal TOOL-dTotalRecall-44

# TOOL-dTotalRecall-44 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `b71b6dd0b` from [2026-11-22-prompt-TOOL-dTotalRecall-44-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-44-build-brief.md), recorded whole; the pass tip is `376f76cd2`.

## Why

I built TOOL-dTotalRecall-44 as its spec (rev-4) says, with no divergence. Every claim I checked against the code held. The split census listed 31 lines at HEAD and 37 over a scratch worktree at 7047890d5, the same counts as spec section 4. `_SPLIT_NAME` had no reader outside id_grammar.py, and neither touched file is on the kickoff manifest's watch list. I committed it as one pass commit with the `Pass: TOOL-dTotalRecall-44` trailer and moved the spec header to CLOSED in that same commit.

## Summary

Commit 376f76cd2 (base b71b6dd0b) holds the unit.

**What changed**
- C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/memory-tree/id_grammar.py: `_READER_SPLIT_SHAPE` no longer uses `_SPLIT_NAME`, which is removed. It now lists any `.split("-")` call with no maxsplit (blanks allowed) unless it is indexed `[0]` right away. It also lists the shell shapes `cut -d-`, `cut -d '-'`, `cut -d "-"`, `IFS=-` and the four `${name%-*}`-style expansions, whatever the variable is called. `.rsplit("-"` is no longer listed. I rewrote the comment and the `scan_readers` docstring to match. I also dropped the old `re.I` flag, because the spec's pattern and its `git grep -P` counts are case-sensitive; the commit records this as a `Decided:` line.
- C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/memory-recall/selftest.py: the S3 plants are added to `_SPLIT_PLANTS`. Three must be listed (`i.split("-")[1]`, `spec_id.split('-')[1][0]`, `fam, slug, seq = x.split("-")`) and two must not (`x.split("-")[0]`, `x.rsplit("-", 1)[1]`). A new `_SPLIT_LISTED` set is now what `test_split_census_and_the_flip_probe_census_check` compares against for equality.
- The commit also carries the acceptance ledger memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-44-1-acceptance-ledger.md, RUN.md, the spec status flip with its regenerated records row, and the index rewrites from `gen_build_index.py --write` (LIVE.md, backlog/TOOL.md, and the build README with my rows only). The README row for unit 46 comes from the spec writer working in this tree, so I left it unstaged. `gen_map.py --write` changed nothing.

**Checks that ran** (each stands in for the `memory-recall kit selftest` leg, which runs the arm)
- **AC1:** I built a scratch git fixture the way `make_repo` does, with every memory-tree `*.py`, a conf file and the plants read from the suite by `ast` (the suite was never imported). Its own `id_grammar.py --readers` listed exactly the six expected plants and none of the control, `py-head` or `py-rsplit`. With unit 38's name-keyed predicate put back in the fixture's copy, the same probe failed: `py-unnamed` and `py-unpack` were missing.
- **AC2:** the tip's `--readers` over a scratch worktree at 7047890d5 listed all 14 lines: unit 38's ten readers, the three in unit 45's row, and `derive_run_kind`. The old predicate missed `derive_probe_labels`, `derive_names` and `derive_run_kind`.
- **AC3:** at the tip the census lists 34 split lines: the 31 found before the edit plus the 3 new plants. Four are unit 45's section 1 readers, and the commit's `Decided:` lines keep every other one with its reason.

**Owed to the close**
- The `New arm:` failing-first check for tools/memory-recall/selftest.py on AC1: restore `_SPLIT_NAME` in `_READER_SPLIT_SHAPE`, see it fail, then see it pass again.
- Section 7's legs: `memory hygiene`, `lexicon naming predicates`, `tier2-review self-test`, `recall floor`, `recall floor arms`, `build-index selftest`, `memory-recall kit selftest`, `drift-audit selftest`, `playbook render selftest`, `policy fixtures`.

**Not run:** no gate, suite, bar or `--selftest`. The only gate that ran was the pre-commit hook's own staged checks during `git commit`, which exited 0. No command timed out or was skipped.

**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` selected 41 classes and none needed action. The arm compares the listed set both ways and was seen failing on the real old predicate. Nothing outside the module read `_SPLIT_NAME`. The failing probe used freshly copied files, so no stale bytecode. Code edits went through the edit tools, not a heredoc.

The scratch worktree and fixtures are removed; the probe scripts remain in the scratchpad.
