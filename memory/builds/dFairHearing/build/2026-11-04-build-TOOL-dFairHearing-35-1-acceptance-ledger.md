# Acceptance ledger — TOOL-dFairHearing-35

**Serves:** journal TOOL-dFairHearing-35

Built against spec rev-5 at pass commit `a4fbcbf33`, whose parent is `a7df5b4b4`. The main loop drafted
this ledger at the close from the builder return and the `## Scoring` section that commit adds to unit
30's record. `attempts.py` is the spec's checker, written under the pass's scratch directory. No suite,
gate or bar ran in the pass. The spec's one `New arm:` line applies only if `ungated` wins, and
`selected` held, so it is owed no observation. The spec's legs are owed to the close.

**Evidences:** TOOL-dFairHearing-35
- AC1 — `attempts.py` — over unit 30's record at the commit it exited 0 and printed 8 `scored` lines, which the `## Scoring` section quotes, with record 2 `selected` scored at f2s2 because f2s1 is void. Each of the manifest's eight `candidates` entries names the report of the clone its `scored` line names
- AC2 — `attempts.py` — nine scratch tables under `probe_ac2.py` each gave the output the criterion names: `scored 4 selected 3` with `unscored 4 selected 4`; `void after cap 4 selected` and exit 3; attempt 2 listed twice, exit 1; failed then completed, `scored 4 selected 2`; failed, failed, completed, `void after cap 4 selected` and exit 3; a `Completed` row, an empty last cell and a `Selected` row, each exit 1 naming line 10; and a row of a second table, not read
- AC3 — `replay_scorer.py --experiment` — the checker having exited 0, it printed `arm ungated: varies checklist from selected`, `parsed selected: 4 of 4` and `parsed ungated: 4 of 4` before any figure. The record names `selected` at 6/22, 2/10, 6/10 and 12/17, `ungated` at 10/22, 0/10, 2/10 and 13/17, `paired 4 of 4`, the pooled 26/59 and 25/59, the decision that `selected` holds, and the `ungated` class set as per-record counts and a checklist sha256. The exit 3 branch has an empty population and is not counted as coverage
- AC4 — `tools/memory-tree/gotchas.py` — its diff and the harness template's against the parent printed nothing, and the record states `selected`. The `ungated` and exit 3 branches have an empty population and are not counted as coverage
- AC5 — `test -e` — it passed for all 8 manifest reports and all 24 quoted transcript files. Nothing was removed, f2s1's report included
