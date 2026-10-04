# TOOL-dUnstuckLanding-12 — acceptance ledger

**Serves:** journal TOOL-dUnstuckLanding-12

Every line each HIGH item cites was re-read at BASE `0c16a66b` before its edit, and each one held as
the review stated. The edits are in the design record, the census, unit 1's ledger and
`BACKLOG.md`. The gotcha catalogue gained one class. No gate leg was run in this pass beyond the
memory hygiene check and `gotchas.py`.

**Evidences:** TOOL-dUnstuckLanding-12
- AC1 — `## 2.` — the design's section 2 states that the probe is structural for an ABORTED record
  read from the tip, citing `unattended.sh:4746-4749`. It names the content predicate's three
  clauses and its numbered refusal. No sentence in the design or the census still says that ancestry
  separates landed from not-landed: `grep -n "separates landed"` over the design and the census
  finds nothing.
- AC2 — `BACKLOG.md` — the rows for asks 4 and 5 each name the witness-equals-base fixture, the
  foreign-tree-witness fixture and the merged-then-reverted fixture, all reading not-landed. Neither
  row names a LANDING stamp or a free-standing sha.
- AC3 — `BACKLOG.md` — ask 6's row files the BLOCKER in "the CLOSING build's backlog". It names
  `run-gates.sh`'s `ATTR_LANDABLE` predicate, and its accept includes "a pre-push over that tree
  lands it". No introducing build appears.
- AC4 — `read_landing_commit` — section 2's owes name STOPS §1, STOPS §8, PROTOCOL §3's "two ends"
  sentence, `lib-unattended.sh` `read_landing_commit`, and `--preflight`'s order, with the line
  references `:5080-5081`, `:5141-5142` and `:5127`.
- AC5 — `python tools/memory-tree/gotchas.py --check` — it exited 0 after `--write` regenerated
  `memory/gotchas/INDEX.md`. The index lists `liveness-negative-from-another-population` with 2
  anchors.
