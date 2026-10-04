# TOOL-dUnstuckLanding-18 — acceptance ledger

**Serves:** journal TOOL-dUnstuckLanding-18

No merge bar and no self-test suite ran in this pass. The new carry-forward block was run ALONE
behind a copy of the driver suite's own prologue and its ask stub, on a fixture repository under the
user temp directory: 48 of 48. It was then run again with four staged breaks at once — the edge
reader printing nothing, the `asks_filed_by` slug filter removed, condition 2 and condition 3 each
forced true — and each of the AC2, AC3 foreign-slug, AC4 and AC5 arms went red while the rest held.
The carrier criteria were observed by the greps and `cmp` calls they name. The whole suites, the
drift-audit and runlog self-tests among them, and the gate legs are owed to the close.

**Evidences:** TOOL-dUnstuckLanding-18
- AC1 — `carried forward` — the fixture's `--close` printed `carried forward — ARCH-tCarry-2,
  DEFERRED against the open ask EXMP-tCarry-5` and no `build-complete` unmet line, with one CLOSED
  unit, the DEFERRED unit in the BASE roster, its defer row, and its spec closing an OPEN ask filed
  under `tCarry`. An `external` consumes-from edge and a `hands-off` edge left it met.
- AC2 — `read_consumes_from` — a CLOSED spec declaring `**consumes-from**` onto the DEFERRED unit
  left `build-complete` unmet with `ARCH-tCarry-1 consumes-from ARCH-tCarry-2`. With the reader
  staged to print nothing, that arm went red and the close printed the carried line instead.
- AC3 — `asks_filed_by` — an empty BACKLOG.md, a stub row deriving the ask CLOSED, and an ask filed
  under `tOther` each left the term unmet naming `ARCH-tCarry-2`; a blank `ASKS_CMD` did too, naming
  the missing contract. With the slug filter staged out, the `tOther` arm went red.
- AC4 — `--rescope --act add` — with BASE holding unit 1 alone, unit 2 recorded as a LATE add and then
  deferred left the term unmet with `a DEFERRED unit was added during this run`. With condition 2
  staged true, that arm went red.
- AC5 — `build-complete` — with no defer row on the record the term was unmet, naming the row and the
  `--rescope tCarry --act defer --item ARCH-tCarry-2` that writes it. With condition 3 staged true,
  that arm went red.
- AC6 — `--successor` — `--act defer` exited 0 and wrote exactly one `rescope · item defer` row; with
  `--successor` it printed `UNATTENDED check 48 FAILED`. `PARK_ACTS_OWED` reads `retire supersede
  defer`. The leg's four-act pattern matched `retire|supersede|add|defer)` in the driver and graded all
  three owed acts live; the three-act pattern matched nothing.
- AC7 — `The close-decision table` — the heading grep printed 1, all seven kinds were found in §15,
  and `cmp` of the template against the render exited 0.
- AC8 — `never an abort` — the M3 slice grep printed 1, and the render measures 27645 of 30720 bytes.
- AC9 — `build-complete` — the §4 row names a unit carried forward under the stop contract's table;
  the render measures 65546 of the declared 65692 bytes after the rev-3 fold, and `cmp` exited 0.
- AC10 — `TOOL-dUnstuckLanding-23` — the driver grep prints the comment line above `build-complete`
  quoting the ruling, and `memory/DECISIONS.md` line 134 is the ruling row superseding D8.
- AC11 — `carried forward` — 6 lines in the Skill template and 6 in the regenerated Skill.
- AC12 — `last-audit:` — the manifest stamp moves in this commit, re-stamped at `f8afa61b`.
- AC13 — `PARK_ACTS_OWED` — the driver, `model.PARK_ACTS_OWED` and `_RUN_PARK_ACTS_OWED` all read
  `defer retire supersede`, the kinds and `PARK_KINDS` agree too, and runlog's leading ledger sources
  equal the driver's owed kinds plus `rescope-retire`, `rescope-supersede` and `rescope-defer`.
