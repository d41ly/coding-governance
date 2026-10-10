# DEPL-aBenchedProbe-2 — acceptance ledger

**Serves:** journal DEPL-aBenchedProbe-2

No merge bar and no self-test suite ran in this pass. AC1 to AC5 were observed through the slice the
spec's section 6 names, which imports `tools/govkit/selftest.py` and runs `check_ceiling_emission`
alone against a fixture under the default `%TEMP%`: it printed 13 `ok` lines and an empty `FAILURES`
list in 37 s. Each new arm was observed RED first on a staged break of `tools/govkit/govkit.py`,
restored by copying a backup back and confirmed byte-identical with `cmp`. With the S3 line that sets
the row's ceiling replaced by `pass`, CE1 and CE5 printed FAIL. With the floor constant at `(1, 1)`,
both CE2 floor arms printed FAIL. With the keep rule's `!=` inverted to `==`, CE4's keep and report
arms and CE5 printed FAIL. With the writer's floor spelled `SUBJECT_FLOOR_RUN_GATES`, the CE2 source
predicate read False. AC6 is the new 7h clause, observed with `govkit selfcheck` on two staged breaks
of the descriptor and once on the restored tree. The close still owes the section 7 legs:
`govkit selftest` whole, where `check_ceiling_emission` now runs from `main()` beside D4, plus
`govkit refusal join`, `govkit acceptance matrix`, `recall floor arms`,
`codebase-map coverage + freshness` and `lexicon naming predicates`.

**Evidences:** DEPL-aBenchedProbe-2
- AC1 — `"ceiling": 1780` — after the slice applied `push-main` into the fixture, the
  `pre-push self-test` manifest row carried `"ceiling": 1780` and the receipt's `emitted` row carried
  ceiling 1780; `FAILURES` printed `[]`. With the S3 line absent from `write_gate_legs`, CE1 printed FAIL
  and the row read with no `ceiling` key.
- AC2 — `floor=govkit.CEILING_FLOOR_RUN_GATES` — `check_target_reads_subject` answered False for a
  fixture runner at `KIT_RUN_GATES_VERSION=1.1` and True at 1.2, the constant read `(1, 2)`, and the
  `govkit.py` source carries `floor=CEILING_FLOOR_RUN_GATES)`. At `(1, 1)` the 1.1 arm and the
  constant arm printed FAIL; with `SUBJECT_FLOOR_RUN_GATES` in the writer the source arm read False.
- AC3 — `push-main self-test` — that row and the `pre-push bar self-test` row carried no `ceiling`
  key in the same fixture manifest, and CE3 printed ok for both.
- AC4 — `kept the target's ceiling` — with the row raised to 3600 and committed, the re-apply of
  `push-main` exited 0, the `pre-push self-test` row still read 3600, stdout carried the
  `kept the target's ceiling` line naming the leg, and no `differs from what the receipt recorded`
  line printed. With the keep rule inverted, the row read 1780 and CE4 printed FAIL.
- AC5 — `emitted` — with the row and the receipt's `emitted` ceiling both set to 1000 and
  committed, the apply passed the receipt preamble with no rewind helper and the row read 1780. With
  the keep rule inverted it stayed 1000 and CE5 printed FAIL.
- AC6 — `python tools/govkit/govkit.py selfcheck` — with the `push-main` descriptor's
  `pre-push self-test` ceiling at 1781 it exited 1, printing that entry `push-main` declares the leg
  with ceiling 1781 while the manifest says 1780; at `true` it exited 1 with the same refusal naming
  `True` and 1780. Restored, it exited 0 and no output line contained "ceiling".
- AC7 — `grep -n "1.2" tools/run-gates/README.md` — line 382, in the `ceiling` section, says the
  deployer carries a kit leg's `ceiling` into your manifest at run-gates 1.2 or later.
