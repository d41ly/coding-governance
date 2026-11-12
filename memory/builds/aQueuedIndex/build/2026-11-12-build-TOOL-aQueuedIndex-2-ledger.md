# TOOL-aQueuedIndex-2 — acceptance ledger

**Serves:** journal TOOL-aQueuedIndex-2

Each line is a probe the builder ran over the pass's working tree at rev-1 of the spec. The plant run built its own
scratch repository under a short temp directory outside the repository, so it wrote no node index. No leg, suite or bar
ran in the pass. Where a line says "owed", the main loop observes it after every unit is terminal.

**Evidences:** TOOL-aQueuedIndex-2
- AC1 — `writer two parsed 0, ran 0 and skipped 0` — `gov_tag.py --fixture --plant queued-writers` exited 0, printing `writer one parsed 1 blob(s); writer two parsed 0, ran 0 and skipped 0` (PINNED, that plant run). The staged break with the waiter's re-read deleted is the `New arm:` line's RED-first observation, owed.
- AC2 — `write blocks: 3 of 3 open with BEGIN IMMEDIATE` — the same run printed that line and no `does not open` line (PINNED, that plant run). The two staged breaks, the overlay's lock line and the collection's, are owed with the arm.
- AC3 — `both writers green` — the same run printed the phrase as its last line, after `incremental rows equal a cold build's` (PINNED, that plant run). Its absence over each staged break is owed with the arm.
- AC4 — `^queued-writers|0|both writers green|DIFFER$` — the spec's `grep -c` printed 1 (PINNED, the pass's diff).

**Owed to the close.** Every leg of the spec's Gates section, and the `New arm:` line's RED-first observation over the three staged breaks for AC1, AC2 and AC3.

**Main-loop observations at the close.** The `queued-writers` row over pass commit a03bb6339 in a scratch clone, one staged
break at a time, each restored before the next (DERIVED at a03bb6339, the scratchpad log aq-arm2.log).

- AC1 — `skipped` — with the waiter's re-read under the lock deleted, the plant exited 1 printing writer two skipped at 7: the
  rebuild the parsed count could not see is now red.
- AC2 — `does not open with BEGIN IMMEDIATE` — with each of the tree-build, overlay and collection blocks' lock deleted in turn,
  the plant exited 1 naming that block's line.
- AC3 — `both writers green` — no break printed it; restored, the plant exited 0 with it as the last line.
