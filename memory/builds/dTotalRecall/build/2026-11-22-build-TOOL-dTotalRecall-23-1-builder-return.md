**Serves:** journal TOOL-dTotalRecall-23
**Caused-by:** TOOL-dTotalRecall-23

# TOOL-dTotalRecall-23 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `7fa604e1d` from [2026-11-22-prompt-TOOL-dTotalRecall-23-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-23-build-brief.md), recorded whole; the pass tip is `30d52b595`.

## Why

TOOL-dTotalRecall-23 is built as its rev-3 spec says. I checked every claim the spec makes about current code against the tree before writing anything, and none failed. The pass is commit 30d52b595 on top of base 7fa604e1d. The spec's status header is CLOSED with today's date, and the commit ends with the `Pass: TOOL-dTotalRecall-23` trailer.

## Summary

**What was built (commit 30d52b595)**
- `tools/memory-tree/tree_lib.py`:
  - `LEG_READERS` with three readers: `unfenced-head`, `id-harvest` and `spec-head`.
  - The `leg_row` table, written only by `build_leg_rows`.
  - `derive_leg_version` (hash of the reader module's import closure, then its params key), `extract_head_lines`, `read_rows_at` (opens the index read-only) and `write_leg_fixture`.
  - `read_bindings` now reads record heads through `read_rows_at` and takes a keyword-only `counts`.
  - Helpers added: `load_leg_module`, `load_leg_reader`, `load_tag_index`, `read_leg_payloads`, `add_leg_counts`, `render_leg_line`, `build_fixture_index`.
- `tools/memory-tree/corpus_ids.py`: `extract_ids` and `derive_id_params` added. `walk` reads its corpus through `id-harvest`. `--check` prints `HYGIENE advisory leg rows: ...`.
- `tools/memory-tree/design_lib.py`: `extract_spec_head` added.
- `tools/memory-tree/gen_build_index.py`: `parse_spec_head` (which `parse_spec_text` now calls) and `read_spec_unit`. `collect` reads spec heads through `spec-head`. `LEG_COUNTS` plus `print_leg_lines` print the `leg rows:` lines on stderr at `--check` and `--print-bindings`.
- `tools/playbook/tag_index.py#build_index` calls `build_leg_rows` after `remove_unheld_rows`.
- `help/tags.md` gained one sentence about the leg rows.
- `memory/map/generated/symbols.json` was regenerated.
- Records: the acceptance ledger `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-23-1-acceptance-ledger.md` and deviation 1007 (`2026-11-23-build-TOOL-dTotalRecall-23-deviation-1007.md`).
- The `gen_build_index.py --write` re-renders went into the commit: `LIVE.md`, `backlog/TOOL.md`, the as-built view, the build README and the spec's records region.

**New selftest arms (owed to the close)**
- `gen_build_index.py#test_leg_rows` covers AC1 to AC6. Its staged break is `read_rows_at` serving a dirty path from its HEAD row.
- `corpus_ids.py#check_leg_harvest` covers AC7. Its staged break is `derive_id_params` leaving the family list out of its key.
- The existing call-graph arm in `corpus_ids.py`'s selftest now expects `route args=['extract_ids:2']`, because the spec's S4 split moves the anchor route call from `walk` into `extract_ids`. This is recorded in deviation 1007.

**Checks that ran (each stands in for the gate named; none is a RED-first observation)**
- A scratch probe over `write_leg_fixture`, plus both arm bodies called in-process with a stand-in `arm` function. All of AC1 to AC7 came out green. This stands in for the build-index and corpus-ids selftests.
- On the real tree, I compared this worktree's output with a shared clone at the base commit:
  - `corpus_ids.py --report` was identical.
  - `gen_build_index.py --print-bindings` stdout was byte-identical.
  - `gen_build_index.py --check` was identical apart from the two `leg rows:` lines; both versions exit 1 the same way at the base.
  - This stands in for the `memory hygiene` leg.
- `lexicon.py --measure` gives 1435, the same as `VERB_OFFENDER_PIN`, after I renamed one nested helper.
- `gotchas.py --for-diff HEAD~1..HEAD` selected 35 classes plus 6 universal. I checked the heredoc, grammar-root, pin-gated, fixture-finds-nothing and portability classes against the diff; no control bytes are in it and nothing needed fixing.

**Owed to the close**
- The RED-first observation of both new arms, each on its staged break.
- The legs: `memory hygiene`, `build-index selftest`, `corpus-ids selftest`, `gotchas selftest`, `memory-hygiene self-test` (corpus_ids `--check` now prints one more `HYGIENE advisory` line, which may move exact-output expectations), `tier2-review self-test`, `policy fixtures`, `govkit acceptance matrix`, `playbook render selftest`, `tags (the resolver's checks)` (a cold tree build now also writes the three readers' rows; that cost was not measured), `recall floor` and `recall floor arms`.

**Things to know**
- My first `--dispatch` (for the deviation record and the README) hit its own 100 s timeout (DERIVED, the builder's command limit) and recorded nothing. It left a lock directory, `.git/worktrees/unattended-dtotalrecall-ae256e/unattended/spec-tokens.dTotalRecall.lock`, which holds an expiry file, so I left it in place. I set the spec back to INPROGRESS and re-ran the dispatch under a larger bound, and it was declared.
- A later `--dispatch` declaring `memory/LIVE.md` was refused by check 49, because this unit also changes LIVE.md's generator, `gen_build_index.py`. Per the refusal and `.unattended.conf`'s `GENERATED_INDEXES`, generated outputs are admitted undeclared, so I staged `LIVE.md`, `backlog/TOOL.md` and the as-built view without declaring them.
- The first commit attempt was refused by hygiene check 23 because the ledger's AC3 token did not match its criterion. I fixed the token and the second attempt went through.
- The record door doubled the deviation record's title prefix; I corrected the heading before committing.
