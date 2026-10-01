**Serves:** journal TOOL-dAlignedCarrier-6

# Fold brief — the closing review's round 2 into TOOL-dAlignedCarrier-6

Round 2 reviewed the round-1 fold and is
`memory/builds/dAlignedCarrier/reviews/2026-09-30-review-TOOL-dAlignedCarrier-6-closing-diff-round2.md`.
Read it WHOLE. Its six items, M1, M2 and L1 to L4, were all introduced by the round-1 fold. Round 1
recorded CONVERGED, which is terminal for the subject, so every item is FOLDED by severity into this
unit's spec as rev-5 with a section 9 line, and fixed where it names. One pass, one commit. The shared
build brief `2026-09-30-prompt-TOOL-dAlignedCarrier-1-build-brief.md` still binds every rule it
states; the spec stays CLOSED.

## The corrected wording, because the last brief got it wrong

The round-1 fold brief told you "the driver sets neither flag". That is FALSE: under
`LANDER_MODE=in-place` the close's gates-green bar is invoked with `GATE_FULL=1` by the driver itself
(`tools/unattended/unattended.sh`, the in-place bar invocation; TOOL-dDerivedDocket-3 S3). What IS
true, and what the owner ruled (TOOL-dDerivedDocket-70), is that the driver never sets
`GATE_SELFTESTS`. So every carrier that now says the driver sets neither flag says instead, in its own
words: the driver never sets `GATE_SELFTESTS`; under `in-place` the close's bar already carries
`GATE_FULL=1`; the main loop exports the pair `GATE_FULL=1 GATE_SELFTESTS=1` into its one `--close`,
which is redundant but harmless under `in-place` and pays the pair under `primary`. Correct the spec's
section 8 F5 text the same way.

## What each item owes, per the record's own Fix and Left-shift

- **M1** — the new gotcha record is claimed by the codebase-map dossier that owns `memory/gotchas/`,
  and the map's generated artifacts are regenerated in the same commit. Observe it with the checker the
  `codebase-map coverage + freshness` leg runs (its argv is in `tools/gate-legs.json`): a direct check,
  not a suite. The class is loud at the bar, so the observation is the left-shift.
- **M2** — the wording above, in all five carriers and the spec's F5, and the protocol render
  re-copied.
- **L1** — check 47's window widened so row 2's widest instance matches; run the widened predicate over
  the tree and print hits and near-misses before committing; stage the eight-token wrap as the break.
- **L2** — the range read uses `-z` with a NUL-safe split instead of relying on `core.quotepath=off`.
- **L3** — the Skill's While-it-runs bullet names the pair, not "it".
- **L4** — row 2's pattern consumes its trailing boundary so the excerpt is whole.

Every arm literal that tracks a message changes in the same commit. Budgets as before: the protocol
at 65310 of 65692 bytes, so at most 200 more; `check-unattended.sh` edited in bytes with its CR count
at 4; `.unattended.conf` edits owe the manifest re-stamp; every written path declared with
`--dispatch`, generated ones included. Append ledger lines for any NEW section 6 criterion.
Commit subject: `fold(dAlignedCarrier): TOOL-dAlignedCarrier-6 — the closing review's round 2`.
