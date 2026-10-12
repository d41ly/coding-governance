# Build brief — TOOL-aBriskPreflight-12: the closing review's mediums and lows, batched

**Serves:** research TOOL-aBriskPreflight-12

Build the unit its spec, `spec/2026-10-12-spec-TOOL-aBriskPreflight-12.md`, describes: the seven
sub-items promoted from the closing diff review
(`reviews/2026-10-12-review-TOOL-aBriskPreflight-1-2-3-4-5-6-7-10-diff-review-round1.md`, M1, M2 and
L1 to L5). TOOL-aBriskPreflight-11 is parked on an owner fork and is NOT built; nothing here touches
the ceilings instrument or the three ceiling constants. This run sequences its passes one at a time.

## How to work in this tree — each line is a lesson a previous pass paid for

- **M1 first and verify it**: every record under `memory/builds/aBriskPreflight/build/` must carry a
  `**Serves:**` line in its first 12 unfenced lines (comment-marked in `.sh`/`.py`/`.log`), and units
  4 and 7 need `**Evidences:**` acceptance ledgers in unit 6's shape: one `**Evidences:** <id>` line
  immediately above that unit's `- AC1 — …` lines, no heading between, each line carrying a
  backticked observation token, never wrapped across a line. Run the FULL
  `bash tools/memory-tree/check-memory-hygiene.sh` (not `--staged`: checks 21 and 23 are held there)
  once at the end and read every failure; it costs minutes on this host — run it in the background.
- **Declare before you write**, with `--dispatch`: every product, test and record path, plus
  `memory/builds/aBriskPreflight/README.md`, `memory/LIVE.md`, `memory/ledger/2026-10.md`,
  `memory/map/generated/symbols.json` and `memory/backlog/TOOL.md`. Stage them AND `RUN.md`.
- If the spec must change, rev it first in its own `Pass: none` commit (spec 4's lines on RB_TOOK's
  premise are revved as part of M2, per this spec).
- Lexicon `--suggest` before naming; `gen_map.py --write` after any new or renamed function;
  `sh_hygiene.scan_file` over every edited shell file before committing.
- No suite, no bar: each new arm verified through a SLICE run alone (temporary script inside the
  owning kit dir, deleted before `gen_map.py --write`), observed RED on its staged break first.
- Do not bump any kit version marker. Never kill a process you did not start.
