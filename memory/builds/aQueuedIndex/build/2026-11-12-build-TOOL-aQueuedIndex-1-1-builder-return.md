# aQueuedIndex — unit 1's builder return

**Serves:** journal TOOL-aQueuedIndex-1

Runs wf_339d4207-44d and wf_7506dff8-e74, summarized from their returns.

- The first run built the whole pass over rev-1 and had its pass commit refused by hygiene check 12: fork F1 carried no
  resolution mark in its own span, which the main loop owed before any code. It restored every path and saved the pass as a
  patch. The spec's rev-2 marked F1 and folded the run's deviation 11, the plant's poll waiting for the lock to be held half a
  second in a row.
- The second run applied that patch, checked it against rev-2, and committed it as pass commit `dd195a2e1`. The index
  connection runs in autocommit; the tree build, overlay and collection write blocks each open with `BEGIN IMMEDIATE`; the
  tree build re-reads its built row under the lock and returns when another writer built it; the busy timeout is 600 s. A new
  `queued-writers` plant races two writers in a scratch repository of its own, and the tags help page says a writer queues.
- Probes it ran, none a gate: the new plant twice with both writers green and the waiter parsing no blob; the sibling plants over
  the autocommit connection; the timeout and help-page greps; the lexicon's offenders.
- Owed to the close: the gates its spec names, the new plant observed red over BASE's index module and green after, and the
  five races of the two checks on a fresh index in a scratch clone.
- One refusal site has no arm asserting its text: the plant's line for writer one never taking the write lock.
