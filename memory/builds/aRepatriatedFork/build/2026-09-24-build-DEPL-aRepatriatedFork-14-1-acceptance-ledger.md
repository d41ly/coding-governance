# DEPL-aRepatriatedFork-14 — acceptance ledger

**Serves:** journal DEPL-aRepatriatedFork-14

One unit pass under the mandate. It ran no merge bar and no self-test suite. The arms this unit adds
to `tools/govkit/selftest.py` were run on their own. `check_pytest_ini_probe` ran by importing the
suite and calling that one function over a scratch root under `%TEMP%`. The two `selfcheck` arms
ran as the suite stages them, in a scratch copy of gov. All held. The whole `selftest.py` suite was
not run, and the close owes it.

Every new arm was observed RED. `govkit selfcheck` over this tree, before any descriptor was
repaired, exited 1 with exactly three problems: `check-testsuite-counts` declaring neither, and each
process-monitor self-test leg naming its own withheld file. With a7c78ad2's root-only probe put back
in the pytest descriptor, the sub-directory arm and the no-configuration arm both redded. With `all`
changed to `any` in the new probe, the two-file arm redded.

The adopters were read-only. inCMS was observed in a `git clone --local --shared` of
`C:/projects/incms/main` at `bc7e95589`, under `%TEMP%/a14i`. NicoCares was observed in a clone of
its git directory, `C:/projects/incms/main/.git/modules/vendor/nicocares-package`, checked out at
`14b9fb7a`, under `%TEMP%/a14n`. The path `C:/projects/nicocares/main` would not clone, because its
`.git` file points at a relative git directory. Nothing was written in either real tree.

**Evidences:** DEPL-aRepatriatedFork-14
- AC1 — `pytest-ini-knobs` — at `%TEMP%/a14i`, `govkit check` prints no line naming the hole, and the kit prints `landed-unmeasured`. The fixture arm `[aRF-14 AC1]` discharges the hole from `services/api/pyproject.toml` beside a root file with no pytest table, and it reds under a7c78ad2's root-only probe
- AC2 — `govkit selftest` — `check_pytest_ini_probe` prints `hole 'pytest-ini-knobs' is UNDISCHARGED` for a sized and an unsized sibling, and for a tree with no pytest table. Run directly, the descriptor's probe exits non-zero with `no tracked pyproject.toml carries [tool.pytest.ini_options]` on stderr, which `check` does not print (spec rev-2)
- AC3 — `stale-header-waiver` — neither `govkit check` run names it. At `%TEMP%/a14i` the only remaining hole line is `measured-pins`, and `%TEMP%/a14n` reports no problem at all. In a clone of gov with `memory/project/stale-header-waiver.txt` deleted, `gen_build_index.py --check` exits 1 with `absent. The stale-header waiver registry is REQUIRED even when empty`. Hygiene check 9 runs that command
- AC4 — `govkit.py selfcheck` — exits 1 naming `entry 'check-testsuite-counts' declares neither` over this tree before S3, and over a gov copy whose `[check]` table is cut away. It exits 0 over this tree after S3, and prints `declared check: 27 entries, 0 silent`
- AC5 — `declares neither` — neither adopter's `govkit check` output carries the phrase
- AC6 — `govkit.py plan` — at `%TEMP%/a14i`, zero `SILENT` rows. With a7c78ad2's process-monitor descriptor put back, the same plan prints two, naming `scripts/process-monitor/selftest.py` and `scripts/process-monitor/adopt-process-monitor.test.sh`
- AC7 — `project-owned` — `selfcheck` exits 1 naming both process-monitor legs and their paths over this tree before S4. In a gov copy, a fixture leg `pm fixture leg` running `{kit}/selftest.py` is refused as `runs tools/process-monitor/selftest.py, which its own project-owned rule withholds`
- AC8 — `any kit-versions finding` — `grep -c` over `tools/govkit/entries/check-kit-versions.kit.toml` prints 1. `govkit check` at `%TEMP%/a14i` reports no `kit-versions-need-list` line. That clone is inCMS HEAD rather than an update branch, so the second half is observed against inCMS's own copy of the gate at that HEAD
