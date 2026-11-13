# TOOL-dDeclaredLoop-36 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-36

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed by
`python` probes that load `tools/govkit/govkit.py` and call the functions the criteria name, over
the working tree and over a scratch clone of this tree holding the working tree's registry
committed, and by the `grep -c` commands AC4 spells. The pass base is `094af7f7`.

Owed to the close: the `govkit selfcheck` leg, which is AC3's own command, and the standing arms the
spec's section 7 names, each of which the main loop observes there: check 7b of
`tools/govkit/govkit.py#selfcheck`, the `OC8 AC2` arm of
`tools/govkit/selftest.py#check_roles_default`, the `RQ5 AC1` arm and the staged 7b arm of
`tools/govkit/selftest.py#main`, and the default-install shape of `tools/govkit/matrix.py#main`.
The spec declares no `New arm:` line, so no RED-first observation is owed.

**Evidences:** TOOL-dDeclaredLoop-36
- AC1 — `derive_unsatisfied_requires` — at the pass base, before the edit, the probe printed
  `[('roles', 'loop')]` for `derive_unsatisfied_requires(list(default_kits(reg)), descs, None)`,
  the red value the criterion pins. With S1's line in the working tree the same call printed `[]`,
  and `derive_install_order` over the same list put `loop` third and `roles` twelfth, `loop` before
  `roles`.
- AC2 — `derive_default_gained` — over a scratch clone with the working tree's registry committed
  on top of the pass base, base commit `ed497191`, the to-commit the clone's HEAD and a receipt
  whose `kits` is the default list read from the registry blob at `ed497191`, the gained list was
  `playbook-render`, `policy`, `loop` and the reason string was empty;
  `derive_unsatisfied_requires` over that gained list and that receipt returned `[]`. The red case
  was observed in the same clone: with the to-commit the clone's parent commit, where the line is
  absent, the gained list was `playbook-render`, `policy` and held no `loop`. It reads the
  derivation, never the landing.
- AC3 — `the default set holds` — NOT RUN: `python tools/govkit/govkit.py selfcheck` is the
  `govkit selfcheck` leg's command, owed to the close. Observed in its place: check 7b builds that
  message once per pair `derive_unsatisfied_requires` returns over the default set with no receipt,
  and AC1's probe is that call, which returned no pair over the working tree and the pair
  `roles`, `loop` at the pass base.
- AC4 — `default selection` — `grep -c "which requires it" help/loop.md` printed `0`,
  `grep -c "through the roles kit" tools/playbook-kit-waivers.txt` printed `0`,
  `grep -c "default selection" help/loop.md` printed a count above zero, and
  `grep -c "loop.*joins the default selection" help/upgrade-steps.md` printed a count above zero.

Beside the criteria: the section of `help/upgrade-steps.md` that gained the bullet opens by
counting its bullets, and the count word moved with the bullet. That edit is recorded as
`2026-11-13-build-TOOL-dDeclaredLoop-36-deviation-363.md`.
