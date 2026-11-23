**Serves:** journal TOOL-dBoundRoles-59

# TOOL-dBoundRoles-59 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on the
worktree before the pass commit at base `f96fceac5`. The probe cut the suite's prologue, its fixture builder,
`tools/roles/adopt-roles.test.sh#check_role_reads` and the arm 44 block out of the edited suite into the run's
scratch path, set the fixture root to a short folder under the host temp folder, and ran them over a git fixture
repository holding a copy of this tree's roles, loop and playbook-register files with the roles kit scaffolded by its
adopter. The helper is unit 53's `check_role_reads`, the name the spec calls `assert_role_reads` (deviation 533), and
it already folded each entry through `roles_lib.parse_read_key` at the base, so no line of it moved (deviation 593).
No gate, suite or bar ran in the pass: arm 44 as the spec's `New arm:` line declares it, its RED-first observation
on the raw split, and the legs the spec's gate line lists are owed to the main loop at the close.

**Evidences:** TOOL-dBoundRoles-59
- AC1 — `input:question` — with the fixture's installed `gov-orienter.agent.md` holding `reads: field.input.question, field.input.prompt?`, `check_role_reads gov-orienter input:question input:prompt` printed `ok` and returned 0; with the probe's copy of the helper's slice staged back to the raw split that strips a trailing `?`, the same call printed FAIL and `gov-orienter does not read input:question`. OWED: arm 44 of `tools/roles/adopt-roles.test.sh` and its RED-first observation on the raw split at the close.
- AC2 — `input:prompt` — with the line rewritten to `reads: input:question, input:prompt?` the same call printed `ok` and returned 0, and with `field.input.prompt?` cut from the tag-spelled line it returned 1 naming `gov-orienter does not read input:prompt`; the three readings are arm 44's three assertions, the floor raised from 184 to 187 (pin: `f96fceac5`). OWED: as AC1.
- AC3 — `rstrip("?")` — `grep -n 'parse_read_key'` over `tools/roles/adopt-roles.test.sh` named the helper's slice in `tools/roles/adopt-roles.test.sh#check_role_reads` and its comment, beside the other arms that fold through it, and `grep -nF 'rstrip("?")'` over the same file printed nothing and exited 1.
- AC4 — `TOOL-dBoundRoles-59` — `grep -n 'parse_read_key'` over unit 53's spec printed S1, its Readers clause and the §4 Evidence read-set line, the grep for the retired `handoff.py` line citation AC4 names printed nothing, and its revision log's rev-4 entry names `TOOL-dBoundRoles-59` and S1, all at the base, left by that spec's rev-4 reground. The rev-5 bump S4 also asks for was refused to this role by the scratch-guard hook, which gives the spec class to gov-spec-writer alone; it is owed with unit 53's `amended rev-5` ledger answers (deviation 593).
