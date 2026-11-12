# TOOL-aQueuedIndex-1 — acceptance ledger

**Serves:** journal TOOL-aQueuedIndex-1

Each line is a probe this unit's builders ran over the pass's working tree, the first at rev-1 of the spec and the second at rev-2, which changed only the plant's poll wording and F1's mark. The plant runs built their own
scratch repositories under a short temp directory outside the repository, so none wrote the node's index. No leg,
suite or bar ran in the pass. Where a line says "owed", the main loop observes it after every unit is terminal.

**Evidences:** TOOL-aQueuedIndex-1
- AC1 — `both writers green` — `gov_tag.py --fixture --plant queued-writers` exited 0 three times in a row, each printing `writer one parsed 1 blob(s), writer two parsed 0; both writers green` and `incremental rows equal a cold build's`, in about 8 s a run, and twice more over the patch re-applied at rev-2 with the same lines (PINNED, those plant runs). Its red over BASE's `tag_index.py` is the `New arm:` line's RED-first observation, owed. Deviation 11 records the poll's half-second hold, folded into the spec's Design at rev-2.
- AC2 — `writer two parsed 0` — the same three runs printed writer one's count at 1 and writer two's at 0 (PINNED, those plant runs). The staged break with the re-read removed is owed with the arm.
- AC3 — `database is locked` — owed: the five races of the two checks in a scratch clone of the pass commit are the main loop's, per the brief.
- AC4 — `BUSY_TIMEOUT = 600` — the spec's grep printed one line, `117:BUSY_TIMEOUT = 600`, and the file holds one assignment of the name (PINNED, the pass's diff).
- AC5 — `queues behind` — `grep -c` over `help/tags.md` printed 1, on the sentence naming the 600 seconds and the reuse of a tree built while waiting (PINNED, the pass's diff).

**Sibling plants over autocommit.** `held-open`, `schema`, `tagless`, `dirty` and `two-versions` each exited 0 over the pass's code, the schema reset's explicit transaction and the plants' own `with con:` blocks included (PINNED, those plant runs).

**Owed to the close.** Every leg of the spec's Gates section, the `New arm:` line's RED-first observation for AC1 and AC2, and AC3's five races.

**Main-loop observations at the close.** Run over pass commit dd195a2e1 in a scratch clone under a short temp directory, its
own index fresh before each race (DERIVED at dd195a2e1, the scratchpad logs aq-ac3.log and tq-arm-*.log).

- AC3 — `database is locked` — five races of the tags check against the instruction-edits check each exited 0 on both
  writers, the slowest writer at 130 s and the rest between 105 s and 110 s, and no log line carried the lock refusal.
- AC1 — `both writers green` — the `queued-writers` row over BASE's index module exited 1 with writer two refused on the lock
  refusal, and exited 0 once the pass's module was restored: the arm's RED-first half holds.
- AC2 — `writer two parsed 0` — with the re-read under the lock deleted, the plant still exited 0 and still printed writer two at
  0: the blob-parse cache counts a rebuild's blobs as skipped, so this arm cannot go red. The closing review's round 1 confirmed
  the same defect as B1; TOOL-aQueuedIndex-2 owns the fix.
