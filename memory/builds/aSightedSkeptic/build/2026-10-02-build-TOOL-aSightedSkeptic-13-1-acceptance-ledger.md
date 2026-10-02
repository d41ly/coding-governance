# TOOL-aSightedSkeptic-13 — acceptance ledger

**Serves:** journal TOOL-aSightedSkeptic-13

Check 7 and check 23 of the unattended kit gate share one predicate, `check_derived_landed`, and check
23 now excludes a LANDING record whose landing commit is on the advertised default-branch tip. The
arm observations below are the unit pass's own, on a slice of the suite's prologue plus the new
block plus check 7's derived-LANDED arm, each break staged in the leg and the leg restored
byte-identical (commit 0ff84646 records them). The grep, version and manifest readings were re-taken
by the main loop at the unit's commit. The full suite and the gate leg itself run at the close.

**Evidences:** TOOL-aSightedSkeptic-13
- AC1 — `check 23 EXCLUDED` — arm A printed it naming the fixture record and its landing commit, with
  no `check 23 FAILED`; against the parent leg the arm failed: no EXCLUDED line and check 23 FAILED.
- AC2 — `check 23 FAILED` — arm B printed FAILED and no EXCLUDED; with `check_adv_reaches` removed
  from the predicate it failed, EXCLUDED appearing and no FAILED.
- AC3 — `check 23 exclusion UNAVAILABLE` — arm C counted 1 UNAVAILABLE line beside check 23 FAILED;
  the parent leg printed 0 UNAVAILABLE lines, and treating return 2 as excluded printed no FAILED.
- AC4 — `UNATTENDED check 23 FAILED` — arm D printed none of the three; with only check 23's
  `LANDED|ABORTED` skip deleted it printed FAILED.
- AC5 — `check_derived_landed` — the grep printed 4, the `c7anchor` grep printed nothing, and check
  7's existing arm passed with its unchanged text; staging the predicate to always return 1 redded it.
- AC6 — `bash tools/unattended/check-arms-groups.sh` — exit 1 with the same 17 findings it prints over
  the parent's suite, none naming a group inside the new block.
- AC7 — `UNDECLARED_WRITE_CEILING=` — `--emit-ceiling` printed 45 before the edit (129 passes graded,
  1946 s) and 0 after it (10 passes graded, 358 s); `.unattended.conf` line 342 holds 0.
- AC8 — `check 23` — the header grep over lines 1 to 45 printed 2.
- AC9 — `bash tools/check-kit-versions.sh` — exit 0, `govkit.py epoch` exit 0, `unattended.sh` line
  48 holds 1.56, and the 1.55 marker grep over tools, .claude and memory/guides printed nothing.
- AC10 — `bash skills/session-kickoff/manifest-check.sh` — exit 0 at the unit's commit.
