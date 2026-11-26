# TOOL-aPrunedIndex-24 — acceptance ledger

**Serves:** journal TOOL-aPrunedIndex-24

No merge bar, no self-test suite and no gate leg ran in this pass. Every reading is node a's, 2026-11-26,
from base `fa7051c3a` at spec rev-2, by `python tools/playbook/gov_tag.py --fixture --plant held-key`, by
one probe script under the run's scratch that puts `tools/playbook` on `sys.path`, imports `gov_tag` and
calls `gov_tag.main(["--fixture", "--plant", "held-key"])`, and by one `python -c` call loading the parent's
`tag_bundle.py` and `gov_tag.py`, each written to the scratch by `git show fa7051c3a:<path>`.

**Evidences:** TOOL-aPrunedIndex-24
- AC1 — the plant exited 0 and printed the four lines of section 4 byte for byte, the keys line `[True, False, True, False, False, False, True, True, False, False, False]; held`, the spawns line `a failing read: 2 reads, 2 spawns; a held read: 2 reads, 1 spawn, one answer; readers put back; held`, the flags line `flags read: --full-tree --name-only -r -z; held`, and last `held keys as listed, failures asked again, every flag read`.
- AC2 — unbroken, `main` returned 0 with no `FAILED` line. Under each break it returned 1 with `FAILED` on one line only: the guard removed on `keys:`, a failed read stored on `a failing read:`, `HELD_ID_RE` taking `HEAD` on `keys:`, `"--"` added to `HELD_FLAGS` on `flags read:`, and `"-z"` taken out of it on `flags read:`.
- AC3 — `sorted(gov_tag.HELD_FLAGS)` printed `['--full-tree', '--name-only', '-r', '-z']` and AC1's keys line held S2's vector. `grep -n -B2 '^HELD_FLAGS' tools/playbook/gov_tag.py` printed line 444, `#: S1: the one full object id a held read names, alone or naming its tree, and every flag it may carry before its paths`.
- AC4 — the probe printed the parent's 14 `SELFTEST_ROWS` lines as a prefix of the built 15, the one added line `held-key|0|held keys as listed, failures asked again, every flag read`, `True` for the `HELD_PLANTS` set, and `defs same: True`. At the close, `git diff --name-only 2f8d3b837^ 2f8d3b837` named `tools/playbook/gov_tag.py`, `tools/playbook/tag_bundle.py`, `memory/LIVE.md`, the build README, this ledger and spec 24, and none of the six cut-line files (PINNED, 2026-11-26)
- AC5 — the main loop, at `2f8d3b837`: the 20-spawn `git --version` gauge read 0.131 s, then `python tools/playbook/tag_bundle.py --selftest` exited 0 with `PASS — the tag plants, 15 rows` in 98.3 s, under the 159 s budget row (PINNED, 2026-11-26)

- seen-red — `tags bundle selftest` — red `2f8d3b837` — green `2f8d3b837` — the `held-key` plant under five breaks patched in memory: the `.git` guard removed, a failed read stored and replayed, `HELD_ID_RE` accepting `HEAD`, `"--"` back in `HELD_FLAGS`, `"-z"` removed. Each exits 1 with `FAILED` on its own line only: keys, spawns, keys, flags, flags. The plant exits 0 before the breaks and after them (PINNED, 2026-11-26)