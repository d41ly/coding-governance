# PLAY-dOrderedCharter-44 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-44

Each line is a plant `gov_tag.py --fixture` built in its own scratch repository under the temp root, or a
probe this pass ran in the worktree at cf0c94574 with the pass applied. The playbook render selftest, the
`tags` leg over the tree and every `New arm:` line's RED-first observation (each plant's failing case
staged by the base freshness rule) are the main loop's at the close: a role agent runs none of them.

**Evidences:** PLAY-dOrderedCharter-44
- AC1 — `--plant new-extractor` — exit 0; the build after `fixture_again:extract_again` is registered printed `2 blobs parsed, 2 extractor runs, 6 skipped as fresh`, `the new extractor's rows over the old blobs: 4` and `incremental rows equal a cold build's`. OWED to the main loop: the arm's RED-first observation
- AC2 — `--plant tagless` — exit 0; with `tools/corekit/none.tags` yielding no row, `1 blob parsed after one file changed, 0 on a build with no change` (the second build walks the tree again with `tree_built` cleared, `0 blobs parsed, 0 extractor runs, 7 skipped as fresh`). OWED to the main loop: the arm's RED-first observation
- AC3 — `--plant extractor-edit` — exit 0; `fixture_tags:extract_declared re-ran over 2 blobs, 0 skipped; the others ran 0 times, 4 skipped as fresh; 0 rows of the old version`, and `incremental rows equal a cold build's`. OWED to the main loop: the arm's RED-first observation
- AC4 — `--plant rebuild` — exit 0, `42 rows, then 42 rows from nothing: dumps equal`, the dump now carrying `blob_parsed`; `two-paths`, `one-commit` (`built, 1 blob parsed`), `dirty`, `none` and `retired` exit as their arm rows ask. OWED to the main loop: the arm's RED-first observation
- AC5 — `--plant schema` — exit 0; a file stamped `user_version` 0 holding a unit-19 `parsed` sentinel row printed `tag-index — rebuilt: schema 0 to 1`, `stamped 1 after the build;` and `incremental rows equal a cold build's`. Over the real tree, with its own index under the scratch root seeded with unit 19's tables and no stamp, a probe printed the same rebuild line, then a cold build `10347 parsed 10360 runs 0 skipped` (21.7 s) and, `tree_built` cleared, a warm one `0 parsed 0 runs 10360 skipped` (2.3 s), `blob_parsed rows 10360 sentinels 0`, and the namespace counts unit 10's ledger names (`doc` 117, `kit` 30, `layer` 12, `reader` 3). OWED to the main loop: the arm's RED-first observation
- §5 error state — `derive_extractor_versions` over a row naming a missing module raised `namespace 'kind' extractor nowhere_mod:extract_x: its module nowhere_mod.py is unreadable`, which `gov_tag.py` exits 2 on
- naming — `lexicon.py --check` printed no verb offender over its pin once the plant's closure was named `print_equal`
