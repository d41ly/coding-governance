**Serves:** research TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43

# Round-1 fix brief — dTotalRecall, the checks the round-1 promotions and folds owe before their commit

The round-1 spec audit's disposal (`unattended-build.js` run `wf_a94908c7-6d6`) wrote the promoted specs
TOOL-dTotalRecall-36 to -43 under `memory/builds/dTotalRecall/spec/` and folded each hands-off edge into the roster
spec it names as rev-2. Nothing of it is committed yet. Clear every finding below over those files, changing nothing
else in any spec's design, so that the main loop's `python tools/check-spec-tokens.py` run prints no dTotalRecall
hit and `bash tools/memory-tree/check-memory-hygiene.sh --only 2,5,12,21,25` prints no FAILED line naming a
dTotalRecall file.

- Units 36 to 43 are uncommitted at rev-1 and unaudited: edit them in place with no rev bump. The roster specs the
  disposal folded are uncommitted at rev-2: edit them in place at rev-2, extending that rev's §9 line.
- Your role admits the hygiene gate and the lexicon only. The files are staged in this worktree, so run the hygiene
  gate in place. Do not commit and do not run the build-index generator.

## F1 · the review record was renamed

The main loop renamed the round-1 record to the recording grammar of hygiene check 5:
`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md`. Re-point every
citation of the old name `2026-10-26-review-dTotalRecall-spec-audit-round1.md` in the specs to the new one.

## F2 · paths in acceptance criteria that do not exist at HEAD

`tools/check-spec-tokens.py` reds a path a criterion names that is not tracked at HEAD. In §6 cite a file this build
or a parent will CREATE by its basename (`record_kinds.py`, `gov_record.py`, `record_causes.py`, `code_record.py`,
`id_grammar.py`, `edge_grammar.py`, `gov_map.py`, `gen_atlas.py`, `extract_code.py`, `memory_front_matter.py`,
`record-kinds.toml`) and keep the full path in §2, §4 and Files touched. A fixture's example path inside a criterion
(`memory/notes/2026-10-26-x.md`, `/c/projects/<clone>/memory/x.md`, `/d/other/memory/x.md`,
`memory/builds/tX/build/2026-10-26-build-X-a-1-shape-run-1.md`,
`memory/builds/<slug>/build/<date>-build-<id>-deviation-1.md`) is spelled so the token arm does not read it as a
tracked path: name it in prose ("a note file under the fixture's `memory/notes/`", "a shape-run record in the fixture
build's folder") or pass it as an argument rather than inside a backticked path literal. The hits are in units 36,
37, 38, 39, 40, 42 and 43.

## F3 · guarded legs missing from §7

Units 36, 37, 38, 40, 41 and 42 name `tools/codebase-map/gen_map.py` in §4 Files touched, which trips the guards of
`codebase-map kit selftest`, `codebase-map gate coverage` and `codebase-map adopter e2e`. Add the three legs to each
one's §7 leg line.

## F4 · unit 43 is over the size ceiling

TOOL-dTotalRecall-43 is 51940 bytes against the 49152 spec ceiling (`tools/template-size-limits.txt`). Trim its
non-criterion text (tables restating the record, repeated rationale, the Files touched layout) to under 49152 bytes.
Do not split it: M4 admits two minors units only over disjoint write sets. Every acceptance criterion and every
finding id it closes stays.

## F5 · three deviations' After, so the clause pins hold

The as-built view renders a clause deviation's **After** in place of the clause text, so a fragment After drops most
of the clause from the view. Deviations 21, 81 and 231
(`memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md`, `-8-deviation-81.md`,
`-23-deviation-231.md`) each restate their WHOLE clause as **After**, the clause's text from the packet's Items with
only the departed words changed, keeping each record's grammar. The main loop then re-renders the view and re-pins
units 2, 8 and 23's `**Carries:**` lines to the hashes the view gives; do not edit those pins yourself.

## Return

The list of files you edited, one line each on what changed, the size of unit 43, and the last line of the hygiene
gate run.
