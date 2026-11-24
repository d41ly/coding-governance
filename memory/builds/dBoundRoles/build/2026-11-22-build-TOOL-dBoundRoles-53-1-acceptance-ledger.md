**Serves:** journal TOOL-dBoundRoles-53

# TOOL-dBoundRoles-53 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on the
worktree before the pass commit at base `0b9e62f92`. The probes ran `tools/roles/adopt-roles.test.sh#check_role_reads`
and the case block of arm 42, each cut out of the edited suite by `sed` into the run's scratch path and sourced by a
driver beside `check_arm`, with `build_fixture` stubbed to move the previous run's build folder aside, over a git
fixture repository under the host temp folder, short-pathed, holding a copy of this tree's roles, loop and
playbook-register files with the roles kit scaffolded by its adopter. No gate, suite or bar ran in the pass: arm 42 as
the spec's `New arm:` line declares it, its RED-first observation on both staged breaks, and the legs the spec's gate
line lists are owed to the main loop at the close.

**Evidences:** TOOL-dBoundRoles-53
- AC1 — `--role gov-builder` — the case block with `A42R=gov-builder` printed `FAIL the role gov-builder reads input:question input:prompt, every key its case passes, before any render runs` and `gov-builder does not read input:question`, and both render arms printed FAIL with `not run: gov-builder does not read a key the case passes`, no render having run; the unmodified block printed `ok` on all its arms. A direct render of `gov-builder` with `--input question=` exited 2 naming `input:question is a key gov-builder does not read`, the usage error the read check now names first. OWED: arm 42 of `tools/roles/adopt-roles.test.sh` and its RED-first observation on the re-roled case at the close.
- AC2 — `input:prompt` — the case block with `A42R=gov-researcher`, a role reading `field.input.question` but no prompt, printed `gov-researcher does not read input:prompt` under a FAIL naming the role; the unmodified block ran the plain-words render first, which exited 0 and wrote `2026-11-23-prompt-TOOL-tFix-1-1-orienter.md`, then the refusal render, which exited 1 naming the span once and wrote no file. OWED: as AC1.
- AC3 — `usage error` — AMENDED by `TOOL-dBoundRoles-60`, its text restated in `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-60-deviation-604.md`: the staged copy calls `ap.error` only for a typed value holding `record:TOOL-tFix-9@000000000000`, so the control render passes and the exit check alone reds the refusal arm, and a failed control render stops the case (`TOOL-dBoundRoles-60` S4 and S5). As this unit's pass read it: with the fixture's `tools/roles/handoff.py` patched to call `ap.error` on every `render`, the read check passed and the refusal arm printed FAIL with `exit 2: a usage error, not the anchor check's refusal` and the staged error; patched to call it only for a typed `record:TOOL-tFix-9@` value, the control arm passed and the refusal arm failed naming the usage error; restored, the block passed whole. OWED: arm 42's RED-first observation on the usage-error render at the close.
