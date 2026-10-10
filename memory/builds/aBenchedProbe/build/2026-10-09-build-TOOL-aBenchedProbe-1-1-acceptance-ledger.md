# TOOL-aBenchedProbe-1 — acceptance ledger

**Serves:** journal TOOL-aBenchedProbe-1

No merge bar and no self-test suite ran in this pass. The criteria were observed with the direct
probes the spec's section 4 records and with `govkit selfcheck`, which is the leg the subject parity
and the pin ratchet live in, run whole three times: on the built tree, on a staged break, and on the
restored tree. The staged break put the manifest's `pre-push self-test` row back to
`"subject": "repo"` with the descriptor at `kit`. Selfcheck went RED, exit 1, with the 7h disagreement line and
the pin-ratchet line both naming that leg. Restored, it went GREEN again, exit 0, naming none of the
three legs. This unit adds and moves no arm, so the 7h arm is the only arm it re-observed. The close
still owes the section 7 legs, `govkit selftest` and both run-gates canaries among them.

**Evidences:** TOOL-aBenchedProbe-1
- AC1 — `govkit.read_descriptors` — the descriptor probe printed `kit` for `push-main self-test`,
  `pre-push self-test` and `pre-push bar self-test` on the built tree; BASE prints `repo` for all three.
- AC2 — `python tools/govkit/govkit.py selfcheck` — the built tree exited 0 and no output line named
  any of the three legs. With only the manifest's `pre-push self-test` row back at
  `"subject": "repo"` it exited 1, printing that entry `push-main` declares the leg as subject `kit` while the
  manifest says `repo`. Restored, it exited 0 with no line naming the three.
- AC3 — `subject pins:` — the held-set probe printed `64 64 True`, and the selfcheck note line read
  `subject pins: 128 pinned · 64 held`. The same predicate over the BASE pin file counts 64 held, so
  gov's own bar holds the same population.
- AC4 — `git diff -U0 -- tools/govkit/subject-pins.tsv` — after `selfcheck --write`, exactly three
  rows moved: `pre-push bar self-test`, `pre-push self-test` and `push-main self-test`, each `repo`
  before and `kit` after, with chunk `selftests` on both sides.
- AC5 — `git grep` — the prose sweep over the leg names and argv files, memory tree excluded, found
  49 hits on the built tree, classified below. None outside section 3 says one of these legs runs
  on a default bar.
  - `tools/gate-legs.json`, `tools/govkit/subject-pins.tsv`, `tools/govkit/entries/push-main.kit.toml`
    (19 hits): the rows this unit wrote, plus the descriptor's `include` and `claims` lists. True.
  - `.githooks/gate-env.sh`, `.githooks/pre-push`, `.githooks/pre-push.runlog.test.sh`,
    `.githooks/pre-push.test.sh`, `.githooks/pre_push_bar_selftest.py`, `tools/push-main.test.sh`
    (14 hits): suite headers, usage lines and cross-references between the suites. None states a
    subject or a default run. True.
  - `tools/check-spec-tokens.py` (2 hits): comments about which keys a guard reads. True.
  - `tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json` (2 hits) and `tools/govkit/selftest.py`
    (1 hit): a receipt fixture's file list and a comment about it. True.
  - `tools/govkit/registry.toml` (1 hit): the exempt-leg reason for the run-log suite, which this
    unit does not touch. True.
  - `tools/run-gates/ceiling-evidence.txt` and `tools/run-gates/selftest-budgets.txt` (6 hits):
    timing and budget rows. True.
  - `tools/run-gates/run-gates.gov.test.sh` (1 hit): a cross-reference to the hook suite. True.
  - `tools/run-gates/run-gates.sh` line 2135 (1 hit): the hold comment saying these legs carry
    `subject = repo`. It is history of the 2026-08-26 ruling and says they are held by chunk, not
    run; section 3 keeps it out of this unit's write set.
  - `WIRE-INTO-PROJECT.md` line 782 (1 hit): the hand-wiring instruction naming no subject, the
    section 3 Edges hand-off, filed as an ask at the close. Line 798 (1 hit) tells an adopter to copy
    the lander files in and says nothing about a bar. True.
