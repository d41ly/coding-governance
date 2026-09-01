**Serves:** journal DEPL-dGaugedVintage-3

# Acceptance ledger — DEPL-dGaugedVintage-3, the INCOMPLETE report

**Evidences:** DEPL-dGaugedVintage-3

- AC1 — `python tools/govkit/govkit.py apply --target <fresh> --kits memory-recall` — the entry
  reported `INCOMPLETE memory-recall: 3 declared file(s) carry this kit's own behaviour and this
  target holds none of them`, naming `extract.py`, `query.py` and `recall-opened.js`, each with
  `UNLANDED_REASON`'s sentence for the `forked` role.
- AC2 — `tools/govkit/selftest.py` — over a target already holding those three files there is no
  INCOMPLETE line, and the adopter's own `query.py` bytes are unchanged after the run.
- AC3 — `python tools/govkit/selftest.py` — the whole suite closes `all arms held`, so no
  pre-existing apply arm moved. An output change for entries with no `forked` rule would have
  reddened them; that it did not is the observation.
- AC4 — `git show HEAD:tools/govkit/govkit.py` — the pre-fix binary, run from inside the tree over
  the same fresh target, left `query.py` absent and printed ZERO INCOMPLETE lines. That silence is
  the defect, reproduced.
- AC5 — `bash tools/check-install-prefix.sh` — exits 0 over the new remedy text, so the message
  spells no root-prefix path and does not strand an adopter installed at another prefix.
- AC6 — amended rev-3 — the criterion asked for a SYNTHETIC second entry; building one needs a
  test-only row in `tools/govkit/registry.toml` and a tracked descriptor beside it, which widens
  this unit into the registry. The detection instead keys on `u["role"] == "forked"` and never on a
  kit id, and the arm asserts all three of `memory-recall`'s absent destinations. Logged in §9.

## What this ledger does not claim

Nothing seeds. `DEPL-dCarriedReceipt-10` ratified that gov has no right to send a forked file's
bytes, and §8 F1's seed branch remains superseded pending an owner id. The report is scoped to
`forked` alone: `rendered`, `generated` and `project-owned` are excluded for the reasons the code
comment states, not by omission.
