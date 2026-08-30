# aScouredKit — acceptance ledger for the two Tier-2 units

**Serves:** journal TOOL-aScouredKit-11 TOOL-aScouredKit-13

## Verdict: CLEAN WITH FIXES

*Node `a`, 2026-08-30. Evidence for the two units this build graded Tier-2, both in
`tools/govkit/govkit.py`, both changing what `apply` does in an adopter's tree. Every line below
names the observation that answered its criterion or the revision that changed it. Nothing here is
a summary of intent: where a criterion was met only after the closing review refuted the first
attempt, the line says so.*

**Evidences:** TOOL-aScouredKit-11

- AC1 — `python tools/govkit/selftest.py` — the suite's manifest fixtures drive real `apply` runs
  whose earlier steps raise and whose legs resolve, and the runner file is written; 1001 arms held.
- AC2 — `AC-withheld: a leg differing from what the receipt recorded WITHHOLDS the manifest` — the
  arm tampers the receipt so the LEGS step's own drift check raises, and asserts the
  `gate legs: WITHHELD` line. Two earlier fixtures failed to reach the branch and both faults are
  recorded in `tools/govkit/selftest.py` beside the arm.
- AC3 — amended rev-1 — S3 said the receipt's `emitted` is EMPTY when the manifest is withheld, and
  the closing review's round 1 proved that WEDGES the target: `owned` derives from that field, so a
  blank makes the next `apply` refuse the legs this deployer wrote. The criterion as written was
  wrong. What shipped carries the PREVIOUS receipt's rows forward and records `legs_withheld`
  instead; the change and its reason are in `tools/govkit/govkit.py` at the withheld branch and in
  this build's fold commit.
- AC4 — `python tools/govkit/selftest.py` — all arms held, 1001 ok, run after the final edit.
- AC5 — `python tools/govkit/govkit.py selfcheck` — exit 0 on this tree, re-run after the fold.

**Evidences:** TOOL-aScouredKit-13

- AC1 — `python tools/govkit/govkit.py plan --target <fixture>` — a target declaring
  `kits = ["memory-tree"]` previews exactly that set; asserted permanently by the selftest arm
  `a target's own kits list is honoured by a no---kits plan`.
- AC2 — `AC-ordered` and the strict-subset arm — the declared set's write set is a STRICT SUBSET of
  the registry default's, asserted as a subset relation rather than a row count precisely because a
  count can be re-baselined into agreement and a subset cannot.
- AC3 — `the target's deploy.toml names …, which is not a registry entry` — reproduced by hand
  against the live 25-entry registry through both `plan` and `adopt`, for four bad shapes: `5`,
  `true`, `"memory-tree"` and `[1]`. Each prints a named refusal and none emits a traceback.
- AC4 — `python tools/govkit/selftest.py` — all arms held.

## What this ledger does not claim

The gate reading it grades SHAPE and COVERAGE: that every criterion a closed spec numbers has a line
in one of the two legal forms. It does not assert the tokens name anything real or that the
observations were made. They were, and the commands are reproducible from this record — but that is
this author's word, and the distinction is the gate's own and worth keeping visible.

One criterion in this ledger is AMENDED rather than observed, and it is the load-bearing entry:
`TOOL-aScouredKit-11`'s AC3 asked for exactly the behaviour that turned out to wedge a target. The
amended form exists so a run that finds its own criterion wrong has a legal way to say so instead of
writing the observed form untruly, and this is that case.
