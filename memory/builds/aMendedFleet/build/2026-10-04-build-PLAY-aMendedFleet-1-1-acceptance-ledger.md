# PLAY-aMendedFleet-1 — acceptance ledger

**Serves:** journal PLAY-aMendedFleet-1

**Evidences:** PLAY-aMendedFleet-1
- AC1 — `awk '/^## The merge bar/,/^## Conventions/' AGENTS.md` — 668 bytes by `wc -c`, under the pinned 1100, and the section names `tools/gate-legs.json`, `.githooks/gate-env.sh` and `MERGE-BAR.md`
- AC2 — `grep -c -e "Measured on node" -e "^GATE_" -e "^bash tools/run-gates" AGENTS.md` — printed 0; `grep -rc "Measured on node" memory/guides` printed 0 for every one of the ten guides
- AC3 — `grep -rl -e "Guards scope a run" -e "Two protocols are BINDING" -e "Every leg's output is persisted" memory/guides AGENTS.md` — printed one path, `memory/guides/MERGE-BAR.md`
- AC4 — `grep -n -e "before you run, scope or debug a bar" -e "TOOL-aRepatriatedFork-5" -e "core.hooksPath" memory/guides AGENTS.md -r` — the first phrase hit the guide's line 3 and the wrapper's line 474; `TOOL-aRepatriatedFork-5` hit the guide only; `core.hooksPath` hit the guide twice and no line of `AGENTS.md`, plus one line of `memory/guides/UNATTENDED-PROTOCOL.md` that carries it at base and is not the merge-bar body
- AC5 — `bash tools/check-template-size.sh AGENTS.md` — after `--bump`, exit 0 at 56383 / 64512 bytes with no WARN line, 7961 below the pinned 64344; `grep -n "^AGENTS.md" tools/template-size-highwater.txt` printed the `AGENTS.md` row at 56383, moved from 60930
- AC6 — `python tools/codebase-map/test_codebase_map.py` — exit 0; `python tools/codebase-map/gen_map.py --check` exit 0; `grep -n "MERGE-BAR.md" memory/map/features/run-gates.md` hit line 35, the `guides` claim
- AC7 — `python tools/memory-tree/corpus_ids.py --check` — exit 0; its one check 16 rule 3 line names `memory/map/baseline.toml` in the untouched preamble, REPORTED and not gated, and present at base

## Owed at the close

The legs §7 names — `charter size`, `line length`, `playbook render wiring`, `agent-cap restatement`,
`codebase-map coverage + freshness`, the two recall legs, `memory hygiene`, `drift-audit records` and
`spec tokens` — were not run in this pass. Only the direct checks above were.
