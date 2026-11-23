# TOOL-dQuietDisk-1 leg-tail 28 — run-gates adopter e2e failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** run-gates adopter e2e
- **Hash:** 7a0f036cc8d9ea7b7ddf620accc50472d76c5658
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
govkit apply — [3/LAND] from 87fdd849 into C:/Users/d41ly/AppData/Local/Temp/gate-work.U2uJ4tRR/tmp/tmp.57FxOUVLnc/nogovkit
govkit apply — SKIPPED [project-owned] tools/run-gates/adopt-run-gates.test.sh <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/profile_bar.test.sh <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/run-gates.evidence.test.sh <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/run-gates.runlog.test.sh <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/run-gates.test.sh <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/run-gates.turnstile.test.sh <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/run-selftests.test.sh <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/run-gates.gov.test.sh <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/foreign-prefix.gov.test.sh <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/ceiling-evidence.txt <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/ceiling-margin.txt <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/bar-wall-evidence.txt <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/pass-leg-evidence.txt <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/selftest-budgets.txt <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/selftest-pooled-evidence.txt <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/windows-only-legs.txt <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/owed_rows.py <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/py_reads.py <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/fixtures/measure-legs/churn.py <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/fixtures/measure-legs/concurrent.json <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/fixtures/measure-legs/forks.sh <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/fixtures/measure-legs/hog.py <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/fixtures/measure-legs/memio.py <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/fixtures/measure-legs/orphan.sh <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/fixtures/measure-legs/printenv.py <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/fixtures/measure-legs/queued.sh <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/fixtures/measure-legs/serial.json <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/fixtures/measure-legs/spawn.py <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/fixtures/measure-legs/stall.json <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/fixtures/measure-legs/stall.sh <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/fixtures/measure-legs/steady.py <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/fixtures/measure-legs/turnstile.json <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — SKIPPED [project-owned] tools/run-gates/fixtures/measure-legs/waitmark.py <- run-gates: nothing in this install produces it — the target or its operator must supply it
govkit apply — landed 26 file(s), 60 row(s) in the receipt
govkit apply — [4/STAGE] 26 path(s)
govkit apply — [5/HOOKPROBE] no-hook
govkit apply — receipt written ahead of CONFIGURE: 60 row(s), 1 kit(s); RECEIPT rewrites it
govkit apply — CONFIGURE run-gates: adopter exit 0 — adopted
govkit apply — [7/OBSERVE] rendered destinations
govkit apply — observed 0 rendered destination(s)
govkit apply — [8/RENORMALIZE] 10 path(s) governed, 0 not LF in the index
govkit apply — [9/LEGS] manifest
govkit apply — gate legs: emitted 4 into tools/gate-legs.json
govkit apply — 1 leg(s) in your runner are kit SELF-TESTS and are HELD by default: they test the kit's own source, which does not change in a repo that copy-installs it. Run them once now to verify this install, and afterwards whenever you edit a kit:
govkit apply —   GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh
govkit apply — GATE_FULL=1 does NOT run them: it ignores every guard, and a kit's own tests are not a guard. A green bar without that variable says nothing about the kits themselves.
govkit apply — [10/AFTER] re-reading the target's runner
govkit apply — attestations: 1 kit(s) attested at 87fdd849
govkit apply — [11/RECEIPT] 60 row(s), 1 kit(s), schema 4
govkit: pin 'tools/gate-legs.json' (declared by run-gates) resolves to no tracked path in this target
govkit: leg 'product-test contract (tests.product)' did not exist before this install and is red after
govkit: 1 problem(s)
  ok   — AC1 regen --list names the factory row skipped, its when not holding
  ok   — AC1 regen --check exits 0 where no govkit sits
  ok   — AC2 the factory module imports with no govkit
  ok   — AC2 --write exits 2 naming the places it looked for govkit, with no traceback
  ok   — AC3 --conform exits 0 over the target's descriptors, naming fresh and enforces ungraded

FAIL (run-gates adopter e2e, 23 assertions)
```
