# TOOL-dUnstuckLanding-16 — acceptance ledger

**Serves:** journal TOOL-dUnstuckLanding-16

No merge bar and no self-test suite ran in this pass. Each new arm was run ALONE behind a copy of its
suite's own prologue, on fixture repositories under the user temp directory, and then run again
against the HEAD copy of the file it grades. The runner arms went red on four assertions against the
HEAD runner. The hook arms went red on ten against the HEAD hook. The driver arms went red on
twenty-three against the HEAD driver. The two LIVE arms went red under two staged breaks of the
generator, one per filter. The whole suites and the gate legs are owed to the close.

**Evidences:** TOOL-dUnstuckLanding-16
- AC1 — `gate-inherited-green` — a twelve-landing fixture whose leg is red since landing 1, run under
  `land` with a bound of 2: the attr line reads `aged at R~2`, and the stamp names R, `max_age` 2 and
  the leg. The same leg under a bound of 10 is stamped too, which flips the old AC17 arm.
- AC2 — `GATE_INHERITED_RED_MAX_AGE` — the same fixture with no bound wrote the stamp with an empty
  `max_age`. The moved-text fixture, one leg aged, one unproven and one numeric, wrote a stamp naming
  all three. A second leg reading OWN wrote no stamp.
- AC3 — `.githooks/pre-push` — with R's file declaring only `INHERITED_RED_MAX_AGE=2`, an aged
  inherited red printed `inherited-red policy at <R8> reads land`, naming the kit default, then the
  `landing under INHERITED_RED=land` line, and the push landed. The runner was handed land and 2.
  `park` and `lnad` at R each read park and blocked, while the pushed tree's own copy said `land`.
- AC4 — `BLOCKER` — `--close` with `INHERITED_RED` undeclared, a bound of 2 and one aged leg: the
  policy line read the kit default land, the item was MET, and the record gained `gates-inherited`.
  The ask was filed SEV BLOCKER with the `older than the 2-landing age bound` text and read back
  through `ASKS_CMD`. Nothing outside `memory/builds/tRun/` was staged.
- AC5 — `HIGH` — an age of 1 under the bound of 2, and an unproven age, were each MET with the ask
  filed HIGH and no `older than` text.
- AC6 — `already OPEN` — under a declared `park`, the second close over the same aged leg at the
  same R printed `already OPEN … · reused`. It staged no BACKLOG row, and the file holds one BLOCKER.
  An ask read back HIGH was not reused. Run under `park` because a MET close moves the run to
  LANDING and cannot be repeated; the SEV follows the age under either policy. A second leg reading
  OWN or MIXED was UNMET with its attribution line, no MET line and no hold line.
- AC7 — `## Open BLOCKER asks` — `python tools/memory-tree/gen_build_index.py --selftest` passed both
  new arms. An OPEN BLOCKER ask rendered the heading and a line naming its id, home and leg. A tree
  whose OPEN asks are all HIGH, beside a CLOSED ask carrying BLOCKER, rendered no heading.
- AC8 — `bash tools/unattended/adopt-unattended.sh --check` — it printed `in sync` and exited 0 after
  the re-render. `grep -n "kit default" tools/unattended/STOPS.template.md` finds §13 naming `land`,
  and no line calls `park` the default.
- AC9 — `grep -c "TOOL-dUnstuckLanding-22" memory/DECISIONS.md` — it printed 1, and that row
  supersedes part of `TOOL-dDerivedDocket-24` by id. This unit wrote no second row.
- AC10 — `.githooks/gate-env.sh` — rev-2, by the driver suite's policy block run alone on a
  throwaway repo: a blank `GATE_POLICY_FILE` beside a hook file declaring park read park from it and
  printed the hold line, where the code before the fold read land and was MET; the conf absent at R,
  the key blank, and a named file absent at R each read land naming that branch and were MET. The
  hook suite's new arm, whose R carries no `.githooks/gate-env.sh`, read land naming the absence and
  landed; it was RED against a hook copy whose absent branch read park.
