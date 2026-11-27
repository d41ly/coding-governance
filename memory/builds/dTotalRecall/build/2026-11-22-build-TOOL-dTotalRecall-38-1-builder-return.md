**Serves:** journal TOOL-dTotalRecall-38

# TOOL-dTotalRecall-38 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `7047890d5` from [2026-11-22-prompt-TOOL-dTotalRecall-38-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-38-build-brief.md), recorded whole; the pass tip is `2f59e5acb`.

## Why

TOOL-dTotalRecall-38 is built and committed on top of base 7047890d5 as one pass commit. It carries the `Pass: TOOL-dTotalRecall-38` trailer, and the spec header moves from INPROGRESS to CLOSED in the same commit. Each spec claim about current code held when probed: unit 54's `parse_id_parts(ident, root, *, alt=None)`, the ten readers, the three kit routes and the census at HEAD. There was no divergence. The remaining checks are criteria only a gate or suite can observe, and they are named in the summary for the close.

## Summary

Commit 2f59e5acb builds TOOL-dTotalRecall-38 on base 7047890d5. All five acceptance criteria were observed with probes. The suite legs and the new arm's RED-first observation are still owed at the close.

**What changed**
- **Census:** `tools/memory-tree/id_grammar.py#scan_readers` now also lists every line that splits a value named for an id, slug or unit on a hyphen. The new `_READER_SPLIT_SHAPE` covers Python `.split("-")` / `.rsplit("-"`, the four shell `${name%-*}`-style expansions, and `cut -d-` / `IFS=-` next to such a name.
- **Flip probe:** `run_flip_probe` adds two checks per flip:
  - `parse_id_parts("TOOL-<slug>-3", clone)` must return the planted slug and 3.
  - The clone's census must list no split hit (compared by path and line text) that this tree's census does not.
- **Cache fix:** the probe now also clears the slug cache of the second `id_grammar` copy that `tree_lib` imports when the probe runs as `__main__`. Without this, the later flips would read the first flip's grammar.
- **`backlog.ANY_FAMILY`:** the family class is now defined once, and `FAMILY_SHAPE` and `GRANT_ID_RE` both splice it.
- **The ten readers** now call `parse_id_parts`, each through its kit's existing route and with the answers the spec's §4 table gives:
  - Backlog's three readers, `build_grade_row`, and migrate's `read_slug` / `build_id_sort_key` pass `alt=ANY_FAMILY`.
  - `cmd_new_build` passes `alt=_id_alternation(conf)`.
  - `derive_probe_labels` and `measure_answer_used` go through `extract.id_grammar`.
  - `_parse_slug(uid, root=None)` goes through `load_memory_tree`. Its 3 call sites (in 2 functions) pass `ctx.root`. If the kit does not load or refuses the tree, it falls back to §8 F5's partition/rpartition strip.
- **Selftest:** a new arm in `tools/memory-recall/selftest.py`, `SELFTEST_ARMS` 87 -> 88, with its chain line.
- **Records:** `memory/map/generated/symbols.json` regenerated; acceptance ledger at `C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-38-1-acceptance-ledger.md`; the generator's rewrites of `memory/LIVE.md`, `memory/backlog/TOOL.md` and the build README included.

**Census:** before the first reader edit it listed 29 split lines, 8 of them §1 readers. 21 remain at the tip, each kept with an S2 reason in the commit's `Decided:` trailers. The Python shape accepts either quote, which adds two single-quoted hits beyond §4's grep. Both are kept: `deviation_join.py` reads the sequence after the last hyphen, and `render_spec_skeleton` is unit 45's. So no code file joined the write set.

**Checks that ran** (each stands in for the gate named in brackets)
- **AC1** [memory-recall kit selftest]: `python -c` probes of `parse_id_parts`.
- **AC2** [memory-recall kit selftest, plus the new arm]: the tip's `--readers` over a scratch clone with base `tools/` listed all eight readers; over the tip it lists none of the ten.
- **AC3:** both `git grep`s. The first printed only the kept hits; the second printed nothing.
- **AC4** [new arm]: `--flip-probe` over a scratch tip clone printed `ok` on all 6 flips. With `read_slug` reverted to its split and committed, every flip named the reverted line and the probe exited 1.
- **AC5** [drift-audit selftest, drift-audit records, backlog migration selftest]: `python -c` over a scratch clone with a dated-slug README returned every expected value, including the `DriftError` fallback.
- **New arm's steps** [memory-recall kit selftest]: reproduced by a scratch script over a `make_repo`-shaped fixture, without importing the suite. The 3 plants were listed and the control was not; the unreverted clone showed no census failure; the reverted clone failed on 6 of 6 flips and exited 1; with the revert skipped, 0 of 6 failed.
- **Real tree:** `gen_build_index.py --asks --all` output is byte-identical between base and tip.
- **Naming lexicon:** the new test name is OK, and `--measure` leaves `VERB_OFFENDER_PIN` at 1446, unchanged.
- **Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` was run and acted on. No control bytes in the diff; new locals checked for collisions; the arm has a control plant and an observed negative.

**Owed at the close**
- The legs in spec §7: tier2-review self-test, drift-audit selftest, drift-audit records, backlog migration selftest, build-index selftest (its EXMP fixtures for §8 F4), build README slot contract, recall floor, recall floor arms, memory-recall kit selftest, policy fixtures, memory hygiene, lexicon naming predicates, and the four codebase-map legs.
- `New arm:` `tools/memory-recall/selftest.py#test_split_census_and_the_flip_probe_census_check` (covers AC2 and AC4). Its RED-first observation is owed.

**Other notes**
- My first `--dispatch` call (110 s bound, DERIVED from the builder's tool timeout) timed out while the spec read CLOSED. I set the status back to INPROGRESS, then declared again.
- That retry refused to declare `memory/LIVE.md` together with its generator `gen_build_index.py` (check 49). It said `memory/LIVE.md` and `memory/backlog/TOOL.md` are generated outputs that commits may carry undeclared. I followed that and declared only `memory/builds/dTotalRecall/README.md`.
- `_parse_slug` measured about 1 ms a call against §5's 0.5 ms. Over the 4629 anchor matches that is about 5 s, far under the 540 s `drift-audit records` ceiling (recorded in a `Decided:` line). (DERIVED, the builder's timing probe at `2f59e5acb` and `tools/gate-legs.json`)
- No check was skipped, and the scratch clones are removed.
