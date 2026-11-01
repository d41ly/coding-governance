**Serves:** research TOOL-dBoundRoles-65 TOOL-dBoundRoles-66

# Round-7 fix brief — dBoundRoles, the reds on round 7's promotions before their commit

The round-7 spec audit (`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-64-spec-audit-round1.md`)
promoted its findings into TOOL-dBoundRoles-65 and -66 and folded hands-off edges into earlier specs; nothing is
committed. `python tools/check-spec-tokens.py` printed seven reds, all on
`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-66.md`. Fix them there and nothing else; the spec
stays `rev-1`. The spec brief `memory/builds/dBoundRoles/prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md`
still binds.

## K1 · suites inside criteria (`[path]` and `[bar]`)

Unit 66's criteria name `tools/roles/spawn-guard.test.sh` (three times; TOOL-dBoundRoles-25 creates it, so git does
not track it yet) and `tools/roles/adopt-roles.test.sh` (once). A suite is never itself an acceptance observation.
Rewrite each criterion to observe the unit's own checker on a staged break, a `--selftest` flag of its own tool, or
a one-case slice of the module's function; where a criterion must refer to a suite, name it in prose ("the
spawn-guard suite unit 25 adds", "the roles adopter suite"), the form units 62 and 64 use. Keep each suite on a
`New arm:` line in §7 and its full path in §2, §4 and Files touched.

## Return

The criteria you changed, one line each. Commit nothing; run the build-index generator only in a throwaway clone.
