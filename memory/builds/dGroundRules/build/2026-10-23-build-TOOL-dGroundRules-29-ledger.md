# TOOL-dGroundRules-29 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-29

No merge bar, no gate leg and no self-test suite ran in this pass. Each criterion was observed by the
kit's own CLI, `check_policy.py --repo` and `--fixture` and `adopt-policy.sh`, over scratch `git init`
targets outside the worktree and over this tree, and AC3's red half by an in-process probe that
replaced `derive_census_tree` for that run only, touching no tracked file. The spec-token checker over
the live tree ran inside `--dispatch` with the change in the working tree, and the dispatch was
declared and effective. The `New arm:` line's red-first observation, and the §7 legs, are the close's.

**Evidences:** TOOL-dGroundRules-29
- AC1 — `arm_cap_census` — `bash adopt-policy.sh --scaffold --target <t>` exited 0 over a fresh `git init` target, then `--check --target <t>` printed `policy-check: arm_cap_census · 0 finding(s) · 33 census row(s) joined to their enforcers and cases, 33 announced`; all 33 `cap census:` lines end `not installed` or `not shipped`. `--check` exited 1, on `arm_legacy_homes` (113 findings), an arm this unit does not own.
- AC2 — `<t>/tools/govkit/registry.toml` — `python check_policy.py --repo <t>` over a `git init` target holding only that copy printed `policy-check: arm_cap_census · 33 finding(s) · ... 0 announced`, one `its enforcer ... is not a file in this tree` per census row; over this repository it printed `arm_cap_census · 0 finding(s) · 33 census row(s) joined ..., 0 announced` and no `not installed` line (count 0).
- AC3 — `WRONG` — `python check_policy.py --fixture census-receiptless-target` exited 0, `33 announce line(s) and no finding · 33 announced · no finding`, then `33 of 33 row(s) red` with the registry copied in, `2 assertion(s) executed · 0 wrong`. With `derive_census_tree` staged in process to answer `source` for every receipt-less tree it exited 1 printing `WRONG: 0 announced` with a finding per row and `1 wrong`.
- AC4 — `<t>/vendor/kits/govkit/registry.toml` — with `<t>/govkit/registry.toml` also planted in a receipt-less `git init` target, `python check_policy.py --repo <t>` printed under `arm_cap_census` the finding `govkit/registry.toml, vendor/kits/govkit/registry.toml: 2 govkit/registry.toml candidates, so the tool root is not guessed and no row is graded`.
- AC5 — `grep -n "registry.toml" README.md` — under the kit it printed line 626, the `arm_cap_census` row of the "Each arm in an adopter" table, stating the three answers and the registry rule.

Owed at the close, observed by no command in this pass:

- The `New arm:` line of §7, `--fixture census-receiptless-target`, RED with `derive_census_tree` staged to answer `source` for every receipt-less tree, GREEN restored, in the tree the close runs.
- The §7 legs `memory hygiene`, `recall floor`, `recall floor arms` and `policy fixtures`.
