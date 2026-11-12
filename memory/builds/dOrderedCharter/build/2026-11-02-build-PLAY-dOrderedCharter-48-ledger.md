# PLAY-dOrderedCharter-48 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-48

Each line is a probe this pass ran at rev-4 of the spec: `positional.py producers` from the repository
root, a `python -c` over `positional.read_producers` and the kept list, `gov_tag.py --fixture --plant`
building its scratch repository, or `positional.py check` from the repository root. The `tags positional
selftest` leg, the `tags (the resolver's checks)` leg, the gates the spec's section 7 names, the merge bar
and the `New arm:` line's RED-first observation are the main loop's at the close: a role agent runs none
of them. This record cites no code line, so the arm reads nothing new in it; a hit is written here as its
file and its line number.

**Evidences:** PLAY-dOrderedCharter-48
- AC1 — before any re-point, `positional.py producers` printed 15 hits, among them `tools/roles/agents/gov-spec-writer.agent.md:30` and `tools/workflows/orient-counterfactual.js` line 111, and no line of `tools/workflows/tier2-review.js`: its four hits (lines 665, 1213, 1400, 1596) printed once each under `tools/workflows/tier2-review.template.js`. The figure is DERIVED: 15 here, down from the spec's 41 at `8aafb0314` because unit 26 S6 re-pointed its sources' lines since
- AC2 — after the re-points `positional.py producers` prints 12 hits; a `python -c` filtering them to hits not on `positional-producers.txt` prints `hits 12 not kept 0 all name a stable form: True`, and `git grep -n -i "path and line" -- tools/roles/agents/gov-spec-writer.agent.md` prints nothing (rc=1). Re-pointed: the spec writer's role line 30 (and its render), the orientation counterfactual line 111, and the spec-audit lens's evidence directive in `tier2-review.template.js` line 1213 (and its render), which still told a lens to cite `read: <path>:<line>`
- AC3 — `positional.py producers --seed` wrote 12 rows (`positional: producers seeded 12 rows`, rc=0); the second run printed `positional: producers seed refused · tools/playbook/positional-producers.txt already holds 12 rows`, rc=1. `positional.py check` then printed `tags: positional · producers · 12 hits, 12 kept rows, 0 unlisted, 0 stale` and `tags: positional · green · 0 red`
- AC4 — `gov_tag.py --fixture --plant positional-producer-new` exits 1: `tags: positional · producer · tools/roles/agents/gov-x.agent.md:3 · - cite it by file:line · re-point it ...`, `tags: RED · 1 red`, then `re-pointed to a stable form: rc=0`; under `--set tags.positional=report` the same hit prints as `report · producer` and the run exits 0. `--plant positional-producer-stale` exits 0 with `tags: positional · producer stale · tools/roles/agents/gov-x.agent.md · - cite it by file:line · no hit carries the row` and `kept: rc=0; a second seed: rc=1; the kept line re-pointed: rc=1`. Each of the four new `SELFTEST_ROWS` lines matches those runs' exits and output. OWED to the main loop: the arm's RED-first observation in the `tags positional selftest` leg, staged by deleting the limb
