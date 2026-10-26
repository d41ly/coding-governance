**Serves:** research TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-55 TOOL-dBoundRoles-58

# Round-3 fix brief — dBoundRoles, the reds on round 3's promotions before their commit

The round-3 spec audit (`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md`)
promoted its findings into TOOL-dBoundRoles-52 to -58 and folded hands-off edges into earlier specs; nothing is
committed. `bash tools/memory-tree/check-memory-hygiene.sh` printed the hygiene check 25 reds below. Fix each in the
spec it names and nothing else; a promoted spec stays `rev-1`. The spec brief
`memory/builds/dBoundRoles/prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md` still binds.

## P1 · retirements with no Readers clause

TOOL-dBoundRoles-53 §2 S1, TOOL-dBoundRoles-55 §2 S2 and TOOL-dBoundRoles-58 §2 S21 and S30 retire a named thing
and carry no `**Readers:**` clause. Write each: `**Readers:**`, then `by name:` and every reader spelling the name,
then `by value:` and the readers of its value, or `NO VALUE READERS` and a reason, each found by `git grep` over the
tree.

## P2 · a Readers clause naming a unit id as a reader

TOOL-dBoundRoles-58 §2 S19's `by name:` lists `TOOL-dBoundRoles-39`, which no tracked file spells as a reader. Name
the reader file that spells the retired name (a spec is a file: cite its path if unit 39's spec is the reader), or
write `READER NOT IN TREE` and a reason on that half.

## Return

The files you changed, one line each with the P-items taken. Commit nothing; run the build-index generator only in a
throwaway clone, where you may also run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`.
