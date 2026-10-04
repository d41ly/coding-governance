# TOOL-dUnstuckLanding-2 — acceptance ledger

**Serves:** journal TOOL-dUnstuckLanding-2

The design was authored inline against the census. Four tests ran against the tree before any pick:

- The witness-ancestry predicate was run over 30 ABORTED records, and read OFF on two known-unmerged
  stamps.
- `grep` counted the HELD readers and the phase-set readers.
- The classifier's rule 5 was read at `run-gates.sh:2403-2405`.
- The node's local bar records and `gh` were probed for the anchor's red set.

No gate leg was run in this pass beyond the memory hygiene check over the staged records.

**Evidences:** TOOL-dUnstuckLanding-2
- AC1 — `2026-10-04-build-TOOL-dUnstuckLanding-2-design.md` — each of sections 1 to 8 names
  candidates (a), (b) and, where there is one, (c). Each states the test that rejected each loser:
  - a reader count (§1);
  - the ancestry probe, and the non-deriving live index (§2);
  - the permanent-red instances, and the owner's pin history (§3);
  - the shared-counter MIXED case (§4);
  - the seven-kind table (§5);
  - the instances outside `in-place` (§6);
  - node b's five runs (§7);
  - 1.40's missing HELD (§8).

  The declined early-detection candidate records its test too: no local bar record and no `gh` for
  anchor `a587e82d`.
- AC2 — `## Failure classes` — each census class is joined to the design:
  - K1 is answered by §3 and §4.
  - K2 is answered by §5 and §6.
  - K3 is answered by §1 and §2.
  - K6 is answered by §7 and §8.
  - K4 and K5 are declined under "What this does not answer", each with its reason and its existing
    asks.
- AC3 — `--settle` — §1 and §2 name each verb's phase or fact:
  - `--handoff` writes `HELD` with `owner-landing` or `owner-decision`.
  - `--settle` writes `LANDED` with `landed-by: attended`, or the `work-landed-at` fact on an
    ABORTED record.

  Each verb's refusals are named, and the route for an existing ABORTED-but-landed record is
  `--settle`. No verb writes a terminal without evaluating it: `--settle` writes only what the
  ancestry derivation proves. `--landed`'s LANDING-only guard and the HELD refusals of
  `UNATTENDED-STOPS.md` §1 are left as they are.
- AC4 — `python tools/memory-tree/gen_build_index.py --asks --build dUnstuckLanding --all` — it read
  back all nine asks, `TOOL-dUnstuckLanding-3` to `-11`. Each was OPEN with a SEV of HIGH or MED, and
  the hygiene gate parsed each one's `KEEP` row with no verdict.
