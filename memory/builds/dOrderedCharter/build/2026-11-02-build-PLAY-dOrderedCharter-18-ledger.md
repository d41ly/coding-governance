# PLAY-dOrderedCharter-18 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-18

Each line is a probe this pass ran, in the worktree or in a scratch clone under `%TEMP%`, and what it
printed. AC1 and AC3 are recorded at `PLAY-dOrderedCharter-49`'s pass, which corrects them (§3 Edges,
`PLAY-dOrderedCharter-55`): read as written, AC1's grep also matches the `repo_root` and `resolve`
of `codebase-map`, `drift-audit`, `govkit` and `policy`, and AC3's query matches
`tools/codebase-map/scen-adversarial.json:180` and the history comment at
`tools/govkit/selftest.py:12028`, all kept readers. AC10 runs `check-kit-versions.sh`, a gate leg, so
the main loop observes it at the close.

**Evidences:** PLAY-dOrderedCharter-18
- AC1 — `git grep -nE "^(def (grammar_for|anchor_at|repo_root|resolve|corpus_inputs|extract_records|extract_supersessions|derive_supersession_map|build_index|match_expr|terms)\b|class (Grammar|Conf)\b|ALIAS_WEIGHT =)" -- tools` — run by the main loop at the close, 2026-11-08: every name prints under `tools/memory-tree/id_grammar.py` and none under `tools/memory-recall/`
- AC2 — `Decided:` — the first query of §4 after the pass prints `check-hook-destinations.test.sh`, `check-kit-versions.sh`, `govkit.py`, `govkit/selftest.py`, the two recorded data files and the runlog hits, each a keep or out row, and `manifest-check.test.sh:889,1446,1448`, the F1 arm §7's `New arm:` line keeps hiding the recall kit's extractor; the pass commit's `Decided:` trailer names each
- AC4 — `cmp` — `extract.py . <out> --rev ce13efbe` in a clone at 98995aa27 and again after the pass wrote identical `spine.jsonl`, `records.jsonl`, `chunks.jsonl`, `anchors.json` and `orphan-ids.txt` (3117 records, 76985 chunks); the query printed `40 hits for: where does the id grammar live` and exited 0
- AC5 — `corpus_ids.py --print-defined-ids` — in a clone with `tools/memory-recall/` deleted it exited 0 and printed the `# id-ere:` line and 3857 ids; `gotchas.py --for-paths tools/memory-tree/` exited 0 with 53 lines and none naming memory-recall; at ce13efbe with the kit deleted the first exited 3, `no id set — the id grammar lives in the memory-recall kit`
- AC6 — `${_kit}id_grammar.py` — in a scratch clone a committed `NODE_TAG_CLASS` change in `id_grammar.py` with the constant unmoved made `check-verdict-epoch.sh <base>` exit 1 printing `moved: tools/memory-tree/id_grammar.py`; with it deleted from DELEGATES it exited 2, `id_grammar.py is imported by tools/memory-tree/row_grammar.py and is not in DELEGATES`; with neither plant it exited 0, `clean`
- AC7 — `id_grammar.py` — `g.resolve().digest()` read `5cb5a183795e`, `212d67b19c85` with a comment line appended to the file, and `5cb5a183795e` again restored; `git grep -nE "recall_conf|KIT_MEMORY_RECALL_VERSION" -- tools/memory-tree/` printed nothing
- AC8 — `scan_foreign_anchors` — sourced out of `check-unattended.sh` in a clone with `RECALL_CLI=""` and no recall kit at all, it returned 0 with `ASK_ANCHORS` naming the planted line, `memory/builds/zProbe/notes.md`, line 3, `TOOL-aOther-7`; the same call at ce13efbe returned 1, `RECALL_CLI is blank in this project`
- AC9 — `grep -c 'kit = "memory-recall"' tools/memory-tree/kit.toml` — printed `0`
- AC10 — `KIT_MEMORY_RECALL_VERSION` — main loop, 2026-11-08, in a scratch worktree: `bash tools/check-kit-versions.sh` exited 0, then with the constant alone changed exited 1 printing `memory-recall README marker != KIT_MEMORY_RECALL_VERSION`
