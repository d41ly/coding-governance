**Serves:** journal TOOL-dTotalRecall-53
**Caused-by:** TOOL-dTotalRecall-53

# TOOL-dTotalRecall-53 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `f5a81b323` from [2026-11-23-prompt-TOOL-dTotalRecall-53-build-brief](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-53-build-brief.md), recorded whole: a divergence, nothing committed.

## Why

DIVERGENCE: the spec cannot be built as written at f5a81b323. I found two problems before writing any product code.

(1) §2 S9, S8 and S34, and §4 "How the batch builds", contradict AC8. S9 grades each `**Serves:** ` literal. Each literal is answered by a `Caused-by` on its own line or the three lines below it: re-deriving the spec's own figures (116 lines in 24 files) matched only with the literal's own line inside the window. Otherwise the literal needs S34's marker on its line. §4 allows a marker "only where its lead opens a comment in that line's language", and a cause line only on "a Serves literal inside text a writer renders into a record". Five of HEAD's 116 unanswered literals meet neither rule, because each sits inside a docstring or a multi-line string:
- `tools/workflows/review_replay.py:36`, in the module docstring, `the `**Serves:** spec-audit` binding`.
- `tools/workflows/review_replay.py:205`, the first line of the triple-quoted `LEGACY` fixture. The file's own comment says its fixtures are "inline, no file or git access", so it writes no record.
- `tools/memory-tree/build_records.py:17` and `:902`, both docstrings.
- `tools/runlog/record.py#check_serves_line:1514`, a docstring.

For review_replay.py this is a direct contradiction: S8 and AC8 need the file listed as kept with reason `reader-prefix`, never red. But only one of its three literals (`:258`, `ROUND1_BINDING`) can take a `#` marker, so under S9 plus §4 the other two read red. S9 or §4 would have to say how such a literal is answered. Possible answers are:
- a marker inside the string text is read as a marker;
- the census skips docstring and string-body lines;
- the literal is reworded, which the spec should name per site.

AC8 must then follow whichever answer is chosen.

(2) §2 S36, §8 F2 and §5 conflict with the `build-method size` ceiling. F2 resolves (a) "within build-method size's ceiling". But `memory/guides/BUILD-METHOD.md` is 30717 LF-normalized bytes (`tr -d '\r' | wc -c`) against its declared `≤30720 bytes` (its M1 Budget line, read by `tools/check-template-size.sh`), so 3 bytes are left. Naming `**Caused-by:** <the first id, bare>` in the two record-head examples (`BUILD-METHOD.template.md` lines 140 and 276, the blob `e11b530ac` lines, unchanged at HEAD) adds far more than 3 bytes, and the render reaches the measured guide. BUILD-METHOD M1 and M3 make the ceiling the owner's, and F2's grant covers only the two examples, not a trim of other method prose. The spec would have to name a trim that fits inside F2's grant, or route the raise to the owner.

The other claims I probed hold at HEAD:
- S16: the 34 split hits.
- S34: the 12 alias hits, 7 kept and 5 red, at the cited lines.
- S23: 309 files with 196 unhomed (gotchas 178, guides 10, map 4, four root documents).
- S19: the awk line `check-memory-hygiene.sh:3654`.
- S22: `deviations.py:380` and no other build-folder census hit.
- S21: the three `derive_record_kind(` callers.
- S24 and S33: the `derive_path_key` and `derive_folded_path` sites.
- S12: the count-only line in `check_edge_cardinality`.
- S5: the view head's first three lines are unmoved since 462d20f3.
- S37: the `shape-run` row's `unarmed` value.

No repository path was changed. The draft is not saved as a patch because no draft was written.

## Summary

I committed nothing: TOOL-dTotalRecall-53 cannot be built as its rev-5 spec is written. I stopped before the first product edit and changed no repository path. `memory/builds/dTotalRecall/RUN.md` was already staged by the main loop before this pass, and I left it untouched. The `--brief` verb answered that the brief was already recorded, unchanged.

**The two divergences** (full detail in `why`):
- **(1) S9 and S8, against §4's marker-placement rule and AC8.** Five unanswered Serves literals sit inside a docstring or a triple-quoted string, so neither a marker nor a cause line can answer them. Two of them are in `tools/workflows/review_replay.py` (lines 36 and 205), which AC8 needs listed as kept and not red.
- **(2) S36 and F2, against the `build-method size` ceiling.** `memory/guides/BUILD-METHOD.md` is 30717 of its 30720 bytes, so the two cause-line additions cannot fit.

**What I checked:** read-only `python -c` probes of the unit's own census functions at HEAD, standing in for the record-causes, record-kinds and corpus-ids legs:
- `record_kinds.check_alias_compares`
- `id_grammar.scan_readers` with `_READER_SPLIT_SHAPE`
- a per-literal Serves window walk over `record_kinds.read_code_paths`, with test-named files excepted
- a tokenize pass sorting each unanswered literal as commentable or inside a string
- the S23 home-glob walk over `record_kinds.read_record_kinds`

I also ran:
- `git cat-file` on the blob pins
- an LF-normalized byte count of BUILD-METHOD.md, standing in for the `build-method size` leg's measure

The probe scripts and the list of the 116 unanswered lines are under `C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/` (`probe_s9.py`, `probe_cls.py`, `s9_lines.txt`).

No gate, suite or bar ran. The `gotchas.py --for-diff` checklist did not run, because there is no commit to range over. Every criterion of §6, and every `New arm:` RED-first observation of §7, is still owed once the spec is revised and the unit is dispatched again.
