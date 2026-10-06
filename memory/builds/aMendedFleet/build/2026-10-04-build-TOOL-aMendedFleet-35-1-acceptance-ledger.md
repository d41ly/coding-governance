# TOOL-aMendedFleet-35 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-35

**Evidences:** TOOL-aMendedFleet-35
- AC1 — `python tools/codebase-map/test_codebase_map.py` — exited 0 with no FAIL line after `gen_map.py --write`; the first run after adding the selftest arm reported `STALE symbols.json` on `test_generated_artifacts_are_fresh` and exited 1, which is the byte-compare reddening on an un-rendered artifact. `grep -c '"file": "skills/session-kickoff/manifest-check.sh"'` over `memory/map/generated/symbols.json` printed 22
- AC2 — `write_card` — `reuse_lookup.py "write the orientation card for a session"` listed `write_card [function | skills/session-kickoff/manifest-check.sh, tools/hooks/scratch-guard.test.sh | fan-in 0]`, and no candidate line names a `_`-prefixed symbol
- AC3 — `scan_shell_layer` — a `python -c` call importing `map_extractors` from the kit directory, over two scratchpad roots and without the `root` keyword: the root holding `broken.sh` with an unterminated quote raised `MapError` naming that file and `unterminated " quote opened at line 2`; the root holding only a `.txt` raised `kit-sh: no public shell definition under [...]`. Neither call returned a list
- AC4 — `RECALL_DARK_LAYERS` — `reuse_lookup.py "anything"` printed `unscanned layers: none — every present layer has an extractor` with no `RECALL_DARK_LAYERS` note on stderr; `grep -n '^RECALL_DARK_LAYERS=""' .codebase-map.conf` printed line 28
- AC5 — `git grep` — the six-needle `git grep -n -i -F` over the six files S5 names printed nothing and exited 1; at the parent it printed seven lines
- AC6 — `python tools/codebase-map/replay-phrases.py` — at the parent, run in this worktree before the first edit: 442 graded, hit rate 0.701, 118 that cannot hit, 16.9 s. With the layer: hit rate 0.842, 118 -> 31 that cannot hit, upper-median rank of first correct 3 -> 5, 24.1 s against its 60 s ceiling, exit 0

## The arm

`test_shell_layer_indexes_public_definitions_only` in `tools/codebase-map/selftest.py`, a fixture
root holding a public definition, a `_`-private one and a function inside a heredoc body, plus a
second root holding one untokenizable file. Run ALONE through a scratchpad script calling `check`:
`ok`. Staged red by removing the underscore filter in `map_extractors.py`: `FAIL`, the row list
carrying `_private_helper`; restored: `ok`. The suite itself did not run.

## Owed at the close

- `codebase-map kit selftest`, `codebase-map coverage + freshness`, `codebase-map adopter e2e`,
  `codebase-map gate coverage`, `lexicon naming predicates`, `lexicon selftest`, `straggler-guard
  arms`, `govkit acceptance matrix`, `recall floor`, `recall floor arms` and `spec tokens`.
- The lexicon and memory-tree kit version bumps owed by the `lexicon.py` docstring and the
  memory-tree README edit, per the brief; `kit epoch` is the close's.
