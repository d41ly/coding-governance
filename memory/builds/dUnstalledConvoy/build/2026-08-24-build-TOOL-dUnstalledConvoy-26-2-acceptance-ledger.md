# The acceptance ledger — the self-tests-on-demand units

**Serves:** journal TOOL-dUnstalledConvoy-26 TOOL-dUnstalledConvoy-27 TOOL-dUnstalledConvoy-28 TOOL-dUnstalledConvoy-29 TOOL-dUnstalledConvoy-30 TOOL-dUnstalledConvoy-31 TOOL-dUnstalledConvoy-32

Every line is OBSERVED or AMENDED. Where a criterion was answered by something other than what it
names, the line says so rather than implying it was answered as written.

**Evidences:** TOOL-dUnstalledConvoy-26
- AC1 — `tools/run-gates/run-gates.test.sh` case 3h2 — a kit-subject leg reports `GATE held` with the switch off AND under `GATE_FULL=1`; the second half is the one the unit rests on.
- AC2 — `tools/run-gates/run-gates.test.sh` case 3h2 — `GATE ok    a kit self-test` under `GATE_SELFTESTS=1`, with a second arm asserting nothing is held.
- AC3 — `tools/run-gates/run-gates.test.sh` case 3h2 — the held line is asserted NOT to carry `skip`'s `(unchanged vs …)` tail, and `ondemands` is its own counter.
- AC4 — AMENDED — `tools/run-gates/profile_bar.test.sh` arm 9, not `run-gates.test.sh` as written: the reader is `profile_bar.py` and its suite is where its arms live. Built at the CLOSING REVIEW, not in this unit's own passes — the verb was added to the runner and not to the reader, dropping 42 of 85 legs from every profile silently.
- AC5 — `tools/run-gates/run-gates.test.sh` case 3h2 — `selftests\t1` read back out of `.git/gate-full-green`. The first draft asserted against a file the fixture could not produce.
- AC6 — `.githooks/pre-push.test.sh` cases 19–23 — built as `TOOL-dUnstalledConvoy-27`, which this criterion anticipated and did not contain.
- AC7 — `tools/govkit/selftest.py` — the cross-check refuses a descriptor leg with no `subject`; the population is `read_descriptors`, both roots.
- AC8 — `tools/govkit/selftest.py` — refusal in both directions, and the exempt-leg path reads its own subject. That second half was UNBUILT until the closing review: an exempted leg is claimed by no descriptor, so every subject arm quantified over a population those rows are not in.
- AC9 — `tools/govkit/matrix.py` — a real `apply` into a real target, the emitted leg read back off that target's manifest carrying `subject = "kit"`, with a control that the target's own leg gains none. Built at close; the unit's own passes never wrote this arm.
- AC10 — `tools/run-gates/run-gates.test.sh` case 3h4 — an all-held manifest exits 2 and says it executed nothing. Built at close; before it, such a run printed `gates GREEN — 0/0 legs passed` and exited 0.
- AC11 — `tools/govkit/selftest.py` — the install summary states the held count, the invocation against the target's OWN runner command, and that `GATE_FULL=1` does not unlock them.
- AC12 — `2026-08-24-build-TOOL-dUnstalledConvoy-26-1-red-first.md` — per-arm, with the two that could not fail named as controls.
- AC13 — `bash tools/run-gates/run-gates.sh` under `GATE_FULL=1 GATE_SELFTESTS=1` — see the build's closing bar.

**Evidences:** TOOL-dUnstalledConvoy-27
- AC1 — `.githooks/pre-push.test.sh` — `rec_st` is read beside the three fields the hook already parsed.
- AC2 — `.githooks/pre-push.test.sh` case 19 — a switch-OFF record offered for a switch-ON push forces FULL.
- AC3 — `.githooks/pre-push.test.sh` case 22 — a switch-ON record satisfies a switch-OFF push. Coverage, not equality; this is the arm equality gets wrong.
- AC4 — `.githooks/pre-push.test.sh` case 21 — a record with no key at all forces, so absence reads as HELD.
- AC5 — `.githooks/pre-push.test.sh` case 20 — the decision line carries `kit self-tests … HELD`.
- AC6 — `2026-08-24-build-TOOL-dUnstalledConvoy-27-1-red-first.md` — three of five RED; the other two assert the boundary chooses SCOPED, which it did before this unit for every case, and the record says so.
- AC7 — `bash tools/run-gates/run-gates.sh` — see the build's closing bar.

**Evidences:** TOOL-dUnstalledConvoy-28
- AC1 — `bash tools/run-gates/run-gates.sh` — `.githooks/gate-env.sh` sets the switch and no kit claims that path; the hook sources it when present.
- AC2 — `tools/govkit/selftest.py` — a bare assignment inside `tools/demo/` (an `include = "**"` engine rule) reds, naming the file and the kit.
- AC3 — `2026-08-24-build-TOOL-dUnstalledConvoy-28-1-red-first.md` — `export GATE_SELFTESTS=1` appended to `.githooks/pre-push`, which is the exact configuration `-26` rev-2 prescribed, refused by name.
- AC4 — `grep` — line 207 is the only mention and it is a read, `[ -n "${GATE_SELFTESTS:-}" ]`. This was already true when the unit started.
- AC5 — `tools/govkit/selftest.py` — the same arm as `-26`'s AC11; the adopter's way to set it IS the install summary's invocation.
- AC6 — `bash tools/run-gates/run-gates.sh` — see the build's closing bar.

