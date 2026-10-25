# TOOL-dGroundRules-17 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-17

No merge bar, no gate leg and no self-test suite ran in this pass, the lexicon's `--suggest` excepted.
AC1, AC2 and AC4 were observed by one scratch probe: `build_source_snapshot` of the working tree,
the snapshot's `govkit.py plan` and `apply --kits policy` into a fresh short-path target under the
system temp directory, then the installed kit's CLIs there. AC3 and AC5 were observed green by the
kit's fixture CLI on the built tree, one named case per run. The `New arm:` line's red-first
observation for both cases, and the `policy check` and `policy fixtures` legs, are owed to the close.

**Evidences:** TOOL-dGroundRules-17
- AC1 — `legacy-homes.txt` — `govkit.py plan --target <t> --kits policy` from the snapshot printed
  13 `write` rows, none ending `legacy-homes.txt`, and one `ORDER [project-owned]` row for
  `tools/policy/legacy-homes.txt`, govkit's mark for a file outside `apply`'s writes; `apply`
  exited 0 and the target held no list. The criterion's red condition, the list installed, does not
  hold. The `ORDER` row is the plan row `TOOL-dGroundRules-25` S9 and AC9 restate the criterion
  against, so this criterion's "names no destination" reads the write rows.
- AC2 — `legacy-homes` — `check_policy.py --repo <t>` in that target printed
  `policy-check: arm_legacy_homes · not graded · the list is gov's own and is withheld from installs`
  and no finding under it; `policy.py lists --write` there exited 0 printing
  `policy lists: legacy-homes.txt · not written`, the same reason after it, and no list existed
  after it. The arm's name prints as `ARMS` spells it, the form
  `check_arm_lines` and the README's adopter table read.
- AC3 — `legacy-homes.txt` — `check_policy.py --fixture legacy-homes-present` on the built tree
  printed the list present in this kit's directory and the descriptor's `project-owned` rule
  naming it: `2 assertion(s) executed · 0 wrong`, exit 0. The red-first observation with the list
  staged deleted from a scratch copy is the close's, on the `New arm:` line.
- AC4 — `arm_cap_census` — over the policy-only target: `0 finding(s)`, 33 rows, 33 announced: the
  7 `ships = false` rows as `enforcer not shipped`, and 26 as `kit <home> not installed`, homes
  `memory-tree`, `roles`, `playbook`, `memory-recall`, `agent-instructions`, `runlog`,
  `codebase-map`, `hooks`, `skills` (the out-of-prefix manifest rows) and `check-line-length.sh`
  (the root-level row, whose first segment below `{prefix}` is the file itself and resolves no
  `kit.toml`). With the memory-tree kit's `kit.toml` planted and its enforcers absent, the arm
  printed 13 findings, each a memory-tree row naming its enforcer as `not a file in this tree`, and
  20 announced. Gov's own tree: 0 findings, 0 announced.
- AC5 — `ships = false` — `check_policy.py --fixture budgets-ships-join` on the built tree printed
  one green line per row the join names, the 7 rows of `{prefix}/check-template-size.sh` and
  `{prefix}/check-spec-tokens.py`, and `7 row(s) of 33, exempt by tools/govkit/registry.toml`:
  `8 assertion(s) executed · 0 wrong`, exit 0. An in-process probe flipping `AGENTS.md` to shipped
  and `guide-bytes` to `ships = false` printed `WRONG` naming each. The staged red-first
  observation on `caps.toml` is the close's. The `policy fixtures` guard already named
  `{prefix}/govkit/registry.toml`, added by `TOOL-dGroundRules-24`, so `tools/gate-legs.json` is
  unchanged.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: legacy-homes.txt staged deleted -> `legacy-homes-present · ... · WRONG: absent in .../tools/policy` (1 wrong); caps.toml row ships=false->true -> budgets-ships-join `WRONG: Refusal: policy: refused · tools/policy/caps.toml:32 · ... ships and lacks kit, installed` (reds by the census refusal TOOL-dGroundRules-23 added, before the join compares). GREEN 69 and 134 assertions, 0 wrong.
