# TOOL-dGroundRules-22 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-22

No merge bar, no gate leg and no self-test suite ran in this pass, the lexicon's `--suggest` excepted.
AC1 and AC2 were observed by in-process probes of `arm_cap_census` through `run_arm`, over this
repository and over scratch targets under the system temp directory. AC3 and AC4 were observed green
by the kit's fixture CLI on the built tree, one named case per run, and AC5 by its grep. The
`New arm:` line's red-first observation, and the `policy fixtures` and `policy check` legs, are owed
to the close.

**Evidences:** TOOL-dGroundRules-22
- AC1 — `installed` — a scratch git repository holding a copy of the kit at its own path, with the
  `installed` line staged off the `manifest-bytes` row of its `caps.toml`, printed
  `policy-check: arm_cap_census · 2 finding(s) · the cap census did not read` and the finding
  `tools/policy/caps.toml:267: manifest-bytes ships and lacks installed`, then the zero-population
  line. A probe of `read_cap_census` over a scratch census also refused a `ships = false` row
  carrying `kit` (`... has ships = false and carries kit`) and a shipped row with both fields removed
  (`runlog-record ships and lacks kit, installed`), and read the unedited census's 33 rows.
- AC2 — `arm_cap_census` — over this repository `derive_census_tree` answered `('source', None)`
  and the arm printed `0 finding(s)` over 33 census rows with `0 announced`, so no `not installed`
  and no `not shipped` line. Over a scratch target whose `install.json` holds `{` it printed
  `2 finding(s) · the install receipt did not read`: the finding names `.governance/install.json`,
  `the install receipt does not parse`, with the JSON error, then the zero-population line. A
  receipt of `[]` read as the same finding, `does not parse as a JSON object`.
- AC3 — `python check_policy.py --fixture census-adopter-receipt` — run from the repository root on
  the kit's file, it printed `cap census: line-length · kit check-line-length not installed`, no
  `manifest-bytes` announce and `no finding`, with the planted tool root `vendor/gov`, unlike gov's
  own, so the `manifest-check.sh` row was graded at `vendor/gov/manifest-check.sh` through the
  receipt's `prefix`: `3 assertion(s) executed · 0 wrong`, exit 0.
- AC4 — `manifest-check.sh` — the same run, with the planted `vendor/gov/manifest-check.sh`
  deleted, printed a finding for `manifest-bytes` naming that installed path and the kit that
  installs it, `kickoff-manifest`, and the same for `manifest-line`, `manifest-trap` and
  `orientation-card`, the other rows that enforcer serves; restored, `no finding`.
- AC5 — `grep -n "install.json" README.md` — run under the kit, it printed one line, 498, the
  `arm_cap_census` row of the "Each arm in an adopter" table, which names the receipt, the
  `kit <kit> not installed` announce and the `enforcer not shipped` announce.

Regression probes on the existing cases this change reaches: `--fixture budgets-census-join`, 3
assertions, 0 wrong, its planted row now red on the source tree as an enforcer that `is not a file`; `--fixture budgets-pinned-exempt`, 2 assertions, 0 wrong. Both plant
`EXEMPT_ROW`, which gained `ships = false` because the census now refuses a shipped row with no
`kit` or `installed`. `--fixture adopter-fresh-target` installed the policy kit by `govkit.py apply`
and printed no line for `arm_cap_census`, so it graded clean or announced there; the case still
reds on five other arms, `arm_mirror_parity`, `arm_mirror_landed`, `arm_mirror_readers`,
`arm_reader_coverage` and `arm_limits_readers`, the adopter gaps the README's table assigns to
later units, none of which this change touches.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: --fixture census-adopter-receipt. Break 2 (derive_census_tree staged to `return "source", ""`) reds 3 of 3 checks (`vendor/gov/manifest-check.sh deleted · red naming manifest-bytes and its installed path · WRONG:`). Break 1 (case's own plant) NOT observed: cd0a70507 budgets.py+caps.toml rollback crashed (`AttributeError: 'Cap' object has no attribute 'kit'`). GREEN `75 assertion(s) executed · 0 wrong`.
