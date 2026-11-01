**Serves:** research TOOL-dScopedBuild-43

# Fix brief — dScopedBuild, the round-4 promotions' token reds

The round-4 spec audit's disposal promoted TOOL-dScopedBuild-42 and -43, uncommitted; the owner ended the audit chain
at round 4 (`memory/builds/dScopedBuild/prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-owner-stop-chain.md`), so no
round reads them again and their specs must be right as written. `tools/check-spec-tokens.py` reds four hits, all in
`memory/builds/dScopedBuild/spec/2026-11-01-spec-TOOL-dScopedBuild-43.md`. Fix each in place with its observation
unchanged, and nothing else. The spec has never been committed, so it stays at `rev-1` and owes no §9 line. Read the
spec brief `memory/builds/dScopedBuild/prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md`, section "What
the last spec runs had to fix after their writers returned", before the first edit.

- A criterion's backticked token reads `tools/run-gates/post-merge.sh)`: the closing parenthesis sits inside the
  backticks, so the check reads a path that does not exist. Close the backticks before the parenthesis, or cite the
  file the way the rest of the spec does if it is one a unit creates (basename in §6, full path elsewhere).
- Criteria name `tools/run-gates/run-gates.gov.test.sh`, `tools/unattended/unattended.test.sh` and
  `tools/run-gates/run-gates.sh`, a suite, a suite and the bar, which are not acceptance observations. Observe the
  unit's own function or checker on a staged break or a fixture instead, and move each suite to a `New arm:` line in
  §7 (keep any already there); the bar is the close's, never a criterion.

Return each change by section, then rerun `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` in the
foreground with a timeout of at most 590 seconds and report its verdict on that file. Write nothing outside
`memory/builds/dScopedBuild/spec/`, commit nothing, run no generator.
