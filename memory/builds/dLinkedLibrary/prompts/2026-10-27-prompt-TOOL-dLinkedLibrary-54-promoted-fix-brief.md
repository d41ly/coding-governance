**Serves:** research TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20

# Promoted-fix brief — dLinkedLibrary, the round-2 promotions' check findings

The round-2 spec audit (run `wf_29b07019-a49`, record
`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md`) promoted
`TOOL-dLinkedLibrary-54` to `-64`, whose uncommitted rev-1 specs sit under `memory/builds/dLinkedLibrary/spec/`. The
main loop ran `tools/check-spec-tokens.py` and the memory hygiene gate over the set; the findings below are the whole
remainder. Fix each in the file it names and nothing else. The 54 to 64 specs are uncommitted rev-1 drafts: edit them
in place, with no rev bump and no §9 line. Units 16 and 20 are committed at their current revision: their edit is a
rev bump with a §9 line naming hygiene check 13. Do not commit, and do not run the build-index generator.

Read `memory/builds/dLinkedLibrary/prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md` "Every spec" and
"What the last spec runs had to fix" first; each finding below breaks one of its rules.

## check-spec-tokens — paths a criterion names that git does not track

A file this build or a parent will CREATE is cited by its basename in §6 (`python region.py …`), keeping its full path
in §2, §4 and Files touched only. A literal that only looks like a path (an assignment such as `MAP_CLI="…"`, a
`<rev>:<path>` spec, a fixture-relative path such as `pfx/kits/…` or `gov/…`) is reworded so no path-shaped token
appears in §6: describe it, or cite its basename. The hits, by spec:

1. `-54`: `tools/lib/region.sh`, `gov/check-microformats.sh`.
2. `-55`: `5fede642:tools/check-microformats.sh`, `pfx/kits/check-microformats.sh`.
3. `-56`: `tools/lib/region.sh` (twice).
4. `-57`: `tools/govkit/steps/retire_reuse_lookup.py`, `MAP_CLI="tools/codebase-map/reuse_lookup.py"`,
   `MAP_CLI="tools/other/cli.py"`.
5. `-58`: `tools/govkit/steps/retire_reuse_lookup.py` (twice), `MAP_CLI="tools/codebase-map/reuse_lookup.py"`.
6. `-59`: `tools/memory-tree/decision_rubric.py`.
7. `-60`: `tools/memory-tree/reuse_entries.py`.
8. `-62`: `tools/memory-tree/annotations.py`.
9. `-63`: `tools/memory-tree/adopt_program.py`, `help/adopt.md`.
10. `-64`: `tools/memory-tree/annotations.py` (twice), `tools/memory-tree/reuse_entries.py`,
    `tools/playbook/namespaces.toml`, `tools/memory-tree/marker-words.toml`, `tools/codebase-map/dossier_move.py`
    (twice), `tools/memory-tree/adopt_program.py`, `tools/run-gates/leg_factory.py`, `tools/lib/region.py` (three
    times), `help/annotations.md`.

## check-spec-tokens — a suite named as an acceptance observation

11. `-56` names `tools/run-gates/run-gates.test.sh` as an observation. A bar or suite is not an acceptance
    observation: observe the checker on a staged break, a `--selftest` flag or a fixture, and name the suite on a
    `New arm:` line in §7, which the main loop observes at the close.

## Hygiene check 25 — a retirement with no `**Readers:**` clause

Each scope item below retires a named thing and carries no `**Readers:**` clause. Write `**Readers:** by name:` and the
readers that spell the name, found by `git grep` over the tree, then `by value:` and the readers of its value, or
`NO VALUE READERS` and a reason, all on the clause's own lines with `NO VALUE READERS` unbroken by a line wrap. A
reader a parent build creates is `READER NOT IN TREE` with the build that lands it. If the item retires nothing,
reword it so no retirement word ("drops", "retired", "replaces", "removes") sits beside a backticked token.

12. `-58` S1.
13. `-59` S1.
14. `-64` S19.

## Hygiene check 13 — a foreign id leading a table cell

A foreign id as the first token of a table cell is read as DEFINING that id in this build's folder. Move it out of
the cell's first position (for example "the two S2 derives of TOOL-dRedressedBar-24"), keeping the citation.

15. `2026-10-26-spec-TOOL-dLinkedLibrary-16.md` line 130: a cell opening `TOOL-dRedressedBar-24`.
16. `2026-10-26-spec-TOOL-dLinkedLibrary-20.md` lines 134 and 135: two cells opening `PLAY-dOrderedCharter-10 S4`.

## Then

Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,25` and confirm none of these files is named, and
re-run the hand-off and §3 reciprocity joins over the edges you touched. Return each finding's number with what you
changed, by file.
