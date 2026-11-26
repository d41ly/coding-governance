**Serves:** journal TOOL-dTotalRecall-116
**Caused-by:** TOOL-dTotalRecall-116

# TOOL-dTotalRecall-116 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `92ed3a99d` from [2026-11-25-prompt-TOOL-dTotalRecall-116-build-brief](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-116-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `none`.

## Why

DIVERGENCE: §2 S3 and §4 "The blob branch" cannot both hold. S3 says the returned `path` is the path the row was read at. The §4 code sets `path = rows[0]["path"]` for every key with a served row, whichever path the indexed blob stands at, and its other-tree fallback takes the first `path_row` of any kind. (DERIVED 2026-11-25, the pass)

Observed in this worktree (DERIVED 2026-11-25, p116.py and q.py):
- `TOOL-cSpliceWarden-6@<blob of memory/DECISIONS.md>` returned the text of the DECISIONS row at line 24 under the path of the TOOL-cSpliceWarden-6 spec. (DERIVED 2026-11-25, the pass)
- Its BACKLOG blob gave the same wrong path, at line 6.
- This is today's behaviour, and the §4 code keeps it. (DERIVED 2026-11-25, the pass)
- 1284 of 16160 keys stand in several paths, with 1945 blobs beyond the first (DERIVED 2026-11-25, q.py). 13 of the several-path keys are file stems, such as a `.md`/`.sh` pair (DERIVED 2026-11-25, p116.py).

The fixture showed the same thing on a scratch copy holding the §4 code: `DEC-tFix-1` at the archive file's blob came back as `memory/DECISIONS.md`, lines 3 to 5 (DERIVED 2026-11-25, p116fx.py). It matters because `edge_grammar.py#resolve_edge` and `gov_tag.py#run_record_show` print `path:line` from this value, so a foreign path is certified, which is the class of H2. No AC observes it: AC1 and AC3 use a key with one path.

WHAT THE SPEC WOULD HAVE TO SAY
1. §4 code, the two path lines: (DERIVED 2026-11-25, the pass)
   - `path = next((r["path"] for r in rows if r["blob"] == sha), "")`
   - under `if held is not None and not path:` `got = [p for (p,) in con.execute("SELECT DISTINCT path FROM path_row WHERE blob=? AND kind='record'", (sha,))]` then `path = min(got, key=lambda p: (pathlib.PurePosixPath(p).stem != key, p))`. `got` should not be empty: `tag_index.py#remove_unheld_rows` drops path rows and blob rows on the same tree and dirty-path holding.
2. §2 S3: "the path the row was read at: for an indexed blob, a path the index holds it at; for an unindexed blob, the served path it was extracted at; never empty". The second clause is needed because §4 accepts an id key at another record's old blob. The archive's old blob of `DEC-tFix-1` then returns `memory/DECISIONS.md`. (DERIVED 2026-11-25, the pass)
3. One criterion observing it (AC3, or a new one): a probe reads an id that stands in two files at each file's blob, and each returned `path` is that file. Red when it is `rows[0]`'s.

Alternatively, S3 can be narrowed to "never the empty string" and the wrong path moved to §3 as a non-goal. That is the spec writer's choice, and the §4 code then builds as written. (DERIVED 2026-11-25, the pass)

MINOR, for the same revision: S2 says "the file-name key of a path git's history holds that blob at", but §4 asks only the served view's paths, so a record moved under its own file name is refused at a blob only its old path held. `git log --diff-filter=R` over memory/builds shows one such move, an R100 whose blob the new path indexes (DERIVED 2026-11-25). Wording only.

## Summary

Nothing is committed and no product file was edited. The worktree stands as found, with only the pre-staged memory/builds/dTotalRecall/RUN.md. The brief was already recorded at d87fe0b96d54.

DRAFT, ready to apply once the spec is revised
- C:\Temp\claude\7a8436c9e3b87ce5\9067262b-db21-4497-8ba8-ef2deab46f53\scratchpad\TOOL-dTotalRecall-116-draft.patch is the whole record_find.py change: check_blob_path, the branch with the corrected path lines, the three plants and the docstring. The suite arms, floor, shell-role row and map are not in it.
- The draft adds `--literal-pathspecs` to the §4 git call. This is not stated in the spec; keep or drop it at the revision. (DERIVED 2026-11-25, the pass)
- The docstring paragraph still needs a reflow.
- The fixture path probe is C:\Temp\claude\7a8436c9e3b87ce5\9067262b-db21-4497-8ba8-ef2deab46f53\scratchpad\p116fx.py.

CHECKS RUN, over a scratch copy of the kits (DERIVED 2026-11-25). They stand in for the memory-hygiene self-test's new arms, which stay owed to the close.
- With §4 as written, and again with the corrected path lines, `--plant blob-unknown-key` printed `refused show: key NO-SUCH-KEY` and exit 2. (DERIVED 2026-11-25, the pass)
- In both runs `blob-foreign-text` and `blob-foreign-record` each printed `is no version of` and exit 2.
- In both runs `unheld-blob` printed `the second` and exit 0.
- AC3's probe returned a path ending `deviation-1.md`, on both versions of the branch.
- With the corrected lines the two-file id returned each file's own path; with §4 as written it returned `memory/DECISIONS.md` for both. (DERIVED 2026-11-25, the pass)

SPEC CLAIMS PROBED TRUE (DERIVED 2026-11-25)
- NO-SUCH-KEY at the README.md blob returned path '' over lines 1 to 121 today. (DERIVED 2026-11-25, the pass)
- The TOOL-dTotalRecall-114 builder-return stem at that blob was certified today, over lines 1 to 120 of its own path. (DERIVED 2026-11-25, the pass)
- `extract_record` emits a stem's row from the path alone.
- FLOOR_ASSERTIONS is 830, and the hygiene suite's shell-role row is 3747. (DERIVED 2026-11-25, the pass)
- The lexicon admits `check_blob_path`.
- No file in Files touched is on the kickoff manifest's `watch:` list.

COST, for AC4: on this tree a warm view load took 7.8 s and one record scan 46 s, so each `read_section` costs about a minute (DERIVED 2026-11-25). AC4's three reads are minutes, as its cost line allows.

SKIPPED OR BOUNDED
- The first whole-tree probe (p116.py) outlived its 600 s bound; I killed it and ran it once more under a 550 s bound. The first run's output was buffered, so I had read nothing from it. (DERIVED 2026-11-25, the pass)
- The rerun printed every answer used above and timed out (DERIVED 2026-11-25) only in its last query, a count of blob rows with no path row. I dropped that query and read the question from the source instead.
- My three scratch fixtures under C:\Temp\rf-* were removed. The other rf-* directories there predate this pass and were left.

NOT RUN: no gate, suite, bar or selftest, and no `gotchas.py --for-diff`, because there is no commit.
