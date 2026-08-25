# Acceptance ledger — DEPL-dCarriedReceipt-14, post-write verification with index rollback

**Serves:** journal DEPL-dCarriedReceipt-14

**Evidences:** DEPL-dCarriedReceipt-14
- AC1 — `python tools/govkit/govkit.py update --write` — RED observed FIRST on a real scratch
  target against the pre-unit engine: the run exited **0**, printed `0 conflict(s)`, left a
  plausible-and-wrong CLEAN three-way merge staged, advanced `gov_commit`, and ran ZERO check
  subprocesses — while the kit's own `[check].argv` reported `landed-but-inert` on the very next
  command. GREEN: the same fixture exits 1 and rolls back.
- AC2 — `tools/govkit/selftest.py` — exit 1, one line carrying `adopted -> landed-but-inert` and
  `exit 0 -> 1`, on a `diverged` row with `0 conflict(s)` so it is provably the clean-merge path.
- AC3 — `tools/govkit/selftest.py` — the rolled-back path's index entry equals its pre-write oid,
  the worktree holds the adopter's bytes, and `git status --porcelain` prints nothing. The rename
  half holds under BOTH spellings.
- AC4 — `tools/govkit/selftest.py` — all SIX pre-run fields restored together, and the NEXT run is
  accepted by `-7` S9's preamble and re-offers exactly the rolled-back work. RED under the break
  that restores only four of six, which is the split S9 refuses on.
- AC5 — `tools/govkit/selftest.py` — the sibling kit is reported verified, its path staged at gov's
  NEW bytes. RED under a whole-run rollback: the rollback is per-kit, not per-run.
- AC6 — `tools/govkit/selftest.py` — three claimed kits, one moving rows: EXACTLY TWO subprocesses
  observed, identities logged. RED at ONE under the no-baseline draft and at FOUR under the
  baseline-every-kit draft — the two wrong drafts the criterion names by hand.
- AC7 — `tools/govkit/selftest.py` — a `none`-declared kit and one whose argv carries an unresolved
  token both print UNVERIFIED, ZERO subprocesses run for them, and neither blocks the receipt.
- AC8 — `python tools/govkit/refusal_join.py` exit 0 at 190; and `check`'s output is byte-identical
  across the S1 extraction, measured by running the HEAD engine — read out of git and ASSERTED to
  lack the new helper — against the new engine over the same fixture.
- AC9 — `tools/govkit/selftest.py` — the wedge arm. A kit red at the BASELINE too prints
  PRE-EXISTING RED with both states, does NOT roll back, and lets gov's new bytes stand. RED under
  the draft that keys the rollback on the after-state alone, which is the wedge itself.

## The one red leg this diff causes, and it is not the builder's to fix

`memory/map/generated/symbols.json` goes stale on two new module-level symbols. The regen rides this
landing commit. Same item `-11`'s ledger recorded for its own.

## A behaviour change beyond the pure extraction, armed

`run_kit_check` catches `OSError`, so a `[check].argv` naming a binary the target does not have is
reported `landed-but-inert` and NAMED rather than taking the run down with a traceback. That changes
`cmd_check` on that one path — traceback becomes a finding — and it is armed by a no-such-binary
fixture seen RED twice.

## A residual the code names rather than hides

S4's touched-kit set is derived BEFORE the write, from the verdict classes the write loop acts on,
because S2's snapshot depends on the same population and must be taken before the first byte moves —
which S4's own sentence concedes. The residual: a row refused at its own arm leaves its kit in the
set, so that kit is checked twice for a byte that never moved.
