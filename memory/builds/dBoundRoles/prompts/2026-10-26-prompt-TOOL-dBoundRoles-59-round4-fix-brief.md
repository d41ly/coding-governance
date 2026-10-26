**Serves:** research TOOL-dBoundRoles-59 TOOL-dBoundRoles-60

# Round-4 fix brief — dBoundRoles, the reds on round 4's promotions before their commit

The round-4 spec audit (`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md`)
promoted its findings into TOOL-dBoundRoles-59 and -60 and folded hands-off edges into earlier specs; nothing is
committed. `python tools/check-spec-tokens.py` printed three reds, all on
`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md`. Fix each there and nothing else; the spec
stays `rev-1`. The spec brief `memory/builds/dBoundRoles/prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md`
still binds.

## N1 · `tools/govkit/selftest.py'` is read as a path with a trailing quote

A criterion spells `tools/govkit/selftest.py` followed by a quote character inside one code span, so the token is not
a tracked path. Rewrite the criterion so the code span holds the path alone, or name the module in prose (the form
units 49 and 50 use: "govkit's self-test module").

## N2 · `other/house/gov-builder.md` is not a tracked path

If it is a fixture path inside a scratch tree, describe the plant without a path shape (the form unit 21 uses for its
`default` role plant); if it means a real file, spell its tracked path.

## N3 · a suite inside a criterion (`[bar]`)

`tools/memory-recall/selftest.py` is named inside a criterion. Observe the unit's own checker on a staged break, a
`--selftest` flag of its own tool or a one-case slice of the module's function instead, and keep the suite on a
`New arm:` line in §7.

## Return

One line per N-item saying what you changed. Commit nothing; run the build-index generator only in a throwaway clone.
