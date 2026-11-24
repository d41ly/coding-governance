# KICK-dKeptSession-58 — acceptance ledger

**Serves:** journal KICK-dKeptSession-58

This unit builds nothing (spec §1, §3, §4 Files touched): no file of the policy kit changes and no
function is added, so the naming lexicon has no new name to grade. No merge bar, no self-test suite,
no gate leg and no `check_policy.py --fixture` run ran in this pass. The `policy fixtures` leg and
the other legs the spec's section 7 names were not run as commands. AC2 was observed on win32 at the
pass's base `905c0062` by running this tree's `tools/policy/budgets.py resolve --explain` from two
scratch repositories under `%TEMP%`, each made by `git init` on `main` and one commit holding only
`.governance/policy.toml`, the commit's tree read back by `git ls-tree` naming that one path, with
`GOV_REMOTE`, `GOV_DEFAULT_BRANCH` and the `GIT_*` variables unset as the case's runner unsets them.
Both repositories were removed after the probe.

Owed to the close: every leg the spec's section 7 names, and in the `policy fixtures` leg the run of
`preset-derived-cap` that AC1 reads, to exit 0 with no `WRONG` line. The case is
`KICK-dKeptSession-34`'s, CLOSED at this base, and its acceptance ledger
(`2026-11-21-build-KICK-dKeptSession-34-1-acceptance-ledger.md`) records the case's in-process
observation at its own base. This unit declares no `New arm:` line; the arm over the case, and the
RED-first observation AC1's red side names, a kit copy of `budgets.py` ignoring the preset's
`budgets.enforce`, are unit 34's.

**Evidences:** KICK-dKeptSession-58
- AC1 — `python check_policy.py --fixture preset-derived-cap` is owed to the close, above; S3
  answers AC1 from unit 34's landed case. Unit 34's ledger's AC2 line records
  `run_preset_derived_cap` reading `budgets.py resolve --explain <cap>` for `guide-bytes`, the row
  `guide-bytes\t-\twarn\tnone` with an empty policy file and `guide-bytes\t-\trefuse\tnone` under
  `preset = "strict"`, each with its `budgets.enforce is <mode>` rule line, the value and source
  equal, and 3 assertions with 0 wrong (PINNED 2026-11-21, unit 34's ledger's figure, read). The
  case at this base, `run_preset_derived_cap` in `tools/policy/check_policy.py`, compares the rows'
  value and source columns alone (`seen[...][1::2]`) and asserts the mode column `warn` then
  `refuse`, so it compares no whole row.
- AC2, strict — `budgets.enforce is refuse`: in the scratch repository on `main` whose one commit
  holds the policy file `preset = "strict"`, `python tools/policy/budgets.py resolve --explain
  guide-bytes` exited 0 (DERIVED, that probe) with 1 stdout line (DERIVED, that probe),
  `guide-bytes\t-\trefuse\tnone`, and 1 stderr line (DERIVED, that probe) opening `budgets:
  guide-bytes · budgets.enforce is refuse · ` and saying the cap has no value because the policy
  file does not set it and its conf home holds none. Strict's switch reaches the caps module.
- AC2, no preset — `budgets.enforce is warn`: in the scratch repository on `main` whose one commit
  holds an empty policy file (0 bytes, DERIVED, that probe), the same command exited 0 (DERIVED,
  that probe) with 1 stdout line (DERIVED, that probe), `guide-bytes\t-\twarn\tnone`, and 1 stderr
  line (DERIVED, that probe) opening `budgets: guide-bytes · budgets.enforce is warn · ` with the
  same reason. The two rows' value and source are `-` and `none` each, equal.
- AC2, the cap — `<cap>` read `guide-bytes`, the census's first `switch` row that is no family and
  whose home is not `limits:` (DERIVED from `budgets.read_cap_census` at 905c0062), the cap unit
  34's case picks.
