**Serves:** journal TOOL-dTotalRecall-52
**Caused-by:** TOOL-dTotalRecall-52

# TOOL-dTotalRecall-52 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `d1920cb20` from [2026-11-22-prompt-TOOL-dTotalRecall-52-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-52-build-brief.md), recorded whole; the pass tip is `none`.

## Why

DIVERGENCE: as written, spec section 6 AC3 and AC5 cannot both be true. AC5 (and S4's "No row is lost") requires the merged home `memory/project/record-kinds-legacy.txt` to keep every row of the old `legacy-records` home. One of those rows is old-home line 24452. Its section key is the derived anchor `m35-derived-anchors-collide-on-legacy-records-that-repeat-a-heading-and-the-uniqueness-check-reds-them-finding-65`, which comes from an untagged heading of `memory/builds/dClosedLoop/reviews/2026-10-17-review-PLAY-dClosedLoop-1-systems-retrofit.md`. After the fold it is a `causes` row of the merged home. AC3's grep, `git grep -n "legacy-records" -- tools .memory-tree.conf memory/project ':!tools/run-gates/ceiling-evidence.txt'`, covers `memory/project`, so it prints that row and AC3 is red. Section 1's carrier count ("18 lines in 6 files besides the home") left the home out, but AC3's pathspec does not leave out the merged home that now holds the row. Dropping the row fails AC5. Editing the frozen review's heading is outside the spec's scope and Files touched. To fix it, AC3 (and section 8 F2, or a new F3) must also spare `memory/project/record-kinds-legacy.txt`, for example `':!memory/project/record-kinds-legacy.txt'`, because it is a ledger home whose rows key derived anchors and name no population. Alternatively, AC3 could grep for the old name as a carrier only, such as `legacy-records.txt` or `"legacy-records"` quoted. Its Red-when line ("a carrier of the old name stays live") already matches that reading. I checked every other claim in the spec against the tree and found no other divergence: the 18 lines in 6 files, the 67,624 old-home rows (139 of them widened), the 7 line-number-shaped sections, the one shared (path, section) pair, both homes absent at 8b8b1374c, and the cited symbols. The draft built every other criterion green and is saved as a patch for the re-dispatch. Every path is restored, and the tree holds only the harness's staged RUN.md, as at start.

## Summary

Nothing committed: the pass stopped on the AC3/AC5 conflict above. Base was d1920cb20428dd50c8c85f1286c42fd62b4152d5. The brief was already recorded (`--brief` reported it unchanged at 7ac82bf1cd67). The changed paths are restored and the tree is back to the staged `memory/builds/dTotalRecall/RUN.md` alone.

The full draft is saved at C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/TOOL-dTotalRecall-52-draft.patch (made with `git diff HEAD`, about 27 MB). It can be re-applied once the spec is revised. What it does:
- **Registration:** `record-kinds-legacy` in `tools/govkit/registry.toml` is keyed `["path","section","check"]` with `verbatim=["section"]`. The `legacy-records` table is removed and the `record causes` leg's `why` names the merged population's `causes` slice.
- **Merged home:** `memory/project/record-kinds-legacy.txt` holds 11,135 `kind-schema` rows and 67,624 `causes` rows. Every row keeps its own sha and disposition, including the 139 `widened:` rows. The header now reads `key record path,section,check`.
- **Old home and conf:** `memory/project/legacy-records.txt` is deleted (`git rm`). Its `PROJECT_REGISTRY_EXTRA` entry and comment are gone from `.memory-tree.conf`.
- **record_causes.py:** `POPULATION` is `record-kinds-legacy` and the docstrings are updated. `read_legacy_paths` reads only the `causes` slice and refuses a registration that has no `check` field. `--measure` prints `<path> <section> causes 1`. `write_fixture`'s table uses the triple and `verbatim`.
- **record_kinds.py:** `read_legacy_keys` returns the `kind-schema` slice as (path, section) pairs. `--seed-legacy` prints both slices, the causes slice through `record_causes.derive_population_rows`. `build_fixture` writes its table and home with the triple.
- **README and hygiene test:** the memory-tree README's causes lines and `--seed-legacy` row are updated, and so is the `--plant none` assertion in `check-memory-hygiene.test.sh`.
- No function and no constant was minted.

Checks run on the draft (unit probes only; no gate, suite or bar):
- **AC1 probe:** printed `('path','section','check') ('section',) 78759 [] ['causes','kind-schema']`. It stands in for the duplicate-key read of `memory hygiene` and `govkit selftest`.
- **AC2 probe (unit 62's):** printed `True` and `(None, 'no memory/project/record-kinds-legacy.txt at 8b8b1374c4fc ...')`, so no `gained` key. It stands in for `ratchet (never gains)`.
- **AC4 probe:** printed `10796 record row(s) (-), 56828 section row(s) 11135`. That is 10,796 + 56,828 = 67,624 `causes` rows and 11,135 `kind-schema` rows, which also covers AC5's per-slice counts.
- **AC4 fixture:** `record_causes.py --fixture --plant none` printed `record causes: record-kinds-legacy · 2 record row(s) (-), 0 section row(s) · memory.legacy-anchors none`. This is the assertion `check-memory-hygiene.test.sh` makes.
- **record_kinds fixture:** `record_kinds.main(['--fixture'])` came back green (exit 0).
- **AC3 grep:** printed the merged-home row described in `why`, which is the divergence.

Not run:
- The `--seed-legacy` run over the full repo. It is S1's observation, owed on the rebuild.
- `gotchas.py --for-diff`, because there was no commit.

Owed to the close after the rebuild, with no new arm (spec section 7): the section 7 gates, `memory hygiene` and `govkit selftest` among them.
