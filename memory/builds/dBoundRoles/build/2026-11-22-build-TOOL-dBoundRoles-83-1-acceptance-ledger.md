**Serves:** journal TOOL-dBoundRoles-83

# TOOL-dBoundRoles-83 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on the
worktree before the pass commit at base `16670469a`: each plant of `tools/playbook/fixtures/row_kind.py#PLANTS` run
by the fixture's own `--plant` CLI, each in the throwaway repository `tools/playbook/fixtures/row_kind.py#main` makes
under the host temp folder, a `python -c` probe of `tools/playbook/row_checks.py#derive_ref_tag`,
`tools/playbook/row_checks.py#check_rows` and `tools/playbook/overlay_rows.py#read_leg_names` over gov's own
spellings, the item composition's pins compared before and after the edit, and a grep of the help page. No gate,
suite or bar ran in the pass: the `New arm:` arm section 7 declares, its RED-first observation with the walk
comparing members as written, and the legs section 7 lists are owed to the main loop at the close.

**Evidences:** TOOL-dBoundRoles-83
- AC1 — `exclude-actor-spelled` — `python tools/playbook/fixtures/row_kind.py --plant exclude-actor-spelled` exited 1 with a `row-checks: red · exclude` line naming the excluded `fixture.beta`, the row `fixture.adopter.actor`, its actor field and the member as spelled, `fixture:beta`. The `python -c` probe gave the same red for an item whose `actor` is `role:gov-builder` with `role.gov-builder` excluded. OWED: the `exclude-actor-spelled` selftest row of the `playbook render selftest` leg, RED first with the walk comparing members as written, at the close.
- AC2 — `exclude-leg-named` — `--plant exclude-leg-named` exited 1 with a `row-checks: red · exclude` line naming the excluded `leg.fixture.fixture-leg`, the row `fixture.adopter.granter`, its grants field and the member as spelled, `fixture leg?`. The `python -c` probe read gov's manifest through `read_leg_names` (DERIVED, its length printed at the probe) and folded `lexicon naming predicates?` to `leg.lexicon.lexicon-naming-predicates`. OWED: the `exclude-leg-named` selftest row, RED first, at the close.
- AC3 — `exclude-actor` — `--plant exclude-actor` still exited 1 naming `fixture.adopter.actor`, its line as before with no `as` clause; `python tools/playbook/overlay_rows.py compose --kind item` printed `pins` equal to the before-pins the same command printed on the worktree at base `16670469a` before the first edit (DERIVED, compared in-process). OWED: the existing `exclude-actor` selftest row at the close.
- AC4 — `exclude-leg-unnamed` — `--plant exclude-leg-unnamed` exited 0, composed `fixture.adopter.granter` and printed no `row-checks: red · exclude` line; `--plant exclude-leg-named --exclude leg.fixture.other` exited 0 too. OWED: the `exclude-leg-unnamed` selftest row, RED first, at the close.
- AC5 — `role:<slot>` — `grep -n "role:<slot>" help/overlay-rows.md` printed the exclusion paragraph's line of "What you may not change, and how a widening is reported" naming `role:<slot>` as `role.<slot>`. OWED: nothing beyond the legs section 7 lists at the close.
- seen-red — `playbook render selftest` — red `f3ec096a8` — green `f3ec096a8` — the actor fold cut, then the leg-name fold: exclude-actor-spelled and exclude-leg-named exit 0
