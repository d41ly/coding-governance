# Acceptance ledger — the shared dispatch width

**Serves:** journal TOOL-aPairedSlots-3

Observed on node a on 2026-10-11. The turnstile suite's new arms 34 to 37 were sliced and run over the
changed runner: 7 assertions, PASS. Each criterion's break was then staged alone and its arm read RED.

**Evidences:** TOOL-aPairedSlots-3
- AC1 — `width 2 at dispatch — 2 of 2 bar slots held` — beside a slot-1 holder, at a profile width of
  4 and `GATE_TURNSTILE_SLOTS=2`, a fixture runner whose rule was `half` printed it and its header
  recorded width 2; one whose rule was `full` printed `width 4 at dispatch` and recorded 4. With the
  held-count read removed neither line printed and both headers read 4.
- AC2 — `GATE_JOBS=3` — the same bar under `half` recorded width 3; with the division applied to the
  operator's width too it recorded 1.
- AC3 — `at dispatch` — a bar holding the only held slot printed no such line and recorded the
  profile's width 4; with the threshold lowered to one held slot it printed the line.
- AC4 — `GATE_MEMINFO` — two concurrent bars reading one file at 95 % used under a 90 % threshold both
  wrote a non-empty `pauses` file; with the second bar pointed at a source of its own, it did not pause.
