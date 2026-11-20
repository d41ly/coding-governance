# TOOL-dWitnessedBar-40 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-40

This pass ran no merge bar, no gate leg and no suite. Every criterion below was checked on node d on
2026-11-20 by probing the unit's own code: the runner over a scratch clone under `%TEMP%/p40` with
the fixture manifest `fx/legs.json` named by `GATE_LEGS`, driven from a probe script; the hook's
`check_green_reuse` and `check_tree_reuse` extracted alone and called over six key pairs; and the
driver's conditional `env` argv run alone under `set -u`. The close owes every leg of section 7 and
the RED-first observation of both `New arm:` lines: the evidence suite's AC1-AC3 arms and the
pre-push suite's AC4 cases.

**Evidences:** TOOL-dWitnessedBar-40
- AC1 — `no gate-verdict written — docs mode` — a scoped run with `GATE_DOCS_BASE=HEAD` left
  `.git/gate-verdict/` absent and printed `run-gates: no gate-verdict written — docs mode`; the same
  run with `GATE_DOCS_BASE` unset wrote `<tree>.scoped` and printed its path. Owed: the evidence arm's
  RED-first observation with the DOCS_BASE guard removed.
- AC2 — `GATE_BASE_FROM=inherited` — the scoped run with `GATE_BASE_FROM=inherited` wrote no
  `.scoped` record and printed `run-gates: no gate-verdict written — scoped on an inherited green`; its
  leg printed `0` for `env | grep -c '^GATE_BASE_FROM='`. With `GATE_BASE_FROM=bogus` the run read
  `full` and wrote the `.scoped` record. The driver's argv carried `GATE_BASE_FROM=inherited` for a
  `-` full base and nothing for a sha. Owed: the evidence arms' RED-first observation.
- AC3 — `reused_cache` — a full run over the fixture manifest wrote a per-tree record whose
  `reused`/`reused_cache` lines read `reused:0 reused_cache:0`. Owed: the evidence arm's RED-first
  observation.
- AC4 — `reused 1` — `check_tree_reuse` forced on a record with neither key, naming the pair
  (`carries neither reused nor reused_cache`), on `reused 1` with no `reused_cache`, and on
  `reused 1`/`reused_cache 1`; it
  adopted `0`/`0`, `2`/`0` and an empty `reused` beside `reused_cache 0`. Not observed here: the hook
  run end to end over a scratch clone printing its `not covered` line, owed to the pre-push suite's
  `keyless` and `reused` cases and their RED-first observation at the close.
