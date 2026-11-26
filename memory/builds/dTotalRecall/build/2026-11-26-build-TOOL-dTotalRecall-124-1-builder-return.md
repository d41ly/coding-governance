**Serves:** journal TOOL-dTotalRecall-124
**Caused-by:** TOOL-dTotalRecall-124

# TOOL-dTotalRecall-124 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `6fa6785f8` from [2026-11-26-prompt-TOOL-dTotalRecall-124-build-brief](../prompts/2026-11-26-prompt-TOOL-dTotalRecall-124-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `2d94dd3b9`.

## Why

TOOL-dTotalRecall-124 is built from spec rev-1 as written, in one pass commit carrying `Pass: TOOL-dTotalRecall-124`. That commit also sets the spec header to CLOSED and carries RUN.md, the acceptance ledger and every file the generators rewrote. No spec claim I probed failed. The two choices I made where the spec's text was silent are recorded as `Decided:` trailers.

## Summary

Built TOOL-dTotalRecall-124 in commit 2d94dd3b9, on top of base 6fa6785f8. No gate, suite or `--selftest` ran in this pass.

**What changed**
- S1: in `tools/playbook/code_record.py#read_ctags_defs`, each line written to ctags's `-L` input is now `./` and the path, and the docstring says why.
- S2: `tools/memory-tree/tree_lib.py#read_blobs_at` no longer writes a request holding a line feed or carriage return to `cat-file --batch`. It reads each such request through its own `git cat-file blob` call, and a failure there answers None. The docstring states the route and its cost, and a batch made only of such requests starts no batch process.
- S3: the arm `ctags list input` sits after `ctags pack`. The stub now writes the stdin it read to `bin/lines`. The arm commits `-fZ.go` and `z9/kit.toml`, adds `n\nl.go` and `j\nk/kit.toml` with `core.protectNTFS=false`, and makes the spec's three assertions.
- S4: the class `memory/gotchas/path-list-input-read-as-options.md` is written. It answers its near match `read-allowlist-admits-a-writing-option` with `coexists-with`. The playbook feature card's `gotcha-classes` lists it, and `memory/gotchas/INDEX.md`, the map files, the build README, `memory/LIVE.md` and the spec's records region were regenerated.

**Two choices the spec's text did not settle** (each is a `Decided:` trailer):
1. The batch reader decodes every body in one closing loop instead of through the spec's nested `decode` helper. `lexicon.py --suggest decode` says to use `parse` instead (DERIVED 2026-11-26), and the spec's Inventory says the unit mints no graded name.
2. The arm treats a derivation that raises `OSError` as producing no skip row. With the printable test cut, Windows cannot copy a path containing a line break (`OSError 22`, DERIVED 2026-11-26). Without the catch the suite would crash instead of printing the `FAIL` row AC1 asks for.

**Checks that ran, and the gate each stands in for**
- A probe at `C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/probe124.py` replays the arm's fixture and its three assertions outside the suite. It stands in for the `code record` and `playbook render selftest` legs (DERIVED 2026-11-26):
  - On the built kit: ok. The stub read `./-fZ.go` alone, `n\nl.go` was skipped as `a path no cell holds`, and the three requests answered `jk`'s text, `z9`'s text and None.
  - On the base `tools/` tree: FAIL. The stub read `-fZ.go`, and the answers were None, None and `z9`'s text, which matches the spec's "today".
  - With the `./` cut: FAIL, showing `-fZ.go`.
  - With the printable test cut: FAIL. The derivation raised `OSError 22`.
  - With the batch route cut: FAIL. The answers were None, None and `z9`'s text.
- For AC3, which stands in for the `memory hygiene`, `gotchas selftest` and codebase-map legs:
  - `gotchas.py --check` named no finding of the class. Its advisory count was back at 55 once I removed a backticked `./` anchor that selected no path (DERIVED 2026-11-26).
  - The `grep -c` over the playbook card printed 1, and `gen_map.py --check` exited 0. (DERIVED 2026-11-26, the pass)
  - After the commit, `row_grammar.py --check-relations 33706662` printed `1 near match(es), 1 satisfied` and no `check 27:` line (DERIVED 2026-11-26).
- `gotchas.py --for-diff HEAD~1..HEAD` printed 26 anchored and 6 universal classes (DERIVED 2026-11-26), and I worked through them. Each red was seen on a fresh `git archive` copy, so no stale bytecode; each break is a real cut, not a synthetic value; each ledger token sits on one line; the crash-instead-of-FAIL case is handled by choice 2.
- The commit's pre-commit hook passed, with only a warning: `readme-entry-chars` on the build README is 379 chars against a budget of 350 (DERIVED 2026-11-26).

**Owed to the close (the main loop)**
- `python tools/playbook/code_record.py --selftest` printing the `ok` row for `code-record ctags list input` and `PASS — the code record's arms` (AC1).
- The `New arm:` RED-first observation of `ctags list input`: red on the base code, then red again on the `./` cut, the printable cut and the batch route cut, then green restored.
- All of section 7's legs, and the bar.
- `KIT_MEMORY_TREE_VERSION`, which is owed for the `tree_lib.py` change and is minted by the lander.

**Left over**
- The `--dispatch` call that declared `memory/gotchas/INDEX.md` and `memory/LIVE.md` hit its 120 s limit and was moved to the background. It had not exited when I returned, and I had no tool to stop it. Its own output said both paths are generated outputs a pass may rewrite without declaring them, so they did not need it. If it still appends a row to `memory/builds/dTotalRecall/RUN.md`, that row is uncommitted and goes with the next pass's commit. (DERIVED 2026-11-26, the pass)
- I wrote no deviation record. The two choices above are trailers only.
