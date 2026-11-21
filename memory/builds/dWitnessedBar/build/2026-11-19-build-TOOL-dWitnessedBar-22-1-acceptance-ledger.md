# TOOL-dWitnessedBar-22 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-22

This pass ran no merge bar, no self-test suite and no gate leg except the naming lexicon's
`--suggest`. Every criterion was checked on node d on 2026-11-19 with a probe of the unit's own
code: a `python -c` call, the three new `edge_grammar.py --fixture` plants, the plant rows run alone
through `run_plant_rows` cut out of `adopt-playbook.sh`, the key-set predicate and the gov canary's
G11 arm cut out of their files and run alone, and a scratch copy of the map under the run's scratch
directory. Still owed to the close: the RED-first observation for each of the three `New arm:` lines
in spec section 7, every leg that section names, and AC6's `govkit.py selfcheck` and `govkit
selftest`, which the role hook refuses in a pass.

**Evidences:** TOOL-dWitnessedBar-22
- AC1 — `tools/gate-legs.json` — a probe re-derived the claims from the dossiers under
  `memory/map/features/` through `map_lib.load_map_tree`: 180 legs (DERIVED) claimed once, none twice, 18
  unclaimed (DERIVED). After the pass 180 rows carry `tests` equal to `["feature.<f>"]` for the
  claiming dossier and 18 carry no `tests` key, `run-gates evidence` among them. The 70 descriptor
  `[[gate_leg]]` rows in the 27 descriptors were joined to the manifest by name: 0 disagree on
  `tests` or `enforces`; the 23 descriptors §4 names were edited and the other 4 were not.
- AC2 — `LEG_KEYS` — the key-set predicate, run with the file's own `LEG_KEYS` line over a fixture
  row carrying `tests` and `enforces`, exited 0; with `tests` cut from `LEG_KEYS` it exited 1. Over the
  real manifest it exited 0, and 1 with `tests` cut. Arm 1a gains the `tests` control pair (near-miss
  `test`) and the canary's floor goes 457 -> 458.
- AC3 — `read_leg_edges` — a `python -c` call over the `leg-resolved` plant's text returned two dicts,
  `{'path': 'gate-legs.json', 'line': 4, 'type': 'tests', 'targets': ['layer.memory'], 'site': 'leg',
  'source': 'leg.x.y'}` and the same for `enforces` with `['practice.land']`; line 4 is the row's
  `"tag"` line. `python tools/playbook/edge_grammar.py --fixture --plant leg-resolved` exited 0 and
  printed the `edges: resolved` line naming the fixture manifest's row 4 and `tests=layer.memory · layer.memory` and the same for
  `enforces=practice.land`. The same probe refused, one `EdgeRefusal` each, a text that is no JSON, a
  JSON object (deviation 221), a row carrying `tests` with no `tag`, a `tests` string, and a target
  holding a space.
- AC4 — `leg-unregistered` — `python tools/playbook/edge_grammar.py --fixture --plant
  leg-unregistered` exited 0 printing `edges: leg rows · 1 tests target(s) unarmed until their
  namespace is registered` and `edges: green · 1 edge(s)`, with no red line.
- AC5 — `tests` — the gov canary's G11 arm, cut out and run alone, was green over the real manifest.
  Over a copy with `pre-push self-test`'s `tests` emptied it was red, printing
  `map/features/push-main.md claims leg 'pre-push self-test', whose tests does not name
  feature.push-main`. Over a scratch copy of the map with `pre-push self-test` added to
  `lexicon.md`'s claims it was red, printing `map/features/lexicon.md claims leg 'pre-push self-test',
  whose tests does not name feature.lexicon`. A copy whose row names `feature.lexicon` printed
  `leg 'pre-push self-test' carries tests feature.lexicon, and map/features/lexicon.md does not claim
  it`, so both directions are read.
- AC6 — `govkit.py selfcheck` — not run: the role hook refuses it in a pass, so the close owes it. A
  probe of the join over the real tree found 0 disagreements on `tests` and `enforces` across the 70
  descriptor legs. 7h compares both keys presence included and the failure line names the entry, the
  leg and both lists. The selftest's new run g stages `tests = ["feature.drifted"]` and
  `enforces = ["principle.p16"]` on `pre-push self-test` and asserts both lines.
- AC7 — `leg-rule-member` — `python tools/playbook/edge_grammar.py --fixture --plant leg-rule-member`
  exited 0, printed the `edges: resolved` line naming the fixture manifest's row 4 and `enforces=practice.land · practice.land` and
  `edges: leg rows · 1 enforces target(s) unarmed, practice rules core meta-check grades`, and printed
  no line resolving or redding `practice.land.paths`. Over the real manifest, `read_leg_edges`,
  `check_edges` and `run_resolve` gave 231 edges, 0 reds, 53 targets resolved and 193 unarmed: 180
  `tests` and 13 rule-member `enforces` (DERIVED).
