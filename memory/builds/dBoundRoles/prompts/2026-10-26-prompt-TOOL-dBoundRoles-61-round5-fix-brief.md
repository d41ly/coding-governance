**Serves:** research TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63

# Round-5 fix brief — dBoundRoles, the reds on round 5's promotions before their commit

The round-5 spec audit (`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-59-spec-audit-round1.md`)
promoted its findings into TOOL-dBoundRoles-61 to -63 and folded hands-off edges into earlier specs; nothing is
committed. Two reds remain. Fix each in the spec it names and nothing else; each stays `rev-1`. The spec brief
`memory/builds/dBoundRoles/prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md` still binds.

## M1 · a path no file holds yet (`check-spec-tokens.py` `[path]`)

`2026-10-26-spec-TOOL-dBoundRoles-62.md` names `tools/roles/spawn-guard.test.sh` inside criteria, once with a
trailing quote inside the code span. TOOL-dBoundRoles-25 creates that suite, so git does not track it yet, and a suite
is never itself an acceptance observation. Name it in §6 only in prose ("the spawn-guard suite unit 25 adds") or move
it to a `New arm:` line in §7, observe the unit's own checker or a fixture instead, and keep the full path in §2, §4
and Files touched.

## M2 · a Readers clause with neither half (hygiene check 25)

`2026-10-26-spec-TOOL-dBoundRoles-63.md` §2 S16 carries a `**Readers:**` clause with no `by name:` half and no
`by value:` half. Write both: `by name:` and every reader spelling the retired name (found by `git grep`), or
`READER NOT IN TREE` and a reason; then `by value:` and the readers of its value, or `NO VALUE READERS` and a reason.

## Return

One line per M-item saying what you changed. Commit nothing; run the build-index generator only in a throwaway clone.
