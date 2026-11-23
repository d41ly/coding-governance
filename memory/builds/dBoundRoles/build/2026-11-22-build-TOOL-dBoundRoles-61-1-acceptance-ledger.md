**Serves:** journal TOOL-dBoundRoles-61

# TOOL-dBoundRoles-61 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on the
worktree before the pass commit at base `1c34ceb59`. The probe was a scratch driver in the run's scratch path that
defined `check_arm`, `PY`, `FX`, `FXK` and `TMP_ROOT`, evaluated the suite's fixture builder and sourced the
`tools/roles/adopt-roles.test.sh#check_role_reads` definition out of the edited suite, and built its fixture, a git
repository holding the roles, loop and playbook-register kits with the roles kit scaffolded by its adopter, under a
short folder of the host temp folder. The helper is unit 53's `check_role_reads`, the name the spec calls
`assert_role_reads` (deviation 533). No gate, suite or bar ran in the pass: arm 45 as the spec's `New arm:` line
declares it, its RED-first observation on a helper reading stdout alone, and the legs the spec's gate line lists are
owed to the main loop at the close. Every departure is in deviation 613.

**Evidences:** TOOL-dBoundRoles-61
- AC1 — `KeyError` — `check_role_reads gov-nosuch input:question` printed a FAIL line naming `gov-nosuch`, `reads slice exit 1` and `KeyError: 'gov-nosuch'`, and returned 1; at the base the same call printed a FAIL naming only `does not read input:question`, its slice exiting 0. With the probe's copy of the helper staged to read stdout alone, its exit branch cut, the call printed ok and returned 0. OWED: arm 45 of `tools/roles/adopt-roles.test.sh` and its RED-first observation on that staging at the close.
- AC2 — `R2` — with the fixture's `gov-orienter.agent.md` holding its `reads:` key indented by one space, `check_role_reads gov-orienter input:question` printed a FAIL line naming `gov-orienter`, `reads slice exit 1` and the `roles_lib.RolesError` line naming `R2`, and returned 1; the file restored, the call printed ok and returned 0. Under the stdout-only staging the indented call printed ok. OWED: as AC1, arm 45's second assertion.
- AC3 — `gov-nosuch` — NOT MET at this pass: a grep for `gov-nosuch` and `exit status` over spec 59 printed only its Edges bullet naming unit 63, its S1 and `### The slice` name no exit status, and its criteria stop at AC4. The rev bump S4 asks for is refused to this role by the scratch-guard hook, which gives the spec class to gov-spec-writer alone; it is owed to a spec-writer pass with unit 59's AC5 ledger answer, whose text the deviation record of this unit holds.
- AC4 — `TOOL-dBoundRoles-61` — `grep -n 'TOOL-dBoundRoles-61' tools/roles/adopt-roles.test.sh` printed the `+2 for arm 45` term of the comment above `FLOOR_ASSERTIONS`, raised from 187 to 189 (pin: `1c34ceb59`), the helper's comment, arm 45's heading, and the call `check_role_reads gov-nosuch input:question` with its AC1 comment.
