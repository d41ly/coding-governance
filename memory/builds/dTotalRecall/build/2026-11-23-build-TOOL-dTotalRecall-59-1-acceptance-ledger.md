# TOOL-dTotalRecall-59 — acceptance ledger, build pass 1

**Serves:** log TOOL-dTotalRecall-59
**Caused-by:** TOOL-dTotalRecall-59

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-4 over base
`206422580` and ran each probe below on node d, 2026-11-23: §4's probe from `tools/memory-tree/`, the two
greps of AC2, and §4's case built by hand in a scratch fixture repository under the system temp directory,
removed after it. §7's legs and the `New arm:` RED-first observation of the case `merged-home-gained` in
section `2o` of `tools/lib/resolve-python.test.sh` are owed to the close.

**Evidences:** TOOL-dTotalRecall-59
- AC1 — `check_new_at_base` — §4's probe printed `True (None, 'no memory/project/record-kinds-legacy.txt at 8b8b1374c4fc (merge-base of HEAD and origin/main)')`: the `new at` reading, and `compare_to_base` names no `gained` key (DERIVED 2026-11-23, this probe). This pass changes no file the probe reads.
- AC2 — `absorbs` — `git grep -n "absorbs" -- legacy_ledger.py` from `tools/lib/` and `git grep -n "absorbs" -- tools/govkit/registry.toml` from the root each printed nothing and exited 1 (DERIVED 2026-11-23, this probe).
- AC3 — `fx-merged (shrink-only): gained b.md<TAB>-<TAB>causes` — over a scratch fixture repository whose `main` holds `fx-merged`'s two-row home and the registration §4 states, fetched from a bare remote, `python tools/lib/legacy_ledger.py compare fx-merged` on the branch `feature` with `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` unset printed that line and exited 1 with `b.md - causes` planted; reset, it printed no `gained` and exited 0 (DERIVED 2026-11-23, this probe). The same commands are the case `merged-home-gained` in section `2o`, whose run and RED-first observation are the close's (`python resolver (behaviour + inline parity + idiom ban)`).
