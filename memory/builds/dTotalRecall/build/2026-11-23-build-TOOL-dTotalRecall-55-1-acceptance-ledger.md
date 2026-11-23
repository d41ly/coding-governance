# TOOL-dTotalRecall-55 — acceptance ledger, build pass 1

**Serves:** log TOOL-dTotalRecall-55
**Caused-by:** TOOL-dTotalRecall-55

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-5 over base
`b9f735339` and ran each probe below on node d, 2026-11-23, from `tools/memory-tree/` unless named: the
census and the check over the working tree, the grep from the root, and the plant's fixture, which
`record_causes.py#run_fixture` builds under the system temp directory and removes. §7's legs and the
`New arm:` RED-first observation of the plant `kept-row-drained` in `tools/memory-tree/check-memory-hygiene.test.sh`
are owed to the close.

**Evidences:** TOOL-dTotalRecall-55
- AC1 — `CAUSE_WRITER_KEPT` — `python record_causes.py --cause-writers` exited 0 and listed the eight files of §1 each as `kept` with its `tree_lib.py#CENSUS_KEPT_PATHS` row's reason (`pinned instrument` for `asbuilt.py` and `packet.py`, `outside the write set` for the six others) and `deviations.py` as `pinned CAUSE_WRITER_PINNED`, its build-folder count line `9 census file(s) · 8 kept · 1 pinned · 0 red`, its build-folder lines identical to the base's (DERIVED 2026-11-23, this probe); `python record_causes.py --check` exited 0, `record causes: green` (DERIVED 2026-11-23, this probe); `git grep -n "CAUSE_WRITER_KEPT\|KEPT_PINNED\|KEPT_OUTSIDE" -- tools` printed nothing and exited 1 (DERIVED 2026-11-23, this probe).
- AC2 — `kept-row-drained` — `python record_causes.py --fixture --plant kept-row-drained` exited 1 with exactly one `RED` line, `cause-writer CENSUS_KEPT_PATHS memory/builds/fRoot/build/2026-01-01-build-TOOL-fRoot-1-kept.py: spells no Serves line past its binding window, so the row keeps nothing; drain the row` (DERIVED 2026-11-23, this probe). With `tree_lib.read_kept_rows` replaced by an empty reader in a `python -c` probe, S4's drain read nothing and the plant exited 0 with no `RED` line, the staged break the `New arm:` names (DERIVED 2026-11-23, this probe). The arm's run in `check-memory-hygiene.test.sh` and its RED-first observation are the close's (`memory hygiene`).
