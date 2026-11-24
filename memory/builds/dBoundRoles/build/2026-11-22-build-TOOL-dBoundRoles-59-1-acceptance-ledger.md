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
- AC4 — `parse_read_key` — AMENDED by `TOOL-dBoundRoles-63`, its text restated in `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-63-deviation-633.md`: a probe over spec 53 found it in S1 through the Readers clause, in the section 4 Evidence bullet citing the read set and in section 10, and no spelling of the retired `handoff.py` line citation in S1 or on the `**Readers:**` line. As this unit's pass read it: `grep -n 'parse_read_key'` over unit 53's spec printed S1, its Readers clause and the section 4 Evidence read-set line, the grep for the retired citation printed nothing, and its revision log's rev-4 entry names `TOOL-dBoundRoles-59` and S1, all at the base, left by that spec's rev-4 reground. Nothing is owed on unit 53's ledger, whose AC1 and AC2 stay OBSERVED (`TOOL-dBoundRoles-63` S14), in place of the bump and the answers deviation 593 left owed.

## The missing slot's criterion, AC5, added on top by TOOL-dBoundRoles-61 and TOOL-dBoundRoles-63

`TOOL-dBoundRoles-61` S4 gives this unit the missing-slot criterion, and `TOOL-dBoundRoles-63`'s deviation record
`memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-63-deviation-633.md` holds the text. This unit's
spec is CLOSED and frozen and numbers no AC5, and the acceptance-ledger check refuses a label its spec does not number,
so the answer stands under this heading rather than in the block above.

OBSERVED: `check_role_reads gov-nosuch input:question`, cut out of the suite into a scratch driver over this tree's
roles kit at `012cdf887`, printed a FAIL line naming `gov-nosuch`, `reads slice exit 1` and `KeyError` and returned 1;
over the roles adopter fixture, with the helper staged to read stdout alone, unit 61's pass read the same call ok
(deviation 613).
