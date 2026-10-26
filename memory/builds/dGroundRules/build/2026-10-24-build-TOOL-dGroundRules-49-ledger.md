# TOOL-dGroundRules-49 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-49

No merge bar, gate leg or self-test suite ran in this pass, and the unit writes no product file. AC1
ran from this worktree's root at `fb47c2eb8`. AC2 ran in a clone made as `SCRATCH` makes it, under
`%TEMP%/gr49` and checked out at `fb47c2eb8`, with `GUARD_DROPPED` staged there by deleting the
`help/policy.md` line of the `policy fixtures` guard and the comma before it, a two-line diff; the
clone was removed after. Owed at the close: the `memory hygiene` leg over the built tree. This unit
declares no `New arm:` line.

**Evidences:** TOOL-dGroundRules-49
- AC1 — `HELP_LEGS_WHOLE` printed `help/policy.md`, then `policy fixtures <- help/policy.md [selftests/kit]` under it, and exited 0 on the built tree; it named no `no guarded leg` line.
- AC2 — after `GUARD_DROPPED`, the fixture printed `policy-fixture: guard-trace · WRONG help/policy.md · not under the policy fixtures guard`, `51 guard line(s) checked` with no `WRONG guard` line, and `210 assertion(s) executed · 1 wrong`, exit 1; after `GUARD_RESTORED`, it printed `52 guard line(s) checked`, no `guard-trace` `WRONG` line of either family, and `211 assertion(s) executed · 0 wrong`, exit 0.
