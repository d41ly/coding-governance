# Acceptance ledger — DEPL-dCarriedReceipt-6, the silenced-gate-leg bar

**Serves:** journal DEPL-dCarriedReceipt-6

Built on node `a` under session slug `aResumedRelay`. No criterion was amended: all seven were
observed as written.

**Evidences:** DEPL-dCarriedReceipt-6
- AC1 — `python tools/govkit/govkit.py selfcheck` — RED observed FIRST, and it is a green: the run
  exited **0** over a descriptor declaring a gate leg whose argv names `{prefix}/check-template-size.sh`
  while the registry exempts that file from shipping. That green-on-a-defect is the whole reason for
  the unit, and it was confirmed on this tree before a line of the arm existed.
- AC2 — `python tools/govkit/govkit.py selfcheck` — BOTH halves observed on this repo, in order.
  Before S5: exit **1**, `1 unshippable`, naming the entry, the leg and the element. After S5: exit
  **0**, `0 unshippable`. An arm only ever seen passing is an assertion about nothing, and the RED
  half is re-armed permanently by a scratch-gov fixture whose descriptor declares a leg engine no
  rule ships, so the predicate stays exercised once gov's own tree is clean.
- AC3 — `python tools/govkit/govkit.py plan --target C:/projects/nicocares/main` — measured against
  the LIVE target, read-only, in both directions. Precondition confirmed first:
  `grep -c "kickoff engine size" <NC>/scripts/gate-legs.json` is **0** and NicoCares tracks no
  `scripts/check-template-size.sh`, so this is an emission that never happens rather than a removal.
  RED: with the withdrawn leg block staged back into the descriptor, `plan` prints one `SILENT` row
  naming BOTH offending elements — the engine and the leg's SUBJECT, `skills/session-kickoff/SKILL.md`
  — which is exactly what §4 says the `/` rule does and does not distinguish. GREEN: with the
  descriptor restored, no `SILENT` row. The descriptor was restored in the same operation;
  nothing was written into `C:/projects/nicocares`.
- AC4 — `tools/govkit/selftest.py` — a fixture kit shipping its own leg engine emits the leg and
  exits 0, plus a liveness arm asserting the target's runner really gained rows. This is the
  false-positive guard for every legitimate first install, and it is the arm that reds if the
  predicate is moved before the STAGE step — which is why that placement is written into the code
  beside it.
- AC5 — `tools/govkit/selftest.py` — a leg naming an absent engine produces the finding and exit 1;
  the leg is absent from the target's runner; **the sibling leg is still there**; and the receipt was
  still written. Four arms, because "not a Refusal" is three separate observable facts and an arm
  checking only the exit code would have passed against the bug this unit shipped and then fixed.
- AC6 — `python tools/govkit/govkit.py plan --target <inCMS mirror>` — over the reconstructed
  descriptor `-4`'s ledger describes, the union predicate is observed directly: no leg is reported
  silenced that this run's own writes would satisfy. `pre-push self-test` does not appear, which is
  `-1`'s resolver holding; a second leg there would have been a regression in `-1` rather than a
  defect here.
- AC7 — `python tools/govkit/govkit.py selfcheck` + `git diff --exit-code -- tools/govkit/subject-pins.tsv`
  — selfcheck green over arms 7h/7h2/7h3 after S5, and the subject pins are untouched. The legs
  tally moved by exactly one row in each direction, claimed down one and exempt up one, which is
  what a withdrawal-plus-exemption is supposed to look like from the outside.

## Two things the spec did not foresee, and neither is a design change

- **S4's first predicate redded an INNOCENT leg.** Written as the spec's wording suggested —
  substitute the install prefix into the argv, look the result up in the shipped map — it reported
  the kickoff kit's OWN ratchet leg as unshippable, because gov's copy of that engine lives under
  `skills/session-kickoff/` rather than under `tools/`. It was caught because the candidate predicate
  was run over the real tree before being wired and its hits printed, which is this repo's standing
  rule and the reason it exists. The comparison is a TAIL match now: does some kit ship this file,
  which is the question the spec actually poses.
- **S2's finding suppressed the manifest write for EVERY leg.** The write-back is guarded on the
  report being clean, so calling `r.fail` inside the loop meant one defective leg silently took the
  healthy ones with it — the install "stood" while the target's runner stayed empty, which is the
  opposite of what S2 says and what AC5 asserts. The findings are collected and raised AFTER the
  write-back now, so that guard keeps doing its real job — withholding the manifest when something
  else went wrong — and the run still exits 1 with each finding named. Found by AC5's third arm,
  which existed only because "the install was not aborted" was written as its own observation
  instead of being folded into the exit code.

`BRANCH_PIN` moved 208 → 210, both values named. Two new branches, both armed.
