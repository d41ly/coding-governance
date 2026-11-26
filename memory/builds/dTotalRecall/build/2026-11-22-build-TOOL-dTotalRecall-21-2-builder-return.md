**Serves:** journal TOOL-dTotalRecall-21
**Caused-by:** TOOL-dTotalRecall-21

# TOOL-dTotalRecall-21 build pass 2 — the builder's return

The gov-builder return for the pass dispatched at `3b34ddf02` from [2026-11-22-prompt-TOOL-dTotalRecall-21-build-brief-2](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-21-build-brief-2.md), recorded whole: a divergence, nothing committed.

## Why

DIVERGENCE: The spec names the wrong kit id for the new dependency, and the change it describes breaks a gate the spec never mentions. Built as written, the dependency would not do its job and the `govkit selftest` leg would go red.

1. §2 S4 and §8 F3 say "`tools/memory-recall/kit.toml`'s `requires` gains `playbook`". In the govkit registry, `playbook` is the entry at `tools/govkit/entries/playbook.kit.toml`. That entry lands no files: its `version_from` says "the entry lands no file since PLAY-dOrderedCharter-31". The kit that ships `tools/playbook/tag_index.py` is a different entry, `playbook-render`. Its descriptor is `tools/playbook/kit.toml` (`id = "playbook-render"`, `home = "playbook"`). It is also the entry whose `requires` already names `playbook`, `memory-tree` and `policy`. So `requires = ["memory-tree", "playbook"]` would let govkit install recall without `tag_index.py`, and `query.py`'s `resolve_kit_dir("playbook", "tag_index.py", here)` would then fail. What S4 and F3 have to say: `requires` gains `playbook-render`, the entry whose home is `playbook`. F3's grant line should name that entry too.

2. §4 Files touched and §7 Gates are both missing `tools/govkit/selftest.py` and its `govkit selftest` leg. Once memory-recall declares a requires edge to either playbook entry, `govkit.py#derive_unsatisfied_requires` makes `apply` refuse the selection, because the dependency is neither selected nor claimed by a receipt. These calls hit that refusal:
   - the aRF-36 block's `apply --kits memory-recall,memory-tree` calls, at selftest.py lines 8391, 8405, 8410, 8421 and 8437 in HEAD's numbering;
   - `pin_target`'s `kits = ["memory-recall"]` at line 8371.

   The arms that assert files landed would go red. What the spec has to say: Files touched gains `tools/govkit/selftest.py`, those selections add the required closure (`playbook-render`, `playbook`, `policy`), and §7 gains `govkit selftest`. `tools/govkit/matrix.py` already closes its selection over `requires` and needs nothing.

Advisory, not blocking (the spec writer may want to state these):
- (a) The query path now needs a born HEAD. `tag_index.load_view` runs `git rev-parse HEAD^{tree}`, so on a repo with no commit the S4 refusal prints "removing it costs one rebuild", which is the wrong remedy there. My draft makes the selftest's `make_repo` commit its seed.
- (b) AC6's grep covers all of `tools/`, so the README's upgrade note must not spell the retired budget key. My draft words around it.

Every other claim I probed holds at HEAD 3b34ddf0, so a revised spec can be built as written. Details are in `summary`.

## Summary

I did not commit TOOL-dTotalRecall-21. Two problems in the spec (listed in `why`) mean I can't build it as written: it names the wrong kit as the new dependency, and adding any such dependency breaks `govkit selftest`, which the spec doesn't list. I put every path I changed back and committed nothing. The tree is back at base 3b34ddf0. The only uncommitted changes are the main loop's staged `memory/builds/dTotalRecall/RUN.md`, which now also holds the extra dispatch row from my own `--dispatch` call, and the untracked unit-36 prompt. Neither is mine to touch.

**Draft saved for the next pass.** It is `TOOL-dTotalRecall-21-pass2-draft.patch` in the run's scratch, covering the paths `r21-paths.txt` there names. `git apply --check` confirmed it reverses cleanly; apply it with `git apply`. It contains:
- **S10:** `tag_index.py#load_index` drops virtual tables first, then re-reads the table list; the docstring says so.
- **S1:** `id_grammar.py#build_fts_rows` (rowids continue from the table's highest, `id` folds in `rec`). Every caller is re-pointed: bench, union, check-recall, test_recall_floor, row_grammar.
- **S2–S7, S9:** `query.py` now writes and reads its rows in the shared index (`load_served_set`, `derive_recall_digest`, `write_recall_rows`, `remove_unheld_recall_rows`). The cache, eviction and budget code is gone, and the inline `common_git_dir` is replaced by the tag index's.
- **S8:** check-recall grades the served set and reads `--data-dir` as an index file opened read-only.
- **The selftest:** 12 cache arms removed, 4 index arms added, pin 88 -> 80 with its provenance line; `make_repo` copies the playbook kit and commits its seed.
- **Docs and conf:** the kit README and both SKILL files, `help/tags.md`, `row-grammar.md`, `common_dir.py`, both conf files, and `legacy-homes.txt` (drained by `policy.py lists --write`).
- `kit.toml` says `playbook-render`, the correction point 1 of `why` asks for, not the spec's `playbook`.

**Not done yet, owed by the next pass:**
- the `test_recall_floor.py` New arm for AC7;
- re-stamping `verbatim.json`;
- `gen_map.py --write` and `gen_build_index.py --write`;
- re-measuring `VERB_OFFENDER_PIN`;
- the F5 and F8 deviation records and the acceptance ledger;
- re-stamping the `SESSION-KICKOFF.md` manifest;
- `memory/map/features/memory-recall.md`;
- the `tools/govkit/selftest.py` fix.

**Checks that ran**, all against the draft, which is now removed from the tree. Each stands in for the gate named:
- In a fixture repo (`%TEMP%/r21a`, plus a linked worktree, `r21b`), all through the CLI:
  - AC3: 1 blob extracted after one edit, 0 after its commit, 3 of 3 corpus paths re-extracted after a FAMILIES edit;
  - AC4: an untracked record is served in its own worktree, not in the other, and is served there once merged;
  - AC5: a zeroed header gives exit 2, naming the file and the remedy, and the file is kept;
  - AC8: `gov_tag.py --rebuild` exits 0 twice, leaves no `fts_` table, and the query between re-extracts 3.
  - These stand in for the `memory-recall kit selftest` arms.
- In a scratch clone (`%TEMP%/r21c`):
  - AC2: 12 of 12 fixture questions print the same hit lines through the tip and through `old/` (the start commit's `tools/`, extracted by `git archive`). Only the index file is created, no `recall/cache/`.
  - AC7: check-recall prints the same lines as the old kit's, with and without `--data-dir`.
  - Cold extraction took 34.8 s; a warm query takes 3.5 s.
  - These stand in for `recall floor`.
- AC1 and AC6 greps came back empty, and `common_git_dir` appears only as `T.` calls. A `build_fts_rows` rowid probe passed. These stand in for `row-grammar selftest`.
- The naming lexicon passed for all new names.
- `gotchas.py --for-diff` did not run, because there is no commit.

**Still owed at the close**, after a revised spec and a rebuilt pass:
- the RED-first observations of both New arms (`tools/memory-recall/selftest.py` AC3/4/5/8, `tools/memory-recall/test_recall_floor.py` AC7);
- the legs on the spec's gates section, plus `govkit selftest`.
- Risk: every fixture query now pays about 1.3 s of tag-index work, so the `memory-recall kit selftest` leg (evidence 270 s, DERIVED from `tools/run-gates/ceiling-evidence.txt`) may approach its ceiling.

No command timed out. Every scratch repo under `%TEMP%` was removed.
