# KICK-dKeptSession-54 — acceptance ledger

**Serves:** journal KICK-dKeptSession-54

This unit builds nothing (spec §3, §4 Files touched): no file of the policy kit changes, and no
function is added, so the naming lexicon has no new name to grade. No merge bar, no self-test suite,
no gate leg and no `check_policy.py --fixture` run ran in this pass. The `policy fixtures` leg and
the other legs the spec's section 7 names were not run as commands. The criteria's `get` halves were
observed on win32 at the pass's base `2db59fbb` by running this tree's `tools/policy/policy.py get`
from a scratch repository under `%TEMP%`, made by `git init` and one commit holding only
`.governance/policy.toml` with the single line `preset = "strict"`, the commit's tree read back by
`git ls-tree` naming that one path.

Owed to the close: every leg the spec's section 7 names, and in the `policy fixtures` leg the runs
of `preset-every-key` and `preset-derived-cap` that AC1's and AC2's first halves read, each to exit 0
with no `WRONG` line and `preset-every-key` with `0 wrong`. Both cases are `KICK-dKeptSession-34`'s,
CLOSED at this base, and its acceptance ledger
(`2026-11-21-build-KICK-dKeptSession-34-1-acceptance-ledger.md`) records their in-process
observation at its own base. This unit declares no `New arm:` line; the arm over both cases is unit
34's.

**Evidences:** KICK-dKeptSession-54
- AC1, the `get` probe — `python tools/policy/policy.py get roles.effort.default --rev HEAD` in the
  scratch repository exited 2 (PINNED 2026-11-21, the spec's figure, matched) with 0 bytes on stdout
  (DERIVED, that probe) and 1 stderr line (DERIVED, that probe). The line opens `policy: refused · `,
  names this tree's `tools/policy/catalogue.toml` as the refusal's source, and reads `the row
  roles.effort.default carries a derived default no reader computes yet, so roles.effort.default
  has no value to read until the file sets it`: dGroundRules' `DerivedDefault` reason, `DERIVED_WHY`
  in `tools/policy/policy.py`, with no `preset` and no `default` source printed.
- AC1, the case half — owed to the close, above.
- AC2, the `get` probe — `python tools/policy/policy.py get 'budgets."guide-bytes"' --rev HEAD` in
  the same scratch repository exited 2 (PINNED 2026-11-21, the spec's figure, matched) with 0 bytes on
  stdout (DERIVED, that probe) and 1 stderr line (DERIVED, that probe), opening `policy: refused · `,
  naming the same catalogue, and reading `the row budgets.* carries a derived default no reader
  computes yet, so budgets.guide-bytes has no value to read until the file sets it`: the same
  `DerivedDefault` reason, naming `budgets.guide-bytes`. `get` does not answer the cap under the
  preset.
- AC2, the case half — owed to the close, above.
- The probe can read a preset — in the same scratch repository `python tools/policy/policy.py get
  hooks.bypass --rev HEAD --explain` exited 0 (DERIVED, that probe), printing `refused` on stdout and
  on stderr an explain line giving source `preset` and `preset strict`. So the repository's preset
  reaches `get`, and the two refusals above are the derived rows' own, never a preset the probe
  failed to name.
