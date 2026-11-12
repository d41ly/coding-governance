# dOrderedCharter — unit 19's builder returns

**Serves:** journal PLAY-dOrderedCharter-19

Runs wf_63e33fb3-61f, wf_4f067f67-62a and wf_7fdffa2d-436, summarized from their returns.

- wf_63e33fb3-61f returned `DIVERGENCE:`: rev-5's citation check graded every token of every text file, so gov's tree
  would red at landing. The spec writer revised spec 19 to rev-6 (Markdown citation syntax outside the build records,
  §8 F4 option d) and folded spec 49's S38 and AC29 into it.
- wf_4f067f67-62a built rev-6 whole and rolled back when `--dispatch` refused AC17's suite run once the spec turned
  INPROGRESS; its change was saved as a scratch patch. The main loop swept every DEFERRED spec of the build with the
  spec-token check read as live and folded the 52 hits it named (`6a7233873`, spec 19 rev-7; `793d3435a`, rev-8).
- wf_7fdffa2d-436 built rev-8 as pass commit `9cb93347d` from the saved patch, and `f1ab441da` (`Pass: none`)
  regenerated `.governance/policy.json` in its own commit as S8 says. `.lexicon.conf`'s verb pin moves 1211 → 1216 for
  the moved names counted in both homes; deviation 195 (`report`) records the cold index cost (10311 blobs, 54 s,
  182 MB at `<git-common-dir>/gov/index.db`).
- Observed by probe: AC1 to AC17 as the ledger records.
- Owed by the checklist: the `playbook render selftest` leg's guard does not name `{prefix}/memory-tree/id_grammar.py`
  or `{prefix}/memory-tree/coverage_join.py`, which `gov_tag.py` loads (class held-suite-guard-misses-a-sibling-kit);
  the write gate refused the edit after the CLOSED flip, so it is handed to PLAY-dOrderedCharter-10's brief.
- Noted, unchanged: `tag_index.read_git_stdout` passes the ambient `GIT_*` environment through; the closing review
  reads it.
- Owed at the close: `python tools/playbook/gov_tag.py check` over the tree; RED then GREEN for the `doc.no-such-doc`
  plant in `memory/guides/MERGE-BAR.md`, the `adopt-playbook.sh --selftest` tag plants, the `coverage_join` and
  `common_git_dir` parity rows, and `tools/codebase-map/selftest.py`; the `policy check`, `policy fixtures` and
  `straggler-guard arms` legs.
