**Serves:** research TOOL-dLinkedLibrary-86

# Promoted-fix brief — dLinkedLibrary, the round-5 minors batch's check findings

The round-5 spec audit (run `wf_2014ef68-a8c`, record
`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md`) promoted
`TOOL-dLinkedLibrary-81` to `-86`. The main loop ran `tools/check-spec-tokens.py` and the memory hygiene gate over the
set; the findings below are the whole remainder, all in one file,
`memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md`, an uncommitted rev-1 draft: edit it in
place, with no rev bump and no §9 line. Do not commit, and do not run the build-index generator.

Read `memory/builds/dLinkedLibrary/prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md` "Every spec" and
"What the last spec runs had to fix" first.

1. **Hygiene check 12 — AC7 names no backticked witness.** Each acceptance bullet names the observation's witness in
   backticks: the command, file, line or output a pass reads. Give AC7 its witness.
2. **Hygiene check 25 — S19 retires a named thing and carries no `**Readers:**` clause.** Write `**Readers:** by
   name:` and the readers that spell the name, found by `git grep` over the tree, then `by value:` and the readers of
   its value, or `NO VALUE READERS` and a reason, with `NO VALUE READERS` unbroken by a line wrap. A reader a parent
   build creates is `READER NOT IN TREE` with the build that lands it. If the item retires nothing, reword it so no
   retirement word ("drops", "retired", "replaces", "removes") sits beside a backticked token.
3. **Hygiene check 25 — S20**, the same.
4. **check-spec-tokens — `/usr/local/bin/python3.12` is a path git does not track.** Describe the interpreter path
   in words or cite it without its directory, so no path-shaped token appears in §6.

Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,25` and confirm the file is not named. Return each
finding's number with what you changed.
