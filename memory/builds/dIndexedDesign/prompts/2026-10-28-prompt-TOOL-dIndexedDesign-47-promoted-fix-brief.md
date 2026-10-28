**Serves:** research TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53

# Fix brief — dIndexedDesign, the round-3 promotions' check findings before their commit

The round-3 spec audit of `unattended-build.js` run `wf_a12af1e5-c85` (record
`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md`) promoted its
findings into seven new specs, `TOOL-dIndexedDesign-47` to `-53`. The main loop ran the memory hygiene gate and
`tools/check-spec-tokens.py` over the staged set, and the findings below are the whole remainder. Your handoff names
the one unit you may write: fix only that unit's findings, in its file, and nothing else. The promoted specs are
uncommitted rev-1 drafts: edit them in place, with no rev bump and no §9 line. Do not commit and do not run the
build-index generator.

Read `memory/builds/dIndexedDesign/prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md` "Every spec" and
"What the last spec runs had to fix" first; each finding below breaks one of its rules.

## TOOL-dIndexedDesign-47

1. `check-spec-tokens.py` reads `tools/unattended/unattended.test.sh` in an acceptance criterion as a suite named as an
   observation. A criterion observes the unit's own code on a planted case; a probe that greps the suite's lines is
   allowed only where the file is an argument the probe reads, not a suite the criterion runs — restate the criterion
   so it names the checker or probe it runs, and keep any suite arm on a `New arm:` line in §7.
2. Hygiene check 25: scope item S1 retires a named thing and carries no `**Readers:**` clause. Write one: `**Readers:**`,
   `by name:` and every reader that spells the name, `by value:` and every reader of its value or `NO VALUE READERS`
   with the reason, each found by `git grep` and cited by path in backticks; `READER NOT IN TREE` where the thing is
   not at HEAD.

## TOOL-dIndexedDesign-49

3. `check-spec-tokens.py` reads `unattended.test.sh` in an acceptance criterion (near line 129) as a suite named as an
   observation. Restate it as finding 1 says.

## TOOL-dIndexedDesign-52

4. Hygiene check 12: the spec carries an unfilled skeleton placeholder (a template placeholder left as written, such as
   an angle-bracketed template instruction or `TBD`). Find it, and fill or delete it.

## TOOL-dIndexedDesign-53

5. §6 cites `tools/memory-tree/build_records.py`, which does not exist at HEAD. In §6 cite it by its basename and keep
   the full path in §2, §4 and Files touched.
6. Hygiene check 25: scope item S19 retires a named thing and carries no `**Readers:**` clause; write one as finding 2
   says.
7. Hygiene check 25: S10's `by name:` lists `check_meet_path`, which no reader spells and no tracked path is. Name a
   reader that spells it, or write `READER NOT IN TREE` with the reason.

When done, run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` against a private copy of the git
index in your scratch path, and return each finding fixed, by number, with the file and the change.
