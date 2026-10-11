# TOOL-aFrugalTurnstile-14 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-14

No merge bar, no suite and no run-gates.sh over this repo ran for this ledger. The TOOL-aFrugalTurnstile-4
fixture script was copied to a short temp root and changed: three legs, of which the unguarded `pu`
appends to tracked `m.txt` once, while a flag file outside the repo exists. Each side ran a FULL run
on a clean tree, restored `m.txt`, then ran `GATE_REUSE=lineage`, with `GATE_TURNSTILE=0` and a
scratch `GATE_TURNSTILE_DIR`. Against the runner at the previous commit `61cd7ee8` both criteria
were RED: every row carried `full` `1`, and the lineage run reused all three legs and stamped
`reused 3`. Against the edit both were GREEN. The close still owes the new arm block in
`tools/run-gates/run-gates.evidence.test.sh`, which was written and not run, and every §7 leg.

**Evidences:** TOOL-aFrugalTurnstile-14
- AC1 — `full` — at the edit the run's verdict was TREE MOVED and all three `gate-ledger.tsv` rows read `ok full=[]`; at `61cd7ee8` the same run wrote all three with `full=[1]`.
- AC2 — `GATE_REUSE=lineage` — at the edit the lineage run printed `GATE ok` for pa, pb and pu and no reuse line, and its `gate-full-green` reads `reused 0`, earned by running every leg; at `61cd7ee8` it printed three `GATE reuse` lines and stamped `reused 3`.
