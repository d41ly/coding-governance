# TOOL-aRepatriatedFork-19 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-19

Written by the unit pass. The new arms were run as a SLICE of `tools/check-wiring.test.sh` (the
prologue plus the unit's own block, in a temp script inside the kit dir), once over the new checker
and once with a7c78ad2's checker swapped in, then restored and byte-compared. No suite ran: the whole
check-wiring self-test is owed by the close. The inCMS observation used a `git clone --local --shared`
of `C:/projects/incms/main` at `bc7e95589` under `%TEMP%`, removed afterwards; nothing was written to
inCMS itself.

**Evidences:** TOOL-aRepatriatedFork-19
- AC1 — `merge=rows` — with the driver and launcher flat under `scripts/` and only a receipt row naming them, the merge line is not a skip and `--fix` wires `bash scripts/merge-rows.sh %O %A %B %P`; a7c78ad2 printed `skip merge — memory-tree merge driver not adopted (no merge-rows.py)`
- AC2 — `.claude/hooks/` — the scratch guard receipted into `.claude/hooks/` and the recall kit receipted at `scripts/recall/` both read `ok`; a7c78ad2 printed `skip` for both, `hooks kit does not ship` and `memory-recall kit not adopted`
- AC3 — `bash tools/check-wiring.sh --check` — run in gov's own worktree, the output is byte-identical to a7c78ad2's checker run in the same tree, eol line included
- AC4 — `merge` — with the receipted driver deleted, the merge line is a `skip` naming `install.json row for memory-tree/merge-rows.py names scripts/merge-rows.py, which is absent`; a7c78ad2 printed the generic not-adopted skip
- AC5 — `.claude/workflows/` — a pinned `.claude/workflows/harness.js` holding CR bytes is named by a `note eol` line, and a pinned `.claude/hooks/other.js` with the same bytes is not; a7c78ad2 printed `ok eol` over it
- AC6 — `grep -c '^# >>> resolve_python' tools/check-wiring.test.sh` — prints `1`; the git grep's only hit is that block's own marker line, which spells the canonical copy's path and is byte-gated, and both inline blocks compare identical to their canonical copies
- AC7 — `bash tools/check-kit-versions.sh` — exits 0 with `KIT_CHECK_WIRING_VERSION=1.8`; the backlog half is owed to the main loop's records commit, because unattended check 49 refused `memory/backlog/TOOL.md` in this unit's write set (spec rev-3, S6)
- AC8 — `check-wiring.sh --check` — gov's checker in the inCMS clone, after both card fragments were merged and `--fix` set `merge.rows.driver`, prints `ok` for scratch, recall, card and merge and exits 0
