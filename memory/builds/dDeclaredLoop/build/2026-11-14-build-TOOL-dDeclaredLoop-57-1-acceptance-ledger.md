# TOOL-dDeclaredLoop-57 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-57

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on
node `d` (win32) by probes of the unit's own code: AC1 and AC4 by a scratch script that commits a
hand-written `.governance/install.json` into a scratch git repository under a short temp directory
and runs `python tools/govkit/govkit.py update --target <scratch>`, once at the pass base `630f0944`
and once on the built tree; AC2, AC3 and AC7 by a `python -c` importing `govkit` over the live
descriptors; AC5, AC6 and AC8 by the `grep` and `sed` commands they spell.

Owed to the close: every leg the spec's section 7 names, the dRB-11 fixture B arms in
`tools/govkit/selftest.py` observed green over the repaired claim, and the RED-first observation of
the one `New arm:` line, the `[dDL-57]` checks in `tools/govkit/selftest.py#check_roles_default`,
staged by taking the call to `demand_claimed_requires` out of `tools/govkit/govkit.py#_cmd_update`
for one run and restoring it.

**Evidences:** TOOL-dDeclaredLoop-57
- AC1 — `'roles' requires 'loop'` — at base the update printed `default-gained: none computed` and
  refused later on the absent `deploy.toml`; built, it exited 2 with stderr naming the pair, the
  `gov_commit` reason and `apply --kits roles,loop`, stdout held no `none computed` line, and
  `git status --porcelain --untracked-files=all` printed nothing. Under `--kits roles` it refused
  naming the same pair.
- AC2 — `does not resolve` — the call over the roles claim with that reason raised `Refusal` naming
  `'roles' requires 'loop'` and the reason; with `gained` set to `["loop"]` it returned.
- AC3 — `'loop' requires 'memory-tree'` — over fixture descriptors with an empty reason it raised
  `Refusal` naming that pair and no `default-gained did not cover it` clause.
- AC4 — `would gain loop` — over a receipt at `ed497191`, at base and built alike stdout held the
  line and neither stream held `update would leave`.
- AC5 — `apply --kits roles,loop` — `grep -n` printed one line inside the bullet that opens "The
  `loop` kit joins the default selection", which says the update is refused before it writes.
- AC6 — `demand_claimed_requires` — `grep -c` over `memory/map/generated/symbols.json` printed 1
  after `gen_map.py --write`.
- AC7 — `'agent-cap' requires 'kickoff-manifest'` — fixture B's claim with `settings-merge` gained
  raised `Refusal` naming that pair; with `kickoff-manifest` claimed it returned.
- AC8 — `kits="check-wiring,kickoff-manifest"` — `grep -n -A1` printed the rq11b call passing it, and
  the `sed` range piped to `grep -c kickoff-manifest` printed 2.
