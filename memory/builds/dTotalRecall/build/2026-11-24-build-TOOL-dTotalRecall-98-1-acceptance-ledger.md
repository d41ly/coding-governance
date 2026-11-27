# TOOL-dTotalRecall-98 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-98
**Caused-by:** TOOL-dTotalRecall-98

No merge bar, no self-test suite and no gate leg in this pass. The builder built spec rev-2 over base
`a39546f8dd82c068d4690e178a16012b2c2e26ae` on node a, 2026-11-24. The pass edits no code, restores no record and writes
no deviation record. §7's legs are the close's. The listings, the fixture and the run over the build are §4's fences and
the probe is spec 93 rev-2 §4's, each extracted verbatim into a file under the scratch directory; the fixture ran as
`bash <file>` and the rest were sourced from the repository root. The fixture repository was made under the system temp
directory and removed after the run.

The fixture's blocks over git 2.56.1.windows.1, the second commit being `af9d7c5afb5c09c626e5c2bb6d92588d912c53d9` and every path standing
under the fixture's build folder (DERIVED 2026-11-24, that run):

| Block | Printed (DERIVED 2026-11-24) |
|---|---|
| `corrected` | the second commit, then x-deviation-1.md |
| `unit 92` | nothing |
| `held` | `refused` x-deviation-1.md, the second commit, `held y-deviation-1.md`; an empty status |
| `restored` | `restored` x-deviation-1.md and x-deviation-7.md, `refused` x-deviation-8.md `moved-since`; the status `A` for the first and `M` for the second, both staged |
| `again` | nothing |

The run over the build at the base, from the repository root (DERIVED 2026-11-24, that run):

| Read | Printed (DERIVED 2026-11-24) |
|---|---|
| `deleted_records 462d20f3..HEAD` | nothing |
| the liveness, `--diff-filter=A` | 151 |
| `write_restores 462d20f3..HEAD` | nothing, the tree unchanged |
| unit 92's spelling | nothing |
| the range with `--full-history --diff-merges=separate` | nothing |
| the liveness from `tools/` | 0 |
| the liveness over `462d20f3..67ffd1289` | 150 |

The liveness moved by the one record unit 92's pass added, `deviation-1014` of unit 87, so the pin and the read agree
(DERIVED 2026-11-24, these commands). No restore was refused, so nothing is handed to `TOOL-dTotalRecall-100`.

**Evidences:** TOOL-dTotalRecall-98
- AC1 — `deleted_records HEAD~2..HEAD` — printed the fixture's second commit and x-deviation-1.md under its build folder, and unit 92's spelling over the same range printed nothing; all five blocks printed what §4 pins, the first table above (DERIVED 2026-11-24, that run).
- AC2 — `deleted_records 462d20f3..HEAD` — printed nothing: the listing is empty, beside a liveness of 151, so no path is absent, none was restored and none refused. `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-98" -- memory/builds/dTotalRecall/build` printed this ledger's block line alone once it was written. `has_deviation memory/builds/dTotalRecall/build 92 'audit-89 id 15 s4'` printed 0, as no path was restored or refused; with no token it printed 1 for unit 92 and 2 for unit 87, so the zero is no unmovable probe (DERIVED 2026-11-24, these commands).
