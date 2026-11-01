**Serves:** research TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91

# Promoted-fix brief — dLinkedLibrary, the round-6 promotions' check findings

The round-6 spec audit (run `wf_604fec13-e61`, record
`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md`) promoted
`TOOL-dLinkedLibrary-87` to `-91`. The main loop ran `tools/check-spec-tokens.py` and the memory hygiene gate over the
set; the findings below are the whole remainder. Each spec is an uncommitted rev-1 draft under
`memory/builds/dLinkedLibrary/spec/`: edit it in place, with no rev bump and no §9 line. Do not commit, and do not run
the build-index generator.

Read `memory/builds/dLinkedLibrary/prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md` "Every spec" and
"What the last spec runs had to fix" first.

## Hygiene check 25 — a retirement with no `**Readers:**` clause

Each scope item below retires a named thing and carries no `**Readers:**` clause. Write `**Readers:** by name:` and the
readers that spell the name, found by `git grep` over the tree, then `by value:` and the readers of its value, or
`NO VALUE READERS` and a reason, with `NO VALUE READERS` unbroken by a line wrap. A reader a parent build creates is
`READER NOT IN TREE` with the build that lands it. If the item retires nothing, reword it so no retirement word
("drops", "retired", "replaces", "removes") sits beside a backticked token.

1. `2026-10-27-spec-TOOL-dLinkedLibrary-87.md` S3.
2. `2026-10-27-spec-TOOL-dLinkedLibrary-87.md` S4.
3. `2026-10-27-spec-TOOL-dLinkedLibrary-90.md` S1.
4. `2026-10-27-spec-TOOL-dLinkedLibrary-91.md` S22.

## Hygiene check 12 — a criterion naming no backticked witness

5. `2026-10-27-spec-TOOL-dLinkedLibrary-91.md` AC13: name the observation's witness in backticks, the command, file,
   line or output a pass reads.

## check-spec-tokens — the bar named as an observation

6. `2026-10-27-spec-TOOL-dLinkedLibrary-91.md` names `run-gates.sh` in §6. A bar or suite is not an acceptance
   observation: observe the checker on a staged break, a `--selftest` flag or a fixture, or describe the file in words
   where it is only the object a grep reads; a suite arm goes on a `New arm:` line in §7.

Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,25` and confirm none of these files is named. Return
each finding's number with what you changed, by file.
