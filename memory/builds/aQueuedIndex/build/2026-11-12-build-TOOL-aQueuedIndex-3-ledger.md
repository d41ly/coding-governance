# TOOL-aQueuedIndex-3 — acceptance ledger

**Serves:** journal TOOL-aQueuedIndex-3

Each line is a probe the builder ran over the pass's working tree at rev-1 of the spec. Every plant run built its own
scratch repository under a short temp directory outside the repository, so it wrote no node index. No leg, suite or bar
ran in the pass. Where a line says "owed", the main loop observes it after every unit is terminal.

**Evidences:** TOOL-aQueuedIndex-3
- AC1 — `busy timeout 600 s` — `gov_tag.py --fixture --plant queued-writers` exited 0, printing that line after the writer-one line, and `both writers green` as its last line (PINNED, that plant run).
- AC2 — `busy timeout 60 s` — over a scratch copy of the playbook, lib and memory-tree kits in a fresh repository under a short temp directory, with the index module's timeout set to 60, the same plant printed that line, exited 1 and printed no green line. With the line set back to 600 it exited 0 and printed `both writers green` last (PINNED, those two plant runs). The `New arm:` line's RED-first observation at the close is still owed.

**Owed to the close.** Every leg of the spec's Gates section, and the `New arm:` line's RED-first observation for AC2.
