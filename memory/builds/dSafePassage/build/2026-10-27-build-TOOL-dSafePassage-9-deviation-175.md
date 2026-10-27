# TOOL-dSafePassage-9 deviation 175 — the fixture module carries its own named helpers

**Serves:** deviation TOOL-dSafePassage-9

- **Departs from:** TOOL-dSafePassage-9@rev-5 [§4 Inventory]
- **Hand-off:** spec-to-code
- **Before:** the Inventory mints `run_fixture` and `main` in the fixture module and no other function there.
- **After:** `tools/govkit/fixtures/retired_edits.py` also defines `build_repo`, `build_scratch_gov`, `build_target`, `write_gov_files`, `write_commit`, `run_git`, `run_govkit`, `run_update`, `run_plant`, `run_dispatch_gap`, `resolve_kit_path`, `read_clean_env`, `read_verdict`, `read_role`, `read_orders`, `read_bytes` and `read_wired`, each passing `tools/lexicon/lexicon.py --suggest <name> --as py.function`; and the `edited-row` and `keep` plants clear the first run's order before the observed run, so an order seen after it is that run's.
- **Cause:** builder discovery
- **Reason:** twelve plants share one scratch gov, one install and one set of readers; written inside `run_fixture` alone they would be one function of several hundred lines, and without the cleared order the `--stub forked` run would still show the first run's order and could not show "no order".
- **Evidence:** this unit's acceptance ledger: every plant exits 0 and every stub exits 1 with its MISS lines, the `--stub forked` run reading `retired-edited orders: '0' · expects '1' · MISS`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-9, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** TOOL-dSafePassage-9
