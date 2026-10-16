# TOOL-dRedressedBar-20 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-20

Written by TOOL-dRedressedBar-27 on 2026-10-15, after the unit closed with no ledger, from what its
builder recorded. Nothing was re-run for it. The unit was built against spec 20 rev-2, which is
still its current revision, in three commits: the code commit `404d45c8c`, the restore commit
`21c2d1531`, and `566c6d831`, which moves the status header alone. The readings are the builder's,
from those commits' bodies and from its return in
`2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`, under the heading
`2026-10-14T17:20:54 · gov-builder · wf_505af0b9-122/a737641ff163ce752` at line 5022. The code
commit's first parent is `20112bce8`. No merge bar, no self-test suite and no gate leg ran in the
build pass, and the section 7 legs and the `New arm:` observation were owed to the close.

**Evidences:** TOOL-dRedressedBar-20
- AC1 — `git diff -U0` — in a clone of `20112bce8` the writer printed the one tuple
  `('tools/playbook/render_playbook.py', 'playbook-render', 'playbook-render', '3.5', '1.28')`, and
  `git diff -U0` changed line 1646 only. In a clone of `404d45c8c` it printed `[]` with a clean
  status. The commit body reads the green half over the code's bytes copied into the first
  clone, where `git status --porcelain` named only the two copied files.
- AC2 — `version: '9.99'` — with `KIT_DRIFT_AUDIT_VERSION` at 9.99, the writer made 14 rewrites,
  two in each harness, and `grep -c "version: '9.99'"` printed 1 for each of the four.
- AC3 — `epoch: playbook-render · clean · 1.28` — `mint --base ebce889c7` in a fresh clone of
  `404d45c8c` exited 0 with `->` lines for agent-cap, branch-reconcile, roles and unattended only,
  and `tools/playbook/` stayed clean. After a scratch commit, `epoch` printed that line and no
  FAILED line at all. The builder recorded one deviation: the scratch commit in the clone took
  `--no-verify`.
- AC4 — `[dRB-20]` — the `arm` probe, run alone with `__pycache__` deleted first, exited 1 over
  the base writer with FAIL lines naming `[dRB-20]` and the count (9), and exited 0 with every
  line ok over the fix, again at HEAD. Its `tempfile.mkdtemp` took `dir=` the scratchpad.
- AC5 — `grep -c "ANY entry's"` — it printed 0, and the scope sentence's grep printed 1.
- AC6 — `tools/govkit/govkit.py` — the code commit's diff names exactly it and
  `tools/govkit/selftest.py`, and adds or removes no `def` line.
- AC7 — `v3.5` — at `21c2d1531`, lines 1397 and 1646 both read it, and the code-to-restore diff is
  one file and changes line 1397 only. In a clone of the restore commit the writer printed `[]`
  with a clean status, and `epoch` printed `epoch: playbook-render · FAILED · moved in 21c2d1531d`,
  the move unit 7's mint dates.
- AC8 — `<!-- governance-template: v3.5 --> True True True` — `v3render`, run from a scratch script
  at the restore commit, exited 0 and printed it. With the marker at `v4.0` in a scratch clone, it
  refused, naming the `when:node-table` fence, so the probe can go red.
