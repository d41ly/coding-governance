**Serves:** journal TOOL-dTotalRecall-54

# TOOL-dTotalRecall-54 first build pass — the builder's return

The gov-builder return for the pass dispatched at `c3bee259d` from [2026-11-22-prompt-TOOL-dTotalRecall-54-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-54-build-brief.md), recorded whole; the pass tip is `79cc8830b`.

## Why

TOOL-dTotalRecall-54 is built as the spec says, with no divergence. Every claim in the spec held against the tree at base c3bee259d. `build_id_token_re(alt, root)` has the named groups fam, slug, seq and rev. There were 3 `sys.path.append` copies. Only `derive_slug_grammar` calls `read_slug_policy` and `read_recorded_grammars`. The lexicon answered OK for `parse_id_parts` and `load_sibling`. None of the new names existed before.

## Summary

TOOL-dTotalRecall-54 is built and committed as 74af3faa4, with a follow-up fix 79cc8830b. Both carry `Pass: TOOL-dTotalRecall-54` and `Co-Authored-By: Claude Opus 5`. The first commit also sets the spec status to CLOSED.

**What changed**
- `C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/memory-tree/id_grammar.py`:
  - New `SUFFIX_RE`, `load_sibling(name)` and `parse_id_parts(ident, root, *, alt=None)`.
  - The parser matches through `tree_lib.build_id_token_re(alt, root)`. By default `alt` is `grammar_for(root).families`.
  - `_parse_spec_h1`, `read_slug_policy` and `read_recorded_grammars` now call `load_sibling("tree_lib")` instead of carrying their own copies of the path guard. `importlib` was added to the imports.
- `C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/memory-recall/selftest.py`: one new arm, `test_id_parts_parse_under_each_tree_grammar`, which runs a probe (`_PARSER_PROBE`). `SELFTEST_ARMS` goes from 86 to 87, with its provenance line, and the arm is added to the order list.
- Regenerated or recorded: `memory/map/generated/symbols.json`, the acceptance ledger `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-54-1-acceptance-ledger.md`, `RUN.md`, and the build-index rewrites (LIVE.md, backlog/TOOL.md, the build README, the spec's records table). All of these paths are in the declared write set.
- Once no unit is INPROGRESS, the generator shows the build status as DEFERRED in LIVE.md and the build README.

**What was checked (stands in for the memory-recall kit selftest and the AC probes, run no gate)**
- `python -c` probes over the worktree:
  - AC1: `("TOOL", "dTotalRecall", 38)` for root `"."` and for `None`.
  - AC2: `TOOL-aDrainedSluice-9b` gives `("TOOL", "aDrainedSluice", 9)`.
  - AC3: `TOOL-001`, `TOOL-d119`, `ARCH-aFix-3`, `TOOL-x` and `TOOL-dTotalRecall-38@rev-2` each raise ValueError naming the id.
  - AC5: `tree_lib` is not loaded after import and is loaded after one call; `grep -c sys.path.append` gives 1.
  - AC6: `EXMP-aFoo-2` is refused, accepted with `alt="EXMP|OTHR"`, and passing `alt` positionally raises TypeError.
  - The parser's source has 0 `ID_RE` and 2 `build_id_token_re`.
- Over a scratch a-f tree that also declares the cited family ZED: `ZED-aFoo-2` parses and `TOOL-xFoo-3` is refused.
- The other functions that now use `load_sibling` still work: `derive_slug_grammar`, `extract_records`, and `read_recorded_grammars` over a scratch README.
- The new arm's probe text was taken out with `ast` and run alone over two scratch trees (a-f and default). It printed the expected JSON. The suite itself was never imported.
- Naming lexicon: `--suggest` gave OK for all four new names. `--measure` gives `VERB_OFFENDER_PIN` 1446, unchanged.
- The bug-class checklist (`gotchas.py --for-diff`) ran after each commit. On the first commit it flagged fixture-inherits-ambient-machine-state: the arm's liveness case read the source tree's own conf, so an adopter that declares a-f would fail a correct parser. Fixed in 79cc8830b, which uses a second throwaway tree at the default conf instead. The rerun after the fix selected nothing further to act on.

**Owed to the close (main loop)**
- The `New arm:` RED-first observation for `tools/memory-recall/selftest.py` (AC1, AC2, AC3, AC5, AC6): break the parser so it reads `ID_RE`'s groups again, see the arm fail, then see it pass with the fix restored.
- AC4 can only be observed at unit 38's pass tip: this commit must come before unit 38's, and `build_id_token_re` must still be in the parser body there.
- The legs on the spec's gates section: memory hygiene, lexicon naming predicates, build-index selftest, recall floor, recall floor arms, memory-recall kit selftest, policy fixtures, drift-audit selftest, playbook render selftest, and the four codebase-map legs.

Nothing was skipped for running past its time limit.
