# Acceptance ledger — the docs key

**Serves:** journal TOOL-aPairedSlots-4

Observed on node a on 2026-10-11. The turnstile suite's new arms 38 to 42 were sliced and run over
the changed runner: 9 assertions, PASS. Two breaks were then staged in copies of the changed runner,
each slice run with a 5 s TTL exported so a doc-only bar that queued failed open in 20 s rather than
waiting out the default bound: the docs branch never taken, and nesting blind to the docs beacons.

**Evidences:** TOOL-aPairedSlots-4
- AC1 — `gate queue: docs-only — admitted on the docs key, not queued` — printed by a doc-only bar
  that finished while a non-doc bar still held the only slot; it took no place in the queue and its
  header recorded `queued_from` `docs`. With the docs branch never taken it queued.
- AC2 — `gate-docs-beacon` — after a doc-only bar exited its own run-id directory was gone while a
  live doc-only neighbour's still stood; with the docs branch never taken neither directory existed.
- AC3 — `gate queue: nested under` — a runner started by a doc-only bar's leg printed it; with
  nesting blind to the docs beacons it did not nest.
- AC4 — `gate queue: waited 0s` — a non-doc bar beside a doc-only holder printed it and no dispatch
  line, and a full bar with `GATE_DOCS_BASE` set took a slot as a non-doc bar; with the docs branch
  never taken the doc-only holder held a slot, and the non-doc bar beside it waited or took a shared
  width.
- AC5 — `sweeping the docs beacon of a dead holder` — printed by the next doc-only bar over a planted
  dead docs beacon, which was gone afterwards; with the docs branch never taken it stood.
