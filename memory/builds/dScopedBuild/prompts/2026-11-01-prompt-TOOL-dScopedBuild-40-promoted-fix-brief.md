**Serves:** research TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41

# Fix brief — dScopedBuild, the round-3 promotions' token reds

The round-3 spec audit's disposal promoted TOOL-dScopedBuild-40 and -41 and folded their hands-off edges into earlier
units, all uncommitted. `tools/check-spec-tokens.py` reds the seven hits below, each in exactly the spec it names.
Fix each in place with its observation unchanged, and nothing else. The two promoted specs have never been committed,
so a fix there stays at `rev-1` and owes no §9 line; TOOL-dScopedBuild-39 is committed at rev-1, so a fix there takes
the rev the disposal's fold gave it (bump to rev-2 with a §9 line if the fold left it at rev-1). Read the spec brief
`memory/builds/dScopedBuild/prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md`, section "What the last
spec runs had to fix after their writers returned", before the first edit.

- TOOL-dScopedBuild-40: criteria cite `packages/README.md`, `["docs/api.md"]` and `src/core/x.py`, planted fixture
  paths no repository tracks. Spell each as the fixture tree's relative path described in words, or pass it as an
  argument, so the check does not read it as a citation.
- TOOL-dScopedBuild-41: criteria cite `/BACKLOG.md` (a fixture path), `tools/codebase-map/reuse_check.py` (which unit
  12 creates) and `memory-tree/policy_value.py` (a parent's, not at HEAD). Spell the fixture path in words; cite each
  file a unit or a parent creates by its basename in §6 and keep its full path in §2, §4 and Files touched.
- TOOL-dScopedBuild-39 hands `build_fixture(..., checkout=True)` to TOOL-dScopedBuild-41, whose spec never names that
  token. Name it in unit 41 where it consumes it, in its §3 `consumes-from` line from unit 39, or correct unit 39's
  bullet to the token unit 41 already carries.

Return each change by spec and section, then rerun `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`
and report its verdict on these files. Write nothing outside `memory/builds/dScopedBuild/spec/`, commit nothing, run
no generator. Run the hygiene check in the foreground with a timeout of at most 590 seconds.
