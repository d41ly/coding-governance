**Serves:** research TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20

# The round-2 promoted-fix pass's return — dLinkedLibrary

The spec writer's final return, extracted from its transcript by script, never retyped.

All 16 findings are fixed, and none of the files is named any more by `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,25`. The run still exits 1 because of one red that isn't mine (below). I didn't run `check-spec-tokens.py`, because my role allows only the hygiene gate and the lexicon. Instead I ran its path rule and its suite-name pattern, copied from the tool, over the acceptance criteria of all 12 files: nothing hit, and every file is under 49152 bytes. Nothing is committed and the build index was not regenerated.

Each spec below is under `memory/builds/dLinkedLibrary/spec/`.

**Paths in acceptance criteria (1 to 10).** Each file a build creates is now cited in §6 by its basename, and its full path is still in §2, §4 or Files touched. Literals that only look like paths are described in words instead.
1. `2026-10-27-spec-TOOL-dLinkedLibrary-54.md`: AC2 cites the lib's `region.sh` (full path in S1). AC3 and AC4 describe the copy at the `gov/` prefix being run by `bash` from the repository root, with `AGENTS.md` as its argument.
2. `2026-10-27-spec-TOOL-dLinkedLibrary-55.md`: AC1 describes the gate's bytes at base `5fede642` (`git show` of `check-microformats.sh`) copied into the prefix `pfx/kits` and run with `charter.md`. I also put the inserted `. "$(dirname "$0")/lib/region.sh"` line back on one line.
3. `2026-10-27-spec-TOOL-dLinkedLibrary-56.md`: AC1 and AC2 cite the lib's `region.sh` (S1).
4. `2026-10-27-spec-TOOL-dLinkedLibrary-57.md`: AC1 is now `python retire_reuse_lookup.py up <target>`. AC2 is now "a `MAP_CLI` line naming the map kit's `reuse_lookup.py` by its repository path". AC3 is now "naming another kit's `cli.py` under `tools/other`".
5. `2026-10-27-spec-TOOL-dLinkedLibrary-58.md`: AC1 and AC3 use `retire_reuse_lookup.py` (AC3 greps "over the step program", path in Files touched). AC2 is worded as in item 4.
6. `2026-10-27-spec-TOOL-dLinkedLibrary-59.md`: AC1 and AC2 are now `python decision_rubric.py …`.
7. `2026-10-27-spec-TOOL-dLinkedLibrary-60.md`: AC1 is now `python reuse_entries.py …`.
8. `2026-10-27-spec-TOOL-dLinkedLibrary-62.md`: AC1 is now `python annotations.py --selftest`.
9. `2026-10-27-spec-TOOL-dLinkedLibrary-63.md`: AC1 is now `python adopt_program.py …`, and AC5 greps "the help page `adopt.md`". I also put the `adopt census` token, which a line wrap had split, back on one line.
10. `2026-10-27-spec-TOOL-dLinkedLibrary-64.md`:
    - AC1, AC2, AC6, AC7, AC11 and AC13 use basenames for `annotations.py`, `reuse_entries.py`, `dossier_move.py`, `adopt_program.py` and `region.py`.
    - AC4 greps the playbook kit's `namespaces.toml` and the memory-tree kit's `marker-words.toml`; S5 still holds both full paths.
    - AC8 reads `python leg_factory.py --check` "run in `tools/run-gates`", as units 46 and 47 already write it. `leg_factory.py` had no full path anywhere else in the spec, so I added an "S10, S11" evidence line in §4. It cites the factory's own spec, TOOL-dWitnessedBar-11 S2, which I read to confirm what `--check` does.
    - AC10 cites "the lib canonical `region.py`", and AC17 cites "the help page `annotations.md`".

**Suite named as an observation (11).**
11. `-56`: AC2 now says "two files: the lib's `region.sh` and the run-gates canary, the file S3 names". §7 gains a second `New arm:` line for `tools/run-gates/run-gates.test.sh`. It covers AC3, the moved `mempause_sh` slice of section 11g, and stages its failing case with the inline block removed so AC14's value check goes red. The floor is unchanged.

**Hygiene check 25, retirements (12 to 14).**
12. `-58` S1 retires nothing of its own, so I reworded it: `up` "takes out the two lookup files exactly as unit 3's S6 states, whose S1 answers for their readers". Unit 3's S1 does carry the full `**Readers:**` clause for those files.
13. `-59` S1 retires nothing either, so I reworded it. It now reads the lines the diff "marks as present at base and absent now", and the class is "any other line of that set", so "removed" is gone.
14. `-64` S19 now has a `**Readers:**` clause:
    - **by name:** `tools/codebase-map/kit.toml` is the only tracked file outside the build records that spells the comment block (git grep prints lines 51, 53 and 54 only). The files the block names keep the readers that TOOL-dLinkedLibrary-3 S1 and TOOL-dLinkedLibrary-52 S41 answer for.
    - **by value:** `NO VALUE READERS`, unbroken, because the block is a TOML comment that the TOML reader discards.

**Hygiene check 13, foreign ids leading table cells (15, 16).** Both specs are bumped as the brief asked. Neither bump has a deviation record, because the brief asked only for a rev bump and a §9 line.
15. `2026-10-26-spec-TOOL-dLinkedLibrary-16.md`: the cell now reads "the research's unit, TOOL-dRedressedBar-24, and its two S2 derives". The header goes to rev-3 · 2026-10-27, and a §9 rev-3 line names §4 and hygiene check 13.
16. `2026-10-26-spec-TOOL-dLinkedLibrary-20.md`: the cells now read "the cited-but-undeclared arm of PLAY-dOrderedCharter-10 S4" and "the dead-selector arm of PLAY-dOrderedCharter-10 S4". The header goes to rev-2 · 2026-10-27, with a matching §9 rev-2 line.

**Joins.** I edited no `### Edges` block. Check 12 is green for every file. I also re-ran the hand-off and §3 reciprocity join by script over every edge that touches these 12 units: there are no one-sided edges, and every hand-off token is present in both specs. It found one older mismatch that I didn't change: unit 20's consumes-from line to unit 19 names `feature-selects`, which is unit 20's own fixture name and doesn't appear in unit 19. Check 12 doesn't flag it.

**The red that isn't mine.** The hygiene run's exit 1 comes from check 15 rule 1: `memory/builds/dLinkedLibrary/BACKLOG.md:6` cites `memory/map/conventions`, which resolves to nothing and has no row in `memory/project/corpus-path-unresolved.txt`. That file is outside what I was handed, so I left it.
