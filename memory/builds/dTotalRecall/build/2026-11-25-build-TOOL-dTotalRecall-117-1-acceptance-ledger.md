# TOOL-dTotalRecall-117 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-117
**Caused-by:** TOOL-dTotalRecall-117

No merge bar, no self-test suite and no gate leg in this pass. The builder built spec rev-1 over base
`ce1c2095e3a8b35078d8754a6059366ff762a040`, 2026-11-25 local, in one commit. The plant ran over the working tree's
`build_records.py`. §7's legs and the `New arm:` RED-first observation of
`tools/memory-tree/check-memory-hygiene.test.sh`'s `door-header` literal are owed to the close.

With the old key put back in a scratch copy of the tools, the plant failed its unit, title, cause, edge, no-edge, build
and typed cases, each printing `exists`, and passed every other (DERIVED 2026-11-25, that copy).

**Evidences:** TOOL-dTotalRecall-117
- AC1 — `python build_records.py --fixture --plant door-header` — printed `PASS door-header — 20 cases`, the replay `exists` at exit 0, unit, title, cause, edge and no edge at exit 2, build and typed at exit 0 with a fresh `wrote`, each case but the replay asserting no `exists` (DERIVED 2026-11-25, that run).
- AC2 — `write_new_record` — a second call with another title raised `ValueError` naming `already holds the record`, and the first record's bytes stood; a CRLF copy of it still replayed `exists` (DERIVED 2026-11-25, the probe over a scratch seed).
- AC3 — `**Caused-by:**` — given a second time by hand, the first call replayed was refused as `already holds the record`, its key `unread`, and never `exists` (DERIVED 2026-11-25, the same probe).
- AC4 — `grep -c 'two builds hold a' tools/memory-tree/gov_record.py` — printed 0 (DERIVED 2026-11-25).
- AC5 — `python tools/memory-tree/gotchas.py --check` — named no finding of the new file, its advisory alone printed (DERIVED 2026-11-25); the relations half reads the commit, so the builder runs it after the commit and returns it.
- AC6 — `grep -oE 'PASS door-header — [0-9]+ cases' tools/memory-tree/check-memory-hygiene.test.sh` — printed 20, the plant's count; `FLOOR_ASSERTIONS` stands, no assertion added, and the `shell-role` row's 3750 stands, the one edited line a literal (DERIVED 2026-11-25).
