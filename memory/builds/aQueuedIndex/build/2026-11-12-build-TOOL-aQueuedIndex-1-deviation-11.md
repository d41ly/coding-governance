# TOOL-aQueuedIndex-1 deviation 11 — the plant waits for a write lock held half a second, not the first one seen

**Serves:** deviation TOOL-aQueuedIndex-1

- **Departs from:** `TOOL-aQueuedIndex-1@rev-1` [Design]
- **Hand-off:** spec-to-code
- **Before:** step 5 of the `queued-writers` plant reads the first `database is locked` from its raw poll as writer one inside its write block.
- **After:** the poll reads writer one as inside its write block once every poll has seen the lock held for 0.5 s in a row; the 0.05 s poll, its 30 s bound and the `writer one never took the write lock` line are unchanged (PINNED, the spec at rev-1).
- **Cause:** builder discovery
- **Reason:** writer one's `load_index` writes `PRAGMA user_version` on every open, a write the spec's own Non-goals name, so the first lock the poll sees can be that write, held for milliseconds before writer one has reached its build. Writer two would then race writer one to the build's lock and could build the tree itself, failing the plant on a coin flip. The tree build holds the lock for the staged 3 s parse, so a 0.5 s hold still leaves writer two most of it, and at BASE writer one's open waits on writer two's held view, so the red path of section 6 is kept. The spec writer folded this into Design step 5 at rev-2, so the departure is closed in the spec and no fold is open (PINNED, the spec at rev-2).
- **Evidence:** over the pass's code, `gov_tag.py --fixture --plant queued-writers` exited 0 three times in a row, each printing `writer one parsed 1 blob(s), writer two parsed 0; both writers green` and `incremental rows equal a cold build's` (PINNED, those plant runs in this pass).
- **Risk:** stricter
- **Approver:** spec writer, the rev-2 line of the spec's revision log, under the chain's `author-recorded` value
- **Follow-through:** ask TOOL-aQueuedIndex-1
- **Caused-by:** TOOL-aQueuedIndex-1
