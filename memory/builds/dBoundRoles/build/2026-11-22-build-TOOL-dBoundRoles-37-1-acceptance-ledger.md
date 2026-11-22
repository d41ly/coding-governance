**Serves:** journal TOOL-dBoundRoles-37

# TOOL-dBoundRoles-37 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on the
worktree before the pass commit: `tools/govkit/selftest.py#derive_roles_expected`, imported as a library by
`python -c`, which runs no case. No gate, suite or bar ran in the pass: the one `New arm:` arm of section 7 and
its RED-first observation, and the section 7 legs, are owed to the main loop at the close.

**Evidences:** TOOL-dBoundRoles-37
- AC1 — `derive_roles_expected` — the AC1 `python -c` over gov's tree printed `agents 12 True overlays 13 True` (DERIVED, the probe): the first set equals the slots `.claude/roles.json` marks `agent` true, `gov-session` absent, and the second the `house/*.md` entries of `tools/roles/kit.toml`'s seed row, `house/policy.toml` excluded.
- AC2 — `agent: true` — the same probe over a scratch copy of `tools/roles/` under the run's scratchpad carrying `agents/gov-zprobe.agent.md` with `agent: true` printed `gained ['gov-zprobe'] lost []`, the overlay set unmoved; the same file at `agent: false` gained nothing. OWED: the section 7 arm, the OC8 AC4 roles install case staged by removing one rendered `gov-*.md`, RED first, at the close.
- AC3 — `len\(agents\) == [0-9]` — the AC3 `grep -nE` over `tools/govkit/selftest.py` printed nothing, exit 1. OWED: the `govkit selftest` leg's OC8 AC4 checks over the built tree at the close.
