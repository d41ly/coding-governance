# dOrderedCharter — unit 51's builder return

**Serves:** journal PLAY-dOrderedCharter-51

Run wf_35939ee0-1ad, summarized from its return.

- Built as pass commit `1f078024a`: `blob_row`, `path_row` and `blob_parsed` carry the extractor version; every resolver
  read joins the reading worktree's own `view_version` map; `tree_built` is keyed (tree, versions); `INDEX_SCHEMA = 2`;
  `read_live_versions`, `remove_dead_versions` and `gov_tag.py --gc`; plants `two-versions` and `served-across`.
- Unit 22's owed items landed here: `{prefix}/memory-tree/design_lib.py` in the `playbook render selftest` guard, with
  the kickoff manifest re-stamped, and the README paragraph on the `purpose` arm and `chain.toml` (deviation 512,
  `report`). Deviation 513 records `--gc` also running `remove_unheld_rows` and the files beyond §4.
- Observed by probe: AC1 to AC4 as the ledger records; a scratch mutation restoring unit 44's tree-only key turned
  `served-across` red; a real-tree probe built cold in 13.1 s and warm in 1.7 s.
- Until landing, worktrees on schema 1 (main) and schema 2 (this branch) evict each other's shared index on each
  switch, by unit 44 S4's stamp rule.
- Owed at the close: RED then GREEN for the `two-versions` and `served-across` rows against unit 44's one-version key;
  the §7 legs, the docs leg for `help/tags.md`'s fingerprint, the kickoff manifest-check, kit/dogfood doc parity and
  the `tags` leg over the tree.
