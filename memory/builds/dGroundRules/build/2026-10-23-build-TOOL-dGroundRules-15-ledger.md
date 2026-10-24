# TOOL-dGroundRules-15 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-15

No merge bar, gate leg or self-test suite ran in this pass. Each criterion was observed before the
commit, with this unit's edit in the worktree: the two new cases and unit 10's three conf cases,
`limit-settings-render` and `limit-hook-admits-eight` through the kit's own fixture CLI, one case per
run, each in its own repository under the system temp directory, and AC4 through a probe that built
the same fixture repository and ran the settings verb in it. The naming lexicon, the one leg the
builder role may run, printed `lexicon OK` with the verb offenders at 1204, unchanged. In this
repository `python tools/policy/policy.py mirror --check` printed "policy: mirror fresh": gov has no
`.agent-cap.conf`, so no mirror value moves and `.governance/policy.json` is not re-rendered. The New
arm's RED-first observation is the close's.

**Evidences:** TOOL-dGroundRules-15
- AC1 — `grep -n "read_legacy_fanout(" policy.py` — run in `tools/policy/`, printed two lines: the definition `def read_legacy_fanout(repo, rev):` and one call, `read["legacy_fanout"] = read_legacy_fanout(read["repo"], read["sha"])`, inside `derive_lowered_limit`. `grep -n "derive_lowered_limit(" policy.py` printed the definition and one call, `return derive_lowered_limit(hit, read) if path == AGENTS_PATH else hit`, the last line of `resolve_read`. `resolve` holds no lowering: it returns `resolve_read` over its read.
- AC2 — `python check_policy.py --fixture limit-conf-mirror` — exit 0, 2 assertions, 0 wrong: with `FANOUT_CAP=2` committed in `.agent-cap.conf`, no policy file and the mirror rendered and committed, `python policy.py get runtime.agents-in-flight --explain` printed `2` with "lowered to 2 by FANOUT_CAP at .agent-cap.conf:1", and `node policy-mirror.js get runtime.agents-in-flight --explain` printed `2` with source `default` and the reason the fresh mirror recorded, "... at <L8>, the landed revision; the catalogue default; lowered to 2 by FANOUT_CAP at .agent-cap.conf:1", no `mirror absent at` or `mirror stale at` fallback.
- AC3 — `python check_policy.py --fixture limit-conf-last-valid` — exit 0, 2 assertions, 0 wrong: after a valid policy file setting 6, `FANOUT_CAP=3` and a malformed policy file, `policy.py get runtime.agents-in-flight --explain` printed `3` with source `last-valid` and a reason ending "read from the last valid revision <sha8>: set in .governance/policy.toml at <sha8>, walked back from <sha8>, local main: this clone has no remote; lowered to 3 by FANOUT_CAP at .agent-cap.conf:1"; the helper over the mirror rendered at that malformed revision printed `3`, source `last-valid`, from the mirror.
- AC4 — `python policy.py settings --check` — over a scratch repository whose conf sets `FANOUT_CAP=2`, `settings --write` printed "policy: settings written · .claude/settings.json · both variables at 2", then `settings --check` exited 0 printing "policy: settings fresh · .claude/settings.json", and both `env` keys, `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` and `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`, held `"2"`.

Owed at the close, observed by no command in this pass:

- The `New arm:` line of §7, `--fixture limit-conf-mirror limit-conf-last-valid`, RED with the lowering staged back into the `resolve` wrapper and GREEN restored.
- The §7 legs over the built tree, `policy fixtures` among them, which now runs the two new cases and `limit-conf-malformed`'s added `mirror --print` refusal.
