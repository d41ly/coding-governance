**Serves:** research TOOL-dBoundRoles-64 TOOL-dBoundRoles-42

# Round-6 fix brief — dBoundRoles, the reds on round 6's promotion before its commit

The round-6 spec audit (`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-61-spec-audit-round1.md`)
promoted its findings into TOOL-dBoundRoles-64 and folded hands-off edges into earlier specs; nothing is committed.
Two reds remain. Fix each in the spec it names and nothing else. The spec brief
`memory/builds/dBoundRoles/prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md` still binds.

## L1 · a suite inside unit 64's criteria (`check-spec-tokens.py` `[path]` and `[bar]`)

`2026-10-26-spec-TOOL-dBoundRoles-64.md` names `tools/roles/adopt-roles.test.sh` inside criteria, once as the
revision-qualified token `462d20f3:tools/roles/adopt-roles.test.sh`, which reads as an untracked path. Observe the
unit's own checker, a fixture or a one-case slice instead (name the suite in prose if a criterion must refer to it),
and keep the suite on a `New arm:` line in §7. Unit 64 stays `rev-1`.

## L2 · unit 42's index row over its cap (hygiene check 7)

The README's generated unit index renders each spec's H1 into one row, capped at 350 characters; unit 42's row is
368 now that this round's fold moved its header. Shorten
`2026-10-26-spec-TOOL-dBoundRoles-42.md`'s H1 (em dash form kept) by at least 25 characters, keeping its meaning,
and note it on that spec's pending §9 line for this round; no new rev.

## Return

One line per L-item saying what you changed. Commit nothing; run the build-index generator only in a throwaway clone.
