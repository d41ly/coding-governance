# PLAY-dOrderedCharter-18 deviation 184 — the move's re-export seam, its pins and its dead resolvers, as built

**Serves:** deviation PLAY-dOrderedCharter-18

- **Departs from:** `PLAY-dOrderedCharter-18@rev-3 [§2 S3, §2 S9, §4]`
- **Hand-off:** spec-to-code
- **Before:** S3 says `extract.py`, `recall_conf.py` and `bench.py` re-export the moved names "reached through the `resolve_kit_dir` copy each already carries"; S9 lists the suite arms the move changes; §4 "Files touched" lists 24 files.
- **After:** `recall_conf.py` and `bench.py` carried no `resolve_kit_dir` copy, so each gained the canonical copy, byte-identical, and resolves `id_grammar.py` through it as `extract.py` does; `bench.py`'s pin in `tools/memory-recall/verbatim.json` is re-stamped to its new bytes; the recall selftest's digest arm, which planted `KIT_MEMORY_RECALL_VERSION` to prove the version folds into `Conf.digest`, is re-planted on the grammar epoch S4 folds instead; the `resolve_kit_dir` copies whose one call reached the recall kit are deleted from `corpus_ids.py`, `merge-rows.py`, `transition_audit.py`, `row_grammar.py` and `check-verdict-epoch.sh`; `row_grammar.load_recall_kit` is `load_index_builder`; the new module's helpers are named `derive_grammar_epoch`, `build_supersede_patterns` and `build_grammar` to the naming lexicon's verbs, and its `Grammar` bundle carries the eras as `eras`, which `extract.ERAS` re-binds from; `check-wiring.test.sh` resolves the recall kit's directory by `query.py` rather than `extract.py`; manifest-check's KQ AC8 R0 arm hides `id_grammar.py`, the reader's grammar, where it hid `extract.py`.
- **Cause:** builder discovery
- **Reason:** the move cannot re-export through a resolver copy a file does not hold, and a re-pinned verbatim file and a re-planted version arm are the two suite consequences of S3 and S4 that S9's list did not name; the deleted copies had no caller left once the grammar is a sibling, and the lexicon gate counts a helper that leads with no declared verb.
- **Evidence:** `tools/memory-recall/recall_conf.py` and `tools/memory-recall/bench.py` at 98995aa27 carry no `# >>> resolve_kit_dir` block; the recall selftest's `test_digest_covers_kit_version` set `KIT_MEMORY_RECALL_VERSION` and asserted the digest moved; `python tools/lexicon/lexicon.py --check` read 1214 verb offenders over its pin of 1211 with the first names and exits 0 with these.
- **Risk:** additive
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-18
