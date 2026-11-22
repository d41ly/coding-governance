# TOOL-dBoundRoles-2 red-fix 2 — shell hygiene (a loop fed by a command substitution) fixed in be10c468

**Serves:** red-fix TOOL-dBoundRoles-2

- **Leg:** shell hygiene (a loop fed by a command substitution)
- **Red line:** tools/roles/adopt-roles.test.sh: a loop is fed by <<< holding a command substitution, and no registry row declares it (1 site(s))
- **Files:** .claude/agents/gov-skeptic.md, tools/roles/adopt-roles.test.sh, tools/roles/agents/gov-skeptic.agent.md, tools/roles/role-schema.toml
- **Commit:** be10c4680ceff2acb8e0bfdf25e83e8fd0e9c788
- **Rerun:** bash tools/run-gates/pass-legs.sh --base 85a3f6e4f6c8776d31adb07a40bf762faff2a44b
- **Caused-by:** TOOL-dBoundRoles-2
