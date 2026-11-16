# TOOL-dDeclaredLoop-71 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-71

No merge bar and no self-test suite ran in this pass, and it wrote no product file, as rev-4 §8 F3 (a)
resolves. The criteria were observed on node `d` (win32), at rev-4 of the spec, over the working tree at
`432668bb0`, which holds the leg `TOOL-dDeclaredLoop-19` landed (`bcdcf0c79`) and the plants
`TOOL-dDeclaredLoop-53` (`dca74c239`) and `TOOL-dDeclaredLoop-64` (`ade343442`) added to `PLANTS`: the
probes section 6 spells, standing in for the `loop breakpoint fixtures` leg itself, which the close runs.
AC1's probe was observed live on an in-memory copy of the manifest whose row was given a `guard`, which
printed `True` for it; AC3's on a copy of `PLANTS` without `pre-placement-records-root`, which printed
that plant; AC4 staged its failed plant in memory, never in the tree, and the tree stayed clean.

Owed to the close: every leg section 7 names. Owed RED-first: none, the spec mints no arm; the leg's own
red is `TOOL-dDeclaredLoop-19`'s `New arm:`.

**Evidences:** TOOL-dDeclaredLoop-71
- AC1 — `1 ['python', '{prefix}/loop/breakpoints.py', '--selftest'] selftests False` — `json.load` over `tools/gate-legs.json`, keeping the rows named `loop breakpoint fixtures`, printed it: one row, chunk `selftests`, carrying no `guard` key.
- AC2 — `[] 1` — `tomllib` over `tools/loop/kit.toml` and `tools/govkit/registry.toml` printed `[] 1`: no `gate_leg` table of that name in the descriptor and one `[[exempt_leg]]` row; `grep -c "loop breakpoint fixtures"` printed 1 for each of `tools/govkit/subject-pins.tsv`, `tools/run-gates/selftest-budgets.txt` and `memory/map/features/loop.md`.
- AC3 — `[]` — the set of `pre-placement`, `driver-pre-placement` and `pre-placement-records-root` less `breakpoints.PLANTS` printed `[]`: each is a case of the leg.
- AC4 — `breakpoints: selftest · FAIL · 1 case(s) · 1 failed: pre-placement-records-root` — with `PLANTS` staged to that one plant and `run_breakpoint_plant` stubbed to print `MISSED staged` and return 1, `main(['--selftest'])` exited 1 and printed that last line (PINNED 2026-11-16, node d, the staged population).