**Evidences:** TOOL-dUnstalledConvoy-29
- AC1 — `tools/govkit/selftest.py` — `gate leg 'demo' is subject 'kit' and pinned 'repo'`, with three further arms on what the message must say.
- AC2 — `tools/govkit/selftest.py` — after `selfcheck --write` the pin holds exactly `demo\tkit` and the planted stale row is gone.
- AC3 — `tools/govkit/selftest.py` — a second leg with no pin row reds.
- AC4 — AMENDED — regenerated from `tools/gate-legs.json`, not from the descriptors as §2 said. Section 7h already asserts the two agree in both directions, so the manifest pins every descriptor leg transitively AND covers the `[[exempt_leg]]` rows a descriptor-derived pin would miss. Spec rev-2 records it.
- AC5 — `grep` — `THIS FILE GRADES CHANGE, NOT CORRECTNESS` in the generated header, and the same statement in the source header and in every refusal.
- AC6 — `2026-08-24-build-TOOL-dUnstalledConvoy-29-1-red-first.md` — twelve of thirteen RED; the thirteenth is labelled `CONTROL` in the arm's own name.
- AC7 — `bash tools/run-gates/run-gates.sh` — see the build's closing bar.

**Evidences:** TOOL-dUnstalledConvoy-30
- AC1 — `grep` over `tools/gate-legs.json` — `pre-push self-test`, `branch-guard self-test`, `push-main self-test` and `run-gates gov canary` all carry `subject = "repo"`.
- AC2 — `bash tools/run-gates/run-gates.sh` — all four appear as `GATE ok` on the closing bar, which ran with the switch on; with it off they are equally unaffected, since the hold reads `subject` alone.
- AC3 — `grep` over `tools/run-gates/run-gates.sh` — the criterion sits at the `subject` field declaration, stated once, and govkit's no-subject refusal points at it rather than restating it.
- AC4 — `bash tools/run-gates/run-gates.sh` — see the build's closing bar.

**Evidences:** TOOL-dUnstalledConvoy-31
- AC1 — `tools/run-gates/run-gates.test.sh` case 3h3 — `gates GREEN — 2/2 legs passed` where five legs are declared and three held.
- AC2 — `tools/run-gates/run-gates.test.sh` case 3h3 — the note reads `(3 held: kit self-tests, GATE_SELFTESTS=1 runs them)`.
- AC3 — `tools/run-gates/run-gates.test.sh` case 3h3 — the verdict record carries `ran 2` and `held 3`, both read back off the file.
- AC4 — `tools/run-gates/run-gates.test.sh` case 3h3 — `gates GREEN — 5/5 legs passed` with the switch on, end-anchored so a stale note would fail it. A control: it passes without the fix.
- AC5 — `2026-08-24-build-TOOL-dUnstalledConvoy-31-1-red-first.md` — four of five RED, the fifth named as the control.
- AC6 — `bash tools/run-gates/run-gates.sh` — see the build's closing bar.

**Evidences:** TOOL-dUnstalledConvoy-32
- AC1 — `tools/run-gates/run-gates.test.sh` case 3h3 — `---- chunk held: skipped  (0 ran, 0 failed, 0 skipped, 0 reused, 2 held)`.
- AC2 — `tools/run-gates/run-gates.test.sh` case 3h3 — `---- chunk mixed: green  (2 ran, 0 failed, 0 skipped, 0 reused, 1 held)`; both lines end-anchored.
- AC3 — `2026-08-24-build-TOOL-dUnstalledConvoy-32-1-red-first.md` — both arms RED, neither a control.
- AC4 — `bash tools/run-gates/run-gates.sh` — see the build's closing bar.

**Evidences:** TOOL-dUnstalledConvoy-33
- AC1 — `tools/unattended/unattended.test.sh` — `LATE record — ARCH-tRun-2 entered the roster after this run went live`, plus the acceptance line beside it. Verified by hermetic probe, not by the suite; see the revision log for why.
- AC2 — `tools/unattended/unattended.test.sh` — a unit already in the baseline roster still draws a check 48 refusal, now naming the baseline rather than the current region.
- AC3 — `tools/unattended/unattended.test.sh` — with the run-state file never committed there is no baseline to derive and the add is refused.
- AC4 — AMENDED — the arm is in the driver's suite rather than the checker's; it greps all three files, so the assertion is the same one for no second harness. `baseline_units` is defined once, in `lib-unattended.sh`, and neither caller defines its own.
- AC5 — `bash tools/unattended/check-unattended.sh` — exit 0 over this build's own run-state file once the four late rows were written. Before them, five check-24 failures.
- AC6 — `2026-08-24-build-TOOL-dUnstalledConvoy-33-1-red-first.md` — six of eight RED; the two that are not are named there.
- AC7 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — see the build's closing bar. The kit's OWN suites named in §7 were not run, per the standing owner instruction; that gap is stated in the spec's revision log.
