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
- AC1 — `KeyError` — AMENDED by `TOOL-dBoundRoles-64`, its text restated in `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-64-deviation-643.md`: the driver also defines `$TMP_ROOT`, a scratch directory, as this unit's did. `check_role_reads gov-nosuch input:question` printed a FAIL line naming `gov-nosuch`, `reads slice exit 1` and `KeyError: 'gov-nosuch'`, and returned 1; at the base the same call printed a FAIL naming only `does not read input:question`, its slice exiting 0. With the probe's copy of the helper staged to read stdout alone, its exit branch cut, the call printed ok and returned 0. OWED: arm 45 of `tools/roles/adopt-roles.test.sh` and its RED-first observation on that staging at the close.
- AC2 — `R2` — with the fixture's `gov-orienter.agent.md` holding its `reads:` key indented by one space, `check_role_reads gov-orienter input:question` printed a FAIL line naming `gov-orienter`, `reads slice exit 1` and the `roles_lib.RolesError` line naming `R2`, and returned 1; the file restored, the call printed ok and returned 0. Under the stdout-only staging the indented call printed ok. OWED: as AC1, arm 45's second assertion.
- AC3 — `gov-nosuch` — AMENDED by `TOOL-dBoundRoles-63`, its text restated in `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-63-deviation-633.md`, by the main loop's decision, item 4: spec 59 is frozen, and that record's text for `TOOL-dBoundRoles-59@rev-3` names the exit status in S1 and "The slice" in one sentence, gives its section 6 an AC5 naming the token and counts itself as the revision-log line naming `TOOL-dBoundRoles-61`; unit 59's ledger answers AC5 under a heading of its own. This unit's pass read it NOT MET, no text of that kind standing then.
- AC4 — `TOOL-dBoundRoles-61` — AMENDED by `TOOL-dBoundRoles-64`, its text restated in `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-64-deviation-643.md`: the call is read by `grep -n 'gov-nosuch'`, which prints it inside a `$(` capture on the built tree, and this token is read for the term, `+2` for the two outer `check_arm` calls. `grep -n 'TOOL-dBoundRoles-61' tools/roles/adopt-roles.test.sh` printed the `+2 for arm 45` term of the comment above `FLOOR_ASSERTIONS`, raised from 187 to 189 (pin: `1c34ceb59`), the helper's comment, arm 45's heading, and the call `check_role_reads gov-nosuch input:question` with its AC1 comment.
