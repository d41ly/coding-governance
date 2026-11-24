**Serves:** journal TOOL-dBoundRoles-19

# TOOL-dBoundRoles-19 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on the
worktree before the pass commit at base `7dae6faf2`: the step program `tools/govkit/steps/house_overlays_to_instructions.py`
run by its own CLI under `-I` over short-pathed fixture targets under the host temp folder, each holding a copy of the
base's roles kit under the prefix `tools` and no overlay; the program of the new arm of `tools/roles/adopt-roles.test.sh`
run by direct CLI over a scratch repository under the host temp folder, with the roles adopter's `--scaffold` between its
passes; a scratch clone of the base with this pass's changes committed, in which `render_agents.py --write` and
`adopt-playbook.sh --target .` were run; the up, witness and the roles kit's `handoff.py stage-efforts` over this
worktree and over the base clone; and the SD8 AC2 span read of `tools/check-spec-tokens.test.sh` cut out and run over
gov's overlay. No gate, suite or bar ran in the pass: each `New arm:` arm section 7 declares, its RED-first observation
on its staged break, and the legs section 7 lists are owed to the main loop at the close.

**Evidences:** TOOL-dBoundRoles-19
- AC1 — `repo.house.gov-builder` — over a fixture whose gov-builder house text file held one line and every other house text file was empty, the witness exited 1 before the up; the up exited 0 writing a single `[[unit]]` (DERIVED, read back by `tomllib`), tag `repo.house.gov-builder`, level 5, `type = "adopter-rule"`, `scope = ["role.gov-builder"]`, `budget = "block"`, its text that line; no `.md` file remained in the target's roles `house` directory, `house/policy.toml` stayed, and the witness exited 0. A unit reworded after the up still read applied, and one re-tagged exited 1 naming the tag. OWED: the `govkit selftest` leg's `house-step-AC1` rows at the close.
- AC2 — `down` — after that up, the down exited 0 and every house text file and the absent overlay were byte-identical to the fixture before the up, and the witness exited 1. Its staged break, the before-image removed after the up, left the down restoring nothing and every house text file and the overlay differing from the fixture: RED. OWED: the `govkit selftest` leg's `house-step-AC2` rows, RED first with an up that skips the before-image, at the close.
- AC3 — `<!-- gov:repo -->` — the new arm's program printed `ac3-up 1` and, after the adopter's `--scaffold` exited 0, `ac3-marked 1`: the fixture's `.claude/agents/gov-builder.md` carries the moved line between `<!-- gov:repo -->` and `<!-- /gov:repo -->` and no `## House rules` heading. On gov's tree the up exited 0 writing the unit `repo.house.gov-spec-writer` alone (DERIVED, from the up's own line) and removing every house text file; in the scratch clone, `render_agents.py --write` at the base printed every agent type and the index unchanged, and after the change rewrote only `.claude/agents/gov-spec-writer.md` and `.claude/roles.json`, both byte-identical to this pass's, the former carrying the text between the marks in place of its `## House rules` section. OWED: arm 47's `ac3-` lines, RED first with the house-file read restored in `tools/roles/roles_lib.py#render_role`, and the `roles render wiring` leg at the close.
- AC4 — `role.gov-nobody` — the new arm's program printed `ac4-clean 1`, then `ac4-nobody 1` and `ac4-heading 1`: `check_roles.py` over a fixture commit whose overlay holds a level-5 unit selecting `role.gov-nobody`, and over one whose unit text carries a `## ` line, each exited 1 with an R10 line naming the unit's tag. OWED: arm 47's `ac4-` lines and the `roles catalogue` leg over gov's tree at the close.
- AC5 — `spec-write` — `grep -n "house/" kit.toml` in `tools/roles/` prints `house/policy.toml` as the only include under a seed rule, the rest the step row's comment and `surfaces`; `python tools/roles/handoff.py stage-efforts spec-write` printed the same levels over the base clone and over this worktree. OWED: the `policy fixtures` leg at the close.
- AC6 — `instructions.toml` — `grep -n "roles/house/<" help/roles.md` prints nothing, and `grep -n "instructions.toml" help/roles.md` names the "Change how a role behaves" entry saying a role's project rules are a level-5 overlay unit selecting it. OWED: nothing beyond the legs section 7 lists at the close.

## The deletion's criterion, AC7, added on top by TOOL-dBoundRoles-60

`TOOL-dBoundRoles-60` S27 gives this unit the criterion unit 55's AC2 names as its after half, and its deviation record
`memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-60-deviation-604.md` holds the text. This unit's
spec is CLOSED and frozen and numbers no AC7, and the acceptance-ledger check refuses a label its spec does not number,
so the answer stands under this heading rather than in the block above.

OBSERVED: `grep -n 'derive_overlay_expected' tools/govkit/selftest.py` printed nothing over the file as this unit's
pass commit `bfccd9126` leaves it and over the tree at `ae8fc1f65`, and printed the definition, its call, the comment
and the docstring at the pass commit's parent `7dae6faf2`.
- seen-red — `roles adopter self-test` — red `3c9b6ad0e` — green `3c9b6ad0e` — the R10 unknown-role test cut, arm 47 ac4-nobody red
- seen-red — `govkit selftest` — red `a6f9ddc6b` — green `a6f9ddc6b` — the before-image write skipped: check_house_step reads a failure
