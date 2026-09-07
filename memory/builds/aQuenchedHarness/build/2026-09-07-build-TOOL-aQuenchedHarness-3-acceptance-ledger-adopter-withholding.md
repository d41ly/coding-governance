# Acceptance ledger — TOOL-aQuenchedHarness-3

**Serves:** journal TOOL-aQuenchedHarness-3

**Evidences:** TOOL-aQuenchedHarness-3

Tier-2 · node a · 2026-09-07. One line per numbered criterion, each naming the observation that
answered it. A line saying MET without an observation is a checkbox, which is why the gate refuses
one; a line saying NOT MET is equally a result and is recorded the same way.

- AC1 — MET, OBSERVED — every kit descriptor claims its own suites with `role = "project-owned"`, which is absent from `LANDABLE_ROLES`, so `apply` never writes them. Verified across eleven `tools/*/kit.toml` files in `e55f933b` and re-asserted on arrival for the two suites added later in this build.
- AC2 — MET, OBSERVED — the 21 withheld legs moved from `[[gate_leg]]` rows to `[[exempt_leg]]` rows in `tools/govkit/registry.toml`, which is what stopped every adopter apply exiting 1 with one silenced-leg problem per suite.
- AC3 — MET, OBSERVED — `python tools/govkit/govkit.py selfcheck` exits 0 with `25 entr(y|ies) · 23 exemption(s) · 0 unclaimed`, and it REFUSED the two legs this build added until each carried a `subject-pins.tsv` row, which is the ratchet working rather than a claim about it.
- AC4 — MET at build time in `e55f933b` and `ea6d9f61`; all ten arms green, recorded in the latter.
- AC5 — MET, OBSERVED — the hold predicate `subject == kit || chunk == selftests` selects 52 of the 99 legs in `tools/gate-legs.json`, and none of them runs without `GATE_SELFTESTS`.
- AC6 — MET at build time in `ea6d9f61`; NOT re-observed. Removing a `project-owned` rule restores both the file and its leg to the payload, which is the failing case that commit records.
