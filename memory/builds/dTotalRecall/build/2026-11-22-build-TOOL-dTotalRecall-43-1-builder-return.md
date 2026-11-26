**Serves:** journal TOOL-dTotalRecall-43
**Caused-by:** TOOL-dTotalRecall-43

# TOOL-dTotalRecall-43 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `f41d86c42` from [2026-11-22-prompt-TOOL-dTotalRecall-43-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-43-build-brief.md), recorded whole; the pass tip is `none`.

## Why

DIVERGENCE: spec 2026-10-26-spec-TOOL-dTotalRecall-43.md rev-7 cannot be built as written. I checked it against HEAD f41d86c42 before any product edit and five checks failed.

(1) §2 S19, §3 and AC19 contradict each other. tools/govkit/registry.toml keys both `[[ledger]]` rows by `fields = ["path", "section"]`. The two homes share one key: (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md`, `research`) is in both memory/project/legacy-records.txt and memory/project/record-kinds-legacy.txt (DERIVED 2026-11-23, a python set intersection over both files). Merged under the pair key, legacy_ledger.py#read_rows marks that row `duplicate`, so AC19's "equal the two homes' row counts" reds. A field `check` in `fields` is the triple key, and §3 gives that key to TOOL-dTotalRecall-52. Also, `fields` holds key fields only: a ledger row is key, count, values, and nothing carries a non-key `check`. The spec must say either that this pass keys by (path, section, check) or that the merge itself moves to unit 52. Files touched also lacks two paths the merge needs. The first is `memory/project/legacy-records.txt`, which the merge empties or deletes. The second is `.memory-tree.conf`, whose PROJECT_REGISTRY_EXTRA lists `legacy-records.txt`. And record_causes.py#POPULATION (`legacy-records`), which S19 says unit 52 moves, has to change at this pass if check_causes is to find a registration.

(2) §2 S22 and AC22: recall's extraction does not fit `blob_parsed`. `blob_parsed` is keyed (blob, extractor, version) with no path. query.py#write_recall_rows extracts per path: `E.extract_records(path, text)`, with FTS rows keyed (path, blob, digest). So one blob at two paths would be extracted once. Recall also serves untracked corpus files hashed by query.py#derive_served_pairs, which no `tree_path` or `dirty_path` row holds. tag_index.py's sweep deletes every `blob_parsed` row no tree or dirty row holds, so such a file's ledger row is swept on every build while its FTS rows stay. The spec must say how path-keyed and untracked pairs are tracked once `fts_blob` goes. Separately, S22's Readers line names tools/memory-recall/check-recall.py (line 300 joins `fts_blob`), but Files touched does not list it.

(3) §2 S21 and AC21 leave the design open. PLAY-dOrderedCharter-44 extractors register as `[[namespace]]` rows of tools/playbook/namespaces.toml, which is not in Files touched. Each such row is a tag namespace (ns, owner, layer, role, purpose-source), and its `blob_row` rows (tag, kind, line, end_line, text) reach gov_tag queries through `path_row`. A leg reader's product is one JSON payload per memory-root blob, and `blob_row` has no payload column. tag_index.py#derive_extractor_versions hashes module closures only and takes no root or conf input, so "an optional params digest" needs a stated design. The spec must state the registration, the row shape, how the rows stay out of tag queries, and where the params digest enters.

(4) S21's Readers line is stale. It says "READER NOT IN TREE — `leg_row` and `LEG_READERS` ... absent at HEAD". At HEAD, tools/memory-tree/tree_lib.py defines them (`LEG_READERS`, `LEG_TABLE`, `read_rows_at`, `build_leg_rows`), and these files read them:
- tools/memory-tree/gen_build_index.py (#test_leg_rows, line 206's import, line 1503)
- tools/memory-tree/corpus_ids.py, line 128
- tools/playbook/tag_index.py, line 834
`LEG_READERS` also holds a third reader the spec never names, `spec-head` (`design_lib:extract_spec_head`), and tools/memory-tree/design_lib.py is not in Files touched.

(5) Files touched is incomplete beyond (1) to (4): tools/memory-recall/check-recall.py, tools/playbook/namespaces.toml, tools/memory-tree/design_lib.py, memory/project/legacy-records.txt and .memory-tree.conf.

No product path was changed and nothing was staged by this pass. The only staged change in the tree is the main loop's RUN.md dispatch and brief rows, left as found. No draft was made, so no patch was saved.

## Summary

I built nothing and committed nothing. The spec cannot be built as written, so I returned a divergence. I made no product edit, so there was nothing to restore. `--brief` reported the brief already recorded (unchanged at 4eaeb47a5cbf).

**Checks that ran.** All were read-only probes against HEAD f41d86c42 (git grep, sed, and a small python script over the two ledger homes). I checked the symbols and lines the spec cites for S1, S6, S10, S14, S15, S16, S19, S21, S22, S34, S41, S43, S44, S53 and S59. These claims held at HEAD:
- `BUILTIN_ARMED` still arms `js` under `ts-tokens`, against lexicon's `KNOWN_EXTS`, which maps it to `js-regex`/`probe`.
- `check_memory_word` takes any `/<root>/`.
- `GIT_OWN` is a name set.
- `write_record` opens its file with mode `"x"`.
- `read_claim_replay` reads a 64-commit window.
- No memory file outside `builds/` carries a Serves line in its head, so S1's arm would name nothing at the tip.

**What failed.** S19 (a shared ledger key, the triple-key split with unit 52, missing paths), S21 (registration design, a stale Readers claim, a third reader `spec-head`), S22 (`blob_parsed` keys no path, and untracked pairs are swept) and Files touched. The details are in `why`.

These probes stand in for no gate. No gate, suite, bar or `--selftest` ran. I did not run gotchas `--for-diff`, because no commit exists to run it over.

**Owed at the close, once the spec is revised and the unit is rebuilt:** the five `New arm:` RED-first observations in §7 (record_kinds.py, gov_record.py, lib/extract_code.py, runlog/memory_measure.py, memory-recall/selftest.py), and the legs on the spec's gates section, S32 and S33 included. No command timed out or was skipped.

Files:
- C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-43.md
- C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/govkit/registry.toml
- C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/memory-recall/query.py
- C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/memory-tree/tree_lib.py
